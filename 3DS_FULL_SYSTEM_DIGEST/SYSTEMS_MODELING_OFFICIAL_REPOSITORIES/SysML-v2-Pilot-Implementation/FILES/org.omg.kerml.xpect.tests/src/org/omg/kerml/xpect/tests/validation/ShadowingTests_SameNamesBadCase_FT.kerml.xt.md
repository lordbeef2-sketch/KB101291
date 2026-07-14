# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_SameNamesBadCase_FT.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_SameNamesBadCase_FT.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_SameNamesBadCase_FT.kerml.xt
- source_bytes: 491
- source_sha256: `dc37283e8591e4d053d233deaa9882b80ba92ff49654634f9607ccd60941e80b`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
			}
		}
	}
END_SETUP 
*/

package test{
	feature A{
		feature a1{}
	}
	feature B : A{
		feature A{
			feature a2{}
		}
		// XPECT errors --> "Couldn't resolve reference to Type 'A::a1'." at "A::a1"
		feature b : A::a1{}
	}
}

````
