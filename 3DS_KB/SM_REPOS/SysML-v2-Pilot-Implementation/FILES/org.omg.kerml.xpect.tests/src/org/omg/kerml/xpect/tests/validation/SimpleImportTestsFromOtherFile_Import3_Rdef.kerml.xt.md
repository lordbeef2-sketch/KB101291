# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/SimpleImportTestsFromOtherFile_Import3_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/SimpleImportTestsFromOtherFile_Import3_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/SimpleImportTestsFromOtherFile_Import3_Rdef.kerml.xt
- source_bytes: 656
- source_sha256: `62e1cc9af9eff845404f5914fa2a9ca60d1cd3a1e3df6e373a1b09e4c7e84dda`
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

// XPECT noErrors --> ""
//xpect link and scope tests ommitted because same as SimpleImportTestsFromOtherFile.import2
package test {
	public import OuterPackage::*;
	feature Try subsets B{
		feature try redefines b redefines B::b;
	}
}

````
