# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MultipleImportTests_ImportFeatureMoreTimes.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MultipleImportTests_ImportFeatureMoreTimes.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MultipleImportTests_ImportFeatureMoreTimes.kerml.xt
- source_bytes: 866
- source_sha256: `46aa57cf0a0bd6237c1257aaaafe4d21be9b0cb8a0ea6ab8244c859dd0ac5cc2`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyOuterPackage.kerml"}
		File {from ="/src/DependencyMultipleMembership.kerml"}
		File {from ="/src/DependencyMembership2.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyOuterPackage.kerml"}
				File {from ="/src/DependencyMultipleMembership.kerml"}
				File {from ="/src/DependencyMembership2.kerml"}
			}
		}
	}
END_SETUP 
*/

package test{
	public import OuterPackage3::D;
	// XPECT errors ---> "Couldn't resolve reference to Classifier 'B'." at "B"
	classifier EE specializes B{
		// XPECT errors ---> "Couldn't resolve reference to Type 'b'." at "b"
		feature try : b;
	}
}

````
