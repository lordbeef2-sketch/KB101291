# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive1_scope_otherfile.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive1_scope_otherfile.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive1_scope_otherfile.kerml.xt
- source_bytes: 1021
- source_sha256: `96da04b9e269c3f09f2718c4b2d64329085dd8cba491eb7492353f42e53fcc3e`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.recursive.KerMLImportRecursiveTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File "Import_Recursive1.kerml" {}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="Import_Recursive1.kerml"}
			}
		}
	}
END_SETUP 
*/

package RecursiveImport {
  
  	public import P::**; 
  	
  	// NOTE: There is some duplication due to the implicit public import of "P" itself
  	// as part of the recursive public import.
	//* XPECT scope at X ---
	P.X, RecursiveImport.P.X, 
	P.Q.Y, RecursiveImport.P.Q.Y,
	P.Q.R.Z, RecursiveImport.P.Q.R.Z,
	
	P.X,
	P.Q.Y,
	P.Q.R.Z,
	
	X, RecursiveImport.X,
	Q.Y, RecursiveImport.Q.Y,
	Q.R.Z,  RecursiveImport.Q.R.Z,	  
	
	Y, RecursiveImport.Y,
	R.Z, RecursiveImport.R.Z,
	
	Z, RecursiveImport.Z,
	
	x, RecursiveImport.x,
	y, RecursiveImport.y,
	z, RecursiveImport.z,
	--- */
	
	x: X;	
	y: Y;
	z: Z;
	 
}

````
