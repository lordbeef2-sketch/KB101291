# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive1.kerml.xt
- source_bytes: 1619
- source_sha256: `5328984f1b2c230230c907f9457e03fe924d0fd1c3bfff021f777d4b7c3d301e`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.recursive.KerMLImportRecursiveTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
			}
		}
	}
END_SETUP 
*/

package RecursiveImport {
	
	public import P::**;
  
	package P {
		classifier X;
		package Q {
			classifier Y;
			package R {
        		classifier Z;
      		}
		}
	
	}

	//* XPECT scope at X ---
	P.Q.R.Z, P.Q.R.Z.self, P.Q.R.Z.self.that, P.Q.Y, P.Q.Y.self, P.Q.Y.self.that,
	P.X, P.X.self, P.X.self.that, Q.R.Z, Q.Y, R.Z, RecursiveImport.P.Q.R.Z,
	RecursiveImport.P.Q.R.Z.self, RecursiveImport.P.Q.R.Z.self.that, RecursiveImport.P.Q.Y,
	RecursiveImport.P.Q.Y.self, RecursiveImport.P.Q.Y.self.that, RecursiveImport.P.X, RecursiveImport.P.X.self,
	RecursiveImport.P.X.self.that, RecursiveImport.Q.R.Z, RecursiveImport.Q.Y, RecursiveImport.R.Z,
	RecursiveImport.X, RecursiveImport.Y, RecursiveImport.Z, RecursiveImport.x,
	RecursiveImport.x.self, RecursiveImport.x.self.that, RecursiveImport.x.that,
	RecursiveImport.x.that.self, RecursiveImport.y, RecursiveImport.y.self, RecursiveImport.y.self.that,
	RecursiveImport.y.that, RecursiveImport.y.that.self, RecursiveImport.z, RecursiveImport.z.self,
	RecursiveImport.z.self.that, RecursiveImport.z.that, RecursiveImport.z.that.self, X, Y, Z, x, x.self,
	x.self.that, x.that, x.that.self, y, y.self, y.self.that, y.that, y.that.self, z, z.self,
	z.self.that, z.that, z.that.self
	--- */

	feature x: X;
	feature y: Y;
	feature z: Z;
	 
}

````
