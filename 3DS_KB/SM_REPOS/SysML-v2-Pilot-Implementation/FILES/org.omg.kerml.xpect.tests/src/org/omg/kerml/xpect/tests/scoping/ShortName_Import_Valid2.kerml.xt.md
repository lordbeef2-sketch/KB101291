# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Import_Valid2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Import_Valid2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Import_Valid2.kerml.xt
- source_bytes: 721
- source_sha256: `0a1d2ef269c7e94a137082f386fa3ca9d11d2fa8ab3b2f0021663b8d5c82c7b7`
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
		 A_Id, Test2.A_Id, Test.Test2.A_Id,
		 VP.VP2.A, Test.VP.VP2.A,
		 VP.VP2.A_Id, Test.VP.VP2.A_Id,  
		--- */
		classifier AA specializes A_Id;
	}
	package VP {
		package VP2 {
			public classifier <'A_Id'> A;
		}
	}
	
}

	
````
