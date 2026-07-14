# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/25. Transitions/Transition Actions.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/25. Transitions/Transition Actions.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/25. Transitions/Transition Actions.sysml
- source_bytes: 965
- source_sha256: `5e695884b6a9703d40885aa47e692eeecefc7a4e35cb912f728c3c78cb10f03f`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Transition Actions' {
	
	attribute def VehicleStartSignal;
	attribute def VehicleOnSignal;
	attribute def VehicleOffSignal;
	
	attribute def ControllerStartSignal;
	
	part def Vehicle {
		brakePedalDepressed : ScalarValues::Boolean;
	}
	part def VehicleController;
	
	action performSelfTest { in vehicle : Vehicle; }
	
	state def VehicleStates;
		
	state vehicleStates : VehicleStates {
		in operatingVehicle : Vehicle;
		in controller : VehicleController;

		first start then off;
		
		state off;
		accept VehicleStartSignal 
			then starting;
			
		state starting;
		accept VehicleOnSignal
			if operatingVehicle.brakePedalDepressed
			do send new ControllerStartSignal() to controller
			then on;
			
		state on {
			entry performSelfTest{ in vehicle = operatingVehicle; }
			do action providePower { /* ... */ }
			exit action applyParkingBrake { /* ... */ }
		}
		accept VehicleOffSignal
			then off;

	}
	
}
````
