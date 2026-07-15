# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/40. Filtering/Filtering Example-2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/40. Filtering/Filtering Example-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/40. Filtering/Filtering Example-2.sysml
- source_bytes: 840
- source_sha256: `768bd0c1eb62eeb783c7505813b302f05798a2b288c4e04d373842aefa0508f1`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Filtering Example-2' {
	private import ScalarValues::Boolean;
	
	metadata def Safety {
		attribute isMandatory : Boolean;
	}
	
	part vehicle {
		part interior {
			part alarm;
			part seatBelt[2] {@Safety{isMandatory = true;}}
			part frontSeat[2];
			part driverAirBag {@Safety{isMandatory = false;}}
		}
		part bodyAssy {
			part body;
			part bumper {@Safety{isMandatory = true;}}
			part keylessEntry;
		}
		part wheelAssy {
			part wheel[2];
			part antilockBrakes[2] {@Safety{isMandatory = false;}}
		}
	}
	
	package 'Safety Features' {
		/* Parts that contribute to safety. */		
		public import vehicle::**[@Safety];
	}
	
	package 'Mandatory Safety Features' {
		/* Parts that contribute to safety AND are mandatory. */
		public import vehicle::**[@Safety and (as Safety).isMandatory];
	}
}
````
