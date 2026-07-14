# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/validation/14-Language Extensions/14a-Language Extensions.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/validation/14-Language Extensions/14a-Language Extensions.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/validation/14-Language Extensions/14a-Language Extensions.sysml
- source_bytes: 594
- source_sha256: `c3f7b8b4ff7a4f052c4db8ac9596349c82b1d2c7fe93e3cf9b11b53f715615fc`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '14a-Language Extensions' {
	private import 'User Defined Extensions'::*;
	
	package 'User Defined Extensions' {
		
		enum def ClassificationLevel {
			uncl;
			conf;
			secret;
		}
		
		metadata def Classified {
			ref :>> annotatedElement : SysML::PartUsage;
			attribute classificationLevel : ClassificationLevel[1];
		}
	}
	
	part part_X {
		metadata Classified {
			classificationLevel = ClassificationLevel::conf;
		}
	}
	
	// Alternative shorthand notation
	part part_Y {
		@Classified {
			classificationLevel = ClassificationLevel::conf;
		}
	}

}
````
