# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/28. Individuals/Individuals and Time Slices.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/28. Individuals/Individuals and Time Slices.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/28. Individuals/Individuals and Time Slices.sysml
- source_bytes: 498
- source_sha256: `6ea6b6fa9a457a8d85097ba3337febd6b8d9268e4442caca4f675ee4fabd97dc`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Individuals and Time Slices' {
	private import 'Individuals and Snapshots Example'::*;
	
	individual item def Alice :> Person;
	individual item def Bob :> Person;
	
	individual : Vehicle_1 {
		
		timeslice aliceDriving {
			ref individual item :>> driver : Alice;

			snapshot :>> start {
				:>> mass = 2000.0;
			}
			
			snapshot :>> done {
				:>> mass = 1500.0;
			}			
		}
		
		then timeslice bobDriving {
			ref individual item :>> driver : Bob;
		}
		
	}
}
````
