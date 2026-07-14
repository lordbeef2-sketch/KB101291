# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/local/Import_QualifiedName1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/local/Import_QualifiedName1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/local/Import_QualifiedName1.kerml.xt
- source_bytes: 1241
- source_sha256: `1badf61e88d345dfb08ec97610a0cadca9970f231d6f7d74b1519501c27a90f7`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.local.KerMLImportLocalTest
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

// XPECT noErrors ---> ""
package Import_QualifiedName {
	package P1 {
		classifier A;
	}
	package P2 {
		package P2a {
			public import P1::*;
		}
		//* XPECT scope at P2a::A ---
			   Import_QualifiedName.P1.A, Import_QualifiedName.P1.A.self,
			   Import_QualifiedName.P1.A.self.that, Import_QualifiedName.P2.P2a.A, Import_QualifiedName.P2.P2a.A.self,
			   Import_QualifiedName.P2.P2a.A.self.that, Import_QualifiedName.P2.x, Import_QualifiedName.P2.x.self,
			   Import_QualifiedName.P2.x.self.that, Import_QualifiedName.P2.x.that, Import_QualifiedName.P2.x.that.self, P1.A,
			   P1.A.self, P1.A.self.that, P2.P2a.A, P2.P2a.A.self, P2.P2a.A.self.that, P2.x, P2.x.self,
			   P2.x.self.that, P2.x.that, P2.x.that.self, P2a.A, P2a.A.self, P2a.A.self.that, x, x.self,
			   x.self.that, x.that, x.that.self
		--- */
		// The following should not fail.
		// A is a member of P2a because of the public import.
		x: P2a::A;
	}
}

````
