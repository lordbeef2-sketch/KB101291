# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/31. Constraints/Derivation Constraints.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/31. Constraints/Derivation Constraints.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/31. Constraints/Derivation Constraints.sysml
- source_bytes: 637
- source_sha256: `8e70fc943eb8efe776639ffbf7187a6026ea0a4614c65ca5d6a289ddc3fffc14`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Derivation Constraints' {
	private import SI::*;
	private import 'Constraints Example-1'::*;
	
	part vehicle1 : Vehicle {
		attribute totalMass : MassValue;			
		assert constraint {totalMass == chassisMass + engine.mass + transmission.mass}	
	}
	
	part vehicle2 : Vehicle {
		attribute totalMass : MassValue = chassisMass + engine.mass + transmission.mass;
	}
	
	constraint def Dynamics {
		in mass: MassValue;
		in initialSpeed : SpeedValue;
		in finalSpeed : SpeedValue;
		in deltaT : TimeValue;
		in force : ForceValue;

		force * deltaT == mass * (finalSpeed - initialSpeed) and
		mass > 0[kg]
	}
	
}
````
