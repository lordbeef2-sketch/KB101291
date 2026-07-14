# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ItemTest.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ItemTest.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ItemTest.sysml.xt
- source_bytes: 1129
- source_sha256: `5d1efdf896792e0a9b75dbd71bb0817b82188dd59bf19f04c948c5d05dbf5e4a`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.simpletests.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
 		File {from ="/library.systems/Items.sysml"}
 		File {from ="/library.systems/Parts.sysml"}
 		File {from ="/library.systems/Ports.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
		       	File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
 				File {from ="/library.systems/Ports.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package ItemTest {
	
	item f: A;

	public item def A {
		item b: B;
		protected ref part c: C;
	}
	
	abstract item def B {
		public abstract part a: A;
	}
	
	private part def C {
		private in ref item y: A, B;
	}
	
	port def P {
		in item a1: A;
		out item a2: A;
	}
	
}
````
