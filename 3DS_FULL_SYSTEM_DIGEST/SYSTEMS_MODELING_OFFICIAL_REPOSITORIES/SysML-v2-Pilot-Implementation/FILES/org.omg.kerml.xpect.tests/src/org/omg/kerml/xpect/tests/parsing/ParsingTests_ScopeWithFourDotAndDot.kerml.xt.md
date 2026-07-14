# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_ScopeWithFourDotAndDot.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_ScopeWithFourDotAndDot.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_ScopeWithFourDotAndDot.kerml.xt
- source_bytes: 633
- source_sha256: `7d5f37141a765f2723672798d61738a8b0dbb714f3128356c7cc5a8da090cf29`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyOuterPackage.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyOuterPackage.kerml"}
			}
		}
	}
END_SETUP 
*/

package test{
	classifier C{
		//* XPECT errors ---
		"Couldn't resolve reference to Feature 'OuterPackage::B'." at "OuterPackage::B"
		"Couldn't resolve reference to Feature 'b'." at "b"
		---
		*/
		feature c : OuterPackage::B.b;
	}
}

````
