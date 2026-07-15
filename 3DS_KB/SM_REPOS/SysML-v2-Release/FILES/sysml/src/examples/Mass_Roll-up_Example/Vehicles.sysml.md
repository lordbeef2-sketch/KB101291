# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Mass Roll-up Example/Vehicles.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Mass Roll-up Example/Vehicles.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Mass Roll-up Example/Vehicles.sysml
- source_bytes: 719
- source_sha256: `99265bff25c1cc4bf9327f0292dd9045d48d6c9597e405775e8e238f00831c31`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package VehicleMasses {
	private import ScalarValues::*;
	private import MassRollup::*;
	
	part def CarPart :> MassedThing {			
		attribute serialNumber: String;
	}
	
	part car: CarPart :> compositeThing {	
		attribute vin redefines serialNumber;
		
		part carParts: CarPart[*] redefines subcomponents;
		
		part engine :> simpleThing, carParts {
			//...
		}
		
		part transmission :> simpleThing, carParts {
			//...
		}
	}

	// Example usage
	private import SI::*;	
	part c :> car {
		redefines mass = 1000 [kg];
		part redefines engine {
			redefines mass = 100 [kg];
		}
		
		part redefines transmission {
			redefines mass = 50 [kg];
		}	
	}
	
	// c.totalMass --> 1150.0 [kg]
}
````
