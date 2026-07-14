# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_UseFQNInSamePackage_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_UseFQNInSamePackage_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_UseFQNInSamePackage_Rdef.kerml.xt
- source_bytes: 586
- source_sha256: `bd78eba7ef186bd3408c7c0c92205cde7ae98d0557378d657ebbece70f765359`
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

//XPECT noErrors ---> ""
package test{
	feature A {}
	//* XPECT scope at test::A ---
	A, A.self, A.that, A.that.self, B, B.self, B.that, B.that.self, test.A,
	test.A.self, test.A.that, test.A.that.self, test.B, test.B.self, test.B.that,
	test.B.that.self
  	--- */
	feature B subsets test::A{}
}

````
