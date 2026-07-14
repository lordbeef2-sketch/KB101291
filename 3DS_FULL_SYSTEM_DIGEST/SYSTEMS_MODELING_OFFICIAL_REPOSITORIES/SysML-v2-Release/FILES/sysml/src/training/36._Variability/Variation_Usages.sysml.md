# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/36. Variability/Variation Usages.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/36. Variability/Variation Usages.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/36. Variability/Variation Usages.sysml
- source_bytes: 626
- source_sha256: `8ba2d6d5c18ad1d29e77e47b2e253344556a7f1d063e913fe1b61c301894ed5d`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Variation Usages' {
	private import 'Variation Definitions'::*;
	
	part def Vehicle;
	part def Transmission;
	part manualTransmission;
	part automaticTransmission;
	
	abstract part vehicleFamily : Vehicle {
		part engine : EngineChoices[1];
		
		variation part transmission : Transmission[1] {
			variant manualTransmission;
			variant automaticTransmission;
		}
		
		assert constraint {
			(engine == engine::'4cylEngine' and
			 transmission == transmission::manualTransmission) xor
			(engine == engine::'6cylEngine' and 
			 transmission == transmission::automaticTransmission)
		}	
	}
	
}
````
