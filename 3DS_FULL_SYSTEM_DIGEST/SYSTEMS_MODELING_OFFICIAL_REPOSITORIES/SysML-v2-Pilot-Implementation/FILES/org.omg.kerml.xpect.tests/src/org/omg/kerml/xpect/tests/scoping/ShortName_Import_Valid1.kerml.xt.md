# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Import_Valid1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Import_Valid1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Import_Valid1.kerml.xt
- source_bytes: 1366
- source_sha256: `2d863ba4fccac4344d521734905bfd1d0ba43d9bfeb25276dc46baf2dc3ca383`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.scoping.KerMLScopingTest
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
		public import VP::VP1::*;
		//* XPECT scope at c_Public_Id ---
		A, A.c_public, Test1.A, Test1.A.c_public, Test.Test1.A, Test.Test1.A.c_public, 
		c_Public, Test1.c_Public, Test.Test1.c_Public, VP.VP1.c_Public, Test.VP.VP1.c_Public,  
		c_Public.c_public, Test1.c_Public.c_public, Test.Test1.c_Public.c_public, VP.VP1.c_Public.c_public, Test.VP.VP1.c_Public.c_public,
		c_Public_Id, Test1.c_Public_Id, Test.Test1.c_Public_Id, VP.VP1.c_Public_Id, Test.VP.VP1.c_Public_Id,
		c_Public_Id.c_public, Test1.c_Public_Id.c_public, Test.Test1.c_Public_Id.c_public, VP.VP1.c_Public_Id.c_public, Test.VP.VP1.c_Public_Id.c_public,
		VP.VP2.A, Test.VP.VP2.A, VP.VP2.A_Id, Test.VP.VP2.A_Id
		--- */
		classifier A specializes c_Public_Id;
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
