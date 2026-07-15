# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Cause and Effect Examples/MedicalDeviceFailure.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Cause and Effect Examples/MedicalDeviceFailure.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Cause and Effect Examples/MedicalDeviceFailure.sysml
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
