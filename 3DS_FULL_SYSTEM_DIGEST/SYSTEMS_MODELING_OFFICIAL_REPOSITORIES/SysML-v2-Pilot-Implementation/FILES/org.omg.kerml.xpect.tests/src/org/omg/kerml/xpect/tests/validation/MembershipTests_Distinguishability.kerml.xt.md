# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MembershipTests_Distinguishability.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MembershipTests_Distinguishability.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MembershipTests_Distinguishability.kerml.xt
- source_bytes: 1058
- source_sha256: `cdf796a0c5983db89243c53e32ca146881fa5640c054eb3726189cea223b831a`
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
	// XPECT warnings ---> "Duplicate of other owned member name" at "A"
	classifier A {}
	// XPECT warnings ---> "Duplicate of other owned member name" at "A"
	package A{
		classifier A {}
		alias A_alias for A;
	}
	// XPECT warnings ---> "Duplicate of other owned member name" at "A"
	package A{}
	// XPECT warnings ---> "Duplicate of other owned member name" at "A"
	feature A: A::A_alias;
	feature B: A::A_alias;
	
	classifier C {
		classifier D {}
		classifier F {}
	}
	classifier D :> C {
		// XPECT warnings --> "Duplicate of inherited member name 'D' from C" at "D"
		classifier D {}
	}
	classifier E :> C;
	classifier F :> E {
		// XPECT warnings --> "Duplicate of inherited member name 'F' from C" at "F"
		classifier F {}
	}	

}

````
