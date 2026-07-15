# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/16. Conditional Succession/Conditional Succession Example-2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/16. Conditional Succession/Conditional Succession Example-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/16. Conditional Succession/Conditional Succession Example-2.sysml
- source_bytes: 719
- source_sha256: `a95174bd4be13c296524d51e8ac5f1630dc1ad7e2fd88ad6a53a2c664b4e0273`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Conditional Succession Example-2' {
	part def Scene;
	part def Image {
		isWellFocused: ScalarValues::Boolean;
	}
	part def Picture;
	
	action def Focus { in scene : Scene; out image : Image; }
	action def Shoot { in image: Image; out picture : Picture; }	
	action def TakePicture { in scene : Scene; out picture : Picture; }
	
	action takePicture : TakePicture {
		in item scene;
		out item picture;
		
		action focus : Focus {
			in item scene = takePicture::scene; 
			out item image;
		}
		
		if focus.image.isWellFocused then shoot;
		
		flow from focus.image to shoot.image;

		action shoot : Shoot {
			in item image; 
			out item picture = takePicture::picture;
		}
	}
	
}
````
