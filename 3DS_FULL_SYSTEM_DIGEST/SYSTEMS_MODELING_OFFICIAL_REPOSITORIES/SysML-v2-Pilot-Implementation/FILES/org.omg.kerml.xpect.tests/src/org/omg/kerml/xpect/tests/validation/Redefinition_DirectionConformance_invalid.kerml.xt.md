# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Redefinition_DirectionConformance_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Redefinition_DirectionConformance_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Redefinition_DirectionConformance_invalid.kerml.xt
- source_bytes: 1460
- source_sha256: `653eab7f4ea1b058ab9f620f974d3f42e70ccd2fd3e77efc612f7060bf1d3c53`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.validation.KerMLValidationTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/library/Links.kerml"}
		File {from ="/library/Occurrences.kerml"}
		File {from ="/library/Performances.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Links.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Performances.kerml"}
			}
		}
	}
END_SETUP 
*/

package Redefinition_DirectionConformance {
    behavior A {
        in x;
        inout y;
        composite step b : B {
        	// XPECT errors ---> "Redefining feature must have a compatible direction" at "in x1;"
            in x1;
        }
    }
    behavior B specializes A {
    	// XPECT errors ---> "Redefining feature must have a compatible direction" at "out x1;"
        out x1;
        out y1;
    }
    class C {
    	in z;
    }
    class D specializes C {
    	// XPECT errors ---> "Redefining feature must have a compatible direction" at "z"
    	out :>> z;
    }
    feature d : D {
    	// XPECT errors ---> "Redefining feature must have a compatible direction" at "z"
    	in :>> z;
    }
    class C1 conjugates C;
    class D1 specializes C1 {
    	// XPECT errors ---> "Redefining feature must have a compatible direction" at "z"
    	in :>> z;
    }
}
````
