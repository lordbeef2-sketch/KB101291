# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/24. States/State Decomposition-1.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/24. States/State Decomposition-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/24. States/State Decomposition-1.sysml
- source_bytes: 437
- source_sha256: `c1a4de673068f7860b3014c4eca64ec839c859e054e3e9dd053190e6adb74435`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'State Decomposition-1' {
	
	attribute def VehicleStartSignal;
	attribute def VehicleOnSignal;
	attribute def VehicleOffSignal;
	
	state def VehicleStates;
		
	state vehicleStates : VehicleStates {
		first start then off;
		
		state off;
		accept VehicleStartSignal 
			then starting;
			
		state starting;
		accept VehicleOnSignal
			then on;
			
		state on;
		accept VehicleOffSignal
			then off;
	}
	
}
````
