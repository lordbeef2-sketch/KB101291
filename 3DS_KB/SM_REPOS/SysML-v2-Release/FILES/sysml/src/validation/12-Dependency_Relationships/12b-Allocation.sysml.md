# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/validation/12-Dependency Relationships/12b-Allocation.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/validation/12-Dependency Relationships/12b-Allocation.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/validation/12-Dependency Relationships/12b-Allocation.sysml
- source_bytes: 518
- source_sha256: `49bee01e14200a73054fcac30424903ad9f30c99c8d24fa5a9008f76da21030d`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '12b-Allocation' {
	private import LogicalModel::*;
	private import PhysicalModel::*;
	
	package LogicalModel {
		action providePower {
			action generateTorque;
		}
		
		part torqueGenerator {
			perform providePower.generateTorque;
		}
	}
	
	package PhysicalModel {
		part powerTrain {
			part engine {
				perform providePower.generateTorque;
			}
		}
	}
	
	allocate torqueGenerator to powerTrain {
		allocate torqueGenerator.generateTorque to powerTrain.engine.generateTorque;
	}
}
````
