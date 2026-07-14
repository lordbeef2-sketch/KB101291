# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive6.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive6.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive6.kerml.xt
- source_bytes: 659
- source_sha256: `8668ab4c26181b46779cb518f272d5436ebb2e4ba158c85059c1fc95eda8bb9b`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.recursive.KerMLImportRecursiveTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors --> ""
package RecursiveImport {
  
  package P {
    classifier C {
    	classifier C1 {
    		classifier C2;
    	}
    }
	package P3 {
		package P4 {
			classifier C5;
		}
	}
  }
  
  public import P::C::**;
  x1: C1;
  x2: C1::C2;
  x3: C2;
  x4: C;
  
  public import P::P3::**;
  x5: C5;
  x6: P3::P4::C5;
	
}

````
