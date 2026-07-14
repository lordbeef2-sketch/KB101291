# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Redefinition_Diamond2_valid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Redefinition_Diamond2_valid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Redefinition_Diamond2_valid.kerml.xt
- source_bytes: 894
- source_sha256: `ac237d337ee1763505e73f71150c4cb9b8841f16d9e694aba795f6ab3b391782`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.validation.KerMLValidationTest
	ResourceSet {
       ThisFile {}
        File {from ="/library/Base.kerml"}
        File {from ="/library/Occurrences.kerml"}
        File {from ="/library/Objects.kerml"}
        File {from ="/library/Performances.kerml"}
    }
    Workspace {
        JavaProject {
            SrcFolder {
                ThisFile {}
		            File {from ="/library/Base.kerml"}
		            File {from ="/library/Occurrences.kerml"}
		            File {from ="/library/Objects.kerml"}
		            File {from ="/library/Performances.kerml"}
			}
		}
	}
END_SETUP 
*/
package RedefinitionDiamond {
	feature A {
		feature p[*];
	}
	feature A1 :> A {
		p1 :>> p;
	}
	feature A2 :> A {
//		p :>> p; // 1
	}
	
	feature B :> A1, A2 {
		p2 :>> p1; // 2
// XPECT noErrors ---> ""
		feature p;
	}
}
````
