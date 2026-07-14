# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Subsetting_MultiplicityConformance.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Subsetting_MultiplicityConformance.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Subsetting_MultiplicityConformance.sysml.xt
- source_bytes: 1230
- source_sha256: `ada260b161e5b5230304bcf30a8913c5d7e36af30e1b2c6cb5abd11a88564b1b`
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
		part cyl1[4] :> cyl;
	}
	part def BigEngine :> Engine {
		part cyl1[6] :> cyl;
		part cyl0[0..1] :> cyl;
	}

	part def Cylinder;
	
}

````
