# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/23. State Definitions/State Definition Example-1.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/23. State Definitions/State Definition Example-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/23. State Definitions/State Definition Example-1.sysml
- source_bytes: 544
- source_sha256: `ee01967efdf155165c197d8032bb8ef68ce40ffa8281be6f8f53dd296309ba7f`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'State Definition Example-1' {
	
	attribute def VehicleStartSignal;
	attribute def VehicleOnSignal;
	attribute def VehicleOffSignal;
		
	state def VehicleStates {
		first start then off;
		
		state off;
		
		transition off_to_starting
			first off
			accept VehicleStartSignal 
			then starting;
			
		state starting;
		
		transition starting_to_on
			first starting
			accept VehicleOnSignal
			then on;
			
		state on;
		
		transition on_to_off
			first on
			accept VehicleOffSignal
			then off;
	}
	
}
````
