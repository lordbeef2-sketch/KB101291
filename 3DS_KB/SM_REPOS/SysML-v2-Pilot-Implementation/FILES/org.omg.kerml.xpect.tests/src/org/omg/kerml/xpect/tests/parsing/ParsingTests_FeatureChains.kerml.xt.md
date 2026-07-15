# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_FeatureChains.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_FeatureChains.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_FeatureChains.kerml.xt
- source_bytes: 2894
- source_sha256: `5a1cb2aa1ade4925fe3cb457fb260781bc9f3801d4c8838c0357b30d6ac1e033`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
        ResourceSet {
                ThisFile {}
                File {from ="/library/Base.kerml"}
                File {from ="/library/Links.kerml"}
                File {from ="/library/Occurrences.kerml"}
                File {from ="/library/Objects.kerml"}
                File {from ="/library/Performances.kerml"}
                File {from ="/library/Transfers.kerml"}
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
                				File {from ="/library/Transfers.kerml"}
                                File {from ="/library/ScalarValues.kerml"}
                                File {from ="/library/BaseFunctions.kerml"}
                                File {from ="/library/DataFunctions.kerml"}
                				File {from ="/library/ControlFunctions.kerml"}
                        }
                }
        }
END_SETUP
*/

// XPECT noErrors ---> ""
package P {
    public import ScalarValues::*;
    
    struct V {
    	feature n : Integer;
    	feature m : Real;
    }
    
    feature v1 : V;
    
    feature v2 :> v1;
    
    feature v1_n : Integer = v1.n;
    feature v1_m : Real = v1.m;
    feature v2_m : Real = v1.n + v2.m;
    
    feature v_4 : V = (v1, v2).{in v : V; v.n == 4};
    feature vv[*] : V = (all V).{in v : V; v.m > 100};
   
	classifier F {
		feature a : A;
	}
	  
	feature f : F;
	  
	classifier A {
		feature g = f.a;
	}
	  
	classifier B {
	  	feature f : F;
	  	feature a : A;
	}
	  
	feature b : B {
	  	connector f.a to a.g;
	  	binding f.a = a.g;
	}
	  
	feature g subsets f.a;
	subset g subsets b.f.a;
	redefinition b.f redefines b.a;
	  
	subtype g.g specializes b.f.a;
	
	disjoint b.f.a from b.a;
	
    behavior BB {
    	out feature a : Integer;
    	step b {
    		step c {
    			feature d : Integer;
    		}
    	}
    }
    
    feature b1 : BB;
    feature b2 : BB;

    // Testing deeply nested item flow connection.
    flow b1.a to b2.b.c.d;
    
	feature h1 unions f, b.f, b.a;
	feature h2 differences b.f, b.a intersects f.a, g disjoint from h1;
	
	feature b_f_a chains b chains f.a;
}

````
