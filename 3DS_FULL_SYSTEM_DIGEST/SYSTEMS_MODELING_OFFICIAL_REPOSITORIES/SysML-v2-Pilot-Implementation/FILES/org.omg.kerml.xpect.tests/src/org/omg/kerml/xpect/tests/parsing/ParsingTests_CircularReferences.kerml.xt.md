# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_CircularReferences.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_CircularReferences.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_CircularReferences.kerml.xt
- source_bytes: 749
- source_sha256: `0c1a7ab536931c025436c45108fc0c83c7b4de5beae653f2a43455efb654ec94`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
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
package Test {
	package Circular {
		classifier A { 
			public import A::*;
			feature a: A;
		}

		alias Circ for Circular;
		package P {
			public import Circular::*;
		}
		
		classifier B :> B;		
		feature b :> b;
		
		// XPECT errors ---> "Must directly or indirectly specialize Base::Anything" at "classifier C ~ C;"
		classifier C ~ C;
		
		// XPECT errors ---> "Features must have at least one type" at "feature c ~ c;"
		feature c ~ c;
	}
}

````
