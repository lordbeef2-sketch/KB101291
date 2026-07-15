# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Packet Example/PacketUsage.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Packet Example/PacketUsage.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Packet Example/PacketUsage.kerml
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
