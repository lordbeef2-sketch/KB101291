# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Metadata Examples/RiskMetadataExample.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Metadata Examples/RiskMetadataExample.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Metadata Examples/RiskMetadataExample.sysml
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
