# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportPackageAlias1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportPackageAlias1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportPackageAlias1.kerml.xt
- source_bytes: 2346
- source_sha256: `6dc2a5736b3a1e354844f7583b48d92dca6c8b9bcc1271a1a22cc26b10cae27a`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyPackageAlias1.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyPackageAlias1.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package test{
	public import PackageAlias1::*;
	classifier A{}
	//XPECT linkedName at A --> test.A
	//* XPECT scope at A ---
		   A, test.A,  
		   A_alias, A_alias.a, A_alias.a_alias, test.A_alias, test.A_alias.a, test.A_alias.a_alias,
		   AA, AA.aa, AA.aa_alias, test.AA, test.AA.aa, test.AA.aa_alias,
		   AA_alias, AA_alias.aa, AA_alias.aa_alias, test.AA_alias, test.AA_alias.aa, test.AA_alias.aa_alias,
 		   test_a, test.test_a,   
 		   test_alias, test_alias.a, test_alias.a_alias, test.test_alias, test.test_alias.a, test.test_alias.a_alias,
 		   PackageAlias1.A, PackageAlias1.A.a,  PackageAlias1.A.a_alias, 
 		   PackageAlias1.AA, PackageAlias1.AA.aa, PackageAlias1.AA.aa_alias,
 		   PackageAlias1.A_alias, PackageAlias1.A_alias.a, PackageAlias1.A_alias.a_alias,
 		   PackageAlias1.AA_alias, PackageAlias1.AA_alias.aa,  PackageAlias1.AA_alias.aa_alias,
		   --- */
	classifier test_a specializes A{} //rename test_A to test_a because xpect linking and scoping throw RuntimeError
 		   
	
	//XPECT linkedName at A_alias --> PackageAlias1.A
	//* XPECT scope at A_alias ---
		   A, test.A,  
		   A_alias, A_alias.a, A_alias.a_alias, test.A_alias, test.A_alias.a, test.A_alias.a_alias,
		   AA, AA.aa, AA.aa_alias, test.AA, test.AA.aa, test.AA.aa_alias,
		   AA_alias, AA_alias.aa, AA_alias.aa_alias, test.AA_alias, test.AA_alias.aa, test.AA_alias.aa_alias,
 		   test_a, test.test_a,   
 		   test_alias, test_alias.a, test_alias.a_alias, test.test_alias, test.test_alias.a, test.test_alias.a_alias,
 		   PackageAlias1.A, PackageAlias1.A.a,  PackageAlias1.A.a_alias, 
 		   PackageAlias1.AA, PackageAlias1.AA.aa, PackageAlias1.AA.aa_alias,
 		   PackageAlias1.A_alias, PackageAlias1.A_alias.a, PackageAlias1.A_alias.a_alias,
 		   PackageAlias1.AA_alias, PackageAlias1.AA_alias.aa,  PackageAlias1.AA_alias.aa_alias,
  		   --- */
	classifier test_alias specializes A_alias{}
}
   

````
