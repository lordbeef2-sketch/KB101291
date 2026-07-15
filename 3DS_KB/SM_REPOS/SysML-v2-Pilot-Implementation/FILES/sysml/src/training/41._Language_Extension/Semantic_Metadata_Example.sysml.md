# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/41. Language Extension/Semantic Metadata Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/41. Language Extension/Semantic Metadata Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/41. Language Extension/Semantic Metadata Example.sysml
- source_bytes: 639
- source_sha256: `3935dbb8ae609ea2f874649e8b859cbbc35e7b3dc66b6d56f987186543b38927`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
library package 'Semantic Metadata Example' {
	private import 'Model Library Example'::*;
	private import Metaobjects::SemanticMetadata;

	metadata def situation :> SemanticMetadata {
		:>> baseType = situations meta SysML::Usage;
	}
	
	metadata def cause :> SemanticMetadata {
		:>> baseType = causes meta SysML::Usage;
	}
	
	metadata def failure :> SemanticMetadata {
		:>> baseType = failures meta SysML::Usage;
	}
	
	metadata def causation :> SemanticMetadata {
		:>> baseType = causations meta SysML::Usage;
	}
	
	metadata def scenario :> SemanticMetadata {
		:>> baseType = scenarios meta SysML::Usage;
	}
	
}
````
