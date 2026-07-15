# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/validation/13-Model Containment/13b-Safety and Security Features Element Group-1.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/validation/13-Model Containment/13b-Safety and Security Features Element Group-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/validation/13-Model Containment/13b-Safety and Security Features Element Group-1.sysml
- source_bytes: 1396
- source_sha256: `f6f0bb32e5717686661983f0d0cabfbd1c12910449abb093557670792c74ae6a`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '13b-Safety and Security Features Element Group-1' {
	private import ScalarValues::*;
	private import AnnotationDefinitions::*;
	private import PartsTree::*;
	
	package AnnotationDefinitions {
		metadata def Safety {
			attribute isMandatory : Boolean;
		}
		metadata def Security;
	}
	
	package PartsTree {
		part vehicle {
			part interior {
				part alarm {@Security;}
				part seatBelt[2] {@Safety{isMandatory = true;}}
				part frontSeat[2];
				part driverAirBag {@Safety{isMandatory = false;}}
			}
			part bodyAssy {
				part body;
				part bumper {@Safety{isMandatory = true;}}
				part keylessEntry {@Security;}
			}
			part wheelAssy {
				part wheel[2];
				part antilockBrakes[2] {@Safety{isMandatory = false;}}
			}
		}
	}
	
	package 'Safety Features' {
		/* Parts that contribute to safety. */		
		public import vehicle::**;
		filter @Safety;
	}
	
	package 'Security Features' {
		/* Parts that contribute to security. */		
		public import vehicle::**;
		filter @Security;
	}
	
	package 'Safety & Security Features' {
		/* Parts that contribute to safety OR security. */		 
		public import vehicle::**;
		filter @Safety or @Security;
	}
	
	package 'Mandatory Safety Features' {
		/* Parts that contribute to safety AND are mandatory. */
		public import vehicle::**;
		filter @Safety and (as Safety).isMandatory;
	}
}

````
