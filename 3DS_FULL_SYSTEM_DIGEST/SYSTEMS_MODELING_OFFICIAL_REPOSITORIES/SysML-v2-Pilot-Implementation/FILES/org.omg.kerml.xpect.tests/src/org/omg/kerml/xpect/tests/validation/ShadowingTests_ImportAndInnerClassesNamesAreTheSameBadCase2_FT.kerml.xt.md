# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase2_FT.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase2_FT.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase2_FT.kerml.xt
- source_bytes: 626
- source_sha256: `ec838cdc2ca0d21b7d215089dee682f2a873236e8d74a207fb2579e4aa6b316a`
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
	feature B : A {
		//* XPECT errors --- 
		   "Couldn't resolve reference to Type 'a1'." at "a1"
		--- */
		feature b : a1{}
	}
}

````
