# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/27. Occurrences/Interaction Example-2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/27. Occurrences/Interaction Example-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/27. Occurrences/Interaction Example-2.sysml
- source_bytes: 833
- source_sha256: `1511ea366b29a3dc6dfcd3ef8679d712453c311f1b8535cb350d98ce7592ed3e`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Interaction Example-2' {
	private import 'Event Occurrence Example'::*;
	
	item def SetSpeed;
	item def SensedSpeed;
	item def FuelCommand;
	
	occurrence def CruiseControlInteraction {
		
		ref part driver : Driver {
			event setSpeedMessage.sourceEvent;
		}
		
		ref part vehicle : Vehicle {
			part cruiseController : CruiseController {
				event setSpeedMessage.targetEvent;		
				then event sensedSpeedMessage.targetEvent;		
				then event fuelCommandMessage.sourceEvent;
			}
			
			part speedometer : Speedometer {
				event sensedSpeedMessage.sourceEvent;
			}
			
			part engine : Engine {
				event fuelCommandMessage.targetEvent;
			}
		}
		
		message setSpeedMessage of SetSpeed;	
		then message sensedSpeedMessage of SensedSpeed;
		message fuelCommandMessage of FuelCommand;
	}
}
````
