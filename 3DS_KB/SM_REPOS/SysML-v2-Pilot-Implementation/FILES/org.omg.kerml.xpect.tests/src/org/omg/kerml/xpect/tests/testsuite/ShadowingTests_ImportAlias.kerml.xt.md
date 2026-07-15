# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAlias.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAlias.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAlias.kerml.xt
- source_bytes: 1368
- source_sha256: `1ae3eefbfb7bc2f2b47a8576aee3d3db3dba36d21ed9298c374e08a240a557fa`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/src/DependencyPackageAlias1.kerml"}
		File {from ="/src/DependencyPackageAlias2.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/src/DependencyPackageAlias1.kerml"}
				File {from ="/src/DependencyPackageAlias2.kerml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package Test1{
	//* XPECT scope at PackageAlias1::A_alias ---
	    a, a_alias,  Test1.a, Test1.a_alias,
	    PackageAlias1, PackageAlias2, Test1,
	   	PackageAlias1.A, PackageAlias1.A.a, PackageAlias1.A.a_alias,
	   	PackageAlias1.AA, PackageAlias1.AA.aa, PackageAlias1.AA.aa_alias,
	   	PackageAlias1.A_alias, PackageAlias1.A_alias.a, PackageAlias1.A_alias.a_alias,
    	PackageAlias1.AA_alias, PackageAlias1.AA_alias.aa, PackageAlias1.AA_alias.aa_alias, 
    	PackageAlias2.A, PackageAlias2.A.a, PackageAlias2.A.a_alias,
	   	PackageAlias2.AA, PackageAlias2.AA.aa, PackageAlias2.AA.aa_alias,
	   	PackageAlias2.A_alias, PackageAlias2.A_alias.a, PackageAlias2.A_alias.a_alias,
    	PackageAlias2.AA_alias, PackageAlias2.AA_alias.aa, PackageAlias2.AA_alias.aa_alias,
    	PackageAlias2.B, PackageAlias2.B.a, PackageAlias2.B.a_alias, PackageAlias2.B.b,  
 --- */
	
	public import PackageAlias1::A_alias::*;
}

````
