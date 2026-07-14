# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/27. Occurrences/Event Occurrence Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/27. Occurrences/Event Occurrence Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/27. Occurrences/Event Occurrence Example.sysml
- source_bytes: 601
- source_sha256: `3e3bad50fd49043a5a030ff6b4365a56e85f911aa6c2bb5ecd65c39e5b4f2cf7`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Event Occurrence Example' {	
	part def Driver;
	part def CruiseController;
	part def Speedometer;
	part def Engine;
	part def Vehicle;
	
	part driver : Driver {
		event occurrence setSpeedSent;
	}
	
	part vehicle : Vehicle {
	
		part cruiseController : CruiseController {
			event occurrence setSpeedReceived;		
			then event occurrence sensedSpeedReceived;		
			then event occurrence fuelCommandSent;
		}
		
		part speedometer : Speedometer {
			event occurrence sensedSpeedSent;
		}
		
		part engine : Engine {
			event occurrence fuelCommandReceived;
		}
	
	}
}
````
