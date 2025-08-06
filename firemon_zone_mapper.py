#!/usr/bin/python
"""
FireMon Zone Mapping Script
Maps firewall zones (from interface zoneDisplays) to FireMon compliance zones
Designed to run on FireMon appliances

Key Features:
- Excludes cloud device interfaces (AWS, Azure, etc.)
- Uses the last zone name when interfaces have multiple zones
- Maps zones to compliance zones with optional auto-creation
- Can rename network segments to include zone names (rename-only mode)

Usage:
  Interactive mode: python firemon_zone_mapper.py
  CLI mode: python firemon_zone_mapper.py --host localhost --username admin --auto-create
  Rename only: python firemon_zone_mapper.py --host localhost --username admin --rename-only

Environment Variables:
  FIREMON_HOST: FireMon server hostname/IP (default: localhost)
  FIREMON_USERNAME: FireMon username
  FIREMON_PASSWORD: FireMon password  
  FIREMON_DOMAIN_ID: Domain ID (default: 1)
"""

import sys
import os
import importlib.util

def ensure_module(module_name):
    """Dynamically import a module by searching for it in potential site-packages locations"""
    # First try the normal import in case it's already in the path
    try:
        return __import__(module_name)
    except ImportError:
        pass
    
    # Get the current Python version
    py_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    
    # Create a list of potential paths to check
    base_path = '/usr/lib/firemon/devpackfw/lib'
    potential_paths = [
        # Current Python version
        f"{base_path}/python{py_version}/site-packages",
        # Exact Python version with patch
        f"{base_path}/python{sys.version.split()[0]}/site-packages",
        # Try a range of nearby versions (for future-proofing)
        *[f"{base_path}/python3.{i}/site-packages" for i in range(8, 20)]
    ]
    
    # Try each path
    for path in potential_paths:
        if os.path.exists(path):
            if path not in sys.path:
                sys.path.append(path)
            try:
                return __import__(module_name)
            except ImportError:
                continue
    
    # If we get here, we couldn't find the module
    raise ImportError(f"Could not find module {module_name} in any potential site-packages location")

# Import required modules
requests = ensure_module("requests")
json = ensure_module("json")
urllib3 = ensure_module("urllib3")
getpass = ensure_module("getpass")
time = ensure_module("time")
argparse = ensure_module("argparse")
logging = ensure_module("logging")

# Import collections normally as it's a standard library module
from collections import defaultdict

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class FireMonZoneMapper:
    def __init__(self, base_url: str, username: str, password: str, domain_id: int = 1):
        """
        Initialize the FireMon Zone Mapper
        
        Args:
            base_url: FireMon base URL (e.g., https://localhost)
            username: FireMon username
            password: FireMon password
            domain_id: Domain ID (default: 1)
        """
        self.base_url = base_url.rstrip('/')
        self.domain_id = domain_id
        self.session = requests.Session()
        self.session.headers = {'Content-Type': 'application/json'}
        self.session.verify = False  # For internal FireMon use
        
        # Authenticate
        self._authenticate(username, password)

    def _authenticate(self, username: str, password: str):
        """Authenticate with FireMon"""
        logon_data = {
            'username': username,
            'password': password
        }
        
        # Validate credentials
        verify_auth = self.session.post(
            f'{self.base_url}/securitymanager/api/authentication/validate', 
            data=json.dumps(logon_data), 
            verify=False
        )
        
        if verify_auth.status_code != 200:
            logger.error("Authentication failed. Please check your username and/or password.")
            sys.exit(1)
        
        auth_status = verify_auth.json().get('authStatus', '')
        if auth_status != 'AUTHORIZED':
            logger.error("Authorization failed. Please check your credentials.")
            sys.exit(1)
        
        # Get token for subsequent requests
        login_response = self.session.post(
            f'{self.base_url}/securitymanager/api/authentication/login',
            data=json.dumps(logon_data),
            verify=False
        )
        
        if login_response.status_code == 200:
            token = login_response.json().get('token')
            if token:
                self.session.headers['Authorization'] = f'Bearer {token}'
                logger.info("Authenticated successfully.")
            else:
                logger.error("No token received during authentication.")
                sys.exit(1)
        else:
            logger.error("Failed to obtain authentication token.")
            sys.exit(1)

    def get_compliance_zones(self) -> list:
        """Fetch all compliance zones"""
        url = f"{self.base_url}/securitymanager/api/domain/{self.domain_id}/zone.json"
        params = {
            'page': 0,
            'pageSize': 1000,
            'sort': 'name'
        }
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            logger.info(f"Retrieved {data['total']} compliance zones")
            return data['results']
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching compliance zones: {e}")
            raise

    def get_interfaces(self) -> list:
        """Fetch all interfaces with their zone displays"""
        all_interfaces = []
        cloud_interfaces = 0
        page = 0
        page_size = 100
        
        while True:
            url = f"{self.base_url}/securitymanager/api/siql/interface/paged-search"
            params = {
                'q': f'domain{{id={self.domain_id}}}',
                'page': page,
                'pageSize': page_size,
                'sort': 'displayName'
            }
            
            try:
                response = self.session.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                
                # Count cloud interfaces for reporting
                for interface in data['results']:
                    if interface.get('deviceType') == 'CLOUD':
                        cloud_interfaces += 1
                
                all_interfaces.extend(data['results'])
                
                if len(all_interfaces) >= data['total']:
                    break
                    
                page += 1
                
            except requests.exceptions.RequestException as e:
                logger.error(f"Error fetching interfaces: {e}")
                raise
        
        logger.info(f"Retrieved {len(all_interfaces)} interfaces total ({cloud_interfaces} cloud interfaces will be excluded)")
        return all_interfaces

    def get_network_segments(self) -> list:
        """Fetch all network segments"""
        all_segments = []
        page = 0
        page_size = 100
        
        while True:
            url = f"{self.base_url}/securitymanager/api/domain/{self.domain_id}/networksegment/filter"
            params = {
                'page': page,
                'pageSize': page_size,
                'sort': 'name'
            }
            
            try:
                response = self.session.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                all_segments.extend(data['results'])
                
                if len(all_segments) >= data['total']:
                    break
                    
                page += 1
                
            except requests.exceptions.RequestException as e:
                logger.error(f"Error fetching network segments: {e}")
                raise
        
        logger.info(f"Retrieved {len(all_segments)} network segments")
        return all_segments

    def extract_firewall_zones(self, interfaces: list) -> set:
        """Extract unique firewall zones from interfaces"""
        firewall_zones = set()
        cloud_zones_skipped = set()
        
        for interface in interfaces:
            # Skip cloud devices
            if interface.get('deviceType') == 'CLOUD':
                if 'zoneDisplays' in interface and interface['zoneDisplays']:
                    cloud_zones_skipped.update(interface['zoneDisplays'])
                    logger.debug(f"Skipping cloud device interface: {interface.get('name')} on {interface.get('deviceName')} with zones: {interface['zoneDisplays']}")
                continue
                
            # Only process interfaces with zoneDisplays
            if 'zoneDisplays' in interface and interface['zoneDisplays']:
                # Use the last zone in the list if multiple zones exist
                zone_name = interface['zoneDisplays'][-1]
                firewall_zones.add(zone_name)
                
                if len(interface['zoneDisplays']) > 1:
                    logger.debug(f"Interface {interface.get('name')} has multiple zones {interface['zoneDisplays']}, using last one: {zone_name}")
        
        logger.info(f"Found {len(firewall_zones)} unique firewall zones (excluding cloud devices)")
        if cloud_zones_skipped:
            logger.info(f"Skipped {len(cloud_zones_skipped)} zones from cloud devices: {sorted(cloud_zones_skipped)[:10]}{'...' if len(cloud_zones_skipped) > 10 else ''}")
        
        return firewall_zones

    def create_compliance_zone(self, name: str, description: str = "", color: str = "#B8BEBF") -> dict:
        """Create a new compliance zone"""
        url = f"{self.base_url}/securitymanager/api/domain/{self.domain_id}/zone"
        
        payload = {
            "name": name,
            "description": description,
            "hexColor": color
        }
        
        try:
            response = self.session.post(url, data=json.dumps(payload))
            response.raise_for_status()
            zone = response.json()
            logger.info(f"Created compliance zone: {zone['name']} (ID: {zone['id']})")
            return zone
        except requests.exceptions.RequestException as e:
            logger.error(f"Error creating compliance zone {name}: {e}")
            raise

    def update_network_segment(self, segment: dict, zone_id: int = None, zone_name: str = None, rename_only: bool = False) -> bool:
        """Update a network segment with compliance zone assignment and/or rename it"""
        url = f"{self.base_url}/securitymanager/api/domain/{self.domain_id}/networksegment/{segment['id']}"
        
        if rename_only:
            # Just rename the segment to include zone name
            original_name = segment['name']
            # Remove any existing zone suffix first
            clean_name = original_name.split(' [')[0].strip()
            segment['name'] = f"{clean_name} [{zone_name}]"
            segment['userEdited'] = True
            
            try:
                response = self.session.put(url, data=json.dumps(segment))
                response.raise_for_status()
                logger.debug(f"Renamed network segment from '{original_name}' to '{segment['name']}'")
                return True
            except requests.exceptions.RequestException as e:
                logger.error(f"Error renaming network segment {original_name}: {e}")
                return False
        else:
            # Update zone assignment (original behavior)
            segment['zoneId'] = zone_id
            segment['zoneName'] = zone_name
            segment['userEdited'] = True
            
            try:
                response = self.session.put(url, data=json.dumps(segment))
                response.raise_for_status()
                logger.debug(f"Updated network segment {segment['name']} with zone {zone_name}")
                return True
            except requests.exceptions.RequestException as e:
                logger.error(f"Error updating network segment {segment['name']}: {e}")
                return False

    def map_zones(self, zone_mappings: dict, auto_create: bool = False, rename_only: bool = False):
        """
        Main method to map firewall zones to compliance zones
        
        Args:
            zone_mappings: Dictionary mapping firewall zone names to compliance zone names
            auto_create: If True, automatically create compliance zones for unmapped firewall zones
            rename_only: If True, only rename segments to include zone name, don't assign to compliance zones
            
        Note:
            - Cloud device interfaces are excluded from zone mapping
            - When multiple zones exist in zoneDisplays, the last one is used
        """
        # Get all data
        compliance_zones = self.get_compliance_zones()
        interfaces = self.get_interfaces()
        network_segments = self.get_network_segments()
        
        # Count cloud interfaces for summary
        cloud_interfaces = sum(1 for i in interfaces if i.get('deviceType') == 'CLOUD')
        
        # Extract firewall zones
        firewall_zones = self.extract_firewall_zones(interfaces)
        
        # Create compliance zone lookup
        compliance_zone_lookup = {zone['name']: zone for zone in compliance_zones}
        
        # Process zone mappings
        zone_id_mappings = {}
        
        if not rename_only:
            # Only process compliance zone mappings if not in rename-only mode
            for fw_zone in firewall_zones:
                compliance_zone_name = zone_mappings.get(fw_zone, fw_zone if auto_create else None)
                
                if compliance_zone_name:
                    if compliance_zone_name in compliance_zone_lookup:
                        zone_id_mappings[fw_zone] = compliance_zone_lookup[compliance_zone_name]
                    elif auto_create:
                        # Create new compliance zone
                        new_zone = self.create_compliance_zone(
                            name=compliance_zone_name,
                            description=f"Auto-created from firewall zone: {fw_zone}"
                        )
                        compliance_zone_lookup[compliance_zone_name] = new_zone
                        zone_id_mappings[fw_zone] = new_zone
                    else:
                        logger.warning(f"No mapping found for firewall zone: {fw_zone}")
                else:
                    logger.warning(f"No mapping found for firewall zone: {fw_zone}")
        
        # Map network segments to zones based on interface associations
        segment_zone_assignments = {}
        
        # Build interface to segment mapping
        interface_segment_map = {}
        for segment in network_segments:
            if 'interfaceRefs' in segment:
                for interface_ref in segment['interfaceRefs']:
                    key = (interface_ref['deviceId'], interface_ref['interfaceName'])
                    if key not in interface_segment_map:
                        interface_segment_map[key] = []
                    interface_segment_map[key].append(segment)
        
        # Determine zone assignments for segments
        cloud_interface_skipped = 0
        
        for interface in interfaces:
            # Skip cloud devices
            if interface.get('deviceType') == 'CLOUD':
                cloud_interface_skipped += 1
                continue
                
            if 'zoneDisplays' in interface and interface['zoneDisplays']:
                key = (interface['deviceId'], interface['name'])
                
                # Use the last zone in the list
                fw_zone = interface['zoneDisplays'][-1]
                
                for segment in interface_segment_map.get(key, []):
                    if segment['id'] not in segment_zone_assignments:
                        segment_zone_assignments[segment['id']] = set()
                    
                    if rename_only:
                        # For rename-only mode, just store the zone name
                        segment_zone_assignments[segment['id']].add((None, fw_zone))
                    elif fw_zone in zone_id_mappings:
                        segment_zone_assignments[segment['id']].add(
                            (zone_id_mappings[fw_zone]['id'], zone_id_mappings[fw_zone]['name'])
                        )
        
        if cloud_interface_skipped > 0:
            logger.debug(f"Skipped {cloud_interface_skipped} cloud interfaces during zone assignment")
        
        # Update network segments
        updated_count = 0
        renamed_count = 0
        skipped_cloud_segments = 0
        
        for segment in network_segments:
            # Check if this segment is only associated with cloud devices
            if 'interfaceRefs' in segment:
                all_cloud = all(ref.get('deviceType') == 'CLOUD' for ref in segment['interfaceRefs'])
                if all_cloud:
                    skipped_cloud_segments += 1
                    logger.debug(f"Skipping segment {segment['name']} - only associated with cloud devices")
                    continue
                    
            if segment['id'] in segment_zone_assignments:
                # If multiple zones, use the first one (you may want to handle this differently)
                zone_assignments = list(segment_zone_assignments[segment['id']])
                if zone_assignments:
                    zone_id, zone_name = zone_assignments[0]
                    
                    if rename_only:
                        # Check if segment already has this zone in its name
                        if f"[{zone_name}]" not in segment['name']:
                            if self.update_network_segment(segment, zone_name=zone_name, rename_only=True):
                                renamed_count += 1
                    else:
                        # Only update if not already assigned to this zone
                        if segment.get('zoneId') != zone_id:
                            if self.update_network_segment(segment, zone_id, zone_name):
                                updated_count += 1
                            
                    if len(zone_assignments) > 1:
                        logger.warning(f"Network segment {segment['name']} has multiple zone mappings. Using {zone_name}")
        
        if rename_only:
            logger.info(f"Network segment renaming complete. Renamed {renamed_count} segments.")
        else:
            logger.info(f"Zone mapping complete. Updated {updated_count} network segments.")
            
        if skipped_cloud_segments > 0:
            logger.info(f"Skipped {skipped_cloud_segments} cloud-only network segments")
        
        # Print summary
        print("\n=== Zone Mapping Summary ===")
        print(f"Total interfaces processed: {len(interfaces)} ({cloud_interfaces} cloud interfaces excluded)")
        print(f"Firewall zones found: {len(firewall_zones)} (excluding cloud devices)")
        
        if rename_only:
            print(f"Network segments renamed: {renamed_count}")
            print("\nSegments were renamed to include zone names (e.g., '10.0.0.0/24 [Internal_1]')")
        else:
            print(f"Compliance zones mapped: {len(zone_id_mappings)}")
            print(f"Network segments updated: {updated_count}")
            
        if skipped_cloud_segments > 0:
            print(f"Cloud-only segments skipped: {skipped_cloud_segments}")
        
        if auto_create and not rename_only:
            created_zones = [name for name in compliance_zone_lookup 
                           if name not in [z['name'] for z in compliance_zones]]
            if created_zones:
                print(f"\nNewly created compliance zones:")
                for zone_name in created_zones:
                    print(f"  - {zone_name}")


def load_zone_mappings(file_path: str) -> dict:
    """Load zone mappings from a JSON file"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading zone mappings from {file_path}: {e}")
        raise


def interactive_mode():
    """Run the script in interactive mode with prompts"""
    print("=== FireMon Zone Mapper ===\n")
    
    # Get FireMon server details
    IP = os.environ.get('FIREMON_HOST') or input("FireMon app server IP or FQDN (default: localhost): >> ") or "localhost"
    
    # Check for username in environment variable
    username = os.environ.get('FIREMON_USERNAME')
    if not username:
        username = input("Username for FireMon UI account: >> ")
    else:
        print(f"Using username from environment variable: {username}")
    
    # Check for password in environment variable
    password = os.environ.get('FIREMON_PASSWORD')
    if not password:
        password = getpass.getpass('Password for FireMon UI account: >> ')
    else:
        print("Using password from environment variable")
    
    # Build base URL
    base_url = f"https://{IP}"
    
    # Ask about zone mapping preferences
    print("\n=== Zone Mapping Options ===")
    print("1. Use manual zone mappings from file")
    print("2. Auto-create compliance zones for all firewall zones")
    print("3. Use manual mappings + auto-create for unmapped zones")
    print("4. Only rename network segments to include zone names (no compliance zone assignment)")
    
    choice = input("\nSelect option (1-4): >> ").strip()
    
    zone_mappings = {}
    auto_create = False
    rename_only = False
    
    if choice == '4':
        rename_only = True
        print("\nRename-only mode selected. Segments will be renamed to include zone names.")
        print("Example: '10.0.0.0/24' → '10.0.0.0/24 [Internal_1]'")
    elif choice in ['1', '3']:
        mapping_file = input("Enter path to zone mappings JSON file: >> ").strip()
        if os.path.exists(mapping_file):
            zone_mappings = load_zone_mappings(mapping_file)
            logger.info(f"Loaded {len(zone_mappings)} zone mappings")
        else:
            print(f"File not found: {mapping_file}")
            sys.exit(1)
    
    if choice in ['2', '3']:
        auto_create = True
    
    # Ask for domain ID
    domain_input = input(f"Enter domain ID (default: {os.environ.get('FIREMON_DOMAIN_ID', '1')}): >> ").strip()
    if not domain_input:
        domain_id = int(os.environ.get('FIREMON_DOMAIN_ID', '1'))
    else:
        domain_id = int(domain_input)
    
    # Initialize mapper and run
    mapper = FireMonZoneMapper(base_url, username, password, domain_id)
    
    try:
        mapper.map_zones(zone_mappings, auto_create, rename_only)
        print("\nZone mapping completed successfully!")
    except Exception as e:
        logger.error(f"Error during zone mapping: {e}")
        return 1
    
    return 0


def cli_mode(args):
    """Run the script in CLI mode with command-line arguments"""
    # Get password from args, environment variable, or prompt
    password = args.password or os.environ.get('FIREMON_PASSWORD')
    if not password:
        password = getpass.getpass('Password for FireMon UI account: >> ')
    
    # Build base URL
    base_url = f"https://{args.host}"
    
    # Load zone mappings if provided
    zone_mappings = {}
    if args.mappings:
        zone_mappings = load_zone_mappings(args.mappings)
        logger.info(f"Loaded {len(zone_mappings)} zone mappings")
    
    # Initialize mapper and run
    mapper = FireMonZoneMapper(base_url, args.username, password, args.domain_id)
    
    try:
        mapper.map_zones(zone_mappings, args.auto_create, args.rename_only)
    except Exception as e:
        logger.error(f"Error during zone mapping: {e}")
        return 1
    
    return 0


def main():
    # Check if any command-line arguments were provided (beyond script name)
    if len(sys.argv) > 1:
        # CLI mode
        parser = argparse.ArgumentParser(
            description='Map firewall zones to FireMon compliance zones',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Example usage:
  # With manual mappings file
  python firemon_zone_mapper.py --host localhost --username admin --mappings zone_mappings.json
  
  # With auto-create enabled
  python firemon_zone_mapper.py --host localhost --username admin --auto-create
  
  # Combined
  python firemon_zone_mapper.py --host localhost --username admin --mappings zone_mappings.json --auto-create
  
  # Rename segments only (no zone assignment)
  python firemon_zone_mapper.py --host localhost --username admin --rename-only

Zone mappings file format (JSON):
{
  "Outside_1": "External",
  "Outside_2": "External",
  "Internal_1": "Internal",
  "trust": "Internal",
  "untrust": "External",
  "DMZ": "DMZ"
}

Notes:
- Cloud device interfaces are automatically excluded
- When interfaces have multiple zones, the last zone name is used
- With --rename-only, segments are renamed (e.g., '10.0.0.0/24' → '10.0.0.0/24 [Internal_1]')
            """
        )
        
        parser.add_argument('--host', default=os.environ.get('FIREMON_HOST', 'localhost'), 
                           help='FireMon host/IP (default: localhost, env: FIREMON_HOST)')
        parser.add_argument('--username', default=os.environ.get('FIREMON_USERNAME'), required=not os.environ.get('FIREMON_USERNAME'),
                           help='FireMon username (env: FIREMON_USERNAME)')
        parser.add_argument('--password', default=os.environ.get('FIREMON_PASSWORD'),
                           help='FireMon password (will prompt if not provided, env: FIREMON_PASSWORD)')
        parser.add_argument('--domain-id', type=int, default=int(os.environ.get('FIREMON_DOMAIN_ID', '1')),
                           help='Domain ID (default: 1, env: FIREMON_DOMAIN_ID)')
        parser.add_argument('--mappings', help='Path to JSON file with zone mappings')
        parser.add_argument('--auto-create', action='store_true', 
                           help='Automatically create compliance zones for unmapped firewall zones')
        parser.add_argument('--rename-only', action='store_true',
                           help='Only rename network segments to include zone names, do not assign to compliance zones')
        parser.add_argument('--debug', action='store_true', help='Enable debug logging')
        
        args = parser.parse_args()
        
        if args.debug:
            logging.getLogger().setLevel(logging.DEBUG)
        
        return cli_mode(args)
    else:
        # Interactive mode
        return interactive_mode()


if __name__ == "__main__":
    sys.exit(main())