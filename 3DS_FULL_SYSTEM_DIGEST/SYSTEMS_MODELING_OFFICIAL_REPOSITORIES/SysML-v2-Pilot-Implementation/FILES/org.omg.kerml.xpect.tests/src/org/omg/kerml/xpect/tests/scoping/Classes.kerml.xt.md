# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/Classes.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/Classes.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/Classes.kerml.xt
- source_bytes: 544
- source_sha256: `97b7da0521cbf2156d8069be7d75b712462bf956275a3a7922d11c541c37a276`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.scoping.KerMLScopingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File "Classes2.kerml" {}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File "Classes2.kerml" {}
			}
		}
	}
END_SETUP 
*/

package Classes1 {
public import Classes2::*;
	// XPECT scope at A --> A, A_Id, B, Classes1.A, Classes1.A_Id, Classes2.A, Classes2.A_Id
	private classifier B specializes A {
		private y: A;
	} 
	
}

````
