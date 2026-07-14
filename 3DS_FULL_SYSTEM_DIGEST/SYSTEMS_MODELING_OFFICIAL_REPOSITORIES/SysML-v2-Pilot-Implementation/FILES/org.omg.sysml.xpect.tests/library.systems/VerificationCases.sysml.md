# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/library.systems/VerificationCases.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/library.systems/VerificationCases.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/library.systems/VerificationCases.sysml
- source_bytes: 2590
- source_sha256: `498e93de337a79b6aea4421866dbdc4898d8471bdadb2b0f92507d599b9db346`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package VerificationCases {
	doc
	/*
	 * This package defines the base types for verification cases and related behavioral elements 
	 * in the SysML language.
	 */

	private import Cases::Case;
	private import Cases::cases;
	private import Requirements::RequirementCheck;
	private import ScalarValues::Boolean;
	
	abstract verification def VerificationCase :> Case {
		doc
		/*
		 * VerificationCase is the most general class of performances of VerificationCaseDefinitions. 
		 * VericationCase is the base class of all VerificationCaseDefinitions.
		 */
	
		ref verification self : VerificationCase :>> Case::self;		
		subject subj :>> Case::subj;
		return verdict : VerdictKind :>> result;
		
		objective obj :>> Case::obj {
			subject subj = VerificationCase::subj;
			
			requirement requirementVerifications : RequirementCheck[0..*] :> subrequirements {
				doc
				/*
				 * A record of the evaluations of the RequirementChecks of requirements being verified.
				 */
			}
		}
		
		ref requirement requirementVerifications : RequirementCheck[0..*] = obj.requirementVerifications {
			doc
			/*
			 * Checks on whether the verifiedRequirements of the VerificationCase have been satisfied.
			 */
		}
		
		abstract verification subVerificationCases : VerificationCase[0..*] :> verificationCases, subcases {
			doc
			/*
			 * The subcases of this VerificationCase that are VerificationCaseUsages.
			 */
		}
		
	}
	
	abstract verification verificationCases : VerificationCase[0..*] nonunique  :> cases {
		doc
		/*
		 * verificationCases is the base feature of all VerificationCaseUsages.
		 */
	}
	
	enum def VerdictKind {
		doc
		/*
		 * VerdictKind is an enumeration of the possible results of a VerificationCase.
		 */
	
		pass;
		fail;
		inconclusive;
		error;
	}
	
	calc def PassIf {
		doc
		/*
		 * PassIf returns a pass or fail VerdictKind depending on whether its argument is
		 * true or false.
		 */
	
		in attribute isPassing : Boolean;
		return attribute verdict : VerdictKind = if isPassing? VerdictKind::pass else VerdictKind::fail;
	}
	
	metadata def VerificationMethod {
		doc
		/*
		 * VerificationMethod can be used as metadata annotating a verification case or action.
		 */
	
		attribute kind : VerificationMethodKind[1..*];
	}
	
	enum def VerificationMethodKind {
		doc
		/*
		 * VerificationMethodKind is an enumeration of the standard methods by which verification
		 * can be carried out.
		 */
	
		inspect;
		analyze;
		demo;
		test;
	}
	
}
````
