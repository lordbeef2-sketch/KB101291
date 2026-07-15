# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive2_scope_otherfile.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive2_scope_otherfile.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive2_scope_otherfile.kerml.xt
- source_bytes: 555
- source_sha256: `654cc9323dd3d9acd38e013b4e93b5f746e9101c589b168f5bc0f308c43887fc`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.recursive.KerMLImportRecursiveTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File "Import_Recursive2.kerml" {}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="Import_Recursive2.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors --> ""
package RecursiveImport {
  
   public import P::**;

	//All X, Y and Z are visible here.
	x: X;	
	y: Y;
	z: Z;
	s: S1;
	t: T1;
	u: U1;
}

````
