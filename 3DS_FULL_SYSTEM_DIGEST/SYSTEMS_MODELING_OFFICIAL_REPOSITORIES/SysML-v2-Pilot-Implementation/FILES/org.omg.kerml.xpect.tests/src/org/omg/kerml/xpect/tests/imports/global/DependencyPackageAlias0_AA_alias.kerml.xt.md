# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias0_AA_alias.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias0_AA_alias.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias0_AA_alias.kerml.xt
- source_bytes: 1180
- source_sha256: `0e1afaa3252579231cabfbff1f24cb6e76c37cafd2c80986ca44dd15cc543220`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.global.KerMLImportGlobalTest
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
//
// XPECT noErrors ---> ""
package test{
	//* XPECT scope at PackageAlias1::AA_alias ---
	    test, PackageAlias1,
		AA_alias, AA_alias.aa, AA_alias.aa_alias,  test.AA_alias, test.AA_alias.aa, test.AA_alias.aa_alias,
	   	PackageAlias1.A, PackageAlias1.A.a, PackageAlias1.A.a_alias,
	   	PackageAlias1.AA, PackageAlias1.AA.aa, PackageAlias1.AA.aa_alias,
	   	PackageAlias1.A_alias, PackageAlias1.A_alias.a, PackageAlias1.A_alias.a_alias,
    	PackageAlias1.AA_alias, PackageAlias1.AA_alias.aa, PackageAlias1.AA_alias.aa_alias,
 --- */
	public import PackageAlias1::AA_alias;
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
}
*/
````
