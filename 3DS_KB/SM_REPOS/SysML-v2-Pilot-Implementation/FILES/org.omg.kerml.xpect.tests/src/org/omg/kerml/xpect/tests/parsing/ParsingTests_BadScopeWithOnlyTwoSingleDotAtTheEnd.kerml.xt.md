# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_BadScopeWithOnlyTwoSingleDotAtTheEnd.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_BadScopeWithOnlyTwoSingleDotAtTheEnd.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_BadScopeWithOnlyTwoSingleDotAtTheEnd.kerml.xt
- source_bytes: 691
- source_sha256: `9d415204ddcf433fd2b1a7de3ec2fcc618038b5b1ffee6973c2c6606d40e7ebe`
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

package test{
	classifier non{}
	classifier A{
		// XPECT errors ---> "Couldn't resolve reference to Feature 'non'." at "non"
		feature aa subsets non;
		feature a: A;
	}
	classifier B{
		//* XPECT errors ---
		"no viable alternative at input '..'" at ".."
		"no viable alternative at input '..'" at "test"
		"no viable alternative at input 'A'" at "A"
		---
		*/
		feature b: test::A..a;
	}
}

````
