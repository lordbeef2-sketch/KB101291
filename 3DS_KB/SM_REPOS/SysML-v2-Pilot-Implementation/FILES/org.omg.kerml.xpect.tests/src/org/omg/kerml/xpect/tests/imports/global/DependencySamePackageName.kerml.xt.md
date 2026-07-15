# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencySamePackageName.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencySamePackageName.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/global/DependencySamePackageName.kerml.xt
- source_bytes: 1081
- source_sha256: `965b36124ef9df7ba81846181f097016b2c7d909c89c435323237374c7412fc7`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.global.KerMLImportGlobalTest
	ResourceSet {
		ThisFile {}
		File {from ="/src/DependencySamePackageName_A.kerml" }
		File {from ="/src/DependencySamePackageName_B.kerml" }
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/src/DependencySamePackageName_A.kerml" }
				File {from ="/src/DependencySamePackageName_B.kerml" }
			}
		}
	}
END_SETUP 
*/
//Both DepedencySamePackageName_A and DependencySamePackageName_B have the same package names "SamePackage"
//What global scope should be?????
// XPECT noErrors ---> ""
package test{
	//* XPECT scope at SamePackage::container ---
		test, 
	    container, container.A, test.container, test.container.A,
	    SamePackage, SamePackage, 
	    SamePackage.container, SamePackage.container, SamePackage.container.A,	SamePackage.container.B, 
	--- */
	public import SamePackage::container;
	
}
//*
package SamePackage{
	class container{
	class A{}
	}
}
package SamePackage{
	class container{
	class B{}
	}
}

*/


````
