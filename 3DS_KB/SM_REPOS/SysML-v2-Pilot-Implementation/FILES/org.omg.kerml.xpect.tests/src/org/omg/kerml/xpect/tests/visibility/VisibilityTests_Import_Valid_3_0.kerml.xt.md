# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Valid_3_0.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Valid_3_0.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Valid_3_0.kerml.xt
- source_bytes: 681
- source_sha256: `372449c227ebf58b89b7d568b260dc8665ac08023f905a2d6bf57ef5b6535570`
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
//XPECT noErrors ---> ""
package Classes {
	public import VisibilityPackage::*;
	feature a : c_Public;
	feature b : c_Public::c_public;
	feature c : c_Public_alias;
	feature d : c_Public_alias::c_public;
	feature e : c_Public_alias::alias_public;
	feature f : c_clazz;
	feature g : c_clazz::c_Public;	
	feature h : c_clazz::c_Public::c_publicc;
}

````
