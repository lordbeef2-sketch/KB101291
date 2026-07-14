# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Mass Roll-up Example/MassRollup_1.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Mass Roll-up Example/MassRollup_1.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Mass Roll-up Example/MassRollup_1.kerml
- source_bytes: 267
- source_sha256: `699c55b324e017fba453b689826ba9a4804adf3396fa24d70db90d7900eb9f14`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package MassRollup_1 {
	private import NumericalFunctions::*;

	class MassedThing {
		feature mass : ScalarValues::Real;	
		composite subcomponents: MassedThing[0..*];

		feature totalMass : ScalarValues::Real = 
			mass + sum(subcomponents.totalMass);
	}
}
````
