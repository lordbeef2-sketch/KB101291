# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Redefinition_OwningType_Invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Redefinition_OwningType_Invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Redefinition_OwningType_Invalid.sysml.xt
- source_bytes: 1641
- source_sha256: `c8d02ded70aaca8a6423a9480b83c91adb5183ef8d5ca65e8983ef3267087661`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
           ThisFile {}
            File {from ="/library.kernel/Base.kerml"}
            File {from ="/library.kernel/Links.kerml"}
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
			            File {from ="/library.kernel/Links.kerml"}
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
	
	part wheel : Wheel;
	// XPECT errors --> "A package-level feature cannot be redefined" at "wheel"
	part wheel1 redefines wheel;
	
	part def B {
		alias eng1 for Vehicle::eng;
	}

	part def Vehicle specializes B {
		part eng : Engine;
		// XPECT errors --> "Featuring types of redefining feature and redefined feature cannot be the same" at "eng1"
		part smallEng : Engine redefines eng1;
	}
	part def Engine {
		part cyl : Cylinder[4..6];
	}
	part def Cylinder;
	part def Wheel;
}

````
