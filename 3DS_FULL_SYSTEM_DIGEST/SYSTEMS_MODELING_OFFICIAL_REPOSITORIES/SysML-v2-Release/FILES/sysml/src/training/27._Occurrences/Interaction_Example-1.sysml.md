# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/27. Occurrences/Interaction Example-1.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/27. Occurrences/Interaction Example-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/27. Occurrences/Interaction Example-1.sysml
- source_bytes: 717
- source_sha256: `8406d1e3968e6cc47c6e87134616fc4b9465f7dcf516828955ca350b7aed022d`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Interaction Example-1' {
	public import 'Event Occurrence Example'::*;
	
	item def SetSpeed;
	item def SensedSpeed;
	item def FuelCommand;
	
	occurrence def CruiseControlInteraction {		
		ref part :>> driver;		
		ref part :>> vehicle;
		
		message setSpeedMessage of SetSpeed 
			from driver.setSpeedSent to vehicle.cruiseController.setSpeedReceived;
			
		message sensedSpeedMessage of SensedSpeed 
			from vehicle.speedometer.sensedSpeedSent to vehicle.cruiseController.sensedSpeedReceived;
			
		message fuelCommandMessage of FuelCommand 
			from vehicle.cruiseController.fuelCommandSent to vehicle.engine.fuelCommandReceived;
		
		first setSpeedMessage then sensedSpeedMessage;
	}
}
````
