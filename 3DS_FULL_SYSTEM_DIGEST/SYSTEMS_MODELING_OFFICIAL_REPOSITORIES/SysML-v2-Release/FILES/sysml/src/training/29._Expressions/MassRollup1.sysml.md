# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/29. Expressions/MassRollup1.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/29. Expressions/MassRollup1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/29. Expressions/MassRollup1.sysml
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
