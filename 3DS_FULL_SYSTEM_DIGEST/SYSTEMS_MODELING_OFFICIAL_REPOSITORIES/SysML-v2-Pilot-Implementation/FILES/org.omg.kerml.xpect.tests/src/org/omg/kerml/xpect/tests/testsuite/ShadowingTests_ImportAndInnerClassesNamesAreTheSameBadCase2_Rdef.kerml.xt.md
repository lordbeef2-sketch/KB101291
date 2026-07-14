# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase2_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase2_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase2_Rdef.kerml.xt
- source_bytes: 627
- source_sha256: `6f88b535e12a778bfd396a5a166f8b94876aed046c581a21ce86ef3b12378bfb`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyOuterPackage_Feature_Rdef.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyOuterPackage_Feature_Rdef.kerml"}
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
	feature B subsets A {
		// XPECT errors --> "Couldn't resolve reference to Feature 'a1'." at "a1"
		feature b subsets a1{}
	}
}

````
