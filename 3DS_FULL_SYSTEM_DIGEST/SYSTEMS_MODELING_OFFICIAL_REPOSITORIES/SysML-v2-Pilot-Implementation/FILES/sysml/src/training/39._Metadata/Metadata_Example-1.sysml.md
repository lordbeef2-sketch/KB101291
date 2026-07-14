# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/39. Metadata/Metadata Example-1.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/39. Metadata/Metadata Example-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/39. Metadata/Metadata Example-1.sysml
- source_bytes: 643
- source_sha256: `b7a12ab801723131f2f4ed4beb795b10e83375a1f0e878bc473970bf47a1d696`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Metadata Example-1' {
	
	metadata def SafetyFeature;
	metadata def SecurityFeature {
		:> annotatedElement : SysML::PartDefinition;
		:> annotatedElement : SysML::PartUsage;
	}
	
	metadata SafetyFeature about 
		vehicle::interior::seatBelt,
		vehicle::interior::driverAirBag,
		vehicle::bodyAssy::bumper;
	
	metadata SecurityFeature about
		vehicle::interior::alarm,
		vehicle::bodyAssy::keylessEntry;
		
	part vehicle {
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
	
}
````
