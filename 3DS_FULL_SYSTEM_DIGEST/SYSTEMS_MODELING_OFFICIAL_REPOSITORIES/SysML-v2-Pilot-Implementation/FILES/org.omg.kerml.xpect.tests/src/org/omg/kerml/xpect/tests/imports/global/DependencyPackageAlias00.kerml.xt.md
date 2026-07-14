# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias00.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias00.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias00.kerml.xt
- source_bytes: 1431
- source_sha256: `989e31c14e286e8db6897694a3659d4201b5697e43ccb3a7d33a832830500f49`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.global.KerMLImportGlobalTest
	ResourceSet {
		ThisFile {}
		File {from ="/src/DependencyPackageAlias1.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/src/DependencyPackageAlias1.kerml"}
			}
		}
	}
END_SETUP 
*/
//
// XPECT noErrors ---> ""
package test{
 	public import PackageAlias1;
	//* XPECT scope at PackageAlias1::A::a ---
	   	PackageAlias1, PackageAlias1.A, PackageAlias1.A.a, PackageAlias1.A.a_alias,
	   	PackageAlias1.AA, PackageAlias1.AA.aa, PackageAlias1.AA.aa_alias,
	   	PackageAlias1.A_alias, PackageAlias1.A_alias.a, PackageAlias1.A_alias.a_alias,
    	PackageAlias1.AA_alias, PackageAlias1.AA_alias.aa, PackageAlias1.AA_alias.aa_alias,
    	
	    test, test.PackageAlias1,
    	test.PackageAlias1.A, test.PackageAlias1.A.a, test.PackageAlias1.A.a_alias,
	   	test.PackageAlias1.AA, test.PackageAlias1.AA.aa, test.PackageAlias1.AA.aa_alias,
	   	test.PackageAlias1.A_alias, test.PackageAlias1.A_alias.a, test.PackageAlias1.A_alias.a_alias,
    	test.PackageAlias1.AA_alias, test.PackageAlias1.AA_alias.aa, test.PackageAlias1.AA_alias.aa_alias,
 --- */
 	public import PackageAlias1::A::a::*;
}
//*
package PackageAlias1{
	alias A_alias for A;
	class A{
		class a{}
			alias a_alias for a;
	}
	alias AA_alias for AA;
	class AA{
		class aa{}
		alias aa_alias for aa;
	}
}*/


````
