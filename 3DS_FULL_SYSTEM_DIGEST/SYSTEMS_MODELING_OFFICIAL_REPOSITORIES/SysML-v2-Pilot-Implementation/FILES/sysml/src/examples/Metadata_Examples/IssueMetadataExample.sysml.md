# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Metadata Examples/IssueMetadataExample.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Metadata Examples/IssueMetadataExample.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Metadata Examples/IssueMetadataExample.sysml
- source_bytes: 1145
- source_sha256: `1836ae34a7def93a8488a143939d5b6a568141d20b6cd34c40a8dc96f65e6a5e`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package IssueMetadataExample {
	private import ModelingMetadata::Issue;
	
    //Example: the following identifies an issue with the interface
    
    metadata InterfaceCompatibilityIssue : Issue about engineToTransmissionInterface {
    	text = "This issue is about the interface compatability between the engine and transmission." +
               "The interface def includes an end defined by a ClutchPort." +
               "However, the interface usage connects the transmission port that is defined by ~DrivePwrPort." +
               "This should have surfaced a compatibility issue, since the interface is not really compatible with its definition";
    }
    
    interface def EngineToTransmissionInterface{
        end p1:DrivePwrPort;
        end p2:ClutchPort;
    }
    port def DrivePwrPort;
    port def ClutchPort;
    
    part engine{
        port drivePwrPort:DrivePwrPort;
    }
    part transmission{
        port clutchPort:~DrivePwrPort;
    }

    interface engineToTransmissionInterface:EngineToTransmissionInterface
        connect engine.drivePwrPort to transmission.clutchPort;       

}
````
