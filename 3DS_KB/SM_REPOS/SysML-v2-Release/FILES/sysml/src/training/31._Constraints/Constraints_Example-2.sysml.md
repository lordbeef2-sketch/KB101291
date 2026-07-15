# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/31. Constraints/Constraints Example-2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/31. Constraints/Constraints Example-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/31. Constraints/Constraints Example-2.sysml
- source_bytes: 702
- source_sha256: `2a1c607f7e23afefc17d0af1f3b17604454b7f63e78f51654c654d2a72b68ff1`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Constraints Example-2' {
	private import ISQ::*;
	private import SI::*;
	private import NumericalFunctions::*;
	
	part def Engine;
	part def Transmission;
	
	constraint def MassConstraint {
		attribute partMasses : MassValue[0..*];
		attribute massLimit : MassValue;
			
		sum(partMasses) <= massLimit
	}
	
	part def Vehicle {
		constraint massConstraint : MassConstraint {
			redefines partMasses = (chassisMass, engine.mass, transmission.mass);
			redefines massLimit = 2500[kg];
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
