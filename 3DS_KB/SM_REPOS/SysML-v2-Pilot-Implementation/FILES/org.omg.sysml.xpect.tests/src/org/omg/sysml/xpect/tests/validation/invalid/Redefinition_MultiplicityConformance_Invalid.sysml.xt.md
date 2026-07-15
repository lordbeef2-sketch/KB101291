# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Redefinition_MultiplicityConformance_Invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Redefinition_MultiplicityConformance_Invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Redefinition_MultiplicityConformance_Invalid.sysml.xt
- source_bytes: 1683
- source_sha256: `e8dc023ec34806e3a1eb313b89cbdebbb6d351bc17f40fa41bb6d352fba3fa4c`
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
package 'Redefinition Example' {

	part def Engine {
		part cyl : Cylinder[4..6];
	}
	part def SmallEngine :> Engine {
		// XPECT warnings --> "Subsetting/redefining feature should not have larger multiplicity upper bound" at "cyl"
		part redefines cyl[7];
		//* XPECT warnings ---
 		"Redefining feature should not have smaller multiplicity lower bound" at "cyl"
		"Subsetting/redefining feature should not have larger multiplicity upper bound" at "cyl"
		--- */
		part mycyl: Cylinder[1..8] redefines cyl;
	}
	part def BigEngine :> Engine {
		// XPECT warnings --> "Redefining feature should not have smaller multiplicity lower bound" at "cyl"
		part redefines cyl[1..6];
		part bcyl: Cylinder[*];
	}

	part def Cylinder;
}

````
