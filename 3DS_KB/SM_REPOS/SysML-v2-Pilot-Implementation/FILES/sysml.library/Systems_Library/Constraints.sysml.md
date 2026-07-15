# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml.library/Systems Library/Constraints.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml.library/Systems Library/Constraints.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml.library/Systems Library/Constraints.sysml
- source_bytes: 1306
- source_sha256: `a8085cadbaa9bc4e4f1b2460c2facfbea8cb7ea3e0436e1ce9a6230daa16b757`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package Constraints {
	doc
	/*
	 * This package defines the base types for constraints and related elements in the
	 * SysML language.
	 */

	private import Performances::BooleanEvaluation;
	private import Performances::booleanEvaluations;
	private import Performances::trueEvaluations;
	private import Performances::falseEvaluations;
	
	abstract constraint def ConstraintCheck :> BooleanEvaluation {
		doc
		/*
		 * ConstraintCheck is the most general class for constraint checking. ConstraintCheck is the base
		 * type of all ConstraintDefinitions.
		 */
	
		ref constraint self: ConstraintCheck :>> BooleanEvaluation::self;
	}
	
	abstract constraint constraintChecks: ConstraintCheck[0..*] nonunique :> booleanEvaluations {
		doc
		/*
		 * constraintChecks is the base feature of all ConstraintUsages.
		 */
	}
	
	abstract constraint assertedConstraintChecks :> constraintChecks, trueEvaluations {
		doc
		/*
		 * assertedConstraintChecks is the subset of constraintChecks for ConstraintChecks asserted to be true.
		 */
	}
		
	abstract constraint negatedConstraintChecks :> constraintChecks, falseEvaluations {
		doc
		/*
		 * negatedConstraintChecks is the subset of constraintChecks for ConstraintChecks asserted to be false.
		 */
	}
		
}
````
