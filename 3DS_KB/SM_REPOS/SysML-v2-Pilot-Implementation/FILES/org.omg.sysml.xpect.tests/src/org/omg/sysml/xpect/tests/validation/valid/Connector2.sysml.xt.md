# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Connector2.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Connector2.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Connector2.sysml.xt
- source_bytes: 1871
- source_sha256: `7585eac3f1d6180a88685fe012b70a6f31b8f25e6d03c1f664a022fecf45f84a`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.validation.valid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
       	File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/ControlFunctions.kerml"}
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
				File {from ="/library.kernel/ControlFunctions.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Connections.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package P {
	
	part def A;
	part def B;
	part def C;
	part def D;
	part def E;
	part def F;
	
	connection def AB {
		end : D[1];
		end : F[1];
	}
	
	part a : A {
		
		part b1 : B[1] {
			part c : C[1] {
				part c: C[1]{
					part d : D[2];
				}			
				part d : D[2];
			}
			part e: E[1] {
				part f: F[2];
			}						
		}
		
		part b2 : B[1] {
			part c : C[1] {
				part cc: C[1]{
					part d : D[2];
				}			
				part d : D[2];
			}
			part e: E[1] {
				part f : F[2];
			}						
				
		}
		connection : AB connect b1.c.d to b2.e.f;	
	}
	
}

````
