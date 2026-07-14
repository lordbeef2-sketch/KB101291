# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Mass Roll-up Example/Vehicles_2.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Mass Roll-up Example/Vehicles_2.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Mass Roll-up Example/Vehicles_2.kerml
- source_bytes: 850
- source_sha256: `f52568111c169b597ab1ae17b9f36b2915371e04ed5cff0c1bcefa2df4feb13d`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Vehicles_2 {
	private import ScalarValues::String;
	private import MassRollup_1::*;
	
	class CarPart specializes MassedThing {		
		feature serialNumber: String;
		feature m redefines mass;
		
		composite subparts: CarPart[0..*] redefines subcomponents;
	}
	
	feature vehicle: CarPart {	
		feature vin redefines serialNumber;
		
		composite engine: CarPart subsets subparts {
			//...
		}
		
		composite transmission: CarPart subsets subparts {
			//...
		}
	}
	
	// Example usage
	
	private import SI::*;
	feature v: vehicle {
		feature m redefines CarPart::m = 1000;
		composite engine redefines vehicle::engine {
			feature m redefines CarPart::m = 100;
		}
		composite transmission redefines vehicle::transmission {
			feature m redefines CarPart::m = 50;
		}
	}
	
	// v.totalMass evaluates to 1150.0
}
````
