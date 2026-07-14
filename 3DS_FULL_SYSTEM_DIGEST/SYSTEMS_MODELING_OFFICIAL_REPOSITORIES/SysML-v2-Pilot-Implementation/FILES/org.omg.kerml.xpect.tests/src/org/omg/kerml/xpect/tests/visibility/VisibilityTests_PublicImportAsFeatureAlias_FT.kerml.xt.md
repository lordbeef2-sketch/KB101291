# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_PublicImportAsFeatureAlias_FT.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_PublicImportAsFeatureAlias_FT.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_PublicImportAsFeatureAlias_FT.kerml.xt
- source_bytes: 6552
- source_sha256: `6915b319e5ecbcb5f5405392a76997c98334f5f6b8d623532b7cffe0d90f195d`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.visibility.KerMLVisibilityTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyVisibilityPackage_Feature.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyVisibilityPackage_Feature.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package Classes {
	alias aliass for VisibilityPackage::c_Public::c_public;
	alias Aliass for VisibilityPackage::c_Public;
	feature Try{
		//scope are the same for at aliass and at Aliass
		//* XPECT scope at aliass ---
		Aliass, Aliass.c_public, Aliass.c_public.self, Aliass.c_public.that,
		Aliass.c_public.that.self, Aliass.self, Aliass.that, Aliass.that.self, Classes.Aliass,
		Classes.Aliass.c_public, Classes.Aliass.c_public.self, Classes.Aliass.c_public.that,
		Classes.Aliass.c_public.that.self, Classes.Aliass.self, Classes.Aliass.that, Classes.Aliass.that.self,
		Classes.Try, Classes.Try.feature4, Classes.Try.feature4.self, Classes.Try.feature4.that,
		Classes.Try.feature4.that.self, Classes.Try.featurepublic, Classes.Try.featurepublic.c_public,
		Classes.Try.featurepublic.c_public.self, Classes.Try.featurepublic.c_public.that,
		Classes.Try.featurepublic.c_public.that.self, Classes.Try.featurepublic.self, Classes.Try.featurepublic.that,
		Classes.Try.featurepublic.that.self, Classes.Try.self, Classes.Try.that, Classes.Try.that.self, Classes.aliass,
		Classes.aliass.self, Classes.aliass.that, Classes.aliass.that.self, Try, Try.feature4,
		Try.feature4.self, Try.feature4.that, Try.feature4.that.self, Try.featurepublic,
		Try.featurepublic.c_public, Try.featurepublic.c_public.self, Try.featurepublic.c_public.that,
		Try.featurepublic.c_public.that.self, Try.featurepublic.self, Try.featurepublic.that, Try.featurepublic.that.self,
		Try.self, Try.that, Try.that.self, VisibilityPackage.c_Public,
		VisibilityPackage.c_Public.c_public, VisibilityPackage.c_Public.c_public.self,
		VisibilityPackage.c_Public.c_public.that, VisibilityPackage.c_Public.c_public.that.self, VisibilityPackage.c_Public.self,
		VisibilityPackage.c_Public.that, VisibilityPackage.c_Public.that.self, VisibilityPackage.c_Public_alias,
		VisibilityPackage.c_Public_alias.alias_public, VisibilityPackage.c_Public_alias.alias_public.self,
		VisibilityPackage.c_Public_alias.alias_public.that, VisibilityPackage.c_Public_alias.alias_public.that.self,
		VisibilityPackage.c_Public_alias.c_public, VisibilityPackage.c_Public_alias.c_public.self,
		VisibilityPackage.c_Public_alias.c_public.that, VisibilityPackage.c_Public_alias.c_public.that.self,
		VisibilityPackage.c_Public_alias.self, VisibilityPackage.c_Public_alias.that,
		VisibilityPackage.c_Public_alias.that.self, VisibilityPackage.c_clazz, VisibilityPackage.c_clazz.c_Public,
		VisibilityPackage.c_clazz.c_Public.self, VisibilityPackage.c_clazz.c_Public.that,
		VisibilityPackage.c_clazz.c_Public.that.self, VisibilityPackage.c_clazz.self, VisibilityPackage.c_clazz.that,
		VisibilityPackage.c_clazz.that.self, aliass, aliass.self, aliass.that, aliass.that.self, feature4, feature4.self,
		feature4.that, feature4.that.self, featurepublic, featurepublic.c_public,
		featurepublic.c_public.self, featurepublic.c_public.that, featurepublic.c_public.that.self,
		featurepublic.self, featurepublic.that, featurepublic.that.self, self, that, that.self
		--- */
		//XPECT linkedName at aliass --> VisibilityPackage.c_Public.c_public
		feature feature4 : aliass;
		//XPECT linkedName at Aliass --> VisibilityPackage.c_Public
		//* XPECT scope at Aliass ---
		Aliass, Aliass.c_public, Aliass.c_public.self, Aliass.c_public.that,
		Aliass.c_public.that.self, Aliass.self, Aliass.that, Aliass.that.self, Classes.Aliass,
		Classes.Aliass.c_public, Classes.Aliass.c_public.self, Classes.Aliass.c_public.that,
		Classes.Aliass.c_public.that.self, Classes.Aliass.self, Classes.Aliass.that, Classes.Aliass.that.self,
		Classes.Try, Classes.Try.feature4, Classes.Try.feature4.self, Classes.Try.feature4.that,
		Classes.Try.feature4.that.self, Classes.Try.featurepublic, Classes.Try.featurepublic.c_public,
		Classes.Try.featurepublic.c_public.self, Classes.Try.featurepublic.c_public.that,
		Classes.Try.featurepublic.c_public.that.self, Classes.Try.featurepublic.self, Classes.Try.featurepublic.that,
		Classes.Try.featurepublic.that.self, Classes.Try.self, Classes.Try.that, Classes.Try.that.self, Classes.aliass,
		Classes.aliass.self, Classes.aliass.that, Classes.aliass.that.self, Try, Try.feature4,
		Try.feature4.self, Try.feature4.that, Try.feature4.that.self, Try.featurepublic,
		Try.featurepublic.c_public, Try.featurepublic.c_public.self, Try.featurepublic.c_public.that,
		Try.featurepublic.c_public.that.self, Try.featurepublic.self, Try.featurepublic.that, Try.featurepublic.that.self,
		Try.self, Try.that, Try.that.self, VisibilityPackage.c_Public,
		VisibilityPackage.c_Public.c_public, VisibilityPackage.c_Public.c_public.self,
		VisibilityPackage.c_Public.c_public.that, VisibilityPackage.c_Public.c_public.that.self, VisibilityPackage.c_Public.self,
		VisibilityPackage.c_Public.that, VisibilityPackage.c_Public.that.self, VisibilityPackage.c_Public_alias,
		VisibilityPackage.c_Public_alias.alias_public, VisibilityPackage.c_Public_alias.alias_public.self,
		VisibilityPackage.c_Public_alias.alias_public.that, VisibilityPackage.c_Public_alias.alias_public.that.self,
		VisibilityPackage.c_Public_alias.c_public, VisibilityPackage.c_Public_alias.c_public.self,
		VisibilityPackage.c_Public_alias.c_public.that, VisibilityPackage.c_Public_alias.c_public.that.self,
		VisibilityPackage.c_Public_alias.self, VisibilityPackage.c_Public_alias.that,
		VisibilityPackage.c_Public_alias.that.self, VisibilityPackage.c_clazz, VisibilityPackage.c_clazz.c_Public,
		VisibilityPackage.c_clazz.c_Public.self, VisibilityPackage.c_clazz.c_Public.that,
		VisibilityPackage.c_clazz.c_Public.that.self, VisibilityPackage.c_clazz.self, VisibilityPackage.c_clazz.that,
		VisibilityPackage.c_clazz.that.self, aliass, aliass.self, aliass.that, aliass.that.self, feature4, feature4.self,
		feature4.that, feature4.that.self, featurepublic, featurepublic.c_public,
		featurepublic.c_public.self, featurepublic.c_public.that, featurepublic.c_public.that.self,
		featurepublic.self, featurepublic.that, featurepublic.that.self, self, that, that.self
		--- */		
		feature featurepublic : Aliass;
	}
}


````
