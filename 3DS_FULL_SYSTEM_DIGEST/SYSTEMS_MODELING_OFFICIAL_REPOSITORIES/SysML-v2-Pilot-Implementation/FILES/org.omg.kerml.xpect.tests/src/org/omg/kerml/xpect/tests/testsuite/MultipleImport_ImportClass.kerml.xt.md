# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImport_ImportClass.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImport_ImportClass.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImport_ImportClass.kerml.xt
- source_bytes: 2146
- source_sha256: `6acdbcdb985f0c9f0011a2de8cfdd445a24c2f6e96aa1e564f885dba74b61088`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyOuterPackage.kerml"}
		File {from ="/src/DependencyMultipleMembership.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyOuterPackage.kerml"}
				File {from ="/src/DependencyMultipleMembership.kerml"}
			}
		}
	}
END_SETUP 
*/
//For scope at C ---why OuterPackage.B.b.a1 and OuterPackage2.C.b are not inscope but OuterPackage2.C.b.a1?
// XPECT noErrors ---> ""
package test{
	public import OuterPackage2::C;
	//XPECT linkedName at C --> OuterPackage2.C
	//* XPECT scope at C ---
	   	   C.b.a1, D.b.a1, D.try.a1, 
		   test.C.b.a1, test.D.b.a1, test.D.try.a1,
		   C, D, test.C, test.D,
		   OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b.a1, 
		   OuterPackage2.B, OuterPackage2.B.b.a1,
		   OuterPackage2.C, OuterPackage2.C.b.a1,
	--- */
	classifier D specializes C {
		//linkedName at b --> OuterPackage.B.b
		//* XPECT scope at b ---
		   C, C.b, C.b.a1, C.c, C.c.self, C.c.that, C.c.that.self, D, D.b, D.b.a1, D.c,
		   D.c.self, D.c.that, D.c.that.self, D.self, D.self.that, D.try, D.try.a1, D.try.self,
		   D.try.that, D.try.that.self, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B,
		   OuterPackage.B.b, OuterPackage.B.b.a1, OuterPackage2.B, OuterPackage2.B.b, OuterPackage2.B.b.a1,
		   OuterPackage2.C, OuterPackage2.C.b, OuterPackage2.C.b.a1, OuterPackage2.C.c,
		   OuterPackage2.C.c.self, OuterPackage2.C.c.that, OuterPackage2.C.c.that.self, b, b.a1, c, c.self,
		   c.that, c.that.self, self, self.that, test.C, test.C.b, test.C.b.a1, test.C.c,
		   test.C.c.self, test.C.c.that, test.C.c.that.self, test.D, test.D.b, test.D.b.a1, test.D.c,
		   test.D.c.self, test.D.c.that, test.D.c.that.self, test.D.self, test.D.self.that, test.D.try,
		   test.D.try.a1, test.D.try.self, test.D.try.that, test.D.try.that.self, try, try.a1, try.self,
		   try.that, try.that.self
	--- */
		feature try : b;
	}
}

````
