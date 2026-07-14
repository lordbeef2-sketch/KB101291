# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/22. Opaque Actions/Opaque Action Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/22. Opaque Actions/Opaque Action Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/22. Opaque Actions/Opaque Action Example.sysml
- source_bytes: 325
- source_sha256: `34b9f4488a1416ac5cca5b12e93e5125846a41c228a9966902f18d8f496a7094`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Opaque Action Example' {
	
	part def Sensor {
		attribute ready : ScalarValues::Boolean;
	}
	
	action def UpdateSensors {
		in sensors : Sensor[*];
		language "Alf" 
			/* 
			 * for (sensor in sensors) {
			 *     if (sensor.ready) {
			 *         Update(sensor);
			 *     }
			 * }
			 */
	}
	
}
````
