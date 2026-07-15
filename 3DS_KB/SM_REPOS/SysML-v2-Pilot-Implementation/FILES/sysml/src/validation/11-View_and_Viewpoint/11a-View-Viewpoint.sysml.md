# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/validation/11-View and Viewpoint/11a-View-Viewpoint.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/validation/11-View and Viewpoint/11a-View-Viewpoint.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/validation/11-View and Viewpoint/11a-View-Viewpoint.sysml
- source_bytes: 1200
- source_sha256: `b0ca9ddbc8e4ec8731eb8fe9aa01ee9e7d80c14269567d678ac121fcc18a2d4b`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '11a-View-Viewpoint' {
	
	package SystemModel {
		private import SI::*;
		
		part def Vehicle;
		part def AxleAssembly;
		part def Axle;
		part def Wheel;
		
		part vehicle : Vehicle {
			attribute mass :> ISQ::mass = 2500[SI::kg];
			part frontAxleAssembly : AxleAssembly[1] {
				attribute mass :> ISQ::mass = 150[kg];
				part frontWheel : Wheel[2];
				part frontAxle : Axle[1] {
					attribute mass;
					attribute steeringAngle;
				}
			}
			part rearAxleAssembly : AxleAssembly[1] {
				attribute mass :> ISQ::mass = 250[kg];
				part rearWheel : Wheel[2];
				part rearAxle : Axle[1] {
					attribute mass;
				}
			}
		}
		
	}
	
	package ViewModel {
		private import Views::*;
	
		part 'systems engineer';
		
		concern 'system breakdown' {
			subject;
			stakeholder :>> 'systems engineer';
		}
		
		viewpoint 'system structure perspective' {		
			frame 'system breakdown';
		}
		
		view 'system structure generation' {
			satisfy 'system structure perspective';
			expose SystemModel::vehicle::**[@SysML::PartUsage];
			render asElementTable {
				view :>> columnView[1] {
					render asTextualNotation;
				}
			}
		}
	
	}
}
````
