# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/15. Actions/Action Decomposition.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/15. Actions/Action Decomposition.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/15. Actions/Action Decomposition.sysml
- source_bytes: 608
- source_sha256: `b9623cc7d352968f1f3dfc294c44f4fb74eedc09587990616907c388ecf78115`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Action Decomposition' {
	part def Scene;
	part def Image;
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
		
		flow from focus.image to shoot.image;

		action shoot : Shoot {
			in item; 
			out item picture = takePicture::picture;
		}
	}
	
}
````
