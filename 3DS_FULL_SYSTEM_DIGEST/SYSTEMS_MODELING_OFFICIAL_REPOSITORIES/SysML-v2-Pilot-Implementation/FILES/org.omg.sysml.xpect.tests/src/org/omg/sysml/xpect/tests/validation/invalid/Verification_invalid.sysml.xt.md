# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Verification_invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Verification_invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Verification_invalid.sysml.xt
- source_bytes: 3090
- source_sha256: `da9a97834f49531bf0879cdd9176c05028154f86ccc3d373105d9aa2b11f51df`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.simpletests.SysMLTests
	ResourceSet {
		ThisFile {} 
 		File {from ="/library.kernel/Base.kerml"}
 		File {from ="/library.kernel/Links.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/ControlPerformances.kerml"}
		File {from ="/library.kernel/TransitionPerformances.kerml"}
		File {from ="/library.kernel/Transfers.kerml"}
		File {from ="/library.kernel/ScalarFunctions.kerml"}
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.systems/Items.sysml"}
 		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Constraints.sysml"}
		File {from ="/library.systems/Requirements.sysml"}
		File {from ="/library.systems/Actions.sysml"}
		File {from ="/library.systems/Calculations.sysml"}
		File {from ="/library.systems/Cases.sysml"}
		File {from ="/library.systems/VerificationCases.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {} 
		 		File {from ="/library.kernel/Base.kerml"}
		 		File {from ="/library.kernel/Links.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
		       	File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/ControlPerformances.kerml"}
				File {from ="/library.kernel/TransitionPerformances.kerml"}
				File {from ="/library.kernel/Transfers.kerml"}
				File {from ="/library.kernel/ScalarFunctions.kerml"}
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.systems/Items.sysml"}
		 		File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Constraints.sysml"}
				File {from ="/library.systems/Requirements.sysml"}
				File {from ="/library.systems/Actions.sysml"}
				File {from ="/library.systems/Calculations.sysml"}
				File {from ="/library.systems/Cases.sysml"}
				File {from ="/library.systems/VerificationCases.sysml"}
			}
		}
	}
END_SETUP
*/
package Verification_invalid {

	requirement def R {
		doc /* ... */
		
		// XPECT errors --> "A requirement verification must be in the objective of a verification case." at "verify requirement : R;"		
		verify requirement : R;

		// XPECT errors --> "A requirement verification must be in the objective of a verification case." at "verify r;"		
		verify r;
	}
	
	requirement r : R;

	verification def VerificationCase {		
		objective {
			verify requirement : R;
		}
		
		requirement {
			// XPECT errors --> "A requirement verification must be in the objective of a verification case." at "verify r;"		
			verify r;
		}
	}
	
	case def VerificationPlan {
		objective {
			// XPECT errors --> "A requirement verification must be in the objective of a verification case." at "verify r;"		
			verify r;
		}
	}
	
}
````
