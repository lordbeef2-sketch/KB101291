# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/40. Filtering/Filtering Example-1.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/40. Filtering/Filtering Example-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/40. Filtering/Filtering Example-1.sysml
- source_bytes: 860
- source_sha256: `4f48a0cc3b977f19166db84fc759f881925fe5b59ef621d5ca449961e7637014`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Filtering Example-1' {
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
		public import vehicle::**;
		filter @Safety;
	}
	
	package 'Mandatory Safety Features' {
		/* Parts that contribute to safety AND are mandatory. */
		public import vehicle::**;
		filter @Safety and (as Safety).isMandatory;
	}
}
````
