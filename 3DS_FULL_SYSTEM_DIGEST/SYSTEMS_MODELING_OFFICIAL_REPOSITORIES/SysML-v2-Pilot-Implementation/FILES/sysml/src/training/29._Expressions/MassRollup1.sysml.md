# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/29. Expressions/MassRollup1.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/29. Expressions/MassRollup1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/29. Expressions/MassRollup1.sysml
- source_bytes: 421
- source_sha256: `fb10f788903d2583ef865e085f08209a941d261d2311784c730415e7e45fc64e`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package MassRollup1 {
	private import NumericalFunctions::*;
	
	part def MassedThing {
		attribute simpleMass :> ISQ::mass; 
		attribute totalMass :> ISQ::mass;
	}
	
	part simpleThing : MassedThing {
		attribute :>> totalMass = simpleMass;
	}
	
	part compositeThing : MassedThing {
		part subcomponents: MassedThing[*];		
		attribute :>> totalMass =
			simpleMass + sum(subcomponents.totalMass); 
	}
	
}
````
