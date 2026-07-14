# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/29. Expressions/MassRollup2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/29. Expressions/MassRollup2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/29. Expressions/MassRollup2.sysml
- source_bytes: 560
- source_sha256: `8af5b03e4930331b7ef53108f06973167735327f52600c85236d82404c0f8c7f`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package MassRollup2 {
	private import NumericalFunctions::*;
	
	part def MassedThing {
		attribute simpleMass :> ISQ::mass; 
		attribute totalMass :> ISQ::mass default simpleMass;
	}
	
	part compositeThing : MassedThing {
		part subcomponents: MassedThing[*];		
		attribute :>> totalMass default
			simpleMass + sum(subcomponents.totalMass); 
	}
	
	part filteredMassThing :> compositeThing {
		attribute minMass :> ISQ::mass;		
		attribute :>> totalMass =
			simpleMass + sum(subcomponents.totalMass.?{in p:>ISQ::mass; p >= minMass});
	}

}
````
