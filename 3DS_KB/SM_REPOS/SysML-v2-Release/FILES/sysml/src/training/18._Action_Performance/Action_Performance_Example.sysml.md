# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/18. Action Performance/Action Performance Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/18. Action Performance/Action Performance Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/18. Action Performance/Action Performance Example.sysml
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
