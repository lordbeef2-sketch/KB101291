# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Mass Roll-up Example/MassRollup_2.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Mass Roll-up Example/MassRollup_2.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Mass Roll-up Example/MassRollup_2.kerml
- source_bytes: 346
- source_sha256: `27b90bb2fa35b928746a3a3d21c05c642b7db42f23cb76475356aff7f5b3ee0d`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package MassRollup_2 {
	private import NumericalFunctions::*;
	private import ISQ::*;
	
	class MassedThing {
		feature mass : ScalarValues::Real; 
		feature totalMass : ScalarValues::Real =
			mass + sum(subcomponents.totalMass);
			
		feature subcomponents redefines massedThings;	
	}
	
	feature massedThings: MassedThing[0..*];

}
````
