# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/validation/17-Sequence Modeling/17b-Sequence-Modeling.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/validation/17-Sequence Modeling/17b-Sequence-Modeling.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/validation/17-Sequence Modeling/17b-Sequence-Modeling.sysml
- source_bytes: 898
- source_sha256: `366e9d8288305130b3947dd6c8371490d2bcfb5bffcad0ff52451b27c2cce030`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '17b-Sequence-Modeling' {
	private import ScalarValues::*;
	private import PayloadDefinitions::*;

	package PayloadDefinitions {
	    item def Subscribe {
	    	attribute topic : String;
	    	ref part subscriber;
	    }
	    
		item def Publish {
			attribute topic : String;
			ref publication;
		}
		
		item def Deliver {
			ref publication;
		}
	}

	occurrence def PubSubSequence {
		part producer[1] {
			event publish_message.sourceEvent;
		}
		
		message publish_message of Publish[1];
		
		part server[1] {
			event subscribe_message.targetEvent;
			then event publish_message.targetEvent;
			then event deliver_message.sourceEvent;
		}
		
		message subscribe_message of Subscribe[1];
		message deliver_message of Deliver[1];
		
		part consumer[1] {
			event subscribe_message.sourceEvent;
			then event deliver_message.targetEvent;
		}
	}
}
````
