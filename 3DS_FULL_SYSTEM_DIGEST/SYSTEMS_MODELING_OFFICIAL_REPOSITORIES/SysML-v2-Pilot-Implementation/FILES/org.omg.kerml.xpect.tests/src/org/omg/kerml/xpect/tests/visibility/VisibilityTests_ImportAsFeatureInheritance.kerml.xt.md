# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsFeatureInheritance.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsFeatureInheritance.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsFeatureInheritance.kerml.xt
- source_bytes: 2053
- source_sha256: `946447f82680d03da4dd090f671e48c214ee3950ee7904d01323c6b84174de1d`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.visibility.KerMLVisibilityTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyVisibilityPackage.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyVisibilityPackage.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package Classes {
	public import VisibilityPackage::c_Public;
	//XPECT linkedName at c_Public --> VisibilityPackage.c_Public
	/* XPECT scope at c_Public ---
	    Try, Try.c_public, Classes.Try, Classes.Try.c_public,
 		c_Public, c_Public.c_public, Classes.c_Public, Classes.c_Public.c_public,  
	  	VisibilityPackage.c_Public_alias.alias_public, 
	  	VisibilityPackage.c_Public, VisibilityPackage.c_Public.c_public, VisibilityPackage.c_Public_alias, VisibilityPackage.c_Public_alias.c_public,
	   	VisibilityPackage.c_clazz, VisibilityPackage.c_clazz.c_Public,  VisibilityPackage.c_clazz.c_Public.c_publicc
	--- */
	classifier Try specializes c_Public {
		//XPECT linkedName at c_public --> VisibilityPackage.c_Public.c_public
		/* XPECT scope at c_public ---
		Classes.Try, Classes.Try.c_public, Classes.Try.feature4, Classes.Try.self,
		Classes.Try.self.that, Classes.c_Public, Classes.c_Public.c_public, Try, Try.c_public, Try.feature4,
		Try.self, Try.self.that, VisibilityPackage.c_Public, VisibilityPackage.c_Public.c_public,
		VisibilityPackage.c_Public_alias, VisibilityPackage.c_Public_alias.alias_public,
		VisibilityPackage.c_Public_alias.c_public, VisibilityPackage.c_clazz, VisibilityPackage.c_clazz.c_Public,
		VisibilityPackage.c_clazz.c_Public.c_publicc, c_Public, c_Public.c_public, c_protected, c_public, feature4, self, self.that
		--- */
		// The following are not visible because qualified names currently require public visibility:
		//  Classes.Try.c_protected, Classes.c_Public.c_protected, 
		//  Try.c_protected, c_Public.c_protected
		feature feature4 : c_public;
	}
}


````
