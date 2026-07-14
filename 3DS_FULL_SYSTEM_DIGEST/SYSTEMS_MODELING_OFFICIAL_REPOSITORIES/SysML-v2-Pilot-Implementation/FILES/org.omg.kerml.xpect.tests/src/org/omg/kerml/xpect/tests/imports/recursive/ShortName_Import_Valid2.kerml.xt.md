# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/ShortName_Import_Valid2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/ShortName_Import_Valid2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/ShortName_Import_Valid2.kerml.xt
- source_bytes: 967
- source_sha256: `9419a7bc8bc3ed657b59699b1f27d4450c3b3f5fb88b0f4ca438831874cdbf22`
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
package Test {

	package Test1 {
		public import VP::**;

		classifier A specializes c_Public_Id;
		//XPECT linkedName at A --> Test.Test1.A
		classifier B specializes A;
		
		//XPECT linkedName at VP2::A --> Test.VP.VP2.A
		classifier C specializes VP2::A;

		//XPECT linkedName at A_Id --> Test.VP.VP2.A
		classifier D specializes A_Id;
	
	}

	package VP {
			
		package VP1 {	
			public classifier <'c_Public_Id'> c_Public {
				private classifier c_private{}
				public classifier c_public{}
				protected classifier c_protected{}
			}
		}
		
		package VP2 {
			public classifier <'A_Id'> A;
		}
	}
	
}

	
````
