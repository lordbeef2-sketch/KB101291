# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsAlias_Invalid_2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsAlias_Invalid_2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsAlias_Invalid_2.kerml.xt
- source_bytes: 767
- source_sha256: `1943634ca8901a98ea0703f78055bf98e4451a939a9d9e4048aca83ca1453658`
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

package Classes {
	// XPECT errors ---> "Couldn't resolve reference to Element 'VisibilityPackage::c_Private::c_public'." at "VisibilityPackage::c_Private::c_public"
	alias aliass for VisibilityPackage::c_Private::c_public;
	classifier Try{
		// XPECT errors ---> "Couldn't resolve reference to Type 'aliass'." at "aliass"
		feature feature1 : aliass;
	}
}

````
