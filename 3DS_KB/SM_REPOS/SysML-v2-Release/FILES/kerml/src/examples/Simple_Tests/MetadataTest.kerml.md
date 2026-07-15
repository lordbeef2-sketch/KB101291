# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/MetadataTest.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/MetadataTest.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/MetadataTest.kerml
- source_bytes: 1236
- source_sha256: `4c9d6c87982833cd427e780b5691acdb27fac3a36b8fcd0af8f4d67b1dc30c81`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package MetadataTest {
	private import 'User Defined Extensions'::*;
	
	library package 'User Defined Extensions' {
		
		datatype ClassificationLevel :> ScalarValues::Natural;
		feature uncl[1] : ClassificationLevel = 0;
		feature conf[1] : ClassificationLevel = 1;
		feature secret[1] : ClassificationLevel = 2;
		
		metaclass Classified {
			feature :>> annotatedElement : KerML::Feature;
			feature classificationLevel : ClassificationLevel;
		}
		
		metaclass Security;
	}
	
	feature x {
		metadata Classified {
			classificationLevel = conf;
		}
	}
	
	feature y {
		@Classified {
			classificationLevel = conf;
		}
		@Security;
	}
	
	private #Classified #Security feature z1;
	abstract #Classified z2;
	
	feature z {
	    #Security #Classified metadata Classified {
	        classificationLevel = secret;
	    }
	}
	
    class CC;
    struct SS {
        feature cc : CC;
    }
    
    metaclass M :> Metaobjects::SemanticMetadata {
      :>> annotatedElement : KerML::Class;
      :>> baseType = if annotatedElement istype KerML::Structure ? 
                         SS meta KerML::Type else CC meta KerML::Class;
    }
    
    #M struct T {
        feature :>> cc;
    }
}
````
