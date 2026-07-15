# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_3_0.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_3_0.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_3_0.kerml.xt
- source_bytes: 3186
- source_sha256: `7a11f8f588f617432a50791fe763225ffe129caa52fc4b36ded1c469ad99eb78`
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
package Classes {
	public import VisibilityPackage::*;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Private'." at "c_Private"
	feature a : c_Private;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Private::c_private'." at "c_Private::c_private"
	feature b : c_Private::c_private;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Private::c_public'." at "c_Private::c_public"
	feature c : c_Private::c_public;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Public::c_private'." at "c_Public::c_private"
	feature d : c_Public::c_private;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Public::c_protected'." at "c_Public::c_protected"
	feature e : c_Public::c_protected;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Public_alias::alias_private'." at "c_Public_alias::alias_private"
	feature f : c_Public_alias::alias_private;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Public_alias::alias_protected'." at "c_Public_alias::alias_protected"
	feature g : c_Public_alias::alias_protected;	
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Private_alias'." at "c_Private_alias"
	feature h : c_Private_alias;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Private_alias::c_public'." at "c_Private_alias::c_public"
	feature i : c_Private_alias::c_public;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Private_alias::alias_private'." at "c_Private_alias::alias_private"
	feature j : c_Private_alias::alias_private; 
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Private_alias::alias_protected'." at "c_Private_alias::alias_protected"
	feature k : c_Private_alias::alias_protected;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Private_alias::alias_public'." at "c_Private_alias::alias_public"
	feature l : c_Private_alias::alias_public;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_clazz::c_Protect'." at "c_clazz::c_Protect"
	feature m : c_clazz::c_Protect;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_clazz::c_Protect::c_publicc'." at "c_clazz::c_Protect::c_publicc"
	feature n : c_clazz::c_Protect::c_publicc;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_clazz::c_Protect::c_protect'." at "c_clazz::c_Protect::c_protect"
	feature o : c_clazz::c_Protect::c_protect;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_clazz::c_Package'." at "c_clazz::c_Package"
	feature p : c_clazz::c_Package;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_clazz::c_Package::c_publicc'." at "c_clazz::c_Package::c_publicc"
	feature q : c_clazz::c_Package::c_publicc;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_clazz::c_Public::c_protect'." at "c_clazz::c_Public::c_protect"
	feature r : c_clazz::c_Public::c_protect;
}

````
