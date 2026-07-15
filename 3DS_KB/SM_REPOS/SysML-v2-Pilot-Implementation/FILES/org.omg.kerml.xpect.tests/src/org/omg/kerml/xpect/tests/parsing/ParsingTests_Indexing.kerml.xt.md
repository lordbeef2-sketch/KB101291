# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Indexing.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Indexing.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Indexing.kerml.xt
- source_bytes: 1320
- source_sha256: `ced970a836e6142c4cb8122a4b22c443e0f50a695ce5ed9e0e36069f3d4ac334`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/library/Links.kerml"}
		File {from ="/library/Occurrences.kerml"}
		File {from ="/library/Performances.kerml"}
		File {from ="/library/ScalarValues.kerml"}
		File {from ="/library/Collections.kerml"}
		File {from ="/library/BaseFunctions.kerml"}
		File {from ="/library/ControlFunctions.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Links.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Performances.kerml"}
				File {from ="/library/ScalarValues.kerml"}
				File {from ="/library/Collections.kerml"}
				File {from ="/library/BaseFunctions.kerml"}
				File {from ="/library/ControlFunctions.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package Indexing {
	classifier A {
	  feature b : B;
	}
	classifier B {
	  feature c;
	}
	feature a : A[*];
	feature b = a#(1).b;
	feature c = b.c;
	
	feature arr : Collections::Array {
	  :>> dimensions = (2, 3);
	  :>> elements = ("a", "b", "c",
	                  "x", "y", "z");
	}
	feature arr13 = arr#(1,3);
	feature arr22 = arr#(2,2);
}

````
