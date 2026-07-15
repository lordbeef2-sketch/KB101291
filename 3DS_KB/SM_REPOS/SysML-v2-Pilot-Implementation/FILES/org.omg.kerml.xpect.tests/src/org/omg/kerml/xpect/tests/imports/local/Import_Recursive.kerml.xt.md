# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/local/Import_Recursive.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/local/Import_Recursive.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/local/Import_Recursive.kerml.xt
- source_bytes: 1745
- source_sha256: `05e526613481a4b3ae4db4e1f9ec0f0a7d89b16fb17feadbecc2854631f50503`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.local.KerMLImportLocalTest
	ResourceSet {
		ThisFile {}
			File {from ="/library/Base.kerml"}
			File {from ="/library/Performances.kerml"}
		    File {from ="/library/ScalarValues.kerml"}
		    File {from ="/library/BaseFunctions.kerml"}
		    File {from ="/library/ControlFunctions.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
			   	File {from ="/library/Performances.kerml"}
		       	File {from ="/library/ScalarValues.kerml"}
		       	File {from ="/library/BaseFunctions.kerml"}
		       	File {from ="/library/ControlFunctions.kerml"}
			}
		}
	}
END_SETUP 
*/

package Import_Recursive {
	package P {
		classifier A {
			classifier A1;
			classifier A2;
			classifier A3;
			classifier A4;
		}
		classifier B {
			classifier B1;
			classifier BB {
				classifier B2;
				classifier B3;
			}
		}
		classifier C {
			classifier C1;
			classifier C2;
			protected classifier C3;
			private classifier C4;
		}
		
		private classifier D {
			classifier D1;
		}
	}
	
	package Q {
		public import P::**; 

		classifier a :> A,A1;   
		classifier b :> A2; 
		classifier c :> A3;  
		classifier d :> A4;  
		classifier f :> B, B1;  
		classifier g :> BB, B2;  
		classifier h :> B3;  
		classifier i :> C, C1;  
		classifier j :> C2;
		
		// XPECT errors ---> "Couldn't resolve reference to Classifier 'C3'." at "C3"
		classifier k :> C3;
		// XPECT errors ---> "Couldn't resolve reference to Classifier 'C4'." at "C4"
		classifier l :> C4;
		// XPECT errors ---> "Couldn't resolve reference to Classifier 'D1'." at "D1"		
		classifier m :> D1;
	}
	
}

	
````
