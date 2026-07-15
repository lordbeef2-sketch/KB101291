# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/24. States/State Actions.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/24. States/State Actions.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/24. States/State Actions.sysml
- source_bytes: 734
- source_sha256: `3bfefd2343ad5cda784a55aa876e52c32a52af5a7356087801910bfd7b48c6c3`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'State Actions' {
	
	attribute def VehicleStartSignal;
	attribute def VehicleOnSignal;
	attribute def VehicleOffSignal;
	
	part def Vehicle;
	
	action performSelfTest { in vehicle : Vehicle; }
	
	state def VehicleStates { in operatingVehicle : Vehicle; }
		
	state vehicleStates : VehicleStates {
		in operatingVehicle : Vehicle;
			
		first start then off;
		
		state off;
		accept VehicleStartSignal 
			then starting;
			
		state starting;
		accept VehicleOnSignal
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
