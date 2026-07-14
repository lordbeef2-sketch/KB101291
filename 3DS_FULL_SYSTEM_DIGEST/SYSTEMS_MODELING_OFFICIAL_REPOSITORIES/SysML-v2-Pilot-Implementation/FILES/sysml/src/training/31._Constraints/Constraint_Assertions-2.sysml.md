# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/31. Constraints/Constraint Assertions-2.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/31. Constraints/Constraint Assertions-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/31. Constraints/Constraint Assertions-2.sysml
- source_bytes: 775
- source_sha256: `9d6560d9ce5798dcf5b10a4672c0c6aa7403eb2b88657ca935563c6d1ee9ab12`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Constraint Assertions-2' {
	private import ISQ::*;
	private import SI::*;
	private import NumericalFunctions::*;
	
	part def Engine;
	part def Transmission;
	
	constraint def MassConstraint {
		in partMasses : MassValue[0..*];
		in massLimit : MassValue;
	}
	
	constraint massConstraint : MassConstraint {
		in partMasses : MassValue[0..*];
		in massLimit : MassValue;
			
		sum(partMasses) <= massLimit
	}
	
	part def Vehicle {
		assert massConstraint {
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
