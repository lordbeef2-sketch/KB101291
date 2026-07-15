# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/23. State Definitions/State Definition Example-2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/23. State Definitions/State Definition Example-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/23. State Definitions/State Definition Example-2.sysml
- source_bytes: 400
- source_sha256: `69c0fb7fdf18dd96dc520111657e4362b1c809b3021374972e81eb573773287e`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'State Definition Example-2' {
	
	attribute def VehicleStartSignal;
	attribute def VehicleOnSignal;
	attribute def VehicleOffSignal;
		
	state def VehicleStates {
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
