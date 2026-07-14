# NOMAGIC DOCUMENTATION SPACE: UML Profiling and DSL Guide

<!--NOMAGIC_SPACE key=UPDG chunk=2 -->

<!--NOMAGIC_PAGE id=243973696 space=UPDG version=1 -->
## PAGE 00154: Creating and specifying derived properties

- page_id: `243973696`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973696/Creating+and+specifying+derived+properties
- version_number: 1
- version_date: `2025-07-31T19:04:51.558+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Extending Metamodel with Derived Properties
- labels: []

### NORMALIZED CONTENT

To be included in a project as a property extending a UML element, an attribute must be owned by a DSL customization element and stereotyped as «derivedPropertySpecification».

##### Specifying derived properties

To create and specify a derived property

1. Select the customization element for which you want to create a derived property. The derived property will be created for the stereotype or metaclass, defined as a customization target in the selected customization element specification.
2. Select **Create Element** > **Derived Property Specification** from the shortcut menu. The attribute is created. 
[IMAGE alt='' src='']
3. Type the attribute name. Your Model Browser should look like this at this stage: [IMAGE alt='' src=''] The attribute’s name corresponds to the name of the derived property.Type derived property names in camel case (i.e.,*realizingActivities*).A property name defined in camel case will be displayed in separate words with the first word capitalized. For example, realizingActivities will be changed to *Realizing Activities* (visible in the user interface).
4. Edit property values specifying the derived property in the attribute's Specification window. All properties are specified in the general specification pane. Some are also specified in the **Tags** specification pane. For detailed information, see the properties .

If you do not see the newly created derived property in the element’s [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'], please read the following:

- In the element’s [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] , the specified derived property is visible by default only in the All properties mode. First, try switching to this mode. Also try changing the mode in which you want the derived property to be visible (click the Customize button).
- If you have specified the derived property for the element (with the Used UML Properties property of DSL customization specified) you must add the newly created derived property to the element’s visible properties list. For detailed information, please refer to [CONFLUENCE_PAGE title='Derived properties visibility' space=''] .

If you need to further customize a customization’s derived property without modifying the existing customization itself, you can create a new customization that can inherit the former one’s properties via a generalization. Then you can redefine the inherited derived property to customize it. The redefining derived property of the new customization overrides that of the original customization.

##### Derived property specification

[IMAGE alt='' src='']

###### The Specification window of the derived property

description_tableThe following table describes the properties specified for the derived property.

| Property | Description |
| --- | --- |
| Name | The name of the property.This name will be added and visible in the specification of the element whose type is defined as a customization target. |
| Type | The type of the derived property values. You may set a model element type or a data type (e.g., string, boolean, orintegerfrom the UML Standard Profile) as a property value.To display classes and components as property values, select the classifier as a type for the derived property value. |
| Multiplicity | The multiplicity of the derived property values.If the multiplicity is “0..1”, the derived property value will be shown as single.If the multiplicity is “0..*”, the derived property values will be shown as collection. |
| Is Read Only | If true, the derived property is read-only. You cannot edit the result elements for the derived property value.If false, the property is read-write. You can edit the result elements for the derived property according to the expressions defined. |
| Is Ordered | If true, the property values are always displayed in the same order.If false, the property values are displayed in nonpredictable order. |
| Is Unique | If true, the property values are unique. The same element is displayed only once.If false, the property values may be displayed more than once. |
| Expression | One or more expressions of the derived property.An expression defines the criterion for selecting result elements.There are ten possible expression types:Metachain navigation (indirect relations through chains of properties)FindUnionExcludeFilterVarious scriptsImplied RelationType TestProperty TestOperation from Model The criterion for selecting the result elements can also be any combination of the expression types above.For the detailed information, see .Only one Simple Navigation operation criterion can be assigned to the expression of the derived property. |
| Documentation | The text displayed as the derived property description in the element’s and Properties panel. |
| customizationTarget | The specified derived property will be added to one or more element types (stereotypes and/ or metaclasses).The expression calculations begin from the element type of the customization target. |

**Related pages:**

- Extending Metamodel with Derived Properties
- Using Customization Data
- Creating Customization Data
- Defining Expressions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To be included in a project as a property extending a UML element, an attribute must be owned by a DSL customization element and stereotyped as «derivedPropertySpecification».</p><h3>Specifying derived properties</h3><p>To create and specify a derived property</p><hr /><ol><li><p>Select the customization element for which you want to create a derived property.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="9a1490db-6cf2-4a7d-86b6-c9da201ccf67"><ac:rich-text-body><p>The derived property will be created for the stereotype or metaclass, defined as a customization target in the selected customization element specification.</p></ac:rich-text-body></ac:structured-macro></li><li><p>Select <strong>Create Element</strong> &gt; <strong>Derived Property Specification</strong> from the shortcut menu. The attribute is created.<br /><ac:image><ri:attachment ri:filename="derived_property_model_browser (1).png" /></ac:image></p></li><li><p>Type the attribute name. Your Model Browser should look like this at this stage:</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="derived_property.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0ba5494f-8d67-4947-b341-5ea39c8fbb55"><ac:rich-text-body><p>The attribute’s name corresponds to the name of the derived property.</p><p>Type derived property names in camel case (i.e.,<em>realizingActivities</em>). </p><p>A property name defined in camel case will be displayed in separate words with the first word capitalized. For example, realizingActivities will be changed to <em>Realizing Activities</em> (visible in the user interface).</p></ac:rich-text-body></ac:structured-macro></li><li><p>Edit property values specifying the derived property in the attribute's Specification window.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="132cd799-45f2-4220-b120-41f9cc97d533"><ac:rich-text-body><p>All properties are specified in the general specification pane. Some are also specified in the <strong>Tags</strong> specification pane. For detailed information, see the properties <ac:link ac:anchor="description_table"><ac:plain-text-link-body><![CDATA[description table]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro></li></ol><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="f710b5c7-ae79-4860-9574-a40c7ec4a352"><ac:rich-text-body><p>If you do not see the newly created derived property in the element’s <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>, please read the following:</p><ul><li>In the element’s <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>, the specified derived property is visible by default only in the <strong>All</strong> properties mode. First, try switching to this mode. Also try changing the mode in which you want the derived property to be visible (click the <strong>Customize</strong> button).</li><li>If you have specified the derived property for the element (with the <strong>Used UML Properties</strong> property of DSL customization specified) you must add the newly created derived property to the element’s visible properties list. For detailed information, please refer to <ac:link><ri:page ri:content-title="Derived properties visibility" /></ac:link>.</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="fe5b16f2-6483-4e62-ae01-03a9a126ada3"><ac:rich-text-body><p><span style="color: rgb(68,71,70);">If you need to further customize a customization’s derived property without modifying the existing customization itself, you can create a new customization that can inherit the former one’s properties via a generalization. Then you can redefine the inherited derived property to customize it. The redefining derived property of the new customization overrides that of the original customization.</span></p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">Derived property specification</h3><p><ac:image ac:align="center"><ri:attachment ri:filename="my_derived_property_specification_window.png" /></ac:image></p><h6 style="text-align: center;">The Specification window of the derived property</h6><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="f4cf1036-75fd-4f09-b4a8-783fee3f6362"><ac:parameter ac:name="">description_table</ac:parameter></ac:structured-macro>The following table describes the properties specified for the derived property.</p><table><colgroup class=""><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><th>Property</th><th>Description</th></tr><tr class=""><td><strong>Name</strong></td><td><p>The name of the property.<br />This name will be added and visible in the specification of the element whose type is defined as a customization target.</p></td></tr><tr class=""><td><strong>Type</strong></td><td><div class="content-wrapper"><p>The type of the derived property values. You may set a model element type or a data type (e.g., string, boolean, orintegerfrom the UML Standard Profile) as a property value.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="86bd63b3-1009-45eb-bfe0-d3bbf518febc"><ac:rich-text-body><p><span>To display classes and components as </span><span>property values, select the classifier as a type for the derived </span><span>property value.</span></p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr class=""><td><strong>Multiplicity</strong></td><td><div class="content-wrapper"><p>The multiplicity of the derived property values.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="00992981-69d2-4101-b56e-1a484480924c"><ac:rich-text-body><p><span>If the multiplicity is “0..1”, the derived property value will be </span><span>shown as single.</span><br /><span>If the multiplicity is “0..*”, the derived property values will be </span><span>shown as collection.</span></p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr class=""><td><p><strong>Is Read Only</strong></p></td><td><div class="content-wrapper"><p>If <em>true</em>, the derived property is read-only. You cannot edit the result elements for the derived property value.<br />If <em>false</em>, the property is read-write. You can edit the result elements for the derived property according to the expressions defined.</p></div></td></tr><tr class=""><td><strong>Is Ordered</strong></td><td><p>If <em>true</em>, the property values are always displayed in the same order.<br />If <em>false</em>, the property values are displayed in nonpredictable order.</p></td></tr><tr class=""><td><strong>Is Unique</strong></td><td><p>If <em>true</em>, the property values are unique. The same element is displayed only once.<br />If <em>false</em>, the property values may be displayed more than once.</p></td></tr><tr class=""><td><p><strong>Expression</strong></p></td><td><div class="content-wrapper"><p>One or more expressions of the derived property.<br />An expression defines the criterion for selecting result elements.</p><p>There are ten possible expression types:</p><ul><li><p>Metachain navigation (indirect relations through chains of properties)</p></li><li><p>Find</p></li><li><p>Union</p></li><li><p>Exclude</p></li><li><p>Filter</p></li><li><p>Various scripts</p></li><li>Implied Relation</li><li>Type Test</li><li>Property Test</li><li>Operation from Model <br /><br /></li></ul><p>The criterion for selecting the result elements can also be any combination of the expression types above.<br />For the detailed information, see <ac:link><ri:page ri:content-title="Defining expressions" /></ac:link>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9bf36350-11cd-45d0-b712-d7229b99c9a9"><ac:rich-text-body><p>Only one Simple Navigation operation criterion can be assigned to the expression of the derived property.   </p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr class=""><td colspan="1"><strong>Documentation</strong></td><td colspan="1"><p>The text displayed as the derived property description in the element’s <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> and Properties panel.</p></td></tr><tr class=""><td colspan="1"><strong>customizationTarget</strong></td><td colspan="1"><div class="content-wrapper"><p>The specified derived property will be added to one or more element types (stereotypes and/ or metaclasses).</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="945286fa-9ad8-49bb-8af2-91e37eab3f6f"><ac:rich-text-body><p><span>The expression calculations begin from the element type of the customization target.</span></p></ac:rich-text-body></ac:structured-macro></div></td></tr></tbody></table><p><br /></p><p class="ancestor-link parent-link"><strong>Related pages:</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MDTWRT/Extending+Metamodel+with+Derived+Properties">Extending Metamodel with Derived Properties</a></li><li class="ancestor-link"><a href="https://docs.nomagic.com/display/MDTWRT/Using+Customization+Data">Using Customization Data</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Creating+Customization+Data">Creating Customization Data</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Defining+expressions">Defining Expressions</a></li></ul>
````

<!--NOMAGIC_PAGE id=243973638 space=UPDG version=1 -->
## PAGE 00155: Creating Custom Rules for Relationships

- page_id: `243973638`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973638/Creating+Custom+Rules+for+Relationships
- version_number: 1
- version_date: `2025-07-31T19:04:50.256+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data
- labels: []

### NORMALIZED CONTENT

DSL relationships may have special rules to describe which elements can be connected. Use the following properties to define the relationships:

| Property | Description |
| --- | --- |
| Types for Source | Specifies metaclasses or allowed to connect as the source of the relationship. Types cannot conflict with UML permitted types for this relationship.NoteThe Types For Source property is intended for relationships only. The Customization Target property can be a relationship or a metaclass of a relationship. |
| Types for Target | Specifies metaclasses or allowed to connect as the target of the relationship. Types cannot conflict with UML permitted types for this relationship.NoteThe Types For Source property is intended for relationships only. The Customization Target property can be a relationship or a metaclass of a relationship. |

#### INFO: Note and Example

Note and Example

Subtypes of a specified end type are allowed only if the type is abstract (for example, the Classifier metaclass), otherwise only concrete types must be used. For example:

- If the value of the Types For Source property is the Classifier metaclass, then the Class, Component and other classifiers are allowed to connect as a source of a relationship.
- If the value of the Types For Source property is the Class metaclass, then the Class elements are allowed to connect as a source of a relationship.
- If the value of the Types For Source property is the «Block» DSL element, then the «Block» elements are allowed to connect as a source of a relationship.

In the following table, see properties that are used for customizing non-relationships:

| Property | Description |
| --- | --- |
| Allowed Relationships | Specifies types of relationships that are allowed to be connected to the DSL element. |
| Disallowed Relationships | Specifies types of relationships that are not allowed to be connected to the DSL element. |

#### INFO: Note and Example

Note and Example

Subtypes of specified allowed or disallowed relationships are analyzed only when a specified relationship type is an abstract metaclass (for example,*DirectedRelationship*). In other cases, only concrete types are checked.

- If «Trace» is allowed, subtypes of trace «copy» and «verify» are allowed also.
- If *Association* is allowed, *Extension (a* subtype) is not allowed, but simplestereotyped Associations are allowed. All DSL Associations are not allowed.
- If *Dependency*is not allowed, simple stereotyped Dependencies like «delegate» are not allowed, but subtypes of *Dependency*, for example, *Abstraction* and DSL types based on *Dependency*are allowed.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Creating Numbering Customizations' space='']
- [CONFLUENCE_PAGE title='Working with paths and relationships' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>DSL relationships may have special rules to describe which elements can be connected. Use the following properties to define the relationships:</p><table class="relative-table wrapped" style="width: 100.0%;"><colgroup> <col style="width: 21.49543%;" /> <col style="width: 78.486145%;" /> </colgroup><tbody><tr><th>Property</th><th>Description</th></tr><tr><td><strong>Types for Source</strong></td><td><div class="content-wrapper"><div class="layoutArea"><div class="column"><p><span>Specifies metaclasses or <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotypes]]></ac:plain-text-link-body></ac:link> allowed to connect as the source of the relationship. Types cannot conflict with UML permitted types for this relationship.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="53cfe691-884f-4108-b26c-fb882038e6c2"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p><span>The </span><strong>Types For Source</strong><span> property is intended for relationships only. The </span><strong>Customization Target</strong><span> property can be a relationship or a metaclass of a relationship.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></div></div></td></tr><tr><td><strong>Types for Target</strong></td><td><div class="content-wrapper"><div class="layoutArea"><div class="column"><p><span>Specifies metaclasses or <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotypes ]]></ac:plain-text-link-body></ac:link>allowed to connect as the target of the relationship. Types cannot conflict with UML permitted types for this relationship.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="68a50d53-84a4-4b5a-adfb-e3ad8f4ec050"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p><span>The </span><span> </span><strong>Types For Source </strong><span> </span><span>property is intended for relationships only. </span><span><span>The </span><strong>Customization Target</strong><span> property can be a relationship or a metaclass of a relationship.</span></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></div></div></td></tr></tbody></table><p class="auto-cursor-target"><br /></p><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="e6b69152-8a16-4f21-bb18-1298ba75181d"><ac:parameter ac:name="title">Note and Example</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p><span>Subtypes of a specified end type are allowed only if the type is abstract (for example, the Classifier metaclass), otherwise only concrete types must be used. For example:</span></p><ul><li>If the value of the <strong>Types For Source</strong> property is the Classifier metaclass, then the Class, Component and other classifiers are allowed to connect as a source of a relationship.</li><li>If the value of the <strong>Types For Source</strong> property is the Class metaclass, then the Class elements are allowed to connect as a source of a relationship.</li><li>If the value of the <strong>Types For Source</strong> property is the «Block» DSL element, then the «Block» elements are allowed to connect as a source of a relationship.</li></ul></div></div></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p>In the following table, see properties that are used for customizing non-relationships:</p><table class="wrapped"><colgroup> <col /> <col /> </colgroup><tbody><tr><th>Property</th><th>Description</th></tr><tr><td><strong>Allowed Relationships</strong></td><td><div class="layoutArea"><div class="column"><p><span>Specifies types of relationships that are allowed to be connected to the DSL element. </span></p></div></div></td></tr><tr><td colspan="1"><strong>Disallowed Relationships</strong></td><td colspan="1"><div class="layoutArea"><div class="column"><p><span>Specifies types of relationships that are </span><span>not</span> <span>allowed to be connected to the DSL element. </span></p></div></div></td></tr></tbody></table><p class="auto-cursor-target"><br /></p><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="f41835e3-ae4c-4e9d-a020-59be3fb63960"><ac:parameter ac:name="title">Note and Example</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p><span>Subtypes of specified allowed or disallowed relationships are analyzed only when a specified relationship type is an abstract metaclass (for example, </span><em>DirectedRelationship</em><span>). In other cases, only concrete types are checked. </span></p><ul><li><p><span>If «Trace» is allowed, subtypes of trace «copy» and «verify» are allowed also. </span></p></li><li><p><span>If </span> <em>Association </em> <span>is allowed,</span> <em>Extension (a</em> <span>subtype) is not allowed, but simple </span>stereotyped Associations are allowed. All DSL Associations are not allowed.</p></li><li><p><span>If </span> <em>Dependency </em><span>is not allowed, simple stereotyped Dependencies like «delegate» are not allowed, but subtypes of </span> <em>Dependency</em><span>, for example, </span> <em>Abstraction</em> <span>and DSL types based on</span> <em>Dependency </em><span>are allowed. </span></p></li></ul></div></div></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="68d6f843-19aa-480d-81e1-df3547d11a1b"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating Numbering Customizations" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Working with paths and relationships" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973552 space=UPDG version=1 -->
## PAGE 00156: Creating Customization Data

- page_id: `243973552`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973552/Creating+Customization+Data
- version_number: 1
- version_date: `2025-07-31T19:04:48.149+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization
- labels: []

### NORMALIZED CONTENT

In our modeling tool, customization creation begins by creating the following components:

- [ATTACHMENT filename='profile_diagrm.png'] [CONFLUENCE_PAGE title='Profile diagram' space='MDTWRT']
- [ATTACHMENT filename='stereotype_button.png'] [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT']
- [ATTACHMENT filename='customization_element (2).png'] Customization element.

[IMAGE alt='' src='']

###### Compounds of DSL customization creation

In the following figure, you can see an example of how customization data is passed to DSL elements through stereotypes.

[IMAGE alt='' src='']

###### Example of applying customization rules to DSL element

In the preceding figure, you can see the customization element, stereotype, class element, DSL element and relations between them. The *Company* stereotype element is set as customization target in the *Company* customization element. In addition, the *Company* stereotype is applied to the class element. The customization data from the *Company* customization element is passed to the class element. Thus, the class element becomes the DSL element. DSL element properties will appear in the [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] and the Properties panel of the DSL element as regular properties.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT']
- [CONFLUENCE_PAGE title='Profile diagram' space='MDTWRT']
- [CONFLUENCE_PAGE title='Specification window' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>In our modeling tool, customization creation begins by creating the following components:</p><ul><li><ac:image><ri:attachment ri:filename="profile_diagrm.png" /></ac:image> <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Profile diagram" /><ac:plain-text-link-body><![CDATA[Profile Diagram]]></ac:plain-text-link-body></ac:link></li><li><ac:image><ri:attachment ri:filename="stereotype_button.png" /></ac:image>  <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /></ac:link></li><li><ac:image><ri:attachment ri:filename="customization_element (2).png" /></ac:image> Customization element.</li></ul><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="customization_creation.png" /></ac:image></p><h6 style="text-align: center;">Compounds of DSL customization creation</h6><p>In the following figure, you can see an example of how customization data is passed to DSL elements through stereotypes. </p><p><ac:image ac:align="center"><ri:attachment ri:filename="customization_creation2.png" /></ac:image></p><h6 style="text-align: center;">Example of applying customization rules to DSL element</h6><div class="layoutArea"><div class="column"><p>In the preceding figure, you can see the customization element, stereotype, class element, DSL element and relations between them. The <em>Company</em> stereotype element is set as customization target in the <em>Company</em> customization element. In addition, the <em>Company</em> stereotype is applied to the class element. The customization data from the <em>Company</em> customization element is passed to the class element. Thus, the class element becomes the DSL element. DSL element properties will appear in the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> and the Properties panel of the DSL element as regular properties. </p><p><span><br /></span></p></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="bc26b85c-b417-4f34-ae40-4e49b382c613"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Profile diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973647 space=UPDG version=1 -->
## PAGE 00157: Creating Element - Specific Help Topics

- page_id: `243973647`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973647/Creating+Element+-+Specific+Help+Topics
- version_number: 1
- version_date: `2025-07-31T19:04:50.560+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data
- labels: []

### NORMALIZED CONTENT

1290299781

1290299801

1290299791

Define a string value referring to an element-specific help topic for each DSL element:

- By clicking the Help button in the element’s [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] .
- By pressing F1 , when the element’s symbol is selected.

To define a help topic ID for the DSL element

1. Select the appropriate [CONFLUENCE_PAGE title='Creating your First Customization' space=''] and open its Specification window.
2. In the general specification pane, select the Help ID property and type the help topic ID text.
3. Click **Close** when you are done. After updating the customization element specification, you must either reuse the DSL Customization profile in the model or reopen the model. The **Help ID** property is connected to the*documentation.server* [CONFLUENCE_PAGE title='Creating path variables' space='MDTWRT'], the default value of which**is *https://docs.nomagic.com*. The opened link is constructed in this way: '<*documentation.server* value> + /display/MD<modeling_tool_version>/ + <help ID text>'. 
Accessing such a link via **F1** or **Help** buttons opens the specified documentation page.

If an element represents two or more DSL elements, the first DSL element’s help topic ID will be taken.

If the DSL type customization does not have the **Help ID** property defined, the help topic ID derives from the more general stereotype customization (ancestor) of the **Help ID** property. If there is no ancestor, the metaclass help opens.

1290299770

**Related pages**

- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Creating Customization Data' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="347e7cf0-7bbb-4773-8f63-c9fb44fef353"><ac:parameter ac:name="id">1290299781</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="1ee3896a-1b0b-46f7-926e-aee48600a2d3"><ac:parameter ac:name="id">1290299801</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="50ad88c2-ece2-4103-a9de-7a27b2f2d760"><ac:parameter ac:name="id">1290299791</ac:parameter><ac:rich-text-body><p>Define a string value referring to an element-specific help topic for each DSL element:</p><ul><li>By clicking the <strong>Help</strong> button in the element’s <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>.</li><li>By pressing <strong>F1</strong>, when the element’s symbol is selected.</li></ul><p><br /></p><p>To define a help topic ID for the DSL element</p><hr /><ol><li>Select the appropriate <ac:link><ri:page ri:content-title="Creating your First Customization" /><ac:plain-text-link-body><![CDATA[customization element]]></ac:plain-text-link-body></ac:link> and open its Specification window.</li><li>In the general specification pane, select the <strong>Help ID</strong> property and type the help topic ID text.</li><li><p>Click <strong>Close</strong> when you are done. After updating the customization element specification, you must either reuse the DSL Customization profile in the model or reopen the model. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="fbb6959d-c28e-41b9-83b0-5f501f09936d"><ac:rich-text-body><p>The <strong>Help ID</strong> property is connected to the<em> documentation.server</em> <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Creating path variables" /><ac:plain-text-link-body><![CDATA[path variable]]></ac:plain-text-link-body></ac:link>, the default value of which<em> </em>is <em><span class="nolink">https://docs.nomagic.com</span></em>. The opened link is constructed in this way: '&lt;<em>documentation.server</em> value&gt; + /display/MD&lt;modeling_tool_version&gt;/ + &lt;help ID text&gt;'. <br />Accessing such a link via <strong>F1</strong> or <strong>Help</strong> buttons opens the specified documentation page.</p></ac:rich-text-body></ac:structured-macro></li></ol><p>If an element represents two or more DSL elements, the first DSL element’s help topic ID will be taken.</p><p>If the DSL type customization does not have the <strong>Help ID</strong> property defined, the help topic ID derives from the more general stereotype customization (ancestor) of the <strong>Help ID</strong> property. If there is no ancestor, the metaclass help opens.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f18f4f39-29fa-411b-8459-36be51cbbd47"><ac:parameter ac:name="id">1290299770</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973599 space=UPDG version=1 -->
## PAGE 00158: Creating Inheritance of DSL Customization

- page_id: `243973599`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973599/Creating+Inheritance+of+DSL+Customization
- version_number: 1
- version_date: `2025-07-31T19:04:49.268+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data
- labels: []

### NORMALIZED CONTENT

861184440

861184453

861184443

DSL customization is inherited when a stereotype is inherited. So, it is not necessary to create new DSL customization.For example, to create your own subtype of SysML «Requirement», named, let's say, *Performance Requirement*, it is enough to define a new stereotype «Performance Requirement» and add a generalization between the SysML «Requirement» stereotype and the «Performance Requirement» stereotype. As a result, all predefined symbol properties (style) and semantic rules of SysML «Requirement» will be reused on elements stereotyped by «Performance Requirement». In the case where the custom stereotype has its own customization, its properties can be overwritten, inherited, or merged.

[IMAGE alt='' src='']

###### «Performance Requirement» stereotype inherits the customization of the SysML «Requirement» through a generalization.

The rules for inheriting/merging/overwriting customization properties are provided in the table below:

|  | Empty customizations | Customizations with overwritten values |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Original | Stereotype and customization are inherited | Stereotype is inherited, customization is not inherited | Stereotype is not inherited, customization is inherited | Stereotype and customization are inherited | Stereotype is inherited, customization is not inherited | Stereotype is not inherited, customization is inherited |
| customizationTarget | - | - | - | - | - | - |
| hideMetatype | Inherited | Inherited | Overwritten | Overwritten | Overwritten |  |
| keyword | - | - |  |  |  |  |
| representationText |  |  |  |  |  |  |
| standardExpertConfiguration | Inherited | Inherited |  |  |  |  |
| usedUMLProperties | Merged |  |  |  |  |  |
| applyToSource | Inherited |  |  |  |  |  |
| applyToTarget |  |  |  |  |  |  |
| superTypes |  |  |  |  |  |  |
| allowedRelationships |  |  |  |  |  |  |
| disallowedRelationships |  |  |  |  |  |  |
| typesForSource |  |  |  |  |  |  |
| typesForTarget |  |  |  |  |  |  |
| connectionRule | - | - | - | - | - |  |
| quickApplyingFor | Inherited | Inherited | Overwritten | Merged | Overwritten |  |
| hiddenOwnedDiagrams | - | Overwritten |  |  |  |  |
| hiddenOwnedTypes |  |  |  |  |  |  |
| suggestedOwnedDiagrams |  |  |  |  |  |  |
| suggestedOwnedTypes |  |  |  |  |  |  |
| inShortcutMenu |  |  |  |  |  |  |
| showPropertiesWhenNotApplied |  |  |  |  |  |  |
| possibleOwners |  |  |  |  |  |  |
| multiLineTextProperties |  |  |  |  |  |  |
| category |  |  |  |  |  |  |
| checkSpelling | Inherited | Merged |  |  |  |  |
| defaultShapeSize | - | Overwritten |  |  |  |  |
| doNotSuggestAsType | Inherited |  |  |  |  |  |
| helpID | - | - | - |  |  |  |
| preferredMetatype | Inherited | Inherited | Inherited | Inherited |  |  |
| showPropertiesWhenNotAppliedLimitedByProfileApplication | - | Overwritten |  |  |  |  |
| showPropertiesWhenNotAppliedLimitedByElementType |  |  |  |  |  |  |
| allowedDragAndDrops |  |  |  |  |  |  |
| abbreviation |  |  |  |  |  |  |
| additionalContent | Inherited |  |  |  |  |  |
| subElementContentsIncluded |  |  |  |  |  |  |
| doNotSuggestNameAutoCompletion |  |  |  |  |  |  |
| symbolStandardExpertConfiguration | - |  |  |  |  |  |

861184439

**Related Pages**

- Creating Customization Data
- Using Customization Data

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ff4fc0bd-064b-42b5-b9e0-aa332379548e"><ac:parameter ac:name="id">861184440</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ab7ee9ee-ecd6-4ccf-9dcb-e36f218be637"><ac:parameter ac:name="id">861184453</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8bf958be-1c56-4b30-916e-9935558e9afe"><ac:parameter ac:name="id">861184443</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p><span>DSL customization is inherited when a stereotype is inherited. So, it is not necessary to create new DSL customization. </span>For example, to create your own subtype of SysML «Requirement», named, let's say, <em style="letter-spacing: 0.0px;">Performance Requirement</em>, it is enough to define a new stereotype «Performance Requirement» and add a generalization between the SysML «Requirement» stereotype and the «Performance Requirement» stereotype. As a result, all predefined symbol properties (style) and semantic rules of SysML «Requirement» will be reused on elements stereotyped by «Performance Requirement». In the case where the custom stereotype has its own customization, its properties can be overwritten, inherited, or merged.<br /><br /></p><p><ac:image ac:align="center" ac:border="true" ac:height="194" ac:width="325"><ri:attachment ri:filename="Creating_Inheritance_of_DSL_Customization.png" /></ac:image></p><h6 style="text-align: center;margin-bottom: 30.0px;"> «Performance Requirement» stereotype inherits the customization of the SysML «Requirement» through a generalization.</h6><p>The rules for inheriting/merging/overwriting customization properties are provided in the table below:</p><table class="relative-table wrapped" style="width: 97.6413%;"><colgroup> <col style="width: 22.1473%;" /> <col style="width: 17.3693%;" /> <col style="width: 12.76%;" /> <col style="width: 10.9612%;" /> <col style="width: 10.905%;" /> <col style="width: 12.0292%;" /> <col style="width: 13.828%;" /> </colgroup><tbody><tr><th><br /></th><th style="text-align: center;" colspan="3">Empty customizations</th><th style="text-align: center;" colspan="3">Customizations with overwritten values</th></tr><tr><th colspan="1">Original</th><th colspan="1">Stereotype and customization are inherited</th><th colspan="1">Stereotype is inherited, customization is not inherited</th><th colspan="1">Stereotype is not inherited, customization is inherited</th><th colspan="1">Stereotype and customization are inherited</th><th colspan="1">Stereotype is inherited, customization is not inherited</th><th colspan="1">Stereotype is not inherited, customization is inherited</th></tr><tr><td colspan="1">customizationTarget</td><td style="text-align: center;" colspan="1">-</td><td rowspan="6"><p style="text-align: center;"><br /></p><p style="text-align: center;">-</p></td><td style="text-align: center;" colspan="1">-</td><td style="text-align: center;" colspan="1">-</td><td style="text-align: center;" colspan="1">-</td><td style="text-align: center;" colspan="1">-</td></tr><tr><td colspan="1">hideMetatype</td><td style="text-align: center;" colspan="1">Inherited</td><td style="text-align: center;" colspan="1">Inherited</td><td rowspan="12"><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p style="text-align: center;">Overwritten</p></td><td style="text-align: center;" rowspan="4"><p><br /></p><p><br /></p><p>Overwritten</p></td><td rowspan="12"><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p style="text-align: center;"><br /></p><p style="text-align: center;">Overwritten</p><p style="text-align: center;"><br /></p></td></tr><tr><td colspan="1">keyword</td><td style="text-align: center;" rowspan="2"><p><br /></p><p>-</p></td><td rowspan="2"><p style="text-align: center;"><br /></p><p style="text-align: center;">-</p></td></tr><tr><td colspan="1">representationText</td></tr><tr><td colspan="1">standardExpertConfiguration</td><td rowspan="23"><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p style="text-align: center;"><br /></p><p style="text-align: center;">Inherited</p></td><td rowspan="9"><p><br /></p><p><br /></p><p style="text-align: center;"><br /></p><p style="text-align: center;"><br /></p><p style="text-align: center;">Inherited</p></td></tr><tr><td colspan="1">usedUMLProperties</td><td rowspan="8"><p><br /></p><p><br /></p><p style="text-align: center;"><br /></p><p style="text-align: center;">Merged</p></td></tr><tr><td colspan="1">applyToSource</td><td rowspan="7"><p><br /></p><p><br /></p><p><br /></p><p style="text-align: center;">Inherited</p></td></tr><tr><td colspan="1">applyToTarget</td></tr><tr><td colspan="1">superTypes</td></tr><tr><td colspan="1">allowedRelationships</td></tr><tr><td colspan="1">disallowedRelationships</td></tr><tr><td colspan="1">typesForSource</td></tr><tr><td colspan="1">typesForTarget</td></tr><tr><td colspan="1">connectionRule</td><td style="text-align: center;" colspan="1">-</td><td style="text-align: center;" colspan="1">-</td><td style="text-align: center;" colspan="1">-</td><td style="text-align: center;" colspan="1">-</td><td style="text-align: center;" colspan="1">-</td></tr><tr><td colspan="1">quickApplyingFor</td><td style="text-align: center;" colspan="1">Inherited</td><td rowspan="13"><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p style="text-align: center;">Inherited</p></td><td rowspan="23"><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p style="text-align: center;"><br /></p><p style="text-align: center;"><br /></p><p style="text-align: center;"><br /></p><p style="text-align: center;">Overwritten</p></td><td style="text-align: center;" colspan="1">Merged</td><td rowspan="23"><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p style="text-align: center;"><br /></p><p style="text-align: center;">Overwritten</p></td></tr><tr><td colspan="1">hiddenOwnedDiagrams</td><td style="text-align: center;" rowspan="9"><p><br /> <br /> <br /> <br /> <br />-</p></td><td rowspan="9"><p><br /></p><p><br /></p><p><br /></p><p style="text-align: center;"><br /></p><p style="text-align: center;">Overwritten</p></td></tr><tr><td colspan="1">hiddenOwnedTypes</td></tr><tr><td colspan="1">suggestedOwnedDiagrams</td></tr><tr><td colspan="1">suggestedOwnedTypes</td></tr><tr><td colspan="1">inShortcutMenu</td></tr><tr><td colspan="1">showPropertiesWhenNotApplied</td></tr><tr><td colspan="1">possibleOwners</td></tr><tr><td colspan="1">multiLineTextProperties</td></tr><tr><td colspan="1">category</td></tr><tr><td colspan="1">checkSpelling</td><td style="text-align: center;" colspan="1">Inherited</td><td style="text-align: center;" colspan="1">Merged</td></tr><tr><td colspan="1">defaultShapeSize</td><td style="text-align: center;" colspan="1">-</td><td rowspan="3"><p><br /></p><p style="text-align: center;">Overwritten</p></td></tr><tr><td colspan="1">doNotSuggestAsType</td><td style="text-align: center;" colspan="1">Inherited</td></tr><tr><td colspan="1">helpID</td><td style="text-align: center;" colspan="1">-</td><td style="text-align: center;" colspan="1">-</td><td style="text-align: center;" colspan="1">-</td></tr><tr><td colspan="1">preferredMetatype</td><td rowspan="9"><p><br /></p><p><br /></p><p><br /></p><p style="text-align: center;"><br /></p><p style="text-align: center;">Inherited</p></td><td style="text-align: center;" colspan="1">Inherited</td><td rowspan="9"><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p style="text-align: center;">Inherited</p></td><td style="text-align: center;" colspan="1">Inherited</td></tr><tr><td colspan="1">showPropertiesWhenNotAppliedLimitedByProfileApplication</td><td rowspan="4"><p style="text-align: center;"><br /> <br />-</p></td><td rowspan="8"><p><br /></p><p><br /></p><p><br /></p><p style="text-align: center;">Overwritten</p></td></tr><tr><td colspan="1">showPropertiesWhenNotAppliedLimitedByElementType</td></tr><tr><td colspan="1">allowedDragAndDrops</td></tr><tr><td colspan="1">abbreviation</td></tr><tr><td colspan="1">additionalContent</td><td rowspan="3"><p><br /></p><p style="text-align: center;">Inherited</p></td></tr><tr><td colspan="1">subElementContentsIncluded</td></tr><tr><td colspan="1">doNotSuggestNameAutoCompletion</td></tr><tr><td colspan="1">symbolStandardExpertConfiguration</td><td style="text-align: center;" colspan="1">-</td></tr></tbody></table></div></div></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f2b10301-000a-4093-bf7c-cec4fbe36d18"><ac:parameter ac:name="id">861184439</ac:parameter><ac:rich-text-body><p><strong>Related Pages</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MDTWRT/Creating+Customization+Data">Creating Customization Data</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Using+Customization+Data">Using Customization Data</a></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973533 space=UPDG version=1 -->
## PAGE 00159: Creating new dependency matrix type

- page_id: `243973533`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973533/Creating+new+dependency+matrix+type
- version_number: 1
- version_date: `2025-07-31T19:04:47.681+02:00`
- ancestors: UML Profiling and DSL Guide > Customizing diagrams
- labels: ['creating-dependency-matrix-type', 'dependency-matrix-customization', 'customizing-dependency-matrix']

### NORMALIZED CONTENT

Creating new dependency matrix types is available in Standard, Professional, Architect and Enterprise editions.

The **Customize Dependency Matrix Wizard** contains the following steps for creating a new dependency matrix type or modifying a chosen one.

3

##### Step 1: Specify Name for a New Matrix Type and Icons

To create your own custom matrix type, first define the following properties

- Matrix type name (for example, UseCase-Actors).
- Abbreviation – a short form of the dependency matrix type. It is displayed on the diagram overview shape of the custom matrix, when the Show Abbreviated Type property is set to true .
- Category – your specific category where the new matrix type will be stored. The category is displayed on the main menu under Diagrams and in the command list of Create Diagram on the Model Browser shortcut menu. You can keep the default value, if you need the new matrix type to be stored in the Analysis Diagrams category.
- Help ID – sets a specific Help ID to invoke help or documentation topics .
- Icons – several icons for the new dependency matrix type representation in GUI. [ATTACHMENT filename='Matrix_Wizard.png']

##### Step 2: Specify Used Projects

Select the required used projects or profiles.

Do not remove the UML Standard Profile, which is selected by default, from the list. It must be used by any custom dependency matrix type.

[IMAGE alt='' src='']

A custom dependency matrix can represent the relationships among stereotyped elements. Profiles that define these stereotypes must be used by the custom dependency matrix type.

All the selected used projects or profiles load when a dependency matrix of the custom matrix type is created in the project.

To choose the stereotype for the custom dependency matrix type

- Click the Diagram Stereotype button.

##### Step 3: Specify Dependency Matrix Properties

This step allows you to specify the appearance of the new dependency matrix type. For example, you can predefine the default column text direction, row and column scope, and so forth.

| Property name | Description |
| --- | --- |
| Dependency Matrix |  |
| Legend Location | Select to choose the location of the legend (Top-Left Corner or Above Column Header) or set the Do Not Display mode to keep it hidden. |
| Take Whole Model As Scope | Set to true to select the whole model as a scope for relation analysis. The root package Model will be selected by default in both the Row Scope and Column Scope boxes. |
| Direction | Select a direction of relationships for the relation analysis and representation in the dependency matrix. Be aware that new relationships will be created with the selected direction. |
| Dependency Criteria | Select an expression type and specify the expression to be used as the relation criteria. |
| Show Elements | Select to show only related (by a selected dependency criteria), only non- related, or all elements. |
| Show Inner Dependencies | Set to true to show the number of relationships in every owning element cell. |
| Suppress Criteria Area | Set to true to suppress the Criteria area toolbar. |
| Read Only | Set to true to make the matrix read-only. You will not be able to create or delete relationships. |
| Description Area | Type the description for the dependency matrix. The text will be displayed in the description area of the matrix. |
| Hide Types | Set to true to hide the Row Element Type and Column Element Type boxes from the Criteria area. |
| Hide Scope | Set to true to hide the Row Element Scope and Column Element Scope boxes from the Criteria area. |
| Hide Dependency Criteria | Set to true to hide the Dependency Criteria and Direction boxes from the Criteria area. |
| Column |  |
| Column Scope Defined | Set to true to take empty scope as a whole model. |
| Column Types Include Subtypes | Set to true to display subtypes of selected element types, for example, if a class is selected, then all its subtypes, such as component or custom subtypes, will be displayed. |
| Column Owner Display Mode | Select the Compact tree mode to display elements with their direct and common owners in the column header. The data will be represented as a tree.Select the Complete tree mode to display elements with all their owners in the column header. The data will be represented as a tree.Select the Hidden mode to display elements without any owners in the column header. The data will be represented as a list.Select the Full qualified name mode to display elements with their owners in the column header. The data will be represented as a list. |
| Column Text Direction | Specify the direction of the text in the column header. Be aware that this property value can be applied only when the Column Owner Display Mode property value is Hidden or Full qualified name. |
| Column Element Type | Specify the element types to show in the columns of the dependency matrix. |
| Column Query | Select Containment or Custom to specify the expression to collect column elements. |
| Column Property Filter | Select properties and their values to create more specific filters for column elements. |
| Column Sorting Mode | Select Ascending or Descending to sort elements alphabetically. You can also select the Custom sorting mode to use your own order. |
| Column Header Height | Specify the height of the column header in pixels. |
| Column Types Include Subtypes | Set to true to display subtypes of selected element types. For example, if a class is selected, then all its subtypes (such as component or custom subtypes like SysML block) and requirements will be displayed. |
| Row |  |
| Row Scope Defined | Set to true to take empty scope as a whole model. |
| Row Types Include Subtypes | Set to true to display the subtypes of selected element types. For example, if a class is selected, all its subtypes (such as component or custom subtypes like SysML block) and requirements will be displayed. |
| Row Owner Display Mode | Select the Compact tree mode to display elements with their direct and common owners in the row header. The data will be represented as a tree.Select the Complete tree mode to display elements with all their owners in the row header. The data will be represented as a tree.Select the Hidden mode to display elements without any owners in the row header. The data will be represented as a list.Select the Full qualified name mode to display elements with their owners in the row header. The data will be represented as a list. |
| Row Element Type | Specify the element types to show in the rows of the dependency matrix. |
| Row Query | Select Containment or Custom to specify the expression to collect row elements. |
| Row Property Filter | Select properties and their values to create more specific filters for row elements. |
| Row Sorting Mode | Select Ascending or Descending to sort elements alphabetically. You can also select the Custom sorting mode to use your own order. |
| Row Header Width | Specify the width of the row header in pixels. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="76ad6fcd-b71e-4911-87e4-3a21ffae70fb"><ac:rich-text-body><p>Creating new dependency matrix types is available in Standard, Professional, Architect and Enterprise editions.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>The <strong>Customize Dependency Matrix Wizard</strong> contains the following steps for creating a new dependency matrix type or modifying a chosen one.</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="53b800e0-dc7b-4411-9d0e-97905b7c89b3"><ac:parameter ac:name="maxLevel">3</ac:parameter></ac:structured-macro></p><h3>Step 1: Specify Name for a New Matrix Type and Icons</h3><p>To create your own custom matrix type, first define the following properties</p><hr /><ul><li>Matrix type name (for example, UseCase-Actors).</li><li>Abbreviation – a short form of the dependency matrix type. It is displayed on the diagram overview shape of the custom matrix, when the <strong>Show</strong> <strong>Abbreviated Type</strong> property is set to <em>true</em>.</li><li>Category – your specific category where the new matrix type will be stored. The category is displayed on the main menu under <strong>Diagrams</strong> and in the command list of <strong>Create Diagram</strong> on the <strong>Model Browser</strong> shortcut menu. You can keep the default value, if you need the new matrix type to be stored in the <strong>Analysis Diagrams</strong> category.</li><li>Help ID – <span style="color: rgb(62,63,64);">sets a specific Help ID to invoke help or documentation topics</span>.</li><li>Icons – several icons for the new dependency matrix type representation in GUI.<br /><br /><ac:image ac:align="center"><ri:attachment ri:filename="Matrix_Wizard.png" /></ac:image></li></ul><h3>Step 2: Specify Used Projects</h3><p><span>Select the required used projects or profiles. </span></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="c6fcda04-7151-4e4e-80d5-e419321e7c36"><ac:rich-text-body><p>Do not remove the UML Standard Profile, which is selected by default, from the list. It must be used by any custom dependency matrix type.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><ac:image ac:align="center"><ri:attachment ri:filename="Dependency_matrix_wizard.png" /></ac:image></p><p>A custom dependency matrix can represent the relationships among stereotyped elements. Profiles that define these stereotypes must be used by the custom dependency matrix type.</p><p>All the selected used projects or profiles load when a dependency matrix of the custom matrix type is created in the project.</p><p><br class="atl-forced-newline" />To choose the stereotype for the custom dependency matrix type</p><hr /><ul><li>Click the <strong>Diagram Stereotype</strong> button.</li></ul><h3>Step 3: Specify Dependency Matrix Properties</h3><p><span><ac:inline-comment-marker ac:ref="fa81eb32-524f-4f9b-94b6-b8f34013455e">This step allows you to specify the appearance of the new dependency matrix type. For example, you can predefine the default column text direction, row and column scope, and so forth.</ac:inline-comment-marker></span></p><table class="relative-table" style="width: 84.147%;"><colgroup><col style="width: 15.7208%;" /><col style="width: 84.2792%;" /></colgroup><tbody><tr><td colspan="1"><span style="color: rgb(51,51,51);"><strong>Property name</strong> </span></td><td colspan="1"><span style="color: rgb(51,51,51);"> <strong>Description</strong> </span></td></tr><tr><td colspan="2"><span style="color: rgb(51,51,51);"> <strong>Dependency Matrix</strong> </span></td></tr><tr><td colspan="1"><span style="color: rgb(51,51,51);"><strong>Legend Location</strong></span></td><td colspan="1"><span style="color: rgb(51,51,51);">Select to choose the location of the legend (<strong>Top-Left Corner</strong> or <strong>Above Column Header</strong>) or set the <strong>Do Not Display</strong> mode to keep it hidden.</span></td></tr><tr><td><p><span style="color: rgb(51,51,51);"><strong>Take Whole Model</strong> <strong>As</strong> <strong>Scope</strong> </span></p></td><td><p><span style="color: rgb(51,51,51);">Set to <em>true</em> to select the whole model as a scope for <ac:inline-comment-marker ac:ref="610d1515-a033-4b00-ba49-45f860e1a841">relation</ac:inline-comment-marker> analysis. The root package <em>Model</em> will be selected by default in both the <strong>Row Scope</strong> and <strong>Column Scope</strong> boxes.</span></p></td></tr><tr><td><p><span style="color: rgb(51,51,51);"><strong>Direction</strong> </span></p></td><td><p><span style="color: rgb(51,51,51);">Select a direction of relationships for the <ac:inline-comment-marker ac:ref="664dd430-8ce9-453f-af1f-4e96424243fc">relation</ac:inline-comment-marker> analysis and representation in the dependency matrix. Be aware that new relationships will be created with the selected direction.</span></p></td></tr><tr><td><p><span style="color: rgb(51,51,51);"><strong>Dependency Criteria</strong> </span></p></td><td><p><span style="color: rgb(51,51,51);">Select an expression type and specify the expression to be used as the relation criteria. </span></p></td></tr><tr><td><p><span style="color: rgb(51,51,51);"><strong>Show Elements</strong> </span></p></td><td><p><span style="color: rgb(51,51,51);">Select to show only related (by a selected dependency criteria), only non- related, or all elements.</span></p></td></tr><tr><td colspan="1"><p><span style="color: rgb(51,51,51);"><strong>Show Inner</strong> <strong>Dependencies</strong> </span></p></td><td colspan="1"><p><span style="color: rgb(51,51,51);">Set to <em>true</em> to show the number of relationships in every owning element cell.</span></p></td></tr><tr><td colspan="1"><p><span style="color: rgb(51,51,51);"><strong>Suppress Criteria</strong> <strong>Area</strong> </span></p></td><td colspan="1"><p><span style="color: rgb(51,51,51);">Set to <em>true</em> to suppress the <strong>Criteria</strong> area toolbar.</span></p></td></tr><tr><td colspan="1"><p><span style="color: rgb(51,51,51);"><strong>Read Only</strong> </span></p></td><td colspan="1"><p><span style="color: rgb(51,51,51);">Set to <em>true</em> to make the matrix read-only. You will not be able to create or delete relationships.</span></p></td></tr><tr><td colspan="1"><p><span style="color: rgb(51,51,51);"><strong>Description</strong> <strong>Area</strong> </span></p></td><td colspan="1"><p><span style="color: rgb(51,51,51);">Type the description for the dependency matrix. The text will be displayed in the description area of the matrix.</span></p></td></tr><tr><td><p><span style="color: rgb(51,51,51);"><strong>Hide Types</strong> </span></p></td><td><p><span style="color: rgb(51,51,51);">Set to <em>true</em> to hide the <strong>Row Element Type</strong> and <strong>Column Element Type</strong> boxes from the <strong>Criteria</strong> area.</span></p></td></tr><tr><td><p><span style="color: rgb(51,51,51);"><strong>Hide Scope</strong> </span></p></td><td><p><span style="color: rgb(51,51,51);">Set to <em>true</em> to hide the <strong>Row Element Scope</strong> and <strong>Column Element Scope </strong>boxes from the <strong>Criteria</strong> area.</span></p></td></tr><tr><td><p><span style="color: rgb(51,51,51);"><strong>Hide Dependency</strong> <strong>Criteria</strong> </span></p></td><td><p><span style="color: rgb(51,51,51);">Set to <em>true</em> to hide the <strong>Dependency</strong> <strong>Criteria</strong> and <strong>Direction</strong> boxes from the <strong>Criteria </strong>area.</span></p></td></tr><tr><td colspan="2"><span style="color: rgb(51,51,51);"><strong>Column</strong> </span></td></tr><tr><td colspan="1"><span style="color: rgb(51,51,51);"><strong>Column Scope Defined</strong></span></td><td colspan="1"><span style="color: rgb(51,51,51);">Set to <em>true</em> to take empty scope as a whole model.</span></td></tr><tr><td colspan="1"><span style="color: rgb(51,51,51);"><strong>Column Types Include Subtypes</strong></span></td><td colspan="1"><span style="color: rgb(51,51,51);">Set to <em>true</em> to display subtypes of selected element types, for example, if a class is selected, then all its subtypes, such as component or custom subtypes, will be displayed. </span></td></tr><tr><td colspan="1"><p><span style="color: rgb(51,51,51);"><strong>Column Owner Display</strong> <strong>Mode</strong> </span></p></td><td colspan="1"><ul><li><span style="color: rgb(51,51,51);">Select the <strong>Compact tree</strong> mode to display elements with their direct and common owners in the column header. The data will be represented as a tree.</span></li><li><span style="color: rgb(51,51,51);">Select the <strong>Complete tree</strong> mode to display elements with all their owners in the column header. The data will be represented as a tree.</span></li><li><span style="color: rgb(51,51,51);">Select the <strong>Hidden</strong> mode to display elements without any owners in the column header. The data will be represented as a list.</span></li><li><span style="color: rgb(51,51,51);">Select the <strong>Full qualified name</strong> mode to display elements with their owners in the column header. The data will be represented as a list.</span></li></ul></td></tr><tr><td colspan="1"><p><span style="color: rgb(51,51,51);"><strong>Column Text Direction</strong> </span></p></td><td colspan="1"><p><span style="color: rgb(51,51,51);">Specify the direction of the text in the column header. Be aware that this property value can be applied only when the <strong>Column Owner Display Mode</strong> property value is <strong>Hidden</strong> or <strong>Full qualified name</strong>.</span></p></td></tr><tr><td colspan="1"><p><span style="color: rgb(51,51,51);"><strong>Column Element Type</strong> </span></p></td><td colspan="1"><p><span style="color: rgb(51,51,51);">Specify the element types to show in the columns of the dependency matrix.</span></p></td></tr><tr><td colspan="1"><span style="color: rgb(51,51,51);"><strong>Column Query</strong></span></td><td colspan="1"><span style="color: rgb(51,51,51);">Select <strong>Containment</strong> or <strong>Custom</strong> to specify the expression to collect column elements.</span></td></tr><tr><td colspan="1"><p><span style="color: rgb(51,51,51);"><strong>Column Property Filter</strong> </span></p></td><td colspan="1"><p><span style="color: rgb(51,51,51);">Select properties and their values to create more specific filters for column elements.</span></p></td></tr><tr><td colspan="1"><strong>Column Sorting Mode</strong></td><td colspan="1">Select<strong> Ascending</strong> or <strong>Descending</strong> to sort elements alphabetically. You can also select the <strong>Custom </strong> sorting mode to use your own order.</td></tr><tr><td><p><span style="color: rgb(51,51,51);"><strong>Column Header Height</strong> </span></p></td><td><p><span style="color: rgb(51,51,51);">Specify the height of the column header in pixels.</span></p></td></tr><tr><td><p><span style="color: rgb(51,51,51);"><strong>Column Types Include</strong> <strong>Subtypes</strong> </span></p></td><td><p><span style="color: rgb(51,51,51);">Set to <em>true</em> to display subtypes of selected element types. For example, if a class is selected, then all its subtypes (such as component or custom subtypes like SysML block) and requirements will be displayed.</span></p></td></tr><tr><td colspan="2"><p><span style="color: rgb(51,51,51);"><strong>Row </strong> </span></p></td></tr><tr><td colspan="1"><span style="color: rgb(51,51,51);"><strong>Row Scope Defined</strong></span></td><td colspan="1"><span style="color: rgb(51,51,51);">Set to <em>true </em>to take empty scope as a whole model.</span></td></tr><tr><td colspan="1"><span style="color: rgb(51,51,51);"><strong>Row Types Include Subtypes</strong></span></td><td colspan="1"><span style="color: rgb(51,51,51);">Set to <em>true</em> to display the subtypes of selected element types. For example, if a class is selected, all its subtypes (such as component or custom subtypes like SysML block) and requirements will be displayed.</span></td></tr><tr><td colspan="1"><p><span style="color: rgb(51,51,51);"><strong>Row Owner Display</strong> <strong>Mode</strong> </span></p></td><td colspan="1"><ul><li><span style="color: rgb(51,51,51);">Select the <strong>Compact tree</strong> mode to display elements with their direct and common owners in the row header. The data will be represented as a tree.</span></li><li><span style="color: rgb(51,51,51);">Select the <strong>Complete tree</strong> mode to display elements with all their owners in the row header. The data will be represented as a tree.</span></li><li><span style="color: rgb(51,51,51);">Select the <strong>Hidden</strong> mode to display elements without any owners in the row header. The data will be represented as a list.</span></li><li><span style="color: rgb(51,51,51);">Select the <strong>Full qualified name</strong> mode to display elements with their owners in the row header. The data will be represented as a list.</span></li></ul></td></tr><tr><td colspan="1"><p><span style="color: rgb(51,51,51);"><strong>Row Element Type</strong> </span></p></td><td colspan="1"><p><span style="color: rgb(51,51,51);">Specify the element types to show in the rows of the dependency matrix.</span></p></td></tr><tr><td colspan="1"><span style="color: rgb(51,51,51);"><strong>Row Query</strong></span></td><td colspan="1"><span style="color: rgb(51,51,51);">Select <strong>Containment</strong> or <strong>Custom</strong> to specify the expression to collect row elements.</span></td></tr><tr><td colspan="1"><p><span style="color: rgb(51,51,51);"><strong>Row Property Filter</strong> </span></p></td><td colspan="1"><p><span style="color: rgb(51,51,51);">Select properties and their values to create more specific filters for row elements.</span></p></td></tr><tr><td colspan="1"><span style="color: rgb(51,51,51);"><strong>Row Sorting Mode</strong></span></td><td colspan="1"><span>Select</span><strong> Ascending</strong><span> or </span><strong>Descending</strong><span> to sort elements alphabetically. You can also select the </span><strong>Custom </strong><span> sorting mode to use your own order.</span></td></tr><tr><td colspan="1"><p><span style="color: rgb(51,51,51);"><strong>Row Header Width</strong> </span></p></td><td colspan="1"><p><span style="color: rgb(51,51,51);">Specify the width of the row header in pixels.</span></p></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243973515 space=UPDG version=1 -->
## PAGE 00160: Creating new diagram type

- page_id: `243973515`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973515/Creating+new+diagram+type
- version_number: 1
- version_date: `2025-07-31T19:04:47.539+02:00`
- ancestors: UML Profiling and DSL Guide > Customizing diagrams
- labels: ['creating-diagram-type', 'diagram-customization', 'customizing-diagrams']

### NORMALIZED CONTENT

The **Customize Diagram Wizard** contains the following steps for creating a new diagram type or modifying a chosen one.

3

All Custom Diagrams are based on standard UML diagrams (like Class, Use Case, Sequence, and other).

##### Step 1: Specify diagram type and icon

To create your own diagram, first specify the following properties

- Diagram type name (for example, Robustness Diagram).
- Base Diagram Type – standard UML diagram to be extended. All configurations, semantics, and other settings will be inherited from this diagram type.
- Abbreviation – a short form of the diagram name. It will be used in Diagram Frames header or Diagram shapes in Content diagrams.
- Category – creates your specific category in the Diagrams menu or in the Create Diagram command list. You can store all your customized diagrams in this category. If you leave this field empty, the customized diagrams will be added to the Custom Diagrams category.
- Help ID – sets a specific Help ID to invoke help or documentation topics .
- Icons – several icons for your custom diagram representation in GUI. A custom diagram icon that you upload from your file system must be in .gif, .jpg, .jpeg, .svg, .png., or .wmf file format.

##### [IMAGE alt='' src='']

##### Step 2: Specify used projects

Custom Diagrams are oriented to a new specific domain, technology or platform, and are often based on a custom profile.

Select the required used projects or local profiles. How to use a custom server profile see in [CONFLUENCE_PAGE title='Customizing diagram palette' space='']

[IMAGE alt='' src='']

- Selected profiles must be local, the server profiles cannot be used.
- Do not remove the UML Standard Profile, which is selected by default, from the list. It must be used by any custom diagram type.

The custom diagram could use stereotyped elements. Profiles defining these stereotypes must be used by the custom diagram. The selected used projects or profiles load when a user creates a custom diagram in a project. You can choose a stereotype for the diagram by clicking the**Diagram Stereotype**button.

##### Step 3: Specify Toolbars

Every diagram differs by the elements used in them. In the **Specify toolbars** step, you can group standard or custom elements.

Only toolbars compatible with the specific diagram type can be added.

You can:

- Create your own custom diagram toolbar.
- Create your own toolbar, name it, and select an icon.
- Choose standard toolbars that will be visible in your diagram.
- Select existing toolbars inherited from the base diagram type.
- Arrange the order of toolbars by using "Up" and "Down" buttons.
- Select which toolbars will expand or collapse by default (use the Open check box).

[IMAGE alt='' src='']

##### Step 4: Specify Toolbar Buttons

Select standard or stereotyped elements for your custom diagram toolbars.

[IMAGE alt='' src='']

Click **Add** and select standard UML elements or click **Add** and then **New** **Button** to create your own buttons to create customized or stereotyped elements.

Only buttons compatible with the specific diagram type can be added to the toolbar.

**Customize the following properties when creating a new button:**

- Model element type
- Custom icon for a button
- Shortcut that activates the button
- Tooltip description
- Stereotype(s) to apply to the created element
- Symbol style – selected symbol properties will be used only when the element is created using this button
- Default values for some primitive model element properties (like isAbstract = true or similar)

###### [IMAGE alt='' src='']

- List as element – select this check box to add the button as a command in the Create Element command list.
- Opposite – this check box is only available for relationship buttons. Select it to add the opposite relationship button.

##### Step 5: Specify Symbol Properties

This step allows you to customize the style for any element appearing in your custom diagram (e.g. a class dropped in your diagram should be suppressed and red).

You can change the appearance of standard symbols, symbols of stereotyped elements, and the custom diagram itself. The customized element style will be used only in the appropriate custom diagram type.

##### Step 6: Specify Smart Manipulators

Only elements that are available in the toolbars specified for the diagram being customized can be added to the smart manipulator of the element shape or path.

Smart manipulators are special buttons that appear in the pop-up window when a shape or path is selected on a diagram.

[IMAGE alt='' src='']

###### Example of smart manipulator

You can configure the element or kind of relationship suggested when a custom shape or path is selected on a diagram.

There are three main sub-steps:

1. Create a new configuration (or modify an existing one). Select the element to customize. The smart manipulators configuration can be related to:
  - Element, displayed as [Element name]
  - Element + stereotype(s)
  - Symbol, displayed as {Symbol name}
  - Symbol + stereotype(s)
  - Stereotype(s), displayed as «Stereotype name»
2. Select suggested relationships for the selected configuration.
3. Select target elements for the selected relationship.

If several configuration settings could be applied to the same selected element on the diagram, only one configuration will be used according to this priority**:**

| # | Configuration | Comment |
| --- | --- | --- |
| 1 | Symbol + stereotype(s) | When stereotype(s) for symbol applied |
| 2 | Stereotype |  |
| 3 | Symbol |  |
| 4 | Element + stereotype(s) | When stereotype(s) for element applied |
| 5 | Element |  |

If several configurations are created for a few stereotypes (for example, Stereotype1 and Stereotype2) in the same diagram, when both stereotypes are applied to one symbol on that diagram pane, the first configuration (in this case, Stereotype1) is used, unless you specify a symbol+ stereotype(s) configuration.

###### Inheritance of configurations

All diagrams inherit their configurations from a base diagram (example: in this hierarchy: Any diagram > Static diagram > Class diagram > Generic DDL diagram).

If you add a new configuration to a class diagram (for example, Symbol A + stereotype B), the configuration will be used in the generic DDL diagram, as the class diagram is its base diagram. Any static diagrams will not have such configurations. 
 
To change the configuration from the base diagram type

- From the Configurations list, select the configuration by the element type and choose the Specify own configuration button. This overwrites the inherited configuration.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The <strong style="letter-spacing: 0.0px;">Customize Diagram Wizard</strong> contains the following steps for creating a new diagram type or modifying a chosen one.</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="9d1dce12-3247-48ea-9ab7-a48ffda2539f"><ac:parameter ac:name="maxLevel">3</ac:parameter></ac:structured-macro></p><p><br /></p><p>All Custom Diagrams are based on standard UML diagrams (like Class, Use Case, Sequence, and other).</p><p><br /></p><h3>Step 1: Specify diagram type and icon </h3><p><br class="atl-forced-newline" />To create your own diagram, first specify the following properties</p><hr /><ul><li>Diagram type name (for example, Robustness Diagram).</li><li>Base Diagram Type – standard UML diagram to be extended. All configurations, semantics, and other settings will be inherited from this diagram type.</li><li>Abbreviation – a short form of the diagram name. It will be used in Diagram Frames header or Diagram shapes in Content diagrams.</li><li>Category – creates your specific category in the <strong>Diagrams</strong> menu or in the <strong>Create Diagram</strong> command list. You can store all your customized diagrams in this category. If you leave this field empty, the customized diagrams will be added to the <strong>Custom Diagrams</strong> category.</li><li>Help ID – sets a specific Help ID to invoke help or documentation topics<ac:inline-comment-marker ac:ref="96071bf5-507f-41a8-9662-81d84b07a72a">.</ac:inline-comment-marker></li><li><p class="auto-cursor-target">Icons – several icons for your custom diagram representation in GUI.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="193b30ab-4b02-49de-b6aa-9a8795607fe0"><ac:rich-text-body><p>A custom diagram icon that you upload from your file system must be in .gif, .jpg, .jpeg, .svg, .png., or .wmf file format.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><h3><ac:image ac:align="center"><ri:attachment ri:filename="Customize_diagram_wizard_new.png" /></ac:image></h3><h3>Step 2: Specify used projects</h3><p>Custom Diagrams are oriented to a new specific domain, technology or platform, and are often based on a custom profile.</p><p>Select the required used projects or local profiles. How to use a custom server profile see in <ac:link><ri:page ri:content-title="Customizing diagram palette" /><ac:plain-text-link-body><![CDATA[customizing diagram palette.]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Customize_Diagram_wizard_new2.png" /></ac:image></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="65433487-86fc-4a27-b273-7d841bb4cb47"><ac:rich-text-body><ul><li>Selected profiles must be local, the server profiles cannot be used.</li><li>Do not remove the UML Standard Profile, which is selected by default, from the list. It must be used by any custom diagram type.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span>The custom diagram could use stereotyped elements. Profiles defining these stereotypes must be used by the custom diagram. The selected used projects or profiles load when a user creates a custom diagram in a project. You can choose a stereotype for the diagram by clicking the </span><strong>Diagram Stereotype</strong><span> button.</span></p><h3>Step 3: Specify Toolbars</h3><p>Every diagram differs by the elements used in them. In the <strong>Specify toolbars</strong> step, you can group standard or custom elements.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="659012d8-4b14-4f7b-82f3-6e046efd73d4"><ac:rich-text-body><p>Only toolbars compatible with the specific diagram type can be added.</p></ac:rich-text-body></ac:structured-macro><p><br />You can:</p><ul><li>Create your own custom diagram toolbar.</li><li>Create your own toolbar, name it, and select an icon.</li><li>Choose standard toolbars that will be visible in your diagram.</li><li>Select existing toolbars inherited from the base diagram type.</li><li>Arrange the order of toolbars by using &quot;Up&quot; and &quot;Down&quot; buttons.</li><li>Select which toolbars will expand or collapse by default (use the <strong>Open</strong> check box).</li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="Specify_toolbars_window.png" /></ac:image></p><h3>Step 4: Specify Toolbar Buttons</h3><p>Select standard or stereotyped elements for your custom diagram toolbars.</p><p style="margin-left: 30.0px;"><ac:image ac:align="center"><ri:attachment ri:filename="customize diagram wizard.png" /></ac:image></p><p>Click <strong>Add</strong> and select standard UML elements or click <strong>Add</strong> and then <strong>New</strong> <strong>Button</strong> to create your own buttons to create customized or stereotyped elements.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ed528404-ce40-4794-8da6-d0359ac24763"><ac:rich-text-body><p>Only buttons compatible with the specific diagram type can be added to the toolbar.</p></ac:rich-text-body></ac:structured-macro><p class="atl-forced-newline"><strong>Customize the following properties when creating a new button:</strong></p><ul><li class="atl-forced-newline">Model element type</li><li class="atl-forced-newline">Custom icon for a button</li><li class="atl-forced-newline">Shortcut that activates the button</li><li class="atl-forced-newline">Tooltip description</li><li class="atl-forced-newline">Stereotype(s) to apply to the created element</li><li class="atl-forced-newline">Symbol style – selected symbol properties will be used only when the element is created using this button</li><li class="atl-forced-newline">Default values for some primitive model element properties (like isAbstract = true or similar)</li></ul><h6 class="atl-forced-newline"><br /><ac:image ac:align="center"><ri:attachment ri:filename="Edit_button1.png" /></ac:image></h6><ul><li>List as element – select this check box to add the button as a command in the <strong>Create Element</strong> command list.</li><li>Opposite – this check box is only available for relationship buttons. Select it to add the opposite relationship button.</li></ul><h3>Step 5: Specify Symbol Properties</h3><p>This step allows you to customize the style for any element appearing in your custom diagram (e.g. a class dropped in your diagram should be suppressed and red).</p><p>You can change the appearance of standard symbols, symbols of stereotyped elements, and the custom diagram itself. The customized element style will be used only in the appropriate custom diagram type.</p><h3 class="auto-cursor-target">Step 6: Specify Smart Manipulators</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e7a45297-8ff3-42c1-9d7c-bb2346d60ca6"><ac:rich-text-body><p>Only elements that are available in the toolbars specified for the diagram being customized can be added to the smart manipulator of the element shape or path.</p></ac:rich-text-body></ac:structured-macro><p><br />Smart manipulators are special buttons that appear in the pop-up window when a shape or path is selected on a diagram.</p><p><ac:image ac:align="center" ac:title="Smart manipulators" ac:alt="Smart manipulators"><ri:attachment ri:filename="smart_manipulators.png" /></ac:image></p><h6 style="text-align: center;">Example of smart manipulator </h6><p><br /></p><p>You can configure the element or kind of relationship suggested when a custom shape or path is selected on a diagram.</p><p>There are three main sub-steps:</p><ol><li>Create a new configuration (or modify an existing one). Select the element to customize. The smart manipulators configuration can be related to:<br /><ul><li>Element, displayed as [Element name]</li><li>Element + stereotype(s)</li><li>Symbol, displayed as {Symbol name}</li><li>Symbol + stereotype(s)</li><li>Stereotype(s), displayed as «Stereotype name»</li></ul></li><li><span style="color: rgb(129,137,156);"> </span>Select suggested relationships for the selected configuration.</li><li>Select target elements for the selected relationship.</li></ol><p>If several configuration settings could be applied to the same selected element on the diagram, only one configuration will be used according to this priority<strong>:</strong></p><table><colgroup><col /><col /><col /></colgroup><tbody><tr><td><p><strong>#</strong></p></td><td><p><strong>Configuration</strong></p></td><td><p><strong>Comment</strong></p></td></tr><tr><td><p>1</p></td><td><p>Symbol + stereotype(s)</p></td><td><p>When stereotype(s) for symbol applied</p></td></tr><tr><td><p>2</p></td><td><p>Stereotype</p></td><td><p><br /></p></td></tr><tr><td><p>3</p></td><td><p>Symbol</p></td><td><p><br /></p></td></tr><tr><td><p>4</p></td><td><p>Element + stereotype(s)</p></td><td><p>When stereotype(s) for element applied</p></td></tr><tr><td><p>5</p></td><td><p>Element</p></td><td><p><br /></p></td></tr></tbody></table><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a0d033a8-b4d6-4d80-835b-01725d79e156"><ac:rich-text-body><p>If several configurations are created for a few stereotypes (for example, Stereotype1 and Stereotype2) in the same diagram, when both stereotypes are applied to one symbol on that diagram pane, the first configuration (in this case, Stereotype1) is used, unless you specify a symbol+ stereotype(s) configuration.</p></ac:rich-text-body></ac:structured-macro><h4>Inheritance of configurations</h4><p>All diagrams inherit their configurations from a base diagram (example: in this hierarchy: Any diagram &gt; Static diagram &gt; Class diagram &gt; Generic DDL diagram).</p><p>If you add a new configuration to a class diagram (for example, Symbol A + stereotype B), the configuration will be used in the generic DDL diagram, as the class diagram is its base diagram. Any  static diagrams will not have such configurations.<br class="atl-forced-newline" /><br class="atl-forced-newline" />To change the configuration from the base diagram type</p><hr /><ul><li>From the <strong>Configurations</strong> list, select the configuration by the element type and choose the <strong>Specify own configuration</strong> button. This overwrites the inherited configuration.</li></ul>
````

<!--NOMAGIC_PAGE id=243973548 space=UPDG version=1 -->
## PAGE 00161: Creating new generic table type

- page_id: `243973548`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973548/Creating+new+generic+table+type
- version_number: 1
- version_date: `2025-07-31T19:04:47.992+02:00`
- ancestors: UML Profiling and DSL Guide > Customizing diagrams
- labels: []

### NORMALIZED CONTENT

The**Customize Generic Table Wizard**contains the following steps for creating a new diagram type or modifying a chosen one:

##### Step 1: Specify diagram type and icon

To create your own diagram, first specify the following properties:

- Diagram type name (for example, Generic Table).
- Abbreviation – a short form of the diagram name. It will be used in Diagram Frames header or Diagram shapes in Content diagrams.
- Category – creates your specific category in the Diagrams menu or in the Create Diagram command list. You can store all your customized diagrams in this category. If you keep this field empty, the customized diagrams will be added to the Custom Diagrams category.
- Help ID – sets a specific Help ID that invokes help or documentation topics.
- Icons – several icons for your custom diagram representation in GUI.

[IMAGE alt='' src='']

##### Step 2: Specify used projects

Custom Diagrams are oriented to a new specific domain, technology or platform, and are often based on a custom profile.

Select the required used projects or profile.

[IMAGE alt='' src='']

Do not remove the UML Standard Profile, which is selected by default, from the list. It must be used by any custom diagram type.

Click the **Diagram Stereotype** button to apply the specific stereotype to your Generic Table.

##### Step 3: Specify Generic Table properties

This step allows you to specify the appearance of a new Generic Table.

| Property Name | Description |
| --- | --- |
| Show Column Icons | Set to true to show icons in column headers. |
| Custom Columns | Click ... to select and specify operations for calculating/gathering values of the custom column. |
| Display Mode | Click ... to select one of the visualization options: Complete tree (the table represents all elements with their owners), Compact tree (the table combines grouping elements), or List (selected model elements are organized into a plain list). |
| Show Scope As Root | Set to true to show scope as a root node in the tree display mode. |
| Show Element Number | Set to true to display the element number in the name column. |
| Row Element Type | Click ... to select the type of elements to be shown as row elements. |
| Query | Click ... to select and specify operations to query the model. |
| Types Include Subtypes | Set to true to include subtypes of the selected elements. |
| Columns | Click ... to select columns to appear in the Generic Table. |
| Row Filters | Set to true to display filtered rows in the Generic Table. |
| Show Detailed Column Name | Set to true to show classifiers next to properties in the column header. |
| Column Width | Click to adjust the width of columns. |
| Default Row Elements Owner | Click to select the default owner of row elements. |
| Hide Columns | Click ... to select columns that will not be displayed in the Generic Table. |
| Show Full Path | Set to true to show the full path of elements. |
| Show Filter | Set to true to show the filter applied in the Generic Table. |
| Show Element Type | Set to true to show the element type specification box in the criteria area of the Generic Table. |
| Show Scope | Set to true to display the scope in the criteria area of the Generic Table. |
| Legends | Click ... to select a legend for the Generic Table. |
| Description Area | Specify the description of the Generic Table. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">The </span><strong>Customize Generic Table Wizard</strong><span style="color: rgb(62,63,64);"> contains the following steps for creating a new diagram type or modifying a chosen one:</span></p><p><span style="color: rgb(62,63,64);"><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="e3489303-c4f4-445b-8704-aae29fa27ef3" /></span></p><h3>Step 1: Specify diagram type and icon</h3><p>To create your own diagram, first specify the following properties:</p><ul><li>Diagram type name (for example, Generic Table).</li><li>Abbreviation – a short form of the diagram name. It will be used in Diagram Frames header or Diagram shapes in Content diagrams.</li><li>Category – creates your specific category in the <strong>Diagrams</strong> menu or in the <strong>Create Diagram</strong> command list. You can store all your customized diagrams in this category. If you <ac:inline-comment-marker ac:ref="e8c517e4-f20c-47e0-a255-bd842bb293f4">keep</ac:inline-comment-marker> this field empty, the customized diagrams will be added to the <strong>Custom Diagrams</strong> category.</li><li>Help ID – sets a specific Help ID that invokes help or documentation topics.</li><li>Icons – several icons for your custom diagram representation in GUI.<br /><br /></li></ul><p><span style="color: rgb(62,63,64);"><ac:image ac:align="center"><ri:attachment ri:filename="generic_table_wizard.png" /></ac:image></span></p><p><br /></p><h3><span>Step 2: Specify used projects</span></h3><p>Custom Diagrams are oriented to a new specific domain, technology or platform, and are often based on a custom profile.</p><p>Select the required used projects or profile.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="specify_used_projects_generic_table_wizard.png" /></ac:image></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="5f4cf476-aae7-4790-886f-984c117acb62"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">Do not remove the UML Standard Profile, which is selected by default, from the list. It must be used by any custom diagram type.</span></p></ac:rich-text-body></ac:structured-macro><p>Click the <strong>Diagram Stereotype</strong> button to apply the specific stereotype to your Generic Table. </p><h3>Step 3: Specify Generic Table properties</h3><p><span style="color: rgb(62,63,64);">This step allows you to specify the appearance of <span style="color: rgb(62,63,64);">a new Generic Table</span>.</span></p><table class="relative-table" style="width: 100.0%;"><colgroup><col style="width: 15.4775%;" /><col style="width: 84.5225%;" /></colgroup><tbody><tr><th>Property Name</th><th>Description</th></tr><tr><td><strong>Show Column Icons</strong></td><td>Set to true to show icons in column headers.</td></tr><tr><td><strong>Custom Columns</strong></td><td>Click ... to select and specify <ac:inline-comment-marker ac:ref="0a9e1061-6b69-42f5-adec-06dabbd1ff06">operations for</ac:inline-comment-marker> calculating/gathering values of the custom column.</td></tr><tr><td><strong>Display Mode</strong></td><td>Click ... to select one of the visualization options: <em>Complete tree </em>(the table represents all elements with their owners), <em>Compact tree </em>(the table combines grouping elements), or <em>List </em>(selected model elements are organized into a plain list).</td></tr><tr><td colspan="1"><strong>Show Scope As Root</strong></td><td colspan="1">Set to <em>true</em> to show scope as a root node in the tree display mode.</td></tr><tr><td colspan="1"><strong>Show Element Number</strong></td><td colspan="1">Set to <em>true</em> to display the element number in the name column.</td></tr><tr><td colspan="1"><strong>Row Element Type</strong></td><td colspan="1">Click ... to select the type of elements to be shown as row elements.</td></tr><tr><td colspan="1"><strong>Query</strong></td><td colspan="1">Click ... to select and specify operations to query the model.</td></tr><tr><td><strong>Types Include Subtypes</strong></td><td>Set to <em>true</em> to include subtypes of the selected elements.</td></tr><tr><td colspan="1"><strong>Columns</strong></td><td colspan="1">Click ... to select columns to appear in the Generic Table.</td></tr><tr><td colspan="1"><strong>Row Filters</strong></td><td colspan="1">Set to <em>true</em> to display filtered rows in the Generic Table.</td></tr><tr><td colspan="1"><strong>Show Detailed Column Name</strong></td><td colspan="1"><ac:inline-comment-marker ac:ref="c751aef0-d7e3-48d7-ba82-8f626cacbf7e">Set to </ac:inline-comment-marker><em><ac:inline-comment-marker ac:ref="c751aef0-d7e3-48d7-ba82-8f626cacbf7e">true</ac:inline-comment-marker></em><ac:inline-comment-marker ac:ref="c751aef0-d7e3-48d7-ba82-8f626cacbf7e"> to show classifiers next to properties in the column header.</ac:inline-comment-marker></td></tr><tr><td colspan="1"><strong>Column Width</strong></td><td colspan="1">Click to adjust the width of columns.</td></tr><tr><td colspan="1"><strong>Default Row Elements Owner</strong></td><td colspan="1"><span>Click to select the default owner of row elements. </span></td></tr><tr><td colspan="1"><strong>Hide Columns</strong></td><td colspan="1">Click ... to select columns that will not be displayed in the Generic Table.</td></tr><tr><td colspan="1"><strong>Show Full Path</strong></td><td colspan="1">Set to <em>true</em> to show the full path of elements.</td></tr><tr><td colspan="1"><strong>Show Filter</strong></td><td colspan="1">Set to <em>true </em>to show the filter applied in the Generic Table.</td></tr><tr><td colspan="1"><strong>Show Element Type</strong></td><td colspan="1">Set to <em>true</em> to show the element type specification box in the criteria area of the Generic Table.</td></tr><tr><td colspan="1"><strong>Show Scope</strong></td><td colspan="1">Set to <em>true</em> to display the scope in the criteria area of the Generic Table.</td></tr><tr><td colspan="1"><strong>Legends</strong></td><td colspan="1">Click ... to select a legend for the Generic Table.</td></tr><tr><td colspan="1"><strong>Description Area</strong></td><td colspan="1">Specify the description of the Generic Table.</td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243973545 space=UPDG version=1 -->
## PAGE 00162: Creating new relation map type

- page_id: `243973545`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973545/Creating+new+relation+map+type
- version_number: 1
- version_date: `2025-07-31T19:04:47.899+02:00`
- ancestors: UML Profiling and DSL Guide > Customizing diagrams
- labels: []

### NORMALIZED CONTENT

The**Customize Relation Map Diagram Wizard**contains the following steps for creating a new diagram type or modifying a chosen one:

##### Step 1: Specify diagram type and icon

To create your own diagram, first specify the following properties:

- Diagram type name (for example, Impact Analysis).
- Abbreviation – a short form of the diagram name. It will be used in Diagram Frames header or Diagram shapes in Content diagrams.
- Category – creates your specific category in the Diagrams menu or in the Create Diagram command list. You can store all your customized diagrams in this category. If you keep this field empty, the customized diagrams will be added to the Custom Diagrams category.
- Help ID – sets a specific Help ID that invokes help or documentation topics.
- Icons – several icons for your custom diagram representation in GUI.

##### [IMAGE alt='' src='']

##### Step 2: Specify used projects

Custom Diagrams are oriented to a new specific domain, technology or platform, and are often based on a custom profile.

Select the required used projects or profiles.

[IMAGE alt='' src='']

Do not remove the UML Standard Profile, which is selected by default, from the list. It must be used by any custom diagram type.

You can apply the stereotype for your Relation Map diagram by clicking the**Diagram Stereotype** button.

##### Step 3: Specify Relation Map Diagram properties

This step allows you to specify the appearance of the new relation map diagram.

| Property Name | Description |
| --- | --- |
| Cut Element Names | Set to true to cut element names that are too long and make the Relation Map difficult to read. |
| Include Subtypes | Set to true to display subtypes of the selected elements. For example, if a class is selected, then all its subtypes (such as component or custom subtypes like SysML block) are displayed. |
| Show Element Numbers | Set to true to show the element number before its name. |
| Show Legend | Set to true to display the relationship legend. |
| Show Parameters | Set to true to show the parameters' signatures of operation and behavior on symbols. |
| Show Single Node Per Element | Set to true to show a single node per element when the graph has more than one representation of that element in the Relation Map. |
| Show Applied Stereotypes | Set to true to display stereotypes applied to the elements. |
| Relation Criterion | Click ... to select and specify criteria in order to represent relations between elements. |
| Element Types | Click ... to select specific element types to be displayed. |
| Layout | Select Tree or Radial from the drop-down menu to customize the layout of your Relation Map. |
| Depth | Type the number to specify the level of the relation map branches that will be expanded automatically. |
| Filter Area Expanded | Set to true to show the filter area expanded. |
| Make Selected As Context | Set to true to make the selected element the core of the Relation Map. |
| Show Full Types | Set to true to show full element types in the Relation Map. |
| Show Relation Styles | Set to true to show relation line styles. |
| Description Area | Specify the description of the Relation Map. |
| Possible Context Types | Click ... to specify the possible context types. |
| Show Scope | Set to true to display the Relation Map scope, that is, to see the fragment of the model (or whole model) from which the Relation Map is built. |
| Show Context | Set to true to show the Context field in the diagram toolbar. |
| Show Element Type | Set to true to show the element type specification box in the diagram toolbar. |
| Show Relation Criterion | Set to true to display relation criteria in the diagram toolbar. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">The </span><strong>Customize Relation Map Diagram Wizard</strong><span style="color: rgb(62,63,64);"> contains the following steps for creating a new diagram type or modifying a chosen one:</span></p><p><span style="color: rgb(62,63,64);"><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="abb958fe-01fd-42f6-830c-1a3b1beacd34" /><br /></span></p><h3>Step 1: Specify diagram type and icon</h3><p><span style="color: rgb(62,63,64);">To create your own diagram, first specify the following properties:</span></p><p><br /></p><ul><li>Diagram type name (for example, Impact Analysis).</li><li>Abbreviation – a short form of the diagram name. It will be used in Diagram Frames header or Diagram shapes in Content diagrams.</li><li>Category – creates your specific category in the <strong>Diagrams</strong> menu or in the <strong>Create Diagram</strong> command list. You can store all your customized diagrams in this category. If you keep this field empty, the customized diagrams will be added to the <strong>Custom Diagrams</strong> category.</li><li>Help ID – sets a specific Help ID that invokes help or documentation topics.</li><li>Icons – several icons for your custom diagram representation in GUI.</li></ul><h3><br /><ac:image ac:align="center"><ri:attachment ri:filename="Customize_Relation_Map_diagram.png" /></ac:image></h3><p><br /></p><h3><span style="font-size: 16.0px;letter-spacing: -0.006em;">Step 2: Specify used projects</span></h3><p>Custom Diagrams are oriented to a new specific domain, technology or platform, and are often based on a custom profile.</p><p>Select the required used projects or profiles.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Specify_used_projects.png" /></ac:image></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="5f4cf476-aae7-4790-886f-984c117acb62"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">Do not remove the UML Standard Profile, which is selected by default, from the list. It must be used by any custom diagram type.</span></p></ac:rich-text-body></ac:structured-macro><p>You can apply the stereotype for your Relation Map diagram by clicking the<strong> Diagram Stereotype</strong> button. </p><h3>Step 3: Specify Relation Map Diagram properties</h3><p><span style="color: rgb(62,63,64);">This step allows you to specify the appearance of the new relation map diagram.</span></p><table class="relative-table" style="width: 100.0%;"><colgroup><col style="width: 14.27%;" /><col style="width: 85.73%;" /></colgroup><tbody><tr><th>Property Name</th><th>Description</th></tr><tr><td><strong>Cut Element Names</strong></td><td>Set to <em>true</em> to cut <ac:inline-comment-marker ac:ref="0e7c8db0-fedd-434c-a99d-5c640e0a472f">element names</ac:inline-comment-marker> that are too long and make the Relation Map difficult to read.</td></tr><tr><td><strong>Include Subtypes</strong></td><td><ac:inline-comment-marker ac:ref="97576ac1-4899-4896-b4b3-46bf7887e17a">Set to </ac:inline-comment-marker><em><ac:inline-comment-marker ac:ref="97576ac1-4899-4896-b4b3-46bf7887e17a">true </ac:inline-comment-marker></em><ac:inline-comment-marker ac:ref="97576ac1-4899-4896-b4b3-46bf7887e17a">to display subtypes of the selected elements. <span style="color: rgb(51,51,51);">For example, if a class is selected, then all its subtypes (such as component or custom subtypes like SysML block) are displayed.</span></ac:inline-comment-marker></td></tr><tr><td><strong>Show Element Numbers</strong></td><td>Set to <em>true</em> to show the element number before its name.</td></tr><tr><td colspan="1"><strong>Show Legend</strong></td><td colspan="1">Set to <em>true</em> to display the relationship legend.</td></tr><tr><td colspan="1"><strong>Show Parameters</strong></td><td colspan="1">Set to <em>true</em> to show the parameters' signatures of operation and behavior on symbols.</td></tr><tr><td colspan="1"><strong>Show Single Node Per Element</strong></td><td colspan="1">Set to <em>true </em>to show a single node per element when the graph has more than one representation of that element in the Relation Map.</td></tr><tr><td colspan="1"><strong>Show Applied Stereotypes</strong></td><td colspan="1">Set to <em>true </em>to display stereotypes applied to the elements.</td></tr><tr><td colspan="1"><strong>Relation Criterion</strong></td><td colspan="1">Click ... to select and specify <ac:inline-comment-marker ac:ref="860cb08c-f719-45a1-97cb-95ce489ad501">criteria in order</ac:inline-comment-marker> to represent relations between elements.</td></tr><tr><td colspan="1"><strong>Element Types</strong></td><td colspan="1">Click ... to select specific element types to be displayed.</td></tr><tr><td colspan="1"><strong>Layout</strong></td><td colspan="1">Select <em>Tree</em> or <em>Radial</em> from the drop-down menu to customize the layout of your Relation Map.</td></tr><tr><td colspan="1"><strong>Depth</strong></td><td colspan="1"><p>Type the number to specify the level of the relation map branches that will be expanded automatically.</p></td></tr><tr><td colspan="1"><strong>Filter Area Expanded</strong></td><td colspan="1">Set to <em>true</em> to show the filter area expanded.</td></tr><tr><td colspan="1"><strong>Make Selected As Context</strong></td><td colspan="1"><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="a5c8086e-ecfe-4ad6-9acd-7fbc84085c38">Set to </ac:inline-comment-marker><em><ac:inline-comment-marker ac:ref="a5c8086e-ecfe-4ad6-9acd-7fbc84085c38">true </ac:inline-comment-marker></em><ac:inline-comment-marker ac:ref="a5c8086e-ecfe-4ad6-9acd-7fbc84085c38">to make the selected element the core of the Relation Map.</ac:inline-comment-marker></span></td></tr><tr><td colspan="1"><strong>Show Full Types</strong></td><td colspan="1">Set to <em>true </em>to show full element types in the Relation Map.</td></tr><tr><td colspan="1"><strong>Show Relation Styles</strong></td><td colspan="1">Set to <em>true</em> to show relation line styles.</td></tr><tr><td colspan="1"><strong>Description Area</strong></td><td colspan="1">Specify the description of the Relation Map.</td></tr><tr><td colspan="1"><strong>Possible Context Types</strong></td><td colspan="1">Click ... to specify the possible context types.</td></tr><tr><td colspan="1"><strong>Show Scope</strong></td><td colspan="1">Set to <em>true</em> to display the Relation Map scope, that is, to see the fragment of the model (or whole model) from which the Relation Map is built.</td></tr><tr><td colspan="1"><strong>Show Context</strong></td><td colspan="1"><ac:inline-comment-marker ac:ref="eb91e469-8eeb-478f-aac3-3c1edfaf933b">Set to </ac:inline-comment-marker><em><ac:inline-comment-marker ac:ref="eb91e469-8eeb-478f-aac3-3c1edfaf933b">true</ac:inline-comment-marker></em><ac:inline-comment-marker ac:ref="eb91e469-8eeb-478f-aac3-3c1edfaf933b"> to show the Context field in the diagram toolbar.</ac:inline-comment-marker></td></tr><tr><td colspan="1"><strong>Show Element Type</strong></td><td colspan="1"><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="84979ef1-7d00-46fc-9712-9d015c30aef7">Set to </ac:inline-comment-marker></span><em><ac:inline-comment-marker ac:ref="84979ef1-7d00-46fc-9712-9d015c30aef7">true</ac:inline-comment-marker></em><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="84979ef1-7d00-46fc-9712-9d015c30aef7"> to show the element type specification box in the diagram toolbar.</ac:inline-comment-marker></span></td></tr><tr><td colspan="1"><strong>Show Relation Criterion</strong></td><td colspan="1"><ac:inline-comment-marker ac:ref="1c4029be-d7d2-425f-b1fe-1d647291b1c0">Set to </ac:inline-comment-marker><em><ac:inline-comment-marker ac:ref="1c4029be-d7d2-425f-b1fe-1d647291b1c0">true</ac:inline-comment-marker></em><ac:inline-comment-marker ac:ref="1c4029be-d7d2-425f-b1fe-1d647291b1c0"> to display relation criteria in the diagram toolbar. </ac:inline-comment-marker></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243973665 space=UPDG version=1 -->
## PAGE 00163: Creating Numbering Customizations

- page_id: `243973665`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973665/Creating+Numbering+Customizations
- version_number: 1
- version_date: `2025-07-31T19:04:51.229+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data
- labels: []

### NORMALIZED CONTENT

**On this page:**

3

The [CONFLUENCE_PAGE title='Generic numbering mechanism' space='MDTWRT'] consists of the Numbering Customization and Numbering Scheme, shown in the figure below.

##### [IMAGE alt='' src='']

###### The structure of the Generic Numbering Mechanism.

Create numbering schemes (formats) and apply them to DSL elements in the modeling tool or plugin ([CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLPTWRT'], [CONFLUENCE_PAGE title='Cameo Business Modeler Plugin Documentation' space='CBMPTWRT'], [CONFLUENCE_PAGE title='UAF 1.2 Plugin Documentation' space='UAF12PTWRT'], or [CONFLUENCE_PAGE title='UPDM 2 Plugin Documentation' space='UPDM2PTWRT']).

You can create one or more numbering schemes for the same DSL element. You can also apply the same numbering scheme to several DSL elements. In this case, instances of different DSL elements will be numbered in sequence. For example, if you use the same numbering customization for both actors and use cases, all actors and use cases in a use case diagram will be numbered in sequence. Another example of numbering different DSL elements in sequence is shown in the figure below. The start events, end events, tasks, and gateways in the BPMN Process diagram are numbered using the same numbering scheme.

[IMAGE alt='' src='']

###### Numbering instances of different BPMN elements in a sequence

Find the instructions to customize the generic numbering mechanism to create your own numbering scheme in [CONFLUENCE_PAGE title='Creating your first numbering customization' space='']. Create your own numbering customization defining specific numbering properties using [CONFLUENCE_PAGE title='Defining expressions' space=''].

##### Basic concepts

| Concept | Description |
| --- | --- |
| Numbering scheme | Defines a numbering style as well as number parts used to compose a DSL element number. A numbering schema can have one or more number parts. A numbering scheme is represented as a class with the «NumberingScheme» stereotype applied. |
| Number part | Represents a rule for calculating an individual part of the whole element number, as the element number is composed of one or more individual number parts. It can be a number, character, separator, or other. Number part is represented as a numbering scheme property with the «NumberPart» stereotype applied. |
| Numbering property | Indicates a DSL element property to store the element number and defines a numbering scheme used for the DSL element numbering. The numbering property is represented as a customization element property with the «AutoNumber» stereotype applied. |

Basic steps for creating numbering customization

To create a numbering customization for an element:

1. [CONFLUENCE_PAGE title='Creating a diagram' space='DEVGTWRT'] .
2. Create a [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT'] to customize a desired element.
3. Add a new attribute to the stereotype. This attribute will store the element number.
4. [CONFLUENCE_PAGE title='Creating your first numbering customization' space=''].
5. [CONFLUENCE_PAGE title='Customization Elements' space=''] for the previously created stereotype.
6. Add a numbering attribute to the customization element. Reopen the project to apply changes.

##### Specifying custom numbering properties

To define your own specific numbering customization, you need to [CONFLUENCE_PAGE title='Defining expressions' space='']. For general numbering it is a binary script. The following script example illustrates the multi-level numbering:

| binary;Binary;com.nomagic.magicdraw.autoid.LinkedDUCBinary; |
| --- |

Where *com.nomagic.magicdraw.autoid.LinkedDUCBinary* is your binary class that implements *INumberingAction.*

For more information, see [CONFLUENCE_PAGE title='Custom elements numbering' space='DEVGTWRT'].

**Related pages**

- [CONFLUENCE_PAGE title='Creating your First Customization' space='']
- [CONFLUENCE_PAGE title='Extending Metamodel with Derived Properties' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page:</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="eec0ed17-c702-4725-b1dd-30c27e5fc853"><ac:parameter ac:name="maxLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>The <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Generic numbering mechanism" /><ac:plain-text-link-body><![CDATA[Generic Numbering Mechanism]]></ac:plain-text-link-body></ac:link> consists of the Numbering Customization and Numbering Scheme, shown in the figure below.</p><h3><ac:image ac:align="center" ac:title="Generic Numbering Mechanism structure" ac:alt="Generic Numbering Mechanism structure"><ri:attachment ri:filename="GenericNumberingMechanism.png" /></ac:image></h3><h6 style="text-align: center;">The structure of the Generic Numbering Mechanism.</h6><p>Create numbering schemes (formats) and apply them to DSL elements in the modeling tool or plugin (<ac:link><ri:page ri:space-key="SYSMLPTWRT" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML]]></ac:plain-text-link-body></ac:link>, <ac:link><ri:page ri:space-key="CBMPTWRT" ri:content-title="Cameo Business Modeler Plugin Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Business Modeler]]></ac:plain-text-link-body></ac:link>, <ac:link><ri:page ri:space-key="UAF12PTWRT" ri:content-title="UAF 1.2 Plugin Documentation" /><ac:plain-text-link-body><![CDATA[UAF 1.2]]></ac:plain-text-link-body></ac:link>, or <ac:link><ri:page ri:space-key="UPDM2PTWRT" ri:content-title="UPDM 2 Plugin Documentation" /><ac:plain-text-link-body><![CDATA[UPDM 2 plugin]]></ac:plain-text-link-body></ac:link>).</p><p>You can create one or more numbering schemes for the same DSL element. You can also apply the same numbering scheme to several DSL elements. In this case, instances of different DSL elements will be numbered in sequence. For example, if you use the same numbering customization for both actors and use cases, all actors and use cases in a use case diagram will be numbered in sequence. Another example of numbering different DSL elements in sequence is shown in the figure below. The start events, end events, tasks, and gateways in the BPMN Process diagram are numbered using the same numbering scheme.</p><p><ac:image ac:align="center" ac:title="Numbering instances of different BPMN elements in sequence" ac:alt="Numbering instances of different BPMN elements in sequence"><ri:attachment ri:filename="Numbering_processes.PNG" /></ac:image></p><h6 style="text-align: center;">Numbering instances of different BPMN elements in a sequence</h6><p>Find the instructions to customize the generic numbering mechanism to create your own numbering scheme in <ac:link><ri:page ri:content-title="Creating your first numbering customization" /></ac:link>. Create your own numbering customization defining specific numbering properties using <ac:link><ri:page ri:content-title="Defining expressions" /><ac:plain-text-link-body><![CDATA[expressions]]></ac:plain-text-link-body></ac:link>.</p><h3><span style="color: rgb(0,0,0);">Basic concepts</span></h3><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Concept</th><th>Description</th></tr><tr><td><p><strong>Numbering scheme</strong></p></td><td><p>Defines a numbering style as well as number parts used to compose a DSL element number. A numbering schema can have one or more number parts. A numbering scheme is represented as a class with the «NumberingScheme» stereotype applied.</p></td></tr><tr><td><p><strong>Number part</strong></p></td><td><p>Represents a rule for calculating an individual part of the whole element number, as the element number is composed of one or more individual number parts. It can be a number, character, separator, or other. Number part is represented as a numbering scheme property with the «NumberPart» stereotype applied.</p></td></tr><tr><td><p><strong>Numbering property</strong></p></td><td><p>Indicates a DSL element property to store the element number  and defines a numbering scheme used for the DSL element numbering. The numbering property is represented as a customization element property with the «AutoNumber» stereotype applied.</p></td></tr></tbody></table><p class="auto-cursor-target"> <br /><span>Basic steps for creating numbering customization</span></p><p>To create a numbering customization for an element:</p><ol><li><ac:link><ri:page ri:space-key="DEVGTWRT" ri:content-title="Creating a diagram" /><ac:plain-text-link-body><![CDATA[Create a profile diagram]]></ac:plain-text-link-body></ac:link>.</li><li>Create a <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotype]]></ac:plain-text-link-body></ac:link> to customize a desired element.</li><li><p class="auto-cursor-target">Add a new attribute to the stereotype.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="1f762f82-2c52-4a11-8951-6f386f19ad55"><ac:rich-text-body><p>This attribute will store the element number.</p></ac:rich-text-body></ac:structured-macro></li><li><p><ac:link ac:anchor="3. Creating a numbering scheme to define a numbering style and number parts"><ri:page ri:content-title="Creating your first numbering customization" /><ac:plain-text-link-body><![CDATA[Create a numbering scheme to define a numbering style and number parts]]></ac:plain-text-link-body></ac:link>.</p></li><li><p><ac:link><ri:page ri:content-title="Customization Elements" /><ac:plain-text-link-body><![CDATA[Create a customization element]]></ac:plain-text-link-body></ac:link> for the previously created stereotype.</p></li><li><p>Add a numbering attribute to the customization element. Reopen the project to apply changes.</p></li></ol><h3>Specifying custom numbering properties</h3><p>To define your own specific numbering customization, you need to <ac:link><ri:page ri:content-title="Defining expressions" /><ac:plain-text-link-body><![CDATA[define an expression]]></ac:plain-text-link-body></ac:link>. For general numbering it is a binary script. The following script example illustrates the multi-level numbering:</p><table class="wrapped"><tbody><tr><td><p><code class="php plain">binary;Binary;com.nomagic.magicdraw.autoid.LinkedDUCBinary;</code></p></td></tr></tbody></table><p><br /><span style="color: rgb(0,0,0);">Where <em>com.nomagic.magicdraw.autoid.LinkedDUCBinary</em> is your binary class that implements <em>INumberingAction.</em></span></p><p><span style="color: rgb(0,0,0);">For more information, see <ac:link><ri:page ri:space-key="DEVGTWRT" ri:content-title="Custom elements numbering" /></ac:link>.</span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Creating your First Customization" /></ac:link></li><li><ac:link><ri:page ri:content-title="Extending Metamodel with Derived Properties" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973493 space=UPDG version=1 -->
## PAGE 00164: Creating Profiles

- page_id: `243973493`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973493/Creating+Profiles
- version_number: 1
- version_date: `2025-07-31T19:04:46.960+02:00`
- ancestors: UML Profiling and DSL Guide > Working with Profiles
- labels: []

### NORMALIZED CONTENT

Profiles can be created in any project. However, often many projects use the same profiles. In order to reuse the same profile, it must be created as an independent file with shared data called a module.

To create a Profile as a module

1. Create a new project.
2. In the [CONFLUENCE_PAGE title='Model Browser' space='MDTWRT'], right-click the root **Model** and create a new Profile.
3. Create a new [CONFLUENCE_PAGE title='Profile diagram' space='MDTWRT'] inside the Profile.
4. Create [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT']in the diagram.
5. Use [CONFLUENCE_PAGE title='Association' space='MDTWRT'] and [CONFLUENCE_PAGE title='Generalization' space='MDTWRT'] between them if needed.
6. In the Model Browser, from the created Profile shortcut menu, choose Project Usages > Share Packages .
7. Select the Profile as shared, enter its description, and click OK .
8. Save the project.

Now you may use this profile in other projects.

To use the created profile in other projects

- From the **File** menu, choose **[CONFLUENCE_PAGE title='Managing used projects' space='MD190']** and select the project file. Only shared packages of the module will be loaded into the project.

#### NOTE: Tip

Tip

If you don’t want to see particular information, move elements from shared packages into the root model or other non-shared packages in your module.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Project partitioning' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span>Profiles can be created in any project. However, often many projects use the same profiles. In order to reuse the same profile, it must be created as an independent file with shared data called </span> <span>a module.</span></p><p><span><br /></span></p><p><span>To create a Profile as a module</span></p><hr /><ol><li>Create a new project.</li><li><span>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Model Browser" /></ac:link>, right-click the root <strong>Model </strong> and create a new Profile.</span></li><li><span>Create a new <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Profile diagram" /></ac:link> inside the Profile.</span></li><li><span>Create <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotypes ]]></ac:plain-text-link-body></ac:link>in the diagram.</span></li><li><span>Use <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Association" /><ac:plain-text-link-body><![CDATA[Associations]]></ac:plain-text-link-body></ac:link> and <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Generalization" /><ac:plain-text-link-body><![CDATA[Generalizations]]></ac:plain-text-link-body></ac:link> between them if needed.</span></li><li><span>In the Model Browser, from the created Profile shortcut menu, choose </span><strong>Project Usages &gt; Share Packages</strong><strong>.</strong></li><li>Select the Profile as shared, enter its description, and click <strong>OK</strong>.</li><li>Save the project.</li></ol><p>Now you may use this profile in other projects.</p><div class="column"><p><span> <br /> </span></p><p><span>To use the created profile in other projects</span></p><hr /><div class="layoutArea"><div class="column"><ul><li><span>From the </span> <span><strong>File</strong> </span> <span>menu, choose </span> <span><strong><ac:link><ri:page ri:space-key="MD190" ri:content-title="Managing used projects" /><ac:plain-text-link-body><![CDATA[Use Project]]></ac:plain-text-link-body></ac:link></strong> </span><span>and select the project file. Only shared packages of the module will be loaded into the project.</span></li></ul><p><span><br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1df7a8b3-7352-49fe-939c-b019e157044c"><ac:parameter ac:name="title">Tip</ac:parameter><ac:rich-text-body><div class="page" title="Page 8"><div class="layoutArea"><div class="column"><p><span>If you don’t want to see particular information, move elements from shared packages into the root model or other non-shared packages in your module. </span></p></div></div></div></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></div></div></div></div><div class="column"><p><br /></p></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="39b06bcc-926e-4d18-b7a7-01bccb16f880"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f7e1aeb3-6478-4f10-b6af-7c9a8c92c427" /></p><ul><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Project partitioning" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973656 space=UPDG version=1 -->
## PAGE 00165: Creating Property Groups and Subgroups

- page_id: `243973656`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973656/Creating+Property+Groups+and+Subgroups
- version_number: 1
- version_date: `2025-07-31T19:04:50.807+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data
- labels: []

### NORMALIZED CONTENT

Create your own groups and subgroups to display the properties of both standard UML metaclasses or [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT']. You can also choose where you want to see these property groups and subgroups. Property groups and subgroups can be visible in the following places:

- Element’s [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] .

[IMAGE alt='' src='']

###### Property groups and subgroups in the element's SpecificationWindow

- Element’s Properties panel (at the bottom of the [CONFLUENCE_PAGE title='Model Browser' space='MDTWRT'] ).
- Element’s shortcut menu > Go To > submenu.

###### Property groups and subgroups in the element's shortcut menu

- [CONFLUENCE_PAGE title='Displaying or hiding elements in compartments on shapes' space='MDTWRT']**Compartment Edit** dialog .

- [CONFLUENCE_PAGE title='Specifying criteria, layout, and depth' space='MDTWRT']**Criterion Editor** dialog for editing the relation’s criteria in the [CONFLUENCE_PAGE title='Relation Map' space='MDTWRT'].

To create a property group

1. In the Model Browser, right-click a customization element and choose Create Element > Property Group .
2. Type the attribute’s name (used to name the property group).
3. Open the attribute’s Specification window.
4. Edit the property values in the general specification pane. Each property is described in the description area in the Specification window.
5. Click Close .

A stereotype [CONFLUENCE_PAGE title='«propertyGroup» Properties' space=''] has been automatically applied to the newly created attribute.

To create a property subgroup

1. Choose the customization element you want to create a property subgroup for. The customization element must have at least one attribute with the stereotype «propertyGroup» applied.
2. Right-click the attribute with a stereotype «propertyGroup» and choose Create Element > Property Group .
3. Type the attribute’s name (used to name the property subgroup).
4. Open the attribute’s Specification window.
5. In the general specification pane, edit the property values (properties are described in the table below). A subgroup does not inherit the properties of the group. You must specify them for each subgroup separately.
6. Click Close .

A stereotype «propertyGroup» has been automatically applied to the newly created attribute.

#### INFO: Note

Note

The stereotype «propertyGroup» is applied when creating either a property group or a subgroup.

Depending on the attribute hierarchy, the attribute will either be a property group or subgroup:

1. If an attribute with a stereotype «propertyGroup» is owned by a customization element, it is a property group.
2. If an attribute with a stereotype «propertyGroup» is owned by another attribute with the same stereotype, then it is a property subgroup.

#### INFO: «propertyGroup» properties

«propertyGroup» properties

All properties of a stereotype «propertyGroup» are described in [CONFLUENCE_PAGE title='«propertyGroup» Properties' space=''].

#### PANEL: Related Pages

Related Pages

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Create your own groups and subgroups to display the properties of both standard UML metaclasses or <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotypes]]></ac:plain-text-link-body></ac:link>. You can also choose where you want to see these property groups and subgroups. Property groups and subgroups can be visible in the following places:</p><p><br /></p><div class="layoutArea"><div class="column"><ul><li>Element’s <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>.</li></ul><p><br /><br /><ac:image ac:align="center"><ri:attachment ri:filename="groups_subgroups_spec.png" /></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(112,112,112);">Property groups and subgroups in the element's Specification </span><span style="color: rgb(112,112,112);">Window</span></h6><ul><li>Element’s <strong>Properties</strong> panel (at the bottom of the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Model Browser" /></ac:link>).</li><li>Element’s shortcut menu &gt; <strong>Go To</strong> &gt; submenu.</li></ul><p><br /></p><ac:image ac:align="center"><ri:attachment ri:filename="groups_subgroups_goto.png" /></ac:image><h6 style="text-align: center;"><span style="color: rgb(112,112,112);">Property groups and subgroups in the element's shortcut menu</span><br /><br /><br /></h6><ul><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Displaying or hiding elements in compartments on shapes" /><ac:link-body><strong>Compartment Edit</strong> dialog</ac:link-body></ac:link>. </li></ul><div class="column"><ul><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specifying criteria, layout, and depth" /><ac:link-body><strong>Criterion Editor </strong> <span>dialog</span></ac:link-body></ac:link><span> for editing the relation’s criteria in the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Relation Map" /><ac:plain-text-link-body><![CDATA[Relation Map diagram]]></ac:plain-text-link-body></ac:link>. <br /></span><span><br /></span></li></ul></div><div class="column"><div class="layoutArea"><div class="column"><p><span>To create a property group</span></p><hr /><ol><li>In the Model Browser, right-click a customization element and choose <strong><ac:inline-comment-marker ac:ref="1728bfeb-1a8c-4309-ae35-b8c597a1d4d5">Create Element</ac:inline-comment-marker></strong> &gt; <strong>Property Group</strong>.</li><li>Type the attribute’s name (used to name the property group).</li><li>Open the attribute’s Specification window.</li><li>Edit the property values in the general specification pane. Each property is described in the description area in the Specification window.</li><li>Click <strong>Close</strong>.</li></ol><div class="column"><p><span> <br /></span></p><p><span>A stereotype <ac:inline-comment-marker ac:ref="926924d3-3697-43da-b310-6788d29c86c9"><ac:link><ri:page ri:content-title="«propertyGroup» Properties" /><ac:plain-text-link-body><![CDATA[«propertyGroup»]]></ac:plain-text-link-body></ac:link></ac:inline-comment-marker> has been automatically applied to the newly created attribute. </span></p><p><br /></p><p>To create a property subgroup</p><hr /><ol><li>Choose the customization element you want to create a property subgroup for. The customization element must have at least one attribute with the stereotype «propertyGroup» applied.</li><li>Right-click the attribute with a stereotype «propertyGroup» and choose <strong>Create Element</strong> &gt; <strong>Property Group</strong>.</li><li>Type the attribute’s name (used to name the property subgroup).</li><li>Open the attribute’s Specification window.</li><li>In the general specification pane, edit the property values (properties are described in the table below). A subgroup does not inherit the properties of the group. You must specify them for each subgroup separately.</li><li>Click <strong>Close</strong>.</li></ol><p>A stereotype «propertyGroup» has been automatically applied to the newly created attribute.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b24be5e3-3718-4650-8fcc-645c3789f20b"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The stereotype «propertyGroup» is applied when creating either a property group or a subgroup.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>Depending on the attribute hierarchy, the attribute will either be a property group or subgroup:</p><ol><li>If an attribute with a stereotype «propertyGroup» is owned by a customization element, it is a property group.</li><li>If an attribute with a stereotype «propertyGroup» is owned by another attribute with the same stereotype, then it is a property subgroup. </li></ol></div><div class="column"><ac:image><ri:attachment ri:filename="groups_and_subgroups.png" /></ac:image></div><div class="column"><p><br /></p><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="4762b923-6321-41cf-88ad-1e2b26459bba"><ac:parameter ac:name="title">«propertyGroup» properties</ac:parameter><ac:rich-text-body><p>All properties of a <span> stereotype «propertyGroup» are described in <ac:link><ri:page ri:content-title="«propertyGroup» Properties" /></ac:link>.</span></p></ac:rich-text-body></ac:structured-macro><p><span><br /></span></p></div></div></div></div></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e6cf0582-f701-4d85-8a56-2af3c971fe97"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d8822dad-e2df-4092-bf1e-9f667a683527"><ac:parameter ac:name="page"><ac:link /></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973503 space=UPDG version=1 -->
## PAGE 00166: Creating Structured Expression Tags

- page_id: `243973503`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973503/Creating+Structured+Expression+Tags
- version_number: 1
- version_date: `2025-07-31T19:04:47.301+02:00`
- ancestors: UML Profiling and DSL Guide > Working with Profiles > Creating Profiles
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Tags

1534683666

#### CONTENT-COLUMN: Tags

1534683677

#### CONTENT-BLOCK: Tags

1534683667

If you need a tag value, as defined by using the dialog for [CONFLUENCE_PAGE title='Specifying criteria for querying model' space='MDTWRT'], you must create a structured expression tag definition.

To create a structured expression tag definition

1. Create a new [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT'] .
2. Right-click the stereotype and select Create Element > Property to create a new tag definition.
3. Open the [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] of the tag definition and select the Type property. Click the property specification cell and select the StructuredExpression value as a type. [ATTACHMENT filename='creating_structured_expression_tag_definition.png']

Once the tag definition is created, you can apply the stereotype with this tag definition on an element in your model. Then, in the Specification window of the element, click the **Tags** property group, select the structured expression tag, and click the **Create Value** button to define the value.

#### NOTE: Tags

Tags

The structured expression tag can also be represented as a regular property in the Specification window and **Properties tab**of the element.You must then [CONFLUENCE_PAGE title='Creating Customization Data' space=''] for the stereotype with this tag definition.

1534683665

**Related Pages**

- Applying Stereotypes
- Stereotype
- Tag
- Creating Customization Data
- Specifying criteria for querying model

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="b208910f-66d7-466e-b1fb-0ea9335dbd2f"><ac:parameter ac:name="id">1534683666</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="7cc74a5f-19fe-4caa-97cd-0eaac3cfb903"><ac:parameter ac:name="id">1534683677</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="768700e6-2ebe-435e-84ca-35849ed42daa"><ac:parameter ac:name="id">1534683667</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p><span>If you need a tag value, as defined by using the dialog for <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specifying criteria for querying model" /><ac:plain-text-link-body><![CDATA[specifying criteria]]></ac:plain-text-link-body></ac:link>, you must create a structured expression tag definition. </span></p><p>To create a structured expression tag definition</p><hr /><ol><li>Create a new <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotype]]></ac:plain-text-link-body></ac:link>.</li><li>Right-click the stereotype and select <strong>Create Element &gt; Property</strong> to create a new tag definition.</li><li>Open the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> of the tag definition and select the <strong>Type </strong>property. Click the property specification cell and select the StructuredExpression value as a type.<br /><ac:image><ri:attachment ri:filename="creating_structured_expression_tag_definition.png" /></ac:image></li></ol><p>Once the tag definition is created, you can apply the stereotype with this tag definition on an element in your model. Then, in the Specification window of the element, click the <strong>Tags</strong> property group, select the structured expression tag, and click the <strong>Create Value</strong> button to define the value.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="78d202bf-2ca4-4f0c-98a8-ef09081d8e9a"><ac:parameter ac:name="title">Tags</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p><span>The structured expression tag can also be represented as a regular property in the Specification window and</span> <strong>Properties tab</strong><span> of the element. </span>You must then <ac:link><ri:page ri:content-title="Creating Customization Data" /><ac:plain-text-link-body><![CDATA[create a customization data]]></ac:plain-text-link-body></ac:link> for the stereotype with this tag definition. </p></div></div></ac:rich-text-body></ac:structured-macro><p><span> <br /> </span></p></div></div></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d6d04c2e-0863-41bb-aeb9-89fff0261fc9"><ac:parameter ac:name="id">1534683665</ac:parameter><ac:rich-text-body><p><strong>Related Pages</strong></p><ul><li><a href="https://docs.nomagic.com/display/MDTWRT/Applying+Stereotypes">Applying Stereotypes</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Stereotype">Stereotype</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Tag">Tag</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Creating+Customization+Data">Creating Customization Data</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Specifying+criteria+for+querying+model">Specifying criteria for querying model</a></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973502 space=UPDG version=1 -->
## PAGE 00167: Creating Tags with Default Values

- page_id: `243973502`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973502/Creating+Tags+with+Default+Values
- version_number: 1
- version_date: `2025-07-31T19:04:47.261+02:00`
- ancestors: UML Profiling and DSL Guide > Working with Profiles > Creating Profiles
- labels: []

### NORMALIZED CONTENT

To create a tag with a default value

1. [CONFLUENCE_PAGE title='Tag' space='MDTWRT'] (Property).
2. [CONFLUENCE_PAGE title='Editing tagged value' space='MDTWRT'] for this tag.
3. Specify multiplicity larger than 0 (1, 1..*, 2, etc.).

Multiplicity means that this tag is mandatory.

When the stereotype is applied, mandatory tags will be automatically created and default values will be assigned.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Applying Stereotypes' space='']
- [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT']
- [CONFLUENCE_PAGE title='Tag' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p>To create a tag with a default value</p><hr /><ol><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Tag" /><ac:plain-text-link-body><![CDATA[Create a tag definition]]></ac:plain-text-link-body></ac:link> (Property).</li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Editing tagged value" /><ac:plain-text-link-body><![CDATA[Specify default value]]></ac:plain-text-link-body></ac:link> for this tag.</li><li><span>Specify multiplicity larger than 0 (1, 1..*, 2, etc.). </span></li></ol><p>Multiplicity means that this tag is mandatory.</p><p>When the stereotype is applied, mandatory tags will be automatically created and default values will be assigned. </p><p><br /></p></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b14401e6-4bad-4948-8ab5-88b81d7034fe"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Applying Stereotypes" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Tag" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973558 space=UPDG version=1 -->
## PAGE 00168: Creating your First Customization

- page_id: `243973558`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973558/Creating+your+First+Customization
- version_number: 1
- version_date: `2025-07-31T19:04:48.278+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Create Element

572341248

#### CONTENT-COLUMN: Create Element

572341251

#### CONTENT-BLOCK: Create Element

572341250

We will demonstrate the recommended step-by-step instructions on how to customize an element, how to begin to create customization, how to create customization data, and how the customization data will be represented on the DSL element.

1. [CONFLUENCE_PAGE title='Creating projects' space='MDTWRT'] and name it *Organization_Stereotypes.mdzip*.
2. Create a Profile element and name it S*tereotypes*. StereotypesThe purpose of the Profile named *Stereotypes* is to store all the stereotypes. Later we will share the package in order to use the stereotypes in the customization project.
3. In the Profile element, [CONFLUENCE_PAGE title='Creating diagrams' space='MDTWRT'] and name it *Stereotypes*. The Profile Diagram palette contains all the necessary buttons for the customization creation.
4. In the Profile Diagram, [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT'] and name it *Company*.
5. Apply the Class metaclass to the *Company* Stereotype. [IMAGE alt='' src=''] You can see how customization rules will be passed to the *DSL* element by using the stereotype.We selected the *Class* metaclass, because the «Company» stereotype will be applied to a class element. In other words, the type of the DSL element will be the class.You can also assign an icon to the stereotype. The icon will be represented on the DSL element.
6. [CONFLUENCE_PAGE title='Sharing project data' space='MDTWRT']. The *Organization_Stereotypes.mdzip* project becomes a shared project. Only the content of the shared *stereotypes*package will be visible in the project that will use the project.
7. Save the*Organization_Stereotypes.mdzip*project.
8. [CONFLUENCE_PAGE title='Creating projects' space='MDTWRT'] and name it*Organization_Customizations.mdzip.*
9. Create a Profile element and name it *C**ustomizations*. The purpose of the *C**ustomizations* package is to store all the customization data. Later we will share the package.
10. In the Profile element, [CONFLUENCE_PAGE title='Creating diagrams' space='MDTWRT'] and name it*Customizations*. The *Customizations* diagram is intended for customization elements creation.
11. In the Profile Diagram, create a customization element and name it Company. [IMAGE alt='' src=''] On a diagram, you can see that the customization element is a class with the applied «*Customization*» stereotype.
12. [CONFLUENCE_PAGE title='Using other projects in a project' space='MDTWRT'] the*Organization_Stereotypes.mdzip*project in the current project.
13. Open the*Company*customization element [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'], under the**General**category, click the**Customization Target**property and then specify the*Company*stereotype. [IMAGE alt='' src=''] To assign a customization target quickly, select the *Company* stereotype in the Model Browser and drag it to the shape of the *Company* customization element on the diagram pane.In the **Customization** Specification window, you can specify customization data that will be passed to the DSL element.
14. In the*Company*customization element Specification window, under the**General**category, set the**Hide Metatype**check box to true. If the value is*true*, the element acts like a new standard element type in the modeling tool.
15. In the*Company*customization element Specification window, under the**Owned Elements**category, click the**Possible Owners**property and then select the*Package*metaclass. [IMAGE alt='' src=''] The DSL element will be added to the package shortcut menu, under the**Create Element**command.
16. Share the *C**ustomizations*package. The*Organization_Customizations.mdzip*project with the shared *C**ustomizations*package becomes a shared project.
17. Save the*Organization_Customizations.mdzip*project.
18. Create a project and name it*Organization*.
19. Use the *Organization_Customizations.mdzip* project in the *Organization* project. The *Organization_Stereotypes.mdzip* project will be used in the *Organization* project automatically, because the *Organization_Customizations.mdzip* project uses the *Organization_Stereotypes.mdzip* project.
20. In the*Organization*project, create a Package and in that package, create a class element and name it*NoMagic*.
21. Apply the*Company*stereotype to the*NoMagic*class element.
22. Save and reopen the project.

If you modify the customization element and/or stereotype, make sure to reopen projects that use it.

In the following figure, you can see the Containment tree of the project with the used

Organization_Stereotypes.mdzip

and

Organization_Customizations.mdzip

projects.

[IMAGE alt='' src='']

###### Structure of a project that use other projects

In this example, the «*Company*» stereotype is applied to the*NoMagic*class element. You can see that the*Company*element is added to the package shortcut menu.

[IMAGE alt='' src='']

###### Example of the “Possible Owner” property realization

#### NOTE: Create Element

Create Element

If you do not want the new DSL element to appear on the **Create Element** menu, you can hide the appropriate command when [CONFLUENCE_PAGE title='Customizing Perspectives' space='MDTWRT'].

572341246

**Related pages**

- [CONFLUENCE_PAGE title='Rules of Stereotypes that cannot be Allowed to Apply' space='']
- [CONFLUENCE_PAGE title='Customization Elements' space='']
- [CONFLUENCE_PAGE title='Customization Element Properties' space='']
- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Project partitioning' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="303d0e07-e13a-49ff-84dd-f1e18ef29ea9"><ac:parameter ac:name="id">572341248</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fd1450a5-f4e5-47e3-b3a2-90e7e8ec5818"><ac:parameter ac:name="id">572341251</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9876e709-fa37-455f-b956-3dd1707b0820"><ac:parameter ac:name="id">572341250</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><span style="color: rgb(0,0,0);">We will demonstrate the recommended step-by-step instructions on how to customize an element, how to begin to create customization, how to create customization data, and how the customization data will be represented on the DSL element. </span></p><ol><li><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Creating projects" /><ac:plain-text-link-body><![CDATA[Create a new project]]></ac:plain-text-link-body></ac:link> and name it <em>Organization_Stereotypes.mdzip</em>.</span></li><li><p class="auto-cursor-target"><span style="color: rgb(0,0,0);">Create a Profile element and name it S<em>tereotypes</em>.</span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="57f64cb1-78e8-44a7-af54-eb5ccb5b2811"><ac:parameter ac:name="title">Stereotypes</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p>The purpose of the Profile named <em>Stereotypes</em> is to store all the stereotypes. Later we will share the package in order to use the stereotypes in the customization project. </p></div></div></ac:rich-text-body></ac:structured-macro></li><li><p class="auto-cursor-target"><span style="color: rgb(0,0,0);">In the Profile element, <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Creating diagrams" /><ac:plain-text-link-body><![CDATA[create a Profile Diagram]]></ac:plain-text-link-body></ac:link> and name it <em>Stereotypes</em>.</span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="6a253e91-3ff6-4a09-b72d-ded28b49d571"><ac:rich-text-body><div class="layoutArea"><div class="column"><p>The Profile Diagram palette contains all the necessary buttons for the customization creation.</p></div></div></ac:rich-text-body></ac:structured-macro></li><li><p class="auto-cursor-target"><span style="color: rgb(0,0,0);">In the Profile Diagram, <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[create a Stereotype element]]></ac:plain-text-link-body></ac:link> and name it <em>Company</em>.</span></p></li><li><p class="auto-cursor-target">Apply the Class metaclass to the <em>Company</em> Stereotype.</p><p class="auto-cursor-target"><ac:image ac:align="center"><ri:attachment ri:filename="case_study1.png" /></ac:image></p><p><br /><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="d528fa48-2508-4cd9-bd87-f181b6e5d7e0"><ac:rich-text-body><div class="layoutArea"><div class="column"><div class="layoutArea"><div class="column"><ul><li><p>You can see how customization rules will be passed to the <em>DSL</em> element by using the stereotype.</p></li><li><p>We selected the <em>Class</em> metaclass, because the «Company» stereotype will be applied to a class element. In other words, the type of the DSL element will be the class.</p></li><li><p>You can also assign an icon to the stereotype. The icon will be represented on the DSL element. </p></li></ul></div></div></div></div></ac:rich-text-body></ac:structured-macro></li><li><p class="auto-cursor-target"><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Sharing project data" /><ac:plain-text-link-body><![CDATA[Share the stereotypes package]]></ac:plain-text-link-body></ac:link>. The <em>Organization_Stereotypes.mdzip</em> project becomes a shared project.</span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="8373ba82-4b66-44a7-8e80-d11a070d6812"><ac:rich-text-body><div class="layoutArea"><div class="column"><p>Only the content of the shared <em>stereotypes </em>package will be visible in the project that will use the project. </p></div></div></ac:rich-text-body></ac:structured-macro></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);">Save the </span><em style="color: rgb(0,0,0);">Organization_Stereotypes.mdzip </em><span style="color: rgb(0,0,0);">project.</span></p></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Creating projects" /><ac:plain-text-link-body><![CDATA[Create a new project]]></ac:plain-text-link-body></ac:link> and name it </span><em style="color: rgb(0,0,0);">Organization_Customizations.mdzip.</em></p></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);">Create a Profile element and name it <em>C</em></span><em style="color: rgb(0,0,0);">ustomizations</em><span style="color: rgb(0,0,0);">.</span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e5afdabb-e53f-4b76-bf89-517b9128110c"><ac:rich-text-body><div class="layoutArea"><div class="column"><p>The purpose of the <em>C</em><em>ustomizations </em> package is to store all the customization data. Later we will share the package. </p></div></div></ac:rich-text-body></ac:structured-macro></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">In the Profile element, <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Creating diagrams" /><ac:plain-text-link-body><![CDATA[create a Profile Diagram]]></ac:plain-text-link-body></ac:link> and name it</span><span style="color: rgb(51,51,51);"> </span><em>Customizations</em>.<br /></span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="0a6a60dd-3ab4-42c9-bb75-7bb920409ef2"><ac:rich-text-body><p>The <em>Customizations </em> diagram is intended for customization elements creation. </p></ac:rich-text-body></ac:structured-macro></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);">In the Profile Diagram, create a customization element and name it Company.</span><br /></span></p><p style="margin-top: 10.0px;color: rgb(51,51,51);text-align: center;"><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);"><ac:image><ri:attachment ri:filename="case_study2.png" /></ac:image><br /></span></span></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="01cb1956-a116-43c1-be69-38d689cc2b3f"><ac:rich-text-body><p>On a diagram, you can see that the customization element is a class with the applied «<em>Customization</em>» stereotype.</p></ac:rich-text-body></ac:structured-macro></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Using other projects in a project" /><ac:plain-text-link-body><![CDATA[Use]]></ac:plain-text-link-body></ac:link> the </span><em>Organization_Stereotypes.mdzip</em><span style="color: rgb(0,0,0);"> project in the current project.</span></span></span></p></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);">Open the </span><em style="color: rgb(0,0,0);">Company</em><span style="color: rgb(0,0,0);"> customization element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>, under the </span><strong style="color: rgb(0,0,0);">General</strong><span style="color: rgb(0,0,0);"> category, click the </span><strong style="color: rgb(0,0,0);">Customization Target</strong><span style="color: rgb(0,0,0);"> property and then specify the </span><em style="color: rgb(0,0,0);">Company</em><span style="color: rgb(0,0,0);"> stereotype.</span></p><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);"><ac:image ac:align="center"><ri:attachment ri:filename="case_study3.png" /></ac:image><br /></span></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="43dc4ef8-8bbc-49c7-9c36-fdb83a750c21"><ac:rich-text-body><ul><li><p>To assign a customization target quickly, select the <em>Company </em> stereotype in the Model Browser and drag it to the shape of the <em>Company</em> customization element on the diagram pane.</p></li><li><p>In the <strong>Customization </strong> Specification window, you can specify customization data that will be passed to the DSL element. </p></li></ul></ac:rich-text-body></ac:structured-macro></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);">In the </span><em>Company</em><span style="color: rgb(0,0,0);"> customization element Specification window, under the </span><strong>General</strong><span style="color: rgb(0,0,0);"> category, set the </span><strong>Hide Metatype</strong><span style="color: rgb(0,0,0);"> check box to true. If the value is </span><em>true</em><span style="color: rgb(0,0,0);">, the element acts like a new standard element type in the modeling tool.</span></span></p></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);">In the </span><em style="color: rgb(0,0,0);">Company</em><span style="color: rgb(0,0,0);"> customization element Specification window, under the </span><strong style="color: rgb(0,0,0);">Owned Elements</strong><span style="color: rgb(0,0,0);"> category, click the </span><strong style="color: rgb(0,0,0);">Possible Owners</strong><span style="color: rgb(0,0,0);"> property and then select the </span><em style="color: rgb(0,0,0);">Package</em><span style="color: rgb(0,0,0);"> metaclass.</span></p><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);"><ac:image ac:align="center"><ri:attachment ri:filename="case_study4.png" /></ac:image></span></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="033e01ee-e083-4779-a008-280634403fab"><ac:rich-text-body><p><span>The DSL element will be added to the package shortcut menu, under the </span><strong>Create Element </strong><span>command.</span></p></ac:rich-text-body></ac:structured-macro></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);">Share the <em>C</em></span><em>ustomizations</em><span style="color: rgb(0,0,0);"> package. The </span><em>Organization_Customizations.mdzip</em><span style="color: rgb(0,0,0);"> project with the shared <em>C</em></span><em>ustomizations</em><span style="color: rgb(0,0,0);"> package becomes a shared project.</span></span></p></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);">Save the </span><em style="color: rgb(0,0,0);">Organization_Customizations.mdzip</em><span style="color: rgb(0,0,0);"> project.</span></p></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);">Create a project and name it</span><em style="color: rgb(0,0,0);"> Organization</em><span style="color: rgb(0,0,0);">.</span></p></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);">Use the <em>Organization_Customizations.mdzip</em> project in the <em>Organization</em> project</span><span style="color: rgb(0,0,0);">.</span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="71339360-f472-49fa-b96a-3086bedcb447"><ac:rich-text-body><p>The <em>Organization_Stereotypes.mdzip </em> project will be used in the <em>Organization </em> project automatically, because the <em>Organization_Customizations.mdzip </em> project uses the <em>Organization_Stereotypes.mdzip </em> project. </p></ac:rich-text-body></ac:structured-macro></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);">In the </span><em>Organization</em><span style="color: rgb(0,0,0);"> project, create a Package and in that package, create a class element and name it </span><em>NoMagic</em><span style="color: rgb(0,0,0);">.</span></span></p></li><li><p style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);">Apply the </span><em style="color: rgb(0,0,0);">Company</em><span style="color: rgb(0,0,0);"> stereotype to the </span><em style="color: rgb(0,0,0);">NoMagic</em><span style="color: rgb(0,0,0);"> class element.</span></p></li><li style="margin-top: 10.0px;color: rgb(51,51,51);"><span style="color: rgb(0,0,0);">Save and reopen the project.</span></li></ol><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="996ebbf2-e535-41c3-99f0-f1a256423bdd"><ac:rich-text-body><p>If you modify the customization element and/or stereotype, make sure to reopen projects that use it.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><div><span style="color: rgb(0,0,0);"><br /></span></div><div><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);">In the following figure, you can see the Containment tree of the project with the used </span><em>Organization_Stereotypes.mdzip </em><span style="color: rgb(0,0,0);">and </span><em><em>Organization_Customizations.mdzip</em></em><span style="color: rgb(0,0,0);"> projects.</span></span></div><div><p><br /><ac:image ac:align="center"><ri:attachment ri:filename="element_added_to_the_package_shortcut_menu.png" /></ac:image></p><h6 style="text-align: center;">Structure of a project that use other projects</h6><p><br /></p></div></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p class="_mce_tagged_br"><span style="color: rgb(0,0,0);">In this example, the «</span><em style="color: rgb(0,0,0);">Company</em><span style="color: rgb(0,0,0);">» stereotype is applied to the </span><em style="color: rgb(0,0,0);">NoMagic</em><span style="color: rgb(0,0,0);"> class element. You can see that the </span><em style="color: rgb(0,0,0);">Company</em><span style="color: rgb(0,0,0);"> element is added to the package shortcut menu.</span></p><p class="_mce_tagged_br"><ac:image ac:align="center"><ri:attachment ri:filename="containment_tree_customization.png" /></ac:image></p><h6 style="text-align: center;">Example of the “Possible Owner” property realization</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="556cab0c-c270-46fa-a7ce-f516c343d4d9"><ac:parameter ac:name="title">Create Element</ac:parameter><ac:rich-text-body><p>If you do not want the new DSL element to appear on the <strong>Create Element</strong> menu, you can hide the appropriate command when <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Customizing Perspectives" /><ac:plain-text-link-body><![CDATA[customizing your modeling tool perspective]]></ac:plain-text-link-body></ac:link>. </p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f602aeb3-90f3-47f1-af3c-25d9ee96a986"><ac:parameter ac:name="id">572341246</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Rules of Stereotypes that cannot be Allowed to Apply" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Elements" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Element Properties" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Project partitioning" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973668 space=UPDG version=1 -->
## PAGE 00169: Creating your first numbering customization

- page_id: `243973668`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973668/Creating+your+first+numbering+customization
- version_number: 1
- version_date: `2025-07-31T19:04:51.270+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Creating Numbering Customizations
- labels: []

### NORMALIZED CONTENT

1099680388

1099680390

1099680389

To create a numbering customization for an element

33none

Assume you need to number packages as shown:

[IMAGE alt='' src='']

###### Task for numbering packages.

There should be three numbering levels. The following table describes the rules for calculating package numbers in each level:

| Numbering level | Numbering format | Examples |
| --- | --- | --- |
| 1st | <number> | “1”, “2”, “3” |
| 2nd | <number><separator><character> | “1.A”, “1.B”, “2.A”, “2.B” |
| 3rd | <number><separator><character><separator><number> | “1.A.1”, “1.A.2”, “1.A.3”,“2.B.1”, “2.B.2” |

So we need to create a numbering scheme and use it in the numbering customization for [CONFLUENCE_PAGE title='Package' space='MDTWRT'] elements.

##### 1. Creating a stereotype to customize a desired element

To create a stereotype that customizes UML Packages

1. Create a Profile element.
2. In the Profile element, [CONFLUENCE_PAGE title='Creating diagrams' space='MDTWRT'].
3. In the Profile Diagram, [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT'].
4. Name the stereotype *Numbered Package.*
5. Right-click the stereotype shape and select Metaclass in the shortcut menu.
6. Select the Package metaclass and click Apply .

[IMAGE alt='' src='']

###### Stereotype for customizing UML packages.

Make the «Numbered Package» stereotype invisible if you want the stereotype and its properties to be hidden in a diagram.

##### 2. Adding a new attribute for storing numbers

To add a new attribute for storing package numbers to the «Numbered Package» stereotype

1. Select the shape of the «Numbered Package» stereotype on the Profile diagram pane.
2. Add a new String type attribute named No .

[IMAGE alt='' src='']

###### Property for storing package numbers.

##### 3. Creating a numbering scheme to define a numbering style and number parts

To create a numbering scheme

1. On the Profile diagram palette, click the Class button.
2. Click a free space on the diagram pane. A new Class shape appears.
3. Name the Class *Package Numbering Scheme*. The name of the numbering scheme will be displayed in the [CONFLUENCE_PAGE title='Element Numbering dialog' space='MDTWRT']**Element Numbering** dialog. We recommend giving it a short and meaningful name.
4. Right-click the Class shape and select Stereotype in the shortcut menu.
5. Select the «NumberingScheme» stereotype and click Apply .

[IMAGE alt='' src='']

###### Scheme for numbering UML packages.

To define a numbering style

1. Open the [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] of the newly created numbering scheme.
2. Click the Numbering Style value cell to open the list of available numbering styles. Select the Multi-level numbering style in this list. You must have three numbering levels to number packages.
3. Click Close when you are done.

[IMAGE alt='' src='']

###### Numbering scheme with multilevel numbering style defined.

create_number_part

The following table shows number parts that should be used to create the numbering formats in the proceeding procedures.

| Number part | Number part name |
| --- | --- |
| <number> | Level 1 |
| <separator> | Dot 1 |
| <character> | Level 2 |
| <separator> | Dot 2 |
| <number> | Level 3 |

To create a number part

1. Open the [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] of the numbering scheme.
2. On the left side menu of the Specification window, select Number Parts and click Create . The Specification of Number Part properties window opens.

[IMAGE alt='' src='']

###### Creating a new number part.

To specify a number part for the first numbering level

1. .
2. In the Specification of Number Part properties window, set the Name to Level 1 .
3. Click the Sequence property value specification cell and select Numeric in the values list. You must have numbers on the first numbering level.
4. Click the Initial Value property value cell and type the number 1 as its value. Numbering at the first level should start at 1 .
5. Click Close when you are done.

[IMAGE alt='' src='']

###### Numbering scheme with number part defined for first numbering level.

To specify a number part for the first separator

1. 
2. In the Specification of Number Part properties window, set the Name to Dot 1 .
3. Click the Sequence property value specification cell. Select Separator in the values list.
4. Click the Initial Value property value cell and type the . character (a dot) as its value. The separator between the first and the second numbering level should be a dot.
5. Click Close when you are done.

To specify a number part for the second numbering level

1. .
2. In the Specification of Number Part properties window, set the Name to Level 2 .
3. Click the Sequence property value specification cell. Select Character in the values list. You must have letters at the second numbering level.
4. Click the **Initial Value** property value cell and type the letter **A** as its value. The numbering at the second level should start at A.
5. Click **Close** when you are done.

[IMAGE alt='' src='']

###### Numbering scheme with number parts defined for the second numbering level.

The rest of the number parts are created accordingly.

[IMAGE alt='' src='']

###### Numbering scheme with all number parts defined.

As there are no number parts specified for the fourth (and beyond) numbering levels, packages will be numbered using the number parts of the third numbering level. For example, “1.A.1.1”, “1.B.1.2”, and so forth.

##### 4. Creating a customization element for the stereotype that customizes the desired element

In order to use the scheme for numbering packages, you must define it in the numbering customization for package elements. First, create a customization element.

To create a customization element for the «Numbered Package» stereotype

1. On the diagram palette, click the Customization button.
2. Click a free space on the diagram pane. The new customization shape appears.
3. Name the customization Numbered Package Customization .
4. Open the [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] of the Customization .
5. Click the Customization Target property. Select the «Numbered Package» stereotype in the element Selection dialog and click OK .
6. Set the **Show Properties When Not Applied** property to *true*. All properties of the «Numbered Package» stereotype will be visible as properties of the *Package* metaclass, even if the stereotype is not yet applied.
7. Click **Close** when you are done.

[IMAGE alt='' src='']

###### Customization element for the «Numbered Package» stereotype.

##### 5. Add a numbering attribute to the customization element

After creating the customization for the «Numbered Package» stereotype, specify the stereotype attribute for storing element numbers as well as defining a numbering scheme to use. For this, you must create a numbering attribute.

To add a numbering attribute to the customization element of the «Numbered Package» stereotype

1. Select the shape of the customization.
2. Add a new Auto Numbering Property named Package Numbering .
3. Open the [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] of the created attribute.
4. Specify a value for the Numbered Property property. Click the property value cell and then click the ... button. In the element Selection dialog, select the No property of the «Numbered Package» stereotype and click OK .
5. Specify a value for the Numbering Scheme property. Click the value cell and either:
  - Select the Package Numbering Scheme class in the opened list.
  - Click the ... button. In the element Selection dialog, select the Package Numbering Scheme class and click OK .
6. Change the Default Number property value to true . The true value indicates that this numbering attribute will be set as the default when numbering instances of the customized Package metaclass.
7. Specify the Use Prefix On Owner attribute value. The true value indicates that the element prefix will be used for its numbered owner as well.
8. Click Close when you are done.
9. Save and reopen the project to apply the created numbering customization.

[IMAGE alt='' src='']

###### Numbering attribute in the customization element of the «Numbered Package» stereotype.

##### 6. Changing the number display mode

To see the number before the element name, you must change the number display mode.

To change the number display mode on packages

1. Open the appropriate package diagram.
2. Create a package to apply the numbering scheme to.
3. Name the package Organization .
4. Right-click the Organization package and select Stereotype in the shortcut menu.
5. Select the «Numbered Package» stereotype and click Apply .
6. Right-click the shape of the package on the diagram pane. Click Symbol Properties .
7. Set the Show Number Tag Name property value to false . The false indicates that the element number tag name (the No property of the «Numbered Package» stereotype) will not be displayed on the package shape.
8. Click the Element Number Display Mode value cell to open the list of available modes. Select the Before the element name mode in this list.
9. Set the Show Tagged Values property value to false . The false indicates that the tagged values will not be displayed on the package shape.
10. Click the Show Stereotypes value cell to open the list of available modes. Select the Do Not Display mode in this list if you don't want the «Numbered Package» stereotype to be displayed on the packages.

##### 7. Reopen the project to apply changes

Open the appropriate package diagram and see the packages numbered using the newly created numbering customization.

[IMAGE alt='' src='']

###### Packages numbered using a numbering customization.

1099680386

**Related pages**

- [CONFLUENCE_PAGE title='Creating Numbering Customizations' space='']
- [CONFLUENCE_PAGE title='Numbering Scheme property values' space='']
- [CONFLUENCE_PAGE title='Profile diagram' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="8de2f52c-3203-4189-86f9-04b49ce43946"><ac:parameter ac:name="id">1099680388</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c9236801-0c9a-4f6f-83ff-953c5fc946cf"><ac:parameter ac:name="id">1099680390</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6380c251-c185-4093-ba51-f68201f1a089"><ac:parameter ac:name="id">1099680389</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>To create a numbering customization for an element</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="179106a8-c8df-4e42-8df2-9799f41f734f"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter><ac:parameter ac:name="style">none</ac:parameter></ac:structured-macro></p><p>Assume you need to number packages as shown:</p><p><ac:image ac:align="center"><ri:attachment ri:filename="1_task_for_numbering_packages.png" /></ac:image></p><h6 style="text-align: center;">Task for numbering packages.</h6><p>There should be three numbering levels. The following table describes the rules for calculating package numbers in each level:</p><table class="wrapped relative-table" style="width: 57.0747%;"><colgroup> <col style="width: 18.5495%;" /> <col style="width: 53.1381%;" /> <col style="width: 28.3124%;" /> </colgroup><tbody><tr><th>Numbering level</th><th>Numbering format</th><th>Examples</th></tr><tr><td>1<sup>st</sup></td><td>&lt;number&gt;</td><td>“1”, “2”, “3”</td></tr><tr><td>2<sup>nd</sup></td><td>&lt;number&gt;&lt;separator&gt;&lt;character&gt;</td><td>“1.A”, “1.B”, “2.A”, “2.B”</td></tr><tr><td>3<sup>rd</sup></td><td>&lt;number&gt;&lt;separator&gt;&lt;character&gt;&lt;separator&gt;&lt;number&gt;</td><td><p>“1.A.1”, “1.A.2”, “1.A.3”,<br />“2.B.1”, “2.B.2”</p></td></tr></tbody></table><p>So we need to create a numbering scheme and use it in the numbering customization for <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Package" /></ac:link> elements. </p><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><span>1. Creating a stereotype to customize a desired element</span></h3><p>To create a stereotype that customizes UML Packages</p><hr /><ol><li><p><span>Create a Profile element</span><span>.</span></p></li><li><p><span> <span>In the Profile element,</span> <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Creating diagrams" /><ac:plain-text-link-body><![CDATA[create a Profile Diagram]]></ac:plain-text-link-body></ac:link>.<br /></span></p></li><li><p class="auto-cursor-target"><span>In the Profile Diagram, <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[create a Stereotype element]]></ac:plain-text-link-body></ac:link>.</span></p></li><li><p><span> <span>Name the stereotype <em>Numbered Package.</em> </span> </span></p></li><li>Right-click the stereotype shape and select <strong style="letter-spacing: 0.0px;">Metaclass </strong>in the shortcut menu.</li><li>Select the <em>Package</em> metaclass and click <strong>Apply</strong>.</li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="2_step_for_package_metaclass.png" /></ac:image></p><h6 style="text-align: center;">Stereotype for customizing UML packages.</h6><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="edc1e9db-7303-4ea2-845a-978debaf7e51"><ac:rich-text-body><p>Make the «Numbered Package» stereotype invisible if you want the stereotype and its properties to be hidden in a diagram.</p></ac:rich-text-body></ac:structured-macro><h3><span>2. Adding a new attribute for storing numbers</span></h3><p><span style="color: rgb(0,0,0);"> </span>To add a new attribute for storing package numbers to the «Numbered Package» stereotype</p><hr /><ol><li>Select the shape of the «Numbered Package» stereotype on the Profile diagram pane.</li><li>Add a new String type attribute named <em>No</em>.</li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="3_prop_for_storing_package_numbers.png" /></ac:image></p><h6 style="text-align: center;">Property for storing package numbers.</h6><h3>3. Creating a numbering scheme to define a numbering style and number parts</h3><p>To create a numbering scheme</p><hr /><ol><li>On the Profile diagram palette, click the <strong>Class</strong> button.</li><li>Click a free space on the diagram pane. A new Class shape appears.</li><li><p>Name the Class <em>Package Numbering Scheme</em>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="fae8d037-b205-4a06-83ec-2d689c415eec"><ac:rich-text-body><p>The name of the numbering scheme will be displayed in the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Element Numbering dialog" /><ac:link-body> <strong>Element Numbering</strong> dialog</ac:link-body></ac:link>. We recommend giving it a short and meaningful name.</p></ac:rich-text-body></ac:structured-macro></li><li>Right-click the Class shape and select <strong>Stereotype</strong> in the shortcut menu. </li><li>Select the «NumberingScheme» stereotype and click <strong>Apply</strong>.</li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="4_package_numbering_scheme.png" /></ac:image></p><h6 style="text-align: center;">Scheme for numbering UML packages.</h6><p><br /></p><p>To define a numbering style</p><hr /><ol><li>Open the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> of the newly created numbering scheme.</li><li>Click the <strong>Numbering Style</strong> value cell to open the list of available numbering styles. Select the <strong>Multi-level</strong> numbering style in this list. You must have three numbering levels to number packages.</li><li>Click <strong>Close</strong> when you are done.</li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="5_numbering_scheme_with_style_selected.png" /></ac:image></p><h6 style="text-align: center;">Numbering scheme with multilevel numbering style defined.</h6><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="19851e23-ee2a-4051-a5a0-38e03e611c7d"><ac:parameter ac:name="">create_number_part</ac:parameter></ac:structured-macro></p><p>The following table shows number parts that should be used to create the numbering formats in the proceeding procedures.</p><table class="wrapped"><colgroup> <col /> <col /> </colgroup><tbody><tr><th>Number part</th><th>Number part name</th></tr><tr><td>&lt;number&gt;</td><td>Level 1</td></tr><tr><td>&lt;separator&gt;</td><td>Dot 1</td></tr><tr><td>&lt;character&gt;</td><td>Level 2</td></tr><tr><td>&lt;separator&gt;</td><td>Dot 2</td></tr><tr><td>&lt;number&gt;</td><td>Level 3</td></tr></tbody></table><p><br /></p><p>To create a number part</p><hr /><ol><li>Open the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> of the numbering scheme.</li><li>On the left side menu of the Specification window, select <strong>Number Parts</strong> and click <strong>Create</strong>. The Specification of Number Part properties window opens.</li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="6_insert_new_number_part.png" /></ac:image></p><h6 style="text-align: center;">Creating a new number part.</h6><p><br /></p><p>To specify a number part for the first numbering level</p><hr /><ol><li><ac:link ac:anchor="create_number_part"><ac:plain-text-link-body><![CDATA[Create a new number part]]></ac:plain-text-link-body></ac:link>.</li><li>In the Specification of Number Part properties window, set the <strong>Name</strong> to <em>Level 1</em>.</li><li>Click the <strong>Sequence</strong> property value specification cell and select <strong>Numeric</strong> in the values list. You must have numbers on the first numbering level.</li><li>Click the <strong>Initial Value</strong> property value cell and type the number <strong>1</strong> as its value. Numbering at the first level should start at <strong>1</strong>.</li><li>Click <strong>Close</strong> when you are done.</li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="7_numbering_scheme_with_level_1.png" /></ac:image></p><h6 style="text-align: center;">Numbering scheme with number part defined for first numbering level.</h6><p>To specify a number part for the first separator</p><hr /><ol><li><ac:link ac:anchor="create_number_part"><ac:plain-text-link-body><![CDATA[Create a new number part.]]></ac:plain-text-link-body></ac:link></li><li>In the Specification of Number Part properties window, set the <strong>Name</strong> to <em>Dot 1</em>.</li><li>Click the <strong style="letter-spacing: 0.0px;">Sequence</strong> property value specification cell. Select <strong>Separator</strong> in the values list.</li><li>Click the <strong>Initial Value</strong> property value cell and type the <strong>.</strong> character (a dot) as its value. The separator between the first and the second numbering level should be a dot.</li><li>Click <strong>Close</strong> when you are done.</li></ol><p><br /></p><p>To specify a number part for the second numbering level</p><hr /><ol><li><ac:link ac:anchor="create_number_part"><ac:plain-text-link-body><![CDATA[Create a new number part]]></ac:plain-text-link-body></ac:link>.</li><li>In the Specification of Number Part properties window, set the <strong>Name</strong> to <em>Level 2</em>.</li><li>Click the <strong style="letter-spacing: 0.0px;">Sequence</strong> property value specification cell. Select <strong style="letter-spacing: 0.0px;">Character</strong> in the values list. You must have letters at the second numbering level.</li><li><p>Click the <strong>Initial Value</strong> property value cell and type the letter <strong>A</strong> as its value. The numbering at the second level should start at A.</p></li><li><p>Click <strong>Close</strong> when you are done.</p></li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="8_numbering_scheme_with_level_2.png" /></ac:image></p><h6 style="text-align: center;">Numbering scheme with number parts defined for the second numbering level.</h6><p><br /></p><p>The rest of the number parts are created accordingly.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="9_numbering_scheme_with_all_number_parts.png" /></ac:image></p><h6 style="text-align: center;">Numbering scheme with all number parts defined.</h6><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e655ce8c-c963-45b6-bf0f-8a3f178e622e"><ac:rich-text-body><p>As there are no number parts specified for the fourth (and beyond) numbering levels, packages will be numbered using the number parts of the third numbering level. For example, “1.A.1.1”, “1.B.1.2”, and so forth.</p></ac:rich-text-body></ac:structured-macro><h3>4. Creating a customization element for the stereotype that customizes the desired element</h3><p>In order to use the scheme for numbering packages, you must define it in the numbering customization for package elements. First, create a customization element.</p><p><br /></p><p>To create a customization element for the «Numbered Package» stereotype</p><hr /><ol><li>On the diagram palette, click the <strong>Customization</strong> button.</li><li>Click a free space on the diagram pane. The new customization shape appears.</li><li>Name the customization <em>Numbered Package Customization</em>.</li><li>Open the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> of the <strong>Customization</strong>.</li><li>Click the <strong>Customization Target</strong> property. Select the «Numbered Package» stereotype in the element Selection dialog and click <strong>OK</strong>.</li><li><p>Set the <strong>Show Properties When Not Applied</strong> property to <em>true</em>. All properties of the «Numbered Package» stereotype will be visible as properties of the <em>Package</em> metaclass, even if the stereotype is not yet applied.</p></li><li><p>Click <strong>Close</strong> when you are done.</p></li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="10_numbered_package_customization.png" /></ac:image></p><h6 style="text-align: center;">Customization element for the «Numbered Package» stereotype.</h6><h3>5. Add a numbering attribute to the customization element</h3><p>After creating the customization for the «Numbered Package» stereotype, specify the stereotype attribute for storing element numbers as well as defining a numbering scheme to use. For this, you must create a numbering attribute.</p><p><br /></p><p>To add a numbering attribute to the customization element of the «Numbered Package» stereotype</p><hr /><ol><li>Select the shape of the customization.</li><li>Add a new <strong>Auto Numbering Property</strong> named <em>Package Numbering</em>.</li><li>Open the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> of the created attribute.</li><li>Specify a value for the <strong>Numbered Property</strong> property. Click the property value cell and then click the <strong>...</strong> button. In the element Selection dialog, select the <em>No</em> property of the «Numbered Package» stereotype and click <strong>OK</strong>.</li><li>Specify a value for the<strong> Numbering Scheme</strong> property. Click the value cell and either:<br /><ul><li>Select the <em>Package Numbering Scheme</em> class in the opened list.</li><li>Click the <strong>...</strong> button. In the element Selection dialog, select the <em>Package Numbering Scheme</em> class and click <strong>OK</strong>.</li></ul></li><li>Change the <strong>Default Number</strong> property value to <em>true</em>. The <em>true</em> value indicates that this numbering attribute will be set as the default when numbering instances of the customized <em>Package </em>metaclass.</li><li>Specify the <strong>Use Prefix On Owner</strong> attribute value. The <em>true</em> value indicates that the element prefix will be used for its numbered owner as well.</li><li>Click <strong>Close</strong> when you are done.</li><li>Save and reopen the project to apply the created numbering customization.</li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="11_cust_class_with_package_numbering_prop.png" /></ac:image></p><h6 style="text-align: center;">Numbering attribute in the customization element of the «Numbered Package» stereotype.</h6><h3>6. Changing the number display mode</h3><p>To see the number before the element name, you must change the number display mode.</p><p><br /></p><p>To change the number display mode on packages</p><hr /><ol><li>Open the appropriate package diagram.</li><li>Create a package to apply the numbering scheme to.</li><li>Name the package <em>Organization</em>.</li><li>Right-click the <em>Organization</em> package and select <strong>Stereotype</strong> in the shortcut menu.</li><li>Select the «Numbered Package» stereotype and click <strong>Apply</strong>.</li><li>Right-click the shape of the package on the diagram pane. Click <strong>Symbol Properties</strong>.</li><li>Set the <strong>Show Number Tag Name</strong> property value to <em>false</em>. The <em>false</em> indicates that the element number tag name (the <em>No</em> property of the<em> «Numbered Package»</em> stereotype) will not be displayed on the package shape.</li><li>Click the <strong>Element Number Display Mode</strong> value cell to open the list of available modes. Select the <strong>Before the element name</strong> mode in this list.</li><li>Set the <strong>Show Tagged Values</strong> property value to <em>false</em>. The <em>false</em> indicates that the tagged values will not be displayed on the package shape.</li><li>Click the <strong>Show Stereotypes</strong> value cell to open the list of available modes. Select the <strong>Do Not Display</strong> mode in this list if you don't want the «Numbered Package» stereotype to be displayed on the packages.</li></ol><h3>7. Reopen the project to apply changes</h3><p>Open the appropriate package diagram and see the packages numbered using the newly created numbering customization.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="12_numbered_packages.png" /></ac:image></p><h6 style="text-align: center;">Packages numbered using a numbering customization.</h6></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="026d7b10-bc5e-42ad-bdcd-ed3573ef1a13"><ac:parameter ac:name="id">1099680386</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Creating Numbering Customizations" /></ac:link></li><li><ac:link><ri:page ri:content-title="Numbering Scheme property values" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Profile diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973593 space=UPDG version=1 -->
## PAGE 00170: Customization Element Properties

- page_id: `243973593`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973593/Customization+Element+Properties
- version_number: 1
- version_date: `2025-07-31T19:04:49.108+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data
- labels: ['attribute', 'customiztion-attribute', 'element-attribute', 'metaproperty', 'meta-property']

### NORMALIZED CONTENT

#### CONTENT-LAYER: Properties

1578480678

#### CONTENT-COLUMN: Properties

1578480680

#### CONTENT-BLOCK: Properties

1578480679

#### NOTE: Properties

Properties

There are two property meanings used in customization elements: properties specifying the element (in the[CONFLUENCE_PAGE title='Specification window' space='MDTWRT']), and properties as element attributes. The latter is described in this section.

You can create a property in the customization element, then apply the particular stereotype and create customization rules.

To create a property in the customization element

1. In a [CONFLUENCE_PAGE title='Profile diagram' space='MDTWRT'] , create a customization element.
2. Select the customization element on the diagram.
3. Click the [ATTACHMENT filename='add_property.png'] button. The menu with properties appears. [ATTACHMENT filename='Create_Element_Menu.png']
4. Select the desired property described in the following table:

| Attribute | Applied Stereotype | Description |
| --- | --- | --- |
| Place on Diagram Palette | «placeOnPaletteProperty» |  |
| Meta Property | «metaProperty» | Changes the name of the default meta property. |
| Property Group | «propertyGroup» | Creates your own groups and subgroups to group the properties either of standard UML metaclasses or stereotypes. |
| Auto Numbering Property | «AutoNumber» | Creates property used to specify numbering rules for a DSL element. |
| Derived Property Specification | «derivedPropertySpecification» | Creates a derived property that is the property whose values are calculated automatically from the other properties’ values. |

1578480677

**Related pages:**

- Creating Customization Data
- Using Customization Data

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="1a7c1127-90c2-4984-b6ba-6eed8b8ba02f"><ac:parameter ac:name="id">1578480678</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="434f6d0f-9a3a-4492-b490-ff786743570a"><ac:parameter ac:name="id">1578480680</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="88cecbd2-15ed-4f96-aa85-f8cc0f5fee6d"><ac:parameter ac:name="id">1578480679</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="128f8861-6918-45a1-9581-43bb07020d7d"><ac:parameter ac:name="title">Properties</ac:parameter><ac:rich-text-body><p><span style="color: rgb(0,0,0);">There are two property meanings used in customization elements: properties specifying the element (in the </span><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link><span style="color: rgb(0,0,0);">), and properties as element attributes. The latter is described in this section. </span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p>You can create a property in the customization element, then apply the particular stereotype and create customization rules.</p><div class="layoutArea"><ac:image ac:align="center"><ri:attachment ri:filename="customization_element_example.png" /></ac:image><div class="column"><p><br /></p><p>To create a property in the customization element</p><hr /><ol><li>In a <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Profile diagram" /><ac:plain-text-link-body><![CDATA[profile diagram]]></ac:plain-text-link-body></ac:link>, create a customization element.</li><li>Select the customization element on the diagram. </li><li>Click the <ac:image ac:thumbnail="true" ac:height="9"><ri:attachment ri:filename="add_property.png" /></ac:image> button. The menu with properties appears.<br /><br /><ac:image><ri:attachment ri:filename="Create_Element_Menu.png" /></ac:image><br /><br /></li><li>Select the desired property described in the following table:</li></ol><table class="relative-table wrapped" style="width: 89.7456%;"><colgroup><col style="width: 16.2234%;" /><col style="width: 19.3262%;" /><col style="width: 64.4504%;" /></colgroup><tbody><tr><th>Attribute</th><th>Applied Stereotype</th><th>Description</th></tr><tr><td colspan="1"><p>Place on Diagram Palette</p></td><td style="text-align: left;" colspan="1"><p>«placeOnPaletteProperty»</p></td><td colspan="1"><br /></td></tr><tr><td>Meta Property</td><td><span style="color: rgb(0,0,0);">«</span>metaProperty<span style="color: rgb(0,0,0);">» </span></td><td>Changes the name of the default meta property.</td></tr><tr><td>Property Group</td><td><p>«propertyGroup»</p></td><td><p>Creates your own groups and subgroups to group the properties either of standard UML metaclasses or stereotypes.</p></td></tr><tr><td>Auto Numbering Property</td><td><p>«AutoNumber»</p></td><td><p>Creates property used to specify numbering rules for a DSL element.</p></td></tr><tr><td>Derived Property Specification</td><td><p>«derivedPropertySpecification»</p></td><td><p>Creates a derived property that is the property whose values are calculated automatically from the other properties’ values.</p></td></tr></tbody></table></div></div></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a66104aa-7035-4e57-b192-af564a57759d"><ac:parameter ac:name="id">1578480677</ac:parameter><ac:rich-text-body><p><strong>Related pages:</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MDTWRT/Creating+Customization+Data">Creating Customization Data</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Using+Customization+Data">Using Customization Data</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973570 space=UPDG version=1 -->
## PAGE 00171: Customization Element Properties Description

- page_id: `243973570`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973570/Customization+Element+Properties+Description
- version_number: 1
- version_date: `2025-07-31T19:04:48.425+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data > Customization Elements
- labels: []

### NORMALIZED CONTENT

1680453345

1680453357

1680453347

| Property | Description |
| --- | --- |
| Customization |  |
| Name | Specifies the name of the Customization element. |
| To Do | Specifies the To Do text of the Customization element. Use the To Do property for adding notes about work to be done. Then, you can . |
| Connection Rules |  |
| Allowed Drag and Drop | Specifies elements that describe allowed . |
| Allowed Relationships | Specifies the types of relationships allowed to connect to the DSL element. For a more detailed description, see . |
| Disallowed Relationships | Specifies types of relationships not allowed to connect to the DSL element. For a more detailed description, see. |
| Types For Source | Specifies metaclasses or stereotypes allowed to connect as the source of the relationship. Types cannot conflict with UML permitted types for this relationship.The Types For Source property is intended for relationships only. The Customization Target property can either be the stereotype that extends the metaclass of the relationship, or the metaclass of the relationship itself.For a more detailed description, see . |
| Types For Target | Specifies metaclasses or stereotypes allowed to connect as targets of the relationship. Types cannot conflict with UML permitted types for this relationship. The Types For Source property is intended for relationships only. That is, the Customization Target property can either be the stereotype that extends the metaclass of the relationship, or the metaclass of the relationship itself.For a more detailed description, see . |
| Content |  |
|  | Stores a rule (in a form of derived property expression) for gathering the additional content of the DSL element. |
|  | Specifies whether the content of the DSL element includes only directly related elements or both directly and indirectly related ones. |
| General |  |
|  | Specifies a stereotype or a metaclass to customize. See a case study in . |
|  | Excludes customized elements from being suggested as a type in the list dialogs. |
|  | Indicates whether the DSL element will be recognized as a new type. |
|  | Specifies a preferred metatype, if there is more than one defined in the Customization Specification window. For more information, see . |
| Quick Applying For | Specifies an element to which the created customization can be applied directly from the element shortcut menu. For more information, see . |
|  | Specifies whether or not the name auto completion list is displayed when entering name for the DSL element on the diagram. If the Do Not Suggest Name Auto Completion property value is true, then the auto completion drop-down list is not displayed. |
| Model Initialization | Specifies stereotypes that can be automatically applied to elements (source or target) after connecting those elements with customized relationships. The condition is that the customization target must be a stereotype for relationship. For more information, see . |
| Apply to Source | Specifies stereotypes that will be applied on the source element of the relationship after connection.The customization target should be a stereotype of relationship.For more information, see . |
| Apply to Target | Specifies stereotypes that will be applied to the target element of the relationship after connection.The customization target should be a stereotype of relationship.For more information, see . |
| Super Types | Specifies the element that will be the super type of the DSL element. The generalization relationship will be created from the DSL element to the specified super type.For more information, see Required Generalization or . |
| Naming |  |
| Category | Creates a category to group DSL elements in various shortcut menus, if the Hide Metatype property is true. For more information, see . |
| Keyword | Defines a keyword to be displayed instead of the applied stereotype name. |
| Representation Text | Defines the text that will be used in status bars, dialogs, logs, and others. See an example of the Representation Text property usage in . |
|  | Specifies a short name for the DSL element. When creating the DSL element, the short name will be added automatically. |
| Owned Elements |  |
| Hidden Owned Diagrams | Specifies the diagram types that will hidden for the DSL element. For example, if the property value is Any Diagram, all diagrams will be hidden and unavailable from the DSL element shortcut menu, under the Create Diagram command in the Model Browser. For more information, see . |
| Hidden Owned Types | Specifies the metaclass or the stereotype that will be hidden for the DSL element. For example, if the property value is the Element metaclass, then all standard UML elements will be hidden in the DSL element shortcut menu, under the Create Element command in the Model Browser. For more information, see . |
| Possible Owners | Specifies the metaclass or stereotype that can own the DSL element (specifies types of elements that can be owners of the DSL element). For example, to create a DSL element inside standard packages in the Model Browser, you must specify the Package metaclass as the Possible Owners property value. For more information, see an example in and for a more detailed description, see . |
| Suggested Owned Diagrams | Specifies types of diagrams that will appear in the DSL element shortcut menu when creating possible inner diagrams. For more information, see . |
| Suggested Owned Types | Specifies types of elements that can be owned by the DSL element. For example, if the property value is Section, then the Section elements can be owned by the customized element. For more information, see . |
| Properties |  |
| Check Spelling | Specifies the properties for which the spell checker is enabled. |
| Help ID | Defines a string value referring to , which can be opened for the DSL element. |
| In Shortcut Menu | Specifies properties that will be displayed in the DSL element shortcut menu. For more information, see . |
| Multi Line Text Properties | Specifies properties for which multi line text editor will be used. Note only properties of string type is listed in editor of this property. For more information about creating properties in the DSL element Specification window, see For more information about editing property values in the Specification window, see the . |
| Show Properties When Not Applied | Customizes the stereotype properties to be visible in the element Specification window even if the stereotype is not yet applied on the element. For more information, see . |
| Show Properties When Not Applied Limited By Element Type | Customize the stereotype properties to be visible in the DSL element Specification window dependent on another stereotype or metaclass. For more information, see . |
| Show Properties When Not Applied Limited By Profile Application | Customize the stereotype properties to be visible in the DSL element Specification window dependent on the corresponding profile application. For more information, see . |
|  | Specifies properties visibility mode in DSL element Specification window. |
| Used UML Properties | Allows to select UML element properties that will be visible in DSL element Specification window. For more information, see . |
| Symbol |  |
| Default Shape Size | Defines default size of the shape when the symbol is created on a diagram. For more information, see |
|  | Specifies properties visibility mode in DSL element , in the symbol shortcut menu and in menus that open after clicking the Compartments or Create Element smart manipulators. |
|  | Allows to select the specific properties to be displayed in compartments on shapes. |

1680453342

**Related pages**

- Specification window

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9f995455-d35c-4419-8a87-7c603fba3dec"><ac:parameter ac:name="id">1680453345</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="6548ea3e-16a4-416b-9fec-ebadca9dada6"><ac:parameter ac:name="id">1680453357</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="78c3a140-8ea9-47be-985d-7eb3f623cec3"><ac:parameter ac:name="id">1680453347</ac:parameter><ac:rich-text-body><table class="relative-table wrapped"><colgroup> <col style="width: 340.0px;" /> <col style="width: 917.0px;" /> </colgroup><tbody><tr><th style="text-align: center;"><span style="color: rgb(0,0,0);">Property</span></th><th class="highlight-grey" style="text-align: left;" title="Background colour : Grey" data-highlight-colour="grey"><span style="color: rgb(0,0,0);" title="">Description</span></th></tr><tr><td class="highlight-grey" title="Background colour : Grey" colspan="2" data-highlight-colour="grey">Customization</td></tr><tr><td>Name</td><td><div class="layoutArea"><div class="column"><p>Specifies the name of the Customization element.</p></div></div></td></tr><tr><td>To Do</td><td>Specifies the To Do text of the Customization element. Use the To Do property for adding notes about work to be done. Then, you can <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Find TODO" /><ac:plain-text-link-body><![CDATA[quickly search for the elements that have the To Do properties defined]]></ac:plain-text-link-body></ac:link>.</td></tr><tr><td class="highlight-grey" title="Background colour : Grey" colspan="2" data-highlight-colour="grey">Connection Rules</td></tr><tr><td colspan="1">Allowed Drag and Drop</td><td colspan="1"><p>Specifies elements that describe allowed <ac:link><ri:page ri:content-title="Customizing Drag-and-Drop" /><ac:plain-text-link-body><![CDATA[drag-and-drop operations for customized elements]]></ac:plain-text-link-body></ac:link>.</p></td></tr><tr><td colspan="1"><p>Allowed Relationships</p></td><td colspan="1"><p>Specifies the types of relationships allowed to connect to the DSL element. For a more detailed description, see <ac:link><ri:page ri:content-title="Creating Custom Rules for Relationships" /><ac:plain-text-link-body><![CDATA[Creating Custom Rules for Relationships ]]></ac:plain-text-link-body></ac:link>.</p></td></tr><tr><td colspan="1">Disallowed Relationships</td><td colspan="1"><p>Specifies types of relationships not allowed to connect to the DSL element. For a more detailed description, see<ac:link><ri:page ri:content-title="Creating Custom Rules for Relationships" /><ac:plain-text-link-body><![CDATA[ Creating Custom Rules for Relationships ]]></ac:plain-text-link-body></ac:link>.</p></td></tr><tr><td colspan="1">Types For Source</td><td colspan="1"><div class="content-wrapper"><p>Specifies metaclasses or stereotypes allowed to connect as the source of the relationship. Types cannot conflict with UML permitted types for this relationship.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0cc334eb-166a-4106-937c-1a9e338e5bf7"><ac:rich-text-body><p>The Types For Source property is intended for relationships only. The Customization Target property can either be the stereotype that extends the metaclass of the relationship, or the metaclass of the relationship itself.</p></ac:rich-text-body></ac:structured-macro><p>For a more detailed description, see <ac:link><ri:page ri:content-title="Creating Custom Rules for Relationships" /><ac:plain-text-link-body><![CDATA[Creating Custom Rules for Relationships ]]></ac:plain-text-link-body></ac:link>.</p></div></td></tr><tr><td colspan="1">Types For Target</td><td colspan="1"><div class="content-wrapper"><p>Specifies metaclasses or stereotypes allowed to connect as targets of the relationship. Types cannot conflict with UML permitted types for this relationship. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4dcf57cb-3333-4ca1-9094-e301afc10f13"><ac:rich-text-body><p>The Types For Source property is intended for relationships only. That is, the Customization Target property can either be the stereotype that extends the metaclass of the relationship, or the metaclass of the relationship itself.</p></ac:rich-text-body></ac:structured-macro><p>For a more detailed description, see <ac:link><ri:page ri:content-title="Creating Custom Rules for Relationships" /><ac:plain-text-link-body><![CDATA[Creating Custom Rules for Relationships ]]></ac:plain-text-link-body></ac:link>. </p></div></td></tr><tr><td class="highlight-grey" title="Background colour : Grey" colspan="2" data-highlight-colour="grey"><div class="layoutArea" title=""><div class="column"><p>Content</p></div></div></td></tr><tr><td colspan="1"><ac:link><ri:page ri:content-title="Additional Content" /></ac:link></td><td colspan="1"><div class="layoutArea"><div class="column"><p>Stores a rule (in a form of derived property expression) for gathering the additional content of the DSL element.</p></div></div></td></tr><tr><td colspan="1"><ac:link><ri:page ri:content-title="Sub Element Contents Included" /></ac:link></td><td colspan="1">Specifies whether the content of the DSL element includes only directly related elements or both directly and indirectly related ones. </td></tr><tr><td class="highlight-grey" title="Background colour : Grey" colspan="2" data-highlight-colour="grey">General</td></tr><tr><td colspan="1"><ac:link><ri:page ri:content-title="Customization Target" /></ac:link></td><td colspan="1"><p>Specifies a stereotype or a metaclass to customize. See a case study in <ac:link><ri:page ri:content-title="Creating your First Customization" /><ac:plain-text-link-body><![CDATA[Creating your First Customization ]]></ac:plain-text-link-body></ac:link>.</p></td></tr><tr><td colspan="1"><ac:link><ri:page ri:content-title="Do Not Suggest As Type" /><ac:plain-text-link-body><![CDATA[Do No Suggest As Type ]]></ac:plain-text-link-body></ac:link></td><td colspan="1">Excludes customized elements from being suggested as a type in the list dialogs.</td></tr><tr><td colspan="1"><ac:link><ri:page ri:content-title="Hide Metatype" /></ac:link></td><td colspan="1">Indicates whether the DSL element will be recognized as a new type.</td></tr><tr><td colspan="1"><ac:link><ri:page ri:content-title="Defining Preferred Metatype" /><ac:plain-text-link-body><![CDATA[Preferred Metatype]]></ac:plain-text-link-body></ac:link></td><td colspan="1"><p>Specifies a preferred metatype, if there is more than one <ac:link><ri:page ri:content-title="Customization Target" /><ac:plain-text-link-body><![CDATA[Customization Target ]]></ac:plain-text-link-body></ac:link> defined in the Customization Specification window. For more information, see <ac:link><ri:page ri:content-title="Creating Property Groups and Subgroups" /><ac:plain-text-link-body><![CDATA[Creating Property Groups and Subgroups ]]></ac:plain-text-link-body></ac:link>. </p></td></tr><tr><td colspan="1">Quick Applying For</td><td colspan="1"><p>Specifies an element to which the created customization can be applied directly from the element shortcut menu. </p><p>For more information, see <ac:link><ri:page ri:content-title="Rules of Stereotypes that cannot be Allowed to Apply" /><ac:plain-text-link-body><![CDATA[Rules of Stereotypes that cannot be Allowed to Apply ]]></ac:plain-text-link-body></ac:link>.</p></td></tr><tr><td colspan="1"><ac:link><ri:page ri:content-title="Customization Target" /></ac:link></td><td colspan="1"><p>Specifies whether or not the name auto completion list is displayed when entering name for the DSL element on the diagram. If the Do Not Suggest Name Auto Completion property value is true, then the auto completion drop-down list is not displayed. </p></td></tr><tr><td><div class="layoutArea"><div class="column"><p>Model Initialization</p></div></div></td><td><div class="layoutArea"><div class="column"><p>Specifies stereotypes that can be automatically applied to elements (source or target) after connecting those elements with customized relationships. The condition is that the customization target must be a stereotype for relationship. For more information, see <ac:link><ri:page ri:content-title="Initializing a Custom Model" /><ac:plain-text-link-body><![CDATA[Initializing Custom Model ]]></ac:plain-text-link-body></ac:link>.</p></div></div></td></tr><tr><td colspan="1">Apply to Source</td><td colspan="1"><div class="content-wrapper"><div class="layoutArea"><div class="column"><p>Specifies stereotypes that will be applied on the source element of the relationship after connection.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9cb0e012-2d54-458b-812b-4af7874a28d4"><ac:rich-text-body><p>The customization target should be a stereotype of relationship.</p></ac:rich-text-body></ac:structured-macro><p>For more information, see <ac:link><ri:page ri:content-title="Initializing a Custom Model" /><ac:plain-text-link-body><![CDATA[Initializing Custom Model ]]></ac:plain-text-link-body></ac:link>.</p></div></div></div></td></tr><tr><td colspan="1">Apply to Target</td><td colspan="1"><div class="content-wrapper"><p>Specifies stereotypes that will be applied to the target element of the relationship after connection.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="14ab25ec-25b4-493d-bc5d-30d681257e32"><ac:rich-text-body><p>The customization target should be a stereotype of relationship.</p></ac:rich-text-body></ac:structured-macro><p>For more information, see <ac:link><ri:page ri:content-title="Initializing a Custom Model" /><ac:plain-text-link-body><![CDATA[Initializing Custom Model ]]></ac:plain-text-link-body></ac:link>.</p></div></td></tr><tr><td colspan="1">Super Types</td><td colspan="1"><p>Specifies the element that will be the super type of the DSL element. The generalization relationship will be created from the DSL element to the specified super type.</p><p>For more information, see Required Generalization or <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Interface realization" /></ac:link>.</p></td></tr><tr><td class="highlight-grey" title="Background colour : Grey" colspan="2" data-highlight-colour="grey">Naming</td></tr><tr><td colspan="1"><p>Category</p></td><td colspan="1"><p>Creates a category to group DSL elements in various shortcut menus, if the Hide Metatype property is true. For more information, see <ac:link><ri:page ri:content-title="Creating a DSL Element from the Customized Category in the Shortcut Menu" /></ac:link>.</p></td></tr><tr><td colspan="1">Keyword</td><td colspan="1">Defines a keyword to be displayed instead of the applied stereotype name.</td></tr><tr><td colspan="1">Representation Text</td><td colspan="1"><p>Defines the text that will be used in status bars, dialogs, logs, and others. See an example of the Representation Text property usage in <ac:link><ri:page ri:content-title="Customizing Drag-and-Drop" /><ac:plain-text-link-body><![CDATA[a drag-and-drop operation customization]]></ac:plain-text-link-body></ac:link>.</p></td></tr><tr><td colspan="1"><ac:link><ri:page ri:content-title="Do Not Suggest Name Auto Completion" /><ac:plain-text-link-body><![CDATA[Do Not Suggest Name Auto Completion ]]></ac:plain-text-link-body></ac:link></td><td colspan="1">Specifies a short name for the DSL element. When creating the DSL element, the short name will be added automatically. </td></tr><tr><td class="highlight-grey" title="Background colour : Grey" colspan="2" data-highlight-colour="grey">Owned Elements</td></tr><tr><td colspan="1">Hidden Owned Diagrams</td><td colspan="1"><div class="layoutArea"><div class="column"><p>Specifies the diagram types that will hidden for the DSL element. For example, if the property value is Any Diagram, all diagrams will be hidden and unavailable from the DSL element shortcut menu, under the Create Diagram command in the Model Browser. For more information, see <ac:link><ri:page ri:content-title="Customizing Possible Owned Elements" /><ac:plain-text-link-body><![CDATA[Customizing Possible Owned Elements ]]></ac:plain-text-link-body></ac:link>.</p></div></div></td></tr><tr><td colspan="1">Hidden Owned Types</td><td colspan="1"><div class="layoutArea"><div class="column"><p>Specifies the metaclass or the stereotype that will be hidden for the DSL element. For example, if the property value is the Element metaclass, then all standard UML elements will be hidden in the DSL element shortcut menu, under the Create Element command in the Model Browser. For more information, see <ac:link><ri:page ri:content-title="Customizing Possible Owned Elements" /></ac:link> .</p></div></div></td></tr><tr><td colspan="1">Possible Owners</td><td colspan="1"><div class="layoutArea"><div class="column"><p>Specifies the metaclass or stereotype that can own the DSL element (specifies types of elements that can be owners of the DSL element). For example, to create a DSL element inside standard packages in the Model Browser, you must specify the Package metaclass as the Possible Owners property value. For more information, see an example in <ac:link><ri:page ri:content-title="Creating your First Customization" /><ac:plain-text-link-body><![CDATA[Creating Your First Customization]]></ac:plain-text-link-body></ac:link> and for a more detailed description, see <ac:link><ri:page ri:content-title="Customizing Possible Owned Elements" /></ac:link> .</p></div></div></td></tr><tr><td colspan="1">Suggested Owned Diagrams</td><td colspan="1"><div class="layoutArea"><div class="column"><p>Specifies types of diagrams that will appear in the DSL element shortcut menu when creating possible inner diagrams. For more information, see <ac:link><ri:page ri:content-title="Customizing Possible Owned Elements" /></ac:link>.  </p></div></div></td></tr><tr><td colspan="1">Suggested Owned Types</td><td colspan="1"><div class="layoutArea"><div class="column"><p>Specifies types of elements that can be owned by the DSL element. For example, if the property value is Section, then the Section elements can be owned by the customized element. For more information, see <ac:link><ri:page ri:content-title="Customizing Possible Owned Elements" /></ac:link>.</p></div></div></td></tr><tr><td class="highlight-grey" title="Background colour : Grey" colspan="2" data-highlight-colour="grey">Properties</td></tr><tr><td colspan="1">Check Spelling</td><td colspan="1"><div class="layoutArea"><div class="column"><p>Specifies the properties for which the spell checker is enabled. </p></div></div></td></tr><tr><td colspan="1">Help ID</td><td colspan="1"><div class="layoutArea"><div class="column"><p>Defines a string value referring to <ac:link><ri:page ri:content-title="Creating Element - Specific Help Topics" /><ac:plain-text-link-body><![CDATA[an element-specific help topic]]></ac:plain-text-link-body></ac:link>, which can be opened for the DSL element.</p></div></div></td></tr><tr><td colspan="1">In Shortcut Menu</td><td colspan="1"><div class="layoutArea"><div class="column"><p>Specifies properties that will be displayed in the DSL element shortcut menu. For more information, see <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Properties" /><ac:plain-text-link-body><![CDATA[Quick property editor]]></ac:plain-text-link-body></ac:link> . </p></div></div></td></tr><tr><td colspan="1">Multi Line Text Properties</td><td colspan="1"><div class="layoutArea"><div class="column"><p>Specifies properties for which multi line text editor will be used. Note only properties of string type is listed in editor of this property. For more information about creating properties in the DSL element Specification window, see <ac:link><ri:page ri:content-title="Customizing Specification Window" /><ac:plain-text-link-body><![CDATA[Customizing Specification Window.]]></ac:plain-text-link-body></ac:link> For more information about editing property values in the Specification window, see the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Editing property values" /><ac:plain-text-link-body><![CDATA[Editing Property Values]]></ac:plain-text-link-body></ac:link>.</p></div></div></td></tr><tr><td colspan="1">Show Properties When Not Applied</td><td colspan="1"><div class="content-wrapper"><div class="layoutArea"><div class="column"><p>Customizes the stereotype properties to be visible in the element Specification window even if the stereotype is not yet applied on the element. For more information, see <ac:link><ri:page ri:content-title="Always Visible Properties" /></ac:link> .</p></div></div></div></td></tr><tr><td colspan="1"><div class="layoutArea"><div class="column"><p>Show Properties When Not Applied Limited By Element Type </p></div></div></td><td colspan="1"><div class="layoutArea"><div class="column"><p>Customize the stereotype properties to be visible in the DSL element Specification window dependent on another stereotype or metaclass. For more information, see <ac:link><ri:page ri:content-title="Always Visible Properties" /></ac:link> .</p></div></div></td></tr><tr><td colspan="1"><div class="layoutArea"><div class="column"><p>Show Properties When Not Applied Limited By Profile Application </p></div></div></td><td colspan="1"><div class="layoutArea"><div class="column"><p>Customize the stereotype properties to be visible in the DSL element Specification window dependent on the corresponding profile application. For more information, see <ac:link><ri:page ri:content-title="Always Visible Properties" /></ac:link> .</p></div></div></td></tr><tr><td colspan="1"><div class="layoutArea"><div class="column"><p><ac:link><ri:page ri:content-title="Standard Expert Configuration" /><ac:plain-text-link-body><![CDATA[Standard Expert Configuration  ]]></ac:plain-text-link-body></ac:link></p></div></div></td><td colspan="1"><div class="layoutArea"><div class="column"><p>Specifies properties visibility mode in DSL element Specification window. </p></div></div></td></tr><tr><td colspan="1"><div class="layoutArea"><div class="column"><p>Used UML Properties </p></div></div></td><td colspan="1"><div class="layoutArea"><div class="column"><p>Allows to select UML element properties that will be visible in DSL element Specification window. For more information, see <ac:link><ri:page ri:content-title="Using Standard UML Properties" /></ac:link>.</p></div></div></td></tr><tr><td class="highlight-grey" title="Background colour : Grey" colspan="2" data-highlight-colour="grey"><div class="layoutArea" title=""><div class="column"><p>Symbol</p></div></div></td></tr><tr><td colspan="1"><div class="layoutArea"><div class="column"><p>Default Shape Size</p></div></div></td><td colspan="1"><div class="layoutArea"><div class="column"><p>Defines default size of the shape when the symbol is created on a diagram. For more information, see <ac:link><ri:page ri:content-title="Customizing Symbols" /><ac:plain-text-link-body><![CDATA[Setting default symbol size]]></ac:plain-text-link-body></ac:link></p></div></div></td></tr><tr><td colspan="1"><div class="layoutArea"><div class="column"><p><ac:link><ri:page ri:content-title="Symbol Standard Expert Configuration" /><ac:plain-text-link-body><![CDATA[Symbol Standard Expert Configuration  ]]></ac:plain-text-link-body></ac:link></p></div></div></td><td colspan="1"><div class="layoutArea"><div class="column"><p>Specifies properties visibility mode in DSL element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Symbol Properties dialog" /></ac:link>, in the symbol shortcut menu and in menus that open after clicking the Compartments or Create Element smart manipulators. </p></div></div></td></tr><tr><td colspan="1"><ac:link><ri:page ri:content-title="Properties Displayed in Compartments" /></ac:link></td><td colspan="1">Allows to select the specific properties to be displayed in compartments on shapes.</td></tr></tbody></table></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e29f2436-ef6d-4bb9-8a2a-9c4d46e96038"><ac:parameter ac:name="id">1680453342</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><a href="https://docs.nomagic.com/display/MDTWRT/Specification+window">Specification window</a></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973567 space=UPDG version=1 -->
## PAGE 00172: Customization Elements

- page_id: `243973567`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973567/Customization+Elements
- version_number: 1
- version_date: `2025-07-31T19:04:48.380+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data
- labels: []

### NORMALIZED CONTENT

Use the customization element properties to customize:

- the DSL element [CONFLUENCE_PAGE title='Specification window' space='MDTWRT']
- the DSL element shortcut menu
- allowed to draw relationships
- allowed to drag-and-drop elements
- other

To specify a new property

1. In a [CONFLUENCE_PAGE title='Profile diagram' space='MDTWRT'], create a customization element.
2. Open the **Customization** element Specification window.
3. In the right side of the window, select a property and modify it depending on its type.

#### INFO: Tip!

Tip!

The properties in the **Customization** Specification window are listed in the following two locations:

1. General specification pane
2. **Tags**property group

Specify properties in either location. Changes made in the general specification pane reflect in the **Tags**property group and vice versa.

###### [IMAGE alt='' src='']Customization element Specification window, list of properties

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Customization Element Properties Description' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><span style="color: rgb(0,0,0);">Use the customization element properties to customize:</span></p><ul><li><span style="color: rgb(0,0,0);">the DSL element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> </span></li><li><span style="color: rgb(0,0,0);">the DSL element shortcut menu </span></li><li><span style="color: rgb(0,0,0);">allowed to draw relationships</span></li><li><span style="color: rgb(0,0,0);">allowed to drag-and-drop elements</span></li><li><span style="color: rgb(0,0,0);">other</span></li></ul><p><br /></p><div class="layoutArea"><p>To specify a new property</p><hr /><ol><li><p>In a <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Profile diagram" /><ac:plain-text-link-body><![CDATA[profile diagram]]></ac:plain-text-link-body></ac:link>, create a customization element. </p></li><li><p>Open the <strong>Customization</strong> element Specification window. </p></li><li><p>In the right side of the window, select a property and modify it depending on its type.</p></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="43e2980e-508a-471b-965b-a21d85c78922"><ac:parameter ac:name="title">Tip!</ac:parameter><ac:rich-text-body><div class="column"><p><span style="color: rgb(0,0,0);">The properties in the <strong>Customization</strong> Specification window are listed in the following two locations: </span></p><ol><li><p><span style="color: rgb(0,0,0);">General specification pane </span></p></li><li><p><span style="color: rgb(0,0,0);"> <strong>Tags </strong>property group </span></p></li></ol><p><span style="color: rgb(0,0,0);">Specify properties in either location. Changes made in the general specification pane reflect in the <strong>Tags </strong>property group and vice versa.</span></p></div></ac:rich-text-body></ac:structured-macro><h6 class="auto-cursor-target" style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="Customization_element.png" /></ac:image>Customization element Specification window, list of properties</h6></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ad4120b1-8402-401a-a26b-e43b8756cb34"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Customization Element Properties Description" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973571 space=UPDG version=1 -->
## PAGE 00173: Customization Target

- page_id: `243973571`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973571/Customization+Target
- version_number: 1
- version_date: `2025-07-31T19:04:48.486+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data > Customization Elements
- labels: []

### NORMALIZED CONTENT

The **Customization Target** property isa mandatory property in customization creation. It specifies the stereotype or metaclass you want to customize.

To define a stereotype as a customization target

1. In the Customization [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] , click the Customization Target property.
2. In the property specification cell, click the [IMAGE alt='' src='']button. The element [CONFLUENCE_PAGE title='Selecting elements' space='MDTWRT'] appears.
3. Select the stereotype.
4. Click OK to close the dialog.
5. Click Close .
6. Apply the selected stereotype to the desired class.
7. Reopen the project.

To define a metaclass as a customization target

1. In the Customization Specification window, click the Customization Target property.
2. In the property specification cell, click the [IMAGE alt='' src='']button. The element [CONFLUENCE_PAGE title='Selecting elements' space='MDTWRT'] appears.
3. Clear the **Apply Filter** selection. All metaclasses will be included in the list.
4. Select the*Class*metaclass. TipAll standard metaclasses are stored in the UML Metamodel. You can also [CONFLUENCE_PAGE title='Filtering' space='MDTWRT'] to find a desired element quicker.
5. Click OK to close the dialog.
6. Click Close .
7. Reopen the project.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Customization Elements' space='']
- [CONFLUENCE_PAGE title='Creating your First Customization' space='']
- [CONFLUENCE_PAGE title='Creating and specifying derived properties' space='']
- [CONFLUENCE_PAGE title='Defining expressions' space='']
- [CONFLUENCE_PAGE title='Hide Metatype' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><span>The </span> <strong>Customization Target </strong> <span>property is </span>a mandatory property in customization creation.  It specifies the stereotype or metaclass you want to customize.</p><div class="layoutArea"><div class="column"><p><br /></p><div class="layoutArea"><div class="column"><p><span>To define a stereotype as a customization target</span></p><hr /><ol><li><span>In the </span> <strong>Customization </strong> <span><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link></span><span>, click the </span> <strong>Customization Target </strong> <span>property. </span></li><li><span>In the property specification cell, click the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="edit.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image>button. The element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Selecting elements" /><ac:plain-text-link-body><![CDATA[Selection dialog]]></ac:plain-text-link-body></ac:link> appears. </span></li><li><span>Select the </span>stereotype.</li><li><span>Click </span> <strong>OK </strong>to close the dialog.</li><li><span>Click </span> <strong>Close</strong><span>. </span></li><li><span>Apply the selected</span><em> </em><span>stereotype to the desired</span><em> </em><span>class.</span></li><li><span>Reopen the project. </span></li></ol><p><span> <br /> </span></p><p><span>To define a metaclass as a customization target</span></p><hr /><ol><li><span>In the </span><strong>Customization </strong><span>Specification window, click the </span><strong>Customization Target </strong><span>property.</span></li><li><span>In the property specification cell, click the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="edit.png" /></ac:image>button. The element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Selecting elements" /><ac:plain-text-link-body><![CDATA[Selection dialog]]></ac:plain-text-link-body></ac:link> appears.  </span></li><li><span>Clear the <strong>Apply Filter</strong> selection. All metaclasses will be included in the list.</span></li><li><p class="auto-cursor-target"><span>Select the </span><em>Class </em><span>metaclass.</span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="7b20faa5-528a-4e4e-8bd3-2e9487d8c5c9"><ac:parameter ac:name="title">Tip</ac:parameter><ac:rich-text-body><p>All standard metaclasses are stored in the UML Metamodel. You can also <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Filtering" /><ac:plain-text-link-body><![CDATA[filter elements]]></ac:plain-text-link-body></ac:link> to find a desired element quicker.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span><br /></span></p></li><li>Click <strong>OK</strong> to close the dialog. </li><li>Click <strong>Close</strong>. </li><li>Reopen the project. </li></ol><p><br /></p><p><br /></p></div></div></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="68d6f843-19aa-480d-81e1-df3547d11a1b"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Elements" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating your First Customization" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating and specifying derived properties" /></ac:link></li><li><ac:link><ri:page ri:content-title="Defining expressions" /></ac:link></li><li><ac:link><ri:page ri:content-title="Hide Metatype" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973538 space=UPDG version=1 -->
## PAGE 00174: Customizing diagram palette

- page_id: `243973538`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973538/Customizing+diagram+palette
- version_number: 1
- version_date: `2025-07-31T19:04:47.790+02:00`
- ancestors: UML Profiling and DSL Guide > Customizing diagrams
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: How can I create the attribute?

1687475344

#### CONTENT-COLUMN: How can I create the attribute?

1687475346

#### CONTENT-BLOCK: How can I create the attribute?

1687475345

You can simply add the appropriate button to the palette of any desired diagram type for a new DSL element type. To do this, you must make certain changes in the customization profile.

To add the button for creating a DSL element on the palette of a relevant diagram type

1. Create a Profile diagram or open an existing one.
2. Create a customization.
3. Set the DSL element type as the customization target. How can I simply set the customization target?Drag the DSL element type to the shape of the newly created customization element.
4. Create the **Place on Diagram Palette** attribute for the customization. How can I create the attribute?Open the Specification window of the customization element.Select **Attributes** on the left side of the window.Click the **Create** button and select **Place on Diagram Palette** (see the following figure).Type the new attribute name (this is optional, since the name is not visible anywhere in UI, except the attribute Specification window).[IMAGE alt='' src='']
5. In the Specification window of the Place on Diagram Palette attribute, select the cell of the Place property value, and click [ATTACHMENT filename='edit_button.png'] .
6. In the open dialog, select the diagram type of the palette to customize.
7. In the same dialog, use the Up and Down buttons to change the position of the new button on the palette.
8. If you want to add several new buttons and organize them into a group on the palette, create a new Group package by clicking the **Create Group** button (shown below, on the left). The button of the DSL element type appears under the Group package (see the screenshot on the right). 
 
[IMAGE alt='' src=''] If you want to undo the group creation, simply click the **Up** or **Down** button.
9. Close the dialogs and save the changes.
10. Reopen the diagram with the customized palette.

As a result, you can see the new button on the diagram palette. If you work in a [CONFLUENCE_PAGE title='Collaborative modeling' space='MDTWRT'], other users who work with the same project or projects using the same customization profile can see the new button instantly after updating their projects.

If you repeat the procedure to add more buttons within the same group on the diagram palette, you can see the appropriate changes (shown in the following figure).

[IMAGE alt='' src='']

1687475336

**Related pages**

- Customizing diagrams

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="baf4cf70-36ec-46b3-ad71-deb71bb25c1f"><ac:parameter ac:name="id">1687475344</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="741d6073-6c89-4180-abd7-b1ebff2474bb"><ac:parameter ac:name="id">1687475346</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="06fdc95b-5683-42f1-b17e-64cdb0414a32"><ac:parameter ac:name="id">1687475345</ac:parameter><ac:rich-text-body><p>You can simply add the appropriate button to the palette of any desired diagram type for a new DSL element type. To do this, you must make certain changes in the customization profile.</p><p><br /></p><p>To add the button for creating a DSL element on the palette of a relevant diagram type</p><hr /><ol><li>Create a Profile diagram or open an existing one.</li><li>Create a customization.</li><li><p>Set the DSL element type as the customization target.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="deee960e-7666-4c61-a6e5-5b01c087b006"><ac:parameter ac:name="title">How can I simply set the customization target?</ac:parameter><ac:rich-text-body><p><span>Drag the DSL element type to the shape of the newly created customization element.</span></p></ac:rich-text-body></ac:structured-macro></li><li><p>Create the <strong>Place on Diagram Palette</strong> attribute for the customization.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c0421bda-95c3-4044-a45b-a8e8551b5f73"><ac:parameter ac:name="title">How can I create the attribute?</ac:parameter><ac:rich-text-body><ol><li>Open the Specification window of the customization element.</li><li>Select <strong>Attributes</strong> on the left side of the window.</li><li>Click the <strong>Create</strong> button and select <strong>Place on Diagram Palette</strong> (see the following figure).</li><li>Type the new attribute name (this is optional, since the name is not visible anywhere in UI, except the attribute Specification window).</li></ol><p><ac:image><ri:attachment ri:filename="specification_of_customization2.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro></li><li>In the Specification window of the <strong>Place on Diagram Palette</strong> attribute, select the cell of the <strong>Place</strong> property value, and click <ac:image><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image>.</li><li>In the open dialog, select the diagram type of the palette to customize.</li><li>In the same dialog, use the <strong>Up</strong> and <strong>Down</strong> buttons to change the position of the new button on the palette.</li><li><p>If you want to add several new buttons and organize them into a group on the palette, create a new Group package by clicking the <strong>Create Group</strong> button (shown below, on the left). The button of the DSL element type appears under the Group package (see the screenshot on the right).<br /><br /><ac:image><ri:attachment ri:filename="diagram_palette.png" /></ac:image></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d49964b1-c726-4cc7-b628-bdd6a4766173"><ac:rich-text-body><p>If you want to undo the group creation, simply click the <strong>Up</strong> or <strong>Down</strong> button.</p></ac:rich-text-body></ac:structured-macro></li><li>Close the dialogs and save the changes.</li><li>Reopen the diagram with the customized palette.</li></ol><p>As a result, you can see the new button on the diagram palette. If you work in a <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Collaborative modeling" /><ac:plain-text-link-body><![CDATA[collaborative environment]]></ac:plain-text-link-body></ac:link>, other users who work with the same project or projects using the same customization profile can see the new button instantly after updating their projects.</p><p>If you repeat the procedure to add more buttons within the same group on the diagram palette, you can see the appropriate changes (shown in the following figure).</p><p><br /></p><p style="margin-left: 30.0px;"><ac:image><ri:attachment ri:filename="More_buttons.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0b71fdd5-d427-4088-945a-a32e7c8430ec"><ac:parameter ac:name="id">1687475336</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MDTWRT/Customizing+diagrams">Customizing diagrams</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973509 space=UPDG version=1 -->
## PAGE 00175: Customizing diagrams

- page_id: `243973509`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973509/Customizing+diagrams
- version_number: 1
- version_date: `2025-07-31T19:04:47.467+02:00`
- ancestors: UML Profiling and DSL Guide
- labels: ['customizing-diagram', 'diagram-customization', 'customize-diagram-wizard']

### NORMALIZED CONTENT

168915473

168915475

168915474

You can create your own diagram types for specific domains, platforms, technology, or other purposes using the **Customize Diagram Wizard**. This powerful engine enables the creation of custom elements in the diagram toolbar, custom symbol styles, and other customizations.

To open the **Customize Diagrams** dialog

- On the main menu, click Diagrams > Customize .

You can change the properties of existing diagrams (**Edit** function) or create your own brand new diagram type (**Create** function). Diagram customization descriptors are saved in a separate file for every diagram, so you are able to exchange these customizations with your partners or colleagues (use **Import** or **Export** function). 
 
The **Reset to default** button in the **Customize Diagrams** dialog restores the default configuration for diagrams bundled with the installation. It does not work with user-defined diagrams.

To open the **Customize Diagram Wizard**

Do either:

- In the Customize Diagrams dialog, select a diagram type and click Edit . [ATTACHMENT filename='customize_diagrams_dialog.png']

- Click Create and then select one of the following commands:
- Diagram with Symbols Type , if you need to create a new diagram type.
- Relation Map Type , if you need to create a new relation map diagram.
- Dependency Matrix Type , if you need to create a new matrix type.
- Generic Table Type , if you need to create a new generic table diagram.
- Create from Existing Diagram , if you need to create custom diagrams from existing ones.

[IMAGE alt='' src='']

168915472

**Related pages**

- Creating new diagram type
- Creating new dependency matrix type
- Customizing diagram palette

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="6a50e9e5-bda9-46ab-8dc5-024964aeac98"><ac:parameter ac:name="id">168915473</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ea8dfe4a-1139-4807-a955-9d2c32c4209a"><ac:parameter ac:name="id">168915475</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c28ece29-1e05-4dd5-af50-11d27eb83fc3"><ac:parameter ac:name="id">168915474</ac:parameter><ac:rich-text-body><p>You can create your own diagram types for specific domains, platforms, technology, or other purposes using the <strong>Customize Diagram Wizard</strong>. This powerful engine enables the creation of custom elements in the diagram toolbar, custom symbol styles, and other customizations.<br class="atl-forced-newline" /><span> </span></p><p>To open the <strong>Customize Diagrams</strong> dialog</p><hr /><ul><li><span style="color: rgb(129,137,156);"> </span> On the main menu, click <strong>Diagrams</strong> &gt; <strong>Customize</strong>.</li></ul><p>You can change the properties of existing diagrams (<strong>Edit</strong> function) or create your own brand new diagram type (<strong>Create</strong> function). Diagram customization descriptors are saved in a separate file for every diagram, so you are able to exchange these customizations with your partners or colleagues (use <strong>Import</strong> or <strong>Export</strong> function).<br /><br class="atl-forced-newline" />The <strong>Reset to default</strong> button in the <strong>Customize Diagrams</strong> dialog restores the default configuration for diagrams bundled with the installation. It does not work with user-defined diagrams.</p><p><br class="atl-forced-newline" />To open the <strong>Customize Diagram Wizard</strong></p><hr /><p>Do either:</p><ul><li>In the <strong>Customize Diagrams</strong> dialog, select a diagram type and click <strong>Edit</strong>.<br /><br /><ac:image ac:align="center"><ri:attachment ri:filename="customize_diagrams_dialog.png" /></ac:image></li></ul><ul><li>Click <strong>Create</strong> and then select one of the following commands:</li><li style="margin-left: 60.0px;"><strong>Diagram with Symbols Type</strong>, if you need to create a new diagram type.</li><li style="margin-left: 60.0px;"><strong>Relation Map Type</strong>, if you need to create a new relation map diagram.</li><li style="margin-left: 60.0px;"><strong>Dependency Matrix Type</strong>, if you need to create a new matrix type.</li><li style="margin-left: 60.0px;"><strong>Generic Table Type</strong>,<strong> </strong>if you need to create a new generic table diagram.</li><li style="margin-left: 60.0px;"><strong>Create from Existing Diagram</strong>, if you need to create custom diagrams from existing ones. </li></ul><p><br class="atl-forced-newline" /><ac:image ac:align="center"><ri:attachment ri:filename="diagram_customization_create_button.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6ccab83b-f9a1-4b15-aaf1-6d527fa5cf57"><ac:parameter ac:name="id">168915472</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul class="childpages-macro"><li><a href="https://docs.nomagic.com/display/MDTWRT/Creating+new+diagram+type">Creating new diagram type</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Creating+new+dependency+matrix+type">Creating new dependency matrix type</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Customizing+diagram+palette">Customizing diagram palette</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973627 space=UPDG version=1 -->
## PAGE 00176: Customizing Drag-and-Drop

- page_id: `243973627`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973627/Customizing+Drag-and-Drop
- version_number: 1
- version_date: `2025-07-31T19:04:49.905+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Drag and Drop Actions

1179366690

#### CONTENT-COLUMN: Drag and Drop Actions

1179366701

#### CONTENT-BLOCK: Drag and Drop Actions

1179366691

The drag-and-drop customization allows you to create relationships or assign property values by dragging and dropping one element onto another right in the diagram pane. By using the DSL engine, you may set up your own drag-and-drop specifications between elements:

- [CONFLUENCE_PAGE title='Case study #1: Adding a rule to create a Generalization relationship on drag-and-drop' space='UPDG']
- [CONFLUENCE_PAGE title='Case study #2: Adding a rule to assign a property type on drag-and-drop' space='UPDG']

There are a number of predefined rules to create relationships or assign property values automatically.

#### TIP: Drag and Drop Actions

Drag and Drop Actions

You can customize the following drag-and-drop actions:

- drag-and-drop one element from the diagram pane onto another element on the diagram pane

- drag-and-drop one element from the Model Browser onto another element on the diagram pane
- drag-and-drop two or more elements from the Model Browser onto an element on the diagram pane

Below is a list of the properties to customize drag-and-drop rules.

| Property | Description |
| --- | --- |
| Source Element | Specify the element type to drag to the target element. Specify a , metaclass, or .This is a mandatory property: if the Source Element property is undefined, then the drag-and-drop rule is inactive. |
| Representation Text | Specify the name of the drag-and-drop rule. |
| Relation Action Result | Specify a relationship created between the source and target elements after drag-and-drop. |
| Property Action Result | Specify a property assigned to the target element after drag-and-drop.Note. Before specifying this property, you need to add the drag-and-drop rule into the target element customization Specification window > Connection Rules category > Allowed Drag And Drops property. |
| Append Mode | Change the append mode for the property assignment. The possible Append Mode property value is true or false.If true, properties are assigned one by one. If false, the created property overwrites the former property. |

1179366688

**Related pages**

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Dragging objects' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="e940cae8-02cd-4bfe-8c12-c129446d87a0"><ac:parameter ac:name="id">1179366690</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="2c604392-9ead-4c9a-bc4a-398ae5f39da3"><ac:parameter ac:name="id">1179366701</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="05156898-34c0-4ae6-85b7-0b877b6d3f11"><ac:parameter ac:name="id">1179366691</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p><span>The drag-and-drop customization allows you to create relationships or assign property values by dragging and dropping one element onto another right in the diagram pane. By using the DSL engine, you may set up your own drag-and-drop specifications between elements:</span></p><ul><li><ac:link><ri:page ri:space-key="UPDG" ri:content-title="Case study #1: Adding a rule to create a Generalization relationship on drag-and-drop" /><ac:plain-text-link-body><![CDATA[create relationships]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="UPDG" ri:content-title="Case study #2: Adding a rule to assign a property type on drag-and-drop" /><ac:plain-text-link-body><![CDATA[assign property values]]></ac:plain-text-link-body></ac:link></li></ul><p>There are a number of predefined rules to create relationships or assign property values automatically.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="4b9fb62f-af72-40ec-b587-65e5b041618c"><ac:parameter ac:name="title">Drag and Drop Actions</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p>You can customize the following drag-and-drop actions:</p><ul><li>drag-and-drop one element from the diagram pane onto another element on the diagram pane</li></ul></div></div><div class="layoutArea"><div class="column"><ul><li>drag-and-drop one element from the Model Browser onto another element on the diagram pane</li><li>drag-and-drop two or more elements from the Model Browser onto an element on the diagram pane</li></ul></div></div></ac:rich-text-body></ac:structured-macro><p><br /></p><p>Below is a list of the properties to customize drag-and-drop rules. </p><table class="relative-table wrapped" style="width: 1013.0px;"><colgroup> <col style="width: 0.0px;" /> <col style="width: 0.0px;" /> </colgroup><thead><tr><th><p>Property</p></th><th><p>Description</p></th></tr></thead><tbody><tr><td><strong>Source Element</strong></td><td><p style="text-align: left;">Specify the element type to drag to the target element. Specify a <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Class" /><ac:plain-text-link-body><![CDATA[class]]></ac:plain-text-link-body></ac:link>, metaclass, or <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotype]]></ac:plain-text-link-body></ac:link>.</p><p style="text-align: left;">This is a mandatory property: if the <strong>Source Element</strong> property is undefined, then the drag-and-drop rule is inactive. </p></td></tr><tr><td><p><strong>Representation Text</strong></p></td><td><p>Specify the name of the drag-and-drop rule.</p></td></tr><tr><td><strong>Relation Action Result</strong></td><td><p style="text-align: left;">Specify a relationship created between the source and target elements after drag-and-drop.</p></td></tr><tr><td><strong>Property Action Result</strong></td><td><p style="text-align: left;">Specify a property assigned to the target element after drag-and-drop.</p><p style="text-align: left;"><strong>Note.</strong> Before specifying this property, you need to add the drag-and-drop rule into the target element customization Specification window &gt; Connection Rules category &gt; Allowed Drag And Drops property.</p></td></tr><tr><td><strong>Append Mode</strong></td><td><p style="text-align: left;">Change the append mode for the property assignment. The possible <strong>Append Mode </strong>property value is <em>true </em>or <em>false</em>.</p><p style="text-align: left;">If <em>t</em><em>rue</em>, properties are assigned one by one. If <em>false</em>, the created property overwrites the former property.</p></td></tr></tbody></table><p><br /></p></div></div><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3c3fdccd-0a52-423b-9779-e4f0911c51a0"><ac:parameter ac:name="id">1179366688</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Dragging objects" /></ac:link></li></ul><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973618 space=UPDG version=1 -->
## PAGE 00177: Customizing Element Shortcut Menu

- page_id: `243973618`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973618/Customizing+Element+Shortcut+Menu
- version_number: 1
- version_date: `2025-07-31T19:04:49.806+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Important

730821357

#### CONTENT-COLUMN: Important

730821368

730821355

**On this page**

- [Quick property editor](https://docs.nomagic.com/display/MDTWRT/Customizing+Element+Shortcut+Menu#CustomizingElementShortcutMenu-Quickpropertyeditor)
- [Applying quick stereotypes](https://docs.nomagic.com/display/MDTWRT/Customizing+Element+Shortcut+Menu#CustomizingElementShortcutMenu-Applyingquickstereotypes)

#### CONTENT-BLOCK: Important

730821358

You can add new items to shortcut menus to use certain modeling tool commands more conveniently. To do so, you need to[CONFLUENCE_PAGE title='Creating your First Customization' space=''].

#### INFO: Important

Important

Properties of all other types are ignored.

##### **Customizing the model**

There are two ways to customize the model:

**Quick property editor**

You can add those properties you frequently use to the customized element shortcut menu. To do so, open the project that includes your [CONFLUENCE_PAGE title='Creating your First Customization' space=''], open the [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] for your customization element, locate the**In Shortcut Menu**property, and specify the property you want to see in the element shortcut menu.

These are the types of properties whose values can be edited directly via the element shortcut menu:

- Boolean – allows selecting or clearing a checkbox.
- Enumeration – allows selecting one of the listed enumeration literals.
- Reference to one element (a subclass of Classifier) – allows using an element list to select a type.

[IMAGE alt='' src='']

###### Example of the boolean property in the shortcut menu

**Applying quick stereotypes**

Stereotypes, for example, «continuous», «buffer», etc., act as flags.You can set these stereotypes on selected elements with a single click from the element shortcut menu.

Use the **Quick Applying For**property in the customization element[CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] to add stereotypes to the customized element shortcut menu. Before you can do that, you need to create your [CONFLUENCE_PAGE title='Creating your First Customization' space=''] for a stereotype.

The **Quick Applying for** property specifies a stereotype or a metaclass to apply customizations directly from the element shortcut menu.For example, if the**Quick Applying For**property value is the*Class*metaclass, the customization will be available for the class elements only.

[IMAGE alt='' src='']

###### Example of a customized element shortcut menu

You can show/hide default modeling tool options in shortcut menus by using the[CONFLUENCE_PAGE title='Customize Perspectives dialog' space='MDTWRT'](**Options**>**Perspectives**>**Customize**).

730832983

**Related Pages**

- Creating Customization Data
- Using Customization Data
- Customizing and Selecting Perspective

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f1f07b15-819f-451d-9cca-c2e211513c74"><ac:parameter ac:name="id">730821357</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="89494d6b-7313-4996-a13e-09b6ea7612b6"><ac:parameter ac:name="id">730821368</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b051173a-13b7-4dc0-980d-25bbcdcc0812"><ac:parameter ac:name="id">730821355</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><ul><li><span class="toc-item-body"><a href="https://docs.nomagic.com/display/MDTWRT/Customizing+Element+Shortcut+Menu#CustomizingElementShortcutMenu-Quickpropertyeditor" class="toc-link">Quick property editor</a></span></li><li><span class="toc-item-body"><a class="toc-link" href="https://docs.nomagic.com/display/MDTWRT/Customizing+Element+Shortcut+Menu#CustomizingElementShortcutMenu-Applyingquickstereotypes">Applying quick stereotypes</a></span></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="54c0e415-dfef-4b0e-b80e-ae2cea276eaa"><ac:parameter ac:name="id">730821358</ac:parameter><ac:rich-text-body><p><span style="color: rgb(0,0,0);">You can add new items to shortcut menus to use certain modeling tool commands more conveniently. To do so, you need to </span><ac:link><ri:page ri:content-title="Creating your First Customization" /><ac:plain-text-link-body><![CDATA[customize the model]]></ac:plain-text-link-body></ac:link><span style="color: rgb(0,0,0);">.</span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="72bb3016-4052-4433-bb34-b92be2a6efdc"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><p><span style="color: rgb(0,0,0);">Properties of all other types are ignored. </span></p></ac:rich-text-body></ac:structured-macro><h3><strong>Customizing the model</strong></h3><p>There are two ways to customize the model:</p><p><strong><span style="color: rgb(0,0,0);">Quic</span><span style="color: rgb(0,0,0);">k</span> <span style="color: rgb(0,0,0);"> property editor</span></strong></p><p><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);">You can add those properties you frequently use to the customized element shortcut menu. To do so, open the project that includes your <ac:link><ri:page ri:content-title="Creating your First Customization" /><ac:plain-text-link-body><![CDATA[DSL customization]]></ac:plain-text-link-body></ac:link>, open the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> for your customization element, locate the </span><strong>In Shortcut Menu</strong><span style="color: rgb(0,0,0);"> property</span>, and specify the property you want to see in the element shortcut menu<span style="color: rgb(0,0,0);">.</span></span></p><p><span style="color: rgb(0,0,0);">These are the types of properties whose values can be edited directly via the element shortcut menu: </span></p><ul><li><span style="color: rgb(0,0,0);">Boolean – allows selecting or clearing a checkbox.</span></li><li><span style="color: rgb(0,0,0);">Enumeration – allows selecting one of the listed enumeration literals.</span></li><li><span style="color: rgb(0,0,0);">Reference to one element (a subclass of Classifier) – allows using an element list to select a type.</span></li></ul><p><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);"><br /></span></span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="customizing_shortcut_menu.png" /></ac:image></p><div class="layoutArea"><div class="column"><div class="column"><h6 style="text-align: center;">Example of the boolean property in the shortcut menu</h6><div class="layoutArea"><div class="column"><p><span style="color: rgb(0,0,0);"><strong>Applying quick stereotypes</strong><br /></span></p><p><span style="color: rgb(0,0,0);">Stereotypes, for example, «continuous», «buffer», etc., act as flags. </span><span style="color: rgb(0,0,0);">You can set these stereotypes on selected elements with a single click from the element shortcut menu. </span></p><p><span style="color: rgb(0,0,0);">Use the <strong>Quick Applying For </strong>property <span style="color: rgb(0,0,0);">in the customization element </span><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> to add stereotypes to the customized element shortcut menu. Before you can do that, you need to create your <ac:link><ri:page ri:content-title="Creating your First Customization" /><ac:plain-text-link-body><![CDATA[DSL customization]]></ac:plain-text-link-body></ac:link> for a stereotype. </span></p><p><span style="color: rgb(0,0,0);">The <strong>Quick Applying for</strong> property s</span><span style="color: rgb(0,0,0);">pecifies a stereotype or a metaclass to apply customizations directly from the element shortcut menu. </span><span style="color: rgb(0,0,0);">For example, if the </span><strong style="color: rgb(0,0,0);">Quick Applying For</strong><span style="color: rgb(0,0,0);"> property value is the </span><em style="color: rgb(0,0,0);">Class</em><span style="color: rgb(0,0,0);"> metaclass, the customization will be available for the class elements only. </span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="customization_of_shortcut_menu2.png" /></ac:image></p><h6 class="column" style="text-align: center;">Example of a customized element shortcut menu</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0c452dcc-d60a-4f26-af33-6b4927eea666"><ac:rich-text-body><p><span style="color: rgb(0,0,0);">You can show/hide default modeling tool options in shortcut menus by using the </span><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Customize Perspectives dialog" /><ac:plain-text-link-body><![CDATA[Perspectives functionality]]></ac:plain-text-link-body></ac:link><span style="color: rgb(0,0,0);"> (</span><strong>Options</strong><span style="color: rgb(0,0,0);"> &gt; </span><strong>Perspectives</strong><span style="color: rgb(0,0,0);"> &gt; </span><strong>Customize</strong><span style="color: rgb(0,0,0);">).</span></p></ac:rich-text-body></ac:structured-macro></div></div></div></div></div></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="74b83522-bb5e-42bb-acf5-9ad20bff5449"><ac:parameter ac:name="id">730832983</ac:parameter><ac:rich-text-body><p><strong>Related Pages</strong></p><ul><li><a href="https://docs.nomagic.com/display/MDTWRT/Creating+Customization+Data">Creating Customization Data</a></li><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MDTWRT/Using+Customization+Data">Using Customization Data</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Customizing+and+Selecting+Perspective">Customizing and Selecting Perspective</a></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973646 space=UPDG version=1 -->
## PAGE 00178: Customizing Possible Owned Elements

- page_id: `243973646`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973646/Customizing+Possible+Owned+Elements
- version_number: 1
- version_date: `2025-07-31T19:04:50.501+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data
- labels: []

### NORMALIZED CONTENT

You can define situations when elements of particular predefined stereotypes or metaclasses are created inside other elements.For example:

- Block contains the BlockProperty property, instead of a standard property.
- Block owns InternalBlockDiagram , instead of a standard CompositeStructureDiagram .

Use properties listed in the customization element [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'], under the **Owned Elements** category, to customize these cases.

###### Customizing Owned Types

Customize the list of owned types in the DSL element shortcut menu (under the **Create Element**command) in the [CONFLUENCE_PAGE title='Model Browser' space='MDTWRT'] and other lists. The properties used in customizing owned types are:

| Property | Description |
| --- | --- |
| Suggested Owned Types | Specifies the list of stereotypes and metaclasses used when creating inner elements in the DSL element. |
| Hidden Owned Types | Specifies the list of stereotypes and metaclasses not used as inner elements. |

You cannot customize a standard element when you use standard UML (rather than DSL) to create certain stereotyped elements (such as a package). In this case, you must specify possible owners using the **Possible Owners**property from the customization element Specification window. The **Possible Owners** property specifies the list of stereotypes and metaclasses used when creating owned elements.

###### Customizing Owned Diagrams

Customize the list of owned diagrams in the DSL element shortcut menu (under the **Create Diagram**command) in the Model Browser and in other lists. The following are the properties used in customizing owned diagrams:

| Property | Description |
| --- | --- |
| Suggested Owned Diagrams | Specifies types of diagrams appearing in the DSL element shortcut menu when creating possible inner diagrams. |
| Hidden Owned Diagrams | Specifies types of diagrams owned by the DSL element. For example, if the property value is Section, then the Section elements are owned by the customized element. |

#### NOTE: Version

Version

Until version 17.0.3, the **Suggested Owned Type**and **Hidden Owned Types**properties did not function if the customization target was a metaclass.

###### Customizing Suggested Relationships

You can customize the list of relationships created directly in the model from the Model Browser, starting from a source or target element.

Customize the relationships list according to the following rules:

- If a DSL relationship has *no*connection rules for restricted end types and the **Hide Metatype**property value specified is *true*, the DSL relationship will be added into all lists where the extended UML type is selected. For example, the «allocation» relationship in SysML model will be used everywhere Dependency is used.
- If a DSL relationship has connection rules, then it will be created only from or to these restricted types.

#### PANEL: On this page

On this page

44

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Customization Element Properties Description' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span>You can define situations when elements of particular predefined stereotypes or metaclasses are created inside other elements. </span>For example:</p><ul><li><em>Block</em> contains the <em>BlockProperty</em> property, instead of a standard property.</li><li><em>Block</em> owns <em>InternalBlockDiagram</em>, instead of a standard <em>CompositeStructureDiagram</em>.</li></ul><p>Use properties listed in the customization element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>, under the <strong>Owned Elements</strong> category, to customize these cases.</p><p><br /></p><h4>Customizing Owned Types</h4><p>Customize the list of owned types in the DSL element shortcut menu (under the <strong>Create Element </strong>command) in the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Model Browser" /></ac:link> and other lists. The properties used in customizing owned types are:</p><table class="wrapped"><colgroup><col /><col /></colgroup><thead><tr><th><p>Property</p></th><th><p>Description</p></th></tr></thead><tbody><tr><td><strong>Suggested Owned Types</strong></td><td><p>Specifies the list of stereotypes and metaclasses used when creating inner elements in the DSL element. </p></td></tr><tr><td><strong>Hidden Owned Types</strong></td><td><p>Specifies the list of stereotypes and metaclasses <em>not </em>used as inner elements. </p></td></tr></tbody></table><p><br /></p><p>You cannot customize a standard element when you use standard UML (rather than DSL) to create certain stereotyped elements (such as a package). In this case, you must specify possible owners using the <strong>Possible Owners </strong>property from the customization element Specification window. The <strong>Possible Owners</strong> property s<span>pecifies the list of stereotypes and metaclasses used when creating owned elements.</span></p><p><br /></p><h4>Customizing Owned Diagrams</h4><p>Customize the list of owned diagrams in the DSL element shortcut menu (under the <strong>Create Diagram </strong>command) in the Model Browser and in other lists. The following are the properties used in customizing owned diagrams:</p><p><br /></p><table class="relative-table wrapped" style="width: 980.0px;"><colgroup><col style="width: 0.0px;" /><col style="width: 0.0px;" /></colgroup><thead><tr><th><p>Property</p></th><th><p>Description</p></th></tr></thead><tbody><tr><td><strong>Suggested Owned Diagrams</strong></td><td><p>Specifies types of diagrams appearing in the DSL element shortcut menu when creating possible inner diagrams. </p></td></tr><tr><td><strong>Hidden Owned Diagrams</strong></td><td><p>Specifies types of diagrams owned by the DSL element. For example, if the property value is <em>Section</em>, then the <em>Section</em> elements are owned by the customized element. </p></td></tr></tbody></table><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3f06f109-1431-47c7-9fb5-e34a71d92748"><ac:parameter ac:name="title">Version</ac:parameter><ac:rich-text-body><p>Until version 17.0.3, the <strong>Suggested Owned Type </strong>and <strong>Hidden Owned Types </strong>properties did not function if the customization target was a metaclass.</p></ac:rich-text-body></ac:structured-macro><br /><h4>Customizing Suggested Relationships</h4><p>You can customize the list of relationships created directly in the model from the Model Browser, starting from a source or target element.</p><p>Customize the relationships list according to the following rules:</p><ul><li><p>If a DSL relationship has <em>no </em>connection rules for restricted end types and the <strong>Hide Metatype </strong>property value specified is <em>true</em>, the DSL relationship will be added into all lists where the extended UML type is selected. For example, the «allocation» relationship in SysML model will be used everywhere Dependency is used.</p></li><li><p>If a DSL relationship has connection rules, then it will be created only from or to these restricted types.</p></li></ul></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e6b65c85-becb-4bdd-a2fd-c5d4d9f93f65"><ac:parameter ac:name="title">On this page</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="997334aa-2247-4e35-b1f5-d1af641d3743"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b0ccb40e-6e11-4ccd-baa7-51ecf465051e"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Element Properties Description" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973602 space=UPDG version=1 -->
## PAGE 00179: Customizing Specification Window

- page_id: `243973602`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973602/Customizing+Specification+Window
- version_number: 1
- version_date: `2025-07-31T19:04:49.417+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data
- labels: []

### NORMALIZED CONTENT

The main purpose of DSL is to hide UML, so that DSL elements would look standard or as new type elements in models. DSL element properties are specified in the DSL element [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] and the **Properties** panel (at the bottom of the [CONFLUENCE_PAGE title='Model Browser' space='MDTWRT']) as regular properties.

There are several customizations and grouping cases for properties:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(0,0,0);">The main purpose of DSL is to hide UML, so that DSL elements would look standard or as new type elements in models. </span> <span style="color: rgb(0,0,0);">DSL element properties are specified in the DSL element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> and the <strong>Properties</strong> panel (at the bottom of the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Model Browser" /><ac:plain-text-link-body><![CDATA[Browser window]]></ac:plain-text-link-body></ac:link>) as regular properties. </span></p><p><span style="color: rgb(0,0,0);">There are several customizations and grouping cases for properties:</span></p><p><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d368bd14-56cc-4bf1-9843-3d76bc07dfd3" /> <br /></span></p>
````

<!--NOMAGIC_PAGE id=243973654 space=UPDG version=1 -->
## PAGE 00180: Customizing Symbols

- page_id: `243973654`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973654/Customizing+Symbols
- version_number: 1
- version_date: `2025-07-31T19:04:50.726+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data
- labels: []

### NORMALIZED CONTENT

###### Setting default symbol size

The **Default Shape Size** property defines the default size of a shape when you create a symbol in a diagram. Use the **Default Shape Size**property in the Customization element [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] to define the default symbol size in DSL customization:

- The first value is the width (x) in pixels. Value= 0 is used if a default symbol width should stay, but the height should change.
- The second value is a height (y) in pixels.

A default shape size is used everywhere a new symbol is created - using [CONFLUENCE_PAGE title='Customizing Drag-and-Drop' space=''], diagram toolbar button, diagram wizards, etc.

###### Setting custom path style

Customize the custom path style by changing:

- Line style (dashes, dots, solid line, etc).
- Arrow style at the first end and arrow style at the second end.
- Custom scalable icon for the first end and for the second style.

To create the custom path style

1. In a profile, create a stereotype.
2. Right-click either the stereotype or a created stereotype (usually created in the profile diagram). Select Metaclass . In the Select Metaclass dialog, clear all selections. Select the Relationships metaclass.
3. Customize the path style. In the stereotype Specification window, click the Icon property and then click the [ATTACHMENT filename='edit.png'] button.
4. Click Yes to open the Path Icon Customization dialog. [ATTACHMENT filename='path_icon_customization_dialog.png']
5. Specify the path style.
6. Click OK when you are done.
7. [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT'] to a relationship.

#### INFO: Symbol Properties

Symbol Properties

Change the line width and the rest of the path properties in the [**Symbol Properties**dialog](https://docs.nomagic.com/display/MDTWRT/Symbol+Properties+dialog).

Path icon usage rules:

- Custom appearance is used only after applying the stereotype.
- End icons are rotated according to path position and direction.
- The end icon size is scaled according to font size (as with standard arrows).

#### PANEL: On this page

On this page

44

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Customization Element Properties Description' space='']
- [CONFLUENCE_PAGE title='Formatting symbols' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p><h4>Setting default symbol size</h4><p>The <strong>Default Shape Size</strong> property defines the default size of a shape when you create a symbol in a diagram. Use the <strong>Default Shape Size </strong>property in the Customization element <ac:inline-comment-marker ac:ref="b0df89a0-346e-4c82-9599-d370b96840e2"><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> to define the default symbol size in DSL customization</ac:inline-comment-marker>:</p><p><br /></p><ul><li>The first value is the width (x) in pixels. Value= 0 is used if a default symbol width should stay, but the height should change.</li><li>The second value is a height (y) in pixels.</li></ul><p><br /></p><p>A default shape size is used everywhere a new symbol is created - using <ac:link><ri:page ri:content-title="Customizing Drag-and-Drop" /><ac:plain-text-link-body><![CDATA[drag-and-drop]]></ac:plain-text-link-body></ac:link>, diagram toolbar button, diagram wizards, etc. </p><p><br /></p><h4>Setting custom path style</h4><p>Customize the custom path style by changing:</p><ul><li>Line style (dashes, dots, solid line, etc).</li><li>Arrow style at the first end and arrow style at the second end.</li><li>Custom scalable icon for the first end and for the second style. <br /><br /></li></ul><p>To create the custom path style</p><hr /><ol><li>In a profile, create a stereotype.</li><li>Right-click either the stereotype or a created stereotype (usually created in the profile diagram). Select <strong>Metaclass</strong>.<strong> </strong>In the <strong>Select Metaclass</strong> dialog, clear all selections. Select the <em>Relationships</em> metaclass.</li><li>Customize the path style. In the stereotype Specification window, click the <strong>Icon</strong> property and then click the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="edit.png"><ri:page ri:content-title="Do Not Suggest As Type" /></ri:attachment></ac:image> button.</li><li>Click <strong>Yes</strong> to open the <strong>Path Icon Customization</strong> dialog.<br /><ac:image><ri:attachment ri:filename="path_icon_customization_dialog.png" /></ac:image><br /><br /></li><li>Specify the path style.</li><li>Click <strong>OK</strong> when you are done.</li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[Apply the stereotype]]></ac:plain-text-link-body></ac:link> to a relationship.<br /><br /></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b822edb4-6104-486b-92fc-b0838c019677"><ac:parameter ac:name="title">Symbol Properties </ac:parameter><ac:rich-text-body><p>Change the line width and the rest of the path properties in the <a href="https://docs.nomagic.com/display/MDTWRT/Symbol+Properties+dialog"><strong>Symbol Properties </strong>dialog</a>. </p></ac:rich-text-body></ac:structured-macro><p class="title"><br /></p><p>Path icon usage rules:</p><ul><li>Custom appearance is used only after applying the stereotype.</li><li>End icons are rotated according to path position and direction.</li><li>The end icon size is scaled according to font size (as with standard arrows).</li></ul><p><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="d3066ec8-3bb5-4611-aaee-00ea39f3995f"><ac:parameter ac:name="title">On this page</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="96373e45-386f-4594-8c93-902998640a55"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="53d73416-7f29-4f60-a43a-bddc008bfc20"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Customization Element Properties Description" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Formatting symbols" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973664 space=UPDG version=1 -->
## PAGE 00181: Default visibility of property groups and subgroups

- page_id: `243973664`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973664/Default+visibility+of+property+groups+and+subgroups
- version_number: 1
- version_date: `2025-07-31T19:04:51.141+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Creating Property Groups and Subgroups
- labels: []

### NORMALIZED CONTENT

You can create property groups and subgroups for both standard UML metaclasses and [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT']. The group will be added to either the metaclass or to the stereotype depending on the customization target of the customized property group.

If the customization target is a stereotype and the **Hide Metatype**property is set to true, the specified property group in this customization is visible only for the elements with this stereotype applied.

If the customization target is a metaclass, the specified group in this customization will be visible for the elements of this particular type. This group is also visible for the elements with applied stereotypes, except when the **Hide Metatype**property in this stereotype customization is set to true.

The table below lists the default property group visibility in the element’s [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'].

| Customization target | Property group visibility in element’s Specification window and Properties panel |  |  |
| --- | --- | --- | --- |
|  | Element of metaclass type | Element with stereotype with DSL customization Hide Metatype=false | Element with stereotype with DSL customization Hide Metatype=true |
| Stereotype | Invisible | Visible in standard mode | Visible in standard mode |
| Metaclass | Visible in standard mode | Visible in standard mode | Visible in all modes |

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Creating Property Groups and Subgroups' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span>You can create property groups and subgroups for both standard UML metaclasses and <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotypes]]></ac:plain-text-link-body></ac:link>. The group will be added to either the metaclass or to the stereotype depending on the customization target of the customized property group.</span></p><p>If the customization target is a stereotype and the <strong>Hide Metatype </strong>property is set to true, the specified property group in this customization is visible only for the elements with this stereotype applied.</p><p>If the customization target is a metaclass, the specified group in this customization will be visible for the elements of this particular type. This group is also visible for the elements with applied stereotypes, except when the <strong>Hide Metatype </strong>property in this stereotype customization is set to true.</p><p><ac:inline-comment-marker ac:ref="c0184295-a96a-40ab-a6e8-ab5c776682f4">The table below</ac:inline-comment-marker> lists the default property group visibility in the element’s <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>.</p><table class="relative-table wrapped" style="width: 100.0%;"><colgroup> <col style="width: 18.324173%;" /> <col style="width: 19.065554%;" /> <col style="width: 29.351587%;" /> <col style="width: 33.234936%;" /> </colgroup><tbody><tr><th><div class="layoutArea"><div class="column"><p><span>Customization target </span></p></div></div></th><th colspan="3"><div class="layoutArea"><div class="column"><p><span>Property group visibility in element’s Specification window and Properties panel </span></p></div></div></th></tr><tr><td><br /></td><td class="highlight-grey" data-highlight-colour="grey"><div class="section"><div class="layoutArea"><div class="column"><p><strong>Element of metaclass type </strong></p></div></div></div></td><td class="highlight-grey" data-highlight-colour="grey"><div class="section"><div class="layoutArea"><div class="column"><p><strong>Element with stereotype with DSL customization Hide Metatype=<em>false</em></strong></p></div></div></div></td><td class="highlight-grey" data-highlight-colour="grey"><div class="layoutArea"><div class="column"><p><strong>Element with stereotype with DSL customization Hide Metatype=<em>true</em> </strong></p></div></div></td></tr><tr><td><div class="layoutArea"><div class="column"><p><strong>Stereotype</strong></p></div></div></td><td><div class="section"><div class="layoutArea"><div class="column"><p><span>Invisible</span></p></div></div></div></td><td><div class="section"><div class="layoutArea"><div class="column"><p><span>Visible in standard mode</span></p></div></div></div></td><td><div class="layoutArea"><div class="column"><p><span>Visible in standard mode</span></p></div></div></td></tr><tr><td><p><strong>Metaclass</strong></p></td><td><div class="layoutArea"><div class="column"><p><span>Visible in standard mode</span></p></div></div></td><td><div class="layoutArea"><div class="column"><p><span>Visible in standard mode</span></p></div></div></td><td><div class="layoutArea"><div class="column"><p><span>Visible in all modes</span></p></div></div></td></tr></tbody></table><p class="auto-cursor-target"><br /></p></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b0ccb40e-6e11-4ccd-baa7-51ecf465051e"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating Property Groups and Subgroups" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973701 space=UPDG version=1 -->
## PAGE 00182: Defining expressions

- page_id: `243973701`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973701/Defining+expressions
- version_number: 1
- version_date: `2025-07-31T19:04:51.647+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Extending Metamodel with Derived Properties
- labels: []

### NORMALIZED CONTENT

1852034054

1852034059

1852034058

Each derived property must have one or more expressions defining the criteria for searching the result elements.

It is strongly recommended that you specify the customization target in the customization element before defining the expression for its derived property.

To open the dialog for a new expression definition

1. Select the attribute with the [CONFLUENCE_PAGE title='Creating and specifying derived properties' space=''].
2. Open the attribute’s [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'].
3. In the general specification pane (opened by default), click the **Expression** property and then click the **...** button. The **Expression**dialog opens, and you can then construct predefined expressions or define your custom operation for calculating derived property values. To learn more about derived properties, see the [CONFLUENCE_PAGE title='Custom traceability rules' space='MDTWRT'] page. For more information on expression specification, see the[CONFLUENCE_PAGE title='Specifying criteria for querying model' space='MDTWRT']page.

1852034052

**Related pages**

- Extending Metamodel with Derived Properties

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="aa783133-3833-4c71-9d6e-cc00b5db18db"><ac:parameter ac:name="id">1852034054</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c9394f54-e2f0-408c-ac12-3717661c65f3"><ac:parameter ac:name="id">1852034059</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="039998f1-9d2b-475c-bb92-b5e8df8a7e28"><ac:parameter ac:name="id">1852034058</ac:parameter><ac:rich-text-body><p>Each derived property must have one or more expressions defining the criteria for searching the result elements.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="c0813361-1bfe-49e9-955c-277c8e7869f6"><ac:rich-text-body><p>It is strongly recommended that you specify the customization target in the customization element before defining the expression for its derived property.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To open the dialog for a new expression definition</p><hr /><ol><li><p>Select the attribute with the <ac:link><ri:page ri:content-title="Creating and specifying derived properties" /><ac:plain-text-link-body><![CDATA[stereotype «derivedPropertySpecification»]]></ac:plain-text-link-body></ac:link>.</p></li><li><p>Open the attribute’s <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>.</p></li><li><p>In the general specification pane (opened by default), click the <strong>Expression</strong> property and then click the <strong>...</strong> button. The <strong>Expression </strong>dialog opens, and you can then construct predefined expressions or define your custom operation for calculating derived property values.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="3f682159-3a5a-4f84-8932-d6d456e4c3f7"><ac:rich-text-body><p>To learn more about derived properties, see the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Custom traceability rules" /></ac:link> page. For more information <span style="letter-spacing: 0.0px;">on expression specification, see the </span><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specifying criteria for querying model" /></ac:link><span style="letter-spacing: 0.0px;"> page.</span></p></ac:rich-text-body></ac:structured-macro></li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="00fbb0df-32d4-4ac3-82f5-986c06e43ce0"><ac:parameter ac:name="id">1852034052</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MDTWRT/Extending+Metamodel+with+Derived+Properties">Extending Metamodel with Derived Properties</a></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973639 space=UPDG version=1 -->
## PAGE 00183: Defining Preferred Metatype

- page_id: `243973639`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973639/Defining+Preferred+Metatype
- version_number: 1
- version_date: `2025-07-31T19:04:50.311+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data
- labels: []

### NORMALIZED CONTENT

The DSL customization engine allows specification of a preferred metatype if more than one metatype is defined for the DSL element.

To define a preferred metatype for the DSL type

1. Select the appropriate [CONFLUENCE_PAGE title='Customization Elements' space=''] and open its [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] .
2. Click the value specification cell of the Preferred Metatype property and do one of the following: The selected metatype will be assigned as the **Preferred Metatype** property value. falseMultiple selection is not allowed. You must define a single value.
  - [CONFLUENCE_PAGE title='Selecting single property value from editable list' space='MDTWRT'] and close the Specification window.
  - Click the [ATTACHMENT filename='edit.png'] button [CONFLUENCE_PAGE title='Creating new elements' space='MDTWRT'] . In the [CONFLUENCE_PAGE title='Selecting elements' space='MDTWRT'] , select the created metatype and click OK. Close the Specification window.

After updating the customization element specification, you must either [CONFLUENCE_PAGE title='Using other projects in a project' space='MDTWRT'] in the model or reopen the model.

From now on, all DSL elements will be created with the preferred metatype specified in the customization.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p><p>The DSL customization engine allows specification of a preferred metatype if more than one metatype is defined for the DSL element.</p><div class="layoutArea"><div class="column"><p><span> <br /> </span></p><p><span>To define a preferred metatype for the DSL type</span></p><hr /><ol><li>Select the appropriate <ac:link><ri:page ri:content-title="Customization Elements" /><ac:plain-text-link-body><![CDATA[customization element]]></ac:plain-text-link-body></ac:link> and open its <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>.</li><li>Click the value specification cell of the <strong>Preferred Metatype</strong> property and do one of the following: <ul><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Selecting single property value from editable list" /><ac:plain-text-link-body><![CDATA[Select the property value from the open list]]></ac:plain-text-link-body></ac:link>  and close the Specification window.</li><li>Click the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="edit.png"><ri:page ri:space-key="ALFP185" ri:content-title="Using Alf for Activity Edge guards" /></ri:attachment></ac:image> button <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Creating new elements" /><ac:plain-text-link-body><![CDATA[to create a new one]]></ac:plain-text-link-body></ac:link>. In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Selecting elements" /><ac:plain-text-link-body><![CDATA[element Selection dialog]]></ac:plain-text-link-body></ac:link>, select the created metatype and click OK. Close the Specification window.</li></ul><p class="auto-cursor-target">The selected metatype will be assigned as the <strong>Preferred Metatype</strong> property value.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d15e29e9-b1b6-4318-af4e-392c34391b6f"><ac:parameter ac:name="icon">false</ac:parameter><ac:rich-text-body><p>Multiple selection is not allowed. You must define a single value.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><span><span>After updating the customization element specification, you must either <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Using other projects in a project" /><ac:plain-text-link-body><![CDATA[reuse the DSL Customization profile]]></ac:plain-text-link-body></ac:link> in the model or reopen the model.</span><br /></span></p><p>From now on, all DSL elements will be created with the preferred metatype specified in the customization.</p></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="68d6f843-19aa-480d-81e1-df3547d11a1b"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973704 space=UPDG version=1 -->
## PAGE 00184: Derived properties visibility

- page_id: `243973704`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973704/Derived+properties+visibility
- version_number: 1
- version_date: `2025-07-31T19:04:51.829+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Extending Metamodel with Derived Properties
- labels: []

### NORMALIZED CONTENT

1852208784

1852208787

1852208785

A newly created derived property is visible by default in the following places:

- General specification pane of the DSL element’s [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] .
- Properties panel of the DSL element.
- **Compartment Edit** dialog. To see derived properties of customized elements that have the**Used UML Properties** property specified, ensure that derived properties are assigned as values for the **Used UML Properties** property.
- **Criterion Editor** dialog for editing relation criteria in a Relation Map diagram.
- **Select Dependency Criteria** dialog for editing the dependency criteria in a Dependency Matrix 
diagram.

Additionally, DSL customization allows more precision when specifying a derived property’s visibility, as this can be done through the specification of the DSL element’s properties group or subgroup to which the derived property is assigned. As a result, the derived property will be visible in the group or subgroup according to this group’s or subgroup’s visibility settings.

To make derived properties of customized elements having the Used UML Properties property specified visible

1. Open the [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] of the customization element.
2. In the general specification pane, select Used UML Properties and assign one or more derived property values.
3. Save and reopen the project.

To assign the derived property to a property group

1. Select the customization element with the derived property.
2. Create a property group for the customization element.
3. In the general specification pane, edit property values that specify the property group’s visibility.
4. In the property group [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] , click the Properties property and then click the ... button.
5. In the Item Filter dialog, select the check box near the appropriate derived property and click OK . As shown in the following figure, the selected derived property will be assigned to Properties as a new value.
6. Click Close .

Use a similar procedure to assign the derived property to a property subgroup. Create a property subgroup in addition and assign the derived property to the subgroup, rather than the property group.

You can also assign a derived property to a property group not specified in the same customization element if both customization elements extend the same UML element.

[IMAGE alt='' src='']

###### Derived property assigned to property group.

All derived properties, together with custom UML properties, are available for creating your own Report templates.

1852208783

**Related Pages**

- [Extending Metamodel with Derived Properties](https://docs.nomagic.com/display/MDTWRT/Extending+Metamodel+with+Derived+Properties)
- [Using Customization Data](https://docs.nomagic.com/display/MDTWRT/Using+Customization+Data)
- [Creating Customization Data](https://docs.nomagic.com/display/MDTWRT/Creating+Customization+Data)
- [Creating Property Groups and Subgroups](https://docs.nomagic.com/display/MDTWRT/Creating+Property+Groups+and+Subgroups)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="7528d95b-4c3e-4c7d-8334-ceff8b8920a2"><ac:parameter ac:name="id">1852208784</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="8a632f58-0b1a-43fd-9d91-0e06cb4654f1"><ac:parameter ac:name="id">1852208787</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3d21a2a2-d4d8-4837-b131-71c8f3e00902"><ac:parameter ac:name="id">1852208785</ac:parameter><ac:rich-text-body><p>A newly created derived property is visible by default in the following places:</p><ul><li>General specification pane of the DSL element’s <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>.</li><li><strong>Properties</strong> panel of the DSL element.</li><li><p><strong>Compartment Edit</strong> dialog. </p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="382e662a-ac44-4527-9565-37b7cede5b54"><ac:rich-text-body><p>To see derived properties of customized elements that have the<strong> Used UML Properties</strong> property specified, ensure that derived properties are assigned as values for the <strong>Used UML Properties</strong> property.</p></ac:rich-text-body></ac:structured-macro></li><li><p><strong>Criterion Editor</strong> dialog for editing relation criteria in a Relation Map diagram.</p></li><li><p><strong>Select Dependency Criteria</strong> dialog for editing the dependency criteria in a Dependency Matrix<br />diagram.</p></li></ul><p>Additionally, DSL customization allows more precision when specifying a derived property’s visibility, as this can be done through the specification of the DSL element’s properties group or subgroup to which the derived property is assigned. As a result, the derived property will be visible in the group or subgroup according to this group’s or subgroup’s visibility settings.</p><p><br /></p><p>To make derived properties of customized elements having the Used UML Properties property specified visible</p><hr /><ol><li>Open the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> of the customization element.</li><li>In the general specification pane, select <strong>Used UML Properties</strong> and assign one or more derived property values.</li><li>Save and reopen the project.</li></ol><p><br /></p><p>To assign the derived property to a property group</p><hr /><ol><li>Select the customization element with the derived property.</li><li>Create a property group for the customization element.</li><li>In the general specification pane, edit property values that specify the property group’s visibility.</li><li>In the property group <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>, click the <strong>Properties</strong> property and then click the <strong>...</strong> button.</li><li>In the <strong>Item Filter</strong> dialog, select the check box near the appropriate derived property and click <strong>OK</strong>. As shown in the following figure, the selected derived property will be assigned to <strong>Properties</strong> as a new value.</li><li>Click <strong>Close</strong>.</li></ol><p>Use a similar procedure to assign the derived property to a property subgroup. Create a property subgroup in addition and assign the derived property to the subgroup, rather than the property group.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ae27718d-8b3a-457c-abe3-43e77f38ccbb"><ac:rich-text-body><p>You can also assign a derived property to a property group not specified in the same customization element if both customization elements extend the same UML element.</p></ac:rich-text-body></ac:structured-macro><p><ac:image ac:align="center" ac:title="Derived property assigned to property group" ac:alt="Derived property assigned to property group"><ri:attachment ri:filename="deriver_property_tgs.png" /></ac:image></p><h6 style="text-align: center;">Derived property assigned to property group.</h6><p>All derived properties, together with custom UML properties, are available for creating your own Report templates.</p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="fa80ee33-5047-4fa0-9c64-0a7b63221206"><ac:parameter ac:name="id">1852208783</ac:parameter><ac:rich-text-body><p><strong>Related Pages</strong></p><ul><li class="ancestor-link parent-link"><span style="color: rgb(0,0,0);"><a href="https://docs.nomagic.com/display/MDTWRT/Extending+Metamodel+with+Derived+Properties">Extending Metamodel with Derived Properties</a></span></li><li class="ancestor-link"><span style="color: rgb(0,0,0);"><a href="https://docs.nomagic.com/display/MDTWRT/Using+Customization+Data">Using Customization Data</a></span></li><li><span style="color: rgb(0,0,0);"><a href="https://docs.nomagic.com/display/MDTWRT/Creating+Customization+Data">Creating Customization Data</a></span></li><li><span style="color: rgb(0,0,0);"><a href="https://docs.nomagic.com/display/MDTWRT/Creating+Property+Groups+and+Subgroups">Creating Property Groups and Subgroups</a> </span></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973707 space=UPDG version=1 -->
## PAGE 00185: Distributing custom diagrams

- page_id: `243973707`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973707/Distributing+custom+diagrams
- version_number: 1
- version_date: `2025-07-31T19:04:51.923+02:00`
- ancestors: UML Profiling and DSL Guide
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Warning

1523698130

#### CONTENT-COLUMN: Warning

1523698132

1523698127

**On this page**

**3**

#### CONTENT-BLOCK: Warning

1523698131

A [CONFLUENCE_PAGE title='Customizing diagrams' space=''] can be exchanged with other usersin a *.zip* file format, as any other resource, for manual import into the modeling tool using the [CONFLUENCE_PAGE title='Resource Manager' space='MDTWRT']. Alternatively, you can export/import the custom diagram descriptor (the .*xml*file) using the **Customize Diagrams** dialog.

##### Distributing custom diagrams using Resource Manager

You need to build a*.zip*file containing a diagram descriptor file (e.g., *descriptor.xml*) and a Resource Manager descriptor file (e.g., *MDR_Custom Diagram_MagicDraw_74842_descriptor.xm**l*.)to be able to share your own custom diagram. For this, you need to use the **Development Tools** plugin. Once you generate and share the file, the diagram customization can then be imported into the modeling tool by another user via the **Resource Manager**for future use and accessibility.

#### WARNING: Warning

Warning

You can build a *.zip* file for custom diagram distribution only after you have [CONFLUENCE_PAGE title='Creating new diagram type' space='']created a newdiagram type or edited an existing standard diagram.

To create a *.zip* file using the **Development Tools** plugin

1. On your local file system, create the following folders structure: ...\<Custom Diagram Resource>\data\defaults\data\diagrams . [IMAGE alt='' src='']
2. Launch the modeling tool.
3. Do one of the following:
  - 
    1. In the main menu, go to **Help** > **About**.
    2. Next to Configuration Files , click the file location path. The configuration files folder opens.
    3. Under <configuration files>\data\diagrams, locate your custom diagram folder containing a descriptor .
  - 
    1. In the main menu, go to**Diagrams** >**Customize**.
    2. In the **Customize Diagrams** dialog, select the custom diagram whose descriptor file you want to export and click the**Export** button. WarningBefore the export operation, create a new folder on your local file system and give it the name of your custom diagram, such as *Custom Diagram*. The exported descriptor file needs to be renamed to *descriptor.xml*and saved in this newly-created folder.
4. Copy and paste the custom diagram folder together with the descriptor file into the folders structure you created in thefirststep. 
[IMAGE alt='' src=''] Distributing ProfilesIf you have specified Profiles when [CONFLUENCE_PAGE title='Customizing diagrams' space=''], it is highly recommended that you distribute them together with your custom diagram. For this, create the *Profiles* folder under the custom diagram resource root folder and place all required Profiles in it before generating a *.zip*archive.You need to mark each Profile distributed together with a custom resource as**Standard/System Profile** (**File** >**Project Properties** > **More** >**Standard/System Profile**) to store it locally. Profiles stored on the server cannot be used for a custom diagram.[IMAGE alt='' src='']
5. Download and [CONFLUENCE_PAGE title='Installing modeling tools and plugins' space='ILTWRT'] the Development Tools plugin.
6. Restart the modeling tool.
7. In the main menu, click Tools > Development Tools > Build Custom Resource .
8. In the Custom Resource Building Wizard , set the custom diagram folder as the Resource Folder .
9. Click Next to skip the other steps and then click Finish . The resource ( . zip file) is built. It can now be distributed and [CONFLUENCE_PAGE title='Resource Manager' space='MDTWRT'].

#### INFO: Info

Info

A created custom diagram resource (.*zip*) can be bundled into the resource distribution file (.*rdzip*) using the **Development Tools** plugin for distribution alongside other resources. [CONFLUENCE_PAGE title='Building a resource distribution file' space='MDTWRT']>]]>

##### Distributing custom diagrams using Customize Diagrams dialog

You can export the custom diagram descriptor (.*xml*) file directly into the**Customize Diagrams** dialog. The exported file can then be shared with others and imported into the modeling tool by another user via the same **Customize Diagrams** dialog using the **Import**command.

#### WARNING: Warning

Warning

You can export an .*xml*file for custom diagram distribution only after you have[CONFLUENCE_PAGE title='Creating new diagram type' space='']or edited an existing standard diagram.

To export a custom diagram descriptor

1. In the main menu, go to Diagrams > Customize .
2. Select a custom diagram from the list and click the Export button. [ATTACHMENT filename='exporting_diagram_descriptor.png']

The .*xml* file is exported. You can now distribute it.

To import a custom diagram descriptor into the modeling tool

1. In the main menu, go to Diagrams > Customize .
2. Click the **Import** button and point to a descriptor (.*xml*)**on your local file system. [IMAGE alt='' src='']

The *.xml* file is imported, and a new diagram type appears under **Custom** **Diagrams**in the **Customize Diagrams** dialog.****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="b277f74b-e3a3-427b-a2c3-cacc84dd1cd6"><ac:parameter ac:name="id">1523698130</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="e5065f0a-667b-4025-a1ec-446a822b81e4"><ac:parameter ac:name="id">1523698132</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f1ab2bcd-1e4b-44c3-b64e-a0452d78669c"><ac:parameter ac:name="id">1523698127</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="e0c159d6-10b5-4b2a-a6db-feb87db6c1ef"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="97826136-737d-4280-9c80-6a6996e8c1b8"><ac:parameter ac:name="id">1523698131</ac:parameter><ac:rich-text-body><p>A <ac:link><ri:page ri:content-title="Customizing diagrams" /><ac:plain-text-link-body><![CDATA[custom diagram]]></ac:plain-text-link-body></ac:link> <ac:inline-comment-marker ac:ref="885cb35b-65e1-4587-be5b-555938d081bc">can be exchanged with other users </ac:inline-comment-marker>in a <em style="letter-spacing: 0.0px;">.zip</em> file format, as any other resource, for manual import into the modeling tool using the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Resource Manager" /></ac:link>. Alternatively, you can export/import the custom diagram descriptor (the .<em style="letter-spacing: 0.0px;">xml </em>file) using the <strong style="letter-spacing: 0.0px;">Customize Diagrams</strong> dialog. </p><h3>Distributing custom diagrams using Resource Manager</h3><p><ac:inline-comment-marker ac:ref="60547a15-a3ad-448d-af43-5e98a7e8f3ff">You need to build a </ac:inline-comment-marker><em><ac:inline-comment-marker ac:ref="60547a15-a3ad-448d-af43-5e98a7e8f3ff">.zip</ac:inline-comment-marker></em><ac:inline-comment-marker ac:ref="60547a15-a3ad-448d-af43-5e98a7e8f3ff"> file containing a diagram descriptor file (e.g., <em>descriptor.xml</em></ac:inline-comment-marker><ac:inline-comment-marker ac:ref="60547a15-a3ad-448d-af43-5e98a7e8f3ff">) and a Resource Manager descriptor file (e.g., <em>MDR_Custom Diagram_MagicDraw_74842_descriptor.xm</em><em>l</em><span style="color: rgb(62,63,64);">.) </span>to be able to share your own custom diagram.</ac:inline-comment-marker> For this, you need to use the <strong>Development Tools</strong> plugin. Once you generate and share the file, the diagram customization can then be imported into the modeling tool by another user via the <strong>Resource Manager </strong>for future use and accessibility. </p><p><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="cf5b8bcc-78e7-416b-a481-a4cb9bb09c9e"><ac:parameter ac:name="title">Warning</ac:parameter><ac:rich-text-body><p>You can build a <em>.zip</em> file for custom diagram distribution <ac:inline-comment-marker ac:ref="e138a9a9-2a19-4a0a-b561-37fa6c4738c6">only after</ac:inline-comment-marker> you have <ac:link><ri:page ri:content-title="Creating new diagram type" /><ac:link-body>created a new<span> diagram type</span></ac:link-body></ac:link> or edited an existing standard diagram.</p></ac:rich-text-body></ac:structured-macro><p>To create a <em>.zip</em> file using the <strong>Development Tools</strong> plugin</p><hr /><ol><li><ac:inline-comment-marker ac:ref="4ad3836a-5451-4c2d-9781-c716582b08f0">On your local file system,</ac:inline-comment-marker> create the following folders structure: <em>...\&lt;Custom Diagram Resource&gt;\data\default<ac:inline-comment-marker ac:ref="176a7421-9e59-4b0a-8345-332a8a3bd37b">s\data\diagrams</ac:inline-comment-marker></em><ac:inline-comment-marker ac:ref="176a7421-9e59-4b0a-8345-332a8a3bd37b">.</ac:inline-comment-marker><br /><ac:inline-comment-marker ac:ref="176a7421-9e59-4b0a-8345-332a8a3bd37b"><ac:image><ri:attachment ri:filename="custom_diagram_resource_folders_structure.png" /></ac:image><br /></ac:inline-comment-marker></li><li>Launch the modeling tool. </li><li>Do one of the following: <ul><li><ac:inline-comment-marker ac:ref="3c2d772e-abb8-40d8-a463-f017fa5bbb44"><br /></ac:inline-comment-marker><ol><li><ac:inline-comment-marker ac:ref="3c2d772e-abb8-40d8-a463-f017fa5bbb44">In the main menu, go to <strong>Help</strong> &gt; <strong>About</strong>. </ac:inline-comment-marker></li><li><ac:inline-comment-marker ac:ref="3c2d772e-abb8-40d8-a463-f017fa5bbb44">Next to </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="3c2d772e-abb8-40d8-a463-f017fa5bbb44">Configuration Files</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="3c2d772e-abb8-40d8-a463-f017fa5bbb44">,</ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="3c2d772e-abb8-40d8-a463-f017fa5bbb44"> </ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="3c2d772e-abb8-40d8-a463-f017fa5bbb44"><ac:inline-comment-marker ac:ref="3c2d772e-abb8-40d8-a463-f017fa5bbb44">click the file location path. The configuration files folder opens.</ac:inline-comment-marker></ac:inline-comment-marker></li><li>Under <em style="letter-spacing: 0.0px;">&lt;configuration files&gt;\data\diagrams,</em><span style="letter-spacing: 0.0px;"> locate your custom diagram folder containing a descriptor</span><span style="letter-spacing: 0.0px;">.</span></li></ol></li><li><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;"><br /></span></p><ol><li><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;">In the main menu, go to<strong> Diagrams</strong> &gt;<strong> Customize</strong>.</span></p></li><li><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;">In the <strong>Customize Diagrams</strong> dialog, select the custom diagram whose descriptor file you want to export and click the<strong> Export</strong> button. </span></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="04cb718a-579a-47d8-98e3-1635280cb9e0"><ac:parameter ac:name="title">Warning</ac:parameter><ac:rich-text-body><p>Before the export operation, create a new folder on your local file system and give it the name of your custom diagram, such as <em>Custom Diagram</em>. The exported descriptor file needs to be renamed to <em>descriptor.xml </em>and saved in this newly-created folder.</p></ac:rich-text-body></ac:structured-macro></li></ol></li></ul></li><li><p class="auto-cursor-target"><ac:inline-comment-marker ac:ref="3c2d772e-abb8-40d8-a463-f017fa5bbb44">Copy and paste the custom diagram folder together with the descriptor file into the folders structure you created in the </ac:inline-comment-marker><ac:inline-comment-marker ac:ref="3c2d772e-abb8-40d8-a463-f017fa5bbb44">first</ac:inline-comment-marker><ac:inline-comment-marker ac:ref="3c2d772e-abb8-40d8-a463-f017fa5bbb44"> step.</ac:inline-comment-marker><span style="letter-spacing: 0.0px;"> </span><br /><span style="letter-spacing: 0.0px;"><ac:image><ri:attachment ri:filename="custom_diagram_folder_with_a_descriptor.png" /></ac:image><br /></span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="6ed1c88c-36c9-4093-ba1b-89777c42636b"><ac:parameter ac:name="title">Distributing Profiles</ac:parameter><ac:rich-text-body><p>If you have specified P<ac:inline-comment-marker ac:ref="63b4a73c-08ff-4f59-8a60-db89fba517a6">rofiles w</ac:inline-comment-marker>hen <ac:link><ri:page ri:content-title="Customizing diagrams" /><ac:plain-text-link-body><![CDATA[customizing a diagram]]></ac:plain-text-link-body></ac:link>, it is highly recommended that you distribute them together with your custom diagram. For this, create the <em>Profiles</em> folder under the custom diagram resource root folder and place all required Profiles in it before generating a <em>.zip </em>archive.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="520947aa-aa71-4079-9342-e66b046aa82b"><ac:rich-text-body><p>You need to mark each Profile distributed together with a custom resource as<strong> Standard/System Profile</strong> (<strong>File</strong> &gt;<strong> Project Properties</strong> &gt; <strong>More</strong> &gt;<strong> Standard/System Profile</strong>) to store it locally. Profiles stored on the server cannot be used for a custom diagram.</p></ac:rich-text-body></ac:structured-macro><p><ac:image ac:align="center"><ri:attachment ri:filename="profiles_folder.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro></li><li>Download and <ac:link><ri:page ri:space-key="ILTWRT" ri:content-title="Installing modeling tools and plugins" /><ac:plain-text-link-body><![CDATA[install]]></ac:plain-text-link-body></ac:link> the <strong>Development Tools</strong> plugin. </li><li>Restart the modeling tool.</li><li>In the main menu, click <strong>Tools</strong> &gt; <strong>Development Tools</strong> &gt; <strong>Build Custom Resource</strong>.</li><li>In the <strong>Custom Resource Building Wizard</strong>, set the custom diagram<em> </em>folder as the <strong>Resource </strong><strong>Folder</strong>. </li><li>Click<strong> Next</strong> to skip the other steps and then click <strong><ac:inline-comment-marker ac:ref="e7e5bbb4-c15b-4440-bf69-d213b65a12ea">Finish</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="e7e5bbb4-c15b-4440-bf69-d213b65a12ea">.</ac:inline-comment-marker> <br /><ac:inline-comment-marker ac:ref="6f76b360-0567-4631-8448-0e5ddfef8e2c"><ac:inline-comment-marker ac:ref="75f63a8f-837b-433a-9320-a72728e616a7">The resource (</ac:inline-comment-marker></ac:inline-comment-marker><em><ac:inline-comment-marker ac:ref="6f76b360-0567-4631-8448-0e5ddfef8e2c"><ac:inline-comment-marker ac:ref="75f63a8f-837b-433a-9320-a72728e616a7">.</ac:inline-comment-marker></ac:inline-comment-marker></em><em><ac:inline-comment-marker ac:ref="6f76b360-0567-4631-8448-0e5ddfef8e2c"><ac:inline-comment-marker ac:ref="75f63a8f-837b-433a-9320-a72728e616a7">zip</ac:inline-comment-marker></ac:inline-comment-marker></em><ac:inline-comment-marker ac:ref="6f76b360-0567-4631-8448-0e5ddfef8e2c"><ac:inline-comment-marker ac:ref="75f63a8f-837b-433a-9320-a72728e616a7"> file) is built.</ac:inline-comment-marker> It can now be distributed and <ac:link ac:anchor="Importing resource using Resource Manager"><ri:page ri:space-key="MDTWRT" ri:content-title="Resource Manager" /><ac:plain-text-link-body><![CDATA[imported into the modeling tool using the Resource Manager]]></ac:plain-text-link-body></ac:link>. </ac:inline-comment-marker></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="66a4e43d-0041-4421-82f5-7b4164fa33cc"><ac:parameter ac:name="title">Info</ac:parameter><ac:rich-text-body><p>A created custom diagram resource (.<em>zip</em>) can be bundled into the resource distribution file (.<em>rdzip</em>) using the <strong>Development Tools</strong> plugin for distribution alongside other resources. <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Building a resource distribution file" /><ac:plain-text-link-body><![CDATA[Learn more about building a resource distribution file>>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><h3>Distributing custom diagrams using Customize Diagrams dialog</h3><p>You can export the custom diagram descriptor (.<em>xml</em>) file directly into the<strong> Customize Diagrams</strong> dialog. The exported file can then be shared with others and imported into the modeling tool by another user via the same <strong>Customize Diagrams</strong> dialog using the <strong>Import </strong>command. </p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="71ad1e09-7273-4ba2-9f50-9333cfe89384"><ac:parameter ac:name="title">Warning</ac:parameter><ac:rich-text-body><p>You can export an .<em>xml </em>file for custom diagram distribution only after <span>you have </span><ac:link><ri:page ri:content-title="Creating new diagram type" /><ac:plain-text-link-body><![CDATA[created a new diagram type]]></ac:plain-text-link-body></ac:link><span style="color: rgb(62,63,64);"> or edited an existing standard diagram.</span></p></ac:rich-text-body></ac:structured-macro><p>To export a custom diagram descriptor </p><hr /><ol><li>In the main menu, go to <strong>Diagrams</strong> &gt; <strong>Customize</strong>.</li><li>Select a custom diagram from the list and click the <strong>Export </strong>button.<br /><ac:image><ri:attachment ri:filename="exporting_diagram_descriptor.png" /></ac:image></li></ol><p>The .<em>xml</em> file is exported. You can now distribute it.</p><p><br /></p><p>To import a custom diagram descriptor into the modeling tool</p><hr /><ol><li>In the main menu, go to <strong>Diagrams</strong> &gt; <strong>Customize</strong>. </li><li><p class="auto-cursor-target">Click the <strong>Import</strong> button and point to a descriptor (.<em>xml</em>)<em> </em>on your local file system.</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="importing_descriptor_file.png" /></ac:image></p></li></ol><p>The <em>.xml</em> file is imported, and a new diagram type appears under <strong>Custom</strong> <strong>Diagrams </strong>in the <strong>Customize Diagrams</strong> dialog.<strong> </strong></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973714 space=UPDG version=1 -->
## PAGE 00186: Distributing Profiles

- page_id: `243973714`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973714/Distributing+Profiles
- version_number: 1
- version_date: `2025-07-31T19:04:52.024+02:00`
- ancestors: UML Profiling and DSL Guide
- labels: []

### NORMALIZED CONTENT

1777779865

1777779876

1777779866

You can distribute profiles with included customization data in the following two ways:

- Exchanging Profiles via XMI
- [CONFLUENCE_PAGE title='Resource Manager' space='MDTWRT']

###### Exchanging Profiles via XMI

Using UML XMI interchange mechanisms it is possible to interchange profiles between tools, together with models to which they have been applied. A profile must therefore be defined as an interchangeable UML model. In addition to exchanging profiles together with models between tools, profile application should also be definable “by reference”; that is, a profile does not need to be interchanged if it is already present in the importing tool.

1777779864

**Related pages**

- Resource Manager
- Distributing Resources

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="87793084-6dda-4cfa-a93a-71ed6e92e598"><ac:parameter ac:name="id">1777779865</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="623df8d3-5c05-474a-8a9d-08341a53128b"><ac:parameter ac:name="id">1777779876</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="80193487-d813-40f5-82ac-63cba23f2518"><ac:parameter ac:name="id">1777779866</ac:parameter><ac:rich-text-body><p>You can distribute profiles with included customization data in the following two ways:</p><ul><li>Exchanging Profiles via XMI</li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Resource Manager" /><ac:plain-text-link-body><![CDATA[Distributing Resources by Using Resource Manager]]></ac:plain-text-link-body></ac:link></li></ul><h4>Exchanging Profiles via XMI</h4><p>Using UML XMI interchange mechanisms it is possible to interchange profiles between tools, together with models to which they have been applied. A profile must therefore be defined as an interchangeable UML model. In addition to exchanging profiles together with models between tools, profile application should also be definable “by reference”; that is, a profile does not need to be interchanged if it is already present in the importing tool.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8d9b39b1-01b7-482f-aeab-0c421c83f8d4"><ac:parameter ac:name="id">1777779864</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><a href="https://docs.nomagic.com/display/MDTWRT/Resource+Manager">Resource Manager</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Distributing+Resources">Distributing Resources</a></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973573 space=UPDG version=1 -->
## PAGE 00187: Do Not Suggest As Type

- page_id: `243973573`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973573/Do+Not+Suggest+As+Type
- version_number: 1
- version_date: `2025-07-31T19:04:48.541+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data > Customization Elements
- labels: []

### NORMALIZED CONTENT

Excludes elements from being suggested as a type in the list dialogs.

To exclude a DSL element from the list dialogs

1. In the Customization [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] , click the Customization Target property.
2. Click the [IMAGE alt='' src=''] button. The element [CONFLUENCE_PAGE title='Selection in diagrams' space='MDTWRT'] dialog appears.
3. Select a stereotype or a metaclass.
4. Click OK to close the dialog.
5. Set the Hide Metatype property to true .
6. Set the Do Not Suggest As Type property to true .
7. Click Close .
8. Reopen the project. Elements or metaclasses selected in the third step of this procedure are not listed in the list dialogs. For example, in the Property [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'], click the Type property and then the [IMAGE alt='' src=''] button. In the element [CONFLUENCE_PAGE title='Selection in diagrams' space='MDTWRT'] dialog, the elements or metaclasses selected as **customization targets** will not be displayed.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Customization Elements' space='']
- [CONFLUENCE_PAGE title='Customization Element Properties Description' space='']
- [CONFLUENCE_PAGE title='Customization Target' space='']
- [CONFLUENCE_PAGE title='Creating your First Customization' space='']
- [CONFLUENCE_PAGE title='Creating and specifying derived properties' space='']
- [CONFLUENCE_PAGE title='Defining expressions' space='']
- [CONFLUENCE_PAGE title='Hide Metatype' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p><div class="layoutArea"><div class="column"><p><span>Excludes elements from being suggested as a type in the list dialogs.</span></p><p>To exclude a DSL element from the list dialogs</p><hr /><ol><li><span>In the </span> <strong>Customization </strong> <span><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link></span> <span>, click the </span> <strong> Customization Target </strong> <span>property. </span></li><li><span>Click the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="edit.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image> button. The element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Selection in diagrams" /><ac:plain-text-link-body><![CDATA[Selection]]></ac:plain-text-link-body></ac:link> dialog appears. </span></li><li>Select a stereotype or a metaclass.</li><li><span>Click </span> <strong>OK </strong>to close the dialog.</li><li><span>Set the </span> <strong>Hide Metatype </strong> <span>property to </span> <em>true</em> <span>. </span></li><li><span>Set the </span> <strong>Do Not Suggest As Type </strong> <span>property to </span> <em>true</em>.</li><li><span>Click </span> <span>Close</span>.</li><li><span>Reopen the project. Elements or metaclasses selected in the third step of this </span> <span>procedure are not listed in the list dialogs. For example, in the </span> <strong>Property </strong> <span> <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>, click the </span> <strong>Type </strong> <span>property and then the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="edit.png" /></ac:image> button. In the element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Selection in diagrams" /><ac:plain-text-link-body><![CDATA[Selection]]></ac:plain-text-link-body></ac:link> dialog, the elements or </span> <span>metaclasses selected as <strong>customization targets</strong> will not be displayed. </span></li></ol><p><span> <br /> </span></p></div></div></ac:layout-cell><ac:layout-cell><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="68d6f843-19aa-480d-81e1-df3547d11a1b"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Elements" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Element Properties Description" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Target" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating your First Customization" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating and specifying derived properties" /></ac:link></li><li><ac:link><ri:page ri:content-title="Defining expressions" /></ac:link></li><li><ac:link><ri:page ri:content-title="Hide Metatype" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973576 space=UPDG version=1 -->
## PAGE 00188: Do Not Suggest Name Auto Completion

- page_id: `243973576`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973576/Do+Not+Suggest+Name+Auto+Completion
- version_number: 1
- version_date: `2025-07-31T19:04:48.636+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data > Customization Elements
- labels: []

### NORMALIZED CONTENT

The property is useful when you do not want to display the name auto completion list for DSL elements typically displayed only in one diagram, or if the names of the DSL elements are full sentences or fragments of sentences.

To hide the name auto completion list

1. In the [CONFLUENCE_PAGE title='Customizing Specification Window' space=''] , click the [CONFLUENCE_PAGE title='Customization Target' space=''] property and then select a customization target.
2. Set the Do Not Suggest Name Auto Completion property to true .
3. Reopen the project.

[IMAGE alt='' src='']

###### Example of name auto completion list that appears when typing a DSL element name.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Customization Elements' space='']
- [CONFLUENCE_PAGE title='Customization Element Properties Description' space='']
- [CONFLUENCE_PAGE title='Customization Target' space='']
- [CONFLUENCE_PAGE title='Creating your First Customization' space='']
- [CONFLUENCE_PAGE title='Creating and specifying derived properties' space='']
- [CONFLUENCE_PAGE title='Defining expressions' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p><div class="layoutArea"><div class="column"><p>The property is useful when you do not want to display the name auto completion list for DSL elements typically displayed only in one diagram, or if the names of the DSL elements are full sentences or fragments of sentences.</p><div class="layoutArea"><div class="column"><p><br /></p><p>To hide the name auto completion list</p><hr /><ol><li>In the <ac:link><ri:page ri:content-title="Customizing Specification Window" /><ac:plain-text-link-body><![CDATA[Customization Specification window]]></ac:plain-text-link-body></ac:link>, click the <ac:link><ri:page ri:content-title="Customization Target" /></ac:link> property and then select a customization target.</li><li>Set the <strong>Do Not Suggest Name Auto Completion</strong> property to <em>true</em>. </li><li>Reopen the project. </li></ol></div></div></div><p><ac:image ac:align="center"><ri:attachment ri:filename="auto_completion.png" /></ac:image></p><h6 style="text-align: center;">Example of name auto completion list that appears when typing a DSL element name.</h6><p><br /></p></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="68d6f843-19aa-480d-81e1-df3547d11a1b"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Elements" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Element Properties Description" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Target" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating your First Customization" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating and specifying derived properties" /></ac:link></li><li><ac:link><ri:page ri:content-title="Defining expressions" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973551 space=UPDG version=1 -->
## PAGE 00189: Domain Specific Language customization

- page_id: `243973551`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973551/Domain+Specific+Language+customization
- version_number: 1
- version_date: `2025-07-31T19:04:48.086+02:00`
- ancestors: UML Profiling and DSL Guide
- labels: []

### NORMALIZED CONTENT

1679637636

1679637647

1679637637

DSL (Domain Specific Language) customization is a model-driven approach, based on UML profiling. Our modeling tool provides the ability to use DSL engine for adapting domain specific profiles to create your own custom specification windows, custom real-time semantic rules and others. In other words, you can create specialized domain specific tool and hide UML underneath.

The modeling tool's DSL customization engine is able to process user defined rules for DSL elements and reflect this in GUI and diagrams behavior.

The topics in this section show you how to create a new DSL element, how to customize its Specification window, shortcut menu, how to create customization rules for relationships drawing, how to customize possible owned elements, how to create numbering customization, how to extend metamodel with derived properties and others.

1679637635

**Related Pages**

- Creating Customization Data
- Using Customization Data

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3857842e-f4de-4cc8-88b3-9b37f48e794d"><ac:parameter ac:name="id">1679637636</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="e37ee9da-75c7-4902-b324-9bb7a67abd66"><ac:parameter ac:name="id">1679637647</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a48e1dc2-89f3-43cf-992d-c5d9795e7351"><ac:parameter ac:name="id">1679637637</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p><span>DSL (Domain Specific Language) customization is a model-driven approach, based on UML profiling. Our modeling tool provides the ability to use DSL engine for adapting domain specific profiles to create your own custom specification windows, custom real-time semantic rules and others. In other words, you can create specialized domain specific tool and hide UML underneath. </span></p><p><span>The modeling tool's DSL customization engine is able to process user defined rules for DSL elements and reflect this in GUI and diagrams behavior. </span></p><p><span>The topics in this section show you how to create a new DSL element, how to customize its Specification window, shortcut menu, how to create customization rules for relationships drawing, how to customize possible owned elements, how to create numbering customization, how to extend metamodel with derived properties and others. </span></p><p><br /></p></div></div></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e1cc433f-370a-46f8-b593-c5c0343d85cc"><ac:parameter ac:name="id">1679637635</ac:parameter><ac:rich-text-body><p><strong>Related Pages</strong></p><ul class="list-children not-expandable"><li> <a href="https://docs.nomagic.com/display/MDTWRT/Creating+Customization+Data">Creating Customization Data</a></li><li> <a href="https://docs.nomagic.com/display/MDTWRT/Using+Customization+Data">Using Customization Data</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973703 space=UPDG version=1 -->
## PAGE 00190: Expressions merge

- page_id: `243973703`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973703/Expressions+merge
- version_number: 1
- version_date: `2025-07-31T19:04:51.768+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Extending Metamodel with Derived Properties
- labels: []

### NORMALIZED CONTENT

1852110634

1852110637

1852110636

Suppose you have two customization elements extending the same UML element (for example, the same element specified as a customization target in both customization elements). Each customization element has a derived property. If the derived properties’ names, types, and multiplicities are the same, then the expressions defined for these derived properties are merged. Consequently, the extended UML element will have only one derived property instead of two and the property values will be calculated according to the union of expressions defined in both derived properties.

This occurs when the derived property (already specified in, for example, the UML Standard Profile) is also specified in a project. Note that in contrast to the example above the real-life expression merge can be performed in more complex situations with more than two derived properties having more than one expression defined. The expression merge can combine different types of expressions.

1852110633

**Related Pages**

- Extending Metamodel with Derived Properties
- Using Customization Data
- Creating Customization Data

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="05b88989-4cb1-4009-9c1a-b008bc772ac2"><ac:parameter ac:name="id">1852110634</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="5d959b93-f142-4719-94c0-1c646dff57db"><ac:parameter ac:name="id">1852110637</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f6a00dea-335a-4033-bdee-fbef99967679"><ac:parameter ac:name="id">1852110636</ac:parameter><ac:rich-text-body><p>Suppose you have two customization elements extending the same UML element (for example, the same element specified as a customization target in both customization elements). Each customization element has a derived property. If the derived properties’ names, types, and multiplicities are the same, then the expressions defined for these derived properties are merged. Consequently, the extended UML element will have only one derived property instead of two and the property values will be calculated according to the union of expressions defined in both derived properties.</p><p>This occurs when the derived property (already specified in, for example, the UML Standard Profile) is also specified in a project. Note that in contrast to the example above the real-life expression merge can be performed in more complex situations with more than two derived properties having more than one expression defined. The expression merge can combine different types of expressions.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="769562e9-b220-4b8c-92d0-be622953898d"><ac:parameter ac:name="id">1852110633</ac:parameter><ac:rich-text-body><p><strong>Related Pages</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MDTWRT/Extending+Metamodel+with+Derived+Properties">Extending Metamodel with Derived Properties</a></li><li class="ancestor-link"><a href="https://docs.nomagic.com/display/MDTWRT/Using+Customization+Data">Using Customization Data</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Creating+Customization+Data">Creating Customization Data</a></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973694 space=UPDG version=1 -->
## PAGE 00191: Extending Metamodel with Derived Properties

- page_id: `243973694`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973694/Extending+Metamodel+with+Derived+Properties
- version_number: 1
- version_date: `2025-07-31T19:04:51.496+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data
- labels: []

### NORMALIZED CONTENT

1851478267

1851478269

1851478268

DSL customization allows extending the UML metamodel or its profile (such as SysML or UPDM) by creating new read-only derived properties.

A derived property's values are automatically calculated from the other properties’ values.

Derived properties are calculated on the fly. The modeling tool analyzes the derived properties and calculates them for existing model elements (when loading a model) and dynamically updates them according to model changes.

Derived properties can be added either to the standard UML elements, or to the ones extended with stereotypes. To extend the metamodel with the derived properties, there is no need to apply the stereotypes: the metamodel is extended in runtime.

Define derived properties using different expression types: Simple, Meta Chain, OCL, and Binary (reference to java code).

Easily access derived properties of a select model element, navigate to its specifications, or use the derived properties in model analysis tools (dependency matrices, report templates, and relation maps).

[IMAGE alt='' src='']

###### Derived properties specification metamodel.

1851478266

**Related pages**

- [CONFLUENCE_PAGE title='Creating and specifying derived properties' space='']
- Defining expressions
- Recursive properties
- Expressions merge
- Derived properties visibility

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9edc5bb4-5006-46c0-ad3d-4ff55b5bb33c"><ac:parameter ac:name="id">1851478267</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="bb2c1378-6bdd-40d2-9173-aaeb6a87c8c9"><ac:parameter ac:name="id">1851478269</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4a1bee9a-36c6-4021-bda0-7204c8940d1d"><ac:parameter ac:name="id">1851478268</ac:parameter><ac:rich-text-body><p>DSL customization allows extending the UML metamodel or its profile (such as SysML or UPDM) by creating new read-only derived properties. </p><p>A derived property's values are automatically calculated from the other properties’ values.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8159d580-66e4-4e3d-98e4-03056d47567a"><ac:rich-text-body><p>Derived properties are calculated on the fly. The modeling tool analyzes the derived properties and calculates them for existing model elements (when loading a model) and dynamically updates them according to model changes. </p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>Derived properties can be added either to the standard UML elements, or to the ones extended with stereotypes. To extend the metamodel with the derived properties, there is no need to apply the stereotypes: the metamodel is extended in runtime. </p><p>Define derived properties using different expression types: Simple, Meta Chain, OCL, and Binary (reference to java code). </p><p>Easily access derived properties of a select model element, navigate to its specifications, or use the derived properties in model analysis tools (dependency matrices, report templates, and relation maps).</p><p><ac:image ac:align="center" ac:title="Derived properties specification metamodel" ac:alt="Derived properties specification metamodel"><ri:attachment ri:filename="domain_model_for_derived_properties.png" /></ac:image></p><h6 style="text-align: center;">Derived properties specification metamodel.</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c518abbb-16aa-46ca-92b3-89dd44868630"><ac:parameter ac:name="id">1851478266</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul class="childpages-macro"><li><ac:link><ri:page ri:content-title="Creating and specifying derived properties" /></ac:link></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Defining+expressions">Defining expressions</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Recursive+properties">Recursive properties</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Expressions+merge">Expressions merge</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Derived+properties+visibility">Derived properties visibility</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973500 space=UPDG version=1 -->
## PAGE 00192: Grouping Tags inside Stereotype

- page_id: `243973500`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973500/Grouping+Tags+inside+Stereotype
- version_number: 1
- version_date: `2025-07-31T19:04:47.212+02:00`
- ancestors: UML Profiling and DSL Guide > Working with Profiles > Creating Profiles
- labels: []

### NORMALIZED CONTENT

When a stereotype has many properties, it is very useful to group these properties into named groups. For this purpose, every property could have a tagged value with its group name.

To group tags

1. Open the [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] of the stereotype property.
2. Click the **Tags** property group.
3. Select the **groupName** property and assign a value for it:
  1. Click the **Edit Value** button
  2. In the **Value** area, type a group name. . [ATTACHMENT filename='creating_property_group.png']
4. Repeat these steps for every stereotype property.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Applying Stereotypes' space='']
- [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT']
- [CONFLUENCE_PAGE title='Tag' space='MDTWRT']
- [CONFLUENCE_PAGE title='Specification window' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span>When a stereotype has many properties, it is very useful to group these properties into named groups. For this purpose, every property could have a tagged value with its group name. </span></p><p><span>To group tags</span></p><hr /><ol><li><span>Open the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link> of the stereotype property.</span></li><li><span>Click the <strong>Tags</strong> property group.</span></li><li><span>Select the <strong>groupName</strong> property and assign a value for it:</span><ol><li><span>Click the <strong>Edit Value</strong> button</span></li><li><span>In the <strong>Value </strong> area, type a group name.</span><br /><br />.<ac:image><ri:attachment ri:filename="creating_property_group.png" /></ac:image></li></ol></li><li>Repeat these steps for every stereotype property. </li></ol></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b14401e6-4bad-4948-8ab5-88b81d7034fe"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Applying Stereotypes" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Tag" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973575 space=UPDG version=1 -->
## PAGE 00193: Hide Metatype

- page_id: `243973575`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973575/Hide+Metatype
- version_number: 1
- version_date: `2025-07-31T19:04:48.593+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data > Customization Elements
- labels: []

### NORMALIZED CONTENT

Indicates whether the customized stereotype is recognized as a new type. If the **Hide Metatype** property value is *false*, the DSL element is *not* considered as a new type element and will not be displayed in the shortcut menus (see the **Possible Owners** property).

To define the hide metatype property

1. In the [CONFLUENCE_PAGE title='Customizing Specification Window' space='']**Customization** Specification window, click the [CONFLUENCE_PAGE title='Customization Target' space='']**Customization Target** property and then select a customization target.
2. Set the **Hide Metatype** property to *true*.
3. Reopen the project.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Customization Elements' space='']
- [CONFLUENCE_PAGE title='Customization Element Properties Description' space='']
- [CONFLUENCE_PAGE title='Customization Target' space='']
- [CONFLUENCE_PAGE title='Creating your First Customization' space='']
- [CONFLUENCE_PAGE title='Creating and specifying derived properties' space='']
- [CONFLUENCE_PAGE title='Defining expressions' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span style="color: rgb(0,0,0);">Indicates whether the customized stereotype is recognized as a new type. If the <strong>Hide Metatype</strong> property value is <em>false</em>, the DSL element is <em>not</em> considered as a new type element and will not be displayed in the shortcut menus (see the <strong>Possible Owners</strong> property).</span></p><p><span style="color: rgb(0,0,0);"> <br /> </span></p><div class="layoutArea"><div class="column"><p><span style="color: rgb(0,0,0);">To define the hide metatype property</span></p><hr /><ol><li><span style="color: rgb(0,0,0);">In the <ac:link><ri:page ri:content-title="Customizing Specification Window" /><ac:link-body> <strong>Customization</strong> Specification window</ac:link-body></ac:link>, click the <ac:link><ri:page ri:content-title="Customization Target" /><ac:link-body> <strong>Customization Target</strong> </ac:link-body></ac:link> property and then select a customization target.</span></li><li><span style="color: rgb(0,0,0);">Set the <strong>Hide Metatype</strong> property to <em>true</em>.</span></li><li><span style="color: rgb(0,0,0);">Reopen the project.</span></li></ol></div></div></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="68d6f843-19aa-480d-81e1-df3547d11a1b"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Elements" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Element Properties Description" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Target" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating your First Customization" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating and specifying derived properties" /></ac:link></li><li><ac:link><ri:page ri:content-title="Defining expressions" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973640 space=UPDG version=1 -->
## PAGE 00194: Initializing a Custom Model

- page_id: `243973640`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973640/Initializing+a+Custom+Model
- version_number: 1
- version_date: `2025-07-31T19:04:50.361+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data
- labels: []

### NORMALIZED CONTENT

With DSL customization, you can modify a model element to act according to your needs depending on the stereotype you apply.

###### Default values

[CONFLUENCE_PAGE title='Tag' space='MDTWRT'] have default values. Use the default values when you create the tag, making sure its definition has multiplicity greater than zero. In this case it is automatically created when applying a stereotype.

###### Stereotypes on relationship ends

At times, DSL requires applying [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT']to some elements after DSL relationship connection to those elements.

Use the following properties for this purpose:

| Property | Description |
| --- | --- |
| Apply to Source | Specifies stereotypes that must be applied to the source element of this relationship after connection. |
| Apply to Target | Specifies stereotypes that must be applied to the target element of this relationship after connection. |

#### INFO: Source and Target in an example

Source and Target in an example

“Source” and “Target” are respectively the “source” and “target” of a directed relationship.

The first connected element acts as a“source” for a non-directed relationship.

Example:

1. Create a stereotype «serve» and select the Dependency metaclass.
2. Create two stereotypes «main» and «servant» and select the Element metaclass.
3. Create a customization element.
4. In the customization [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] , specify the following property values:
  1. for the Customization Target property, select the «serve» stereotype,
  2. for the Apply To Source property, select the «main» stereotype,
  3. for the Apply To Target property, select the «servant» stereotype.
5. Reopen the project. Draw the «serve» dependency from one element to another. The «main» and «servant» stereotypes are applied to these elements.

###### Required Generalization or Interface Realization

Sometimes DSL requires elements to be subtypes of a general abstract [CONFLUENCE_PAGE title='Class' space='MDTWRT']or [CONFLUENCE_PAGE title='Interface' space='MDTWRT']. Use the **Super Types**property for this purpose. The **Super Types** property specifies types to be super types of the DSL element. The*Generalization*or*InterfaceRealization*(if using an interface) will be created in the model after applying the customized stereotype.

#### INFO: Example

Example

The following is an example of customization. Every JAVA class will be a subclass of the *Object*class. In other words, every Class marked with the «JAVAClass» stereotype is inherited from the Object.

1. Create a customization element.
2. In the customization Specification window, specify the **Customization Target**property as the «JAVAClass» stereotype.
3. In the customization Specification window, specify the **Super Types**property as the *Object* class.

#### PANEL: On this page

On this page

44

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Model' space='MDTWRT']
- [CONFLUENCE_PAGE title='Tag' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span>With DSL customization, you can modify a model element to act according to your needs depending on the stereotype you apply.</span></p><h4>Default values</h4><p><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Tag" /><ac:plain-text-link-body><![CDATA[Tags]]></ac:plain-text-link-body></ac:link> have default values. Use the default values when you create the tag, making sure its definition has multiplicity greater than zero. In this case it is automatically created when applying a stereotype. </p><h4 class="with-breadcrumbs">Stereotypes on relationship ends</h4><p>At times, DSL requires applying <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotypes ]]></ac:plain-text-link-body></ac:link>to some elements after DSL relationship connection to those elements.</p><p>Use the following properties for this purpose:</p><table class="wrapped"><colgroup><col /><col /></colgroup><thead><tr><th><p>Property</p></th><th><p>Description</p></th></tr></thead><tbody><tr><td><strong>Apply to Source</strong></td><td><p>Specifies stereotypes that must be applied to the source element of this relationship after connection. </p></td></tr><tr><td colspan="1"><strong>Apply to Target</strong></td><td colspan="1"><p>Specifies stereotypes that must be applied to the target element of this relationship after connection. </p></td></tr></tbody></table><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c8a0fe03-8493-4af3-81af-9bfa69a2f37b"><ac:parameter ac:name="title">Source and Target in an example</ac:parameter><ac:rich-text-body><p>“Source” and “Target” are respectively the “source” and “target” of a directed relationship.</p><p>The first connected element acts as a“source” for a non-directed relationship.</p><p>Example:</p><ol><li>Create a stereotype <em>«serve»</em> and select the Dependency metaclass.</li><li>Create two stereotypes<em> «main»</em> and <em>«servant»</em> and select the Element metaclass. </li><li>Create a customization element.</li><li>In the customization <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>, specify the following property values: <ol><li>for the <strong>Customization Target</strong> property, select the<em> «serve»</em> stereotype, </li><li>for the <strong>Apply To Source</strong> property, select the <em>«main»</em> stereotype, </li><li>for the <strong>Apply To Target</strong> property, select the <em>«servant»</em> stereotype. </li></ol></li><li>Reopen the project. Draw the <em>«serve»</em> dependency from one element to another. The <em>«main»</em> and <em>«servant»</em> stereotypes are applied to these elements. </li></ol></ac:rich-text-body></ac:structured-macro><p><br /></p><h4 class="with-breadcrumbs">Required Generalization or Interface Realization</h4><p>Sometimes DSL requires elements to be subtypes of a general abstract <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Class" /><ac:plain-text-link-body><![CDATA[class ]]></ac:plain-text-link-body></ac:link>or <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Interface" /><ac:plain-text-link-body><![CDATA[interface]]></ac:plain-text-link-body></ac:link>. Use the <strong>Super Types </strong>property for this purpose. The <strong>Super Types</strong> property s<span>pecifies types to be super types of the DSL element. The </span><em>Generalization </em><span>or </span><em>InterfaceRealization </em><span>(if using an interface) will be created in the model after applying the customized stereotype.</span></p><p class="title"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="01a887db-39d5-4714-bf98-cda4d0edb5df"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p>The following is an example of customization. Every JAVA class will be a subclass of the <em>Object </em>class. In other words, every Class marked with the «JAVAClass» stereotype is inherited from the Object.</p><ol><li><p>Create a customization element.</p></li><li><p>In the customization Specification window, specify the <strong>Customization Target </strong>property as the «JAVAClass» stereotype.</p></li><li><p>In the customization Specification window, specify the <strong>Super Types </strong>property as the <em>Object</em> class. </p></li></ol></ac:rich-text-body></ac:structured-macro><p class="title auto-cursor-target"><br /></p></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="125cbb27-ef07-4f96-a991-9413ef20e9aa"><ac:parameter ac:name="title">On this page</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="35330ce1-f9b9-46a1-998f-48f5a21510e5"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="68d6f843-19aa-480d-81e1-df3547d11a1b"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Model" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Tag" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973495 space=UPDG version=1 -->
## PAGE 00195: Initializing opposite association end

- page_id: `243973495`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973495/Initializing+opposite+association+end
- version_number: 1
- version_date: `2025-07-31T19:04:47.090+02:00`
- ancestors: UML Profiling and DSL Guide > Working with Profiles > Creating Profiles
- labels: []

### NORMALIZED CONTENT

If two stereotypes are connected with an [CONFLUENCE_PAGE title='Association' space='MDTWRT']and there are roles at both ends, the role at one end will be automatically initialized when the opposite role is specified.

#### INFO: Example:

Example:

When «dog» Rex is set as a pet for «human» Tom, Tom will be automatically set as “main” for Rex:

[IMAGE alt='' src='']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT']
- [CONFLUENCE_PAGE title='Association' space='MDTWRT']
- [CONFLUENCE_PAGE title='Association End' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span>If two stereotypes are connected with an <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Association" /><ac:plain-text-link-body><![CDATA[Association ]]></ac:plain-text-link-body></ac:link>and there are roles at both ends, the role at one end will be <span>automatically </span> initialized when the opposite role is specified. </span></p><p><span><br /></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="079e92f2-14af-4600-9586-9e0aabb85b18"><ac:parameter ac:name="title">Example:</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p><span>When «dog» Rex is set as a pet for «human» Tom, Tom will be automatically set as “main” for Rex:</span></p><p><span>  <ac:image><ri:attachment ri:filename="Initializing Opposite Association End.png" /></ac:image><br /> </span></p></div></div></ac:rich-text-body></ac:structured-macro><p><span> <br /> </span></p></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="7c94b9e3-fe28-468c-a38a-773ee720d4ca"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Association" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Association End" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973663 space=UPDG version=1 -->
## PAGE 00196: Merging property groups and subgroups

- page_id: `243973663`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973663/Merging+property+groups+and+subgroups
- version_number: 1
- version_date: `2025-07-31T19:04:51.065+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Creating Property Groups and Subgroups
- labels: []

### NORMALIZED CONTENT

You can specify property groups and subgroups for different customization elements of the same element. That element will have groups and subgroups from all customization elements.

#### INFO: Example

Example

Let’s say we have two customizations of the same element type, the actor. The first customization has the property group *My Group* with the subgroup *Subgroup 1* containing the property *Prop 1*. The second customization has the same property group with the same subgroup specified, but the subgroup *Subgroup 1* contains the property *Prop 2* .

As a result, the actor element type will have *My Group,* with *Subgroup 1* containing both*Prop 1* and *Prop 2*.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Creating Property Groups and Subgroups' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span>You can specify property groups and subgroups for different customization elements of the same element. That element will have groups and subgroups from all customization elements. </span></p><p><span><br /></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d70bdea3-8b22-4fee-9042-256bf3a1707e"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p><span>Let’s say we have two customizations of the same element type, the actor. The first customization has the property group </span> <em><ac:inline-comment-marker ac:ref="63646f21-6f23-4d63-a774-0eed08769f53">My Group</ac:inline-comment-marker> </em> <span>with the subgroup </span> <span><em>Subgroup 1</em> </span> <span>containing the property </span> <em>Prop 1 </em><span>. The second customization has the same property group with the same subgroup specified, but the subgroup </span> <em>Subgroup 1 </em> <span>contains the property </span> <em>Prop 2</em> <span>. </span></p><p>As a result, the actor element type will have <em>My Group,</em> with <em>Subgroup 1</em> containing both<em> Prop 1</em> and <em>Prop 2</em>. </p></div></div></ac:rich-text-body></ac:structured-macro><p><span> <br /> </span></p></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="0e78ddfd-bec9-4837-bd51-242520587f8a"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating Property Groups and Subgroups" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973613 space=UPDG version=1 -->
## PAGE 00197: Meta property substitution (changing name of UML property)

- page_id: `243973613`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973613/Meta+property+substitution+changing+name+of+UML+property
- version_number: 1
- version_date: `2025-07-31T19:04:49.744+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Customizing Specification Window
- labels: []

### NORMALIZED CONTENT

You can customize a standard UML property to represent a more restricted type. You can also rename the property.

###### Property name substitution

The following case study presents an example of property name substitution.

**Case study**

In the DSL element [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'], rename the Name property to *blockName*.

1. [CONFLUENCE_PAGE title='Customization Element Properties' space='']Create a *name* attribute in the customization element.
2. [CONFLUENCE_PAGE title='Applying Stereotypes' space='']Apply the «*metaProperty*» stereotype on the attribute.
3. In the «*metaProperty*» attribute Specification window, click the **New Name** property, and then type a new name *blockName*.
4. To apply the changes, reopen the project.

###### Example of property name substitution.

###### Property description substitution

In the element [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'], the description of the selected property is displayed below the properties list (see the preceding figure). You can customize (change) the property description. For example, after changing the property name (see the Case Study above), you could also change the property description.

[IMAGE alt='' src='']

###### Example of property description area in element Specification window .

****

**Case study**

****

To change the *Name* property description

1. [CONFLUENCE_PAGE title='Customization Element Properties' space=''] in the customization element.
2. [CONFLUENCE_PAGE title='Applying Stereotypes' space='']Apply the «*metaProperty*» stereotype on the attribute.
3. Type a new description in the customization element Specification window, under the description attribute, **Documentation/Hyperlinks** property group. [ATTACHMENT filename='property_description2.png']
4. To apply the changes, save and reopen the project. The description of the *Name* property changes.

[IMAGE alt='' src='']

###### Example of property description substitution.

###### Type substitution (restriction)

To change the type

1. [CONFLUENCE_PAGE title='Customization Element Properties' space='']Create the *type* attribute for the customization element.
2. [CONFLUENCE_PAGE title='Applying Stereotypes' space='']Apply the «*metaProperty*» stereotype.
3. Click the **New Types** property in the type *attribute* Specification window.
4. Specify the «Block» stereotype.
5. To apply the changes, save and reopen the project.

###### Suggesting predefined values

To create properties to list predefined values suggested for the end user (such as "type modifier")

1. [CONFLUENCE_PAGE title='Customization Element Properties' space=''] for the customization element.
2. Name attribute as a property to customize.
3. [CONFLUENCE_PAGE title='Applying Stereotypes' space=''].
4. Enter suggested values into the Suggested Values property.

#### PANEL: On this page

On this page

44

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Customization Element Properties' space='']
- [CONFLUENCE_PAGE title='Customizing Specification Window' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span style="color: rgb(0,0,0);">You can customize a standard UML property to represent a more restricted type. You can also rename the property.<br /></span></p><h4><span style="color: rgb(0,0,0);"> Property name substitution</span></h4><p>The following case study presents an example of property name substitution.</p><p><br /></p><p><span style="color: rgb(0,0,0);"> <strong>Case study</strong> </span></p><p><span style="color: rgb(0,0,0);">In the DSL element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>, rename the Name property to <em>blockName</em>.</span></p><ol><li><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:content-title="Customization Element Properties" /><ac:link-body>Create a <em>name</em> attribute</ac:link-body></ac:link> in the customization element.</span></li><li><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:content-title="Applying Stereotypes" /><ac:link-body>Apply the «<em>metaProperty</em>» stereotype</ac:link-body></ac:link> on the attribute.</span></li><li><span style="color: rgb(0,0,0);">In the «<em>metaProperty</em>» attribute Specification window, click the <strong>New Name</strong> property, and then type a new name <em>blockName</em>. </span></li><li><span style="color: rgb(0,0,0);">To apply the changes, reopen the project.</span></li></ol><ac:image ac:align="center"><ri:attachment ri:filename="property_name_substitution.png" /></ac:image><h6 class="column" style="text-align: center;">Example of property name substitution.</h6><h4 class="column"><span style="color: rgb(0,0,0);">Property description substitution</span></h4><p><span style="color: rgb(0,0,0);">In the element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>, the description of the selected property is displayed below the properties list (see the preceding figure). You can customize (change) the property description. For example, after changing the property name (see the Case Study above), you could also change the property description. </span></p><div class="layoutArea"><div class="column"><div class="layoutArea"><div class="layoutArea"><p><span style="color: rgb(0,0,0);"> <ac:image ac:align="center"><ri:attachment ri:filename="property_description1.png" /></ac:image> </span></p><div class="layoutArea"><h6><span style="color: rgb(0,0,0);"><br /></span></h6><h6 class="column" style="text-align: center;">Example of property description area in element Specification window .</h6></div></div><p><span style="color: rgb(0,0,0);"><strong><br /></strong></span></p><p><br /></p><p><span style="color: rgb(0,0,0);"> <strong>Case study</strong></span></p><p><span style="color: rgb(0,0,0);"><strong><br /></strong></span></p><p><span style="color: rgb(0,0,0);">To change the <em>Name</em> property description</span></p><hr /><ol><li><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:content-title="Customization Element Properties" /><ac:plain-text-link-body><![CDATA[Create a new description attribute]]></ac:plain-text-link-body></ac:link> in the customization element.</span></li><li><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:content-title="Applying Stereotypes" /><ac:link-body>Apply the «<em>metaProperty</em>» stereotype</ac:link-body></ac:link> on the attribute.</span></li><li><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);">Type a new description</span> in the customization element Specification window, under the description attribute, <strong>Documentation/Hyperlinks</strong> property group.</span><br /><span style="color: rgb(0,0,0);"><br /></span><ac:image><ri:attachment ri:filename="property_description2.png" /></ac:image><br /><br /></li><li><span style="color: rgb(0,0,0);">To apply the changes, save and reopen the project. The description of the <em>Name</em> property changes. </span></li></ol><p><span style="color: rgb(0,0,0);"><br /></span></p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="property_description3.png" /></ac:image></p></div></div></div><h6 class="column" style="text-align: center;">Example of property description substitution.</h6><h4 class="layoutArea"><span style="color: rgb(0,0,0);"> Type substitution (restriction)</span></h4><div class="layoutArea"><span style="color: rgb(0,0,0);"><br /></span></div><div class="layoutArea"><span style="color: rgb(0,0,0);">To change the type</span></div><div class="layoutArea"><hr /></div><ol><li class="layoutArea"><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:content-title="Customization Element Properties" /><ac:link-body>Create the <em>type</em> attribute</ac:link-body></ac:link> for the customization element.</span></li><li class="layoutArea"><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:content-title="Applying Stereotypes" /><ac:link-body>Apply the «<em>metaProperty</em>» stereotype</ac:link-body></ac:link>.</span></li><li class="layoutArea"><span style="color: rgb(0,0,0);">Click the <strong>New Types</strong> property in the type <em>attribute</em> Specification window.</span></li><li class="layoutArea"><span style="color: rgb(0,0,0);">Specify the «Block» stereotype.</span></li><li class="layoutArea"><span style="color: rgb(0,0,0);">To apply the changes, save and reopen the project.</span></li></ol><h4 class="layoutArea"><span style="color: rgb(0,0,0);">Suggesting predefined values </span></h4><p class="layoutArea"><span style="color: rgb(0,0,0);">To create properties to list predefined values suggested for the end user (such as &quot;type modifier&quot;)</span></p><hr /><div class="layoutArea"><ol><li><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:content-title="Customization Element Properties" /><ac:plain-text-link-body><![CDATA[Create an attribute]]></ac:plain-text-link-body></ac:link> for the customization element.</span></li><li><span style="color: rgb(0,0,0);">Name attribute as a property to customize.</span></li><li><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:content-title="Applying Stereotypes" /><ac:plain-text-link-body><![CDATA[Apply the «metaProperty» stereotype]]></ac:plain-text-link-body></ac:link>.</span></li><li><span style="color: rgb(0,0,0);">Enter suggested values into the Suggested Values property. </span></li></ol><p><span style="color: rgb(0,0,0);"><br /></span></p></div></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="0746f1bc-2e30-468c-a42f-643411f56660"><ac:parameter ac:name="title">On this page</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="b58cb921-5240-4edd-913f-0dd5edbd334a"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="68d6f843-19aa-480d-81e1-df3547d11a1b"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Element Properties" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customizing Specification Window" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973508 space=UPDG version=1 -->
## PAGE 00198: Modifying Profile

- page_id: `243973508`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973508/Modifying+Profile
- version_number: 1
- version_date: `2025-07-31T19:04:47.416+02:00`
- ancestors: UML Profiling and DSL Guide > Working with Profiles
- labels: []

### NORMALIZED CONTENT

If you want to make changes in the profile, you can modify it by either opening the profile as a regular project or modify it in the read-write mode.

###### Opening Profile as Project

This is the safest way to modify your profiles. It helps to see all infrastructure (including diagrams, tests, examples, etc.) that is not shared.

To open a Profile as a project

- In the Browser, from the used Profile shortcut menu, choose Project Usages > Open .
- On the File menu, click Open Project to open the Profile as a simple Project.

###### Modifying Profile in Read-Write Mode

Using the profile in the read-write mode is the fastest way to add changes when you are not in teamwork and do not care if there are possible editing conflicts. It helps to perform basic refactoring of your shared projects by moving the elements directly from one project to the other. You may choose read-write usage mode when trying to use a profile as a project.

To use Profile in the read-write mode

1. Do one of the following:
  - If the profile is not in use yet, on the File menu, click Use Project . Select Use Local Project or Use Server Project, depending on where the project is located. Select a profile project and click Next .
  - If the profile is already in use, choose Project Usages > Options from its shortcut menu.
2. In the Accessibility area, click Read-write . By setting this option you will be able to change the profile directly in your project. Click Finish after you are done.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Working with projects' space='MDTWRT']
- [CONFLUENCE_PAGE title='Project partitioning' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>If you want to make changes in the profile, you can modify it by either opening the profile as a regular project or modify it in the read-write mode.</p><p><br /></p><div class="layoutArea"><h4 class="column">Opening Profile as Project</h4><p>This is the safest way to modify your profiles. It helps to see all infrastructure (including diagrams, tests, examples, etc.) that is not shared.</p><p><br /></p><div class="column"><p>To open a Profile as a project</p><hr /><ul><li>In the Browser, from the used Profile shortcut menu, choose <strong>Project Usages</strong><strong> &gt; Open</strong>.</li><li>On the <strong>File</strong> menu, click <strong>Open Project</strong> to open the Profile as a simple Project.</li></ul><p><span style="color: rgb(114,126,148);font-weight: bold;"> <br /> </span></p><h4 class="column">Modifying Profile in Read-Write Mode</h4><p><br /></p><div class="column">Using the profile in the read-write mode is the fastest way to add changes when you are not in teamwork and do not care if there are possible editing conflicts. It helps to perform basic refactoring of your shared projects by moving the elements directly from one project to the other. You may choose read-write usage mode when trying to use a profile as a project.</div><p><br /></p><p>To use Profile in the read-write mode</p><hr /><ol><li>Do one of the following:<ul><li>If the profile is not in use yet, on the <strong>File</strong> menu, click <strong>Use Project</strong>. Select <strong>Use Local Project</strong> or <strong>Use Server Project, </strong>depending on where the project is located. Select a profile project and click <strong>Next</strong>.</li><li>If the profile is already in use, choose <strong>Project Usages &gt; Options</strong> from its shortcut menu.</li></ul></li><li>In the <strong>Accessibility</strong> area, click <strong>Read-write</strong>. By setting this option you will be able to change the profile directly in your project. Click <strong>Finish</strong> after you are done.</li></ol><p><br /></p></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9569b377-0595-446b-af99-2098202f55af"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Working with projects" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Project partitioning" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973693 space=UPDG version=1 -->
## PAGE 00199: Numbering Scheme property values

- page_id: `243973693`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973693/Numbering+Scheme+property+values
- version_number: 1
- version_date: `2025-07-31T19:04:51.445+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Creating Numbering Customizations
- labels: []

### NORMALIZED CONTENT

1099459255

1099459258

1099517007

**On this page**

3

1099459257

##### Numbering Style property values

| Property value | Description |
| --- | --- |
| Multi-level | Select this style to number elements in several numbering levels. Specify at least one number part for each numbering level.Top level elements will be numbered using the first number part. Elements in subsequent levels (directly or indirectly contained in the top level element) will be numbered using successive number parts.If you specified fewer number parts than there are element levels, both the last element number part of the separator type and the last element number part of the non-separator type (numeric or character) will be reused to number subsequent level elements. For instance, if number parts are specified only for two numbering levels, and elements in the second level are numbered as “1.A”, “1.B”, and “1.C”, elements in the third numbering level will be numbered as “1.A.A”, “1.A.B”, etc. |
| Consecutive | Select this style to number elements in one numbering level. Specify only one number part.If you specified more than one number part, elements will be numbered using only the last number part. All other number parts in this case will be treated as static. For instance, if an element number includes five number parts (i.e., “1.1.1”). and the consecutive numbering style is selected, all elements will be numbered by changing only the last number part (“1.1.1”, “1.1.2”, “1.1.3”, etc.). The same happens after changing a multilevel numbering style to consecutive. |

##### Sequence property values

| Property value | Description |
| --- | --- |
| Numeric | Select this type to use only positive numbers for calculating a value of the number part.Elements will be numbered starting with “1” in ascending order, if no initial value is specified. |
| Character | Select this type to use only Latin letters for calculating a value of the number part.Elements will be numbered starting with “A” in ascending order, if no initial value is specified. |
| Expression | Select this type to use a Binary (Reference to a code class) expression for calculating a value of the number part. Use the Expression Editor dialog to define the expression. |
| Separator | Select this type to specify a separator between two number parts.Do not forget to specify the separator value for the Initial Value property. If the property value is not specified, the separator will not be used. |
| OwnerNumber | Select this type to use the number of an owner numbered using another numbering customization for calculating a value of the number part. |

1099459254

**Related pages**

- [CONFLUENCE_PAGE title='Creating Numbering Customizations' space='']
- [CONFLUENCE_PAGE title='Creating your first numbering customization' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="793ba7f6-2449-4df1-bce1-aec11613915e"><ac:parameter ac:name="id">1099459255</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="2006dc26-73c6-4f42-94ef-bbf1451448d6"><ac:parameter ac:name="id">1099459258</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="16245e82-31ff-4c35-94c2-4df015271299"><ac:parameter ac:name="id">1099517007</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="286b405d-463c-45cf-85b2-5aeac8d00eee"><ac:parameter ac:name="maxLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9a3b0298-2f02-4dda-88a6-433e95107376"><ac:parameter ac:name="id">1099459257</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3><span style="color: rgb(0,0,0);">Numbering Style property values</span></h3><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Property value</th><th>Description</th></tr><tr><td><h4>Multi-level</h4></td><td><div class="content-wrapper"><p>Select this style to number elements in several numbering levels. Specify at least one number part for each numbering level.<br />Top level elements will be numbered using the first number part. Elements in subsequent levels (directly or indirectly contained in the top level element) will be numbered using successive number parts.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="87d5b27c-2d5c-4ae2-b326-75127d285c68"><ac:rich-text-body><p>If you specified fewer number parts than there are element levels, both the last element number part of the separator type and the last element number part of the non-separator type (numeric or character) will be reused to number subsequent level elements. For instance, if number parts are specified only for two numbering levels, and elements in the second level are numbered as “1.A”, “1.B”, and “1.C”, elements in the third numbering level will be numbered as “1.A.A”, “1.A.B”, etc.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><h4>Consecutive</h4></td><td><div class="content-wrapper"><p> <span>Select this style to number elements in one numbering level. Specify </span><span>only one number part.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="707ae023-289a-482d-8b96-1f5a34425b52"><ac:rich-text-body><p>If you specified more than one number part, elements will be numbered using only the last number part. All other number parts in this case will be treated as static. For instance, if an element number includes five number parts (i.e., “1.1.1”). and the consecutive numbering style is selected, all elements will be numbered by changing only the last number part (“1.1.<span style="color: rgb(255,0,0);">1</span>”, “1.1.<span style="color: rgb(255,0,0);">2</span>”, “1.1.<span style="color: rgb(255,0,0);">3</span>”, etc.). The same happens after changing a multilevel numbering style to consecutive.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr></tbody></table><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p> </p><h3>Sequence property values</h3><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Property value</th><th>Description</th></tr><tr><td><h4>Numeric</h4></td><td><div class="content-wrapper"><p>Select this type to use only positive numbers for calculating a value of the number part.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="22bb99c0-e26a-4020-9403-93c507339239"><ac:rich-text-body><p>Elements will be numbered starting with “1” in ascending order, if no initial value is specified.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><h4>Character</h4></td><td><div class="content-wrapper"><p><span>Select this type to use only Latin letters for calculating a value of the </span><span>number part.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="71c427b4-4f14-4a71-91c8-2e4003f6a341"><ac:rich-text-body><p>Elements will be numbered starting with “A” in ascending order, if no initial value is specified.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><h4>Expression</h4></td><td><span>Select this type to use a Binary (Reference to a code class) </span>expression for calculating a value of the number part. Use the <strong>Expression </strong><span><strong>Editor</strong> dialog to define the expression.</span></td></tr><tr><td><h4>Separator</h4></td><td><div class="content-wrapper"><p>Select this type to specify a separator between two number parts.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="838229e6-2041-4557-a570-b63f8902eab4"><ac:rich-text-body><p>Do not forget to specify the separator value for the <strong>Initial Value</strong> property. If the property value is not specified, the separator will not be used.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>OwnerNumber</strong></td><td><p>Select this type to use the number of an owner numbered using another numbering customization for calculating a value of the number part.</p></td></tr></tbody></table><p class="auto-cursor-target"><br /></p><p> </p><p> </p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c237e2ca-440a-49dc-a51e-87a8cbec343c"><ac:parameter ac:name="id">1099459254</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Creating Numbering Customizations" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating your first numbering customization" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973591 space=UPDG version=1 -->
## PAGE 00200: Properties Displayed in Compartments

- page_id: `243973591`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973591/Properties+Displayed+in+Compartments
- version_number: 1
- version_date: `2025-07-31T19:04:49.040+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data > Customization Elements
- labels: []

### NORMALIZED CONTENT

Using Properties Displayed in Compartments, you can select the specific properties to be displayed on the element shape.

To customize the properties to be displayed in compartments

1. Create a customization for your DSL element or select an existing one.
2. In the element [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] , under Symbol, locate Properties Displayed in Compartments , and click the [ATTACHMENT filename='button.png'] button.
3. In the Select Properties dialog, select the specific properties you want to see displayed in the compartment of your shape(s).
4. Reopen or refresh the project.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Using Properties Displayed in Compartments, you can select the specific properties to be displayed on the element shape.</p><p>To customize the properties to be displayed in compartments</p><hr /><ol><li>Create a customization for your DSL element or select an existing one.</li><li>In the element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>, under Symbol, locate <strong>Properties Displayed in Compartments</strong>, and click the <ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="button.png" /></ac:image> button. </li><li>In the <strong>Select Properties</strong> dialog, select the specific properties you want to see displayed in the compartment of your shape(s). </li><li>Reopen or refresh the project. </li></ol>
````

<!--NOMAGIC_PAGE id=243973702 space=UPDG version=1 -->
## PAGE 00201: Recursive properties

- page_id: `243973702`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973702/Recursive+properties
- version_number: 1
- version_date: `2025-07-31T19:04:51.710+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Extending Metamodel with Derived Properties
- labels: []

### NORMALIZED CONTENT

1852081948

1852081950

1852081949

A recursive property is defined as a binary class “*com.nomagic.magicdraw.derivedproperty.RecursiveExpression()*” with parameters*<property-name>* and 
*<recursive-property-name>*.

Specify the expression in the following form *- com.nomagic.magicdraw.derivedproperty.RecursiveExpression(*<property-name>*, *<recursive-property-name>** (e.g.*com.nomagic.magicdraw.derivedproperty.RecursiveExpression(Classifier.specificClassifier, Classifier.allSpecificClassifiers)*

Recursive properties enable you to collect and represent:

- All elements directly or indirectly related to a specific element through the generalization relationships. Refer to the derived property customization expression, available at "UML Standard Profile::MagicDraw Profile::Traceability customization::Properties descriptors::Other::All Specific Classifiers::allSpecificClassifiers".

- All elements directly or indirectly related to a specific element through the abstraction and other types of relations. Refer to the derived property customization expression, available at "UML Standard Profile::MagicDraw Profile::Traceability customization::Properties descriptors::Realization::Element All Realizing Elements::allRealizingElements".

1852081947

**Related Pages**

- Extending Metamodel with Derived Properties
- Using Customization Data
- Creating Customization Data

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="081264b5-8865-47e0-9e0b-765ad62e2b21"><ac:parameter ac:name="id">1852081948</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="bed7a4e2-be4c-4853-944b-eb26e8d08bde"><ac:parameter ac:name="id">1852081950</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0e620078-0886-4fe7-ac61-e5d6c5a33e86"><ac:parameter ac:name="id">1852081949</ac:parameter><ac:rich-text-body><p>A recursive property is defined as a binary class “<em>com.nomagic.magicdraw.derivedproperty.RecursiveExpression()</em>” with parameters<em> &lt;property-name&gt;</em> and<br /><em>&lt;recursive-property-name&gt;</em>.</p><p>Specify the expression in the following form <em>- com.nomagic.magicdraw.derivedproperty.RecursiveExpression(<em>&lt;property-name&gt;</em>, <em>&lt;recursive-property-name&gt;</em></em> (e.g.<em> com.nomagic.magicdraw.derivedproperty.RecursiveExpression(Classifier.specificClassifier, Classifier.allSpecificClassifiers)</em></p><p>Recursive properties enable you to collect and represent:</p><ul><li><p>All elements directly or indirectly related to a specific element through the generalization relationships. </p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="56647db3-f363-4a99-899d-f4b87f59597d"><ac:rich-text-body><p>Refer to the derived property customization expression, available at &quot;UML Standard Profile::MagicDraw Profile::Traceability customization::Properties descriptors::Other::All Specific Classifiers::allSpecificClassifiers&quot;.</p></ac:rich-text-body></ac:structured-macro></li></ul><ul><li><p>All elements directly or indirectly related to a specific element through the abstraction and other types of relations.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="ef3e7b25-f310-455e-b416-cc19e90d71d6"><ac:rich-text-body><p>Refer to the derived property customization expression, available at &quot;UML Standard Profile::MagicDraw Profile::Traceability customization::Properties descriptors::Realization::Element All Realizing Elements::allRealizingElements&quot;.</p></ac:rich-text-body></ac:structured-macro></li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c8f60a75-9a70-42ee-acf0-5ba9f2eb530d"><ac:parameter ac:name="id">1852081947</ac:parameter><ac:rich-text-body><p><strong>Related Pages</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MDTWRT/Extending+Metamodel+with+Derived+Properties">Extending Metamodel with Derived Properties</a></li><li class="ancestor-link"><a href="https://docs.nomagic.com/display/MDTWRT/Using+Customization+Data">Using Customization Data</a></li><li><a href="https://docs.nomagic.com/display/MDTWRT/Creating+Customization+Data">Creating Customization Data</a></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973598 space=UPDG version=1 -->
## PAGE 00202: Rules of Stereotypes that cannot be Allowed to Apply

- page_id: `243973598`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973598/Rules+of+Stereotypes+that+cannot+be+Allowed+to+Apply
- version_number: 1
- version_date: `2025-07-31T19:04:49.203+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data
- labels: []

### NORMALIZED CONTENT

When applying a stereotype to a DSL element, the list of the available stereotypes that may be applied is filtered according to the following rules:

- Only one DSL stereotype (with Hide Metatype=*true*) may be applied to an element. For example, if «Block» is already applied, the «Requirement» stereotype will not appear in the stereotype shortcut menu.
- In order to apply a new DSL stereotype (e.g. when changing from «Requirement» to «businessRequirement»), clear the currently applied stereotype and apply the change. The stereotype shortcut menu will then show all DSL stereotypes. Tip!Quickly change the stereotype by converting one element type to other (in the DSL element shortcut menu, click **Refactor**and then **Convert**).

- DSL ownership rules are checked and it is not allowed to apply a stereotype not allowed in the parent element of DSL element.
- DSL relationship rules are checked and it is not allowed to apply a stereotype if a relationship exists and the source or target element violates DSL rules for the existing DSL relationship.
- DSL rules are also checked when drawing new relationships in a diagram.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Customization Elements' space='']
- [CONFLUENCE_PAGE title='Customization Element Properties' space='']
- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Creating your First Customization' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span><span style="color: rgb(0,0,0);"><span><span>When applying a stereotype to a DSL element, the list of the available stereotypes that may be applied is filtered according to the following rules: </span></span></span><br /></span></p><ul><li><span><span style="color: rgb(0,0,0);"><span><span> </span><span>Only one DSL stereotype (with Hide Metatype=</span><span><em>true</em></span><span>) may be applied to an element</span></span></span>. <span style="color: rgb(0,0,0);"><span><span>For example, if «Block» is already applied, the «Requirement» stereotype will not appear in the stereotype shortcut menu. <br /></span></span></span></span></li><li><p class="auto-cursor-target"><span style="color: rgb(0,0,0);"><span><span>In order to apply a new DSL stereotype (e.g. when changing from «Requirement» to «businessRequirement»), clear the currently applied stereotype and apply the change.  The stereotype shortcut menu will then show all DSL stereotypes.</span></span></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bed4a04c-5095-48b6-9021-24e006c535f2"><ac:parameter ac:name="title">Tip!</ac:parameter><ac:rich-text-body><p>Quickly change the stereotype by converting one element type to other (in the DSL element shortcut menu, click <strong>Refactor </strong>and then <strong>Convert</strong>).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul></div><div class="layoutArea"><div class="column"><ul><li><span>DSL ownership rules are checked and it is not allowed to apply a stereotype not allowed in the parent element of DSL element. </span></li><li><span><span style="color: rgb(0,0,0);"><span><span>DSL relationship rules are checked and it is not allowed to apply a stereotype if a relationship exists and the source or target element violates DSL rules for the existing DSL relationship. </span></span></span></span></li><li><span><span style="color: rgb(0,0,0);"><span><span>DSL rules are also checked when drawing new relationships in a diagram.</span></span></span> </span></li></ul></div></div></div><p><span> <br /> </span></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="6efd5fee-3aef-4601-a134-650bec14b3cc"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li class="_mce_tagged_br"><ac:link><ri:page ri:content-title="Customization Elements" /></ac:link></li><li class="_mce_tagged_br"><ac:link><ri:page ri:content-title="Customization Element Properties" /></ac:link></li><li class="_mce_tagged_br"><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li class="_mce_tagged_br"><ac:link><ri:page ri:content-title="Creating your First Customization" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973636 space=UPDG version=1 -->
## PAGE 00203: Selecting more than one drag-and-drop rule

- page_id: `243973636`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973636/Selecting+more+than+one+drag-and-drop+rule
- version_number: 1
- version_date: `2025-07-31T19:04:50.197+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Customizing Drag-and-Drop
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Tip

1254667587

#### CONTENT-COLUMN: Tip

1254667598

#### CONTENT-BLOCK: Tip

1254667597

In some cases, more than one rule can be applied to a drag-and-drop operation. This enables you to select what to create.

To select a rule

1. Do one of the following:
  - Drag a selected element to another, hold it for a few seconds till the tool-tip opens, and then release. A shortcut menu is displayed.
  - Right-click an element, drag it onto another element, and then drop it. A shortcut menu is displayed. ( Note: this procedure is valid on Windows OS only).
2. On the shortcut menu, click the rule to apply. The rule is applied. [ATTACHMENT filename='drag_and_drop8.png']

#### TIP: Tip

Tip

Our modeling tools have a number of predefined drag-and-drop rules.

1254667586

**Related pages**

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Creating Numbering Customizations' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="bc1e2e9d-a266-4ec9-8fc3-00f05d204ae4"><ac:parameter ac:name="id">1254667587</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="a6b6a888-4057-40cb-8e74-c9e27ebe7459"><ac:parameter ac:name="id">1254667598</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d463841a-bf5d-49a4-98b5-511bc4eac929"><ac:parameter ac:name="id">1254667597</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p><span>In some cases, more than one rule can be applied to a drag-and-drop operation. This enables you to select what to create.</span></p><p><span> <br /></span></p><p>To select a rule</p><hr /><ol><li>Do one of the following:<ul><li>Drag a selected element to another, hold it for a few seconds till the tool-tip opens, and then release. A shortcut menu is displayed.</li><li>Right-click an element, drag it onto another element, and then drop it. A shortcut menu is displayed. (<strong>Note:</strong> this procedure is valid on Windows OS only).</li></ul></li><li>On the shortcut menu, click the rule to apply. The rule is applied.<ac:image><ri:attachment ri:filename="drag_and_drop8.png" /></ac:image></li></ol><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="57250a5c-3cda-460e-8f74-cccc44bf6821"><ac:parameter ac:name="title">Tip</ac:parameter><ac:rich-text-body><p>Our modeling tools have a number of predefined drag-and-drop rules. </p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></div></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9dc03ebc-b47b-404a-ae00-61b574ff939f"><ac:parameter ac:name="id">1254667586</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating Numbering Customizations" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973494 space=UPDG version=2 -->
## PAGE 00204: Specifying Invisible Stereotypes, Tags, and Constraints

- page_id: `243973494`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973494/Specifying+Invisible+Stereotypes+Tags+and+Constraints
- version_number: 2
- version_date: `2026-06-23T17:21:31.179+02:00`
- ancestors: UML Profiling and DSL Guide > Working with Profiles > Creating Profiles
- labels: []

### NORMALIZED CONTENT

Normally, tags are used to hold additional specific information. This information helps interpret basic elements differentiated by some external tools, such as transformations, code engineering, etc.

In these cases, you only want to mark the model, not make an impact on existing diagrams.

Tag definitions are properties of stereotype in UML2. UML does not allow using tagged values without assigning stereotype. Your diagrams will be changed when some tags are added into the model.

A modeling tool enables you to make chosen stereotypes or tags in diagrams invisible.

To make a stereotype invisible

The stereotype you want to make invisible must be inherited from «InvisibleStereotype» found in the modeling tool profile.

1. Create a custom stereotype.
2. Create a Generalization between your stereotype and InvisibleStereotype. Your custom stereotype will be not displayed on symbols where it is applied. Note that all tags will also be invisible on symbols.

#### INFO: Example

Example

It is not desirable to see an author tag in diagrams. To accomplish this, follow these steps:

1. Create a stereotype «copyrighted» that extends the Element metaclass.
2. Create a property “author: String” for a «copyrighted» stereotype.
3. Inherit this stereotype from «InvisibleStereotype» (create generalization in the model or diagram).

Now you may enter the tagged value “author” for any element in your model.

The stereotype «copyrighted» will be automatically applied but will be invisible in diagrams.

To create an invisible tag

1. Apply «InvisibleStereotype» on your tag definition (a property of a stereotype).

#### NOTE: Hidden Tags

Hidden Tags

All hidden tags will be invisible on the symbols of stereotyped elements.

#### INFO: Example:

Example:

The stereotype «identification» has two tags: ID and Description. The user would like to see a Description value on elements in diagrams, but ID should be hidden as it is used in some external model transformation tools or similar activities.

Apply «InvisibleStereotype» on the ID property of the «identification» stereotype and it will be not visible on stereotyped elements on diagrams.

To make a constraint invisible

1. Apply the «InvisibleStereotype» stereotype to the constraint.
2. Invisible constraints may be used while creating validation constraints, in DSL customization, or in other modeling cases.

**Related pages**

- [CONFLUENCE_PAGE title='Stereotype' space='MED']
- [CONFLUENCE_PAGE title='Tag' space='MED']
- [CONFLUENCE_PAGE title='Generalization' space='MED']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>Normally, tags are used to hold additional specific information. This information helps interpret basic elements differentiated by some external tools, such as transformations, code engineering, etc.</p><p>In these cases, you only want to mark the model, not make an impact on existing diagrams.</p><p>Tag definitions are properties of stereotype in UML2. UML does not allow using tagged values without assigning stereotype. Your diagrams will be changed when some tags are added into the model.</p><p>A modeling tool enables you to make chosen stereotypes or tags in diagrams invisible.</p><p><br /></p><p>To make a stereotype invisible</p><hr /><p style="margin-left: 30.0px;">The stereotype you want to make invisible must be inherited from «InvisibleStereotype» found in the modeling tool profile.</p><ol><li data-uuid="96f54fca-ef44-481e-98c0-c1c3ee59fe5b">Create a custom stereotype.</li><li data-uuid="5f0cd7df-9d8c-4d73-ae39-3aa3b1c273be">Create a Generalization between your stereotype and InvisibleStereotype. Your custom stereotype will be not displayed on symbols where it is applied. Note that all tags will also be invisible on symbols.</li></ol><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="cd8ec6b3-4229-4cde-bef1-45e8478d3730"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p>It is not desirable to see an author tag in diagrams. To accomplish this, follow these steps:</p><ol><li data-uuid="318c199f-0df0-48d1-bb8b-ea352c4981a8"><p>Create a stereotype «copyrighted» that extends the Element metaclass. </p></li><li data-uuid="04d0a12c-0b2a-4482-b5f8-bb0baf4fcd98"><p>Create a property “author: String” for a «copyrighted» stereotype. </p></li><li data-uuid="b818e3e3-e179-4966-be65-a641f1282858"><p>Inherit this stereotype from «InvisibleStereotype» (create generalization in the model or diagram).</p></li></ol><p>Now you may enter the tagged value “author” for any element in your model.</p><p>The stereotype «copyrighted» will be automatically applied but will be invisible in diagrams. </p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><span> </span></p><p><span>To create an invisible tag</span></p><hr /><ol><li data-uuid="0735e886-8cb0-4cc1-86ef-884269ef0f67">Apply «InvisibleStereotype» on your tag definition (a property of a stereotype). </li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c1c56333-cdb9-46a7-9560-d742d96ae3cc"><ac:parameter ac:name="title">Hidden Tags</ac:parameter><ac:rich-text-body><p>All hidden tags will be invisible on the symbols of stereotyped elements.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="815f069d-cf37-4cbc-ba9b-dac1cdb64a35"><ac:parameter ac:name="title">Example:</ac:parameter><ac:rich-text-body><p>The stereotype «identification» has two tags: ID and Description. The user would like to see a Description value on elements in diagrams, but ID should be hidden as it is used in some external model transformation tools or similar activities.</p><p>Apply «InvisibleStereotype» on the ID property of the «identification» stereotype and it will be not visible on stereotyped elements on diagrams.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To make a constraint invisible</p><hr /><ol><li data-uuid="65a9c1d2-ce33-4524-9993-694c309035c9">Apply the «InvisibleStereotype» stereotype to the constraint. </li><li data-uuid="b8cb9334-e350-4776-ae2a-25a6611ec045">Invisible constraints may be used while creating validation constraints, in DSL customization, or in other modeling cases.</li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li data-uuid="0d4189b5-e5dc-4ef2-9786-63837f74e293"><ac:link><ri:page ri:space-key="MED" ri:content-title="Stereotype" /></ac:link></li><li data-uuid="e70c2900-3840-403f-8134-58b5bc87c31b"><ac:link><ri:page ri:space-key="MED" ri:content-title="Tag" /></ac:link></li><li data-uuid="90e7caa4-0c94-448c-bda4-4e18285388ca"><ac:link><ri:page ri:space-key="MED" ri:content-title="Generalization" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973589 space=UPDG version=1 -->
## PAGE 00205: Standard Expert Configuration

- page_id: `243973589`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973589/Standard+Expert+Configuration
- version_number: 1
- version_date: `2025-07-31T19:04:48.915+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data > Customization Elements
- labels: []

### NORMALIZED CONTENT

In the DSL element [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'], properties are hidden or displayed by using Standard, Expert and All modes.

To customize Standard Expert mode

1. Create a [CONFLUENCE_PAGE title='Creating your First Customization' space=''] for the DSL element or select an existing one.
2. In the element Specification window, click the Standard Expert Configuration property and then click the [ATTACHMENT filename='edit.png'] button.
3. In the [CONFLUENCE_PAGE title='Dialog for customizing selected modeling tool area' space='MDTWRT']**Customize Properties** dialog , click to select the mode in which the property will be displayed in the DSL element Specification window.

#### NOTE: Tip!

Tip!

- The Customize Properties dialog contains the list of used UML properties and custom properties. You can select which UML properties and DSL specific properties will be displayed in the DSL element Specification window.
- You can also customize property groups. In the Customize Properties dialog, property groups are displayed at the end of the list.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p>In the DSL element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>, properties are hidden or displayed by using Standard, Expert and All modes.</p><p><br /></p><p>To customize Standard Expert mode</p><hr /><ol><li>Create a <ac:link><ri:page ri:content-title="Creating your First Customization" /><ac:plain-text-link-body><![CDATA[customization element]]></ac:plain-text-link-body></ac:link> for the DSL element or select an existing one. </li><li>In the element Specification window, click the <strong>Standard Expert Configuration</strong> property and then click the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="edit.png"><ri:page ri:content-title="Do Not Suggest As Type" /></ri:attachment></ac:image> button. </li><li>In the<ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Dialog for customizing selected modeling tool area" /><ac:link-body> <strong>Customize Properties</strong> dialog</ac:link-body></ac:link>, click to select the mode in which the property will be displayed in the DSL element Specification window. </li></ol><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="341355eb-0046-47d9-b1c7-d1ad5fb174ef"><ac:parameter ac:name="title">Tip!</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><ul><li><span>The </span><strong>Customize Properties </strong><span>dialog contains the list of used UML properties and custom properties. You can select which UML properties and DSL specific properties will be displayed in the DSL element Specification window. </span></li><li>You can also customize property groups. In the <strong>Customize Properties</strong> dialog, property groups are displayed at the end of the list.</li></ul></div></div></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="68d6f843-19aa-480d-81e1-df3547d11a1b"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973586 space=UPDG version=1 -->
## PAGE 00206: Sub Element Contents Included

- page_id: `243973586`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973586/Sub+Element+Contents+Included
- version_number: 1
- version_date: `2025-07-31T19:04:48.843+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data > Customization Elements
- labels: []

### NORMALIZED CONTENT

Use the **Sub Element Contents Included** property to specify whether the content of a desired element typeincludes only directly related elements or both directly and indirectly related ones.

The property value can be either:

- None : the content includes only directly related elements. [ATTACHMENT filename='not_include_subelements_in_content.png']

- All : the content includes both directly and indirectly related elements. [ATTACHMENT filename='include_subelements_in_content.png']

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Customization Elements' space='']
- [CONFLUENCE_PAGE title='Customization Element Properties Description' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span>Use the </span> <strong>Sub Element Contents Included </strong> <span>property to specify whether the content of a desired element type </span>includes only directly related elements or both directly and indirectly related ones.</p><p>The property value can be either:</p><ul><li><em>None</em>: the content includes only directly related elements.<br /><ac:image><ri:attachment ri:filename="not_include_subelements_in_content.png" /></ac:image></li></ul><p><br /></p><ul><li><em>All</em>: the content includes both directly and indirectly related elements.<br /><ac:image><ri:attachment ri:filename="include_subelements_in_content.png" /></ac:image></li></ul><div class="layoutArea"><div class="column"><p><span> <br /> </span></p></div></div></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="68d6f843-19aa-480d-81e1-df3547d11a1b"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Elements" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customization Element Properties Description" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973590 space=UPDG version=1 -->
## PAGE 00207: Symbol Standard Expert Configuration

- page_id: `243973590`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973590/Symbol+Standard+Expert+Configuration
- version_number: 1
- version_date: `2025-07-31T19:04:48.979+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Creating Customization Data > Customization Elements
- labels: []

### NORMALIZED CONTENT

Using the **Symbol Standard Expert Configuration** property, you can specify properties visibility mode:

- in the DSL element [CONFLUENCE_PAGE title='Symbol Properties dialog' space='MDTWRT'] ,
- in the [CONFLUENCE_PAGE title='Customizing Element Shortcut Menu' space=''] , and
- in menus that open after clicking the [CONFLUENCE_PAGE title='Compartments' space='MDTWRT'] or Create Element smart manipulators.

To customize Standard Expert mode

1. Create a customization element for the DSL element or select an existing one.
2. In the element [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] , click the Symbol Standard Expert Configuration property and then click the button.
3. In the [CONFLUENCE_PAGE title='Dialog for customizing selected modeling tool area' space='MDTWRT']**Customize Properties** dialog , click to select the mode to display the property in the DSL element Symbol Properties dialog and in other places.
4. Reopen the project.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p>Using the <strong>Symbol Standard Expert Configuration</strong> property, you can specify properties visibility mode:</p><ul><li>in the DSL element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Symbol Properties dialog" /></ac:link>,</li><li>in the <ac:link><ri:page ri:content-title="Customizing Element Shortcut Menu" /><ac:plain-text-link-body><![CDATA[symbol shortcut menu]]></ac:plain-text-link-body></ac:link>, and</li><li>in menus that open after clicking the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Compartments" /></ac:link> or Create Element smart manipulators.</li></ul><p><br /></p><p>To customize Standard Expert mode</p><hr /><ol><li>Create a customization element for the DSL element or select an existing one.</li><li>In the element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>, click the <strong>Symbol Standard Expert Configuration</strong> property and then click the button. </li><li>In the <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Dialog for customizing selected modeling tool area" /><ac:link-body><strong>Customize Properties</strong> dialog</ac:link-body></ac:link>, click to select the mode to display the property in the DSL element Symbol Properties dialog and in other places.</li><li>Reopen the project. </li></ol><p><br /></p></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="68d6f843-19aa-480d-81e1-df3547d11a1b"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973661 space=UPDG version=1 -->
## PAGE 00208: Type Restriction for Custom Table in Specification Window

- page_id: `243973661`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973661/Type+Restriction+for+Custom+Table+in+Specification+Window
- version_number: 1
- version_date: `2025-07-31T19:04:50.977+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Creating Property Groups and Subgroups
- labels: []

### NORMALIZED CONTENT

DSL allows you to create a new node in the [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'] and show values of some UML properties in table form. Use the **Filter** property to filter elements by type. The **Filter** property stores the element types (UML metaclasses and custom [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT']) displayed as property values.The DSL engine checks these values and displays only these types of elements in the table. The**Create**button allows you to create new elements of these restricted types.

**Rules for subtypes**

- If the type is a stereotype, all subtypes (sub stereotypes) are also accepted. For example, if the type is [CONFLUENCE_PAGE title='Requirement' space='SYSMLP185'] , [CONFLUENCE_PAGE title='Business Requirement' space='SYSMLP185'] is also accepted.
- If the type is an abstract metaclass, all subclasses are accepted. For example, if the type is Classifier, [CONFLUENCE_PAGE title='Class' space='MDTWRT'] , [CONFLUENCE_PAGE title='Component' space='MDTWRT'] and other are accepted. DSL elements are also accepted.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Creating Property Groups and Subgroups' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>DSL allows you to create a new node in the <ac:inline-comment-marker ac:ref="27ce3e9c-1b83-4571-b8a8-1ec914e2caab"><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link></ac:inline-comment-marker> and show values of some UML properties in table form. Use the <strong>Filter</strong> property to filter elements by type. The <strong>Filter</strong> property s<span>tores the element types (UML metaclasses and custom <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotypes]]></ac:plain-text-link-body></ac:link>) displayed as property values. </span><span>The DSL engine checks these values and displays only these types of elements in the table. The </span><strong>Create</strong><span> button allows you to create new elements of these restricted types. </span></p><div class="layoutArea"><div class="column"><div class="layoutArea"><div class="column"><p><span> <br /> </span></p><p><strong>Rules for subtypes</strong></p><ul><li>If the type is a stereotype, all subtypes (sub stereotypes) are also accepted. For example, if the type is <ac:link><ri:page ri:space-key="SYSMLP185" ri:content-title="Requirement" /></ac:link>, <ac:link><ri:page ri:space-key="SYSMLP185" ri:content-title="Business Requirement" /><ac:plain-text-link-body><![CDATA[BusinessRequirement]]></ac:plain-text-link-body></ac:link> is also accepted.</li><li>If the type is an abstract metaclass, all subclasses are accepted. For example, if the type is Classifier, <ac:inline-comment-marker ac:ref="c2ef78fb-06b1-4dda-99a1-46fd2cdea831"><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Class" /></ac:link></ac:inline-comment-marker>, <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Component" /></ac:link> and other are accepted. DSL elements are also accepted. </li></ul></div></div></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b0ccb40e-6e11-4ccd-baa7-51ecf465051e"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating Property Groups and Subgroups" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973476 space=UPDG version=5 -->
## PAGE 00209: UML Profiling and DSL Guide

- page_id: `243973476`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973476/UML+Profiling+and+DSL+Guide
- version_number: 5
- version_date: `2025-07-31T19:09:03.990+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

UML is a general-purpose visual modeling language for specifying, constructing, and documenting the artifacts of systems to be used with all major application domains and implementation platforms. It has been widely adopted by both industry and academia as the standard language for describing software systems.

The MagicDraw UML tool provides the ability to use the DSL engine to adapt domain-specific profiles, enabling you to create your own custom diagrams, custom specification dialogs, custom real-time semantic rules, etc. In other words, you can create a low-budget, specialized domain-specific tool and hide the UML underneath.

DSL customization is a model-driven approach, based on UML profiling.

##### Demo

700360

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>UML is a general-purpose visual modeling language for specifying, constructing, and documenting the artifacts of systems to be used with all major application domains and implementation platforms. It has been widely adopted by both industry and academia as the standard language for describing software systems.</p><p>The MagicDraw UML tool provides the ability to use the DSL engine to adapt domain-specific profiles, enabling you to create your own custom diagrams, custom specification dialogs, custom real-time semantic rules, etc. In other words, you can create a low-budget, specialized domain-specific tool and hide the UML underneath. </p><p>DSL customization is a model-driven approach, based on UML profiling.</p><h3>Demo</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="81304f0d-9c8d-483b-8bc4-05db80d8b839"><ac:parameter ac:name="width">700</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=ha89QJzS9nk" /></ac:parameter><ac:parameter ac:name="height">360</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=243973601 space=UPDG version=1 -->
## PAGE 00210: Using Customization Data

- page_id: `243973601`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973601/Using+Customization+Data
- version_number: 1
- version_date: `2025-07-31T19:04:49.358+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization
- labels: []

### NORMALIZED CONTENT

The following sections describe how to use customization data in particular cases while working with models and our modeling tools.

#### PANEL: Additional resources

Additional resources

[Enabling Domain Specific Extensions to SysML](https://www.youtube.com/watch?v=3IBv3922a-A&feature=youtu.be)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The following sections describe how to use customization data in particular cases while working with models and our modeling tools.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="65065f1e-a8c3-473d-a9c6-e279e0305abb" /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c60fb1a7-50d3-48c7-9573-58056a5b2b40"><ac:parameter ac:name="title">Additional resources</ac:parameter><ac:rich-text-body><p><a href="https://www.youtube.com/watch?v=3IBv3922a-A&amp;feature=youtu.be">Enabling Domain Specific Extensions to SysML</a></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973603 space=UPDG version=1 -->
## PAGE 00211: Using Standard UML Properties

- page_id: `243973603`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973603/Using+Standard+UML+Properties
- version_number: 1
- version_date: `2025-07-31T19:04:49.484+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Customizing Specification Window
- labels: []

### NORMALIZED CONTENT

DSL element specification may contain custom properties defined in a stereotype.All DSL element properties are used by default, but you may select which UML properties should be used in the DSL element [CONFLUENCE_PAGE title='Specification window' space='MDTWRT'].

To use standard UML properties

1. Open the customization element Specification window.
2. Click the Used UML Properties property value specification cell and then click the [ATTACHMENT filename='edit.png'] button.
3. In the Select properties dialog, set the selected standard UML properties that you want to be displayed in the DSL element Specification window value to true .
4. Click OK when you are done.

[IMAGE alt='' src='']

###### Select Properties dialog.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Creating Customization Data' space='']
- [CONFLUENCE_PAGE title='Using Customization Data' space='']
- [CONFLUENCE_PAGE title='Customizing Specification Window' space='']
- [CONFLUENCE_PAGE title='Always Visible Properties' space='']
- [CONFLUENCE_PAGE title='Meta property substitution (changing name of UML property)' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span>DSL element specification may contain custom properties defined in a stereotype. </span>All DSL element properties are used by default, but you may select which UML properties should be used in the DSL element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>.</p><p><br /></p><p>To use standard UML properties</p><hr /><ol><li>Open the customization element Specification window.</li><li>Click the <strong>Used UML Properties</strong> property value specification cell and then click the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="edit.png"><ri:page ri:content-title="Do Not Suggest As Type" /></ri:attachment></ac:image> button.</li><li>In the <strong>Select properties</strong> dialog, set the selected standard UML properties that you want to be displayed in the DSL element Specification window value to <em>true</em>.</li><li>Click <strong>OK</strong> when you are done. </li></ol><p><br /><ac:image ac:align="center"><ri:attachment ri:filename="select_properties_dialog.png" /></ac:image></p><h6 style="text-align: center;">Select Properties dialog.</h6></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="68d6f843-19aa-480d-81e1-df3547d11a1b"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using Customization Data" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customizing Specification Window" /></ac:link></li><li><ac:link><ri:page ri:content-title="Always Visible Properties" /></ac:link></li><li><ac:link><ri:page ri:content-title="Meta property substitution (changing name of UML property)" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=246156653 space=UPDG version=1 -->
## PAGE 00212: Versions of UML Profiling and DSL Guide

- page_id: `246156653`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/246156653/Versions+of+UML+Profiling+and+DSL+Guide
- version_number: 1
- version_date: `2025-08-01T13:22:31.672+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

47dd4cbbbb8f818d0d7822de65f23a3c

UML Profiling and DSL Guide

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="702cd5c3-f264-4cf9-bb43-6d40c18f1a10"><ac:parameter ac:name="permaId">47dd4cbbbb8f818d0d7822de65f23a3c</ac:parameter><ac:parameter ac:name="documentTitle">UML Profiling and DSL Guide</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243973492 space=UPDG version=1 -->
## PAGE 00213: Working with Profiles

- page_id: `243973492`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973492/Working+with+Profiles
- version_number: 1
- version_date: `2025-07-31T19:04:46.935+02:00`
- ancestors: UML Profiling and DSL Guide
- labels: []

### NORMALIZED CONTENT

Profile in UML is a special kind of [CONFLUENCE_PAGE title='Package' space='MDTWRT'], used to contain collections of [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT'], domain specific data types, and libraries.

This chapter includes the following sections on working with profiles:

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Package' space='MDTWRT']
- [CONFLUENCE_PAGE title='Stereotype' space='MDTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="layoutArea"><div class="column"><p><span>Profile in UML is a special kind of <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Package" /></ac:link>, used to contain collections of <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotypes]]></ac:plain-text-link-body></ac:link>, domain specific data types, and libraries. </span></p><p><span>This chapter includes the following sections on working with profiles:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="4ebd1584-697f-45b9-bfb1-06cfdf9f6a8c" /></p></div></div></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="d6dd31f2-9f5f-42a1-abd1-91fa70f0e896"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Package" /></ac:link></li><li><ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Stereotype" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243973660 space=UPDG version=1 -->
## PAGE 00214: «propertyGroup» Properties

- page_id: `243973660`
- space_key: `UPDG`
- source_url: https://docs.nomagic.com/spaces/UPDG/pages/243973660/%C2%ABpropertyGroup%C2%BB+Properties
- version_number: 1
- version_date: `2025-07-31T19:04:50.900+02:00`
- ancestors: UML Profiling and DSL Guide > Domain Specific Language customization > Using Customization Data > Creating Property Groups and Subgroups
- labels: []

### NORMALIZED CONTENT

| Property | Description |
| --- | --- |
| Show Group In Compartment Edit | This property allows for displaying the element properties in the Compartment Edit dialog > the Element Properties tab and in a note on a diagram either within the property group/subgroup or without it. If the value is true, the property name is displayed as follows: <property_group_name>::<property_name>. If the value is false, the property name is displayed as follows: <property_name> . |
| Show Group In Dependency Matrix | If the value is true, the property group/subgroup is visible in the dialog, when you create or edit a . |
| Show Group In Element Specification | If the value is true, the property group/subgroup is visible in the element . |
| Show Group In Go To | If the value is true, the property group/subgroup is visible in element’s shortcut menu as a submenu under the Go To menu. |
| Show Group In Quick Properties | If the value is true, the property group/subgroup is visible in the element Properties panel. |
| Show Group In Relation Map | If the value is true, the property group/subgroup is visible in the Criterion Editor dialog, when you create or edit a . |
| Use As Node | If the value is true, the property group is displayed in a separate tab in the element Specification window and/or Properties panel. If the value is false, the property group is displayed as a group in the general (default) pane of the element Specification window and/or Properties panel. Do not set this property value to true for the property subgroup. |
| Properties | Stores a list of properties that is visible in the property group or subgroup. Do not set this property value to true for the property subgroup. |
| Columns | Stores the specified table columns for showing the values of a multivalued property in the element Specification window, for example, ownedOperation in Class. Do not specify this property, when there is more than one property assigned to the properties group and/or subgroup, i.e., when there is more than one value added to the Properties property.The property group, to which the multivalued property is assigned, must be specified as a separate tab in the element Specification window, for example, the Use As Node property must be set to true. |
| Filter | Stores the element types (UML metaclasses and custom stereotypes) that will be displayed as property values. |
| Title Bar Name | Stores the property group title bar name shown in the element Specification window. |
| Title Bar Description | Stores the property group title bar description shown in the element Specification window. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><table class="wrapped fixed-table" style="letter-spacing: 0.0px;"><colgroup><col style="width: 246.0px;" /><col style="width: 917.0px;" /></colgroup><tbody><tr><th>Property</th><th>Description</th></tr><tr><td><strong>Show Group In Compartment Edit</strong></td><td><div class="layoutArea"><div class="column"><p><span>This property allows for displaying the element properties in the </span><strong>Compartment Edit</strong> <span>dialog &gt; the </span><strong>Element Properties </strong><span>tab and in a note on a diagram either within the property group/subgroup or without it. </span>If the value is <em>true</em>, the property name is displayed as follows: <em>&lt;property_group_name&gt;::&lt;property_name&gt;</em>. If the value is <strong>false</strong>, the property name is displayed as follows:<em> &lt;property_name&gt;</em> . </p></div></div></td></tr><tr><td colspan="1"><strong>Show Group In Dependency Matrix</strong></td><td colspan="1">If the value is <em>true</em>, the property group/subgroup is visible in the <ac:link ac:anchor="Dependency Criteria dialog"><ri:page ri:space-key="MDTWRT" ri:content-title="Selecting criteria" /><ac:plain-text-link-body><![CDATA[Dependency Criteria]]></ac:plain-text-link-body></ac:link> dialog, when you create or edit a <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Dependency Matrix" /></ac:link>.</td></tr><tr><td><strong>Show Group In Element Specification</strong></td><td><div class="layoutArea"><div class="column"><p><span>If the value is </span><em>true</em><span>, the property group/subgroup is visible in the element <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specification window" /></ac:link>. </span></p></div></div></td></tr><tr><td><strong>Show Group In Go To</strong></td><td><div class="layoutArea"><div class="column"><p><span>If the value is </span><em>true</em><span>, the property group/subgroup is visible in element’s shortcut menu as a submenu under the</span> <strong>Go To</strong> <span>menu. </span></p></div></div></td></tr><tr><td><strong>Show Group In Quick Properties</strong></td><td><div class="layoutArea"><div class="column"><p><span>If the value is </span><em>true</em><span>, the property group/subgroup is visible in the element</span> <strong>Properties</strong> <span>panel. </span></p></div></div></td></tr><tr><td><strong>Show Group In Relation Map</strong></td><td><div class="layoutArea"><div class="column"><p><span>If the value is </span> <em>true</em><span>, the property group/subgroup is visible in the </span> <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Specifying criteria, layout, and depth" /><ac:link-body><span>Criterion Editor </span><span>dialog</span></ac:link-body></ac:link><span>, when you create or edit a <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Relation Map" /></ac:link>. </span></p></div></div></td></tr><tr><td><strong>Use As Node</strong></td><td><div class="content-wrapper"><div class="layoutArea"><div class="column"><p><span>If the value is </span><em>true</em><span>, the property group is displayed in a separate tab in the element Specification window and/or </span><strong>Properties</strong> <span>panel. </span></p><p><span>If the value is </span><em>false</em><span>, the property group is displayed as a group in the general (default) pane of the element Specification window and/or </span> <strong>Properties </strong> <span>panel. </span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="39828f64-f20a-4833-af73-8968137ae24c"><ac:rich-text-body><p><span>Do not set this property value to </span><em>true </em><span>for the property subgroup. </span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></div></div></td></tr><tr><td><strong>Properties</strong></td><td><div class="content-wrapper"><div class="layoutArea"><div class="column"><p><span>Stores a list of properties that is visible in the property group or subgroup. </span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="30d13991-51b1-4d1f-a0bc-388a9b6be44a"><ac:rich-text-body><p>Do not set this property value to <em>true</em> for the property subgroup. </p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></div></div></td></tr><tr><td><strong>Columns</strong></td><td><div class="content-wrapper"><div class="layoutArea"><div class="column"><p><span>Stores the specified table columns for showing the values of a multivalued property in the element Specification window, for example, </span> <strong>ownedOperation</strong> <span>in Class. </span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a73ab6a3-e6ea-455c-92cc-c4c63211b54c"><ac:rich-text-body><ul><li>Do not specify this property, when there is more than one property assigned to the properties group and/or subgroup, i.e., when there is more than one value added to the <strong>Properties </strong>property.</li><li><p>The property group, to which the multivalued property is assigned, must be specified as a separate tab in the element Specification window, for example, the <strong>Use As Node</strong> property must be set to true. </p></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></div></div></td></tr><tr><td><strong>Filter</strong></td><td><div class="layoutArea"><div class="column"><p><span>Stores the element types (UML metaclasses and custom stereotypes) that will be displayed as property values. </span></p></div></div></td></tr><tr><td colspan="1"><strong>Title Bar Name</strong></td><td colspan="1">Stores the property group title bar name shown in the element Specification window.</td></tr><tr><td colspan="1"><strong>Title Bar Description</strong></td><td colspan="1">Stores the property group title bar description shown in the element Specification window.</td></tr></tbody></table><p class="auto-cursor-target"><br /></p><p><br /></p>
````
