# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyOuterPackage3.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyOuterPackage3.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyOuterPackage3.kerml.xt
- source_bytes: 4341
- source_sha256: `702a3313e9d2662104858c614a4a562226c82da542554718e3f105571ebde6d5`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.global.KerMLImportGlobalTest
	ResourceSet {
		ThisFile {}
		File {from ="/src/DependencyOuterPackage.kerml"}
		File {from ="/src/DependencyMultipleMembership.kerml"}
		File {from ="/src/DependencyMembership2.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/src/DependencyOuterPackage.kerml"}
				File {from ="/src/DependencyMultipleMembership.kerml"}
				File {from ="/src/DependencyMembership2.kerml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package test{
	//* XPECT scope at OuterPackage::A ---
		test,
   	   	A, A.a1, test.A, test.A.a1,
       	B, B.b, B.b.a1, test.B, test.B.b, test.B.b.a1,
       	C, C.b, C.b.a1, C.c, test.C, test.C.b, test.C.b.a1, test.C.c,
       	D, D.f, D.f.a1, D.b, D.b.a1, D.c, test.D, test.D.f, test.D.f.a1, test.D.b, test.D.b.a1, test.D.c,
	   	OuterPackage, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, 
	   	OuterPackage2, OuterPackage2.B, OuterPackage2.B.b, OuterPackage2.B.b.a1,
	   	OuterPackage2.C, OuterPackage2.C.b, OuterPackage2.C.b.a1, OuterPackage2.C.c,
		OuterPackage3, OuterPackage3.C, OuterPackage3.C.b, OuterPackage3.C.b.a1, OuterPackage3.C.c, OuterPackage3.D, OuterPackage3.D.f, OuterPackage3.D.f.a1, OuterPackage3.D.b, OuterPackage3.D.b.a1, OuterPackage3.D.c
	--- */
	public import OuterPackage::A;
	
	//* XPECT scope at OuterPackage::B ---
		test,
   	   	A, A.a1, test.A, test.A.a1,
       	B, B.b, B.b.a1, test.B, test.B.b, test.B.b.a1,
       	C, C.b, C.b.a1, C.c, test.C, test.C.b, test.C.b.a1, test.C.c,
       	D, D.f, D.f.a1, D.b, D.b.a1, D.c, test.D, test.D.f, test.D.f.a1, test.D.b, test.D.b.a1, test.D.c,
	   	OuterPackage, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, 
	   	OuterPackage2, OuterPackage2.B, OuterPackage2.B.b, OuterPackage2.B.b.a1,
	   	OuterPackage2.C, OuterPackage2.C.b, OuterPackage2.C.b.a1, OuterPackage2.C.c,
				OuterPackage3, OuterPackage3.C, OuterPackage3.C.b, OuterPackage3.C.b.a1, OuterPackage3.C.c, OuterPackage3.D, OuterPackage3.D.f, OuterPackage3.D.f.a1, OuterPackage3.D.b, OuterPackage3.D.b.a1, OuterPackage3.D.c
	--- */
	public import OuterPackage::B;
	//* XPECT scope at OuterPackage2::C ---
		test,
   	   	A, A.a1, test.A, test.A.a1,
       	B, B.b, B.b.a1, test.B, test.B.b, test.B.b.a1,
       	C, C.b, C.b.a1, C.c, test.C, test.C.b, test.C.b.a1, test.C.c,
       	D, D.f, D.f.a1, D.b, D.b.a1, D.c, test.D, test.D.f, test.D.f.a1, test.D.b, test.D.b.a1, test.D.c,
	   	OuterPackage, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, 
	   	OuterPackage2, OuterPackage2.B, OuterPackage2.B.b, OuterPackage2.B.b.a1,
	   	OuterPackage2.C, OuterPackage2.C.b, OuterPackage2.C.b.a1, OuterPackage2.C.c,
		OuterPackage3, OuterPackage3.C, OuterPackage3.C.b, OuterPackage3.C.b.a1, OuterPackage3.C.c, OuterPackage3.D, OuterPackage3.D.f, OuterPackage3.D.f.a1, OuterPackage3.D.b, OuterPackage3.D.b.a1, OuterPackage3.D.c
	--- */
	public import OuterPackage2::C;
	//* XPECT scope at OuterPackage3::D ---
		test,
   	   	A, A.a1, test.A, test.A.a1,
       	B, B.b, B.b.a1, test.B, test.B.b, test.B.b.a1,
       	C, C.b, C.b.a1, C.c, test.C, test.C.b, test.C.b.a1, test.C.c,
       	D, D.f, D.f.a1, D.b, D.b.a1, D.c, test.D, test.D.f, test.D.f.a1, test.D.b, test.D.b.a1, test.D.c,  
	   	OuterPackage, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, 
	   	OuterPackage2, OuterPackage2.B, OuterPackage2.B.b, OuterPackage2.B.b.a1,
	   	OuterPackage2.C, OuterPackage2.C.b, OuterPackage2.C.b.a1, OuterPackage2.C.c,
		OuterPackage3, OuterPackage3.C, OuterPackage3.C.b, OuterPackage3.C.b.a1, OuterPackage3.C.c, OuterPackage3.D, OuterPackage3.D.f, OuterPackage3.D.f.a1, OuterPackage3.D.b, OuterPackage3.D.b.a1, OuterPackage3.D.c	
		--- */
	public import OuterPackage3::D;
	
}
  
//*
   package OuterPackage{	
		class A{
			class a1{}
		}
		class B{
			feature b: A;
		}
	}
   
   package OuterPackage2{
		public import OuterPackage::B;
		class C specializes B{
			feature c;
		}
	}
	package OuterPackage3{
		public import OuterPackage2::C;
		class D specializes C{
			feature f : b;
		}
	}
 */  
  

````
