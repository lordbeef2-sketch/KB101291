# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Interaction Sequencing Examples/ServerSequenceModel.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Interaction Sequencing Examples/ServerSequenceModel.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Interaction Sequencing Examples/ServerSequenceModel.sysml
- source_bytes: 1069
- source_sha256: `453c7016a1582ea3f987d1ddc8fe468958c27485b3bb503cf6c31cb625e70bfe`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ServerSequenceModel {
	private import ScalarValues::String;
	public import SignalDefinitions::*;

	package SignalDefinitions {
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

	part def PubSubSequence {
		part producer[1] {
			event occurrence publish_source_event;
		}
		
		message publish_message from producer.publish_source_event to server.publish_target_event;
		
		part server[1] {
			event occurrence subscribe_target_event;
			then event occurrence publish_target_event;
			then event occurrence deliver_source_event;
		}
		
		message subscribe_message from consumer.subscribe_source_event to server.subscribe_target_event;
		message deliver_message from server.deliver_source_event to consumer.deliver_target_event;
		
		part consumer {
			event occurrence subscribe_source_event;
			then event occurrence deliver_target_event;
		}
	}
}
````
