# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyVisibilityPackage.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyVisibilityPackage.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencyVisibilityPackage.kerml.xt
- source_bytes: 946
- source_sha256: `20a627bd264244764b1fe018af056ec68172c6f4d32d4311c4ef7d2e3dfaafc2`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.global.KerMLImportGlobalTest
	ResourceSet {
		ThisFile {}
		File {from ="/src/DependencyVisibilityPackage.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/src/DependencyVisibilityPackage.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package Test3{
	//* XPECT scope at VisibilityPackage::c_Public ---
	    c_Public, c_Public.c_public,
	    Test3, Test3.c_Public, Test3.c_Public.c_public,
	    VisibilityPackage, 
	    VisibilityPackage.c_Public,
	    VisibilityPackage.c_Public.c_public, 
	    VisibilityPackage.c_Public_alias,
	    VisibilityPackage.c_Public_alias.alias_public, 
	    VisibilityPackage.c_Public_alias.c_public, 
	    VisibilityPackage.c_clazz,
	    VisibilityPackage.c_clazz.c_Public,
	    VisibilityPackage.c_clazz.c_Public.c_publicc
	--- */
	public import VisibilityPackage::c_Public;
}

````
