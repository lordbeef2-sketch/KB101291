# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase2.kerml.xt
- source_bytes: 624
- source_sha256: `6195fac75ce1d7c3c40c474130d54fc2f140d0bd140761c287d91b0b14d99c87`
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
	public import OuterPackage::*;
	classifier A{
		classifier a2{}
	}
	classifier B specializes A {
		// XPECT errors --> "Couldn't resolve reference to Classifier 'a1'." at "a1"
		classifier b specializes a1{}
	}
}

````
