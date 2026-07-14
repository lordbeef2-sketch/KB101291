# NOMAGIC DOCUMENTATION SPACE: Magic Real-Time Communication Designer / DDS Real-Time Communication 

<!--NOMAGIC_SPACE key=MRTCD chunk=1 -->

<!--NOMAGIC_PAGE id=304014753 space=MRTCD version=1 -->
## PAGE 00001: (2026x Refresh1) Applying DDS Sterotypes

- page_id: `304014753`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014753/2026x+Refresh1+Applying+DDS+Sterotypes
- version_number: 1
- version_date: `2026-04-29T16:51:01.465+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Home Control Example
- labels: []

### NORMALIZED CONTENT

First and for most we need do define the data structures and the topics which will be used in the communication. This can easily be done with a Topic Definition diagram. [CONFLUENCE_PAGE title='(2026x Refresh1) Defining topics and types' space='']>]]>

Topics must contain exactly one property that has to be stereotyped with the TopicTypeProperty stereotype and has to be a type of either a Struct or Union.

[IMAGE alt='' src='']

###### The example defines three packages or DDS Modules for the three factor that we would like to measure and control.

Now that we have the data structures for the communication we can assign them to ports turning them into data writers and data readers in the DDS sense. [CONFLUENCE_PAGE title='(2026x Refresh1) Defining Domain Participant communication' space='']>]]>

First we need to apply the DomainParticipant stereotypes on Blocks whose instances will be used as the individual applications in the communication. [CONFLUENCE_PAGE title='(2026x Refresh1) Defining Domains and Domain Participants' space='']>]]>

[IMAGE alt='' src='']

###### The SysML BLock Definition diagram that contains all Domain Participants of Home Controller system.

After SysML model is created with the right stereotypes applied, we can define our DDS domains with them.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">First and for most we need do define the data structures and the topics which will be used in the communication. This can easily be done with a Topic Definition diagram. <ac:link><ri:page ri:content-title="(2026x Refresh1) Defining topics and types" /><ac:plain-text-link-body><![CDATA[How to define topics and types >>]]></ac:plain-text-link-body></ac:link></p><p>Topics must contain exactly one property that has to be stereotyped with the TopicTypeProperty stereotype and has to be a type of either a Struct or Union.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="topic_Definition_diagram_homeControlerSystem.png"><ri:page ri:content-title="(2026x Refresh1) Applying DDS Sterotypes" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example defines three packages or DDS Modules for the three factor that we would like to measure and control.</h6><p><br /></p><p>Now that we have the data structures for the communication we can assign them to ports turning them into data writers and data readers in the DDS sense. <ac:link><ri:page ri:content-title="(2026x Refresh1) Defining Domain Participant communication" /><ac:plain-text-link-body><![CDATA[How to define Domain Participant communication >>]]></ac:plain-text-link-body></ac:link></p><p>First we need to apply the DomainParticipant stereotypes on Blocks whose instances will be used as the individual applications in the communication. <ac:link><ri:page ri:content-title="(2026x Refresh1) Defining Domains and Domain Participants" /><ac:plain-text-link-body><![CDATA[How to define Domains and Domain Participants >>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center"><ri:attachment ri:filename="bdd_homeControlerSystem.png"><ri:page ri:content-title="(2026x Refresh1) Applying DDS Sterotypes" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The SysML BLock Definition diagram that contains all Domain Participants of Home Controller system.</h6><p><br /></p><p>After  SysML model is created with the right stereotypes applied, we can define our DDS domains with them.</p>
````

<!--NOMAGIC_PAGE id=304014732 space=MRTCD version=1 -->
## PAGE 00002: (2026x Refresh1) Creating DDS project

- page_id: `304014732`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014732/2026x+Refresh1+Creating+DDS+project
- version_number: 1
- version_date: `2026-04-29T16:51:00.869+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Getting started
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
<p>To create a blank DDS project</p><hr /><ol><li><span style="color: rgb(51,51,51);">Do one of the following:<br /> </span><ul><li><span style="color: rgb(51,51,51);">Select <strong>File </strong>&gt; <strong>New</strong> <strong>Project</strong>.</span></li><li><span style="color: rgb(51,51,51);">On the main toolbar, click the <strong>New</strong> <strong>Project</strong> button.</span></li><li><span style="color: rgb(51,51,51);">Press Ctr+Shiftl+N.</span> <span style="color: rgb(51,51,51);"> <br /> </span></li></ul></li><li class="_mce_tagged_br"><span style="color: rgb(51,51,51);">In the <strong>New</strong> <strong> Project</strong> dialog, under <strong>Systems Engineering</strong>, select <strong>DDS</strong> <strong> Project</strong>.<br /> </span></li><li><span style="color: rgb(51,51,51);">Specify name and location.</span></li><li><span style="color: rgb(51,51,51);">Click <strong>OK</strong> when you are done.<br />The blank project is created and stored in your file system with defined name.<br /> <ac:image><ri:attachment ri:filename="create_new_DDS_project_steps.png"><ri:page ri:content-title="(2026x Refresh1) Creating DDS project" /></ri:attachment></ac:image> </span></li></ol><p><span style="color: rgb(51,51,51);"> <br /> </span></p><p><span style="color: rgb(51,51,51);">Once you created the blank DDS Project, you can use for modeling already predefined Package structure as shown in the following figure.</span></p><h6 style="text-align: center;"><span style="color: rgb(51,51,51);"> <ac:image ac:align="center"><ri:attachment ri:filename="predefined_DDS_package_structure.png"><ri:page ri:content-title="(2026x Refresh1) Creating DDS project" /></ri:attachment></ac:image> </span> <br /> <span>The predefined Package structure of blank DDS project.</span></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=304014757 space=MRTCD version=2 -->
## PAGE 00003: (2026x Refresh1) Creating the domain

- page_id: `304014757`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014757/2026x+Refresh1+Creating+the+domain
- version_number: 2
- version_date: `2026-04-29T16:54:12.165+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Home Control Example
- labels: []

### NORMALIZED CONTENT

The Domain can be created by using the DDS Domain Table. As shown in the following table, the Smart Home DDS Domain is created with specified its id, topics, participants and participant instances. [How to create DDS Domain Table>>](https://docs.nomagic.com/display/MRTCD/(2026x Refresh1) Defining+Domains+and+Domain+Participants#DefiningDomainsandDomainParticipants-CreatingDomainandDomainParticipantsbyusingtheDDSDomainTable)

[IMAGE alt='' src='']

###### The example of DDS Domain Table.

The Participant Instances derived column displays all the instances that will be in the the DDS XML.Now we are ready to export the model if we desire, but first we need to assign quality of service requirements on the DDS elements.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Domain can be created by using the <span style="color: rgb(62,63,64);">DDS Domain Table. As shown in the following table, the Smart Home DDS Domain is created with specified its id, topics, participants and participant instances. <a href="https://docs.nomagic.com/display/MRTCD/(2026x Refresh1) Defining+Domains+and+Domain+Participants#DefiningDomainsandDomainParticipants-CreatingDomainandDomainParticipantsbyusingtheDDSDomainTable">How to create DDS Domain Table&gt;&gt;</a></span></p><p><span style="color: rgb(62,63,64);"><ac:image ac:align="center"><ri:attachment ri:filename="domain_table.png"><ri:page ri:content-title="(2026x Refresh1) Creating the domain" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">The example of DDS Domain Table.</span></h6><p class="auto-cursor-target"><span><span><span style="color: rgb(62,63,64);">The Participant Instances derived column displays all the instances that will be in the the DDS XML. </span>Now we are ready to export the model if we desire, but first we need to assign quality of service requirements on the DDS elements.</span><br /></span></p><p class="auto-cursor-target"><span><br /></span></p><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=304014693 space=MRTCD version=1 -->
## PAGE 00004: (2026x Refresh1) Defining Domain Participant communication

- page_id: `304014693`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014693/2026x+Refresh1+Defining+Domain+Participant+communication
- version_number: 1
- version_date: `2026-04-29T16:50:59.836+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Getting started
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
<p>Communication between DDS elements is determined by ports owned by Domain Participants. Ports that are parts of the communication has to have DDS Endpoint stereotype otherwise they will be omitted.</p><p><br /></p><p>To apply DDS Endpoint stereotype on a port</p><hr /><ol><li>Right-click the port and from the shortcut menu, select Stereotype.</li><li>In the opened dialog, select DDS Endpoint. </li><li>Click <strong>Apply</strong>.</li></ol><p><br /></p><p>The derived direction of ports determine whether they are considered Data Reader or Data Writers. In case of non-nested ports the publishers and subscribers which contain the Data Readers or Writers are implicitly defined under the Domain Participants. Publishers and Subscribers in DDS group Data Readers and Writers.</p><p>Nested ports can be used to group Data Writers and Readers. The grouping is determined by the ports highest in the hierarchy (direct children of the Block). Note that non-nested ports must have a type of Topic.</p><p><span>In between ports have no effective meaning.</span></p><p><span>In case of </span>nested ports<span>, ports highest in the hierarchy implicitly define </span>subscribers<span> and </span>publishers<span> as well.</span></p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="image2020-11-12_14-1-30.png"><ri:page ri:content-title="(2026x Refresh1) Defining Domain Participant communication" /></ri:attachment></ac:image></p><p><span><br /></span></p><p><br /></p><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=304014684 space=MRTCD version=1 -->
## PAGE 00005: (2026x Refresh1) Defining Domains and Domain Participants

- page_id: `304014684`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014684/2026x+Refresh1+Defining+Domains+and+Domain+Participants
- version_number: 1
- version_date: `2026-04-29T16:50:59.679+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Getting started
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

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MDTWRT'] , right-click a Package wherein you want to create Domain Participants or Domain.
2. From the shortcut menu, select Create Element and from the opened dialog, select DomainParticipant or Domain.
3. The unnamed element is created. Type its name and press enter. [ATTACHMENT filename='domain_participant_and_domain_in_containment_tree.png']

##### Creating Domain and Domain Participants by using the DDS Domain Table

You can use the DDS Domain Table to create a Domain inside a Domain Library. It also helps to assign Topics and Domain Participants to the Domain. The DDS Domain Table named Domain is already created in predefined DDS Package structure. If you want to create a new one, follow the procedure below.

To create an empty DDS Domain Table

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MDTWRT'] , right-click a predefined Domain Package.
2. From the shortcut menu, select Create Diagram and from the opened dialog, select DDS Domain Table.
3. The unnamed table is created. Type its name and press enter.

To fill in the DDS Domain Table

1. From the table toolbar, click the Add New button. The new row appears and DDSDomain element is created in the model.
2. In the table, specify the following: 
 - Double-click **Name** cell and type a domain name. 
 - Double-click the **Domain_id** cell and type domain id number. 
 - Double-click the **Topics** cell, select [IMAGE alt='' src=''] and in the **Select Elements** dialog choose already created topics or use the **Creation Mode** to create new topics. Topics referenced by a Domain Participants must be assigned to every Domain that the participant is assigned to. Unassigned Topics lead to validation errors. - Double-click the **Participants** cell, select [IMAGE alt='' src=''] and in the **Select Elements** dialog choose already created Domain Participants or use the **Creation Mode** to create new Domain Participants. 
 - The **Participant Instances** column fill in automatically when instances are created in the model. >]]>[CONFLUENCE_PAGE title='(2026x Refresh1) Defining Domains and Domain Participants' space=''] 
[IMAGE alt='' src='']

##### Creating Domain Participants by refactoring the Block

To create a Domain Participant or Domain by refactoring a Block

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MDTWRT'] , right-click a Package wherein you want to create Domain Participants or Domain.
2. From the shortcut menu, select Create Element and from the opened dialog, select Block.
3. Right-click the Block and select Refactor > Convert To > More Specific > Domain Participant or Domain . The Block is refactored to the Domain Participant or Domain.

[IMAGE alt='' src='']

##### Creating instances

The difference between instances of Domain Participants and Members of DDS Data types are the following:

- Domain Participant instances: are any Block property typed by Domain Participant. They can be any kid of property: Value Property, Part Property, Reference Property etc. 
 - Members: DDS Data type Members are used in the data definition section of the meta-model. They allow to define custom, DDS annotated data types. They rely heavily on multiplicity definitions in order to be able to produce a syntactically correct DDS xml output.

To create a Domain Participant instances

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MDTWRT'] , right-click a Block which will be the owner of the instances.
2. From the shortcut menu, select Create Diagram and from the opened dialog, select SysML Internal Block Diagram.
3. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] select a property (e.g. Part Property) and click on the diagram pane.
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

1. Double-click the Part Property to open it's [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] .
2. Select the Multiplicity property value or type Lower Value and Upper Value.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>All Domain Participants are assigned to the Domain regardless of where they are in the containment hierarchy. Domain Participants should have at least one instance which can be any kind of lock property typed by Domain Participant. During DDS XML generation, all properties of the Block are considered a Domain Participants.</p><p>You can create Domain and Domain Participants by using:</p><ul><li>The Containment tree.</li><li>DDS Domain Table.</li></ul><p>This page contains the following topics:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="e20bb792-47ca-49f9-8f77-b9d92eb13d0b"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p><div><p><br /></p><h3>Creating Domain and Domain Participants by using the Containment tree</h3><p><br /></p><p>To create a Domain Participant or Domain in the Containment tree</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a Package wherein you want to create Domain Participants or Domain.</li><li>From the shortcut menu, select <strong>Create Element </strong>and from the opened dialog, select DomainParticipant or Domain.</li><li>The unnamed element is created. Type its name and press enter.<br /><ac:image><ri:attachment ri:filename="domain_participant_and_domain_in_containment_tree.png"><ri:page ri:content-title="(2026x Refresh1) Defining Domains and Domain Participants" /></ri:attachment></ac:image></li></ol><h3>Creating Domain and Domain Participants by using the DDS Domain Table</h3><p>You can use the DDS Domain Table to create a Domain inside a Domain Library. It also helps to assign Topics and Domain Participants to the Domain. The DDS Domain Table named Domain is already created in predefined DDS Package structure. If you want to create a new one, follow the procedure below.</p><p>To create an empty DDS Domain Table</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a predefined <em>Domain</em> Package.</li><li>From the shortcut menu, select <strong>Create Diagram </strong>and from the opened dialog, select DDS Domain Table.</li><li>The unnamed table is created. Type its name and press enter.</li></ol><p><br /></p><p>To fill in the DDS Domain Table</p><hr /><ol><li>From the table toolbar, click the <strong>Add New</strong> button. The new row appears and DDSDomain element is created in the model.</li><li><p class="auto-cursor-target">In the table, specify the following:<br /> - Double-click <strong>Name</strong> cell and type a domain name.<br /> - Double-click the <strong>Domain_id</strong> cell and type domain id number.<br /> - Double-click the <strong>Topics</strong> cell, select <ac:image ac:title="Edit" ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="(2026x Refresh1) Defining Domains and Domain Participants" /></ri:attachment></ac:image> and in the <strong>Select Elements</strong> dialog choose already created topics or use the <strong>Creation Mode</strong> to create new topics.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="ccea59d8-2dd6-47db-a1e2-75bba1a8ff67"><ac:rich-text-body><p>Topics referenced by a Domain Participants must be assigned to every Domain that the participant is assigned to. Unassigned Topics lead to validation errors.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"> - Double-click the <strong>Participants</strong> cell, select <ac:image ac:title="Edit" ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="(2026x Refresh1) Defining Domains and Domain Participants" /></ri:attachment></ac:image> and in the <strong>Select Elements</strong> dialog choose already created Domain Participants or use the <strong>Creation Mode</strong> to create new Domain Participants.<br /> - The <strong>Participant Instances</strong> column fill in automatically when instances are created in the model. <ac:link ac:anchor="Creating instances of Domain Participants"><ac:plain-text-link-body><![CDATA[How to create Participant Instances >>]]></ac:plain-text-link-body><ri:page ri:content-title="(2026x Refresh1) Defining Domains and Domain Participants" /></ac:link><br /><ac:image><ri:attachment ri:filename="DDSDomain_table.png"><ri:page ri:content-title="(2026x Refresh1) Defining Domains and Domain Participants" /></ri:attachment></ac:image></p></li></ol><h3>Creating Domain Participants by refactoring the Block</h3><p><br /></p><p>To create a Domain Participant or Domain by refactoring a Block</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a Package wherein you want to create Domain Participants or Domain.</li><li>From the shortcut menu, select <strong>Create Element </strong>and from the opened dialog, select Block.</li><li>Right-click the Block and select <strong>Refactor</strong> &gt; <strong>Convert To</strong> &gt; <strong>More Specific</strong> &gt; <strong>Domain Participant</strong> or <strong>Domain</strong>.<br />The Block is refactored to the Domain Participant or Domain.</li></ol><p><ac:image><ri:attachment ri:filename="Block_refactor_to_domain_participant.png"><ri:page ri:content-title="(2026x Refresh1) Defining Domains and Domain Participants" /></ri:attachment></ac:image></p><h3>Creating instances </h3><p>The difference between instances of Domain Participants and Members of DDS Data types are the following:</p><p>   - Domain Participant instances: are any Block property typed by Domain Participant. They can be any kid of property: Value Property, Part Property, Reference Property etc.<br />    - Members: DDS Data type Members are used in the data definition section of the meta-model. They allow to define custom, DDS annotated data types. They rely heavily on multiplicity definitions in order to be able to produce a syntactically correct DDS xml output.<br /><br /></p><p>To create a Domain Participant instances</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a Block which will be the owner of the instances.</li><li>From the shortcut menu, select <strong>Create Diagram </strong>and from the opened dialog, select SysML Internal Block Diagram.</li><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram palette]]></ac:plain-text-link-body></ac:link> select a property (e.g. Part Property) and click on the diagram pane.</li><li>Type the name of the property.</li><li>Select a Domain Participant as type of the property.<br />The instance of Domain Participant is created.<br /><br /><ac:image><ri:attachment ri:filename="instances_of_domain_participants.png"><ri:page ri:content-title="(2026x Refresh1) Defining Domains and Domain Participants" /></ri:attachment></ac:image></li></ol><h3>Defining instances multiplicity</h3></div><p>To define a instances as an array or sequence, its multiplicity needs to be changed as it follows, where N must be at least 1 and M must be greater than N.</p><table><colgroup><col /><col /><col /><col /><col /></colgroup><tbody><tr><td colspan="2"><p class="Compact"><strong>Lower Value</strong></p></td><td><p class="Compact"><strong>Upper Value</strong></p></td><td><p class="Compact"><strong>Multiplicity</strong></p></td><td><p class="Compact"><strong>Type</strong></p></td></tr><tr><td colspan="2"><p>N</p></td><td><p>N</p></td><td><p>N</p></td><td><p>Array</p></td></tr><tr><td colspan="2"><p>0</p></td><td><p>-1</p></td><td><p>0 .. *</p></td><td><p>Boundless Array</p></td></tr><tr><td colspan="2"><p>0</p></td><td><p>N-1</p></td><td><p>0 .. N-1</p></td><td><p>Sequence</p></td></tr><tr><td colspan="2"><p>N</p></td><td><p>M</p></td><td><p>N .. M</p></td><td><p>Sequence</p></td></tr></tbody></table><p><br /></p><p>To change the instance multiplicity</p><hr /><ol><li>Double-click the Part Property to open it's <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>.</li><li>Select the Multiplicity property value or type Lower Value and Upper Value.</li></ol><p><ac:image><ri:attachment ri:filename="members_multiplicity.png"><ri:page ri:content-title="(2026x Refresh1) Defining Domains and Domain Participants" /></ri:attachment></ac:image></p><p class="Compact"><br /></p>
````

<!--NOMAGIC_PAGE id=304014743 space=MRTCD version=1 -->
## PAGE 00006: (2026x Refresh1) Defining topics and types

- page_id: `304014743`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014743/2026x+Refresh1+Defining+topics+and+types
- version_number: 1
- version_date: `2026-04-29T16:51:01.173+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Getting started
- labels: ['define-topics', 'define-types', 'create-dds-topic-definition-diagram']

### NORMALIZED CONTENT

You can define topic and types used by them in the DDS Topic Definition Diagram.

[IMAGE alt='' src='']

###### The example of the DDS Topic Definition Diagram where main elements are highlighed: DDS Module, Types and Topic.

##### Creating DDS Topic Definition Diagram

After a blank DDS Project is created, the predefined package structure is prepared where the DDS Topic Definition Diagram is already created under the *Topics* Package named *Topics*. It contains an empty DDS Module. If you need another one, create it manually, as described in the following procedure.

To create blank DDS Topic Definition Diagram

1. In the [CONFLUENCE_PAGE title='Model Browser' space='MDTWRT'] , select the owner for the new diagram.
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

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select a type you need and click on DDS Module element.
2. Type its name.
3. Click the Create Member [CONFLUENCE_PAGE title='Smart manipulators' space='MDTWRT'] to create a Members for the type.
4. Select newly created Member on the shape, click [ATTACHMENT filename='specify_type.png'] and select a type for a it.

Creating and defining topics

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select a Topic and click on the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] .
2. Type its name.
3. Click the Create Element [CONFLUENCE_PAGE title='Smart manipulators' space='MDTWRT'] to create a Topic Type Property or Reception for the Topic.
4. Select newly created Topic Type Property or Reception, click [IMAGE alt='' src='']and select a type for a it. Press Ctrl+Space to search among the available types.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can define topic and types <span style="color: rgb(62,63,64);">used by them</span> in the DDS Topic Definition Diagram.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="DDS_Topic_Definition_Diagram.png"><ri:page ri:content-title="(2026x Refresh1) Defining topics and types" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example of the DDS Topic Definition Diagram where main elements are highlighed: DDS Module, Types and Topic.</h6><h3>Creating DDS Topic Definition Diagram</h3><p>After a blank DDS Project is created, the predefined package structure is prepared where the DDS Topic Definition Diagram is already created under the <em>Topics</em> Package named <em>Topics</em>. It contains an empty DDS Module. If you need another one, create it manually, as described in the following procedure.</p><p>To create blank DDS Topic Definition Diagram</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Model Browser" /></ac:link>, select the owner for the new diagram.</li><li>Do one of the following:<br /><ul><li>Right-click the Package, and from the shortcut menu select <strong>Create Diagram.</strong></li><li>Press Ctrl+N.</li><li>On the main toolbar, click <span class="confluence-embedded-file-wrapper"><ac:image ac:alt="Create Diagram"><ri:attachment ri:filename="create_diagram.png"><ri:page ri:content-title="(2026x Refresh1) Defining topics and types" /></ri:attachment></ac:image></span> .</li><li>From the main menu, select <strong>Diagrams</strong> &gt; <strong>Create Diagram</strong>.</li></ul></li><li><p>In the <strong>Create Diagram</strong> box, under <strong>General</strong> diagram group, select the <strong>DDS Topic Definition Diagram</strong>.</p></li></ol><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="8fa80951-960a-4327-aedd-357ca62fe7c8"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">Press Esc or click outside the dialog to close the diagram creation dialog without creating the diagram.</span></p></ac:rich-text-body></ac:structured-macro><h3>Defining topics and types</h3><p>You can create the following types:</p><ul><li>Struct Type</li><li>Union Type</li><li>Bitmask Type</li><li>Enumeration Type</li><li>Map Type</li><li>Alias Type</li><li>Annotation Type</li></ul><p><br /></p><p>Creating and defining types</p><hr /><ol><li>From the<ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[ diagram palette]]></ac:plain-text-link-body></ac:link>, select a type you need and click on DDS Module element. </li><li>Type its name.</li><li>Click the <strong>Create Member</strong> <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Smart manipulators" /><ac:plain-text-link-body><![CDATA[smart manipulator]]></ac:plain-text-link-body></ac:link> to create a Members for the type.</li><li>Select newly created Member on the shape, click <ac:image ac:title="Specify Type" ac:alt="Specify Type"><ri:attachment ri:filename="specify_type.png"><ri:page ri:content-title="(2026x Refresh1) Defining topics and types" /></ri:attachment></ac:image> and select a type for a it.</li></ol><p><br /></p><p>Creating and defining topics</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram palette]]></ac:plain-text-link-body></ac:link>, select a Topic and click on the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram pane]]></ac:plain-text-link-body></ac:link>. </li><li>Type its name.</li><li>Click the <strong>Create Element</strong> <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Smart manipulators" /><ac:plain-text-link-body><![CDATA[smart manipulator]]></ac:plain-text-link-body></ac:link> to create a Topic Type Property or Reception for the Topic.</li><li><p class="auto-cursor-target">Select newly created Topic Type Property or Reception, click <ac:image ac:title="Specify Type" ac:alt="Specify Type"><ri:attachment ri:filename="specify_type.png"><ri:page ri:content-title="(2026x Refresh1) Defining topics and types" /></ri:attachment></ac:image>and select a type for a it.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="f4ba630b-5037-4766-aa0d-f65b82385bbb"><ac:rich-text-body><p>Press Ctrl+Space to search among the available types.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><br /></p><p class="Compact">              </p><p class="Compact"><br /></p>
````

<!--NOMAGIC_PAGE id=304014765 space=MRTCD version=1 -->
## PAGE 00007: (2026x Refresh1) Domain not in Library

- page_id: `304014765`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014765/2026x+Refresh1+Domain+not+in+Library
- version_number: 1
- version_date: `2026-04-29T16:51:01.832+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014767 space=MRTCD version=1 -->
## PAGE 00008: (2026x Refresh1) Domain Participant without Instance

- page_id: `304014767`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014767/2026x+Refresh1+Domain+Participant+without+Instance
- version_number: 1
- version_date: `2026-04-29T16:51:01.902+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014769 space=MRTCD version=1 -->
## PAGE 00009: (2026x Refresh1) Duplicate Domain ID

- page_id: `304014769`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014769/2026x+Refresh1+Duplicate+Domain+ID
- version_number: 1
- version_date: `2026-04-29T16:51:01.980+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014771 space=MRTCD version=1 -->
## PAGE 00010: (2026x Refresh1) Endpoint not Referenced

- page_id: `304014771`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014771/2026x+Refresh1+Endpoint+not+Referenced
- version_number: 1
- version_date: `2026-04-29T16:51:02.068+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014723 space=MRTCD version=1 -->
## PAGE 00011: (2026x Refresh1) Environment setup

- page_id: `304014723`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014723/2026x+Refresh1+Environment+setup
- version_number: 1
- version_date: `2026-04-29T16:51:00.577+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Simulation with Simulink
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

<!--NOMAGIC_PAGE id=304014750 space=MRTCD version=1 -->
## PAGE 00012: (2026x Refresh1) Example Model

- page_id: `304014750`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014750/2026x+Refresh1+Example+Model
- version_number: 1
- version_date: `2026-04-29T16:51:01.365+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Home Control Example
- labels: []

### NORMALIZED CONTENT

HomeControler.mdzip contains a model that describes a system that consists of an air conditioner unit, a dehumidifiers, shutters and a light sensor. The air conditioner and the dehumidifier both contain a controller and a sensor component. The system is supervised by the Home Controller whose main responsibility is to monitor data received from the components and to control them.

[IMAGE alt='' src='']

###### The SysmL Internal Block Diagram of Home Controller environment.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">HomeControler.mdzip contains a model that describes a system that consists of an air conditioner unit, a dehumidifiers, shutters and a light sensor. The air conditioner and the dehumidifier both contain a controller and a sensor component. The system is supervised by the Home Controller whose main responsibility is to monitor data received from the components and to control them.</p><p class="FirstParagraph"><ac:image ac:align="center"><ri:attachment ri:filename="ibd_homeControlerSystem.png"><ri:page ri:content-title="(2026x Refresh1) Example Model" /></ri:attachment></ac:image></p><h6 class="FirstParagraph" style="text-align: center;">The SysmL Internal Block Diagram of Home Controller environment.</h6>
````

<!--NOMAGIC_PAGE id=304014763 space=MRTCD version=2 -->
## PAGE 00013: (2026x Refresh1) Exporting DDS Control Example to XML

- page_id: `304014763`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014763/2026x+Refresh1+Exporting+DDS+Control+Example+to+XML
- version_number: 2
- version_date: `2026-04-29T16:54:12.257+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Home Control Example
- labels: []

### NORMALIZED CONTENT

You can export the DDS examples to XML. For this, follow the procedures provided in the page [Exporting DDS XML](https://docs.nomagic.com/display/MRTCD/(2026x Refresh1) Exporting+DDS+XML).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can export the DDS examples to XML. For this, follow the procedures provided in the page <a class="current" style="letter-spacing: 0.0px;" href="https://docs.nomagic.com/display/MRTCD/(2026x Refresh1) Exporting+DDS+XML">Exporting DDS XML</a>.</p><p><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=304014703 space=MRTCD version=1 -->
## PAGE 00014: (2026x Refresh1) Exporting DDS XML

- page_id: `304014703`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014703/2026x+Refresh1+Exporting+DDS+XML
- version_number: 1
- version_date: `2026-04-29T16:50:59.997+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Getting started
- labels: ['generate-dds-xml']

### NORMALIZED CONTENT

You can generate DDS xml file directly from the modeling tool. Referenced QoS profiles are included in the resulting XML. Before the export a pre-check is initiated to ensure that the QoS Profiles imported to modeling tool were not changed and still up to date. You can use the resulting XML in the **RTI DDS Code Generator**, **RTI System Designer**, the **DDS Simulink Tooling** or other standards-compliant tool.

To generate DDS XML

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select Tools > DDS > Generate DDS XML .
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
<p>You can generate DDS xml file directly from the modeling tool. Referenced QoS profiles are included in the resulting XML. Before the export a pre-check is initiated to ensure that the QoS Profiles imported to modeling tool were not changed and still up to date. You can use the resulting XML in the <strong style="letter-spacing: 0.0px;">RTI DDS Code Generator</strong>, <strong style="letter-spacing: 0.0px;">RTI System Designer</strong>, the <strong style="letter-spacing: 0.0px;">DDS Simulink Tooling</strong> or other standards-compliant tool.</p><p><br /></p><p>To generate DDS XML</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main menu]]></ac:plain-text-link-body></ac:link>, select <strong>Tools </strong>&gt; <strong>DDS</strong> &gt; <strong>Generate DDS XML</strong>.</li><li>In the <strong style="letter-spacing: 0.0px;">Generate DDS XML</strong><span style="letter-spacing: 0.0px;"> dialog, select the following:</span><span style="letter-spacing: 0.0px;"><br /></span></li></ol><p class="auto-cursor-target"> -<strong> Select Scope</strong> - select a Package which content you want to export. Click <strong>Next</strong>.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="72fbaaef-7a44-4b88-9f40-a83af6e3bbaa"><ac:rich-text-body><p><span>To ensure that the exported XML is valid, make sure the selected package contains at least one domain participant library containing at least one Domain Participant. Otherwise, the tool takes care of the validity of references by including the elements referred from the selected package even if they are outside the selected Package.</span></p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="select_scope.png"><ri:page ri:content-title="(2026x Refresh1) Exporting DDS XML" /></ri:attachment></ac:image></p><p class="auto-cursor-target"> - <strong>Select target version</strong> - select DDS target version. Click <strong>Next</strong>.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="75827afe-6c50-4001-a769-860dc4e01ba3"><ac:rich-text-body><p>QoS Profiles between versions are not compatible. QoS Profiles with a version that is not matching with the target version selected it the wizard will prevent the export.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="select_target_version.png"><ri:page ri:content-title="(2026x Refresh1) Exporting DDS XML" /></ri:attachment></ac:image><br /> - <strong>Select output directory</strong> - select the location of exported DDS XML file. Click <strong>Finish</strong>.<br /><br /><ac:image><ri:attachment ri:filename="select_output_directory.png"><ri:page ri:content-title="(2026x Refresh1) Exporting DDS XML" /></ri:attachment></ac:image><br />The DDS XML file is generated.</p><p><br /><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=304014725 space=MRTCD version=1 -->
## PAGE 00015: (2026x Refresh1) Generating the Simulink model

- page_id: `304014725`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014725/2026x+Refresh1+Generating+the+Simulink+model
- version_number: 1
- version_date: `2026-04-29T16:51:00.629+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Simulation with Simulink
- labels: []

### NORMALIZED CONTENT

After the initialization step you can generate Simulink models using the LoadSimulinkModel.m script.

To generate the Simulink models

1. Run LoadSimulinkModel.
2. Select the desired xml you want to generate from. The xml gets copied to the matlab workspace, and the generation starts. After the generation finishes (assuming that you used the example Thermostat.xml) the workspace should look like this: [ATTACHMENT filename='image2020-11-12_15-12-49.png']
3. Open <your_model>.slx.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">After the initialization step you can generate Simulink models using the LoadSimulinkModel.m script.</p><p class="FirstParagraph"><br /></p><p class="FirstParagraph">To generate the Simulink models</p><hr /><ol><li>Run LoadSimulinkModel.</li><li>Select the desired xml you want to generate from. The xml gets copied to the matlab workspace, and the generation starts. After the generation finishes (assuming that you used the example Thermostat.xml) the workspace should look like this:<br /><ac:image><ri:attachment ri:filename="image2020-11-12_15-12-49.png"><ri:page ri:content-title="(2026x Refresh1) Generating the Simulink model" /></ri:attachment></ac:image></li><li>Open &lt;your_model&gt;.slx.</li></ol><p class="FirstParagraph"><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=304014682 space=MRTCD version=1 -->
## PAGE 00016: (2026x Refresh1) Getting started

- page_id: `304014682`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014682/2026x+Refresh1+Getting+started
- version_number: 1
- version_date: `2026-04-29T16:50:59.648+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: []

### NORMALIZED CONTENT

**Welcome!**This user guide will walk you through the basics of using DDS Real-Time Communication Plugin, including working with projects, setting up the modeling environment, defining DDS elements, importing and exporting XML files, and more.

Use the search box to find a specific topic or select one from the list below:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Welcome!</strong><span style="color: rgb(62,63,64);"> This user guide will walk you through the basics of using DDS Real-Time Communication Plugin, including working with projects, setting up the modeling environment</span><span style="color: rgb(62,63,64);">, defining DDS elements, importing and exporting XML files, and more.</span></p><p><span style="color: rgb(62,63,64);">Use the search box to find a specific topic or select one from the list below</span><span class="confluence-link" style="color: rgb(62,63,64);">:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="60201284-9a7d-44b0-812b-445cfcf90c54" /></p>
````

<!--NOMAGIC_PAGE id=304014730 space=MRTCD version=1 -->
## PAGE 00017: (2026x Refresh1) Home Control Example

- page_id: `304014730`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014730/2026x+Refresh1+Home+Control+Example
- version_number: 1
- version_date: `2026-04-29T16:51:00.813+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: []

### NORMALIZED CONTENT

The aim of this example is to demonstrate how to make models using DDS and SysML semantics, how to assign quality of service profiles. Also it provides information how to generate RTI Connext DDS model in XML format that can be used in various ways like for the RTI Connext code generator or for generating MATLAB Simulink models.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><span lang="EN">The aim of this example is to demonstrate how to make models using DDS and SysML semantics, how to assign quality of service profiles. Also it provides information how to generate RTI Connext DDS model in XML format that can be used in various ways like for the RTI Connext code generator or for generating MATLAB Simulink models.</span></p><p class="FirstParagraph"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="cfb9a75d-74f0-4ba6-97ca-91ec209cd98e" /></p>
````

<!--NOMAGIC_PAGE id=304014773 space=MRTCD version=1 -->
## PAGE 00018: (2026x Refresh1) Illegal Inheritance

- page_id: `304014773`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014773/2026x+Refresh1+Illegal+Inheritance
- version_number: 1
- version_date: `2026-04-29T16:51:02.152+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014736 space=MRTCD version=1 -->
## PAGE 00019: (2026x Refresh1) Importing DDS Profile and DDS Style in Other Projects

- page_id: `304014736`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014736/2026x+Refresh1+Importing+DDS+Profile+and+DDS+Style+in+Other+Projects
- version_number: 1
- version_date: `2026-04-29T16:51:00.987+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Getting started
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
<p class="FirstParagraph">The created DDS projects already have the DDS profile imported and DDS Style set. You ca reuse them in non-DDs projects. </p><p class="FirstParagraph"><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="3c27f29d-5174-4870-87d5-2a8fd1589241" /></p><h3 class="FirstParagraph">Reusing the DDS profile in non-DDS projects</h3><p class="FirstParagraph">Reusing the DDS profile in non-DDS projects</p><hr /><ol><li class="FirstParagraph">Open a non-DDS project in which you want to reuse the DDS profile.</li><li class="FirstParagraph">On the main menu, select <strong>File</strong> &gt; <strong>Use Project</strong> &gt; <strong>Use Local Project.</strong></li><li class="FirstParagraph">In the opened <strong>Use Project</strong> dialog, you can select the DDS profile either: <br /> - From predefined location. Select the <strong>Paths to used projects</strong>: &lt;install.root&gt;\profiles and from the list below, select the <em>dds_profile.mdzip</em>.<br /> - From File system. Click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="three_dot_button.png"><ri:page ri:content-title="(2026x Refresh1) Importing DDS Profile and DDS Style in Other Projects" /></ri:attachment></ac:image> and from the product install folder, select <em>profiles/dds_profile.mdzip</em>. Click <strong>Open</strong>.</li><li class="FirstParagraph">Click <strong>Next</strong> &gt; <strong>Finish</strong>.<br />The DDS profile is used in the project.<br /><ac:image><ri:attachment ri:filename="using_dds_profile_in_other_projects.png"><ri:page ri:content-title="(2026x Refresh1) Importing DDS Profile and DDS Style in Other Projects" /></ri:attachment></ac:image></li></ol><h3 class="FirstParagraph">Reusing the DDS Style in non-DDS projects</h3><p class="FirstParagraph">Reusing the DDS Style in non-DDS projects</p><hr /><ol><li class="FirstParagraph">Open a non-DDS project in which you want to reuse the DDS Style.</li><li>On the main menu, select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li>In the <strong>Project Options</strong> dialog, select the <strong>Symbol Style </strong>property group.</li><li>On the right side of the dialog, click the <strong>Import</strong> button, and from the product install folder, select <em>templates/DDSStyle.stl</em>. Click <strong>Open</strong>.</li><li>Select the <strong>DDSSyle</strong> from the Symbol Styles list.</li><li>Click <strong>OK</strong>.<br />The DDS Style is used in the project.<br /><br /><ac:image><ri:attachment ri:filename="selecting_ddsStyle_in_other_projects.png"><ri:page ri:content-title="(2026x Refresh1) Importing DDS Profile and DDS Style in Other Projects" /></ri:attachment></ac:image></li></ol>
````

<!--NOMAGIC_PAGE id=304014713 space=MRTCD version=1 -->
## PAGE 00020: (2026x Refresh1) Importing DDS XML

- page_id: `304014713`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014713/2026x+Refresh1+Importing+DDS+XML
- version_number: 1
- version_date: `2026-04-29T16:51:00.251+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Getting started
- labels: ['import-dds-models-in-xml-format']

### NORMALIZED CONTENT

You can also import already existing DDS models in XML format. The imported model does not contain the diagrams associated with the models. You can use modeling tool diagram initialization to make and customize your diagrams very easily however.

To import DDS models in XML format

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select Tools > DDS > Import DDS XML.
2. In the Select DDS XML file dialog, select the DDS XML file.
3. Click Import DDS .
4. In the opened **Select Package** dialog, select the Package from the model wherein the file will be imported. 
The model defined in the XML is imported. As example see the figure below. QoS Profilescontained by the same file will not be imported. For this, you have to use the [CONFLUENCE_PAGE title='(2026x Refresh1) Importing QoS Profile' space=''] to import them.

[IMAGE alt='' src='']

###### The XML file content imported into model.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can also import already existing DDS models in XML format. The imported model does not contain the diagrams associated with the models. You can use modeling tool diagram initialization to make and customize your diagrams very easily however.</p><p>To import DDS models in XML format</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main menu]]></ac:plain-text-link-body></ac:link>, select <strong>Tools</strong> &gt; <strong>DDS</strong> &gt; <strong>Import DDS XML.</strong></li><li>In the <strong>Select DDS XML file</strong> dialog, select the DDS XML file.</li><li>Click <strong>Import DDS</strong>.</li><li><p class="auto-cursor-target">In the opened <strong style="letter-spacing: 0.0px;">Select Package</strong> dialog, select the Package from the model wherein the file will be imported.<br />The model defined in the XML is imported. As example see the figure below.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="a0a739d2-8e24-4780-9d6a-b6d2956620e0"><ac:rich-text-body><p>QoS Profiles<span> contained by the same file will not be imported. For this, you have to use the <ac:link><ri:page ri:content-title="(2026x Refresh1) Importing QoS Profile" /><ac:plain-text-link-body><![CDATA[Import QoS Profile feature]]></ac:plain-text-link-body></ac:link> to import them.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p class="auto-cursor-target"><ac:image ac:align="center"><ri:attachment ri:filename="importing_xml.png"><ri:page ri:content-title="(2026x Refresh1) Importing DDS XML" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The XML file content imported into model.</h6>
````

<!--NOMAGIC_PAGE id=304014708 space=MRTCD version=1 -->
## PAGE 00021: (2026x Refresh1) Importing QoS Profile

- page_id: `304014708`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014708/2026x+Refresh1+Importing+QoS+Profile
- version_number: 1
- version_date: `2026-04-29T16:51:00.099+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Getting started
- labels: ['import-qos-profile', 'reimport-qos']

### NORMALIZED CONTENT

You can import your already existing QoS Profiles in DDS XML format created with e.g. RTI System Designer, as shown in figure below.

[IMAGE alt='' src='']

To import QoS Profile

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select Tools > DDS > Import QoS Profile .
2. In the Select DDS XML file containing QoS libraries dialog, select QoS Profile.
3. Click Import QoS .
4. In the opened Select Package dialog, select the Package from the model wherein the profile will be imported.

[IMAGE alt='' src='']

If you modify the original QoS definition file, you can reimport it. Note, that the existing QoS Profiles will be replaced, so you will have to restore their assignments manually.

To reimport QoS

- Right-click the imported*UserQosRepository*element and from the shortcut menu, select the **Reimport QoS Profile**. [IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can import your already existing QoS Profiles in DDS XML format created with e.g. RTI System Designer, as shown in figure below.</p><p><ac:image><ri:attachment ri:filename="image2020-11-12_14-57-57.png"><ri:page ri:content-title="(2026x Refresh1) Importing QoS Profile" /></ri:attachment></ac:image></p><p><br /></p><p>To import QoS Profile</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main menu]]></ac:plain-text-link-body></ac:link>, select <strong>Tools</strong> &gt; <strong>DDS</strong> &gt; <strong>Import QoS Profile</strong>.</li><li>In the <strong>Select DDS XML file containing QoS libraries</strong> dialog, select QoS Profile.</li><li>Click <strong>Import QoS</strong>.</li><li>In the opened <strong>Select Package</strong> dialog, select the Package from the model wherein the profile will be imported.</li></ol><p><ac:image><ri:attachment ri:filename="Import_QoS_Profile.png"><ri:page ri:content-title="(2026x Refresh1) Importing QoS Profile" /></ri:attachment></ac:image><span style="letter-spacing: 0.0px;"><br /></span></p><p><span style="letter-spacing: 0.0px;"><br /></span></p><p><span style="letter-spacing: 0.0px;">If you modify the original QoS definition file, you can reimport it. Note, that t<span>he existing QoS Profiles will be replaced, so you will have to restore their assignments manually.</span></span></p><p><span style="letter-spacing: 0.0px;"><span style="letter-spacing: 0.0px;">To reimport QoS</span><br /></span></p><hr /><ul><li><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;">Right-click the imported </span><em style="letter-spacing: 0.0px;">UserQosRepository</em><span style="letter-spacing: 0.0px;"> element and from the shortcut menu, select the <strong>Reimport QoS Profile</strong>. <br /></span></p><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;"><ac:image><ri:attachment ri:filename="reimport_QoS_profile.png"><ri:page ri:content-title="(2026x Refresh1) Importing QoS Profile" /></ri:attachment></ac:image><br /></span></p></li></ul>
````

<!--NOMAGIC_PAGE id=304014775 space=MRTCD version=1 -->
## PAGE 00022: (2026x Refresh1) Incompatible Base Extendibility

- page_id: `304014775`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014775/2026x+Refresh1+Incompatible+Base+Extendibility
- version_number: 1
- version_date: `2026-04-29T16:51:02.236+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014721 space=MRTCD version=1 -->
## PAGE 00023: (2026x Refresh1) Install for simulation

- page_id: `304014721`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014721/2026x+Refresh1+Install+for+simulation
- version_number: 1
- version_date: `2026-04-29T16:51:00.517+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Simulation with Simulink
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

<!--NOMAGIC_PAGE id=304014728 space=MRTCD version=1 -->
## PAGE 00024: (2026x Refresh1) Installation

- page_id: `304014728`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014728/2026x+Refresh1+Installation
- version_number: 1
- version_date: `2026-04-29T16:51:00.734+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: ['installing-dds-plugin', 'install-dds-plugin']

### NORMALIZED CONTENT

Before installing Connext DDS for MagicDraw, first install RTI Connext DDS by following the instructions in its [Getting Started guide](https://www.rti.com/gettingstarted).

To install Connext DDS for MagicDraw

1. Install [CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='MDTWRT'] .
2. Install [CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='SYSMLPTWRT'] .
3. Start MagicDraw.
4. On the main menu, click Help > Resource/Plugin Manager .
5. Click Import and select the Connext DDS for MagicDraw plugin archive ( connext-dds-magicdraw-plugin.zip ).
6. After the successful installation, restart the MagicDraw.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">Before installing Connext DDS for MagicDraw, first install RTI Connext DDS by following the instructions in its <a href="https://www.rti.com/gettingstarted">Getting Started guide</a>.</p><p>To install Connext DDS for MagicDraw</p><hr /><ol><li>Install <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[MagicDraw]]></ac:plain-text-link-body></ac:link>.</li><li>Install <ac:link><ri:page ri:space-key="SYSMLPTWRT" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[SysML plugin]]></ac:plain-text-link-body></ac:link>.</li><li>Start MagicDraw.</li><li>On the main menu, click <strong>Help</strong> &gt; <strong>Resource/Plugin Manager</strong>. </li><li>Click <strong>Import</strong> and select the <em>Connext DDS for MagicDraw plugin</em> archive (<em>connext-dds-magicdraw-plugin.zip</em>).</li><li>After the successful installation, restart the MagicDraw.</li></ol>
````

<!--NOMAGIC_PAGE id=304014777 space=MRTCD version=1 -->
## PAGE 00025: (2026x Refresh1) Instance not Participant

- page_id: `304014777`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014777/2026x+Refresh1+Instance+not+Participant
- version_number: 1
- version_date: `2026-04-29T16:51:02.312+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014779 space=MRTCD version=1 -->
## PAGE 00026: (2026x Refresh1) Invalid Member Multiplicity

- page_id: `304014779`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014779/2026x+Refresh1+Invalid+Member+Multiplicity
- version_number: 1
- version_date: `2026-04-29T16:51:02.397+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014781 space=MRTCD version=1 -->
## PAGE 00027: (2026x Refresh1) Invalid Member Type

- page_id: `304014781`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014781/2026x+Refresh1+Invalid+Member+Type
- version_number: 1
- version_date: `2026-04-29T16:51:02.485+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014783 space=MRTCD version=1 -->
## PAGE 00028: (2026x Refresh1) Invalid Port Type

- page_id: `304014783`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014783/2026x+Refresh1+Invalid+Port+Type
- version_number: 1
- version_date: `2026-04-29T16:51:02.577+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014785 space=MRTCD version=1 -->
## PAGE 00029: (2026x Refresh1) Invalid Repository

- page_id: `304014785`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014785/2026x+Refresh1+Invalid+Repository
- version_number: 1
- version_date: `2026-04-29T16:51:02.666+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014787 space=MRTCD version=1 -->
## PAGE 00030: (2026x Refresh1) Invalid Topic Type Property Direction

- page_id: `304014787`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014787/2026x+Refresh1+Invalid+Topic+Type+Property+Direction
- version_number: 1
- version_date: `2026-04-29T16:51:02.749+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014676 space=MRTCD version=1 -->
## PAGE 00031: (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication

- page_id: `304014676`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014676/2026x+Refresh1+Magic+Real-Time+Communication+Designer+DDS+Real-Time+Communication
- version_number: 1
- version_date: `2026-04-29T16:50:59.412+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin
- labels: ['dds-real-time-communication-plugin']

### NORMALIZED CONTENT

Magic Real-Time Communication Designer / DDS Real-Time Communication plugin is an environment for editing [Connext DDS](https://www.rti.com/products/connext-dds-professional) models in a visual way.

##### Background

The OMG Data-Distribution Service for Real-Time Systems (DDS) is the first open international middleware standard directly addressing publish-subscribe communications for real-time and embedded systems.

RTI Connext DDS Professional, based on a connectivity databus, offers a robust framework for developing and integrating mission critical systems. It is fully compliant with the OMG DDS for Real-Time Systems standard.

##### Advantages

With the Connext DDS for MagicDraw plugin, you can model the DDS-related aspects of your system using UML, extended by a DDS-specific profile. This offers the following advantages:

- The overall system (from requirements to functional applications) will have a unified representation, providing a common view of the system and a single source of truth.
- You can use an already familiar modeling language.
- The DDS entities and their relationships are displayed visually in a graphical notation.

The DDS Real-Time Communication Plugin documentation consists of the following sections:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">Magic Real-Time Communication Designer / DDS Real-Time Communication plugin is an environment for editing <a href="https://www.rti.com/products/connext-dds-professional">Connext DDS</a> models in a visual way.</p><h3>Background</h3><p class="FirstParagraph">The OMG Data-Distribution Service for Real-Time Systems (DDS) is the first open international middleware standard directly addressing publish-subscribe communications for real-time and embedded systems.</p><p>RTI Connext DDS Professional, based on a connectivity databus, offers a robust framework for developing and integrating mission critical systems. It is fully compliant with the OMG DDS for Real-Time Systems standard.</p><h3>Advantages</h3><p class="FirstParagraph">With the Connext DDS for MagicDraw plugin, you can model the DDS-related aspects of your system using UML, extended by a DDS-specific profile. This offers the following advantages:</p><ul><li>The overall system (from requirements to functional applications) will have a unified representation, providing a common view of the system and a single source of truth.</li><li>You can use an already familiar modeling language.</li><li>The DDS entities and their relationships are displayed visually in a graphical notation.</li></ul><p><br /></p><p><span style="color:var(--ds-text,#333333);">The DDS Real-Time Communication Plugin documentation consists of the following sections:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="675a6e7f-bff9-4f71-809c-aa22cf1a125d" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=304014789 space=MRTCD version=1 -->
## PAGE 00032: (2026x Refresh1) Missing Domain Attribute

- page_id: `304014789`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014789/2026x+Refresh1+Missing+Domain+Attribute
- version_number: 1
- version_date: `2026-04-29T16:51:02.832+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014791 space=MRTCD version=1 -->
## PAGE 00033: (2026x Refresh1) Missing Domain ID

- page_id: `304014791`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014791/2026x+Refresh1+Missing+Domain+ID
- version_number: 1
- version_date: `2026-04-29T16:51:02.911+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014793 space=MRTCD version=1 -->
## PAGE 00034: (2026x Refresh1) Missing Element Name

- page_id: `304014793`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014793/2026x+Refresh1+Missing+Element+Name
- version_number: 1
- version_date: `2026-04-29T16:51:02.991+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014795 space=MRTCD version=1 -->
## PAGE 00035: (2026x Refresh1) Multiple Struct Inheritance

- page_id: `304014795`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014795/2026x+Refresh1+Multiple+Struct+Inheritance
- version_number: 1
- version_date: `2026-04-29T16:51:03.086+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014797 space=MRTCD version=1 -->
## PAGE 00036: (2026x Refresh1) Multitype Topic

- page_id: `304014797`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014797/2026x+Refresh1+Multitype+Topic
- version_number: 1
- version_date: `2026-04-29T16:51:03.180+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014799 space=MRTCD version=1 -->
## PAGE 00037: (2026x Refresh1) Non-Nmeric Domain ID

- page_id: `304014799`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014799/2026x+Refresh1+Non-Nmeric+Domain+ID
- version_number: 1
- version_date: `2026-04-29T16:51:03.264+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014801 space=MRTCD version=1 -->
## PAGE 00038: (2026x Refresh1) Participant Type not Referenced

- page_id: `304014801`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014801/2026x+Refresh1+Participant+Type+not+Referenced
- version_number: 1
- version_date: `2026-04-29T16:51:03.377+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014760 space=MRTCD version=1 -->
## PAGE 00039: (2026x Refresh1) Qos Assignments

- page_id: `304014760`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014760/2026x+Refresh1+Qos+Assignments
- version_number: 1
- version_date: `2026-04-29T16:51:01.677+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Home Control Example
- labels: []

### NORMALIZED CONTENT

The currents version allows three kind of QoS assignment each of which can be swiftly created with specific generic tables. Since they were already covered in previous sections we only assign one for demonstration purposes. [CONFLUENCE_PAGE title='(2026x Refresh1) QoS profile assignments' space='']>]]>

As shown in the figure below, the case is a kind of a special one because the port readLight is not actually on the HomeController block but on its light port’s type called NestedLightPort. There is a validation rule which checks if the port has no connection with the given instance.

[IMAGE alt='' src='']

###### The example of Endpoint QoS Assignment Table.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The currents version allows three kind of QoS assignment each of which can be swiftly created with specific generic tables. Since they were already covered in previous sections we only assign one for demonstration purposes. <ac:link><ri:page ri:content-title="(2026x Refresh1) QoS profile assignments" /><ac:plain-text-link-body><![CDATA[Learn how to create Endpoint QoS Assignment Table >>]]></ac:plain-text-link-body></ac:link></p><p>As shown in the figure below, the case is a kind of a special one because the port readLight is not actually on the HomeController block but on its light port’s type called NestedLightPort. There is a validation rule which checks if the port has no connection with the given instance.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="QoS_Assignment_table.png"><ri:page ri:content-title="(2026x Refresh1) Qos Assignments" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example of Endpoint QoS Assignment Table.</h6>
````

<!--NOMAGIC_PAGE id=304014696 space=MRTCD version=1 -->
## PAGE 00040: (2026x Refresh1) QoS profile assignments

- page_id: `304014696`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014696/2026x+Refresh1+QoS+profile+assignments
- version_number: 1
- version_date: `2026-04-29T16:50:59.891+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Getting started
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
<p class="FirstParagraph">There are three elements that QoS Profiles can be assigned to in the model:</p><ul><li class="FirstParagraph">Endpoints typed by Topic.</li><li class="FirstParagraph">DomainParticipants.</li><li class="FirstParagraph">Topics.</li></ul><p><br /></p><p>To create an empty Endpoint QoS Assignment Table</p><hr /><ol><li>In the <a href="https://docs.nomagic.com/display/MDTWRT/Containment+tab">Containment tree</a>, right-click a predefined <em>Endpoint QoS </em>Package.</li><li>From the shortcut menu, select <strong>Create Diagram </strong>and from the opened dialog, select Endpoint QoS Assignment Table.</li><li>The unnamed table is created. Type its name and press enter.</li></ol><p><br /></p><p>To fill in the Endpoint QoS Assignment Table</p><hr /><ol><li>From the table toolbar, click the <strong>Add New</strong> button. The new row appears and Endpoint QoS Assignment element is created in the model.</li><li><p class="auto-cursor-target">In the table, specify the following:<br /> - Double-click the <strong>Name</strong> cell and type Endpoint QoS Assignment name.<br /> - Double-click the <strong>QoS Profile</strong> cell, select <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="(2026x Refresh1) QoS profile assignments" /></ri:attachment></ac:image></span> and in the <strong>Select Elements</strong> dialog choose QoS Profile.<br /> - Double-click the <strong>Endpoint</strong> cell, select <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="(2026x Refresh1) QoS profile assignments" /></ri:attachment></ac:image></span> and in the <strong>Select Port </strong>dialog choose already created ports or use the <strong>Creation Mode</strong> to create new port.<br /> - Double-click the <strong>Domain Participant Instance</strong> cell, select <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="(2026x Refresh1) QoS profile assignments" /></ri:attachment></ac:image></span> and in the <strong>Select Property </strong>dialog choose already created Part Properties or use the <strong>Creation Mode</strong> to create new Part Property.</p></li></ol><p class="FirstParagraph"><span><br /></span></p><p class="FirstParagraph"><span>Assigning QoS on subscribers/publishers is not possible since they are derived from the model and not explicitly marked.</span></p><ul><li>To assign QoS Profiles on Topics create a Topic QoS Assignment Table.<br /><ac:image><ri:attachment ri:filename="topic_qos_assignemnt_table_example.png"><ri:page ri:content-title="(2026x Refresh1) QoS profile assignments" /></ri:attachment></ac:image></li><li>To assign QoS Profiles on Domain Participants create a Participant QoS Assignment Table.<br /><ac:image><ri:attachment ri:filename="participant_qos_assignment.png"><ri:page ri:content-title="(2026x Refresh1) QoS profile assignments" /></ri:attachment></ac:image></li><li>To assign QoS Profiles on Endpoints create a Endpoint QoS Assignment Table.<br /><ac:image><ri:attachment ri:filename="endpoint_Qos_assignment_table.png"><ri:page ri:content-title="(2026x Refresh1) QoS profile assignments" /></ri:attachment></ac:image></li></ul>
````

<!--NOMAGIC_PAGE id=304014741 space=MRTCD version=1 -->
## PAGE 00041: (2026x Refresh1) Setting up the Simulink model

- page_id: `304014741`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014741/2026x+Refresh1+Setting+up+the+Simulink+model
- version_number: 1
- version_date: `2026-04-29T16:51:01.116+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Simulation with Simulink
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

<!--NOMAGIC_PAGE id=304014719 space=MRTCD version=1 -->
## PAGE 00042: (2026x Refresh1) Simulation with Simulink

- page_id: `304014719`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014719/2026x+Refresh1+Simulation+with+Simulink
- version_number: 1
- version_date: `2026-04-29T16:51:00.474+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: []

### NORMALIZED CONTENT

A Simulink model can be generated from the DDS XML generated by the Matlab plugin, which can be used to simulate the behavior of the modeled DDS system.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><span lang="EN">A Simulink model can be generated from the DDS XML generated by the Matlab plugin, which can be used to simulate the behavior of the modeled DDS system.</span></p><p class="FirstParagraph"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e4ccea78-c681-4939-b6e4-a9a976eb6044" /></p>
````

<!--NOMAGIC_PAGE id=304014803 space=MRTCD version=1 -->
## PAGE 00043: (2026x Refresh1) Struct Member Visibility

- page_id: `304014803`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014803/2026x+Refresh1+Struct+Member+Visibility
- version_number: 1
- version_date: `2026-04-29T16:51:03.459+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014805 space=MRTCD version=1 -->
## PAGE 00044: (2026x Refresh1) Topic Missing from Domain

- page_id: `304014805`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014805/2026x+Refresh1+Topic+Missing+from+Domain
- version_number: 1
- version_date: `2026-04-29T16:51:03.540+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014748 space=MRTCD version=1 -->
## PAGE 00045: (2026x Refresh1) Type mapping

- page_id: `304014748`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014748/2026x+Refresh1+Type+mapping
- version_number: 1
- version_date: `2026-04-29T16:51:01.287+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Simulation with Simulink
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

<!--NOMAGIC_PAGE id=304014807 space=MRTCD version=1 -->
## PAGE 00046: (2026x Refresh1) Unspecified String Bounds

- page_id: `304014807`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014807/2026x+Refresh1+Unspecified+String+Bounds
- version_number: 1
- version_date: `2026-04-29T16:51:03.624+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014809 space=MRTCD version=1 -->
## PAGE 00047: (2026x Refresh1) Unspecified String Bounds of Map Key

- page_id: `304014809`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014809/2026x+Refresh1+Unspecified+String+Bounds+of+Map+Key
- version_number: 1
- version_date: `2026-04-29T16:51:03.755+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014680 space=MRTCD version=1 -->
## PAGE 00048: (2026x Refresh1) Unsupported Discriminator Type

- page_id: `304014680`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014680/2026x+Refresh1+Unsupported+Discriminator+Type
- version_number: 1
- version_date: `2026-04-29T16:50:59.481+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Validation Suite
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

<!--NOMAGIC_PAGE id=304014716 space=MRTCD version=1 -->
## PAGE 00049: (2026x Refresh1) Validation

- page_id: `304014716`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014716/2026x+Refresh1+Validation
- version_number: 1
- version_date: `2026-04-29T16:51:00.406+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x Refresh1) Getting started
- labels: []

### NORMALIZED CONTENT

The validity of the DDS model is continuously checked by active validation rules contained in the DDS Validation Suite. For example, if you accidentally add multiple attributes to a Topic, an error is displayed. You can fix some of these DDS modeling problems by right-clicking on them and selecting the appropriate solver.

[IMAGE alt='' src='']

There is a separate validation suite for Simulink named DDS Simulink Validation Suite. It contains validation rules for data types that are not supported by Simulink. It can be activated independently from the rest of the rules.

The detailed descriptions of the validation rules are available in [CONFLUENCE_PAGE title='(2026x Refresh1) Validation Suite' space=''].

[CONFLUENCE_PAGE title='Validation' space='MDTWRT']>]]>

.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><span lang="EN">The validity of the DDS model is continuously checked by active validation rules contained in the DDS Validation Suite. For example, if you accidentally add multiple attributes to a Topic, an error is displayed. You can fix some of these DDS modeling problems by right-clicking on them and selecting the appropriate solver.</span></p><p class="FirstParagraph"><span lang="EN"><ac:image><ri:attachment ri:filename="image2020-11-12_15-7-35.png"><ri:page ri:content-title="(2026x Refresh1) Validation" /></ri:attachment></ac:image></span></p><p class="FirstParagraph"><br /></p><p class="FirstParagraph"><span lang="EN"><span><span>There is a separate validation suite for Simulink named DDS Simulink Validation Suite. It contains validation rules for data types that are not supported by Simulink. It can be activated independently from the rest of the rules.</span></span></span></p><p>The detailed descriptions of the validation rules are available in <ac:link><ri:page ri:content-title="(2026x Refresh1) Validation Suite" /></ac:link>.</p><p><br /></p><p><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Validation" /><ac:plain-text-link-body><![CDATA[Learn more about Validation >>]]></ac:plain-text-link-body></ac:link></p><p>.</p><p class="FirstParagraph"><span lang="EN"><br /></span></p><div><span style="white-space: pre-wrap;"><br /></span></div><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=304014678 space=MRTCD version=1 -->
## PAGE 00050: (2026x Refresh1) Validation Suite

- page_id: `304014678`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/304014678/2026x+Refresh1+Validation+Suite
- version_number: 1
- version_date: `2026-04-29T16:50:59.451+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x Refresh1) Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: []

### NORMALIZED CONTENT

In this section are detailed descriptions of the validation rules, each page describing one.

The severity is either error or warning. Warning means that the state is not necessarily incorrect, but probably is. The implementation, qualified name, and abbreviation are given because those are the identifiers modeling tool provides for a validation rule, so this document is searchable by either. [CONFLUENCE_PAGE title='Validation' space='MDTWRT']>]]>

The list of DDS validation rules:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">In this section are detailed descriptions of the validation rules, each page describing one. </p><p>The severity is either error or warning. Warning means that the state is not necessarily incorrect, but probably is. The implementation, qualified name, and abbreviation are given because those are the identifiers modeling tool provides for a validation rule, so this document is searchable by either. <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Validation" /><ac:plain-text-link-body><![CDATA[Learn more about modeling tool validation >>]]></ac:plain-text-link-body></ac:link></p><p>The list of DDS validation rules: </p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3606a106-ac5e-449f-becd-0cbba497615c" /></p>
````

<!--NOMAGIC_PAGE id=258048543 space=MRTCD version=1 -->
## PAGE 00051: (2026x) Applying DDS Sterotypes

- page_id: `258048543`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048543/2026x+Applying+DDS+Sterotypes
- version_number: 1
- version_date: `2025-09-24T15:29:37.909+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Home Control Example
- labels: []

### NORMALIZED CONTENT

First and for most we need do define the data structures and the topics which will be used in the communication. This can easily be done with a Topic Definition diagram. [CONFLUENCE_PAGE title='(2026x) Defining topics and types' space='']>]]>

Topics must contain exactly one property that has to be stereotyped with the TopicTypeProperty stereotype and has to be a type of either a Struct or Union.

[IMAGE alt='' src='']

###### The example defines three packages or DDS Modules for the three factor that we would like to measure and control.

Now that we have the data structures for the communication we can assign them to ports turning them into data writers and data readers in the DDS sense. [CONFLUENCE_PAGE title='(2026x) Defining Domain Participant communication' space='']>]]>

First we need to apply the DomainParticipant stereotypes on Blocks whose instances will be used as the individual applications in the communication. [CONFLUENCE_PAGE title='(2026x) Defining Domains and Domain Participants' space='']>]]>

[IMAGE alt='' src='']

###### The SysML BLock Definition diagram that contains all Domain Participants of Home Controller system.

After SysML model is created with the right stereotypes applied, we can define our DDS domains with them.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">First and for most we need do define the data structures and the topics which will be used in the communication. This can easily be done with a Topic Definition diagram. <ac:link><ri:page ri:content-title="(2026x) Defining topics and types" /><ac:plain-text-link-body><![CDATA[How to define topics and types >>]]></ac:plain-text-link-body></ac:link></p><p>Topics must contain exactly one property that has to be stereotyped with the TopicTypeProperty stereotype and has to be a type of either a Struct or Union.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="topic_Definition_diagram_homeControlerSystem.png"><ri:page ri:content-title="(2026x) Applying DDS Sterotypes" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example defines three packages or DDS Modules for the three factor that we would like to measure and control.</h6><p><br /></p><p>Now that we have the data structures for the communication we can assign them to ports turning them into data writers and data readers in the DDS sense. <ac:link><ri:page ri:content-title="(2026x) Defining Domain Participant communication" /><ac:plain-text-link-body><![CDATA[How to define Domain Participant communication >>]]></ac:plain-text-link-body></ac:link></p><p>First we need to apply the DomainParticipant stereotypes on Blocks whose instances will be used as the individual applications in the communication. <ac:link><ri:page ri:content-title="(2026x) Defining Domains and Domain Participants" /><ac:plain-text-link-body><![CDATA[How to define Domains and Domain Participants >>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center"><ri:attachment ri:filename="bdd_homeControlerSystem.png"><ri:page ri:content-title="(2026x) Applying DDS Sterotypes" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The SysML BLock Definition diagram that contains all Domain Participants of Home Controller system.</h6><p><br /></p><p>After  SysML model is created with the right stereotypes applied, we can define our DDS domains with them.</p>
````

<!--NOMAGIC_PAGE id=258048522 space=MRTCD version=1 -->
## PAGE 00052: (2026x) Creating DDS project

- page_id: `258048522`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048522/2026x+Creating+DDS+project
- version_number: 1
- version_date: `2025-09-24T15:29:37.431+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Getting started
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
<p>To create a blank DDS project</p><hr /><ol><li><span style="color: rgb(51,51,51);">Do one of the following:<br /> </span><ul><li><span style="color: rgb(51,51,51);">Select <strong>File </strong>&gt; <strong>New</strong> <strong>Project</strong>.</span></li><li><span style="color: rgb(51,51,51);">On the main toolbar, click the <strong>New</strong> <strong>Project</strong> button.</span></li><li><span style="color: rgb(51,51,51);">Press Ctr+Shiftl+N.</span> <span style="color: rgb(51,51,51);"> <br /> </span></li></ul></li><li class="_mce_tagged_br"><span style="color: rgb(51,51,51);">In the <strong>New</strong> <strong> Project</strong> dialog, under <strong>Systems Engineering</strong>, select <strong>DDS</strong> <strong> Project</strong>.<br /> </span></li><li><span style="color: rgb(51,51,51);">Specify name and location.</span></li><li><span style="color: rgb(51,51,51);">Click <strong>OK</strong> when you are done.<br />The blank project is created and stored in your file system with defined name.<br /> <ac:image><ri:attachment ri:filename="create_new_DDS_project_steps.png"><ri:page ri:content-title="(2026x) Creating DDS project" /></ri:attachment></ac:image> </span></li></ol><p><span style="color: rgb(51,51,51);"> <br /> </span></p><p><span style="color: rgb(51,51,51);">Once you created the blank DDS Project, you can use for modeling already predefined Package structure as shown in the following figure.</span></p><h6 style="text-align: center;"><span style="color: rgb(51,51,51);"> <ac:image ac:align="center"><ri:attachment ri:filename="predefined_DDS_package_structure.png"><ri:page ri:content-title="(2026x) Creating DDS project" /></ri:attachment></ac:image> </span> <br /> <span>The predefined Package structure of blank DDS project.</span></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=258048547 space=MRTCD version=2 -->
## PAGE 00053: (2026x) Creating the domain

- page_id: `258048547`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048547/2026x+Creating+the+domain
- version_number: 2
- version_date: `2025-09-24T15:33:07.606+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Home Control Example
- labels: []

### NORMALIZED CONTENT

The Domain can be created by using the DDS Domain Table. As shown in the following table, the Smart Home DDS Domain is created with specified its id, topics, participants and participant instances. [How to create DDS Domain Table>>](https://docs.nomagic.com/display/MRTCD/(2026x) Defining+Domains+and+Domain+Participants#DefiningDomainsandDomainParticipants-CreatingDomainandDomainParticipantsbyusingtheDDSDomainTable)

[IMAGE alt='' src='']

###### The example of DDS Domain Table.

The Participant Instances derived column displays all the instances that will be in the the DDS XML.Now we are ready to export the model if we desire, but first we need to assign quality of service requirements on the DDS elements.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Domain can be created by using the <span style="color: rgb(62,63,64);">DDS Domain Table. As shown in the following table, the Smart Home DDS Domain is created with specified its id, topics, participants and participant instances. <a href="https://docs.nomagic.com/display/MRTCD/(2026x) Defining+Domains+and+Domain+Participants#DefiningDomainsandDomainParticipants-CreatingDomainandDomainParticipantsbyusingtheDDSDomainTable">How to create DDS Domain Table&gt;&gt;</a></span></p><p><span style="color: rgb(62,63,64);"><ac:image ac:align="center"><ri:attachment ri:filename="domain_table.png"><ri:page ri:content-title="(2026x) Creating the domain" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">The example of DDS Domain Table.</span></h6><p class="auto-cursor-target"><span><span><span style="color: rgb(62,63,64);">The Participant Instances derived column displays all the instances that will be in the the DDS XML. </span>Now we are ready to export the model if we desire, but first we need to assign quality of service requirements on the DDS elements.</span><br /></span></p><p class="auto-cursor-target"><span><br /></span></p><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=258048483 space=MRTCD version=1 -->
## PAGE 00054: (2026x) Defining Domain Participant communication

- page_id: `258048483`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048483/2026x+Defining+Domain+Participant+communication
- version_number: 1
- version_date: `2025-09-24T15:29:36.685+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Getting started
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
<p>Communication between DDS elements is determined by ports owned by Domain Participants. Ports that are parts of the communication has to have DDS Endpoint stereotype otherwise they will be omitted.</p><p><br /></p><p>To apply DDS Endpoint stereotype on a port</p><hr /><ol><li>Right-click the port and from the shortcut menu, select Stereotype.</li><li>In the opened dialog, select DDS Endpoint. </li><li>Click <strong>Apply</strong>.</li></ol><p><br /></p><p>The derived direction of ports determine whether they are considered Data Reader or Data Writers. In case of non-nested ports the publishers and subscribers which contain the Data Readers or Writers are implicitly defined under the Domain Participants. Publishers and Subscribers in DDS group Data Readers and Writers.</p><p>Nested ports can be used to group Data Writers and Readers. The grouping is determined by the ports highest in the hierarchy (direct children of the Block). Note that non-nested ports must have a type of Topic.</p><p><span>In between ports have no effective meaning.</span></p><p><span>In case of </span>nested ports<span>, ports highest in the hierarchy implicitly define </span>subscribers<span> and </span>publishers<span> as well.</span></p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="image2020-11-12_14-1-30.png"><ri:page ri:content-title="(2026x) Defining Domain Participant communication" /></ri:attachment></ac:image></p><p><span><br /></span></p><p><br /></p><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=258048474 space=MRTCD version=1 -->
## PAGE 00055: (2026x) Defining Domains and Domain Participants

- page_id: `258048474`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048474/2026x+Defining+Domains+and+Domain+Participants
- version_number: 1
- version_date: `2025-09-24T15:29:36.544+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Getting started
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

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MDTWRT'] , right-click a Package wherein you want to create Domain Participants or Domain.
2. From the shortcut menu, select Create Element and from the opened dialog, select DomainParticipant or Domain.
3. The unnamed element is created. Type its name and press enter. [ATTACHMENT filename='domain_participant_and_domain_in_containment_tree.png']

##### Creating Domain and Domain Participants by using the DDS Domain Table

You can use the DDS Domain Table to create a Domain inside a Domain Library. It also helps to assign Topics and Domain Participants to the Domain. The DDS Domain Table named Domain is already created in predefined DDS Package structure. If you want to create a new one, follow the procedure below.

To create an empty DDS Domain Table

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MDTWRT'] , right-click a predefined Domain Package.
2. From the shortcut menu, select Create Diagram and from the opened dialog, select DDS Domain Table.
3. The unnamed table is created. Type its name and press enter.

To fill in the DDS Domain Table

1. From the table toolbar, click the Add New button. The new row appears and DDSDomain element is created in the model.
2. In the table, specify the following: 
 - Double-click **Name** cell and type a domain name. 
 - Double-click the **Domain_id** cell and type domain id number. 
 - Double-click the **Topics** cell, select [IMAGE alt='' src=''] and in the **Select Elements** dialog choose already created topics or use the **Creation Mode** to create new topics. Topics referenced by a Domain Participants must be assigned to every Domain that the participant is assigned to. Unassigned Topics lead to validation errors. - Double-click the **Participants** cell, select [IMAGE alt='' src=''] and in the **Select Elements** dialog choose already created Domain Participants or use the **Creation Mode** to create new Domain Participants. 
 - The **Participant Instances** column fill in automatically when instances are created in the model. >]]>[CONFLUENCE_PAGE title='(2026x) Defining Domains and Domain Participants' space=''] 
[IMAGE alt='' src='']

##### Creating Domain Participants by refactoring the Block

To create a Domain Participant or Domain by refactoring a Block

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MDTWRT'] , right-click a Package wherein you want to create Domain Participants or Domain.
2. From the shortcut menu, select Create Element and from the opened dialog, select Block.
3. Right-click the Block and select Refactor > Convert To > More Specific > Domain Participant or Domain . The Block is refactored to the Domain Participant or Domain.

[IMAGE alt='' src='']

##### Creating instances

The difference between instances of Domain Participants and Members of DDS Data types are the following:

- Domain Participant instances: are any Block property typed by Domain Participant. They can be any kid of property: Value Property, Part Property, Reference Property etc. 
 - Members: DDS Data type Members are used in the data definition section of the meta-model. They allow to define custom, DDS annotated data types. They rely heavily on multiplicity definitions in order to be able to produce a syntactically correct DDS xml output.

To create a Domain Participant instances

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MDTWRT'] , right-click a Block which will be the owner of the instances.
2. From the shortcut menu, select Create Diagram and from the opened dialog, select SysML Internal Block Diagram.
3. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] select a property (e.g. Part Property) and click on the diagram pane.
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

1. Double-click the Part Property to open it's [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] .
2. Select the Multiplicity property value or type Lower Value and Upper Value.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>All Domain Participants are assigned to the Domain regardless of where they are in the containment hierarchy. Domain Participants should have at least one instance which can be any kind of lock property typed by Domain Participant. During DDS XML generation, all properties of the Block are considered a Domain Participants.</p><p>You can create Domain and Domain Participants by using:</p><ul><li>The Containment tree.</li><li>DDS Domain Table.</li></ul><p>This page contains the following topics:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="e20bb792-47ca-49f9-8f77-b9d92eb13d0b"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p><div><p><br /></p><h3>Creating Domain and Domain Participants by using the Containment tree</h3><p><br /></p><p>To create a Domain Participant or Domain in the Containment tree</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a Package wherein you want to create Domain Participants or Domain.</li><li>From the shortcut menu, select <strong>Create Element </strong>and from the opened dialog, select DomainParticipant or Domain.</li><li>The unnamed element is created. Type its name and press enter.<br /><ac:image><ri:attachment ri:filename="domain_participant_and_domain_in_containment_tree.png"><ri:page ri:content-title="(2026x) Defining Domains and Domain Participants" /></ri:attachment></ac:image></li></ol><h3>Creating Domain and Domain Participants by using the DDS Domain Table</h3><p>You can use the DDS Domain Table to create a Domain inside a Domain Library. It also helps to assign Topics and Domain Participants to the Domain. The DDS Domain Table named Domain is already created in predefined DDS Package structure. If you want to create a new one, follow the procedure below.</p><p>To create an empty DDS Domain Table</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a predefined <em>Domain</em> Package.</li><li>From the shortcut menu, select <strong>Create Diagram </strong>and from the opened dialog, select DDS Domain Table.</li><li>The unnamed table is created. Type its name and press enter.</li></ol><p><br /></p><p>To fill in the DDS Domain Table</p><hr /><ol><li>From the table toolbar, click the <strong>Add New</strong> button. The new row appears and DDSDomain element is created in the model.</li><li><p class="auto-cursor-target">In the table, specify the following:<br /> - Double-click <strong>Name</strong> cell and type a domain name.<br /> - Double-click the <strong>Domain_id</strong> cell and type domain id number.<br /> - Double-click the <strong>Topics</strong> cell, select <ac:image ac:title="Edit" ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="(2026x) Defining Domains and Domain Participants" /></ri:attachment></ac:image> and in the <strong>Select Elements</strong> dialog choose already created topics or use the <strong>Creation Mode</strong> to create new topics.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="ccea59d8-2dd6-47db-a1e2-75bba1a8ff67"><ac:rich-text-body><p>Topics referenced by a Domain Participants must be assigned to every Domain that the participant is assigned to. Unassigned Topics lead to validation errors.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"> - Double-click the <strong>Participants</strong> cell, select <ac:image ac:title="Edit" ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="(2026x) Defining Domains and Domain Participants" /></ri:attachment></ac:image> and in the <strong>Select Elements</strong> dialog choose already created Domain Participants or use the <strong>Creation Mode</strong> to create new Domain Participants.<br /> - The <strong>Participant Instances</strong> column fill in automatically when instances are created in the model. <ac:link ac:anchor="Creating instances of Domain Participants"><ac:plain-text-link-body><![CDATA[How to create Participant Instances >>]]></ac:plain-text-link-body><ri:page ri:content-title="(2026x) Defining Domains and Domain Participants" /></ac:link><br /><ac:image><ri:attachment ri:filename="DDSDomain_table.png"><ri:page ri:content-title="(2026x) Defining Domains and Domain Participants" /></ri:attachment></ac:image></p></li></ol><h3>Creating Domain Participants by refactoring the Block</h3><p><br /></p><p>To create a Domain Participant or Domain by refactoring a Block</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a Package wherein you want to create Domain Participants or Domain.</li><li>From the shortcut menu, select <strong>Create Element </strong>and from the opened dialog, select Block.</li><li>Right-click the Block and select <strong>Refactor</strong> &gt; <strong>Convert To</strong> &gt; <strong>More Specific</strong> &gt; <strong>Domain Participant</strong> or <strong>Domain</strong>.<br />The Block is refactored to the Domain Participant or Domain.</li></ol><p><ac:image><ri:attachment ri:filename="Block_refactor_to_domain_participant.png"><ri:page ri:content-title="(2026x) Defining Domains and Domain Participants" /></ri:attachment></ac:image></p><h3>Creating instances </h3><p>The difference between instances of Domain Participants and Members of DDS Data types are the following:</p><p>   - Domain Participant instances: are any Block property typed by Domain Participant. They can be any kid of property: Value Property, Part Property, Reference Property etc.<br />    - Members: DDS Data type Members are used in the data definition section of the meta-model. They allow to define custom, DDS annotated data types. They rely heavily on multiplicity definitions in order to be able to produce a syntactically correct DDS xml output.<br /><br /></p><p>To create a Domain Participant instances</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a Block which will be the owner of the instances.</li><li>From the shortcut menu, select <strong>Create Diagram </strong>and from the opened dialog, select SysML Internal Block Diagram.</li><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram palette]]></ac:plain-text-link-body></ac:link> select a property (e.g. Part Property) and click on the diagram pane.</li><li>Type the name of the property.</li><li>Select a Domain Participant as type of the property.<br />The instance of Domain Participant is created.<br /><br /><ac:image><ri:attachment ri:filename="instances_of_domain_participants.png"><ri:page ri:content-title="(2026x) Defining Domains and Domain Participants" /></ri:attachment></ac:image></li></ol><h3>Defining instances multiplicity</h3></div><p>To define a instances as an array or sequence, its multiplicity needs to be changed as it follows, where N must be at least 1 and M must be greater than N.</p><table><colgroup><col /><col /><col /><col /><col /></colgroup><tbody><tr><td colspan="2"><p class="Compact"><strong>Lower Value</strong></p></td><td><p class="Compact"><strong>Upper Value</strong></p></td><td><p class="Compact"><strong>Multiplicity</strong></p></td><td><p class="Compact"><strong>Type</strong></p></td></tr><tr><td colspan="2"><p>N</p></td><td><p>N</p></td><td><p>N</p></td><td><p>Array</p></td></tr><tr><td colspan="2"><p>0</p></td><td><p>-1</p></td><td><p>0 .. *</p></td><td><p>Boundless Array</p></td></tr><tr><td colspan="2"><p>0</p></td><td><p>N-1</p></td><td><p>0 .. N-1</p></td><td><p>Sequence</p></td></tr><tr><td colspan="2"><p>N</p></td><td><p>M</p></td><td><p>N .. M</p></td><td><p>Sequence</p></td></tr></tbody></table><p><br /></p><p>To change the instance multiplicity</p><hr /><ol><li>Double-click the Part Property to open it's <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>.</li><li>Select the Multiplicity property value or type Lower Value and Upper Value.</li></ol><p><ac:image><ri:attachment ri:filename="members_multiplicity.png"><ri:page ri:content-title="(2026x) Defining Domains and Domain Participants" /></ri:attachment></ac:image></p><p class="Compact"><br /></p>
````

<!--NOMAGIC_PAGE id=258048533 space=MRTCD version=1 -->
## PAGE 00056: (2026x) Defining topics and types

- page_id: `258048533`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048533/2026x+Defining+topics+and+types
- version_number: 1
- version_date: `2025-09-24T15:29:37.675+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Getting started
- labels: ['define-topics', 'define-types', 'create-dds-topic-definition-diagram']

### NORMALIZED CONTENT

You can define topic and types used by them in the DDS Topic Definition Diagram.

[IMAGE alt='' src='']

###### The example of the DDS Topic Definition Diagram where main elements are highlighed: DDS Module, Types and Topic.

##### Creating DDS Topic Definition Diagram

After a blank DDS Project is created, the predefined package structure is prepared where the DDS Topic Definition Diagram is already created under the *Topics* Package named *Topics*. It contains an empty DDS Module. If you need another one, create it manually, as described in the following procedure.

To create blank DDS Topic Definition Diagram

1. In the [CONFLUENCE_PAGE title='Model Browser' space='MDTWRT'] , select the owner for the new diagram.
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

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select a type you need and click on DDS Module element.
2. Type its name.
3. Click the Create Member [CONFLUENCE_PAGE title='Smart manipulators' space='MDTWRT'] to create a Members for the type.
4. Select newly created Member on the shape, click [ATTACHMENT filename='specify_type.png'] and select a type for a it.

Creating and defining topics

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select a Topic and click on the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] .
2. Type its name.
3. Click the Create Element [CONFLUENCE_PAGE title='Smart manipulators' space='MDTWRT'] to create a Topic Type Property or Reception for the Topic.
4. Select newly created Topic Type Property or Reception, click [IMAGE alt='' src='']and select a type for a it. Press Ctrl+Space to search among the available types.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can define topic and types <span style="color: rgb(62,63,64);">used by them</span> in the DDS Topic Definition Diagram.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="DDS_Topic_Definition_Diagram.png"><ri:page ri:content-title="(2026x) Defining topics and types" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example of the DDS Topic Definition Diagram where main elements are highlighed: DDS Module, Types and Topic.</h6><h3>Creating DDS Topic Definition Diagram</h3><p>After a blank DDS Project is created, the predefined package structure is prepared where the DDS Topic Definition Diagram is already created under the <em>Topics</em> Package named <em>Topics</em>. It contains an empty DDS Module. If you need another one, create it manually, as described in the following procedure.</p><p>To create blank DDS Topic Definition Diagram</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Model Browser" /></ac:link>, select the owner for the new diagram.</li><li>Do one of the following:<br /><ul><li>Right-click the Package, and from the shortcut menu select <strong>Create Diagram.</strong></li><li>Press Ctrl+N.</li><li>On the main toolbar, click <span class="confluence-embedded-file-wrapper"><ac:image ac:alt="Create Diagram"><ri:attachment ri:filename="create_diagram.png"><ri:page ri:content-title="(2026x) Defining topics and types" /></ri:attachment></ac:image></span> .</li><li>From the main menu, select <strong>Diagrams</strong> &gt; <strong>Create Diagram</strong>.</li></ul></li><li><p>In the <strong>Create Diagram</strong> box, under <strong>General</strong> diagram group, select the <strong>DDS Topic Definition Diagram</strong>.</p></li></ol><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="8fa80951-960a-4327-aedd-357ca62fe7c8"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">Press Esc or click outside the dialog to close the diagram creation dialog without creating the diagram.</span></p></ac:rich-text-body></ac:structured-macro><h3>Defining topics and types</h3><p>You can create the following types:</p><ul><li>Struct Type</li><li>Union Type</li><li>Bitmask Type</li><li>Enumeration Type</li><li>Map Type</li><li>Alias Type</li><li>Annotation Type</li></ul><p><br /></p><p>Creating and defining types</p><hr /><ol><li>From the<ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[ diagram palette]]></ac:plain-text-link-body></ac:link>, select a type you need and click on DDS Module element. </li><li>Type its name.</li><li>Click the <strong>Create Member</strong> <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Smart manipulators" /><ac:plain-text-link-body><![CDATA[smart manipulator]]></ac:plain-text-link-body></ac:link> to create a Members for the type.</li><li>Select newly created Member on the shape, click <ac:image ac:title="Specify Type" ac:alt="Specify Type"><ri:attachment ri:filename="specify_type.png"><ri:page ri:content-title="(2026x) Defining topics and types" /></ri:attachment></ac:image> and select a type for a it.</li></ol><p><br /></p><p>Creating and defining topics</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram palette]]></ac:plain-text-link-body></ac:link>, select a Topic and click on the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram pane]]></ac:plain-text-link-body></ac:link>. </li><li>Type its name.</li><li>Click the <strong>Create Element</strong> <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Smart manipulators" /><ac:plain-text-link-body><![CDATA[smart manipulator]]></ac:plain-text-link-body></ac:link> to create a Topic Type Property or Reception for the Topic.</li><li><p class="auto-cursor-target">Select newly created Topic Type Property or Reception, click <ac:image ac:title="Specify Type" ac:alt="Specify Type"><ri:attachment ri:filename="specify_type.png"><ri:page ri:content-title="(2026x) Defining topics and types" /></ri:attachment></ac:image>and select a type for a it.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="f4ba630b-5037-4766-aa0d-f65b82385bbb"><ac:rich-text-body><p>Press Ctrl+Space to search among the available types.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><br /></p><p class="Compact">              </p><p class="Compact"><br /></p>
````

<!--NOMAGIC_PAGE id=258048555 space=MRTCD version=1 -->
## PAGE 00057: (2026x) Domain not in Library

- page_id: `258048555`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048555/2026x+Domain+not+in+Library
- version_number: 1
- version_date: `2025-09-24T15:29:38.215+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048557 space=MRTCD version=1 -->
## PAGE 00058: (2026x) Domain Participant without Instance

- page_id: `258048557`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048557/2026x+Domain+Participant+without+Instance
- version_number: 1
- version_date: `2025-09-24T15:29:38.279+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048559 space=MRTCD version=1 -->
## PAGE 00059: (2026x) Duplicate Domain ID

- page_id: `258048559`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048559/2026x+Duplicate+Domain+ID
- version_number: 1
- version_date: `2025-09-24T15:29:38.340+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048561 space=MRTCD version=1 -->
## PAGE 00060: (2026x) Endpoint not Referenced

- page_id: `258048561`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048561/2026x+Endpoint+not+Referenced
- version_number: 1
- version_date: `2025-09-24T15:29:38.401+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048513 space=MRTCD version=1 -->
## PAGE 00061: (2026x) Environment setup

- page_id: `258048513`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048513/2026x+Environment+setup
- version_number: 1
- version_date: `2025-09-24T15:29:37.225+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Simulation with Simulink
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

<!--NOMAGIC_PAGE id=258048540 space=MRTCD version=1 -->
## PAGE 00062: (2026x) Example Model

- page_id: `258048540`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048540/2026x+Example+Model
- version_number: 1
- version_date: `2025-09-24T15:29:37.839+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Home Control Example
- labels: []

### NORMALIZED CONTENT

HomeControler.mdzip contains a model that describes a system that consists of an air conditioner unit, a dehumidifiers, shutters and a light sensor. The air conditioner and the dehumidifier both contain a controller and a sensor component. The system is supervised by the Home Controller whose main responsibility is to monitor data received from the components and to control them.

[IMAGE alt='' src='']

###### The SysmL Internal Block Diagram of Home Controller environment.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">HomeControler.mdzip contains a model that describes a system that consists of an air conditioner unit, a dehumidifiers, shutters and a light sensor. The air conditioner and the dehumidifier both contain a controller and a sensor component. The system is supervised by the Home Controller whose main responsibility is to monitor data received from the components and to control them.</p><p class="FirstParagraph"><ac:image ac:align="center"><ri:attachment ri:filename="ibd_homeControlerSystem.png"><ri:page ri:content-title="(2026x) Example Model" /></ri:attachment></ac:image></p><h6 class="FirstParagraph" style="text-align: center;">The SysmL Internal Block Diagram of Home Controller environment.</h6>
````

<!--NOMAGIC_PAGE id=258048553 space=MRTCD version=2 -->
## PAGE 00063: (2026x) Exporting DDS Control Example to XML

- page_id: `258048553`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048553/2026x+Exporting+DDS+Control+Example+to+XML
- version_number: 2
- version_date: `2025-09-24T15:33:09.537+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Home Control Example
- labels: []

### NORMALIZED CONTENT

You can export the DDS examples to XML. For this, follow the procedures provided in the page [Exporting DDS XML](https://docs.nomagic.com/display/MRTCD/(2026x) Exporting+DDS+XML).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can export the DDS examples to XML. For this, follow the procedures provided in the page <a class="current" style="letter-spacing: 0.0px;" href="https://docs.nomagic.com/display/MRTCD/(2026x) Exporting+DDS+XML">Exporting DDS XML</a>.</p><p><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=258048493 space=MRTCD version=1 -->
## PAGE 00064: (2026x) Exporting DDS XML

- page_id: `258048493`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048493/2026x+Exporting+DDS+XML
- version_number: 1
- version_date: `2025-09-24T15:29:36.837+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Getting started
- labels: ['generate-dds-xml']

### NORMALIZED CONTENT

You can generate DDS xml file directly from the modeling tool. Referenced QoS profiles are included in the resulting XML. Before the export a pre-check is initiated to ensure that the QoS Profiles imported to modeling tool were not changed and still up to date. You can use the resulting XML in the **RTI DDS Code Generator**, **RTI System Designer**, the **DDS Simulink Tooling** or other standards-compliant tool.

To generate DDS XML

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select Tools > DDS > Generate DDS XML .
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
<p>You can generate DDS xml file directly from the modeling tool. Referenced QoS profiles are included in the resulting XML. Before the export a pre-check is initiated to ensure that the QoS Profiles imported to modeling tool were not changed and still up to date. You can use the resulting XML in the <strong style="letter-spacing: 0.0px;">RTI DDS Code Generator</strong>, <strong style="letter-spacing: 0.0px;">RTI System Designer</strong>, the <strong style="letter-spacing: 0.0px;">DDS Simulink Tooling</strong> or other standards-compliant tool.</p><p><br /></p><p>To generate DDS XML</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main menu]]></ac:plain-text-link-body></ac:link>, select <strong>Tools </strong>&gt; <strong>DDS</strong> &gt; <strong>Generate DDS XML</strong>.</li><li>In the <strong style="letter-spacing: 0.0px;">Generate DDS XML</strong><span style="letter-spacing: 0.0px;"> dialog, select the following:</span><span style="letter-spacing: 0.0px;"><br /></span></li></ol><p class="auto-cursor-target"> -<strong> Select Scope</strong> - select a Package which content you want to export. Click <strong>Next</strong>.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="72fbaaef-7a44-4b88-9f40-a83af6e3bbaa"><ac:rich-text-body><p><span>To ensure that the exported XML is valid, make sure the selected package contains at least one domain participant library containing at least one Domain Participant. Otherwise, the tool takes care of the validity of references by including the elements referred from the selected package even if they are outside the selected Package.</span></p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="select_scope.png"><ri:page ri:content-title="(2026x) Exporting DDS XML" /></ri:attachment></ac:image></p><p class="auto-cursor-target"> - <strong>Select target version</strong> - select DDS target version. Click <strong>Next</strong>.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="75827afe-6c50-4001-a769-860dc4e01ba3"><ac:rich-text-body><p>QoS Profiles between versions are not compatible. QoS Profiles with a version that is not matching with the target version selected it the wizard will prevent the export.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="select_target_version.png"><ri:page ri:content-title="(2026x) Exporting DDS XML" /></ri:attachment></ac:image><br /> - <strong>Select output directory</strong> - select the location of exported DDS XML file. Click <strong>Finish</strong>.<br /><br /><ac:image><ri:attachment ri:filename="select_output_directory.png"><ri:page ri:content-title="(2026x) Exporting DDS XML" /></ri:attachment></ac:image><br />The DDS XML file is generated.</p><p><br /><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=258048515 space=MRTCD version=1 -->
## PAGE 00065: (2026x) Generating the Simulink model

- page_id: `258048515`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048515/2026x+Generating+the+Simulink+model
- version_number: 1
- version_date: `2025-09-24T15:29:37.269+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Simulation with Simulink
- labels: []

### NORMALIZED CONTENT

After the initialization step you can generate Simulink models using the LoadSimulinkModel.m script.

To generate the Simulink models

1. Run LoadSimulinkModel.
2. Select the desired xml you want to generate from. The xml gets copied to the matlab workspace, and the generation starts. After the generation finishes (assuming that you used the example Thermostat.xml) the workspace should look like this: [ATTACHMENT filename='image2020-11-12_15-12-49.png']
3. Open <your_model>.slx.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">After the initialization step you can generate Simulink models using the LoadSimulinkModel.m script.</p><p class="FirstParagraph"><br /></p><p class="FirstParagraph">To generate the Simulink models</p><hr /><ol><li>Run LoadSimulinkModel.</li><li>Select the desired xml you want to generate from. The xml gets copied to the matlab workspace, and the generation starts. After the generation finishes (assuming that you used the example Thermostat.xml) the workspace should look like this:<br /><ac:image><ri:attachment ri:filename="image2020-11-12_15-12-49.png"><ri:page ri:content-title="(2026x) Generating the Simulink model" /></ri:attachment></ac:image></li><li>Open &lt;your_model&gt;.slx.</li></ol><p class="FirstParagraph"><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=258048472 space=MRTCD version=1 -->
## PAGE 00066: (2026x) Getting started

- page_id: `258048472`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048472/2026x+Getting+started
- version_number: 1
- version_date: `2025-09-24T15:29:36.513+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: []

### NORMALIZED CONTENT

**Welcome!**This user guide will walk you through the basics of using DDS Real-Time Communication Plugin, including working with projects, setting up the modeling environment, defining DDS elements, importing and exporting XML files, and more.

Use the search box to find a specific topic or select one from the list below:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Welcome!</strong><span style="color: rgb(62,63,64);"> This user guide will walk you through the basics of using DDS Real-Time Communication Plugin, including working with projects, setting up the modeling environment</span><span style="color: rgb(62,63,64);">, defining DDS elements, importing and exporting XML files, and more.</span></p><p><span style="color: rgb(62,63,64);">Use the search box to find a specific topic or select one from the list below</span><span class="confluence-link" style="color: rgb(62,63,64);">:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="60201284-9a7d-44b0-812b-445cfcf90c54" /></p>
````

<!--NOMAGIC_PAGE id=258048520 space=MRTCD version=1 -->
## PAGE 00067: (2026x) Home Control Example

- page_id: `258048520`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048520/2026x+Home+Control+Example
- version_number: 1
- version_date: `2025-09-24T15:29:37.388+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: []

### NORMALIZED CONTENT

The aim of this example is to demonstrate how to make models using DDS and SysML semantics, how to assign quality of service profiles. Also it provides information how to generate RTI Connext DDS model in XML format that can be used in various ways like for the RTI Connext code generator or for generating MATLAB Simulink models.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><span lang="EN">The aim of this example is to demonstrate how to make models using DDS and SysML semantics, how to assign quality of service profiles. Also it provides information how to generate RTI Connext DDS model in XML format that can be used in various ways like for the RTI Connext code generator or for generating MATLAB Simulink models.</span></p><p class="FirstParagraph"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="cfb9a75d-74f0-4ba6-97ca-91ec209cd98e" /></p>
````

<!--NOMAGIC_PAGE id=258048563 space=MRTCD version=1 -->
## PAGE 00068: (2026x) Illegal Inheritance

- page_id: `258048563`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048563/2026x+Illegal+Inheritance
- version_number: 1
- version_date: `2025-09-24T15:29:38.465+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048526 space=MRTCD version=1 -->
## PAGE 00069: (2026x) Importing DDS Profile and DDS Style in Other Projects

- page_id: `258048526`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048526/2026x+Importing+DDS+Profile+and+DDS+Style+in+Other+Projects
- version_number: 1
- version_date: `2025-09-24T15:29:37.528+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Getting started
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
<p class="FirstParagraph">The created DDS projects already have the DDS profile imported and DDS Style set. You ca reuse them in non-DDs projects. </p><p class="FirstParagraph"><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="3c27f29d-5174-4870-87d5-2a8fd1589241" /></p><h3 class="FirstParagraph">Reusing the DDS profile in non-DDS projects</h3><p class="FirstParagraph">Reusing the DDS profile in non-DDS projects</p><hr /><ol><li class="FirstParagraph">Open a non-DDS project in which you want to reuse the DDS profile.</li><li class="FirstParagraph">On the main menu, select <strong>File</strong> &gt; <strong>Use Project</strong> &gt; <strong>Use Local Project.</strong></li><li class="FirstParagraph">In the opened <strong>Use Project</strong> dialog, you can select the DDS profile either: <br /> - From predefined location. Select the <strong>Paths to used projects</strong>: &lt;install.root&gt;\profiles and from the list below, select the <em>dds_profile.mdzip</em>.<br /> - From File system. Click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="three_dot_button.png"><ri:page ri:content-title="(2026x) Importing DDS Profile and DDS Style in Other Projects" /></ri:attachment></ac:image> and from the product install folder, select <em>profiles/dds_profile.mdzip</em>. Click <strong>Open</strong>.</li><li class="FirstParagraph">Click <strong>Next</strong> &gt; <strong>Finish</strong>.<br />The DDS profile is used in the project.<br /><ac:image><ri:attachment ri:filename="using_dds_profile_in_other_projects.png"><ri:page ri:content-title="(2026x) Importing DDS Profile and DDS Style in Other Projects" /></ri:attachment></ac:image></li></ol><h3 class="FirstParagraph">Reusing the DDS Style in non-DDS projects</h3><p class="FirstParagraph">Reusing the DDS Style in non-DDS projects</p><hr /><ol><li class="FirstParagraph">Open a non-DDS project in which you want to reuse the DDS Style.</li><li>On the main menu, select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li>In the <strong>Project Options</strong> dialog, select the <strong>Symbol Style </strong>property group.</li><li>On the right side of the dialog, click the <strong>Import</strong> button, and from the product install folder, select <em>templates/DDSStyle.stl</em>. Click <strong>Open</strong>.</li><li>Select the <strong>DDSSyle</strong> from the Symbol Styles list.</li><li>Click <strong>OK</strong>.<br />The DDS Style is used in the project.<br /><br /><ac:image><ri:attachment ri:filename="selecting_ddsStyle_in_other_projects.png"><ri:page ri:content-title="(2026x) Importing DDS Profile and DDS Style in Other Projects" /></ri:attachment></ac:image></li></ol>
````

<!--NOMAGIC_PAGE id=258048503 space=MRTCD version=1 -->
## PAGE 00070: (2026x) Importing DDS XML

- page_id: `258048503`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048503/2026x+Importing+DDS+XML
- version_number: 1
- version_date: `2025-09-24T15:29:37.002+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Getting started
- labels: ['import-dds-models-in-xml-format']

### NORMALIZED CONTENT

You can also import already existing DDS models in XML format. The imported model does not contain the diagrams associated with the models. You can use modeling tool diagram initialization to make and customize your diagrams very easily however.

To import DDS models in XML format

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select Tools > DDS > Import DDS XML.
2. In the Select DDS XML file dialog, select the DDS XML file.
3. Click Import DDS .
4. In the opened **Select Package** dialog, select the Package from the model wherein the file will be imported. 
The model defined in the XML is imported. As example see the figure below. QoS Profilescontained by the same file will not be imported. For this, you have to use the [CONFLUENCE_PAGE title='(2026x) Importing QoS Profile' space=''] to import them.

[IMAGE alt='' src='']

###### The XML file content imported into model.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can also import already existing DDS models in XML format. The imported model does not contain the diagrams associated with the models. You can use modeling tool diagram initialization to make and customize your diagrams very easily however.</p><p>To import DDS models in XML format</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main menu]]></ac:plain-text-link-body></ac:link>, select <strong>Tools</strong> &gt; <strong>DDS</strong> &gt; <strong>Import DDS XML.</strong></li><li>In the <strong>Select DDS XML file</strong> dialog, select the DDS XML file.</li><li>Click <strong>Import DDS</strong>.</li><li><p class="auto-cursor-target">In the opened <strong style="letter-spacing: 0.0px;">Select Package</strong> dialog, select the Package from the model wherein the file will be imported.<br />The model defined in the XML is imported. As example see the figure below.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="a0a739d2-8e24-4780-9d6a-b6d2956620e0"><ac:rich-text-body><p>QoS Profiles<span> contained by the same file will not be imported. For this, you have to use the <ac:link><ri:page ri:content-title="(2026x) Importing QoS Profile" /><ac:plain-text-link-body><![CDATA[Import QoS Profile feature]]></ac:plain-text-link-body></ac:link> to import them.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p class="auto-cursor-target"><ac:image ac:align="center"><ri:attachment ri:filename="importing_xml.png"><ri:page ri:content-title="(2026x) Importing DDS XML" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The XML file content imported into model.</h6>
````

<!--NOMAGIC_PAGE id=258048498 space=MRTCD version=1 -->
## PAGE 00071: (2026x) Importing QoS Profile

- page_id: `258048498`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048498/2026x+Importing+QoS+Profile
- version_number: 1
- version_date: `2025-09-24T15:29:36.916+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Getting started
- labels: ['import-qos-profile', 'reimport-qos']

### NORMALIZED CONTENT

You can import your already existing QoS Profiles in DDS XML format created with e.g. RTI System Designer, as shown in figure below.

[IMAGE alt='' src='']

To import QoS Profile

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select Tools > DDS > Import QoS Profile .
2. In the Select DDS XML file containing QoS libraries dialog, select QoS Profile.
3. Click Import QoS .
4. In the opened Select Package dialog, select the Package from the model wherein the profile will be imported.

[IMAGE alt='' src='']

If you modify the original QoS definition file, you can reimport it. Note, that the existing QoS Profiles will be replaced, so you will have to restore their assignments manually.

To reimport QoS

- Right-click the imported*UserQosRepository*element and from the shortcut menu, select the **Reimport QoS Profile**. [IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can import your already existing QoS Profiles in DDS XML format created with e.g. RTI System Designer, as shown in figure below.</p><p><ac:image><ri:attachment ri:filename="image2020-11-12_14-57-57.png"><ri:page ri:content-title="(2026x) Importing QoS Profile" /></ri:attachment></ac:image></p><p><br /></p><p>To import QoS Profile</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main menu]]></ac:plain-text-link-body></ac:link>, select <strong>Tools</strong> &gt; <strong>DDS</strong> &gt; <strong>Import QoS Profile</strong>.</li><li>In the <strong>Select DDS XML file containing QoS libraries</strong> dialog, select QoS Profile.</li><li>Click <strong>Import QoS</strong>.</li><li>In the opened <strong>Select Package</strong> dialog, select the Package from the model wherein the profile will be imported.</li></ol><p><ac:image><ri:attachment ri:filename="Import_QoS_Profile.png"><ri:page ri:content-title="(2026x) Importing QoS Profile" /></ri:attachment></ac:image><span style="letter-spacing: 0.0px;"><br /></span></p><p><span style="letter-spacing: 0.0px;"><br /></span></p><p><span style="letter-spacing: 0.0px;">If you modify the original QoS definition file, you can reimport it. Note, that t<span>he existing QoS Profiles will be replaced, so you will have to restore their assignments manually.</span></span></p><p><span style="letter-spacing: 0.0px;"><span style="letter-spacing: 0.0px;">To reimport QoS</span><br /></span></p><hr /><ul><li><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;">Right-click the imported </span><em style="letter-spacing: 0.0px;">UserQosRepository</em><span style="letter-spacing: 0.0px;"> element and from the shortcut menu, select the <strong>Reimport QoS Profile</strong>. <br /></span></p><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;"><ac:image><ri:attachment ri:filename="reimport_QoS_profile.png"><ri:page ri:content-title="(2026x) Importing QoS Profile" /></ri:attachment></ac:image><br /></span></p></li></ul>
````

<!--NOMAGIC_PAGE id=258048565 space=MRTCD version=1 -->
## PAGE 00072: (2026x) Incompatible Base Extendibility

- page_id: `258048565`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048565/2026x+Incompatible+Base+Extendibility
- version_number: 1
- version_date: `2025-09-24T15:29:38.530+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048511 space=MRTCD version=1 -->
## PAGE 00073: (2026x) Install for simulation

- page_id: `258048511`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048511/2026x+Install+for+simulation
- version_number: 1
- version_date: `2025-09-24T15:29:37.178+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Simulation with Simulink
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

<!--NOMAGIC_PAGE id=258048518 space=MRTCD version=1 -->
## PAGE 00074: (2026x) Installation

- page_id: `258048518`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048518/2026x+Installation
- version_number: 1
- version_date: `2025-09-24T15:29:37.326+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: ['installing-dds-plugin', 'install-dds-plugin']

### NORMALIZED CONTENT

Before installing Connext DDS for MagicDraw, first install RTI Connext DDS by following the instructions in its [Getting Started guide](https://www.rti.com/gettingstarted).

To install Connext DDS for MagicDraw

1. Install [CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='MDTWRT'] .
2. Install [CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='SYSMLPTWRT'] .
3. Start MagicDraw.
4. On the main menu, click Help > Resource/Plugin Manager .
5. Click Import and select the Connext DDS for MagicDraw plugin archive ( connext-dds-magicdraw-plugin.zip ).
6. After the successful installation, restart the MagicDraw.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">Before installing Connext DDS for MagicDraw, first install RTI Connext DDS by following the instructions in its <a href="https://www.rti.com/gettingstarted">Getting Started guide</a>.</p><p>To install Connext DDS for MagicDraw</p><hr /><ol><li>Install <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[MagicDraw]]></ac:plain-text-link-body></ac:link>.</li><li>Install <ac:link><ri:page ri:space-key="SYSMLPTWRT" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[SysML plugin]]></ac:plain-text-link-body></ac:link>.</li><li>Start MagicDraw.</li><li>On the main menu, click <strong>Help</strong> &gt; <strong>Resource/Plugin Manager</strong>. </li><li>Click <strong>Import</strong> and select the <em>Connext DDS for MagicDraw plugin</em> archive (<em>connext-dds-magicdraw-plugin.zip</em>).</li><li>After the successful installation, restart the MagicDraw.</li></ol>
````

<!--NOMAGIC_PAGE id=258048567 space=MRTCD version=1 -->
## PAGE 00075: (2026x) Instance not Participant

- page_id: `258048567`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048567/2026x+Instance+not+Participant
- version_number: 1
- version_date: `2025-09-24T15:29:38.591+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048569 space=MRTCD version=1 -->
## PAGE 00076: (2026x) Invalid Member Multiplicity

- page_id: `258048569`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048569/2026x+Invalid+Member+Multiplicity
- version_number: 1
- version_date: `2025-09-24T15:29:38.673+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048571 space=MRTCD version=1 -->
## PAGE 00077: (2026x) Invalid Member Type

- page_id: `258048571`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048571/2026x+Invalid+Member+Type
- version_number: 1
- version_date: `2025-09-24T15:29:38.740+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048573 space=MRTCD version=1 -->
## PAGE 00078: (2026x) Invalid Port Type

- page_id: `258048573`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048573/2026x+Invalid+Port+Type
- version_number: 1
- version_date: `2025-09-24T15:29:38.809+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048575 space=MRTCD version=1 -->
## PAGE 00079: (2026x) Invalid Repository

- page_id: `258048575`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048575/2026x+Invalid+Repository
- version_number: 1
- version_date: `2025-09-24T15:29:38.878+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048577 space=MRTCD version=1 -->
## PAGE 00080: (2026x) Invalid Topic Type Property Direction

- page_id: `258048577`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048577/2026x+Invalid+Topic+Type+Property+Direction
- version_number: 1
- version_date: `2025-09-24T15:29:38.951+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048466 space=MRTCD version=2 -->
## PAGE 00081: (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication

- page_id: `258048466`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048466/2026x+Magic+Real-Time+Communication+Designer+DDS+Real-Time+Communication
- version_number: 2
- version_date: `2025-10-30T13:47:15.998+01:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin
- labels: ['dds-real-time-communication-plugin']

### NORMALIZED CONTENT

Magic Real-Time Communication Designer / DDS Real-Time Communication plugin is an environment for editing [Connext DDS](https://www.rti.com/products/connext-dds-professional) models in a visual way.

##### Background

The OMG Data-Distribution Service for Real-Time Systems (DDS) is the first open international middleware standard directly addressing publish-subscribe communications for real-time and embedded systems.

RTI Connext DDS Professional, based on a connectivity databus, offers a robust framework for developing and integrating mission critical systems. It is fully compliant with the OMG DDS for Real-Time Systems standard.

##### Advantages

With the Connext DDS for MagicDraw plugin, you can model the DDS-related aspects of your system using UML, extended by a DDS-specific profile. This offers the following advantages:

- The overall system (from requirements to functional applications) will have a unified representation, providing a common view of the system and a single source of truth.
- You can use an already familiar modeling language.
- The DDS entities and their relationships are displayed visually in a graphical notation.

The DDS Real-Time Communication Plugin documentation consists of the following sections:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">Magic Real-Time Communication Designer / DDS Real-Time Communication plugin is an environment for editing <a href="https://www.rti.com/products/connext-dds-professional">Connext DDS</a> models in a visual way.</p><h3>Background</h3><p class="FirstParagraph">The OMG Data-Distribution Service for Real-Time Systems (DDS) is the first open international middleware standard directly addressing publish-subscribe communications for real-time and embedded systems.</p><p>RTI Connext DDS Professional, based on a connectivity databus, offers a robust framework for developing and integrating mission critical systems. It is fully compliant with the OMG DDS for Real-Time Systems standard.</p><h3>Advantages</h3><p class="FirstParagraph">With the Connext DDS for MagicDraw plugin, you can model the DDS-related aspects of your system using UML, extended by a DDS-specific profile. This offers the following advantages:</p><ul><li>The overall system (from requirements to functional applications) will have a unified representation, providing a common view of the system and a single source of truth.</li><li>You can use an already familiar modeling language.</li><li>The DDS entities and their relationships are displayed visually in a graphical notation.</li></ul><p><br /></p><p><span style="color:var(--ds-text,#333333);">The DDS Real-Time Communication Plugin documentation consists of the following sections:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="675a6e7f-bff9-4f71-809c-aa22cf1a125d" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=258048579 space=MRTCD version=1 -->
## PAGE 00082: (2026x) Missing Domain Attribute

- page_id: `258048579`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048579/2026x+Missing+Domain+Attribute
- version_number: 1
- version_date: `2025-09-24T15:29:39.045+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048581 space=MRTCD version=1 -->
## PAGE 00083: (2026x) Missing Domain ID

- page_id: `258048581`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048581/2026x+Missing+Domain+ID
- version_number: 1
- version_date: `2025-09-24T15:29:39.129+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048583 space=MRTCD version=1 -->
## PAGE 00084: (2026x) Missing Element Name

- page_id: `258048583`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048583/2026x+Missing+Element+Name
- version_number: 1
- version_date: `2025-09-24T15:29:39.207+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048585 space=MRTCD version=1 -->
## PAGE 00085: (2026x) Multiple Struct Inheritance

- page_id: `258048585`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048585/2026x+Multiple+Struct+Inheritance
- version_number: 1
- version_date: `2025-09-24T15:29:39.280+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048587 space=MRTCD version=1 -->
## PAGE 00086: (2026x) Multitype Topic

- page_id: `258048587`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048587/2026x+Multitype+Topic
- version_number: 1
- version_date: `2025-09-24T15:29:39.356+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048589 space=MRTCD version=1 -->
## PAGE 00087: (2026x) Non-Nmeric Domain ID

- page_id: `258048589`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048589/2026x+Non-Nmeric+Domain+ID
- version_number: 1
- version_date: `2025-09-24T15:29:39.435+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048591 space=MRTCD version=1 -->
## PAGE 00088: (2026x) Participant Type not Referenced

- page_id: `258048591`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048591/2026x+Participant+Type+not+Referenced
- version_number: 1
- version_date: `2025-09-24T15:29:39.512+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048550 space=MRTCD version=1 -->
## PAGE 00089: (2026x) Qos Assignments

- page_id: `258048550`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048550/2026x+Qos+Assignments
- version_number: 1
- version_date: `2025-09-24T15:29:38.075+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Home Control Example
- labels: []

### NORMALIZED CONTENT

The currents version allows three kind of QoS assignment each of which can be swiftly created with specific generic tables. Since they were already covered in previous sections we only assign one for demonstration purposes. [CONFLUENCE_PAGE title='(2026x) QoS profile assignments' space='']>]]>

As shown in the figure below, the case is a kind of a special one because the port readLight is not actually on the HomeController block but on its light port’s type called NestedLightPort. There is a validation rule which checks if the port has no connection with the given instance.

[IMAGE alt='' src='']

###### The example of Endpoint QoS Assignment Table.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The currents version allows three kind of QoS assignment each of which can be swiftly created with specific generic tables. Since they were already covered in previous sections we only assign one for demonstration purposes. <ac:link><ri:page ri:content-title="(2026x) QoS profile assignments" /><ac:plain-text-link-body><![CDATA[Learn how to create Endpoint QoS Assignment Table >>]]></ac:plain-text-link-body></ac:link></p><p>As shown in the figure below, the case is a kind of a special one because the port readLight is not actually on the HomeController block but on its light port’s type called NestedLightPort. There is a validation rule which checks if the port has no connection with the given instance.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="QoS_Assignment_table.png"><ri:page ri:content-title="(2026x) Qos Assignments" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example of Endpoint QoS Assignment Table.</h6>
````

<!--NOMAGIC_PAGE id=258048486 space=MRTCD version=1 -->
## PAGE 00090: (2026x) QoS profile assignments

- page_id: `258048486`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048486/2026x+QoS+profile+assignments
- version_number: 1
- version_date: `2025-09-24T15:29:36.749+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Getting started
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
<p class="FirstParagraph">There are three elements that QoS Profiles can be assigned to in the model:</p><ul><li class="FirstParagraph">Endpoints typed by Topic.</li><li class="FirstParagraph">DomainParticipants.</li><li class="FirstParagraph">Topics.</li></ul><p><br /></p><p>To create an empty Endpoint QoS Assignment Table</p><hr /><ol><li>In the <a href="https://docs.nomagic.com/display/MDTWRT/Containment+tab">Containment tree</a>, right-click a predefined <em>Endpoint QoS </em>Package.</li><li>From the shortcut menu, select <strong>Create Diagram </strong>and from the opened dialog, select Endpoint QoS Assignment Table.</li><li>The unnamed table is created. Type its name and press enter.</li></ol><p><br /></p><p>To fill in the Endpoint QoS Assignment Table</p><hr /><ol><li>From the table toolbar, click the <strong>Add New</strong> button. The new row appears and Endpoint QoS Assignment element is created in the model.</li><li><p class="auto-cursor-target">In the table, specify the following:<br /> - Double-click the <strong>Name</strong> cell and type Endpoint QoS Assignment name.<br /> - Double-click the <strong>QoS Profile</strong> cell, select <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="(2026x) QoS profile assignments" /></ri:attachment></ac:image></span> and in the <strong>Select Elements</strong> dialog choose QoS Profile.<br /> - Double-click the <strong>Endpoint</strong> cell, select <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="(2026x) QoS profile assignments" /></ri:attachment></ac:image></span> and in the <strong>Select Port </strong>dialog choose already created ports or use the <strong>Creation Mode</strong> to create new port.<br /> - Double-click the <strong>Domain Participant Instance</strong> cell, select <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:content-title="(2026x) QoS profile assignments" /></ri:attachment></ac:image></span> and in the <strong>Select Property </strong>dialog choose already created Part Properties or use the <strong>Creation Mode</strong> to create new Part Property.</p></li></ol><p class="FirstParagraph"><span><br /></span></p><p class="FirstParagraph"><span>Assigning QoS on subscribers/publishers is not possible since they are derived from the model and not explicitly marked.</span></p><ul><li>To assign QoS Profiles on Topics create a Topic QoS Assignment Table.<br /><ac:image><ri:attachment ri:filename="topic_qos_assignemnt_table_example.png"><ri:page ri:content-title="(2026x) QoS profile assignments" /></ri:attachment></ac:image></li><li>To assign QoS Profiles on Domain Participants create a Participant QoS Assignment Table.<br /><ac:image><ri:attachment ri:filename="participant_qos_assignment.png"><ri:page ri:content-title="(2026x) QoS profile assignments" /></ri:attachment></ac:image></li><li>To assign QoS Profiles on Endpoints create a Endpoint QoS Assignment Table.<br /><ac:image><ri:attachment ri:filename="endpoint_Qos_assignment_table.png"><ri:page ri:content-title="(2026x) QoS profile assignments" /></ri:attachment></ac:image></li></ul>
````

<!--NOMAGIC_PAGE id=258048531 space=MRTCD version=1 -->
## PAGE 00091: (2026x) Setting up the Simulink model

- page_id: `258048531`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048531/2026x+Setting+up+the+Simulink+model
- version_number: 1
- version_date: `2025-09-24T15:29:37.624+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Simulation with Simulink
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

<!--NOMAGIC_PAGE id=258048509 space=MRTCD version=1 -->
## PAGE 00092: (2026x) Simulation with Simulink

- page_id: `258048509`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048509/2026x+Simulation+with+Simulink
- version_number: 1
- version_date: `2025-09-24T15:29:37.137+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: []

### NORMALIZED CONTENT

A Simulink model can be generated from the DDS XML generated by the Matlab plugin, which can be used to simulate the behavior of the modeled DDS system.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><span lang="EN">A Simulink model can be generated from the DDS XML generated by the Matlab plugin, which can be used to simulate the behavior of the modeled DDS system.</span></p><p class="FirstParagraph"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e4ccea78-c681-4939-b6e4-a9a976eb6044" /></p>
````

<!--NOMAGIC_PAGE id=258048593 space=MRTCD version=1 -->
## PAGE 00093: (2026x) Struct Member Visibility

- page_id: `258048593`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048593/2026x+Struct+Member+Visibility
- version_number: 1
- version_date: `2025-09-24T15:29:39.590+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048595 space=MRTCD version=1 -->
## PAGE 00094: (2026x) Topic Missing from Domain

- page_id: `258048595`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048595/2026x+Topic+Missing+from+Domain
- version_number: 1
- version_date: `2025-09-24T15:29:39.662+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048538 space=MRTCD version=1 -->
## PAGE 00095: (2026x) Type mapping

- page_id: `258048538`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048538/2026x+Type+mapping
- version_number: 1
- version_date: `2025-09-24T15:29:37.783+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Simulation with Simulink
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

<!--NOMAGIC_PAGE id=258048597 space=MRTCD version=1 -->
## PAGE 00096: (2026x) Unspecified String Bounds

- page_id: `258048597`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048597/2026x+Unspecified+String+Bounds
- version_number: 1
- version_date: `2025-09-24T15:29:39.736+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048599 space=MRTCD version=1 -->
## PAGE 00097: (2026x) Unspecified String Bounds of Map Key

- page_id: `258048599`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048599/2026x+Unspecified+String+Bounds+of+Map+Key
- version_number: 1
- version_date: `2025-09-24T15:29:39.807+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048470 space=MRTCD version=1 -->
## PAGE 00098: (2026x) Unsupported Discriminator Type

- page_id: `258048470`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048470/2026x+Unsupported+Discriminator+Type
- version_number: 1
- version_date: `2025-09-24T15:29:36.483+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Validation Suite
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

<!--NOMAGIC_PAGE id=258048506 space=MRTCD version=1 -->
## PAGE 00099: (2026x) Validation

- page_id: `258048506`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048506/2026x+Validation
- version_number: 1
- version_date: `2025-09-24T15:29:37.077+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication > (2026x) Getting started
- labels: []

### NORMALIZED CONTENT

The validity of the DDS model is continuously checked by active validation rules contained in the DDS Validation Suite. For example, if you accidentally add multiple attributes to a Topic, an error is displayed. You can fix some of these DDS modeling problems by right-clicking on them and selecting the appropriate solver.

[IMAGE alt='' src='']

There is a separate validation suite for Simulink named DDS Simulink Validation Suite. It contains validation rules for data types that are not supported by Simulink. It can be activated independently from the rest of the rules.

The detailed descriptions of the validation rules are available in [CONFLUENCE_PAGE title='(2026x) Validation Suite' space=''].

[CONFLUENCE_PAGE title='Validation' space='MDTWRT']>]]>

.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><span lang="EN">The validity of the DDS model is continuously checked by active validation rules contained in the DDS Validation Suite. For example, if you accidentally add multiple attributes to a Topic, an error is displayed. You can fix some of these DDS modeling problems by right-clicking on them and selecting the appropriate solver.</span></p><p class="FirstParagraph"><span lang="EN"><ac:image><ri:attachment ri:filename="image2020-11-12_15-7-35.png"><ri:page ri:content-title="(2026x) Validation" /></ri:attachment></ac:image></span></p><p class="FirstParagraph"><br /></p><p class="FirstParagraph"><span lang="EN"><span><span>There is a separate validation suite for Simulink named DDS Simulink Validation Suite. It contains validation rules for data types that are not supported by Simulink. It can be activated independently from the rest of the rules.</span></span></span></p><p>The detailed descriptions of the validation rules are available in <ac:link><ri:page ri:content-title="(2026x) Validation Suite" /></ac:link>.</p><p><br /></p><p><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Validation" /><ac:plain-text-link-body><![CDATA[Learn more about Validation >>]]></ac:plain-text-link-body></ac:link></p><p>.</p><p class="FirstParagraph"><span lang="EN"><br /></span></p><div><span style="white-space: pre-wrap;"><br /></span></div><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=258048468 space=MRTCD version=1 -->
## PAGE 00100: (2026x) Validation Suite

- page_id: `258048468`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048468/2026x+Validation+Suite
- version_number: 1
- version_date: `2025-09-24T15:29:36.449+02:00`
- ancestors: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin > (2026x) Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: []

### NORMALIZED CONTENT

In this section are detailed descriptions of the validation rules, each page describing one.

The severity is either error or warning. Warning means that the state is not necessarily incorrect, but probably is. The implementation, qualified name, and abbreviation are given because those are the identifiers modeling tool provides for a validation rule, so this document is searchable by either. [CONFLUENCE_PAGE title='Validation' space='MDTWRT']>]]>

The list of DDS validation rules:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">In this section are detailed descriptions of the validation rules, each page describing one. </p><p>The severity is either error or warning. Warning means that the state is not necessarily incorrect, but probably is. The implementation, qualified name, and abbreviation are given because those are the identifiers modeling tool provides for a validation rule, so this document is searchable by either. <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Validation" /><ac:plain-text-link-body><![CDATA[Learn more about modeling tool validation >>]]></ac:plain-text-link-body></ac:link></p><p>The list of DDS validation rules: </p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3606a106-ac5e-449f-becd-0cbba497615c" /></p>
````

<!--NOMAGIC_PAGE id=249573264 space=MRTCD version=1 -->
## PAGE 00101: Applying DDS Sterotypes

- page_id: `249573264`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573264/Applying+DDS+Sterotypes
- version_number: 1
- version_date: `2020-11-20T10:17:19.370+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Home Control Example
- labels: []

### NORMALIZED CONTENT

First and for most we need do define the data structures and the topics which will be used in the communication. This can easily be done with a Topic Definition diagram. [CONFLUENCE_PAGE title='Defining topics and types' space='MRTCD']>]]>

Topics must contain exactly one property that has to be stereotyped with the TopicTypeProperty stereotype and has to be a type of either a Struct or Union.

[IMAGE alt='' src='']

###### The example defines three packages or DDS Modules for the three factor that we would like to measure and control.

Now that we have the data structures for the communication we can assign them to ports turning them into data writers and data readers in the DDS sense. [CONFLUENCE_PAGE title='Defining Domain Participant communication' space='MRTCD']>]]>

First we need to apply the DomainParticipant stereotypes on Blocks whose instances will be used as the individual applications in the communication. [CONFLUENCE_PAGE title='Defining Domains and Domain Participants' space='MRTCD']>]]>

[IMAGE alt='' src='']

###### The SysML BLock Definition diagram that contains all Domain Participants of Home Controller system.

After SysML model is created with the right stereotypes applied, we can define our DDS domains with them.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">First and for most we need do define the data structures and the topics which will be used in the communication. This can easily be done with a Topic Definition diagram. <ac:link><ri:page ri:space-key="MRTCD" ri:content-title="Defining topics and types" /><ac:plain-text-link-body><![CDATA[How to define topics and types >>]]></ac:plain-text-link-body></ac:link></p><p>Topics must contain exactly one property that has to be stereotyped with the TopicTypeProperty stereotype and has to be a type of either a Struct or Union.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="topic_Definition_diagram_homeControlerSystem.png"><ri:page ri:space-key="MRTCD" ri:content-title="Applying DDS Sterotypes" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example defines three packages or DDS Modules for the three factor that we would like to measure and control.</h6><p><br /></p><p>Now that we have the data structures for the communication we can assign them to ports turning them into data writers and data readers in the DDS sense. <ac:link><ri:page ri:space-key="MRTCD" ri:content-title="Defining Domain Participant communication" /><ac:plain-text-link-body><![CDATA[How to define Domain Participant communication >>]]></ac:plain-text-link-body></ac:link></p><p>First we need to apply the DomainParticipant stereotypes on Blocks whose instances will be used as the individual applications in the communication. <ac:link><ri:page ri:space-key="MRTCD" ri:content-title="Defining Domains and Domain Participants" /><ac:plain-text-link-body><![CDATA[How to define Domains and Domain Participants >>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center"><ri:attachment ri:filename="bdd_homeControlerSystem.png"><ri:page ri:space-key="MRTCD" ri:content-title="Applying DDS Sterotypes" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The SysML BLock Definition diagram that contains all Domain Participants of Home Controller system.</h6><p><br /></p><p>After  SysML model is created with the right stereotypes applied, we can define our DDS domains with them.</p>
````

<!--NOMAGIC_PAGE id=249573214 space=MRTCD version=1 -->
## PAGE 00102: Creating DDS project

- page_id: `249573214`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573214/Creating+DDS+project
- version_number: 1
- version_date: `2020-11-16T10:06:58.269+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Getting started
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
<p>To create a blank DDS project</p><hr /><ol><li><span style="color: rgb(51,51,51);">Do one of the following:<br /> </span><ul><li><span style="color: rgb(51,51,51);">Select <strong>File </strong>&gt; <strong>New</strong> <strong>Project</strong>.</span></li><li><span style="color: rgb(51,51,51);">On the main toolbar, click the <strong>New</strong> <strong>Project</strong> button.</span></li><li><span style="color: rgb(51,51,51);">Press Ctr+Shiftl+N.</span> <span style="color: rgb(51,51,51);"> <br /> </span></li></ul></li><li class="_mce_tagged_br"><span style="color: rgb(51,51,51);">In the <strong>New</strong> <strong> Project</strong> dialog, under <strong>Systems Engineering</strong>, select <strong>DDS</strong> <strong> Project</strong>.<br /> </span></li><li><span style="color: rgb(51,51,51);">Specify name and location.</span></li><li><span style="color: rgb(51,51,51);">Click <strong>OK</strong> when you are done.<br />The blank project is created and stored in your file system with defined name.<br /> <ac:image><ri:attachment ri:filename="create_new_DDS_project_steps.png"><ri:page ri:space-key="MRTCD" ri:content-title="Creating DDS project" /></ri:attachment></ac:image> </span></li></ol><p><span style="color: rgb(51,51,51);"> <br /> </span></p><p><span style="color: rgb(51,51,51);">Once you created the blank DDS Project, you can use for modeling already predefined Package structure as shown in the following figure.</span></p><h6 style="text-align: center;"><span style="color: rgb(51,51,51);"> <ac:image ac:align="center"><ri:attachment ri:filename="predefined_DDS_package_structure.png"><ri:page ri:space-key="MRTCD" ri:content-title="Creating DDS project" /></ri:attachment></ac:image> </span> <br /> <span>The predefined Package structure of blank DDS project.</span></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=249573267 space=MRTCD version=2 -->
## PAGE 00103: Creating the domain

- page_id: `249573267`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573267/Creating+the+domain
- version_number: 2
- version_date: `2025-08-19T15:31:21.815+02:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Home Control Example
- labels: []

### NORMALIZED CONTENT

The Domain can be created by using the DDS Domain Table. As shown in the following table, the Smart Home DDS Domain is created with specified its id, topics, participants and participant instances. [How to create DDS Domain Table>>](https://docs.nomagic.com/display/MRTCD/Defining+Domains+and+Domain+Participants#DefiningDomainsandDomainParticipants-CreatingDomainandDomainParticipantsbyusingtheDDSDomainTable)

[IMAGE alt='' src='']

###### The example of DDS Domain Table.

The Participant Instances derived column displays all the instances that will be in the the DDS XML.Now we are ready to export the model if we desire, but first we need to assign quality of service requirements on the DDS elements.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Domain can be created by using the <span style="color: rgb(62,63,64);">DDS Domain Table. As shown in the following table, the Smart Home DDS Domain is created with specified its id, topics, participants and participant instances. <a href="https://docs.nomagic.com/display/MRTCD/Defining+Domains+and+Domain+Participants#DefiningDomainsandDomainParticipants-CreatingDomainandDomainParticipantsbyusingtheDDSDomainTable">How to create DDS Domain Table&gt;&gt;</a></span></p><p><span style="color: rgb(62,63,64);"><ac:image ac:align="center"><ri:attachment ri:filename="domain_table.png"><ri:page ri:space-key="MRTCD" ri:content-title="Creating the domain" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">The example of DDS Domain Table.</span></h6><p class="auto-cursor-target"><span><span><span style="color: rgb(62,63,64);">The Participant Instances derived column displays all the instances that will be in the the DDS XML. </span>Now we are ready to export the model if we desire, but first we need to assign quality of service requirements on the DDS elements.</span><br /></span></p><p class="auto-cursor-target"><span><br /></span></p><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=249573234 space=MRTCD version=1 -->
## PAGE 00104: Defining Domain Participant communication

- page_id: `249573234`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573234/Defining+Domain+Participant+communication
- version_number: 1
- version_date: `2020-11-20T10:13:12.084+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Getting started
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
<p>Communication between DDS elements is determined by ports owned by Domain Participants. Ports that are parts of the communication has to have DDS Endpoint stereotype otherwise they will be omitted.</p><p><br /></p><p>To apply DDS Endpoint stereotype on a port</p><hr /><ol><li>Right-click the port and from the shortcut menu, select Stereotype.</li><li>In the opened dialog, select DDS Endpoint. </li><li>Click <strong>Apply</strong>.</li></ol><p><br /></p><p>The derived direction of ports determine whether they are considered Data Reader or Data Writers. In case of non-nested ports the publishers and subscribers which contain the Data Readers or Writers are implicitly defined under the Domain Participants. Publishers and Subscribers in DDS group Data Readers and Writers.</p><p>Nested ports can be used to group Data Writers and Readers. The grouping is determined by the ports highest in the hierarchy (direct children of the Block). Note that non-nested ports must have a type of Topic.</p><p><span>In between ports have no effective meaning.</span></p><p><span>In case of </span>nested ports<span>, ports highest in the hierarchy implicitly define </span>subscribers<span> and </span>publishers<span> as well.</span></p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="image2020-11-12_14-1-30.png"><ri:page ri:space-key="MRTCD" ri:content-title="Defining Domain Participant communication" /></ri:attachment></ac:image></p><p><span><br /></span></p><p><br /></p><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=249573225 space=MRTCD version=1 -->
## PAGE 00105: Defining Domains and Domain Participants

- page_id: `249573225`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573225/Defining+Domains+and+Domain+Participants
- version_number: 1
- version_date: `2020-12-01T13:30:31.611+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Getting started
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

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MDTWRT'] , right-click a Package wherein you want to create Domain Participants or Domain.
2. From the shortcut menu, select Create Element and from the opened dialog, select DomainParticipant or Domain.
3. The unnamed element is created. Type its name and press enter. [ATTACHMENT filename='domain_participant_and_domain_in_containment_tree.png']

##### Creating Domain and Domain Participants by using the DDS Domain Table

You can use the DDS Domain Table to create a Domain inside a Domain Library. It also helps to assign Topics and Domain Participants to the Domain. The DDS Domain Table named Domain is already created in predefined DDS Package structure. If you want to create a new one, follow the procedure below.

To create an empty DDS Domain Table

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MDTWRT'] , right-click a predefined Domain Package.
2. From the shortcut menu, select Create Diagram and from the opened dialog, select DDS Domain Table.
3. The unnamed table is created. Type its name and press enter.

To fill in the DDS Domain Table

1. From the table toolbar, click the Add New button. The new row appears and DDSDomain element is created in the model.
2. In the table, specify the following: 
 - Double-click **Name** cell and type a domain name. 
 - Double-click the **Domain_id** cell and type domain id number. 
 - Double-click the **Topics** cell, select [IMAGE alt='' src=''] and in the **Select Elements** dialog choose already created topics or use the **Creation Mode** to create new topics. Topics referenced by a Domain Participants must be assigned to every Domain that the participant is assigned to. Unassigned Topics lead to validation errors. - Double-click the **Participants** cell, select [IMAGE alt='' src=''] and in the **Select Elements** dialog choose already created Domain Participants or use the **Creation Mode** to create new Domain Participants. 
 - The **Participant Instances** column fill in automatically when instances are created in the model. >]]>[CONFLUENCE_PAGE title='Defining Domains and Domain Participants' space='MRTCD'] 
[IMAGE alt='' src='']

##### Creating Domain Participants by refactoring the Block

To create a Domain Participant or Domain by refactoring a Block

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MDTWRT'] , right-click a Package wherein you want to create Domain Participants or Domain.
2. From the shortcut menu, select Create Element and from the opened dialog, select Block.
3. Right-click the Block and select Refactor > Convert To > More Specific > Domain Participant or Domain . The Block is refactored to the Domain Participant or Domain.

[IMAGE alt='' src='']

##### Creating instances

The difference between instances of Domain Participants and Members of DDS Data types are the following:

- Domain Participant instances: are any Block property typed by Domain Participant. They can be any kid of property: Value Property, Part Property, Reference Property etc. 
 - Members: DDS Data type Members are used in the data definition section of the meta-model. They allow to define custom, DDS annotated data types. They rely heavily on multiplicity definitions in order to be able to produce a syntactically correct DDS xml output.

To create a Domain Participant instances

1. In the [CONFLUENCE_PAGE title='Containment tab' space='MDTWRT'] , right-click a Block which will be the owner of the instances.
2. From the shortcut menu, select Create Diagram and from the opened dialog, select SysML Internal Block Diagram.
3. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] select a property (e.g. Part Property) and click on the diagram pane.
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

1. Double-click the Part Property to open it's [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] .
2. Select the Multiplicity property value or type Lower Value and Upper Value.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>All Domain Participants are assigned to the Domain regardless of where they are in the containment hierarchy. Domain Participants should have at least one instance which can be any kind of lock property typed by Domain Participant. During DDS XML generation, all properties of the Block are considered a Domain Participants.</p><p>You can create Domain and Domain Participants by using:</p><ul><li>The Containment tree.</li><li>DDS Domain Table.</li></ul><p>This page contains the following topics:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="e20bb792-47ca-49f9-8f77-b9d92eb13d0b"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p><div><p><br /></p><h3>Creating Domain and Domain Participants by using the Containment tree</h3><p><br /></p><p>To create a Domain Participant or Domain in the Containment tree</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a Package wherein you want to create Domain Participants or Domain.</li><li>From the shortcut menu, select <strong>Create Element </strong>and from the opened dialog, select DomainParticipant or Domain.</li><li>The unnamed element is created. Type its name and press enter.<br /><ac:image><ri:attachment ri:filename="domain_participant_and_domain_in_containment_tree.png"><ri:page ri:space-key="MRTCD" ri:content-title="Defining Domains and Domain Participants" /></ri:attachment></ac:image></li></ol><h3>Creating Domain and Domain Participants by using the DDS Domain Table</h3><p>You can use the DDS Domain Table to create a Domain inside a Domain Library. It also helps to assign Topics and Domain Participants to the Domain. The DDS Domain Table named Domain is already created in predefined DDS Package structure. If you want to create a new one, follow the procedure below.</p><p>To create an empty DDS Domain Table</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a predefined <em>Domain</em> Package.</li><li>From the shortcut menu, select <strong>Create Diagram </strong>and from the opened dialog, select DDS Domain Table.</li><li>The unnamed table is created. Type its name and press enter.</li></ol><p><br /></p><p>To fill in the DDS Domain Table</p><hr /><ol><li>From the table toolbar, click the <strong>Add New</strong> button. The new row appears and DDSDomain element is created in the model.</li><li><p class="auto-cursor-target">In the table, specify the following:<br /> - Double-click <strong>Name</strong> cell and type a domain name.<br /> - Double-click the <strong>Domain_id</strong> cell and type domain id number.<br /> - Double-click the <strong>Topics</strong> cell, select <ac:image ac:title="Edit" ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="MRTCD" ri:content-title="Defining Domains and Domain Participants" /></ri:attachment></ac:image> and in the <strong>Select Elements</strong> dialog choose already created topics or use the <strong>Creation Mode</strong> to create new topics.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="ccea59d8-2dd6-47db-a1e2-75bba1a8ff67"><ac:rich-text-body><p>Topics referenced by a Domain Participants must be assigned to every Domain that the participant is assigned to. Unassigned Topics lead to validation errors.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"> - Double-click the <strong>Participants</strong> cell, select <ac:image ac:title="Edit" ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="MRTCD" ri:content-title="Defining Domains and Domain Participants" /></ri:attachment></ac:image> and in the <strong>Select Elements</strong> dialog choose already created Domain Participants or use the <strong>Creation Mode</strong> to create new Domain Participants.<br /> - The <strong>Participant Instances</strong> column fill in automatically when instances are created in the model. <ac:link ac:anchor="Creating instances of Domain Participants"><ac:plain-text-link-body><![CDATA[How to create Participant Instances >>]]></ac:plain-text-link-body><ri:page ri:space-key="MRTCD" ri:content-title="Defining Domains and Domain Participants" /></ac:link><br /><ac:image><ri:attachment ri:filename="DDSDomain_table.png"><ri:page ri:space-key="MRTCD" ri:content-title="Defining Domains and Domain Participants" /></ri:attachment></ac:image></p></li></ol><h3>Creating Domain Participants by refactoring the Block</h3><p><br /></p><p>To create a Domain Participant or Domain by refactoring a Block</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a Package wherein you want to create Domain Participants or Domain.</li><li>From the shortcut menu, select <strong>Create Element </strong>and from the opened dialog, select Block.</li><li>Right-click the Block and select <strong>Refactor</strong> &gt; <strong>Convert To</strong> &gt; <strong>More Specific</strong> &gt; <strong>Domain Participant</strong> or <strong>Domain</strong>.<br />The Block is refactored to the Domain Participant or Domain.</li></ol><p><ac:image><ri:attachment ri:filename="Block_refactor_to_domain_participant.png"><ri:page ri:space-key="MRTCD" ri:content-title="Defining Domains and Domain Participants" /></ri:attachment></ac:image></p><h3>Creating instances </h3><p>The difference between instances of Domain Participants and Members of DDS Data types are the following:</p><p>   - Domain Participant instances: are any Block property typed by Domain Participant. They can be any kid of property: Value Property, Part Property, Reference Property etc.<br />    - Members: DDS Data type Members are used in the data definition section of the meta-model. They allow to define custom, DDS annotated data types. They rely heavily on multiplicity definitions in order to be able to produce a syntactically correct DDS xml output.<br /><br /></p><p>To create a Domain Participant instances</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click a Block which will be the owner of the instances.</li><li>From the shortcut menu, select <strong>Create Diagram </strong>and from the opened dialog, select SysML Internal Block Diagram.</li><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram palette]]></ac:plain-text-link-body></ac:link> select a property (e.g. Part Property) and click on the diagram pane.</li><li>Type the name of the property.</li><li>Select a Domain Participant as type of the property.<br />The instance of Domain Participant is created.<br /><br /><ac:image><ri:attachment ri:filename="instances_of_domain_participants.png"><ri:page ri:space-key="MRTCD" ri:content-title="Defining Domains and Domain Participants" /></ri:attachment></ac:image></li></ol><h3>Defining instances multiplicity</h3></div><p>To define a instances as an array or sequence, its multiplicity needs to be changed as it follows, where N must be at least 1 and M must be greater than N.</p><table><colgroup><col /><col /><col /><col /><col /></colgroup><tbody><tr><td colspan="2"><p class="Compact"><strong>Lower Value</strong></p></td><td><p class="Compact"><strong>Upper Value</strong></p></td><td><p class="Compact"><strong>Multiplicity</strong></p></td><td><p class="Compact"><strong>Type</strong></p></td></tr><tr><td colspan="2"><p>N</p></td><td><p>N</p></td><td><p>N</p></td><td><p>Array</p></td></tr><tr><td colspan="2"><p>0</p></td><td><p>-1</p></td><td><p>0 .. *</p></td><td><p>Boundless Array</p></td></tr><tr><td colspan="2"><p>0</p></td><td><p>N-1</p></td><td><p>0 .. N-1</p></td><td><p>Sequence</p></td></tr><tr><td colspan="2"><p>N</p></td><td><p>M</p></td><td><p>N .. M</p></td><td><p>Sequence</p></td></tr></tbody></table><p><br /></p><p>To change the instance multiplicity</p><hr /><ol><li>Double-click the Part Property to open it's <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>.</li><li>Select the Multiplicity property value or type Lower Value and Upper Value.</li></ol><p><ac:image><ri:attachment ri:filename="members_multiplicity.png"><ri:page ri:space-key="MRTCD" ri:content-title="Defining Domains and Domain Participants" /></ri:attachment></ac:image></p><p class="Compact"><br /></p>
````

<!--NOMAGIC_PAGE id=249573221 space=MRTCD version=1 -->
## PAGE 00106: Defining topics and types

- page_id: `249573221`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573221/Defining+topics+and+types
- version_number: 1
- version_date: `2020-11-21T05:18:09.720+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Getting started
- labels: ['define-topics', 'define-types', 'create-dds-topic-definition-diagram']

### NORMALIZED CONTENT

You can define topic and types used by them in the DDS Topic Definition Diagram.

[IMAGE alt='' src='']

###### The example of the DDS Topic Definition Diagram where main elements are highlighed: DDS Module, Types and Topic.

##### Creating DDS Topic Definition Diagram

After a blank DDS Project is created, the predefined package structure is prepared where the DDS Topic Definition Diagram is already created under the *Topics* Package named *Topics*. It contains an empty DDS Module. If you need another one, create it manually, as described in the following procedure.

To create blank DDS Topic Definition Diagram

1. In the [CONFLUENCE_PAGE title='Model Browser' space='MDTWRT'] , select the owner for the new diagram.
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

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select a type you need and click on DDS Module element.
2. Type its name.
3. Click the Create Member [CONFLUENCE_PAGE title='Smart manipulators' space='MDTWRT'] to create a Members for the type.
4. Select newly created Member on the shape, click [ATTACHMENT filename='specify_type.png'] and select a type for a it.

Creating and defining topics

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select a Topic and click on the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] .
2. Type its name.
3. Click the Create Element [CONFLUENCE_PAGE title='Smart manipulators' space='MDTWRT'] to create a Topic Type Property or Reception for the Topic.
4. Select newly created Topic Type Property or Reception, click [IMAGE alt='' src='']and select a type for a it. Press Ctrl+Space to search among the available types.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can define topic and types <span style="color: rgb(62,63,64);">used by them</span> in the DDS Topic Definition Diagram.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="DDS_Topic_Definition_Diagram.png"><ri:page ri:space-key="MRTCD" ri:content-title="Defining topics and types" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example of the DDS Topic Definition Diagram where main elements are highlighed: DDS Module, Types and Topic.</h6><h3>Creating DDS Topic Definition Diagram</h3><p>After a blank DDS Project is created, the predefined package structure is prepared where the DDS Topic Definition Diagram is already created under the <em>Topics</em> Package named <em>Topics</em>. It contains an empty DDS Module. If you need another one, create it manually, as described in the following procedure.</p><p>To create blank DDS Topic Definition Diagram</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Model Browser" /></ac:link>, select the owner for the new diagram.</li><li>Do one of the following:<br /><ul><li>Right-click the Package, and from the shortcut menu select <strong>Create Diagram.</strong></li><li>Press Ctrl+N.</li><li>On the main toolbar, click <span class="confluence-embedded-file-wrapper"><ac:image ac:alt="Create Diagram"><ri:attachment ri:filename="create_diagram.png"><ri:page ri:space-key="MRTCD" ri:content-title="Defining topics and types" /></ri:attachment></ac:image></span> .</li><li>From the main menu, select <strong>Diagrams</strong> &gt; <strong>Create Diagram</strong>.</li></ul></li><li><p>In the <strong>Create Diagram</strong> box, under <strong>General</strong> diagram group, select the <strong>DDS Topic Definition Diagram</strong>.</p></li></ol><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="8fa80951-960a-4327-aedd-357ca62fe7c8"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">Press Esc or click outside the dialog to close the diagram creation dialog without creating the diagram.</span></p></ac:rich-text-body></ac:structured-macro><h3>Defining topics and types</h3><p>You can create the following types:</p><ul><li>Struct Type</li><li>Union Type</li><li>Bitmask Type</li><li>Enumeration Type</li><li>Map Type</li><li>Alias Type</li><li>Annotation Type</li></ul><p><br /></p><p>Creating and defining types</p><hr /><ol><li>From the<ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[ diagram palette]]></ac:plain-text-link-body></ac:link>, select a type you need and click on DDS Module element. </li><li>Type its name.</li><li>Click the <strong>Create Member</strong> <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Smart manipulators" /><ac:plain-text-link-body><![CDATA[smart manipulator]]></ac:plain-text-link-body></ac:link> to create a Members for the type.</li><li>Select newly created Member on the shape, click <ac:image ac:title="Specify Type" ac:alt="Specify Type"><ri:attachment ri:filename="specify_type.png"><ri:page ri:space-key="MRTCD" ri:content-title="Defining topics and types" /></ri:attachment></ac:image> and select a type for a it.</li></ol><p><br /></p><p>Creating and defining topics</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram palette]]></ac:plain-text-link-body></ac:link>, select a Topic and click on the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram pane]]></ac:plain-text-link-body></ac:link>. </li><li>Type its name.</li><li>Click the <strong>Create Element</strong> <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Smart manipulators" /><ac:plain-text-link-body><![CDATA[smart manipulator]]></ac:plain-text-link-body></ac:link> to create a Topic Type Property or Reception for the Topic.</li><li><p class="auto-cursor-target">Select newly created Topic Type Property or Reception, click <ac:image ac:title="Specify Type" ac:alt="Specify Type"><ri:attachment ri:filename="specify_type.png"><ri:page ri:space-key="MRTCD" ri:content-title="Defining topics and types" /></ri:attachment></ac:image>and select a type for a it.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="f4ba630b-5037-4766-aa0d-f65b82385bbb"><ac:rich-text-body><p>Press Ctrl+Space to search among the available types.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><br /></p><p class="Compact">              </p><p class="Compact"><br /></p>
````

<!--NOMAGIC_PAGE id=249573273 space=MRTCD version=1 -->
## PAGE 00107: Domain not in Library

- page_id: `249573273`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573273/Domain+not+in+Library
- version_number: 1
- version_date: `2020-11-20T13:40:26.614+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573274 space=MRTCD version=1 -->
## PAGE 00108: Domain Participant without Instance

- page_id: `249573274`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573274/Domain+Participant+without+Instance
- version_number: 1
- version_date: `2020-11-20T13:40:05.429+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573275 space=MRTCD version=1 -->
## PAGE 00109: Duplicate Domain ID

- page_id: `249573275`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573275/Duplicate+Domain+ID
- version_number: 1
- version_date: `2020-11-20T13:39:52.148+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573276 space=MRTCD version=1 -->
## PAGE 00110: Endpoint not Referenced

- page_id: `249573276`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573276/Endpoint+not+Referenced
- version_number: 1
- version_date: `2020-11-20T13:39:38.629+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573256 space=MRTCD version=1 -->
## PAGE 00111: Environment setup

- page_id: `249573256`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573256/Environment+setup
- version_number: 1
- version_date: `2020-11-19T15:15:52.545+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Simulation with Simulink
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

<!--NOMAGIC_PAGE id=249573262 space=MRTCD version=1 -->
## PAGE 00112: Example Model

- page_id: `249573262`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573262/Example+Model
- version_number: 1
- version_date: `2020-11-20T10:05:03.532+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Home Control Example
- labels: []

### NORMALIZED CONTENT

HomeControler.mdzip contains a model that describes a system that consists of an air conditioner unit, a dehumidifiers, shutters and a light sensor. The air conditioner and the dehumidifier both contain a controller and a sensor component. The system is supervised by the Home Controller whose main responsibility is to monitor data received from the components and to control them.

[IMAGE alt='' src='']

###### The SysmL Internal Block Diagram of Home Controller environment.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">HomeControler.mdzip contains a model that describes a system that consists of an air conditioner unit, a dehumidifiers, shutters and a light sensor. The air conditioner and the dehumidifier both contain a controller and a sensor component. The system is supervised by the Home Controller whose main responsibility is to monitor data received from the components and to control them.</p><p class="FirstParagraph"><ac:image ac:align="center"><ri:attachment ri:filename="ibd_homeControlerSystem.png"><ri:page ri:space-key="MRTCD" ri:content-title="Example Model" /></ri:attachment></ac:image></p><h6 class="FirstParagraph" style="text-align: center;">The SysmL Internal Block Diagram of Home Controller environment.</h6>
````

<!--NOMAGIC_PAGE id=249573271 space=MRTCD version=2 -->
## PAGE 00113: Exporting DDS Control Example to XML

- page_id: `249573271`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573271/Exporting+DDS+Control+Example+to+XML
- version_number: 2
- version_date: `2025-08-19T15:31:21.902+02:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Home Control Example
- labels: []

### NORMALIZED CONTENT

You can export the DDS examples to XML. For this, follow the procedures provided in the page [Exporting DDS XML](https://docs.nomagic.com/display/MRTCD/Exporting+DDS+XML).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can export the DDS examples to XML. For this, follow the procedures provided in the page <a class="current" style="letter-spacing: 0.0px;" href="https://docs.nomagic.com/display/MRTCD/Exporting+DDS+XML">Exporting DDS XML</a>.</p><p><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=249573242 space=MRTCD version=1 -->
## PAGE 00114: Exporting DDS XML

- page_id: `249573242`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573242/Exporting+DDS+XML
- version_number: 1
- version_date: `2021-09-21T09:00:47.575+02:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Getting started
- labels: ['generate-dds-xml']

### NORMALIZED CONTENT

You can generate DDS xml file directly from the modeling tool. Referenced QoS profiles are included in the resulting XML. Before the export a pre-check is initiated to ensure that the QoS Profiles imported to modeling tool were not changed and still up to date. You can use the resulting XML in the **RTI DDS Code Generator**, **RTI System Designer**, the **DDS Simulink Tooling** or other standards-compliant tool.

To generate DDS XML

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select Tools > DDS > Generate DDS XML .
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
<p>You can generate DDS xml file directly from the modeling tool. Referenced QoS profiles are included in the resulting XML. Before the export a pre-check is initiated to ensure that the QoS Profiles imported to modeling tool were not changed and still up to date. You can use the resulting XML in the <strong style="letter-spacing: 0.0px;">RTI DDS Code Generator</strong>, <strong style="letter-spacing: 0.0px;">RTI System Designer</strong>, the <strong style="letter-spacing: 0.0px;">DDS Simulink Tooling</strong> or other standards-compliant tool.</p><p><br /></p><p>To generate DDS XML</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main menu]]></ac:plain-text-link-body></ac:link>, select <strong>Tools </strong>&gt; <strong>DDS</strong> &gt; <strong>Generate DDS XML</strong>.</li><li>In the <strong style="letter-spacing: 0.0px;">Generate DDS XML</strong><span style="letter-spacing: 0.0px;"> dialog, select the following:</span><span style="letter-spacing: 0.0px;"><br /></span></li></ol><p class="auto-cursor-target"> -<strong> Select Scope</strong> - select a Package which content you want to export. Click <strong>Next</strong>.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="72fbaaef-7a44-4b88-9f40-a83af6e3bbaa"><ac:rich-text-body><p><span>To ensure that the exported XML is valid, make sure the selected package contains at least one domain participant library containing at least one Domain Participant. Otherwise, the tool takes care of the validity of references by including the elements referred from the selected package even if they are outside the selected Package.</span></p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="select_scope.png"><ri:page ri:space-key="MRTCD" ri:content-title="Exporting DDS XML" /></ri:attachment></ac:image></p><p class="auto-cursor-target"> - <strong>Select target version</strong> - select DDS target version. Click <strong>Next</strong>.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="75827afe-6c50-4001-a769-860dc4e01ba3"><ac:rich-text-body><p>QoS Profiles between versions are not compatible. QoS Profiles with a version that is not matching with the target version selected it the wizard will prevent the export.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="select_target_version.png"><ri:page ri:space-key="MRTCD" ri:content-title="Exporting DDS XML" /></ri:attachment></ac:image><br /> - <strong>Select output directory</strong> - select the location of exported DDS XML file. Click <strong>Finish</strong>.<br /><br /><ac:image><ri:attachment ri:filename="select_output_directory.png"><ri:page ri:space-key="MRTCD" ri:content-title="Exporting DDS XML" /></ri:attachment></ac:image><br />The DDS XML file is generated.</p><p><br /><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=249573257 space=MRTCD version=1 -->
## PAGE 00115: Generating the Simulink model

- page_id: `249573257`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573257/Generating+the+Simulink+model
- version_number: 1
- version_date: `2020-11-19T15:20:32.932+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Simulation with Simulink
- labels: []

### NORMALIZED CONTENT

After the initialization step you can generate Simulink models using the LoadSimulinkModel.m script.

To generate the Simulink models

1. Run LoadSimulinkModel.
2. Select the desired xml you want to generate from. The xml gets copied to the matlab workspace, and the generation starts. After the generation finishes (assuming that you used the example Thermostat.xml) the workspace should look like this: [ATTACHMENT filename='image2020-11-12_15-12-49.png']
3. Open <your_model>.slx.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">After the initialization step you can generate Simulink models using the LoadSimulinkModel.m script.</p><p class="FirstParagraph"><br /></p><p class="FirstParagraph">To generate the Simulink models</p><hr /><ol><li>Run LoadSimulinkModel.</li><li>Select the desired xml you want to generate from. The xml gets copied to the matlab workspace, and the generation starts. After the generation finishes (assuming that you used the example Thermostat.xml) the workspace should look like this:<br /><ac:image><ri:attachment ri:filename="image2020-11-12_15-12-49.png"><ri:page ri:space-key="MRTCD" ri:content-title="Generating the Simulink model" /></ri:attachment></ac:image></li><li>Open &lt;your_model&gt;.slx.</li></ol><p class="FirstParagraph"><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=249573213 space=MRTCD version=1 -->
## PAGE 00116: Getting started

- page_id: `249573213`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573213/Getting+started
- version_number: 1
- version_date: `2020-11-21T05:14:05.241+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: []

### NORMALIZED CONTENT

**Welcome!**This user guide will walk you through the basics of using DDS Real-Time Communication Plugin, including working with projects, setting up the modeling environment, defining DDS elements, importing and exporting XML files, and more.

Use the search box to find a specific topic or select one from the list below:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Welcome!</strong><span style="color: rgb(62,63,64);"> This user guide will walk you through the basics of using DDS Real-Time Communication Plugin, including working with projects, setting up the modeling environment</span><span style="color: rgb(62,63,64);">, defining DDS elements, importing and exporting XML files, and more.</span></p><p><span style="color: rgb(62,63,64);">Use the search box to find a specific topic or select one from the list below</span><span class="confluence-link" style="color: rgb(62,63,64);">:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="60201284-9a7d-44b0-812b-445cfcf90c54" /></p>
````

<!--NOMAGIC_PAGE id=249573261 space=MRTCD version=1 -->
## PAGE 00117: Home Control Example

- page_id: `249573261`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573261/Home+Control+Example
- version_number: 1
- version_date: `2020-11-20T05:37:34.561+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: []

### NORMALIZED CONTENT

The aim of this example is to demonstrate how to make models using DDS and SysML semantics, how to assign quality of service profiles. Also it provides information how to generate RTI Connext DDS model in XML format that can be used in various ways like for the RTI Connext code generator or for generating MATLAB Simulink models.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><span lang="EN">The aim of this example is to demonstrate how to make models using DDS and SysML semantics, how to assign quality of service profiles. Also it provides information how to generate RTI Connext DDS model in XML format that can be used in various ways like for the RTI Connext code generator or for generating MATLAB Simulink models.</span></p><p class="FirstParagraph"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="cfb9a75d-74f0-4ba6-97ca-91ec209cd98e" /></p>
````

<!--NOMAGIC_PAGE id=249573277 space=MRTCD version=1 -->
## PAGE 00118: Illegal Inheritance

- page_id: `249573277`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573277/Illegal+Inheritance
- version_number: 1
- version_date: `2020-11-20T13:40:52.102+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573217 space=MRTCD version=1 -->
## PAGE 00119: Importing DDS Profile and DDS Style in Other Projects

- page_id: `249573217`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573217/Importing+DDS+Profile+and+DDS+Style+in+Other+Projects
- version_number: 1
- version_date: `2020-11-16T06:01:26.585+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Getting started
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
<p class="FirstParagraph">The created DDS projects already have the DDS profile imported and DDS Style set. You ca reuse them in non-DDs projects. </p><p class="FirstParagraph"><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="3c27f29d-5174-4870-87d5-2a8fd1589241" /></p><h3 class="FirstParagraph">Reusing the DDS profile in non-DDS projects</h3><p class="FirstParagraph">Reusing the DDS profile in non-DDS projects</p><hr /><ol><li class="FirstParagraph">Open a non-DDS project in which you want to reuse the DDS profile.</li><li class="FirstParagraph">On the main menu, select <strong>File</strong> &gt; <strong>Use Project</strong> &gt; <strong>Use Local Project.</strong></li><li class="FirstParagraph">In the opened <strong>Use Project</strong> dialog, you can select the DDS profile either: <br /> - From predefined location. Select the <strong>Paths to used projects</strong>: &lt;install.root&gt;\profiles and from the list below, select the <em>dds_profile.mdzip</em>.<br /> - From File system. Click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="three_dot_button.png"><ri:page ri:space-key="MRTCD" ri:content-title="Importing DDS Profile and DDS Style in Other Projects" /></ri:attachment></ac:image> and from the product install folder, select <em>profiles/dds_profile.mdzip</em>. Click <strong>Open</strong>.</li><li class="FirstParagraph">Click <strong>Next</strong> &gt; <strong>Finish</strong>.<br />The DDS profile is used in the project.<br /><ac:image><ri:attachment ri:filename="using_dds_profile_in_other_projects.png"><ri:page ri:space-key="MRTCD" ri:content-title="Importing DDS Profile and DDS Style in Other Projects" /></ri:attachment></ac:image></li></ol><h3 class="FirstParagraph">Reusing the DDS Style in non-DDS projects</h3><p class="FirstParagraph">Reusing the DDS Style in non-DDS projects</p><hr /><ol><li class="FirstParagraph">Open a non-DDS project in which you want to reuse the DDS Style.</li><li>On the main menu, select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li>In the <strong>Project Options</strong> dialog, select the <strong>Symbol Style </strong>property group.</li><li>On the right side of the dialog, click the <strong>Import</strong> button, and from the product install folder, select <em>templates/DDSStyle.stl</em>. Click <strong>Open</strong>.</li><li>Select the <strong>DDSSyle</strong> from the Symbol Styles list.</li><li>Click <strong>OK</strong>.<br />The DDS Style is used in the project.<br /><br /><ac:image><ri:attachment ri:filename="selecting_ddsStyle_in_other_projects.png"><ri:page ri:space-key="MRTCD" ri:content-title="Importing DDS Profile and DDS Style in Other Projects" /></ri:attachment></ac:image></li></ol>
````

<!--NOMAGIC_PAGE id=249573250 space=MRTCD version=1 -->
## PAGE 00120: Importing DDS XML

- page_id: `249573250`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573250/Importing+DDS+XML
- version_number: 1
- version_date: `2021-09-21T09:03:26.043+02:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Getting started
- labels: ['import-dds-models-in-xml-format']

### NORMALIZED CONTENT

You can also import already existing DDS models in XML format. The imported model does not contain the diagrams associated with the models. You can use modeling tool diagram initialization to make and customize your diagrams very easily however.

To import DDS models in XML format

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select Tools > DDS > Import DDS XML.
2. In the Select DDS XML file dialog, select the DDS XML file.
3. Click Import DDS .
4. In the opened **Select Package** dialog, select the Package from the model wherein the file will be imported. 
The model defined in the XML is imported. As example see the figure below. QoS Profilescontained by the same file will not be imported. For this, you have to use the [CONFLUENCE_PAGE title='Importing QoS Profile' space='MRTCD'] to import them.

[IMAGE alt='' src='']

###### The XML file content imported into model.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can also import already existing DDS models in XML format. The imported model does not contain the diagrams associated with the models. You can use modeling tool diagram initialization to make and customize your diagrams very easily however.</p><p>To import DDS models in XML format</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main menu]]></ac:plain-text-link-body></ac:link>, select <strong>Tools</strong> &gt; <strong>DDS</strong> &gt; <strong>Import DDS XML.</strong></li><li>In the <strong>Select DDS XML file</strong> dialog, select the DDS XML file.</li><li>Click <strong>Import DDS</strong>.</li><li><p class="auto-cursor-target">In the opened <strong style="letter-spacing: 0.0px;">Select Package</strong> dialog, select the Package from the model wherein the file will be imported.<br />The model defined in the XML is imported. As example see the figure below.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="a0a739d2-8e24-4780-9d6a-b6d2956620e0"><ac:rich-text-body><p>QoS Profiles<span> contained by the same file will not be imported. For this, you have to use the <ac:link><ri:page ri:space-key="MRTCD" ri:content-title="Importing QoS Profile" /><ac:plain-text-link-body><![CDATA[Import QoS Profile feature]]></ac:plain-text-link-body></ac:link> to import them.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p class="auto-cursor-target"><ac:image ac:align="center"><ri:attachment ri:filename="importing_xml.png"><ri:page ri:space-key="MRTCD" ri:content-title="Importing DDS XML" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The XML file content imported into model.</h6>
````

<!--NOMAGIC_PAGE id=249573246 space=MRTCD version=1 -->
## PAGE 00121: Importing QoS Profile

- page_id: `249573246`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573246/Importing+QoS+Profile
- version_number: 1
- version_date: `2021-09-21T09:02:36.448+02:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Getting started
- labels: ['import-qos-profile', 'reimport-qos']

### NORMALIZED CONTENT

You can import your already existing QoS Profiles in DDS XML format created with e.g. RTI System Designer, as shown in figure below.

[IMAGE alt='' src='']

To import QoS Profile

1. From the [CONFLUENCE_PAGE title='Understanding the user interface' space='MDTWRT'] , select Tools > DDS > Import QoS Profile .
2. In the Select DDS XML file containing QoS libraries dialog, select QoS Profile.
3. Click Import QoS .
4. In the opened Select Package dialog, select the Package from the model wherein the profile will be imported.

[IMAGE alt='' src='']

If you modify the original QoS definition file, you can reimport it. Note, that the existing QoS Profiles will be replaced, so you will have to restore their assignments manually.

To reimport QoS

- Right-click the imported*UserQosRepository*element and from the shortcut menu, select the **Reimport QoS Profile**. [IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can import your already existing QoS Profiles in DDS XML format created with e.g. RTI System Designer, as shown in figure below.</p><p><ac:image><ri:attachment ri:filename="image2020-11-12_14-57-57.png"><ri:page ri:space-key="MRTCD" ri:content-title="Importing QoS Profile" /></ri:attachment></ac:image></p><p><br /></p><p>To import QoS Profile</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main menu]]></ac:plain-text-link-body></ac:link>, select <strong>Tools</strong> &gt; <strong>DDS</strong> &gt; <strong>Import QoS Profile</strong>.</li><li>In the <strong>Select DDS XML file containing QoS libraries</strong> dialog, select QoS Profile.</li><li>Click <strong>Import QoS</strong>.</li><li>In the opened <strong>Select Package</strong> dialog, select the Package from the model wherein the profile will be imported.</li></ol><p><ac:image><ri:attachment ri:filename="Import_QoS_Profile.png"><ri:page ri:space-key="MRTCD" ri:content-title="Importing QoS Profile" /></ri:attachment></ac:image><span style="letter-spacing: 0.0px;"><br /></span></p><p><span style="letter-spacing: 0.0px;"><br /></span></p><p><span style="letter-spacing: 0.0px;">If you modify the original QoS definition file, you can reimport it. Note, that t<span>he existing QoS Profiles will be replaced, so you will have to restore their assignments manually.</span></span></p><p><span style="letter-spacing: 0.0px;"><span style="letter-spacing: 0.0px;">To reimport QoS</span><br /></span></p><hr /><ul><li><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;">Right-click the imported </span><em style="letter-spacing: 0.0px;">UserQosRepository</em><span style="letter-spacing: 0.0px;"> element and from the shortcut menu, select the <strong>Reimport QoS Profile</strong>. <br /></span></p><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;"><ac:image><ri:attachment ri:filename="reimport_QoS_profile.png"><ri:page ri:space-key="MRTCD" ri:content-title="Importing QoS Profile" /></ri:attachment></ac:image><br /></span></p></li></ul>
````

<!--NOMAGIC_PAGE id=249573278 space=MRTCD version=1 -->
## PAGE 00122: Incompatible Base Extendibility

- page_id: `249573278`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573278/Incompatible+Base+Extendibility
- version_number: 1
- version_date: `2020-11-20T13:41:14.973+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573255 space=MRTCD version=1 -->
## PAGE 00123: Install for simulation

- page_id: `249573255`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573255/Install+for+simulation
- version_number: 1
- version_date: `2020-11-19T15:12:59.203+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Simulation with Simulink
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

<!--NOMAGIC_PAGE id=249573212 space=MRTCD version=1 -->
## PAGE 00124: Installation

- page_id: `249573212`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573212/Installation
- version_number: 1
- version_date: `2020-11-19T14:00:11.077+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: ['installing-dds-plugin', 'install-dds-plugin']

### NORMALIZED CONTENT

Before installing Connext DDS for MagicDraw, first install RTI Connext DDS by following the instructions in its [Getting Started guide](https://www.rti.com/gettingstarted).

To install Connext DDS for MagicDraw

1. Install [CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='MDTWRT'] .
2. Install [CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='SYSMLPTWRT'] .
3. Start MagicDraw.
4. On the main menu, click Help > Resource/Plugin Manager .
5. Click Import and select the Connext DDS for MagicDraw plugin archive ( connext-dds-magicdraw-plugin.zip ).
6. After the successful installation, restart the MagicDraw.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">Before installing Connext DDS for MagicDraw, first install RTI Connext DDS by following the instructions in its <a href="https://www.rti.com/gettingstarted">Getting Started guide</a>.</p><p>To install Connext DDS for MagicDraw</p><hr /><ol><li>Install <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[MagicDraw]]></ac:plain-text-link-body></ac:link>.</li><li>Install <ac:link><ri:page ri:space-key="SYSMLPTWRT" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[SysML plugin]]></ac:plain-text-link-body></ac:link>.</li><li>Start MagicDraw.</li><li>On the main menu, click <strong>Help</strong> &gt; <strong>Resource/Plugin Manager</strong>. </li><li>Click <strong>Import</strong> and select the <em>Connext DDS for MagicDraw plugin</em> archive (<em>connext-dds-magicdraw-plugin.zip</em>).</li><li>After the successful installation, restart the MagicDraw.</li></ol>
````

<!--NOMAGIC_PAGE id=249573279 space=MRTCD version=1 -->
## PAGE 00125: Instance not Participant

- page_id: `249573279`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573279/Instance+not+Participant
- version_number: 1
- version_date: `2020-11-20T13:41:41.681+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573280 space=MRTCD version=1 -->
## PAGE 00126: Invalid Member Multiplicity

- page_id: `249573280`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573280/Invalid+Member+Multiplicity
- version_number: 1
- version_date: `2020-11-20T13:42:11.081+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573281 space=MRTCD version=1 -->
## PAGE 00127: Invalid Member Type

- page_id: `249573281`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573281/Invalid+Member+Type
- version_number: 1
- version_date: `2020-11-20T13:42:34.845+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573282 space=MRTCD version=1 -->
## PAGE 00128: Invalid Port Type

- page_id: `249573282`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573282/Invalid+Port+Type
- version_number: 1
- version_date: `2020-11-20T13:42:57.978+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573283 space=MRTCD version=1 -->
## PAGE 00129: Invalid Repository

- page_id: `249573283`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573283/Invalid+Repository
- version_number: 1
- version_date: `2020-11-20T13:43:33.472+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573284 space=MRTCD version=1 -->
## PAGE 00130: Invalid Topic Type Property Direction

- page_id: `249573284`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573284/Invalid+Topic+Type+Property+Direction
- version_number: 1
- version_date: `2020-11-20T13:44:05.226+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573211 space=MRTCD version=4 -->
## PAGE 00131: Magic Real-Time Communication Designer / DDS Real-Time Communication

- page_id: `249573211`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573211/Magic+Real-Time+Communication+Designer+DDS+Real-Time+Communication
- version_number: 4
- version_date: `2025-10-30T13:46:29.159+01:00`
- ancestors: 
- labels: ['dds-real-time-communication-plugin']

### NORMALIZED CONTENT

Magic Real-Time Communication Designer / DDS Real-Time Communication plugin is an environment for editing [Connext DDS](https://www.rti.com/products/connext-dds-professional) models in a visual way.

##### Background

The OMG Data-Distribution Service for Real-Time Systems (DDS) is the first open international middleware standard directly addressing publish-subscribe communications for real-time and embedded systems.

RTI Connext DDS Professional, based on a connectivity databus, offers a robust framework for developing and integrating mission critical systems. It is fully compliant with the OMG DDS for Real-Time Systems standard.

##### Advantages

With the Connext DDS for MagicDraw plugin, you can model the DDS-related aspects of your system using UML, extended by a DDS-specific profile. This offers the following advantages:

- The overall system (from requirements to functional applications) will have a unified representation, providing a common view of the system and a single source of truth.
- You can use an already familiar modeling language.
- The DDS entities and their relationships are displayed visually in a graphical notation.

The DDS Real-Time Communication Plugin documentation consists of the following sections:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">Magic Real-Time Communication Designer / DDS Real-Time Communication plugin is an environment for editing <a href="https://www.rti.com/products/connext-dds-professional">Connext DDS</a> models in a visual way.</p><h3>Background</h3><p class="FirstParagraph">The OMG Data-Distribution Service for Real-Time Systems (DDS) is the first open international middleware standard directly addressing publish-subscribe communications for real-time and embedded systems.</p><p>RTI Connext DDS Professional, based on a connectivity databus, offers a robust framework for developing and integrating mission critical systems. It is fully compliant with the OMG DDS for Real-Time Systems standard.</p><h3>Advantages</h3><p class="FirstParagraph">With the Connext DDS for MagicDraw plugin, you can model the DDS-related aspects of your system using UML, extended by a DDS-specific profile. This offers the following advantages:</p><ul><li>The overall system (from requirements to functional applications) will have a unified representation, providing a common view of the system and a single source of truth.</li><li>You can use an already familiar modeling language.</li><li>The DDS entities and their relationships are displayed visually in a graphical notation.</li></ul><p><br /></p><p><span style="color:var(--ds-text,#333333);">The DDS Real-Time Communication Plugin documentation consists of the following sections:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="675a6e7f-bff9-4f71-809c-aa22cf1a125d" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=249573286 space=MRTCD version=1 -->
## PAGE 00132: Missing Domain Attribute

- page_id: `249573286`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573286/Missing+Domain+Attribute
- version_number: 1
- version_date: `2020-11-20T13:44:33.149+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573287 space=MRTCD version=1 -->
## PAGE 00133: Missing Domain ID

- page_id: `249573287`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573287/Missing+Domain+ID
- version_number: 1
- version_date: `2020-11-20T13:47:14.738+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573288 space=MRTCD version=1 -->
## PAGE 00134: Missing Element Name

- page_id: `249573288`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573288/Missing+Element+Name
- version_number: 1
- version_date: `2020-11-20T13:47:43.591+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573289 space=MRTCD version=1 -->
## PAGE 00135: Multiple Struct Inheritance

- page_id: `249573289`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573289/Multiple+Struct+Inheritance
- version_number: 1
- version_date: `2020-11-20T13:48:05.493+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573290 space=MRTCD version=1 -->
## PAGE 00136: Multitype Topic

- page_id: `249573290`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573290/Multitype+Topic
- version_number: 1
- version_date: `2020-11-20T13:48:45.979+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573291 space=MRTCD version=1 -->
## PAGE 00137: Non-Nmeric Domain ID

- page_id: `249573291`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573291/Non-Nmeric+Domain+ID
- version_number: 1
- version_date: `2020-11-20T13:50:41.269+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573292 space=MRTCD version=1 -->
## PAGE 00138: Participant Type not Referenced

- page_id: `249573292`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573292/Participant+Type+not+Referenced
- version_number: 1
- version_date: `2020-11-20T13:51:06.831+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573269 space=MRTCD version=1 -->
## PAGE 00139: Qos Assignments

- page_id: `249573269`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573269/Qos+Assignments
- version_number: 1
- version_date: `2020-11-20T10:49:57.990+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Home Control Example
- labels: []

### NORMALIZED CONTENT

The currents version allows three kind of QoS assignment each of which can be swiftly created with specific generic tables. Since they were already covered in previous sections we only assign one for demonstration purposes. [CONFLUENCE_PAGE title='QoS profile assignments' space='MRTCD']>]]>

As shown in the figure below, the case is a kind of a special one because the port readLight is not actually on the HomeController block but on its light port’s type called NestedLightPort. There is a validation rule which checks if the port has no connection with the given instance.

[IMAGE alt='' src='']

###### The example of Endpoint QoS Assignment Table.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The currents version allows three kind of QoS assignment each of which can be swiftly created with specific generic tables. Since they were already covered in previous sections we only assign one for demonstration purposes. <ac:link><ri:page ri:space-key="MRTCD" ri:content-title="QoS profile assignments" /><ac:plain-text-link-body><![CDATA[Learn how to create Endpoint QoS Assignment Table >>]]></ac:plain-text-link-body></ac:link></p><p>As shown in the figure below, the case is a kind of a special one because the port readLight is not actually on the HomeController block but on its light port’s type called NestedLightPort. There is a validation rule which checks if the port has no connection with the given instance.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="QoS_Assignment_table.png"><ri:page ri:space-key="MRTCD" ri:content-title="Qos Assignments" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example of Endpoint QoS Assignment Table.</h6>
````

<!--NOMAGIC_PAGE id=249573236 space=MRTCD version=1 -->
## PAGE 00140: QoS profile assignments

- page_id: `249573236`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573236/QoS+profile+assignments
- version_number: 1
- version_date: `2020-11-20T12:34:27.276+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Getting started
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
<p class="FirstParagraph">There are three elements that QoS Profiles can be assigned to in the model:</p><ul><li class="FirstParagraph">Endpoints typed by Topic.</li><li class="FirstParagraph">DomainParticipants.</li><li class="FirstParagraph">Topics.</li></ul><p><br /></p><p>To create an empty Endpoint QoS Assignment Table</p><hr /><ol><li>In the <a href="https://docs.nomagic.com/display/MDTWRT/Containment+tab">Containment tree</a>, right-click a predefined <em>Endpoint QoS </em>Package.</li><li>From the shortcut menu, select <strong>Create Diagram </strong>and from the opened dialog, select Endpoint QoS Assignment Table.</li><li>The unnamed table is created. Type its name and press enter.</li></ol><p><br /></p><p>To fill in the Endpoint QoS Assignment Table</p><hr /><ol><li>From the table toolbar, click the <strong>Add New</strong> button. The new row appears and Endpoint QoS Assignment element is created in the model.</li><li><p class="auto-cursor-target">In the table, specify the following:<br /> - Double-click the <strong>Name</strong> cell and type Endpoint QoS Assignment name.<br /> - Double-click the <strong>QoS Profile</strong> cell, select <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="MRTCD" ri:content-title="QoS profile assignments" /></ri:attachment></ac:image></span> and in the <strong>Select Elements</strong> dialog choose QoS Profile.<br /> - Double-click the <strong>Endpoint</strong> cell, select <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="MRTCD" ri:content-title="QoS profile assignments" /></ri:attachment></ac:image></span> and in the <strong>Select Port </strong>dialog choose already created ports or use the <strong>Creation Mode</strong> to create new port.<br /> - Double-click the <strong>Domain Participant Instance</strong> cell, select <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:alt="Edit" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="MRTCD" ri:content-title="QoS profile assignments" /></ri:attachment></ac:image></span> and in the <strong>Select Property </strong>dialog choose already created Part Properties or use the <strong>Creation Mode</strong> to create new Part Property.</p></li></ol><p class="FirstParagraph"><span><br /></span></p><p class="FirstParagraph"><span>Assigning QoS on subscribers/publishers is not possible since they are derived from the model and not explicitly marked.</span></p><ul><li>To assign QoS Profiles on Topics create a Topic QoS Assignment Table.<br /><ac:image><ri:attachment ri:filename="topic_qos_assignemnt_table_example.png"><ri:page ri:space-key="MRTCD" ri:content-title="QoS profile assignments" /></ri:attachment></ac:image></li><li>To assign QoS Profiles on Domain Participants create a Participant QoS Assignment Table.<br /><ac:image><ri:attachment ri:filename="participant_qos_assignment.png"><ri:page ri:space-key="MRTCD" ri:content-title="QoS profile assignments" /></ri:attachment></ac:image></li><li>To assign QoS Profiles on Endpoints create a Endpoint QoS Assignment Table.<br /><ac:image><ri:attachment ri:filename="endpoint_Qos_assignment_table.png"><ri:page ri:space-key="MRTCD" ri:content-title="QoS profile assignments" /></ri:attachment></ac:image></li></ul>
````

<!--NOMAGIC_PAGE id=249573259 space=MRTCD version=1 -->
## PAGE 00141: Setting up the Simulink model

- page_id: `249573259`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573259/Setting+up+the+Simulink+model
- version_number: 1
- version_date: `2020-11-20T05:35:45.336+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Simulation with Simulink
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

<!--NOMAGIC_PAGE id=249573254 space=MRTCD version=1 -->
## PAGE 00142: Simulation with Simulink

- page_id: `249573254`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573254/Simulation+with+Simulink
- version_number: 1
- version_date: `2020-11-20T05:33:39.410+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: []

### NORMALIZED CONTENT

A Simulink model can be generated from the DDS XML generated by the Matlab plugin, which can be used to simulate the behavior of the modeled DDS system.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><span lang="EN">A Simulink model can be generated from the DDS XML generated by the Matlab plugin, which can be used to simulate the behavior of the modeled DDS system.</span></p><p class="FirstParagraph"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e4ccea78-c681-4939-b6e4-a9a976eb6044" /></p>
````

<!--NOMAGIC_PAGE id=249573293 space=MRTCD version=1 -->
## PAGE 00143: Struct Member Visibility

- page_id: `249573293`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573293/Struct+Member+Visibility
- version_number: 1
- version_date: `2020-11-20T13:51:35.563+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573294 space=MRTCD version=1 -->
## PAGE 00144: Topic Missing from Domain

- page_id: `249573294`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573294/Topic+Missing+from+Domain
- version_number: 1
- version_date: `2020-11-20T13:52:50.666+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573260 space=MRTCD version=1 -->
## PAGE 00145: Type mapping

- page_id: `249573260`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573260/Type+mapping
- version_number: 1
- version_date: `2020-11-20T05:36:17.714+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Simulation with Simulink
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

<!--NOMAGIC_PAGE id=249573295 space=MRTCD version=1 -->
## PAGE 00146: Unspecified String Bounds

- page_id: `249573295`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573295/Unspecified+String+Bounds
- version_number: 1
- version_date: `2020-11-20T13:53:14.722+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573296 space=MRTCD version=1 -->
## PAGE 00147: Unspecified String Bounds of Map Key

- page_id: `249573296`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573296/Unspecified+String+Bounds+of+Map+Key
- version_number: 1
- version_date: `2020-11-20T13:53:34.565+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573297 space=MRTCD version=1 -->
## PAGE 00148: Unsupported Discriminator Type

- page_id: `249573297`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573297/Unsupported+Discriminator+Type
- version_number: 1
- version_date: `2020-11-20T13:54:08.015+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Validation Suite
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

<!--NOMAGIC_PAGE id=249573252 space=MRTCD version=1 -->
## PAGE 00149: Validation

- page_id: `249573252`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573252/Validation
- version_number: 1
- version_date: `2020-11-19T13:39:05.521+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication > Getting started
- labels: []

### NORMALIZED CONTENT

The validity of the DDS model is continuously checked by active validation rules contained in the DDS Validation Suite. For example, if you accidentally add multiple attributes to a Topic, an error is displayed. You can fix some of these DDS modeling problems by right-clicking on them and selecting the appropriate solver.

[IMAGE alt='' src='']

There is a separate validation suite for Simulink named DDS Simulink Validation Suite. It contains validation rules for data types that are not supported by Simulink. It can be activated independently from the rest of the rules.

The detailed descriptions of the validation rules are available in [CONFLUENCE_PAGE title='Validation Suite' space='MRTCD'].

[CONFLUENCE_PAGE title='Validation' space='MDTWRT']>]]>

.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph"><span lang="EN">The validity of the DDS model is continuously checked by active validation rules contained in the DDS Validation Suite. For example, if you accidentally add multiple attributes to a Topic, an error is displayed. You can fix some of these DDS modeling problems by right-clicking on them and selecting the appropriate solver.</span></p><p class="FirstParagraph"><span lang="EN"><ac:image><ri:attachment ri:filename="image2020-11-12_15-7-35.png"><ri:page ri:space-key="MRTCD" ri:content-title="Validation" /></ri:attachment></ac:image></span></p><p class="FirstParagraph"><br /></p><p class="FirstParagraph"><span lang="EN"><span><span>There is a separate validation suite for Simulink named DDS Simulink Validation Suite. It contains validation rules for data types that are not supported by Simulink. It can be activated independently from the rest of the rules.</span></span></span></p><p>The detailed descriptions of the validation rules are available in <ac:link><ri:page ri:space-key="MRTCD" ri:content-title="Validation Suite" /></ac:link>.</p><p><br /></p><p><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Validation" /><ac:plain-text-link-body><![CDATA[Learn more about Validation >>]]></ac:plain-text-link-body></ac:link></p><p>.</p><p class="FirstParagraph"><span lang="EN"><br /></span></p><div><span style="white-space: pre-wrap;"><br /></span></div><div><span style="white-space: pre-wrap;"><br /></span></div>
````

<!--NOMAGIC_PAGE id=249573272 space=MRTCD version=1 -->
## PAGE 00150: Validation Suite

- page_id: `249573272`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/249573272/Validation+Suite
- version_number: 1
- version_date: `2020-11-20T13:31:04.756+01:00`
- ancestors: Magic Real-Time Communication Designer / DDS Real-Time Communication
- labels: []

### NORMALIZED CONTENT

In this section are detailed descriptions of the validation rules, each page describing one.

The severity is either error or warning. Warning means that the state is not necessarily incorrect, but probably is. The implementation, qualified name, and abbreviation are given because those are the identifiers modeling tool provides for a validation rule, so this document is searchable by either. [CONFLUENCE_PAGE title='Validation' space='MDTWRT']>]]>

The list of DDS validation rules:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="FirstParagraph">In this section are detailed descriptions of the validation rules, each page describing one. </p><p>The severity is either error or warning. Warning means that the state is not necessarily incorrect, but probably is. The implementation, qualified name, and abbreviation are given because those are the identifiers modeling tool provides for a validation rule, so this document is searchable by either. <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Validation" /><ac:plain-text-link-body><![CDATA[Learn more about modeling tool validation >>]]></ac:plain-text-link-body></ac:link></p><p>The list of DDS validation rules: </p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3606a106-ac5e-449f-becd-0cbba497615c" /></p>
````

<!--NOMAGIC_PAGE id=258048463 space=MRTCD version=1 -->
## PAGE 00151: Versions of Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin

- page_id: `258048463`
- space_key: `MRTCD`
- source_url: https://docs.nomagic.com/spaces/MRTCD/pages/258048463/Versions+of+Magic+Real-Time+Communication+Designer+DDS+Real-Time+Communication+Plugin
- version_number: 1
- version_date: `2025-09-24T15:29:35.502+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

aecc246002dc4a501dac1f7961f9c819

Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="a07b80c7-1b38-42dd-83d7-839cf2b56310"><ac:parameter ac:name="permaId">aecc246002dc4a501dac1f7961f9c819</ac:parameter><ac:parameter ac:name="documentTitle">Magic Real-Time Communication Designer / DDS Real-Time Communication Plugin</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````
