# NOMAGIC DOCUMENTATION SPACE: Enterprise Architect Import Plugin 2024x Refresh2

<!--NOMAGIC_SPACE key=EAI2024xR2 chunk=1 -->

<!--NOMAGIC_PAGE id=194643668 space=EAI2024xR2 version=1 -->
## PAGE 00001: Activity diagram elements

- page_id: `194643668`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643668/Activity+diagram+elements
- version_number: 1
- version_date: `2020-10-05T08:18:23.320+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Special Transformation
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

1401072400

#### CONTENT-COLUMN: Note

1401072403

1401072398

**On this page**

33

#### CONTENT-BLOCK: Note

1401072402

##### Activity

You can directly place an Activity element in EA as an element view on an Activity diagram. However, this behavior conflicts with MagicDraw and UML notation. In MagicDraw, if you drag an Activity from the containment tree to an Activity diagram, a new CallBehaviorAction view will be created and the 'Behavior' property of the CallBehaviorAction will be set to the Activity. This same behavior will be used in the import process.

An Activity element created in EA and placed on an Activity diagram will be transformed into two elements: Activity, and CallBehaviorAction elements. Both elements will have the same name and will be linked through the property of a CallBehaviorAction element called 'Behavior'.

After transforming the element, the following transformation message will open:

```text
: A new CallBehaviorAction was created and its Behavior was set to the element.]]>
```

[IMAGE alt='' src='']

###### An EA Activity.

[IMAGE alt='' src='']

###### An Activity with a New CallBehavior in MagicDraw.

#### NOTE: Note

Note

The EAActivityand CallBehaviorAction elements have similar characteristics in that you can attach a control flow toit and others. EAhas its own CallBehaviorAction element.

Additionally,any ObjectNode elements attached totheActivityelement will be transformed into InputPin elements and attached tothe newly created CallBehaviorAction element.

[IMAGE alt='' src='']

###### An ObjectNode converted into an InputPin.

##### Activity diagram

EveryActivityDiagram element from EAwill be placed inside anActivityelement thathas the same name.

[IMAGE alt='' src='']

###### The Activity diagram in the MagicDraw Containment tree.

#### NOTE: Note

Note

InMagicDraw,everyActivitydiagram element mustbe placed inside anActivity element thathas the same name. However, this is not the case in EA.

##### Object as the inner element of an Activity

Object elements inside an Activity element in EA will be removed.

[IMAGE alt='' src='']

###### Object elements transformation.

#### NOTE: Note

Note

Object elements in MagicDraw have their XMItypes defined as 'uml:Central- BufferNode'. However,those in EAhave their XMItypes defined as 'uml:InstanceSpecification', which do not belong toanActivitydiagram.

An Object element containing anyActivityDiagram-related elements will be removed.

[IMAGE alt='' src='']

###### An Object Containing Activity-related elements.

#### NOTE: Note

Note

InMagicDraw,an Object element (CentralBufferNode) is not allowed tocontainelements other than comments and hyperlinks.

##### Synch Node

A Synch element in EA will be transformed into a Join element in MagicDraw. It will look exactly like a Fork/Join element.

[IMAGE alt='' src='']

###### Synch element transformation.

#### NOTE: Note

Note

A MagicDraw Fork/Join element (whose type is uml:ForkNode) can be used to construct either a Fork and Join node in an Activity diagram. The JoinNode element (whose type is uml:JoinNode) is allowed to be placed in the Activity diagram, but the element’s image will be displayed as the Fork/Join element’s default image.

##### Activity Parameter

If you create an ActivityParameter element, MagicDraw will automatically create an ActivityParameterNode element to represent it. Every ActivityParameterNode element in EA will be transformed into a Pin element.

[IMAGE alt='' src='']

###### An Activity parameter node.

You can specify four parameter types for each Activity Parameter element: in, out, inout, and return.

The ActivityParameterNode element of an ActivityParameter element whose parameter type is either 'in' or 'inout' will be transformed into an InputPin element. The ActivityParameterNode element of an ActivityParameter element whose parameter type is either 'out' or 'return' will be transformed into an OutputPin element.

[IMAGE alt='' src='']

###### An Activity parameter Type.

#### NOTE: Note

Note

Usually, if you specify the parameter type of an ActivityParameter element as 'inout', two Pin elements (InputPin and OutputPin elements) will be created for the element. Since EA will only create one ActivityParameterNode element, this element will be transformed into an InputPin element.

##### Exception Handler

The Exception Handler element in EA differs from the UML’s ExceptionHandler. This EA element will be transformed into a CallBehaviorAction element. Any ObjectNode element attached to it will be transformed into an InputPin element and any InterruptFlow line will be transformed into an ExceptionHandler line in MagicDraw.

After completing the transformation, the following transformation messages will open:

```text
: EA ExceptionHandler is transformed to an CallBehaviorAction with and input pin.
Updated element : EA InterruptFlow was transformed to an ExceptionHandler.]]>
```

[IMAGE alt='' src='']

###### ExceptionHandler.

##### ObjectFlow

An ObjectFlow line whose ends are not attached to any of the following elements will be transformed into a ControlFlow.

- InputPin
- OutputPin
- ObjectNode
- CentralBufferNode
- DataStoreNode

After completing the transformation, the following transformation message will open:

```text
: uml:ObjectFlow updated to uml:ControlFlow.]]>
```

##### ExpansionRegion

Most of the elements placed inside any ExpansionRegion elements in EA will stay in their original place.

[IMAGE alt='' src='']

###### ExpansionRegion tree view.

However,if there is anyActivity,Swimlane, InterruptibleActivityRegion, StructuredActivityNode, LooNode, SequenceNode, ConditionalNode, or other ExpansionRegion contained within an ExpansionRegion, it will be placed within a dummyActivityelement.The created dummy will have the same name and will be placed atthe same level as the ExpansionRegion element.

[IMAGE alt='' src='']

###### Nested ExpansionRegion tree view.

After completing the transformation, the following transformation message will open:

```text
: ExpansionRegion cannot contain some inner elements.
An Activity with the same name as the ExpansionRegion was created to contain inner elements.]]>
```

##### InterruptibleActivityRegion

Most of the elements placed inside an InterruptibleActivityRegion element in EA will be placed at the same level as the InterruptibleActivityRegion element.

[IMAGE alt='' src='']

###### InterruptibleActivityRegion tree view.

However,if there is anyActivity,Swimlane, ExpansionRegion, StructuredActivityNode, LoopNode, SequenceNode, ConditionalNode, or other InterruptibleActivityRegion contained within an InterruptibleActivityRegion, it will be placed within a dummyActivity.The created dummy will have the same name and will be placed atthe same level as the InterruptibleActivityRegion.

[IMAGE alt='' src='']

###### Nested InterruptibleActivityRegion tree view.

After completing the process, the following transformation message will open:

```text
: InterruptibleActivityRegion cannot contain some inner elements.
An Activity with the same name as the InterruptibleActivityRegion was created to contain inner elements.]]>
```

##### Swimlane

Most of the elements placed inside any Swimlane element in EA will be placed at the same level as the Swimlane element.

[IMAGE alt='' src='']

###### Swimlane tree view.

A dummy Activity will also be created to hold any other Swimlanes that it may contain. The dummy Activity will have the same name and will be placed at the same level as the Swimlane.

If two or more Swimlanes are nested together, then every element (except Swimlane element) contained within either of them will be placed at the same level as the Swimlane topping the nested-Swimlane-elements hierarchy.

[IMAGE alt='' src='']

###### Nested Swimlane tree view.

After completing the process, the following transformation message will open:

```text
: Swimlane cannot contain some inner elements.
The XMI structure was fixed.]]>
```

##### StructuredActivity

Four elements are classified as Structured Activity elements in EA:

- StructuredActivityNode element
- LoopNode element
- SequenceNode element
- ConditionalNode element

Most of the elements placed inside any StructuredActivityNode, LoopNode, SequenceNode, or ConditionalNode elements in EA will stay in their original place.

[IMAGE alt='' src='']

###### StructuredActivityNode tree view.

However, if there is any Activity, Swimlane, InterruptibleActivityRegion, ExpansionRegion, or another StructuredActivity contained within a StructuredActivity, it will be placed within a dummy Activity. The created dummy will have the same name, and will be placed at the same level as the StructuredActivity.

[IMAGE alt='' src='']

###### Nested StructuredActivityNode tree view.

After completing the process, the following transformation messages will open, depending on the Structured Activity elements involved:

```text
: StructuredActivityNode cannot contain some inner elements. An Activity with the same name as the StructuredActivityNode was created to contain inner elements.
Updated element : ConditionalNode cannot contain some inner elements. An Activity with the same name as the ConditionalNode was 
created to contain inner elements.
Updated element : LoopNode cannot contain some inner elements. An Activity with the same name as the LoopNode was created to contain inner elements.
Updated element : SequenceNode cannot contain some inner elements. An Activity with the same name as the SequenceNode was created to contain inner elements.]]>
```

##### InterruptFlow

In some cases, EA InterruptFlows are ControlFlow lines. Their image will be displayed as the InterruptFlow line in the Activity diagram. An InterruptFlow is not a ControlFlow line if the InterruptFlow line is drawn from one element in an InterruptibleActivityRegion to another outside the InterruptibleActivityRegion. In an XMI file, this line will be imported as a ControlFlow line, and its image will be changed to that of the ControlFlow line.

However, if either end of the line is any of the following elements, it will be transformed into an ObjectFlow line.

- InputPin element
- OutputPin element
- ObjectNode element
- CentralBufferNode element
- DataStoreNode element

[IMAGE alt='' src='']

###### InterruptFlow.

##### ExpansionNode

An ExpansionNode is a Pin which can only be contained within an ExpansionRegion and will be imported like any other Pin elements. However, if an ExpansionNode in EA is created inside another element rather than an ExpansionRegion, that particular ExpansionNode will not be imported.

[IMAGE alt='' src='']

###### ExpansionNode.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d8ed03b3-28e4-47c1-9483-fc5a3300ffb1"><ac:parameter ac:name="id">1401072400</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="29b9096e-1474-4ee7-9690-ab6a82436e0a"><ac:parameter ac:name="id">1401072403</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="aee8a522-8c5b-45da-802d-644771183ef7"><ac:parameter ac:name="id">1401072398</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="ef9c4f51-abfc-4368-a1ea-4714a782adcf"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0ef54d9c-0b4f-4ecc-96d0-17cd62b6810c"><ac:parameter ac:name="id">1401072402</ac:parameter><ac:rich-text-body><h3>Activity</h3><p>You can directly place an Activity element in EA as an element view on an Activity diagram. However, this behavior conflicts with MagicDraw and UML notation. In MagicDraw, if you drag an Activity from the containment tree to an Activity diagram, a new CallBehaviorAction view will be created and the 'Behavior' property of the CallBehaviorAction will be set to the Activity. This same behavior will be used in the import process.</p><p>An Activity element created in EA and placed on an Activity diagram will be transformed into two elements: Activity, and CallBehaviorAction elements. Both elements will have the same name and will be linked through the property of a CallBehaviorAction element called 'Behavior'.</p><p>After transforming the element, the following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="818c35a3-e5f9-4007-adaf-4b0b226ae431"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: A new CallBehaviorAction was created and its Behavior was set to the element.]]></ac:plain-text-body></ac:structured-macro><p><ac:image ac:align="center"><ri:attachment ri:filename="EA_activities.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An EA Activity.</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="activity_withcallbehavior.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Activity with a New CallBehavior in MagicDraw.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2c6395e5-0cdb-42ab-b3f9-ba7b27e9d86e"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p><span>The EA<span> </span>Activity<span> </span>and CallBehaviorAction elements have similar characteristics in that you can attach a control flow to<span> </span>it and others. EA<span> </span>has its own CallBehaviorAction element.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span>Additionall<span>y</span>,<span> </span>any ObjectNode elements attached to<span> </span>the<span> </span>Activity<span> </span>element will be transformed into InputPin elements and attached to<span> </span>the newly created CallBehaviorAction element.</span></p><p><span><ac:image ac:align="center"><ri:attachment ri:filename="objectNode_toInputPin.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image><br /></span></p><h6 style="text-align: center;"><span>An ObjectNode converted into an InputPin.</span></h6><h3>Activity diagram</h3><p><span>Every<span> </span>Activity<span> </span>Diagram element from EA<span> </span>will be placed inside an<span> </span>Activity<span> </span>element that<span> </span>has the same name.</span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Activityplacement_inMD.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The Activity diagram in the MagicDraw Containment tree.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6b03c020-9f05-4a19-b923-5f7e3b7976c0"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p><span>In<span> </span>MagicDra<span>w</span>,<span> </span>every<span> </span>Activity<span> </span>diagram element must<span> </span>be placed inside an<span> </span>Activity element that<span> </span>has the same name. However, this is not the case in EA.</span></p></ac:rich-text-body></ac:structured-macro><h3>Object as the inner element of an Activity</h3><p>Object elements inside an Activity element in EA will be removed.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="objectElements.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Object elements transformation.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f4f7163f-8dcb-44bd-b689-a03f6c39f5c1"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p><span>Object elements in MagicDraw have their XMI<span> </span>types defined as 'uml:Central- Bu<span>f</span>ferNode'. However,<span> </span>those in EA<span> </span>have their XMI<span> </span>types defined as 'uml:InstanceSpecification', which do not belong to<span> </span>an<span> </span>Activity<span> </span>diagram.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span>An Object element containing any<span> </span>ActivityDiagram-related elements will be removed.</span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="activityelements_inObject.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Object Containing Activity-related elements.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bf838990-8395-4eed-9ce2-53a47622c801"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p><span>In<span> </span>MagicDra<span>w</span>,<span> </span>an Object element (CentralBu<span>f</span>ferNode) is not allowed to<span> </span>contain </span><span>elements other than comments and hyperlinks.</span></p></ac:rich-text-body></ac:structured-macro><h3>Synch Node</h3><p class="auto-cursor-target">A Synch element in EA will be transformed into a Join element in MagicDraw. It will look exactly like a Fork/Join element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="synchElement.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Synch element transformation.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d813c350-a6e7-45fe-be4a-b570b8058ff7"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>A MagicDraw Fork/Join element (whose type is uml:ForkNode) can be used to construct either a Fork and Join node in an Activity diagram. The JoinNode element (whose type is uml:JoinNode) is allowed to be placed in the Activity diagram, but the element’s image will be displayed as the Fork/Join element’s default image.</p></ac:rich-text-body></ac:structured-macro><h3>Activity Parameter</h3><p class="auto-cursor-target">If you create an ActivityParameter element, MagicDraw will automatically create an ActivityParameterNode element to represent it. Every ActivityParameterNode element in EA will be transformed into a Pin element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="actParameternode.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Activity parameter node.</h6><p>You can specify four parameter types for each Activity Parameter element: in, out, inout, and return.</p><p>The ActivityParameterNode element of an ActivityParameter element whose parameter type is either 'in' or 'inout' will be transformed into an InputPin element. The ActivityParameterNode element of an ActivityParameter element whose parameter type is either 'out' or 'return' will be transformed into an OutputPin element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="actParametertype.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Activity parameter Type.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4277f2fc-bc39-45cc-8ea8-f6ed3d7c6e17"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>Usually, if you specify the parameter type of an ActivityParameter element as 'inout', two Pin elements (InputPin and OutputPin elements) will be created for the element. Since EA will only create one ActivityParameterNode element, this element will be transformed into an InputPin element.</p></ac:rich-text-body></ac:structured-macro><h3>Exception Handler</h3><p>The Exception Handler element in EA differs from the UML’s ExceptionHandler. This EA element will be transformed into a CallBehaviorAction element. Any ObjectNode element attached to it will be transformed into an InputPin element and any InterruptFlow line will be transformed into an ExceptionHandler line in MagicDraw.</p><p><br /></p><p>After completing the transformation, the following transformation messages will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ab8bb5ed-f75d-4fff-81bb-c62c65ee41ae"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: EA ExceptionHandler is transformed to an CallBehaviorAction with and input pin.
Updated element <xmi:id>: EA InterruptFlow was transformed to an ExceptionHandler.]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="exceptionHandler.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">ExceptionHandler.</h6><h3>ObjectFlow</h3><p>An ObjectFlow line whose ends are not attached to any of the following elements will be transformed into a ControlFlow.</p><ul><li>InputPin</li><li>OutputPin</li><li>ObjectNode</li><li>CentralBufferNode</li><li>DataStoreNode</li></ul><p>After completing the transformation, the following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="0f371b79-8583-415c-b6d9-a968a484103b"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: uml:ObjectFlow updated to uml:ControlFlow.]]></ac:plain-text-body></ac:structured-macro><h3>ExpansionRegion</h3><p>Most of the elements placed inside any ExpansionRegion elements in EA will stay in their original place.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="expansionregion_tree.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">ExpansionRegion tree view.</h6><p><span>Howeve<span>r</span>,<span> </span>if there is any<span> </span>Activit<span>y</span>,<span> </span>Swimlane, InterruptibleActivityRegion, StructuredActivityNode, LooNode, SequenceNode, ConditionalNode, or other ExpansionRegion contained within an ExpansionRegion, it will be placed within a dummy<span> </span>Activity<span> </span>element.<span> </span>The created dummy will have the same name and will be placed at<span> </span>the same level as the ExpansionRegion element.</span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="nestedExpansionregion_tree.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(112,112,112);">Nested ExpansionRegion tree view.</span></h6><p>After completing the transformation, the following transformation message will open: </p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="0ecd3997-297e-4f62-abe1-491c0ae035af"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: ExpansionRegion cannot contain some inner elements.
An Activity with the same name as the ExpansionRegion was created to contain inner elements.]]></ac:plain-text-body></ac:structured-macro><h3>InterruptibleActivityRegion</h3><p>Most of the elements placed inside an InterruptibleActivityRegion element in EA will be placed at the same level as the InterruptibleActivityRegion element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="interruptibleActivityregion_tree.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">InterruptibleActivityRegion tree view.</h6><p><span>Howeve<span>r</span>,<span> </span>if there is any<span> </span>Activit<span>y</span>,<span> </span>Swimlane, ExpansionRegion, StructuredActivityNode, LoopNode, SequenceNode, ConditionalNode, or other InterruptibleActivityRegion contained within an InterruptibleActivityRegion, it will be placed within a dummy<span> </span>Activit<span>y</span>.<span> </span>The created dummy will have the same name and will be placed at<span> </span>the same level as the InterruptibleActivityRegion.</span></p><p style="text-align: center;"><span><ac:image ac:align="center"><ri:attachment ri:filename="nestedInterruptibleActivity_tree.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;">Nested InterruptibleActivityRegion tree view.</h6><p>After completing the process, the following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="fb4c3bf2-f999-49e6-ba02-86051c5b33ae"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: InterruptibleActivityRegion cannot contain some inner elements.
An Activity with the same name as the InterruptibleActivityRegion was created to contain inner elements.]]></ac:plain-text-body></ac:structured-macro><h3>Swimlane</h3><p>Most of the elements placed inside any Swimlane element in EA will be placed at the same level as the Swimlane element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="swimlane_tree.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Swimlane tree view.</h6><p>A dummy Activity will also be created to hold any other Swimlanes that it may contain. The dummy Activity will have the same name and will be placed at the same level as the Swimlane.</p><p>If two or more Swimlanes are nested together, then every element (except Swimlane element) contained within either of them will be placed at the same level as the Swimlane topping the nested-Swimlane-elements hierarchy.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="nestedSwimlane_tree.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Nested Swimlane tree view.</h6><p>After completing  the process, the following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f8561cb0-0105-4202-b570-329f1699c9fb"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: Swimlane cannot contain some inner elements.
The XMI structure was fixed.]]></ac:plain-text-body></ac:structured-macro><h3>StructuredActivity</h3><p>Four elements are classified as Structured Activity elements in EA:</p><ul><li>StructuredActivityNode element</li><li>LoopNode element</li><li>SequenceNode element</li><li>ConditionalNode element</li></ul><p>Most of the elements placed inside any StructuredActivityNode, LoopNode, SequenceNode, or ConditionalNode elements in EA will stay in their original place.</p><p style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="structuredActivitynode_tree.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">StructuredActivityNode tree view.</h6><p>However, if there is any Activity, Swimlane, InterruptibleActivityRegion, ExpansionRegion, or another StructuredActivity contained within a StructuredActivity, it will be placed within a dummy Activity. The created dummy will have the same name, and will be placed at the same level as the StructuredActivity.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="nestedStructuredActnode_tree.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(112,112,112);">Nested StructuredActivityNode tree view.</span></h6><p>After completing the process, the following transformation messages will open, depending on the Structured Activity elements involved:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="fae2d861-d0bc-46b5-a431-54120d4dcb11"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: StructuredActivityNode cannot contain some inner elements. An Activity with the same name as the StructuredActivityNode was created to contain inner elements.
Updated element <xmi:id>: ConditionalNode cannot contain some inner elements. An Activity with the same name as the ConditionalNode was 
created to contain inner elements.
Updated element <xmi:id>: LoopNode cannot contain some inner elements. An Activity with the same name as the LoopNode was created to contain inner elements.
Updated element <xmi:id>: SequenceNode cannot contain some inner elements. An Activity with the same name as the SequenceNode was created to contain inner elements.]]></ac:plain-text-body></ac:structured-macro><h3>InterruptFlow</h3><p>In some cases, EA InterruptFlows are ControlFlow lines. Their image will be displayed as the InterruptFlow line in the Activity diagram. An InterruptFlow is not a ControlFlow line if the InterruptFlow line is drawn from one element in an InterruptibleActivityRegion to another outside the InterruptibleActivityRegion. In an XMI file, this line will be imported as a ControlFlow line, and its image will be changed to that of the ControlFlow line.</p><p>However, if either end of the line is any of the following elements, it will be transformed into an ObjectFlow line.</p><ul><li>InputPin element</li><li>OutputPin element</li><li>ObjectNode element</li><li>CentralBufferNode element</li><li>DataStoreNode element</li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="interruptFlow.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">InterruptFlow.</h6><h3>ExpansionNode</h3><p>An ExpansionNode is a Pin which can only be contained within an ExpansionRegion and will be imported like any other Pin elements. However, if an ExpansionNode in EA is created inside another element rather than an ExpansionRegion, that particular ExpansionNode will not be imported.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="expansionNode.png"><ri:page ri:content-title="Activity diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">ExpansionNode.</h6></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643714 space=EAI2024xR2 version=1 -->
## PAGE 00002: Communication diagram elements

- page_id: `194643714`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643714/Communication+diagram+elements
- version_number: 1
- version_date: `2020-10-05T08:27:24.421+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Special Transformation
- labels: []

### NORMALIZED CONTENT

1402052451

1402052462

1402052450

**On this page**

43

1402052452

##### Object, Boundary, Entity, and Control

All Object, Boundary, Entity, Control elements in EA are InstanceSpecifications. After conversion, their UML element types will remain, and a Lifeline and an OwnedAttribute element will be created to represent each of them in the Communication diagram in which they occur.

[IMAGE alt='' src='']

###### Object, Boundary, Entity, and Control (diagram view).

###### [IMAGE alt='' src='']

###### Object, Boundary, Entity, and Control (Containment tree).

Other elements that can be drawn in a Communication diagram will be handled in a similar manner.

##### Exception elements

Some of the elements that can be drawn in a Communication diagram using EA are not supported by MagicDraw. Consequently, their displaying parts will not be imported. These elements include Package, Activity, Action, DiagramFrame, State, Interaction, ExceptionHandler, CentralBufferNode, InterruptibleActivityRegion, MergeNode, Trigger, ExpansionRegion, and InteractionFragment.

[IMAGE alt='' src='']

###### Exception elements.

###### Realization and Nesting

The Realization element type in EA is 'uml:Realization'. The Nesting element type in EA is exported in XMI as *uml:Dependency*. The Realization and Nesting lines in EA are not supported in the Communication diagram; therefore, only their model data will be imported, not the displaying parts.

[IMAGE alt='' src='']

###### Realization and Nesting.

##### Association

Every Association relationship drawn in a Communication diagram in EA will have a Connector line created for each of them. The elements attached to both ends of the Association line will have a Lifeline element created to represent each of them. The Association lines and the elements attached to them will not be removed. However, the elements that will be shown in the MagicDraw diagram frame will be the Lifeline elements and the Connector lines created to represent them.

[IMAGE alt='' src='']

[IMAGE alt='' src='']

###### Association.

If an Association line is connected to the InstanceSpecification elements, its data will be removed. If an Association line is linked between two InstanceSpecification elements, it will be transformed into an InstanceSpecification element. This is one of the constraints belonging to the Communication diagram.

[IMAGE alt='' src='']

[IMAGE alt='' src='']

###### Association Line between InstanceSpecifications.

##### Message

Messages can be created on Connectors and will be imported to MagicDraw.

[IMAGE alt='' src='']

###### Message.

##### Operations

An InstanceSpecification cannot contain Operation elements. If the XMI file from EA has some InstanceSpecification elements containing Operation elements, those Operations will be removed.

[IMAGE alt='' src='']

###### Operations.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="6f963810-754d-4e6e-98a8-582a3755178d"><ac:parameter ac:name="id">1402052451</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="6090926f-a58c-4bce-9213-6fba5f5df6a8"><ac:parameter ac:name="id">1402052462</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f1539e92-6984-4c58-b259-f83fa04d6da9"><ac:parameter ac:name="id">1402052450</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="fa06c9b5-57f5-45ef-b068-02cc9b4ca22f"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8d0dca89-c8a1-48b2-82a5-99d9e18ea52e"><ac:parameter ac:name="id">1402052452</ac:parameter><ac:rich-text-body><h3>Object, Boundary, Entity, and Control</h3><p>All Object, Boundary, Entity, Control elements in EA are InstanceSpecifications. After conversion, their UML element types will remain, and a Lifeline and an OwnedAttribute element will be created to represent each of them in the Communication diagram in which they occur.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="obj_bound_entity_control.png"><ri:page ri:content-title="Communication diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Object, Boundary, Entity, and Control (diagram view).</h6><h6><ac:image ac:align="center"><ri:attachment ri:filename="obj_bound_entity_controltree.png"><ri:page ri:content-title="Communication diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></h6><h6 style="text-align: center;">Object, Boundary, Entity, and Control (Containment tree).</h6><p>Other elements that can be drawn in a Communication diagram will be handled in a similar manner.</p><h3>Exception elements</h3><p>Some of the elements that can be drawn in a Communication diagram using EA are not supported by MagicDraw. Consequently, their displaying parts will not be imported. These elements include Package, Activity, Action, DiagramFrame, State, Interaction, ExceptionHandler, CentralBufferNode, InterruptibleActivityRegion, MergeNode, Trigger, ExpansionRegion, and InteractionFragment.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="exceptionElement.png"><ri:page ri:content-title="Communication diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Exception elements.</h6><h4>Realization and Nesting</h4><p>The Realization element type in EA is 'uml:Realization'. The Nesting element type in EA is exported in XMI as <em>uml:Dependency</em>. The Realization and Nesting lines in EA are not supported in the Communication diagram; therefore, only their model data will be imported, not the displaying parts.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="realization_nesting.png"><ri:page ri:content-title="Communication diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Realization and Nesting.</h6><h3>Association</h3><p>Every Association relationship drawn in a Communication diagram in EA will have a Connector line created for each of them. The elements attached to both ends of the Association line will have a Lifeline element created to represent each of them. The Association lines and the elements attached to them will not be removed. However, the elements that will be shown in the MagicDraw diagram frame will be the Lifeline elements and the Connector lines created to represent them.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="association_beforeconversion.png"><ri:page ri:content-title="Communication diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="association_afterconversion.png"><ri:page ri:content-title="Communication diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Association.</h6><p>If an Association line is connected to the InstanceSpecification elements, its data will be removed. If an Association line is linked between two InstanceSpecification elements, it will be transformed into an InstanceSpecification element. This is one of the constraints belonging to the Communication diagram.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="assocline_beforeconversion.png"><ri:page ri:content-title="Communication diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="assocline_afterconversion.png"><ri:page ri:content-title="Communication diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Association Line between InstanceSpecifications.</h6><h3>Message</h3><p>Messages can be created on Connectors and will be imported to MagicDraw. </p><p><ac:image ac:align="center"><ri:attachment ri:filename="message.png"><ri:page ri:content-title="Communication diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Message.</h6><h3>Operations</h3><p>An InstanceSpecification cannot contain Operation elements. If the XMI file from EA has some InstanceSpecification elements containing Operation elements, those Operations will be removed.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="operations.png"><ri:page ri:content-title="Communication diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Operations.</h6></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643743 space=EAI2024xR2 version=1 -->
## PAGE 00003: Composite structure diagrams

- page_id: `194643743`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643743/Composite+structure+diagrams
- version_number: 1
- version_date: `2020-10-05T08:50:09.167+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Special Transformation
- labels: []

### NORMALIZED CONTENT

1402619655

1402619658

1402619653

**On this page**

43

1402619657

This section presents additional EA specific Composite Structure diagram information.

##### Import elements

EA differs from MagicDraw in the Composite Structure diagram's content elements design. The table below shows the differences by focusing on the EA’s elements and how they will be transformed or converted into a format MagicDraw can correctly load and display. The element names shown in the table are the same in both EA and MagicDraw's GUI. The contents in the brackets ([…]) are the XMI element type references.

| Enterprise Architect | MagicDraw |
| --- | --- |
| Interaction |  |
| Class [uml:Class] | Class [uml:Class] |
| Interface [uml:Interface] | Interface [uml:Interface] |
| Part [uml:Class]Part [uml:Property] | Part [uml:Property] |
| Port [uml:Port] | Port [uml:Port] |
| Collaboration [uml:Collaboration] | Collaboration Use [uml:Collaboration] |
| Expose Interface [does not exist] |  |
| Connector [element type does not exist] | Connector [uml:Connector] |
| Assembly [element type does not exist] |  |
| Delegate [element type does not exist] | Connector [uml:Connector] |
| Role Binding [uml:Dependency] | Role Binding [uml:Dependency] |
| Represents [uml:Dependency] | Dependency [uml:Dependency] |
| Occurrence [uml:Dependency] | Dependency [uml:Dependency] |

##### Conversion details

###### Dummy class

In MagicDraw, the Composite Structure diagram needs a Context element to contain itself. However, in EA there is no Context element. After conversion, a dummy Class element will be created to represent the Context element of the Composite Structure diagram.

A dummy Class will be named after the closest owner package of the Composite Structure diagram. The Composite Structure diagram and all of the Composite Structure elements will be placed inside the dummy Class element.

[IMAGE alt='' src='']

###### A Dummy Class.

###### Class

The Class element data will be normally copied even if the Class element is drawn in a Composite Structure diagram. A Property element will be created to represent the Class element. The Property element will be named after the Class element.

[IMAGE alt='' src='']

###### A Property element representing a Class element.

###### Class with attributes and operations

The Class view in EA will be converted to a Part in MagicDraw. Attributes and operations will not be shown in the Composite Structure diagram.

[IMAGE alt='' src='']

###### A Part element after conversion.

###### Interface

The Interface element data will be normally copied even if the Interface element is drawn in a Composite Structure diagram. A Property element will be created to represent the Interface element. The Property element will be named after the Interface element.

[IMAGE alt='' src='']

###### A Property element representing an Interface element.

###### Part

There are two types of Parts: (i) Parts with Ports; and (ii) Parts that set type to other elements.

###### Parts with Ports

If you assign the type of a Part element to a Class, Component, or Node, the Part element can have a [CONFLUENCE_PAGE title='Composite structure diagrams' space='EAI2024xR2']. If a Part is not nested to any element, the Part element will be exported from EA as a Class. Therefore, this Part element can have a Port.

[IMAGE alt='' src='']

###### A Part that does not nest element(s) with Ports.

If a Part is nested to an element, and the type is not set, then the Part type will be used to set type to a dummy Class. This particular Part can have a Port. A dummy Class will be created at the same level of the Part element that sets type to it. The dummy Class will be named after the Part concatenated with '_type'.

[IMAGE alt='' src='']

###### A Part that nests element(s) with Ports.

###### Parts that set type to other elements

The type of a Part can be set to another element, e.g., Class, Actor, Component, and Usecase, by right-clicking the Part element and selecting **Advanced**> **Set Property Type**> **Select Property Type.**

[IMAGE alt='' src='']

###### Setting Part Type.

If the Part type is set to a type that cannot be the owner of a Port, the Port will be removed.

In MagicDraw, the Property element data cannot have any elements. However, in EA, it can have elements. Therefore, if you draw a Part element and it has an element inside it, that particular element will be relocated to an element, which is the Part type.

If a Part is not nested to any element, the Part element will be exported from EA as a Class. The element inside the Part will not be relocated. If that particular Part assigns a type to other elements, its type will always be set to Class.

[IMAGE alt='' src='']

###### A Part that sets type to other elements.

If a nested Part whose type is set to another element, e.g., Class, Actor, and Usecase, and this Part contains nested elements, all of the nested elements of the Part will be relocated to the element that is the type of this Part.

[IMAGE alt='' src='']

###### A Part that sets Type to other elements has nested elements inside itself.

###### portPort

In MagicDraw, a Property element that can have a Port is the Property that sets type to a Class, Component, or Node, and other elements cannot have a Port. However, in EA, most of the elements can have a Port.

If a Port is created with an element that is not a Class, Component or Node, the Port will be removed from the diagram view. However, its data will be preserved.

[IMAGE alt='' src='']

###### Only Class, Component, and Node can have a Port.

The following transformation message will open:

```text
: Invalid Port. Port can be added to Part that its type is set to Class, Component and Node only.]]>
```

###### Ports whose type is set to other elements

You can set the type of Port element to another element, e.g., Class, Actor, Component, and Usecase, by right-clicking the Port element and selecting **Advanced**> **Set Property Type**> **Select Property Type**.

**[IMAGE alt='' src='']**

###### Setting Port Type.

###### Port whose type is set to another element and containing Expose Interfaces

If an Expose Interface is created on a Port, and the Port type is set to another element, the Expose Interface data will be relocated to the Port's type element. For example, if the Port1 type is set to Actor, an Interface Realization (the Expose Interface data) will be placed inside the Actor after conversion.

[IMAGE alt='' src='']

###### A Port that sets Type to other elements contains an Expose Interface.****

###### Collaboration

The Collaboration element data and its nested data will normally be copied. However, if the Collaboration element is drawn in a Composite Structure diagram, a Collaboration use element will be created to represent the Collaboration element. The Collaboration use element will be named after the Collaboration element.

[IMAGE alt='' src='']

###### A Collaboration use element.

**Collaboration containing other elements**

A Collaboration can contain only Property, Activity, State Machine, and Interaction. Elements other than these will be removed. If any element is drawn inside the Collaboration, it will be removed from the diagram view.

[IMAGE alt='' src='']

###### A Collaboration containing other elements.

The following transformation messages will open:

```text
: Invalid Element. Collaboration can contain Property, Activity, State Machine and Interaction only.
Removed view : Invalid Element view. Collaboration cannot be contained in any element view.]]>
```

###### Expose Interface

Expose Interfaces are the provided and required interfaces in MagicDraw.

In MagicDraw, you can draw a provided Interface or required Interface in a Port only and set the type of the Port to another element, e.g., Actor, Usecase, and Class. You can create that particular Port on a Part element whose type is set to a Class, Component, or Node only.

###### Expose Interface with Ports

If you draw an Expose Interface in a Port, and the Port does not assign a Type to any elements, that particular Port will be used to set Type to a Dummy Class. The Dummy Class will be created and named after the Port concatenated with '_type'. The Interface element will be moved to the same level of the Port.

[IMAGE alt='' src='']

###### An Expose Interface with a Port.

If an Expose Interface is created on a Port, and the Type of the Port is set to another element, the Expose Interface data will be relocated to the Port's Type element (see (ii) Port whose type is set to another element and containing Expose Interfaces for more information).

In MagicDraw, some elements can be used as a Port Type. These elements can have either a provided Interface or required Interface, or both.

The following list shows the Port's Type elements with specific conditions:

- Interfaces can only have a provided Interface.
- Artifacts cannot have a provided Interface.
- Information Items cannot have a provided Interface.
- Signals cannot have a provided Interface.
- Components always have both provided and required Interfaces.
- The other elements can have both provided and required Interfaces.
- After conversion, if the type of a Port is set to an Interface and the Port has an Expose Interface, only the provided Interface will be shown and the Interface Realization data will be removed.
- Artifacts, Information Items, and Signals cannot hold Interface Realization. If the type of a Port is set to one of them, the provided Interface will be removed. However, this does not affect the required Interface.
- If the Type of a Port is set to a Component, and the Port has an Expose Interface, it will always show both the provided and required Interfaces.

###### [IMAGE alt='' src='']

###### The Type element of a Port with specific conditions.

The following transformation message will open:

```text
: Provided Interface conflicts with Port type.
The Port type is updated to an owner of Interface Realization.]]>
```

If an Expose Interface is created with an element that is not a Port, the element will be removed both from the Containment tree and diagram view.

[IMAGE alt='' src='']

###### An Expose Interface with the element that is not a Port.

The following transformation message will open:

```text
: Invalid Element. Expose Interface can be added to Port only.]]>
```

###### Expose Interface with Relationships

In MagicDraw, the provided and required Interfaces cannot be connected with any Relationship, as shown in the figure below. If there is any Relationship connecting to the Expose Interface, it will be removed from both the Containment tree and diagram view.

[IMAGE alt='' src='']

###### An Expose Interface with Lines.

The following transformation message will open:

```text
: Invalid Element. Expose Interface cannot be connected with the element.]]>
```

###### Package

In MagicDraw, a Package cannot be drawn in a Composite Structure diagram. If it is drawn in EA, it will be removed from the diagram once it has been converted to MagicDraw.

[IMAGE alt='' src='']

###### A Package element.

###### Assembly

In MagicDraw, there is no Assembly Line. It will be updated to a Connector.

The following transformation message will open:

```text
: Assembly updated to Connector.]]>
```

[IMAGE alt='' src='']

###### Updating the Assembly Line to the Connector Line.

###### Dependency

There are many relationships that EA exporter exports to Dependency as the following elements:

- Delegate
- Role Binding
- Represents
- Occurrence
- Nest
- Derive
- Import
- Instantiate
- Usage
- Realize
- Trace

The Relationships above will be shown in the diagram view as Dependencies with stereotype.

###### Removed relationships

If an Association, Direct Association, Aggregation, Composition, Generalization, or Specialization is created in a Composite Structure diagram, it will be removed from the diagram view, but its data will be preserved.

**[IMAGE alt='' src='']**

###### Removing Lines.

The following transformation messages will open:

```text
: Association cannot be shown in Composite Structure diagram.
Removed view : Direct Association cannot be shown in Composite Structure diagram.
Removed view : Aggregation cannot be shown in Composite Structure diagram.
Removed view : Composition cannot be shown in Composite Structure diagram.
Removed view : Generalization cannot be shown in Composite Structure diagram.]]>
```

##### Transformation report

A report containing the conflicts solved during transformation, along with other transformation information, e.g., special mapping and removal of some irrelevant data, is required to be provided for the users.

The following list shows the transformation messages:

```text
: Invalid Port. Port can be added to Part that set type to Class, Component, and Node only.
Removed element : Invalid Element. Collaboration can contain Property, Activity, State Machine, and Interaction only.
Removed view : Collaboration cannot be contained in any element view.
Removed view : UseCase cannot be contained in any element view.
Removed element : Invalid Element. Expose Interface can be added to Port only.
Removed element : Invalid Element. Expose Interface cannot be connected with the element.
Updated element : Assembly updated to Connector.
Updated element : Provided Interface conflicts with Port type. The Port type is updated to an owner of Interface Realization.
Removed view : Association cannot be shown in CompositeStructure diagram.
Removed view : Direct Association cannot be shown in Composite Structure diagram.
Removed view : Aggregation cannot be shown in Composite Structure diagram.
Removed view : Composition cannot be shown in Composite Structure diagram.
Removed view : Generalization cannot be shown in Composite Structure diagram.]]>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="7fb256bc-f60c-4cdf-a06f-8be6014a911d"><ac:parameter ac:name="id">1402619655</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="96b06bb8-8164-44ac-9f72-aabe01051ff6"><ac:parameter ac:name="id">1402619658</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="491f28b4-cc6a-494d-ae4e-8624b41bf725"><ac:parameter ac:name="id">1402619653</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f5e11967-3883-444f-a5a5-da3ceb0ff423"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0cf3d4e9-6497-48fa-85e9-cebac92078e1"><ac:parameter ac:name="id">1402619657</ac:parameter><ac:rich-text-body><p>This section presents additional EA specific Composite Structure diagram information.</p><h3>Import elements</h3><p>EA differs from MagicDraw in the Composite Structure diagram's content elements design. The table below shows the differences by focusing on the EA’s elements and how they will be transformed or converted into a format MagicDraw can correctly load and display. The element names shown in the table are the same in both EA and MagicDraw's GUI. The contents in the brackets ([…]) are the XMI element type references.</p><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Enterprise Architect</th><th>MagicDraw</th></tr><tr><td>Interaction</td><td><br /></td></tr><tr><td><span>Class [uml:Class]</span></td><td><span>Class [uml:Class] </span></td></tr><tr><td><span>Interface [uml:Interface]</span></td><td><p>Interface [uml:Interface]</p></td></tr><tr><td><p>Part [uml:Class]</p><p>Part [uml:Property]</p></td><td><p>Part [uml:Property]</p></td></tr><tr><td><span>Port<span> </span>[uml:Port]</span></td><td><span>Port<span> </span>[uml:Port]</span></td></tr><tr><td><span>Collaboration [uml:Collaboration]</span></td><td><span>Collaboration Use [uml:Collaboration] </span></td></tr><tr><td><span>Expose Interface [does not<span> </span>exist]</span></td><td><br /></td></tr><tr><td><span>Connector [element type does not exist]</span></td><td><span>Connector [uml:Connector] </span></td></tr><tr><td><span>Assembly [element type does not exist]</span></td><td><br /></td></tr><tr><td><span>Delegate [element type does not exist]</span></td><td><span>Connector [uml:Connector]</span></td></tr><tr><td><span>Role Binding [uml:Dependency]</span></td><td><span>Role Binding [uml:Dependency] </span></td></tr><tr><td><span>Represents [uml:Dependency]</span></td><td><span>Dependency [uml:Dependency] </span></td></tr><tr><td><span>Occurrence [uml:Dependency]            <span> </span></span></td><td><span>Dependency [uml:Dependency]</span></td></tr></tbody></table><h3>Conversion details</h3><h4>Dummy class</h4><p>In MagicDraw, the Composite Structure diagram needs a Context element to contain itself. However, in EA there is no Context element. After conversion, a dummy Class element will be created to represent the Context element of the Composite Structure diagram.</p><p>A dummy Class will be named after the closest owner package of the Composite Structure diagram. The Composite Structure diagram and all of the Composite Structure elements will be placed inside the dummy Class element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="dummyClass.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Dummy Class.</h6><h4>Class</h4><p>The Class element data will be normally copied even if the Class element is drawn in a Composite Structure diagram. A Property element will be created to represent the Class element. The Property element will be named after the Class element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="propertyrepresent_class.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Property element representing a Class element.</h6><h4>Class with attributes and operations</h4><p>The Class view in EA will be converted to a Part in MagicDraw. Attributes and operations will not be shown in the Composite Structure diagram.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="partElement_converted.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Part element after conversion.</h6><h4>Interface</h4><p>The Interface element data will be normally copied even if the Interface element is drawn in a Composite Structure diagram. A Property element will be created to represent the Interface element. The Property element will be named after the Interface element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="propertyrepresent_interface.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Property element representing an Interface element.</h6><h4>Part</h4><p>There are two types of Parts: (i) Parts with Ports; and (ii) Parts that set type to other elements.</p><h4>Parts with Ports</h4><p>If you assign the type of a Part element to a Class, Component, or Node, the Part element can have a <ac:link ac:anchor="port"><ac:plain-text-link-body><![CDATA[Port]]></ac:plain-text-link-body><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ac:link>. If a Part is not nested to any element, the Part element will be exported from EA as a Class. Therefore, this Part element can have a Port.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="part_withoutNestElement.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Part that does not nest element(s) with Ports.</h6><p>If a Part is nested to an element, and the type is not set, then the Part type will be used to set type to a dummy Class. This particular Part can have a Port. A dummy Class will be created at the same level of the Part element that sets type to it. The dummy Class will be named after the Part concatenated with '_type'.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="part_withNestElement.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Part that nests element(s) with Ports.</h6><h4>Parts that set type to other elements</h4><p>The type of a Part can be set to another element, e.g., Class, Actor, Component, and Usecase, by right-clicking the Part element and selecting  <strong>Advanced </strong>&gt; <strong>Set Property Type </strong>&gt; <strong>Select Property Type.</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="partType.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Setting Part Type.</h6><p>If the Part type is set to a type that cannot be the owner of a Port, the Port will be removed.</p><p>In MagicDraw, the Property element data cannot have any elements. However, in EA, it can have elements. Therefore, if you draw a Part element and it has an element inside it, that particular element will be relocated to an element, which is the Part type.</p><p>If a Part is not nested to any element, the Part element will be exported from EA as a Class. The element inside the Part will not be relocated. If that particular Part assigns a type to other elements, its type will always be set to Class.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="part_setType_otherElement.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Part that sets type to other elements.</h6><p>If a nested Part whose type is set to another element, e.g., Class, Actor, and Usecase, and this Part contains nested elements, all of the nested elements of the Part will be relocated to the element that is the type of this Part.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="part_setType_otherElementwithNest.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Part that sets Type to other elements has nested elements inside itself.</h6><h4><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="bfb33356-5197-4c86-acec-96a4507efd85"><ac:parameter ac:name="">port</ac:parameter></ac:structured-macro>Port</h4><p>In MagicDraw, a Property element that can have a Port is the Property that sets type to a Class, Component, or Node, and other elements cannot have a Port. However, in EA, most of the elements can have a Port.</p><p>If a Port is created with an element that is not a Class, Component or Node, the Port will be removed from the diagram view. However, its data will be preserved.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="class_component_nodewithport.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Only Class, Component, and Node can have a Port.</h6><p>The following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="3d9f6661-a196-4f08-a349-aebabceaf440"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed view <xmi:id>: Invalid Port. Port can be added to Part that its type is set to Class, Component and Node only.]]></ac:plain-text-body></ac:structured-macro><h4>Ports whose type is set to other elements</h4><p>You can set the type of Port element to another element, e.g., Class, Actor, Component, and Usecase, by right-clicking the Port element and selecting <strong>Advanced </strong>&gt; <strong>Set Property Type </strong>&gt; <strong>Select Property Type</strong>.</p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="portType.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image><br /></strong></p><h6 style="text-align: center;">Setting Port Type.</h6><h4>Port whose type is set to another element and containing Expose Interfaces</h4><p>If an Expose Interface is created on a Port, and the Port type is set to another element, the Expose Interface data will be relocated to the Port's type element. For example, if the Port1 type is set to Actor, an Interface Realization (the Expose Interface data) will be placed inside the Actor after conversion.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="port_setTypetoElement.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Port that sets Type to other elements contains an Expose Interface.<strong><br /></strong></h6><h4>Collaboration</h4><p>The Collaboration element data and its nested data will normally be copied. However, if the Collaboration element is drawn in a Composite Structure diagram, a Collaboration use element will be created to represent the Collaboration element. The Collaboration use element will be named after the Collaboration element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="collaborationUse.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Collaboration use element.</h6><p><strong>Collaboration containing other elements</strong></p><p>A Collaboration can contain only Property, Activity, State Machine, and Interaction. Elements other than these will be removed. If any element is drawn inside the Collaboration, it will be removed from the diagram view.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="collaboration_containElement.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Collaboration containing other elements.</h6><p>The following transformation messages will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="b7dfd88e-c322-4e78-ade6-ee5017b64b64"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed element <xmi:id>: Invalid Element. Collaboration can contain Property, Activity, State Machine and Interaction only.
Removed view <xmi:id>: Invalid Element view. Collaboration cannot be contained in any element view.]]></ac:plain-text-body></ac:structured-macro><p><br /></p><h4>Expose Interface</h4><p>Expose Interfaces are the provided and required interfaces in MagicDraw.</p><p>In MagicDraw, you can draw a provided Interface or required Interface in a Port only and set the type of the Port to another element, e.g., Actor, Usecase, and Class. You can create that particular Port on a Part element whose type is set to a Class, Component, or Node only.</p><h4>Expose Interface with Ports</h4><p>If you draw an Expose Interface in a Port, and the Port does not assign a Type to any elements, that particular Port will be used to set Type to a Dummy Class. The Dummy Class will be created and named after the Port concatenated with '_type'. The Interface element will be moved to the same level of the Port.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="exposeInterface_withPort.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Expose Interface with a Port.</h6><p>If an Expose Interface is created on a Port, and the Type of the Port is set to another element, the Expose Interface data will be relocated to the Port's Type element (see (ii) Port whose type is set to another element and containing Expose Interfaces for more information).</p><p>In MagicDraw, some elements can be used as a Port Type. These elements can have either a provided Interface or required Interface, or both.</p><p>The following list shows the Port's Type elements with specific conditions:</p><ul><li>Interfaces can only have a provided Interface.</li><li>Artifacts cannot have a provided Interface.</li><li>Information Items cannot have a provided Interface.</li><li>Signals cannot have a provided Interface.</li><li>Components always have both provided and required Interfaces.</li><li>The other elements can have both provided and required Interfaces.</li><li>After conversion, if the type of a Port is set to an Interface and the Port has an Expose Interface, only the provided Interface will be shown and the Interface Realization data will be removed.</li><li>Artifacts, Information Items, and Signals cannot hold Interface Realization. If the type of a Port is set to one of them, the provided Interface will be removed. However, this does not affect the required Interface.</li><li>If the Type of a Port is set to a Component, and the Port has an Expose Interface, it will always show both the provided and required Interfaces.</li></ul><h6><ac:image ac:align="center"><ri:attachment ri:filename="port_withTypeElement.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></h6><h6 style="text-align: center;">The Type element of a Port with specific conditions.</h6><p>The following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9d7a5088-06dd-48ab-b837-255decc1a053"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: Provided Interface conflicts with Port type.
The Port type is updated to an owner of Interface Realization.]]></ac:plain-text-body></ac:structured-macro><p>If an Expose Interface is created with an element that is not a Port, the element will be removed both from the Containment tree and diagram view.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="exposeInterface_withElement.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Expose Interface with the element that is not a Port.</h6><p>The following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="38aff7f2-5fda-4f9f-afea-9b84c6987afb"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed element <xmi:id>: Invalid Element. Expose Interface can be added to Port only.]]></ac:plain-text-body></ac:structured-macro><h4>Expose Interface with Relationships</h4><p>In MagicDraw, the provided and required Interfaces cannot be connected with any Relationship, as shown in the figure below. If there is any Relationship connecting to the Expose Interface, it will be removed from both the Containment tree and diagram view.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="exposeInterface_withLines.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Expose Interface with Lines.</h6><p>The following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9b348355-72c9-45cc-ab58-aa1ba2a34b8e"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed element <xmi:id>: Invalid Element. Expose Interface cannot be connected with the element.]]></ac:plain-text-body></ac:structured-macro><h4>Package</h4><p>In MagicDraw, a Package cannot be drawn in a Composite Structure diagram. If it is drawn in EA, it will be removed from the diagram once it has been converted to MagicDraw.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="package.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Package element.</h6><h4>Assembly</h4><p>In MagicDraw, there is no Assembly Line. It will be updated to a Connector.</p><p>The following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7d3f2953-f8ab-4155-82b4-033d493e4088"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: Assembly updated to Connector.]]></ac:plain-text-body></ac:structured-macro><p><ac:image ac:align="center"><ri:attachment ri:filename="assemblyLine_toConnectorLine.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Updating the Assembly Line to the Connector Line.</h6><h4>Dependency</h4><p>There are many relationships that EA exporter exports to Dependency as the following elements:</p><ul><li>Delegate</li><li>Role Binding</li><li>Represents</li><li>Occurrence</li><li>Nest</li><li>Derive</li><li>Import</li><li>Instantiate</li><li>Usage</li><li>Realize</li><li>Trace</li></ul><p>The Relationships above will be shown in the diagram view as Dependencies with stereotype.</p><h4>Removed relationships</h4><p>If an Association, Direct Association, Aggregation, Composition, Generalization, or Specialization is created in a Composite Structure diagram, it will be removed from the diagram view, but its data will be preserved.</p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="removeLines.png"><ri:page ri:content-title="Composite structure diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image><br /></strong></p><h6 style="text-align: center;">Removing Lines.</h6><p>The following transformation messages will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d33086db-778f-4c77-a716-0f66d1a85daf"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed view <xmi:id>: Association cannot be shown in Composite Structure diagram.
Removed view <xmi:id>: Direct Association cannot be shown in Composite Structure diagram.
Removed view <xmi:id>: Aggregation cannot be shown in Composite Structure diagram.
Removed view <xmi:id>: Composition cannot be shown in Composite Structure diagram.
Removed view <xmi:id>: Generalization cannot be shown in Composite Structure diagram.]]></ac:plain-text-body></ac:structured-macro><h3>Transformation report</h3><p>A report containing the conflicts solved during transformation, along with other transformation information, e.g., special mapping and removal of some irrelevant data, is required to be provided for the users.</p><p>The following list shows the transformation messages:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="92ff5963-7fcd-4471-b7d2-77ca8dbe345a"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed view <xmi:id>: Invalid Port. Port can be added to Part that set type to Class, Component, and Node only.
Removed element <xmi:id>: Invalid Element. Collaboration can contain Property, Activity, State Machine, and Interaction only.
Removed view <xmi:id>: Collaboration cannot be contained in any element view.
Removed view <xmi:id>: UseCase cannot be contained in any element view.
Removed element <xmi:id>: Invalid Element. Expose Interface can be added to Port only.
Removed element <xmi:id>: Invalid Element. Expose Interface cannot be connected with the element.
Updated element <xmi:id>: Assembly updated to Connector.
Updated element <xmi:id>: Provided Interface conflicts with Port type. The Port type is updated to an owner of Interface Realization.
Removed view <xmi:id>: Association cannot be shown in CompositeStructure diagram.
Removed view <xmi:id>: Direct Association cannot be shown in Composite Structure diagram.
Removed view <xmi:id>: Aggregation cannot be shown in Composite Structure diagram.
Removed view <xmi:id>: Composition cannot be shown in Composite Structure diagram.
Removed view <xmi:id>: Generalization cannot be shown in Composite Structure diagram.]]></ac:plain-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643658 space=EAI2024xR2 version=1 -->
## PAGE 00004: Conversion messages

- page_id: `194643658`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643658/Conversion+messages
- version_number: 1
- version_date: `2020-10-05T07:47:16.511+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Working with Enterprise Architect Import Plugin
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

1399618665

#### CONTENT-COLUMN: Note

1399618676

#### CONTENT-BLOCK: Note

1399618666

The Enterprise Architect Import Plugin consists of a series of XMI conversions. Each conversion will be reported to the MagicDraw **Messages**window and also saved to a log file if the **Generate conversion log**option is selected.

The conversion log will be saved in the same directory as the MagicDraw output file using the same name, but with a different .log extension.****

#### INFO: Note

Note

You can open the MagicDraw **Messages**window by pressing **Ctrl**+ **M**.

1399618664

**Related page**

- [CONFLUENCE_PAGE title='Conversion messages' space='EAI2024xR2'] [CONFLUENCE_PAGE title='Conversion options' space='EAI2024xR2']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="07ba0a20-39d9-473c-8dbe-f2376fb23243"><ac:parameter ac:name="id">1399618665</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="6240c871-bf2d-4844-9e96-14692c899521"><ac:parameter ac:name="id">1399618676</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5acd89ea-a6fa-4263-a21b-6d64555eae6e"><ac:parameter ac:name="id">1399618666</ac:parameter><ac:rich-text-body><p>The Enterprise Architect Import Plugin consists of a series of XMI conversions. Each conversion will be reported to the MagicDraw <strong>Messages </strong>window and also saved to a log file if the <strong>Generate conversion log </strong>option is selected.</p><p>The conversion log will be saved in the same directory as the MagicDraw output file using the same name, but with a different .log extension.<strong>                      </strong></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="5855b8a2-1ee4-44bf-9368-c49e1f5d0f9b"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>You can open the MagicDraw <strong>Messages </strong>window by pressing <strong>Ctrl </strong>+ <strong>M</strong>.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c935b5ee-e985-450e-9f94-b328d1787584"><ac:parameter ac:name="id">1399618664</ac:parameter><ac:rich-text-body><p><strong>Related page</strong></p><ul><li><ac:link><ac:plain-text-link-body><![CDATA[C]]></ac:plain-text-link-body><ri:page ri:content-title="Conversion messages" ri:space-key="EAI2024xR2" /></ac:link><ac:link><ri:page ri:content-title="Conversion options" ri:space-key="EAI2024xR2" /><ac:plain-text-link-body><![CDATA[onversion options]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643655 space=EAI2024xR2 version=1 -->
## PAGE 00005: Conversion options

- page_id: `194643655`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643655/Conversion+options
- version_number: 1
- version_date: `2020-10-05T07:46:16.377+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Working with Enterprise Architect Import Plugin
- labels: []

### NORMALIZED CONTENT

1399498380

1399498391

1399509739

**On this page**

33

1399498381

In addition to the options that you have in the **Import Enterprise Architect File**dialog, several other conversion options exist in the MagicDraw **Environment Options**dialog.

[IMAGE alt='' src='']

###### The EA options in the Environment Options dialog.

The transformation options are classified into two groups: General and Activity element mapping.

##### General

The options available in the **General**group are the same as those in the **Import Enterprise Architect Files**dialog.

##### Activity element mapping option

The Activity element mapping group provides options to convert the EA elements to other element types. The following table shows the Activity Element Mapping options.

| Property name | Function |
| --- | --- |
| Convert EA WriteVariableAction to | To convert EA WriteVariableAction to either AddVariableValueAction or RemoveVariableValueAction. |
| Convert EA WriteLinkAction to | To convert EA WriteLinkAction to either CreateLinkAction or DestroyLinkAction. |
| Convert EA WriteStructuralFeatureAction to | To convert EA WriteStructuralFeatureAction to either AddStructuralFeatureValueAction or RemoveStructuralFeatureValueAction. |

To view the other Enterprise Architect Import options in the **Environment Options**dialog

1. Click Options > Environment on the MagicDraw main menu to open the Environment Options dialog.
2. Select Enterprise Architect Import from the tree menu on the left-hand side of the dialog.

1399498379

**Related page**

- [CONFLUENCE_PAGE title='Conversion options' space='EAI2024xR2']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="e1b5addf-b02a-4952-a58a-9ebcceddfaf3"><ac:parameter ac:name="id">1399498380</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="884f1e25-866c-4d8a-b3c2-7fc930cb039f"><ac:parameter ac:name="id">1399498391</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="258b311d-d39f-472f-a19f-63673e9194a1"><ac:parameter ac:name="id">1399509739</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="86527829-1e63-4dee-942c-bda4de40e153"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="eb8e76c4-cd10-426c-92ad-a806d5f005e2"><ac:parameter ac:name="id">1399498381</ac:parameter><ac:rich-text-body><p>In addition to the options that you have in the <strong>Import Enterprise Architect File </strong>dialog, several other conversion options exist in the MagicDraw <strong>Environment Options </strong>dialog.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="EA_EnvironmentOptions.png"><ri:page ri:content-title="Conversion options" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The EA options in the Environment Options dialog.</h6><p>The transformation options are classified into two groups: General and Activity element mapping.</p><h3>General</h3><p>The options available in the <strong>General </strong>group are the same as those in the <strong>Import Enterprise Architect Files </strong>dialog.</p><h3>Activity element mapping option </h3><p>The Activity element mapping group provides options to convert the EA elements to other element types. The following table shows the Activity Element Mapping options.</p><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Property name</th><th>Function</th></tr><tr><td><p>Convert EA WriteVariableAction to</p></td><td><p>To convert EA WriteVariableAction to either AddVariableValueAction or RemoveVariableValueAction.</p></td></tr><tr><td>Convert EA WriteLinkAction to</td><td><p>To convert EA WriteLinkAction to either CreateLinkAction or DestroyLinkAction.</p></td></tr><tr><td><p>Convert EA WriteStructuralFeatureAction to</p></td><td><p>To convert EA WriteStructuralFeatureAction to either AddStructuralFeatureValueAction or RemoveStructuralFeatureValueAction.</p></td></tr></tbody></table><p><br /></p><p>To view the other Enterprise Architect Import options in the <strong>Environment Options </strong>dialog</p><hr /><ol><li>Click <strong>Options </strong>&gt; <strong>Environment </strong>on the MagicDraw main menu to open the <strong>Environment </strong><strong>Options </strong>dialog.</li><li>Select <strong>Enterprise Architect Import </strong>from the tree menu on the left-hand side of the dialog. </li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="bd25c4e7-c8fe-466e-ba7f-a08dd03e180c"><ac:parameter ac:name="id">1399498379</ac:parameter><ac:rich-text-body><p><strong>Related page</strong></p><ul><li><ac:link><ri:page ri:content-title="Conversion options" ri:space-key="EAI2024xR2" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643639 space=EAI2024xR2 version=1 -->
## PAGE 00006: Enterprise Architect Import Plugin Documentation

- page_id: `194643639`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643639/Enterprise+Architect+Import+Plugin+Documentation
- version_number: 1
- version_date: `2024-01-31T15:49:44.126+01:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

2

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="17ae9ea4-625d-4774-9a0b-01afec01660a"><ac:parameter ac:name="depth">2</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=194643653 space=EAI2024xR2 version=1 -->
## PAGE 00007: Enterprise Architect Import plugin menu

- page_id: `194643653`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643653/Enterprise+Architect+Import+plugin+menu
- version_number: 1
- version_date: `2020-08-28T07:34:19.369+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Working with Enterprise Architect Import Plugin
- labels: []

### NORMALIZED CONTENT

To import an EA project

1. Either type an EA exported XMI file or click [IMAGE alt='' src=''] to select the file. NoteEnterprise Architect Import Plugin supports the EA XMI files exported with the option specified as: XMI Type = **UML2.1(XMI 2.1**).
2. Either type a MagicDraw output filename or click [IMAGE alt='' src=''] to select the file.
3. Select the conversion options.
4. Click Import to start importing the file.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To import an EA project</p><hr /><ol><li><p class="auto-cursor-target">Either type an EA exported XMI file or click <ac:image><ri:attachment ri:filename="browse_button.png"><ri:page ri:content-title="Enterprise Architect Import plugin menu" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image> to select the file.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="466811aa-fd22-4257-aec1-fe87a0b012b4"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>Enterprise Architect Import Plugin supports the EA XMI files exported with the option specified as: XMI Type = <strong>UML2.1(XMI 2.1</strong>).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Either type a MagicDraw output filename or click <strong><ac:image><ri:attachment ri:filename="browse_button.png"><ri:page ri:content-title="Enterprise Architect Import plugin menu" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></strong> to select the file.</li><li>Select the conversion options.</li><li>Click <strong>Import</strong> to start importing the file.</li></ol>
````

<!--NOMAGIC_PAGE id=194643641 space=EAI2024xR2 version=1 -->
## PAGE 00008: Getting started

- page_id: `194643641`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643641/Getting+started
- version_number: 1
- version_date: `2020-10-05T07:38:20.965+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

1399077947

1399077959

1399077949

This user guide will serve as an introduction to the Enterprise Architect Import plugin features and functionality. It also shows how to use it to work with your modeling tools.

1399077936

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="cd0e3905-b0b9-4fe8-a505-39a45b03cabb"><ac:parameter ac:name="id">1399077947</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fd57249f-680a-4738-a3ae-7dad9c746966"><ac:parameter ac:name="id">1399077959</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d5d15672-30d4-49f6-9163-8612d24a06a7"><ac:parameter ac:name="id">1399077949</ac:parameter><ac:rich-text-body><p>This user guide will serve as an introduction to the Enterprise Architect Import plugin features and functionality. It also shows how to use it to work with your modeling tools.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="577713f2-a132-4bb3-8d07-5f161e085897"><ac:parameter ac:name="id">1399077936</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3614b4c6-4572-413d-a553-9d6bbb4c4fbc" /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643662 space=EAI2024xR2 version=1 -->
## PAGE 00009: Importing Diagrams

- page_id: `194643662`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643662/Importing+Diagrams
- version_number: 1
- version_date: `2020-10-05T08:01:08.426+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

1400475026

#### CONTENT-COLUMN: Note

1400475039

1400475025

**On this page**

43

#### CONTENT-BLOCK: Note

1400475029

Enterprise Architect Import Plugin allows you to import diagrams. The imported diagram information includes:

33

##### Geometry Properties

The geometry properties imported to MagicDraw are:

- Positions on a diagram (for shape elements)
- Width and height (for shape elements)
- Path break points (for link elements)

#### NOTE: Note

Note

Other display properties can override geometry information.For example, if an imported element width is shorter than the required width to display text on the element, the width will be adjusted automatically.

##### Color Properties

Color properties will be imported along with the diagrams to MagicDraw. Each color property has a different name in MagicDraw. The following table shows color properties mapping.

| EA | MagicDraw |
| --- | --- |
| Background | Fill color |
| Border color (for shape element) | Pen color |
| Font color | Text color |
| Line color (for link element) | Pen color |

##### Display Properties

The display properties in EA can be categorized into three groups: shape, link, and diagram. Only those properties that correspond to MagicDraw will be imported. For example, the **Show Diagram Details**property in EA will be imported as the **Show Diagram Info**property in MagicDraw.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="1fed4064-2959-4e50-b227-0f8814e23fa5"><ac:parameter ac:name="id">1400475026</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="388bb616-1148-426c-afb0-6036ca887161"><ac:parameter ac:name="id">1400475039</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a29434aa-eafc-4d50-a64e-2ac14788354a"><ac:parameter ac:name="id">1400475025</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f5e11967-3883-444f-a5a5-da3ceb0ff423"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6e9be5d4-90d7-403d-8405-ca01896a4185"><ac:parameter ac:name="id">1400475029</ac:parameter><ac:rich-text-body><p>Enterprise Architect Import Plugin allows you to import diagrams. The imported diagram information includes:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="6eeee738-6a1a-47fa-bb30-70cfafa46597"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p><h3>Geometry Properties</h3><p>The geometry properties imported to MagicDraw are:</p><ul><li>Positions on a diagram (for shape elements)</li><li>Width and height (for shape elements)</li><li>Path break points (for link elements)</li></ul><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9067b152-2de0-447c-a428-0923be62ccce"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>Other display properties can override geometry information.For example, if an imported element width is shorter than the required width to display text on the element, the width will be adjusted automatically.</p></ac:rich-text-body></ac:structured-macro><h3>Color Properties</h3><p>Color properties will be imported along with the diagrams to MagicDraw. Each color property has a different name in MagicDraw. The following table shows color properties mapping.</p><table class="relative-table wrapped" style="width: 32.1145%;"><colgroup><col style="width: 64.0199%;" /><col style="width: 35.9801%;" /></colgroup><tbody><tr><th>EA</th><th>MagicDraw</th></tr><tr><td>Background</td><td><p>Fill color</p></td></tr><tr><td><p>Border color (for shape element)</p></td><td><p>Pen color</p></td></tr><tr><td><span>Font<span> </span>color</span></td><td><p>Text color</p></td></tr><tr><td><span>Line color (for link element)</span></td><td><p>Pen color</p></td></tr></tbody></table><h3>Display Properties</h3><p>The display properties in EA can be categorized into three groups: shape, link, and diagram. Only those properties that correspond to MagicDraw will be imported. For example, the <strong>Show Diagram Details </strong>property in EA will be imported as the <strong>Show Diagram Info </strong>property in MagicDraw.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643644 space=EAI2024xR2 version=1 -->
## PAGE 00010: Installation

- page_id: `194643644`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643644/Installation
- version_number: 1
- version_date: `2024-05-09T12:12:08.728+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Getting started
- labels: []

### NORMALIZED CONTENT

1399356814

1399356825

1399356815

The Enterprise Architect Import plugin comes bundled with your modeling tool. When you install the tool, the plugin is automatically installed as well.

1399356813

**Related pages**

- Introduction
- Plugin information

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="84fb96ad-befe-425c-8f94-6f34810375e6"><ac:parameter ac:name="id">1399356814</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="664fe2be-bd02-4c2b-8fd5-d7c758f10078"><ac:parameter ac:name="id">1399356825</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="607b89fa-2cfa-474c-b429-9b3c61078fc7"><ac:parameter ac:name="id">1399356815</ac:parameter><ac:rich-text-body><p>The Enterprise Architect Import plugin comes bundled with your modeling tool. When you install the tool, the plugin is automatically installed as well.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4bbbdd71-174b-4b0a-a503-6def011b0e38"><ac:parameter ac:name="id">1399356813</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><a href="https://docs.nomagic.com/display/EAI2024xR1/Introduction">Introduction</a></li><li><a href="https://docs.nomagic.com/display/EAI2024xR1/Plugin+information">Plugin information</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643765 space=EAI2024xR2 version=1 -->
## PAGE 00011: Interaction Overview Diagrams

- page_id: `194643765`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643765/Interaction+Overview+Diagrams
- version_number: 1
- version_date: `2020-10-05T08:52:06.719+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Special Transformation
- labels: []

### NORMALIZED CONTENT

1403496358

1403496369

1403496357

**On this page**

43

1403496359

The following sections describe additional EA specific information about the Interaction Overview diagram.

##### Conversion details

###### Interaction Overview diagram

An Interaction Overview diagram is one of four types of Interaction diagrams. The other three are Timing, Sequence, and Communication diagrams. An Interaction Overview diagram, just like an Activity diagram, visualizes a sequence of Activities. Most of the notation elements for the Interaction Overview diagram are the same as those for the Activity diagram, e.g., Initial, Decision, Fork, Join, and Final nodes. Interaction Occurrences and Interaction elements are two new elements in the Interaction Overview diagram.

[IMAGE alt='' src='']

###### The Interaction Overview diagram.

Afterconversion, the Interaction Overview diagram will be placed within anActivityelement.

[IMAGE alt='' src='']

###### The Interaction Overview diagram placed within an Activity element.

###### Interaction element

Interaction elements display an inline Interaction diagram (Interaction Overview, Timing, Sequence, or Communication diagram). In EA, Interaction elements can be created to display more of other diagrams than those classified as Interaction diagrams.

[IMAGE alt='' src='']

###### An Interaction element.

[IMAGE alt='' src='']

###### An Interaction element in the Interaction Overview diagram.

###### Interaction Occurrence

Interaction Occurrence elements refer to an existing Interaction diagram. They are visually represented by a rectangular frame, which can be created by dragging the Interaction diagram from the project Browser to an Interaction Overview diagram and selecting the **Interaction Occurrence** option from the pop-up dialog.

[IMAGE alt='' src='']

###### An Interaction Occurrence element.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ea3bd590-96d1-4ecf-b456-1daec801c638"><ac:parameter ac:name="id">1403496358</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="9ed59701-7986-4afd-b87c-e64d79566665"><ac:parameter ac:name="id">1403496369</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3bafd022-8770-47d6-bae6-b86001b44893"><ac:parameter ac:name="id">1403496357</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f5e11967-3883-444f-a5a5-da3ceb0ff423"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="fe08629b-dfd4-4d10-82de-3c90ec5d7858"><ac:parameter ac:name="id">1403496359</ac:parameter><ac:rich-text-body><p>The following sections describe additional EA specific information about the Interaction Overview diagram.</p><h3>Conversion details</h3><h4>Interaction Overview diagram</h4><p>An Interaction Overview diagram is one of four types of Interaction diagrams. The other three are Timing, Sequence, and Communication diagrams.  An Interaction Overview diagram, just like an Activity diagram, visualizes a sequence of Activities. Most of the notation elements for the Interaction Overview diagram are the same as those for the Activity diagram, e.g., Initial, Decision, Fork, Join, and Final nodes. Interaction Occurrences and Interaction elements are two new elements in the Interaction Overview diagram.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="interactionOverview.png"><ri:page ri:content-title="Interaction Overview Diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The Interaction Overview diagram.</h6><p><span>After<span> </span>conversion, the Interaction Overview diagram will be placed within an<span> </span>Activity<span> </span>element.</span></p><p><span><ac:image ac:align="center"><ri:attachment ri:filename="interactionOverview_placement.png"><ri:page ri:content-title="Interaction Overview Diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;">The Interaction Overview diagram placed within an Activity element.</h6><h4>Interaction element</h4><p>Interaction elements display an inline Interaction diagram (Interaction Overview, Timing, Sequence, or Communication diagram). In EA, Interaction elements can be created to display more of other diagrams than those classified as Interaction diagrams.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="interactionElement.png"><ri:page ri:content-title="Interaction Overview Diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Interaction element.</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="interactionElement_inOverview.png"><ri:page ri:content-title="Interaction Overview Diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Interaction element in the Interaction Overview diagram.</h6><h4>Interaction Occurrence</h4><p>Interaction Occurrence elements refer to an existing Interaction diagram. They are visually represented by a rectangular frame, which can be created by dragging the Interaction diagram from the project Browser to an Interaction Overview diagram and selecting the <strong>Interaction Occurrence</strong> option from the pop-up dialog.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="interactionOccurenceElement.png"><ri:page ri:content-title="Interaction Overview Diagrams" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Interaction Occurrence element.</h6></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643642 space=EAI2024xR2 version=1 -->
## PAGE 00012: Introduction

- page_id: `194643642`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643642/Introduction
- version_number: 1
- version_date: `2020-10-05T07:41:11.777+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Getting started
- labels: []

### NORMALIZED CONTENT

1399189246

1399189257

1399189247

MagicDraw has the functionality to import UML models that conform to various XMI versions (including XMI 2.1) from Sparx Systems Enterprise Architect (EA), a modeling and visualization tool based on the UML 2.3 standard. EA has the ability to import and export XMI compliant models; therefore, you can use EA to import UML2.1(XMI2.1). However, the XMI models exported from EA contain some XMI conflicts and EA-specific data that do not conform to the UML standards.

Enterprise Architect Import Plugin for MagicDraw allows you to migrate the XMI models from EA to MagicDraw flawlessly by using an additional transformation process with a set of mapping rules.

The main purpose of Enterprise Architect Import Plugin is to help MagicDraw users who need to import models from EA manage the conflicts that can cause problems during loading the XMI models to MagicDraw, as well as transforming some EA-specific data into UML elements with stereotypes.

In addition to the ability to import model elements, the plugin also allows for the import of diagrams. The current plugin version supports:

- Class diagrams
- Package diagrams
- Object diagrams
- Component diagrams
- Deployment diagrams
- Use Case diagrams
- Activity diagrams
- Sequence diagrams
- Communication diagrams
- StateMachine diagrams
- CompositeStructure diagrams
- InteractionOverview diagrams

1399189245

**Related pages**

- [CONFLUENCE_PAGE title='Plugin information' space='EAI2024xR2']
- [CONFLUENCE_PAGE title='Installation' space='EAI2024xR2']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="297958b5-5650-4cef-b4d9-944c29afe31b"><ac:parameter ac:name="id">1399189246</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ad892fe1-5533-4231-9e45-7815728923cc"><ac:parameter ac:name="id">1399189257</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ff42e3e5-ef45-4ab0-aad8-6f16f6b899dd"><ac:parameter ac:name="id">1399189247</ac:parameter><ac:rich-text-body><p>MagicDraw has the functionality to import UML models that conform to various XMI versions (including XMI 2.1) from Sparx Systems Enterprise Architect (EA), a modeling and visualization tool based on the UML 2.3 standard. EA has the ability to import and export XMI compliant models; therefore, you can use EA to import UML2.1(XMI2.1). However, the XMI models exported from EA contain some XMI conflicts and EA-specific data that do not conform to the UML standards.</p><p>Enterprise Architect Import Plugin for MagicDraw allows you to migrate the XMI models from EA to MagicDraw flawlessly by using an additional transformation process with a set of mapping rules.</p><p>The main purpose of Enterprise Architect Import Plugin is to help MagicDraw users who need to import models from EA manage the conflicts that can cause problems during loading the XMI models to MagicDraw, as well as transforming some EA-specific data into UML elements with stereotypes.</p><p>In addition to the ability to import model elements, the plugin also allows for the import of diagrams. The current plugin version supports:</p><ul><li>Class diagrams </li><li>Package diagrams </li><li>Object diagrams</li><li>Component diagrams</li><li>Deployment diagrams</li><li>Use Case diagrams </li><li>Activity diagrams</li><li>Sequence diagrams</li><li>Communication diagrams</li><li>StateMachine diagrams</li><li>CompositeStructure diagrams</li><li>InteractionOverview diagrams</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8742c39a-cfe0-4abf-9d92-f7e1f576d067"><ac:parameter ac:name="id">1399189245</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Plugin information" ri:space-key="EAI2024xR2" /></ac:link></li><li><ac:link><ri:page ri:content-title="Installation" ri:space-key="EAI2024xR2" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643771 space=EAI2024xR2 version=1 -->
## PAGE 00013: Known limitations and constraints

- page_id: `194643771`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643771/Known+limitations+and+constraints
- version_number: 1
- version_date: `2020-10-05T08:52:36.355+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

The following tableshows the conversion limitations and constraints in EAexported XMIand the EAImportplugin.

| No. | Constraint name | Description |
| --- | --- | --- |
| 1 | N-ary Association | Due to the difference between the EA exported XMI and MagicDraw XMI, the view of N-ary Associations will not be imported. |
| 2 | Diagram Legend | MagicDraw does not have a similar element. Diagram Legends will not be imported. |
| 3 | Diagram Note | The element most similar to the Diagram Note is the MagicDraw Diagram Information Table (through Option > Show diagram info). However, in EA it will be accessed through Option > show diagram details. Therefore, Diagram Notes will not be imported to MagicDraw. |
| 4 | Text size | The size of text displayed in EA and MagicDraw may vary. The text size in EA is usually larger. |
| 5 | Word wrap | Due to the size constraints in text displayed in element Blocks, the result of word wrap in EA and MagicDraw is likely to be different. |
| 6 | Contact point between elements and links | The position of both ends of a link element cannot be mapped to MagicDraw because the last segments of the link element in MagicDraw always point to the center of connected elements. |
| 7 | Display alternative image | In EA, you can display an element in a diagram by using an alternative image. MagicDraw will not import that particular image and will use a default shape instead. |
| 8 | Link label position | A Link element such as an Association has many text labels, e.g., multiplicity and role name labels. MagicDraw will not import the position of these labels and will use the default position instead. |
| 9 | Pin position | A Pin position in MagicDraw may have been slightly moved from its original position in EA. Especially, if the Pin is placed at the corner of its containing element, it will be slightly shifted away from the corner (mostly in a clockwise direction). |
| 10 | Nested CallBehavior- Action | A CallBehaviorAction element is nested with another CallBehaviorAction element. The outermost part of the element will remain. The other will be removed. |
| 11 | DataStoreNode inner element | A DataStoreNode element that contains Activity-diagram-related elements. Every element inside that particular DataStoreNode element will be removed. Only the DataStoreNode element will remain. |
| 12 | Object inner element | An Object element that contains Activity-diagram-related elements. Every element inside that particular Object element will be removed. Only the Object element will remain. |
| 13 | Lifeline position | The Lifeline position in MagicDraw will not correspond to the original position in EA. The position is fixed. |
| 14 | Diagonal Sequence Message | MagicDraw does not support Diagonal Sequence Messages. |
| 15 | Sequence Activation Options | MagicDraw does not support manipulating Sequence Activation through Sequence Activation Options. |
| 16 | State Contains diagram | A diagram element placed inside a State element will be removed. |
| 17 | Region in Orthogonal State | EA exported XMI contains incorrect information when the following happen:More than one Region has identical names.The Region was created and then removed before exporting to XMI.This will result in an unexpected result after imported into MagicDraw. |
| 18 | Assembly Relationship in the Composite Structure diagram | Assembly Relationships in EA are exported to XMI as Connectors. They will then be imported to MagicDraw as Connectors. |
| 19 | Interaction elements as the diagram frame | MagicDraw does not import Interaction elements displayed as the diagram frame in an Interaction Overview diagram. |
| 20 | Message timing details | Duration Observation, and Timing Observation are not imported to MagicDraw. |
| 21 | Concurrent State Regions in StateMachine | Adding and removing multiple Concurrent State Regions to and from StateMachine in EA can cause the EA XMI to be incorrectly exported. If the EA exported XMI is in this state, the result of the StateMachine imported to MagicDraw cannot be determined.The same problem also occurs if there are multiple Concurrent State Regions with the same name. |
| 22 | Combined Fragment | Adding and removing multiple Interaction Operands to and from Combined Fragment in EA can cause the EA XMI to be incorrectly exported. The problem can be fixed by importing the EA XMI back to a new project in EA and exporting it back before importing it to MagicDraw. |
| 23 | Problem occurs during conversion of the Sequence diagram. | Importing EA XMI to MagicDraw sometimes results in the following error message: “Problem occurred during conversion of Sequence diagram”. If this occurs, please import the XMI back to a new project in EA and export it back again before importing it to MagicDraw. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span>The following table </span><span>shows the conversion limitations and constraints in EA<span> </span>exported XMI<span> </span>and the EA<span> </span>Import<span> </span>plugin.</span></p><table class="wrapped"><colgroup><col /><col /><col /></colgroup><tbody><tr><th>No.</th><th>Constraint name</th><th>Description</th></tr><tr><td>1</td><td><span style="color: black;">N-ary<span> </span>Association</span></td><td><span style="color: black;">Due to<span> </span>the di<span>f</span>ference between the EA<span> </span>exported XMI<span> </span>and MagicDraw XMI, </span><span style="color: black;">the view of<span> </span>N-ary Associations will not be imported.</span></td></tr><tr><td>2</td><td><span style="color: black;">Diagram Legend</span></td><td><span style="color: black;">MagicDraw does not have a similar element. Diagram Legends will not be </span><span style="color: black;">imported.</span></td></tr><tr><td>3</td><td><span style="color: black;">Diagram Note</span></td><td><p>The element most similar to the Diagram Note is the MagicDraw Diagram Information Table (through <strong>Option </strong>&gt; <strong>Show diagram info</strong>). However, in EA it will be accessed through <strong>Option </strong>&gt; <strong>show diagram details</strong>. Therefore, Diagram Notes will not be imported to MagicDraw.</p></td></tr><tr><td>4</td><td>Text size</td><td><p>The size of text displayed in EA and MagicDraw may vary. The text size in EA is usually larger.</p></td></tr><tr><td>5</td><td><p>Word wrap</p></td><td><span style="color: black;">Due to<span> </span>the size constraints in text<span> </span>displayed in element Blocks, the result of </span><span style="color: black;">word wrap in EA<span> </span>and MagicDraw is likely to<span> </span>be di<span>f</span>ferent.</span></td></tr><tr><td>6</td><td><span style="color: black;">Contact point </span><span style="color: black;">between<span> </span>elements<span> </span>and links</span></td><td><span>The position of<span> </span>both ends of<span> </span>a link element cannot be mapped to<span> </span>MagicDraw<span> </span>because<span> </span>the<span> </span>last<span> </span>segments<span> </span>of<span> </span>the<span> </span>link<span> </span>element<span> </span>in<span> </span>MagicDraw<span> </span>always point to<span> </span>the center of<span> </span>connected elements.</span></td></tr><tr><td>7</td><td><span style="color: black;">Display alternative </span><span style="color: black;">image</span></td><td><p>In EA, you can display an element in a diagram by using an alternative image. MagicDraw will not import that particular image and will use a default shape instead.</p></td></tr><tr><td>8</td><td><span style="color: black;">Link<span> </span>label<span> </span>position       <span> </span></span></td><td><span style="color: black;">A<span> </span>Link<span> </span>element<span> </span>such<span> </span>as<span> </span>an<span> </span>Association<span> </span>has<span> </span>many<span> </span>text<span> </span>labels,<span> </span>e.g., </span><span style="color: black;">multiplicity<span> </span>and<span> </span>role<span> </span>name<span> </span>labels.<span> </span>MagicDraw<span> </span>will<span> </span>not<span> </span>import<span> </span>the<span> </span>position<span> </span>of these labels and will use the<span> </span>default position instead.</span></td></tr><tr><td>9</td><td><span style="color: black;">Pin position</span></td><td><p>A Pin position in MagicDraw may have been slightly moved from its original position in EA. Especially, if the Pin is placed at the corner of its containing element, it will be slightly shifted away from the corner (mostly in a clockwise direction).</p></td></tr><tr><td>10</td><td><span style="color: black;">Nested CallBehavior- </span><span style="color: black;">Action</span></td><td><p>A CallBehaviorAction element is nested with another CallBehaviorAction element. The outermost part of the element will remain. The other will be removed.</p></td></tr><tr><td>11</td><td><span style="color: black;">DataStoreNode inner </span><span style="color: black;">element</span></td><td><p>A DataStoreNode element that contains Activity-diagram-related elements. Every element inside that particular DataStoreNode element will be removed. Only the DataStoreNode element will remain.</p></td></tr><tr><td>12</td><td><span style="color: rgb(0,0,0);">Object inner element</span></td><td><span style="color: black;">An<span> </span>Object<span> </span>element<span> </span>that<span> </span>contains<span> </span>Activity-diagram-related elements.<span> </span>Every </span><span style="color: black;">element inside that<span> </span>particular Object element will be removed. Only the Object element will remain.</span></td></tr><tr><td>13</td><td><span style="color: rgb(0,0,0);">Lifeline position</span></td><td><p>The Lifeline position in MagicDraw will not correspond to the original position in EA. The position is fixed.</p></td></tr><tr><td>14</td><td><span>Diagonal Sequence Message</span></td><td><p>MagicDraw does not support Diagonal Sequence Messages.</p></td></tr><tr><td>15</td><td><p>Sequence Activation Options</p></td><td><p>MagicDraw does not support manipulating Sequence Activation through Sequence Activation Options.</p></td></tr><tr><td>16</td><td><span style="color: black;">State<span> </span>Contains dia</span><span style="color: black;">gram</span></td><td><p>A diagram element placed inside a State element will be removed.</p></td></tr><tr><td>17</td><td><span style="color: black;">Region in Orthogo</span><span style="color: black;">nal State</span></td><td><p>EA exported XMI contains incorrect information when the following happen:</p><ul><li>More than one Region has identical names.</li><li>The Region was created and then removed before exporting to XMI.</li></ul><p>This will result in an unexpected result after imported into MagicDraw.</p></td></tr><tr><td>18</td><td><span style="color: black;">Assembly Relation</span><span style="color: black;">ship in the Composite Structure diagram</span></td><td><p>Assembly Relationships in EA are exported to XMI as Connectors. They will then be imported to MagicDraw as Connectors.</p></td></tr><tr><td>19</td><td><span style="color: black;">Interaction elements </span><span style="color: black;">as the diagram frame</span></td><td><p>MagicDraw does not import Interaction elements displayed as the diagram frame in an Interaction Overview diagram.</p></td></tr><tr><td colspan="1">20</td><td colspan="1"><span style="color: black;">Message timing </span><span style="color: black;">details</span></td><td colspan="1"><p>Duration Observation, and Timing Observation are not imported to MagicDraw.</p></td></tr><tr><td colspan="1">21</td><td colspan="1"><span style="color: black;">Concurrent State </span><span style="color: black;">Regions in StateMachine</span></td><td colspan="1"><p>Adding and removing multiple Concurrent State Regions to and from StateMachine in EA can cause the EA XMI to be incorrectly exported. If the EA exported XMI is in this state, the result of the StateMachine imported to MagicDraw cannot be determined.</p><p>The same problem also occurs if there are multiple Concurrent State Regions with the same name.</p></td></tr><tr><td colspan="1">22</td><td colspan="1"><span style="color: black;">Combined Fragment</span></td><td colspan="1"><p>Adding and removing multiple Interaction Operands to and from Combined Fragment in EA can cause the EA XMI to be incorrectly exported. The problem can be fixed by importing the EA XMI back to a new project in EA and exporting it back before importing it to MagicDraw.</p></td></tr><tr><td colspan="1">23</td><td colspan="1"><span style="color: black;">Problem<span> </span>occurs<span> </span>during </span><span style="color: black;">conversion of the Sequence diagram.</span></td><td colspan="1"><p>Importing EA XMI to MagicDraw sometimes results in the following error message: “Problem occurred during conversion of Sequence diagram”. If this occurs, please import the XMI back to a new project in EA and export it back again before importing it to MagicDraw.</p></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=194643643 space=EAI2024xR2 version=1 -->
## PAGE 00014: Plugin information

- page_id: `194643643`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643643/Plugin+information
- version_number: 1
- version_date: `2024-05-09T12:12:08.659+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Getting started
- labels: []

### NORMALIZED CONTENT

1399256752

1399256773

1399256763

Enterprise Architect Import Plugin for MagicDraw supports Enterprise Architect Versions 7.1, 7.5, and 8.0 (most of the testing procedures performed on EA 7.1.833 and EA 7.5.847). The plugin helps you import and transform an EA exported XMI using the UML2.1(XMI2.1) option into a MagicDraw file (*.mdxml).

Your imported models will include the following details:

- UML models
- Profiles
- Stereotype usage information
- EA-specific data:
  - Constraints
  - Requirements
  - Scenarios
  - Files
  - Requirements (External)
  - Changes
  - Issues
- Diagram information
  - Class diagrams
  - Package diagrams
  - Object diagrams
  - Component diagrams
  - Deployment diagrams
  - Use Case diagrams
  - Activity diagrams
  - Sequence diagrams
  - Communication diagrams
  - State Machine diagrams
  - Composite Structure diagrams
  - Interaction Overview diagrams
- SysML (SysML 1.1 model from EA will be transformed to MagicDraw SysML.)

1399256751

**Related pages**

- Introduction
- Installation

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a1125f24-8f8b-46a0-8045-7e490bd4542f"><ac:parameter ac:name="id">1399256752</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="f04eed40-57a8-483b-b766-799e0c760fcd"><ac:parameter ac:name="id">1399256773</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="86d6d062-ff25-4f16-b949-82a1291787ee"><ac:parameter ac:name="id">1399256763</ac:parameter><ac:rich-text-body><p>Enterprise Architect Import Plugin for MagicDraw supports Enterprise Architect Versions 7.1, 7.5, and 8.0 (most of the testing procedures performed on EA 7.1.833 and EA 7.5.847). The plugin helps you import and transform an EA exported XMI using the UML2.1(XMI2.1) option into a MagicDraw file (*.mdxml).</p><p>Your imported models will include the following details:</p><ul><li>UML models</li><li>Profiles</li><li>Stereotype usage information</li><li>EA-specific data:<ul><li>Constraints</li><li>Requirements</li><li>Scenarios</li><li>Files</li><li>Requirements (External)</li><li>Changes</li><li>Issues</li></ul></li><li>Diagram information<ul><li>Class diagrams</li><li>Package diagrams</li><li>Object diagrams</li><li>Component diagrams</li><li>Deployment diagrams</li><li>Use Case diagrams</li><li>Activity diagrams</li><li>Sequence diagrams</li><li>Communication diagrams</li><li>State Machine diagrams</li><li>Composite Structure diagrams</li><li>Interaction Overview diagrams</li></ul></li><li>SysML (SysML 1.1 model from EA will be transformed to MagicDraw SysML.)</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b32cf660-4f98-4f28-887b-9273285d357e"><ac:parameter ac:name="id">1399256751</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><a href="https://docs.nomagic.com/display/EAI2024xR1/Introduction">Introduction</a></li><li><a href="https://docs.nomagic.com/display/EAI2024xR1/Installation">Installation</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643689 space=EAI2024xR2 version=1 -->
## PAGE 00015: Sequence diagram elements

- page_id: `194643689`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643689/Sequence+diagram+elements
- version_number: 1
- version_date: `2020-10-05T08:25:03.355+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Special Transformation
- labels: []

### NORMALIZED CONTENT

1401567461

1401567463

1401567460

**On this page**

43

1401567462

##### Lifelines

All of the EA Lifelines will be imported, but a Part or Port within a Lifeline will be transformed into a new separate Lifeline.

###### Gaps between Lifelines

The position and width of any Lifeline created in EA will not be imported. Every Lifeline will be given a fixed value and position in MagicDraw. MagicDraw will place the first Lifeline on the left-hand side of the diagram and the second Lifeline on the right-hand side next to the first one. The length of the gap between the Lifelines will be fixed.

[IMAGE alt='' src='']

###### Gaps between Lifelines.

###### Lifelines Arrangement

A Lifeline can be nested within another component, such as a Part or Port. If this is the case, every component nested within the Lifeline and the Lifeline itself will be drawn separately in MagicDraw. They will be arranged in order depending on the position of their Lifeline lines.

[IMAGE alt='' src='']

###### Lifelines arrangement.

###### Class, Part, and Port

When represented as Lifelines, Classes, Parts, and Ports have different characteristics from the others. They will be bundled according to their relationships. A Composite Structure diagram provides one convenient way to create a Class, Part, or Port.

[IMAGE alt='' src='']

###### Class, Part, and Port.

##### Gate

A Sequence Message whose tail is connected to a Gate and head connected to a Lifeline in EA will be transformed into a Sequence Message with its tail connected to one of the boundary lines of the diagram in which it is contained. The Gate itself will be removed.

[IMAGE alt='' src='']

###### Gate.

Once the Gate has been removed and the transformation process has been completed, the following transformation message will open:

```text
: uml:Gate.]]>
```

A Sequence Message whose head is connected to a Gate and tail connected to a Lifeline line in EA will be transformed into a Reply Message with its tail connected to one of the boundary lines of the diagram in which it is contained. The Gate itself will be removed

[IMAGE alt='' src='']

###### Gate (EA) and Reply Message (MagicDraw).

The Diagonal Message and Reply Message will be connected tothe nearest diagram boundary.

[IMAGE alt='' src='']

###### Gate (EA) and Direction of Diagonal Message (MagicDraw).

Anything else connected to a Gate will also be removed, except the tail of a Sequence Message. For example, if the head of a Sequence Message is connected to a Gate, the Message will be removed. If the tail of a Message is connected to a Gate, but the head is connected to anything other than a Lifeline line, the Message will be removed.

##### Endpoints

A Sequence Message whose head connected to an Endpoint and tail connected to a Lifeline line in EA will be transformed into a Lost Message. The Endpoint element itself will be removed. Once the process has been completed, the following transformation message will open:

```text
: EndPoint.]]>
```

A Message whose head connected to a Lifeline line and tail connected to an Endpoint will be transformed into a Found Message.

[IMAGE alt='' src='']

###### Endpoint.

Anything else connected to an endpoint will also be removed, except the head of a Sequence Message. For example, if the tail of a Sequence Message is connected to an endpoint, the Message will be removed.

If the head of a Message is connected to an endpoint, but the tail is connected to anything other than a Lifeline line, the Message will be removed. Once the process has been completed, the following transformation message will open:

```text
: Invalid Message. Source and Target of the Message are not connected to any Lifeline.]]>
```

##### Delete Messages

A Sequence Message whose property 'Lifecycle' is set to 'Delete' (that causes the Lifeline targeted by the Message to end at some range after the point of contact), will be transformed into a Delete Message. The Lifeline connected to its head will end at the point of contact, and all Messages will be removed after that point of contact of the Lifeline. MagicDraw will report the following transformation message once each process has been completed:

```text
: Message is under Delete Message.]]>
```

[IMAGE alt='' src='']

###### Delete Messages.

Under certain circumstances, a Lifeline connected tothe head ofa Delete Message does notendatthepointofcontact.Instead,anActivationwillbecreatedandstartedfromthepointofcontact. TheLifelinewill thenendattheendoftheActivation.However,thatActivationshouldnot interact with any Message.

[IMAGE alt='' src='']

###### A special case of Delete Messages.

Under certain circumstances, an 'X' sign (normally drawn after a Delete Message) in EA will be drawn on a Lifeline line whose Lifeline is being pointed by a Create Message. If this is the case, the **X** sign has no significant meaning and can be ignored.

[IMAGE alt='' src='']

###### The X sign.

##### Branch Messages

If the **Branch with previous Message**option of a Sequence Message is enabled, the tail of the Message connect to the tail of its previous Message on the same Lifeline line. The Message will be called 'Branch Message' from that time on.

Every Branch Message in EAwill be transformed into a normal Message in MagicDraw.

[IMAGE alt='' src='']

###### A Branch Message.

After the transformation process has been completed, the following transformation message will open:

```text
: Branch Message updated to regular Message.]]>
```

##### Boundaries, Controls, and Entities

The Boundary, Control, and Entity elements in a Sequence diagram context in EA are Lifeline elements whose stereotype property types are set to *Boundary*, *Control*, or *Entity*. They will be imported like any other normal Lifelines. However, an XMI exported from EA has an <<entity>> stereotype problem. This means the Lifeline with the *<<entity>> stereotype* applied is unable to show the stereotype icon. You can solve this problem by placing an *<<entity>> stereotype* in *EA_Profile.xml.*The converted model can then use it instead of the one from EA.

[IMAGE alt='' src='']

###### Boundary, Control, and Entity.

##### Actors

An Actor element in the Sequence diagram context in EA is not a regular Lifeline element. It is a special Lifeline element whose property type is *uml:Actor*. It will be transformed into a regular Actor and a Lifeline element will be created to represent it. The figure below shows an Actor element in the MagicDraw Containment tree.

[IMAGE alt='' src='']

###### Actor.

##### General Ordering

Not every General Ordering element in EA will be imported, as MagicDraw does not support it in the current release.

[IMAGE alt='' src='']

###### General Ordering.

After completing the transformation process, the following transformation Message will open:

```text
: General Ordering will not be imported.]]>
```

##### State Invariant

A State Invariant in EA will be transformed as is. MagicDraw does not support State Invariants in the current release.

[IMAGE alt='' src='']

###### State Invariant.

##### Continuation

Continuations from EA can be imported to MagicDraw. They are viewable in the Containment tree in MagicDraw, but without a picture displayed in the diagram. MagicDraw does not support Continuations in the current release.

[IMAGE alt='' src='']

###### Continuation.

After completing the transformation process, the following transformation message will open:

```text
: Continuation will not be displayed.]]>
```

##### Diagonal Message

A Diagonal Message is a Message whose destination's height is adjustable. A diagonal Message may change Activations.

[IMAGE alt='' src='']

###### A Diagonal Message element.

Tocreate a Diagonal Message in EA,you mustspecify theTimingDetails property ofthe Message and add a numeric value tothe Duration Constraint input field.

[IMAGE alt='' src='']

###### Creating a Diagonal Message.

##### Synchronous Message Behavior

The placement of Synchronous Messages in EA affects the way Activations are created.

###### Order

A Message in EA has a 'Sequence Number' that indicates the order of the Message in the diagram. This information can be found in the exported XMI file. Knowing it helps predict how Activations will be created. The order starts from the top and goes downward, so the first Message in the diagram is the one drawn at the top of the diagram. Its Sequence Number will be set to '1'.

[IMAGE alt='' src='']

###### Message sequence number.

###### Process

Generally, in EA, any two Synchronous Messages will be in the same process if they meet the following conditions:

- Both of their tails are placed on the same Lifeline.
- The head of the upper Message and the tail of the lower Message are on the same Lifeline.

[IMAGE alt='' src='']

###### Process.

###### Activation level

The Activation Level starts from level 0. It will increase in increments of 1 as an ongoing process that receives a Message that is not a Return Message (Reply Message in MagicDraw).

[IMAGE alt='' src='']

###### Activation level.

##### Asynchronous Message Behavior

If a Message is an Asynchronous Message in EA, its source Activation will end if there is no other Message in the same group with a higher Sequence Number. Its source will be attached to the same Lifeline.

[IMAGE alt='' src='']

###### Asynchronous Message.

##### Return Message Behavior

A Return Message in EA is called a Reply Message in MagicDraw. When it is pointed to an Activation, it will not create an Activation at the top of the existing Activation, unlike other normal Synchronous Messages.

[IMAGE alt='' src='']

###### Return Message.

##### Activation options

You can control how Activations behave at some level through the Message options. You can access Message options by right-clicking any Message, and then selecting the **Activations**option. However, MagicDraw does not support Activation options in the current release.

[IMAGE alt='' src='']

###### Activation options.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="60f37c22-a730-499e-b5c6-00043a3e8b10"><ac:parameter ac:name="id">1401567461</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="5b6731d6-7627-4897-be3a-7cef67e96486"><ac:parameter ac:name="id">1401567463</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="211f0b6a-79eb-4d01-9aa6-63fb9a4afbc5"><ac:parameter ac:name="id">1401567460</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f5e11967-3883-444f-a5a5-da3ceb0ff423"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="62db403e-68b5-40c1-a6f5-9c5cd1ea3bf8"><ac:parameter ac:name="id">1401567462</ac:parameter><ac:rich-text-body><h3>Lifelines</h3><p>All of the EA Lifelines will be imported, but a Part or Port within a Lifeline will be transformed into a new separate Lifeline.</p><h4>Gaps between Lifelines</h4><p>The position and width of any Lifeline created in EA will not be imported. Every Lifeline will be given a fixed value and position in MagicDraw. MagicDraw will place the first Lifeline on the left-hand side of the diagram and the second Lifeline on the right-hand side next to the first one. The length of the gap between the Lifelines will be fixed.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="gaps_lifelines.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Gaps between Lifelines.</h6><h4>Lifelines Arrangement</h4><p>A Lifeline can be nested within another component, such as a Part or Port. If this is the case, every component nested within the Lifeline and the Lifeline itself will be drawn separately in MagicDraw. They will be arranged in order depending on the position of their Lifeline lines.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="lifelines_arrangement.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Lifelines arrangement.</h6><h4>Class, Part, and Port</h4><p>When represented as Lifelines, Classes, Parts, and Ports have different characteristics from the others. They will be bundled according to their relationships. A Composite Structure diagram provides one convenient way to create a Class, Part, or Port.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="class_part_port.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Class, Part, and Port.</h6><h3>Gate</h3><p>A Sequence Message whose tail is connected to a Gate and head connected to a Lifeline in EA will be transformed into a Sequence Message with its tail connected to one of the boundary lines of the diagram in which it is contained. The Gate itself will be removed.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="gate.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Gate.</h6><p>Once the Gate has been removed and the transformation process has been completed, the following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f65279d1-3fe6-4a51-9a31-58e93f2a1ff4"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed element <xmi:id>: uml:Gate.]]></ac:plain-text-body></ac:structured-macro><p>A Sequence Message whose head is connected to a Gate and tail connected to a Lifeline line in EA will be transformed into a Reply Message with its tail connected to one of the boundary lines of the diagram in which it is contained. The Gate itself will be removed</p><p><ac:image ac:align="center"><ri:attachment ri:filename="gateEA_replyMD.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Gate (EA) and Reply Message (MagicDraw).</h6><p><span>The Diagonal Message and Reply Message will be connected to<span> </span>the nearest diagram boundary.</span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="gateEA_diagonalMD.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Gate (EA) and Direction of Diagonal Message (MagicDraw).</h6><p>Anything else connected to a Gate will also be removed, except the tail of a Sequence Message. For example, if the head of a Sequence Message is connected to a Gate, the Message will be removed. If the tail of a Message is connected to a Gate, but the head is connected to anything other than a Lifeline line, the Message will be removed.</p><h3>Endpoints</h3><p>A Sequence Message whose head connected to an Endpoint and tail connected to a Lifeline line in EA will be transformed into a Lost Message. The Endpoint element itself will be removed. Once the process has been completed, the following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="be70fbc0-382b-4e32-9b74-115be6f24dfb"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed element <xmi:id>: EndPoint.]]></ac:plain-text-body></ac:structured-macro><p>A Message whose head connected to a Lifeline line and tail connected to an Endpoint will be transformed into a Found Message.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="endpoint.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Endpoint.</h6><p>Anything else connected to an endpoint will also be removed, except the head of a Sequence Message. For example, if the tail of a Sequence Message is connected to an endpoint, the Message will be removed.</p><p>If the head of a Message is connected to an endpoint, but the tail is connected to anything other than a Lifeline line, the Message will be removed. Once the process has been completed, the following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="1dfaad20-a7d2-46ea-a81c-30564ebd5ab0"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed element <xmi:id>: Invalid Message. Source and Target of the Message are not connected to any Lifeline.]]></ac:plain-text-body></ac:structured-macro><h3>Delete Messages</h3><p>A Sequence Message whose property 'Lifecycle' is set to 'Delete' (that causes the Lifeline targeted by the Message to end at some range after the point of contact), will be transformed into a Delete Message. The Lifeline connected to its head will end at the point of contact, and all Messages will be removed after that point of contact of the Lifeline. MagicDraw will report the following transformation message once each process has been completed:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="1e316008-0ff3-4472-b409-6838c8fc1fbd"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed element <xmi:id>: Message is under Delete Message.]]></ac:plain-text-body></ac:structured-macro><p><ac:image ac:align="center"><ri:attachment ri:filename="deleteMessage.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Delete Messages.</h6><p><span>Under certain circumstances, a Lifeline connected to<span> </span>the head of<span> </span>a Delete Message does not<span> </span>end<span> </span>at<span> </span>the<span> </span>point<span> </span>of<span> </span>contact.<span> </span>Instead,<span> </span>an<span> </span>Activation<span> </span>will<span> </span>be<span> </span>created<span> </span>and<span> </span>started<span> </span>from<span> </span>the<span> </span>point<span> </span>of<span> </span>contact. The<span> </span>Lifeline<span> </span>will then<span> </span>end<span> </span>at<span> </span>the<span> </span>end<span> </span>of<span> </span>the<span> </span>Activation.<span> </span>Howeve<span>r</span>,<span> </span>that<span> </span>Activation<span> </span>should<span> </span>not interact with any Message.</span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="deleteMessage_special.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A special case of Delete Messages.</h6><p>Under certain circumstances, an 'X' sign (normally drawn after a Delete Message) in EA will be drawn on a Lifeline line whose Lifeline is being pointed by a Create Message. If this is the case, the <strong>X</strong> sign has no significant meaning and can be ignored. </p><p><ac:image ac:align="center"><ri:attachment ri:filename="xsign.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The X sign.</h6><h3>Branch Messages</h3><p>If the <strong>Branch with previous Message </strong>option of a Sequence Message is enabled, the tail of the Message connect to the tail of its previous Message on the same Lifeline line. The Message will be called 'Branch Message' from that time on.</p><p><span>Every Branch Message in EA<span> </span>will be transformed into a normal Message in MagicDraw.</span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="branchMessage.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Branch Message.</h6><p>After the transformation process has been completed, the following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="cb04064c-6d53-4e66-b3e9-e2a46f5ad5e6"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: Branch Message updated to regular Message.]]></ac:plain-text-body></ac:structured-macro><h3>Boundaries, Controls, and Entities</h3><p>The Boundary, Control, and Entity elements in a Sequence diagram context in EA are Lifeline elements whose stereotype property types are set to <em>Boundary</em>, <em>Control</em>, or <em>Entity</em>. They will be imported like any other normal Lifelines. However, an XMI exported from EA has an &lt;&lt;entity&gt;&gt; stereotype problem. This means the Lifeline with the <em>&lt;&lt;entity&gt;&gt; stereotype</em> applied is unable to show the stereotype icon. You can solve this problem by placing an <em>&lt;&lt;entity&gt;&gt; stereotype</em> in <em>EA_Profile.xml. </em>The converted model can then use it instead of the one from EA.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="boundary_control_entity.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Boundary, Control, and Entity.</h6><h3>Actors</h3><p>An Actor element in the Sequence diagram context in EA is not a regular Lifeline element. It is a special Lifeline element whose property type is <em>uml:Actor</em>. It will be transformed into a regular Actor and a Lifeline element will be created to represent it. The figure below shows an Actor element in the MagicDraw Containment tree.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="actor.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Actor.</h6><h3>General Ordering</h3><p>Not every General Ordering element in EA will be imported, as MagicDraw does not support it in the current release.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="generalOrdering.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">General Ordering.</h6><p>After completing the transformation process, the following transformation Message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="698dfb62-5fc6-4160-be58-579e0b2799df"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: General Ordering will not be imported.]]></ac:plain-text-body></ac:structured-macro><h3>State Invariant</h3><p>A State Invariant in EA will be transformed as is. MagicDraw does not support State Invariants in the current release.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="stateInvariant.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">State Invariant.</h6><h3>Continuation</h3><p>Continuations from EA can be imported to MagicDraw. They are viewable in the Containment tree in MagicDraw, but without a picture displayed in the diagram. MagicDraw does not support Continuations in the current release.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="continuation.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Continuation.</h6><p>After completing the transformation process, the following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f20a8a84-30fe-4590-a1f2-9d8e90566e93"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: Continuation will not be displayed.]]></ac:plain-text-body></ac:structured-macro><h3>Diagonal Message</h3><p>A Diagonal Message is a Message whose destination's height is adjustable. A diagonal Message may change Activations.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="diagonalMessage.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;"><span>A Diagonal Message element.<br /></span></h6><p><span>T</span><span>o<span> </span>create a Diagonal Message in EA,<span> </span>you must<span> </span>specify the<span> </span><span>T</span>iming<span> </span>Details property of<span> </span>the Message and add a numeric value to<span> </span>the Duration Constraint input field.</span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="create_diagonalMessage.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Creating a Diagonal Message.</h6><h3>Synchronous Message Behavior</h3><p>The placement of Synchronous Messages in EA affects the way Activations are created.</p><h4>Order</h4><p>A Message in EA has a 'Sequence Number' that indicates the order of the Message in the diagram. This information can be found in the exported XMI file. Knowing it helps predict how Activations will be created. The order starts from the top and goes downward, so the first Message in the diagram is the one drawn at the top of the diagram. Its Sequence Number will be set to '1'.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Message_sequenceNo.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Message sequence number.</h6><h4>Process</h4><p>Generally, in EA, any two Synchronous Messages will be in the same process if they meet the following conditions:</p><ul><li>Both of their tails are placed on the same Lifeline.</li><li>The head of the upper Message and the tail of the lower Message are on the same Lifeline.</li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="process.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Process.</h6><h4>Activation level</h4><p>The Activation Level starts from level 0. It will increase in increments of 1 as an ongoing process that receives a Message that is not a Return Message (Reply Message in MagicDraw).</p><p><ac:image ac:align="center"><ri:attachment ri:filename="activationLevel.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Activation level.</h6><h3>Asynchronous Message Behavior</h3><p>If a Message is an Asynchronous Message in EA, its source Activation will end if there is no other Message in the same group with a higher Sequence Number. Its source will be attached to the same Lifeline.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="asynchronous_message.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Asynchronous Message.</h6><h3>Return Message Behavior</h3><p>A Return Message in EA is called a Reply Message in MagicDraw. When it is pointed to an Activation, it will not create an Activation at the top of the existing Activation, unlike other normal Synchronous Messages.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="returnMessage.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Return Message.</h6><h3>Activation options</h3><p>You can control how Activations behave at some level through the Message options. You can access Message options by right-clicking any Message, and then selecting the <strong>Activations </strong>option. However, MagicDraw does not support Activation options in the current release.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="activationOptions.png"><ri:page ri:content-title="Sequence diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Activation options.</h6></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643663 space=EAI2024xR2 version=1 -->
## PAGE 00016: Special Transformation

- page_id: `194643663`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643663/Special+Transformation
- version_number: 1
- version_date: `2020-10-05T08:02:09.040+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

1400518686

1400518697

1400518687

An EA-exported XMI contains both non-standard UML elements and elements that can break the XMI schema. To retain standard UML elements and keep the XMI schema intact, the Enterprise Architect Import Plugin applies specific transformation rules. The following sections describe how the plugin transforms each model element, enabling you to import a complete XMI model that conforms to UML standards.

1400518685

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="2ff0bdad-fc3b-4655-ac2f-c9104d43ccaf"><ac:parameter ac:name="id">1400518686</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ef444e01-b974-4bb2-a0f2-2ebd80a47d7e"><ac:parameter ac:name="id">1400518697</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a0365897-6350-4768-ae10-c165018bf144"><ac:parameter ac:name="id">1400518687</ac:parameter><ac:rich-text-body><p>An EA-exported XMI contains both non-standard UML elements and elements that can break the XMI schema. To retain standard UML elements and keep the XMI schema intact, the Enterprise Architect Import Plugin applies specific transformation rules. The following sections describe how the plugin transforms each model element, enabling you to import a complete XMI model that conforms to UML standards.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="fd1e0266-d431-4d2f-b20c-603ad2fb11cf"><ac:parameter ac:name="id">1400518685</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f34cc2ac-1b86-4e92-a521-57071f59087c" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643725 space=EAI2024xR2 version=1 -->
## PAGE 00017: State Machine diagram

- page_id: `194643725`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643725/State+Machine+diagram
- version_number: 1
- version_date: `2020-10-05T08:35:16.307+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Special Transformation
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

1402114021

#### CONTENT-COLUMN: Note

1402114032

1402114019

**On this page**

43

#### CONTENT-BLOCK: Note

1402114022

##### StateMachine

After conversion, a dummy StateMachine element will be created. The dummy StateMachine is either created by the XMI exporter from EA or by EA Import plugin. A StateMachine diagram will be placed inside the dummy StateMachine and a dummy Region element will be created to contain all of the StateMachine elements.

[IMAGE alt='' src='']

###### A dummy StateMachine element and a dummy Region element.

##### State

###### State containing other elements

A State element containing other elements will be transformed to a Composite State. All of the contained elements will be placed inside the Region element of the State element.

[IMAGE alt='' src='']

###### A State containing other elements.

###### State containing a StateMachine

If a State element contains a StateMachine element, the StateMachine element will be brought out and placed at the same level of the Region element of the State element.

[IMAGE alt='' src='']

###### A State containing a StateMachine.

###### State containing Attributes and Operations

If a State element contains Attribute and Operation elements, the Attribute and Operation elements will be removed from both the Diagram view and Containment tree.

[IMAGE alt='' src='']

###### A State containing Attributes and Operations.

The following transformation messages will open:

```text
: State cannot contain Attribute.
Removed element : State cannot contain Operation.]]>
```

###### State containing a Diagram Element

If a diagram element is placed inside a State element, it will be removed.

[IMAGE alt='' src='']

###### A State containing a Diagram element.

The following transformation message will open:

```text
: State cannot contain diagram element.]]>
```

##### StateMachine placed on a diagram

If a StateMachine element is drawn in a StateMachine diagram, an additional SubMachineState will be created to represent the StateMachine.

#### NOTE: Note

Note

A SubMachine State is a State whose SubMachine property is set to a StateMachine.

[IMAGE alt='' src='']

###### A StateMachine represented by a SubMachine State.

##### Object

An Object element placed in a State Machine diagram will be removed from the Diagram view. However, its data will be preserved in the Containment tree as an InstanceSpecification.

[IMAGE alt='' src='']

###### An Object.

The following transformation message will open:

```text
: The view represents element that does not support in State Machine Diagram.]]>
```

###### Object containing a State Machine element

In EA, an Object element can contain a State Machine element. After it has been imported to MagicDraw, the State Machine element placed inside an Object element will be removed both from the Diagram view and Containment tree. However, the Object element data will be preserved. All of the Object element data will be placed at the closest owner package of the Object element.

[IMAGE alt='' src='']

###### An Object containing a State Machine Element.

The following transformation message will open:

```text
: Invalid element. Instancespecification cannot contain element from State Machine.]]>
```

##### Synch

A Synch element will be transformed to a Junction element.

[IMAGE alt='' src='']

###### A Synch element.

The following transformation message will open:

```text
: Synch updated to Junction.]]>
```

##### EntryPoint / ExitPoint

An Entry or Exit point placed inside a State (or StateMachine) element will be placed outside a Region element of its parent element in the Containment tree. It will be relocated to the nearest boundary of its parent element in the Diagram view.

[IMAGE alt='' src='']

###### An Entry/Exit point.

##### Object Flow connecting State Machine elements

An Object Flow connecting the elements in a State Machine will be removed from both the Diagram view and Containment tree.

[IMAGE alt='' src='']

###### An ObjectFlow connecting State Machine elements.

The following transformation message will open:

```text
: Invalid ObjectFlow. Source or Target of theObjectFlow are connected to element from State Machine.]]>
```

##### Information Flow connecting State Machine elements

An Information Flow connecting the elements in a State Machine will be removed from the Diagram view; however, its data will be preserved.

[IMAGE alt='' src='']

###### Information Flow, Trace, and Dependency.

The following transformation message will open:

```text
: The view represents element that does not support in State Machine Diagram.]]>
```

##### Trigger

If there is a Trigger element unrelated to any Transition line, a dummy StateMachine will be created to hold the Trigger element. The dummy StateMachine will be named after the parent package name concatenated with a Trigger.

In the case of a Trigger element related to Transition, the data of the Trigger element will be placed inside its parent Transition. Each Trigger element will be given an event type, represented by an Event element. After conversion, the Event will be placed at the closest owner package of the Event.

[IMAGE alt='' src='']

###### A Trigger element.

##### Self Transition

Most of the elements in a StateMachine diagram can have a self transition, except the Initial, Final, and History elements. The self transition in these three elements will be removed from the Diagram view, but the data of the self transition will be preserved in the Containment tree.

[IMAGE alt='' src='']

###### A Self Transition.

The following transformation messages will open:

```text
: Self Transition does not support forInitial.
Removed view : Self Transition does not support forFinal.
Removed view : Self Transition does not support forHistory.]]>
```

##### Removed element

Any element which is not the element of a State Machine diagram (such as Class, Actor, Use-case, or Action) drawn in the State Machine diagram will be removed from the Diagram view. However, its data will be preserved in the Containment tree.

[IMAGE alt='' src='']

###### A removed element.

Ifan element which is not the element ofa StateMachine diagram has a child element and is drawn in the StateMachine diagram, the element will be removed from the Diagram view. However, its data will be preserved in the Containment tree.

[IMAGE alt='' src='']

###### A removed element with a child element.

The following transformation message will open:

```text
:The view represents element that does not support in State Machine Diagram.]]>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a86654fe-78ad-4ff4-bb62-680fc6bbc572"><ac:parameter ac:name="id">1402114021</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="0fd19671-06a0-46ce-a92b-690a925b54d7"><ac:parameter ac:name="id">1402114032</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3e2ecef8-590e-41d5-b90c-ff5cd2667e8b"><ac:parameter ac:name="id">1402114019</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="fa06c9b5-57f5-45ef-b068-02cc9b4ca22f"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="333a7b92-38df-4f91-9050-addd0e44b2c0"><ac:parameter ac:name="id">1402114022</ac:parameter><ac:rich-text-body><h3>StateMachine</h3><p>After conversion, a dummy StateMachine element will be created. The dummy StateMachine is either created by the XMI exporter from EA or by EA Import plugin. A StateMachine diagram will be placed inside the dummy StateMachine and a dummy Region element will be created to contain all of the StateMachine elements.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="StateMachine.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A dummy StateMachine element and a dummy Region element.</h6><h3>State</h3><h4>State containing other elements</h4><p>A State element containing other elements will be transformed to a Composite State. All of the contained elements will be placed inside the Region element of the State element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="state_containElement.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A State containing other elements.</h6><h4>State containing a StateMachine</h4><p>If a State element contains a StateMachine element, the StateMachine element will be brought out and placed at the same level of the Region element of the State element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="state_containStatemachine.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A State containing a StateMachine.</h6><h4>State containing Attributes and Operations</h4><p>If a State element contains Attribute and Operation elements, the Attribute and Operation elements will be removed from both the Diagram view and Containment tree.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="state_containAttribute.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A State containing Attributes and Operations.</h6><p>The following transformation messages will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="5e9ef00b-33a0-4ccb-a80e-db6def4a3b1c"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed element <xmi:id>: State cannot contain Attribute.
Removed element <xmi:id>: State cannot contain Operation.]]></ac:plain-text-body></ac:structured-macro><h4>State containing a Diagram Element</h4><p>If a diagram element is placed inside a State element, it will be removed.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="state_containDiagram.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A State containing a Diagram element.</h6><p>The following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="26f6ebc0-d47d-41bb-86e3-ef28ec645c2b"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed element <xmi:id>: State cannot contain diagram element.]]></ac:plain-text-body></ac:structured-macro><h3>StateMachine placed on a diagram</h3><p>If a StateMachine element is drawn in a StateMachine diagram, an additional SubMachineState will be created to represent the StateMachine.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="de586889-301c-4944-9e4e-8629abecdc0e"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>A SubMachine State is a State whose SubMachine property is set to a StateMachine.</p></ac:rich-text-body></ac:structured-macro><p><ac:image ac:align="center"><ri:attachment ri:filename="stateMachine_representedbySMstate.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A StateMachine represented by a SubMachine State.</h6><h3>Object</h3><p>An Object element placed in a State Machine diagram will be removed from the Diagram view. However, its data will be preserved in the Containment tree as an InstanceSpecification.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="object.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Object.</h6><p>The following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d6b9db30-5f8b-4ad7-ade7-3f5fd1d3a5d8"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed view <xmi:id>: The view represents element that does not support in State Machine Diagram.]]></ac:plain-text-body></ac:structured-macro><h4>Object containing a State Machine element</h4><p>In EA, an Object element can contain a State Machine element. After it has been imported to MagicDraw, the State Machine element placed inside an Object element will be removed both from the Diagram view and Containment tree. However, the Object element data will be preserved. All of the Object element data will be placed at the closest owner package of the Object element.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="object_containSMelement.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Object containing a State Machine Element.</h6><p>The following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="56123747-c088-4f42-b4e9-e8da02469f41"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed element <xmi:id>: Invalid element. Instancespecification cannot contain element from State Machine.]]></ac:plain-text-body></ac:structured-macro><h3>Synch</h3><p>A Synch element will be transformed to a Junction element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="synch.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Synch element.</h6><p>The following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="0bbd8609-fff2-4699-9feb-e007c1c45855"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Updated element <xmi:id>: Synch updated to Junction.]]></ac:plain-text-body></ac:structured-macro><h3>EntryPoint / ExitPoint</h3><p>An Entry or Exit point placed inside a State (or StateMachine) element will be placed outside a Region element of its parent element in the Containment tree. It will be relocated to the nearest boundary of its parent element in the Diagram view.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="entryexit_point.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An Entry/Exit point.</h6><h3>Object Flow connecting State Machine elements</h3><p>An Object Flow connecting the elements in a State Machine will be removed from both the Diagram view and Containment tree.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="objectflow_connectSMelement.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An ObjectFlow connecting State Machine elements.</h6><p>The following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c46f2b39-1d89-4c80-9636-38cda9c3e19b"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed element <xmi:id>: Invalid ObjectFlow. Source or Target of theObjectFlow are connected to element from State Machine.]]></ac:plain-text-body></ac:structured-macro><h3>Information Flow connecting State Machine elements</h3><p>An Information Flow connecting the elements in a State Machine will be removed from the Diagram view; however, its data will be preserved.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="infoflow_connectSMelement.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Information Flow, Trace, and Dependency.</h6><p>The following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="23c8769b-3cb1-40bc-bf85-fc13a519a1d4"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed element <xmi:id>: The view represents element that does not support in State Machine Diagram.]]></ac:plain-text-body></ac:structured-macro><p><br /></p><h3>Trigger</h3><p>If there is a Trigger element unrelated to any Transition line, a dummy StateMachine will be created to hold the Trigger element. The dummy StateMachine will be named after the parent package name concatenated with a Trigger.</p><p>In the case of a Trigger element related to Transition, the data of the Trigger element will be placed inside its parent Transition. Each Trigger element will be given an event type, represented by an Event element. After conversion, the Event will be placed at the closest owner package of the Event.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="trigger.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Trigger element.</h6><h3>Self Transition</h3><p>Most of the elements in a StateMachine diagram can have a self transition, except the Initial, Final, and History elements. The self transition in these three elements will be removed from the Diagram view, but the data of the self transition will be preserved in the Containment tree.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="selfTransition.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Self Transition.</h6><p>The following transformation messages will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4a522d75-6eec-416a-abba-3939d3d23c7a"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed view <xmi:id>: Self Transition does not support forInitial.
Removed view <xmi:id>: Self Transition does not support forFinal.
Removed view <xmi:id>: Self Transition does not support forHistory.]]></ac:plain-text-body></ac:structured-macro><h3>Removed element</h3><p>Any element which is not the element of a State Machine diagram (such as Class, Actor, Use-case, or Action) drawn in the State Machine diagram will be removed from the Diagram view. However, its data will be preserved in the Containment tree.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="removedElement.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(112,112,112);">A removed element.</span></h6><p><span>If<span> </span>an element which is not the element of<span> </span>a State<span> </span>Machine diagram has a child element and is drawn in the State<span> </span>Machine diagram, the element will be removed from the Diagram vie<span>w. H</span>oweve<span>r</span>, its data will be preserved in the Containment tree.</span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="removedElement_withchild.png"><ri:page ri:content-title="State Machine diagram" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A removed element with a child element.</h6><p>The following transformation message will open:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="673a6388-a714-4e10-96c0-8fbd85183cb2"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[Removed view <xmi:id>:The view represents element that does not support in State Machine Diagram.]]></ac:plain-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643659 space=EAI2024xR2 version=1 -->
## PAGE 00018: Transforming EA Specific Data

- page_id: `194643659`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643659/Transforming+EA+Specific+Data
- version_number: 1
- version_date: `2020-10-05T08:00:00.382+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

1399692571

#### CONTENT-COLUMN: Note

1399692584

1400288818

**On this page**

33

#### CONTENT-BLOCK: Note

1399692574

In addition to UML data, each EA-exported XMI contains EA-specific information. The Enterprise Architect Import Plugin can transform this particular information into UML elements with the stereotypes applied if you include EA-specific data before importing the XMI file. This data includes:

- Constraints: name, description, type, weight, and status.
- Requirements: name, description, type, status, difficulty, priority, and last update.
- Scenarios: name, description, type, and weight.
- Files: file path type.
- Requirements (External): type, status, difficulty, priority, last update, created, and note.
- Changes: type, status, difficulty, priority, last update, created, and note.
- Issues: type, status, difficulty, priority, last update, created, and note.

#### NOTE: Note

Note

You can access and specify the EA information in the **Property**dialog in EA.

****

To include EA-specific data in the transformation process, the plugin creates a set of stereotypes and tag definitions as the EA Profile.

[IMAGE alt='' src='']

###### The EA Profile in a treeview.

##### Constraints

Each EA constraint will be transformed into a UML constraint and <<EAConstraint>> will be applied to the constraint. The properties of an EA constraint will be mapped either to the properties of a UML constraint or to the tag values of <<EAConstraint>>. The following table shows the constraint mapping details.

| EA | MagicDraw |
| --- | --- |
| name | The name property of a UML constraint. |
| description | EAConstraint::type tag value. |
| type | EAConstraint::weight tag value. |
| weight | EAConstraint::status tag value. |
| constraint owner | Constrained Element property point to the constraint owner. |

##### Requirements

Each EARequirement will be transformed into a UML Class. Because a Requirement cannot be created in an element that is the owner ofa Class in EA, the transformed Requirement will be kept in a separatePackage,named**EARequirement**. ARealizationwillthenbecreatedfromtheownerofthe Requirement into a transformed Requirement. See the following table fordetails.

| EA | MagicDraw |
| --- | --- |
| name | EARequirement :: name tag value |
| description | EARequirement :: description tag value |
| type | EARequirement :: type tag value |
| status | EARequirement :: status tag value |
| difficulty | EARequirement :: difficulty tag value |
| priority | EARequirement :: priority tag value |
| last update | EARequirement :: name update value |

##### Scenarios

Each EA scenario will be transformed into a UML Comment and <<EAScenario>> will be applied to the comment. The properties of a scenario will be mapped either to the properties of each UML Comment or to the tag values of <<EAScenario>>. See the following table for details.

| EA | MagicDraw |
| --- | --- |
| name | EAScenario::name tag value |
| description | The Body property of a UML Comment. |
| type | EAScenario :: type tag value |
| weight | EARequirement :: weight tag value |
| subject | An annotated Element property pointing to an EA subject element. |

##### Files

EA can add files to a UML element. The information will be transformed into a Hyperlink in MagicDraw.

| EA | MagicDraw |
| --- | --- |
| Local file | File |
| Web address | Webpage. |

##### Requirements (external)

An EA-created Requirement differs from the one you create as an internal element for each element. EA Requirements will appear in the Project Browser and can be pasted on a diagram. Each EA Requirement will be transformed into a Class and <<EARequirement>> will be applied to the Requirement.

| EA | MagicDraw |
| --- | --- |
| type | EARequirement :: type tag value |
| status | EARequirement :: status tag value |
| difficulty | EARequirement :: difficulty tag value |
| priority | EARequirement :: priority tag value |
| last update | EARequirement :: last update value |
| created | EARequirement :: created tag value |
| note | Documentation |

##### Changes

EA can create a Change and will export it as a Class. The Class information will be transformed into the <<EAChange>> tag values. See the following table for details.

| EA | MagicDraw |
| --- | --- |
| type | EAChange :: type tag value |
| status | EAChange :: status tag value |
| difficulty | EAChange :: difficulty tag value |
| priority | EAChange :: priority tag value |
| last update | EAChange :: last update value |
| created | EAChange :: created tag value |
| note | Documentation |

##### Issues

EA can create an Issue and will export it as a Class. The Issue information will be transformed into the <<EAIssue>> tag values. See the following table for details.

| EA | MagicDraw |
| --- | --- |
| type | EAIssue :: type tag value |
| status | EAIssue :: status tag value |
| difficulty | EAIssue :: difficulty tag value |
| priority | EAIssue :: priority tag value |
| last update | EAIssue :: last update value |
| created | EAIssue :: created tag value |
| note | Documentation |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="2f052a8e-c626-4e1f-8d4a-fc1dcf0212e0"><ac:parameter ac:name="id">1399692571</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="17282bd1-eeb6-4aa2-acdb-744ca05d1885"><ac:parameter ac:name="id">1399692584</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="daba6bc6-f6b4-4df0-9c20-72fc93439d03"><ac:parameter ac:name="id">1400288818</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="b953ab21-b10a-4281-a232-df11de3fd235"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7f8679f6-5f09-45c0-88de-fed748234f88"><ac:parameter ac:name="id">1399692574</ac:parameter><ac:rich-text-body><p>In addition to UML data, each EA-exported XMI contains EA-specific information. The Enterprise Architect Import Plugin can transform this particular information into UML elements with the stereotypes applied if you include EA-specific data before importing the XMI file. This data includes:</p><ul><li>Constraints: name, description, type, weight, and status.</li><li>Requirements: name, description, type, status, difficulty, priority, and last update.</li><li>Scenarios: name, description, type, and weight.</li><li>Files: file path type.</li><li>Requirements (External): type, status, difficulty, priority, last update, created, and note.</li><li>Changes: type, status, difficulty, priority, last update, created, and note.</li><li>Issues: type, status, difficulty, priority, last update, created, and note.<br /><br /></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="765991d4-cad8-453e-bf03-a6abb4db1989"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>You can access and specify the EA information in the <strong>Property </strong>dialog in EA.</p></ac:rich-text-body></ac:structured-macro><p><strong>           </strong></p><p>To include EA-specific data in the transformation process, the plugin creates a set of stereotypes and tag definitions as the EA Profile.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="treeview.png"><ri:page ri:content-title="Transforming EA Specific Data" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The EA Profile in a treeview.</h6><h3 style="text-align: left;">Constraints</h3><p>Each EA constraint will be transformed into a UML constraint and &lt;&lt;EAConstraint&gt;&gt; will be applied to the constraint. The properties of an EA constraint will be mapped either to the properties of a UML constraint or to the tag values of &lt;&lt;EAConstraint&gt;&gt;. The following table shows the constraint mapping details.</p><table class="relative-table wrapped" style="width: 47.0588%;"><colgroup><col style="width: 25.2115%;" /><col style="width: 74.7885%;" /></colgroup><tbody><tr><th>EA</th><th>MagicDraw</th></tr><tr><td>name</td><td><span>The name property of<span> </span>a UML constraint.</span></td></tr><tr><td>description</td><td><span>EAConstraint::type tag value.</span></td></tr><tr><td>type</td><td><span>EAConstraint::weight tag value.</span></td></tr><tr><td>weight</td><td><span>EAConstraint::status tag value.</span></td></tr><tr><td>constraint owner</td><td><span>Constrained Element property point to<span> </span>the constraint owne<span>r</span>.</span></td></tr></tbody></table><h3>Requirements</h3><p><span>Each EA<span> </span>Requirement will be transformed into a UML Class. Because a Requirement cannot be created in an element that is the owner of<span> </span>a Class in EA, the transformed Requirement will be kept in a separate<span> </span>Package,<span> </span>named<span> </span><strong>EA<span> </span>Requirement</strong>. <span>A</span><span> </span>Realization<span> </span>will<span> then </span>be<span> </span>created<span> </span>from<span> </span>the<span> </span>owner<span> </span>of<span> </span>the Requirement into a transformed Requirement. See the following table for<span> </span>details.</span></p><table class="relative-table wrapped" style="width: 47.2178%;"><colgroup><col style="width: 25.2951%;" /><col style="width: 74.7049%;" /></colgroup><tbody><tr><th>EA</th><th>MagicDraw</th></tr><tr><td>name</td><td><span>EARequirement ::<span> </span>name tag value</span></td></tr><tr><td>description</td><td><span>EARequirement ::<span> </span>description tag value</span></td></tr><tr><td>type</td><td><span>EARequirement ::<span> </span>type tag value</span></td></tr><tr><td>status</td><td><span>EARequirement ::<span> </span>status<span> </span>tag value</span></td></tr><tr><td>difficulty</td><td><span>EARequirement ::<span> </span>di<span>f</span>ficulty tag value</span></td></tr><tr><td>priority</td><td><span>EARequirement ::<span> </span>priority tag value</span></td></tr><tr><td>last update</td><td><span>EARequirement ::<span> </span>name update value</span></td></tr></tbody></table><h3>Scenarios</h3><p>Each EA scenario will be transformed into a UML Comment and &lt;&lt;EAScenario&gt;&gt; will be applied to the comment. The properties of a scenario will be mapped either to the properties of each UML Comment or to the tag values of &lt;&lt;EAScenario&gt;&gt;. See the following table for details.</p><table class="relative-table wrapped" style="width: 47.3768%;"><colgroup><col style="width: 25.7143%;" /><col style="width: 74.2857%;" /></colgroup><tbody><tr><th>EA</th><th>MagicDraw</th></tr><tr><td>name</td><td><span>EAScenario::name tag value</span></td></tr><tr><td>description</td><td><span>The Body property of<span> </span>a UML Comment. </span></td></tr><tr><td>type</td><td>EAScenario :: type tag value</td></tr><tr><td>weight</td><td>EARequirement :: weight tag value</td></tr><tr><td>subject</td><td><span>An annotated Element property pointing to<span> </span>an EA<span> </span>subject element.</span></td></tr></tbody></table><h3>Files</h3><p>EA can add files to a UML element. The information will be transformed into a Hyperlink in MagicDraw.</p><table class="relative-table wrapped" style="width: 35.1243%;"><colgroup><col style="width: 35.4691%;" /><col style="width: 64.5309%;" /></colgroup><tbody><tr><th>EA</th><th>MagicDraw</th></tr><tr><td>Local file</td><td>File</td></tr><tr><td>Web address</td><td>Webpage. </td></tr></tbody></table><h3>Requirements (external)</h3><p>An EA-created Requirement differs from the one you create as an internal element for each element. EA Requirements will appear in the Project Browser and can be pasted on a diagram. Each EA Requirement will be transformed into a Class and &lt;&lt;EARequirement&gt;&gt; will be applied to the Requirement.</p><table class="relative-table wrapped" style="width: 47.2178%;"><colgroup><col /><col /></colgroup><tbody><tr><th>EA</th><th>MagicDraw</th></tr><tr><td>type</td><td>EARequirement :: type tag value</td></tr><tr><td>status</td><td>EARequirement :: status tag value</td></tr><tr><td>difficulty</td><td>EARequirement :: difficulty tag value</td></tr><tr><td>priority</td><td>EARequirement :: priority tag value</td></tr><tr><td>last update</td><td>EARequirement :: last update value</td></tr><tr><td colspan="1">created</td><td colspan="1"><span>EARequirement :: created tag value</span></td></tr><tr><td colspan="1">note</td><td colspan="1">Documentation</td></tr></tbody></table><h3>Changes</h3><p>EA can create a Change and will export it as a Class. The Class information will be transformed into the &lt;&lt;EAChange&gt;&gt; tag values. See the following table for details.</p><table class="relative-table wrapped" style="width: 47.2178%;"><colgroup><col /><col /></colgroup><tbody><tr><th>EA</th><th>MagicDraw</th></tr><tr><td>type</td><td>EAChange :: type tag value</td></tr><tr><td>status</td><td>EAChange :: status tag value</td></tr><tr><td>difficulty</td><td>EAChange :: difficulty tag value</td></tr><tr><td>priority</td><td>EAChange :: priority tag value</td></tr><tr><td>last update</td><td>EAChange :: last update value</td></tr><tr><td colspan="1">created</td><td colspan="1">EAChange :: created tag value</td></tr><tr><td colspan="1">note</td><td colspan="1">Documentation</td></tr></tbody></table><h3>Issues</h3><p>EA can create an Issue and will export it as a Class. The Issue information will be transformed into the &lt;&lt;EAIssue&gt;&gt; tag values. See the following table for details.</p><table class="relative-table wrapped" style="width: 47.2178%;"><colgroup><col /><col /></colgroup><tbody><tr><th>EA</th><th>MagicDraw</th></tr><tr><td>type</td><td>EAIssue :: type tag value</td></tr><tr><td>status</td><td>EA<span>Issue</span> :: status tag value</td></tr><tr><td>difficulty</td><td>EA<span>Issue</span> :: difficulty tag value</td></tr><tr><td>priority</td><td>EA<span>Issue</span> :: priority tag value</td></tr><tr><td>last update</td><td>EA<span>Issue</span> :: last update value</td></tr><tr><td colspan="1">created</td><td colspan="1">EA<span>Issue</span> :: created tag value</td></tr><tr><td colspan="1">note</td><td colspan="1">Documentation</td></tr></tbody></table></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643664 space=EAI2024xR2 version=1 -->
## PAGE 00019: Use Case diagram elements

- page_id: `194643664`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643664/Use+Case+diagram+elements
- version_number: 1
- version_date: `2020-10-05T08:03:35.598+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Special Transformation
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

1400571615

#### CONTENT-COLUMN: Note

1400571627

1400571614

**On this page**

43

#### CONTENT-BLOCK: Note

1400571617

This page describes all Use Case diagram elements.

##### Actor with Properties

An Actor with properties will be transformed into a Class with the **EAActor**stereotype.

[IMAGE alt='' src='']

###### An actor with properties.

#### NOTE: Note

Note

An Actor that has been converted to a Class with <<EAActor>> will not display some properties (such as Fill Color) because the stereotype image will be shown instead.

##### Use Case with Invalid Inner Elements

A NestedClassifier, ownedComment, ownedRule, ownedAttribute, or ownedOperation cannot be an inner element of a uml:UseCase. It will be moved to a new created realized Class.

[IMAGE alt='' src='']

###### A Use Case with invalid inner elements.

##### Boundary

A boundary in EA will be converted into a rectangle with rounded corners in MagicDraw. The boundary can contain inner elements. Unlike the rectangular boundary in MagicDraw, the boundary in EA will take all inner elements with it whenever it is moved.

[IMAGE alt='' src='']

###### Boundaries.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="27c9c4f6-9055-4bc3-b138-7b2f2e3790c6"><ac:parameter ac:name="id">1400571615</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="92c12233-bd99-44fe-bfb7-0412acee6806"><ac:parameter ac:name="id">1400571627</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3b7b606d-fefd-4d0e-83bc-c7344c7f74bd"><ac:parameter ac:name="id">1400571614</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="fa06c9b5-57f5-45ef-b068-02cc9b4ca22f"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="37dd28f5-6f30-4a39-92b2-bda7c1fa0c56"><ac:parameter ac:name="id">1400571617</ac:parameter><ac:rich-text-body><p>This page describes all Use Case diagram elements.</p><h3>Actor with Properties</h3><p>An Actor with properties will be transformed into a Class with the <strong>EAActor </strong>stereotype.</p><p class="auto-cursor-target"><ac:image ac:align="center"><ri:attachment ri:filename="actor_withproperty.png"><ri:page ri:content-title="Use Case diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(112,112,112);">An actor with properties.</span></h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7e58d8d1-6032-4ae9-ab51-92f87e6befc3"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>An Actor that has been converted to a Class with &lt;&lt;EAActor&gt;&gt; will not display some properties (such as Fill Color) because the stereotype image will be shown instead.</p></ac:rich-text-body></ac:structured-macro><h3>Use Case with Invalid Inner Elements</h3><p>A NestedClassifier, ownedComment, ownedRule, ownedAttribute, or ownedOperation cannot be an inner element of a uml:UseCase. It will be moved to a new created realized Class.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="UC_withinvalidelements.png"><ri:page ri:content-title="Use Case diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Use Case with invalid inner elements.</h6><h3>Boundary</h3><p>A boundary in EA will be converted into a rectangle with rounded corners in MagicDraw. The boundary can contain inner elements. Unlike the rectangular boundary in MagicDraw, the boundary in EA will take all inner elements with it whenever it is moved.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="boundaries.png"><ri:page ri:content-title="Use Case diagram elements" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(112,112,112);">Boundaries.</span></h6></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=194643640 space=EAI2024xR2 version=1 -->
## PAGE 00020: User Guide

- page_id: `194643640`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643640/User+Guide
- version_number: 1
- version_date: `2021-10-12T10:21:03.357+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation
- labels: ['featured', 'documentation-space-sample']

### NORMALIZED CONTENT

true1h4

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="67369544-aa23-45db-a367-44b9d926af31"><ac:parameter ac:name="all">true</ac:parameter><ac:parameter ac:name="depth">1</ac:parameter><ac:parameter ac:name="style">h4</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=194643650 space=EAI2024xR2 version=1 -->
## PAGE 00021: Using the Enterprise Architect Import plugin to import files

- page_id: `194643650`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643650/Using+the+Enterprise+Architect+Import+plugin+to+import+files
- version_number: 1
- version_date: `2020-08-28T07:18:05.058+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide > Working with Enterprise Architect Import Plugin
- labels: []

### NORMALIZED CONTENT

The following table describes the UI components of the **Import Enterprise Architect Files** dialog.

| UI component | Function |
| --- | --- |
| EA exported XMI: UML 2.1 (XMI2.1) | To specify an EA exported XMI file. You can click to select the file. |
| MagicDraw output filename (*.mdxml) | To specify a MagicDraw output filename. You can click to select the file. |
| Switch aggregation side | To configure the aggregation switch-side. This option is recommended for XMI files exported from EA 7.1. |
| Exclude EA specific data | To exclude all EA-specific data from being imported (see Transforming EA Specific Data to see a list of EA specific-data that can be transformed into UML elements with stereotypes). |
| Open project after conversion | To load the output project file once the conversion process has been completed. |
| Generate conversion log | To generate a conversion log and save it in the same folder as the MagicDraw output file. The same conversion information will also be displayed on the MagicDraw messages window. |

To open the **Import Enterprise Architect Files**dialog

- On the MagicDraw main menu, click File > Import From > Enterprise Architect UML2.1 XMI2.1 File to open the Import Enterprise Architect Files dialog. [IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The following table describes the UI components of the <strong>Import Enterprise Architect Files</strong> dialog.</p><table class="relative-table"><colgroup><col style="width: 306.0px;" /><col style="width: 721.0px;" /></colgroup><tbody><tr><th>UI component</th><th>Function</th></tr><tr><td><p>EA exported XMI: UML 2.1 (XMI2.1)</p></td><td><div class="content-wrapper"><p>To specify an EA exported XMI file. You can click <ac:image ac:thumbnail="true" ac:height="21"><ri:attachment ri:filename="browse_button.png"><ri:page ri:content-title="Using the Enterprise Architect Import plugin to import files" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image> to select the file.</p></div></td></tr><tr><td><p>MagicDraw output filename (*.mdxml)</p></td><td><div class="content-wrapper"><p>To specify a MagicDraw output filename. You can click <ac:image ac:thumbnail="true" ac:height="21"><ri:attachment ri:filename="browse_button.png"><ri:page ri:content-title="Using the Enterprise Architect Import plugin to import files" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image> to select the file.</p></div></td></tr><tr><td><span>Switch aggregation side</span></td><td><span>T</span><span>o<span> </span>configure the <strong>aggregation<span> </span>switch-side</strong>.<span> </span>This option is recommended for<span> </span>XMI<span> </span>files exported from EA<span> </span>7.1.</span></td></tr><tr><td><span>Exclude EA<span> </span>specific data</span></td><td><span>T</span><span>o<span> </span>exclude all EA-specific data from being imported (see <ac:link><ri:page ri:content-title="Transforming EA Specific Data" ri:space-key="EAI2024xR2" /><ac:link-body><span>T</span>ransforming<span> </span>EA<span> </span>Specific Data</ac:link-body></ac:link> to<span> </span>see a list of EA<span> </span>specific-data that<span> </span>can be transformed into UML elements with stereotypes).</span></td></tr><tr><td><span>Open project after<span> </span>conversion</span></td><td><span>T</span><span>o<span> </span>load the output project file once the conversion process has been completed.</span></td></tr><tr><td><span>Generate conversion log</span></td><td><p>To generate a conversion log and save it in the same folder as the MagicDraw output file. The same conversion information will also be displayed on the MagicDraw messages window.</p></td></tr></tbody></table><p>To open the <strong>Import Enterprise Architect Files </strong>dialog</p><hr /><ul><li>On the MagicDraw main menu, click <strong>File </strong>&gt; <strong>Import From </strong>&gt; <strong>Enterprise Architect UML2.1 XMI2.1 File</strong> to open the<strong> </strong> <strong>Import Enterprise Architect Files </strong>dialog.<br /><p><ac:image><ri:attachment ri:filename="EA_menu.png"><ri:page ri:content-title="Using the Enterprise Architect Import plugin to import files" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p></li></ul>
````

<!--NOMAGIC_PAGE id=194643645 space=EAI2024xR2 version=1 -->
## PAGE 00022: Working with Enterprise Architect Import Plugin

- page_id: `194643645`
- space_key: `EAI2024xR2`
- source_url: https://docs.nomagic.com/spaces/EAI2024xR2/pages/194643645/Working+with+Enterprise+Architect+Import+Plugin
- version_number: 1
- version_date: `2020-10-05T07:44:01.258+02:00`
- ancestors: Enterprise Architect Import Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

1399451339

1399451350

1399451349

The Enterprise Architect Import (EA) plugin will automatically load when you start MagicDraw. You can use it to import UML 2.1 XMI 2.1 to your modeling tool.

[IMAGE alt='' src='']

1399451338

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="2a2570fa-8e72-4394-84e2-30704100e62b"><ac:parameter ac:name="id">1399451339</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b6f3a87d-b148-4636-a634-58bdeefe240f"><ac:parameter ac:name="id">1399451350</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="68950fcb-d111-429f-b9cc-be2861d26509"><ac:parameter ac:name="id">1399451349</ac:parameter><ac:rich-text-body><p>The Enterprise Architect Import (EA) plugin will automatically load when you start MagicDraw. You can use it to import UML 2.1 XMI 2.1 to your modeling tool. </p><p><ac:image><ri:attachment ri:filename="Import EAfiles.png"><ri:page ri:content-title="Working with Enterprise Architect Import Plugin" ri:space-key="EAI2024xR2" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0bc21967-4503-4a0f-a020-155d9cc403af"><ac:parameter ac:name="id">1399451338</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d14b0f06-6d05-4659-96fd-cbddaa6e0618" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````
