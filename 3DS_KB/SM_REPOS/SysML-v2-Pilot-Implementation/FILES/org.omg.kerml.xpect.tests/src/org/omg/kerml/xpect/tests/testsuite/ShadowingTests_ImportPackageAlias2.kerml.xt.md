# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportPackageAlias2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportPackageAlias2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportPackageAlias2.kerml.xt
- source_bytes: 1773
- source_sha256: `74372a94d686bbab2c19eda501046d7bf271a8af20bef9a8f8ae893f8e9975e7`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyPackageAlias1.kerml"}
		File {from ="/src/DependencyPackageAlias2.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyPackageAlias1.kerml"}
				File {from ="/src/DependencyPackageAlias2.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package test{
	public import PackageAlias1::*;
	classifier A{}
	alias A_alias for A;
	//XPECT linkedName at  A_alias --> test.A
	//* XPECT scope at  A_alias ---
 		   test_A, test.test_A,
	        A, test.A, 
			A_alias, test.A_alias,
			AA, AA.aa, AA.aa_alias, test.AA, test.AA.aa, test.AA.aa_alias, 
			AA_alias, AA_alias.aa, AA_alias.aa_alias, test.AA_alias, test.AA_alias.aa,test.AA_alias.aa_alias,
 		        
 		    PackageAlias1.A, PackageAlias1.A.a, PackageAlias1.A.a_alias, 
 		    PackageAlias1.A_alias, PackageAlias1.A_alias.a, PackageAlias1.A_alias.a_alias,
 		    PackageAlias1.AA, PackageAlias1.AA.aa, PackageAlias1.AA.aa_alias, 
 		    PackageAlias1.AA_alias,PackageAlias1.AA_alias.aa, PackageAlias1.AA_alias.aa_alias, 
 		   
 		    PackageAlias2.A, PackageAlias2.A.a, PackageAlias2.A.a_alias, 
 		    PackageAlias2.A_alias, PackageAlias2.A_alias.a, PackageAlias2.A_alias.a_alias,
 		    PackageAlias2.AA, PackageAlias2.AA.aa, PackageAlias2.AA.aa_alias, 
 		    PackageAlias2.AA_alias,PackageAlias2.AA_alias.aa, PackageAlias2.AA_alias.aa_alias, 
 		     
 		   	PackageAlias2.B, PackageAlias2.B.a, PackageAlias2.B.b,  PackageAlias2.B.a_alias,
 		   			   --- */
	classifier test_A specializes A_alias{}
}
 

````
