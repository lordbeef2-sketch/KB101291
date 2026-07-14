# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Simple Tests/MetadataTest.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Simple Tests/MetadataTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Simple Tests/MetadataTest.sysml
- source_bytes: 908
- source_sha256: `56c6569da41422951e371106ce52f2186d63ebedd9a5bd958d6150edb1037d16`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package MetadataTest {
	private import 'User Defined Extensions'::*;
	
	library package 'User Defined Extensions' {
		
		#Security enum def ClassificationLevel :> ScalarValues::Natural {
			uncl : ClassificationLevel = 0;
			conf : ClassificationLevel = 1;
			#Security enum secret : ClassificationLevel = 2;
		}
		
		metadata def Classified {
			ref :>> annotatedElement : SysML::Usage;
			ref classificationLevel : ClassificationLevel;
		}
		
		metadata def Security;
	}
	
	ref x {
		metadata Classified {
			classificationLevel = ClassificationLevel::conf;
		}
	}
	
	ref y {
		@Classified {
			classificationLevel = ClassificationLevel::conf;
		}
		@Security;
	}
	
	private ref #Classified #Security z1;
	abstract #Classified z2;
	
	ref z {
	    #Security #Classified metadata Classified {
	        classificationLevel = ClassificationLevel::secret;
	    }
	}	
	
}
````
