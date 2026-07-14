# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_MultiplicityDeclaration.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_MultiplicityDeclaration.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_MultiplicityDeclaration.kerml.xt
- source_bytes: 622
- source_sha256: `ee19086ca316da440ac1ac3dd7c0697e8990050b9fd046631be596d53754e483`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/library/Occurrences.kerml"}
		File {from ="/library/Performances.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Performances.kerml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package test{
	multiplicity zeroOrMore [0..*];
	multiplicity m subsets zeroOrMore;
	feature f {
		multiplicity [1..1];
	}
}

````
