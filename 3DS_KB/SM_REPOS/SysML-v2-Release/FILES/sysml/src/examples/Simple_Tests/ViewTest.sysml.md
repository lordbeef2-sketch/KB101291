# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Simple Tests/ViewTest.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Simple Tests/ViewTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Simple Tests/ViewTest.sysml
- source_bytes: 591
- source_sha256: `e1a21097f33fb4a39775e032750ecba56b43ac637f1504fa127625813d11f01a`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ViewTest {
	package P {
		public part p1;
		private part p2;
	}
	
	part def S;
	
	concern def C {
	    subject;
		stakeholder s : S;
	}
	
	concern c : C {
	    subject;
		stakeholder s1;
	}
	
	viewpoint def VP {
		frame c;
	}
	
	rendering def R;
	
	rendering r : R;
	
	view def V {
		viewpoint vp: VP {
			frame concern c1;
			concern c2;
		}
		render rendering r1: R[0..1]; 
		
		view v: V[0..*] {
			expose P::*;
			render r;
			
			rendering r2;
			
			alias vp1 for p1;
			// Note: "expose" imports all.
			alias vp2 for p2;
		}
	}

}
````
