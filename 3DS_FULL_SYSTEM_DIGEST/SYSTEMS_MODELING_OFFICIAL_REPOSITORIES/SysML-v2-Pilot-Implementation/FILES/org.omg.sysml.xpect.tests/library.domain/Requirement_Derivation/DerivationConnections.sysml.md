# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/library.domain/Requirement Derivation/DerivationConnections.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/library.domain/Requirement Derivation/DerivationConnections.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/library.domain/Requirement Derivation/DerivationConnections.sysml
- source_bytes: 2367
- source_sha256: `f9f587423c1151f6ea89dae3e4a2e9b446906c5660bd8b3532952876fd9b9adc`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package DerivationConnections {
	doc
	/*
	 * This package provides a library model for derivation connections between requirements.
	 */
	 
	private import SequenceFunctions::excludes;
	private import ControlFunctions::allTrue;
	
	requirement originalRequirements[*] {
		doc /* originalRequirements are the original requirements in Derivation connections. */
	}
	requirement derivedRequirements[*] {
		doc /* derivedRequirements are the derived requirments in Derivation connections. */
	}
	
	abstract connection def Derivation {
		doc
		/*
		 * A Derivation connection asserts that one or more derivedRequirements are derived from
		 * a single originalRequirement. This means that any subject that satisfies the
		 * originalRequirement should, in itself or though other things related to it, satisfy
		 * each of the derivedRequirements.
		 * 
		 * A connection usage typed by Derivation must have requirement usages for all its ends.
		 * The single end for the originalRequirement should subset originalRequirement, while
		 * the rest of the ends should subset derivedRequirements.
		 */
		
		// Note: This redefinition causes a distinguishibility problem for binary connections, becuse
		// participant is already redefined for them to limit the multiplicity to 2.
		// ref requirement :>> participant {
		//	doc /* All the participants in a Derivation must be requirements. */
		// }
		
		ref requirement originalRequirement[1] :>> originalRequirements :> participant {
			doc /* The single original requirement. */
		}
		ref requirement :>> derivedRequirements[1..*] :> participant {
			doc /* The one or more requirements that are derived from the original requirement. */
		}
		
		private assert constraint originalNotDerived {
			doc /* The original requirement must not be a derived requirement. */
			
			derivedRequirements->excludes(originalRequirement)
		}
		
		private assert constraint originalImpliesDerived {
			doc 
			/* 
			 * Whenever the originalRequirement is satisfied, all of the derivedRequirements must also
			 * be satisfied.
			 */
			 
			originalRequirement.result implies allTrue(derivedRequirements.result)
		}	
	}
	
	abstract connection derivations : Derivation[*] {
		doc /* derivations is the base feature for Derivation connection usages. */
	}
}
````
