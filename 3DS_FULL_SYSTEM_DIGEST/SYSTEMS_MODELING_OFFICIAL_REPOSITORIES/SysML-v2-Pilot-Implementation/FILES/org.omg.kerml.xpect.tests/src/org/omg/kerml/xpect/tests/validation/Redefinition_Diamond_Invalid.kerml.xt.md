# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Redefinition_Diamond_Invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Redefinition_Diamond_Invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Redefinition_Diamond_Invalid.kerml.xt
- source_bytes: 947
- source_sha256: `1e42709729edd8d78731170b7672728fdf1f4443690a10bd961eb9e0c0e0d3de`
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
		p :>> p; // 1
	}
	
	feature B :> A1, A2 {
//		p2 :>> p1; // 2
// XPECT warnings ---> "Duplicate of inherited member name 'p' from A2" at "p"
		feature p;
	}
}
````
