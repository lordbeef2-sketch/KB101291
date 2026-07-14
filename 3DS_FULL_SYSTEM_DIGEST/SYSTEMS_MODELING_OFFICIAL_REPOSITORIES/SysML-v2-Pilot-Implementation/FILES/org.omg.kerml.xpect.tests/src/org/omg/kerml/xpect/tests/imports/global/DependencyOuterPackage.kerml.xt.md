# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyOuterPackage.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyOuterPackage.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyOuterPackage.kerml.xt
- source_bytes: 968
- source_sha256: `b05ac3efe5d4ba7a0493821d37fe1a9d308b92b2568d4ea9a7bcb14741fc05cf`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.global.KerMLImportGlobalTest
	ResourceSet {
		ThisFile {}
		File {from ="/src/DependencyOuterPackage.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/src/DependencyOuterPackage.kerml"}
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
       	OuterPackage, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1
	--- */
	public import OuterPackage::A;
	//* XPECT scope at OuterPackage::B ---
		test,
   	   	A, A.a1, test.A, test.A.a1,
       	B, B.b, B.b.a1, test.B, test.B.b, test.B.b.a1,
		OuterPackage, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, 
	--- */
	public import OuterPackage::B;
	
	
}
  

````
