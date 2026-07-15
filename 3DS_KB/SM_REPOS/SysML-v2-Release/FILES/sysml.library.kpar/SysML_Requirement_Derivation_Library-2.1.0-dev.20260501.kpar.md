# OFFICIAL REPOSITORY BINARY INVENTORY: SysML-v2-Release/sysml.library.kpar/SysML_Requirement_Derivation_Library-2.1.0-dev.20260501.kpar

- repository: `SysML-v2-Release`
- source_path: `sysml.library.kpar/SysML_Requirement_Derivation_Library-2.1.0-dev.20260501.kpar`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library.kpar/SysML_Requirement_Derivation_Library-2.1.0-dev.20260501.kpar
- source_bytes: 2172
- source_sha256: `3d747c68fab9a8db39471fb6326a537c557cef5d16135a42375aad65b2bfb9cd`
- payload_status: binary metadata only
- reason: final knowledge base is Markdown-only; binary bytes are not executable knowledge

## ARCHIVE CONTENTS

### ENTRY: .project.json

- bytes: 547
- crc32: `52908aea`
- decoded_as: `utf-8`

````json
{"name":"SysML Requirement Derivation Library","description":"Standard requirements derivation domain library for the Systems Modeling Language (SysML)","version":"2.1.0-dev.20260501","usage":[{"resource":"https://www.omg.org/spec/KerML/20250201/Semantic-Library.kpar","versionConstraint":"1.1.0-dev.20260501"},{"resource":"https://www.omg.org/spec/KerML/20250201/Function-Library.kpar","versionConstraint":"1.1.0-dev.20260501"},{"resource":"https://www.omg.org/spec/SysML/20250201/Systems-Library.kpar","versionConstraint":"2.1.0-dev.20260501"}]}
````

### ENTRY: .meta.json

- bytes: 475
- crc32: `7d75aa6a`
- decoded_as: `utf-8`

````json
{"index":{"DerivationConnections":"DerivationConnections.sysml","RequirementDerivation":"RequirementDerivation.sysml"},"created":"2025-03-13T00:00:00Z","metamodel":"https://www.omg.org/spec/SysML/20250201","checksum":{"RequirementDerivation.sysml":{"value":"ee5bed2b7ad17e5c7505e6761d164e14de3d041d97e4bffc005853a130e09a20","algorithm":"SHA256"},"DerivationConnections.sysml":{"value":"40e8b13458c120bfa4f9a4059bfc4982ef959815e8580a6ac7f113bed36f55fc","algorithm":"SHA256"}}}
````

### ENTRY: DerivationConnections.sysml

- bytes: 2305
- crc32: `0eaeff2a`
- decoded_as: `utf-8`

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

### ENTRY: RequirementDerivation.sysml

- bytes: 1269
- crc32: `dea85bae`
- decoded_as: `utf-8`

````sysml
standard library package RequirementDerivation {
	doc /* This package provides language-extension metadata for modeling requirement derivation. */
	
	public import DerivationConnections::*;
	private import Metaobjects::SemanticMetadata;
	
	metadata def <original> OriginalRequirementMetadata :> SemanticMetadata {
		doc
		/*
		 * OriginalRequirementMetadata identifies a usage as an original requirement.
		 * It is intended to be used to tag the original requirement end of a Derivation.
		 */
		 
		:> annotatedElement : SysML::Usage;
		:>> baseType = originalRequirements meta SysML::Usage;
	}
	
	metadata def <derive> DerivedRequirementMetadata :> SemanticMetadata {
		doc
		/*
		 * DerivedRequirementMetadata identifies a usage as a derived requirement.
		 * It is intended to be used to tag the derived requirement ends of a Derivation.
		 */
		 
		:> annotatedElement : SysML::Usage;	
		:>> baseType = derivedRequirements meta SysML::Usage;
	}
	
	metadata def <derivation> DerivationMetadata :> SemanticMetadata {
		doc
		/*
		 * DerivationMetadata is SemanticMetadata for a Derivation connection.
		 */
		 
		:> annotatedElement : SysML::ConnectionDefinition;
		:> annotatedElement : SysML::ConnectionUsage;
		:>> baseType = derivations meta SysML::Usage;
	}	
}
````

