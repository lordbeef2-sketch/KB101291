# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/UseCaseTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/UseCaseTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/UseCaseTest.sysml
- source_bytes: 599
- source_sha256: `9b2c769c791d4ad49bd7af537e653eb2d9125bc924e47081668c9c46cfaf6a07`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package UseCaseTest {

	part def System;	
	part def User;
	
	use case def UseSystem {
		subject system : System;
		actor user : User;
		
		objective  { 
			/* Goal */
		}
		
		include use case uc1 : UC1;	
		include use case uc2 {
			subject = system;
			actor user = UseSystem::user;
		}
	}
	
	use case def UC1;
	
	part user : User;
	
	use case uc2 {
	    subject;
		actor :>> user;
	}
	
	use case u : UseSystem;
	
	part system : System {
		include uc2;
		perform u;
		use case uc1 : UC1;
	}
	
	use case uc3 {
	    include u;
	    include system.uc1;
	}
	
}
````
