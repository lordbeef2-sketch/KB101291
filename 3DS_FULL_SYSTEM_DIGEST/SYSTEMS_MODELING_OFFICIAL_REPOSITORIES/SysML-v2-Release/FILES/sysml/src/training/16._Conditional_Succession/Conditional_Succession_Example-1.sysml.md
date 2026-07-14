# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/16. Conditional Succession/Conditional Succession Example-1.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/16. Conditional Succession/Conditional Succession Example-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/16. Conditional Succession/Conditional Succession Example-1.sysml
- source_bytes: 732
- source_sha256: `4d846fc50b1f5a9b055ca84d08d3068f30825c2ca17b4617b860c7af1af058b5`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Conditional Succession Example-1' {
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
				
		first focus 
			if focus.image.isWellFocused then shoot;
		
		flow from focus.image to shoot.image;

		action shoot : Shoot {
			in item; 
			out item picture = takePicture::picture;
		}
	}
	
}
````
