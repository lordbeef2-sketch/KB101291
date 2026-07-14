# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/validation/11-View and Viewpoint/11b-Safety and Security Feature Views.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/validation/11-View and Viewpoint/11b-Safety and Security Feature Views.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/validation/11-View and Viewpoint/11b-Safety and Security Feature Views.sysml
- source_bytes: 1671
- source_sha256: `9fd344c614d34133a758d60fdfc0789333bc6462efb248f4e02a149e6bdc8787`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
private import Views::*; // private import library package, not internal Views package!
package '11b-Safety and Security Feaure Views' {
	private import ScalarValues::*;
	
	package AnnotationDefinitions {	
		metadata def Safety {
			attribute isMandatory : Boolean;
		}
		metadata def Security;
	}
	
	package PartsTree {
		public import AnnotationDefinitions::*;
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

	package ViewDefinitions {	
		public import AnnotationDefinitions::*;
		view def SafetyFeatureView {
			/* Parts that contribute to safety. */		
			filter @Safety;
			render asTreeDiagram;
		}
		
		view def SafetyOrSecurityFeatureView {
			/* Parts that contribute to safety OR security. */		 
			filter @Safety | @Security;
		}	
	}
	
	package Views {
		private import ViewDefinitions::*;
		private import PartsTree::vehicle;
		
		view vehicleSafetyFeatureView : SafetyFeatureView {
			expose vehicle;
		}
		
		view vehicleMandatorySafetyFeatureView :> vehicleSafetyFeatureView {
		    expose vehicle::*::**;
			filter @Safety and (as Safety).isMandatory;
		}
		
		view vehicleMandatorySafetyFeatureViewStandalone {
			expose vehicle::**[@Safety and (as Safety).isMandatory];
			render asElementTable;
		}	
	}
	
}
````
