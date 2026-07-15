# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportClassAndUseAlias2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportClassAndUseAlias2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportClassAndUseAlias2.kerml.xt
- source_bytes: 2161
- source_sha256: `24746b9d8491e49eb37e77d030e40250e5ee96cfd899f5c0e7bd200d6e3abd21`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.visibility.KerMLVisibilityTest
	ResourceSet {
		ThisFile {}
		File  {from ="/src/DependencyVisibilityPackage.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File  {from ="/src/DependencyVisibilityPackage.kerml" }
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors --> ""
package Classes {
	public import VisibilityPackage::*;
	//XPECT linkedName at c_Public_alias::alias_public --> VisibilityPackage.c_Public_alias.c_public
	//* XPECT scope at c_Public_alias::alias_public  ---
    	 Classes.c_Public, Classes.c_Public.c_public, Classes.c_Public_alias,
    Classes.c_Public_alias.alias_public, Classes.c_Public_alias.c_public, Classes.c_clazz, Classes.c_clazz.c_Public,
    Classes.c_clazz.c_Public.c_publicc, Classes.f, VisibilityPackage.c_Public, VisibilityPackage.c_Public.c_public,
    VisibilityPackage.c_Public_alias, VisibilityPackage.c_Public_alias.alias_public,
    VisibilityPackage.c_Public_alias.c_public, VisibilityPackage.c_clazz, VisibilityPackage.c_clazz.c_Public,
    VisibilityPackage.c_clazz.c_Public.c_publicc, c_Public, c_Public.c_public, c_Public_alias, c_Public_alias.alias_public,
    c_Public_alias.c_public, c_clazz, c_clazz.c_Public, c_clazz.c_Public.c_publicc, f
 	--- */
	feature f : c_Public_alias::alias_public;
}


//*
      	VisibilityPackage.c_clazz, VisibilityPackage.c_clazz.c_Public, VisibilityPackage.c_Public, VisibilityPackage.c_Public.c_public, VisibilityPackage.c_Public_alias.alias_public, VisibilityPackage.c_Public_alias.c_public, 
    	VisibilityPackage.c_clazz.c_Protect, VisibilityPackage.c_clazz.c_Protect.c_publicc,  VisibilityPackage.c_clazz.c_Package, VisibilityPackage.c_clazz.c_Package.c_publicc, VisibilityPackage.c_clazz.c_Public.c_packagee, VisibilityPackage.c_clazz.c_Public.c_protect, VisibilityPackage.c_Private, VisibilityPackage.c_Private.c_private, VisibilityPackage.c_Private.c_public, VisibilityPackage.c_Private_alias, VisibilityPackage.c_Private_alias.alias_public, VisibilityPackage.c_Private_alias.c_public, VisibilityPackage.c_Public.c_private, VisibilityPackage.c_Public_alias, 
   
 */

````
