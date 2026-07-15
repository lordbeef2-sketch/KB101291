# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/14. Action Definitions/Action Succession Example-1.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/14. Action Definitions/Action Succession Example-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/14. Action Definitions/Action Succession Example-1.sysml
- source_bytes: 574
- source_sha256: `a7fbffa42b7eed8e00d8568f9b4dcc648ba7746a9b33e622890f670a0fd8cbf8`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Action Succession Example-1' {
	item def Scene;
	item def Image;
	item def Picture;
	
	action def Focus { in scene : Scene; out image : Image; }
	action def Shoot { in image: Image; out picture : Picture; }	
				
	action def TakePicture {
		in item scene : Scene;
		out item picture : Picture;
		
		bind focus.scene = scene;
		
		action focus: Focus { in scene; out image; }
		
		flow from focus.image to shoot.image;
		
		first focus then shoot;
		
		action shoot: Shoot { in image; out picture; }
		
		bind shoot.picture = picture;
	}
	
}
````
