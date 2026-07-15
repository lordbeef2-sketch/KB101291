# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberFromInheritance_2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberFromInheritance_2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberFromInheritance_2.kerml.xt
- source_bytes: 671
- source_sha256: `8c054336020c7999f8a77ce4053bb7b9b5cc359d4af685ced88d1f0f9e5069ea`
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
	classifier EE {}
	classifier A{
		classifier a {}
		alias aa for a;
	}
	//* XPECT scope at A ---
		A, A.a, A.aa, B, B.a, B.aa, EE, 
		test.A, test.A.a, test.A.aa, test.B, test.B.a, test.B.aa, test.EE,
				
		--- */
	classifier B specializes A{
		//XPECT linkedName at aa --> test.A.a
		feature b: aa;
		alias b_alias for b;
	}
}

````
