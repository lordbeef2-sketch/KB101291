# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive2.kerml.xt
- source_bytes: 789
- source_sha256: `cf37ff462eaca12a82f5126f39bb66d163d6a06725a7cc0d8cc1f5ff3765ada2`
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
     classifier X;
    package Q {
       classifier Y;
      package R {
         classifier Z;
      }
    }
    package S {
       classifier S1;
      package T {
         classifier T1;
        package U {
        	 classifier U1;
        }
      }
    }
    
  }
 
   	public import P::**;

	//All X, Y and Z are visible here.
	 x: X;	
	 y: Y;
	 z: Z;
	 s: S1;
	 t: T1;
	 u: U1;
	
}

````
