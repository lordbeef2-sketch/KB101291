# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/14. Action Definitions/Action Definition Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/14. Action Definitions/Action Definition Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/14. Action Definitions/Action Definition Example.sysml
- source_bytes: 519
- source_sha256: `3a17d11357e1a5c2afe6e5a223d84b6f2e25c3df72874e4bf9292080257c5372`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Action Definition Example' {
	item def Scene;
	item def Image;
	item def Picture;
	
	action def Focus { in scene : Scene; out image : Image; }
	action def Shoot { in image: Image; out picture : Picture; }	
		
	action def TakePicture { in scene : Scene; out picture : Picture;
		bind focus.scene = scene;
		
		action focus: Focus { in scene; out image; }
		
		flow from focus.image to shoot.image;
		
		action shoot: Shoot { in image; out picture; }
		
		bind shoot.picture = picture;
	}
	
}
````
