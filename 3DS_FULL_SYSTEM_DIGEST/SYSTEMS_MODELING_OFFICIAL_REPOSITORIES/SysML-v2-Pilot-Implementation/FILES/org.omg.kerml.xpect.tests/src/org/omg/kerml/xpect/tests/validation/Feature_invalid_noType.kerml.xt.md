# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Feature_invalid_noType.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Feature_invalid_noType.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Feature_invalid_noType.kerml.xt
- source_bytes: 447
- source_sha256: `2a3149c33feef87351142d4512edaaf14519057c1e4854d0f204f248baa6faf8`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
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
		// XPECT errors --> "Must directly or indirectly specialize Base::Anything" at "classifier A;"
		classifier A;
		// XPECT errors --> "Features must have at least one type" at "feature f;"
		feature f;
	}
}
````
