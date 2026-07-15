# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_PublicImportAsFeatureAlias.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_PublicImportAsFeatureAlias.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_PublicImportAsFeatureAlias.kerml.xt
- source_bytes: 2349
- source_sha256: `b07ad4d4d8fe9c3d38aa1262ce4ca56c6e66c88a9f176ec306670e36e3a5b904`
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
	alias aliass for VisibilityPackage::c_Public::c_public;
	alias Aliass for VisibilityPackage::c_Public;
	classifier Try{
		//scope are the same for at aliass and at Aliass
		//* XPECT scope at aliass ---
			Aliass, Aliass.c_public, Classes.Aliass, Classes.Aliass.c_public, Classes.Try,
			Classes.Try.feature4, Classes.Try.featurepublic, Classes.Try.featurepublic.c_public,
			Classes.Try.self, Classes.Try.self.that, Classes.aliass, Try, Try.feature4, Try.featurepublic,
			Try.featurepublic.c_public, Try.self, Try.self.that, VisibilityPackage.c_Public,
			VisibilityPackage.c_Public.c_public, VisibilityPackage.c_Public_alias,
			VisibilityPackage.c_Public_alias.alias_public, VisibilityPackage.c_Public_alias.c_public, VisibilityPackage.c_clazz,
			VisibilityPackage.c_clazz.c_Public, VisibilityPackage.c_clazz.c_Public.c_publicc, aliass, feature4, featurepublic,
			featurepublic.c_public, self, self.that
		--- */
		//XPECT linkedName at aliass --> VisibilityPackage.c_Public.c_public
		feature feature4 : aliass;
		//XPECT linkedName at Aliass --> VisibilityPackage.c_Public
		//* XPECT scope at Aliass ---
			Aliass, Aliass.c_public, Classes.Aliass, Classes.Aliass.c_public, Classes.Try,
			Classes.Try.feature4, Classes.Try.featurepublic, Classes.Try.featurepublic.c_public,
			Classes.Try.self, Classes.Try.self.that, Classes.aliass, Try, Try.feature4, Try.featurepublic,
			Try.featurepublic.c_public, Try.self, Try.self.that, VisibilityPackage.c_Public,
			VisibilityPackage.c_Public.c_public, VisibilityPackage.c_Public_alias,
			VisibilityPackage.c_Public_alias.alias_public, VisibilityPackage.c_Public_alias.c_public, VisibilityPackage.c_clazz,
			VisibilityPackage.c_clazz.c_Public, VisibilityPackage.c_clazz.c_Public.c_publicc, aliass, feature4, featurepublic,
			featurepublic.c_public, self, self.that
		--- */
		feature featurepublic : Aliass;
	}
}


````
