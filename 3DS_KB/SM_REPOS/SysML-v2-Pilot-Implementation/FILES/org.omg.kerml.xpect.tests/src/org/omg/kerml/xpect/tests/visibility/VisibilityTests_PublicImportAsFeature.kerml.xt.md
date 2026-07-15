# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_PublicImportAsFeature.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_PublicImportAsFeature.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_PublicImportAsFeature.kerml.xt
- source_bytes: 2476
- source_sha256: `7a638ca3d65df0b981235ec3dfade2f8bfa17dac194ea34a6d03f45f4d37e1bd`
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
	public import VisibilityPackage::c_Public::c_public ;
	public import VisibilityPackage::c_Public;
	classifier Try{
		//XPECT linkedName at c_public --> VisibilityPackage.c_Public.c_public
		// The below pass the junit test but if change scope at VisibilityPackage.c_Private get an Error "Reference type is not visible in this scope." 
		//* XPECT scope at c_public ---
			Classes.Try, Classes.Try.feature4, Classes.Try.featurepublic,
			Classes.Try.featurepublic.c_public, Classes.Try.self, Classes.Try.self.that, Classes.c_Public,
			Classes.c_Public.c_public, Classes.c_public, Try, Try.feature4, Try.featurepublic,
			Try.featurepublic.c_public, Try.self, Try.self.that, VisibilityPackage.c_Public,
			VisibilityPackage.c_Public.c_public, VisibilityPackage.c_Public_alias,
			VisibilityPackage.c_Public_alias.alias_public, VisibilityPackage.c_Public_alias.c_public, VisibilityPackage.c_clazz,
			VisibilityPackage.c_clazz.c_Public, VisibilityPackage.c_clazz.c_Public.c_publicc, c_Public, c_Public.c_public,
			c_public, feature4, featurepublic, featurepublic.c_public, self, self.that
		--- */
		feature feature4 : c_public;
		//XPECT linkedName at c_Public --> VisibilityPackage.c_Public
		//* XPECT scope at c_Public ---
			Classes.Try, Classes.Try.feature4, Classes.Try.featurepublic,
			Classes.Try.featurepublic.c_public, Classes.Try.self, Classes.Try.self.that, Classes.c_Public,
			Classes.c_Public.c_public, Classes.c_public, Try, Try.feature4, Try.featurepublic,
			Try.featurepublic.c_public, Try.self, Try.self.that, VisibilityPackage.c_Public,
			VisibilityPackage.c_Public.c_public, VisibilityPackage.c_Public_alias,
			VisibilityPackage.c_Public_alias.alias_public, VisibilityPackage.c_Public_alias.c_public, VisibilityPackage.c_clazz,
			VisibilityPackage.c_clazz.c_Public, VisibilityPackage.c_clazz.c_Public.c_publicc, c_Public, c_Public.c_public,
			c_public, feature4, featurepublic, featurepublic.c_public, self, self.that
		--- */
		feature featurepublic : c_Public;
	}
}


````
