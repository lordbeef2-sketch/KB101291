# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase3.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase3.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase3.kerml.xt
- source_bytes: 653
- source_sha256: `90f2415fd9cd7cbd7cf0e747c9ced7199bcf4fae14ec280b946328ed00dcf7c4`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyOuterPackage.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyOuterPackage.kerml"}
			}
		}
	}
END_SETUP 
*/

package test{
	classifier A{
		classifier a2{}
	}
	classifier inner{
		public import OuterPackage::*;
		classifier B specializes A {
			// XPECT errors --> "Couldn't resolve reference to Classifier 'a2'." at "a2"
			classifier b specializes a2{}
		}
	}
}

````
