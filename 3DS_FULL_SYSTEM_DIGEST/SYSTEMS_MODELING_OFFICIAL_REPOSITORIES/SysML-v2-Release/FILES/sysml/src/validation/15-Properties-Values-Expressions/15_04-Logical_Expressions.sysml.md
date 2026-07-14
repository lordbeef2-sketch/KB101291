# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/validation/15-Properties-Values-Expressions/15_04-Logical Expressions.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/validation/15-Properties-Values-Expressions/15_04-Logical Expressions.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/validation/15-Properties-Values-Expressions/15_04-Logical Expressions.sysml
- source_bytes: 753
- source_sha256: `8ad32fe7c8c05d36a2cfd2dccbbb206a6832c2e9f92c0163d9d7b2efadc99adb`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '15_04-Logical Expressions' {
	private import ScalarValues::*;
	
	part def Engine;
	part def '4CylEngine' :> Engine;
	part def '6CylEngine' :> Engine;
	
	part def Transmission;
	part def ManualTransmission :> Transmission;
	part def AutomaticTransmission :> Transmission;
	
	part def Vehicle {
		attribute isHighPerformance: Boolean;
		
		part engine: Engine[1];
		part transmission: Transmission[1];
		
		assert constraint {
			if isHighPerformance? engine istype '6CylEngine'
			else engine istype '4CylEngine'
		}
		
		assert constraint {
			(engine istype '4CylEngine' and 
			 transmission istype ManualTransmission) xor
			(engine istype '6CylEngine' and
			 transmission istype AutomaticTransmission)
		}
	}
}
````
