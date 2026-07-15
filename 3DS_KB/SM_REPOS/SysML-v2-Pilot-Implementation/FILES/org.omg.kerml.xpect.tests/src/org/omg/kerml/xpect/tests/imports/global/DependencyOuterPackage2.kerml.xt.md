# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyOuterPackage2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyOuterPackage2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyOuterPackage2.kerml.xt
- source_bytes: 2433
- source_sha256: `00c380c5bf9f80391adb457c8cbcf280d1d33bb8da6c65bf06cbe16fcf6cedaa`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.global.KerMLImportGlobalTest
	ResourceSet {
		ThisFile {}
		File {from ="/src/DependencyOuterPackage.kerml"}
		File {from ="/src/DependencyMultipleMembership.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/src/DependencyOuterPackage.kerml"}
				File {from ="/src/DependencyMultipleMembership.kerml"}
			}
		}
	}
END_SETUP 
*/

//Note: DependencyMultipleMembership.kerml and DependencyMultipleImport.alf" are similar that yields the same global scope.
// XPECT noErrors ---> ""
package test{
	//* XPECT scope at OuterPackage2::C ---
		test,
   	   	A, A.a1, test.A, test.A.a1,
       	B, B.b, B.b.a1, test.B, test.B.b, test.B.b.a1,
       	C, C.b, C.b.a1, C.c, test.C, test.C.b, test.C.b.a1, test.C.c,
	   	OuterPackage, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, 
	   	OuterPackage2, OuterPackage2.B, OuterPackage2.B.b, OuterPackage2.B.b.a1,
	   	OuterPackage2.C, OuterPackage2.C.b, OuterPackage2.C.b.a1, OuterPackage2.C.c
	--- */
	public import OuterPackage2::C;
	//* XPECT scope at OuterPackage::A ---
		test,
   	   	A, A.a1, test.A, test.A.a1,
       	B, B.b, B.b.a1, test.B, test.B.b, test.B.b.a1,
       	C, C.b, C.b.a1, C.c, test.C, test.C.b, test.C.b.a1, test.C.c,
	   	OuterPackage, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, 
	   	OuterPackage2, OuterPackage2.B, OuterPackage2.B.b, OuterPackage2.B.b.a1,
	   	OuterPackage2.C, OuterPackage2.C.b, OuterPackage2.C.b.a1, OuterPackage2.C.c
	--- */
	public import OuterPackage::A;
	
	//* XPECT scope at OuterPackage::B ---
		test,
   	   	A, A.a1, test.A, test.A.a1,
       	B, B.b, B.b.a1, test.B, test.B.b, test.B.b.a1,
       	C, C.b, C.b.a1, C.c, test.C, test.C.b, test.C.b.a1, test.C.c,
	   	OuterPackage, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, 
	   	OuterPackage2, OuterPackage2.B, OuterPackage2.B.b, OuterPackage2.B.b.a1,
	   	OuterPackage2.C, OuterPackage2.C.b, OuterPackage2.C.b.a1, OuterPackage2.C.c
	--- */
	public import OuterPackage::B;
	
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
 */  
  

````
