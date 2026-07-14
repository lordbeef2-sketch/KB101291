# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/21. Asynchronous Messaging/Messaging Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/21. Asynchronous Messaging/Messaging Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/21. Asynchronous Messaging/Messaging Example.sysml
- source_bytes: 697
- source_sha256: `94ca0e4af1ac69fc51aa45b83393c4ab615cf19dfbc2a756f1652ed534b1aeac`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Messaging Example' {
	item def Scene;
	item def Image;
	item def Picture;
	
	attribute def Show {
		item picture : Picture;
	}
	
	action def Focus { in item scene : Scene; out item image : Image; }
	action def Shoot { in item image : Image; out item picture : Picture; }
	action def TakePicture;
	
	action screen;
		
	action takePicture : TakePicture {
		action trigger accept scene : Scene;
		
		then action focus : Focus {
			in item scene = trigger.scene;
			out item image;
		}
		
		flow from focus.image to shoot.image;
		
		then action shoot : Shoot {
			in item image; 
			out item picture;
		}
		
		then send new Show(shoot.picture) to screen;
	}
}
````
