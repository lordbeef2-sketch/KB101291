# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase3_FT.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase3_FT.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase3_FT.kerml.xt
- source_bytes: 651
- source_sha256: `56bb5be430d3b9209cb22b7bf9dea9c3f6cb1ec4be0b0d71f589f93cff3e2dc5`
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
	feature A{
		feature a2{}
	}
	feature inner{
		public import OuterPackage::*;
		feature B : A {
			//* XPECT errors --- 
			"Couldn't resolve reference to Type 'a2'." at "a2"
			--- */
			feature b : a2{}
		}
	}
}

````
