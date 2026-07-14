# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/28. Individuals/Individuals and Roles-1.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/28. Individuals/Individuals and Roles-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/28. Individuals/Individuals and Roles-1.sysml
- source_bytes: 520
- source_sha256: `eddf8b381aaed8a1959416b7c73454085d48401cf22f8c634b8d42f75b81983c`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Individuals and Roles' {
	private import 'Part Definition Example'::*;
	
	part def Wheel;
	
	individual part def Vehicle_1 :> Vehicle {
		part leftFrontWheel : Wheel;
		part rightFrontWheel : Wheel;
	}
	
	individual part def Wheel_1 :> Wheel;
	
	individual part vehicle_1 : Vehicle_1 {
		snapshot part vehicle_1_t0 {
			snapshot leftFrontWheel_t0 : Wheel_1 :>> leftFrontWheel;
		}
		
		then snapshot part vehicle_1_t1 {
			snapshot rightFrontWheel_t1 : Wheel_1 :>> rightFrontWheel;
		}
	}
}
````
