Make a python script to mapa firewall zones shown as zoneDisplays on the interface to FireMon complaince zones. We'll need to use key mappings since firewall zones names wont be the same as compliance zone names. Add an option to automatically create complaince zones based on firewall zone names. 

## List complaince Zones
Request URL
https://demo01.firemon.xyz/securitymanager/api/domain/1/zone.json?page=0&pageSize=20&search=&sort=name
Request Method
GET

### Example Response:
```
{
    "total": 16,
    "page": 0,
    "pageSize": 20,
    "count": 16,
    "results": [
        {
            "id": 3,
            "name": "All",
            "description": "All Zones",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": true,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 1,
            "name": "Any",
            "description": "Any",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": true,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 4,
            "name": "BES",
            "description": "Bulk Electric System (BES) Cyber Systems",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 13,
            "name": "DMZ",
            "description": "Demilitarized Zone (DMZ)",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 5,
            "name": "ePHI",
            "description": "Electronic Protected Health Information (ePHI)",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 2,
            "name": "External",
            "description": "External Zone",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 6,
            "name": "ICS_DMZ",
            "description": "Industrial Control System DMZ Network",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 7,
            "name": "ICS_External",
            "description": "Industrial Control System External Network",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 8,
            "name": "ICS_Network",
            "description": "Industrial Control System Internal Network",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 14,
            "name": "Internal",
            "description": "Internal Zone",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 17,
            "name": "NetZone3",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": false,
            "virtual": false,
            "hexColor": "#B8BEBF",
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 15,
            "name": "Partner",
            "description": "Partner Zone",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 9,
            "name": "PCI_Management",
            "description": "Payment Card Management Zone",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 10,
            "name": "PCI_Network",
            "description": "**NOTE: MUST be completed by client based upon their needs/requirements.",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "hexColor": "#B8BEBF",
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 11,
            "name": "PCI_Wireless Network",
            "description": "**NOTE: MUST be completed by client based upon their needs/requirements.",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        {
            "id": 12,
            "name": "Unused Zone",
            "description": "Not external zone",
            "domainId": 1,
            "domainName": "Enterprise",
            "system": true,
            "virtual": false,
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        }
    ]
}
```

## List Network Segment
Request URL
https://demo01.firemon.xyz/securitymanager/api/domain/1/networksegment/filter?page=0&pageSize=100&sort=name
Request Method
GET

### Example Response:
```
{
    "total": 175,
    "page": 0,
    "pageSize": 100,
    "count": 100,
    "results": [
        {
            "id": 516,
            "name": "10.0.0.0/20",
            "description": "Auto-generated from Device AWS-ACT-7176 for subnet-0820195af4f752818",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0cc44bd4b1d97af51",
                    "interfaceDisplayName": "subnet-0cc44bd4b1d97af51",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-023635d761aed138c",
                    "interfaceDisplayName": "subnet-023635d761aed138c",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0820195af4f752818",
                    "interfaceDisplayName": "subnet-0820195af4f752818",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0d2d8fa5a56bb3fd7",
                    "interfaceDisplayName": "subnet-0d2d8fa5a56bb3fd7",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 19,
            "name": "10.0.0.0/24",
            "description": "Auto-generated from Device srx.firemon.xyz for ge-0/0/0.0",
            "hexColor": "#B8BEBF",
            "domainId": 1,
            "domainName": "Enterprise",
            "zoneId": 10,
            "excluded": false,
            "generated": false,
            "zoneName": "PCI_Network",
            "zoneHexColor": "#B8BEBF",
            "userEdited": true,
            "interfaceRefs": [
                {
                    "deviceId": 5,
                    "deviceName": "fortigate.firemon.xyz",
                    "deviceType": "FIREWALL",
                    "interfaceName": "mgmt",
                    "interfaceDisplayName": "mgmt (Management)",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 4,
                    "deviceName": "paloalto.firemon.xyz",
                    "deviceType": "FIREWALL",
                    "interfaceName": "ethernet1/1",
                    "interfaceDisplayName": "ethernet1/1",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 3,
                    "deviceName": "srx.firemon.xyz",
                    "deviceType": "FIREWALL",
                    "interfaceName": "ge-0/0/0.0",
                    "interfaceDisplayName": "ge-0/0/0.0",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 638,
            "name": "10.0.0.0/24 (1)",
            "description": "Auto-generated from Device sophos.firemon.xyz for Port1",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 2,
                    "deviceName": "sophos.firemon.xyz",
                    "deviceType": "FIREWALL",
                    "interfaceName": "Port1",
                    "interfaceDisplayName": "Port1",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 603,
            "name": "10.0.11.208",
            "description": "Auto-generated from Device AWS-ACT-7176 for eni-048439ea52171baec",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-048439ea52171baec",
                    "interfaceDisplayName": "eni-048439ea52171baec",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 506,
            "name": "10.0.128.0/20",
            "description": "Auto-generated from Device AWS-ACT-7176 for subnet-050f45265ed5aa648",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-07f11524effd17280",
                    "interfaceDisplayName": "subnet-07f11524effd17280",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-050f45265ed5aa648",
                    "interfaceDisplayName": "subnet-050f45265ed5aa648",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-08203f7002a9ab6f2",
                    "interfaceDisplayName": "subnet-08203f7002a9ab6f2",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0483e39d2fd5c6cda",
                    "interfaceDisplayName": "subnet-0483e39d2fd5c6cda",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 524,
            "name": "10.0.128.68",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0e1ce64683c23ac22",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0e1ce64683c23ac22",
                    "interfaceDisplayName": "eni-0e1ce64683c23ac22",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 106,
            "name": "10.0.133.234",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0a2c5ba459227989f",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": true,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0a2c5ba459227989f",
                    "interfaceDisplayName": "eni-0a2c5ba459227989f",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 24,
                    "deviceName": "Core-rtr-Dallas-ofc",
                    "deviceType": "ROUTER_SWITCH",
                    "interfaceName": "fm-intf-2",
                    "interfaceDisplayName": "fm-intf-2",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 624,
            "name": "10.0.136.73",
            "description": "Auto-generated from Device AWS-ACT-7176 for eni-09b9efd25fe86e85f",
            "domainId": 1,
            "domainName": "Enterprise",
            "zoneId": 10,
            "excluded": false,
            "generated": false,
            "zoneName": "PCI_Network",
            "zoneHexColor": "#B8BEBF",
            "userEdited": true,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-09b9efd25fe86e85f",
                    "interfaceDisplayName": "eni-09b9efd25fe86e85f",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 536,
            "name": "10.0.140.215",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0d78f3dc4e68a80e1",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0d78f3dc4e68a80e1",
                    "interfaceDisplayName": "eni-0d78f3dc4e68a80e1",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 492,
            "name": "10.0.144.0/20",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-04e0715f6f1570942",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-04e0715f6f1570942",
                    "interfaceDisplayName": "subnet-04e0715f6f1570942",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0332a823f2a53ebcd",
                    "interfaceDisplayName": "subnet-0332a823f2a53ebcd",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 518,
            "name": "10.0.149.178",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0d09072242dccd2a7",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0d09072242dccd2a7",
                    "interfaceDisplayName": "eni-0d09072242dccd2a7",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 537,
            "name": "10.0.150.169",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-07d6a556307ecf88c",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-07d6a556307ecf88c",
                    "interfaceDisplayName": "eni-07d6a556307ecf88c",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 599,
            "name": "10.0.15.247",
            "description": "Auto-generated from Device AWS-ACT-7176 for eni-0d69e0071d8c0b375",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0d69e0071d8c0b375",
                    "interfaceDisplayName": "eni-0d69e0071d8c0b375",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 532,
            "name": "10.0.153.174",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0721b3d1e0cfcfe82",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0721b3d1e0cfcfe82",
                    "interfaceDisplayName": "eni-0721b3d1e0cfcfe82",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 512,
            "name": "10.0.16.0/20",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-0be87cc8e6fc46390",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0debe7567def7ecbf",
                    "interfaceDisplayName": "subnet-0debe7567def7ecbf",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0be87cc8e6fc46390",
                    "interfaceDisplayName": "subnet-0be87cc8e6fc46390",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 562,
            "name": "10.0.2.206",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-051d286f28c85de46",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-051d286f28c85de46",
                    "interfaceDisplayName": "eni-051d286f28c85de46",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 513,
            "name": "10.0.3.33",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-01fecbff16438668f",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-01fecbff16438668f",
                    "interfaceDisplayName": "eni-01fecbff16438668f",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 523,
            "name": "10.0.9.100",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-07d053087fa444fbe",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-07d053087fa444fbe",
                    "interfaceDisplayName": "eni-07d053087fa444fbe",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 573,
            "name": "10.1.0.0/24",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-0ec476907ef83a8f2",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0ec476907ef83a8f2",
                    "interfaceDisplayName": "subnet-0ec476907ef83a8f2",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 568,
            "name": "10.1.0.142",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0993050c6c5ec5329",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0993050c6c5ec5329",
                    "interfaceDisplayName": "eni-0993050c6c5ec5329",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 567,
            "name": "10.1.1.0/24",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-0738fbf21f10e5b4c",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0738fbf21f10e5b4c",
                    "interfaceDisplayName": "subnet-0738fbf21f10e5b4c",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 571,
            "name": "10.1.1.237",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0290820169d3a63ea",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0290820169d3a63ea",
                    "interfaceDisplayName": "eni-0290820169d3a63ea",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 582,
            "name": "10.2.0.0/24",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-0738a7622023690de",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0738a7622023690de",
                    "interfaceDisplayName": "subnet-0738a7622023690de",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 576,
            "name": "10.2.0.123",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0fa170984bdd0c048",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0fa170984bdd0c048",
                    "interfaceDisplayName": "eni-0fa170984bdd0c048",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 589,
            "name": "10.2.1.0/24",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-05dc4d38ff9c1cb80",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-05dc4d38ff9c1cb80",
                    "interfaceDisplayName": "subnet-05dc4d38ff9c1cb80",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 569,
            "name": "10.2.1.77",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0073ed44581a5037a",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0073ed44581a5037a",
                    "interfaceDisplayName": "eni-0073ed44581a5037a",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 636,
            "name": "10.255.0.0/24",
            "description": "Auto-generated from Device sophos.firemon.xyz for GuestAP",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 2,
                    "deviceName": "sophos.firemon.xyz",
                    "deviceType": "FIREWALL",
                    "interfaceName": "GuestAP",
                    "interfaceDisplayName": "GuestAP",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 4,
            "name": "103.214.110.208/28",
            "description": "Auto-generated from Device sophos.firemon.xyz for Port2",
            "hexColor": "#B8BEBF",
            "domainId": 1,
            "domainName": "Enterprise",
            "zoneId": 13,
            "excluded": false,
            "generated": false,
            "zoneName": "DMZ",
            "userEdited": true,
            "interfaceRefs": [],
            "ipAddresses": [
                "103.214.110.209"
            ],
            "type": "INET"
        },
        {
            "id": 637,
            "name": "103.214.110.208/28 (1)",
            "description": "Auto-generated from Device sophos.firemon.xyz for Port2",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 2,
                    "deviceName": "sophos.firemon.xyz",
                    "deviceType": "FIREWALL",
                    "interfaceName": "Port2",
                    "interfaceDisplayName": "Port2",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 502,
            "name": "172.31.0.0/20",
            "description": "Auto-generated from Device AWS-ACT-7176 for subnet-04466fb12b78f7fed",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0640c0f0f28015fbc",
                    "interfaceDisplayName": "subnet-0640c0f0f28015fbc",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-01957bb97cbdaf2de",
                    "interfaceDisplayName": "subnet-01957bb97cbdaf2de",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0538dbf4a80dc3ae1",
                    "interfaceDisplayName": "subnet-0538dbf4a80dc3ae1",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0b1fb3c2481007d3c",
                    "interfaceDisplayName": "subnet-0b1fb3c2481007d3c",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0b27063d0a6062a94",
                    "interfaceDisplayName": "subnet-0b27063d0a6062a94",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-00b770aa221ac9e4c",
                    "interfaceDisplayName": "subnet-00b770aa221ac9e4c",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0e2f59d2ae3910092",
                    "interfaceDisplayName": "subnet-0e2f59d2ae3910092",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-057435e22a5d6e922",
                    "interfaceDisplayName": "subnet-057435e22a5d6e922",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-03ca6f11363a76963",
                    "interfaceDisplayName": "subnet-03ca6f11363a76963",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0770979161c1b8256",
                    "interfaceDisplayName": "subnet-0770979161c1b8256",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-043b3479af491b170",
                    "interfaceDisplayName": "subnet-043b3479af491b170",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-066a9d593f130189f",
                    "interfaceDisplayName": "subnet-066a9d593f130189f",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0d13ab7b71e323631",
                    "interfaceDisplayName": "subnet-0d13ab7b71e323631",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-00fae1e844c63da79",
                    "interfaceDisplayName": "subnet-00fae1e844c63da79",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0477ee63deb15dfb7",
                    "interfaceDisplayName": "subnet-0477ee63deb15dfb7",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0f6945b2dfcbfa270",
                    "interfaceDisplayName": "subnet-0f6945b2dfcbfa270",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-02a62f605de835360",
                    "interfaceDisplayName": "subnet-02a62f605de835360",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0394d410a281ed64b",
                    "interfaceDisplayName": "subnet-0394d410a281ed64b",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0b958e8f1a2a58fcf",
                    "interfaceDisplayName": "subnet-0b958e8f1a2a58fcf",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0b07ef8b08cbcdbdc",
                    "interfaceDisplayName": "subnet-0b07ef8b08cbcdbdc",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0621640e6b3cf2fb4",
                    "interfaceDisplayName": "subnet-0621640e6b3cf2fb4",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-01894f4aa037d4208",
                    "interfaceDisplayName": "subnet-01894f4aa037d4208",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-08b9e71fabae47f2e",
                    "interfaceDisplayName": "subnet-08b9e71fabae47f2e",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-049787621b330d4ce",
                    "interfaceDisplayName": "subnet-049787621b330d4ce",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-04466fb12b78f7fed",
                    "interfaceDisplayName": "subnet-04466fb12b78f7fed",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-092581ac407855ae3",
                    "interfaceDisplayName": "subnet-092581ac407855ae3",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0d8626f2a6bba937c",
                    "interfaceDisplayName": "subnet-0d8626f2a6bba937c",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-07d22e480d5d5b9fa",
                    "interfaceDisplayName": "subnet-07d22e480d5d5b9fa",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0d3d7cd4d3193feeb",
                    "interfaceDisplayName": "subnet-0d3d7cd4d3193feeb",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-09c91028dac6213fc",
                    "interfaceDisplayName": "subnet-09c91028dac6213fc",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-07b6985ffa347abfe",
                    "interfaceDisplayName": "subnet-07b6985ffa347abfe",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-016d187da5f96df42",
                    "interfaceDisplayName": "subnet-016d187da5f96df42",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0b52b26134f6a75ef",
                    "interfaceDisplayName": "subnet-0b52b26134f6a75ef",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0e4b32b4fb14ac5bb",
                    "interfaceDisplayName": "subnet-0e4b32b4fb14ac5bb",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 598,
            "name": "172.31.0.0/24",
            "description": "Auto-generated from Device AWS-ACT-7176 for subnet-0cf93fc14caa771b4",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0cf93fc14caa771b4",
                    "interfaceDisplayName": "subnet-0cf93fc14caa771b4",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 604,
            "name": "172.31.0.133",
            "description": "Auto-generated from Device AWS-ACT-7176 for eni-0861e0b61f7ccf876",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0861e0b61f7ccf876",
                    "interfaceDisplayName": "eni-0861e0b61f7ccf876",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 614,
            "name": "172.31.0.181",
            "description": "Auto-generated from Device AWS-ACT-7176 for eni-0ff322fde324d5fb8",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0ff322fde324d5fb8",
                    "interfaceDisplayName": "eni-0ff322fde324d5fb8",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 500,
            "name": "172.31.0.63",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0272540c017646fe8",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0272540c017646fe8",
                    "interfaceDisplayName": "eni-0272540c017646fe8",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 579,
            "name": "172.31.11.94",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-07b6b35506869ed08",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-07b6b35506869ed08",
                    "interfaceDisplayName": "eni-07b6b35506869ed08",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 550,
            "name": "172.31.1.209",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0395c27d357abc6b4",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0395c27d357abc6b4",
                    "interfaceDisplayName": "eni-0395c27d357abc6b4",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 545,
            "name": "172.31.1.222",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-089cc2327ded163be",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-089cc2327ded163be",
                    "interfaceDisplayName": "eni-089cc2327ded163be",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 505,
            "name": "172.31.128.0/20",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-05adec1069c1492c8",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-05adec1069c1492c8",
                    "interfaceDisplayName": "subnet-05adec1069c1492c8",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0b8182b12ccce4676",
                    "interfaceDisplayName": "subnet-0b8182b12ccce4676",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 531,
            "name": "172.31.133.22",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0278af107f16fb4e0",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0278af107f16fb4e0",
                    "interfaceDisplayName": "eni-0278af107f16fb4e0",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 501,
            "name": "172.31.14.201",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0290186d1c551ed16",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0290186d1c551ed16",
                    "interfaceDisplayName": "eni-0290186d1c551ed16",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 561,
            "name": "172.31.143.62",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-06eceeef9372164dc",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-06eceeef9372164dc",
                    "interfaceDisplayName": "eni-06eceeef9372164dc",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 533,
            "name": "172.31.144.0/20",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-0aa9969b450eff5c2",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-02954179f1f173345",
                    "interfaceDisplayName": "subnet-02954179f1f173345",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0aa9969b450eff5c2",
                    "interfaceDisplayName": "subnet-0aa9969b450eff5c2",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 511,
            "name": "172.31.146.137",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0d2c21d420073a5f1",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0d2c21d420073a5f1",
                    "interfaceDisplayName": "eni-0d2c21d420073a5f1",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 503,
            "name": "172.31.16.0/20",
            "description": "Auto-generated from Device AWS-ACT-7176 for subnet-05d859880c211d843",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-05aa9bff1686924f4",
                    "interfaceDisplayName": "subnet-05aa9bff1686924f4",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0f0417c23ae450b65",
                    "interfaceDisplayName": "subnet-0f0417c23ae450b65",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-00332ac0dec7025f5",
                    "interfaceDisplayName": "subnet-00332ac0dec7025f5",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0caa8f43df9aa1db0",
                    "interfaceDisplayName": "subnet-0caa8f43df9aa1db0",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0b2c4e4358868ca62",
                    "interfaceDisplayName": "subnet-0b2c4e4358868ca62",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0d773f6892361e651",
                    "interfaceDisplayName": "subnet-0d773f6892361e651",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0ddc7ed824141ed6d",
                    "interfaceDisplayName": "subnet-0ddc7ed824141ed6d",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0be4685e20562a910",
                    "interfaceDisplayName": "subnet-0be4685e20562a910",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0bb0a7454c4fee042",
                    "interfaceDisplayName": "subnet-0bb0a7454c4fee042",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0eba55f1d1d3917b9",
                    "interfaceDisplayName": "subnet-0eba55f1d1d3917b9",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0d3a15e8615060800",
                    "interfaceDisplayName": "subnet-0d3a15e8615060800",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0835162028067753f",
                    "interfaceDisplayName": "subnet-0835162028067753f",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0d088741fd1fb73f4",
                    "interfaceDisplayName": "subnet-0d088741fd1fb73f4",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-03fb436ef95401c18",
                    "interfaceDisplayName": "subnet-03fb436ef95401c18",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0186c6a4938d415ba",
                    "interfaceDisplayName": "subnet-0186c6a4938d415ba",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-071dcbbdb3b7e5bd8",
                    "interfaceDisplayName": "subnet-071dcbbdb3b7e5bd8",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0ed5dc29f2f62f804",
                    "interfaceDisplayName": "subnet-0ed5dc29f2f62f804",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-04088bbe13a6e7ade",
                    "interfaceDisplayName": "subnet-04088bbe13a6e7ade",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-023855b6d73c6512c",
                    "interfaceDisplayName": "subnet-023855b6d73c6512c",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0866d46fe256fc443",
                    "interfaceDisplayName": "subnet-0866d46fe256fc443",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0956ff9c6a6ccc413",
                    "interfaceDisplayName": "subnet-0956ff9c6a6ccc413",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0d0b5976d3f288aec",
                    "interfaceDisplayName": "subnet-0d0b5976d3f288aec",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-04d8c81258e272be5",
                    "interfaceDisplayName": "subnet-04d8c81258e272be5",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0c6965c10a27f0dc3",
                    "interfaceDisplayName": "subnet-0c6965c10a27f0dc3",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0c4f3c3498c8cf631",
                    "interfaceDisplayName": "subnet-0c4f3c3498c8cf631",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0ef7a763ef3a1ebce",
                    "interfaceDisplayName": "subnet-0ef7a763ef3a1ebce",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-00926675a4e425906",
                    "interfaceDisplayName": "subnet-00926675a4e425906",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-02c266b42a51c8bbb",
                    "interfaceDisplayName": "subnet-02c266b42a51c8bbb",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-05d859880c211d843",
                    "interfaceDisplayName": "subnet-05d859880c211d843",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-09ab1b0cd12f02f02",
                    "interfaceDisplayName": "subnet-09ab1b0cd12f02f02",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0464b5f47fbe519d9",
                    "interfaceDisplayName": "subnet-0464b5f47fbe519d9",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0bc499013ba244888",
                    "interfaceDisplayName": "subnet-0bc499013ba244888",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-058bd71432411a552",
                    "interfaceDisplayName": "subnet-058bd71432411a552",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-00aab411fb3b6fa4c",
                    "interfaceDisplayName": "subnet-00aab411fb3b6fa4c",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 539,
            "name": "172.31.16.111",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0b39a5c0a321d50a1",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0b39a5c0a321d50a1",
                    "interfaceDisplayName": "eni-0b39a5c0a321d50a1",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 543,
            "name": "172.31.2.124",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0c1a70ad1dba508c9",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0c1a70ad1dba508c9",
                    "interfaceDisplayName": "eni-0c1a70ad1dba508c9",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 554,
            "name": "172.31.23.149",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-068d447e0f0e50294",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-068d447e0f0e50294",
                    "interfaceDisplayName": "eni-068d447e0f0e50294",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 586,
            "name": "172.31.2.37",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-02ff7397a19ee0123",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-02ff7397a19ee0123",
                    "interfaceDisplayName": "eni-02ff7397a19ee0123",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 575,
            "name": "172.31.27.17",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0a60e6eb5a07439bb",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0a60e6eb5a07439bb",
                    "interfaceDisplayName": "eni-0a60e6eb5a07439bb",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 565,
            "name": "172.31.31.34",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0c1e8a84d8a66c2a2",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0c1e8a84d8a66c2a2",
                    "interfaceDisplayName": "eni-0c1e8a84d8a66c2a2",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 498,
            "name": "172.31.32.0/20",
            "description": "Auto-generated from Device AWS-ACT-7176 for subnet-090b18d49966253a6",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0e08fb00078c1d6b3",
                    "interfaceDisplayName": "subnet-0e08fb00078c1d6b3",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-03a2ac421ef3f9328",
                    "interfaceDisplayName": "subnet-03a2ac421ef3f9328",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-09858caf5426e175b",
                    "interfaceDisplayName": "subnet-09858caf5426e175b",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-07fc4ffd7501d9731",
                    "interfaceDisplayName": "subnet-07fc4ffd7501d9731",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-028be09b8e1c7a2c9",
                    "interfaceDisplayName": "subnet-028be09b8e1c7a2c9",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-09b16ebe1d66d107e",
                    "interfaceDisplayName": "subnet-09b16ebe1d66d107e",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-03b10db6dd3001bb0",
                    "interfaceDisplayName": "subnet-03b10db6dd3001bb0",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0840662adf9f4e8bc",
                    "interfaceDisplayName": "subnet-0840662adf9f4e8bc",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-08aacaa41a5ebdb8c",
                    "interfaceDisplayName": "subnet-08aacaa41a5ebdb8c",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0a06bd624e2598309",
                    "interfaceDisplayName": "subnet-0a06bd624e2598309",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0ff329b35967fc6b6",
                    "interfaceDisplayName": "subnet-0ff329b35967fc6b6",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0a5c5970e85354484",
                    "interfaceDisplayName": "subnet-0a5c5970e85354484",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-000a88d3b78786169",
                    "interfaceDisplayName": "subnet-000a88d3b78786169",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-01ebddc1a6cf01b7b",
                    "interfaceDisplayName": "subnet-01ebddc1a6cf01b7b",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0ebe6a657b9236ec5",
                    "interfaceDisplayName": "subnet-0ebe6a657b9236ec5",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-090b18d49966253a6",
                    "interfaceDisplayName": "subnet-090b18d49966253a6",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0833f171a2930d659",
                    "interfaceDisplayName": "subnet-0833f171a2930d659",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-04ea29d3e330787ab",
                    "interfaceDisplayName": "subnet-04ea29d3e330787ab",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-057271ee0efdb68ab",
                    "interfaceDisplayName": "subnet-057271ee0efdb68ab",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-04c5e853d7a19d791",
                    "interfaceDisplayName": "subnet-04c5e853d7a19d791",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0cce27418e98562a1",
                    "interfaceDisplayName": "subnet-0cce27418e98562a1",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0ae0f6e5fc756ad95",
                    "interfaceDisplayName": "subnet-0ae0f6e5fc756ad95",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0a3511ec234f9f48d",
                    "interfaceDisplayName": "subnet-0a3511ec234f9f48d",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0c641a70d3d69755b",
                    "interfaceDisplayName": "subnet-0c641a70d3d69755b",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-004cd3b58f684171c",
                    "interfaceDisplayName": "subnet-004cd3b58f684171c",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0ea05fcf0d81559e5",
                    "interfaceDisplayName": "subnet-0ea05fcf0d81559e5",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-056bac616ce9940c5",
                    "interfaceDisplayName": "subnet-056bac616ce9940c5",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-07ad62a0c8a893466",
                    "interfaceDisplayName": "subnet-07ad62a0c8a893466",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-03c7477dfb02fdcb6",
                    "interfaceDisplayName": "subnet-03c7477dfb02fdcb6",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-04f986fb3cc473779",
                    "interfaceDisplayName": "subnet-04f986fb3cc473779",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 499,
            "name": "172.31.3.73",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-07532092a2fbf31e3",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-07532092a2fbf31e3",
                    "interfaceDisplayName": "eni-07532092a2fbf31e3",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 525,
            "name": "172.31.48.0/20",
            "description": "Auto-generated from Device AWS-ACT-7176 for subnet-09cefca7e61cff1da",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-04735d93460e3215a",
                    "interfaceDisplayName": "subnet-04735d93460e3215a",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-09cefca7e61cff1da",
                    "interfaceDisplayName": "subnet-09cefca7e61cff1da",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-04083dd603e96ecbc",
                    "interfaceDisplayName": "subnet-04083dd603e96ecbc",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-00cb275a6f424db5f",
                    "interfaceDisplayName": "subnet-00cb275a6f424db5f",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 627,
            "name": "172.31.64.0/20",
            "description": "Auto-generated from Device AWS-ACT-7176 for subnet-092d11f59d84bdb9f",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-092d11f59d84bdb9f",
                    "interfaceDisplayName": "subnet-092d11f59d84bdb9f",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 529,
            "name": "172.31.7.238",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0861ceef3c352989b",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0861ceef3c352989b",
                    "interfaceDisplayName": "eni-0861ceef3c352989b",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 620,
            "name": "172.31.80.0/20",
            "description": "Auto-generated from Device AWS-ACT-7176 for subnet-04a062a9f486e8dec",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-04a062a9f486e8dec",
                    "interfaceDisplayName": "subnet-04a062a9f486e8dec",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 563,
            "name": "172.31.9.199",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-017e886b5cdbd01cc",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-017e886b5cdbd01cc",
                    "interfaceDisplayName": "eni-017e886b5cdbd01cc",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 508,
            "name": "192.168.0.0/20",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-0bf0f04ce6be9b41a",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0214337fca5fbcb96",
                    "interfaceDisplayName": "subnet-0214337fca5fbcb96",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0bf0f04ce6be9b41a",
                    "interfaceDisplayName": "subnet-0bf0f04ce6be9b41a",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 616,
            "name": "192.168.0.0/21",
            "description": "Auto-generated from Device AWS-ACT-7176 for subnet-0fa457e00f4a4be0b",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0fa457e00f4a4be0b",
                    "interfaceDisplayName": "subnet-0fa457e00f4a4be0b",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 467,
            "name": "192.168.0.0/24",
            "description": "Auto-generated from Device srx.firemon.xyz for ge-0/0/1.0",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 3,
                    "deviceName": "srx.firemon.xyz",
                    "deviceType": "FIREWALL",
                    "interfaceName": "ge-0/0/1.0",
                    "interfaceDisplayName": "ge-0/0/1.0",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 469,
            "name": "192.168.100.0/24",
            "description": "Auto-generated from Device fortigate.firemon.xyz for port3 (MPLS)",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 5,
                    "deviceName": "fortigate.firemon.xyz",
                    "deviceType": "FIREWALL",
                    "interfaceName": "port3",
                    "interfaceDisplayName": "port3 (MPLS)",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 4,
                    "deviceName": "paloalto.firemon.xyz",
                    "deviceType": "FIREWALL",
                    "interfaceName": "ethernet1/3",
                    "interfaceDisplayName": "ethernet1/3",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 572,
            "name": "192.168.100.0/28",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-0024ddfc85de4f8f3",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0024ddfc85de4f8f3",
                    "interfaceDisplayName": "subnet-0024ddfc85de4f8f3",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 587,
            "name": "192.168.100.32/28",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-0e4a1296638060e1c",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0e4a1296638060e1c",
                    "interfaceDisplayName": "subnet-0e4a1296638060e1c",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 588,
            "name": "192.168.100.37",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0a48d559a30bbfde5",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0a48d559a30bbfde5",
                    "interfaceDisplayName": "eni-0a48d559a30bbfde5",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 580,
            "name": "192.168.100.4",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0ca7b763eaf46c693",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0ca7b763eaf46c693",
                    "interfaceDisplayName": "eni-0ca7b763eaf46c693",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 491,
            "name": "192.168.102.0/24",
            "description": "Auto-generated from Device Aruba Orchestrator for 3.NE_lan0.20",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "3.NE_lan0.20",
                    "interfaceDisplayName": "3.NE_lan0.20",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 510,
            "name": "192.168.10.22",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-084045a3dfb4dade4",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-084045a3dfb4dade4",
                    "interfaceDisplayName": "eni-084045a3dfb4dade4",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 591,
            "name": "192.168.1.0/24",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-06679defb54a01fba",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-06679defb54a01fba",
                    "interfaceDisplayName": "subnet-06679defb54a01fba",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 564,
            "name": "192.168.11.0/24",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-02d2ece68295b8401",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-02d2ece68295b8401",
                    "interfaceDisplayName": "subnet-02d2ece68295b8401",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 583,
            "name": "192.168.11.57",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0e364c8bd07e1537e",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0e364c8bd07e1537e",
                    "interfaceDisplayName": "eni-0e364c8bd07e1537e",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 581,
            "name": "192.168.12.0/24",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-0bb6d34c87fb68e63",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0bb6d34c87fb68e63",
                    "interfaceDisplayName": "subnet-0bb6d34c87fb68e63",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 566,
            "name": "192.168.12.45",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-05da84d5485acf1e8",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-05da84d5485acf1e8",
                    "interfaceDisplayName": "eni-05da84d5485acf1e8",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 553,
            "name": "192.168.128.0/20",
            "description": "Auto-generated from Device Core-rtr-Dallas-ofc for fm-intf-3",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0b11af218bab764fb",
                    "interfaceDisplayName": "subnet-0b11af218bab764fb",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-003d217290db18273",
                    "interfaceDisplayName": "subnet-003d217290db18273",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-07b9f7957d69c9f25",
                    "interfaceDisplayName": "subnet-07b9f7957d69c9f25",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 24,
                    "deviceName": "Core-rtr-Dallas-ofc",
                    "deviceType": "ROUTER_SWITCH",
                    "interfaceName": "fm-intf-3",
                    "interfaceDisplayName": "fm-intf-3",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 615,
            "name": "192.168.131.101",
            "description": "Auto-generated from Device AWS-ACT-7176 for eni-0c853a58929540aa8",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0c853a58929540aa8",
                    "interfaceDisplayName": "eni-0c853a58929540aa8",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 548,
            "name": "192.168.131.16",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-04bcb4844257e34cd",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-04bcb4844257e34cd",
                    "interfaceDisplayName": "eni-04bcb4844257e34cd",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 541,
            "name": "192.168.137.57",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-09d6a3e1a8f4ab154",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-09d6a3e1a8f4ab154",
                    "interfaceDisplayName": "eni-09d6a3e1a8f4ab154",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 497,
            "name": "192.168.144.0/20",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-05680869a21aaaa02",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0439bb69353b6c067",
                    "interfaceDisplayName": "subnet-0439bb69353b6c067",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-05680869a21aaaa02",
                    "interfaceDisplayName": "subnet-05680869a21aaaa02",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 584,
            "name": "192.168.1.52",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-00737a0a693edf3cb",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-00737a0a693edf3cb",
                    "interfaceDisplayName": "eni-00737a0a693edf3cb",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 556,
            "name": "192.168.16.0/20",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-0fdcbb69488cb5086",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0b05489050ecd89c3",
                    "interfaceDisplayName": "subnet-0b05489050ecd89c3",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0fdcbb69488cb5086",
                    "interfaceDisplayName": "subnet-0fdcbb69488cb5086",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 585,
            "name": "192.168.1.73",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-006f4ba31d107c77b",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-006f4ba31d107c77b",
                    "interfaceDisplayName": "eni-006f4ba31d107c77b",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 487,
            "name": "192.168.200.0/23",
            "description": "Auto-generated from Device Aruba Orchestrator for 3.NE_wan0",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "0.NE_wan0",
                    "interfaceDisplayName": "0.NE_wan0",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "1.NE_wan0",
                    "interfaceDisplayName": "1.NE_wan0",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "3.NE_wan0",
                    "interfaceDisplayName": "3.NE_wan0",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 549,
            "name": "192.168.20.141",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-04f9170f610144fa5",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-04f9170f610144fa5",
                    "interfaceDisplayName": "eni-04f9170f610144fa5",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 468,
            "name": "192.168.2.0/24",
            "description": "Auto-generated from Device paloalto.firemon.xyz for ethernet1/2",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 4,
                    "deviceName": "paloalto.firemon.xyz",
                    "deviceType": "FIREWALL",
                    "interfaceName": "ethernet1/2",
                    "interfaceDisplayName": "ethernet1/2",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-076921fd1a502a2e8",
                    "interfaceDisplayName": "subnet-076921fd1a502a2e8",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 490,
            "name": "192.168.204.0/23",
            "description": "Auto-generated from Device Aruba Orchestrator for 3.NE_mgmt0",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "3.NE_mgmt0",
                    "interfaceDisplayName": "3.NE_mgmt0",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 486,
            "name": "192.168.204.0/24",
            "description": "Auto-generated from Device Aruba Orchestrator for 0.NE_mgmt0",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "0.NE_mgmt0",
                    "interfaceDisplayName": "0.NE_mgmt0",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "1.NE_mgmt0",
                    "interfaceDisplayName": "1.NE_mgmt0",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 485,
            "name": "192.168.208.0/24",
            "description": "Auto-generated from Device Aruba Orchestrator for 0.NE_lan1",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "0.NE_lan1",
                    "interfaceDisplayName": "0.NE_lan1",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "1.NE_lan1",
                    "interfaceDisplayName": "1.NE_lan1",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 489,
            "name": "192.168.209.0/24",
            "description": "Auto-generated from Device Aruba Orchestrator for 0.NE_lan1:v100",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "0.NE_lan1:v100",
                    "interfaceDisplayName": "0.NE_lan1:v100",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 488,
            "name": "192.168.209.0/30",
            "description": "Auto-generated from Device Aruba Orchestrator for 0.NE_lan0",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "1.NE_lan0",
                    "interfaceDisplayName": "1.NE_lan0",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "0.NE_lan0",
                    "interfaceDisplayName": "0.NE_lan0",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 484,
            "name": "192.168.209.4/30",
            "description": "Auto-generated from Device Aruba Orchestrator for 0.NE_lan2",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "0.NE_lan2",
                    "interfaceDisplayName": "0.NE_lan2",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 10,
                    "deviceName": "Aruba Orchestrator",
                    "deviceType": "FIREWALL",
                    "interfaceName": "1.NE_lan2",
                    "interfaceDisplayName": "1.NE_lan2",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 574,
            "name": "192.168.21.0/24",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-0e2e6da0f6bdb5028",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0e2e6da0f6bdb5028",
                    "interfaceDisplayName": "subnet-0e2e6da0f6bdb5028",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 570,
            "name": "192.168.21.85",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-073f02e9be95eb95d",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-073f02e9be95eb95d",
                    "interfaceDisplayName": "eni-073f02e9be95eb95d",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 577,
            "name": "192.168.2.201",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-003f680a491126945",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-003f680a491126945",
                    "interfaceDisplayName": "eni-003f680a491126945",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 592,
            "name": "192.168.22.0/24",
            "description": "Auto-generated from Device AWS-ACT-8687 for subnet-015c9554aa7ab067f",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-015c9554aa7ab067f",
                    "interfaceDisplayName": "subnet-015c9554aa7ab067f",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 590,
            "name": "192.168.22.215",
            "description": "Auto-generated from Device AWS-ACT-8687 for eni-0c400c3e5753bb0b1",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 17,
                    "deviceName": "AWS-ACT-8687",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-0c400c3e5753bb0b1",
                    "interfaceDisplayName": "eni-0c400c3e5753bb0b1",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 470,
            "name": "192.168.3.0/24",
            "description": "Auto-generated from Device fortigate.firemon.xyz for port1 (LAN)",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 5,
                    "deviceName": "fortigate.firemon.xyz",
                    "deviceType": "FIREWALL",
                    "interfaceName": "port1",
                    "interfaceDisplayName": "port1 (LAN)",
                    "interfaceTransparentMode": false
                },
                {
                    "deviceId": 24,
                    "deviceName": "Core-rtr-Dallas-ofc",
                    "deviceType": "ROUTER_SWITCH",
                    "interfaceName": "fm-intf-4",
                    "interfaceDisplayName": "fm-intf-4",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 606,
            "name": "192.168.64.0/21",
            "description": "Auto-generated from Device AWS-ACT-7176 for subnet-0e7757f9be528c106",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0e7757f9be528c106",
                    "interfaceDisplayName": "subnet-0e7757f9be528c106",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 629,
            "name": "192.168.69.11",
            "description": "Auto-generated from Device AWS-ACT-7176 for eni-047d49ab0a99334c0",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-047d49ab0a99334c0",
                    "interfaceDisplayName": "eni-047d49ab0a99334c0",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 594,
            "name": "192.168.70.28",
            "description": "Auto-generated from Device AWS-ACT-7176 for eni-07c9c5347ac76cadb",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-07c9c5347ac76cadb",
                    "interfaceDisplayName": "eni-07c9c5347ac76cadb",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 610,
            "name": "192.168.72.0/21",
            "description": "Auto-generated from Device AWS-ACT-7176 for subnet-0bf2d5292b4947e15",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "subnet-0bf2d5292b4947e15",
                    "interfaceDisplayName": "subnet-0bf2d5292b4947e15",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        },
        {
            "id": 597,
            "name": "192.168.74.160",
            "description": "Auto-generated from Device AWS-ACT-7176 for eni-03d3a01eb2e02f823",
            "domainId": 1,
            "domainName": "Enterprise",
            "excluded": false,
            "generated": false,
            "userEdited": false,
            "interfaceRefs": [
                {
                    "deviceId": 18,
                    "deviceName": "AWS-ACT-7176",
                    "deviceType": "CLOUD",
                    "interfaceName": "eni-03d3a01eb2e02f823",
                    "interfaceDisplayName": "eni-03d3a01eb2e02f823",
                    "interfaceTransparentMode": false
                }
            ],
            "type": "LAN"
        }
    ]
}
```

## List Interfaces
Request URL
https://demo01.firemon.xyz/securitymanager/api/siql/interface/paged-search?q=domain%7Bid%3D1%7D&page=0&pageSize=20&sort=displayName
Request Method
GET

### Example Response:
```
{
    "total": 398,
    "page": 0,
    "pageSize": 20,
    "count": 20,
    "results": [
        {
            "name": "0.NE_lan0",
            "displayName": "0.NE_lan0",
            "inactive": false,
            "tunnel": false,
            "transparentMode": false,
            "primaryAddress": {
                "type": "IPV4",
                "address": "192.168.209.1/30",
                "objectType": "NETWORK"
            },
            "secondaryAddresses": [],
            "id": "587c694b-22ed-43ed-8c20-0bc96262f8ec",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "networkSegmentDisplays": [
                "192.168.209.0/30"
            ],
            "zoneDisplays": [
                "VRF0",
                "INET2_Label",
                "Outside_2"
            ],
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan1",
            "displayName": "0.NE_lan1",
            "inactive": false,
            "tunnel": false,
            "transparentMode": false,
            "primaryAddress": {
                "type": "IPV4",
                "address": "192.168.208.9/24",
                "objectType": "NETWORK"
            },
            "secondaryAddresses": [],
            "id": "fc8b0a8d-d817-47d7-b09f-73ba2c31a8cf",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "networkSegmentDisplays": [
                "192.168.208.0/24"
            ],
            "zoneDisplays": [
                "VRF0",
                "Data_Label",
                "Internal_1"
            ],
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan10",
            "displayName": "0.NE_lan10",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "64a01052-5e79-400c-abaf-10d78f0e650f",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan11",
            "displayName": "0.NE_lan11",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "6792f26b-62d1-466a-a74e-f1ad06e47ad3",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan12",
            "displayName": "0.NE_lan12",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "483ea986-9bb0-4a41-909c-1ce793e70041",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan13",
            "displayName": "0.NE_lan13",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "439bfb23-b977-463a-b5f1-b9d7a1d3212b",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan14",
            "displayName": "0.NE_lan14",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "8ae0bd10-c3f3-402d-91d1-132e815c9a2d",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan15",
            "displayName": "0.NE_lan15",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "665684fa-2d3e-4a75-9b0d-3e5d410706ea",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan1:v100",
            "displayName": "0.NE_lan1:v100",
            "inactive": false,
            "tunnel": false,
            "transparentMode": false,
            "primaryAddress": {
                "type": "IPV4",
                "address": "192.168.209.7/24",
                "objectType": "NETWORK"
            },
            "secondaryAddresses": [],
            "id": "48eb3784-7b9e-4198-b9fa-bc21f4374a00",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "networkSegmentDisplays": [
                "192.168.209.0/24"
            ],
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan2",
            "displayName": "0.NE_lan2",
            "inactive": false,
            "tunnel": false,
            "transparentMode": false,
            "primaryAddress": {
                "type": "IPV4",
                "address": "192.168.209.6/30",
                "objectType": "NETWORK"
            },
            "secondaryAddresses": [],
            "id": "e0a7246a-d905-4854-a8b8-e3b2e5d7af25",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "networkSegmentDisplays": [
                "192.168.209.4/30"
            ],
            "zoneDisplays": [
                "VRF0",
                "Outside_2"
            ],
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan3",
            "displayName": "0.NE_lan3",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "20b2c22f-2434-4982-b886-b385f92a0ff4",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan4",
            "displayName": "0.NE_lan4",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "8f61b913-afb5-440f-bdd5-41025f16d24d",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan5",
            "displayName": "0.NE_lan5",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "80e4825f-b94e-4381-8d67-d93d2b4baa35",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan6",
            "displayName": "0.NE_lan6",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "b6f937ab-df63-43b7-a48e-b467b4e7c5f5",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan7",
            "displayName": "0.NE_lan7",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "65148123-fb37-4cc2-9528-41dc5b83b29f",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan8",
            "displayName": "0.NE_lan8",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "a153dce2-8842-49b2-975f-740f4fa5a8aa",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_lan9",
            "displayName": "0.NE_lan9",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "secondaryAddresses": [],
            "id": "2c8cc56e-f8cb-4f69-b126-a61d9668544e",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_mgmt0",
            "displayName": "0.NE_mgmt0",
            "inactive": false,
            "tunnel": false,
            "transparentMode": false,
            "primaryAddress": {
                "type": "IPV4",
                "address": "192.168.204.79/24",
                "objectType": "NETWORK"
            },
            "secondaryAddresses": [],
            "id": "99ecf650-56bf-47f9-aa34-1f3f0d602bd3",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "networkSegmentDisplays": [
                "192.168.204.0/24"
            ],
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_mgmt1",
            "displayName": "0.NE_mgmt1",
            "inactive": true,
            "tunnel": false,
            "transparentMode": false,
            "primaryAddress": {
                "type": "IPV4",
                "address": "169.254.0.1/16",
                "objectType": "NETWORK"
            },
            "secondaryAddresses": [],
            "id": "f6f90bbd-0907-4cd7-95e8-6584e32b44c5",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "ingressPolicies": [],
            "egressPolicies": []
        },
        {
            "name": "0.NE_wan0",
            "displayName": "0.NE_wan0",
            "inactive": false,
            "tunnel": false,
            "transparentMode": false,
            "primaryAddress": {
                "type": "IPV4",
                "address": "192.168.201.156/23",
                "objectType": "NETWORK"
            },
            "secondaryAddresses": [],
            "id": "aaf01bd3-7396-46b9-8637-d565116d132b",
            "deviceName": "Aruba Orchestrator",
            "deviceId": 10,
            "deviceType": "FIREWALL",
            "networkSegmentDisplays": [
                "192.168.200.0/23"
            ],
            "zoneDisplays": [
                "INET1_Label",
                "VRF0",
                "Outside_2"
            ],
            "ingressPolicies": [],
            "egressPolicies": []
        }
    ]
}
```

## Update Network Segment
Request URL
https://demo01.firemon.xyz/securitymanager/api/domain/1/networksegment/512
Request Method
PUT

### Example Payload:
```
{"id":512,"name":"10.0.16.0/20","description":"Auto-generated from Device AWS-ACT-8687 for subnet-0be87cc8e6fc46390","domainId":1,"domainName":"Enterprise","excluded":false,"generated":false,"userEdited":false,"interfaceRefs":[{"deviceId":17,"deviceName":"AWS-ACT-8687","deviceType":"CLOUD","interfaceName":"subnet-0debe7567def7ecbf","interfaceDisplayName":"subnet-0debe7567def7ecbf","interfaceTransparentMode":false},{"deviceId":17,"deviceName":"AWS-ACT-8687","deviceType":"CLOUD","interfaceName":"subnet-0be87cc8e6fc46390","interfaceDisplayName":"subnet-0be87cc8e6fc46390","interfaceTransparentMode":false}],"type":"LAN","hexColor":"#B8BEBF","zoneName":"DMZ","zoneId":13}
```

## Create Compliance Zone

Request URL
https://demo01.firemon.xyz/securitymanager/api/domain/1/zone
Request Method
POST

### Example Payload:
```{"hexColor":"#B8BEBF","name":"NewZoneName","description":""}
```
### Example Response:
````
{
    "id": 18,
    "name": "NewZoneName",
    "description": "",
    "domainId": 1,
    "domainName": "Enterprise",
    "system": false,
    "virtual": false,
    "hexColor": "#B8BEBF",
    "x": 0,
    "y": 0,
    "width": 0,
    "height": 0
}
```
