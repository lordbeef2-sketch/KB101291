# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Metadata Examples/RequirementMetadataExample.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Metadata Examples/RequirementMetadataExample.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Metadata Examples/RequirementMetadataExample.sysml
- source_bytes: 956
- source_sha256: `853c36e4126898560b2ad76eef6680fc6b09c1f0bff9b042eeedbae711d77fd9`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package RequirementMetadataExample {
	private import Metaobjects::SemanticMetadata;
	private import ModelingMetadata::*;
	private import RiskMetadata::*;
	private import RiskLevelEnum::*;
	
	requirement def Goal;
	requirement goals : Goal[*] nonunique;
	metadata def goal :> SemanticMetadata {
	    :>> baseType = goals meta SysML::RequirementUsage;
	}

    requirement <'1'> vehicleMassRequirement {
        doc /* The total mass of a vehicle shall be less than or equal to the required mass. */
 
        @StatusInfo {
            status = StatusKind::tbd;
            risk {
		    	totalRisk = high;
		    	technicalRisk = medium;
		    	scheduleRisk = low;
		    	costRisk = medium;
		    }            
		    originator = "Bob";
            owner = "Mary";
        }
    }
    
    #goal requirement deliverPayload {
    	assume #goal constraint payloadMassLimit;
    	require #goal vehicleMassRequirement;
    }
    
}
````
