# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Packet Example/Packets.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Packet Example/Packets.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Packet Example/Packets.sysml
- source_bytes: 1030
- source_sha256: `4e66a98b8ec7d49f486a0401e57ea1c0dd9472cf3a88df6cd9c6ed3345ad8194`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package Packets {
	private import ScalarValues::*;
	private import Time::DateTime;
	
	attribute 'packet header' { }
	
	attribute 'packet data field' {	
		attribute 'packet secondary header' redefines 'packet header';
		attribute 'user data field';
	}
	
	part def 'Data Packet' {
		attribute 'packet primary header' redefines 'packet header' {
			attribute 'packet version number': Integer;
			attribute 'packet identification': String;
			attribute 'packet data length': Integer;
		}
		attribute redefines 'packet data field';
	}
	
	part def 'Thermal Data Packet' :> 'Data Packet' {
		attribute 'packet data field' redefines Packets::'packet data field'{
			attribute 'packet secondary header' redefines 'packet header' {
				attribute 'packet timestamp': DateTime;
				attribute 'telemetry packet type': String;
			}
			
			attribute 'user data field' redefines Packets::'packet data field'::'user data field' {
				attribute timestamp: DateTime;
				attribute temperature: Real;
			}
		}
	}
	
}
````
