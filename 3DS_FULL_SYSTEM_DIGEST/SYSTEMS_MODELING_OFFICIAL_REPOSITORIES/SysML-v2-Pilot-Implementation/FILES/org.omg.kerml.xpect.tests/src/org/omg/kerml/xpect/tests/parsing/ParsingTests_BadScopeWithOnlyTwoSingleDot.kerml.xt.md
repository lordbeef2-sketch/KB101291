# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_BadScopeWithOnlyTwoSingleDot.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_BadScopeWithOnlyTwoSingleDot.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_BadScopeWithOnlyTwoSingleDot.kerml.xt
- source_bytes: 690
- source_sha256: `0567e5874ef79325d3c252958aade73bc4dc32c0d581d7893e6e531965fe9df8`
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
		"no viable alternative at input '..'" at "test"
		"no viable alternative at input '::'" at "::"
		"no viable alternative at input 'A'" at "A"
		--- */
		feature b: test..A::a;
	}
}


````
