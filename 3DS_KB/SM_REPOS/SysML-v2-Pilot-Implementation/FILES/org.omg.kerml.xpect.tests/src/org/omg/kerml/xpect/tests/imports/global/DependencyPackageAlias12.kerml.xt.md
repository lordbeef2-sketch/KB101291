# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias12.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias12.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias12.kerml.xt
- source_bytes: 1382
- source_sha256: `7d6970497dccb98fd92445a93d0f48b3dc42b4c43b52e70ae0e8ba29e5bd636a`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.global.KerMLImportGlobalTest
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
	//* XPECT scope at PackageAlias1::A ---
	    A, A.a, A.a_alias,  Test1.A, Test1.A.a, Test1.A.a_alias,
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
	public import PackageAlias1::A;
}

````
