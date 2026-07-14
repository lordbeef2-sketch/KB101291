# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsAlias_Invalid_0.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsAlias_Invalid_0.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsAlias_Invalid_0.kerml.xt
- source_bytes: 772
- source_sha256: `178be3e011dd06cc8fcc8596a4bca1c3997743a190575c2e321d7bcc651144a7`
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
	// XPECT errors ---> "Couldn't resolve reference to Element 'VisibilityPackage::c_Private::c_private'." at "VisibilityPackage::c_Private::c_private"
	alias aliass for VisibilityPackage::c_Private::c_private;
	classifier Try{
		// XPECT errors ---> "Couldn't resolve reference to Type 'aliass'." at "aliass"
		feature feature1 : aliass;
	}
}


````
