# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Packet Example/PacketUsage.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Packet Example/PacketUsage.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Packet Example/PacketUsage.kerml
- source_bytes: 378
- source_sha256: `9e940d566017af873a6aacd4add472e9f39ffac5d32fa86c2ed9b6c1be55e355`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
private import Packets::*;
private import ScalarValues::Real;
package 'Packet Usage' {
	
	feature packet1: 'Thermal Data Packet';
	feature packet2: 'Thermal Data Packet';
	feature packet3: 'Thermal Data Packet' {
		feature 'special data field' redefines 'packet data field'{
			feature :>> 'user data field' {
				feature 'special data': Real;
			}
		}
	}
	
}
	

````
