# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_BadScopeWithOnlyTwoDotAtTheEnd.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_BadScopeWithOnlyTwoDotAtTheEnd.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_BadScopeWithOnlyTwoDotAtTheEnd.kerml.xt
- source_bytes: 661
- source_sha256: `9eee0385ae9fcb95b16a48b3d3c63a79bba64af090f8133ee9611bc5118a1d48`
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
			"Couldn't resolve reference to Type 'Test3::A'." at "Test3::A"
			"Couldn't resolve reference to Type 'a'." at "a"
		--- */
		feature b: Test3::A:a;
	}
}

````
