# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Subsetting_UniquenessConformance_Invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Subsetting_UniquenessConformance_Invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Subsetting_UniquenessConformance_Invalid.sysml.xt
- source_bytes: 1641
- source_sha256: `a9d29baed0e0fc0b70881d1def1b6f64d813ddab1f1a81f90c18e170f094eca4`
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
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}

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
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
			}
		}
	}
END_SETUP 
*/
package '1a-Parts Tree Simplified' {
	
	part rearAxleAssembly {			
		part rearWheel: Wheel[2];
		// XPECT errors --> "Subsetting/redefining feature cannot be nonunique if subsetted/redefined feature is unique" at "rearWheel"
		part rearWheel_1: Wheel[2] nonunique subsets rearWheel;
		// XPECT errors --> "Subsetting/redefining feature cannot be nonunique if subsetted/redefined feature is unique" at "rearWheel"
		part rearWheel_2[0..1] nonunique subsets rearWheel;
	}
	part def Wheel;
}


````
