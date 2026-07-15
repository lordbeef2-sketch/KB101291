# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_UseFQNInSamePackage.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_UseFQNInSamePackage.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_UseFQNInSamePackage.kerml.xt
- source_bytes: 566
- source_sha256: `7620af2e9d4e956693cfdb806e6215108fc23f71f12471363ba1fec6cdfa9f85`
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
	classifier <'A_Id'> A {}
	//XPECT linkedName at A --> test.A
	//* XPECT scope at test::A ---
	   	A, B, C, test.A, test.B, test.C, A_Id, test.A_Id
	   	--- */
	classifier B specializes test::A{}
	classifier C specializes test::A_Id{}
}

````
