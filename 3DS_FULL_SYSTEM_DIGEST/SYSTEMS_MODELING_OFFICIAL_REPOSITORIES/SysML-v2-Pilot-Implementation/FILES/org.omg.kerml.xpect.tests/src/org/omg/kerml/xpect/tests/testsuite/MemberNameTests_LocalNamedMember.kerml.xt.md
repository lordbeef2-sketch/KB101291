# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_LocalNamedMember.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_LocalNamedMember.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_LocalNamedMember.kerml.xt
- source_bytes: 1538
- source_sha256: `6e5d28fb2be7c620ea18588b420574372419787749ec09e3bb5ac89563c92dec`
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
	classifier <A_Id> A;
	alias A_alias for A;
	alias A_Id_alias for A_Id;
	
	// besides "A_alias", we can reference...
	//* XPECT scope at A_alias ---
	    A, A.self, A.self.that, A_Id, A_Id.self, A_Id.self.that, A_Id_alias,
	    A_Id_alias.self, A_Id_alias.self.that, A_alias, A_alias.self, A_alias.self.that, a, a.self,
	    a.self.that, a.that, a.that.self, a_Id, a_Id.self, a_Id.self.that, a_Id.that,
	    a_Id.that.self, a_Id_1, a_Id_1.self, a_Id_1.self.that, a_Id_1.that, a_Id_1.that.self, test.A,
	    test.A.self, test.A.self.that, test.A_Id, test.A_Id.self, test.A_Id.self.that,
	    test.A_Id_alias, test.A_Id_alias.self, test.A_Id_alias.self.that, test.A_alias,
	    test.A_alias.self, test.A_alias.self.that, test.a, test.a.self, test.a.self.that, test.a.that,
	    test.a.that.self, test.a_Id, test.a_Id.self, test.a_Id.self.that, test.a_Id.that,
	    test.a_Id.that.self, test.a_Id_1, test.a_Id_1.self, test.a_Id_1.self.that, test.a_Id_1.that,
	    test.a_Id_1.that.self
	--- */
	//XPECT linkedName at A_alias --> test.A
	feature a: A_alias;
	//XPECT linkedName at A_Id --> test.A
	feature a_Id: A_Id;
	//XPECT linkedName at A_Id_alias --> test.A
	feature a_Id_1: A_Id_alias;
	
}

````
