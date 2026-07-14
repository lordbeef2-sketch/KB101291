# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/32. Requirements/Requirement Satisfaction.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/32. Requirements/Requirement Satisfaction.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/32. Requirements/Requirement Satisfaction.sysml
- source_bytes: 594
- source_sha256: `8015e9947463bf4e6d4e638c0b7299ce27c7e9facf955b681c6735d9f1f908fe`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Requirement Satisfaction' {
	private import 'Requirement Definitions'::*;
	private import 'Requirement Groups'::*;
	
	action 'provide power' {
		action 'generate torque' { }
	}
	
	part vehicle_c1 : Vehicle {
		perform 'provide power';
			
		part engine_v1: Engine {
			port :>> clutchPort;
			perform 'provide power'.'generate torque' :>> generateTorque;
		}	
	}
	
	part 'Vehicle c1 Design Context' {
		
		ref vehicle_design :> vehicle_c1;
	
		satisfy vehicleSpecification by vehicle_design;
		satisfy engineSpecification by vehicle_design.engine_v1;
	
	}
	
}
````
