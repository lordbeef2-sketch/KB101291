# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml.library/Systems Library/AnalysisCases.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml.library/Systems Library/AnalysisCases.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml.library/Systems Library/AnalysisCases.sysml
- source_bytes: 1075
- source_sha256: `839177ea10bf5eae65b8eac406c99ca54cea7404e075e77ae937b19d7c485da1`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package AnalysisCases {
	doc
	/*
	 * This package defines the base types for analysis cases and related behavioral elements 
	 * in the SysML language.
	 */

	private import Performances::Evaluation;
	private import Performances::evaluations;
	private import Calculations::Calculation;
	private import Cases::Case;
	private import Cases::cases;
	
	abstract analysis def AnalysisCase :> Case {
		doc
		/*
		 * AnalysisCase is the most general class of performances of AnalysisCaseDefinitions. 
		 * AnalysisCase is the base class of all AnalysisCaseDefinitions.
		 */
	
		ref analysis self : AnalysisCase :>> Case::self;		
		subject subj :>> Case::subj;
		
		abstract analysis subAnalysisCases : AnalysisCase[0..*] :> analysisCases, subcases {
			doc
			/*
			 * Other AnalysisCases carried out as part of the performance of this AnalysisCase.
			 */
		}
	}
	
	abstract analysis analysisCases : AnalysisCase[0..*] nonunique :> cases {
		doc
		/*
		 * analysisCases is the base feature of all AnalysisCaseUsages.
		 */
	}
}
````
