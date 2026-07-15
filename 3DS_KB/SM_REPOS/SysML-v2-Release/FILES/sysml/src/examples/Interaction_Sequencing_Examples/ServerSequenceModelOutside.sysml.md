# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Interaction Sequencing Examples/ServerSequenceModelOutside.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Interaction Sequencing Examples/ServerSequenceModelOutside.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Interaction Sequencing Examples/ServerSequenceModelOutside.sysml
- source_bytes: 733
- source_sha256: `4417c2eddc29eaa1a7b481c529c4e62d06e47d709e5b4898242ce426bbaba1b9`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ServerSequenceModelOutside {
	public import ServerSequenceModel::*;

	part def PubSubSequenceOutside :> PubSubSequence {
		part :>> producer {
			event publish_source_event = publish_message.start;
		}
		
		part :>> server {
			event occurrence :>> subscribe_target_event = subscribe_message.done;
			then event occurrence :>> publish_target_event = publish_message.done;
			then event occurrence :>> deliver_source_event = deliver_message.start;
		}
		
		part :>> consumer {  /* Redundant with timing constraints on server and generic transfers. */
			event occurrence :>> subscribe_source_event = subscribe_message.start;
			then event occurrence :>> deliver_target_event = deliver_message.done;
		}
	}
}
````
