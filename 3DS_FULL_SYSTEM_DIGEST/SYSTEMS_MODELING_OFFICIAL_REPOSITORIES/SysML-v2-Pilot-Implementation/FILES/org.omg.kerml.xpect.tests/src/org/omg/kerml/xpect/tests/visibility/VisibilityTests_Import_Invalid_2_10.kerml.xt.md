# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_10.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_10.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_10.kerml.xt
- source_bytes: 913
- source_sha256: `26b6f42347d1633e16dd9dcdc56e302c4624e42a67156b645468da45a42f9feb`
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
	// XPECT errors --> "Couldn't resolve reference to Membership 'VisibilityPackage::c_Private'." at "VisibilityPackage::c_Private"
	public import VisibilityPackage::c_Private;
	// XPECT errors --> "Couldn't resolve reference to Classifier 'c_Private::c_private'." at "c_Private::c_private"
	classifier try specializes c_Private::c_private{}
	// XPECT errors --> "Couldn't resolve reference to Type 'c_Private::c_private'." at "c_Private::c_private"
	feature f : c_Private::c_private;
}

````
