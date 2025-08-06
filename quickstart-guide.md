# FireMon Zone Mapper - Quick Start Guide

## 1. Basic Interactive Mode (Easiest)

Just run the script and follow the prompts:

```bash
python firemon_zone_mapper.py
```

## 2. Command Line Mode (For Automation)

### Using Environment Variables (Recommended)

1. Create a `.env` file:
```bash
cat > .env << EOF
FIREMON_HOST=localhost
FIREMON_USERNAME=admin
FIREMON_PASSWORD=your_password
FIREMON_DOMAIN_ID=1
EOF

# Secure the file
chmod 600 .env
```

2. Load variables and run:
```bash
# Linux/Mac
export $(cat .env | xargs)
python firemon_zone_mapper.py --auto-create

# Or use the secure wrapper
./secure_wrapper.sh --auto-create
```

### Direct Command Line

```bash
# Auto-create all zones
python firemon_zone_mapper.py --host localhost --username admin --auto-create

# Use zone mappings file
python firemon_zone_mapper.py --host localhost --username admin --mappings zone_mappings.json

# Combined (recommended)
python firemon_zone_mapper.py --host localhost --username admin --mappings zone_mappings.json --auto-create
```

## 3. Zone Mappings File

Create a `zone_mappings.json` file to map firewall zones to compliance zones:

```json
{
  "Outside_1": "External",
  "Outside_2": "External", 
  "Internal_1": "Internal",
  "Internal_2": "Internal",
  "trust": "Internal",
  "untrust": "External",
  "DMZ": "DMZ",
  "Guest": "Partner",
  "Management": "Internal"
}
```

**Important**: When interfaces have multiple zones like `["VRF0", "INET2_Label", "Outside_2"]`, the script uses the **last one** (`Outside_2`)

## 4. Common Use Cases

### Map Everything Automatically
```bash
export FIREMON_PASSWORD="your_password"
python firemon_zone_mapper.py --username admin --auto-create
```

### Use Predefined Mappings + Auto-create Unknown Zones
```bash
export FIREMON_PASSWORD="your_password"
python firemon_zone_mapper.py --username admin --mappings zone_mappings.json --auto-create
```

### Just Rename Segments (No Zone Assignment)
```bash
export FIREMON_PASSWORD="your_password"
python firemon_zone_mapper.py --username admin --rename-only
```
This will rename segments like:
- `10.0.0.0/24` → `10.0.0.0/24 [Internal_1]`
- `192.168.1.0/24` → `192.168.1.0/24 [DMZ]`

### Debug Mode
```bash
python firemon_zone_mapper.py --username admin --auto-create --debug
```

## 5. Security Best Practices

1. **Never** put passwords in command line arguments (visible in ps/process list)
2. **Always** use environment variables or .env files for credentials
3. **Set** proper permissions on .env files: `chmod 600 .env`
4. **Add** .env to .gitignore to prevent accidental commits
5. **Clear** sensitive environment variables after use in shared systems:
   ```bash
   unset FIREMON_PASSWORD FIREMON_USERNAME
   ```
6. **Consider** using secure credential stores for production:
   - HashiCorp Vault
   - AWS Secrets Manager
   - Azure Key Vault
   - CyberArk

## 6. Troubleshooting

- **Authentication Failed**: Check username/password
- **Module Not Found**: Script should auto-detect FireMon paths, ensure running on FireMon appliance
- **SSL Errors**: Normal for internal use, script disables SSL verification
- **No Zones Found**: Check that interfaces have zoneDisplays configured (cloud devices are excluded)
- **Unexpected Zone Names**: Remember the script uses the LAST zone when multiple exist
- **Missing Cloud Zones**: Cloud device zones like "eni-xxx" are intentionally excluded
- **Segments Already Renamed**: The script won't rename segments that already have the zone name in brackets

## 7. What the Script Does

1. Connects to FireMon using your credentials
2. Finds all firewall zones from interface configurations
   - **Excludes cloud devices** (AWS, Azure, etc.) to avoid cloud-specific interface names
   - When interfaces have multiple zones, uses the **last zone name** in the list
   - Example: `["VRF0", "INET2_Label", "Outside_2"]` → uses `"Outside_2"`
3. Either:
   - **Zone Assignment Mode**: Maps zones to compliance zones and assigns network segments
   - **Rename Only Mode**: Just renames segments to include zone names (e.g., `10.0.0.0/24 [Internal_1]`)
4. Updates network segments as appropriate
5. Reports what was changed

**Note**: Cloud device interfaces (like AWS ENIs) are automatically excluded to prevent creating zones with names like "eni-00737a0a693edf3cb"

That's it! The script handles all the complex API calls and logic for you.