# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml.library/Domain Libraries/Metadata/ParametersOfInterestMetadata.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml.library/Domain Libraries/Metadata/ParametersOfInterestMetadata.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml.library/Domain Libraries/Metadata/ParametersOfInterestMetadata.sysml
- source_bytes: 1229
- source_sha256: `51474ef5606a9f2be33b860e85b4758008573591b6f3dba984fd40aa5a2ca694`
- decoded_as: `utf-8`


## EXACT SOURCE

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
