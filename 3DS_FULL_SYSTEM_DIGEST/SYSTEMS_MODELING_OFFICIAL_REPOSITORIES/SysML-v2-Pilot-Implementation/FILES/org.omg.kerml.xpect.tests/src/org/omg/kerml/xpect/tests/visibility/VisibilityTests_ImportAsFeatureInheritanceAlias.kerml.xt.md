# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsFeatureInheritanceAlias.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsFeatureInheritanceAlias.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsFeatureInheritanceAlias.kerml.xt
- source_bytes: 2016
- source_sha256: `13becc7a23e72e7cbc287928f73cdd5e47fbdb5279c99a5a0105582bed1e9be4`
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

// XPECT noErrors ---> " "
package Classes {
	alias aliass for VisibilityPackage::c_Public;
	//XPECT linkedName at aliass --> VisibilityPackage.c_Public
	/* XPECT scope at  aliass ---
	  	 Classes.Try, Classes.Try.c_public, Classes.aliass,	Classes.aliass.c_public, 
	  	 Try, Try.c_public, aliass, aliass.c_public,
	  	 VisibilityPackage.c_clazz, VisibilityPackage.c_clazz.c_Public, VisibilityPackage.c_Public, VisibilityPackage.c_Public.c_public, VisibilityPackage.c_Public_alias.alias_public, VisibilityPackage.c_Public_alias.c_public, 
		 VisibilityPackage.c_Public_alias,VisibilityPackage.c_clazz.c_Public.c_publicc
	--- */
	classifier Try specializes aliass{
		//XPECT linkedName at c_public --> VisibilityPackage.c_Public.c_public
		/* XPECT scope at c_public ---
		Classes.Try, Classes.Try.c_public, Classes.Try.feature4, Classes.Try.self,
		Classes.Try.self.that, Classes.aliass, Classes.aliass.c_public, Try, Try.c_public, Try.feature4,
		Try.self, Try.self.that, VisibilityPackage.c_Public, VisibilityPackage.c_Public.c_public,
		VisibilityPackage.c_Public_alias, VisibilityPackage.c_Public_alias.alias_public,
		VisibilityPackage.c_Public_alias.c_public, VisibilityPackage.c_clazz, VisibilityPackage.c_clazz.c_Public,
		VisibilityPackage.c_clazz.c_Public.c_publicc, aliass, aliass.c_public, c_protected, c_public, feature4, self, self.that
		--- */
		// The following are not visible because qualified names currently require public visibility:
		//  Classes.Try.c_protected, Classes.aliass.c_protected, Try.c_protected, aliass.c_protected
		feature feature4 : c_public;
	}
}


````
