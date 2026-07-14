# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsAlias_Invalid_1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsAlias_Invalid_1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsAlias_Invalid_1.kerml.xt
- source_bytes: 767
- source_sha256: `0e58ced5449d3c2d863333afef7af781a48583e026c248bcdef20fc38203ca05`
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
	// XPECT errors ---> "Couldn't resolve reference to Element 'VisibilityPackage::c_Public::c_private'." at "VisibilityPackage::c_Public::c_private"
	alias aliass for VisibilityPackage::c_Public::c_private;
	classifier Try{
		// XPECT errors ---> "Couldn't resolve reference to Type 'aliass'." at "aliass"
		feature feature1 : aliass;
	}
}

````
