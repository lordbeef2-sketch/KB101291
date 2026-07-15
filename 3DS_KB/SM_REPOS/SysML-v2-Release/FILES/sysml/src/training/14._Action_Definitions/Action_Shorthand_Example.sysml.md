# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/14. Action Definitions/Action Shorthand Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/14. Action Definitions/Action Shorthand Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/14. Action Definitions/Action Shorthand Example.sysml
- source_bytes: 555
- source_sha256: `30a9efd539b7bfb8e6c730cb26e7f52c5a8d029b168a149aaf8c11543e123fde`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Action Shorthand Example' {
	item def Scene;
	item def Image;
	item def Picture;
	
	action def Focus { in scene : Scene; out image : Image; }
	action def Shoot { in image: Image; out picture : Picture; }	
				
	action def TakePicture {
		in item scene : Scene;
		out item picture : Picture;
		
		action focus: Focus {
			in item scene = TakePicture::scene;
			out item image;
		}
		
		flow from focus.image to shoot.image;
		
		then action shoot: Shoot {
			in item;
			out item picture = TakePicture::picture;
		}
	}
	
}
````
