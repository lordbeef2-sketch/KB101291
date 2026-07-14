# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/26. State Exhibition/State Exhibition Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/26. State Exhibition/State Exhibition Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/26. State Exhibition/State Exhibition Example.sysml
- source_bytes: 281
- source_sha256: `b1041c321dee03b551f75a0531b4cdf8d6626056b04ed1d2a0ea337c2cfd7534`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'State Exhibition Example' {
	private import 'Transition Actions'::*;
	
	part vehicle : Vehicle {
		
		part vehicleController : VehicleController;
		
		exhibit vehicleStates {
			in operatingVehicle = vehicle;
			in controller = vehicleController;
		}

	}
	
}
````
