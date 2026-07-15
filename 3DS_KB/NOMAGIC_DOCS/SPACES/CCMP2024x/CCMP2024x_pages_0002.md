# NOMAGIC DOCUMENTATION SPACE: Concept Modeler Plugin 2024x

<!--NOMAGIC_SPACE key=CCMP2024x chunk=2 -->

<!--NOMAGIC_PAGE id=136717997 space=CCMP2024x version=2 -->
## PAGE 00266: Working with annotation properties

- page_id: `136717997`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717997/Working+with+annotation+properties
- version_number: 2
- version_date: `2024-02-01T08:42:52.509+01:00`
- ancestors: Concept Modeler Documentation > Usage > Working with annotations
- labels: []

### NORMALIZED CONTENT

1377296134

1377296136

1377296135

Annotation Properties is a stereotype applicable to annotations in your concept model. The following subsections will explain how to work with this stereotype.

1377296133

Related Pages

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="749c1f61-5783-457d-9839-6e2e5cf80fb4"><ac:parameter ac:name="id">1377296134</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d4221f40-321b-4b89-9f6a-a80997e14021"><ac:parameter ac:name="id">1377296136</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="72fea0a5-ea7d-4f4f-97a7-4bf25a523299"><ac:parameter ac:name="id">1377296135</ac:parameter><ac:rich-text-body><p>Annotation Properties is a stereotype applicable to annotations in your concept model. The following subsections will explain how to work with this stereotype.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6a284df4-cf82-47fa-a735-65b8ad67b722"><ac:parameter ac:name="id">1377296133</ac:parameter><ac:rich-text-body><p>Related Pages</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f2f9aed8-98c3-4ce7-b910-a75ed9bc8145" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136717958 space=CCMP2024x version=2 -->
## PAGE 00267: Working with annotations

- page_id: `136717958`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717958/Working+with+annotations
- version_number: 2
- version_date: `2024-02-01T08:44:18.196+01:00`
- ancestors: Concept Modeler Documentation > Usage
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Importing Annotations

1048646494

#### CONTENT-COLUMN: Importing Annotations

1048646496

#### CONTENT-BLOCK: Importing Annotations

1048646495

Annotations in Cameo Concept Modeler (CCM) offer a way to add contextual documentation to model elements, e.g., concept models, concepts, and properties. CCM primarily supports two types of annotations: **Literal** and **Internationalized Resource Identifier** (IRI) annotations. For a more in-depth explanation of annotations, please refer to [CONFLUENCE_PAGE title='Annotation and annotation properties' space='CCMP2024x'].

- An «IRI Annotation» is a use of an IRI, whereas a «Literal Annotation» of any URI type is a mention of an IRI.

[IMAGE alt='' src='']

**Two types of annotations primarily supported in CCM: Literal and IRI annotations.**

- A literal annotation provides a data value, e.g., particular string or an integer, that optionally specifies language or datatype of the value.
- An IRI annotation specifies an IRI to annotate a model element.

Annotations are stereotyped as either «Literal Annotation» or «IRI Annotation» to identify the type of the annotation value.

**More on Literal Annotation**

You can specify **datatype** or **language** in the Literal annotation’s specification.

[IMAGE alt='' src='']

**Datatype and language can be specified in the literal annotation’s specification.**

**Importing and Exporting Annotations**

- A concept model can be specified as an annotated element, like a concept or a property, for an annotation.
- When the concept model is exported to OWL, the annotation will be on the ontology which corresponds to the exported concept model.

#### NOTE: Exporting Annotations

Exporting Annotations

When a concept model is exported to OWL:

- The stereotyped UML comments will be exported as OWL annotations.
- UML comments that are not stereotyped as annotations will be ignored.

- IRI annotations are not lost on importing and exporting.
- Similarly, when an ontology with annotations annotating the ontology itself is imported to CCM, the resulting concept model will contain the annotations that annotated the original ontology.

#### INFO: Importing Annotations

Importing Annotations

An annotation on an ontology, when that ontology is imported, is converted to an annotation on the concept model which corresponds to that ontology.

1048656469

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="de931a54-b240-4d9a-b7de-d6b316c1d815"><ac:parameter ac:name="id">1048646494</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="004d99ce-7f08-42a2-b86a-84a60d391b1f"><ac:parameter ac:name="id">1048646496</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a8882faf-3594-4d73-b15b-eeadbbd10c2d"><ac:parameter ac:name="id">1048646495</ac:parameter><ac:rich-text-body><p>Annotations in Cameo Concept Modeler (CCM) offer a way to add contextual documentation to model elements, e.g., concept models, concepts, and properties. CCM primarily supports two types of annotations: <strong>Literal</strong> and <strong>Internationalized Resource Identifier</strong> (IRI) annotations. For a more in-depth explanation of annotations, please refer to <ac:link><ri:page ri:space-key="CCMP2024x" ri:content-title="Annotation and annotation properties" /></ac:link>.</p><ul><li>An «IRI Annotation» is a <em>use</em> of an IRI, whereas a «Literal Annotation» of any URI type is a <em>mention</em> of an IRI.</li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Annotation Menu.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with annotations" /></ri:attachment></ac:image></p><p style="text-align: center;"><strong style="text-align: center;">Two types of annotations primarily supported in CCM: Literal and IRI annotations.</strong></p><ul><li style="text-align: left;">A <strong style="letter-spacing: 0.0px;text-align: left;">literal annotation</strong> provides a data value, e.g., particular string or an integer, that optionally specifies language or datatype of the value.</li><li>An <strong>IRI annotation</strong> specifies an IRI to annotate a model element.</li></ul><p>Annotations are stereotyped as either «Literal Annotation» or «IRI Annotation» to identify the type of the annotation value.</p><p><strong>More on Literal Annotation</strong></p><p>You can specify <strong>datatype</strong> or <strong>language</strong> in the Literal annotation’s specification.</p><p style="text-align: center;"><ac:image ac:align="center" ac:height="400"><ri:attachment ri:filename="Datatype and Language in the Literal Annotation Specification.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with annotations" /></ri:attachment></ac:image></p><p style="text-align: center;"><strong style="text-align: center;">Datatype and language can be specified in the literal annotation’s specification.</strong></p><p><strong>Importing and Exporting Annotations</strong></p><ul><li>A concept model can be specified as an annotated element, like a concept or a property, for an annotation.</li><li>When the concept model is exported to OWL, the annotation will be on the ontology which corresponds to the exported concept model.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="46a16bf3-4b8e-40b3-9a7c-ac5f1906fcdd"><ac:parameter ac:name="title">Exporting Annotations</ac:parameter><ac:rich-text-body><p>When a concept model is exported to OWL:</p><ul><li>The stereotyped UML comments will be exported as OWL annotations.</li><li>UML comments that are not stereotyped as annotations will be ignored.</li></ul></ac:rich-text-body></ac:structured-macro><ul><li><span>IRI annotations are not lost on importing and exporting.</span></li><li>Similarly, when an ontology with annotations annotating the ontology itself is imported to CCM, the resulting concept model will contain the annotations that annotated the original ontology.</li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="117e7145-d745-4f7d-b580-7f059cf232ae"><ac:parameter ac:name="title">Importing Annotations</ac:parameter><ac:rich-text-body><p>An annotation on an ontology, when that ontology is imported, is converted to an annotation on the concept model which corresponds to that ontology.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7f092a6c-27f6-4050-9c3c-7530d2a5ec07"><ac:parameter ac:name="id">1048656469</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="bc4cc1b9-fcd1-4e3d-8fce-d6b1d5dc8d7f" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136717612 space=CCMP2024x version=1 -->
## PAGE 00268: Working with association classes

- page_id: `136717612`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717612/Working+with+association+classes
- version_number: 1
- version_date: `2023-09-21T06:55:29.065+02:00`
- ancestors: Concept Modeler Documentation > Usage > Experimental Features
- labels: []

### NORMALIZED CONTENT

Before creating an Association Class between Class elements in your diagram, make sure the [CONFLUENCE_PAGE title='Experimental Features' space='CCMP2024x'] is enabled. Once the option is enabled, please follow the steps below.

There are two ways to create an association class into your model. One way is through the diagram palette, and the other way is through the diagram pane.

To create an Association Class in the diagram pane

1. Right-click on any Class element in your diagram. [ATTACHMENT filename='as2.png']
2. You can also select Association Class from the diagram palette. [ATTACHMENT filename='as7.PNG']
3. Select Association Class.
4. A Class element can have a Association Class attached to itself, or to another class element. The figure below shows an association class joining two classes. [ATTACHMENT filename='as3.png']
5. You have created an Association Class, *class attendance,* in your Concept Modeling Diagram. [IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">Before creating</span> an Association Class between Class elements in your diagram, make sure the <ac:link><ri:page ri:space-key="CCMP2024x" ri:content-title="Experimental Features" /><ac:plain-text-link-body><![CDATA[Experimental Features option]]></ac:plain-text-link-body></ac:link> is enabled. Once the option is enabled, please follow the steps below.</p><p>There are two ways to create an association class into your model. One way is through the diagram palette, and the other way is through the diagram pane.</p><p><span style="color: rgb(62,63,64);"><br /></span></p><p><span style="color: rgb(62,63,64);">To create an Association Class in the diagram pane</span></p><hr /><ol><li>Right-click on any Class element in your diagram.<br /><ac:image ac:align="center" ac:height="250"><ri:attachment ri:filename="as2.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with association classes" /></ri:attachment></ac:image></li><li>You can also select Association Class from the diagram palette. <br /><ac:image ac:align="center" ac:thumbnail="true" ac:height="227"><ri:attachment ri:filename="as7.PNG"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with association classes" /></ri:attachment></ac:image></li><li>Select <strong>Association Class.</strong></li><li>A Class element can have a Association Class attached to itself, or to another class element. The figure below shows an association class joining two classes. <br /><ac:image ac:align="center" ac:height="101"><ri:attachment ri:filename="as3.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with association classes" /></ri:attachment></ac:image></li><li><span>You have created an Association Class, <em>class attendance,</em> in your Concept Modeling Diagram.</span><br /><span><ac:image ac:align="center" ac:height="144"><ri:attachment ri:filename="as4.PNG"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with association classes" /></ri:attachment></ac:image></span></li></ol><p><span><br /></span></p>
````

<!--NOMAGIC_PAGE id=136717773 space=CCMP2024x version=1 -->
## PAGE 00269: Working with Complement Of

- page_id: `136717773`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717773/Working+with+Complement+Of
- version_number: 1
- version_date: `2023-09-21T06:55:34.843+02:00`
- ancestors: Concept Modeler Documentation > Usage
- labels: []

### NORMALIZED CONTENT

Refer to [CONFLUENCE_PAGE title='Complement Of' space='CCMP'] to read more about the benefit of the stereotype in the modeling tool. This page explains the steps on how to use the dependency *"Complement of"* in your Concept Modeling project.

To create the dependency Complement of

1. Create two classes. E.g. Class 1 and Class 2 .
2. Do one of the following:
  1. Click on one of the classes so that the Smart Manipulator tool appears. Click on the [ATTACHMENT filename='Complement.PNG'] button. Click on the other class.
  2. Click on the [ATTACHMENT filename='complementofdiagrampallet.PNG'] button on the diagram pallet. Click on one class, and then click on the other class.
3. From either steps above, the final result should look like the following. [ATTACHMENT filename='Complement created.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Refer to <ac:link><ri:page ri:space-key="CCMP" ri:content-title="Complement Of" /></ac:link> to read more about the benefit of the stereotype in the modeling tool. This page explains the steps on how to use the dependency <em>&quot;Complement of&quot;</em> in your Concept Modeling project. </p><p><br /></p><p>To create the dependency Complement of</p><hr /><ol><li>Create two classes. E.g. <em>Class 1</em> and <em>Class 2</em>.</li><li>Do one of the following:<ol><li>Click on one of the classes so that the Smart Manipulator tool appears. Click on the <ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="Complement.PNG"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with Complement Of" /></ri:attachment></ac:image> button. Click on the other class. </li><li>Click on the <ac:image ac:thumbnail="true" ac:width="150"><ri:attachment ri:filename="complementofdiagrampallet.PNG"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with Complement Of" /></ri:attachment></ac:image> button on the diagram pallet. Click on one class, and then click on the other class. </li></ol></li><li>From either steps above, the final result should look like the following.<br /><ac:image ac:align="center"><ri:attachment ri:filename="Complement created.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with Complement Of" /></ri:attachment></ac:image></li></ol><p><br /></p>
````

<!--NOMAGIC_PAGE id=136717944 space=CCMP2024x version=2 -->
## PAGE 00270: Working with glossaries

- page_id: `136717944`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717944/Working+with+glossaries
- version_number: 2
- version_date: `2024-02-01T08:39:41.085+01:00`
- ancestors: Concept Modeler Documentation > Usage
- labels: []

### NORMALIZED CONTENT

1585603849

1585603869

1585603859

This section will focus on the modeling tool's capability of creating glossaries. These glossaries depend on your Concept Modeling project.

1585603848

**Related Pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="53184229-9cd4-4558-8076-65ca72fed16c"><ac:parameter ac:name="id">1585603849</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="81bd7f16-876c-4d77-82e0-5eddbdc176fc"><ac:parameter ac:name="id">1585603869</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9d60f21a-d96e-4109-be89-14badb95ee35"><ac:parameter ac:name="id">1585603859</ac:parameter><ac:rich-text-body><p>This section will focus on the modeling tool's capability of creating glossaries. These glossaries depend on your Concept Modeling project. </p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0c4a1d03-0512-4331-af5f-743a13b0f2ca"><ac:parameter ac:name="id">1585603848</ac:parameter><ac:rich-text-body><p><strong>Related Pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="eeecbe58-34ce-4e37-a503-34e9a63105e1" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136718061 space=CCMP2024x version=2 -->
## PAGE 00271: Working with intersection

- page_id: `136718061`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136718061/Working+with+intersection
- version_number: 2
- version_date: `2024-02-01T08:35:51.347+01:00`
- ancestors: Concept Modeler Documentation > Usage
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Superclass Intersection

1595971174

#### CONTENT-COLUMN: Superclass Intersection

1595971195

#### CONTENT-BLOCK: Superclass Intersection

1595971185

To create an intersection

1. Create or select at least three classes in your project. Name at least two of the classes, as shown below. [ATTACHMENT filename='naming two classes.PNG']
2. Draw two subclass from the anonymous class to the two named classes. [ATTACHMENT filename='ns1.PNG']
3. Right-click on each subclass arrows and in the menu shown, select Concept Modeling > Add superclass to the conditions sufficient to classify an instance. [ATTACHMENT filename='ns2.png']
4. Two Necessary & Sufficient stereotypes appear.
5. Hover over the unnamed class and it will describe the intersection. [ATTACHMENT filename='ns3.png']
6. You can stop here OR you can go further and create a Superclass Intersection.
7. Right click on the unnamed or named class and select Concept Modeling > Convert to Superclass Intersection notation . [ATTACHMENT filename='ns4.png']
8. The end result should look like the following figure. [ATTACHMENT filename='ns5.PNG']

You can also create an intersections as shown below, simply by naming all the classes created.

[IMAGE alt='' src='']**Example of Intersection using «Necessary & Sufficient»**

[IMAGE alt='' src='']**Example of Intersection Using «Superclass Intersection»**

#### INFO: Superclass Intersection

Superclass Intersection

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="e9157a95-44ba-4ac0-b047-a134071be4de"><ac:parameter ac:name="id">1595971174</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="3f440b14-b0bd-4413-a501-502863a5f660"><ac:parameter ac:name="id">1595971195</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f6835896-d8f4-44ad-8188-e773c4b47a31"><ac:parameter ac:name="id">1595971185</ac:parameter><ac:rich-text-body><p>To create an intersection</p><hr /><ol><li>Create or select at least three classes in your project. Name at least two of the classes, as shown below.<br /><ac:image ac:align="center" ac:height="148"><ri:attachment ri:filename="naming two classes.PNG"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with intersection" /></ri:attachment></ac:image></li><li>Draw two subclass from the anonymous class to the two named classes. <br /><ac:image ac:align="center" ac:height="142"><ri:attachment ri:filename="ns1.PNG"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with intersection" /></ri:attachment></ac:image></li><li>Right-click on each subclass arrows and in the menu shown, select Concept Modeling &gt; Add superclass to the conditions sufficient to classify an instance.<br /><ac:image ac:align="center" ac:width="400"><ri:attachment ri:filename="ns2.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with intersection" /></ri:attachment></ac:image></li><li>Two <strong>Necessary</strong> <strong>&amp; Sufficient</strong> stereotypes appear.</li><li>Hover over the unnamed class and it will describe the intersection.<br /><ac:image ac:align="center" ac:width="600"><ri:attachment ri:filename="ns3.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with intersection" /></ri:attachment></ac:image></li><li><strong>You can stop here</strong> OR <strong>you can go further and create a Superclass Intersection.</strong></li><li>Right click on the unnamed or named class and select <strong>Concept</strong> <strong>Modeling</strong> &gt; <strong>Convert to Superclass Intersection notation</strong>.<br /><ac:image ac:align="center" ac:width="600"><ri:attachment ri:filename="ns4.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with intersection" /></ri:attachment></ac:image></li><li>The end result should look like the following figure.<br /><ac:image ac:align="center" ac:width="400"><ri:attachment ri:filename="ns5.PNG"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with intersection" /></ri:attachment></ac:image></li></ol><p>You can also create an intersections as shown below, simply by naming all the classes created. </p><p style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="NSPic.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with intersection" /></ri:attachment></ac:image><strong style="text-align: center;letter-spacing: 0.0px;">Example of Intersection using «Necessary &amp; Sufficient»</strong></p><p style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="SIpic.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with intersection" /></ri:attachment></ac:image><strong>Example of Intersection Using «Superclass Intersection»</strong></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="9c7498ea-5d8d-4288-8513-86eed56c8a6b"><ac:parameter ac:name="title">Superclass Intersection</ac:parameter><ac:rich-text-body>Please read <ac:link><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ac:link> for more information about Superclass Intersections. </ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136717596 space=CCMP2024x version=2 -->
## PAGE 00272: Working with non-CCM projects

- page_id: `136717596`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717596/Working+with+non-CCM+projects
- version_number: 2
- version_date: `2024-02-01T08:42:36.398+01:00`
- ancestors: Concept Modeler Documentation > Usage
- labels: []

### NORMALIZED CONTENT

1283716351

1283716371

1283716361

1283716350

**Related Pages**

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="cbbd630a-4214-4822-81da-4ab7a5a3b10d"><ac:parameter ac:name="id">1283716351</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b394f814-55a8-45e8-8a98-4d9a507d895d"><ac:parameter ac:name="id">1283716371</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6dccdee6-ee06-450d-82e4-553b24034294"><ac:parameter ac:name="id">1283716361</ac:parameter><ac:rich-text-body><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="77fa8637-ad75-4aec-9286-e789981e8b2c"><ac:parameter ac:name="id">1283716350</ac:parameter><ac:rich-text-body><p><strong>Related Pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="9b4bd59f-f90a-4436-b334-a9607fd44c1f"><ac:parameter ac:name="showRoot">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136717619 space=CCMP2024x version=1 -->
## PAGE 00273: Working with phases

- page_id: `136717619`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717619/Working+with+phases
- version_number: 1
- version_date: `2023-09-21T06:55:29.158+02:00`
- ancestors: Concept Modeler Documentation > Usage > Experimental Features
- labels: []

### NORMALIZED CONTENT

To create a Phase in your model

1. Click on the drop down menu next to Class on the diagram palette and click on Phase. [ATTACHMENT filename='p2.png']
2. Drop it onto your diagram pane. You have created a Phase element.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To create a Phase in your model</p><hr /><ol><li><span style="color: rgb(62,63,64);">Click on the drop down menu next to Class on the diagram palette and click on Phase.</span><br /><ac:image ac:align="center" ac:height="160"><ri:attachment ri:filename="p2.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with phases" /></ri:attachment></ac:image></li><li><span style="color: rgb(62,63,64);">Drop it onto your diagram pane. You have created a Phase element.</span></li></ol><p><span style="color: rgb(62,63,64);"><ac:image ac:align="center" ac:height="138"><ri:attachment ri:filename="p3.PNG"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with phases" /></ri:attachment></ac:image></span></p>
````

<!--NOMAGIC_PAGE id=136717797 space=CCMP2024x version=2 -->
## PAGE 00274: Working with properties

- page_id: `136717797`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717797/Working+with+properties
- version_number: 2
- version_date: `2024-02-01T08:43:57.916+01:00`
- ancestors: Concept Modeler Documentation > Usage
- labels: []

### NORMALIZED CONTENT

1585759740

1585759760

1585759750

This section focuses on explaining almost everything concerning properties in your concept model.

1585759739

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="b4bfdef6-380a-416b-aae2-6e4b253317ca"><ac:parameter ac:name="id">1585759740</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fe915c1b-0ba6-441e-a752-e0c451c164dd"><ac:parameter ac:name="id">1585759760</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2261843f-afaa-411a-9c98-5475fac11e26"><ac:parameter ac:name="id">1585759750</ac:parameter><ac:rich-text-body><p>This section focuses on explaining almost everything concerning properties in your concept model. </p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b02a141c-8f79-458b-a249-84ea8f978930"><ac:parameter ac:name="id">1585759739</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="32e69f38-8425-4ed0-b302-48348b85f71f" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136717896 space=CCMP2024x version=1 -->
## PAGE 00275: Working with restrictions

- page_id: `136717896`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717896/Working+with+restrictions
- version_number: 1
- version_date: `2023-09-21T06:55:40.106+02:00`
- ancestors: Concept Modeler Documentation > Usage
- labels: []

### NORMALIZED CONTENT

417112990

417113001

417113000

There are two types of Restrictions: Universal quantification constraint and existential quantification constraint.

##### Universal quantification constraint

A universal quantification constraint is created from redefining an existing property created in the context of the owning class. This interpretation is based on {redefines} in UML, which allows for more specific constraints to be added to an existing property without defining a new one.

##### Existential quantification constraint

An existential quantification constraint is created from subsetting a property without giving the new property a different name (or leaving off the new property name altogether). As {subsets} with an omitted name is not well defined in UML, it is used in the Concept Modeling profile to express that a subset of values must meet the stated cardinality and type constraints of the subsetting property.

417112988

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="6c4797c3-a4be-45ac-a370-621032563869"><ac:parameter ac:name="id">417112990</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="7d28917a-14d8-4a96-9e66-cc0ce6da71b1"><ac:parameter ac:name="id">417113001</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="68c12f96-febb-432b-b742-ee428c7539fe"><ac:parameter ac:name="id">417113000</ac:parameter><ac:rich-text-body><p>There are two types of Restrictions: Universal quantification constraint and existential quantification constraint.</p><h3>Universal quantification constraint</h3><p>A universal quantification constraint is created from redefining an existing property created in the context of the owning class. This interpretation is based on {redefines} in UML, which allows for more specific constraints to be added to an existing property without defining a new one.</p><h3>Existential quantification constraint</h3><p>An existential quantification constraint is created from subsetting a property without giving the new property a different name (or leaving off the new property name altogether). As {subsets} with an omitted name is not well defined in UML, it is used in the Concept Modeling profile to express that a subset of values must meet the stated cardinality and type constraints of the subsetting property.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2760631e-252c-4bea-bd2a-3c5395b3200e"><ac:parameter ac:name="id">417112988</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="544cf57f-690c-4e45-bdf4-68d3593457f0" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136717622 space=CCMP2024x version=1 -->
## PAGE 00276: Working with roles

- page_id: `136717622`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717622/Working+with+roles
- version_number: 1
- version_date: `2023-09-21T06:55:29.231+02:00`
- ancestors: Concept Modeler Documentation > Usage > Experimental Features
- labels: []

### NORMALIZED CONTENT

To create the Role stereotype

1. Click on the drop down menu next to Class on the diagram palette and click on Role. [ATTACHMENT filename='r1.png']
2. Drop the element on your diagram pane and you have created a Role. [ATTACHMENT filename='r2.PNG']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To create the Role stereotype</p><hr /><ol><li>Click on the drop down menu next to Class on the diagram palette and click on Role. <br /><ac:image ac:align="center" ac:height="152"><ri:attachment ri:filename="r1.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with roles" /></ri:attachment></ac:image></li><li>Drop the element on your diagram pane and you have created a Role.<br /><ac:image ac:align="center" ac:height="143"><ri:attachment ri:filename="r2.PNG"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with roles" /></ri:attachment></ac:image></li></ol><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136717778 space=CCMP2024x version=1 -->
## PAGE 00277: Working with subclasses

- page_id: `136717778`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717778/Working+with+subclasses
- version_number: 1
- version_date: `2023-09-21T06:55:35.062+02:00`
- ancestors: Concept Modeler Documentation > Usage
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

428320751

#### CONTENT-COLUMN: Note

428320753

#### CONTENT-BLOCK: Note

428320752

Users may want to make a set of existing subclasses disjoint, overlapping, complete, or incomplete. The Concept Modeler provides a quick method for adding a generalization set to your concept model and for setting its properties.

#### NOTE: Note

Note

- Creating generalization sets through the Concept Modeler is only applicable to generalization relationships connected together through the shared target notation. The manual method of creating generalization sets will still be available through the Specification window. Please see the MagicDraw user guide for additional information.
- Anonymous unions are incompatible with {incomplete} because an instance can only be classified by one or more classes in a union, not the union itself.

428328618

**Related pages**

- Usage
- Making subclasses disjoint
- Making subclasses complete
- Making subclasses overlapping
- Making subclasses incomplete

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="dbc8b6f9-a46b-4df3-96c1-7f8e36d094de"><ac:parameter ac:name="id">428320751</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="2246dee2-ae2f-4ce1-8fce-00f7904c7d69"><ac:parameter ac:name="id">428320753</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2a6ce801-7286-4056-aa9f-eb050a8d19be"><ac:parameter ac:name="id">428320752</ac:parameter><ac:rich-text-body><p>Users may want to make a set of existing subclasses disjoint, overlapping, complete, or incomplete. The Concept Modeler provides a quick method for adding a generalization set to your concept model and for setting its properties.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5f5b61d0-116b-4946-af97-fa32a90df504"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>Creating generalization sets through the Concept Modeler is only applicable to generalization relationships connected together through the shared target notation. The manual method of creating generalization sets will still be available through the Specification window. Please see the MagicDraw user guide for additional information.</li><li>Anonymous unions are incompatible with {incomplete} because an instance can only be classified by one or more classes in a union, not the union itself.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="fd0f6094-656c-4fa8-a510-d21851b981ec"><ac:parameter ac:name="id">428328618</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CCMP2024x/Usage" rel="nofollow">Usage</a></li><li><a href="https://docs.nomagic.com/display/CCMP2024x/Making+subclasses+disjoint">Making subclasses disjoint</a></li><li><a href="https://docs.nomagic.com/display/CCMP2024x/Making+subclasses+complete">Making subclasses complete</a></li><li><a href="https://docs.nomagic.com/display/CCMP2024x/Making+subclasses+overlapping">Making subclasses overlapping</a></li><li><a href="https://docs.nomagic.com/display/CCMP2024x/Making+subclasses+incomplete">Making subclasses incomplete</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136717887 space=CCMP2024x version=1 -->
## PAGE 00278: Working with subproperties

- page_id: `136717887`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717887/Working+with+subproperties
- version_number: 1
- version_date: `2023-09-21T06:55:39.639+02:00`
- ancestors: Concept Modeler Documentation > Usage > Working with properties
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Removing Multiple Subproperties

425322037

#### CONTENT-COLUMN: Removing Multiple Subproperties

425322039

#### CONTENT-BLOCK: Removing Multiple Subproperties

425322038

In the Concept Modeling interpretation of UML, subsetting a property creates a subproperty when the subsetting property has a different name than the subsetted property (see section [CONFLUENCE_PAGE title='Subproperty' space='CCMP2024x']). UML provides a {subsets} constraint that asserts that the values within a subsetting property are also in the set of values within a subsetted property. The Concept Modeling Profile interprets a subproperty as a subsetting property that has a different name.

To add a subproperty

1. Drag and drop a subsetted property, e.g. *has child,* onto a property, e.g. *has daughter.* [IMAGE alt='' src='']
2. After you drop the subsetted property, you will see the following menu appear. Click Create subproperty. [ATTACHMENT filename='su2.png']
3. You should see something like the following. [ATTACHMENT filename='su3.PNG']

To remove a subproperty from a property

1. Right-click on a subsetting property, e.g., {subsets has child} .
2. Select Concept Modeling > Remove subproperty.

[IMAGE alt='' src='']

#### INFO: Removing Multiple Subproperties

Removing Multiple Subproperties

When you have multiple subproperties on the same generalization, the following window will appear when you are trying to remove the subproperties. This dialog allows you to choose the subproperty you want to remove. It does not remove the subproperties at once, it lets you choose one at a time.

[IMAGE alt='' src='']

425322036

**Related page**

- Usage

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="7e1a4acc-b2b6-4312-94ce-ba2c96d0de41"><ac:parameter ac:name="id">425322037</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d38324f5-c1b9-459e-aa61-577246d96671"><ac:parameter ac:name="id">425322039</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c094ec66-373b-41c8-a952-e6220a647cca"><ac:parameter ac:name="id">425322038</ac:parameter><ac:rich-text-body><p>In the Concept Modeling interpretation of UML, subsetting a property creates a subproperty when the subsetting property has a different name than the subsetted property (see section <ac:link><ri:page ri:space-key="CCMP2024x" ri:content-title="Subproperty" /></ac:link>). UML provides a {subsets} constraint that asserts that the values within a subsetting property are also in the set of values within a subsetted property. The Concept Modeling Profile interprets a subproperty as a subsetting property that has a different name.</p><p><br /></p><p>To add a subproperty</p><hr /><ol><li><p class="auto-cursor-target">Drag and drop a subsetted property, e.g. <em>has child,</em> onto a property, e.g. <em>has daughter.</em></p><p class="auto-cursor-target"><ac:image ac:align="center" ac:height="137"><ri:attachment ri:filename="su1.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with subproperties" /></ri:attachment></ac:image></p></li><li>After you drop the subsetted property, you will see the following menu appear. Click <strong>Create subproperty.</strong><br /><ac:image ac:align="center" ac:height="250"><ri:attachment ri:filename="su2.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with subproperties" /></ri:attachment></ac:image></li><li>You should see something like the following.<br /><ac:image ac:align="center" ac:height="162"><ri:attachment ri:filename="su3.PNG"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with subproperties" /></ri:attachment></ac:image></li></ol><p>To remove a subproperty from a property</p><hr /><ol><li>Right-click on a subsetting property, e.g., <em>{subsets has child}</em>.</li><li>Select <strong>Concept Modeling &gt; Remove subproperty.</strong></li></ol><p style="margin-left: 30.0px;"><ac:image ac:align="center" ac:width="600"><ri:attachment ri:filename="su4.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with subproperties" /></ri:attachment></ac:image></p><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="74ecd76d-f4be-4c24-b6a2-abc3d12bcc93"><ac:parameter ac:name="title">Removing Multiple Subproperties</ac:parameter><ac:rich-text-body><p>When you have multiple subproperties on the same generalization, the following window will appear when you are trying to remove the subproperties. This dialog allows you to choose the subproperty you want to remove. It does not remove the subproperties at once, it lets you choose one at a time.</p><p><ac:image ac:align="center" ac:width="700"><ri:attachment ri:filename="sub7.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with subproperties" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p><br /></p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="78e7a810-4b9b-4e32-ab14-e3afe00d0dcf"><ac:parameter ac:name="id">425322036</ac:parameter><ac:rich-text-body><p><strong>Related page</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CCMP2024x/Usage" rel="nofollow">Usage</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136717160 space=CCMP2024x version=1 -->
## PAGE 00279: Working with superclass intersection

- page_id: `136717160`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136717160/Working+with+superclass+intersection
- version_number: 1
- version_date: `2023-09-21T06:55:06.033+02:00`
- ancestors: Concept Modeler Documentation > Concept Modeling Semantics
- labels: []

### NORMALIZED CONTENT

This section will demonstrate the different menu options that appear in the cases of relationships between Superclass Intersections and other class elements.

#### INFO: Stereotypes

Stereotypes

Please note that stereotype of the **selected Class** is *Superclass Intersection* and the stereotype of the **selected Generalization** is *Necessary and Sufficient.*

The following cases are based on a **selected Class.**

Case 1: Selected class has no stereotype, and all outgoing generalizations have no stereotypes.

[IMAGE alt='' src='']

Case 2: Selected class has no stereotype, and some outgoing generalizations have stereotypes

[IMAGE alt='' src='']

Case 3: Selected class has no stereotype, all outgoing generalizations have stereotypes.

[IMAGE alt='' src='']

Case 4: Selected class has a stereotype, but the generalizations do not.

[IMAGE alt='' src='']Case 5: Selected class has a stereotype and some outgoing generalizations also have a stereotype.

[IMAGE alt='' src='']

Case 6: Selected class has a stereotype and all outgoing generalizations also have a stereotype.

[IMAGE alt='' src='']

The following cases are based on the **selected** **Generalization**of specific class.

Case 1: Specific class of selected generalization has no stereotype, selected generalization has no stereotype, and all outgoing generalizations of specific class have no stereotype.

[IMAGE alt='' src='']

Case 2: Specific class of selected generalization has no stereotype, selected generalization has no stereotype, but some other outgoing generalizations of specific class have stereotype.

[IMAGE alt='' src='']

Case 3: Specific class of selected generalization has no stereotype, selected generalization has no stereotype, and all outgoing generalizations of specific class have stereotype, but some other outgoing generalizations of specific class have stereotype.

[IMAGE alt='' src='']

Case 4: Specific class of selected generalization has no stereotype, selected generalization has stereotype, and all outgoing generalizations of specific class have no stereotype, but some other outgoing generalizations of specific class have no stereotype.

[IMAGE alt='' src='']

Case 5: Specific class of selected generalization has no stereotype, selected generalization has stereotype, and all outgoing generalizations of specific class have no stereotype, but some other outgoing generalizations of specific class have stereotype.

[IMAGE alt='' src='']

Case 6: Specific class of selected generalization has no stereotype, selected generalization has stereotype, and all outgoing generalizations of specific class have stereotype, but some other outgoing generalizations of specific class have stereotype.

[IMAGE alt='' src='']

Case 7: Specific class of selected generalization has stereotype, selected generalization has no stereotype, and all outgoing generalizations of specific class have no stereotype, and some other outgoing generalizations of specific class have no stereotype.

[IMAGE alt='' src='']

Case 8: Specific class of selected generalization has stereotype, selected generalization has no stereotype, and all outgoing generalizations of specific class have no stereotype, and some other outgoing generalizations of specific class have stereotype.

Case 9: Specific class of selected generalization has stereotype, selected generalization has no stereotype, and all outgoing generalizations of specific class have stereotype, and some other outgoing generalizations of specific class have stereotype.

Case 10: Specific class of selected generalization has stereotype, selected generalization has stereotype, and all outgoing generalizations of specific class have no stereotype, and some other outgoing generalizations of specific class have no stereotype.

[IMAGE alt='' src='']

Case 11: Specific class of selected generalization has stereotype, selected generalization has stereotype, and all outgoing generalizations of specific class have no stereotype, and some other outgoing generalizations of specific class have stereotype.

[IMAGE alt='' src='']

Case 12: Specific class of selected generalization has stereotype, selected generalization has stereotype, and all outgoing generalizations of specific class have stereotype, and some other outgoing generalizations of specific class have stereotype.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section will demonstrate the different menu options that appear in the cases of relationships between Superclass Intersections and other class elements.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="9b1c400d-a944-40cc-b851-d224ca8596b5"><ac:parameter ac:name="title">Stereotypes</ac:parameter><ac:rich-text-body><p>Please note that stereotype of the <strong>selected Class</strong> is <em>Superclass Intersection</em> and the stereotype of the <strong>selected Generalization</strong> is <em>Necessary and Sufficient.</em></p></ac:rich-text-body></ac:structured-macro><p>The following cases are based on a <strong style="letter-spacing: 0.0px;">selected Class.</strong></p><p style="text-align: left;">Case 1: Selected class has no stereotype, and all outgoing generalizations have no stereotypes.</p><p style="text-align: left;"><ac:image ac:align="center" ac:width="500"><ri:attachment ri:filename="s3.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p style="text-align: left;">Case 2: Selected class has no stereotype, and some outgoing generalizations have stereotypes</p><p style="text-align: left;"><ac:image ac:align="center" ac:width="500"><ri:attachment ri:filename="s4.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p style="text-align: left;"><br /></p><p style="text-align: left;">Case 3: Selected class has no stereotype, all outgoing generalizations have stereotypes.</p><p style="text-align: left;"><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="s5.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p style="text-align: left;">Case 4: Selected class has a stereotype, but the generalizations do not.</p><p style="text-align: left;"><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="s6.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image>Case 5: Selected class has a stereotype and some outgoing generalizations also have a stereotype.</p><p style="text-align: left;"><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="su6.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p>Case 6: Selected class has a stereotype and all outgoing generalizations also have a stereotype.</p><p><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="su5.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p><br /></p><p>The following cases are based on the <strong style="letter-spacing: 0.0px;">selected</strong> <strong style="letter-spacing: 0.0px;">Generalization </strong>of specific class.</p><p>Case 1: Specific class of selected generalization has no stereotype, selected generalization has no stereotype, and all outgoing generalizations of specific class have no stereotype. </p><p><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="s10.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p>Case 2: Specific class of selected generalization has no stereotype, selected generalization has no stereotype, but some other outgoing generalizations of specific class have stereotype.</p><p><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="s9.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p><br /></p><p>Case 3: Specific class of selected generalization has no stereotype, selected generalization has no stereotype, and all outgoing generalizations of specific class have stereotype, but some other outgoing generalizations of specific class have stereotype.</p><p><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="s11.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p>Case 4: Specific class of selected generalization has no stereotype, selected generalization has stereotype, and all outgoing generalizations of specific class have no stereotype, but some other outgoing generalizations of specific class have no stereotype.</p><p><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="s12.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p>Case 5: Specific class of selected generalization has no stereotype, selected generalization has stereotype, and all outgoing generalizations of specific class have no stereotype, but some other outgoing generalizations of specific class have stereotype.</p><p><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="s13.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p><br /></p><p>Case 6: Specific class of selected generalization has no stereotype, selected generalization has stereotype, and all outgoing generalizations of specific class have stereotype, but some other outgoing generalizations of specific class have stereotype.</p><p><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="s14.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p>Case 7: Specific class of selected generalization has stereotype, selected generalization has no stereotype, and all outgoing generalizations of specific class have no stereotype, and some other outgoing generalizations of specific class have no stereotype.</p><p><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="s15.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p>Case 8: Specific class of selected generalization has stereotype, selected generalization has no stereotype, and all outgoing generalizations of specific class have no stereotype, and some other outgoing generalizations of specific class have stereotype.</p><p><br /></p><p>Case 9: Specific class of selected generalization has stereotype, selected generalization has no stereotype, and all outgoing generalizations of specific class have stereotype, and some other outgoing generalizations of specific class have stereotype.</p><p><br /></p><p>Case 10: Specific class of selected generalization has stereotype, selected generalization has stereotype, and all outgoing generalizations of specific class have no stereotype, and some other outgoing generalizations of specific class have no stereotype.</p><p><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="su7.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p>Case 11: Specific class of selected generalization has stereotype, selected generalization has stereotype, and all outgoing generalizations of specific class have no stereotype, and some other outgoing generalizations of specific class have stereotype.</p><p><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="su8.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p><p>Case 12: Specific class of selected generalization has stereotype, selected generalization has stereotype, and all outgoing generalizations of specific class have stereotype, and some other outgoing generalizations of specific class have stereotype.</p><p><ac:image ac:align="center" ac:width="550"><ri:attachment ri:filename="su9.png"><ri:page ri:space-key="CCMP2024x" ri:content-title="Working with superclass intersection" /></ri:attachment></ac:image></p>
````

<!--NOMAGIC_PAGE id=136718023 space=CCMP2024x version=2 -->
## PAGE 00280: Working with the Natural Language Glossary

- page_id: `136718023`
- space_key: `CCMP2024x`
- source_url: https://docs.nomagic.com/spaces/CCMP2024x/pages/136718023/Working+with+the+Natural+Language+Glossary
- version_number: 2
- version_date: `2024-02-01T08:40:57.976+01:00`
- ancestors: Concept Modeler Documentation > Usage
- labels: []

### NORMALIZED CONTENT

1213942032

1213942044

1213942034

A big capability of the modeling tool is generating natural language glossaries for your concept modeling project. This section explains how to generate a natural language glossary and how to customize to your liking.

1213942031

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f2cbab65-1189-42e7-8f8d-ac74d38376d1"><ac:parameter ac:name="id">1213942032</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="3119cbe5-735b-490d-b1b1-db5a5184efbb"><ac:parameter ac:name="id">1213942044</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cdb11df2-c9aa-4a7e-9b55-8a5a7041137b"><ac:parameter ac:name="id">1213942034</ac:parameter><ac:rich-text-body><p>A big capability of the modeling tool is generating natural language glossaries for your concept modeling project. This section explains how to generate a natural language glossary and how to customize to your liking.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3fe438e9-1987-491d-bd13-ae6cf8338c41"><ac:parameter ac:name="id">1213942031</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="091841bd-ccaa-4fc8-8223-6aa92cfc80d7" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````
