# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Metadata Examples/RiskMetadataExample.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Metadata Examples/RiskMetadataExample.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Metadata Examples/RiskMetadataExample.sysml
- source_bytes: 402
- source_sha256: `72180bdb6c2a1b5912b61956225a548137fbcf2f382f52788d6f3c3bb8e1e4c6`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package RiskMetadataExample {
	private import RiskMetadata::*;
	private import RiskLevelEnum::*;
	
    part engine4cyl{
        @Risk {
            totalRisk = high;
            technicalRisk = medium;
            scheduleRisk = medium;
        }
        @Risk {
        	totalRisk { 
        		probability = 0.3;
        		impact = 0.7;
        	}        	
        }
    }
        
}
````
