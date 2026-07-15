# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/RedefinitionDiamond1_invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/RedefinitionDiamond1_invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/RedefinitionDiamond1_invalid.sysml.xt
- source_bytes: 1206
- source_sha256: `e4f265d37c9bf81e2d0d21619373912c4d1a769b0016d43867f288aff08d04c4`
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
		            File {from ="/library.kernel/Performances.kerml"}
		            File {from ="/library.systems/Items.sysml"}
		            File {from ="/library.systems/Parts.sysml"}
			}
		}
	}
END_SETUP 
*/
package RedefinitionDiamond {
	part A {
		part p[*];
	}
	part A1 :> A {
		p1 :>> p;
	}
	part A2 :> A {
		p :>> p; // 1
	}
	
	part B :> A1, A2 {
		p2 :>> p1; // 2
// XPECT warnings ---> "Duplicate of inherited member name 'p' from A2" at "p"
		part p;
	}
}
````
