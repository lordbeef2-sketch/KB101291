# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/AnalysisTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/AnalysisTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/AnalysisTest.sysml
- source_bytes: 525
- source_sha256: `bc9ec8a433e15d77f9f1843bee23760cb5bd9dee37ed50df6f272f9ae4b5afed`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package AnalysisTest {

	part def V {
		m;
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
		
		v.m
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
