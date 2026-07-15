# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase1_FT.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase1_FT.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase1_FT.kerml.xt
- source_bytes: 608
- source_sha256: `66e4be75f070cf635b5dbcfe3affd613747aa1eb1974ab9f9abece91435e208a`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyOuterPackage_Feature_FT.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyOuterPackage_Feature_FT.kerml"}
			}
		}
	}
END_SETUP 
*/

package test{
	public import OuterPackage::*;
	feature A{
		feature a2{}
	}
	//* XPECT errors --- 
	"Couldn't resolve reference to Type 'A::a1'." at "A::a1"
	--- */
	feature B : A::a1 {} 
}

````
