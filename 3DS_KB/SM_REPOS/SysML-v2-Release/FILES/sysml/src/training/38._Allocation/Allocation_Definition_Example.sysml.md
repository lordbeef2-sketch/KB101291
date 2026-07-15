# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/38. Allocation/Allocation Definition Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/38. Allocation/Allocation Definition Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/38. Allocation/Allocation Definition Example.sysml
- source_bytes: 864
- source_sha256: `922da707cd931fb6a9eebed2b1282413453798398f45c4be578b7389dcbdb817`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Allocation Definition Example' {
	package LogicalModel {
		action def ProvidePower;
		action def GenerateTorque;
		
		part def LogicalElement;
		part def TorqueGenerator :> LogicalElement;
		
		action providePower : ProvidePower {
			action generateTorque : GenerateTorque;
		}
		
		part torqueGenerator : TorqueGenerator {
			perform providePower.generateTorque;
		}
		
	}
	
	package PhysicalModel {
		private import LogicalModel::*;
		
		part def PhysicalElement;
		part def PowerTrain :> PhysicalElement;
		
		part powerTrain : PowerTrain {
			part engine {
				perform providePower.generateTorque;
			}
		}
	
		allocation def LogicalToPhysical {
			end logical : LogicalElement;
			end physical : PhysicalElement;
		}
		
		allocation torqueGenAlloc : LogicalToPhysical allocate torqueGenerator to powerTrain;
	}	
}
````
