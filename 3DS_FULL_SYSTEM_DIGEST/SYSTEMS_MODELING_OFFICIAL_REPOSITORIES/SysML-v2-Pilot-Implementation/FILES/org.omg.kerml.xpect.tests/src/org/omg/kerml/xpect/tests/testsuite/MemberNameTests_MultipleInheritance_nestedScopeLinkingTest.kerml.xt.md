# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance_nestedScopeLinkingTest.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance_nestedScopeLinkingTest.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance_nestedScopeLinkingTest.kerml.xt
- source_bytes: 1671
- source_sha256: `8bf040fecbf03243d85e6054da0ff499c73ffdece511f14a39d2204769acee6f`
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
	classifier A{
		classifier a {}
		classifier AA {}
		classifier xx {}
		classifier aa{}
	}
	
	classifier B specializes A {
    //XPECT linkedName at aa --> test.A.aa
	classifier b4 specializes aa{}	

		//XPECT linkedName at A::a --> test.A.a
		classifier b specializes A::a {}

//java.lang.RuntimeException: Error creating value for argument org.eclipse.xpect.xtext.lib.tests.LinkingTest.linkedName(..., ICrossEReferenceAndEObject arg1)
//Caused by: java.lang.RuntimeException: no EStructuralFeature found at '...\n	--- */\n		cl|ass b1 specia...'
		//XPEC T linkedName at a --> test.A.a
//		classifier b1 specializes a{}

		//XPECT linkedName at A::AA --> test.A.AA

		classifier b2 specializes A::AA{}
		//XPECT linkedName at AA --> test.A.AA
		classifier b3 specializes AA{}
	}
	classifier C specializes B{
//java.lang.RuntimeException: Error creating value for argument org.eclipse.xpect.xtext.lib.tests.LinkingTest.linkedName(..., ICrossEReferenceAndEObject arg1)
		//XPEC T linkedName at a --> test.A.a
//		classifier c0 specializes a {}

		//XPECT linkedName at b --> test.B.b
		classifier c1 specializes b {}

		//XPEC T linkedName at b1 --> test.B.b1
//		classifier c2 specializes b1{}
	
		//XPECT linkedName at AA --> test.A.AA
		classifier c3 specializes AA{}
	}
	classifier D specializes A::xx{} 
}

````
