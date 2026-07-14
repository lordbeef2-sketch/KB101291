# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/29. Expressions/Car Mass Rollup Example 2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/29. Expressions/Car Mass Rollup Example 2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/29. Expressions/Car Mass Rollup Example 2.sysml
- source_bytes: 712
- source_sha256: `7e40a50232b9f1c263f9da1d3e0d5a79a4c785dccb49d26abcb6c465ff0b730e`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Car Mass Rollup 1' {
	private import ScalarValues::*;
	private import MassRollup2::*;
	
	part def CarPart :> MassedThing {			
		attribute serialNumber: String;
	}
	
	part car: CarPart :> compositeThing {	
		attribute vin :>> serialNumber;
		
		part carParts: CarPart[*] :>> subcomponents;
		
		part engine :> carParts {
			//...
		}
		
		part transmission :> carParts {
			//...
		}
	}

	// Example usage
	
	private import SI::kg;
	part c :> car {
		attribute :>> simpleMass = 1000[kg];
		part :>> engine {
			attribute :>> simpleMass = 100[kg];
		}
		
		part redefines transmission {
			attribute :>> simpleMass = 50[kg];
		}	
	}
	
	// c::totalMass --> 1150.0[kg]
}
````
