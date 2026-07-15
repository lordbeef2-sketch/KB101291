# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ResultExpressionMembership_Invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ResultExpressionMembership_Invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ResultExpressionMembership_Invalid.kerml.xt
- source_bytes: 864
- source_sha256: `d90b04c23281a03b7a42c705d54c5fc86ed0148c7aa33dcc0341e73f4979134a`
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
				File {from ="/library/Occurrences.kerml"}
       			File {from ="/library/Performances.kerml"}
			}
		}
	}
END_SETUP 
*/
package ResultExpressionMembersio_invalid {
	function F {
		1
	}
	function G :> F {
		//XPECT errors --> "Only one (owned or inherited) result expression is allowed" at "2"
		2
	}
	
	expr f : F {
		//XPECT errors --> "Only one (owned or inherited) result expression is allowed" at "1"
		1
	}
	//XPECT errors --> "Only one (owned or inherited) result expression is allowed" at "expr g :> f;"
	expr g :> f;
}

````
