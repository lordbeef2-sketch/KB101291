# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/17. Control/Merge Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/17. Control/Merge Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/17. Control/Merge Example.sysml
- source_bytes: 852
- source_sha256: `2c8e411106ac597164dcd04936abcf4b7bbb3ac0ef859b8a3f681fb2274fae85`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Merge Example' {
	part def Scene;
	part def Image;
	part def Picture;
	
	action def Focus { in item scene : Scene; out item image : Image; }
	action def Shoot { in item image : Image; out item picture : Picture; }
	action def Display { in item picture : Picture; }
	action def TakePicture;
	
	action takePicture : TakePicture {
		first start;
		
		then merge continue;
			
		then action trigger {
			out item scene : Scene;
		}
		
		flow from trigger.scene to focus.scene;
		
		then action focus : Focus {
			in item scene;
			out item image;
		}
		
		flow from focus.image to shoot.image;
		
		then action shoot : Shoot {
			in item image ;
			out item picture;
		}
		
		flow from shoot.picture to display.picture;
		
		then action display : Display {
			in item picture;
		}
		
		then continue;	
	}
}
````
