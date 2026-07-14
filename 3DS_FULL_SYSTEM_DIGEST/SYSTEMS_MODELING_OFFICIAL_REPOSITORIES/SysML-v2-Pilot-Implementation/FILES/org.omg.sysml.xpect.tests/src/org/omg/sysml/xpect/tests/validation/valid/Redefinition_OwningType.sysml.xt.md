# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Redefinition_OwningType.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Redefinition_OwningType.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Redefinition_OwningType.sysml.xt
- source_bytes: 1708
- source_sha256: `40410f03420d6de0a88c9ccfdb0767971434e321d29a31849474ff90815ca787`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//Owning type conformance: For a redefinition, the owningType of the subsettingFeature shall not be to the owningType of the subsettedFeature
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
	
	part wheel : Wheel;

	part def Vehicle {
		part eng : Engine;
		
		// A feature owned by a package is treated as if it was owned by Anything.
		part redefines wheel;
	}
	part def SmallVehicle :> Vehicle {
		part smallEng : SmallEngine redefines eng;
	}
	part def BigVehicle :> Vehicle {
		part bigEng : BigEngine :>> eng;
	}

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
	part def Wheel;
}

````
