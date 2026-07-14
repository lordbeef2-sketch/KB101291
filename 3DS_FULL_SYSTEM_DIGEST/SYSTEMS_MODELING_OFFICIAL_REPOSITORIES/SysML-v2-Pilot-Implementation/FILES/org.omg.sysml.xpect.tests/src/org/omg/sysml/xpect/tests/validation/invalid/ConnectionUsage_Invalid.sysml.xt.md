# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/ConnectionUsage_Invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/ConnectionUsage_Invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/ConnectionUsage_Invalid.sysml.xt
- source_bytes: 1792
- source_sha256: `8111b5ed0ef22efd0bf42b308b94aa8b7bd5a1b38b23a68197eaafd88ffdb5be`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
       	File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Connections.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Occurrences.kerml"}
 		      	File {from ="/library.kernel/Objects.kerml"}
 		      	File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Connections.sysml"}
			}
		}
	}
END_SETUP 
*/
package P {
	part def A;	
	part def B;	
	part def C;	
	part def D;	
	part def E;
	
	connection def DE {
		end : D[1];
		end : E[1];
	}
	connection def BC {
		end : B[1];
		end : C[1];
	}
	part apart : A {
		part b :B[1];
		part c: C[1];
		
		connection bc : BC connect b to c;
		connection de : DE, BC connect b to c;
		
		// XPECT errors --> "A connection must be typed by connection definitions." at "connection :A connect b to c;"
		connection :A connect b to c;
		// XPECT errors --> "A connection must be typed by connection definitions." at "connection :apart connect b to c;"
		connection :apart connect b to c;
	}
}


````
