# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/18. Action Performance/Action Performance Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/18. Action Performance/Action Performance Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/18. Action Performance/Action Performance Example.sysml
- source_bytes: 380
- source_sha256: `0dc8639fdd28ec972f85497961123920eb26b8631a55c40d98113453ab292687`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Action Performance Example' {
	private import 'Action Decomposition'::*;
	
	part def Camera;
	part def AutoFocus;
	part def Imager;
	
	part camera : Camera {
		
		perform action takePhoto[*] ordered 
			references takePicture;
		
		part f : AutoFocus {
			perform takePhoto.focus;			
		}
		
		part i : Imager {
			perform takePhoto.shoot;
		}		
	}
}

````
