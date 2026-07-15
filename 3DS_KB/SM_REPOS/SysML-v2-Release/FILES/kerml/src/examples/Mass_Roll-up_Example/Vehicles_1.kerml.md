# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Mass Roll-up Example/Vehicles_1.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Mass Roll-up Example/Vehicles_1.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Mass Roll-up Example/Vehicles_1.kerml
- source_bytes: 930
- source_sha256: `97b8bf866720e4c52bd07d0d3878f166dbc10c09c9a7771c45b4d4518eb0f8e3`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Vehicles_1 {
	private import ScalarValues::String;
	private import MassRollup_1::*;

	class Vehicle specializes MassedThing {
		feature vin: String;
		feature m redefines mass;
	
		composite engine: Engine subsets subcomponents;
		composite transmission: Transmission subsets subcomponents;
	}
	
	class Engine specializes MassedThing {
		feature serialNumber: String;
		feature m redefines mass;
		
		// ...
	}
	
	class Transmission specializes MassedThing {
		feature serialNumber: String;
		feature m redefines mass;
		
		// ...
	}
	
	// Example usage
	
	private import SI::*;
	feature v: Vehicle {
		feature m redefines Vehicle::m = 1000;
		composite engine redefines Vehicle::engine {
			feature m redefines Engine::m = 100;
		}
		composite transmission redefines Vehicle::transmission {
			feature m redefines Transmission::m = 50;
		}
	}

	// v.totalMass evaluates to 1150.0
}
````
