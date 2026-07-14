# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Redefinition_MultiplicityConformance.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Redefinition_MultiplicityConformance.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Redefinition_MultiplicityConformance.sysml.xt
- source_bytes: 1204
- source_sha256: `aebc40f2785c4648815689f5886e1c49bbf5e7cc6d22fad3de8bfcc0c009b2ef`
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
// XPECT noErrors ---> ""
package 'Redefinition Example' {

	part def Engine {
		part cyl : Cylinder[4..6];
	}
	part def SmallEngine :> Engine {
		part redefines cyl[4];
	}
	part def BigEngine :> Engine {
		part redefines cyl[6];
	}

	part def Cylinder;
}

````
