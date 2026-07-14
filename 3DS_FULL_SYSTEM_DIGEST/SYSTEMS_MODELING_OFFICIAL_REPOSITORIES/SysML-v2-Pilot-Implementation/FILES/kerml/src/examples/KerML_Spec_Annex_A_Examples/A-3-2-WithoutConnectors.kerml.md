# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/KerML Spec Annex A Examples/A-3-2-WithoutConnectors.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/KerML Spec Annex A Examples/A-3-2-WithoutConnectors.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/KerML Spec Annex A Examples/A-3-2-WithoutConnectors.kerml
- source_bytes: 609
- source_sha256: `3a36d857d9b95ab2fcace2435a6831a42dfedc16754edd8d3254d5884f27b62a`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml

package WithoutConnectorsModelToBeExecuted {
	doc
	/* 
	 */

	classifier Bicycle {
		feature rollsOn : Wheel [2];
		feature holdsWheel : BikeFork [*];
	}
	classifier Wheel;
	classifier BikeFork;
}

package WithoutConnectorsExecution {
	doc
	/* 
	 */

	private import Atoms::*;
	private import WithoutConnectorsModelToBeExecuted::*;

	#atom
	classifier MyWheel1 specializes Wheel;
	#atom
	classifier MyWheel2 specializes Wheel;

	classifier MyWheel unions MyWheel1, MyWheel2;

	#atom
	classifier MyBike specializes Bicycle {
		feature redefines rollsOn : MyWheel;
	}
}




````
