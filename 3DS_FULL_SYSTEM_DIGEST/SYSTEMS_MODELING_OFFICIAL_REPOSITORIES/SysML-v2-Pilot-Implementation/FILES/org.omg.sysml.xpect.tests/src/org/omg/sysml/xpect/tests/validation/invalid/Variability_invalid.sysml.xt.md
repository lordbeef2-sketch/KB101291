# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Variability_invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Variability_invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Variability_invalid.sysml.xt
- source_bytes: 2775
- source_sha256: `e2219515cea5f9e3e3de3225e7e1ba060a2e8533bbd1fb21cf4811b98bc1bf3f`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
		File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/ControlPerformances.kerml"}
		File {from ="/library.kernel/TransitionPerformances.kerml"}
		File {from ="/library.kernel/Transfers.kerml"}
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Actions.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/ControlPerformances.kerml"}
				File {from ="/library.kernel/TransitionPerformances.kerml"}
				File {from ="/library.kernel/Transfers.kerml"}
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Actions.sysml"}
			}
		}
	}
END_SETUP 
*/
package VariabilityModel {

	part def B;
	part b1 : B;
	part b2 : B;

    variation attribute def AttributeChoices {
    	variant attribute a1;
		// XPECT errors --> "An owned usage of a variation must be a variant." at "attribute a2;"
    	attribute a2;
    }

    // XPECT errors --> "A variation must not specialize another variation." at "AttributeChoices"
    variation attribute def AttributeChoices1 :> AttributeChoices;
    
    part def PartChoices :> B {
		// XPECT errors --> "A variant must be an owned member of a variation." at "variant b1;"
        variant b1;
		// XPECT errors --> "A variant must be an owned member of a variation." at "variant b2;"
        variant b2;
    }
    
    part def D;
    part d1 : D;
    part d2 : D;

    part c {
        variation part d : D {
			// XPECT errors --> "An owned usage of a variation must be a variant." at "part d1;"
        	part d1;
        	variant part d2;
        }
        
        action f {
			// XPECT errors --> "A variant must be an owned member of a variation." at "variant action f1;"
        	variant action f1;
        	action f2;
        }
        
        // XPECT errors --> "A variation must not specialize another variation." at "d"
    	variation part e :> d;
              
    }
}

````
