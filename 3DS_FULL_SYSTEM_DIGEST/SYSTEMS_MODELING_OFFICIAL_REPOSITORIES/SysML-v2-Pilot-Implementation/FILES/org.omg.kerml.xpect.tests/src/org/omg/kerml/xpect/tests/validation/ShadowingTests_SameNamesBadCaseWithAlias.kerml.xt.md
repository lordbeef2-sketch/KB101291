# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_SameNamesBadCaseWithAlias.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_SameNamesBadCaseWithAlias.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShadowingTests_SameNamesBadCaseWithAlias.kerml.xt
- source_bytes: 536
- source_sha256: `c7536631be28c0155b3f26ab7762ab97caed484ab59fed8919d008256be2aded`
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
	classifier A{
		classifier a1{}
	}
	classifier B specializes A{
		classifier A{
			classifier a2{}
		}
		// XPECT errors ---> "Couldn't resolve reference to Classifier 'A::a1'." at "A::a1"
		classifier b specializes A::a1{}
	}
}

````
