# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Mass Roll-up Example/Vehicles_3.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Mass Roll-up Example/Vehicles_3.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Mass Roll-up Example/Vehicles_3.kerml
- source_bytes: 984
- source_sha256: `28d253d4b493f19a16ae37ca6f908d63a21ffd7aeb87c0cb186bc6e14d207c78`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Vehicles_3 {
	private import ScalarValues::*;
	private import MassRollup_2::*;
	
	class CarPart specializes MassedThing {			
		feature serialNumber: String;
		feature m redefines MassedThing::mass;
		
		feature subparts redefines carParts;	
	}
	
	composite feature carParts: CarPart[0..*] subsets massedThings;
	
	feature vehicle subsets carParts {	
		feature vin redefines serialNumber;
		
		feature redefines engine;
		feature redefines transmission;
	}
	
	composite feature engine subsets carParts {
		//...
	}
	
	composite feature transmission subsets carParts {
		//...
	}

	// Example usage
	
	private import SI::*;
	feature v: vehicle {
		feature m redefines CarPart::m = 1000;
		composite :>> engine = e;
		composite :>> transmission = t;
	}
	
	feature e :> engine {
		feature m redefines CarPart::m = 100;
	}
	
	feature t :> transmission {
		feature m redefines CarPart::m = 50;
	}
	
	// v.totalMass evaluates to 1150.0
}
````
