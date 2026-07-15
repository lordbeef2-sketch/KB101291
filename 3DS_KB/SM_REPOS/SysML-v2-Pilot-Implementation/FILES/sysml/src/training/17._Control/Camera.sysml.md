# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/17. Control/Camera.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/17. Control/Camera.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/17. Control/Camera.sysml
- source_bytes: 512
- source_sha256: `fe465e835f878198cb7f4f0daa904413ef9c3b86c5dfd0f24fece98245de5c81`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package Camera {
	private import 'Action Decomposition'::*;
	
	part def Camera;
	part def FocusingSubsystem;
	part def ImagingSubsystem;
	
	part camera : Camera {
		ref item scene : Scene;
		part photos : Picture[*];
				
		part autoFocus {
			in ref item scene : Scene = camera::scene;		
			out ref item realImage : Image;
		}
		
		flow autoFocus.realImage to imager.focusedImage;
		
		part imager {
			in item focusedImage : Image;		
			out item photo : Picture :> photos;
		}
		
	}
}

````
