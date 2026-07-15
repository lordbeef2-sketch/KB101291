# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Packet Example/Packets.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Packet Example/Packets.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Packet Example/Packets.kerml
- source_bytes: 1000
- source_sha256: `eb786dc3b12e97b51c1c34a70bb0dba0a3e2e12b3de6e5171a01ba869481e267`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
private import ScalarValues::*;
private import Time::DateTime;
package Packets {
	
	feature 'packet header' { }
	
	feature 'packet data field' {	
		feature 'packet secondary header' redefines 'packet header';
		feature 'user data field';
	}
	
	class 'Data Packet' { 
		feature 'packet primary header' redefines 'packet header' {
			feature 'packet version number': Integer;
			feature 'packet identification': String;
			feature 'packet data length': Integer;
		}
		feature redefines 'packet data field';
	}
	
	class 'Thermal Data Packet' specializes 'Data Packet' {
		feature 'packet data field' redefines Packets::'packet data field'{
			feature 'packet secondary header' redefines 'packet header' {
				feature 'packet timestamp': DateTime;
				feature 'telemetry packet type': String;
			}
			
			feature 'user data field' redefines Packets::'packet data field'::'user data field' {
				feature timestamp: DateTime;
				feature temperature: Real;
			}
		}
	}
	
}
````
