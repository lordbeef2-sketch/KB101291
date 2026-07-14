# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Feature_invalid_noType.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Feature_invalid_noType.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Feature_invalid_noType.sysml.xt
- source_bytes: 438
- source_sha256: `25ee355b7c07352185022df85d9d82ea63888a36fb8a0e7bb98de09e7c8a04b1`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
			}
		}
	}
END_SETUP 
*/

package 'Test' {
	package A {
		// XPECT errors --> "Must directly or indirectly specialize Parts::Part" at "part def B;"
		part def B;
		// XPECT errors --> "Features must have at least one type" at "ref f;"
		ref f;
	}
}

````
