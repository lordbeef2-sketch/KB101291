# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/24. States/State Decomposition-2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/24. States/State Decomposition-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/24. States/State Decomposition-2.sysml
- source_bytes: 545
- source_sha256: `5182ad33a6dff4e44e5fda13c0c9fd518a60a78f76d5742d4f3b9af73e643007`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'State Decomposition-1' {
	
	attribute def VehicleStartSignal;
	attribute def VehicleOnSignal;
	attribute def VehicleOffSignal;
	
	state def VehicleStates;
		
	state vehicleStates : VehicleStates parallel {
		
		state operationalStates {
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
		
		state healthStates { 
			/* ... */
		}
	}
	
}
````
