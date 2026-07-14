# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Type_Relationships_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Type_Relationships_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Type_Relationships_invalid.kerml.xt
- source_bytes: 1252
- source_sha256: `ce8d252dc80ad97bff9f017d06c8b09e4b7e4a837c7e23d5a7202f45c2bee6d0`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.kerml.xpect.tests.validation.KerMLValidationTest
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
package TypeRelationships {
	classifier A;
	classifier B;
	classifier C;
	
	//* XPECT errors ---
	   "Cannot have only one unioning" at "A"
	   "Cannot have only one intersecting" at "B"
	   "Cannot have only one differencing" at "C"
	   ---
	*/
	classifier X unions A intersects B differences C;
	
	//* XPECT errors ---
	   "Type cannot union with itself" at "Y"
	   "Type cannot intersect with itself" at "Y"
	   "Type cannot difference with itself" at "Y"
	   ---
	*/
	classifier Y unions A, Y intersects B, Y differences C, Y;
	
	feature f {
   		// XPECT errors ---> "Feature cannot have itself in a feature chain" at "h"
		feature h chains f.h;
	}
	
    // XPECT errors ---> "Cannot have only one chaining feature" at "f"
    feature g chains f;
    
}

````
