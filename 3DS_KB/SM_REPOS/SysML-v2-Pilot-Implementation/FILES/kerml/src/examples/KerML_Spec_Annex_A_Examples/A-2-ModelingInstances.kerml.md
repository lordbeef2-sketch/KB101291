# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/KerML Spec Annex A Examples/A-2-ModelingInstances.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/KerML Spec Annex A Examples/A-2-ModelingInstances.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/KerML Spec Annex A Examples/A-2-ModelingInstances.kerml
- source_bytes: 740
- source_sha256: `d7022eb67c25572bd93cb3074f40cc02fd490c12c52f04ac0c45585eb25c834d`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package ModelingInstances {
	doc
	/* 
	 */

	classifier Vehicle;
	classifier Bicycle specializes Vehicle;
	classifier MyBike [1] specializes Bicycle;
	classifier YourBike [1] specializes Bicycle disjoint from MyBike;
}

package ModelingInstancesWithAtoms {
	doc
	/* 
	 */

	private import Atoms::atom;

	classifier Vehicle;
	classifier Bicycle specializes Vehicle;

	#atom
	classifier MyBike specializes Bicycle;
	#atom
	classifier YourBike specializes Bicycle;

	/* Assigning feature values. */

	classifier Garage {
		feature stores : Bicycle [*];
	}
	classifier OurBicycle unions MyBike, YourBike;

	#atom
	classifier OurGarage specializes Garage {
		feature redefines stores : OurBicycle [2];
	}
}

````
