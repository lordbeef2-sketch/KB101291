# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesInnerClassAndOuterClassWithAlias_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesInnerClassAndOuterClassWithAlias_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesInnerClassAndOuterClassWithAlias_Rdef.kerml.xt
- source_bytes: 920
- source_sha256: `bde3b7e2eed7745bcac1cdc179a97df92ea0be1bd7747aa242cc2245ed6524e9`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
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

// XPECT noErrors --> ""
package test{
	alias A for A1;
	feature A1{
		feature A{
			//XPECT linkedName at A --> test.A1.A
			//* XPECT scope at A ---
            A, A.self, A.that, A.that.self, A1, A1.A, A1.A.self, A1.A.that, A1.A.that.self,
            A1.self, A1.that, A1.that.self, self, test.A, test.A.A, test.A.A.self, test.A.A.that,
            test.A.A.that.self, test.A.self, test.A.that, test.A.that.self, test.A1, test.A1.A, test.A1.A.self,
            test.A1.A.that, test.A1.A.that.self, test.A1.self, test.A1.that, test.A1.that.self, that,
            that.self
			--- */
			feature B redefines A{}
		}
	}
}

````
