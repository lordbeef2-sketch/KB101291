# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/validation/12-Dependency Relationships/12b-Allocation-1.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/validation/12-Dependency Relationships/12b-Allocation-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/validation/12-Dependency Relationships/12b-Allocation-1.sysml
- source_bytes: 1373
- source_sha256: `82149b94a62645eeaf8a560f866085b216fff19043c3d45fb302272fa812a476`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '12b-Allocation-1' {
	private import SI::*;
	private import RequirementModel::*;
	private import LogicalModel::*;
	private import PhysicalModel::*;
	
	package RequirementModel {
		requirement torqueGeneration {
			subject generator: TorqueGenerator;
			require constraint { 
				 generator.generateTorque.torque > 0.0 [N*m]
			}
		}
	}
	
	package LogicalModel {
		action def GenerateTorque { out torque :> ISQ::torque; }
		
		part def LogicalElement;
		part def TorqueGenerator :> LogicalElement {
			perform action generateTorque : GenerateTorque;
		}	
		
		action providePower {
			action generateTorque : GenerateTorque;
		}
		
		part torqueGenerator : TorqueGenerator {
			perform providePower.generateTorque :>> generateTorque;
		}
		
		satisfy torqueGeneration by torqueGenerator;			
	}
	
	package PhysicalModel {
		part def PhysicalElement;
		part def PowerTrain :> PhysicalElement;
		
		part powerTrain : PowerTrain {
			part engine {
				perform providePower.generateTorque;
			}
		}
	}
	
	allocation def LogicalToPhysical {
		end logical : LogicalElement;
		end physical : PhysicalElement;
	}
	
	allocation torqueGenAlloc : LogicalToPhysical 
		allocate logical ::> torqueGenerator to physical ::> powerTrain {
			
		allocate torqueGenerator.generateTorque to powerTrain.engine.generateTorque;		
	}
}
````
