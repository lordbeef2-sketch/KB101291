# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/BindingConnector_simple.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/BindingConnector_simple.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/BindingConnector_simple.sysml.xt
- source_bytes: 1813
- source_sha256: `7dbe420e141eeedc00ac0c1d07fca63f3b15c1cae2d70275ddf379f60ef55340`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.validation.valid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Links.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
       	File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/ControlFunctions.kerml"}
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
				File {from ="/library.kernel/ControlFunctions.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package BindingConnectorExample {
	part def B0;
	part def B1; 
	part def V;
	part v : V {
		part b0 : B0 {
			port p0 {
				in ref myIn;
				out ref myOut;
			}
		}
		part b1 : B1 {
			port p1 {
				in ref myIn;
				out ref myOut;
			}
		}
		//in[Part, Object] out[Part, Object]
		bind b0.p0.myIn = b1.p1.myOut;
		bind b0.p0.myOut = b1.p1.myIn;
		//inin
		bind b0.p0.myIn = b1.p1.myIn;
		bind b0.p0.myOut = b1.p1.myOut;
		//outout
		bind b0.p0.myIn = b1.p1.myOut;
		bind b0.p0.myOut = b1.p1.myIn;
		
	} 
}

````
