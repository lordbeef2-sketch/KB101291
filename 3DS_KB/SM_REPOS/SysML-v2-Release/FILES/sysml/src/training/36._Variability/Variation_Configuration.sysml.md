# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/36. Variability/Variation Configuration.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/36. Variability/Variation Configuration.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/36. Variability/Variation Configuration.sysml
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
