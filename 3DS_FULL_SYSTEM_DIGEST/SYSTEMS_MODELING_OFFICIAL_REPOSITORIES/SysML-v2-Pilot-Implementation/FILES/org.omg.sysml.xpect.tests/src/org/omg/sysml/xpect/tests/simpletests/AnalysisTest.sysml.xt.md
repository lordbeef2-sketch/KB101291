# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/AnalysisTest.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/AnalysisTest.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/AnalysisTest.sysml.xt
- source_bytes: 2929
- source_sha256: `13732aec99e17dcf4fde832a5ddd25bd665e0ff14c1157e85ecce7ecb4f48673`
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
		File {from ="/library.kernel/ControlFunctions.kerml"}
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
		File {from ="/library.systems/AnalysisCases.sysml"}
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
				File {from ="/library.kernel/ControlFunctions.kerml"}
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
				File {from ="/library.systems/AnalysisCases.sysml"}
			}
		}
	}
END_SETUP
*/
// XPECT noErrors ---> ""
package AnalysisTest {

	part def V { 
		attribute m;
	}
	
	part vv : V;
	
	requirement def AnalysisObjective {
		doc /* ... */
	}

	analysis def AnalysisCase {
		subject v : V;
		objective obj : AnalysisObjective {
			subject = result;
		}
		
		return ref result = v.m;
	}
	
	analysis def AnalysisPlan {
		subject v : V;
		objective {
			doc /* ... */
		}
		
		analysis analysisCase : AnalysisCase { return mass; }
	}
	
	part analysisContext {
		analysis analysisPlan : AnalysisPlan {
			subject v = vv;
		}
	}
}
````
