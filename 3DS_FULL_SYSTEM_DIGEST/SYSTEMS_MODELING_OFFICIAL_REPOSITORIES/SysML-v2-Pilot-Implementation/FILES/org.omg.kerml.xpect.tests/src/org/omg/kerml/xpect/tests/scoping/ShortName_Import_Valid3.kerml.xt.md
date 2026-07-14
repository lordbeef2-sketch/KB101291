# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Import_Valid3.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Import_Valid3.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Import_Valid3.kerml.xt
- source_bytes: 751
- source_sha256: `5c322655efee2e09267773080aab0804388d849aa59aac3d1195c6cbae31d4db`
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

	package Test2 {
		public import VP::VP2::*;
		classifier A;
		//* XPECT scope at A_Id ---
		 A,  Test2.A, Test.Test2.A,
		 AA, Test2.AA, Test.Test2.AA,
		 B, Test2.B, Test.Test2.B,
		 A_Id, Test2.A_Id, Test.Test2.A_Id,
		 VP.VP2.B, Test.VP.VP2.B,
		 VP.VP2.A_Id, Test.VP.VP2.A_Id,  
		--- */
		classifier AA specializes A_Id;
	}
	package VP {
		package VP2 {
			public classifier <'A_Id'> B;
		}
	}
	
}

	
````
