# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/36. Variability/Variation Configuration.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/36. Variability/Variation Configuration.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/36. Variability/Variation Configuration.sysml
- source_bytes: 403
- source_sha256: `f62e0f7e9020ae2adc90dd0532f22e339752745eaa77b2093c68d826c92a8af3`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Variation Configuration' {
	private import 'Variation Usages'::*;
	
	part vehicle4Cyl :> vehicleFamily {
		part redefines engine = engine::'4cylEngine';
		part redefines transmission = transmission::manualTransmission;
	}
	
	part vehicle6Cyl :> vehicleFamily {
		part redefines engine = engine::'6cylEngine';
		part redefines transmission = transmission::manualTransmission;
	}
	
}
````
