# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias0.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias0.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias0.kerml.xt
- source_bytes: 1252
- source_sha256: `4126066e5813357bade761d53275dd7149c4612ab434af80b7aa99b735d8dfe9`
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
	
	public import PackageAlias1::*;
	
	//* XPECT scope at A ---
	    X, X.a, X.a_alias,  test.X, test.X.a, test.X.a_alias,
		A, A.a, A.a_alias,  test.A, test.A.a, test.A.a_alias,   
		AA, AA.aa, AA.aa_alias,  test.AA, test.AA.aa, test.AA.aa_alias,
		A_alias, A_alias.a, A_alias.a_alias,  test.A_alias, test.A_alias.a, test.A_alias.a_alias,
		AA_alias, AA_alias.aa, AA_alias.aa_alias,  test.AA_alias, test.AA_alias.aa, test.AA_alias.aa_alias,
	   	PackageAlias1.A, PackageAlias1.A.a, PackageAlias1.A.a_alias,
	   	PackageAlias1.AA, PackageAlias1.AA.aa, PackageAlias1.AA.aa_alias,
	   	PackageAlias1.A_alias, PackageAlias1.A_alias.a, PackageAlias1.A_alias.a_alias,
    	PackageAlias1.AA_alias, PackageAlias1.AA_alias.aa, PackageAlias1.AA_alias.aa_alias,
 --- */
	classifier X specializes A {}
}

````
