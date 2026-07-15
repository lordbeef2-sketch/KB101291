# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/32. Requirements/Requirement Usages.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/32. Requirements/Requirement Usages.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/32. Requirements/Requirement Usages.sysml
- source_bytes: 624
- source_sha256: `da3e5c487abc484aa8a66cd266486db2ed25e571030900e9575a850bd6226bd7`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Requirement Usages' {
	private import SI::*;
	private import 'Requirement Definitions'::*;
	
	requirement <'1.1'> fullVehicleMassLimit : VehicleMassLimitationRequirement {
		subject vehicle : Vehicle;
		attribute :>> massReqd = 2000[kg];
		
		assume constraint {
			doc /* Full tank is full. */
			vehicle.fuelMass == vehicle.fuelFullMass
		}
	}
	
	requirement <'1.2'> emptyVehicleMassLimit : VehicleMassLimitationRequirement {
		subject vehicle : Vehicle;
		attribute :>> massReqd = 1500[kg];
		
		assume constraint {
			doc /* Full tank is empty. */
			vehicle.fuelMass == 0[kg]
		}
	}
	
}
````
