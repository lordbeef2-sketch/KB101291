# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/31. Constraints/Constraint Assertions-1.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/31. Constraints/Constraint Assertions-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/31. Constraints/Constraint Assertions-1.sysml
- source_bytes: 684
- source_sha256: `6bdcf5d9a99e60fe17b1705aaaaaa0a06f8af3c6812fcd247a8fe2d61e34081c`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Constraint Assertions-1' {
	private import ISQ::*;
	private import SI::*;
	private import NumericalFunctions::*;
	
	part def Engine;
	part def Transmission;
	
	constraint def MassConstraint {
		in partMasses : MassValue[0..*];
		in massLimit : MassValue;
			
		sum(partMasses) <= massLimit
	}
	
	part def Vehicle {
		assert constraint massConstraint : MassConstraint {
			in partMasses = (chassisMass, engine.mass, transmission.mass);
			in massLimit = 2500[kg];
		}
		
		attribute chassisMass : MassValue;
		
		part engine : Engine {
			attribute mass : MassValue;
		}
		
		part transmission : Engine {
			attribute mass : MassValue;
		}
	}	
}
````
