# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_FeatureChaining.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_FeatureChaining.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_FeatureChaining.kerml.xt
- source_bytes: 1475
- source_sha256: `8eff90a3c94fe25079b5dccc37719b841503f6e08bcf45474d68535adf4e5239`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.visibility.KerMLVisibilityTest
	ResourceSet {
		ThisFile {}
		File {from = "/library/Base.kerml"}
        File {from = "/library/Occurrences.kerml"}
        File {from = "/library/Performances.kerml"}
        File {from = "/library/ControlFunctions.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from = "/library/Base.kerml"}
				File {from = "/library/Occurrences.kerml"}
                File {from = "/library/Performances.kerml"}
                File {from = "/library/ControlFunctions.kerml"}
			}
		}
	}
END_SETUP 
*/
package Visibility_Protected_FeatureChaining {
    feature x {
        feature a;
        protected feature b;
        private feature c;
    }
    
    feature y subsets x {
        feature redefines a;
        feature redefines b;
        // XPECT errors --> "Couldn't resolve reference to Feature 'c'." at "c"        
        feature redefines c;
    }
    
    feature redefines x.a;
    // XPECT errors --> "Couldn't resolve reference to Feature 'b'." at "b"        
    feature redefines x.b;
    // XPECT errors --> "Couldn't resolve reference to Feature 'c'." at "c"
    feature redefines x.c;
    
    feature x1 = x.a;
    // XPECT errors --> "Couldn't resolve reference to Element 'b'." at "b"
    feature x2 = x.b;
    // XPECT errors --> "Couldn't resolve reference to Element 'c'." at "c"
    feature x3 = x.c;
}

````
