# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias0_A.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias0_A.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyPackageAlias0_A.kerml.xt
- source_bytes: 856
- source_sha256: `aa313ae31bc7a4e8edff1a4b897a49272c995f85c3d9de2a3bf6c12c0f5d9b49`
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
	//* XPECT scope at PackageAlias1::A ---
	    test, PackageAlias1,
		A, A.a, A.a_alias,  test.A, test.A.a, test.A.a_alias,   
	   	PackageAlias1.A, PackageAlias1.A.a, PackageAlias1.A.a_alias,
	   	PackageAlias1.AA, PackageAlias1.AA.aa, PackageAlias1.AA.aa_alias,
	   	PackageAlias1.A_alias, PackageAlias1.A_alias.a, PackageAlias1.A_alias.a_alias,
    	PackageAlias1.AA_alias, PackageAlias1.AA_alias.aa, PackageAlias1.AA_alias.aa_alias,
 --- */
 	public import PackageAlias1::A;
}

````
