# OFFICIAL REPOSITORY BINARY INVENTORY: SysML-v2-Release/sysml.library.kpar/SysML_Metadata_Library-2.1.0-dev.20260501.kpar

- repository: `SysML-v2-Release`
- source_path: `sysml.library.kpar/SysML_Metadata_Library-2.1.0-dev.20260501.kpar`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library.kpar/SysML_Metadata_Library-2.1.0-dev.20260501.kpar
- source_bytes: 4020
- source_sha256: `bfebcc1c43c3c449b033c012d1faae0a391d94b442e981f5e468a25364411956`
- payload_status: binary metadata only
- reason: final knowledge base is Markdown-only; binary bytes are not executable knowledge

## ARCHIVE CONTENTS

### ENTRY: .project.json

- bytes: 519
- crc32: `0fba4f50`
- decoded_as: `utf-8`

````json
{"name":"SysML Metadata Library","description":"Standard metadata domain library for the Systems Modeling Language (SysML)","version":"2.1.0-dev.20260501","usage":[{"resource":"https://www.omg.org/spec/KerML/20250201/Semantic-Library.kpar","versionConstraint":"1.1.0-dev.20260501"},{"resource":"https://www.omg.org/spec/KerML/20250201/Data-Type-Library.kpar","versionConstraint":"1.1.0-dev.20260501"},{"resource":"https://www.omg.org/spec/SysML/20250201/Systems-Library.kpar","versionConstraint":"2.1.0-dev.20260501"}]}
````

### ENTRY: .meta.json

- bytes: 794
- crc32: `23fc4258`
- decoded_as: `utf-8`

````json
{"index":{"ImageMetadata":"ImageMetadata.sysml","ModelingMetadata":"ModelingMetadata.sysml","ParametersOfInterestMetadata":"ParametersOfInterestMetadata.sysml","RiskMetadata":"RiskMetadata.sysml"},"created":"2025-03-13T00:00:00Z","metamodel":"https://www.omg.org/spec/SysML/20250201","checksum":{"RiskMetadata.sysml":{"value":"ee4f0734fa5995f435ca9c6144f48e3b7a10d422372a71c4396bba2401c14a6e","algorithm":"SHA256"},"ImageMetadata.sysml":{"value":"b7fa6baf2ee3e3c0708c2b5901abd0d51deeba8e61652909cac57069b4e06731","algorithm":"SHA256"},"ModelingMetadata.sysml":{"value":"bb6c664cfe65dc298827c6cca8fc21941965db3a40a0412ba211cf6ff1cc254d","algorithm":"SHA256"},"ParametersOfInterestMetadata.sysml":{"value":"f5c6da3be824a82a34482f00a3e43976787c03ea1d30cbda84b1be838c557876","algorithm":"SHA256"}}}
````

### ENTRY: ImageMetadata.sysml

- bytes: 2099
- crc32: `7da38fb3`
- decoded_as: `utf-8`

````sysml
standard library package ImageMetadata {
	doc
	/*
	 * This package provides attributive data and metadata to allow a model element to be
	 * annotated with an image to be used in its graphical rendering or as a marker to
	 * adorn graphical or textual renderings.
	 */
	 
	private import ScalarValues::String;
	
	attribute def Image {
		doc
		/*
		 * Image provides the data necessary for the physical definition of 
		 * a graphical image.
		 */
		 
		attribute content : String[0..1] {
			doc
			/*
			 * Binary data for the image according to the given MIME type, 
			 * encoded as given by the encoding.
			 */
		}
		
		attribute encoding : String[0..1] {
			doc
			/*
			 * Describes how characters in the content are to be decoded into 
			 * binary data. At least "base64", "hex", "identify", and "JSONescape"
			 * shall be supported.
			 */
		}
		
		attribute type : String[0..1] {
			doc
			/*
			 * The MIME type according to which the content should be interpreted.
			 */
		}
		
		attribute location : String[0..1] {
			doc
			/*
			 * A URI for the location of a resource containing the image content,
			 * as an alternative for embedding it in the content attribute.
			 */
		}
	}
	
	metadata def Icon {
		doc
		/*
		 * Icon metadata can be used to annotate a model element with an image to be used
		 * to show render the element on a diagram and/or a small image to be used as an
		 * adornment on a graphical or textual rendering. Alternatively, another metadata
		 * definition can be annotated with an Icon to indicate that any model element 
		 * annotated by the containing metadata can be rendered according to the Icon.
		 */
		 
		attribute fullImage : Image[0..1] {
			doc
			/*
			 * A full-sized image that can be used to render the annotated element on a
			 * graphical view, potentially as an alternative to its standard rendering.
			 */
		}
		
		attribute smallImage : Image[0..1] {
			doc
			/*
			 * A smaller image that can be used as an adornment on the graphical rendering
			 * of the annotated element or as a marker in a textual rendering.
			 */
		}
	}
	
}
````

### ENTRY: ParametersOfInterestMetadata.sysml

- bytes: 1191
- crc32: `610ad600`
- decoded_as: `utf-8`

````sysml
standard library package ParametersOfInterestMetadata {
	doc
	/*
	 * This package contains definitions of metadata to identify key parameters of interest,
	 * including measures of effectiveness (MOE) and other key measures of performance (MOP).
	 */
	 
	 private import Metaobjects::SemanticMetadata;
	 
	 attribute measuresOfEffectiveness[*] nonunique {
	 	doc /* Base feature for attributes that are measures of effectiveness. */
	 }
	 
	 attribute measuresOfPerformance[*] nonunique {
	 	doc /* Base feature for attributes that are measures of performance. */
	 }
	 
	 metadata def <moe> MeasureOfEffectiveness :> SemanticMetadata {
	 	doc 
	 	/*
	 	 * MeasureOfEffectiveness is semantic metadata for identifying an attribute as a
	 	 * measure of effectiveness.
	 	 */
	 	
	 	:>> annotatedElement : SysML::Usage;
	 	:>> baseType = measuresOfEffectiveness meta SysML::Usage;
	 }
	 
	 metadata def <mop> MeasureOfPerformance :> SemanticMetadata {
	 	doc 
	 	/*
	 	 * MeasureOfPerformance is semantic metadata for identifying an attribute as a
	 	 * measure of performance.
	 	 */
	 	
	 	:>> annotatedElement : SysML::Usage;
	 	:>> baseType = measuresOfPerformance meta SysML::Usage;
	 }
}
````

### ENTRY: RiskMetadata.sysml

- bytes: 2085
- crc32: `89e2c169`
- decoded_as: `utf-8`

````sysml
standard library package RiskMetadata {
	doc
	/*
	 * This package defines metadata for annotating model elements with assessments of risk.
	 */

	private import ScalarValues::Real;
	
	attribute def Level :> Real {
		doc
		/*
		 * A Level is a Real number in the interval 0.0 to 1.0, inclusive.
		 */
	
		assert constraint { that >= 0.0 and that <= 1.0 }
	}
	
	enum def LevelEnum :> Level {
		doc
		/*
		 * LevelEnum provides standard probability Levels for low, medium and high risks.
		 */
	
		low = 0.25;
		medium = 0.50;
		high = 0.75;
	}

	attribute def RiskLevel {
		doc
		/*
		 * RiskLevel gives the probability of a risk occurring and, optionally, the impact
		 * if the risk occurs.
		 */
	
		attribute probability : Level {
			doc
			/*
			 * The probability that a risk will occur.
			 */
		}
		
		attribute impact : Level [0..1] {
			doc
			/*
			 * The impact of the risk if it occurs (with 0.0 being no impact and 1.0 being 
			 * the most severe impact).
			 */
		}
	}
	
	enum def RiskLevelEnum :> RiskLevel {
		doc
		/*
		 * RiskLevelEnum enumerates standard RiskLevels for low, medium and high risks
		 * (without including impact).
		 */

		low = new RiskLevel(probability = LevelEnum::low);
		medium = new RiskLevel(probability = LevelEnum::medium);
		high = new RiskLevel(probability = LevelEnum::high);
	}
	
	metadata def Risk {
		doc
		/*
		 * Risk is used to annotate a model element with an assessment of the risk related to it
		 * in some typical risk areas.
		 */
	
		attribute totalRisk : RiskLevel [0..1] {
			doc
			/*
			 * The total risk associated with the annotated element.
			 */
		}
		
		attribute technicalRisk : RiskLevel [0..1] {
			doc
			/*
			 * The risk of unresolved technical issues regarding the annotated element.
			 */
		}
		
		attribute scheduleRisk : RiskLevel [0..1] {
			doc
			/*
			 * The risk that work on the annotated element will not be completed on schedule.
			 */
		}
		
		attribute costRisk : RiskLevel [0..1] {
			doc
			/*
			 * The risk that work on the annotated element will exceed its planned cost.
			 */
		}
	}
	
}
````

### ENTRY: ModelingMetadata.sysml

- bytes: 2423
- crc32: `9a484a37`
- decoded_as: `utf-8`

````sysml
standard library package ModelingMetadata {
	doc
	/*
	 * This package contains definitions of metadata generally useful for annotating models.
	 */

	private import Base::Anything;
	private import ScalarValues::String;
	private import RiskMetadata::Risk;
	
	enum def StatusKind {
		doc
		/*
		 * StatusKind enumerates the possible statuses of work on a model element.
		 */
	
		open {
			doc
			/*
			 * Status is open.
			 */
		}
		
		tbd {
			doc
			/*
			 * Status is to be determined.
			 */
		}
		
		tbr {
			doc
			/*
			 * Status is to be resolved.
			 */
		}
		
		tbc {
			doc
			/*
			 * Status is to be confirmed.
			 */
		}
		
		done {
			doc
			/*
			 * Status is done.
			 */
		}
		
		closed {
			doc
			/*
			 * Status is closed.
			 */
		}
	}
	
	metadata def StatusInfo {
		doc
		/*
		 * StatusInfo is used to annotate a model element with status information.
		 */
	
		attribute originator : String [0..1] {
			doc
			/*
			 * The originator of the annotated element.
			 */
		}
		
		attribute owner : String [0..1] {
			doc
			/*
			 * The current owner of the annotated element.
			 */
		}
		
		attribute status : StatusKind {
			doc
			/*
			 * The current status of work on the annotated element (required).
			 */
		}
		
		item risk : Risk [0..1] {
			doc
			/*
			 * An assessment of risk for the annotated element.
			 */
		}
	}
	
	metadata def Rationale {
		doc
		/*
		 * Rationale is used to explain a choice or other decision made related to the
		 * annotated element.
		 */
	
		attribute text : String {
			doc
			/*
			 * A textual description of the rationale (required).
			 */
		}
		
		ref explanation : Anything [0..1] {
			doc
			/*
			 * A reference to a feature that provides a formal explanation of the rationale.
			 * (For example, a trade study whose result explains the choice of a certain alternative).
			 */
		}
	}
	
	metadata def Issue {
		doc
		/*
		 * Issue is used to record some issue concerning the annotated element.
		 */
	
		attribute text : String {
		doc
		/*
		 * A textual description of the issue.
		 */
		}
	}
	
	metadata def <refinement> Refinement {
		doc
		/*
		 * Refinement is used to identify a dependency as modeling a refinement relationship.
		 * In such a relationship, the source elements of the relationship provide a more precise and/or 
		 * accurate representation than the target elements.
		 */
	
		:>> annotatedElement : SysML::Dependency;
	}
	
}
````

