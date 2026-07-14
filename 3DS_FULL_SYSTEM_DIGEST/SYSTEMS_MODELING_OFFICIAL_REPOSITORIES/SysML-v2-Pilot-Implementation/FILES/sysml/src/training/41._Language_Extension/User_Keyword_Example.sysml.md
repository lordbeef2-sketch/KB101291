# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/41. Language Extension/User Keyword Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/41. Language Extension/User Keyword Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/41. Language Extension/User Keyword Example.sysml
- source_bytes: 682
- source_sha256: `60381524d6a3c9f4b4f8cd3dd40518d858f4c5b54177cd2a47347a3670d5e119`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'User Keyword Example' {
	private import ScalarValues::Real;
	private import 'Semantic Metadata Example'::*;
	private import RiskMetadata::LevelEnum;
	
	part def Device {
		part battery {
			attribute power : Real;
		}
	}
	
	#scenario def DeviceFailure {
		ref device : Device;
		attribute minPower : Real;
		
		#cause 'battery old' {
			:>> probability = 0.01;			
		}
		
		#causation connect 'battery old' to 'power low';
		
		#situation 'power low' {
			constraint { device.battery.power < minPower }			
		}
		
		#causation connect 'power low' to 'device shutoff';
		
		#failure 'device shutoff' {
			:>> severity = LevelEnum::high;
		}
	}
}
````
