# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_PublicPackImport.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_PublicPackImport.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_PublicPackImport.kerml.xt
- source_bytes: 953
- source_sha256: `7af2f46d0e82dcd625327ee527c0261e8ee9c5bdf6bbf2e567a78723442b6696`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.visibility.KerMLVisibilityTest
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
	public import VisibilityPackage::c_Public::*;
	//XPECT linkedName at c_public --> VisibilityPackage.c_Public.c_public
	//* XPECT scope at c_public ---
		   c_public, f,
		   Test3.c_public, Test3.f, 
			 
			VisibilityPackage.c_Public_alias.alias_public,
			VisibilityPackage.c_Public, 
			
			VisibilityPackage.c_Public.c_public, 
			VisibilityPackage.c_Public_alias, 
			VisibilityPackage.c_Public_alias.c_public,
			VisibilityPackage.c_clazz, 
			VisibilityPackage.c_clazz.c_Public,
			VisibilityPackage.c_clazz.c_Public.c_publicc
	--- */
	feature f : c_public;
}

````
