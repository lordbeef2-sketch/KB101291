# NOMAGIC DOCUMENTATION SPACE: Magic Real-Time Communication Designer 2024x Refresh2

<!--NOMAGIC_SPACE key=MRTCD2024xR2 chunk=1 -->

<!--NOMAGIC_PAGE id=191936044 space=MRTCD2024xR2 version=1 -->
## PAGE 00001: Applying DDS Sterotypes

- page_id: `191936044`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936044/Applying+DDS+Sterotypes
- version_number: 1
- version_date: `2023-09-22T14:02:24.982+02:00`
- ancestors: Magic Real-Time Communication Designer > Home Control Example
- labels: []

### NORMALIZED CONTENT

First and for most we need do define the data structures and the topics which will be used in the communication. This can easily be done with a Topic Definition diagram. [CONFLUENCE_PAGE title='Defining topics and types' space='MRTCD2024xR2']>]]>

Topics must contain exactly one property that has to be stereotyped with the TopicTypeProperty stereotype and has to be a type of either a Struct or Union.

[IMAGE alt='' src='']

###### The example defines three packages or DDS Modules for the three factor that we would like to measure and control.

Now that we have the data structures for the communication we can assign them to ports turning them into data writers and data readers in the DDS sense. [CONFLUENCE_PAGE title='Defining Domain Participant communication' space='MRTCD2024xR2']>]]>

First we need to apply the DomainParticipant stereotypes on Blocks whose instances will be used as the individual applications in the communication. [CONFLUENCE_PAGE title='Defining Domains and Domain Participants' space='MRTCD2024xR2']>]]>

[IMAGE alt='' src='']

###### The SysML BLock Definition diagram that contains all Domain Participants of Home Controller system.

After SysML model is created with the right stereotypes applied, we can define our DDS domains with them.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">First and for most we need do define the data structures and the topics which will be used in the communication. This can easily be done with a Topic Definition diagram. <ac:link><ri:page ri:content-title="Defining topics and types" ri:space-key="MRTCD2024xR2" /><ac:plain-text-link-body><![CDATA[How to define topics and types >>]]></ac:plain-text-link-body></ac:link></p><p>Topics must contain exactly one property that has to be stereotyped with the TopicTypeProperty stereotype and has to be a type of either a Struct or Union.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="topic_Definition_diagram_homeControlerSystem.png"><ri:page ri:content-title="Applying DDS Sterotypes" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example defines three packages or DDS Modules for the three factor that we would like to measure and control.</h6><p><br /></p><p>Now that we have the data structures for the communication we can assign them to ports turning them into data writers and data readers in the DDS sense. <ac:link><ri:page ri:content-title="Defining Domain Participant communication" ri:space-key="MRTCD2024xR2" /><ac:plain-text-link-body><![CDATA[How to define Domain Participant communication >>]]></ac:plain-text-link-body></ac:link></p><p>First we need to apply the DomainParticipant stereotypes on Blocks whose instances will be used as the individual applications in the communication. <ac:link><ri:page ri:content-title="Defining Domains and Domain Participants" ri:space-key="MRTCD2024xR2" /><ac:plain-text-link-body><![CDATA[How to define Domains and Domain Participants >>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center"><ri:attachment ri:filename="bdd_homeControlerSystem.png"><ri:page ri:content-title="Applying DDS Sterotypes" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The SysML BLock Definition diagram that contains all Domain Participants of Home Controller system.</h6><p><br /></p><p>After  SysML model is created with the right stereotypes applied, we can define our DDS domains with them.</p>
````

<!--NOMAGIC_PAGE id=191935995 space=MRTCD2024xR2 version=1 -->
## PAGE 00002: Creating DDS project

- page_id: `191935995`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191935995/Creating+DDS+project
- version_number: 1
- version_date: `2023-09-22T14:02:23.875+02:00`
- ancestors: Magic Real-Time Communication Designer > Getting started
- labels: ['create-dds-project', 'new-dds-project', 'blank-dds-project']

### NORMALIZED CONTENT

To create a blank DDS project

1. Do one of the following:
  - Select **File**> **New** **Project**.
  - On the main toolbar, click the **New** **Project** button.
  - Press Ctr+Shiftl+N.
2. In the **New** **Project** dialog, under **Systems Engineering**, select **DDS** **Project**.
3. Specify name and location.
4. Click **OK** when you are done. 
The blank project is created and stored in your file system with defined name. 
 [IMAGE alt='' src='']

Once you created the blank DDS Project, you can use for modeling already predefined Package structure as shown in the following figure.

###### [IMAGE alt='' src=''] 
 The predefined Package structure of blank DDS project.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To create a blank DDS project</p><hr /><ol><li><span style="color: rgb(51,51,51);">Do one of the following:<br /> </span><ul><li><span style="color: rgb(51,51,51);">Select <strong>File </strong>&gt; <strong>New</strong> <strong>Project</strong>.</span></li><li><span style="color: rgb(51,51,51);">On the main toolbar, click the <strong>New</strong> <strong>Project</strong> button.</span></li><li><span style="color: rgb(51,51,51);">Press Ctr+Shiftl+N.</span> <span style="color: rgb(51,51,51);"> <br /> </span></li></ul></li><li class="_mce_tagged_br"><span style="color: rgb(51,51,51);">In the <strong>New</strong> <strong> Project</strong> dialog, under <strong>Systems Engineering</strong>, select <strong>DDS</strong> <strong> Project</strong>.<br /> </span></li><li><span style="color: rgb(51,51,51);">Specify name and location.</span></li><li><span style="color: rgb(51,51,51);">Click <strong>OK</strong> when you are done.<br />The blank project is created and stored in your file system with defined name.<br /> <ac:image><ri:attachment ri:filename="create_new_DDS_project_steps.png"><ri:page ri:content-title="Creating DDS project" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image> </span></li></ol><p><span style="color: rgb(51,51,51);"> <br /> </span></p><p><span style="color: rgb(51,51,51);">Once you created the blank DDS Project, you can use for modeling already predefined Package structure as shown in the following figure.</span></p><h6 style="text-align: center;"><span style="color: rgb(51,51,51);"> <ac:image ac:align="center"><ri:attachment ri:filename="predefined_DDS_package_structure.png"><ri:page ri:content-title="Creating DDS project" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image> </span> <br /> <span>The predefined Package structure of blank DDS project.</span></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=191936047 space=MRTCD2024xR2 version=2 -->
## PAGE 00003: Creating the domain

- page_id: `191936047`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936047/Creating+the+domain
- version_number: 2
- version_date: `2024-10-08T09:29:18.976+02:00`
- ancestors: Magic Real-Time Communication Designer > Home Control Example
- labels: []

### NORMALIZED CONTENT

The Domain can be created by using the DDS Domain Table. As shown in the following table, the Smart Home DDS Domain is created with specified its id, topics, participants and participant instances. [How to create DDS Domain Table>>](https://docs.nomagic.com/display/DRCP2024xR2/Defining+Domains+and+Domain+Participants#DefiningDomainsandDomainParticipants-CreatingDomainandDomainParticipantsbyusingtheDDSDomainTable)

[IMAGE alt='' src='']

###### The example of DDS Domain Table.

The Participant Instances derived column displays all the instances that will be in the the DDS XML.Now we are ready to export the model if we desire, but first we need to assign quality of service requirements on the DDS elements.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Domain can be created by using the <span style="color: rgb(62,63,64);">DDS Domain Table. As shown in the following table, the Smart Home DDS Domain is created with specified its id, topics, participants and participant instances. <a href="https://docs.nomagic.com/display/DRCP2024xR2/Defining+Domains+and+Domain+Participants#DefiningDomainsandDomainParticipants-CreatingDomainandDomainParticipantsbyusingtheDDSDomainTable">How to create DDS Domain Table&gt;&gt;</a></span></p><p><span style="color: rgb(62,63,64);"><ac:image ac:align="center"><ri:attachment ri:filename="domain_table.png"><ri:page ri:content-title="Creating the domain" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">The example of DDS Domain Table.</span></h6><p class="auto-cursor-target"><span><span><span style="color: rgb(62,63,64);">The Participant Instances derived column displays all the instances that will be in the the DDS XML. </span>Now we are ready to export the model if we desire, but first we need to assign quality of service requirements on the DDS elements.</span><br /></span></p><p class="auto-cursor-target"><span><br /></span></p><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=191936014 space=MRTCD2024xR2 version=1 -->
## PAGE 00004: Defining Domain Participant communication

- page_id: `191936014`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936014/Defining+Domain+Participant+communication
- version_number: 1
- version_date: `2023-09-22T14:02:24.207+02:00`
- ancestors: Magic Real-Time Communication Designer > Getting started
- labels: ['dds-endpoint-stereotype', 'domain-participant-communication']

### NORMALIZED CONTENT

Communication between DDS elements is determined by ports owned by Domain Participants. Ports that are parts of the communication has to have DDS Endpoint stereotype otherwise they will be omitted.

To apply DDS Endpoint stereotype on a port

1. Right-click the port and from the shortcut menu, select Stereotype.
2. In the opened dialog, select DDS Endpoint.
3. Click Apply .

The derived direction of ports determine whether they are considered Data Reader or Data Writers. In case of non-nested ports the publishers and subscribers which contain the Data Readers or Writers are implicitly defined under the Domain Participants. Publishers and Subscribers in DDS group Data Readers and Writers.

Nested ports can be used to group Data Writers and Readers. The grouping is determined by the ports highest in the hierarchy (direct children of the Block). Note that non-nested ports must have a type of Topic.

In between ports have no effective meaning.

In case ofnested ports, ports highest in the hierarchy implicitly definesubscribersandpublishersas well.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Communication between DDS elements is determined by ports owned by Domain Participants. Ports that are parts of the communication has to have DDS Endpoint stereotype otherwise they will be omitted.</p><p><br /></p><p>To apply DDS Endpoint stereotype on a port</p><hr /><ol><li>Right-click the port and from the shortcut menu, select Stereotype.</li><li>In the opened dialog, select DDS Endpoint. </li><li>Click <strong>Apply</strong>.</li></ol><p><br /></p><p>The derived direction of ports determine whether they are considered Data Reader or Data Writers. In case of non-nested ports the publishers and subscribers which contain the Data Readers or Writers are implicitly defined under the Domain Participants. Publishers and Subscribers in DDS group Data Readers and Writers.</p><p>Nested ports can be used to group Data Writers and Readers. The grouping is determined by the ports highest in the hierarchy (direct children of the Block). Note that non-nested ports must have a type of Topic.</p><p><span>In between ports have no effective meaning.</span></p><p><span>In case of </span>nested ports<span>, ports highest in the hierarchy implicitly define </span>subscribers<span> and </span>publishers<span> as well.</span></p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="image2020-11-12_14-1-30.png"><ri:page ri:content-title="Defining Domain Participant communication" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></p><p><span><br /></span></p><p><br /></p><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=191936006 space=MRTCD2024xR2 version=2 -->
## PAGE 00005: Defining Domains and Domain Participants

- page_id: `191936006`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936006/Defining+Domains+and+Domain+Participants
- version_number: 2
- version_date: `2024-10-08T09:29:18.572+02:00`
- ancestors: Magic Real-Time Communication Designer > Getting started
- labels: ['create-domain-participant', 'create-domain', 'define-instances', 'create-dds-domain-table', 'dds-domain-table']

### NORMALIZED CONTENT

All Domain Participants are assigned to the Domain regardless of where they are in the containment hierarchy. Domain Participants should have at least one instance which can be any kind of lock property typed by Domain Participant. During DDS XML generation, all properties of the Block are considered a Domain Participants.

You can create Domain and Domain Participants by using:

- The Containment tree.
- DDS Domain Table.

This page contains the following topics:

4

##### Creating Domain and Domain Participants by using the Containment tree

To create a Domain Participant or Domain in the Containment tree

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MD2024xR2'] , right-click a Package wherein you want to create Domain Participants or Domain.
2. From the shortcut menu, select Create Element and from the opened dialog, select DomainParticipant or Domain.
3. The unnamed element is created. Type its name and press enter. [ATTACHMENT filename='domain_participant_and_domain_in_containment_tree.png']

##### Creating Domain and Domain Participants by using the DDS Domain Table

You can use the DDS Domain Table to create a Domain inside a Domain Library. It also helps to assign Topics and Domain Participants to the Domain. The DDS Domain Table named Domain is already created in predefined DDS Package structure. If you want to create a new one, follow the procedure below.

To create an empty DDS Domain Table

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MD2024xR2'] , right-click a predefined Domain Package.
2. From the shortcut menu, select Create Diagram and from the opened dialog, select DDS Domain Table.
3. The unnamed table is created. Type its name and press enter.

To fill in the DDS Domain Table

1. From the table toolbar, click the Add New button. The new row appears and DDSDomain element is created in the model.
2. In the table, specify the following: 
 - Double-click **Name** cell and type a domain name. 
 - Double-click the **Domain_id** cell and type domain id number. 
 - Double-click the **Topics** cell, select [IMAGE alt='' src=''] and in the **Select Elements** dialog choose already created topics or use the **Creation Mode** to create new topics. Topics referenced by a Domain Participants must be assigned to every Domain that the participant is assigned to. Unassigned Topics lead to validation errors. - Double-click the **Participants** cell, select [IMAGE alt='' src=''] and in the **Select Elements** dialog choose already created Domain Participants or use the **Creation Mode** to create new Domain Participants. 
 - The **Participant Instances** column fill in automatically when instances are created in the model. >]]>[CONFLUENCE_PAGE title='Defining Domains and Domain Participants' space='MRTCD2024xR2'] 
[IMAGE alt='' src='']

##### Creating Domain Participants by refactoring the Block

To create a Domain Participant or Domain by refactoring a Block

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MD2024xR2'] , right-click a Package wherein you want to create Domain Participants or Domain.
2. From the shortcut menu, select Create Element and from the opened dialog, select Block.
3. Right-click the Block and select Refactor > Convert To > More Specific > Domain Participant or Domain . The Block is refactored to the Domain Participant or Domain.

[IMAGE alt='' src='']

##### Creating instances

The difference between instances of Domain Participants and Members of DDS Data types are the following:

- Domain Participant instances: are any Block property typed by Domain Participant. They can be any kid of property: Value Property, Part Property, Reference Property etc. 
 - Members: DDS Data type Members are used in the data definition section of the meta-model. They allow to define custom, DDS annotated data types. They rely heavily on multiplicity definitions in order to be able to produce a syntactically correct DDS xml output.

To create a Domain Participant instances

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MD2024xR2'] , right-click a Block which will be the owner of the instances.
2. From the shortcut menu, select Create Diagram and from the opened dialog, select SysML Internal Block Diagram.
3. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MD2024xR2'] select a property (e.g. Part Property) and click on the diagram pane.
4. Type the name of the property.
5. Select a Domain Participant as type of the property. The instance of Domain Participant is created. [ATTACHMENT filename='instances_of_domain_participants.png']

##### Defining instances multiplicity

To define a instances as an array or sequence, its multiplicity needs to be changed as it follows, where N must be at least 1 and M must be greater than N.

| Lower Value | Upper Value | Multiplicity | Type |
| --- | --- | --- | --- |
| N | N | N | Array |
| 0 | -1 | 0 .. * | Boundless Array |
| 0 | N-1 | 0 .. N-1 | Sequence |
| N | M | N .. M | Sequence |

To change the instance multiplicity

1. Double-click the Part Property to open it's [CONFLUENCE_PAGE title='Specification window' space='MD2024xR2'] .
2. Select the Multiplicity property value or type Lower Value and Upper Value.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>All Domain Participants are assigned to the Domain regardless of where they are in the containment hierarchy. Domain Participants should have at least one instance which can be any kind of lock property typed by Domain Participant. During DDS XML generation, all properties of the Block are considered a Domain Participants.</p><p>You can create Domain and Domain Participants by using:</p><ul><li>The Containment tree.</li><li>DDS Domain Table.</li></ul><p>This page contains the following topics:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="e20bb792-47ca-49f9-8f77-b9d92eb13d0b"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p><div><p><br /></p><h3>Creating Domain and Domain Participants by using the Containment tree</h3><p><br /></p><p>To create a Domain Participant or Domain in the Containment tree</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a Package wherein you want to create Domain Participants or Domain.</li><li>From the shortcut menu, select <strong>Create Element </strong>and from the opened dialog, select DomainParticipant or Domain.</li><li>The unnamed element is created. Type its name and press enter.<br /><ac:image><ri:attachment ri:filename="domain_participant_and_domain_in_containment_tree.png"><ri:page ri:content-title="Defining Domains and Domain Participants" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></li></ol><h3>Creating Domain and Domain Participants by using the DDS Domain Table</h3><p>You can use the DDS Domain Table to create a Domain inside a Domain Library. It also helps to assign Topics and Domain Participants to the Domain. The DDS Domain Table named Domain is already created in predefined DDS Package structure. If you want to create a new one, follow the procedure below.</p><p>To create an empty DDS Domain Table</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a predefined <em>Domain</em> Package.</li><li>From the shortcut menu, select <strong>Create Diagram </strong>and from the opened dialog, select DDS Domain Table.</li><li>The unnamed table is created. Type its name and press enter.</li></ol><p><br /></p><p>To fill in the DDS Domain Table</p><hr /><ol><li>From the table toolbar, click the <strong>Add New</strong> button. The new row appears and DDSDomain element is created in the model.</li><li><p class="auto-cursor-target">In the table, specify the following:<br /> - Double-click <strong>Name</strong> cell and type a domain name.<br /> - Double-click the <strong>Domain_id</strong> cell and type domain id number.<br /> - Double-click the <strong>Topics</strong> cell, select <ac:image ac:title="Edit" ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="Defining Domains and Domain Participants" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image> and in the <strong>Select Elements</strong> dialog choose already created topics or use the <strong>Creation Mode</strong> to create new topics.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="ccea59d8-2dd6-47db-a1e2-75bba1a8ff67"><ac:rich-text-body><p>Topics referenced by a Domain Participants must be assigned to every Domain that the participant is assigned to. Unassigned Topics lead to validation errors.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"> - Double-click the <strong>Participants</strong> cell, select <ac:image ac:title="Edit" ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="Defining Domains and Domain Participants" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image> and in the <strong>Select Elements</strong> dialog choose already created Domain Participants or use the <strong>Creation Mode</strong> to create new Domain Participants.<br /> - The <strong>Participant Instances</strong> column fill in automatically when instances are created in the model. <ac:link ac:anchor="Creating instances of Domain Participants"><ac:plain-text-link-body><![CDATA[How to create Participant Instances >>]]></ac:plain-text-link-body><ri:page ri:content-title="Defining Domains and Domain Participants" ri:space-key="MRTCD2024xR2" /></ac:link><br /><ac:image><ri:attachment ri:filename="DDSDomain_table.png"><ri:page ri:content-title="Defining Domains and Domain Participants" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></p></li></ol><h3>Creating Domain Participants by refactoring the Block</h3><p><br /></p><p>To create a Domain Participant or Domain by refactoring a Block</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a Package wherein you want to create Domain Participants or Domain.</li><li>From the shortcut menu, select <strong>Create Element </strong>and from the opened dialog, select Block.</li><li>Right-click the Block and select <strong>Refactor</strong> &gt; <strong>Convert To</strong> &gt; <strong>More Specific</strong> &gt; <strong>Domain Participant</strong> or <strong>Domain</strong>.<br />The Block is refactored to the Domain Participant or Domain.</li></ol><p><ac:image><ri:attachment ri:filename="Block_refactor_to_domain_participant.png"><ri:page ri:content-title="Defining Domains and Domain Participants" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></p><h3>Creating instances </h3><p>The difference between instances of Domain Participants and Members of DDS Data types are the following:</p><p>   - Domain Participant instances: are any Block property typed by Domain Participant. They can be any kid of property: Value Property, Part Property, Reference Property etc.<br />    - Members: DDS Data type Members are used in the data definition section of the meta-model. They allow to define custom, DDS annotated data types. They rely heavily on multiplicity definitions in order to be able to produce a syntactically correct DDS xml output.<br /><br /></p><p>To create a Domain Participant instances</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a Block which will be the owner of the instances.</li><li>From the shortcut menu, select <strong>Create Diagram </strong>and from the opened dialog, select SysML Internal Block Diagram.</li><li>From the <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram palette]]></ac:plain-text-link-body></ac:link> select a property (e.g. Part Property) and click on the diagram pane.</li><li>Type the name of the property.</li><li>Select a Domain Participant as type of the property.<br />The instance of Domain Participant is created.<br /><br /><ac:image><ri:attachment ri:filename="instances_of_domain_participants.png"><ri:page ri:content-title="Defining Domains and Domain Participants" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></li></ol><h3>Defining instances multiplicity</h3></div><p>To define a instances as an array or sequence, its multiplicity needs to be changed as it follows, where N must be at least 1 and M must be greater than N.</p><table><colgroup><col /><col /><col /><col /><col /></colgroup><tbody><tr><td colspan="2"><p class="Compact"><strong>Lower Value</strong></p></td><td><p class="Compact"><strong>Upper Value</strong></p></td><td><p class="Compact"><strong>Multiplicity</strong></p></td><td><p class="Compact"><strong>Type</strong></p></td></tr><tr><td colspan="2"><p>N</p></td><td><p>N</p></td><td><p>N</p></td><td><p>Array</p></td></tr><tr><td colspan="2"><p>0</p></td><td><p>-1</p></td><td><p>0 .. *</p></td><td><p>Boundless Array</p></td></tr><tr><td colspan="2"><p>0</p></td><td><p>N-1</p></td><td><p>0 .. N-1</p></td><td><p>Sequence</p></td></tr><tr><td colspan="2"><p>N</p></td><td><p>M</p></td><td><p>N .. M</p></td><td><p>Sequence</p></td></tr></tbody></table><p><br /></p><p>To change the instance multiplicity</p><hr /><ol><li>Double-click the Part Property to open it's <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Specification window" /></ac:link>.</li><li>Select the Multiplicity property value or type Lower Value and Upper Value.</li></ol><p><ac:image><ri:attachment ri:filename="members_multiplicity.png"><ri:page ri:content-title="Defining Domains and Domain Participants" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></p><p class="Compact"><br /></p>
````

<!--NOMAGIC_PAGE id=191936002 space=MRTCD2024xR2 version=2 -->
## PAGE 00006: Defining topics and types

- page_id: `191936002`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936002/Defining+topics+and+types
- version_number: 2
- version_date: `2024-10-08T09:29:18.494+02:00`
- ancestors: Magic Real-Time Communication Designer > Getting started
- labels: ['define-topics', 'define-types', 'create-dds-topic-definition-diagram']

### NORMALIZED CONTENT

You can define topic and types used by them in the DDS Topic Definition Diagram.

[IMAGE alt='' src='']

###### The example of the DDS Topic Definition Diagram where main elements are highlighed: DDS Module, Types and Topic.

##### Creating DDS Topic Definition Diagram

After a blank DDS Project is created, the predefined package structure is prepared where the DDS Topic Definition Diagram is already created under the *Topics* Package named *Topics*. It contains an empty DDS Module. If you need another one, create it manually, as described in the following procedure.

To create blank DDS Topic Definition Diagram

1. In the [CONFLUENCE_PAGE title='Model Browser' space='MD2024xR2'] , select the owner for the new diagram.
2. Do one of the following:
  - Right-click the Package, and from the shortcut menu select Create Diagram.
  - Press Ctrl+N.
  - On the main toolbar, click [IMAGE alt='' src=''] .
  - From the main menu, select Diagrams > Create Diagram .
3. In the **Create Diagram** box, under **General** diagram group, select the **DDS Topic Definition Diagram**.

Press Esc or click outside the dialog to close the diagram creation dialog without creating the diagram.

##### Defining topics and types

You can create the following types:

- Struct Type
- Union Type
- Bitmask Type
- Enumeration Type
- Map Type
- Alias Type
- Annotation Type

Creating and defining types

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MD2024xR2'] , select a type you need and click on DDS Module element.
2. Type its name.
3. Click the Create Member [CONFLUENCE_PAGE title='Smart manipulators' space='MD2024xR2'] to create a Members for the type.
4. Select newly created Member on the shape, click [ATTACHMENT filename='specify_type.png'] and select a type for a it.

Creating and defining topics

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MD2024xR2'] , select a Topic and click on the [CONFLUENCE_PAGE title='Understanding the user interface' space='MD2024xR2'] .
2. Type its name.
3. Click the Create Element [CONFLUENCE_PAGE title='Smart manipulators' space='MD2024xR2'] to create a Topic Type Property or Reception for the Topic.
4. Select newly created Topic Type Property or Reception, click [IMAGE alt='' src='']and select a type for a it. Press Ctrl+Space to search among the available types.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can define topic and types <span style="color: rgb(62,63,64);">used by them</span> in the DDS Topic Definition Diagram.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="DDS_Topic_Definition_Diagram.png"><ri:page ri:content-title="Defining topics and types" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example of the DDS Topic Definition Diagram where main elements are highlighed: DDS Module, Types and Topic.</h6><h3>Creating DDS Topic Definition Diagram</h3><p>After a blank DDS Project is created, the predefined package structure is prepared where the DDS Topic Definition Diagram is already created under the <em>Topics</em> Package named <em>Topics</em>. It contains an empty DDS Module. If you need another one, create it manually, as described in the following procedure.</p><p>To create blank DDS Topic Definition Diagram</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Model Browser" /></ac:link>, select the owner for the new diagram.</li><li>Do one of the following:<br /><ul><li>Right-click the Package, and from the shortcut menu select <strong>Create Diagram.</strong></li><li>Press Ctrl+N.</li><li>On the main toolbar, click <span class="confluence-embedded-file-wrapper"><ac:image ac:alt="Create Diagram"><ri:attachment ri:filename="create_diagram.png"><ri:page ri:content-title="Defining topics and types" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></span> .</li><li>From the main menu, select <strong>Diagrams</strong> &gt; <strong>Create Diagram</strong>.</li></ul></li><li><p>In the <strong>Create Diagram</strong> box, under <strong>General</strong> diagram group, select the <strong>DDS Topic Definition Diagram</strong>.</p></li></ol><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="8fa80951-960a-4327-aedd-357ca62fe7c8"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">Press Esc or click outside the dialog to close the diagram creation dialog without creating the diagram.</span></p></ac:rich-text-body></ac:structured-macro><h3>Defining topics and types</h3><p>You can create the following types:</p><ul><li>Struct Type</li><li>Union Type</li><li>Bitmask Type</li><li>Enumeration Type</li><li>Map Type</li><li>Alias Type</li><li>Annotation Type</li></ul><p><br /></p><p>Creating and defining types</p><hr /><ol><li>From the<ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[ diagram palette]]></ac:plain-text-link-body></ac:link>, select a type you need and click on DDS Module element. </li><li>Type its name.</li><li>Click the <strong>Create Member</strong> <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Smart manipulators" /><ac:plain-text-link-body><![CDATA[smart manipulator]]></ac:plain-text-link-body></ac:link> to create a Members for the type.</li><li>Select newly created Member on the shape, click <ac:image ac:title="Specify Type" ac:alt="Specify Type"><ri:attachment ri:filename="specify_type.png"><ri:page ri:content-title="Defining topics and types" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image> and select a type for a it.</li></ol><p><br /></p><p>Creating and defining topics</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram palette]]></ac:plain-text-link-body></ac:link>, select a Topic and click on the <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram pane]]></ac:plain-text-link-body></ac:link>. </li><li>Type its name.</li><li>Click the <strong>Create Element</strong> <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Smart manipulators" /><ac:plain-text-link-body><![CDATA[smart manipulator]]></ac:plain-text-link-body></ac:link> to create a Topic Type Property or Reception for the Topic.</li><li><p class="auto-cursor-target">Select newly created Topic Type Property or Reception, click <ac:image ac:title="Specify Type" ac:alt="Specify Type"><ri:attachment ri:filename="specify_type.png"><ri:page ri:content-title="Defining topics and types" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image>and select a type for a it.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="f4ba630b-5037-4766-aa0d-f65b82385bbb"><ac:rich-text-body><p>Press Ctrl+Space to search among the available types.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><br /></p><p class="Compact">              </p><p class="Compact"><br /></p>
````

<!--NOMAGIC_PAGE id=191936053 space=MRTCD2024xR2 version=1 -->
## PAGE 00007: Domain not in Library

- page_id: `191936053`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936053/Domain+not+in+Library
- version_number: 1
- version_date: `2023-09-22T14:02:25.290+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: warning

**Implementation**: com.nomagic.magicdraw.dds.validation.DomainNotInLibraryRule

**Qualified name**: DDS::Validation::DDS_Domain_Not_In_Library

**Description:**A Domain should be directly contained in a Domain Library, otherwise it cannot be exported into DDS XML. A Domain Library is a stereotyped Package.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: warning</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.DomainNotInLibraryRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Domain_Not_In_Library</p><p><strong>Description: </strong>A Domain should be directly contained in a Domain Library, otherwise it cannot be exported into DDS XML. A Domain Library is a stereotyped Package.</p>
````

<!--NOMAGIC_PAGE id=191936054 space=MRTCD2024xR2 version=1 -->
## PAGE 00008: Domain Participant without Instance

- page_id: `191936054`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936054/Domain+Participant+without+Instance
- version_number: 1
- version_date: `2023-09-22T14:02:25.354+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: warning

**Implementation**: com.nomagic.magicdraw.dds.validation.DomainParticipantsWithoutInstancesRule

**Qualified name**: DDS::Validation::DDS_Domain_Participants_Without_Instance

**Abbreviation**: DOMAN_PARTICIPANT_NO_INST

**Description**: Here *instance* refers to properties on other Blocks.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: warning</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.DomainParticipantsWithoutInstancesRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Domain_Participants_Without_Instance</p><p class="FirstParagraph"><strong>Abbreviation</strong>: DOMAN_PARTICIPANT_NO_INST</p><p><strong>Description</strong>: Here <em>instance</em> refers to properties on other Blocks.</p>
````

<!--NOMAGIC_PAGE id=191936055 space=MRTCD2024xR2 version=1 -->
## PAGE 00009: Duplicate Domain ID

- page_id: `191936055`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936055/Duplicate+Domain+ID
- version_number: 1
- version_date: `2023-09-22T14:02:25.423+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: warning

**Implementation**: com.nomagic.magicdraw.dds.validation.NonUniqueDDSDomainIDRule

**Qualified name**: DDS::Validation::DDS_Duplicate_Domain_ID

**Description**: Each Domain ID should be unique. If backwards compatibility is not an issue, you can try reordering. The button is hidden by the Detailed toggle in the Element Numbering window that can be opened by clicking on the … button when the ID field of a Domain is selected.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: warning</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.NonUniqueDDSDomainIDRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Duplicate_Domain_ID</p><p><strong>Description</strong>: Each Domain ID should be unique. If backwards compatibility is not an issue, you can try reordering. The button is hidden by the Detailed toggle in the Element Numbering window that can be opened by clicking on the … button when the ID field of a Domain is selected.</p>
````

<!--NOMAGIC_PAGE id=191936056 space=MRTCD2024xR2 version=1 -->
## PAGE 00010: Endpoint not Referenced

- page_id: `191936056`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936056/Endpoint+not+Referenced
- version_number: 1
- version_date: `2023-09-22T14:02:25.493+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.qos.QoSEndpointNotReferencedRule

**Qualified name**: DDS::Validation::QoS Validation Suite::QoS_Endpoint_Not_Referenced

**Abbreviation**: ENDPOINT_NOT_REFERENCED

**Description**: Data Port QoS assignments must reference the definitions of their assigned instances. Use a Data Port Qos Assignment Table to manage these elements.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.qos.QoSEndpointNotReferencedRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::QoS Validation Suite::QoS_Endpoint_Not_Referenced</p><p class="FirstParagraph"><strong>Abbreviation</strong>: ENDPOINT_NOT_REFERENCED</p><p><strong>Description</strong>: Data Port QoS assignments must reference the definitions of their assigned instances. Use a Data Port Qos Assignment Table to manage these elements.</p>
````

<!--NOMAGIC_PAGE id=191936036 space=MRTCD2024xR2 version=1 -->
## PAGE 00011: Environment setup

- page_id: `191936036`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936036/Environment+setup
- version_number: 1
- version_date: `2023-09-22T14:02:24.715+02:00`
- ancestors: Magic Real-Time Communication Designer > Simulation with Simulink
- labels: []

### NORMALIZED CONTENT

The Connext DDS for modeling tool ships with a pre-setup matlab workspace under the name of matlab_vs. Perform the following steps every time after starting Matlab:

- Change directory to the matlab_vs subdirectory
- Run InitializeEnvironment

Running the script should only be done once per session otherwise it results in errors.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">The Connext DDS for modeling tool ships with a pre-setup matlab workspace under the name of matlab_vs. Perform the following steps every time after starting Matlab:</p><ul><li>Change directory to the matlab_vs subdirectory</li><li>Run InitializeEnvironment</li></ul><p class="FirstParagraph">Running the script should only be done once per session otherwise it results in errors.</p>
````

<!--NOMAGIC_PAGE id=191936042 space=MRTCD2024xR2 version=1 -->
## PAGE 00012: Example Model

- page_id: `191936042`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936042/Example+Model
- version_number: 1
- version_date: `2023-09-22T14:02:24.927+02:00`
- ancestors: Magic Real-Time Communication Designer > Home Control Example
- labels: []

### NORMALIZED CONTENT

HomeControler.mdzip contains a model that describes a system that consists of an air conditioner unit, a dehumidifiers, shutters and a light sensor. The air conditioner and the dehumidifier both contain a controller and a sensor component. The system is supervised by the Home Controller whose main responsibility is to monitor data received from the components and to control them.

[IMAGE alt='' src='']

###### The SysmL Internal Block Diagram of Home Controller environment.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">HomeControler.mdzip contains a model that describes a system that consists of an air conditioner unit, a dehumidifiers, shutters and a light sensor. The air conditioner and the dehumidifier both contain a controller and a sensor component. The system is supervised by the Home Controller whose main responsibility is to monitor data received from the components and to control them.</p><p class="FirstParagraph"><ac:image ac:align="center"><ri:attachment ri:filename="ibd_homeControlerSystem.png"><ri:page ri:content-title="Example Model" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></p><h6 class="FirstParagraph" style="text-align: center;">The SysmL Internal Block Diagram of Home Controller environment.</h6>
````

<!--NOMAGIC_PAGE id=191936051 space=MRTCD2024xR2 version=2 -->
## PAGE 00013: Exporting DDS Control Example to XML

- page_id: `191936051`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936051/Exporting+DDS+Control+Example+to+XML
- version_number: 2
- version_date: `2024-10-08T09:29:19.032+02:00`
- ancestors: Magic Real-Time Communication Designer > Home Control Example
- labels: []

### NORMALIZED CONTENT

You can export the DDS examples to XML. For this, follow the procedures provided in the page [Exporting DDS XML](https://docs.nomagic.com/display/DRCP2024xR2/Exporting+DDS+XML).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can export the DDS examples to XML. For this, follow the procedures provided in the page <a class="current" style="letter-spacing: 0.0px;" href="https://docs.nomagic.com/display/DRCP2024xR2/Exporting+DDS+XML">Exporting DDS XML</a>.</p><p><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=191936022 space=MRTCD2024xR2 version=2 -->
## PAGE 00014: Exporting DDS XML

- page_id: `191936022`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936022/Exporting+DDS+XML
- version_number: 2
- version_date: `2024-10-08T09:29:18.742+02:00`
- ancestors: Magic Real-Time Communication Designer > Getting started
- labels: ['generate-dds-xml']

### NORMALIZED CONTENT

You can generate DDS xml file directly from the modeling tool. Referenced QoS profiles are included in the resulting XML. Before the export a pre-check is initiated to ensure that the QoS Profiles imported to modeling tool were not changed and still up to date. You can use the resulting XML in the **RTI DDS Code Generator**, **RTI System Designer**, the **DDS Simulink Tooling** or other standards-compliant tool.

To generate DDS XML

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MD2024xR2'] , select Tools > DDS > Generate DDS XML .
2. In the Generate DDS XML dialog, select the following:

-**Select Scope** - select a Package which content you want to export. Click **Next**.

To ensure that the exported XML is valid, make sure the selected package contains at least one domain participant library containing at least one Domain Participant. Otherwise, the tool takes care of the validity of references by including the elements referred from the selected package even if they are outside the selected Package.

[IMAGE alt='' src='']

- **Select target version** - select DDS target version. Click **Next**.

QoS Profiles between versions are not compatible. QoS Profiles with a version that is not matching with the target version selected it the wizard will prevent the export.

[IMAGE alt='' src=''] 
 - **Select output directory** - select the location of exported DDS XML file. Click **Finish**. 
 
[IMAGE alt='' src=''] 
The DDS XML file is generated.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can generate DDS xml file directly from the modeling tool. Referenced QoS profiles are included in the resulting XML. Before the export a pre-check is initiated to ensure that the QoS Profiles imported to modeling tool were not changed and still up to date. You can use the resulting XML in the <strong style="letter-spacing: 0.0px;">RTI DDS Code Generator</strong>, <strong style="letter-spacing: 0.0px;">RTI System Designer</strong>, the <strong style="letter-spacing: 0.0px;">DDS Simulink Tooling</strong> or other standards-compliant tool.</p><p><br /></p><p>To generate DDS XML</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main menu]]></ac:plain-text-link-body></ac:link>, select <strong>Tools </strong>&gt; <strong>DDS</strong> &gt; <strong>Generate DDS XML</strong>.</li><li>In the <strong style="letter-spacing: 0.0px;">Generate DDS XML</strong><span style="letter-spacing: 0.0px;"> dialog, select the following:</span><span style="letter-spacing: 0.0px;"><br /></span></li></ol><p class="auto-cursor-target"> -<strong> Select Scope</strong> - select a Package which content you want to export. Click <strong>Next</strong>.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="72fbaaef-7a44-4b88-9f40-a83af6e3bbaa"><ac:rich-text-body><p><span>To ensure that the exported XML is valid, make sure the selected package contains at least one domain participant library containing at least one Domain Participant. Otherwise, the tool takes care of the validity of references by including the elements referred from the selected package even if they are outside the selected Package.</span></p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="select_scope.png"><ri:page ri:content-title="Exporting DDS XML" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></p><p class="auto-cursor-target"> - <strong>Select target version</strong> - select DDS target version. Click <strong>Next</strong>.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="75827afe-6c50-4001-a769-860dc4e01ba3"><ac:rich-text-body><p>QoS Profiles between versions are not compatible. QoS Profiles with a version that is not matching with the target version selected it the wizard will prevent the export.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="select_target_version.png"><ri:page ri:content-title="Exporting DDS XML" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image><br /> - <strong>Select output directory</strong> - select the location of exported DDS XML file. Click <strong>Finish</strong>.<br /><br /><ac:image><ri:attachment ri:filename="select_output_directory.png"><ri:page ri:content-title="Exporting DDS XML" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image><br />The DDS XML file is generated.</p><p><br /><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=191936037 space=MRTCD2024xR2 version=1 -->
## PAGE 00015: Generating the Simulink model

- page_id: `191936037`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936037/Generating+the+Simulink+model
- version_number: 1
- version_date: `2023-09-22T14:02:24.756+02:00`
- ancestors: Magic Real-Time Communication Designer > Simulation with Simulink
- labels: []

### NORMALIZED CONTENT

After the initialization step you can generate Simulink models using the LoadSimulinkModel.m script.

To generate the Simulink models

1. Run LoadSimulinkModel.
2. Select the desired xml you want to generate from. The xml gets copied to the matlab workspace, and the generation starts. After the generation finishes (assuming that you used the example Thermostat.xml) the workspace should look like this: [ATTACHMENT filename='image2020-11-12_15-12-49.png']
3. Open <your_model>.slx.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">After the initialization step you can generate Simulink models using the LoadSimulinkModel.m script.</p><p class="FirstParagraph"><br /></p><p class="FirstParagraph">To generate the Simulink models</p><hr /><ol><li>Run LoadSimulinkModel.</li><li>Select the desired xml you want to generate from. The xml gets copied to the matlab workspace, and the generation starts. After the generation finishes (assuming that you used the example Thermostat.xml) the workspace should look like this:<br /><ac:image><ri:attachment ri:filename="image2020-11-12_15-12-49.png"><ri:page ri:content-title="Generating the Simulink model" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></li><li>Open &lt;your_model&gt;.slx.</li></ol><p class="FirstParagraph"><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=191935994 space=MRTCD2024xR2 version=2 -->
## PAGE 00016: Getting started

- page_id: `191935994`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191935994/Getting+started
- version_number: 2
- version_date: `2025-05-06T15:05:03.131+02:00`
- ancestors: Magic Real-Time Communication Designer
- labels: []

### NORMALIZED CONTENT

**Welcome!**This user guide will walk you through the basics of using Magic Real-Time Communication Designer, including working with projects, setting up the modeling environment, defining DDS elements, importing and exporting XML files, and more.

Use the search box to find a specific topic or select one from the list below:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Welcome!</strong><span style="color: rgb(62,63,64);"> This user guide will walk you through the basics of using Magic Real-Time Communication Designer, including working with projects, setting up the modeling environment</span><span style="color: rgb(62,63,64);">, defining DDS elements, importing and exporting XML files, and more.</span></p><p><span style="color: rgb(62,63,64);">Use the search box to find a specific topic or select one from the list below</span><span class="confluence-link" style="color: rgb(62,63,64);">:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="60201284-9a7d-44b0-812b-445cfcf90c54" /></p>
````

<!--NOMAGIC_PAGE id=191936041 space=MRTCD2024xR2 version=1 -->
## PAGE 00017: Home Control Example

- page_id: `191936041`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936041/Home+Control+Example
- version_number: 1
- version_date: `2023-09-22T14:02:24.886+02:00`
- ancestors: Magic Real-Time Communication Designer
- labels: []

### NORMALIZED CONTENT

The aim of this example is to demonstrate how to make models using DDS and SysML semantics, how to assign quality of service profiles. Also it provides information how to generate RTI Connext DDS model in XML format that can be used in various ways like for the RTI Connext code generator or for generating MATLAB Simulink models.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><span lang="EN">The aim of this example is to demonstrate how to make models using DDS and SysML semantics, how to assign quality of service profiles. Also it provides information how to generate RTI Connext DDS model in XML format that can be used in various ways like for the RTI Connext code generator or for generating MATLAB Simulink models.</span></p><p class="FirstParagraph"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="cfb9a75d-74f0-4ba6-97ca-91ec209cd98e" /></p>
````

<!--NOMAGIC_PAGE id=191936057 space=MRTCD2024xR2 version=1 -->
## PAGE 00018: Illegal Inheritance

- page_id: `191936057`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936057/Illegal+Inheritance
- version_number: 1
- version_date: `2023-09-22T14:02:25.554+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.NonStructInheritanceRule

**Qualified name**: DDS::Validation::DDS_Illegal_DDS_Inheritance

**Description:**This plugin currently only supports inheritance between Structs.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.NonStructInheritanceRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Illegal_DDS_Inheritance</p><p><strong>Description: </strong>This plugin currently only supports inheritance between Structs.</p>
````

<!--NOMAGIC_PAGE id=191935998 space=MRTCD2024xR2 version=1 -->
## PAGE 00019: Importing DDS Profile and DDS Style in Other Projects

- page_id: `191935998`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191935998/Importing+DDS+Profile+and+DDS+Style+in+Other+Projects
- version_number: 1
- version_date: `2023-09-22T14:02:23.944+02:00`
- ancestors: Magic Real-Time Communication Designer > Getting started
- labels: ['reuse-dds-style', 'reuse-dds-profile']

### NORMALIZED CONTENT

The created DDS projects already have the DDS profile imported and DDS Style set. You ca reuse them in non-DDs projects.

##### Reusing the DDS profile in non-DDS projects

Reusing the DDS profile in non-DDS projects

1. Open a non-DDS project in which you want to reuse the DDS profile.
2. On the main menu, select File > Use Project > Use Local Project.
3. In the opened Use Project dialog, you can select the DDS profile either: - From predefined location. Select the Paths to used projects : <install.root>\profiles and from the list below, select the dds_profile.mdzip . - From File system. Click [ATTACHMENT filename='three_dot_button.png'] and from the product install folder, select profiles/dds_profile.mdzip . Click Open .
4. Click Next > Finish . The DDS profile is used in the project. [ATTACHMENT filename='using_dds_profile_in_other_projects.png']

##### Reusing the DDS Style in non-DDS projects

Reusing the DDS Style in non-DDS projects

1. Open a non-DDS project in which you want to reuse the DDS Style.
2. On the main menu, select Options > Project .
3. In the Project Options dialog, select the Symbol Style property group.
4. On the right side of the dialog, click the Import button, and from the product install folder, select templates/DDSStyle.stl . Click Open .
5. Select the DDSSyle from the Symbol Styles list.
6. Click OK . The DDS Style is used in the project. [ATTACHMENT filename='selecting_ddsStyle_in_other_projects.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">The created DDS projects already have the DDS profile imported and DDS Style set. You ca reuse them in non-DDs projects. </p><p class="FirstParagraph"><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="3c27f29d-5174-4870-87d5-2a8fd1589241" /></p><h3 class="FirstParagraph">Reusing the DDS profile in non-DDS projects</h3><p class="FirstParagraph">Reusing the DDS profile in non-DDS projects</p><hr /><ol><li class="FirstParagraph">Open a non-DDS project in which you want to reuse the DDS profile.</li><li class="FirstParagraph">On the main menu, select <strong>File</strong> &gt; <strong>Use Project</strong> &gt; <strong>Use Local Project.</strong></li><li class="FirstParagraph">In the opened <strong>Use Project</strong> dialog, you can select the DDS profile either: <br /> - From predefined location. Select the <strong>Paths to used projects</strong>: &lt;install.root&gt;\profiles and from the list below, select the <em>dds_profile.mdzip</em>.<br /> - From File system. Click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="three_dot_button.png"><ri:page ri:content-title="Importing DDS Profile and DDS Style in Other Projects" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image> and from the product install folder, select <em>profiles/dds_profile.mdzip</em>. Click <strong>Open</strong>.</li><li class="FirstParagraph">Click <strong>Next</strong> &gt; <strong>Finish</strong>.<br />The DDS profile is used in the project.<br /><ac:image><ri:attachment ri:filename="using_dds_profile_in_other_projects.png"><ri:page ri:content-title="Importing DDS Profile and DDS Style in Other Projects" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></li></ol><h3 class="FirstParagraph">Reusing the DDS Style in non-DDS projects</h3><p class="FirstParagraph">Reusing the DDS Style in non-DDS projects</p><hr /><ol><li class="FirstParagraph">Open a non-DDS project in which you want to reuse the DDS Style.</li><li>On the main menu, select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li>In the <strong>Project Options</strong> dialog, select the <strong>Symbol Style </strong>property group.</li><li>On the right side of the dialog, click the <strong>Import</strong> button, and from the product install folder, select <em>templates/DDSStyle.stl</em>. Click <strong>Open</strong>.</li><li>Select the <strong>DDSSyle</strong> from the Symbol Styles list.</li><li>Click <strong>OK</strong>.<br />The DDS Style is used in the project.<br /><br /><ac:image><ri:attachment ri:filename="selecting_ddsStyle_in_other_projects.png"><ri:page ri:content-title="Importing DDS Profile and DDS Style in Other Projects" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></li></ol>
````

<!--NOMAGIC_PAGE id=191936030 space=MRTCD2024xR2 version=2 -->
## PAGE 00020: Importing DDS XML

- page_id: `191936030`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936030/Importing+DDS+XML
- version_number: 2
- version_date: `2024-10-08T09:29:18.852+02:00`
- ancestors: Magic Real-Time Communication Designer > Getting started
- labels: ['import-dds-models-in-xml-format']

### NORMALIZED CONTENT

You can also import already existing DDS models in XML format. The imported model does not contain the diagrams associated with the models. You can use modeling tool diagram initialization to make and customize your diagrams very easily however.

To import DDS models in XML format

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MD2024xR2'] , select Tools > DDS > Import DDS XML.
2. In the Select DDS XML file dialog, select the DDS XML file.
3. Click Import DDS .
4. In the opened **Select Package** dialog, select the Package from the model wherein the file will be imported. 
The model defined in the XML is imported. As example see the figure below. QoS Profilescontained by the same file will not be imported. For this, you have to use the [CONFLUENCE_PAGE title='Importing QoS Profile' space='MRTCD2024xR2'] to import them.

[IMAGE alt='' src='']

###### The XML file content imported into model.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can also import already existing DDS models in XML format. The imported model does not contain the diagrams associated with the models. You can use modeling tool diagram initialization to make and customize your diagrams very easily however.</p><p>To import DDS models in XML format</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main menu]]></ac:plain-text-link-body></ac:link>, select <strong>Tools</strong> &gt; <strong>DDS</strong> &gt; <strong>Import DDS XML.</strong></li><li>In the <strong>Select DDS XML file</strong> dialog, select the DDS XML file.</li><li>Click <strong>Import DDS</strong>.</li><li><p class="auto-cursor-target">In the opened <strong style="letter-spacing: 0.0px;">Select Package</strong> dialog, select the Package from the model wherein the file will be imported.<br />The model defined in the XML is imported. As example see the figure below.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="a0a739d2-8e24-4780-9d6a-b6d2956620e0"><ac:rich-text-body><p>QoS Profiles<span> contained by the same file will not be imported. For this, you have to use the <ac:link><ri:page ri:content-title="Importing QoS Profile" ri:space-key="MRTCD2024xR2" /><ac:plain-text-link-body><![CDATA[Import QoS Profile feature]]></ac:plain-text-link-body></ac:link> to import them.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p class="auto-cursor-target"><ac:image ac:align="center"><ri:attachment ri:filename="importing_xml.png"><ri:page ri:content-title="Importing DDS XML" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The XML file content imported into model.</h6>
````

<!--NOMAGIC_PAGE id=191936026 space=MRTCD2024xR2 version=2 -->
## PAGE 00021: Importing QoS Profile

- page_id: `191936026`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936026/Importing+QoS+Profile
- version_number: 2
- version_date: `2024-10-08T09:29:18.795+02:00`
- ancestors: Magic Real-Time Communication Designer > Getting started
- labels: ['import-qos-profile', 'reimport-qos']

### NORMALIZED CONTENT

You can import your already existing QoS Profiles in DDS XML format created with e.g. RTI System Designer, as shown in figure below.

[IMAGE alt='' src='']

To import QoS Profile

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MD2024xR2'] , select Tools > DDS > Import QoS Profile .
2. In the Select DDS XML file containing QoS libraries dialog, select QoS Profile.
3. Click Import QoS .
4. In the opened Select Package dialog, select the Package from the model wherein the profile will be imported.

[IMAGE alt='' src='']

If you modify the original QoS definition file, you can reimport it. Note, that the existing QoS Profiles will be replaced, so you will have to restore their assignments manually.

To reimport QoS

- Right-click the imported*UserQosRepository*element and from the shortcut menu, select the **Reimport QoS Profile**. [IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can import your already existing QoS Profiles in DDS XML format created with e.g. RTI System Designer, as shown in figure below.</p><p><ac:image><ri:attachment ri:filename="image2020-11-12_14-57-57.png"><ri:page ri:content-title="Importing QoS Profile" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></p><p><br /></p><p>To import QoS Profile</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main menu]]></ac:plain-text-link-body></ac:link>, select <strong>Tools</strong> &gt; <strong>DDS</strong> &gt; <strong>Import QoS Profile</strong>.</li><li>In the <strong>Select DDS XML file containing QoS libraries</strong> dialog, select QoS Profile.</li><li>Click <strong>Import QoS</strong>.</li><li>In the opened <strong>Select Package</strong> dialog, select the Package from the model wherein the profile will be imported.</li></ol><p><ac:image><ri:attachment ri:filename="Import_QoS_Profile.png"><ri:page ri:content-title="Importing QoS Profile" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image><span style="letter-spacing: 0.0px;"><br /></span></p><p><span style="letter-spacing: 0.0px;"><br /></span></p><p><span style="letter-spacing: 0.0px;">If you modify the original QoS definition file, you can reimport it. Note, that t<span>he existing QoS Profiles will be replaced, so you will have to restore their assignments manually.</span></span></p><p><span style="letter-spacing: 0.0px;"><span style="letter-spacing: 0.0px;">To reimport QoS</span><br /></span></p><hr /><ul><li><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;">Right-click the imported </span><em style="letter-spacing: 0.0px;">UserQosRepository</em><span style="letter-spacing: 0.0px;"> element and from the shortcut menu, select the <strong>Reimport QoS Profile</strong>. <br /></span></p><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;"><ac:image><ri:attachment ri:filename="reimport_QoS_profile.png"><ri:page ri:content-title="Importing QoS Profile" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image><br /></span></p></li></ul>
````

<!--NOMAGIC_PAGE id=191936058 space=MRTCD2024xR2 version=1 -->
## PAGE 00022: Incompatible Base Extendibility

- page_id: `191936058`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936058/Incompatible+Base+Extendibility
- version_number: 1
- version_date: `2023-09-22T14:02:25.621+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.IncompatibleBaseExtendibilityRule

**Qualified name**: DDS::Validation::DDS_Incompatible_Base_Extendibility

**Description:**The extensibility of an Alias and its referenced type must be the same.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.IncompatibleBaseExtendibilityRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Incompatible_Base_Extendibility</p><p><strong>Description: </strong>The extensibility of an Alias and its referenced type must be the same.</p>
````

<!--NOMAGIC_PAGE id=191936035 space=MRTCD2024xR2 version=1 -->
## PAGE 00023: Install for simulation

- page_id: `191936035`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936035/Install+for+simulation
- version_number: 1
- version_date: `2023-09-22T14:02:24.666+02:00`
- ancestors: Magic Real-Time Communication Designer > Simulation with Simulink
- labels: []

### NORMALIZED CONTENT

To install for simulation

1. Install Matlab with Simulink
2. Install RTI DDS Blockset by following the instructions in the installation guide video
3. According to OS do the following: - Windows: Add <rti_connext_dds_installation_folder>\lib\x64Win64VS2017\ to PATH - macOS: a. Install Xcode Command Line Tools with xcode-select --install b. Configure environment variables by updating the following section of /Applications/MATLAB_R2019a.app/Contents/Info.plist :

<key>LSEnvironment</key> 
 <dict> 
 <key>MATLAB_USE_USERWORK</key> 
 <string>1</string> 
 <key>NDDSHOME</key> 
 <string>/Applications/rti_connext_dds-5.3.1</string> 
 <key>RTI_LICENSE_FILE</key> 
 <string>/Applications/rti_connext_dds-5.3.1/rti_license.dat</string> 
 <key>RTI_LD_LIBRARY_PATH</key> 
 <string>/Applications/rti_connext_dds-5.3.1/lib/x64Darwin17clang9.0</string> 
 <key>DEVELOPER_DIR</key> 
 <string>/Library/Developer/CommandLineTools</string> 
 </dict>

If you are using RTI Connext 6.0.0, use rti_connext_dds-6.0.0 in the above script.

c. Notify macOS about the Info.plist change: */System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -v -f /Applications/MATLAB_R2019a.app/* 
 d. Start Matlab 
 e. Run DDS.Rpath.add

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="letter-spacing: 0.0px;">To install for simulation</span></p><hr /><ol><li>Install <a href="https://www.mathworks.com/downloads/">Matlab with Simulink</a></li><li>Install <a href="https://www.mathworks.com/hardware-support/rti-dds.html">RTI DDS Blockset</a> by following the instructions in <a href="https://bit.ly/2lXuMOK">the installation guide video</a></li><li>According to OS do the following:<br /> - Windows: Add <em>&lt;rti_connext_dds_installation_folder&gt;\lib\x64Win64VS2017\ to PATH</em><br /> - macOS:<br />       a. Install Xcode Command Line Tools with xcode-select --install<br />       b. Configure environment variables by updating the following section of <em>/Applications/MATLAB_R2019a.app/Contents/Info.plist</em>:</li></ol><p class="SourceCode">   &lt;key&gt;LSEnvironment&lt;/key&gt;<br />     &lt;dict&gt;<br />         &lt;key&gt;MATLAB_USE_USERWORK&lt;/key&gt;<br />         &lt;string&gt;1&lt;/string&gt;<br />         &lt;key&gt;NDDSHOME&lt;/key&gt;<br />         &lt;string&gt;/Applications/rti_connext_dds-5.3.1&lt;/string&gt;<br />         &lt;key&gt;RTI_LICENSE_FILE&lt;/key&gt;<br />         &lt;string&gt;/Applications/rti_connext_dds-5.3.1/rti_license.dat&lt;/string&gt;<br />         &lt;key&gt;RTI_LD_LIBRARY_PATH&lt;/key&gt;<br />         &lt;string&gt;/Applications/rti_connext_dds-5.3.1/lib/x64Darwin17clang9.0&lt;/string&gt;<br />         &lt;key&gt;DEVELOPER_DIR&lt;/key&gt;<br />         &lt;string&gt;/Library/Developer/CommandLineTools&lt;/string&gt;<br />     &lt;/dict&gt;</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="a95ac908-5528-47dc-9e59-288f34d2da31"><ac:rich-text-body><p><span>If you are using RTI Connext 6.0.0, use rti_connext_dds-6.0.0 in the above script.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">                   c. Notify macOS about the Info.plist change: <em>/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -v -f /Applications/MATLAB_R2019a.app/</em><br />                   d. Start Matlab<br />                   e. Run DDS.Rpath.add</p><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=191935993 space=MRTCD2024xR2 version=2 -->
## PAGE 00024: Installation

- page_id: `191935993`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191935993/Installation
- version_number: 2
- version_date: `2024-10-08T09:25:52.478+02:00`
- ancestors: Magic Real-Time Communication Designer
- labels: ['installing-dds-plugin', 'install-dds-plugin']

### NORMALIZED CONTENT

Before installing Connext DDS for MagicDraw, first install RTI Connext DDS by following the instructions in its [Getting Started guide](https://www.rti.com/gettingstarted).

To install Connext DDS for MagicDraw

1. Install [CONFLUENCE_PAGE title='Installation, Licensing, and System Requirements Documentation' space='IL2024xR2'] .
2. Install [CONFLUENCE_PAGE title='Installation, Licensing, and System Requirements Documentation' space='IL2024xR2'] .
3. Start MagicDraw.
4. On the main menu, click Help > Resource/Plugin Manager .
5. Click Import and select the Connext DDS for MagicDraw plugin archive ( connext-dds-magicdraw-plugin.zip ).
6. After the successful installation, restart the MagicDraw.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">Before installing Connext DDS for MagicDraw, first install RTI Connext DDS by following the instructions in its <a href="https://www.rti.com/gettingstarted">Getting Started guide</a>.</p><p>To install Connext DDS for MagicDraw</p><hr /><ol><li>Install <ac:link><ri:page ri:space-key="IL2024xR2" ri:content-title="Installation, Licensing, and System Requirements Documentation" /><ac:plain-text-link-body><![CDATA[MagicDraw]]></ac:plain-text-link-body></ac:link>.</li><li>Install <ac:link><ri:page ri:space-key="IL2024xR2" ri:content-title="Installation, Licensing, and System Requirements Documentation" /><ac:plain-text-link-body><![CDATA[SysML plugin]]></ac:plain-text-link-body></ac:link>.</li><li>Start MagicDraw.</li><li>On the main menu, click <strong>Help</strong> &gt; <strong>Resource/Plugin Manager</strong>. </li><li>Click <strong>Import</strong> and select the <em>Connext DDS for MagicDraw plugin</em> archive (<em>connext-dds-magicdraw-plugin.zip</em>).</li><li>After the successful installation, restart the MagicDraw.</li></ol>
````

<!--NOMAGIC_PAGE id=191936059 space=MRTCD2024xR2 version=1 -->
## PAGE 00025: Instance not Participant

- page_id: `191936059`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936059/Instance+not+Participant
- version_number: 1
- version_date: `2023-09-22T14:02:25.677+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.qos.QosDDSInstanceNotParticipantRule

**Qualified name**: DDS::Validation::QoS Validation Suite::QoS_Instance_Not_Participant

**Abbreviation**: INSTANCE_NOT_PARTICIPANT

**Description:**The types of properties assigned to QoS Assignments must be Domain Participants.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.qos.QosDDSInstanceNotParticipantRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::QoS Validation Suite::QoS_Instance_Not_Participant</p><p class="FirstParagraph"><strong>Abbreviation</strong>: INSTANCE_NOT_PARTICIPANT</p><p><strong>Description: </strong>The types of properties assigned to QoS Assignments must be Domain Participants.</p>
````

<!--NOMAGIC_PAGE id=191936060 space=MRTCD2024xR2 version=1 -->
## PAGE 00026: Invalid Member Multiplicity

- page_id: `191936060`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936060/Invalid+Member+Multiplicity
- version_number: 1
- version_date: `2023-09-22T14:02:25.744+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: warning

**Implementation**: com.nomagic.magicdraw.dds.validation.InvalidMemberMultiplicityRule

**Qualified name**: DDS::Validation::DDS_Invalid_Member_Multiplicity

**Description:**The multiplicity of a DDS Member must either be an exact number, or fully optional with a finite upper limit e.g.: 8..8 or 0..4. If you have a Member with multiplicity 8..12, that can be separated into two Members, a 8..8 and a 0..4.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: warning</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.InvalidMemberMultiplicityRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Invalid_Member_Multiplicity</p><p><strong>Description: </strong>The multiplicity of a DDS Member must either be an exact number, or fully optional with a finite upper limit e.g.: 8..8 or 0..4. If you have a Member with multiplicity 8..12, that can be separated into two Members, a 8..8 and a 0..4.</p>
````

<!--NOMAGIC_PAGE id=191936061 space=MRTCD2024xR2 version=1 -->
## PAGE 00027: Invalid Member Type

- page_id: `191936061`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936061/Invalid+Member+Type
- version_number: 1
- version_date: `2023-09-22T14:02:25.807+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.InvalidMemberTypeRule

**Qualified name**: DDS::Validation::DDS_Invalid_Member_Type

**Abbreviation**: INV_MEMBER_TYPE

**Description:**The types of Members must be DDS types. For primitive types, use the ones in DDS::TypeSystem::PrimitiveTypes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.InvalidMemberTypeRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Invalid_Member_Type</p><p class="FirstParagraph"><strong>Abbreviation</strong>: INV_MEMBER_TYPE</p><p><strong>Description: </strong>The types of Members must be DDS types. For primitive types, use the ones in DDS::TypeSystem::PrimitiveTypes.</p>
````

<!--NOMAGIC_PAGE id=191936062 space=MRTCD2024xR2 version=1 -->
## PAGE 00028: Invalid Port Type

- page_id: `191936062`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936062/Invalid+Port+Type
- version_number: 1
- version_date: `2023-09-22T14:02:25.866+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.InvalidPortTypeRule

**Qualified name**: DDS::Validation::DDS_Invalid_Port_Type

**Abbreviation**: INVALID_PORT_TYPE

**Description:**Domain Participants must not be used as port types.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.InvalidPortTypeRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Invalid_Port_Type</p><p class="FirstParagraph"><strong>Abbreviation</strong>: INVALID_PORT_TYPE</p><p><strong>Description: </strong>Domain Participants must not be used as port types.</p>
````

<!--NOMAGIC_PAGE id=191936063 space=MRTCD2024xR2 version=1 -->
## PAGE 00029: Invalid Repository

- page_id: `191936063`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936063/Invalid+Repository
- version_number: 1
- version_date: `2023-09-22T14:02:25.942+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.qos.QoSRepositoryValidator

**Qualified name**: DDS::Validation::QoS Validation Suite::QoS_Invalid_Repository

**Abbreviation**: QOS_REPO_DESYNC

**Description:**QoS XML moved or changed. Check the source xml file and reimport profile.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.qos.QoSRepositoryValidator</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::QoS Validation Suite::QoS_Invalid_Repository</p><p class="FirstParagraph"><strong>Abbreviation</strong>: QOS_REPO_DESYNC</p><p><strong>Description: </strong>QoS XML moved or changed. Check the source xml file and reimport profile.</p>
````

<!--NOMAGIC_PAGE id=191936064 space=MRTCD2024xR2 version=1 -->
## PAGE 00030: Invalid Topic Type Property Direction

- page_id: `191936064`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936064/Invalid+Topic+Type+Property+Direction
- version_number: 1
- version_date: `2023-09-22T14:02:26.035+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.InvalidTopicTypeDirectionRule

**Qualified name**: DDS::Validation::DDS_Invalid_Topic_Type_Property_Direction

**Abbreviation**: INV_TOPIC_PROP_DIR

**Description:**Direction of Topic Type Properties must be 'out'.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.InvalidTopicTypeDirectionRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Invalid_Topic_Type_Property_Direction</p><p class="FirstParagraph"><strong>Abbreviation</strong>: INV_TOPIC_PROP_DIR</p><p><strong>Description: </strong>Direction of Topic Type Properties must be 'out'.</p>
````

<!--NOMAGIC_PAGE id=191935992 space=MRTCD2024xR2 version=2 -->
## PAGE 00031: Magic Real-Time Communication Designer

- page_id: `191935992`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191935992/Magic+Real-Time+Communication+Designer
- version_number: 2
- version_date: `2025-05-06T15:05:02.998+02:00`
- ancestors: 
- labels: ['dds-real-time-communication-plugin']

### NORMALIZED CONTENT

The Connext DDS for MagicDraw plugin is an environment for editing [Connext DDS](https://www.rti.com/products/connext-dds-professional) models in a visual way.

##### Background

The OMG Data-Distribution Service for Real-Time Systems (DDS) is the first open international middleware standard directly addressing publish-subscribe communications for real-time and embedded systems.

RTI Connext DDS Professional, based on a connectivity databus, offers a robust framework for developing and integrating mission critical systems. It is fully compliant with the OMG DDS for Real-Time Systems standard.

##### Advantages

With the Connext DDS for MagicDraw plugin, you can model the DDS-related aspects of your system using UML, extended by a DDS-specific profile. This offers the following advantages:

- The overall system (from requirements to functional applications) will have a unified representation, providing a common view of the system and a single source of truth.
- You can use an already familiar modeling language.
- The DDS entities and their relationships are displayed visually in a graphical notation.

The Magic Real-Time Communication Designer documentation consists of the following sections:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">The Connext DDS for MagicDraw plugin is an environment for editing <a href="https://www.rti.com/products/connext-dds-professional">Connext DDS</a> models in a visual way.</p><h3>Background</h3><p class="FirstParagraph">The OMG Data-Distribution Service for Real-Time Systems (DDS) is the first open international middleware standard directly addressing publish-subscribe communications for real-time and embedded systems.</p><p>RTI Connext DDS Professional, based on a connectivity databus, offers a robust framework for developing and integrating mission critical systems. It is fully compliant with the OMG DDS for Real-Time Systems standard.</p><h3>Advantages</h3><p class="FirstParagraph">With the Connext DDS for MagicDraw plugin, you can model the DDS-related aspects of your system using UML, extended by a DDS-specific profile. This offers the following advantages:</p><ul><li>The overall system (from requirements to functional applications) will have a unified representation, providing a common view of the system and a single source of truth.</li><li>You can use an already familiar modeling language.</li><li>The DDS entities and their relationships are displayed visually in a graphical notation.</li></ul><p><br /></p><p><span style="color: rgb(62,63,64);">The Magic Real-Time Communication Designer documentation consists of the following sections:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="675a6e7f-bff9-4f71-809c-aa22cf1a125d" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=191936065 space=MRTCD2024xR2 version=1 -->
## PAGE 00032: Missing Domain Attribute

- page_id: `191936065`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936065/Missing+Domain+Attribute
- version_number: 1
- version_date: `2023-09-22T14:02:26.112+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: warning

**Implementation**: com.nomagic.magicdraw.dds.validation.MissingDomainAttribute

**Qualified name**: DDS::Validation::DDS_Missing_Domain_Attribute

**Description:**A Domain should refer at least one Topic and at least one Domain Participant. Use a DDS Domain Table for managing domains.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: warning</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.MissingDomainAttribute</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Missing_Domain_Attribute</p><p><strong>Description: </strong>A Domain should refer at least one Topic and at least one Domain Participant. Use a DDS Domain Table for managing domains.</p>
````

<!--NOMAGIC_PAGE id=191936066 space=MRTCD2024xR2 version=1 -->
## PAGE 00033: Missing Domain ID

- page_id: `191936066`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936066/Missing+Domain+ID
- version_number: 1
- version_date: `2023-09-22T14:02:26.162+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.IncompatibleBaseExtendibilityRule

**Qualified name**: DDS::Validation::DDS_Incompatible_Base_Extendibility

**Description:**Domains must specify Domain IDs.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.IncompatibleBaseExtendibilityRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Incompatible_Base_Extendibility</p><p><strong>Description: </strong>Domains must specify Domain IDs.</p>
````

<!--NOMAGIC_PAGE id=191936067 space=MRTCD2024xR2 version=1 -->
## PAGE 00034: Missing Element Name

- page_id: `191936067`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936067/Missing+Element+Name
- version_number: 1
- version_date: `2023-09-22T14:02:26.215+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: warning

**Implementation**: com.nomagic.magicdraw.dds.validation.MissingDDSElementNameRule

**Qualified name**: DDS::Validation::DDS_Missing_Element_Name

**Abbreviation**: DOMAN_PARTICIPANT_NO_INST

**Description:**DDS elements sould have names.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: warning</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.MissingDDSElementNameRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Missing_Element_Name</p><p class="FirstParagraph"><strong>Abbreviation</strong>: DOMAN_PARTICIPANT_NO_INST</p><p><strong>Description: </strong>DDS elements sould have names.</p>
````

<!--NOMAGIC_PAGE id=191936068 space=MRTCD2024xR2 version=1 -->
## PAGE 00035: Multiple Struct Inheritance

- page_id: `191936068`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936068/Multiple+Struct+Inheritance
- version_number: 1
- version_date: `2023-09-22T14:02:26.274+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.MutipleStructInheritanceRule

**Qualified name**: DDS::Validation::DDS_Multiple_Struct_Inheritance

**Description:**This plugin currently only supports single inheritance between Structs.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.MutipleStructInheritanceRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Multiple_Struct_Inheritance</p><p><strong>Description: </strong>This plugin currently only supports single inheritance between Structs.</p>
````

<!--NOMAGIC_PAGE id=191936069 space=MRTCD2024xR2 version=1 -->
## PAGE 00036: Multitype Topic

- page_id: `191936069`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936069/Multitype+Topic
- version_number: 1
- version_date: `2023-09-22T14:02:26.333+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.MultitypeTopicRule

**Qualified name**: DDS::Validation::DDS_Multitype_Topic

**Description:**Topics must have only one Topic Type Property. If you simply want either-or, use a DDS Union. For more complicated types, read the [DDS Extensibe Type System.](https://www.omg.org/spec/DDS-XTypes/1.3/PDF)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.MultitypeTopicRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Multitype_Topic</p><p><strong>Description: </strong>Topics must have only one Topic Type Property. If you simply want either-or, use a DDS Union. For more complicated types, read the <a href="https://www.omg.org/spec/DDS-XTypes/1.3/PDF" style="letter-spacing: 0.0px;">DDS Extensibe Type System.</a></p>
````

<!--NOMAGIC_PAGE id=191936070 space=MRTCD2024xR2 version=1 -->
## PAGE 00037: Non-Nmeric Domain ID

- page_id: `191936070`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936070/Non-Nmeric+Domain+ID
- version_number: 1
- version_date: `2023-09-22T14:02:26.378+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.NonNumericDDSDomainIDRule

**Qualified name**: DDS::Validation::DDS_NonNumeric_Domain_ID

**Description:**Domain IDs must be numeric.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.NonNumericDDSDomainIDRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_NonNumeric_Domain_ID</p><p><strong>Description: </strong>Domain IDs must be numeric.</p>
````

<!--NOMAGIC_PAGE id=191936071 space=MRTCD2024xR2 version=1 -->
## PAGE 00038: Participant Type not Referenced

- page_id: `191936071`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936071/Participant+Type+not+Referenced
- version_number: 1
- version_date: `2023-09-22T14:02:26.424+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.qos.QoSParticipantTypeNotReferencedRule

**Qualified name**: DDS::Validation::QoS Validation Suite::QoS_Participant_Type_Not_Referenced

**Abbreviation**: PARTICIPANT_TYPE_NOT_REFERENCED

**Description:**Data Port QoS assignments must reference its instances' types.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.qos.QoSParticipantTypeNotReferencedRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::QoS Validation Suite::QoS_Participant_Type_Not_Referenced</p><p class="FirstParagraph"><strong>Abbreviation</strong>: PARTICIPANT_TYPE_NOT_REFERENCED</p><p><strong>Description: </strong>Data Port QoS assignments must reference its instances' types.</p>
````

<!--NOMAGIC_PAGE id=191936049 space=MRTCD2024xR2 version=1 -->
## PAGE 00039: Qos Assignments

- page_id: `191936049`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936049/Qos+Assignments
- version_number: 1
- version_date: `2023-09-22T14:02:25.114+02:00`
- ancestors: Magic Real-Time Communication Designer > Home Control Example
- labels: []

### NORMALIZED CONTENT

The currents version allows three kind of QoS assignment each of which can be swiftly created with specific generic tables. Since they were already covered in previous sections we only assign one for demonstration purposes. [CONFLUENCE_PAGE title='QoS profile assignments' space='MRTCD2024xR2']>]]>

As shown in the figure below, the case is a kind of a special one because the port readLight is not actually on the HomeController block but on its light port’s type called NestedLightPort. There is a validation rule which checks if the port has no connection with the given instance.

[IMAGE alt='' src='']

###### The example of Endpoint QoS Assignment Table.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The currents version allows three kind of QoS assignment each of which can be swiftly created with specific generic tables. Since they were already covered in previous sections we only assign one for demonstration purposes. <ac:link><ri:page ri:content-title="QoS profile assignments" ri:space-key="MRTCD2024xR2" /><ac:plain-text-link-body><![CDATA[Learn how to create Endpoint QoS Assignment Table >>]]></ac:plain-text-link-body></ac:link></p><p>As shown in the figure below, the case is a kind of a special one because the port readLight is not actually on the HomeController block but on its light port’s type called NestedLightPort. There is a validation rule which checks if the port has no connection with the given instance.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="QoS_Assignment_table.png"><ri:page ri:content-title="Qos Assignments" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example of Endpoint QoS Assignment Table.</h6>
````

<!--NOMAGIC_PAGE id=191936016 space=MRTCD2024xR2 version=2 -->
## PAGE 00040: QoS profile assignments

- page_id: `191936016`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936016/QoS+profile+assignments
- version_number: 2
- version_date: `2024-10-08T09:29:18.674+02:00`
- ancestors: Magic Real-Time Communication Designer > Getting started
- labels: ['create-endpoint-qos-assignment-table']

### NORMALIZED CONTENT

There are three elements that QoS Profiles can be assigned to in the model:

- Endpoints typed by Topic.
- DomainParticipants.
- Topics.

To create an empty Endpoint QoS Assignment Table

1. In the Containment tree , right-click a predefined Endpoint QoS Package.
2. From the shortcut menu, select Create Diagram and from the opened dialog, select Endpoint QoS Assignment Table.
3. The unnamed table is created. Type its name and press enter.

To fill in the Endpoint QoS Assignment Table

1. From the table toolbar, click the Add New button. The new row appears and Endpoint QoS Assignment element is created in the model.
2. In the table, specify the following: 
 - Double-click the **Name** cell and type Endpoint QoS Assignment name. 
 - Double-click the **QoS Profile** cell, select [IMAGE alt='' src=''] and in the **Select Elements** dialog choose QoS Profile. 
 - Double-click the **Endpoint** cell, select [IMAGE alt='' src=''] and in the **Select Port**dialog choose already created ports or use the **Creation Mode** to create new port. 
 - Double-click the **Domain Participant Instance** cell, select [IMAGE alt='' src=''] and in the **Select Property**dialog choose already created Part Properties or use the **Creation Mode** to create new Part Property.

Assigning QoS on subscribers/publishers is not possible since they are derived from the model and not explicitly marked.

- To assign QoS Profiles on Topics create a Topic QoS Assignment Table. [ATTACHMENT filename='topic_qos_assignemnt_table_example.png']
- To assign QoS Profiles on Domain Participants create a Participant QoS Assignment Table. [ATTACHMENT filename='participant_qos_assignment.png']
- To assign QoS Profiles on Endpoints create a Endpoint QoS Assignment Table. [ATTACHMENT filename='endpoint_Qos_assignment_table.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">There are three elements that QoS Profiles can be assigned to in the model:</p><ul><li class="FirstParagraph">Endpoints typed by Topic.</li><li class="FirstParagraph">DomainParticipants.</li><li class="FirstParagraph">Topics.</li></ul><p><br /></p><p>To create an empty Endpoint QoS Assignment Table</p><hr /><ol><li>In the <a href="https://docs.nomagic.com/display/MD2024xR2/Containment+tab">Containment tree</a>, right-click a predefined <em>Endpoint QoS </em>Package.</li><li>From the shortcut menu, select <strong>Create Diagram </strong>and from the opened dialog, select Endpoint QoS Assignment Table.</li><li>The unnamed table is created. Type its name and press enter.</li></ol><p><br /></p><p>To fill in the Endpoint QoS Assignment Table</p><hr /><ol><li>From the table toolbar, click the <strong>Add New</strong> button. The new row appears and Endpoint QoS Assignment element is created in the model.</li><li><p class="auto-cursor-target">In the table, specify the following:<br /> - Double-click the <strong>Name</strong> cell and type Endpoint QoS Assignment name.<br /> - Double-click the <strong>QoS Profile</strong> cell, select <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="QoS profile assignments" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></span> and in the <strong>Select Elements</strong> dialog choose QoS Profile.<br /> - Double-click the <strong>Endpoint</strong> cell, select <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="QoS profile assignments" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></span> and in the <strong>Select Port </strong>dialog choose already created ports or use the <strong>Creation Mode</strong> to create new port.<br /> - Double-click the <strong>Domain Participant Instance</strong> cell, select <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="QoS profile assignments" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></span> and in the <strong>Select Property </strong>dialog choose already created Part Properties or use the <strong>Creation Mode</strong> to create new Part Property.</p></li></ol><p class="FirstParagraph"><span><br /></span></p><p class="FirstParagraph"><span>Assigning QoS on subscribers/publishers is not possible since they are derived from the model and not explicitly marked.</span></p><ul><li>To assign QoS Profiles on Topics create a Topic QoS Assignment Table.<br /><ac:image><ri:attachment ri:filename="topic_qos_assignemnt_table_example.png"><ri:page ri:content-title="QoS profile assignments" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></li><li>To assign QoS Profiles on Domain Participants create a Participant QoS Assignment Table.<br /><ac:image><ri:attachment ri:filename="participant_qos_assignment.png"><ri:page ri:content-title="QoS profile assignments" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></li><li>To assign QoS Profiles on Endpoints create a Endpoint QoS Assignment Table.<br /><ac:image><ri:attachment ri:filename="endpoint_Qos_assignment_table.png"><ri:page ri:content-title="QoS profile assignments" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></li></ul>
````

<!--NOMAGIC_PAGE id=191936039 space=MRTCD2024xR2 version=1 -->
## PAGE 00041: Setting up the Simulink model

- page_id: `191936039`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936039/Setting+up+the+Simulink+model
- version_number: 1
- version_date: `2023-09-22T14:02:24.813+02:00`
- ancestors: Magic Real-Time Communication Designer > Simulation with Simulink
- labels: []

### NORMALIZED CONTENT

If Simulink Buses are not created they must be created manually.

To send data through a data writer

1. Create a Bus Creator.
2. Set output type to the Simulink Bus compatible with the data writer.
3. Add and name pins so they correspond to members in the Simulink Bus.
4. Connect signals to the pins.

Signal names and types has to correspond to the names and types specified by the Simulink Bus as well.

To collect data from data readers

1. Create a Bus Selector.
2. Connect it to the data reader.
3. Select the signals to output.

Connecting the Bus Selector to a data reader picks the Simulink Bus type automatically.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">If Simulink Buses are not created they must be created manually.</p><p><br /></p><p>To send data through a data writer</p><hr /><ol><li>Create a Bus Creator.</li><li>Set output type to the Simulink Bus compatible with the data writer.</li><li>Add and name pins so they correspond to members in the Simulink Bus.</li><li>Connect signals to the pins.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="6ba60b43-b9ac-434c-b9ff-8770af2917af"><ac:rich-text-body><p>Signal names and types has to correspond to the names and types specified by the Simulink Bus as well.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To collect data from data readers</p><hr /><ol><li>Create a Bus Selector.</li><li>Connect it to the data reader.</li><li>Select the signals to output.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="73d0e571-8cdb-479b-986a-42beb83230b6"><ac:rich-text-body><p>Connecting the Bus Selector to a data reader picks the Simulink Bus type automatically.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=191936034 space=MRTCD2024xR2 version=1 -->
## PAGE 00042: Simulation with Simulink

- page_id: `191936034`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936034/Simulation+with+Simulink
- version_number: 1
- version_date: `2023-09-22T14:02:24.615+02:00`
- ancestors: Magic Real-Time Communication Designer
- labels: []

### NORMALIZED CONTENT

A Simulink model can be generated from the DDS XML generated by the Matlab plugin, which can be used to simulate the behavior of the modeled DDS system.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><span lang="EN">A Simulink model can be generated from the DDS XML generated by the Matlab plugin, which can be used to simulate the behavior of the modeled DDS system.</span></p><p class="FirstParagraph"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e4ccea78-c681-4939-b6e4-a9a976eb6044" /></p>
````

<!--NOMAGIC_PAGE id=191936072 space=MRTCD2024xR2 version=1 -->
## PAGE 00043: Struct Member Visibility

- page_id: `191936072`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936072/Struct+Member+Visibility
- version_number: 1
- version_date: `2023-09-22T14:02:26.475+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.InvisibleStructMember

**Qualified name**: DDS::Validation::DDS_Stuct_Member_Visibility

**Description:**Members of Structs must have public visibility.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.InvisibleStructMember</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Stuct_Member_Visibility</p><p><strong>Description: </strong>Members of Structs must have public visibility.</p>
````

<!--NOMAGIC_PAGE id=191936073 space=MRTCD2024xR2 version=1 -->
## PAGE 00044: Topic Missing from Domain

- page_id: `191936073`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936073/Topic+Missing+from+Domain
- version_number: 1
- version_date: `2023-09-22T14:02:26.526+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.ReferencedTopicMissingFromDomainRule

**Qualified name**: DDS::Validation::DDS_ReferencedTopicMissingFromDomainRule

**Abbreviation**: TOPIC_MISSING_FROM_DOMAIN

**Description:**Topics referenced by a Domain’s Participants must be in the Domain’s topics field.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.ReferencedTopicMissingFromDomainRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_ReferencedTopicMissingFromDomainRule</p><p class="FirstParagraph"><strong>Abbreviation</strong>: TOPIC_MISSING_FROM_DOMAIN</p><p><strong>Description: </strong>Topics referenced by a Domain’s Participants must be in the Domain’s topics field.</p>
````

<!--NOMAGIC_PAGE id=191936040 space=MRTCD2024xR2 version=1 -->
## PAGE 00045: Type mapping

- page_id: `191936040`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936040/Type+mapping
- version_number: 1
- version_date: `2023-09-22T14:02:24.850+02:00`
- ancestors: Magic Real-Time Communication Designer > Simulation with Simulink
- labels: []

### NORMALIZED CONTENT

This table shows how different types match between the models. The use of n..n and 0..n multiplicities in the modeling tool is supported but will result in fixed variable sized signals in Simulink.

| DDS for MagicDraw | Connext DDS XML | MATLAB Type | Simulink Type |
| --- | --- | --- | --- |
| Boolean | boolean | logical | boolean |
| Byte | byte | uint8 | uint8 |
| Char8 | char8 | uint8 | uint8 |
| Char16 | char16 | Not Supported | Not Supported |
| Float32 | float32 | single | single |
| Float64 | float64 | double | double |
| Float128 | float128 | Not Supported | Not Supported |
| Int16 | int16 | int16 | int16 |
| Int32 | int32 | int32 | int32 |
| Int64 | int64 | int64 | int64 |
| UInt16 | uint16 | uint16 | uint16 |
| UInt32 | uint32 | uint32 | uin32 |
| UInt64 | uint64 | uint64 | uint64 |
| String8 | string | int8 | int8 |
| String16 | wstring | Not Supported | Not Supported |
| Enum | enum | MATLAB Enumeration | Simulink.Enum |
| Union | union | Not Supported | Not Supported |
| Struct | struct | Matlab struct/class | Simulink.Bus |
| Map | struct+typedef | Matlab struct/class | Simulink.Bus |
| Bitmask | enum | MATLAB Enumeration | Simulink.Enum |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">This table shows how different types match between the models. The use of n..n and 0..n multiplicities in the modeling tool is supported but will result in fixed variable sized signals in Simulink.</p><table><colgroup><col /><col /><col /><col /></colgroup><tbody><tr><td><p class="Compact">DDS for MagicDraw</p></td><td><p class="Compact">Connext DDS XML</p></td><td><p class="Compact">MATLAB Type</p></td><td><p class="Compact">Simulink Type</p></td></tr><tr><td><p>Boolean</p></td><td><p>boolean</p></td><td><p>logical</p></td><td><p>boolean</p></td></tr><tr><td><p>Byte</p></td><td><p>byte</p></td><td><p>uint8</p></td><td><p>uint8</p></td></tr><tr><td><p>Char8</p></td><td><p>char8</p></td><td><p>uint8</p></td><td><p>uint8</p></td></tr><tr><td><p>Char16</p></td><td><p>char16</p></td><td><p>Not Supported</p></td><td><p>Not Supported</p></td></tr><tr><td><p>Float32</p></td><td><p>float32</p></td><td><p>single</p></td><td><p>single</p></td></tr><tr><td><p>Float64</p></td><td><p>float64</p></td><td><p>double</p></td><td><p>double</p></td></tr><tr><td><p>Float128</p></td><td><p>float128</p></td><td><p>Not Supported</p></td><td><p>Not Supported</p></td></tr><tr><td><p>Int16</p></td><td><p>int16</p></td><td><p>int16</p></td><td><p>int16</p></td></tr><tr><td><p>Int32</p></td><td><p>int32</p></td><td><p>int32</p></td><td><p>int32</p></td></tr><tr><td><p>Int64</p></td><td><p>int64</p></td><td><p>int64</p></td><td><p>int64</p></td></tr><tr><td><p>UInt16</p></td><td><p>uint16</p></td><td><p>uint16</p></td><td><p>uint16</p></td></tr><tr><td><p>UInt32</p></td><td><p>uint32</p></td><td><p>uint32</p></td><td><p>uin32</p></td></tr><tr><td><p>UInt64</p></td><td><p>uint64</p></td><td><p>uint64</p></td><td><p>uint64</p></td></tr><tr><td><p>String8</p></td><td><p>string</p></td><td><p>int8</p></td><td><p>int8</p></td></tr><tr><td><p>String16</p></td><td><p>wstring</p></td><td><p>Not Supported</p></td><td><p>Not Supported</p></td></tr><tr><td><p>Enum</p></td><td><p>enum</p></td><td><p>MATLAB Enumeration</p></td><td><p>Simulink.Enum</p></td></tr><tr><td><p>Union</p></td><td><p>union</p></td><td><p>Not Supported</p></td><td><p>Not Supported</p></td></tr><tr><td><p>Struct</p></td><td><p>struct</p></td><td><p>Matlab struct/class</p></td><td><p>Simulink.Bus</p></td></tr><tr><td><p>Map</p></td><td><p>struct+typedef</p></td><td><p>Matlab struct/class</p></td><td><p>Simulink.Bus</p></td></tr><tr><td><p>Bitmask</p></td><td><p>enum</p></td><td><p>MATLAB Enumeration</p></td><td><p>Simulink.Enum</p></td></tr></tbody></table><p><br /></p>
````

<!--NOMAGIC_PAGE id=191936074 space=MRTCD2024xR2 version=1 -->
## PAGE 00046: Unspecified String Bounds

- page_id: `191936074`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936074/Unspecified+String+Bounds
- version_number: 1
- version_date: `2023-09-22T14:02:26.573+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.UnspecifiedStringBoundsRule

**Qualified name**: DDS::Validation::DDS_Unspecified_String_Bounds

**Description:**Type references to String must define the String Bound property. It sets the maximum length the string can be.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.UnspecifiedStringBoundsRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Unspecified_String_Bounds</p><p><strong>Description: </strong>Type references to String must define the String Bound property. It sets the maximum length the string can be.</p>
````

<!--NOMAGIC_PAGE id=191936075 space=MRTCD2024xR2 version=1 -->
## PAGE 00047: Unspecified String Bounds of Map Key

- page_id: `191936075`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936075/Unspecified+String+Bounds+of+Map+Key
- version_number: 1
- version_date: `2023-09-22T14:02:26.620+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error

**Implementation**: com.nomagic.magicdraw.dds.validation.UnspecifiedMapKeyStringBoundsRule

**Qualified name**: DDS::Validation::DDS_Unspecified_Map_Key_String_Bounds

**Description:**Maps with the key type of String must define the String Bounds property. It sets the maximum length the string can be.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error</p><p class="FirstParagraph"><strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.UnspecifiedMapKeyStringBoundsRule</p><p class="FirstParagraph"><strong>Qualified name</strong>: DDS::Validation::DDS_Unspecified_Map_Key_String_Bounds</p><p><strong>Description: </strong>Maps with the key type of String must define the String Bounds property. It sets the maximum length the string can be.</p>
````

<!--NOMAGIC_PAGE id=191936076 space=MRTCD2024xR2 version=1 -->
## PAGE 00048: Unsupported Discriminator Type

- page_id: `191936076`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936076/Unsupported+Discriminator+Type
- version_number: 1
- version_date: `2023-09-22T14:02:26.675+02:00`
- ancestors: Magic Real-Time Communication Designer > Validation Suite
- labels: []

### NORMALIZED CONTENT

**Severity**: error 
 **Implementation**: com.nomagic.magicdraw.dds.validation.UnsupportedDiscriminatorTypesRule 
 **Qualified name**: DDS::Validation::DDS_Unsupported_Discriminator_Types

**Description:**Union Cases must define discriminator values that can be parsed into their parent Union’s discriminator type. In DDS, a discriminator can either be a number or a string. A discriminator is used to differentiate at runtime the possible types of a union. Last updated 2020-10-26 16:13:23 +0100

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><strong>Severity</strong>: error<br /> <strong>Implementation</strong>: com.nomagic.magicdraw.dds.validation.UnsupportedDiscriminatorTypesRule<br /> <strong>Qualified name</strong>: DDS::Validation::DDS_Unsupported_Discriminator_Types</p><p><strong>Description: </strong>Union Cases must define discriminator values that can be parsed into their parent Union’s discriminator type. In DDS, a discriminator can either be a number or a string. A discriminator is used to differentiate at runtime the possible types of a union. Last updated 2020-10-26 16:13:23 +0100</p>
````

<!--NOMAGIC_PAGE id=191936032 space=MRTCD2024xR2 version=2 -->
## PAGE 00049: Validation

- page_id: `191936032`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936032/Validation
- version_number: 2
- version_date: `2024-10-08T09:29:18.905+02:00`
- ancestors: Magic Real-Time Communication Designer > Getting started
- labels: []

### NORMALIZED CONTENT

The validity of the DDS model is continuously checked by active validation rules contained in the DDS Validation Suite. For example, if you accidentally add multiple attributes to a Topic, an error is displayed. You can fix some of these DDS modeling problems by right-clicking on them and selecting the appropriate solver.

[IMAGE alt='' src='']

There is a separate validation suite for Simulink named DDS Simulink Validation Suite. It contains validation rules for data types that are not supported by Simulink. It can be activated independently from the rest of the rules.

The detailed descriptions of the validation rules are available in [CONFLUENCE_PAGE title='Validation Suite' space='MRTCD2024xR2'].

[CONFLUENCE_PAGE title='Validation' space='MD2024xR2']>]]>

.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><span lang="EN">The validity of the DDS model is continuously checked by active validation rules contained in the DDS Validation Suite. For example, if you accidentally add multiple attributes to a Topic, an error is displayed. You can fix some of these DDS modeling problems by right-clicking on them and selecting the appropriate solver.</span></p><p class="FirstParagraph"><span lang="EN"><ac:image><ri:attachment ri:filename="image2020-11-12_15-7-35.png"><ri:page ri:content-title="Validation" ri:space-key="MRTCD2024xR2" /></ri:attachment></ac:image></span></p><p class="FirstParagraph"><br /></p><p class="FirstParagraph"><span lang="EN"><span><span>There is a separate validation suite for Simulink named DDS Simulink Validation Suite. It contains validation rules for data types that are not supported by Simulink. It can be activated independently from the rest of the rules.</span></span></span></p><p>The detailed descriptions of the validation rules are available in <ac:link><ri:page ri:content-title="Validation Suite" ri:space-key="MRTCD2024xR2" /></ac:link>.</p><p><br /></p><p><ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Validation" /><ac:plain-text-link-body><![CDATA[Learn more about Validation >>]]></ac:plain-text-link-body></ac:link></p><p>.</p><p class="FirstParagraph"><span lang="EN"><br /></span></p><div><span style="white-space: pre-wrap;"><br /></span></div><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=191936052 space=MRTCD2024xR2 version=2 -->
## PAGE 00050: Validation Suite

- page_id: `191936052`
- space_key: `MRTCD2024xR2`
- source_url: https://docs.nomagic.com/spaces/MRTCD2024xR2/pages/191936052/Validation+Suite
- version_number: 2
- version_date: `2024-10-08T09:29:19.083+02:00`
- ancestors: Magic Real-Time Communication Designer
- labels: []

### NORMALIZED CONTENT

In this section are detailed descriptions of the validation rules, each page describing one.

The severity is either error or warning. Warning means that the state is not necessarily incorrect, but probably is. The implementation, qualified name, and abbreviation are given because those are the identifiers modeling tool provides for a validation rule, so this document is searchable by either. [CONFLUENCE_PAGE title='Validation' space='MD2024xR2']>]]>

The list of DDS validation rules:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">In this section are detailed descriptions of the validation rules, each page describing one. </p><p>The severity is either error or warning. Warning means that the state is not necessarily incorrect, but probably is. The implementation, qualified name, and abbreviation are given because those are the identifiers modeling tool provides for a validation rule, so this document is searchable by either. <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Validation" /><ac:plain-text-link-body><![CDATA[Learn more about modeling tool validation >>]]></ac:plain-text-link-body></ac:link></p><p>The list of DDS validation rules: </p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3606a106-ac5e-449f-becd-0cbba497615c" /></p>
````
