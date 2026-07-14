# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/21. Asynchronous Messaging/Messaging with Ports.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/21. Asynchronous Messaging/Messaging with Ports.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/21. Asynchronous Messaging/Messaging with Ports.sysml
- source_bytes: 818
- source_sha256: `3f83c4189f746b9a57bbc1df1c0fa935e54d480fb9cb3517c043a760cfac29ce`
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
	
	part screen {
		port displayPort;
	}
	
	part camera {
		port viewPort;
		port displayPort;
		
		action takePicture : TakePicture {
			action trigger accept scene : Scene via viewPort;
			
			then action focus : Focus {
				in item scene = trigger.scene;
				out item image;
			}
			
			flow from focus.image to shoot.image;
		
			then action shoot : Shoot {
				in item image; 
				out item picture;
			}
			
			then send new Show(shoot.picture) via displayPort;
		}
	}
}
````
