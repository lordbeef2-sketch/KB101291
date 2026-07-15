# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_CircleInheritance.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_CircleInheritance.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_CircleInheritance.kerml.xt
- source_bytes: 1032
- source_sha256: `87ddfe18d561bc3e3c0560d0033ace2735a4357e4fc9ee0757a0929b13b90ba4`
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
package Test1{
	classifier <'A_Id'> A specializes A::B{
		//XPECT linkedName at A --> Test1.A
		//* XPECT scope at A ---
   		A, A.B, A.B.B, B, B.B, 
   		Test1.A, Test1.A.B, Test1.A.B.B,
   		A_Id, A_Id.B, A_Id.B_Id, A.B_Id, 
   		A_Id.B.B, A_Id.B_Id.B, A_Id.B_Id.B_Id, A_Id.B.B_Id,
   		B_Id, B.B_Id, B_Id.B, B_Id.B_Id,
   		A.B_Id.B, A.B_Id.B_Id, A.B.B_Id, 
   		Test1.A_Id, Test1.A_Id.B, Test1.A_Id.B_Id, Test1.A.B_Id, 
   		Test1.A_Id.B.B, Test1.A_Id.B_Id.B, Test1.A_Id.B_Id.B_Id, Test1.A_Id.B.B_Id,
   		
   		Test1.A.B_Id.B, Test1.A.B_Id.B_Id, Test1.A.B.B_Id, 
 	--- */
		classifier <'B_Id'> B specializes A, Base::Anything {}
	}
}
//not included Test1.B_Id, Test1.B.B_Id, Test1.B_Id.B, Test1.B_Id.B_Id,
````
