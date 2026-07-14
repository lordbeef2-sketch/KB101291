# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/validation/13-Model Containment/13b-Safety and Security Features Element Group-2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/validation/13-Model Containment/13b-Safety and Security Features Element Group-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/validation/13-Model Containment/13b-Safety and Security Features Element Group-2.sysml
- source_bytes: 1356
- source_sha256: `35c9e367cb4a118dff42852bce810f3254eeafd179ab2dc8cd454ce83f42e1f7`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '13b-Safety and Security Features Element Group-2' {
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
		public import vehicle::**[@Safety];
	}
	
	package 'Security Features' {
		/* Parts that contribute to security. */		
		public import vehicle::**[@Security];
	}
	
	package 'Safety & Security Features' {
		/* Parts that contribute to safety OR security. */		 
		public import vehicle::**[@Safety or @Security];
	}
	
	package 'Mandatory Saftey Features' {
		/* Parts that contribute to safety AND are mandatory. */
		public import vehicle::**[@Safety and (as Safety).isMandatory];
	}
}

````
