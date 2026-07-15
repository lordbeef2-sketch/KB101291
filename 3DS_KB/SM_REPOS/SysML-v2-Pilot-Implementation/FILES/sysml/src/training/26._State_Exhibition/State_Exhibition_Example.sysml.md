# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/26. State Exhibition/State Exhibition Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/26. State Exhibition/State Exhibition Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/26. State Exhibition/State Exhibition Example.sysml
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
