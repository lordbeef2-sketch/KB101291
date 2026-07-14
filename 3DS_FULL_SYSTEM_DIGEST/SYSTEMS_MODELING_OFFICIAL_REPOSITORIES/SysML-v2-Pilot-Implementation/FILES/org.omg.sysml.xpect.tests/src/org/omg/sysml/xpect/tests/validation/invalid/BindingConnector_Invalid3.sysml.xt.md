# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/BindingConnector_Invalid3.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/BindingConnector_Invalid3.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/BindingConnector_Invalid3.sysml.xt
- source_bytes: 1736
- source_sha256: `83ff8c471bef9eb984703551715c769c8c5c661af6029eaaee88f7c5901d1c42`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Links.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
       	File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}

	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Links.kerml"}
				File {from ="/library.kernel/Occurrences.kerml"}
		       	File {from ="/library.kernel/Objects.kerml"}
		       	File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
			}
		}
	}
END_SETUP 
*/
package Test {
	
	part def A;
	part def B;
	part def C specializes B;
	
	part P {
		part a: A {
			in x: ScalarValues::Integer;
		}
		
		part b: B {
			out x;
			out y: ScalarValues::String;
		}
		
		part c: C {
			in y;
		}
		
		// XPECT warnings --> "Bound features should have conforming types" at "bind a = b;"
		bind a = b;
		// TBD errors --> "Output feature must conform to input feature" at "bind a.x = b.x;"
		bind a.x = b.x;
		
		bind b = c;
		bind b.y = c.y;
	}
}
````
