# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Feature_nonunique_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Feature_nonunique_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Feature_nonunique_invalid.kerml.xt
- source_bytes: 894
- source_sha256: `ff5d58cb11de1705c93e2ca61b4909c692b2a4f21023fda9925f87cff0e80906`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.validation.KerMLValidationTest
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
package Feature_nonunique_invalid {
	classifier A {
		feature x; // "unique" by default
	}
	classifier B specializes A {
		// XPECT errors --> "Subsetting/redefining feature cannot be nonunique if subsetted/redefined feature is unique" at "x"
		feature x1 nonunique subsets x;
	}
	classifier C specializes A {
		// XPECT errors --> "Subsetting/redefining feature cannot be nonunique if subsetted/redefined feature is unique" at "x"
		feature x2 nonunique redefines x;
	}
}
````
