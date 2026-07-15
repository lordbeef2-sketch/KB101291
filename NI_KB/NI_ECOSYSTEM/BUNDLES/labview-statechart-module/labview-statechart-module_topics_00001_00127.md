# NI DOCUMENT BUNDLE: labview-statechart-module

<!--NI_BUNDLE_CHUNK bundle=labview-statechart-module start=1 end=127 -->
<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscdbggencodemissingdbginfo.html language=enus -->
## TOPIC 00001: Statechart is missing debugging information

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscdbggencodemissingdbginfo.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscdbggencodemissingdbginfo.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart is missing debugging information

You cannot perform [debugging](../lvschowto/sc_h_debugsc.html) on the statechart even though debugging is enabled on the [Statechart Code Generation](../lvsc/sc_codegen.html) page of the [Project Library Properties](/csh?topicname=lvdialog/library_props_db.html) dialog box.

To correct this error, [regenerate LabVIEW code for the statechart](../lvschowto/sc_h_gencode.html).

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscdbgnodenotgenerated.html language=enus -->
## TOPIC 00002: Statechart does not have debugging information

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscdbgnodenotgenerated.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscdbgnodenotgenerated.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart does not have debugging information

The statechart does not allow you to perform debugging.

To correct this error, change the properties of the statechart to enable debugging on the [Statechart Code Generation](../lvsc/sc_codegen.html) page of the [Project Library Properties](/csh?topicname=lvdialog/library_props_db.html) dialog box, and [regenerate LabVIEW code](../lvschowto/sc_h_gencode.html) for this statechart.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscforkhavenooutput.html language=enus -->
## TOPIC 00003: Connector does not have any outgoing transitions

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscforkhavenooutput.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscforkhavenooutput.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Connector does not have any outgoing transitions

A [connector](../lvscconcepts/sc_c_pseudocon.html) on the statechart diagram does not have any outgoing [transitions](../lvscconcepts/sc_c_trans.html).

[IMAGE alt='image' src='noloc_bd_edscforkhavenooutput.gif']

To correct this error, create an outgoing transition from the connector to another object on the statechart diagram.

[IMAGE alt='image' src='noloc_bd_edscforkhavenooutputfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscforkinputnotwired.html language=enus -->
## TOPIC 00004: Connector does not have an incoming transition

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscforkinputnotwired.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscforkinputnotwired.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Connector does not have an incoming transition

A [connector](../lvscconcepts/sc_c_pseudocon.html) on the statechart diagram does not have an incoming [transition](../lvscconcepts/sc_c_trans.html).

[IMAGE alt='image' src='noloc_bd_edscforkinputnotwired.gif']

To correct this error, create a transition and wire the transition to the connector.

[IMAGE alt='image' src='noloc_bd_edscforkinputnotwiredfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscforkinvalidinput.html language=enus -->
## TOPIC 00005: Invalid incoming transition

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscforkinvalidinput.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscforkinvalidinput.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Invalid incoming transition

A [transition](../lvscconcepts/sc_c_trans.html) does not connect to any [state](../lvsc/sc_state.html) or [pseudostate](../lvscconcepts/sc_c_pseudocon.html).

[IMAGE alt='image' src='noloc_bd_edscforkinvalidinput.gif']

To correct this error, wire the transition to a state or pseudostate.

[IMAGE alt='image' src='noloc_bd_edscforkinvalidinputfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscforkoutputjunction.html language=enus -->
## TOPIC 00006: Invalid transition to Junction connector

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscforkoutputjunction.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscforkoutputjunction.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Invalid transition to Junction connector

A [Fork](../lvsc/sc_fork.html) connector has an outgoing [transition](../lvscconcepts/sc_c_trans.html) that connects to a [Junction](../lvsc/sc_junction.html) connector.

[IMAGE alt='image' src='noloc_bd_edscforkoutputjunction.gif']

To correct this error, delete the transition from the Fork connector to the Junction connector.

[IMAGE alt='image' src='noloc_bd_edscforkoutputjunctionfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscforkoutputmustpointtostateindistinctregion.html language=enus -->
## TOPIC 00007: Outgoing transitions connect to substates in a single region

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscforkoutputmustpointtostateindistinctregion.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscforkoutputmustpointtostateindistinctregion.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Outgoing transitions connect to substates in a single region

The outgoing [transitions](../lvscconcepts/sc_c_trans.html) from a [Fork](../lvsc/sc_fork.html) connector on the statechart diagram only connect to [substates](../lvscconcepts/sc_c_hierarchy.html) within a single [region](../lvsc/sc_region.html).

[IMAGE alt='image' src='noloc_bd_edscforkoutputmustpointtostateindistinctregion.gif']

To correct this error, create transitions from the Fork connector to substates in different [orthogonal regions](../lvscconcepts/sc_c_orthogonal.html).

[IMAGE alt='image' src='noloc_bd_edscforkoutputmustpointtostateindistinctregionfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edschisthaveunexpectedoutput.html language=enus -->
## TOPIC 00008: Pseudostate has an outgoing transition

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edschisthaveunexpectedoutput.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edschisthaveunexpectedoutput.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Pseudostate has an outgoing transition

A [Terminal](../lvsc/sc_terminal.html), [Deep History](../lvsc/sc_deephistory.html), or [Shallow History](../lvsc/sc_shistory.html) 
[pseudostate](../lvscconcepts/sc_c_pseudocon.html) has an outgoing [transition](../lvscconcepts/sc_c_trans.html).

[IMAGE alt='image' src='noloc_bd_edschisthaveunexpectedoutput.gif']

To correct this error, change the outgoing transition to an incoming transition.

[IMAGE alt='image' src='noloc_bd_edschisthaveunexpectedoutputfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edschistmusthaveinput.html language=enus -->
## TOPIC 00009: Pseudostate must have at least one incoming transition

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edschistmusthaveinput.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edschistmusthaveinput.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Pseudostate must have at least one incoming transition

A [Terminal](../lvsc/sc_terminal.html), [Deep History](../lvsc/sc_deephistory.html), or [Shallow History](../lvsc/sc_shistory.html) [pseudostate](../lvscconcepts/sc_c_pseudocon.html) does not have at least one incoming [transition](../lvscconcepts/sc_c_trans.html).

[IMAGE alt='image' src='noloc_bd_edschistmusthaveinput.gif']

To correct this error, [create a transition](../lvschowto/sc_h_createtrans.html) from a state to the pseudostate.

[IMAGE alt='image' src='noloc_bd_edschistmusthaveinputfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscinitialinvalidendnode.html language=enus -->
## TOPIC 00010: Pseudostate is not connected to a state

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscinitialinvalidendnode.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscinitialinvalidendnode.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Pseudostate is not connected to a state

A [pseudostate](../lvscconcepts/sc_c_pseudocon.html) does not have any outgoing [transitions](../lvscconcepts/sc_c_trans.html) that connect to a [state](../lvsc/sc_state.html).

[IMAGE alt='image' src='noloc_bd_edscinitialinvalidendnode.gif']

To correct this error, [create a transition](../lvschowto/sc_h_createtrans.html) from the pseudostate to a state.

[IMAGE alt='image' src='noloc_bd_edscinitialinvalidendnodefixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscinitialmusthaveoutgoing.html language=enus -->
## TOPIC 00011: Pseudostate must be connected to a state within the same region

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscinitialmusthaveoutgoing.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscinitialmusthaveoutgoing.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Pseudostate must be connected to a state within the same region

A [pseudostate](../lvscconcepts/sc_c_pseudocon.html) does not have a [transition](../lvscconcepts/sc_c_trans.html) to a [state](../lvsc/sc_state.html) in the same [region](../lvsc/sc_region.html).

[IMAGE alt='image' src='noloc_bd_edscinitialmusthaveoutgoingfixed.gif']

To correct this error, [create a transition](../lvschowto/sc_h_createtrans.html) from the pseudostate to a state in the same region.

[IMAGE alt='image' src='noloc_bd_edscinitialmusthaveoutgoing.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscjoinhavenoinput.html language=enus -->
## TOPIC 00012: Connector does not have any incoming transitions

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscjoinhavenoinput.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscjoinhavenoinput.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Connector does not have any incoming transitions

A [connector](../lvscconcepts/sc_c_pseudocon.html) on the statechart diagram does not have any incoming [transitions](../lvscconcepts/sc_c_trans.html).

[IMAGE alt='image' src='noloc_bd_edscjoinhavenoinput.gif']

To correct this error, [create an incoming transition](../lvschowto/sc_h_createtrans.html) to the connector.

[IMAGE alt='image' src='noloc_bd_edscjoinhavenoinputfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscjoininputjunction.html language=enus -->
## TOPIC 00013: Invalid transition from Junction connector

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscjoininputjunction.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscjoininputjunction.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Invalid transition from Junction connector

A [Junction](../lvsc/sc_junction.html) connector has an outgoing [transition](../lvscconcepts/sc_c_trans.html) that connects to a [Join](../lvsc/sc_join.html) connector.

[IMAGE alt='image' src='noloc_bd_edscjoininputjunction.gif']

To correct this error, delete the transition from the Junction connector to the Join connector.

[IMAGE alt='image' src='noloc_bd_edscjoininputjunctionfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscjoininputmustoriginatefromstateindistinctregion.html language=enus -->
## TOPIC 00014: Incoming transitions originate from substates in a single region

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscjoininputmustoriginatefromstateindistinctregion.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscjoininputmustoriginatefromstateindistinctregion.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Incoming transitions originate from substates in a single region

[Transitions](../lvscconcepts/sc_c_trans.html) from [substates](../lvscconcepts/sc_c_hierarchy.html) in the same [region](../lvsc/sc_region.html) connect to a [Join](../lvsc/sc_join.html) connector.

[IMAGE alt='image' src='noloc_bd_edscjoininputmustoriginatefromstateindistinctregion.gif']

To correct this error, [create incoming transitions](../lvschowto/sc_h_createtrans.html) to the Join connector from substates in different [orthogonal regions](../lvscconcepts/sc_c_orthogonal.html).

[IMAGE alt='image' src='noloc_bd_edscjoininputmustoriginatefromstateindistinctregionfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscjoininvalidoutput.html language=enus -->
## TOPIC 00015: Invalid outgoing transition

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscjoininvalidoutput.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscjoininvalidoutput.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Invalid outgoing transition

A [transition](../lvscconcepts/sc_c_trans.html) has no origin [port](../lvsc/sc_port.html).

[IMAGE alt='image' src='noloc_bd_edscjoininvalidoutput.gif']

To correct this error, wire a [state](../lvsc/sc_state.html) or [pseudostate](../lvscconcepts/sc_c_pseudocon.html) to the transition.

[IMAGE alt='image' src='noloc_bd_edscjoininvalidoutputfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscjoinoutputnotwired.html language=enus -->
## TOPIC 00016: Connector does not have an outgoing transition

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscjoinoutputnotwired.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscjoinoutputnotwired.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Connector does not have an outgoing transition

A [connector](../lvscconcepts/sc_c_pseudocon.html) on the statechart diagram does not have an outgoing [transition](../lvscconcepts/sc_c_trans.html).

[IMAGE alt='image' src='noloc_bd_edscjoinoutputnotwired.gif']

To correct this error, create an outgoing transition from the connector to another object on the statechart diagram.

[IMAGE alt='image' src='noloc_bd_edscjoinoutputnotwiredfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscjunctionhavenoinput.html language=enus -->
## TOPIC 00017: Connector not reachable during execution

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscjunctionhavenoinput.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscjunctionhavenoinput.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Connector not reachable during execution

A [connector](../lvscconcepts/sc_c_pseudocon.html) on the statechart diagram has no incoming [transitions](../lvscconcepts/sc_c_trans.html). When the statechart runs, the flow of execution does not reach the connector.

[IMAGE alt='image' src='noloc_bd_edscjunctionhavenoinput.gif']

To correct this error, [create a transition or transitions](../lvschowto/sc_h_createtrans.html) to this connector.

[IMAGE alt='image' src='noloc_bd_edscjunctionhavenoinputfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscjunctionhavenooutput.html language=enus -->
## TOPIC 00018: Connector has no outgoing transitions

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscjunctionhavenooutput.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscjunctionhavenooutput.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Connector has no outgoing transitions

A [Junction](../lvsc/sc_junction.html) connector has no outgoing [transitions](../lvscconcepts/sc_c_trans.html).

[IMAGE alt='image' src='noloc_bd_edscjunctionhavenooutput.gif']

To correct this error, [create an outgoing transition](../lvschowto/sc_h_createtrans.html) from the Junction connector to another object on the statechart diagram.

[IMAGE alt='image' src='noloc_bd_edscjunctionhavenooutputfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscjunctionpartofcycle.html language=enus -->
## TOPIC 00019: Connector has incoming or outgoing transitions that create a cycle during transition evaluation

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscjunctionpartofcycle.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscjunctionpartofcycle.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Connector has incoming or outgoing transitions that create a cycle during transition evaluation

A [connector](../lvscconcepts/sc_c_pseudocon.html) has [transitions](../lvscconcepts/sc_c_trans.html) that create a cycle when the statechart evaluates the transitions. For example, you can create such a cycle by wiring two [Junction](../lvsc/sc_junction.html) connectors together.

[IMAGE alt='image' src='noloc_bd_edscjunctionpartofcycle.gif']

To correct this error, delete the transition that causes the cycle.

[IMAGE alt='image' src='noloc_bd_edscjunctionpartofcyclefixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edsclogichaveunwiredtunnel.html language=enus -->
## TOPIC 00020: Has unconnected transition segment

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edsclogichaveunwiredtunnel.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edsclogichaveunwiredtunnel.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Has unconnected transition segment

A [transition node](../lvscconcepts/sc_c_trans.html#transition_node) does not connect to any object on the statechart diagram.

[IMAGE alt='image' src='noloc_bd_edsclogichaveunwiredtunnel.gif']

To correct this error, wire the transition to an object on the statechart diagram.

[IMAGE alt='image' src='noloc_bd_edsclogichaveunwiredtunnelfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edsclogicinvalidnumoftunnels.html language=enus -->
## TOPIC 00021: Has less than or more than two segments

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edsclogicinvalidnumoftunnels.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edsclogicinvalidnumoftunnels.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Has less than or more than two segments

A [transition node](../lvscconcepts/sc_c_trans.html#transition_node) has less than or more than two wire segments running to and from the node.

[IMAGE alt='image' src='noloc_bd_edsclogicinvalidnumoftunnels.gif']

To correct this error, add or delete wires where applicable. You also can delete the node.

[IMAGE alt='image' src='noloc_bd_edsclogicinvalidnumoftunnelsfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edsclogicinvalidtunneldir.html language=enus -->
## TOPIC 00022: Has invalid transition direction

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edsclogicinvalidtunneldir.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edsclogicinvalidtunneldir.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Has invalid transition direction

A [transition node](../lvscconcepts/sc_c_trans.html#transition_node) connects to an object on the statechart diagram in an invalid direction, such as a transition node connecting to an [Initial](../lvsc/sc_initial.html) pseudostate.

[IMAGE alt='image' src='noloc_bd_edsclogicinvalidtunneldir.gif']

To correct this error, right-click the transition node and select **Reverse** from the shortcut menu to flip the node. Delete the wire segments on either side of the node. After you delete the wire segments, wire the transition node in the correct direction. You also can delete the transition node.

[IMAGE alt='image' src='noloc_bd_edsclogicinvalidtunneldirfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscnodenotcontainedinregion.html language=enus -->
## TOPIC 00023: Placed outside region

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscnodenotcontainedinregion.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscnodenotcontainedinregion.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Placed outside region

An invalid object, such as an [Initial](../lvsc/sc_initial.html) pseudostate, exists outside of a [region](../lvsc/sc_region.html).

[IMAGE alt='image' src='noloc_bd_edscnodenotcontainedinregion.gif']

To correct this error, move the object into a region. You also can delete the object.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscnodenotcontainedinstate.html language=enus -->
## TOPIC 00024: Placed outside state

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscnodenotcontainedinstate.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscnodenotcontainedinstate.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Placed outside state

An invalid object, such as a [Deep History](../lvsc/sc_deephistory.html) pseudostate, exists outside of a [state](../lvsc/sc_state.html).

[IMAGE alt='image' src='noloc_bd_edscnodenotcontainedinstate.gif']

To correct this error, move the object into a state. You also can delete the object.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscnodenotreachable.html language=enus -->
## TOPIC 00025: Is not reachable from the Initial pseudostate in this region

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscnodenotreachable.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscnodenotreachable.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Is not reachable from the Initial pseudostate in this region

A [state](../lvsc/sc_state.html) is not reachable from the [Initial](../lvsc/sc_initial.html) pseudostate in this [region](../lvsc/sc_region.html).

[IMAGE alt='image' src='noloc_bd_edscnodenotreachable.gif']

To correct this error, wire the Initial pseudostate to the state or [create a transition](../lvschowto/sc_h_createtrans.html) that connects the state to another state that has an incoming transition from the Initial pseudostate.

[IMAGE alt='image' src='noloc_bd_edscnodenotreachablefixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscregionhaveduplabel.html language=enus -->
## TOPIC 00026: Name is not unique within the state

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscregionhaveduplabel.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscregionhaveduplabel.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Name is not unique within the state

Multiple [regions](../lvsc/sc_region.html) in a [state](../lvsc/sc_state.html) have the same name.

[IMAGE alt='image' src='noloc_bd_edscregionhaveduplabel.gif']

To correct this error, rename one of the regions.

[IMAGE alt='image' src='noloc_bd_edscregionhaveduplabelfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscregionhaveinvalidnumofinitialnd.html language=enus -->
## TOPIC 00027: Has zero or more than one Initial pseudostate

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscregionhaveinvalidnumofinitialnd.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscregionhaveinvalidnumofinitialnd.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Has zero or more than one Initial pseudostate

A [region](../lvsc/sc_region.html) of the statechart diagram has zero or more than one [Initial](../lvsc/sc_initial.html) pseudostates.

[IMAGE alt='image' src='noloc_bd_edscregionhaveinvalidnumofinitialnd.gif']

To correct this error, either add an Initial pseudostate to the region or delete Initial pseudostates until only one remains in the region.

[IMAGE alt='image' src='noloc_bd_edscregionhaveinvalidnumofinitialndfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscstatebadsubdiag.html language=enus -->
## TOPIC 00028: Subdiagram contains errors

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscstatebadsubdiag.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscstatebadsubdiag.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Subdiagram contains errors

A [superstate](../lvscconcepts/sc_c_hierarchy.html) on the statechart diagram contains errors.

To correct this error, [display the state as a subdiagram](../lvschowto/sc_h_subdiag.html) and address the errors.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscstatefailcreateopaque.html language=enus -->
## TOPIC 00029: Failed to create subdiagram

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscstatefailcreateopaque.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscstatefailcreateopaque.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Failed to create subdiagram

The LabVIEW Statechart Module cannot [display a state as a subdiagram](../lvschowto/sc_h_subdiag.html).

This is an internal error. The Statechart Module cannot parse the subdiagram. If the problem persists, contact National Instruments technical support.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscstatefailembedopaque.html language=enus -->
## TOPIC 00030: Failed to embed subdiagram

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscstatefailembedopaque.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscstatefailembedopaque.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Failed to embed subdiagram

The LabVIEW Statechart Module cannot [display a state as a subdiagram](../lvschowto/sc_h_subdiag.html).

This is an internal error. The Statechart Module cannot parse the subdiagram. If the problem persists, contact National Instruments technical support.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscstatehavebadsubvi.html language=enus -->
## TOPIC 00031: Trigger, guard or action code contains errors

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscstatehavebadsubvi.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscstatehavebadsubvi.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Trigger, guard or action code contains errors

The [trigger](../lvscconcepts/sc_c_tga.html#trigger), [guard](../lvscconcepts/sc_c_tga.html#guard), or [action](../lvscconcepts/sc_c_tga.html#action) code for a [state](../lvsc/sc_state.html) or [transition](../lvscconcepts/sc_c_trans.html) contains errors.

To correct this error, double-click the state or transition to display the [Configure State](../lvsc/sc_configstate_db.html) or [Configure Transition](../lvsc/sc_config_db.html) dialog box. Locate the trigger, guard, or action code with errors and fix the errors.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscstatehaveduplabel.html language=enus -->
## TOPIC 00032: Name is not unique within the region

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscstatehaveduplabel.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscstatehaveduplabel.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Name is not unique within the region

Multiple [states](../lvsc/sc_state.html) in a [region](../lvsc/sc_region.html) have the same name.

[IMAGE alt='image' src='noloc_bd_edscstatehaveduplabel.gif']

To correct this error, rename one of the states.

[IMAGE alt='image' src='noloc_bd_edscstatehaveduplabelfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edscstatehavepassthroughtunnel.html language=enus -->
## TOPIC 00033: Has an incoming transition that does not terminate within the state

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edscstatehavepassthroughtunnel.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edscstatehavepassthroughtunnel.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Has an incoming transition that does not terminate within the state

A [transition](../lvscconcepts/sc_c_trans.html) enters and exits a [state](../lvsc/sc_state.html) without terminating.

[IMAGE alt='image' src='noloc_bd_edscstatehavepassthroughtunnel.gif']

To correct this error, delete the transition segment.

[IMAGE alt='image' src='noloc_bd_edscstatehavepassthroughtunnelfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edsctopdiaghaveinvalidnumofinitalnd.html language=enus -->
## TOPIC 00034: Top-level statechart diagram has zero or more than one Initial pseudostate

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edsctopdiaghaveinvalidnumofinitalnd.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edsctopdiaghaveinvalidnumofinitalnd.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Top-level statechart diagram has zero or more than one Initial pseudostate

The main [region](../lvsc/sc_region.html) of the statechart diagram has zero or more than one [Initial](../lvsc/sc_initial.html) pseudostates.

[IMAGE alt='image' src='noloc_bd_edsctopdiaghaveinvalidnumofinitalnd.gif']

To correct this error, either add an Initial pseudostate to the region or delete Initial pseudostates until only one remains in the region.

[IMAGE alt='image' src='noloc_bd_edsctopdiaghaveinvalidnumofinitalndfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edsctransitioninvalid.html language=enus -->
## TOPIC 00035: Transition exists between an invalid pair of objects, such as two pseudostates

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edsctransitioninvalid.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edsctransitioninvalid.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Transition exists between an invalid pair of objects, such as two pseudostates

You cannot wire a [transition node](../lvscconcepts/sc_c_trans.html#transition_node) between an invalid pair of objects, such as two [pseudostates](../lvscconcepts/sc_c_pseudocon.html).

[IMAGE alt='image' src='noloc_bd_edsctransitioninvalid.gif']

To correct this error, wire the transition node between a pair of valid objects. You also can delete the transition node.

[IMAGE alt='image' src='noloc_bd_edsctransitioninvalidfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edsctunnelunwiredonjunction.html language=enus -->
## TOPIC 00036: Not connected to outer transition segment

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edsctunnelunwiredonjunction.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edsctunnelunwiredonjunction.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Not connected to outer transition segment

A [port](../lvsc/sc_port.html) on the statechart diagram does not connect to a [transition](../lvscconcepts/sc_c_trans.html).

[IMAGE alt='image' src='noloc_bd_edsctunnelunwiredonjunction.gif']

To correct this error, delete the port or connect the port to an object on the statechart diagram.

[IMAGE alt='image' src='noloc_bd_edsctunnelunwiredonjunctionfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/edsctunnelunwiredonregion.html language=enus -->
## TOPIC 00037: Not connected to transition segment

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/edsctunnelunwiredonregion.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/edsctunnelunwiredonregion.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Not connected to transition segment

A [port](../lvsc/sc_port.html) on the statechart diagram does not connect to a [transition](../lvscconcepts/sc_c_trans.html).

[IMAGE alt='image' src='noloc_bd_edsctunnelunwiredonregion.gif']

To correct this error, delete the port or [create a transition](../lvschowto/sc_h_createtrans.html) from the port to an object on the statechart diagram.

[IMAGE alt='image' src='noloc_bd_edsctunnelunwiredonregionfixed.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_comm.html language=enus -->
## TOPIC 00038: Statechart Communication Functions

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_comm.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_comm.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Communication Functions

**Owning Palette:** [Statechart Functions and Objects](../lvsc/sc_pal.html)

**Requires:** Statechart Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Statechart Communication functions to execute a statechart, send [triggers](../lvscconcepts/sc_c_tga.html#trigger) to a statechart, and determine whether a particular state is active. You can place these functions on a block diagram.

The functions on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| IsIn | Determines whether the specified state is active. An active state is one that a statechart is currently in. You can use this function in either a guard, an action, or a subVI that a guard or action calls. |
| Run Statechart | Executes an instance of the linked statechart. You typically place this function inside a loop in the caller VI. The parameters of this function depend on whether you configured the statechart to be synchronous or asynchronous. You configure the statechart by using the Statechart Code Generation page of the Project Library Properties dialog box. |
| Send External Trigger | Sends a trigger to the external queue of an instance of the linked statechart. You can use this function in the caller VI or in a VI that runs parallel to the caller VI. You can use this function with only asynchronous statecharts. |
| Send Internal Trigger | Sends a trigger to the internal queue of the statechart. You can use this function within only an action or in a subVI that an action calls. You can use this function with both asynchronous and synchronous statecharts. However, you cannot use this function in a statechart that is configured for a single-cycle loop application. |

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_deephistory.html language=enus -->
## TOPIC 00039: Deep History Pseudostate

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_deephistory.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_deephistory.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Deep History Pseudostate

**Owning Palette:** [Statechart Development Objects](../lvsc/sc_obj.html)

**Requires:** Statechart Module

Specifies that, when the statechart leaves and then returns to a [region](../lvsc/sc_region.html), the statechart enters the lowest-level [substates](../lvscconcepts/sc_c_hierarchy.html) that were active when the statechart left the region.

To use the Deep History [pseudostate](../lvscconcepts/sc_c_pseudocon.html), place this pseudostate in a region and then [create a transition](../lvschowto/sc_h_createtrans.html) from a [state](../lvsc/sc_state.html) to this pseudostate.

|  | Note You use this pseudostate in Part 5 of the Getting Started tutorial. |
| --- | --- |

[IMAGE alt='image' src='dhistory.gif']

| Add to the statechart diagram | Find on the palette |
| --- | --- |

|  | Note Statechart history is erased after the statechart terminates. |
| --- | --- |

You can create multiple incoming transitions to this pseudostate, but you cannot create any outgoing transitions from this pseudostate.

The Deep History pseudostate returns to the lowest-level substates that were active when the statechart left the region. To return to the highest-level substates, use the [Shallow History](../lvsc/sc_shistory.html) pseudostate.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_fork.html language=enus -->
## TOPIC 00040: Fork Connector

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_fork.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_fork.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Fork Connector

**Owning Palette:** [Statechart Development Objects](../lvsc/sc_obj.html)

**Requires:** Statechart Module

Splits one incoming [transition](../lvscconcepts/sc_c_trans.html) segment into multiple outgoing segments. You can place this [connector](../lvscconcepts/sc_c_pseudocon.html) within only a [state](../lvsc/sc_state.html).

Use the Fork connector to [create one transition to multiple substates](../lvschowto/sc_h_tfork.html). Each [substate](../lvscconcepts/sc_c_hierarchy.html) must exist in a different [orthogonal region](../lvscconcepts/sc_c_orthogonal.html).

[IMAGE alt='image' src='fork_connector.gif']

| Add to the statechart diagram | Find on the palette |
| --- | --- |

You can [create only one incoming transition segment](../lvschowto/sc_h_createtrans.html#stateobject) to a Fork connector. You must create at least two outgoing segments from a Fork connector. Each outgoing segment must connect to a substate in a different orthogonal region. The statechart considers all segments as a single transition, even though the outgoing segments terminate in different substates.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_initial.html language=enus -->
## TOPIC 00041: Initial Pseudostate

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_initial.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_initial.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Initial Pseudostate

**Owning Palette:** [Statechart Development Objects](../lvsc/sc_obj.html)

**Requires:** Statechart Module

Specifies the first [state](../lvsc/sc_state.html) that the enclosing [region](../lvsc/sc_region.html) enters when the statechart enters that region. To specify this state, [create a transition](../lvschowto/sc_h_createtrans.html) from the Initial [pseudostate](../lvscconcepts/sc_c_pseudocon.html) to the state that you want to enter first.

You can place this pseudostate within only a region or at the top level of a statechart diagram. Each region must have one and only one Initial pseudostate.

[IMAGE alt='image' src='initial_pseudo.gif']

| Add to the statechart diagram | Find on the palette |
| --- | --- |

No transitions can enter this pseudostate, and only one transition can exit this pseudostate. Because the statechart executes the initial transition unconditionally, the outgoing transition segment cannot have a [trigger](../lvscconcepts/sc_c_tga.html#trigger) or [guard](../lvscconcepts/sc_c_tga.html#guard).

|  | Note You cannot create a transition from an Initial pseudostate to a Junction connector. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_isin.html language=enus -->
## TOPIC 00042: IsIn Function

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_isin.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_isin.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### IsIn Function

**Owning Palette:** [Statechart Communication Functions](../lvsc/sc_comm.html)

**Requires:** Statechart Module

Determines whether the specified [state](../lvsc/sc_state.html) is active. An active state is one that a statechart is currently in. You can [use this function](../lvschowto/sc_h_isin.html) in either a [guard](../lvscconcepts/sc_c_tga.html#guard), an [action](../lvscconcepts/sc_c_tga.html#action), or a [subVI](/csh?topicname=lvconcepts/creating_subvis.html) that a guard or action calls.

Use this function to determine the active substate of an [orthogonal region](../lvscconcepts/sc_c_orthogonal.html) or a different statechart.

[Details](#details)

[IMAGE alt='image' src='isin_c.gif']

|  | Statechart States specifies the list of states in the current statechart. After wiring the StatechartState cluster control, located on the left side of the block diagram to this input. Then, double-click the IsIn function to specify a state to check. Note If you place this function in a subVI, you must pass this parameter to that subVI. |
| --- | --- |
|  | Note If you place this function in a subVI, you must pass this parameter to that subVI. |
|  | IsIn? returns TRUE if the specified state is active. IsIn? returns FALSE if the specified state is not active. |

#### IsIn Details

You can [configure the icon style](../lvscconcepts/sc_c_iconstyles.html) of this function to display the [custom icon](/csh?topicname=lvconcepts/using_icons.html) of the statechart diagram and/or the name or path of the specified state.

In determining whether a state is active, this function analyzes the state vector, which is the path of states and [regions](../lvsc/sc_region.html) that contain the state. For example, consider the following figure:

[IMAGE alt='image' src='isin_usage.gif']

Consider a situation where you want to check State 4 in State 1, but not State 4 in State 3. In this situation, the function takes into account the regions and states that contain the State 4 you specify.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_join.html language=enus -->
## TOPIC 00043: Join Connector

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_join.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_join.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Join Connector

**Owning Palette:** [Statechart Development Objects](../lvsc/sc_obj.html)

**Requires:** Statechart Module

Merges multiple incoming [transition](../lvscconcepts/sc_c_trans.html) segments into one outgoing segment. You can place this [connector](../lvscconcepts/sc_c_pseudocon.html) within only a [state](../lvsc/sc_state.html).

Use the Join connector to [specify the substates that a statechart must be in before the statechart can leave the enclosing superstate](../lvschowto/sc_h_join.html). Each [substate](../lvscconcepts/sc_c_hierarchy.html) must exist in a different [orthogonal region](../lvscconcepts/sc_c_orthogonal.html).

[IMAGE alt='image' src='join_connector.gif']

| Add to the statechart diagram | Find on the palette |
| --- | --- |

You must [create at least two incoming transition segments](../lvschowto/sc_h_createtrans.html#stateobject) to the Join connector. Each incoming segment must originate from a substate in a different orthogonal region. You can create only one outgoing segment from the Join connector. The statechart considers all segments as a single transition, even though the incoming segments originate in different substates.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_junction.html language=enus -->
## TOPIC 00044: Junction Connector

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_junction.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_junction.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Junction Connector

**Owning Palette:** [Statechart Development Objects](../lvsc/sc_obj.html)

**Requires:** Statechart Module

Connects common elements of multiple [transitions](../lvscconcepts/sc_c_trans.html) together. For example, you can use a Junction [connector](../lvscconcepts/sc_c_pseudocon.html) to specify that multiple transitions use the same [action](../lvscconcepts/sc_c_tga.html#action), even though each transition might have a different [trigger](../lvscconcepts/sc_c_tga.html#trigger). You can place this connector only in a [region](../lvsc/sc_region.html).

[IMAGE alt='image' src='junction.gif']

| Add to the statechart diagram | Find on the palette |
| --- | --- |

You can create multiple incoming and outgoing transition segments for a Junction connector. However, you cannot specify a trigger for these segments.

The statechart executes all Junction transitions during a single [iteration](../lvscconcepts/sc_c_iteration.html) of the statechart. You can [configure the priority](../lvschowto/sc_h_transprior.html) of these transitions.

|  | Note You cannot create a transition from an Initial pseudostate to a Junction connector. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_obj.html language=enus -->
## TOPIC 00045: Statechart Development Objects

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_obj.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_obj.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Development Objects

**Owning Palette:** [Statechart Functions and Objects](../lvsc/sc_pal.html)

**Requires:** Statechart Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Statechart Development objects, consisting of [states](../lvsc/sc_state.html), [regions](../lvsc/sc_region.html), [pseudostates, and connectors](../lvscconcepts/sc_c_pseudocon.html), to construct statecharts. You can place these objects on a statechart diagram.

| Palette Object | Description |
| --- | --- |
| Deep History | Specifies that, when the statechart leaves and then returns to a region, the statechart enters the lowest-level substates that were active when the statechart left the region. To use the Deep History pseudostate, place this pseudostate in a region and then create a transition from a state to this pseudostate. Note You use this pseudostate in Part 5 of the Getting Started tutorial. |
| Fork | Splits one incoming transition segment into multiple outgoing segments. You can place this connector within only a state. Use the Fork connector to create one transition to multiple substates. Each substate must exist in a different orthogonal region. |
| Initial | Specifies the first state that the enclosing region enters when the statechart enters that region. To specify this state, create a transition from the Initial pseudostate to the state that you want to enter first. You can place this pseudostate within only a region or at the top level of a statechart diagram. Each region must have one and only one Initial pseudostate. |
| Join | Merges multiple incoming transition segments into one outgoing segment. You can place this connector within only a state. Use the Join connector to specify the substates that a statechart must be in before the statechart can leave the enclosing superstate. Each substate must exist in a different orthogonal region. |
| Junction | Connects common elements of multiple transitions together. For example, you can use a Junction connector to specify that multiple transitions use the same action, even though each transition might have a different trigger. You can place this connector only in a region. |
| Port | Indicates where a transition leaves a state or connector. Ports also indicate where a transition passes through a region. When you are editing a statechart, ports appear automatically as you create transitions. You can place ports manually only when you are viewing a state as a subdiagram. |
| Region | Defines the area in which you can place states and pseudostates. Each region must contain an Initial pseudostate and at least one substate. The top-level statechart diagram represents a region. You can place regions within only a state. |
| Shallow History | Specifies that, when the statechart leaves and then returns to a region, the statechart enters the highest-level substates that were active when the statechart left the region. To use the Shallow History pseudostate, place this pseudostate in a region and then create a transition from a state to this pseudostate. |
| State | Defines a state, which is a unique condition in which the statechart can be. You must place all states within a region. All states must have at least one incoming transition. |
| Terminal | Specifies a state that can terminate the execution of the enclosing region. To specify this state, create a transition from a state to a Terminal pseudostate. You can place this pseudostate within only a region. You can place more than one Terminal pseudostate in a region. |

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_pal.html language=enus -->
## TOPIC 00046: Statechart Functions and Objects

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_pal.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Functions and Objects

June 2013, 372105F-01

**Requires:** Statechart Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Statechart Communication functions to communicate with statecharts from LabVIEW. Use the Statechart Development objects to construct statecharts.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

| Subpalette | Description |
| --- | --- |
| Statechart Communication Functions | Use the Statechart Communication functions to execute a statechart, send triggers to a statechart, and determine whether a particular state is active. You can place these functions on a block diagram. The functions on this palette can return general LabVIEW error codes. |
| Statechart Development Objects | Use the Statechart Development objects, consisting of states, regions, pseudostates, and connectors, to construct statecharts. You can place these objects on a statechart diagram. |

© 2007–2013 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_port.html language=enus -->
## TOPIC 00047: Port

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_port.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_port.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Port

**Owning Palette:** [Statechart Development Objects](../lvsc/sc_obj.html)

**Requires:** Statechart Module

Indicates where a [transition](../lvscconcepts/sc_c_trans.html) leaves a [state](../lvsc/sc_state.html) or [connector](../lvscconcepts/sc_c_pseudocon.html). Ports also indicate where a transition passes through a [region](../lvsc/sc_region.html).

When you are editing a statechart, ports appear automatically as you [create transitions](../lvschowto/sc_h_createtrans.html). You can place ports manually only when you are viewing a state as a [subdiagram](../lvscconcepts/sc_c_subsc.html).

[IMAGE alt='image' src='port.gif']

| Add to the statechart diagram | Find on the palette |
| --- | --- |

Triangular ports indicate where the transition enters a state or connector. You cannot place triangular ports on a subdiagram. LabVIEW places triangular ports automatically as you create transitions on the statechart diagram.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_region.html language=enus -->
## TOPIC 00048: Region

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_region.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_region.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Region

**Owning Palette:** [Statechart Development Objects](../lvsc/sc_obj.html)

**Requires:** Statechart Module

Defines the area in which you can place [states](../lvsc/sc_state.html) and [pseudostates](../lvscconcepts/sc_c_pseudocon.html). Each region must contain an [Initial](../lvsc/sc_initial.html) pseudostate and at least one [substate](../lvscconcepts/sc_c_hierarchy.html).

The top-level statechart diagram represents a region. You can place regions within only a state.

[IMAGE alt='image' src='region.gif']

| Add to the statechart diagram | Find on the palette |
| --- | --- |

Using regions allows you to place states within states, as the previous figure shows. Two or more regions in the same state are called [orthogonal regions](../lvscconcepts/sc_c_orthogonal.html).

When the statechart enters a region, the statechart enters the substate to which the [Initial](../lvsc/sc_initial.html) pseudostate is connected, except in the following situations:

- The statechart is following a transition directly to a substate.
- The statechart has entered that region at least once since you first executed the statechart, and the region contains a Shallow History or Deep History pseudostate.

In these situations, the statechart enters the substate that the transition or pseudostate specifies.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_runsc.html language=enus -->
## TOPIC 00049: Run Statechart Function

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_runsc.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_runsc.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Run Statechart Function

**Owning Palette:** [Statechart Communication Functions](../lvsc/sc_comm.html)

**Requires:** Statechart Module

Executes an [instance](../lvscconcepts/sc_c_instances.html) of the linked statechart. You typically place this function inside a [loop](/csh?topicname=lvhowto/using_loops.html) in the [caller VI](../lvscconcepts/sc_c_callervi.html).

The parameters of this function depend on whether you configured the statechart to be [synchronous or asynchronous](../lvscconcepts/sc_c_syncasync.html). You configure the statechart by using the [Statechart Code Generation](../lvsc/sc_codegen.html) page of the [Project Library Properties](/csh?topicname=lvdialog/library_props_db.html) dialog box.

[Details](#details)

#### Run Statechart (Synchronous)

[IMAGE alt='image' src='run_statechart_sync.gif']

|  | Trigger specifies the trigger to send to the statechart. To specify a trigger, right-click this input terminal and select Create»Control or Create»Constant from the shortcut menu to create an enumerated type control/constant that contains the list of available triggers.You can send only triggers that you create by using the Edit Triggers and Groups dialog box. The default value is NULL. |
| --- | --- |
|  | Inputs specifies the input data to the statechart. You define the type of input data by editing the Inputs.ctl type definition of the .lvsc file. |
|  | Init? is TRUE if you want to restart the statechart from any initial conditions you provide. Init? is FALSE if you do not want to restart the statechart. The default value is FALSE. |
|  | Outputs returns the output data from the statechart. You define the type of data by editing the Outputs.ctl type definition of the .lvsc file. |
|  | Terminated? returns TRUE after the top-level statechart enters the Terminal pseudostate, that is, after the entire statechart finishes executing. Terminated? returns FALSE at all other times. |

#### Run Statechart (Asynchronous)

[IMAGE alt='image' src='run_statechart_async.gif']

|  | Instance Name specifies the instance of the statechart you want to run. |
| --- | --- |
|  | Inputs specifies the input data to the statechart. You define the type of input data by editing the Inputs.ctl type definition of the .lvsc file. |
|  | Init? is TRUE if you want to restart the statechart from any initial conditions you provide. Init? is FALSE if you do not want to restart the statechart. The default value is FALSE. |
|  | Outputs returns the output data from the statechart. You define the type of data by editing the Outputs.ctl type definition of the .lvsc file. |
|  | Terminated? returns TRUE after the top-level statechart enters the Terminal pseudostate, that is, after the entire statechart finishes executing. Terminated? returns FALSE at all other times. |

#### Run Statechart Details

You must link this function to a statechart before configuring the parameters. To link this function to a statechart, right-click this function and select **Link to Statechart** from the shortcut menu. You also can double-click the function. You must link to a statechart for which you have [generated code](../lvschowto/sc_h_gencode.html).

|  | Tip Instead of dragging this function from the palette to the block diagram of the caller VI, you can drag the .lvsc file from the Project Explorer window onto a block diagram to create a Run Statechart function that is linked to the statechart. |
| --- | --- |

You can [configure the icon style](../lvscconcepts/sc_c_iconstyles.html) of this function to display the [custom icon](/csh?topicname=lvconcepts/using_icons.html) of the statechart diagram, the statechart to which this function links, and/or the trigger that this function sends to the linked statechart.

You can configure several inputs and outputs of this function. Right-click this function and select **Configure** from the shortcut menu to display the [Configure Statechart Run Node](../lvsc/configure_run_statechart_db.html) dialog box.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_send_event.html language=enus -->
## TOPIC 00050: Send External Trigger Function

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_send_event.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_send_event.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Send External Trigger Function

**Owning Palette:** [Statechart Communication Functions](../lvsc/sc_comm.html)

**Requires:** Statechart Module

Sends a [trigger](../lvscconcepts/sc_c_tga.html#trigger) to the [external queue](../lvscconcepts/sc_c_trigqueue.html) of an [instance](../lvscconcepts/sc_c_instances.html) of the linked statechart. You can use this function in the [caller VI](../lvscconcepts/sc_c_callervi.html) or in a VI that runs parallel to the caller VI.

You can use this function with only [asynchronous statecharts](../lvscconcepts/sc_c_syncasync.html).

[Details](#details)

[IMAGE alt='image' src='sendevent_c.gif']

|  | Instance Name specifies the instance of the statechart to which this function sends triggers. The value of this parameter must match the value of the Instance Name parameter of the Run Statechart function to which you want to send triggers. |
| --- | --- |
|  | Trigger specifies the trigger to send to the statechart. To specify a trigger, right-click this input and select Create»Control or Create»Constant from the shortcut menu to create an enumerated type control/constant that contains the list of available triggers.You can send only triggers that you define by using the Edit Triggers and Groups dialog box. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Timed out? returns TRUE if this function did not send the Trigger in time. Timed out? returns FALSE if this function sent the Trigger in time. Configure the timeout length by using the Statechart Code Generation page of the Project Library Properties dialog box. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Send External Trigger Details

You must link this function to a statechart before configuring the parameters. To link this function to a statechart, right-click this function and select **Link to Statechart** from the shortcut menu. You must link to a statechart for which you have [generated code](../lvschowto/sc_h_gencode.html). You also must link a [Run Statechart](../lvsc/sc_runsc.html) function to the same statechart.

|  | Tip Instead of linking this function to a statechart manually, you can right-click an asynchronous Run Statechart function and select Create Send External Trigger Function from the shortcut menu to create a Send External Trigger function that is linked to the statechart. |
| --- | --- |

You can [configure the icon style](../lvscconcepts/sc_c_iconstyles.html) of this function to display the [custom icon](/csh?topicname=lvconcepts/using_icons.html) of the statechart diagram, the statechart to which this function links, and/or the trigger that this function sends to the linked statechart.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_send_signal.html language=enus -->
## TOPIC 00051: Send Internal Trigger Function

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_send_signal.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_send_signal.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Send Internal Trigger Function

**Owning Palette:** [Statechart Communication Functions](../lvsc/sc_comm.html)

**Requires:** Statechart Module

Sends a [trigger](../lvscconcepts/sc_c_tga.html#trigger) to the [internal queue](../lvscconcepts/sc_c_trigqueue.html) of the statechart. You can [use this function](../lvschowto/sc_h_sendsignal.html) within only an [action](../lvscconcepts/sc_c_tga.html#action) or in a [subVI](/csh?topicname=lvconcepts/creating_subvis.html) that an action calls.

You can use this function with both [asynchronous and synchronous](../lvscconcepts/sc_c_syncasync.html) statecharts. However, you cannot use this function in a statechart that is configured for a single-cycle loop application.

You can configure this function either by using the parameters or by double-clicking the function.

[Details](#details)

[IMAGE alt='image' src='sendinternal.gif']

|  | Internal Queue In specifies the internal queue of the statechart. Wire the Outputs»InternalQueue»All Elements cluster element, located on the left side of the block diagram, to this input terminal. Then, double-click this function to specify a trigger to send to the internal queue. Note If you place this function in a subVI, you must pass this parameter to that subVI. |
| --- | --- |
|  | Note If you place this function in a subVI, you must pass this parameter to that subVI. |
|  | Internal Queue Out returns the internal queue of the statechart. Wire this output terminal to the Outputs»InternalQueue»All Elements cluster element, located on the right side of the guard/action block diagram. Note If you place this function in a subVI, you must return this parameter from that subVI. |
|  | Note If you place this function in a subVI, you must return this parameter from that subVI. |
|  | Trigger specifies the trigger to send to the internal queue. |
|  | Overflow? returns TRUE if the internal queue is full and cannot accept any more triggers. Overflow? returns FALSE if the internal queue can accept more triggers. You configure the size of the internal queue by using the Statechart Code Generation page of the Project Library Properties dialog box. |

#### Send Internal Trigger Details

You can [configure the icon style](../lvscconcepts/sc_c_iconstyles.html) of this function to display the [custom icon](/csh?topicname=lvconcepts/using_icons.html) of the statechart diagram and/or the trigger that this function sends to the linked statechart.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_shistory.html language=enus -->
## TOPIC 00052: Shallow History Pseudostate

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_shistory.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_shistory.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Shallow History Pseudostate

**Owning Palette:** [Statechart Development Objects](../lvsc/sc_obj.html)

**Requires:** Statechart Module

Specifies that, when the statechart leaves and then returns to a [region](../lvsc/sc_region.html), the statechart enters the highest-level [substates](../lvscconcepts/sc_c_hierarchy.html) that were active when the statechart left the region.

To use the Shallow History [pseudostate](../lvscconcepts/sc_c_pseudocon.html), place this pseudostate in a region and then [create a transition](../lvschowto/sc_h_createtrans.html) from a [state](../lvsc/sc_state.html) to this pseudostate.

[IMAGE alt='image' src='shistory.gif']

| Add to the statechart diagram | Find on the palette |
| --- | --- |

|  | Note Statechart history is erased after the statechart terminates. |
| --- | --- |

You can create multiple incoming transitions to this pseudostate, but you cannot create any outgoing transitions from this pseudostate.

The Shallow History pseudostate returns to the highest-level substates that were active when the statechart left the region. To return to the lowest-level substates, use the [Deep History](../lvsc/sc_deephistory.html) pseudostate.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_state.html language=enus -->
## TOPIC 00053: State

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_state.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_state.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### State

**Owning Palette:** [Statechart Development Objects](../lvsc/sc_obj.html)

**Requires:** Statechart Module

Defines a state, which is a unique condition in which the statechart can be.

You must [place](../lvschowto/sc_h_defineobj.html) all states within a [region](../lvsc/sc_region.html). All states must have at least one incoming [transition](../lvscconcepts/sc_c_trans.html).

[IMAGE alt='image' src='state.gif']

| Add to the statechart diagram | Find on the palette |
| --- | --- |

For example, a light bulb connected to a circuit might have two states, ON and OFF. In the ON state, the circuit provides power to the light bulb. In the OFF state, the circuit does not provide power to the light bulb.

In the previous figure, the inner border (1) is where you click to create [transitions](../lvscconcepts/sc_c_trans.html) between states. The outer border (2) is where you click to manipulate the state on the [statechart diagram](../lvscconcepts/sc_c_editor.html). For example, you can press the <Ctrl> key and click and drag this border to duplicate a state.

For each state, you can [define several types of actions](../lvschowto/sc_h_configstate.html) that modify [output and state data](../lvscconcepts/sc_c_iodata.html). The valid types of actions include [entry actions](../lvscconcepts/sc_c_entryexit.html), [exit actions](../lvscconcepts/sc_c_entryexit.html), and [static reactions](../lvscconcepts/sc_c_staticrxn.html).

You can place states within only a [region](../lvsc/sc_region.html). Because you can place regions within states, you can use regions to create hierarchical [superstates and substates](../lvscconcepts/sc_c_hierarchy.html).

Within a region, each state must have a unique name. The statechart can be in one state in a region at a time.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/sc_terminal.html language=enus -->
## TOPIC 00054: Terminal Pseudostate

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/sc_terminal.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/sc_terminal.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Terminal Pseudostate

**Owning Palette:** [Statechart Development Objects](../lvsc/sc_obj.html)

**Requires:** Statechart Module

Specifies a [state](../lvsc/sc_state.html) that can terminate the execution of the enclosing [region](../lvsc/sc_region.html). To specify this state, [create a transition](../lvschowto/sc_h_createtrans.html) from a state to a Terminal [pseudostate](../lvscconcepts/sc_c_pseudocon.html). You can place this pseudostate within only a region. You can place more than one Terminal pseudostate in a region.

[IMAGE alt='image' src='terminal.gif']

| Add to the statechart diagram | Find on the palette |
| --- | --- |

|  | Note Because the top-level statechart diagram represents a region, a Terminal pseudostate at this level terminates the entire statechart. |
| --- | --- |

More than one [transition](../lvscconcepts/sc_c_trans.html) can enter this pseudostate, which means more than one state can terminate a region. No transitions can leave this pseudostate.

After a statechart enters the Terminal pseudostate, all [substates](../lvscconcepts/sc_c_hierarchy.html) in enclosing region terminate execution.

<!--NI_TOPIC bundle=labview-statechart-module path=lvsc/statechart_error_codes.html language=enus -->
## TOPIC 00055: Error Codes (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvsc/statechart_error_codes.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvsc/statechart_error_codes.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Error Codes (Statechart Module)

The [Statechart](sc_pal.html) functions and objects can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| 1480 | LabVIEW did not generate documentation files because some of the files are read-only. Choose a different path for the generation of the documentation files or change the read/write permission of the files. |
| 1538 | To perform this operation you must have the LabVIEW Statechart Module installed. |
| 1549 | An unexpected error occurred during statechart code generation. |
| 1563 | LabVIEW did not generate documentation files for the statechart. Ensure all configuration windows are closed. |

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_buildconfig.html language=enus -->
## TOPIC 00056: Building and Configuring Statecharts (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_buildconfig.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_buildconfig.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Building and Configuring Statecharts (Statechart Module)

Before a statechart is ready to execute, you must build and configure the statechart to perform the way you want the statechart to perform upon execution.

This book contains information about using [Statechart Communication](../lvsc/sc_comm.html) functions and [Statechart Development](../lvsc/sc_obj.html) objects to build and configure statecharts.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_callervi.html language=enus -->
## TOPIC 00057: Using a Caller VI to Execute a Statechart (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_callervi.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_callervi.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Using a Caller VI to Execute a Statechart (Statechart Module)

The caller VI is the VI you [create](../lvschowto/sc_h_callsc.html) that contains a [Run Statechart](../lvsc/sc_runsc.html) function. This function creates and executes an [instance](sc_c_instances.html) of a statechart. Executing a statechart means sending [input data](sc_c_iodata.html) to a statechart. You also can use the caller VI to send [triggers](sc_c_tga.html#trigger) to a statechart.

The caller VI has a different structure depending on whether the statechart is [asynchronous or synchronous](sc_c_syncasync.html). The following sections provide information about these differences.

#### Asynchronous Statecharts

Executing asynchronous statecharts involves the following two processes:

- Executing the statechart by using the Run Statechart function.
- Sending triggers to the external queue by using the Send External Trigger function.

In this situation, the VI that contains the Run Statechart function is the caller VI. You can send triggers to the external queue from another VI or a parallel loop in the caller VI. The following figure shows a caller VI that both executes an asynchronous statechart and sends triggers to the external queue.

[IMAGE alt='image' src='callervi_async.gif']

In the previous figure, the Statechart Loop, which is a [While Loop](/csh?topicname=glang/while_loop.html), executes the statechart. The **Inputs** control contains any input data of the types that you [defined](../lvschowto/sc_h_iodata.html). The **Outputs** indicator returns output data from the statechart. The **Instance Name** constant specifies Statechart 1 as the name of the statechart [instance](sc_c_instances.html).

The Trigger Loop, which can execute in [parallel](/csh?topicname=lvconcepts/labview_and_hyper_threading.html) with the Statechart Loop, contains an [Event structure](/csh?topicname=glang/event_structure.html). This Event structure handles events that occur within the VI. In this case, an event occurs when you click the **Button** front panel control. When you click this control, the Event structure detects this event and the Send External Trigger function sends the Trigger1 trigger to the Statechart 1 statechart instance.

|  | Note This example uses the caller VI to send triggers to an external queue. However, as long as the caller VI is running and the statechart is in memory, you can use any VI to send triggers to an external queue. This behavior means that you can place the Trigger Loop and Statechart Loop in separate VIs. |
| --- | --- |

#### Synchronous Statecharts

The following figure shows a caller VI that executes a synchronous statechart.

[IMAGE alt='image' src='callervi_sync.gif']

Notice the differences between this caller VI and the asynchronous caller VI. The typical use case for a synchronous statechart is an application that executes at defined time intervals. Therefore, this caller VI uses a [Timed Loop](/csh?topicname=glang/timed_loop.html) with frames to (1) read input data, (2) execute the statechart, and (3) write output data within the specified time. The Read Input Data and Write Output Data subVIs represent LabVIEW block diagram code that communicates with measurement hardware. For example, these VIs can represent NI-DAQmx code that communicates with an NI DAQ device.

|  | Note Sending triggers to synchronous statecharts is optional. If you do not send triggers, LabVIEW sends the NULL trigger to the statechart. If you do send triggers to a synchronous statechart, you can send these triggers from only the caller VI. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_callsc.html language=enus -->
## TOPIC 00058: Executing Statecharts (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_callsc.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_callsc.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Executing Statecharts (Statechart Module)

Each statechart has an associated [Run Statechart](../lvsc/sc_runsc.html) function that contains the LabVIEW code that represents that statechart. To execute a statechart, you must [generate code for that statechart](../lvschowto/sc_h_gencode.html) to update the Run Statechart function, which you place in a [caller VI](sc_c_callervi.html). You can [debug the statechart](../lvschowto/sc_h_debugsc.html) while the caller VI is running.

You can execute statecharts on a variety of different [targets](sc_c_targets.html), including certain embedded devices, PDAs, National Instruments Real-Time Series targets, and NI FPGA targets. Refer to the National Instruments Web site for information about these products. You specify the execution target by using the [Statechart Code Generation](../lvsc/sc_codegen.html) page of the [Project Library Properties](/csh?topicname=lvdialog/library_props_db.html) dialog box.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_editor.html language=enus -->
## TOPIC 00059: Statechart Editor Window (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_editor.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_editor.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Editor Window (Statechart Module)

You use the Statechart Editor window to edit a statechart. You can display the Statechart Editor window in one of the following ways:

- Double-click the Diagram.vi item in the Project Explorer window of the statechart.
- Right-click the Diagram.vi item and select Open from the shortcut menu.
- Right-click a Run Statechart function that links to the statechart and select View»Statechart Diagram from the shortcut menu.

The Statechart Editor window, which [displays](../lvschowto/sc_h_dispsc.html) a statechart diagram, is similar to the LabVIEW window that displays a block diagram. In both of these windows, you can place objects from the [Functions](/csh?topicname=glang/functions_palette.html) palette on the diagram, use the LabVIEW [tools](/csh?topicname=glang/tools_palette_icons.html) to manipulate objects, and connect objects together. However, the Statechart Editor window is different from the LabVIEW window in the following ways:

- You can place only Statechart Development objects on a statechart diagram. You cannot place LabVIEW VIs, functions, or structures directly on a statechart diagram. You also can use these functions in a guard or action .
- The LabVIEW block diagram window displays the Run button on the toolbar. The Statechart Editor window displays the Generate Code button on the toolbar. Clicking this button generates code for the statechart.
- The LabVIEW block diagram has a front panel window. The Statechart Editor window does not have a front panel window.
- On the LabVIEW block diagram, you use the wiring tool to create wires between VIs and functions. In the Statechart Editor window, you use the wiring tool to create transitions between states and other objects .
- The LabVIEW block diagram provides options for debugging VIs. The Statechart Editor window does not provide any debugging options. You debug statecharts by using a separate window that you can access while the statechart is running.
- The Statechart Editor window disables many LabVIEW pull-down menu items that do not apply to statecharts.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_entryexit.html language=enus -->
## TOPIC 00060: Entry and Exit Actions (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_entryexit.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_entryexit.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Entry and Exit Actions (Statechart Module)

An entry action is LabVIEW code that a statechart executes upon entering a particular [state](../lvsc/sc_state.html), that is, after completing a [transition](sc_c_trans.html) from another state. An exit action is LabVIEW code that the statechart executes upon exiting a state, that is, before completing a transition to another state. You [define entry and exit actions](../lvschowto/sc_h_configstate.html) by right-clicking a state border and selecting **Configure State**, which launches the [Configure State](../lvsc/sc_configstate_db.html) dialog box. You then write LabVIEW block diagram code to define the actions.

Each state can have only one entry action and one exit action. These actions are optional, but if you define one, the action executes every time the statechart enters or exits that state. This behavior means you cannot define a [trigger](sc_c_tga.html#trigger) or a [guard](sc_c_tga.html#guard) for an entry or exit action.

To specify state actions that execute conditionally, use [static reactions](sc_c_staticrxn.html).

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_gendoc.html language=enus -->
## TOPIC 00061: Generating Documentation for Statecharts (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_gendoc.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_gendoc.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Generating Documentation for Statecharts (Statechart Module)

You can [generate documentation](../lvschowto/sc_h_gendoc.html) that describes all components of a completed statechart. Print or save statechart documentation to keep a record you can refer to later.

You can generate statechart documentation from either the [Project Explorer](/csh?topicname=lvconcepts/using_labview_projects.html) window or the [Statechart Editor](../lvscconcepts/sc_c_editor.html) window. In the **Project Explorer** window, right-click the .lvsc item, or statechart library, for a statechart and select **Generate Documentation** from the shortcut menu. In the **Statechart Editor** window, select **File»Generate Documentation**. The LabVIEW Statechart Module generates an [XML file](../lvscconcepts/sc_c_gendocfile.html) that contains information about all components, including [states](../lvsc/sc_state.html), [pseudostates](../lvscconcepts/sc_c_pseudocon.html), [connectors](../lvscconcepts/sc_c_pseudocon.html), [regions](../lvsc/sc_region.html), and [transitions](../lvscconcepts/sc_c_trans.html), of the statechart. You can view the XML file in a Web browser.

The Statechart Module also generates a folder of support files in the same location as the XML file you generate. This support folder contains files that the XML file references, including images of the statechart components, an Extensible Stylesheet Language Transformations (XSLT) file, and an XML Schema Definition (XSD) file. An XSLT file determines the appearance of an XML document and can transform the document into another format, such as HTML. An XSD file defines the elements and attributes of the XML file. You can use the NI_Statechart_Documentation_Tool.xslt file in the support folder to personalize the appearance of the XML file you generate. Do not modify the NI_Statechart_Documentation_Tool.xsd file.

|  | Note You may freely distribute your generated XML file and support folder containing the XSLT and XSD files. However, National Instruments claims all copyrights on NI_Statechart_Documentation_Tool.xslt and NI_Statechart_Documentation_Tool.xsd. Do not use or distribute these files except with the associated XML file and support folder generated by the LabVIEW Statechart Module Generate Documentation feature. You may modify NI_Statechart_Documentation_Tool.xslt, but the file must retain the National Instruments copyright notice contained therein, which may not be modified or obscured. You also must add a prominent notice at the top of the file that states that you have modified the file. You may not modify NI_Statechart_Documentation_Tool.xsd. |
| --- | --- |

You also can use the [Generate Documentation](/csh?topicname=lvprop/statechartlibrary_generate_documentation.html) method to generate statechart documentation programmatically.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_gendocfile.html language=enus -->
## TOPIC 00062: Statechart Documentation Structure (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_gendocfile.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_gendocfile.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Documentation Structure (Statechart Module)

Statechart documentation you [generate](../lvschowto/sc_h_gendoc.html) can vary in appearance depending on the components of the statechart and any modifications you make to the NI_Statechart_Documentation_Tool.xslt file. In general, information in the documentation XML file appears in order of the location of each statechart component. For example, the file begins with information about the statechart components that occupy the top level of the statechart diagram. The XML file then lists any components of the statechart that the top-level components contain, as well as sub-components of those components, until the file lists all of the components of the statechart diagram.

The generated XML file presents the following information about the statechart:

- Statechart Description —Displays a description of the statechart. This description corresponds to the Description field of the Documentation page of the Project Library Properties dialog box for the statechart. The text in this field also appears in the Context Help window when you move the cursor over the statechart in the Project Explorer window.
- Statechart Type Definitions —Displays the input, output, and state data of the statechart corresponding to the Inputs.ctl , Outputs.ctl , and StateData.ctl type definitions.
- Trigger List —Lists all triggers in the statechart and the group(s) to which they belong. When you configure a transition or static reaction to react to a group, any trigger in that group can initiate the associated transition or static reaction. 
 The Trigger List adheres to the following structure: ALL
List of all triggers in the statechart
Name of Group 1
List of triggers and groups in Group 1
Name of Group *N*
List of triggers and groups in Group *N*
- Code Generation Properties —Displays the code generation settings for the statechart. This information corresponds to the options on the Statechart Code Generation page of the VI Properties dialog box.
  - Execution Target —Displays the target on which the statechart executes.
  - Usage —Indicates whether the statechart is synchronous or asynchronous . If the statechart executes on an FPGA target, Usage indicates whether the statechart runs in a single-cycle Timed Loop application or if the statechart runs in an internal loop.
  - Queue Settings —(Asynchronous statecharts only) Displays the following information relating to the trigger queue type of the statechart.
    - Type —Displays the type of trigger queue the statechart uses.
      - LV Queue —Indicates that the external queue is a LabVIEW queue.
      - RT FIFO — (Real-Time Module) Indicates that the external queue is an RT FIFO.
    - Size —Displays the maximum number of triggers in the queue that the statechart allows.
    - Enqueue timeout in ms —(RT FIFO only) Displays the amount of time, in milliseconds, LabVIEW waits for an open slot in the queue before either overwriting the trigger or discarding the incoming trigger.
    - Enqueue overwrite on timeout —(RT FIFO only) Indicates whether LabVIEW overwrites the oldest value in the RT FIFO if the RT FIFO does not have an available slot.
    - Read mode —(RT FIFO only) Displays the read behavior of the RT FIFO.
      - Polling —Indicates whether LabVIEW continually polls the RT FIFO for new data or an open slot.
      - Blocking —Indicates whether the thread of the statechart does not poll the RT FIFO while the statechart waits, thus allowing other tasks in the system to execute.
    - Write mode —(RT FIFO only) Displays the write behavior of the RT FIFO.
      - Polling —Indicates whether LabVIEW continually polls the RT FIFO for new data or an open slot.
      - Blocking —Indicates whether the thread of the statechart does not poll the RT FIFO while the statechart waits, thus allowing other tasks in the system to execute.
  - Internal trigger queue size —Displays the maximum number of triggers in the internal trigger queue that the statechart allows.
  - Debugging —Indicates whether debugging is Enabled or Disabled for the statechart.
  - Reset output values after each iteration —Displays TRUE if the statechart resets the values of the Outputs.ctl type definition after every iteration of the statechart. Displays FALSE if the statechart caches output values between iterations.
  - Guard or Action VI reentrancy —Displays how the statechart handles the reentrancy of the guards and actions of this statechart. This option is not valid if you specify Enabled in the Debugging pull-down menu of the Statechart Code Generation page of the Project Library Properties dialog box.
    - Preallocate clone for each instance —Indicates whether LabVIEW allocates clones of the reentrant guard or action code for every call to the reentrant code.
    - Share clones between instances —Indicates whether LabVIEW allocates clones of the reentrant guard or action code on-demand for each call to the reentrant code.
- Statechart Diagram —Describes the properties of the pseudostates, connectors, states, transitions, and regions of the statechart. If any of the components on the statechart diagram do not have a label, LabVIEW assigns generic names to the components in the XML file. For example, if a transition does not have a label, LabVIEW assigns the name Transition to the transition.
  - Main Diagram —Displays an image of the statechart diagram and lists the pseudostates, connectors, states, and transitions that the main region contains.
    - Image —Displays an image of the entire statechart diagram.
    - Contained Objects —Lists the pseudostates, connectors, and states that the main region contains.
    - Contained Transitions —Lists the transitions that the main region contains.
  - Pseudostates and Connectors —Displays the following information about each pseudostate or connector in the statechart.
    - Image —Displays an image of the pseudostate or connector.
    - Description —Displays a description of the pseudostate or connector. This description corresponds to the Description field of the Description and Tip dialog box for the pseudostate or connector.
    - Source —Lists the statechart object from which each transition into the current pseudostate or connector begins. Source also lists the transitions into the current pseudostate or connector. The –> symbol indicates the sequence in which a statechart moves between states and pseudostates/connectors through transitions. For example, State 1 –> Transition 1 indicates that the statechart moves from State 1 to the current pseudostate or connector through Transition 1.
    - Destination —Lists the transitions from the current pseudostate or connector. Destination also lists the statechart object to which each transition leads. The –> symbol indicates the sequence in which a statechart moves between states and pseudostates/connectors through transitions. For example, Transition 1 –> State 1 indicates that the statechart moves from the current pseudostate or connector to State 1 through Transition 1.
    - Containing Region —Lists the region that contains the pseudostate or connector.
  - States —Displays the following information about each state in the statechart.
    - Image —Displays an image of the state.
    - Description —Displays a description of the state. This description corresponds to the Description field of the Description and Tip dialog box for the state.
    - Source —Lists the statechart object from which each transition into the current state begins. Source also lists the transitions into the current state. The –> symbol indicates the sequence in which a statechart moves between states and pseudostates/connectors through transitions.
    - Destination —Lists the transitions from the current state or connector. Destination also lists the statechart object to which each transition leads. The –> symbol indicates the sequence in which a statechart moves between states and pseudostates/connectors through transitions.
    - Containing Region —Lists the region that contains the state.
    - Contained Regions —Lists the region(s) that the state contains.
    - Contained Objects —Lists any Fork or Join connectors that the state contains.
    - Subdiagram —Displays an image of the state if the state appears as a subdiagram .
    - Entry Action —Displays the following information about the entry action of the state.
      - Description —Displays a description of the entry action. This description corresponds to the Description field on the Properties page of the Configure State dialog box.
      - Action —Displays information about the action code for the state.
        - Code —Displays the block diagram of the action code.
        - Disable —Indicates, when TRUE, that LabVIEW nullifies the action code on this block diagram and the action does nothing. This information corresponds to the Disable? checkbox on the Action page of the Configure State dialog box.
        - AutoPreAllocate —Indicates, when TRUE, that LabVIEW optimizes array and string operations in the action code for this reaction by preallocating memory at compile time rather than dynamically allocating memory at run time. This information is only available when editing a statechart that you configure to run on an FPGA target in the Statechart Code Generation page of the Project Library Properties dialog box.
    - Exit Action —Displays the following information about the exit action of the state.
      - Description —Displays a description of the exit action. This description corresponds to the Description field on the Properties page of the Configure State dialog box.
      - Action —Displays information about the action code for the state.
        - Code —Displays the block diagram of the action code.
        - Disable —Indicates, when TRUE, that LabVIEW nullifies the action code on this block diagram and the action does nothing. This information corresponds to the Disable? checkbox on the Action page of the Configure State dialog box.
        - AutoPreAllocate —Indicates, when TRUE, that LabVIEW optimizes array and string operations in the action code for this reaction by preallocating memory at compile time rather than dynamically allocating memory at run time. This information is only available when editing a statechart that you configure to run on an FPGA target in the Statechart Code Generation page of the Project Library Properties dialog box.
    - Static Rxn —Displays the following information about the static reaction of the state.
      - Description —Displays a description of the static reaction. This description corresponds to the Description field on the Properties page of the Configure State dialog box.
      - Trigger List —Lists all triggers and groups to which the static reaction responds.
      - Guard —Displays the block diagram of the guard code for the state. Also displays if the guard code is disabled, and how LabVIEW preallocates memory when running the guard code.
        - Code —Displays the block diagram of the guard code.
        - Disable —Indicates, when TRUE, that LabVIEW nullifies the guard code on this block diagram and the guard always evaluates to TRUE. This information corresponds to the Disable? checkbox on the Guard page of the Configure State dialog box.
        - AutoPreAllocate —Indicates, when TRUE, that LabVIEW optimizes array and string operations in the guard code for this reaction by preallocating memory at compile time rather than dynamically allocating memory at run time. This information is only available when editing a statechart that you configure to run on an FPGA target in the Statechart Code Generation page of the Project Library Properties dialog box.
      - Action —Displays the block diagram of the action code for the state. Also displays if the action code is disabled, and how LabVIEW preallocates memory when running the action code.
        - Code —Displays the block diagram of the action code.
        - Disable —Indicates, when TRUE, that LabVIEW nullifies the action code on this block diagram and the action does nothing. This information corresponds to the Disable? checkbox on the Action page of the Configure State dialog box.
        - AutoPreAllocate —Indicates, when TRUE, that LabVIEW optimizes array and string operations in the action code for this reaction by preallocating memory at compile time rather than dynamically allocating memory at run time. This information is only available when editing a statechart that you configure to run on an FPGA target in the Statechart Code Generation page of the Project Library Properties dialog box.
  - Transitions —Displays the following information about each transition in the statechart.
    - Image —Displays an image of the transition.
    - Description —Displays a description of the transition. This description corresponds to the Description field of the Description and Tip dialog box for the transition.
    - Source —Lists the statechart object from which the current transition begins.
    - Destination —Lists the statechart object to which the current transition leads.
    - Containing Region —Lists the region that contains the transition.
    - Transition Code —Displays the following information about the guard and action code of the transition.
      - Description —Displays a description of the transition code. This description corresponds to the Description field of the Properties page of the Configure Transition dialog box.
      - Trigger List —Lists all triggers and groups to which the transition reacts.
      - Guard —Displays the block diagram of the guard code for the transition. Also displays if the guard code is disabled, and how LabVIEW preallocates memory when running the guard code.
        - Code —Displays the block diagram of the guard code.
        - Disable —Indicates, when TRUE, that LabVIEW nullifies the guard code on this block diagram and the guard always evaluates to TRUE. This information corresponds to the Disable? checkbox on the Guard page of the Configure Transition dialog box.
        - AutoPreAllocate —Indicates, when TRUE, that LabVIEW optimizes array and string operations in the guard code for this reaction by preallocating memory at compile time rather than dynamically allocating memory at run time. This information is only available when editing a statechart that you configure to run on an FPGA target in the Statechart Code Generation page of the Project Library Properties dialog box.
      - Action —Displays the block diagram of the action code for the transition. Also displays if the action code is disabled, and how LabVIEW preallocates memory when running the action code.
        - Code —Displays the block diagram of the action code.
        - Disable —Indicates, when TRUE, that LabVIEW nullifies the action code on this block diagram and the action does nothing. This information corresponds to the Disable? checkbox on the Action page of the Configure Transition dialog box.
        - AutoPreAllocate —Indicates, when TRUE, that LabVIEW optimizes array and string operations in the action code for this reaction by preallocating memory at compile time rather than dynamically allocating memory at run time. This information is only available when editing a statechart that you configure to run on an FPGA target in the Statechart Code Generation page of the Project Library Properties dialog box.
  - Regions —Displays the following information about each region in the statechart.
    - Image —Displays an image of the region.
    - Description —Displays a description of the region. This description corresponds to the Description field of the Description and Tip dialog box for the region.
    - Containing State —Lists the state that contains the region.
    - Contained Objects —Lists the pseudostates, connectors, and states that the region contains.
    - Contained Transitions —Lists the transitions that the region contains.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_hierarchy.html language=enus -->
## TOPIC 00063: Substates and Superstates (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_hierarchy.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_hierarchy.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Substates and Superstates (Statechart Module)

You can use [regions](../lvsc/sc_region.html) to place [states](../lvsc/sc_state.html) within states. In this situation, the state that contains the region is called a superstate. The states inside the region are called substates. For example, the following figure shows a superstate and substates.

[IMAGE alt='image' src='subsuper.gif']

In the previous figure, the [Initial](../lvsc/sc_initial.html)
 [pseudostate](sc_c_pseudocon.html) specifies that the statechart enters State 2 immediately after entering State 1.

|  | Note While the statechart is in a substate, the statechart can take any transition, or execute any static reaction, associated with the enclosing superstate. Transitions and static reactions of the superstate have higher priority than transitions and static reactions of a substate. |
| --- | --- |

You can bypass this initial state by creating transitions to and from substates directly. The following figure shows this situation:

[IMAGE alt='image' src='subsuper2.gif']

In the previous figure, the statechart follows the same initial behavior, which means that the statechart enters State 2 first. However, State 2 now has a transition (1) to State 4. Similarly, State 3 has a transition (2) to State 6. If the statechart takes transition 1 and enters State 4, the Initial pseudostate in Region 2 specifies that the statechart enters State 5. However, if the statechart takes transition 2, the statechart bypasses State 5 and enters State 6.

|  | Note You can place regions inside substates and substates inside these regions. In this situation, a substate becomes a superstate. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_iconstyles.html language=enus -->
## TOPIC 00064: Changing Function Icon Styles (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_iconstyles.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_iconstyles.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Changing Function Icon Styles (Statechart Module)

You can change the icon style of a [Statechart Communication](../lvsc/sc_comm.html) function on the block diagram. Right-click a Statechart Communication function and select **Icon Style** from the shortcut menu to display the following options:

- Custom Icon —Displays the Statechart Communication function with the custom icon of the statechart diagram.
- Configuration —Displays the Statechart Communication function with a list of configuration information, such as the linked statechart, the triggers to send, or the state to check.
 [IMAGE alt='image' src='note.gif']
**Note** For the [IsIn](../lvsc/sc_isin.html) function, you can select **Configuration»State Name** to display the name of the state that the function checks. Select **Configuration»State Path** to display the path to the state that the function checks.

You also can set the default icon style of Statechart Communication functions by using the [Statechart](../lvsc/statechart_options.html) page.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_instances.html language=enus -->
## TOPIC 00065: Calling Multiple Instances of a Statechart (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_instances.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_instances.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Calling Multiple Instances of a Statechart (Statechart Module)

Each [Run Statechart](../lvsc/sc_runsc.html) function represents a separate copy, or instance, of a statechart. Because this function is [reentrant](/csh?topicname=lvconcepts/suggestions_for_exec.html), you can call multiple statechart instances simultaneously. You can call multiple instances of both [asynchronous and synchronous](sc_c_syncasync.html) statecharts.

The following figure shows a single [caller VI](sc_c_callervi.html) that calls two instances of the same asynchronous statechart.

[IMAGE alt='image' src='async_instance.gif']

In the previous figure, notice how the caller VI contains two instances of the Run Statechart function. Each instance has a unique **Instance Name**, which separates the external trigger queues from one another. When you click the **Button** front panel control, the Send External Trigger 1 function sends Trigger1 to Statechart 1 while the Send External Trigger 2 function sends Trigger2 to Statechart 2. Also notice that both instances read the same [input data](sc_c_iodata.html) but write to different output data.

|  | Note This example uses the caller VI to send triggers to an external queue. However, as long as the caller VI is running and the statechart is in memory, you can use any VI to send triggers to an external queue. This behavior means that you can place the Trigger Loop and Statechart Loop in separate VIs. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_intro.html language=enus -->
## TOPIC 00066: Introduction to the LabVIEW Statechart Module (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_intro.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_intro.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Introduction to the LabVIEW Statechart Module (Statechart Module)

Using the LabVIEW Statechart Module involves the following two steps:

1. Using the Statechart Editor window to build a statechart.
2. Creating a VI that executes the statechart. This VI also sends information to, and receives information from, the statechart.

The following sections provide information about these steps.

#### Building a Statechart

Building a statechart involves defining the following items:

- States
- Actions and static reactions these states execute
- Transitions between states
- Actions these transitions execute
- Triggers

When you build a statechart, you define unique states in which the statechart can be. You also define transitions between these states, when the statechart can take these transitions, and what actions these transitions can take. You then [define triggers](../lvschowto/sc_h_createtrig.html) that cause the statechart to begin evaluating a certain transition. For example, consider a statechart that you use to control a chemical process. You can specify that the statechart moves from State 1 to State 2 after receiving the Valve Open trigger. States and transitions also have associated actions, which you use to modify [output and state data](sc_c_iodata.html) associated with the statechart.

#### Creating a VI that Executes the Statechart

After you define the valid triggers and configure the statechart to react to those triggers, you must send those triggers to the statechart. You send triggers to the statechart by creating a VI, known as the [caller VI](sc_c_callervi.html), to [send triggers](../lvschowto/sc_h_callsc.html) at a specific time. For example, you can configure the caller VI to send the Stop trigger after you click the **Stop** front panel button.

The caller VI also sends [input data](sc_c_iodata.html) to the statechart so the statechart can act on that data. The caller VI receives data that the statechart modifies as a result of a state or transition action. You then can use this data in other parts of the caller VI or send this data to other VIs.

The following figure shows how a caller VI interacts with a statechart.

[IMAGE alt='image' src='lv_statechart_trigger.gif']

The previous figure shows how the caller VI sends data to the statechart, which returns output data to the caller VI. If the statechart is asynchronous, the caller VI also might send a trigger to the statechart. Sending a trigger to the statechart causes the statechart to begin executing.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_iodata.html language=enus -->
## TOPIC 00067: Input, Output, and State Data (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_iodata.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_iodata.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Input, Output, and State Data (Statechart Module)

The LabVIEW Statechart Module uses [type definitions](/csh?topicname=lvconcepts/custom_cont_ind_type.html) to represent data that you use with a statechart. By default, these type definitions contain [clusters](/csh?topicname=lvhowto/clusters.html) and appear as .ctl files in the **Project Explorer** window. When looking at the .lvsc file in the **Project Explorer** window, you see several items, including the following items:

- Inputs.ctl —Data that the statechart can read but not write. You send this data from the caller VI to the statechart by wiring this type definition to the Inputs parameter of the Run Statechart function.
- Outputs.ctl —Data that the statechart can read and write. The Run Statechart function returns output data to the caller VI. Access this data by using the Outputs output of the Run Statechart function. Use the Outputs.ctl typedef to define data types that other VIs need to access.
- StateData.ctl —Data that the statechart can read and write. Items in the StateData.ctl typedef are available to only guards and action . Therefore, the Run Statechart function does not return state data to the caller VI. Use the StateData.ctl typedef to define data types that other VIs do not need to access.

|  | Note If you want to define only a single element for input, output, or state data, you do not need to use a cluster. However, if you want to define two or more elements, you must place these elements in a cluster. |
| --- | --- |

Double-click a .ctl file to [define input, output, and/or state data types](../lvschowto/sc_h_iodata.html) for a statechart. You also can drag the .ctl file to a block diagram to access the contents of that type definition from within a VI.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_iteration.html language=enus -->
## TOPIC 00068: Executing Statechart Iterations (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_iteration.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_iteration.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Executing Statechart Iterations (Statechart Module)

The first iteration of the statechart executes the following two steps:

1. Takes the transition to the state that the top-level Initial 
 pseudostate specifies.
2. Executes any entry action of this first state and any specified substates .

|  | Note During the initial iteration, the statechart ignores incoming triggers. |
| --- | --- |

After completing these steps, the statechart is in the first state. What happens next depends on whether the statechart is [asynchronous or synchronous](sc_c_syncasync.html). Synchronous statecharts begin an iteration according to the [flow of data](/csh?topicname=lvconcepts/block_diagram_data_flow.html) through the [Run Statechart](../lvsc/sc_runsc.html) function. Asynchronous statecharts begin an iteration after receiving a trigger from the [external trigger queue](sc_c_trigqueue.html).

In either situation, the statechart completes the following steps upon receiving a trigger.

1. Reacts to this trigger.
2. Checks the internal trigger queue .
3. Reacts to any triggers in this queue.
4. Checks the internal trigger queue again.

The iteration finishes after the internal trigger queue is empty. After the iteration finishes, the statechart returns [output data](sc_c_iodata.html) to the caller VI.

|  | Note You can configure a statechart to either reset or cache this output data. |
| --- | --- |

The following figure shows a full iteration of an asynchronous statechart. This iteration is the same for synchronous statecharts except that synchronous statecharts do not receive triggers from an external queue.

[IMAGE alt='image' src='statechart_ex_flow.gif']

The following figures show detailed views of processes A, B, and C in the previous figure. Items 1, 2, and 3 are results of these processes.

[IMAGE alt='image' src='sc_exec_abc.gif']

* The statechart checks outgoing transitions according to the [priority you specify for each transition](../lvschowto/sc_h_transprior.html). Also, this step does not occur for transitions that leave an Initial pseudostate. Statecharts take these initial transitions unconditionally. The statechart checks static reactions according to the order in which you define these reactions.

|  | Note Substates in orthogonal regions execute concurrently during the same iteration. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_orthogonal.html language=enus -->
## TOPIC 00069: Orthogonal Regions and Concurrency (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_orthogonal.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_orthogonal.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Orthogonal Regions and Concurrency (Statechart Module)

When a [superstate](sc_c_hierarchy.html) contains two or more [regions](../lvsc/sc_region.html), those regions are called orthogonal regions. For example, in the following figure, Region 1 and Region 2 are orthogonal.

[IMAGE alt='image' src='orthogonal.gif']

[Substates](sc_c_hierarchy.html) in orthogonal regions are concurrent, which means that while the superstate is active, the statechart can be in exactly one substate from each orthogonal region during each statechart [iteration](sc_c_iteration.html). For example, in the previous figure, the statechart can be in State 3 and State 5 concurrently. Substates that exist within the same region, such as State 2 and State 3 in the previous figure, cannot be active concurrently.

|  | Note Some textbooks refer to orthogonal regions as AND-states. |
| --- | --- |

Concurrency is different from parallelism. Concurrent substates take turns being active during each statechart [iteration](sc_c_iteration.html), whereas parallel substates are active simultaneously. The LabVIEW Statechart Module does not support parallel state activity.

The statechart enters orthogonal regions in descending alphabetical order of the region name. For example, in the previous figure, the statechart enters Region 1 before entering Region 2. Double-click the name of a region to change the name.

|  | Tip Try to avoid situations in which the actions of a substate depend on the results of a concurrent substate. This configuration might result in unexpected behavior or invalid data. |
| --- | --- |

You can create one transition [to](../lvschowto/sc_h_tfork.html) and [from](../lvschowto/sc_h_join.html) multiple substates in orthogonal regions.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_pseudocon.html language=enus -->
## TOPIC 00070: Pseudostates and Connectors (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_pseudocon.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_pseudocon.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Pseudostates and Connectors (Statechart Module)

Except for the [State](../lvsc/sc_state.html), [Region](../lvsc/sc_region.html), and [Port](../lvsc/sc_port.html), the LabVIEW Statechart Module categorizes the [Statechart Development](../lvsc/sc_obj.html) objects as either pseudostates or connectors. A pseudostate is a statechart object that represents a state. The Statechart Module includes the following pseudostates:

- Initial —Represents the first state that a region enters.
- Terminal —Represents a state that can terminate a region.
- Shallow History —Represents the highest-level substate in a region the statechart has entered previously.
- Deep History —Represents the lowest-level substate in a region the statechart has entered previously.

A connector is a statechart object that connects multiple [transition](sc_c_trans.html) segments together. The Statechart Module includes the following connectors:

- Fork —Splits one transition segment into multiple segments.
- Join —Merges multiple transition segments into one segment.
- Junction —Connects multiple transition segments together.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_related.html language=enus -->
## TOPIC 00071: Related Documentation (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_related.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_related.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Related Documentation (Statechart Module)

The following documents contain information that you might find helpful as you use the Statechart Module.

- LabVIEW Statechart Module Readme —Open this file by navigating to the labview\readme\ directory and opening readme_Statechart.html .
- LabVIEW Statechart Module Example VIs—Refer to the labview\examples\Statechart\ directory for example VIs that demonstrate common tasks and concepts using the LabVIEW Statechart Module. You also can access these VIs by selecting Help»Find Examples and selecting Toolkits and Modules»Statechart in the NI Example Finder window.
- Additional LabVIEW documentation .

The following resources contain information about concepts related to the Statechart Module.

|  | Note The following resources offer useful background information on the general concepts discussed in this documentation. These resources are provided for general informational purposes only and are not affiliated, sponsored, or endorsed by National Instruments. The content of these resources is not a representation of, may not correspond to, and does not imply current or future functionality in the Statechart Module or any other National Instruments product. |
| --- | --- |

- Douglass, Bruce Powel. 2000. Real-time UML: Developing efficient objects for embedded systems. 2d ed. Upper Saddle River, NJ: Pearson Education.
- Harel, David. 1987. Statecharts: A visual formalism for complex systems. Science of computer programming 8, no. 3:231–74.

Refer to the National Instruments Product Manuals Library for updated documentation resources.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_staticrxn.html language=enus -->
## TOPIC 00072: Static Reactions (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_staticrxn.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_staticrxn.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Static Reactions (Statechart Module)

Static reactions define the behavior of a [state](../lvsc/sc_state.html) while that state is not taking any outgoing [transitions](sc_c_trans.html). Static reactions execute only if both of the following conditions are met:

- The statechart receives the trigger to which you configured the reaction to respond.
- The guard associated with that reaction evaluates to TRUE. If a static reaction does not have a guard, that guard evaluates to TRUE always.

One state can have multiple static reactions. The statechart can execute multiple static reactions during one [iteration](sc_c_iteration.html) of the statechart.

You [configure static reactions](../lvschowto/sc_h_configstate.html) by right-clicking a state border and selecting **Configure State** to launch the [Configure State](../lvsc/sc_configstate_db.html) dialog box.

|  | Note If you define multiple static reactions that react to the same trigger, the statechart executes those static reactions one after the other. The order of execution is the order in which you defined the reactions. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_subsc.html language=enus -->
## TOPIC 00073: Subdiagrams (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_subsc.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_subsc.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Subdiagrams (Statechart Module)

By default, the LabVIEW Statechart Module displays the [hierarchy](sc_c_hierarchy.html) of a [state](../lvsc/sc_state.html) directly on the statechart diagram. However, because states can contain numerous [regions](../lvsc/sc_region.html), a complex state can make visual navigation difficult. In this situation, you can [view a state as a subdiagram](../lvschowto/sc_h_subdiag.html) to simplify the visual appearance of the statechart diagram.

LabVIEW displays the contents of subdiagrams in a separate [Statechart Editor](sc_c_editor.html) window. This separation provides more space in which you can edit the contents of a state. This separation also provides a way to save space on the top-level statechart diagram.

For example, the following figure shows a statechart with two top-level states, State 1 and State 2.

[IMAGE alt='image' src='subdiagram1.gif']

Viewing State 2 as a subdiagram and then resizing State 2 results in the following statechart diagram.

[IMAGE alt='image' src='subdiagram2.gif']

In the above figure, notice that State 2 lacks an inner border. This change provides a visual distinction you can use to identify subdiagrams on a statechart diagram. Also notice how using a subdiagram saves space on the top-level statechart diagram.

The following figure shows the subdiagram itself.

[IMAGE alt='image' src='subdiagram3.gif']

In the above figure, notice that the subdiagram contents are identical to how this state appeared previously on the statechart diagram. Also notice the blue background that distinguishes the subdiagram from a top-level statechart diagram, which has a white background.

|  | Note You can view states in subdiagrams as subdiagrams themselves. For example, in the previous figure, you can view State 5 as a subdiagram. |
| --- | --- |

In the above figure, the rectangular and triangular objects to the left of the Region are [ports](../lvsc/sc_port.html). Notice how these ports correspond to [transitions](sc_c_trans.html) that enter and exit State 2.

You can place outgoing ports on a subdiagram by placing a [Port](../lvsc/sc_port.html) object, located on the [Statechart Development](../lvsc/sc_obj.html) palette, on the subdiagram. That port then appears on the top-level statechart diagram. To match ports between the statechart diagram and the subdiagram, right-click the port and select either **Find Port on State** or **Find Port on Subdiagram**, depending on whether you are viewing the statechart diagram or the subdiagram.

While viewing a subdiagram, you can change the appearance of a port by right-clicking the port and selecting either **Rotate** or **Reverse**.

|  | Note You cannot create incoming ports by placing a port object on a subdiagram. You create incoming ports only by creating a transition to the state. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_syncasync.html language=enus -->
## TOPIC 00074: Synchronous and Asynchronous Statecharts (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_syncasync.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_syncasync.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Synchronous and Asynchronous Statecharts (Statechart Module)

You can use the LabVIEW Statechart Module to build two types of statecharts: synchronous and asynchronous. The type you choose to build affects the configuration of the [Run Statechart](../lvsc/sc_runsc.html) function when you [generate code for the statechart](../lvschowto/sc_h_gencode.html). National Instruments recommends that you decide on the type of statechart you want to use before building the statechart. While you can convert between asynchronous and synchronous statecharts, the two types handle data in different manners. If you change the type of statechart after building the statechart, you need to restructure the way in which other VIs send data to the statechart.

The type of statechart you build depends on when you want the statechart to perform an [iteration](sc_c_iteration.html). Synchronous statecharts execute one iteration at the moment the [Run Statechart](../lvsc/sc_runsc.html) function receives all [input data](sc_c_iodata.html). Asynchronous statecharts execute one iteration once the Run Statechart function receives all input data and a [trigger](sc_c_tga.html#trigger) is present on the [external trigger queue](../lvscconcepts/sc_c_trigqueue.html). If the Run Statechart function receives all input data and a trigger is not present on the external trigger queue, the function does not execute until a trigger is present. The Run Statechart function specifies that the thread that executes the statechart sleeps until a trigger is present on the external trigger queue.

|  | Note Synchronous statecharts begin an iteration according to the flow of data through the block diagram of the caller VI. Asynchronous statecharts begin an iteration according to the flow of data through the block diagram of the caller VI and the presence of a trigger on the external trigger queue. |
| --- | --- |

#### A Synchronous Example

For example, consider a statechart that implements logic similar to a programmable logic controller (PLC). This statechart might read input data, execute an action, and then return output data, all within 10 milliseconds. A synchronous statechart is suitable for this example because the statechart executes at defined time intervals, that is, the statechart does not rely on a trigger to execute.

If the synchronous statechart must execute at defined time intervals, consider placing the statechart in a [timed structure](/csh?topicname=glang/timed_loop_vis_and_func.html). For example, you can place a statechart in a [Timed Loop](/csh?topicname=glang/timed_loop.html) in the [caller VI](sc_c_callervi.html). Timed Loops execute at intervals that you define. If you install the LabVIEW Control Design and Simulation Module, you can place the statechart in a Simulation Loop. Refer to the National Instruments Web site for information about this module.

#### An Asynchronous Example

For another example, consider a National Instruments DAQ device that monitors the temperature of a car engine. If the temperature rises above a certain threshold, the VI that reads from the DAQ device sends a trigger to the statechart, which then performs some action. An asynchronous statechart is suitable for this example because the statechart executes only after receiving a trigger, that is, the statechart does not execute at defined time intervals.

Because asynchronous statecharts do not execute at defined time intervals, you typically place these statecharts in a [While Loop](/csh?topicname=glang/while_loop.html) in the caller VI. You can place the code that sends triggers in a parallel While Loop or in another VI.

You specify the type of statechart by using the [Statechart Code Generation](../lvsc/sc_codegen.html) page of the [Project Library Properties](/csh?topicname=lvdialog/library_props_db.html) dialog box.

#### Sending Data to Statecharts

Whereas asynchronous statecharts react to triggers, synchronous statecharts typically react to [input data](sc_c_iodata.html) only. This difference is important when you create [transitions](sc_c_trans.html) and [static reactions](sc_c_staticrxn.html) for a statechart. When you create these items for an asynchronous statechart, you specify a trigger that causes the statechart to begin taking the transition or executing the static reaction. However, when you create these items for a synchronous statechart, you typically use a [guard](sc_c_tga.html#guard) that takes into account input data only.

Consider the DAQ and PLC examples again. The DAQ example uses a trigger to tell the statechart when to react. The PLC example does not need a trigger because the PLC executes at defined time intervals. The only data the PLC needs is the input data. Therefore, the transitions and static reactions in this statechart do not have triggers. Instead, the guards in these transitions and reactions return TRUE or FALSE depending on some logic that is based on the input data.

|  | Note You also can use guards with asynchronous statecharts. |
| --- | --- |

#### Calling Statecharts

Another difference between synchronous and asynchronous statecharts is the number of VIs that can send triggers to the statechart. Only one VI, the caller VI, can send triggers to synchronous statecharts. Conversely, multiple parallel VIs, which might include the caller VI, can send triggers to an asynchronous statechart. This parallelism is possible because asynchronous statecharts provide an [external queue](sc_c_trigqueue.html) in which the statechart stores incoming triggers.

Any VI can send a trigger to this queue at any time. If a VI sends a trigger while the statechart is waiting for a trigger, the statechart reacts to that trigger. If a VI sends a trigger while the statechart is executing, LabVIEW stores that trigger in the external queue. For example, consider the DAQ statechart again. This statechart can receive triggers from multiple DAQ devices. The statechart stores these triggers in the external queue and reacts to these triggers one at a time.

|  | Note Synchronous statecharts do not have external queues. |
| --- | --- |

By default, all VIs that send triggers to an asynchronous statechart must be running on the same execution target. However, you can use a [network-published shared variable](/csh?topicname=lvconcepts/project_variables.html) to send triggers between these VIs and statecharts running on distributed execution targets.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_targets.html language=enus -->
## TOPIC 00075: Executing Statecharts on Supported Targets (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_targets.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_targets.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Executing Statecharts on Supported Targets (Statechart Module)

You can use the LabVIEW Statechart Module to execute a statechart on many different types of targets. The following table shows the supported target types and any additional software you must install to execute a statechart on that type of target.

| Type of Target | Additional Required Software |
| --- | --- |
| A computer running Windows | — |
| A National Instruments FPGA target, such as an NI Reconfigurable I/O (NI-RIO) device or CompactRIO controller | LabVIEW FPGA Module NI-RIO driver software |
| An NI Real-Time (RT) target, such as a PXI controller, Compact FieldPoint, or Compact Vision System | LabVIEW Real-Time Module Driver software for any hardware devices |
| A target that runs Windows Mobile | LabVIEW Mobile Module |
| An embedded target, such as the MCB2400 target | LabVIEW Embedded Module for ARM Microcontrollers |
| A Touch Panel target that runs Windows XP Embedded or Windows CE | LabVIEW Touch Panel Module |

|  | Note Refer to the National Instruments Web site for information about the National Instruments products this table mentions. |
| --- | --- |

You specify the execution target for the statechart by using the [Statechart Code Generation](../lvsc/sc_codegen.html) page of the [Project Library Properties](/csh?topicname=lvdialog/library_props_db.html) dialog box.

When generating code for a different target, you do not need to modify the [guard](sc_c_tga.html#guard) or [action](sc_c_tga.html#action) logic of the statechart. This logic is cross-platform as long as the target supports the [data types](sc_c_iodata.html) you use.

For [asynchronous](sc_c_syncasync.html) statecharts that execute on an RT target, you must use an RT FIFO for the [external trigger queue](sc_c_trigqueue.html). You can specify this and other options by using the **Statechart Code Generation** page.

#### Deploying Statecharts

You deploy statecharts to targets by using the [Project Explorer](/csh?topicname=lvconcepts/using_labview_projects.html) window. In this window, you must add the [caller VI](sc_c_callervi.html) to the target on which you want to run the statechart. However, National Instruments recommends that you add both the caller VI and the statechart .lvsc file to the target.

#### Considerations for FPGA Targets

Before building a statechart that runs on an FPGA target, you must decide whether the statechart runs in a single-cycle loop application. Then, configure the statechart appropriately by using the **Statechart Code Generation** page. This dialog box contains a **Usage** pull-down menu that you use to specify whether the statechart runs in a single-cycle loop or regular [While Loop](/csh?topicname=glang/while_loop.html). Then, [generate code for the statechart](../lvschowto/sc_h_gencode.html).

|  | Note If you configure a statechart to run single-cycle loop application, the statechart does not have an internal trigger queue. Therefore, you cannot send triggers to this queue. |
| --- | --- |

If you configure a statechart for a single-cycle loop application but place that statechart in a While Loop, the statechart does not behave like a single-cycle application.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_tga.html language=enus -->
## TOPIC 00076: Triggers, Guards, and Actions (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_tga.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_tga.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Triggers, Guards, and Actions (Statechart Module)

[Transitions](sc_c_trans.html) and [static reactions](sc_c_staticrxn.html) rely upon triggers, guards, and actions. These three elements form a logic structure that the statechart uses to determine whether to take a transition or execute a static reaction. The following sections provide more information about these elements.

#### Triggers

A trigger is something to which a statechart reacts. For example, a trigger can be a button press or a value change that happens in a [caller VI](sc_c_callervi.html). When you [configure a transition or static reaction](../lvschowto/sc_h_configt.html), you specify which trigger(s) cause the statechart to begin evaluating that transition or static reaction. Statecharts can react only to triggers that are defined for the current active state or [superstate](sc_c_hierarchy.html).

For example, consider a DVD player. When you press the Play button on a DVD player, the movie begins playing. When you press the Pause button, the movie pauses. The DVD player does not know when you are going to press a particular button, that is, the DVD player only can react to the button you press.

This behavior describes an [asynchronous statechart](sc_c_syncasync.html) that executes an action only after receiving a trigger. You typically use triggers with asynchronous statecharts, although you can [use triggers with synchronous statecharts](#null) also.

|  | Note You may specify a trigger for every transition and static reaction except in the following situations: entry actions, exit actions, and transitions that leave an Initial pseudostate, because these situations react to any triggers received. |
| --- | --- |

Statecharts can receive triggers from a VI or from the statechart itself. In either situation, you must [define the triggers to which a statechart can react](../lvschowto/sc_h_createtrig.html). Asynchronous statecharts store incoming triggers in a [trigger queue](sc_c_trigqueue.html).

|  | Note Statecharts evaluate transitions before static reactions. Therefore, if you configure a static reaction and a transition to react to the same trigger, the statechart evaluates the transition first. |
| --- | --- |

You can [combine triggers into groups](../lvschowto/sc_h_createtrig.html#creategroups). When you configure a transition or static reaction to react to a group, any trigger in that group can initiate the associated transition or static reaction.

After receiving a valid trigger, the statechart then evaluates the [guard](#guard) associated with that reaction or transition. A valid trigger is one that you have created and specified for the transition or static reaction.

##### NULL Triggers

The NULL trigger is the default trigger to which a transition or static reaction reacts in synchronous statecharts. During each iteration of a synchronous statechart, the statechart evaluates NULL transitions and static reactions for the current state. By default, synchronous [Run Statechart](../lvsc/sc_runsc.html) functions send the NULL trigger to the statechart at every iteration of the statechart.

|  | Note You can override this behavior by wiring a trigger value to the Trigger input of the Run Statechart function. You then also must configure the transition or static reaction to react to this trigger. |
| --- | --- |

The [Send External Trigger](../lvsc/sc_send_event.html) and [Send Internal Trigger](../lvsc/sc_send_signal.html) functions, however, require you to provide a trigger. You can configure the Send External Trigger and Send Internal Trigger functions to send the NULL trigger or another trigger of your choosing to the statechart. The Send External Trigger function only provides triggers to [asynchronous statecharts](../lvschowto/sc_h_callsc.html#async).

You must configure transitions and static reactions to respond to any triggers other than the NULL trigger.

If a transition responds to the NULL trigger and the statechart sends the NULL trigger during every iteration of the statechart, the guard is the primary factor in determining whether the statechart takes a transition.

#### Guards

A guard is LabVIEW block diagram code that the statechart evaluates to determine if the transition or static reaction is valid. After receiving a trigger for a transition or static reaction, the statechart evaluates the guard code. This code, which must return either TRUE or FALSE, determines whether the statechart takes the transition or executes the static reaction. By combining a guard with triggers, you can be more specific about the conditions under which a statechart takes transitions and executes static reactions.

After receiving a specified trigger, the statechart evaluates the guard code. If the guard code returns TRUE, the statechart proceeds with the transition or static reaction. If the guard code returns FALSE, the statechart does not proceed with the transition or static reaction. In this situation, the statechart remains in the [state](../lvsc/sc_state.html) that initiated the transition or static reaction. The statechart then can evaluate other transitions and/or static reactions for that state.

|  | Note Statecharts evaluate transitions according to the priority you specify. |
| --- | --- |

For example, a guard can return TRUE if five or more minutes have elapsed since the statechart began executing. This TRUE value means the statechart takes the transition and enters the next state. Otherwise, the guard returns FALSE. This FALSE value prevents the statechart from taking the transition, and the statechart remains in the same state.

|  | Note Defining a guard is optional. Not defining a guard is equivalent to specifying that the guard returns TRUE always. |
| --- | --- |

If you add code to a previously empty guard or if you delete all code from a guard, you must re-generate code for the statechart. Click the **Generate Code** button [IMAGE alt='image' src='sc_gencode.gif'] to generate code that corresponds to the statechart. If you modify an existing, non-empty guard, you do not need to re-generate code for the statechart.

#### Actions

An action is LabVIEW block diagram code that modifies [output or state data](sc_c_iodata.html) and/or [sends a trigger to the internal queue](../lvschowto/sc_h_sendsignal.html). The statechart executes actions at different times depending on whether that action is associated with a transition or a static reaction. The statechart executes actions in the following situations:

- When taking a transition —After completing the state exit action but before completing the entry action of the next state. Because the transition does not exit a state unless the guard code returns TRUE, the action does not execute unless the guard returns TRUE.
- When executing a static reaction —After the guard code returns TRUE.

If the guard code returns FALSE in either situation, the statechart does not execute the action. Defining an action is optional.

|  | Note In addition to defining actions for transitions and static reactions, you can define entry and exit actions of a state. |
| --- | --- |

If you add code to a previously empty action or if you delete all code from an action, you must re-generate code for the statechart. Click the **Generate Code** button [IMAGE alt='image' src='sc_gencode.gif'] to generate code that corresponds to the statechart. If you modify an existing, non-empty action, you do not need to re-generate code for the statechart.

#### Combining Triggers, a Guard, and an Action

You [configure a transition or static reaction](../lvschowto/sc_h_configt.html) by combining one or more triggers, a guard, and an action into a logical sequence. For example, consider the following statement:

While in State 1: *When the user presses the "Transfer" button and if the measured temperature is equal to or above 32 degrees Celsius, transfer the liquid from Container A to Container B.*

The following table shows how this statement forms the logic of a transition.

| Phrase | Element of Transition Logic |
| --- | --- |
| When the user presses the "Transfer" button | Trigger |
| if the measured temperature is equal to or above 32 degrees Celsius | Guard |
| transfer the liquid from Container A to Container B. | Action |

In the LabVIEW Statechart Module, you write LabVIEW block diagram code to express each element of the transition logic.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_top.html language=enus -->
## TOPIC 00077: Statechart Module

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_top.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_top.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Module

June 2013, 372103F-01

Statecharts are useful in simplifying the design of applications that use complex decision-making algorithms. By constructing a statechart, you can visualize the flow of a complex decision-making algorithm and achieve a high-level view of an application. This view helps you improve the overall design of the application.

You can use the LabVIEW Statechart Module to construct a statechart that you can call from a VI. If you are unfamiliar with the Statechart Module, consider completing the [Getting Started with the LabVIEW Statechart Module](../lvschowto/sc_h_gs.html) tutorial.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

© 2007–2013 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_trans.html language=enus -->
## TOPIC 00078: Transitions (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_trans.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_trans.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Transitions (Statechart Module)

Transitions define the conditions under which the statechart can move between [states](../lvsc/sc_state.html). By [creating transitions between states](../lvschowto/sc_h_createtrans.html), you specify how the statechart reacts to certain [triggers](sc_c_tga.html#trigger) or [guards](sc_c_tga.html#guard), which triggers cause the statechart to move to certain states, and in what order the statechart can move between states.

The statechart can take only the transitions that you define. For example, consider the following figure:

[IMAGE alt='image' src='transitions.gif']

In the previous figure, the [Initial](../lvsc/sc_initial.html)
 [pseudostate](sc_c_pseudocon.html) defines [the state that the statechart executes first](../lvschowto/sc_h_firststate.html). In this situation, the first state is State 1. State 1 has an outgoing transition to State 2, and State 2 has an outgoing transition to State 3. This placement of transitions means that the statechart cannot enter State 3 without passing through State 2 first.

Notice also that State 3 has a transition that returns to State 2. You must specify these returning transitions because transitions go in one direction only. State 2 does not have a transition to State 1. This placement of transitions means that, in the previous figure, the statechart cannot return to State 1 after entering State 2.

#### Ports

[Ports](../lvsc/sc_port.html) are the areas on a state that are connected by transition segments. Ports are either rectangular or triangular. Rectangular ports indicate where a transition leaves a state or [connector](sc_c_pseudocon.html). Rectangular ports also indicate where a transition passes through a [region](../lvsc/sc_region.html).

Triangular ports indicate where the transition enters a state or connector. Notice that the ports combine with the transition segments to form an arrow that indicates the direction of the transition.

#### Transition Node

A transition node is the object that divides the transition into segments. You use these nodes to [define the trigger(s), guard, and action of the transition](../lvschowto/sc_h_configt.html). LabVIEW creates these nodes automatically after you [create a transition](../lvschowto/sc_h_createtrans.html).

The following figure shows a transition node.

[IMAGE alt='image' src='tnode.gif']

|  | Note You can see a brief description of the transition by displaying the Context Help window and moving the cursor over the transition node. |
| --- | --- |

The node is divided visually into three white rectangles. The rectangle on the left, closest to the state that initiates the transition, represents the trigger for the transition. A white rectangle here means the transition is configured to use only the [NULL trigger](sc_c_tga.html#null). This configuration is the default for new transitions. A blue rectangle here means the transition is configured to use at least one trigger in addition to, or instead of, the NULL trigger.

The middle rectangle indicates the presence of a guard. This rectangle is white when no guard is defined but turns blue when you define a guard. The rectangle closest to the state that terminates the transition indicates the presence of an action. This rectangle is white when no action is defined but turns blue when you define an action.

For example, the transition node in the following figure has a guard and an action. This transition node is configured to react only to the NULL trigger.

[IMAGE alt='image' src='tnodeblue.gif']

#### Viewing and Changing the Transition Label

Each transition node has a built-in label. To see this label, right-click a transition node you created and select **Visible Items»Label**. LabVIEW displays Transition as the label for this transition. You can double-click this label to change the label. You also can use the **Label** text box in the **Configure Transition** dialog box. The **Show transition node labels** option of the [Statechart](../lvsc/statechart_options.html) page also specifies to display the label of the transition node after you create a transition.

#### Transition Evaluation and Execution

Transitions have the following two phases:

1. Evaluation —This phase occurs when the statechart receives the specified trigger. This phase also evaluates any guard that is associated with the transition. The statechart evaluates transitions according to the priority you specify .
2. Execution —This phase, which occurs only if the guard returns TRUE, executes the specified transition action .

After the Execution phase, the statechart enters the state that terminates the transition. These phases occur during a single [iteration](sc_c_iteration.html) of the statechart.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_c_trigqueue.html language=enus -->
## TOPIC 00079: Trigger Queues (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_c_trigqueue.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_c_trigqueue.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Trigger Queues (Statechart Module)

Each statechart has one or more associated trigger queues. The LabVIEW Statechart Module uses these queues, which operate in a first-in first-out (FIFO) manner, to handle [triggers](sc_c_tga.html#trigger) that you send to the statechart. The statechart checks these queues during each [iteration](sc_c_iteration.html) of the statechart.

[Asynchronous](sc_c_syncasync.html) statecharts have an external queue and an internal queue. The external queue stores triggers that you [send to the statechart](../lvscconcepts/sc_c_callervi.html#async) by using the [Send External Trigger](../lvsc/sc_send_event.html) function. As long as the statechart is in memory, you can send triggers to the external queue from any VI. You also can send triggers to the external queue from a parallel thread in the [caller VI](sc_c_callervi.html). For example, you can have one [While Loop](/csh?topicname=glang/while_loop.html) that executes the [Run Statechart](../lvsc/sc_runsc.html) function and a parallel While Loop that executes the Send External Trigger function.

|  | Note By default, the external queue is a LabVIEW queue. When executing a statechart on a real-time (RT) target, you can use the Statechart Code Generation page of the Project Library Properties dialog box to specify that the external queue is an RT FIFO to ensure that the queue is deterministic by restricting the size of the data. You specify this size, and other queue options, by using this dialog box. |
| --- | --- |

The internal queue, which is a circular buffer, stores triggers that you [send to the statechart](../lvschowto/sc_h_sendsignal.html) by using the [Send Internal Trigger](../lvsc/sc_send_signal.html) function. You can use this function only in an action of a state or transition. This usage means you cannot modify the internal queue by using the caller VI.

|  | Note By default, the internal queue can hold ten triggers. You can change this number by using the Statechart Code Generation page. |
| --- | --- |

[Synchronous](sc_c_syncasync.html) statecharts have an internal queue but not an external queue. This configuration means that you do not use a Send External Trigger function to send triggers to a synchronous statechart. Instead, you can [wire triggers directly](../lvscconcepts/sc_c_callervi.html#sync) to the **Trigger** input of the Run Statechart function. If you do not wire a value to this input, the LabVIEW sends the [NULL trigger](sc_c_tga.html#null) to the statechart.

|  | Note You typically do not send triggers to synchronous statecharts. Synchronous statecharts begin an iteration according to the flow of data through the block diagram of the caller VI. |
| --- | --- |

#### Asynchronous Statecharts and Queue Priority

Asynchronous statecharts begin an iteration only after receiving a trigger from the external queue. The statechart checks the external queue only if the internal queue is empty. For example, consider the following scenario:

1. You use the caller VI to send a trigger to the external queue of an asynchronous statechart. Sending this trigger causes the statechart to begin an iteration.
2. During this iteration, the statechart sends several triggers to the internal queue.
3. Also during this iteration, you use the caller VI to send a second trigger to the external queue.

In this scenario, the statechart stores the second trigger in the external queue. However, the statechart does not check the external queue until the internal trigger queue is empty.

<!--NI_TOPIC bundle=labview-statechart-module path=lvscconcepts/sc_concepts.html language=enus -->
## TOPIC 00080: Concepts (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvscconcepts/sc_concepts.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvscconcepts/sc_concepts.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Concepts (Statechart Module)

Use this book to learn about concepts in LabVIEW Statechart Module. Refer to the [How-To](../lvschowto/sc_howto.html) book for step-by-step instructions for using the Statechart Module.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_gs.html language=enus -->
## TOPIC 00081: Tutorial: Getting Started with the LabVIEW Statechart Module

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_gs.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_gs.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Tutorial: Getting Started with the LabVIEW Statechart Module

This tutorial introduces you to the LabVIEW Statechart Module. In this tutorial, you learn to create a synchronous statechart. This tutorial is divided into the following five parts:

- In Part 1 , you learn how a statechart moves between states and examine how LabVIEW executes statecharts. You also learn some debugging techniques.
- In Part 2 , you learn to create a new statechart.
- In Part 3 , you learn to define the data types that a statechart can use.
- In Part 4 , you learn to place substates within a state.
- In Part 5 , you learn to add substates that the statechart executes concurrently .

|  | Note Refer to the labview\\examples\\Statechart\\Tutorial\\Synchronous directory for completed versions of the statecharts you create in this tutorial. |
| --- | --- |

In the [Asynchronous](sc_h_gs.html) book, you learn to create an asynchronous statechart.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_gs_1.html language=enus -->
## TOPIC 00082: Statechart Module Tutorial Part 1: Examining a Statechart

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_gs_1.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_gs_1.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Module Tutorial Part 1: Examining a Statechart

In Part 1 of this tutorial, you examine how LabVIEW executes a statechart and debug the statechart.

|  | You can complete these exercises in approximately 25 minutes. |
| --- | --- |

#### Running the Caller VI

The first step is opening and running the [caller VI](../lvscconcepts/sc_c_callervi.html), which is the VI that executes the statechart. In this example, the caller VI shows a simulated watch with stopwatch capabilities. Complete the following steps to open and run this VI.

1. Launch LabVIEW and display the Getting Started window.
2. Select File»Open .
3. Browse to the labview\examples\Statechart\Tutorial\Synchronous directory and double-click Getting Started Caller VI.vi .
4. Display the front panel of the VI and click the Run button , located on the LabVIEW toolbar.
5. Click the Insert Battery button. Notice the watch displays the current time.
6. Click the Mode front panel button on the left side of the watch face. Notice the watch displays 00:00:00.0 .
7. Click the Start front panel button and notice the number displayed on the watch increments. Continue pressing buttons on the front panel and notice the changes in the numbers the watch displays.
8. Click the Quit front panel button to stop the VI.

#### Examining the Caller VI

The next step is examining the caller VI. Press the <Ctrl-E> keys to view the block diagram of this VI.

The statechart is [synchronous](../lvscconcepts/sc_c_syncasync.html). Synchronous statecharts execute one iteration at the moment the Run Statechart function receives all input data.

#### Launching the Statechart Editor Window

The next step is launching the [Statechart Editor](../lvscconcepts/sc_c_editor.html) window. This window displays the statechart diagram that you executed in the *Running the Caller VI* section of this tutorial. The statechart diagram is where you place the statechart objects that comprise a statechart.

Complete the following steps to launch the Statechart Editor window.

1. Locate the Run Statechart function on the block diagram.
2. Right-click this function and select View»Statechart Diagram from the shortcut menu to open the Statechart Editor window, which contains the statechart diagram.

#### Examining the Statechart

The statechart diagram resembles the following image:

[IMAGE alt='image' src='s_gsg1_1.gif']

When you ran the caller VI, the statechart located the 
 [Initial](../lvsc/sc_initial.html) [pseudostate](../lvscconcepts/sc_c_pseudocon.html). The transition (1) that exits this pseudostate specifies which state the statechart enters first. Therefore, the statechart executed the Watch Dead state (2) first. The statechart then waited for the caller VI to send a trigger, which happened when you clicked the **Insert Battery** front panel button. When you clicked this button, the caller VI sent a trigger to the statechart. This trigger caused the statechart to take the transition (3) to the Watch Running state and wait for another trigger, which you sent by clicking the **Mode** front panel button. Each state is configured to update the text of the **Time Display** indicator.

|  | Note Because transitions go in only one direction, notice that the transition that enters the Watch Running state is separate from the transition that exits the Watch Running state. |
| --- | --- |

The arrow-shaped objects in the middle of each transition are the [transition nodes](../lvscconcepts/sc_c_trans.html#transition_node). The following image shows a transition node.

[IMAGE alt='image' src='transnodeblue.gif']

The blue rectangles on these nodes indicate certain information about the transition. You will create and configure a transition in [Part 2](sc_gs_2.html) of this tutorial.

#### Highlighting Statechart Execution

The next step is highlighting the execution of the statechart. Complete the following steps to highlight the execution of the statechart.

1. Run the caller VI and display the block diagram.
2. Right-click the Run Statechart function and select Debug Statechart from the shortcut menu to display the statechart in the Statechart Debugging window.
3. Click the Highlight Execution button , located on the toolbar of the Statechart Debugging window, to enable statechart execution highlighting.
4. Display the front panel of the caller VI and click the Insert Battery front panel button. Watch LabVIEW highlight the transition from the Watch Dead state to the Watch Running state.
5. Click the Mode front panel button and watch the statechart move from the Clock substate to the Timer substate.
6. Click the Start front panel button. Watch the statechart move from the Idle substate to the Running substate.
7. Click the Quit front panel button. Watch the statechart move to the Terminal pseudostate and stop the execution of the statechart.
8. Click the Highlight Execution button to disable execution highlighting.

#### Watching Statechart Data

The next step is running the caller VI and watching how the statechart increments the **Time Display** indicator. Complete the following steps to view data in the **Statechart Data Display** window.

1. In the Statechart Debugging window, click the Open Statechart Data Display button , located on the toolbar of this window. LabVIEW displays the Statechart Data Display window. This window shows the values of the state data, output data, and internal trigger queue.
2. Run the caller VI.
3. Click the Insert Battery button. The watch displays the current time.
4. Look at the Statechart Data Display window. Notice the Time Display indicator displays the same value as the front panel indicator of the caller VI.
5. Click the Mode front panel button. The watch displays 00.00.00.0 , which means the statechart is in the Timer substate. Notice the Time Display indicator in the Statechart Data Display window also displays 00.00.00.0 .
6. Click the Mode front panel button again and notice the value of the Time Display indicator in the Statechart Data Display window displays the current time.
7. Close the Statechart Data Display window.

#### Viewing the Execution of a Transition Guard

The next step is viewing the execution of a transition guard. A transition guard is LabVIEW block diagram code that determines whether the statechart takes the associated transition. The guard code must return either TRUE or FALSE. If the guard returns TRUE, the statechart takes the transition. If the guard returns FALSE, the statechart does not take the transition. Complete the following steps to view the execution of a guard.

1. In the Statechart Debugging window, locate the guarded transition node from the Idle substate to the Running substate.
2. Right-click this transition node and select Guard . LabVIEW displays the block diagram of the VI that corresponds to the guard.
3. Move the cursor over the green wire that exits the IsIn? function.
4. Click this wire to place a probe on this wire.
5. Click the Start front panel button. The probe shows that the guard code sends FALSE to the Execute? indicator. This FALSE value means the statechart does not take the transition to the Running state.
6. Click the Mode front panel button to transition the statechart to the Timer substate.
7. Click the Start front panel button again. The IsIn function sends TRUE to the Execute? indicator, which means the guard returns TRUE. The statechart then takes the transition to the Running substate.
8. Click the Quit front panel button to stop the statechart and the caller VI.
9. Close all windows.

#### Summary

In this tutorial, you learned about the following tasks:

- Opening and running a caller VI.
- Examining a statechart.
- Highlighting the execution of a statechart.
- Displaying the statechart data during execution.
- Viewing the execution of a transition guard.

#### Where to Go from Here

In [Part 2](sc_gs_2.html) of this tutorial, you create and configure a new statechart.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_gs_2.html language=enus -->
## TOPIC 00083: Statechart Module Tutorial Part 2: Building a Statechart

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_gs_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_gs_2.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Module Tutorial Part 2: Building a Statechart

In [Part 1](sc_gs_1.html) of this tutorial, you examined a statechart that represented an average watch. You recreate this statechart in Parts 2-5 of this tutorial.

|  | You can complete these exercises in approximately 35 minutes. |
| --- | --- |

|  | Note You can refer to the labview\\examples\\Statechart\\Tutorial\\Synchronous\\Getting Started 2.lvsc for a completed version of the statechart you create in this part of the tutorial. |
| --- | --- |

#### Creating and Configuring the Statechart

Complete the following steps to create and configure the statechart.

1. Launch LabVIEW and display the Getting Started window.
2. Select File»New to display the New dialog box.
3. Select Other Files»Statechart from the Create New tree.
4. Click the OK button. LabVIEW prompts you to save the statechart.
5. Enter My Getting Started Statechart.lvsc and save the statechart in a convenient location on disk.
 LabVIEW displays a Project Explorer window that contains the necessary support files under the My Getting Started Statechart.lvsc project item. This project item represents the .lvsc file in which LabVIEW stores statechart information.
6. Right-click the My Getting Started Statechart.lvsc item and select Properties from the shortcut menu. LabVIEW launches the Properties dialog box.
7. Select the Statechart Code Generation item from the Category list. LabVIEW displays options relating to statechart code generation .
8. Verify that the Usage pull-down menu displays Synchronous .
9. Click the OK button to save changes and return to the Project Explorer window.

#### Defining States

The next step is defining the states that comprise the statechart. A state is a unique condition in which the statechart can exist. For example, a basic light bulb can be either ON or OFF. Therefore, a statechart that represents this light bulb would contain only those two states.

The statechart you construct represents a basic watch. This statechart consists of two fundamental states: Watch Dead and Watch Running. Complete the following steps to create these states.

1. In the Project Explorer window, double-click the Diagram.vi item to open the Statechart Editor window.
 This window displays the statechart diagram. You build a statechart by placing statechart objects on the statechart diagram.
 
 [IMAGE alt='image' src='note.gif']
**Note** If you do not see the [Functions](/csh?topicname=glang/functions_palette.html) palette, select **View»Functions Palette** to display this palette.
2. On the Functions palette, select Statechart»Statechart Development to display the Statechart Development palette.
3. Click the State object.
4. Move the cursor over the statechart diagram. Click to place the top left corner of the state, drag the cursor diagonally to establish the size of the state, and click again to place the state on the statechart diagram.
5. Notice the state is labeled State . Double-click this label to enable text editing and enter Watch Dead as the new label.
6. Move the cursor over the gray outline of the Watch Dead state until the cursor changes to the Positioning tool .
7. Press the <Ctrl> key and click and drag the cursor below the Watch Dead state to create a copy of the state.
8. Label this new state Watch Running .
9. Return to the Statechart Development palette and place a Terminal pseudostate to the right of the Watch Dead state.
 [IMAGE alt='image' src='note.gif']
**Note** A pseudostate is a statechart object that represents a state. The Terminal pseudostate represents a state that terminates the execution of the statechart.

The statechart diagram now resembles the following image:

[IMAGE alt='image' src='s_gsg2_1.gif']

#### Creating a Transition

The next step is defining how the statechart moves between states. To define this behavior, you use transitions to connect one state to another visually. Complete the following steps to create transitions between two states.

1. Move the cursor just inside the bottom border of the Watch Dead state until the cursor changes to the Wiring tool .
2. Click the state border. As you move the cursor down the statechart diagram, LabVIEW draws a dotted line between the state and the Wiring tool.
3. Move the cursor over the top border of the Watch Running state. A gray box appears under the cursor.
4. Click the border to finish the transition. LabVIEW creates a transition between the two states.

The statechart diagram now resembles the following image:

[IMAGE alt='image' src='s_gsg2_2.gif']

The object that appears in the middle of the transition is a [transition node](../lvscconcepts/sc_c_trans.html#transition_node). You use this node to configure the transition.

#### Creating a Trigger and Configuring a Transition

The next step is specifying when the statechart takes the transition. The statechart takes a transition only after receiving a specific event, called a trigger.

You create a list of triggers for use with each statechart. In this tutorial, you configure a transition by associating a trigger with the transition. Complete the following steps to create a trigger and configure the transition.

1. Double-click the transition node between the Watch Dead and Watch Running states to launch the Configure Transition dialog box. You use this dialog box to configure transitions.
 The first tab in this dialog box is the Triggers/Groups tab. Notice that the NULL trigger is selected by default in the Triggers and Groups list. Every statechart has this trigger by default.
2. Click the Edit Triggers and Groups button to launch the Edit Triggers and Groups dialog box. You use this dialog box to create and modify triggers.
3. Click the Create Trigger button to create a new trigger, which appears in the Triggers and Groups list.
4. Enter Insert Battery as the new trigger name.
5. Click the OK button to save changes and return to the Configure Transition dialog box. Notice the new trigger appears in the Triggers list.
6. In the Triggers/Groups list, place a checkmark in the Insert Battery checkbox to specify that this trigger causes the statechart to take the transition.
7. Remove the checkmark from the NULL checkbox.
8. Click the OK button to save changes and return to the statechart diagram.
9. Save the statechart by selecting File»Save in the Statechart Editor window. You also can press the <Ctrl-S> keys.

Notice the blue rectangle on the transition node. This rectangle indicates that you have specified a non-NULL trigger for the transition. If you move the cursor over the transition node, the [Context Help](/csh?topicname=lvdialog/context_help_window.html) window displays the properties of the transition, including the trigger. If you do not see the **Context Help** window, press the <Ctrl-H> keys to display this window.

#### Creating and Configuring Additional Transitions

When you create a transition, the state border you click first is the state that initiates the transition. Because transitions are unidirectional, you must create a second transition to return to the initiating state.

|  | Note Notice that the transition itself forms an arrow indicating the direction of the transition. |
| --- | --- |

Create and configure the following transitions and triggers. You may want to create all of the triggers at one time and then configure the transitions. Remember to deselect the NULL trigger for each transition.

- From the Watch Running state to the Watch Dead state. Configure this transition to react to a Dead Battery trigger.
- From the Watch Running state to the Terminal pseudostate. Configure this transition to react to a Quit trigger.
- From the Watch Dead state to the Terminal pseudostate. Configure this transition to react to a Quit trigger.

|  | Tip Right-click a transition and select Clean Up Wire to automatically reroute a transition on the diagram. |
| --- | --- |

Save the statechart by pressing the <Ctrl-S> keys.

The statechart diagram now resembles the following image:

[IMAGE alt='image' src='s_gsg2_3.gif']

#### Finding and Fixing Statechart Errors

The toolbar of the Statechart Editor window contains a button that you click to generate code for the statechart. Currently, this button appears broken [IMAGE alt='image' src='sc_broken.gif']. This icon means that this statechart contains errors. You must fix these errors before you can generate code for this statechart.

Complete the following steps to find and fix errors in this statechart.

1. Click the List Errors button to display the Error list window, which displays several errors.
 These errors appear because the top-level statechart diagram does not have an Initial pseudostate. This pseudostate defines the first state that the statechart enters. The top-level statechart diagram must have one and only one Initial pseudostate.
2. Click the Close button to return to the statechart diagram.
3. Place an Initial pseudostate, located on the Statechart Development palette, to the left of the Watch Dead state.
4. Wire the Initial pseudostate to the Watch Dead state to create a transition. Notice the Generate Code button replaces the List Errors button. Transitions that exit Initial pseudostates cannot have triggers or guards. Therefore, you do not have to configure this transition. The statechart diagram now resembles the following image:
 [IMAGE alt='image' src='s_gsg2_4.gif']
5. Save the statechart.
6. Close the Statechart Editor window.

#### Summary

In this tutorial, you learned about the following tasks:

- Creating a statechart.
- Creating states.
- Creating transitions between states.
- Creating triggers.
- Configuring a transition to react to a trigger.
- Finding errors on the statechart diagram.
- Specifying the first state that a statechart executes.
- Specifying a state that terminates the statechart.

#### Where to Go from Here

In [Part 3](sc_gs_3.html) of this tutorial, you define statechart data.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_gs_3.html language=enus -->
## TOPIC 00084: Statechart Module Tutorial Part 3: Defining Statechart Data Types

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_gs_3.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_gs_3.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Module Tutorial Part 3: Defining Statechart Data Types

In [Part 2](sc_gs_2.html) of this tutorial, you created the beginnings of a statechart and learned how to find errors on the statechart diagram. In Part 3 of this tutorial, you define types of data upon which the statechart acts.

|  | You can complete these exercises in approximately 20 minutes. |
| --- | --- |

|  | Note You can refer to the labview\\examples\\Statechart\\Tutorial\\Synchronous\\Getting Started 3.lvsc for a completed version of the statechart you create in this part of the tutorial. |
| --- | --- |

#### Defining the Type of Output Data

If you want the statechart to modify data, you first must define the type of data. This process involves creating the controls and/or indicators that represent the statechart data.

Complete the following steps to define the statechart output data. In [Part 4](sc_gs_4.html) of this tutorial, you configure the statechart to modify this data.

1. Open the My Getting Started.lvsc statechart you constructed in Part 2 of this tutorial. You also can navigate to the labview\examples\Statechart\Tutorial\Synchronous directory and open Getting Started 2.lvsc for a completed statechart from Part 2 of this tutorial.
2. In the Project Explorer window, double-click the Outputs.ctl item. LabVIEW displays the Control Editor window for this type definition .
3. Notice the numeric control Numeric inside the Outputs cluster. Right-click this control and select Change to Indicator from the shortcut menu to change this control to a numeric indicator.
4. Right-click the Numeric indicator and select Replace»Express»Text Indicators»String Indicator from the shortcut menu. This action replaces the numeric indicator with a string indicator.
5. Double-click the String label and enter Time Display as the new label.
6. Press the <Ctrl-S> keys to save this type definition.
7. Close the Control Editor window to return to the Project Explorer window.

#### Defining the Type of State Data

You also define state data, which differs from output data. State data is accessible only from the statechart, whereas output data also is accessible from a VI that calls the statechart. Use state data to define data types that other VIs do not need to access.

Complete the following steps to define the statechart state data. You modify this data in Part 4 of this tutorial.

1. In the Project Explorer window, double-click the StateData.ctl item.
2. Double-click the Data label and enter Timer as the new label.
3. Right-click the Timer control and select Representation»Unsigned Long from the shortcut menu.
4. Expand the StateData cluster by dragging the bottom-right corner down and to the right.
5. Move the cursor over the border of the Timer control until the cursor changes to the Positioning tool .
6. Press the <Ctrl> key and click and drag the cursor below the Timer numeric control to create a copy of the control.
7. Label this new control Clock .
8. Press the <Ctrl-S> keys to save this type definition.
9. Close the Control Editor window to return to the Project Explorer window.

#### Generating Code for the Statechart

The next step is generating code for the statechart. This code is contained in a single [Run Statechart](../lvsc/sc_runsc.html) function that you place on the block diagram of the [caller VI](../lvscconcepts/sc_c_callervi.html). Complete the following steps to generate code for this statechart.

1. Display the Statechart Editor window for the My Getting Started Statechart.lvsc statechart that you constructed in Part 2 of this tutorial. You can display the Statechart Editor window by double-clicking the Diagram.vi item in the Project Explorer window for the statechart.
2. Click the Generate Code button , which is located on the toolbar of this window. LabVIEW displays a dialog box indicating the status of the code generation progress.

|  | Note You also can generate code by right-clicking the .lvsc file in the Project Explorer window and selecting Generate Code from the shortcut menu. |
| --- | --- |

#### Configuring the Caller VI

The next step is configuring a caller VI to execute and send triggers to the statechart. This VI contains the Run Statechart function that you must link to the statechart. Complete the following steps to link the Run Statechart function to the statechart.

1. In the Statechart Editor window, select File»Open .
2. Browse to the labview\examples\Statechart\Tutorial\Synchronous directory and double-click Getting Started Caller VI (Unlinked).vi .
3. Display the block diagram of this VI. All the wires are broken because the Run Statechart function is not linked to a statechart.
4. Locate the Run Statechart function. This function executes the statechart when you run the caller VI.
5. Right-click this function and select Link to Statechart from the shortcut menu. LabVIEW prompts you for a .lvsc file to which the function can link.
6. Click the Browse button and navigate to the directory that contains the My Getting Started Statechart.lvsc file.
7. Click the OK button. Notice the wires to and from this function now are intact.
8. Select File»Save As and save the caller VI as Getting Started Caller VI Linked.vi .
9. Press the <Ctrl-R> keys to run the caller VI. Click the front panel buttons and notice the Time Display indicator does not change value. You configure the statechart to change the value of the Time Display indicator in Part 4 of this tutorial.
10. Click the Quit button to stop the VI.
11. Save and close the caller VI.

|  | Note The inputs and triggers wired to the Run Statechart function are not linked to the My Getting Started Statechart.lvsc file. The Getting Started Caller VI (Unlinked).vi does not reflect any changes you make to the inputs or triggers in the My Getting Started Statechart.lvsc code. |
| --- | --- |

#### Summary

In this tutorial, you learned about the following tasks:

- Defining types of data that the statechart can modify.
- Generating code for the statechart.
- Linking the Run Statechart function to a statechart.

#### Where to Go from Here

In [Part 4](sc_gs_4.html) of this tutorial, you add regions and substates to the statechart.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_gs_4.html language=enus -->
## TOPIC 00085: Statechart Module Tutorial Part 4: Adding Regions and Substates

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_gs_4.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_gs_4.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Module Tutorial Part 4: Adding Regions and Substates

In Parts 2 and 3 of this tutorial, you created a statechart consisting of two states, two pseudostates, and transitions between these objects. You also defined output types and state data types and configured a caller VI.

In Part 4 of this tutorial, you add hierarchical substates to the statechart, create a trigger using the **Project Explorer** window, and configure static reactions. You also modify statechart data.

|  | You can complete these exercises in approximately 30 minutes. |
| --- | --- |

|  | Note You can refer to the labview\\examples\\Statechart\\Tutorial\\Synchronous\\Getting Started 4.lvsc for a completed version of the statechart you create in this part of the tutorial. |
| --- | --- |

#### Adding a Region and Two Substates

A region defines an area in which you can place states. You can place regions within states, which means you can use regions to define hierarchical substates. Complete the following steps to add a region and two substates to this statechart.

1. Display the Statechart Editor window for the My Getting Started Statechart.lvsc statechart that you constructed in Part 3 of this tutorial. You also can navigate to the labview\examples\Statechart\Tutorial\Synchronous directory and open Getting Started 3.lvsc for the completed statechart from Part 3 of this tutorial. You can display the Statechart Editor window by double-clicking the Diagram.vi item in the Project Explorer window for the statechart.
2. Move the cursor over the bottom of the Watch Running state until resizing handles appear.
3. Drag the resizing handles down and to the right to increase the size of this state.
4. Display the Statechart Development palette.
5. Click the Region icon.
6. Move the cursor within the Watch Running state. Click and drag to place this region on the statechart diagram.
7. Notice the region is labeled Region . Enter Display as the new label.
8. Place two states and an Initial pseudostate in this region.
9. Label the first state Clock and the second state Timer .
10. Save the statechart.

The statechart diagram now resembles the following image:

[IMAGE alt='image' src='s_gsg4_1.gif']

|  | Note The Watch Running state now contains two substates. Therefore, the Watch Running state now is a superstate. |
| --- | --- |

#### Creating Another Trigger

The next step is creating a trigger. You will configure a transition to react to this trigger.

Complete the following steps to create this trigger.

1. Display the Project Explorer window for this statechart.
2. Double-click the Edit Triggers and Groups item. LabVIEW launches the Edit Triggers and Groups dialog box, which you use to create triggers and groups of triggers.
3. Click the Create Trigger button to add a trigger to the list.
4. Enter Mode as the name of this trigger.
5. Click the OK button to save changes.

#### Creating and Configuring Transitions in a Region

The next step is creating and configuring two transitions in the Display region. Create and configure the following transitions:

- From the Initial pseudostate to the Clock substate.
- From the Clock substate to the Timer substate. Configure this transition to react to the Mode trigger only.
- From the Timer substate to the Clock substate. Configure this transition to react to the Mode trigger only.

The statechart diagram now resembles the following image:

[IMAGE alt='image' src='s_gsg4_4a.gif']

#### Configuring the Timer Substate

The next step is configuring the Timer substate by creating a [static reaction](../lvscconcepts/sc_c_staticrxn.html) to modify the **Time Display** output data you defined in [Part 3](sc_gs_3.html) of this tutorial. A static reaction defines the behavior of a state while that state is not taking any outgoing transitions.

Complete the following steps to create a static reaction for the Timer substate.

1. Double-click the border of the Timer substate. LabVIEW launches the Configure State dialog box.
 
 [IMAGE alt='image' src='note.gif']
**Note** When you configure a state, a wrench icon appears on the state ([IMAGE alt='image' src='noloc_env_state_config_wrench.gif']) in the **Statechart Editor** window. The state also changes color. You can [customize the configuration color](../lvschowto/sc_h_config_color.html) for states. The default configuration color is yellow. 
 The left side of this dialog box contains the Reactions list. By default, the dialog box displays the Entry Action item in the Reactions list. This selection specifies that you want to define the entry action of the state.
 The right side of this dialog box displays several tabs that correspond to the reaction you select from the Reactions list. By default, the Action tab is selected. This tab displays the block diagram you use to define the entry action.
2. Click the Create button to add a static reaction to the Reactions listbox. Label the new static reaction Chrono Display .
3. On the Action tab, notice the Outputs cluster element on the right side of this block diagram. Click this cluster element and select Outputs»Time Display . This element now displays Outputs.Time Display . You now can use this element to write to the value of the Time Display indicator.
4. Click the Outputs cluster element on the left side of the block diagram and select StateData»Timer .
5. Place the Convert Timer to Time Stamp VI on the diagram.
  1. On the Functions palette, select Select a VI to display the dialog box you use to select the subVI.
  2. Navigate to the labview\examples\Statechart\Tutorial\Synchronous directory and double-click Convert Timer to Time Stamp.vi .
  3. Place the VI on the block diagram.
  4. Wire the StateData.Timer cluster control to the Timer input of the Convert Timer to Time Stamp VI.
  5. Wire the date/time string output of the Convert Timer to Time Stamp VI to the Outputs.Time Display cluster control.
 

 The block diagram resembles the following image:
 [IMAGE alt='image' src='s_gsg4_5.gif']
6. Click the OK button to save the changes.

#### Configuring the Clock Substate

The next step is configuring the Clock substate to display the current time. You accomplish this by adding a static reaction to the Clock substate and using action code to display the current time in the **Time Display** output data.

Complete the following steps to configure the Clock substate.

1. Double-click the border of the Clock substate to launch the Configure State dialog box.
2. Create a static reaction . Label the new static reaction Display Time .
3. On the Action tab, write LabVIEW code that displays the current time in the Time Display control.
  1. Click the Outputs cluster element on the left side of the diagram and select StateData»Clock .
  2. Place the Get Date/Time in Seconds and Format Date/Time String functions on the block diagram.
  3. Wire the current time output of the Get Date/Time in Seconds function to the time stamp input of the Format Date/Time String function.
  4. Right-click the time format string terminal of the Format Date/Time String function and select Create»Constant from the shortcut menu. Enter %I:%M:%S %p for the value of the constant.
  5. Click the Outputs cluster element on the right side of the diagram and select Outputs»Time Display .
  6. Wire the date/time string output of the Format Date/Time String function to the Outputs.Time Display cluster element. The block diagram resembles the following image:
 [IMAGE alt='image' src='s_gsg4_6.gif']
4. Click the OK button to save the changes.

#### Running the Caller VI

1. In the Statechart Editor window, click the Generate Code button.
2. Open the Getting Started Caller VI Linked VI you created in Part 3 of this tutorial.
3. Run the caller VI.
4. Click the Insert Battery front panel button. Notice the watch displays the current time.
5. Click the Mode button. Notice the watch displays 00.00.00.0 .
6. Click the Quit front panel button.
7. Save and close the VI and statechart.

#### Summary

In this tutorial, you learned the following tasks:

- Creating regions.
- Creating substates.
- Creating triggers using the Project Explorer window.
- Configuring reactions.
- Modifying statechart data.

#### Where to Go from Here

In [Part 5](sc_gs_5.html) of this tutorial, you add orthogonal regions and define the guard for a transition.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_gs_5.html language=enus -->
## TOPIC 00086: Statechart Module Tutorial Part 5: Using Orthogonal Regions

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_gs_5.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_gs_5.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Module Tutorial Part 5: Using Orthogonal Regions

In [Part 4](sc_gs_4.html) of this tutorial, you learned how to create and configure regions and substates. In Part 5 of this tutorial, you add orthogonal regions.

|  | You can complete these exercises in approximately 35 minutes. |
| --- | --- |

|  | Note You can refer to the labview\\examples\\Statechart\\Tutorial\\Synchronous\\Getting Started 5.lvsc for a completed version of the statechart you create in this part of the tutorial. |
| --- | --- |

#### Creating the Orthogonal Region

Orthogonal regions are multiple regions in the same state. Substates in orthogonal regions execute concurrently, which means these states both execute during a single iteration of the statechart. Complete the following steps to add orthogonal regions to the statechart.

1. Display the Statechart Editor window for the My Getting Started Statechart.lvsc statechart that you constructed in Part 4 of this tutorial. You also can navigate to the labview\examples\Statechart\Tutorial\Synchronous directory and open Getting Started 4.lvsc for the completed statechart from Part 4 of this tutorial. You can display the Statechart Editor window by double-clicking the Diagram.vi item in the Project Explorer window for the statechart.
2. Click and drag to increase the size of the Watch Running superstate.
3. Place a second region inside the Watch Running superstate below the Display region.
4. Label this new region Timer .
5. Place two states inside this region.
6. Label the substates Idle and Running .
7. Place an Initial pseudostate in the Timer region.
8. Create the following transitions:
  - From the Initial pseudostate to the Idle substate.
  - From the Idle substate to the Running substate. Configure this transition to react to a Start trigger only.
  - From the Running substate to the Idle substate. Configure this transition to react to a Stop/Reset trigger only.

The statechart diagram now resembles the following image:

[IMAGE alt='image' src='s_gsg5_1.gif']

#### Defining a Transition Guard

The next step is specifying that the statechart transitions from the Idle to the Running state only when the statechart also is executing the Timer substate. To specify this behavior, you use a transition guard. A transition guard is LabVIEW block diagram code that determines whether the statechart takes the associated transition. The guard code must return either TRUE or FALSE. If the guard returns TRUE, the statechart takes the transition. If the guard returns FALSE, the statechart does not take the transition.

Complete the following steps to define this guard.

1. Double-click the transition node from the Idle state to the Running state to display the Configure Transition dialog box.
2. Click the Guard tab.
3. Click the Inputs cluster control on the left-side of the block diagram and select StatechartState .
4. Use the IsIn function on the Statechart Communication palette to return TRUE if the Timer state is active.
  1. Place the IsIn function on the block diagram.
  2. Wire the StatechartState cluster control to the Statechart States input of the IsIn function.
  3. Wire the IsIn? output to the Execute? cluster element.
  4. Right-click the IsIn function and select Select State from the shortcut menu. LabVIEW displays the Select State dialog box. You use this dialog box to specify the state vector, which is the path of states and regions that contain the state.
  5. Select Watch Running»Display»Timer . The Current Selection text box displays Watch Running\Display\Timer .
  6. Click the OK button. The block diagram resembles the following image:
 [IMAGE alt='image' src='s_gsg5_2.gif']
5. Click the OK button to return to the statechart diagram.
6. Repeat steps 1-4 to create a transition guard from the Running state to the Idle state.
7. Save the statechart.

With this configuration, the statechart checks the guard code every time the caller VI sends the Start or Stop/Reset trigger. The guard code returns FALSE if the Timer substate is not active.

#### Modifying State Data

The next step is to modify state data while the Running and Idle states run. You do this by creating static reactions to modify the state data controls. Complete the following steps to modify the Timer and Clock state data controls.

1. Define a static reaction in the Running state called Increment .
  1. On the Action tab, click the Outputs cluster element on the left side of the diagram and select StateData»Timer .
  2. Place the Add function on the block diagram.
  3. Wire the StateData.Timer cluster element to the x input of the Add function.
  4. Right-click the y input of the Add function and select Create»Constant from the shortcut menu.
  5. Enter 50 for the value of the constant.
  6. Click the Outputs cluster element on the right side of the diagram and select StateData»Timer .
  7. Wire the x+y output of the Add function to the StateData.Timer cluster element on the right side of the diagram. The action code for the Increment static reaction resembles the following image:
 [IMAGE alt='image' src='s_gsg5_3.gif']
2. Configure the Increment static reaction to react to all triggers.
  1. Navigate to the Triggers/Groups tab.
  2. Click the Select All Triggers button.
3. Define a static reaction in the Idle state called Reset . You configure the Reset reaction to reset the Timer state data control to 0.
  1. On the Action tab, click the Outputs cluster control on the left side of the diagram and select StateData»Timer .
  2. Click the Outputs cluster control on the right side of the diagram and select StateData»Timer .
  3. Right-click the StateData.Timer cluster element on the right side of the block diagram and select Create»Constant from the shortcut menu. Leave the default value 0 for the constant.
4. On the Triggers/Groups tab, specify the Reset static reaction only reacts to the Stop/Reset trigger.
5. Click the OK button to close the Configure State dialog box.
6. Save the statechart.
7. Close the Statechart Editor window.

#### Enabling Debugging for the Statechart

If you want to use the debugging tools for a statechart, you first must enable debugging for the statechart.

Complete the following steps to enable debugging for the statechart.

1. Right-click the My Getting Started Statechart.lvsc item in the Project Explorer window and select Properties from the shortcut menu. LabVIEW launches the Properties dialog box.
2. Select the Statechart Code Generation item from the Category list. LabVIEW displays options relating to statechart code generation .
3. Select Enabled from the Debugging pull-down menu to specify that debugging is enabled for the statechart. The default value is Enabled . 
 [IMAGE alt='image' src='note.gif']
**Note** Debugging is only available on Desktop, Real-Time, and FPGA targets.
4. Click the OK button to save changes and return to the Project Explorer window.
5. Right-click the My Getting Started Statechart.lvsc item and select Generate Code from the shortcut menu to generate code for the statechart.

#### Running the Caller VI Again

1. Run the caller VI and watch the state data .
2. Click the Insert Battery button. The Time Display indicator displays the current time.
3. Click the Mode front panel button. The Time Display indicator displays 00.00.00.0 , which means the statechart is in the Timer substate.
4. Click the Start front panel button to start the timer.
5. Click the Mode front panel button to switch the statechart to the Clock substate.
6. Click the Mode front panel button again to switch back to the Timer substate. Notice the Time Display indicator continued to increment while the statechart was in the Clock substate.
7. Click the Quit front panel button to stop the caller VI.
8. Save the caller VI.

#### Summary

In this tutorial, you learned the following tasks:

- Creating orthogonal regions.
- Defining regions that execute concurrently.
- Defining the guard of a transition.
- Generating code for the statechart from the Project Explorer window.

#### Where to Go from Here

- Documentation related to the LabVIEW Statechart Module.
- The Getting Started with LabVIEW manual contains an in-depth introduction to LabVIEW, including several tutorials that showcase LabVIEW features.
- The LabVIEW Fundamentals book provides information about LabVIEW programming concepts, techniques, features, VIs, and functions you can use to create many types of applications.
- Refer to the National Instruments Web site for additional developer resources, training, technical support, and so on.

|  | (Windows) To view topics related to the Statechart Module, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_breakpoints.html language=enus -->
## TOPIC 00087: Setting Breakpoints in a Statechart (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_breakpoints.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_breakpoints.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Setting Breakpoints in a Statechart (Statechart Module)

You can set [breakpoints](/csh?topicname=lvconcepts/debug_techniques.html) on a statechart diagram or in a [guard](../lvscconcepts/sc_c_tga.html#guard) or [action](../lvscconcepts/sc_c_tga.html#action). The following sections provide information about setting breakpoints in both of these locations.

#### Setting Breakpoints on a Statechart Diagram

Complete the following steps to set a breakpoint on a statechart diagram.

1. Run the caller VI .
2. Right-click the Run Statechart function and select Debug Statechart . The statechart diagram appears in debugging mode, which means you cannot edit the diagram.
 [IMAGE alt='image' src='note.gif']
**Note** If you do not see the **Debug Statechart** option, you might have [disabled statechart debugging](sc_h_disabledebug.html). You must re-enable debugging and re-generate the code before proceeding.
3. Right-click any transition node or state and select Breakpoint»Set Breakpoint from the shortcut menu. LabVIEW highlights the selected object in red.
 When you reach a breakpoint during execution, the statechart pauses. You can take the following actions:
  - Right-click the object and use the shortcut menu to display the guards and/or actions of that object.
  - Single-step through execution by using the single-stepping buttons.
  - Click the Pause button to continue running until the next breakpoint or until the statechart finishes executing.

#### Setting Breakpoints in a Guard or Action

You can set breakpoints in a guard or action by right-clicking an object on the block diagram and selecting **Breakpoint»Set Breakpoint** from the shortcut menu. When an executing statechart encounters these breakpoints, LabVIEW pauses execution, and you can debug the guard or action similar to [debugging a VI](/csh?topicname=lvconcepts/debug_techniques.html).

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_callsc.html language=enus -->
## TOPIC 00088: Creating a Caller VI (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_callsc.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_callsc.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Creating a Caller VI (Statechart Module)

Creating a [caller VI](../lvscconcepts/sc_c_callervi.html) to communicate with a statechart is different depending on whether the statechart is [asynchronous or synchronous](../lvscconcepts/sc_c_syncasync.html). In either case, you complete the following steps to prepare the statechart.

1. Generate code for the statechart .
2. Display the Project Explorer window that contains the .lvsc file for which you generated code.
3. Create a new, blank VI to serve as the caller VI.
4. Display the block diagram of this VI.
5. Drag the .lvsc project item onto the block diagram to create a Run Statechart function that links to the appropriate statechart.
6. (Optional) Provide input data to the statechart by wiring a value to the Inputs input of the Run Statechart function.
7. (Optional) Right-click the Outputs output and select Create»Indicator from the shortcut menu to create a cluster indicator for data that the statechart returns. You can unbundle this cluster to access specific elements.

#### Asynchronous Statecharts

The following example shows how to create a caller VI that both executes and sends triggers to an asynchronous statechart. In this situation, the caller VI has two [While Loops](/csh?topicname=glang/while_loop.html) that execute in parallel. The first While Loop contains an [Event structure](/csh?topicname=glang/event_structure.html) that uses the [Send External Trigger](../lvsc/sc_send_event.html) function to send triggers to the [external queue](../lvscconcepts/sc_c_trigqueue.html) of the statechart. The second While Loop contains the [Run Statechart](../lvsc/sc_runsc.html) function that executes the statechart. You also can place these loops in two separate VIs to achieve greater modularization.

Complete the following steps to configure a caller VI to execute and send triggers to an asynchronous statechart.

1. Place an Event structure in the first loop and the Run Statechart function in the second loop.
2. Add event cases to the Event structure. Each case should correspond to one or more triggers that you want to send to the statechart.
3. Wire a value to the Instance Name input of the Run Statechart function to create a name for the external queue of the statechart instance this function runs.
 [IMAGE alt='image' src='note.gif']
**Note** If you do not see this input, the Run Statechart function is linked to a synchronous statechart. You must link the Run Statechart function to an asynchronous statechart.
4. Right-click the Run Statechart function and select Create Send External Trigger Function to create a Send External Trigger function that links to the appropriate statechart.
5. Place the Send External Trigger function in the loop that contains the Event structure.
6. Specify the queue to which this function sends the trigger by wiring a value to the Instance Name terminal of the Send External Trigger function. Ensure this name is identical to the value you wired to the Instance Name input of the Run Statechart function.
7. Specify the trigger to send by wiring a value to the Trigger input of the Send External Trigger function.
 [IMAGE alt='image' src='tip.gif']
**Tip** You can obtain a list of valid triggers by right-clicking the **Trigger** input and selecting either **Create»Control** or **Create»Constant** from the shortcut menu.
8. Move the trigger constant or control inside the corresponding case of the Event structure.
9. Wire the trigger constant or control to the Trigger input of the Send External Trigger function. This wire exits the Event structure through an output tunnel.
10. For each case of the Event structure, right-click the output tunnel and select either Create Control or Create Constant . Change the control or constant to represent the trigger you want to send.

The caller VI now resembles the following figure:

[IMAGE alt='image' src='lvschowto_callervi_async.gif']

The caller VI now is configured to execute and send triggers to the statechart.

#### Synchronous Statecharts

You use only one loop in a caller VI. This loop contains only the Run Statechart function. You also can use this loop to send triggers to the statechart by wiring a trigger to the **Trigger** input of this function.

This loop can be a While Loop. However, if you need to execute the statechart at specific intervals, National Instruments recommends placing the Run Statechart function in a [Timed Loop](/csh?topicname=glang/timed_loop.html) instead.

Complete the following steps to configure a caller VI to execute a synchronous statechart.

1. Place the Run Statechart function in the loop.
2. (Optional) Specify the trigger to send by wiring a value to the Trigger input of the Run Statechart function.
 [IMAGE alt='image' src='tip.gif']
**Tip** You can obtain a list of valid triggers by right-clicking the **Trigger** input and selecting either **Create»Control** or **Create»Constant** from the shortcut menu.

The caller VI now is configured to execute the statechart.

#### Creating a Caller VI to Call from C Code

Complete the following steps to create a statechart [caller VI](../lvscconcepts/sc_c_callervi.html) that you can call using C code.

|  | Note To build a build a shared library (DLL) for the project, you must have the Application Builder installed. The LabVIEW Professional Development System includes the Application Builder. If you use the LabVIEW Base Development System or Full Development System, you can purchase the Application Builder separately by visiting the National Instruments Web site. |
| --- | --- |

1. Select File»New Project to display the Project Explorer window.
2. Right-click the My Computer item in the Project Explorer window and select Add»File from the shortcut menu.
3. Navigate to the .lvsc file for the statechart you want to call and click the Add File button to add the statechart to the project.
4. Select File»New VI to create a new VI. LabVIEW adds the new VI to the project.
5. Create a caller VI that links to the statechart.
6. Select File»Save to save the VI.
7. From the Project Explorer window, select File»Save to save the project.
8. Build a shared library (DLL) for the project. Define the caller VI as an exported VI in the shared library.

The DLL has the same functionality as the statechart caller VI. Using C code, obtain the function pointer to the address of the caller VI inside the DLL. You then can use the function pointer to call the caller VI inside the DLL. The caller VI will run the iterations of the statechart until the statechart terminates. The caller VI then returns output data to the C code construct.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_config_color.html language=enus -->
## TOPIC 00089: Customizing the Configuration Color of States and Transitions (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_config_color.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_config_color.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Customizing the Configuration Color of States and Transitions (Statechart Module)

When you configure a state or transition, a wrench icon appears on the state ([IMAGE alt='image' src='noloc_env_state_config_wrench.gif']) or transition ([IMAGE alt='image' src='noloc_env_transition_config_wrench.gif']) in the [Statechart Editor](../lvscconcepts/sc_c_editor.html) window. The state or transition also changes color. You can customize the configuration color for states and transitions. The default configuration color is yellow.

Complete the following steps to change the configuration color of states and transitions.

1. Select Tools»Options in the Statechart Editor window to display the Options dialog box.
2. Select Statechart from the Category list to display the Statechart page.
3. Remove the checkmark from the Use default colors checkbox.
4. Click the Node being configured color box to display the color picker .
5. Select the configuration color you want to use for states and transitions.
 [IMAGE alt='image' src='note.gif']
**Note** Avoid selecting a light blue color similar to the default color of a state you are not configuring. Selecting this color might lead to confusion about which state on the **Statechart Editor** window you are configuring.
6. Click the OK button to implement the changes. When you next configure a state or transition, the state or transition changes color to the configuration color you selected.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_configstate.html language=enus -->
## TOPIC 00090: Configuring a State (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_configstate.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_configstate.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Configuring a State (Statechart Module)

Complete the following steps to configure a [state](../lvsc/sc_state.html).

1. Right-click the border of a state and select Configure State to launch the Configure State dialog box. [IMAGE alt='image' src='note.gif']
**Note** You can open multiple [Configure State](../lvsc/sc_configstate_db.html) and [Configure Transition](../lvsc/sc_config_db.html) dialog boxes simultaneously. If you do so, you may not otherwise edit the [statechart diagram](../lvscconcepts/sc_c_editor.html) until you close all configuration dialog boxes. When you configure a state, a wrench icon appears on the state ([IMAGE alt='image' src='noloc_env_state_config_wrench.gif']) in the **Statechart Editor** window. The state also changes color. You can [customize the configuration color](../lvschowto/sc_h_config_color.html) for states. The default configuration color is yellow.
2. The Reactions list on the left side of this dialog box contains the state actions you can configure. To define the entry or exit action , select the appropriate action from the Reactions list.
 To configure a static reaction , first click the Create button to create a new static reaction. This new static reaction appears as StaticRxn0 , and LabVIEW selects this static reaction automatically.
3. Use the tabs on the right side of this dialog box to define the trigger(s) , guard , and action associated with the action you chose from the Reactions list. You configure these elements by writing LabVIEW block diagram code.
 [IMAGE alt='image' src='note.gif']
**Note** You cannot define triggers or guards for entry or exit actions. Therefore, LabVIEW disables the **Triggers/Groups** and **Guard** pages when you select either the **Entry Action** or **Exit Action** item.
4. Click the OK button to save changes and return to the statechart diagram.

To remove a static reaction, select that reaction from the **Reactions** list and then click the **Delete** button. You cannot delete entry or exit actions. However, you can disable the LabVIEW code that comprises these actions. Place a checkmark in the **Disable?** checkbox on the **Action** page to disable the LabVIEW code that comprises these actions. You also can disable the guard and/or action of a static reaction.

You also can configure a state by [specifying the priority of the transitions that exit the state](sc_h_transprior.html).

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_configt.html language=enus -->
## TOPIC 00091: Configuring Transitions (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_configt.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_configt.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Configuring Transitions (Statechart Module)

After you [create a transition](sc_h_createtrans.html), LabVIEW creates a [transition node](../lvscconcepts/sc_c_trans.html#transition_node) that appears on a segment of that transition. Double-click this transition node to launch the [Configure Transition](../lvsc/sc_config_db.html) dialog box. You use this dialog box to define the [trigger(s)](../lvscconcepts/sc_c_tga.html#trigger), [guard](../lvscconcepts/sc_c_tga.html#guard), and [action](../lvscconcepts/sc_c_tga.html#action) of the transition by writing LabVIEW code.

|  | Note You can open multiple Configure State and Configure Transition dialog boxes simultaneously. If you do so, you may not otherwise edit the statechart diagram until you close all configuration dialog boxes. When you configure a transition, a wrench icon appears on the transition () in the Statechart Editor window. The transition also changes color. You can customize the configuration color for transitions. The default configuration color is yellow. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_createtrans.html language=enus -->
## TOPIC 00092: Creating and Manipulating Transitions (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_createtrans.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_createtrans.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Creating and Manipulating Transitions (Statechart Module)

You can create a [transition](../lvscconcepts/sc_c_trans.html) between a [state](../lvsc/sc_state.html) and any other [statechart object](../lvsc/sc_obj.html) except a [region](../lvsc/sc_region.html). The following sections provide information about creating transitions between objects on a statechart diagram.

|  | Note When you create a transition, the order in which you click the objects establishes the direction of the transition. The first state you click is the state from which the transition originates. The second object you click is the object at which the transition terminates. |
| --- | --- |

#### Creating a Transition between Two States

You can create a transition between two states that exist in the same statechart. These states can exist in any region. Complete the following steps to create a transition between two states.

1. Place two states on the statechart diagram.
2. Move the cursor over the border of the first state until the cursor changes to the Wiring tool .
3. Click the border to begin placing the transition.
4. Move the cursor over the border of the second state.
5. Click the border again to complete the transition. Notice the transition node that appears in between the transition segments.
6. Configure the transition .

#### Creating a Transition between a State and a Pseudostate or Connector

To create a transition between a state and a [pseudostate](../lvscconcepts/sc_c_pseudocon.html), move the cursor over the center of the pseudostate on the statechart diagram. After the cursor changes to the Wiring tool, click the pseudostate to initiate or terminate the transition.

To create a transition between a state and a [connector](../lvscconcepts/sc_c_pseudocon.html), move the cursor over the gray area of the connector on the statechart diagram. After the cursor changes to the Wiring tool, click to initiate or terminate the transition.

#### Duplicating a Transition Node

To duplicate a transition node, press the <Ctrl> key and drag a transition node to another location on the statechart diagram to duplicate all triggers, guards, and actions of the original transition node. Then, connect the segments of the duplicated node to other states or pseudostates.

|  | Note If you configure a trigger for a transition node, duplicate that node, and then create a transition from an Initial pseudostate to that node, errors appear when you generate code for that statechart. These errors appear because transitions that leave an Initial pseudostate cannot have triggers. Complete the following steps to correct these errors. |
| --- | --- |

1. Double-click the transition node that exits the Initial pseudostate.
2. Click the OK button to save changes and return to the statechart diagram to remove all triggers from the node.

#### Reversing Transition Direction

Recall that transitions are unidirectional. In some cases you might create a transition, define some logic for that transition, and then realize the transition needs to go the other way. You can reverse the direction of a transition without deleting and re-creating the transition node, which means that reversing the direction of a transition maintains any transition logic you configure.

For example, consider the following figure:

[IMAGE alt='image' src='reversetrans_before.gif']

Complete the following steps to reverse the direction of this transition.

1. Use the Positioning tool to click either segment of the transition.
2. Press the <Delete> key to delete the segment.
3. Delete the other transition segment. The transition node now is unconnected to either state.
4. Right-click the transition node and select Reverse . The transition node now points the other way.
5. Using the Wiring tool, move the cursor over the triangular end of the transition node until LabVIEW displays a tip strip that reads Segment Out .
6. Click the head to initiate a transition segment.
7. Create a transition segment to the border of State 1. The statechart diagram now resembles the following figure:
 [IMAGE alt='image' src='reversetrans_during.gif'] 
 [IMAGE alt='image' src='note.gif']
**Note** Recall that the order in which you click the objects establishes the order of the transition. Therefore, you cannot create this segment by clicking State 1 and then the head of the transition node. The LabVIEW Statechart Module interprets this sequence as you attempting to create a transition segment to an object that does not allow any incoming segments.
8. Create a transition segment from State 2 to the other end of the transition node.

The transition now goes from State 2 to State 1 instead of from State 1 to State 2. The statechart diagram now resembles the following figure:

[IMAGE alt='image' src='reversetrans_after.gif']

Notice the transition node itself remains unchanged except for the visual appearance. Reversing transition direction preserves any logic you had configured for this node.

#### Manipulating a Transition Node

You can adjust the placement and orientation of transition nodes by right-clicking this node and selecting the appropriate option.

|  | Note Manipulating a transition node does not affect the direction of the transition itself. The manipulation is for visual purposes only. |
| --- | --- |

Select the **Rotate** option to rotate the node 90 degrees. Rotating a transition node is useful if you want to move the transition node from a vertical transition segment to a horizontal transition segment, or vice-versa.

Select the **Reverse** option to reverse the beginning and end of the transition node. If the end of the node faces right and you select this option, the end of the node faces left.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_createtrig.html language=enus -->
## TOPIC 00093: Creating Triggers and Groups (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_createtrig.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_createtrig.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Creating Triggers and Groups (Statechart Module)

Complete the following steps to create a [trigger](../lvscconcepts/sc_c_tga.html#trigger).

1. Open the .lvsc file that contains the statechart for which you want to create triggers.
2. Display the Project Explorer window for this .lvsc file.
3. Double-click the Edit Triggers and Groups item to launch the Edit Triggers and Groups dialog box.
 [IMAGE alt='image' src='note.gif']
**Note** You also can access this dialog box by clicking the **Edit Triggers and Groups** button in either the [Configure Transition](../lvsc/sc_config_db.html) or [Configure State](../lvsc/sc_configstate_db.html) dialog box.
4. Click the Create Trigger button to create a new trigger. The Triggers and Groups list updates to display this new trigger.
5. Enter a name for the trigger and press the <Enter> key to accept the name.
6. Click the OK button to save changes and close this dialog box.

You now can configure a [transition](../lvscconcepts/sc_c_trans.html) or [static reaction](../lvscconcepts/sc_c_staticrxn.html) to react to this trigger.

To rename a trigger, select the trigger, press the <F2> key, and enter the new name. Press the <Enter> key to accept the name.

#### Combining Triggers into a Group

You also can combine triggers into [groups](../lvscconcepts/sc_c_tga.html#trigger). Complete the following steps to combine triggers into groups.

1. In the Edit Triggers and Groups dialog box, click the Create Group button. The Triggers and Groups list updates to display this new group.
2. Select this new group from the Group Composition pull-down menu on the right of this dialog box. You also can double-click a group name in the Triggers and Groups list.
3. Select a trigger or group from the Triggers and Groups list. To select multiple items, press the <Ctrl> key as you select triggers and/or groups.
4. Click the Add button to add the selection to the current group.
5. When you are finished, click the OK button to save changes and close this dialog box.

To remove items from a group, select the item(s) in the **Group Composition** list and click the **Remove** button.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_dbgexechl.html language=enus -->
## TOPIC 00094: Highlighting Statechart Execution (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_dbgexechl.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_dbgexechl.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Highlighting Statechart Execution (Statechart Module)

Complete the following steps to highlight the execution of a statechart.

1. Run the caller VI .
2. Right-click the Run Statechart function and select Debug Statechart . The statechart diagram appears in debugging mode, which means you cannot edit the diagram.
 [IMAGE alt='image' src='note.gif']
**Note** If you do not see the **Debug Statechart** option, you might have [disabled statechart debugging](sc_h_disabledebug.html). You must re-enable debugging and re-generate the code before proceeding.
3. Click the Highlight Execution button , which is located on the statechart diagram toolbar. Notice that with execution highlighting, LabVIEW highlights the appropriate transitions and states as the statechart receives triggers from the caller VI and moves from one state to another.
 During execution highlighting, LabVIEW can display one of the following icons in the upper-left corner of a state.
 A yellow square indicates that the state is executing an entry action .
 A green triangle indicates that the state is executing a static reaction .
 A red circle indicates that the state is executing an exit action .
4. Click the Highlight Execution button at any time to disable execution highlighting.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_debugsc.html language=enus -->
## TOPIC 00095: Debugging Statecharts (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_debugsc.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_debugsc.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Debugging Statecharts (Statechart Module)

To debug a statechart for which you have generated code, right-click a [Run Statechart](../lvsc/sc_runsc.html) function and select **Debug Statechart**. You only can debug a statechart when you have [linked the Run Statechart function to a statechart](../lvschowto/sc_h_linksc.html).

|  | Note If you do not see the Debug Statechart option, you might have disabled statechart debugging. You must re-enable debugging and re-generate the code before proceeding. |
| --- | --- |

Debugging a statechart is available for statecharts that execute on the desktop, on a LabVIEW real-time target, or on a LabVIEW FPGA target running on the host computer.

While debugging a statechart, you can perform the following actions:

- Set breakpoints .
- Highlight statechart execution .
- Single-step through a statechart .
- Watch statechart data .

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_defineobj.html language=enus -->
## TOPIC 00096: Placing States, Regions, Forks, Joins, and Junctions on a Statechart Diagram (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_defineobj.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_defineobj.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Placing States, Regions, Forks, Joins, and Junctions on a Statechart Diagram (Statechart Module)

Complete the following steps to place a [state](../lvsc/sc_state.html), [region](../lvsc/sc_region.html), [Fork](../lvsc/sc_fork.html), [Join](../lvsc/sc_join.html), or [Junction](../lvsc/sc_junction.html) the statechart diagram.

1. Display the Statechart Editor window .
2. Select the object on the Statechart Development palette.
3. Move the cursor over the statechart diagram.
4. Click to place the top left corner of the object.
5. Drag the cursor diagonally to establish the size of the object.
6. Click again to place the object on the statechart diagram.

You can resize these objects on the statechart diagram.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_disabledebug.html language=enus -->
## TOPIC 00097: Disabling Debugging (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_disabledebug.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_disabledebug.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Disabling Debugging (Statechart Module)

By default, statechart debugging is enabled, which means you can [debug a statechart](sc_h_debugsc.html). However, in some situations, you might want to disable debugging. Disabling debugging improves the efficiency of the generated [Run Statechart](../lvsc/sc_runsc.html) function that represents the statechart. Disabling debugging also reduces the code size of a statechart that executes on a real-time target.

Complete the following steps to disable statechart debugging.

1. Display the Project Explorer window for the statechart you want to debug.
2. Right-click the .lvsc project item and select Properties .
3. Click Statechart Code Generation item in the Category list to display the Statechart Code Generation page.
4. Select Disabled from the Debugging pull-down menu.
5. Click the OK button to save changes.
6. Double-click the Diagram.vi project item.
7. Generate code for the statechart diagram .

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_displaydata.html language=enus -->
## TOPIC 00098: Watching Statechart Data (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_displaydata.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_displaydata.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Watching Statechart Data (Statechart Module)

You can use the Statechart Data Display tool to watch [statechart data](../lvscconcepts/sc_c_iodata.html) while debugging that statechart. This behavior is similar to a LabVIEW [probe](/csh?topicname=lvhowto/using_the_probe_tool.html) except that the Statechart Data Display shows all statechart data at once, whereas a probe shows only the value of a single wire.

Complete the following steps to use this tool:

1. Run the caller VI .
2. Right-click the Run Statechart function and select Debug Statechart . The statechart diagram appears in debugging mode, which means you cannot edit the diagram.
 [IMAGE alt='image' src='note.gif']
**Note** If you do not see the **Debug Statechart** option, you might have [disabled statechart debugging](sc_h_disabledebug.html). You must re-enable debugging and re-generate the code before proceeding.
3. Click the Open Statechart Data Display button , which is located on the toolbar of this window. LabVIEW displays a window that shows the StateData and Outputs clusters that contain statechart data. Each cluster contains indicators that show the current value of that data type. These indicators update after a statechart iteration changes one of the indicator values.
 This window also contains the InternalQueue cluster, which shows the values of the internal trigger queue .

|  | Note The Statechart Debugging window also contains the Open Statechart Custom Data Display button . This button opens a data display that you can customize. You customize this data display by opening the Project Explorer window for the .lvsc file and double-clicking the CustomDataDisplay.vi item. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_dispsc.html language=enus -->
## TOPIC 00099: Displaying the Statechart Editor Window (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_dispsc.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_dispsc.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Displaying the Statechart Editor Window (Statechart Module)

The [Statechart Editor](../lvscconcepts/sc_c_editor.html) window displays the statechart diagram on which you place [Statechart Development](../lvsc/sc_obj.html). Complete the following steps to display this window.

1. Create a new statechart or open an existing .lvsc file.
2. Display the Project Explorer window associated with this statechart.
3. Double-click the Diagram.vi item to open the Statechart Editor window.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_findtrigg.html language=enus -->
## TOPIC 00100: Finding All Instances of Triggers or Groups (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_findtrigg.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_findtrigg.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Finding All Instances of Triggers or Groups (Statechart Module)

You can find all instances of a [trigger](../lvscconcepts/sc_c_tga.html#trigger) or [group](../lvschowto/sc_h_createtrig.html#creategroups) to determine which [static reactions](../lvscconcepts/sc_c_staticrxn.html) and [transitions](../lvscconcepts/sc_c_trans.html) react to the trigger or group.

Complete the following steps to find all instances of a trigger or group in a [statechart diagram](../lvscconcepts/sc_c_editor.html).

1. Right-click a state and select Configure State from the shortcut menu to display the Configure State dialog box, or right-click a transition and select Configure transition from the shortcut menu to display the Configure Transition dialog box.
2. On the Triggers/Groups page, right-click a trigger or group in the Triggers list and select Find Trigger/Group from the shortcut menu to display the Search Results window. The Search Results window displays a list of the static reactions and transitions that react to the trigger or group.
 [IMAGE alt='image' src='note.gif']
**Note** The **Search Results** window appears only if LabVIEW finds more than one object during a search. If LabVIEW finds only one object, LabVIEW highlights either the state corresponding to the static reaction or the transition in the [Statechart Editor](../lvscconcepts/sc_c_editor.html) window.
3. Double-click an item in the Search Results window to highlight the item in the Statechart Editor window.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_firststate.html language=enus -->
## TOPIC 00101: Specifying the State that a Region Executes First (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_firststate.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_firststate.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Specifying the State that a Region Executes First (Statechart Module)

Complete the following steps to specify the [state](../lvsc/sc_state.html) that a [region](../lvsc/sc_region.html) executes first.

1. Place an Initial 
 pseudostate on the statechart diagram.
 [IMAGE alt='image' src='add.gif'] Add
2. Create a transition from this pseudostate to the state that you want to execute first.
3. (Optional) Define any actions for this transition . You cannot define a trigger or guard for this transition.

For example, consider the following figure:

[IMAGE alt='image' src='initial.gif']

Each region must have an Initial pseudostate. In the previous figure, the statechart executes State 1 first. If the statechart takes the transition into State 2, the statechart executes State 3 first.

|  | Note The Terminal pseudostate specifies the state that can terminate the enclosing region. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_fpdiagram.html language=enus -->
## TOPIC 00102: Displaying Statechart Diagrams on the Front Panel of a Caller VI (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_fpdiagram.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_fpdiagram.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Displaying Statechart Diagrams on the Front Panel of a Caller VI (Statechart Module)

You can display [statechart diagrams](../lvscconcepts/sc_c_editor.html) on the front panel of a [caller VI](../lvschowto/sc_h_callsc.html). The **Statechart Diagram Display** option of the **Configure Statechart Run Node** dialog box specifies the number of statechart diagrams to display on the front panel of the caller VI in a **Diagram Display** picture control. Right-click a [Run Statechart](../lvsc/sc_runsc.html) function and select **Configure** from the shortcut menu to display the **Configure Statechart Run Node** dialog box. You also can double-click the Run Statechart function to display the **Configure Statechart Run Node** dialog box.

You can choose to display one statechart diagram, *n* statechart diagrams, or all statechart diagrams. You can display multiple diagrams only if the statechart diagram contains [superstates](../lvscconcepts/sc_c_hierarchy.html) that you [view as a subdiagram](../lvschowto/sc_h_subdiag.html). The front panel of the caller VI displays the contents of the superstate.

Complete the following steps to display one statechart diagram on the front panel of a caller VI.

1. Open a caller VI that contains a Run Statechart function that links to a statechart.
2. Press the <Ctrl-E> keys to display the block diagram of the caller VI.
3. Locate the Run Statechart function .
4. Right-click the Run Statechart function and select Configure from the shortcut menu to display the Configure Statechart Run Node dialog box. [IMAGE alt='image' src='note.gif']
**Note** You also can display the **Configure Statechart Run Node** dialog box by double-clicking the Run Statechart function.
5. Place a checkmark in the Show Terminal? checkbox next to the Statechart Diagram Display option. The Statechart Diagram Display option specifies to display a statechart diagram(s) in a Diagram Display picture control on the front panel of the caller VI. You can choose to display one statechart diagram, n statechart diagrams, or all statechart diagrams.
6. Select Display one diagram from the Statechart Diagram Display pull-down menu. Selecting Display one diagram adds a Diagram Display Index input and a Diagram Display output to the Run Statechart function.
7. Click the OK button to apply the changes to the Run Statechart function and close the Configure Statechart Run Node dialog box.
8. Right-click the Diagram Display Index input of the Run Statechart function and select Create»Control from the shortcut menu. The Diagram Display Index control specifies which statechart diagram the front panel of the caller VI displays.
9. Right-click the Diagram Display output of the Run Statechart function and select Create»Indicator from the shortcut menu. The Diagram Display indicator displays the statechart diagram on the front panel of the caller VI.
10. Press the <Ctrl-E> keys to display the front panel of the caller VI. Notice the Diagram Display Index control and the Diagram Display indicator on the front panel.
11. (Optional) Specify the number of the statechart diagram in the Diagram Display Index that you want the Diagram Display indicator to display. LabVIEW assigns the top-level statechart diagram a value of 0 . LabVIEW assigns increasing values in increments of one to all superstates in the statechart diagram in a random order. The default value for the Diagram Display Index is 0 .
12. Run the caller VI once to display the statechart diagram in the Diagram Display indicator.
13. Resize the Diagram Display indicator as necessary to view the entire statechart diagram.

The statechart diagram display shows the statechart when you run the caller VI. The statechart diagram display also highlights the states that are active at the end of each iteration of the statechart.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_gencode.html language=enus -->
## TOPIC 00103: Generating Code for a Statechart (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_gencode.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_gencode.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Generating Code for a Statechart (Statechart Module)

After you build a statechart, click the **Generate Code** button [IMAGE alt='image' src='sc_generate_code.gif'], which is located on the toolbar of the [Statechart Editor](../lvscconcepts/sc_c_editor.html) window to generate the code that corresponds to the statechart. You then use a [Run Statechart](../lvsc/sc_runsc.html) function to execute this code in a [VI](../lvscconcepts/sc_c_callervi.html).

|  | Note If you add code to a previously empty guard or action, or if you delete all code from a guard or action, you must re-generate code for the statechart. If you modify an existing, non-empty guard or action, you do not need to re-generate code for the statechart. |
| --- | --- |

If this button appears broken [IMAGE alt='image' src='sc_broken.gif'], the statechart code has errors. Clicking this button displays the errors.

If this button appears dimmed [IMAGE alt='image' src='sc_gencode_dim.gif'], the generated code already is usable. You do not need to generate code for the statechart.

|  | Note You also can generate code for the statechart by right-clicking the .lvsc file in the Project Explorer window and selecting Generate Code from the shortcut menu. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_gendoc.html language=enus -->
## TOPIC 00104: Generating Statechart Documentation (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_gendoc.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_gendoc.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Generating Statechart Documentation (Statechart Module)

You can [generate documentation](../lvscconcepts/sc_c_gendocfile.html) that describes all components, including [states](../lvsc/sc_state.html), [pseudostates](../lvscconcepts/sc_c_pseudocon.html), [connectors](../lvscconcepts/sc_c_pseudocon.html), [regions](../lvsc/sc_region.html), and [transitions](../lvscconcepts/sc_c_trans.html), of a completed statechart. Complete the following steps to generate statechart documentation.

1. Open the Project Explorer window for the statechart for which you want to generate documentation.
2. Double-click the Diagram.vi item to open the Statechart Editor window.
3. Select File»Generate Documentation .
 [IMAGE alt='image' src='note.gif']
**Note** You also can right-click the .lvsc item, or statechart library, in the **Project Explorer** window and select **Generate Documentation** from the shortcut menu.
4. In the prompt that appears, specify whether you want to open the statechart documentation in a Web browser after LabVIEW generates the documentation.
5. In the file dialog box that appears, specify the location to which you want to save the statechart documentation.
6. Click the OK button. LabVIEW generates an XML file and a folder of support files in the location you specified. If you selected to view the documentation in a Web browser, LabVIEW displays the XML file in the default Web browser.

You also can use the [Generate Documentation](/csh?topicname=lvprop/statechartlibrary_generate_documentation.html) method to generate statechart documentation programmatically.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_gs.html language=enus -->
## TOPIC 00105: Tutorial: Creating an Asynchronous Statechart with the LabVIEW Statechart Module

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_gs.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_gs.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Tutorial: Creating an Asynchronous Statechart with the LabVIEW Statechart Module

This tutorial introduces you to creating an asynchronous statechart. This tutorial is divided into the following six parts:

- In Part 1 , you learn to add a state to an existing statechart, see how the statechart moves between states , and examine how LabVIEW executes statecharts.
- In Part 2 , you learn to create a new statechart.
- In Part 3 , you learn to define the data types that a statechart can use.
- In Part 4 , you learn to place substates within a state. You also learn some debugging techniques.
- In Part 5 , you learn to add substates that the statechart executes concurrently .
- In Part 6 , you learn to split and merge transition segments.
- In the Statechart Objects in a Statechart Diagram topic, you can view the statechart diagram that you complete in this tutorial with links to each of the objects in the diagram.

|  | Note Refer to the labview\\examples\\Statechart\\Tutorial\\Asynchronous directory for completed versions of the statecharts you create in this tutorial. |
| --- | --- |

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_gs_1.html language=enus -->
## TOPIC 00106: Statechart Module Tutorial Part 1: Modifying a Statechart

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_gs_1.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_gs_1.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Module Tutorial Part 1: Modifying a Statechart

In Part 1 of this tutorial, you examine how LabVIEW executes a statechart. You also add a [state](../lvsc/sc_state.html) to an existing statechart, create [transitions](../lvscconcepts/sc_c_trans.html) to and from this state, create a [trigger](../lvscconcepts/sc_c_tga.html#trigger) that causes the statechart to take a transition, and debug the statechart.

|  | You can complete these exercises in approximately 60 minutes. |
| --- | --- |

|  | Note Refer to the labview\\examples\\Statechart\\Tutorial\\Asynchronous\\Getting Started 1.lvsc for a completed version of the statechart you create in this part of the tutorial. |
| --- | --- |

#### Running the Caller VI

The first step is opening and running the [caller VI](../lvscconcepts/sc_c_callervi.html), which is the VI that executes the statechart. Complete the following steps to open and run this VI.

1. Launch LabVIEW and display the Getting Started window.
2. Select File»Open .
3. Browse to the labview\examples\Statechart\Tutorial\Asynchronous directory and double-click Getting Started Caller VI.vi .
4. Display the front panel of the VI and click the Run button , located on the LabVIEW toolbar.
5. Notice the Current Activity indicator displays Menu .
6. Click the Play front panel button. Notice the Current Activity indicator now displays Playing .
7. Click the Menu front panel button and notice the Current Activity indicator displays Menu again.
8. Click the Pause front panel button. Notice that nothing happens to the Current Activity indicator.
 Nothing happens because the statechart this VI calls has only two states: Menu and Play. These states are configured to update the Current Activity indicator after you click the appropriate button. The statechart does not have a state that handles the Pause front panel button. You will add this state to the statechart.
9. Click the Stop front panel button. The Current Activity indicator displays Stopped , and the VI stops executing.
 [IMAGE alt='image' src='note.gif']
**Note** The statechart does not have a Stop state. The statechart is configured to update the **Current Activity** indicator before the statechart terminates.

#### Examining the Caller VI

The next step is examining the caller VI. Press the <Ctrl-E> keys to view the block diagram of this VI.

This caller VI has two loops because the statechart is [asynchronous](../lvscconcepts/sc_c_syncasync.html). Asynchronous statecharts react to triggers that another thread or VI sends. In this caller VI, one [While Loop](/csh?topicname=glang/while_loop.html) sends triggers to the statechart, and the other While Loop executes the statechart after receiving a trigger. These loops execute in parallel. You also can place each loop in a separate VI.

#### Launching the Statechart Editor Window

The next step is launching the [Statechart Editor](../lvscconcepts/sc_c_editor.html) window. This window displays the statechart diagram that you executed in the *Running the Caller VI* section of this tutorial. The statechart diagram is where you place the statechart objects that comprise a statechart.

Complete the following steps to launch the Statechart Editor window.

1. Locate the Run Statechart function .
2. Right-click this function and select View»Statechart Diagram to launch the Statechart Editor window that contains the statechart diagram.

#### Examining the Statechart

The statechart diagram resembles the following figure:

[IMAGE alt='image' src='gsg1_1.gif']

When you ran the caller VI, the statechart located the [Initial](../lvsc/sc_initial.html)
 [pseudostate](../lvscconcepts/sc_c_pseudocon.html). The transition (1) that exits this pseudostate specifies which state the statechart enters first. Therefore, the statechart executed the Menu state (2) first. The statechart then waited for the caller VI to send a trigger, which happened when you clicked the **Play** front panel button. When you clicked this button, the caller VI sent a trigger to the statechart. This trigger caused the statechart to take the transition (3) to the Play state and wait for another trigger, which you sent by clicking the **Menu** front panel button. Each state is configured to update the text of the **Current Activity** indicator.

|  | Note Because transitions go in only one direction, notice that the transition that enters the Play state is separate from the transition that exits the Play state. |
| --- | --- |

As the previous figure shows, there is no Pause state. Therefore, when you clicked the **Pause** front panel button, nothing happened. However, when you clicked the **Stop** front panel button, the statechart took the transition (4) to the [Terminal](../lvsc/sc_terminal.html) pseudostate, which halted the execution of the statechart.

The arrow-shaped objects in the middle of each transition are the [transition nodes](../lvscconcepts/sc_c_trans.html#transition_node). The following figure shows a transition node.

[IMAGE alt='image' src='transnodeblue.gif']

The blue rectangles on these nodes indicate certain information about the transition. You will create and configure a transition later in this part of the tutorial.

#### Saving a Backup Copy of the Statechart

During this part of the tutorial, you modify the example statechart that installs with the LabVIEW Statechart Module. You can save a backup copy of this example in case you need to return to the original form of this example. This step is optional.

Complete the following steps to save a backup copy of this statechart.

1. In the caller VI, right-click the Run Statechart function and select View»Statechart to launch the Project Explorer window that contains the .lvsc file.
2. Right-click the Getting Started 1.lvsc file in the Project Explorer window and select Save»Save As to launch the Save As dialog box.
3. Ensure the Copy option is selected.
4. Enter a descriptive name in the Name for copy of library file text box.
5. Click the Continue button. LabVIEW prompts you for a location to save the .lvsc file.
6. Browse to a convenient directory and click the Current Folder button. LabVIEW creates a copy of the .lvsc file and saves this copy in the location you specified. The original statechart remains in memory.

#### Adding a State to the Statechart

The next step is creating the state that reacts to the **Pause** front panel button. Complete the following steps to add this state to the statechart.

1. Display the Statechart Editor window.
2. If you do not see the Functions palette, select View»Functions Palette to display this palette.
3. On this palette, select Statechart»Statechart Development to display the Statechart Development palette.
4. Click the State icon.
5. Move the cursor over the statechart diagram. Click to place the top left corner of the state, drag the cursor diagonally to establish the size of the state, and click again to place the state on the statechart diagram.
6. Notice the state is labeled State . Double-click this label to enable text editing and enter Pause as the new label.
7. Move the Pause state to the right of the Play state as shown in the following figure:
 [IMAGE alt='image' src='gsg1_2.gif']
8. Save the statechart by selecting File»Save or by pressing the <Ctrl-S> keys.

#### Creating a Transition from the Play State to the Pause State

The next step is defining when the statechart can enter and exit the Pause state. You accomplish this step by creating transitions to and from this state. Complete the following steps to create a transition from the Play state to the Pause state.

1. Move the cursor over the right border of the Play state until the inner border blinks and the cursor changes to the Wiring tool .
 
 [IMAGE alt='image' src='note.gif']
**Note** If you do not see the Wiring tool, you might have disabled [automatic tool selection](/csh?topicname=lvhowto/selecting_a_tool.html). Either enable this feature or press the <Tab> key until the Wiring tool appears.
2. Click the border to initiate a transition. Notice that when you move the cursor now, a dotted line follows the cursor to indicate the placement of the transition.
3. Move the cursor over the left border of the Pause state. Notice a gray box appears under the cursor.
4. Click the border. LabVIEW creates a transition between the two states.
 
 [IMAGE alt='image' src='note.gif']
**Note** If you move the cursor inside the state border before clicking it, LabVIEW attempts to create a transition into the state instead of to the state. In this situation, press the <Esc> key to remove the erroneous transition.

The statechart diagram now resembles the following figure:

[IMAGE alt='image' src='gsg1_3.gif']

#### Creating a Trigger and Configuring the Transition

The next step is specifying that the statechart takes the transition only after receiving a specific event, also called a trigger. By default, transitions are configured to react to the NULL trigger. However, the caller VI that executes this statechart does not send the NULL trigger. Therefore, you must configure this transition to react to a different trigger.

Notice the transition node. You use this node to define the trigger(s) that cause the statechart to take a transition. Complete the following steps to configure this transition.

1. Double-click the transition node between the Play and Pause states to launch the Configure Transition dialog box. You use this dialog box to configure transitions.
 [IMAGE alt='image' src='note.gif']
**Note** When you configure a transition, a wrench icon appears on the transition ([IMAGE alt='image' src='noloc_env_transition_config_wrench.gif']) in the **Statechart Editor** window. The transition also changes color. You can [customize the configuration color](../lvschowto/sc_h_config_color.html) for transitions. The default configuration color is yellow. 
 The first tab in this dialog box is the Triggers/Groups tab. This tab contains a list that shows the Play , Menu , and Stop triggers. These triggers are the valid triggers that the caller VI can send to the statechart. Also notice the NULL trigger. The LabVIEW Statechart Module provides this default trigger for every statechart.
2. Click the Edit Triggers and Groups button to launch the Edit Triggers and Groups dialog box. You use this dialog box to create and modify triggers.
3. Click the Create Trigger button to add a new trigger, which appears in the Triggers and Groups list.
4. Enter Pause as the new trigger name.
5. Click the OK button to save changes and return to the Configure Transition dialog box. Notice the new trigger appears in the Triggers/Groups list.
6. In the Triggers/Groups list, place a checkmark in the Pause checkbox to specify that this trigger causes the statechart to take the transition.
7. Remove the checkmark from the NULL checkbox.
8. Click the OK button to save changes and return to the statechart diagram.

Notice the blue rectangle that appears on the transition node. This rectangle indicates that the transition has a specified trigger that is not NULL.

Recall that transitions are unidirectional. As the previous figure shows, the statechart cannot move from the Pause state to the Play state. Complete the following steps to address this limitation.

1. Create a transition from the Pause state to the Play state.
2. Configure this transition to react to the existing Play trigger. Remember to deselect the NULL trigger.
3. Save the statechart.

The statechart diagram now resembles the following figure:

[IMAGE alt='image' src='gsg1_4.gif']

#### Viewing and Changing the Transition Label

Each transition node has a built-in label. To see this label, right-click the second transition node you created and select **Visible Items»Label** from the shortcut menu. LabVIEW displays Transition as the label for this transition. You can double-click this label to change the label. You also can use the **Label** text box in the **Configure Transition** dialog box.

#### Duplicating a Transition Node

Notice that the statechart cannot move from the Pause state to the Terminal pseudostate. You can create this transition by duplicating the transition node that connects the Menu state to the Terminal pseudostate. Complete the following steps to duplicate this transition.

1. Press the <Ctrl> key and click and drag this transition node.
2. Move this node under the Pause state.
3. Click the border of the Pause state to initiate a transition segment.
4. Move the cursor over the incoming tunnel of the transition node until LabVIEW displays a tip strip that reads Segment In .
5. Click again to complete the transition segment.
6. Create a transition segment from the other side of this node to the Terminal pseudostate.
7. (Optional) Right-click the transition node and select either Rotate or Reverse to ensure the node faces the proper direction.
8. Save the statechart.

The statechart now resembles the following figure:

[IMAGE alt='image' src='gsg1_5.gif']

#### Configuring the Pause State

The next step is configuring the Pause state to update the **Current Activity** front panel indicator appropriately. You accomplish this task by defining an [entry action](../lvscconcepts/sc_c_entryexit.html) for this state. An entry action is LabVIEW code that the statechart executes immediately after entering a state.

Complete the following steps to configure the Pause state to update this indicator.

1. Double-click the border of the Pause state to launch the Configure State dialog box.
 
 [IMAGE alt='image' src='note.gif']
**Note** When you configure a state, a wrench icon appears on the state ([IMAGE alt='image' src='noloc_env_state_config_wrench.gif']) in the **Statechart Editor** window. The state also changes color. You can [customize the configuration color](../lvschowto/sc_h_config_color.html) for states. The default configuration color is yellow. 
 The left side of this dialog box contains the Reactions list. The right side of this dialog box displays several tabs that correspond to the item you select from the Reactions list. By default, the dialog box displays the Entry Action item in the Reactions list. This selection specifies that you want to define the entry action of the state.
 The tabs on the right correspond to the selected item in the Reactions list. By default, the Action tab is selected. LabVIEW displays the block diagram you use to define the entry action.
2. Notice the Outputs cluster element on the right side of this block diagram. Click this cluster element and select Outputs»Current Activity from the shortcut menu. This element now displays Outputs.Current Activity . You now can use this element to write to the value of this indicator.
3. Move the cursor over the input of this cluster element until the cursor changes to the Wiring tool.
4. Right-click the input and select Create»Constant from the shortcut menu. LabVIEW places a string constant on the block diagram.
 [IMAGE alt='image' src='note.gif']
**Note** You cannot access the front panel window for this block diagram. Therefore, National Instruments recommends using block diagram constants instead of front panel controls.
5. Double-click inside this constant and enter Paused as the value of the constant. The block diagram now resembles the following figure:
 [IMAGE alt='image' src='gsg1_6.gif'] 
 This code means that, every time the statechart enters the Pause state, the statechart changes the Current Activity indicator to read Paused .
6. Click the OK button to save changes and return to the statechart diagram.
7. Save the statechart.

#### Generating Code for the Statechart

The next step is generating code for the statechart. You then call this code by executing the Run Statechart function, which you place on the block diagram of the [caller VI](../lvscconcepts/sc_c_callervi.html). Complete the following steps to generate code for this statechart.

1. Display the Statechart Editor window.
2. Click the Generate Code button , which is located on the toolbar of this window.

|  | Note You also can generate code by right-clicking the .lvsc file in the Project Explorer window and selecting Generate Code from the shortcut menu. |
| --- | --- |

#### Configuring the Caller VI to Communicate with the Pause State

The next step is configuring the caller VI to send the Pause trigger to the statechart when you click the **Pause** front panel button. Complete the following steps to configure this behavior.

1. Display the block diagram of the caller VI.
2. Select the Pause event case of the Event structure . Notice the blue output tunnel on the right side of this structure. A wire connects this tunnel to the Trigger input of the Send External Trigger function.
3. Right-click this output tunnel and select Create»Constant from the shortcut menu. LabVIEW creates an enumerated type constant that contains the triggers you can send to this statechart.
4. Select Pause as the value of this constant.
5. Select File»Save As to launch the Save As dialog box.
6. Ensure the Substitute copy for original option is selected and click the Continue button.
7. Enter My Getting Started Caller VI.vi as the new name and click the OK button. LabVIEW saves a copy of this caller VI and opens this copy in memory.

This case of the Event structure now resembles the following figure:

[IMAGE alt='image' src='gsg1_7.gif']

In the previous figure, clicking the **Pause** front panel button causes the Event structure to send the Pause trigger, which you [created](#configtrans), to the Send External Trigger function. This function sends the Pause trigger to the external trigger queue of the statechart, which then reacts to the trigger by moving to the appropriate state.

|  | Note Notice that you did not have to replace the Run Statechart or Send External Trigger functions on the block diagram. After you generate code for the statechart, LabVIEW updates this function automatically. LabVIEW also updates the Trigger enumerated type constant with the Pause trigger you created. |
| --- | --- |

#### Running the Caller VI Again

The next step is running the caller VI again and seeing the behavior you defined for the **Pause** front panel button. Complete the following steps to run this VI and test the new state.

1. Display the front panel of the caller VI.
2. Press the <Ctrl-R> keys to run the VI.
3. Click the Play front panel button to move to the Play state.
4. Click the Pause front panel button. Notice Current Activity indicator displays Paused . This behavior is what you configured during this part of the tutorial.
5. Click the Menu front panel button. Notice the statechart does nothing. You have not defined a transition from the Pause state to the Menu state. You can move to the Menu state from only the Play state.

#### Highlighting Statechart Execution

The next step is highlighting the execution of the statechart. Complete the following steps to highlight the execution of the statechart.

1. While the caller VI is running, display the block diagram of the caller VI.
2. Right-click the Run Statechart function and select Debug Statechart to display the statechart in the Statechart Debugging window.
3. Click the Highlight Execution button , located on the toolbar of the Statechart Debugging window, to enable statechart execution highlighting.
4. Display the front panel of the caller VI and click the Play front panel button. Watch LabVIEW highlight the transition from the Pause state to the Play state.
5. Click the Menu front panel button and watch the statechart move to the Menu state.
6. Click the Stop front panel button. Watch the statechart move to the Terminal pseudostate and stop the execution of the statechart.
7. Close the Statechart Debugging window and the caller VI.

#### Summary

In this tutorial, you learned about the following tasks:

- Defining a state.
- Creating transitions.
- Creating and specifying triggers.
- Defining the entry action of a state.
- Generating code for a statechart.
- Calling a statechart from a VI.
- Highlighting the execution of a statechart.

#### Where to Go from Here

In [Part 2](sc_h_gs_2.html) of this tutorial, you create and configure a new statechart.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_gs_2.html language=enus -->
## TOPIC 00107: Statechart Module Tutorial Part 2: Building a Statechart

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_gs_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_gs_2.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Module Tutorial Part 2: Building a Statechart

In [Part 1](sc_h_gs_1.html) of this tutorial, you learned the basics of modifying a statechart. In Part 2 of this tutorial, you recreate part of statechart that you modified in Part 1. You finish recreating this statechart in Part 3.

|  | You can complete these exercises in approximately 45 minutes. |
| --- | --- |

|  | Note Refer to the labview\\examples\\Statechart\\Tutorial\\Asynchronous\\Getting Started 2.lvsc for a completed version of the statechart you create in this part of the tutorial. |
| --- | --- |

#### Creating and Configuring the Statechart

Complete the following steps to create and configure the statechart.

1. Launch LabVIEW and display the Getting Started window.
2. Select File»New to launch the New dialog box.
3. Select Other Files»Statechart from the Create New tree.
4. Click the OK button. LabVIEW prompts you to save the statechart.
5. Enter My Getting Started Statechart.lvsc and save the statechart in a convenient location on disk.
 LabVIEW displays a Project Explorer window that contains the necessary support files under the My Getting Started Statechart.lvsc project item. This project item represents the .lvsc file in which LabVIEW stores statechart information.
6. Right-click the My Getting Started Statechart.lvsc item and select Properties . LabVIEW launches the Properties dialog box.
7. Select the Statechart Code Generation item from the Category list. LabVIEW displays options relating to statechart code generation .
8. Select Asynchronous from the Usage pull-down menu to specify that the statechart is asynchronous .
9. Click the OK button to save changes and return to the Project Explorer window.

#### Defining States

The next step is creating the states that comprise the statechart. A state is a unique condition in which the statechart can be. For example, a basic light bulb can be either ON or OFF. Therefore, a statechart that represents this light bulb would contain only these two states.

The statechart you construct does not represent any real-world application. This statechart consists of three states: Menu, Play, and Pause. Complete the following steps to create these states.

1. In the Project Explorer window, double-click the Diagram.vi item to launch the Statechart Editor window.
 This window displays the statechart diagram. You build a statechart by placing statechart objects on the statechart diagram.
2. If you do not see the Functions palette, select View»Functions Palette to display this palette.
3. On this palette, select Statechart»Statechart Development to display the Statechart Development palette.
4. Click the State object.
5. Move the cursor over the statechart diagram. Click to place the top left corner of the state, drag the cursor diagonally to establish the size of the state, and click again to place the state on the statechart diagram.
6. Notice the state is labeled State . Double-click this label to enable text editing and enter Menu as the new label.
7. Move the cursor over the black border of the Menu state until the cursor changes to the Positioning tool .
8. Press the <Ctrl> key and click and drag the cursor to the right of the Menu state to create a copy of the state.
9. Label this new state Play .
10. Create another new state labeled Pause . Place this state to the right of the Play state.
11. Return to the Statechart Development palette and place a Terminal pseudostate below the Play state.
 [IMAGE alt='image' src='note.gif']
**Note** A pseudostate is a statechart object that represents a state. The Terminal pseudostate represents a state that can terminate the statechart.

The statechart diagram now resembles the following figure:

[IMAGE alt='image' src='gsg2_1.gif']

#### Creating a Transition

The next step is defining the ways in which the statechart can move between states. To define this behavior, you use transitions to connect one state to another visually. Complete the following steps to create transitions between two states.

1. Move the cursor over the right border of the Menu state until the cursor changes to the Wiring tool .
 
 [IMAGE alt='image' src='note.gif']
**Note** If you do not see the Wiring tool, you might have disabled [automatic tool selection](/csh?topicname=lvhowto/selecting_a_tool.html). Either enable this feature or press the <Tab> key until the Wiring tool appears.
2. Click the state border. As you move the cursor across the statechart diagram, LabVIEW draws a dotted line between the state and the Wiring tool.
3. Move the cursor over the left border of the Play state. A gray box appears under the cursor.
4. Click the border to finish the transition. LabVIEW creates a transition between the two states.
 
 [IMAGE alt='image' src='note.gif']
**Note** If you move the cursor inside the state border before clicking it, LabVIEW attempts to create a transition into the state instead of to the state. In this situation, press the <Esc> key to remove the erroneous transition.

The statechart diagram now resembles the following figure:

[IMAGE alt='image' src='gsg2_2.gif']

The object that appears in the middle of the transition is a transition node. You use this node to configure the transition.

#### Creating a Trigger and Configuring a Transition

The next step is specifying that the statechart takes the transition only after receiving a specific event, also called a trigger. By default, transitions are configured to react to the NULL trigger. However, the caller VI that executes this statechart does not send the NULL trigger. Therefore, you must configure this transition to react to a different trigger.

|  | Note Statecharts can receive triggers from an external program, such as a VI, and from within the statechart itself. Later in this tutorial you will use a VI to send triggers to the statechart. |
| --- | --- |

Each statechart has a list of triggers from which you can choose when configuring a transition. Configuring a transition involves creating a trigger and then associating that trigger with the transition. Complete the following steps to configure the transition.

1. Double-click the transition node between the Menu and Play states to launch the Configure Transition dialog box. You use this dialog box to configure transitions.
 The first tab in this dialog box is the Triggers/Groups tab. Notice that the NULL trigger is selected by default in the Triggers and Groups list. Every statechart has this trigger by default.
2. Click the Edit Triggers and Groups button to launch the Edit Triggers and Groups dialog box. You use this dialog box to create and modify triggers.
3. Click the Create Trigger button to create a new trigger, which appears in the Triggers and Groups list.
4. Enter Play as the new trigger name.
5. Click the OK button to save changes and return to the Configure Transition dialog box. Notice the new trigger appears in the Triggers list.
6. In the Triggers/Groups list, place a checkmark in the Play checkbox to specify that this trigger causes the statechart to take the transition.
7. Remove the checkmark from the NULL checkbox.
8. Click the OK button to save changes and return to the statechart diagram.
9. Save the statechart by selecting File»Save in the Statechart Editor window. You also can press the <Ctrl-S> keys.

Notice the blue rectangle on the transition node. This rectangle indicates that you have specified a non-NULL trigger for the transition. If you move the cursor over the transition node, the [Context Help](/csh?topicname=lvdialog/context_help_window.html) window displays the properties of the transition, including the trigger. If you do not see the **Context Help** window, press the <Ctrl-H> keys to display this window.

#### Creating and Configuring Additional Transitions

When you create a transition, the state border you click first is the state that initiates the transition. Because transitions are unidirectional, you can return to that initiating state only by creating a second transition.

|  | Note Notice that the transition itself forms an arrow that shows the direction in which the transition moves. |
| --- | --- |

Create and configure the following transitions and triggers. Remember also to deselect the NULL trigger for each transition.

- From the Play state to the Menu state. Configure this transition to react to the Menu trigger.
- From the Pause state to the Play state. Configure this transition to react to the Play trigger.
- From the Play state to the Pause state. Configure this transition to react to the Pause trigger.

#### Creating and Configuring the Terminal Transitions

Create a transition from the Menu state to the Terminal pseudostate. Configure this transition to react only to a new trigger, Stop. This transition specifies that if the statechart is in the Menu state and receives the Stop trigger, the statechart terminates.

(Optional) Right-click the transition node and select either **Rotate** or **Reverse** to ensure the node faces the proper direction.

Then, save the statechart by pressing the <Ctrl-S> keys.

The statechart diagram now resembles the following figure:

[IMAGE alt='image' src='gsg2_3.gif']

#### Finding and Fixing Statechart Errors

The toolbar of the Statechart Editor window contains a button that you click to generate code for the statechart. Currently, this button appears broken [IMAGE alt='image' src='sc_broken.gif']. This icon means that this statechart contains errors. You must fix these errors before you can generate code for this statechart.

Complete the following steps to find and fix errors with this statechart.

1. Click this button to display the Error list window, which displays several errors.
 These errors appear because the top-level statechart diagram does not have an Initial pseudostate. This pseudostate defines the first state that the statechart enters. The top-level statechart diagram must have one and only one Initial pseudostate.
2. Click the Close button to return to the statechart diagram.
3. Place an Initial pseudostate, located on the Statechart Development palette, to the left of the Menu state.
4. Create a transition between this pseudostate and the Menu state. Notice the Generate Code button no longer is broken . 
 [IMAGE alt='image' src='note.gif']
**Note** Transitions that exit Initial pseudostates cannot have triggers or guards. Therefore, you do not have to configure this transition.
5. Save the statechart.

The statechart diagram now resembles the following figure:

[IMAGE alt='image' src='gsg2_4.gif']

#### Summary

In this tutorial, you learned about the following tasks:

- Creating a statechart.
- Defining states.
- Creating transitions between states.
- Creating triggers.
- Configuring a transition to react to a trigger.
- Specifying the first state that a statechart executes.
- Specifying a state that can terminate the statechart.
- Finding errors on the statechart diagram.

#### Where to Go from Here

In [Part 3](sc_h_gs_3.html) of this tutorial, you define and modify statechart data.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_gs_3.html language=enus -->
## TOPIC 00108: Statechart Module Tutorial Part 3: Defining and Modifying Statechart Data Types

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_gs_3.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_gs_3.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Module Tutorial Part 3: Defining and Modifying Statechart Data Types

In [Part 2](sc_h_gs_2.html) of this tutorial, you created the beginnings of a statechart and learned how to find errors on the statechart diagram. In Part 3 of this tutorial, you define types of data upon which the statechart acts. You also configure the statechart to modify some of this data.

|  | You can complete these exercises in approximately 45 minutes. |
| --- | --- |

|  | Note Refer to the labview\\examples\\Statechart\\Tutorial\\Asynchronous\\Getting Started 3.lvsc for a completed version of the statechart you create in this part of the tutorial. |
| --- | --- |

#### Defining the Type of Output Data

If you want the statechart to modify data, you first must define the type of data. This process involves creating the controls and/or indicators that represent the statechart data.

Complete the following steps to define the statechart output data. Later in this part of the tutorial, you configure the statechart to modify this data.

1. Open the My Getting Started Statechart.lvsc statechart that you constructed in Part 2 of this tutorial. You also can navigate to the labview\examples\Statechart\Tutorial\Asynchronous directory and open Getting Started 2.lvsc for the completed statechart from Part 2 of this tutorial.
 [IMAGE alt='image' src='note.gif']
**Note** Recall that the Getting Started 2.lvsc statechart appears in a [Project Explorer](/csh?topicname=lvconcepts/using_labview_projects.html) window containing the necessary support files for the statechart.
2. Double-click the Outputs.ctl item. LabVIEW displays the Control Editor window for this type definition .
3. Notice the numeric control Numeric inside the Outputs cluster. Right-click this control and select Change to Indicator to change this control to a numeric indicator.
4. Right-click the Numeric indicator and select Replace»Express»Text Indicators»String Indicator from the shortcut menu to replace the numeric indicator with a string indicator.
5. Double-click the String label and enter Current Activity as the new label.
6. Press the <Ctrl-S> keys to save this type definition.
7. Close the Control Editor window to return to the Project Explorer window.

#### Defining the Type of State Data

State data is different from output data. State data is accessible from only the statechart, whereas output data also is accessible from a VI that calls the statechart. Use state data to define data types that other VIs do not need to access.

Complete the following steps to define the statechart state data. You modify this data in Part 4 of this tutorial.

1. In the Project Explorer window, double-click the StateData.ctl item.
2. Right-click the Data control and select Change to Indicator to replace the numeric control with a numeric indicator.
3. Double-click the Data label and enter Counter as the new label.
4. Press the <Ctrl-S> keys to save this type definition.
5. Close the Control Editor window to return to the Project Explorer window.

#### Defining a State Entry Action

The next step is configuring each state to modify the **Current Activity** indicator that you [defined](#editoutputdata) earlier. You accomplish this task by defining an entry action for a state. An entry action is LabVIEW block diagram code that the statechart executes immediately after entering a state.

Complete the following steps to configure the Menu state to update this indicator.

1. Double-click the Diagram.vi item to display the Statechart Editor window.
2. Double-click the border of the Menu state to launch the Configure State dialog box.
 
 [IMAGE alt='image' src='note.gif']
**Note** When you configure a state, a wrench icon appears on the state ([IMAGE alt='image' src='noloc_env_state_config_wrench.gif']) in the **Statechart Editor** window. The state also changes color. You can [customize the configuration color](../lvschowto/sc_h_config_color.html) for states. The default configuration color is yellow. 
 The left side of this dialog box contains the Reactions list. The right side of this dialog box displays several tabs that correspond to the item you select from the Reactions list. By default, the dialog box displays the Entry Action item in the Reactions list. This selection specifies that you want to define the entry action of the state.
 The tabs on the right correspond to the selected item in the Reactions list. By default, the Action tab is selected. LabVIEW displays the block diagram you use to define the entry action.
3. Notice the Outputs cluster element on the right side of this block diagram. Click this cluster element and select Outputs»Current Activity . This element now displays Outputs.Current Activity , which indicates you can write to the value of the type definition you defined.
4. Move the cursor over the input of this cluster element until the cursor changes to the Wiring tool.
5. Right-click the input and select Create»Constant from the shortcut menu. LabVIEW places a string constant on the block diagram.
 [IMAGE alt='image' src='note.gif']
**Note** You cannot access the front panel window for this block diagram. Therefore, National Instruments recommends using block diagram constants instead of front panel controls.
6. Enter Menu as the value of the constant. The block diagram now resembles the following figure:
 [IMAGE alt='image' src='gsg3_1.gif'] 
 This entry action code means that, immediately after entering the Menu state, the statechart changes the Current Activity indicator to read Menu . Later in this tutorial, you will display the value of this indicator in the VI that calls the statechart.
7. Click the OK button to save changes and return to the statechart diagram.
8. The next step is defining the Play and Pause states to update the Current Activity indicator appropriately. Define the Entry Action for each state to update this indicator to Playing or Paused , respectively.
9. Save the statechart.

#### Defining the Action of a Transition

The transition from the Menu state to the Terminal pseudostate also causes a change in the activity of the statechart. Complete the following steps to configure this transition.

1. Double-click the transition node in between the Menu state and Terminal pseudostate to launch the Configure Transition dialog box. Notice the tabs in this dialog box are identical to those in the Configure State dialog box. The only difference is that the Configure Transition dialog box does not have a list of items on the left side of the dialog box. These tabs apply to the whole transition.
2. Click the Action tab.
3. Write the block diagram code that changes the value of the Current Activity indicator to Stopped .
4. Click the OK button to save changes and return to the statechart diagram.

Notice the transition node you just configured now displays two blue rectangles. The second blue rectangle indicates the transition has a specified action.

#### Duplicating the Transition Node

The next step is creating transitions from the Play and Pause states to the Terminal pseudostate. Instead of configuring additional transition nodes, you can duplicate the transition node you configured already. Complete the following steps to duplicate this transition node.

1. Press the <Ctrl> key and click and drag the transition node you just configured.
2. Move this node under the Play state.
3. Click the bottom border of the Play state to initiate a transition segment.
4. Move the cursor over the incoming tunnel of the transition node until LabVIEW displays a tip strip that reads Segment In .
5. Click again to complete the transition segment.
6. Create a transition segment from the other side of this node to the Terminal pseudostate.
7. (Optional) Right-click the transition node and select either Rotate or Reverse to ensure the node faces the proper direction.
8. Repeat steps 1–7 to create an additional transition node from the Pause state to the Terminal pseudostate. All three states now have a transition to the Terminal pseudostate.
9. Save the statechart.

#### Generating Code for the Statechart

The next step is generating code for the statechart. This code is contained in a single [Run Statechart](../lvsc/sc_runsc.html) function that you place on the block diagram of the [caller VI](../lvscconcepts/sc_c_callervi.html). Complete the following steps to generate code for this statechart.

1. Display the Statechart Editor window.
2. Click the Generate Code button , which is located on the toolbar of this window.
3. Close the Statechart Editor window.

|  | Note You also can generate code by right-clicking the .lvsc file in the Project Explorer window and selecting Generate Code from the shortcut menu. |
| --- | --- |

#### Configuring the Caller VI

The next step is configuring a caller VI to execute and send triggers to the statechart. This VI contains two functions, Run Statechart and [Send External Trigger](../lvsc/sc_send_event.html), that you must link to the statechart. Complete the following steps to link these functions to the statechart.

1. In the Project Explorer window, select File»Open .
2. Browse to the labview\examples\Statechart\Tutorial\Asynchronous directory and double-click Getting Started Caller VI (Unlinked).vi . Open example
3. Display the block diagram of this VI. All the wires are broken because neither the Run Statechart nor the Send External Trigger function is linked to a statechart.
4. Locate the Run Statechart function . This function executes the statechart when you run the caller VI.
5. Right-click this function and select Link to Statechart from the shortcut menu. LabVIEW prompts for a .lvsc file to which the function can link.
6. Click the Browse button and navigate to the directory that contains the My Getting Started Statechart.lvsc file.
7. Click the OK button. Notice the wires to and from this function now are intact.
8. Repeat steps 4–7 for the Send External Trigger function.
9. Select File»Save As and save the caller VI as Getting Started Caller VI Linked.vi .
10. Press the <Ctrl-R> keys to run the caller VI. Click the front panel buttons and notice how the Current Activity indicators changes according to the state.
11. Stop the caller VI.
12. Save and close the caller VI.

|  | Note The inputs and triggers wired to the Run Statechart function and the Send External Trigger function are not linked to the My Getting Started Statechart.lvsc file. The Getting Started Caller VI (Unlinked).vi does not reflect any changes you make to the inputs or triggers in the My Getting Started Statechart.lvsc code. |
| --- | --- |

#### Summary

In this tutorial, you learned about the following tasks:

- Defining types of data that the statechart can modify.
- Defining the entry action of a state.
- Defining the action of a transition.
- Generating code for the statechart.
- Linking the Run Statechart and Send External Trigger functions to a statechart.

#### Where to Go from Here

In [Part 4](sc_h_gs_4.html) of this tutorial, you create and configure regions and substates.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_gs_4.html language=enus -->
## TOPIC 00109: Statechart Module Tutorial Part 4: Adding Regions and Substates

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_gs_4.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_gs_4.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Module Tutorial Part 4: Adding Regions and Substates

In Parts [2](sc_h_gs_2.html) and [3](sc_h_gs_3.html) of this tutorial, you created a statechart consisting of three states, two pseudostates, and transitions between these objects. You also defined types output and state data types, configured the statechart to modify this data, and configured a caller VI.

In Part 4 of this tutorial, you add hierarchical [substates](../lvscconcepts/sc_c_hierarchy.html) to the statechart. You also send a trigger to the internal trigger queue, define a transition guard, and use some more in-depth debugging techniques.

|  | You can complete these exercises in approximately 45 minutes. |
| --- | --- |

|  | Note Refer to the labview\\examples\\Statechart\\Tutorial\\Asynchronous\\Getting Started 4.lvsc for a completed version of the statechart you create in this part of the tutorial. |
| --- | --- |

#### Adding a Region and Two Substates

A region defines the area in which you can place states. You can place regions within states, which means you can use regions to define hierarchical substates. Complete the following steps to add a region and two substates to this statechart.

1. Display the Statechart Editor window for the My Getting Started Statechart.lvsc statechart that you constructed in Part 3 of this tutorial. You also can navigate to the labview\examples\Statechart\Tutorial\Asynchronous directory and open Getting Started 3.lvsc for the completed statechart from Part 3 of this tutorial. You can display the Statechart Editor window by double-clicking the Diagram.vi item in the Project Explorer window for the statechart.
2. Move the cursor over the Play state until resizing handles appear.
3. Drag the resizing handles down and to the right to increase the size of this state.
4. Display the Statechart Development palette.
5. Click the Region icon.
6. Move the cursor within the Play state. Click and drag to place this region on the statechart diagram.
7. Notice the region is labeled Region . Enter Tick Counter as the new label.
8. Place two states in this region.
9. Label the first state Tick and the second state Tock .
10. Save the statechart.

The statechart diagram now resembles the following figure:

[IMAGE alt='image' src='gsg4_1.gif']

|  | Note The Play state now contains two substates. Therefore, the Play state now is a superstate. |
| --- | --- |

#### Creating Another Trigger

The next step is creating a trigger. You will configure a transition to react to this trigger. Unlike the triggers you created in Part 2 of this tutorial, you will not send this trigger from the caller VI to the statechart. Instead, you will cause the statechart to send this trigger to the [internal trigger queue](../lvscconcepts/sc_c_trigqueue.html) of the statechart. You can send triggers to this queue only as part of a statechart action or a subVI that an action calls.

Complete the following steps to create this trigger.

1. Display the Project Explorer window for this statechart.
2. Double-click the Edit Triggers and Groups item. LabVIEW launches the Edit Triggers and Groups dialog box, which you use to create triggers and groups of triggers.
3. Click the Create Trigger button to add a trigger to the list.
4. Enter Increment as the name of this trigger.
5. Click the OK button to save changes.

#### Configuring the Tick Substate

The next step is configuring the Tick substate to change the **Current Activity** indicator you defined in Part 3 of this tutorial. You also configure the Tick substate to send the Increment trigger to the internal queue of the statechart. Later in this part of the tutorial, you will configure a transition to react to this trigger.

Complete the following steps to define this behavior.

1. Right-click the Tick substate and select Configure State to launch the Configure State dialog box.
2. Define the entry action of this substate to display Counting in the Current Activity indicator. Refer to the Defining a State Entry Action section of Part 3 of this tutorial for more information about configuring the Current Activity indicator.
3. Move the cursor over the Outputs.Current Activity element to display resizing handles .
4. Click and drag to display another terminal of this element.
5. Click this additional terminal and select InternalQueue»All Elements .
6. Repeat step 5 for the Outputs terminal cluster on the left side of the block diagram.
7. Place a Send Internal Trigger function, located on the Statechart Communication palette, on the block diagram.
8. Wire the InternalQueue terminal cluster on the left side of the block diagram to the Internal Queue In input of the Send Internal Trigger function.
9. Wire the Internal Queue Out output of the Send Internal Trigger function to the InternalQueue terminal on the right side of the block diagram.
10. Right-click the Trigger input of this function and select Create»Constant from the shortcut menu.
11. Select Increment as the value of this constant. The entry action resembles the following figure:
 [IMAGE alt='image' src='gsg4_2.gif']
12. Click the OK button to save changes and return to the statechart diagram.

The entry action of the Tick substate now updates the **Current Activity** indicator and sends the Increment trigger to the internal queue of the statechart.

#### Creating and Configuring Transitions in the Tick Counter Region

The next step is creating and configuring two transitions in the Tick Counter region. Complete the following steps to configure these transitions:

1. Place an Initial pseudostate in this region.
2. Create a transition from this pseudostate to the Tick substate. LabVIEW creates a transition node for this transition.
3. Double-click the new transition node to launch the Configure Transition dialog box.
 [IMAGE alt='image' src='note.gif']
**Note** Notice that the **Triggers/Groups** and **Guard** tabs are disabled. You cannot define triggers or guards for initial transitions.
4. Ensure you are on the Action page of this dialog box.
5. Write LabVIEW code that sets the Counter indicator to 0 . You defined this indicator in Part 3 of this tutorial. 
 The following figure shows this code: [IMAGE alt='image' src='gsg4_3.gif']
6. Click the OK button to save changes and return to the statechart diagram.
7. Create a transition from the Tick substate to the Tock substate.
8. Configure this transition to react to the Increment trigger only.
9. Click the Action tab.
10. Use the Increment function to write LabVIEW code that increments the Counter indicator by 1. The following figure shows this code.
 [IMAGE alt='image' src='gsg4_4.gif']
11. Click the OK button to save changes and return to the statechart diagram.
12. Create a transition from the Tock substate to the Tick substate.
13. Create a new trigger named Return. Configure this transition to react to the Return trigger only. Later in this part of the tutorial you will configure the caller VI to send this trigger.
14. Save the statechart.

The Play superstate now resembles the following figure:

[IMAGE alt='image' src='gsg4_4a.gif']

#### Defining a Transition Guard

The next step is specifying that the statechart leaves the Play superstate automatically after the **Counter** indicator reaches a certain value. To specify this behavior, you can use a transition guard. A transition guard is LabVIEW block diagram code that determines whether the statechart takes the associated transition. The guard code must return either TRUE or FALSE. If the guard returns TRUE, the statechart takes the transition. If the guard returns FALSE, the statechart does not take the transition.

Complete the following steps to define this guard.

1. The Play superstate already has one transition to the Menu state. Create a second transition from the Play superstate to the Menu state.
2. Double-click the new transition node. LabVIEW launches the Configure Transition dialog box.
3. Configure this transition to react to the Return trigger only.
4. Click the Guard tab.
5. Use the Greater? function to write LabVIEW code that returns TRUE if the Counter indicator is greater than 25. The following figure shows this code:
 [IMAGE alt='image' src='gsg4_6.gif']
6. Click the OK button to save changes and return to the statechart diagram.
7. Save the statechart.
8. 
9. Close the Statechart Editor window.

With this configuration, the statechart checks the guard code every time the caller VI sends the Return trigger. The guard code returns FALSE if the value of the **Counter** indicator is 25 or less. When the **Counter** indicator reaches 26, the guard code returns TRUE, and the statechart takes the transition to the Menu state.

#### Configuring the Caller VI to Send the Return Trigger

Complete the following steps to configure the caller VI from the **Configuring the Caller VI** section of [Part 3](sc_h_gs_3.html) of this tutorial to send the Return trigger to the statechart.

1. Open the caller VI and display the block diagram.
2. Select the Timeout event case of the Event structure . Notice the blue output tunnel on the right side of this structure. A wire connects this tunnel to the Trigger input of the Send External Trigger function.
3. Right-click this output tunnel and select Create»Constant from the shortcut menu. LabVIEW creates an enumerated type constant that contains the triggers you can send to this statechart.
4. Select Return as the value of this constant.
5. Save the caller VI.

The caller VI now is configured to send the Return trigger when a [Timeout event](/csh?topicname=lvprop/app_timeout.html) occurs. The following figure shows this configuration in the caller VI.

[IMAGE alt='image' src='gsg4_5.gif']

The 500 constant specifies that a timeout occurs after 500 milliseconds elapse with no event occurring. Therefore, the statechart takes the transition from the Tick substate to the Tock substate every 500 milliseconds. Now the statechart increments the **Counter** indicator until you send the Pause, Stop, or Menu trigger. These triggers cause the statechart to exit the Play superstate. The statechart also exits the Play superstate when the **Counter** indicator reaches 26.

#### Enabling Debugging for the Statechart

If you want to use the debugging tools for a statechart, you first must enable debugging for the statechart.

Complete the following steps to enable debugging for the statechart.

1. Right-click the My Getting Started Statechart.lvsc item and select Properties . LabVIEW launches the Properties dialog box.
2. Select the Statechart Code Generation item from the Category list. LabVIEW displays options relating to statechart code generation .
3. Select Enabled from the Debugging pull-down menu to specify that debugging is enabled for the statechart. The default value is Enabled . Debugging is only available on Desktop, Real-Time, and FPGA targets.
4. Click the OK button to save changes and return to the Project Explorer window.

#### Watching Statechart Data

The next step is running the caller VI and watching how the statechart increments the **Counter** indicator.

1. Right-click the Run Statechart function and select Debug Statechart . LabVIEW displays the Statechart Debugging window for the statechart.
2. Click the Open Statechart Data Display button , located on the toolbar of this window. LabVIEW displays the Statechart Data Display window. This window shows the values of the output data, state data, and internal trigger queue.
3. Run the caller VI. The Current Activity indicator reads Menu .
4. Look at the Statechart Data Display window. Notice the Current Activity indicator reads Menu , which is the same value as the front panel indicator of the caller VI.
5. Click the Play front panel button. The Current Activity indicator displays Counting , which means the statechart is in the Tick substate. Watch the Statechart Data Display window as the value of the Counter indicator increases. 
 When the value of the Counter indicator reaches 26, the statechart returns to the Menu state. This behavior is what you configured by using a transition guard.

#### Viewing the Execution of the Transition Guard

The next step is viewing the execution of the transition guard you defined. Complete the following steps to view the execution of this guard.

1. While the caller VI is running, display the Statechart Debugging window and locate the guarded transition node from the Play superstate to the Menu state.
2. Right-click this transition node and select Guard . LabVIEW displays the block diagram of the VI that corresponds to the guard you defined. Notice the code appears as you created it earlier in this tutorial.
3. Move the cursor over the green wire that exits the Greater? function.
4. Click this wire to place a probe on this wire.
5. Click the Play front panel button again. Notice the Counter indicator resets to 0 and begins incrementing again. You configured this behavior by using the transition between the Initial pseudostate and the Tick substate.
6. Watch the probe as the Counter indicator increments. The probe shows that the guard code sends FALSE to the Execute? indicator. This FALSE value means the statechart does not take the transition to the Menu state.
 After the Counter indicator reaches 26, the Greater? function sends TRUE to the Execute? indicator, which means the guard returns TRUE. The statechart then takes the transition to the Menu state.
7. Click the Stop front panel button to stop the statechart and the caller VI.
8. Close all windows except for the Project Explorer window.

#### Debugging the Statechart

If you get unexpected data from a caller VI that references a statechart, you can debug the statechart to identify and correct problems with the statechart data flow.

Complete the following steps to use LabVIEW debugging tools to debug the statechart.

1. Double-click the Getting Started Caller VI Linked.vi to open your caller VI.
2. Display the block diagram of this VI.
3. Right-click the Run Statechart function and select Debug Statechart from the context menu to display the statechart diagram in debugging mode.
4. Click the Highlight Execution button located on the statechart diagram toolbar. Highlighting Statechart Execution highlights the appropriate transitions and states as the statechart receives triggers from the caller VI and moves from one state to another.
5. Run the Getting Started Caller VI Linked.vi and click the Play button on the front panel.
6. Switch back to the statechart diagram. Observe the statechart passing between states, pseudostates and transitions.
7. Click the Stop front panel button to stop the statechart and the caller VI when you are done observing the statechart diagram.
8. Switch to the statechart diagram in debugging mode.
9. Right-click the Tick substate and select Set Breakpoint from the context menu. A red border appears around the substate. This breakpoint pauses execution when the statechart reaches the substate.
10. Repeat steps 5-6. When the statechart progress reaches the Tick substate, the statechart pauses execution.
11. Right-click the Tick substate and select Entry Action from the context menu to display the Tick:Entry Action Block Diagram . [IMAGE alt='image' src='note.gif']
**Note** You also can set breakpoints in the guard and action code for states and transitions.
12. Click the Highlight Execution button.
13. Switch to the statechart diagram in debugging mode.
14. Click the Step Into button located on the statechart diagram toolbar to enter the Tick substate and pause execution.
15. Click the Step Into button again to execute the entry action of the Tick substate.
16. Switch to the Tick:Entry Action Block Diagram to observe the execution of the entry action.
17. Click the Stop front panel button to stop the statechart and the caller VI when you are done observing the entry action and statechart diagram.
18. Close all windows except for the Project Explorer window.

#### Summary

In this tutorial, you learned about the following tasks:

- Creating regions.
- Creating substates.
- Creating triggers by using the Project Explorer window.
- Sending triggers to the internal queue of a statechart.
- Defining the guard of a transition.
- Displaying statechart data during execution.
- Viewing the execution of a guard.
- Debugging a statechart.

#### Where to Go from Here

In [Part 5](sc_h_gs_5.html) of this tutorial, you create and configure orthogonal regions. You also learn how to use state history.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_gs_5.html language=enus -->
## TOPIC 00110: Statechart Module Tutorial Part 5: Using Orthogonal Regions and State History

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_gs_5.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_gs_5.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Module Tutorial Part 5: Using Orthogonal Regions and State History

In [Part 4](sc_h_gs_4.html) of this tutorial, you learned how to create and configure regions and substates. You also learned how to use some debugging tools included in the LabVIEW Statechart Module. In Part 5 of this tutorial, you add [orthogonal regions](../lvscconcepts/sc_c_orthogonal.html). You also use state history.

|  | You can complete these exercises in approximately 45 minutes. |
| --- | --- |

|  | Note Refer to the labview\\examples\\Statechart\\Tutorial\\Asynchronous\\Getting Started 5.lvsc for a completed version of the statechart you create in this part of the tutorial. |
| --- | --- |

#### Defining More State Data

The first step is defining an additional state data type. This type of data is modified in the Concurrent orthogonal region. Complete the following steps to define this data type.

1. Ensure you have closed all debugging windows and statechart diagrams.
2. Display the Project Explorer window for the My Getting Started Statechart.lvsc statechart that you constructed in Part 4 of this tutorial. You also can navigate to the labview\examples\Statechart\Tutorial\Asynchronous directory and open Getting Started 4.lvsc for the completed statechart from Part 4 of this tutorial.
3. Double-click the StateData.ctl item. LabVIEW displays the Control Editor window for this type definition .
4. Right-click in the Control Editor window to access the Controls palette.
5. Select Express»Text Indicators»String Indicators to add a string indicator to the type definition.
6. Label this indicator Color .
7. Drag this indicator inside the StateData cluster.
8. Press the <Ctrl-S> keys to save this type definition.
9. Close the Control Editor window to return to the Project Explorer window.

#### Creating the Orthogonal Region

Orthogonal regions are multiple regions in the same state. Substates in orthogonal regions execute concurrently, which means these states both execute during a single iteration of the statechart. Complete the following steps to add orthogonal regions to this statechart.

1. Display the statechart diagram.
2. Click and drag to increase the size of the Play superstate.
3. Place a second region inside the Play superstate and to the right of the Tick Counter region.
4. Label this new region Concurrent .
5. Place two substates inside this region.
6. Label the substates Red and Green .
7. Place an Initial pseudostate in the Concurrent region.
8. Create the following transitions:
  - From the Initial pseudostate to the Red substate.
  - From the Red substate to the Green substate.
  - From the Green substate to the Red substate.

The Play superstate now resembles the following figure:

[IMAGE alt='image' src='gsg5_1.gif']

#### Configuring the Substates and Transitions

The next step is defining the actions of these substates and transitions. Complete the following steps to configure these items.

1. Configure the initial transition to write an Empty String Constant to the Color indicator to reset this indicator every time the statechart enters the Concurrent region.
2. Define the entry action of the Red substate to write Red to the Color indicator.
3. Locate the transition node on the transition from the Red substate to the Green substate. Configure this transition to write Green to the Color indicator.
 Configure this transition to react to the Return trigger only. Remember that the caller VI sends this trigger during the Timeout event of the Event structure.
4. Configure the other transition to react to the Return trigger only.
 [IMAGE alt='image' src='note.gif']
**Note** Even though you configured both transitions to react to the same trigger, the statechart checks only transitions that exit the current substate. Therefore, when the statechart is in the Green substate, the statechart does not consider triggers that exit the Red substate, and vice versa.
5. Save the statechart.
6. Generate code for the statechart.
7. Close the statechart diagram.

#### Running the Caller VI

Complete the following steps to see the effect of the orthogonal region.

1. Run the caller VI from the Debugging the Statechart section of Part 4 of this tutorial, watch the state data , and click the Play front panel button. Notice the Counter indicator increments while the Color changes from Red to Green .
2. Click the Highlight Execution button to see the statechart move between orthogonal substates concurrently. You also can see the Increment trigger pass to the internal queue of the statechart.
3. Click this button again to turn off execution highlighting. Then, stop the caller VI.
4. Close all debugging windows. You cannot edit a statechart while debugging windows are open.

#### Taking State History into Account

While the statechart is in the Play superstate, clicking the **Pause** front panel button and then the **Play** front panel button resets the **Counter** variable to 0. The next step is configuring the statechart to remember the previous value of the **Counter** indicator. In this configuration, when you re-enter the Play superstate from the Pause state, the variable does not reset from 0. Instead, the statechart remembers the value of the **Counter** indicator and begins counting from that value.

Complete the following steps to define this behavior.

1. Display the statechart diagram.
2. Place a Deep History pseudostate, located on the Statechart Development palette, in the Tick Counter region. [IMAGE alt='image' src='note.gif']
**Note** In this situation, you also can use the [Shallow History](../lvsc/sc_shistory.html) pseudostate because the Play superstate contains only one level of [hierarchy](../lvscconcepts/sc_c_hierarchy.html).
3. Locate the transition from the Pause state to the Play superstate. The triangular port of this transition is in the Play superstate.
4. Move the cursor over this triangular port until the cursor changes to the Wiring tool .
 
 [IMAGE alt='image' src='note.gif']
**Note** If you do not see the Wiring tool, you might have disabled [automatic tool selection](/csh?topicname=lvhowto/selecting_a_tool.html). Either enable this feature or press the <Tab> key until the Wiring tool appears.
5. Click to initiate a transition segment.
6. Move the cursor over the Deep History pseudostate.
7. Click to complete the transition. The Play superstate now resembles the following figure:
 [IMAGE alt='image' src='gsg5_2.gif']
8. Save the statechart.
9. Generate code for the statechart.

In this configuration, the first time the statechart enters the Tick Counter region, the statechart executes the Tick substate because this substate is connected to the Initial pseudostate. However, if you move to the Pause state and then return to the Play superstate, the statechart enters the substate that was active when the statechart left the Play superstate. The Deep History pseudostate defines this behavior. Because this behavior bypasses the Initial pseudostate, the **Counter** indicator does not reset to 0.

|  | Note Only the Pause state has a transition to the Deep History pseudostate. Therefore, if you leave the Play superstate and return to the Menu state, the statechart resets the Counter indicator as usual. Also, notice that the Deep History pseudostate applies only to the Tick Counter region. |
| --- | --- |

#### Watching the Counter

Complete the following steps to see this behavior.

1. Run the caller VI and watch the state data .
2. Click the Play front panel button. The statechart begins incrementing the Counter variable.
3. After the Counter indicator reaches 10 , click the Pause front panel button. The statechart moves to the Pause state.
4. Click the Play front panel button again. The Counter variable resumes counting from the number 10 .
5. After the Counter indicator reaches 20 , click the Menu front panel button. The statechart moves to the Menu state.
6. Click the Play front panel button again. The Counter indicator resets because the Menu state does not have a transition to the Deep History pseudostate.
7. Stop the caller VI.
8. Close the caller VI and all debugging windows.

#### Summary

In this tutorial, you learned about the following tasks:

- Creating orthogonal regions.
- Defining substates that execute concurrently.
- Extending an existing transition.
- Using state history.

#### Where to Go from Here

In [Part 6](sc_h_gs_6.html) of this tutorial, you create one transition that enters and exits multiple substates simultaneously.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_gs_6.html language=enus -->
## TOPIC 00111: Statechart Module Tutorial Part 6: Splitting and Merging Transition Segments

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_gs_6.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_gs_6.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Module Tutorial Part 6: Splitting and Merging Transition Segments

In [Part 5](sc_h_gs_5.html) of this tutorial, you added orthogonal regions and used state history. In Part 6 of this tutorial, you create one transition to multiple substates. You also create one transition from multiple substates to a single state. You also use a subdiagram to improve the appearance of the statechart diagram.

|  | You can complete these exercises in approximately 45 minutes. |
| --- | --- |

|  | Note Refer to the labview\\examples\\Statechart\\Tutorial\\Asynchronous\\Getting Started 6.lvsc for a completed version of the statechart you create in this part of the tutorial. |
| --- | --- |

#### Creating One Transition to Multiple Substates

Examine the **Statechart Editor** window for the My Getting Started Statechart.lvsc statechart that you constructed in [Part 5](sc_h_gs_5.html) of this tutorial. You also can navigate to the labview\examples\Statechart\Tutorial\Asynchronous directory and open Getting Started 5.lvsc for the completed statechart from Part 5 of this tutorial. In the current configuration, when the statechart takes the transition from the Pause state to the Play superstate, the statechart enters the [Deep History](../lvsc/sc_deephistory.html) pseudostate and the Red substate. The statechart enters the Red substate because this substate is connected to the Initial pseudostate in the region.

In some cases, you might want to bypass this initial transition by creating a transition to a specific substate. The Play superstate has a specific transition already that goes from the Pause state to the Deep History pseudostate. Instead of creating an additional transition, you can specify that this transition goes to not only the Deep History pseudostate, but also the Green substate.

Complete the following steps to define this behavior.

1. Locate the transition that goes from the Pause state to the Deep History pseudostate.
2. Double-click the segment of this transition that lies inside the Play superstate.
3. Press the <Delete> key to delete this transition segment.
4. Place a Fork connector, located on the Statechart Development palette, in the location of the segment you deleted.
 [IMAGE alt='image' src='note.gif']
**Note** You might have to resize the Play superstate. You also can resize the Fork connector. 
 Notice the triangular port on the top half of the Fork connector. This port is where you connect the incoming transition segment. The gray area on the bottom half of this connector is where you click to create outgoing transition segments.

The Play superstate now resembles the following figure:

[IMAGE alt='image' src='gsg6_1.gif']

#### Creating Transition Segments to and from the Fork Connector

Complete the following steps to define the transition that the Fork connector takes.

1. Locate the triangular port of the transition from the Pause state to the Play superstate. This port is in the Play superstate.
2. Move the cursor over this port until the cursor changes to the Wiring tool .
3. Click to initiate a transition segment.
4. Move the cursor over the incoming port to the Fork connector.
5. Click to complete the transition segment. The Play superstate now resembles the following figure:
 [IMAGE alt='image' src='gsg6_2.gif']
6. Click the gray area on the bottom half of the Fork connector to initiate an outgoing transition segment from the Fork connector.
7. Click the rectangular port that connects to the Deep History pseudostate to complete the outgoing transition segment from the Fork connector to the Deep History pseudostate.
8. Create a transition segment from the Fork connector to the Green substate.
9. Save the statechart.

The Play superstate now resembles the following figure:

[IMAGE alt='image' src='gsg6_3.gif']

|  | Note You can click and drag the transition segments to rearrange the position of these segments on the statechart diagram. You also can right-click a segment and select Clean Up Wire to have LabVIEW route the segment automatically. |
| --- | --- |

Before you placed the Fork connector, upon moving from the Pause state to the Play superstate, the statechart entered the Deep History pseudostate and the Red substate. In the current configuration, the Fork connector specifies that, upon moving from the Pause state to the Play superstate, the statechart enters the Deep History pseudostate and the Green substate. For the purposes of the statechart execution, this split segment is considered a single transition, even though the outgoing segments move to different substates.

|  | Note Notice the transition segments that are in the Play superstate have no transition nodes. You can configure this transition only at the point where the transition is in a region. In this situation, the top-level statechart diagram is the region. |
| --- | --- |

#### Specifying the Substates in which the Statechart Must Be Before It can Leave the Play Superstate

Recall the guarded transition that exits the Play superstate and enters the Menu state. The statechart takes this transition only if the value of the **Counter** indicator is greater than 25. In some situations, you might want to specify that the statechart must be in particular substates before taking this transition. This specification adds another condition to the transition. However, this condition is based on which states are active rather than the value of statechart data.

Complete the following steps to define this behavior.

1. Place a Join connector, located on the Statechart Development palette, in the Play superstate below the two regions. 
 [IMAGE alt='image' src='note.gif']
**Note** You might have to resize the Play superstate. You also can resize the Join connector.
2. Create a transition segment from the Tock substate to the gray area of the Join connector.
3. Create a transition segment from the Green substate to the gray area of the Join connector.
4. Create a transition segment from the Join connector to the rectangular port of the guarded transition from the Play superstate to the Menu state.
 The Play superstate resembles the following figure: [IMAGE alt='image' src='gsg6_4.gif'] 
 The Join connector specifies that the statechart must be in both the Tock and Green substates before the statechart can evaluate the transition guard. Again, for the purposes of statechart execution, these merged segments are considered a single transition.
5. Save the statechart.
6. Generate code for the statechart.

#### Running the Caller VI Again

1. Run the caller VI and watch the state data .
2. Click the Play front panel button.
3. When the Counter indicator reaches 10 , click the Pause front panel button.
4. Highlight the execution of the statechart.
5. Click the Play front panel button. Watch the execution of the statechart as the statechart takes the transition segment into the Fork connector and then into the Deep History pseudostate and Green substate.
6. Turn off execution highlighting.
7. Stop the caller VI.
8. Close all debugging windows.

#### Viewing the Play Superstate as a Subdiagram

During this tutorial, you have added a significant amount of content to the Play superstate. A state of this size and complexity can make visual navigation of the statechart difficult. To address this issue, you can use subdiagrams to separate parts of the statechart diagram visually. This separation hides states you do not need to see, which makes the statechart diagram easier to navigate.

Complete the following steps to view the Play superstate as a subdiagram.

1. Display the statechart diagram.
2. Right-click the border of the Play superstate and select View as Subdiagram . LabVIEW displays a new window that shows the contents of the Play superstate on a blue diagram. For now, minimize this window.
3. Return to the statechart diagram and look at the Play superstate. Notice how this state has a darker color and no longer has a border.
4. Resize the Play superstate to be smaller. Notice how viewing the state as a subdiagram can save a lot of room on the statechart diagram.
5. Right-click the Play superstate and select Open Subdiagram . The contents of the state appear in a separate window. Notice how this window has a blue diagram that distinguishes this window from the statechart diagram. You can place statechart objects in this window the same way as if you were viewing the state in the Statechart Editor window.
 [IMAGE alt='image' src='note.gif']
**Note** You can view the state normally again by repeating step 3. However, if you resized the state to be smaller, the state contents might not fit in the smaller state. You might have to resize the state again.
6. Save the statechart.
7. Close LabVIEW.

#### Summary

In this tutorial, you learned about the following tasks:

- Creating one transition that goes to multiple substates.
- Specifying that the statechart must be in certain substates before taking a transition.
- Viewing states as subdiagrams.

#### Where to Go from Here

- You can view the statechart diagram that you completed in this tutorial with links to each of the objects in the diagram.
- Documentation related to the LabVIEW Statechart Module.
- The Getting Started with LabVIEW manual contains an in-depth introduction to LabVIEW, including several tutorials that showcase LabVIEW features.
- The LabVIEW Fundamentals book provides information about LabVIEW programming concepts, techniques, features, VIs, and functions you can use to create many types of applications.
- Refer to the National Instruments Web site for additional developer resources, training, technical support, and so on.

|  | (Windows) To view topics related to the Statechart Module, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_iodata.html language=enus -->
## TOPIC 00112: Defining Data Types for a Statechart (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_iodata.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_iodata.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Defining Data Types for a Statechart (Statechart Module)

You use the [caller VI](../lvscconcepts/sc_c_callervi.html) to send [input, output, and state data](../lvscconcepts/sc_c_iodata.html) to the statechart. Before sending this data, you must define the types of data the caller VI can send to the statechart and receive from the statechart. The following example shows how to define output data.

1. Create a new statechart or open an existing .lvsc file.
2. Display the Project Explorer window associated with this statechart.
3. Double-click the Outputs.ctl item to open the Outputs 
 type definition . This type definition consists of a cluster that can contain elements of multiple data types. By default, this cluster contains a single numeric control labeled Numeric .
4. Right-click this control and select Replace»Express»Text Controls»String Control from the shortcut menu to replace the numeric control with a string control.
5. Double-click the String label and enter SC Example as the new label.
6. (Optional) Enter a default value in the SC Example text box. For example, you can enter Hello World in this string control.
7. Press the <Ctrl-S> keys to save the type definition, and close the window.

|  | Note The previous steps used a string control to represent data. You can place controls and indicators of any data type in any of the three type definitions. |
| --- | --- |

This process is identical for modifying input and state data, except for step 1 in which you double-click either the **Inputs.ctl** or **StateData.ctl** type definition.

Now that you have defined an output data type, the **SC Example** string appears as a cluster element of the **Outputs** cluster when you [configure a transition or static reaction](sc_h_configt.html).

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_isin.html language=enus -->
## TOPIC 00113: Determining Whether a State is Active (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_isin.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_isin.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Determining Whether a State is Active (Statechart Module)

Complete the following steps to determine whether a state is active.

1. Place the IsIn function on the block diagram of a guard or action .
 [IMAGE alt='image' src='add.gif'] Add
2. Click the Inputs cluster element, located on the left side of the block diagram, to display a list of cluster elements.
3. Select the StatechartState element.
4. Wire the StatechartState element to the Statechart States input of the IsIn function.
5. Double-click the IsIn function to launch the Select State dialog box.
6. Select the state that you want to check for activity.
7. Click the OK button to save changes and return to the block diagram.

The guard or action code now resembles the following figure:

[IMAGE alt='image' src='isin.gif']

The **IsIn?** Boolean indicator of this function returns TRUE if the specified state is active. This Boolean returns FALSE if the specified state is not active.

|  | Note You can configure the icon of the IsIn function to display the name of the state or the path to the state that the function checks. Right-click the IsIn function and select Icon Style»Configuration»State Name to display the name of the state. Select Icon Style»Configuration»State Path to display the path to the state. |
| --- | --- |

You also can configure the [Run Statechart](../lvsc/sc_runsc.html) function to display the current active state in the [caller VI](../lvscconcepts/sc_c_callervi.html).

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_join.html language=enus -->
## TOPIC 00114: Specifying the Substates a Statechart Must Be in before Exiting the Superstate (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_join.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_join.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Specifying the Substates a Statechart Must Be in before Exiting the Superstate (Statechart Module)

You can specify that the statechart must be in multiple [substates](../lvscconcepts/sc_c_hierarchy.html) before the statechart can exit a particular [superstate](../lvscconcepts/sc_c_hierarchy.html). These substates must be in different [orthogonal regions](../lvscconcepts/sc_c_orthogonal.html), such as the following figure shows.

[IMAGE alt='image' src='fork_begin.gif']

In the previous figure, the statechart can move from State 1 to the [Terminal](../lvsc/sc_terminal.html) pseudostate at any time. However, you might want to specify that the statechart must be in particular substates before the statechart can take this transition. You can specify this behavior by creating a single transition that exits multiple substates.

Complete the following steps to create a single transition that exits multiple substates.

1. Place a Join 
 connector below the regions in State 1.
 [IMAGE alt='image' src='add.gif'] Add
2. Create a transition from State 3 to the Join connector.
3. Create a transition from State 5 to the Join connector.
4. Create a transition from the Join connector to the outgoing port that connects to the Terminal pseudostate.

The statechart diagram now resembles the following figure.

[IMAGE alt='image' src='join.gif']

In the previous figure, the statechart must be in both State 3 and State 5 before the statechart can exit State 1 and move to the Terminal pseudostate.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_junction.html language=enus -->
## TOPIC 00115: Sharing Transition Actions (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_junction.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_junction.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Sharing Transition Actions (Statechart Module)

You can specify that multiple [transitions](../lvscconcepts/sc_c_trans.html) use the same [action](../lvscconcepts/sc_c_tga.html#action), even though each transition might have a different [trigger](../lvscconcepts/sc_c_tga.html#trigger), such as the following figure shows.

[IMAGE alt='image' src='no_junction.gif']

In the previous figure, Transition 1, Transition 2, and Transition 3 use the same action code. You can simplify this behavior by using the [Junction](../lvsc/sc_junction.html)
 [connector](../lvscconcepts/sc_c_pseudocon.html) to share the three transition actions and create a single transition.

Complete the following steps to share the three transition actions and create a single transition..

1. Remove Transition 1, Transition 2, and Transition 3.
2. Place a Junction connector to the left of State 4.
 [IMAGE alt='image' src='add.gif'] Add
3. Create a transition from State 1 to the Junction connector.
4. Create a transition from State 2 to the Junction connector.
5. Create a transition from State 3 to the Junction connector.
6. Create a transition from the Junction connector to State 4.
7. Define the action of the transition from the Junction connector to State 4.

The statechart diagram now resembles the following figure.

[IMAGE alt='image' src='with_junction.gif']

In the previous figure, the behavior of the statechart remains the same. The Junction connector specifies that the transitions from State 1, State 2, and State 3 use the same action.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_label.html language=enus -->
## TOPIC 00116: Statechart Objects in a Statechart Diagram (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_label.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_label.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Statechart Objects in a Statechart Diagram (Statechart Module)

In [Parts 1-6](../lvschowto/sc_h_gs.html) of this tutorial, you learned about many of the objects available when programming a statechart. The following figure is the completed [statechart diagram](../lvscconcepts/sc_c_editor.html) from the tutorial containing these objects.

[IMAGE alt='image' src='sc_labeled.gif']

The following table lists the objects in the preceding figure.

| Statechart Objects |  |  |
| --- | --- | --- |
| 1 Initial pseudostate | 5 Superstate | 9 Substate |
| 2 State | 6 Fork connector | 10 Deep History pseudostate |
| 3 Port | 7 Orthogonal region | 11 Join connector |
| 4 Transition | 8 Orthogonal region | 12 Terminal pseudostate |

The preceding figure does not display some of the [Statechart Development](../lvsc/sc_obj.html) objects available. This figure does not display [regions](../lvsc/sc_region.html), [Junction](../lvsc/sc_junction.html) connectors, or [Shallow History](../lvsc/sc_shistory.html) pseudostates.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_laststate.html language=enus -->
## TOPIC 00117: Specifying a State that Can Terminate a Region (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_laststate.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_laststate.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Specifying a State that Can Terminate a Region (Statechart Module)

Complete the following steps to specify a [state](../lvsc/sc_state.html) that can terminate a [region](../lvsc/sc_region.html).

1. Place a Terminal 
 pseudostate on the statechart diagram. Having this pseudostate in a region is optional.
 [IMAGE alt='image' src='add.gif'] Add
2. Create a transition from a state to this pseudostate. More than one state can terminate a region, so you can create transitions from multiple states to a single Terminal pseudostate.
3. (Optional) Define any triggers , guards , or actions for this transition.

|  | Note When the statechart enters a Terminal pseudostate that is at the top level of the statechart diagram, the entire statechart terminates. |
| --- | --- |

For example, consider the following figure:

[IMAGE alt='image' src='initial.gif']

Each Terminal pseudostate corresponds to a region. In the previous figure, notice that you can terminate Region 1 only when the statechart is in State 4. You can terminate the entire statechart only when the statechart is in State 1.

|  | Note The Initial pseudostate specifies the state that a region executes first. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_linksc.html language=enus -->
## TOPIC 00118: Linking the Run Statechart Function to a Statechart (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_linksc.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_linksc.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Linking the Run Statechart Function to a Statechart (Statechart Module)

If you place a [Run Statechart](../lvsc/sc_runsc.html) function on the block diagram from the [Statechart Communication](../lvsc/sc_comm.html) palette, you need to link this function to a statechart .lvsc file. Complete the following steps to accomplish this task.

1. Generate code for the statechart .
2. Place a Run Statechart function on the block diagram of the caller VI .
3. Right-click the function and select Link to Statechart .
4. Use the Link to Statechart dialog box to specify a .lvsc file.
5. Click the OK button to save changes and return to the block diagram.

The Run Statechart function now is linked to a statechart.

|  | Tip To link the function without completing these steps, drag the .lvsc file from the Project Explorer window to the block diagram to create a Run Statechart function that already is linked to the proper .lvsc file. |
| --- | --- |

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_newsc.html language=enus -->
## TOPIC 00119: Creating a Statechart (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_newsc.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_newsc.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Creating a Statechart (Statechart Module)

Complete the following steps to create a new statechart.

1. Launch LabVIEW and display the Getting Started window.
2. Select File»New to launch the New dialog box.
3. Select Other Files»Statechart from the Create New tree.
4. Click the OK button. LabVIEW prompts you to save the statechart.
5. Enter a filename and save the statechart in a convenient location on disk.
 LabVIEW displays a Project Explorer window that contains the necessary project folders, VIs, and type definitions under the *<filename>* .lvsc project item. This project item represents the .lvsc file format in which LabVIEW stores statechart information.

You now can [display the Statechart Editor window](sc_h_dispsc.html), [create triggers](sc_h_createtrig.html), or [define types of statechart data](sc_h_iodata.html).

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_outputs.html language=enus -->
## TOPIC 00120: Resetting or Caching Output Values Between Statechart Iterations (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_outputs.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_outputs.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Resetting or Caching Output Values Between Statechart Iterations (Statechart Module)

You can configure whether a statechart resets or caches the [output data](../lvscconcepts/sc_c_iodata.html) between statechart [iterations](../lvscconcepts/sc_c_iteration.html). The behavior you configure depends on the purpose of the statechart.

For example, consider a statechart that implements logic similar to a programmable logic controller (PLC). This statechart might read input data, execute an action, and then return output data. The output data from one iteration does not depend on output data from any previous iteration. In this situation, you can configure the statechart to reset the output data between iterations. Resetting output data frees up memory for other uses.

Conversely, consider a statechart that implements logic similar to a proportional-integral-derivative (PID) controller. PID controllers must take into account the history of the error. In this situation, you can configure this statechart to cache the output data between iterations. Storing output data requires memory in which LabVIEW stores the data.

Complete the following steps to specify either behavior.

1. Launch the Statechart Code Generation page of the Project Library Properties dialog box.
2. To specify that the statechart resets output values between iterations, place a checkmark in the Reset output values after each iteration checkbox.
 To specify that the statechart caches output values between iterations, remove the checkmark from this checkbox.
3. Click the OK button.

The new setting takes effect after you [generate code for the statechart](../lvschowto/sc_h_gencode.html).

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_scfromc.html language=enus -->
## TOPIC 00121: Calling a Statechart from C Code (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_scfromc.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_scfromc.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Calling a Statechart from C Code (Statechart Module)

Complete the following steps to prepare a [synchronous statechart](../lvscconcepts/sc_c_syncasync.html) that you can call using C code.

|  | Note To build a build a shared library (DLL) for the project, you must have the Application Builder installed. The LabVIEW Professional Development System includes the Application Builder. If you use the LabVIEW Base Development System or Full Development System, you can purchase the Application Builder separately by visiting the National Instruments Web site. |
| --- | --- |

1. Select File»New Project to display the Project Explorer window.
2. Right-click the My Computer item in the Project Explorer window and select Add»File from the shortcut menu.
3. Navigate to the .lvsc file for the statechart you want to call and click the Add File button to add the statechart to the project.
4. Select File»New VI to create a new VI. LabVIEW adds the new VI to the project.
5. Drag the .lvsc project item onto the block diagram to create a Run Statechart function that links to the appropriate statechart.
6. Right-click the Run Statechart function and select Link to Statechart from the shortcut menu to display the Link to Statechart dialog box.
7. Click the Browse button and navigate to the .lvsc file for the statechart you want to call.
8. Click the OK button.
 [IMAGE alt='image' src='note.gif']
**Note** You also can drag the .lvsc project item for the statechart from the **Project Explorer** window onto the block diagram to create a Run Statechart function that links to the appropriate statechart.
9. Right-click the Trigger input of the Run Statechart function and select Create»Control from the shortcut menu to create an enum control.
10. Right-click the Inputs input of the Run Statechart function and select Create»Control from the shortcut menu to create a control for the Inputs cluster.
11. Right-click the Init? input of the Run Statechart function and select Create»Control from the shortcut menu to create a Boolean control.
12. Right-click the Outputs output of the Run Statechart function and select Create»Indicator from the shortcut menu to create an indicator for the Outputs cluster.
13. Right-click the Terminated? output of the Run Statechart function and select Create»Indicator from the shortcut menu to create a Boolean indicator.
14. Press the <Ctrl-E> keys to display the front panel.
15. Right-click the VI icon in the upper right corner of the front panel window and select Show Connector from the shortcut menu to display the connector pane. The connector pane appears in place of the VI icon.
16. Assign terminals to each of the controls and indicators.
17. Select File»Save to save the VI.
18. From the Project Explorer window, select File»Save to save the project.
19. Build a shared library (DLL) for the project. Define the VI you save in step #17 as an exported VI in the shared library.

The DLL has the same functionality as the statechart. Using C code, obtain the function pointer to the address of the caller VI inside the DLL. You then can use the function pointer to call the statechart inside the DLL. You can use C code to supply the DLL with inputs and outputs. You also can use C code to specify when the statechart undergoes iterations.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_sendsignal.html language=enus -->
## TOPIC 00122: Sending Triggers to the Internal Queue of a Statechart (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_sendsignal.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_sendsignal.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Sending Triggers to the Internal Queue of a Statechart (Statechart Module)

Complete the following steps to send a [trigger](../lvscconcepts/sc_c_tga.html#trigger) to the [internal queue](../lvscconcepts/sc_c_trigqueue.html) of a statechart.

1. Place a Send Internal Trigger function on the block diagram of an action .
2. Click the Outputs cluster element, located on the left of this block diagram, to display a list of cluster elements.
3. Select the InternalQueue»All Elements element.
4. Repeat steps 2 and 3 for the Outputs cluster element located on the right side of the block diagram.
5. Wire the InternalQueue element to the Internal Queue In input of the Send Internal Trigger function.
6. Wire a trigger to the Trigger input of this function. The values in this list come from the triggers you create in the Edit Triggers and Groups dialog box.
 [IMAGE alt='image' src='tip.gif']
**Tip** You can obtain a list of valid triggers by right-clicking the **Trigger** input and selecting either **Create»Control** or **Create»Constant** from the shortcut menu.
7. Wire the Internal Queue Out output terminal to the InternalQueue cluster element on the right side of the block diagram.

The action now resembles the following figure:

[IMAGE alt='image' src='internalqueue.gif']

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_singlestep.html language=enus -->
## TOPIC 00123: Single-Stepping through a Statechart (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_singlestep.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_singlestep.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Single-Stepping through a Statechart (Statechart Module)

Single-stepping through a statechart works similarly to [single-stepping through a VI](/csh?topicname=lvhowto/single_step_mode.html). You can single-step through a statechart only when the **Pause** button [IMAGE alt='image' src='pausebutton.gif'], located on the toolbar of the **Statechart Debugging** window, is red. This button turns red after the statechart reaches a [breakpoint](sc_h_breakpoints.html) you placed. This button also turns red after you click the button, which means you can pause the statechart and begin single-stepping at any time.

|  | Tip You can start a statechart in single-stepping mode by clicking the Pause button before running the caller VI. |
| --- | --- |

Complete the following steps to single-step through a statechart:

1. Run the caller VI .
2. Right-click the Run Statechart function and select Debug Statechart . The statechart diagram appears in debugging mode, which means you cannot edit the diagram.
 [IMAGE alt='image' src='note.gif']
**Note** If you do not see the **Debug Statechart** option, you might have [disabled statechart debugging](sc_h_disabledebug.html). You must re-enable debugging and re-generate the code before proceeding.
3. Run the statechart until the statechart pauses at a breakpoint or until you click the Pause button.
4. Click one of the following buttons:
 Step Into —Executes the next transition or state action and then pauses, regardless of where that transition or state is in the statechart hierarchy. Use this button to step through an entire statechart hierarchy while pausing at each action.
 Step Over —Executes the next transition or state action and then pauses at the next transition or state that is at the same statechart hierarchy level. This behavior means that the Step Over button does not pause before executing substates of the current superstate . Conversely, the Step In button does pause in these situations. Use the Step Over button to step through an entire statechart hierarchy without pausing at substate actions.
 Step Out —Finishes executing the current transition or state action, returns to the superstate, and then pauses. Use this button to return to a superstate after having stepped into the substate(s) of that superstate.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_subdiag.html language=enus -->
## TOPIC 00124: Viewing a State as a Subdiagram (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_subdiag.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_subdiag.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Viewing a State as a Subdiagram (Statechart Module)

Viewing a [state](../lvsc/sc_state.html) as a [subdiagram](../lvscconcepts/sc_c_subsc.html) can simplify the visual appearance of the statechart diagram. Complete the following steps to view a state as a subdiagram.

1. Right-click the border of a state.
2. Select View as Subdiagram .

After you select this option, LabVIEW displays the contents of the state in a separate [Statechart Editor](../lvscconcepts/sc_c_editor.html) window, which you can close. To view this subdiagram again, right-click the state and select **Open Subdiagram**.

To view a state normally, right-click the state and select **View as Subdiagram** again to remove the checkmark from this menu item.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_tfork.html language=enus -->
## TOPIC 00125: Creating One Transition to Multiple Substates (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_tfork.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_tfork.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Creating One Transition to Multiple Substates (Statechart Module)

You can specify that a single [transition](../lvscconcepts/sc_c_trans.html) goes to multiple [substates](../lvscconcepts/sc_c_hierarchy.html) simultaneously. These destination substates must be in different [orthogonal regions](../lvscconcepts/sc_c_orthogonal.html), such as the following figure shows.

[IMAGE alt='image' src='fork_begin.gif']

In the previous figure, the statechart enters State 1, which then enters the substates State 2 and State 4 concurrently. The statechart enters these substates because the [Initial](../lvsc/sc_initial.html)
 [pseudostates](../lvscconcepts/sc_c_pseudocon.html) specify that these are the substates to execute first.

Consider what happens if the statechart takes the transition to State 6 and then returns to State 1. In this situation, the statechart enters States 2 and 4 again. However, you might want the statechart to enter States 3 and 5 instead. You can specify this behavior by creating a single transition that enters multiple substates.

Complete the following steps to create a single transition to multiple substates.

1. Place a Fork 
 connector above the regions in State 1.
 [IMAGE alt='image' src='add.gif'] Add
2. Create a transition from the incoming port to the Fork connector.
3. Create a transition from the Fork connector to State 3.
4. Create a transition from the Fork connector to State 5.

The statechart diagram now resembles the following figure.

[IMAGE alt='image' src='fork.gif']

In the previous figure, the behavior of the initial transition remains the same: the statechart enters states 2 and 4. However, if the statechart enters State 6 and then returns to State 1, the Fork connector specifies that the statechart enters States 3 and 5 instead of States 2 and 4.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_h_transprior.html language=enus -->
## TOPIC 00126: Setting Transition Priority (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_h_transprior.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_h_transprior.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### Setting Transition Priority (Statechart Module)

To set the priorities of [transitions](../lvscconcepts/sc_c_trans.html) that exit a [state](../lvsc/sc_state.html), right-click that state and select **Set Transition Priorities**. LabVIEW displays a set of black and white boxes at each outgoing transition. The process for setting transition priorities is similar to the process for [modifying the order of elements in a cluster](/csh?topicname=lvhowto/modifying_cluster_element.html).

|  | Note You can set transition priorities for only transitions that exit the selected state. Transitions that exit substates of this state are unaffected. To set the priorities of transitions that exit a substate, you must right-click the substate itself. |
| --- | --- |

You also can set transition priorities for transitions that exit a [Junction](../lvsc/sc_junction.html) connector.

<!--NI_TOPIC bundle=labview-statechart-module path=lvschowto/sc_howto.html language=enus -->
## TOPIC 00127: How-To (Statechart Module)

- bundle_id: `labview-statechart-module`
- source_path: `lvschowto/sc_howto.html`
- source_url: https://docs-be.ni.com/bundle/labview-statechart-module/raw/resource/enus/lvschowto/sc_howto.html
- document_id: `labview-statechart-module`
- page_type: `leaf`
- content_type: ``

### How-To (Statechart Module)

This book contains step-by-step instructions and other information that might be useful as you use the LabVIEW Statechart Module. Refer to the [Concepts](../lvscconcepts/sc_concepts.html) book to learn about related concepts.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |
