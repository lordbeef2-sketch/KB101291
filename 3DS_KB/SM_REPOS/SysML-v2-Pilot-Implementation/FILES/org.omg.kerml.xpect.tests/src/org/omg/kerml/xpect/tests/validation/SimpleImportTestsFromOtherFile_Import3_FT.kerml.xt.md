# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/SimpleImportTestsFromOtherFile_Import3_FT.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/SimpleImportTestsFromOtherFile_Import3_FT.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/SimpleImportTestsFromOtherFile_Import3_FT.kerml.xt
- source_bytes: 642
- source_sha256: `99445e5ad5963ad262ad66bc2ccb466fb70c4610ef17958f179e339dfe8975d7`
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

// XPECT noErrors --> ""
//xpect link and scope tests ommitted because same as SimpleImportTestsFromOtherFile.import2
package test {
	public import OuterPackage::*;
	feature Try : B{
		feature try : A::a1 redefines B::b;
	}
}

````
