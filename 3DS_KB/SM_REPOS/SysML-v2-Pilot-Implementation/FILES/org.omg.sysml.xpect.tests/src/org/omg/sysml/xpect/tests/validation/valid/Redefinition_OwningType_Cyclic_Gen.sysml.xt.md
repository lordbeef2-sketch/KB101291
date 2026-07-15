# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Redefinition_OwningType_Cyclic_Gen.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Redefinition_OwningType_Cyclic_Gen.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Redefinition_OwningType_Cyclic_Gen.sysml.xt
- source_bytes: 1038
- source_sha256: `4649b9a0d31db4413f2b0ab95187129ea5b8ac44cdbbffdc7c6ada628731476a`
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
            File {from ="/library.systems/Items.sysml"}
            File {from ="/library.systems/Parts.sysml"}
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
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package 'Redefinition Example' {
	
	part def A :> C;
	
	part def B {
		part a: A;
	}
	
	part def C :> A, B {
		part a redefines B::a;
	}

}

````
