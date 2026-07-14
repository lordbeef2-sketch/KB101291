# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberForPrivate_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberForPrivate_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberForPrivate_Rdef.kerml.xt
- source_bytes: 783
- source_sha256: `5fd135666e718a74d227c49a825d089295d7602d972c48b41f627b81dfb288f7`
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
	private feature something{}
	private alias k for something;
	feature hello {
		//* XPECT scope at k ---
        hello, hello.self, hello.that, hello.that.self, k, k.self, k.that, k.that.self,
        self, something, something.self, something.that, something.that.self, test.hello,
        test.hello.self, test.hello.that, test.hello.that.self, that, that.self
		--- */
		//XPECT linkedName at k --> test.something
		feature test redefines k{}
	}
}

````
