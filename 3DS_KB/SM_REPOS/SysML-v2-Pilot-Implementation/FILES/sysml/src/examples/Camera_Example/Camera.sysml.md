# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Camera Example/Camera.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Camera Example/Camera.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Camera Example/Camera.sysml
- source_bytes: 251
- source_sha256: `d2411282ad14538ac72da1c654b67edf7f080be44d6ecae452c1b28cf59c517e`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
part def Camera {
	private import PictureTaking::*;
	
	perform action takePicture[*] :> PictureTaking::takePicture;
	
	part focusingSubsystem {
		perform takePicture.focus;
	}
	
	part imagingSubsystem {
		perform takePicture.shoot;
	}
	
}
````
