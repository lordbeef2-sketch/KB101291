# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/AssociationTest_EndRedefinitionGoodCase.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/AssociationTest_EndRedefinitionGoodCase.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/AssociationTest_EndRedefinitionGoodCase.kerml.xt
- source_bytes: 871
- source_sha256: `88dae01b95ad97af0fae22e7397e891f7e3d642432b5052d799f8d380cd8634a`
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
		File {from ="/library/Objects.kerml"}
		File {from ="/library/Performances.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Links.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Objects.kerml"}
				File {from ="/library/Performances.kerml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors --> ""
package test{
	assoc A {
		end x;
		end [1..*] feature y;
	}
	
	assoc B specializes A {
		end x1;
		// Reducing multiplicity lower bound is OK for an end feature.
		end [0..*] feature y1 redefines y;
	}
}

````
