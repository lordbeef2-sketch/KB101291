# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/28. Individuals/Individuals and Snapshots Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/28. Individuals/Individuals and Snapshots Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/28. Individuals/Individuals and Snapshots Example.sysml
- source_bytes: 489
- source_sha256: `81dd5e6cf5a52cc31329b24b23c9febc085a7eb8a329970147e821c3575ed5a3`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Individuals and Snapshots Example' {
	public import 'Part Definition Example'::*;
	
	individual part def Vehicle_1 :> Vehicle {
		
		snapshot part vehicle_1_t0 {
			:>> mass = 2000.0;
			:>> status {
				:>> gearSetting = 0;
				:>> acceleratorPosition = 0.0;
			}
		}
		
		snapshot part vehicle_1_t1 {
			:>> mass = 1500.0;
			:>> status {
				:>> gearSetting = 2;
				:>> acceleratorPosition = 0.5;
			}
		}
		
		first vehicle_1_t0 then vehicle_1_t1;
	}
}
````
