# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/validation/13-Model Containment/13b-Safety and Security Features Element Group.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/validation/13-Model Containment/13b-Safety and Security Features Element Group.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/validation/13-Model Containment/13b-Safety and Security Features Element Group.sysml
- source_bytes: 926
- source_sha256: `934ac161f661855b7d0682d741535fb339c75ee85790215284b3fc41b59c4432`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '13b-Safety and Security Features Element Group' {
	
	part vehicle1_c1 {
		part interior {
			part alarm;
			part seatBelt[2];
			part frontSeat[2];
			part driverAirBag;
		}
		part bodyAssy {
			part body;
			part bumper;
			part keylessEntry;
		}
	}
	
	package 'Safety Features' {
		/* Parts that contribute to safety. */
		
		public import vehicle1_c1::interior::seatBelt;
		public import vehicle1_c1::interior::driverAirBag;
		public import vehicle1_c1::bodyAssy::bumper;		
	}
	
	package 'Security Features' {
		/* Parts that contribute to security. */
		
		public import vehicle1_c1::interior::alarm;
		public import vehicle1_c1::bodyAssy::keylessEntry;
	}
	
	package 'Safety & Security Features' {
		/* Parts that contribute to safety AND
		 * parts that contribute to security.
		 */
		 
		public import 'Safety Features'::*;
		public import 'Security Features'::*;
	}
}

````
