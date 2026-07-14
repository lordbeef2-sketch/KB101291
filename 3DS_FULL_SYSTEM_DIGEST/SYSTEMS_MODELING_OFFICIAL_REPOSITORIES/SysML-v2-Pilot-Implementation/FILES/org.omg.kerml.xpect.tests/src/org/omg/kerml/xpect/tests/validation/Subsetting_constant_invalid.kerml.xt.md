# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Subsetting_constant_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Subsetting_constant_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Subsetting_constant_invalid.kerml.xt
- source_bytes: 872
- source_sha256: `020510b80e91ec0be844ef2a142279c3f1e80a5366edfb5bb1aedc87f20975f6`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/library/Occurrences.kerml"}
		File {from ="/library/Objects.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Objects.kerml"}
			}
		}
	}
END_SETUP 
*/
package Subsetting_constant_invalid {
	
	class A {
		const feature f;
		// XPECT errors--->"Subsetting/redefining feature must be constant if subsetted/redefined feature is constant" at "f"
		var feature g :> f;
	}
	
	class B :> A {
		// XPECT errors--->"Subsetting/redefining feature must be constant if subsetted/redefined feature is constant" at "f"
		var feature h :>> f;
		var feature i :> g;
	}

}

````
