# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/38. Allocation/Allocation Usage Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/38. Allocation/Allocation Usage Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/38. Allocation/Allocation Usage Example.sysml
- source_bytes: 716
- source_sha256: `8c982de250d0586620964a516796553ea284ebb4c593eb582aa8a2db6ae745e6`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Allocation Usage Example' {
	package LogicalModel {
		action def ProvidePower;
		action def GenerateTorque;
		
		part def TorqueGenerator;
		
		action providePower : ProvidePower {
			action generateTorque : GenerateTorque;
		}
		
		part torqueGenerator : TorqueGenerator {
			perform providePower.generateTorque;
		}
	}
	
	package PhysicalModel {
		private import LogicalModel::*;
	
		part def PowerTrain;
		part def Engine;
		
		part powerTrain : PowerTrain {
			part engine : Engine {
				perform providePower.generateTorque;
			}
		}
		
		allocate torqueGenerator to powerTrain {
			allocate torqueGenerator.generateTorque to powerTrain.engine.generateTorque;
		}
	}
	
}
````
