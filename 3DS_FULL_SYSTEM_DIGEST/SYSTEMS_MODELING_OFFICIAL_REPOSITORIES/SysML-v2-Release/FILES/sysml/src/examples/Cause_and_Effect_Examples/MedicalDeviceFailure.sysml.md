# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Cause and Effect Examples/MedicalDeviceFailure.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Cause and Effect Examples/MedicalDeviceFailure.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Cause and Effect Examples/MedicalDeviceFailure.sysml
- source_bytes: 515
- source_sha256: `8c4f5060527c7d9436409932ec713e15165715b2c232cf299f38aea43ca91a74`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package MedicalDeviceFailure {
	private import CauseAndEffect::*;
	
	part medicalDevice {
		part battery {
			event occurrence depleted;
			event occurrence cannotBeCharged;
		}
		
		event occurrence deviceFails;
		
		ref patient {
			event occurrence therapyDelayed;
		}
		
		#multicausation connection {
			end #cause ::> battery.depleted;
			end #cause ::> battery.cannotBeCharged;
			end #effect ::> deviceFails;
		}
		
		#causation connect deviceFails to patient.therapyDelayed;
	}	
	
}
````
