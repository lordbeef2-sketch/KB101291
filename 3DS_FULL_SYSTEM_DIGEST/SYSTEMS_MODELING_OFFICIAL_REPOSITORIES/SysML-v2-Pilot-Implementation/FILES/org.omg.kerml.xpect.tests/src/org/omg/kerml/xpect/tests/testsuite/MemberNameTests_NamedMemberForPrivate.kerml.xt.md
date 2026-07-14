# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberForPrivate.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberForPrivate.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberForPrivate.kerml.xt
- source_bytes: 739
- source_sha256: `a37b71f97887527802238b6e0f2ae13b40f61bc879a38d1ac3aa134903602b32`
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
package test {
	private classifier <'s_Id'> something{}
	private alias k for something;
	private alias kk for s_Id;
	classifier hello {
		//* XPECT scope at k ---
		   		hello, hello.test, k, something, 
		   		test, s_Id, kk, hello.test1, test1
		--- */
		//XPECT linkedName at k --> test.something
		classifier test specializes k{}
		//XPECT linkedName at kk --> test.something
		classifier test1 specializes kk;
	}
}

````
