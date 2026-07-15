# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/FeatureChain_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/FeatureChain_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/FeatureChain_invalid.kerml.xt
- source_bytes: 2647
- source_sha256: `10f55931372055acff937f5c2960e5fec4b7cf1050f27a8009c8d0af40c36fe6`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.kerml.xpect.tests.validation.KerMLValidationTest
        ResourceSet {
                ThisFile {}
                File {from ="/library/Base.kerml"}
                File {from ="/library/Links.kerml"}
                File {from ="/library/Occurrences.kerml"}
                File {from ="/library/Objects.kerml"}
                File {from ="/library/Performances.kerml"}
                File {from ="/library/ScalarValues.kerml"}
                File {from ="/library/BaseFunctions.kerml"}
                File {from ="/library/DataFunctions.kerml"}
                File {from ="/library/ControlFunctions.kerml"}
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
                                File {from ="/library/ScalarValues.kerml"}
                                File {from ="/library/BaseFunctions.kerml"}
                                File {from ="/library/DataFunctions.kerml"}
                				File {from ="/library/ControlFunctions.kerml"}
                        }
                }
        }
END_SETUP
*/
package P {
    public import ScalarValues::*;
    
    struct V {
    	feature n : Integer;
    	feature m : Real;
    	struct S;
    }
    
    feature v1 : V {
    	feature redefines n;
    }
    
    feature v2 :> v1 {
    	feature redefines m {
    		feature mm;
    	}
    }
    
    // XPECT errors --> "Must be an accessible feature (use dot notation for nesting)" at "v1::n"
    feature v1_n : Integer = v1::n;
    // XPECT errors --> "Must be an accessible feature (use dot notation for nesting)" at "v1::m"
    feature v1_m : Real = v1::m;
    // XPECT errors ---> "Must be an accessible feature (use dot notation for nesting)" at "v2::m"
    feature v2_m : Real = v1.n + v2::m;
    
    // XPECT errors ---> "Must be a valid feature" at "m::mm"
	feature v2_m_mm = v2.m::mm;
    // XPECT errors ---> "Must be a valid feature" at "S"
    feature v1_S : Integer = v1.S;    
    // XPECT errors ---> "Must be a valid feature" at "V"
    feature v2_V : Integer = V;
    
    // XPECT errors ---> "Cannot have only one chaining feature" at "v1"
    feature v1_ chains v1;
 
    binding v1.n = v2.n;
}

````
