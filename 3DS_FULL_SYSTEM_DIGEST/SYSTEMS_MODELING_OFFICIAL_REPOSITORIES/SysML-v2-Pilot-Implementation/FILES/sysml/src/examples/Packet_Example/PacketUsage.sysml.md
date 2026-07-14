# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Packet Example/PacketUsage.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Packet Example/PacketUsage.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Packet Example/PacketUsage.sysml
- source_bytes: 382
- source_sha256: `7cecc1bd583948de9beb2cbc3f3cbe903355e6cedf729f9eb10ae72529aa9be3`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Packet Usage' {
	public import Packets::*;
	private import ScalarValues::Real;
	
	part packet1: 'Thermal Data Packet';
	part packet2: 'Thermal Data Packet';
	part packet3: 'Thermal Data Packet' {
		attribute 'special data field' redefines 'packet data field'{
			attribute redefines 'user data field' {
				attribute 'special data': Real;
			}
		}
	}
	
}
	

````
