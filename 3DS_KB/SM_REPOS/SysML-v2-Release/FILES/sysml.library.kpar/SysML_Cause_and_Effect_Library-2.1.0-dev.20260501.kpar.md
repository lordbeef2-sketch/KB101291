# OFFICIAL REPOSITORY BINARY INVENTORY: SysML-v2-Release/sysml.library.kpar/SysML_Cause_and_Effect_Library-2.1.0-dev.20260501.kpar

- repository: `SysML-v2-Release`
- source_path: `sysml.library.kpar/SysML_Cause_and_Effect_Library-2.1.0-dev.20260501.kpar`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library.kpar/SysML_Cause_and_Effect_Library-2.1.0-dev.20260501.kpar
- source_bytes: 2620
- source_sha256: `3aff0fbd507e4c902f68bab33864cca4f08967eaeb17fd4ec1ee0cf72fc20b32`
- payload_status: binary metadata only
- reason: final knowledge base is Markdown-only; binary bytes are not executable knowledge

## ARCHIVE CONTENTS

### ENTRY: .project.json

- bytes: 653
- crc32: `0fada57f`
- decoded_as: `utf-8`

````json
{"name":"SysML Cause and Effect Library","description":"Standard cause-and-effect domain library for the Systems Modeling Language (SysML)","version":"2.1.0-dev.20260501","usage":[{"resource":"https://www.omg.org/spec/KerML/20250201/Semantic-Library.kpar","versionConstraint":"1.1.0-dev.20260501"},{"resource":"https://www.omg.org/spec/KerML/20250201/Data-Type-Library.kpar","versionConstraint":"1.1.0-dev.20260501"},{"resource":"https://www.omg.org/spec/KerML/20250201/Function-Library.kpar","versionConstraint":"1.1.0-dev.20260501"},{"resource":"https://www.omg.org/spec/SysML/20250201/Systems-Library.kpar","versionConstraint":"2.1.0-dev.20260501"}]}
````

### ENTRY: .meta.json

- bytes: 451
- crc32: `75852a4f`
- decoded_as: `utf-8`

````json
{"index":{"CausationConnections":"CausationConnections.sysml","CauseAndEffect":"CauseAndEffect.sysml"},"created":"2025-03-13T00:00:00Z","metamodel":"https://www.omg.org/spec/SysML/20250201","checksum":{"CauseAndEffect.sysml":{"value":"a2d39ed3e61477fde0273473a2c46d8eeb93ed81fcfdaeac5d48b9f942ac5403","algorithm":"SHA256"},"CausationConnections.sysml":{"value":"ad96c5282470e30d859582560225a75091b7c8058c0b949608e9dd07c130b661","algorithm":"SHA256"}}}
````

### ENTRY: CauseAndEffect.sysml

- bytes: 2441
- crc32: `b58c20a9`
- decoded_as: `utf-8`

````sysml
standard library package CauseAndEffect {
	doc /* This package provides language-extension metadata for cause-effect modeling. */
	
	public import CausationConnections::*;
	private import ScalarValues::*;
	private import Metaobjects::SemanticMetadata;

	metadata def <cause> CauseMetadata :> SemanticMetadata {
		doc
		/*
		 * CauseMetadata identifies a usage as being a cause occurrence.
		 * It is intended to be used to tag the cause ends of a Multicausation.
		 */
		 
		ref :>> annotatedElement : SysML::Usage;
		ref :>> baseType = causes as SysML::Usage;
	}
	
	metadata def <effect> EffectMetadata :> SemanticMetadata {
		doc
		/*
		 * EffectMetadata identifies a usage as being an effect occurrence.
		 * It is intended to be used to tag the effect ends of a Multicausation.
		 */
		 
		ref :>> annotatedElement : SysML::Usage;
		ref :>> baseType = effects as SysML::Usage;
	}
	
	metadata def CausationMetadata {
		doc
		/*
		 * CausationMetadata allows for the specification of additional metadata about
		 * a cause-effect connection definition or usage.
		 */
		 
		ref :> annotatedElement : SysML::ConnectionDefinition;
		ref :> annotatedElement : SysML::ConnectionUsage;
		
		attribute isNecessary : Boolean default false {
			doc 
			/* 
			 * Whether all the causes are necessary for all the effects to occur.
			 * If this is false (the default), then some or all of the effects may 
			 * still have occurred even if some of the causes did not.
			 */
		}
		
		attribute isSufficient : Boolean default false {
			doc
			/*
			 * Whether the causes were sufficient for all the effects to occur.
			 * If this is false (the default), then it may be the case that some
			 * other occurrences were also necessary for some or all of the effects
			 * to have occurred.
			 */
		}
		
		attribute probability : Real[0..1] {
			doc /* The probability that the causes will actually result in effects occurring. */
		}	
	}
	
	metadata def <multicausation> MulticausationSemanticMetadata :> CausationMetadata, SemanticMetadata {
		doc
		/*
		 * MulticausationMetadata is SemanticMetadata for a Multicausation connection.
		 */
		 
		ref :>> baseType = multicausations meta SysML::Usage;
	}
	
	metadata def <causation> CausationSemanticMetadadata :> CausationMetadata, SemanticMetadata {
		doc
		/*
		 * CausationMetadata is SemanticMetadata for a Causation connection.
		 */
		 
		ref :>> baseType = causations meta SysML::Usage;
	}
}

````

### ENTRY: CausationConnections.sysml

- bytes: 2650
- crc32: `4fea6e14`
- decoded_as: `utf-8`

````sysml
standard library package CausationConnections {	
	doc 
	/* 
	 * This package provides a library model modeling causes, effects, and causation connections 
	 * between them.
	 */

	private import SequenceFunctions::isEmpty;
	private import SequenceFunctions::size;
	private import SequenceFunctions::intersection;
		 
	abstract occurrence causes[*] {
		doc /* Occurrences that are causes. */
	}
	
	abstract occurrence effects[*]  {
		doc /* Occurrences that are effects. */
	}
	
	abstract connection def Multicausation {
		doc
		/*
		 * A Multicausation connection models the situation in which one set of
		 * occurrences causes another.
		 * 
		 * To create a Multicausation connection, specialize this connection definition
		 * adding specific end features of the relavent types. Ends representing causes
		 * should subset 'causes', while ends representing effects should subset 'effects'.
		 * There must be at least one cause and at least one effect.
		 */
		 
		abstract constant ref occurrence causes[1..*] :>> causes :> participant {
			doc 
			/* 
			 * The causing occurrences. (Constant for each Multicausation instance.)
			 */
		}
		abstract constant ref occurrence effects[1..*] :>> effects :> participant {
			doc 
			/* 
			 * The effect occurrences caused by the causing occurrences. 
			 * (Constant for each Multicausation instance.)
			 */
		}
		
		private assert constraint disjointCauseEffect {
			doc /* causes must be disjoint from effects. */
			isEmpty(intersection(causes, effects))
		}
		
		private succession causalOrdering first [nCauses] causes.startShot then [nEffects] effects {
			doc /* All causes must exist before all effects. */
			attribute nCauses = size(causes);
			attribute nEffects = size(effects);
		}
	}
	
	abstract connection multicausations : Multicausation[*] {
		doc /* multicausations is the base feature for Multicausation ConnectionUsages. */
	}
	
	connection def Causation :> Multicausation {
		doc
		/*
		 * A Causation is a binary Multicausation in which a single cause occurrence
		 * causes a single effect occurrence. (However, a single cause can separately
		 * have multiple effects, and a single effect can have separate Causation
		 * connections with multiple causes.)
		 */
		
		end theCauses [*] occurrence theCause :> causes :>> source {
		    doc /* The single causing occurrence. */
		}
		
		end theEffects [*] occurrence theEffect :> effects :>> target {
			doc /* The single effect occurrence resulting from the cause. */
		}
	}
	
	abstract connection causations : Causation[*] :> multicausations {
		doc /* causations is the base feature for Causation ConnectionUsages. */
	}
}
````

