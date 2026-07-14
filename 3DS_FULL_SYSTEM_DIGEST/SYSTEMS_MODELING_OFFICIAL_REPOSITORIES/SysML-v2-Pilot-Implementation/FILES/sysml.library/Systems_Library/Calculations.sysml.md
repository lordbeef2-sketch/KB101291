# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml.library/Systems Library/Calculations.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml.library/Systems Library/Calculations.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml.library/Systems Library/Calculations.sysml
- source_bytes: 1026
- source_sha256: `e35be6d273ea61ca86cd2e7d77b0e7a5d5f714d984e9a601ecfb1bfa6e225271`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package Calculations {
	doc
	/*
	 * This package defines the base types for calculations and related behavioral elements in the
	 * SysML language.
	 */

	private import Performances::Evaluation;
	private import Performances::evaluations;
	private import Actions::Action;
	private import Actions::actions;
	
	abstract calc def Calculation :> Action, Evaluation {
		doc
		/*
		 * Calculation is the most general class of evaluations of CalculationDefinitions in a
		 * system or part of a system. Calculation is the base class of all CalculationDefinitions.
		 */
	
		ref calc self: Calculation :>> Action::self, Evaluation::self;
		
		abstract calc subcalculations: Calculation :> calculations, subactions {
			doc
			/*
			 * The subactions of this Calculation that are Calculations.
			 */
		}
		
	}
	
	abstract calc calculations: Calculation[0..*] nonunique :> actions, evaluations {
		doc
		/*
		 * calculations is the base Feature for all CalculationUsages.
		 */
	}
}
````
