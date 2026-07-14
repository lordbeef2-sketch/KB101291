# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/AssignmentActionUsage_invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/AssignmentActionUsage_invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/AssignmentActionUsage_invalid.sysml.xt
- source_bytes: 1602
- source_sha256: `07935fef020739cb96da65ccc5b26be7764e1ffe796893b5c42211611b4a6b25`
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
		File {from ="/library.kernel/FeatureReferencingPerformances.kerml"}
		File {from ="/library.systems/Attributes.sysml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Actions.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/FeatureReferencingPerformances.kerml"}
                File {from ="/library.systems/Attributes.sysml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Actions.sysml"}
			}
		}
	}
END_SETUP 
*/
package AssignmentActionUsage_invalid {
    item i {
        attribute a;
        protected attribute b;
        private attribute c;
        action d;
    }
	action def A {
        assign i.a := null;
        // XPECT errors --> "Couldn't resolve reference to Element 'b'." at "b"
        assign i.b := null;
        // XPECT errors --> "Couldn't resolve reference to Element 'c'." at "c"
        assign i.c := null;
        // XPECT errors --> "Referent must be time varying." at "d"
        assign i.d := null;
	}
}

````
