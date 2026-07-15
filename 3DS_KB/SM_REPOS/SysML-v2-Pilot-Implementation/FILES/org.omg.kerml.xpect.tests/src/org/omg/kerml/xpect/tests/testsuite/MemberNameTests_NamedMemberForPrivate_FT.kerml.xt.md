# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberForPrivate_FT.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberForPrivate_FT.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberForPrivate_FT.kerml.xt
- source_bytes: 804
- source_sha256: `a0768f8c5f6a8dabb5cb2f371f103c628d2218e37006f34107398045c26c4e82`
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
		hello, hello.self, hello.test, hello.test.self, hello.test.that,
		hello.test.that.self, hello.that, hello.that.self, k, k.self, k.that, k.that.self, self, something,
		something.self, something.that, something.that.self, test, test.self, test.that,
		test.that.self, that, that.self
		--- */
		//XPECT linkedName at k --> test.something
		feature test : k{}
	}
}

````
