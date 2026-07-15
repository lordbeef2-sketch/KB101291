# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/validation/07-Variant Configuration/7a-Variant Configuration - General Concept.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/validation/07-Variant Configuration/7a-Variant Configuration - General Concept.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/validation/07-Variant Configuration/7a-Variant Configuration - General Concept.sysml
- source_bytes: 1033
- source_sha256: `77323db9654a1bc3798539c36d0a9b6edc0be012a9e173b4e3bc36918c1c52dd`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '7a-Variant Configuration - General Concept' {
	
	part def Vehicle;
	
	part part1;
	part part2;
	part part3;
	part part4;
	part part5;
	part part6;
	
	abstract part anyVehicleConfig : Vehicle {
		
		variation part subsystemA {
			variant part subsystem1 {
				part :>> part1;
				part :>> part2;
			}
			variant part subsystem2 {
				part :>> part2;
				part :>> part3;
			}
		}

		variation part subsystemB {
			variant part subsystem3 {
				part :>> part4;
				part :>> part5;
			}
			variant part subsystem4 {
				part :>> part5;
				part :>> part6;
			}
		}
		
		assert constraint {
			subsystemA != subsystemA::subsystem2 | 
			subsystemB == subsystemB::subsystem3
		}
		
	}
	
	part vehicleConfigA :> anyVehicleConfig {		
		part :>> subsystemA = subsystemA::subsystem1;
		part :>> subsystemB = subsystemB::subsystem3;
	}
	
	part VehicleConfigB :> anyVehicleConfig {
		part :>> subsystemA = subsystemA::subsystem2;
		part :>> subsystemB = subsystemB::subsystem3;
	}
	
}
````
