# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_ScopeWithOnlyDot.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_ScopeWithOnlyDot.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_ScopeWithOnlyDot.kerml.xt
- source_bytes: 888
- source_sha256: `fba7b939df9144627c4bd33d5bd5a7826a94e8d84ac92eb8ea5861e6ede409e9`
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

// XPECT noErrors ---> ""
package test{
	classifier C {
		//* XPECT scope at OuterPackage::B::b ---
			C, C.c, C.c.a1, C.c.self, C.c.that, C.c.that.self, C.self, C.self.that,
			OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, c,
			c.a1, c.self, c.that, c.that.self, self, self.that, test.C, test.C.c, test.C.c.a1,
			test.C.c.self, test.C.c.that, test.C.c.that.self, test.C.self, test.C.self.that
		--- */
		feature c : OuterPackage::B::b;
	}
}


````
