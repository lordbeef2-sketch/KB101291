# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/32. Requirements/Requirement Groups.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/32. Requirements/Requirement Groups.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/32. Requirements/Requirement Groups.sysml
- source_bytes: 752
- source_sha256: `805a4df68510228f71b479706af54eca6fc8cf2a54788a885acd2238557b62cf`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Requirement Groups' {
	private import 'Requirement Definitions'::*;
	private import 'Requirement Usages'::*;
	
	part def Engine {
		port clutchPort: ClutchPort;
		perform action generateTorque: GenerateTorque;
	}
	
	requirement vehicleSpecification {
		doc /* Overall vehicle requirements group */
		
		subject vehicle : Vehicle;
		
		require fullVehicleMassLimit;
		require emptyVehicleMassLimit;
	}
	
	requirement engineSpecification {
		doc /* Engine power requirements group */
		
		subject engine : Engine;
		
		requirement drivePowerInterface : DrivePowerInterface {
			subject = engine.clutchPort;
		}
		
		requirement torqueGeneration : TorqueGeneration {
			subject = engine.generateTorque;	
		}
	}
	
}
````
