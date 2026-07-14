# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesImportAsFeature.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesImportAsFeature.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesImportAsFeature.kerml.xt
- source_bytes: 970
- source_sha256: `c266ce87af6fbc0c143ee6c1e509769dc81af36d0f2a31b2ccbc738952ec47e9`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencySamePackageName_A.kerml"}
		File {from ="/src/DependencySamePackageName_B.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencySamePackageName_A.kerml"}
				File {from ="/src/DependencySamePackageName_B.kerml"}
			}
		}
	}
END_SETUP 
*/
//Both DepedencySamePackageName_A and DependencySamePackageName_B have the same package names "SamePackage"
//Current implemention public import from the first src package(A).
//XPECT noErrors --> ""
package test{
	public import SamePackage::container;
	classifier something1 specializes container::A{}
	//XPECT errors -->"Couldn't resolve reference to Classifier 'container::B'." at "container::B"
	classifier something2 specializes container::B{}
}

````
