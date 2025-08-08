# FireMon Zone Mapper

This script maps firewall zones to FireMon compliance zones. Designed to run directly on FireMon appliances.

## Features

- **Dual Mode Operation**: Runs interactively when no arguments provided, or accepts command-line arguments for automation
- **Smart Zone Selection**: 
  - Excludes cloud device interfaces to avoid non-firewall zone names
  - Uses the last zone from `zoneDisplays` when multiple zones exist (typically the most specific zone)
- **Two Operation Modes**:
  - **Zone Assignment**: Maps firewall zones to compliance zones and assigns network segments
  - **Rename Only**: Just renames network segments to include zone names (e.g., `10.0.0.0/24 [Internal_1]`)
- Maps firewall zones to compliance zones using customizable key mappings
- Automatically creates compliance zones for unmapped firewall zones (optional)
- Updates network segments with appropriate compliance zone assignments
- Provides detailed logging and summary reports
- Handles FireMon appliance-specific Python library paths
- Uses username/password authentication with environment variable support

## Installation

For FireMon Appliances:
- The script automatically handles Python library paths on FireMon appliances
- No additional installation needed - uses FireMon's built-in Python environment

For External Systems:
1. Install Python 3.6 or higher
2. Install dependencies:
```bash
pip install requests
```

## Usage

The script automatically detects whether to run in interactive or command-line mode based on whether arguments are provided.

### Environment Variables

The script supports the following environment variables for credentials and configuration:

- `FIREMON_HOST`: FireMon server hostname/IP (default: localhost)
- `FIREMON_USERNAME`: FireMon username
- `FIREMON_PASSWORD`: FireMon password
- `FIREMON_DOMAIN_ID`: Domain ID (default: 1)

### Interactive Mode (No Arguments)

Simply run the script without any arguments for interactive prompts:

```bash
python firemon_zone_mapper.py
```
<img width="1252" height="707" alt="image" src="https://github.com/user-attachments/assets/5a7113f8-1e06-4e2f-9d83-1f13a3f92205" />


The script will ask for:
- FireMon server IP/FQDN (default: localhost)
- Username and password
- Zone mapping preference:
  1. Manual file
  2. Auto-create
  3. Manual + auto-create
  4. **Rename segments only** (no compliance zone assignment)
- Path to mappings file (if using manual mappings)
- Domain ID (default: 1)

### Command-Line Mode (With Arguments)

For automated/scripted usage, provide command-line arguments:

```bash
# With manual mappings file
python3 firemon_zone_mapper.py --host localhost --username admin --mappings zone_mappings.json

# With auto-create enabled
python3 firemon_zone_mapper.py --host localhost --username admin --auto-create

# Combined mode (recommended)
python3 firemon_zone_mapper.py --host localhost --username admin --mappings zone_mappings.json --auto-create

# Rename segments only (no zone assignment)
python3 firemon_zone_mapper.py --host localhost --username admin --rename-only

# With password on command line (not recommended for security)
python3 firemon_zone_mapper.py --host localhost --username admin --password mypass --auto-create
```

### Using Environment Variables

Environment variables provide a secure way to handle credentials in automated scripts:

```bash
# Set environment variables (Linux/Mac)
export FIREMON_HOST="firemon.company.com"
export FIREMON_USERNAME="admin"
export FIREMON_PASSWORD="your_secure_password"
export FIREMON_DOMAIN_ID="1"

# Set environment variables (Windows Command Prompt)
set FIREMON_HOST=firemon.company.com
set FIREMON_USERNAME=admin
set FIREMON_PASSWORD=your_secure_password
set FIREMON_DOMAIN_ID=1

# Set environment variables (Windows PowerShell)
$env:FIREMON_HOST = "firemon.company.com"
$env:FIREMON_USERNAME = "admin"
$env:FIREMON_PASSWORD = "your_secure_password"
$env:FIREMON_DOMAIN_ID = "1"

# Run the script - credentials will be picked up from environment
python3 firemon_zone_mapper.py --auto-create

# You can still override environment variables with command-line arguments
python3 firemon_zone_mapper.py --username different_user --auto-create
```

### Secure Automation Examples

```bash
# Example 1: Using a .env file (requires python-dotenv package)
cat > .env << EOF
FIREMON_HOST=localhost
FIREMON_USERNAME=admin
FIREMON_PASSWORD=secure_password
EOF

# Load variables and run
export $(cat .env | xargs)
python3 firemon_zone_mapper.py --auto-create

# Example 2: Using a secure credential store (like HashiCorp Vault)
export FIREMON_PASSWORD=$(vault kv get -field=password secret/firemon)
python3 firemon_zone_mapper.py --username admin --auto-create

# Example 3: In a CI/CD pipeline (like Jenkins)
# Set credentials as secret environment variables in your pipeline
python3 firemon_zone_mapper.py --mappings zone_mappings.json --auto-create

# Example 4: Using a bash script wrapper
#!/bin/bash
# Read password securely
read -s -p "Enter FireMon password: " FIREMON_PASSWORD
export FIREMON_PASSWORD
python3 firemon_zone_mapper.py --username admin --auto-create

# Example 5: Rename-only mode in automation
export FIREMON_PASSWORD=$(vault kv get -field=password secret/firemon)
python3 firemon_zone_mapper.py --username admin --rename-only
```

### Command-Line Options

- `--host`: FireMon host/IP (default: localhost, env: FIREMON_HOST)
- `--username`: FireMon username (required in CLI mode unless set via env: FIREMON_USERNAME)
- `--password`: FireMon password (will prompt if not provided, env: FIREMON_PASSWORD)
- `--domain-id`: Specify domain ID (default: 1, env: FIREMON_DOMAIN_ID)
- `--mappings`: Path to JSON file with zone mappings
- `--auto-create`: Automatically create compliance zones for unmapped firewall zones
- `--rename-only`: Only rename network segments to include zone names (no compliance zone assignment)
- `--debug`: Enable debug logging

## How It Works

1. **Authentication**:
   - Uses username/password to authenticate with FireMon
   - Obtains a session token for API calls
   - All API calls use SSL (with certificate verification disabled for internal use)

2. **Discovery Phase**:
   - Fetches all interfaces and extracts unique firewall zones from `zoneDisplays`
   - **Excludes cloud device interfaces** (deviceType: CLOUD) to avoid cloud-specific zone names
   - When multiple zones exist in `zoneDisplays`, uses the **last zone** in the list
   - Retrieves all existing compliance zones
   - Gets all network segments

3. **Mapping Phase**:
   - Maps firewall zones to compliance zones using provided mappings
   - If auto-create is enabled, creates new compliance zones for unmapped firewall zones

4. **Assignment Phase**:
   - Determines which network segments should be assigned to which compliance zones
   - Updates network segments with appropriate zone assignments
   - Only considers non-cloud device interfaces for zone assignments
   
5. **Rename-Only Mode** (optional):
   - Instead of assigning zones, renames network segments to include zone names
   - Example: `10.0.0.0/24` becomes `10.0.0.0/24 [Internal_1]`
   - Useful for visual identification without changing compliance zone assignments
     <img width="1920" height="963" alt="image" src="https://github.com/user-attachments/assets/18b3925a-1d0c-4b46-a4ce-ba1d903408bc" />


## Zone Mappings File Format

The zone mappings file should be a JSON object mapping firewall zone names to compliance zone names:

```json
{
  "firewall_zone_name": "compliance_zone_name",
  "INET1_Label": "External",
  "Internal_1": "Internal",
  "VRF0": "Internal"
}
```

## Output

The script provides:
- Real-time logging of operations
- Summary report showing:
  - Number of firewall zones found
  - Number of compliance zones mapped
  - Number of network segments updated
  - List of newly created compliance zones (if any)

## Error Handling

The script includes comprehensive error handling for:
- API connection issues
- Authentication failures
- Invalid zone mappings
- Network segment update failures

## Notes

- **Cloud devices are excluded**: Interfaces from cloud devices (AWS, Azure, etc.) are automatically skipped to avoid creating zones with cloud-specific names like "eni-xxx"
- **Multiple zones handling**: When an interface has multiple zones in `zoneDisplays`, the script uses the **last zone** in the list
  - Example: `["VRF0", "INET2_Label", "Outside_2"]` → uses `"Outside_2"`
- **Rename-only mode**: With `--rename-only`, segments are renamed to include zone names without changing compliance zone assignments
  - Original: `10.0.0.0/24`
  - Renamed: `10.0.0.0/24 [Internal_1]`
  - Useful for visual identification in the FireMon UI
  - The script won't rename segments that already have zone names in brackets
  - To reverse: manually remove the bracketed zone names or use the FireMon API
- Network segments can only be assigned to one compliance zone
- If a network segment has interfaces in multiple firewall zones that map to different compliance zones, the first mapping is used (with a warning)
- The script only updates network segments that need changes (idempotent operation)
- Cloud-only network segments (those only associated with cloud device interfaces) are skipped.
- Existing zone assignments are preserved unless they need to be changed

## Security Considerations

- The script disables SSL certificate verification for internal FireMon use
- Passwords are masked when entered interactively
- **Best Practice**: Use environment variables for credentials instead of command-line arguments
- Avoid passing passwords via command line in production environments (visible in process lists)
- Set appropriate file permissions on any .env files containing credentials (chmod 600)
- Clear environment variables after use in shared environments:
  ```bash
  unset FIREMON_PASSWORD FIREMON_USERNAME FIREMON_HOST FIREMON_DOMAIN_ID
  ```
