# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_0.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_0.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_0.kerml.xt
- source_bytes: 945
- source_sha256: `91ecaf6e0b01c52ae1f0209e2d2b52e6db401c14aff404e522ef82df1192f0db`
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


package Test3{
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_Private'." at "VisibilityPackage::c_Private"
	public import VisibilityPackage::c_Private::*;
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_Private::c_private'." at "VisibilityPackage::c_Private::c_private"
	public import VisibilityPackage::c_Private::c_private::*;
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_Private::c_public'." at "VisibilityPackage::c_Private::c_public"
	public import VisibilityPackage::c_Private::c_public::*;
}
	

````
