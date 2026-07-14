# NOMAGIC DOCUMENTATION SPACE: Cameo Data Modeler Plugin 2024x Refresh1

<!--NOMAGIC_SPACE key=CDMP2024xR1 chunk=1 -->

<!--NOMAGIC_PAGE id=170459969 space=CDMP2024xR1 version=2 -->
## PAGE 00001: 2024x Refresh1 Version News

- page_id: `170459969`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459969/2024x+Refresh1+Version+News
- version_number: 2
- version_date: `2024-07-05T09:20:57.133+02:00`
- ancestors: Cameo Data Modeler Plugin
- labels: []

### NORMALIZED CONTENT

### Cameo Data Modeler Plugin

Released on: July 5, 2024

This version was released for compatibility purposes only. It does not contain new capabilities only minor bug fixes.

Check the product compatibility [CONFLUENCE_PAGE title='Product compatibility' space='NMDOC'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h1 style="text-align: center;">Cameo Data Modeler Plugin</h1><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released on: July 5, 2024</span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>This version was released for compatibility purposes only. It does not contain new capabilities only minor bug fixes.</p><p>Check the product compatibility <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Product compatibility" /><ac:plain-text-link-body><![CDATA[here]]></ac:plain-text-link-body></ac:link>.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170459694 space=CDMP2024xR1 version=3 -->
## PAGE 00002: 2024x Version News

- page_id: `170459694`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459694/2024x+Version+News
- version_number: 3
- version_date: `2024-07-05T09:21:21.029+02:00`
- ancestors: Cameo Data Modeler Plugin
- labels: []

### NORMALIZED CONTENT

### Cameo Data Modeler Plugin

Released on: November 10, 2023

This version was released for compatibility purposes only. It does not contain new capabilities only minor bug fixes.

Check the product compatibility [CONFLUENCE_PAGE title='Product compatibility' space='NMDOC'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h1 style="line-height: 1.66667;letter-spacing: normal;text-align: center;">Cameo Data Modeler Plugin</h1><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released on: November 10, 2023</span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>This version was released for compatibility purposes only. It does not contain new capabilities only minor bug fixes.</p><p>Check the product compatibility <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Product compatibility" /><ac:plain-text-link-body><![CDATA[here]]></ac:plain-text-link-body></ac:link>.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170459764 space=CDMP2024xR1 version=5 -->
## PAGE 00003: Access control

- page_id: `170459764`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459764/Access+control
- version_number: 5
- version_date: `2024-05-08T13:55:21.362+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support > Database modeling
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

127221132

#### CONTENT-COLUMN: Note

127221134

127221131

**On this page**

33

#### CONTENT-BLOCK: Note

127221133

###### [IMAGE alt='' src='']Access control example.

SQL has means to specify and control the rules of access to various data objects. This subset of SQL language is sometimes called Data Control Language. The relevant concepts are: User, Group, Role (3 different kinds of authorization subjects), Permission and Role Authorization (2 kinds of access control rules). Possible object types for access control varies depending on database flavor, but usually Tables, User-defined Types, Domains, Routines, Sequences can be specified as the target objects of access control.

##### User

#### NOTE: Note

Note

SQL User is modeled as UML Actor with the «User» stereotype applied.

User object represents the single user person in the system. User is subject to access control rules.

Besides the standard SQL element properties, user has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Owned Schema | Schemas that are owned by this user. |

##### Group

#### NOTE: Note

Note

SQL Group is modeled as UML Actor with the «Group» stereotype applied.

Group object represents a collection of Users. Group is subject to access control rules, and allows specifying access control rules on several users simultaneously.

Besides the standard SQL element properties, group has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| User | Collection of users the group is made of. |
| Owned Schema | Schemas that are owned by this group. |

##### Role

#### NOTE: Note

Note

SQL Role is modeled as UML Actor with the «Role» stereotype applied.

Role object represents a specific role (typical activities) that can be played by users. Role is subject to access control rules, and allows specifying access control rules for all subjects, playing this role.

Besides the standard SQL element properties, role has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Owned Schema | Schemas that are owned by this role. |

##### Privilege

#### NOTE: Note

Note

SQL Privilege is modeled as UML Dependency with the «Privilege» stereotype applied.

Privilege relationship expresses the fact that the permission to perform specified action on specified object (relationship target) is granted to specified grantee (relationship source). Grantee can be any authorization subject - Use, Group or another Role. Object can by another SQL object (the precise list of object types, that can be targeted by privileges, varies by database type).

Privilege corresponds to SQL grant privilege statement as follows.

```text
[()] ON  TO  [WITH HIERARCHY
OPTION][WITH GRANT OPTION]]]>
```

Besides the standard SQL element properties, privilege has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Action | Specifies action that is being granted (such as SELECT or UPDATE). |
| Action Objects | Specifies additional more narrow subobject lists, on which the specified action is permitted (usually column list for SELECT or UPDATE). |
| Grantable | Specifies that this privilege can be further re-granted to other subjects by the recipients. Corresponds to WITH GRANT OPTION part of GRANT statement. |
| With Hierarchy | Specifies that this privilege applies to subobjects (subtables). Corresponds to WITH HIERARCHY OPTION part of the GRANT statement. |
| Grantor | Subject, who grants this privilege to the grantees. |

##### Role authorization

#### NOTE: Note

Note

SQL Role Authorization is modeled as UML Dependency with «RoleAuthorization» stereotype applied.

Role authorization relationship expresses the fact that the specified role (relationship target) is granted to specified grantee (relationship source). Grantee can be any authorization subject - Use, Group or another Role.

Role authorization corresponds to SQL grant role statement as follows.

```text
TO  [WITH ADMIN OPTION]]]>
```

Besides the standard SQL element properties, role authorization has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Grantable | Specifies that this role can be further re-granted to other subjects by the recipients. Corresponds to WITH ADMIN OPTION part of GRANT statement. |
| Grantor | Subject, who grants this role to the grantees. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3c4efbca-3fa6-4a75-9275-1732acae08a5"><ac:parameter ac:name="id">127221132</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="a43a8f85-4ac3-4528-a5d6-8d6097b88179"><ac:parameter ac:name="id">127221134</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cc3c8e7b-04f0-41db-b81b-96970287164d"><ac:parameter ac:name="id">127221131</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="1c972d95-8c6e-4247-94dd-a267191993c4"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="549aa6ba-9c2b-472c-ac25-1cfc3721df5a"><ac:parameter ac:name="id">127221133</ac:parameter><ac:rich-text-body><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 31 Access Control Example.png" /></ac:image>Access control example.</h6><p>SQL has means to specify and control the rules of access to various data objects. This subset of SQL language is sometimes called Data Control Language. The relevant concepts are: User, Group, Role (3 different kinds of authorization subjects), Permission and Role Authorization (2 kinds of access control rules). Possible object types for access control varies depending on database flavor, but usually Tables, User-defined Types, Domains, Routines, Sequences can be specified as the target objects of access control.</p><h3>User</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="eda2a134-da0d-4d2f-9850-52d8b753e358"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL User is modeled as UML Actor with the «User» stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>User object represents the single user person in the system. User is subject to access control rules.</p><p>Besides the standard SQL element properties, user has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9457%;"><colgroup><col style="width: 24.144%;" /><col style="width: 75.856%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Owned Schema</strong></td><td>Schemas that are owned by this user.</td></tr></tbody></table><h3>Group</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="67b477f8-2ba7-4671-9ac5-afaccc913d79"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Group is modeled as UML Actor with the «Group» stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>Group object represents a collection of Users. Group is subject to access control rules, and allows specifying access control rules on several users simultaneously.</p><p>Besides the standard SQL element properties, group has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.7257%;"><colgroup><col style="width: 24.313%;" /><col style="width: 75.687%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>User</strong></td><td>Collection of users the group is made of.</td></tr><tr><td><strong>Owned Schema</strong></td><td>Schemas that are owned by this group.</td></tr></tbody></table><h3>Role</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d4ae25de-aab8-4d8c-ad92-1f4a24a1082c"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Role is modeled as UML Actor with the «Role» stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>Role object represents a specific role (typical activities) that can be played by users. Role is subject to access control rules, and allows specifying access control rules for all subjects, playing this role.</p><p>Besides the standard SQL element properties, role has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 23.7727%;" /><col style="width: 76.2273%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Owned Schema</strong></td><td>Schemas that are owned by this role.</td></tr></tbody></table><h3>Privilege</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="914b4477-f891-4b63-b32c-10cb1cc5921d"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Privilege is modeled as UML Dependency with the «Privilege» stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>Privilege relationship expresses the fact that the permission to perform specified action on specified object (relationship target) is granted to specified grantee (relationship source). Grantee can be any authorization subject - Use, Group or another Role. Object can by another SQL object (the precise list of object types, that can be targeted by privileges, varies by database type).</p><p>Privilege corresponds to SQL grant privilege statement as follows.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c3f62bdb-05bc-4b58-be12-0c2b3af69a55"><ac:plain-text-body><![CDATA[GRANT <action>[(<column list>)] ON <object> TO <grantee> [WITH HIERARCHY
OPTION][WITH GRANT OPTION]]]></ac:plain-text-body></ac:structured-macro><p>Besides the standard SQL element properties, privilege has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 23.9347%;" /><col style="width: 76.0654%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Action</strong></td><td>Specifies action that is being granted (such as SELECT or UPDATE).</td></tr><tr><td><strong>Action Objects</strong></td><td>Specifies additional more narrow subobject lists, on which the specified action is permitted (usually column list for SELECT or UPDATE).</td></tr><tr><td><strong>Grantable</strong></td><td>Specifies that this privilege can be further re-granted to other subjects by the recipients. Corresponds to WITH GRANT OPTION part of GRANT statement.</td></tr><tr><td><strong>With Hierarchy</strong></td><td><p>Specifies that this privilege applies to subobjects (subtables). Corresponds to WITH HIERARCHY OPTION part of the GRANT statement.</p></td></tr><tr><td><strong>Grantor</strong></td><td>Subject, who grants this privilege to the grantees.</td></tr></tbody></table><h3>Role authorization</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9ed80462-be26-4efb-a8a8-0d35e2b7819d"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Role Authorization is modeled as UML Dependency with «RoleAuthorization» stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>Role authorization relationship expresses the fact that the specified role (relationship target) is granted to specified grantee (relationship source). Grantee can be any authorization subject - Use, Group or another Role.</p><p>Role authorization corresponds to SQL grant role statement as follows.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="62f836b3-dbaf-46ff-8e57-6d9d96054077"><ac:plain-text-body><![CDATA[GRANT <role> TO <grantee> [WITH ADMIN OPTION]]]></ac:plain-text-body></ac:structured-macro><p>Besides the standard SQL element properties, role authorization has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.8903%;"><colgroup><col style="width: 24.0531%;" /><col style="width: 75.9469%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Grantable</strong></td><td>Specifies that this role can be further re-granted to other subjects by the recipients. Corresponds to WITH ADMIN OPTION part of GRANT statement.</td></tr><tr><td><strong>Grantor</strong></td><td>Subject, who grants this role to the grantees.</td></tr></tbody></table></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459915 space=CDMP2024xR1 version=5 -->
## PAGE 00004: Annotation

- page_id: `170459915`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459915/Annotation
- version_number: 5
- version_date: `2024-05-08T14:25:39.656+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Comment with or without the stereotype XSDannotation. The documentation content maps to the UML Comment body (name).

“documentation” maps as a UML comment, as outlined below:

- the “content” value - the comment name.

- the “xml:lang” value – the tag “xml:lang” value.

- the source value – the tag ”source” value.

“appinfo” maps as a tag value with the name “appInfoSource”:

- the “source” value will be the tag value.
- the “content” will be documentation for the tagged value.

When several annotation nodes appear on one element node, mapping shall be done as follows:

- the “documentation” text shall be merged into one UML comment with merged content, but the “content” and “xml:lang” tag values shall represent only the first matched values.
- “appInfo” shall have “content” merged into one tag “appInfoSource” comment, but the tag value shall represent the “appinfo” matched first.

#### PANEL: annotation XML representation summary

annotation XML representation summary

```text
<annotation
```

```text
id = ID
```

```text
{any attributes with non-schema namespace …}>
```

```text
Content: (anninfn I dorumpnrarioWl.
```

```text
</annotation>
```

```text
<appinfo
```

```text
source = anyURI>
```

```text
Content: ({any})*
```

```text
</appinfo>
```

```text
<documentation
```

```text
source = anyURI
```

```text
xml:lang = language>
```

```text
Content: ({any})*
```

```text
</documentation>
```

#### PANEL: XML representations of three kinds of annotation

XML representations of three kinds of annotation

```text
<xs:simpleType fn:note="special">
```

```text
<xs:annotation>
```

```text
<xs:documentation>A type for experts only</xs:documentation>		<xs:appinfo>
```

```text
<fn:specialHandling>checkForPrimes</fn:specialHandling>		</xs:appinfo>
```

```text
</xs:annotation>
```

###### [IMAGE alt='' src='']

###### annotation UML model example.

#### PANEL: annotation XML code sample

annotation XML code sample

```text
<xs:schema xmlns:nm = "http://nomagic.com" xmlns:xs = "http://www.w3.org/2001/XMLSchema" targetNamespace = "http://nomagic.com">	<xs:annotation >
```

```text
<xs:appinfo source = "infoSource">infoContent</xs:appinfo>		<xs:documentation source = "documentation source" xml:lang = "EN">the documentation for this schema</xs:documentation>	</xs:annotation>
```

```text
</xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Comment with or without the stereotype XSDannotation. The documentation content maps to the UML Comment body (name).</p><p>“documentation” maps as a UML comment, as outlined below:</p><ul><li>the “content” value - the comment name.</li></ul><ul><li>the “xml:lang” value – the tag “xml:lang” value.</li></ul><ul><li>the source value – the tag ”source” value.</li></ul><p>“appinfo” maps as a tag value with the name “appInfoSource”:</p><ul><li>the “source” value will be the tag value.</li><li>the “content” will be documentation for the tagged value.</li></ul><p>When several annotation nodes appear on one element node, mapping shall be done as follows:</p><ul><li>the “documentation” text shall be merged into one UML comment with merged content, but the “content” and “xml:lang” tag values shall represent only the first matched values.</li><li><p>“appInfo” shall have “content” merged into one tag “appInfoSource” comment, but the tag value shall represent the “appinfo” matched first.</p></li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="cc54fd92-d6c2-4aa6-bba6-b111375d12c5"><ac:parameter ac:name="title">annotation XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;annotation</pre><pre>	id = ID</pre><pre>	{any attributes with non-schema namespace …}&gt;</pre><pre>	Content: (anninfn I dorumpnrarioWl.</pre><pre>&lt;/annotation&gt;</pre><pre>&lt;appinfo</pre><pre>	source = anyURI&gt;</pre><pre>	Content: ({any})*</pre><pre>&lt;/appinfo&gt;</pre><pre>&lt;documentation</pre><pre>	source = anyURI</pre><pre>	xml:lang = language&gt;</pre><pre>	Content: ({any})*</pre><pre>&lt;/documentation&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="7667825d-5075-43b2-ad75-9d42a1bfe3e3"><ac:parameter ac:name="title">XML representations of three kinds of annotation</ac:parameter><ac:rich-text-body><pre>&lt;xs:simpleType fn:note=&quot;special&quot;&gt;</pre><pre>	&lt;xs:annotation&gt;</pre><pre>		&lt;xs:documentation&gt;A type for experts only&lt;/xs:documentation&gt;<br />		&lt;xs:appinfo&gt;</pre><pre>			&lt;fn:specialHandling&gt;checkForPrimes&lt;/fn:specialHandling&gt;<br />		&lt;/xs:appinfo&gt;</pre><pre>	&lt;/xs:annotation&gt;</pre></ac:rich-text-body></ac:structured-macro><h6><ac:image ac:height="250"><ri:attachment ri:filename="Figure 111 annotation UML Model Example.png" /></ac:image></h6><h6 style="text-align: center;">annotation UML model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9e1b2a62-911a-446f-b27c-30e93e38410f"><ac:parameter ac:name="title">annotation XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot;&gt;<br />	&lt;xs:annotation &gt;</pre><pre>		&lt;xs:appinfo source = &quot;infoSource&quot;&gt;infoContent&lt;/xs:appinfo&gt;<br />		&lt;xs:documentation source = &quot;documentation source&quot; xml:lang = &quot;EN&quot;&gt;the documentation for this schema&lt;/xs:documentation&gt;<br />	&lt;/xs:annotation&gt;</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459930 space=CDMP2024xR1 version=5 -->
## PAGE 00005: Any and anyAttribute

- page_id: `170459930`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459930/Any+and+anyAttribute
- version_number: 5
- version_date: `2024-05-08T14:26:24.837+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDany or XSDanyAttribute.

maxOccurs - to multiplicity upper range. The unbounded value maps to an asterisk in UML.

minOccurs – to multiplicity lower range.

annotation maps to Attribute documentation.

Other properties map to TaggedValues.

#### PANEL: any and anyAttribute XML representation summary

any and anyAttribute XML representation summary

```text
<any
```

```text
id = ID
```

```text
maxOccurs = (nonNegativeInteger | unbounded) : 1
```

```text
minOccurs = nonNegativeInteger : 1
```

```text
namespace = ((##any | ##other)| List of (anyURI | (##targetNamespace |
```

```text
##local)) ) : ##any 	processContents = (lax | skip | strict) : strict
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</any>
```

```text
<anyAttribute
```

```text
id = ID
```

```text
namespace = ((##any | ##other) | List of (anyURI | (##targetNamespace |
```

```text
##local)) ) : ##any
```

```text
processContents = (lax | skip | strict) : strict
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)</anyAttribute>
```

#### PANEL: XML representations of the four basic types of wildcard

XML representations of the four basic types of wildcard

```text
<xs:any processContents = "skip"/>
```

```text
<xs:any namespace = "##other" processContents="lax"/>
```

```text
<xs:any namespace = "http://www.w3.org/1999/XSL/Transform"/>
```

```text
<xs:any namespace = "##targetNamespace"/>
```

```text
<xs:anyAttribute namespace = "http://www.w3.org/XML/1998/namespace"/>
```

###### [IMAGE alt='' src='']

###### any and anyAttribute UML model example.

#### PANEL: any and anyAttribute XML code sample

any and anyAttribute XML code sample

```text
<?xml version='1.0' encoding='Cp1252'?>
```

```text
<xs:schema xmlns:nm = "http://nomagic.com" xmlns:xs = "http://www.w3.org/2001/XMLSchema" targetNamespace = "http://nomagic.com">
```

```text
<xs:group name = "my_type" >		<xs:choice>
```

```text
<xs:any id = "anyID" namespace = "http://bla" processContents = "strict" minOccurs = "0" maxOccurs = "1" >
```

```text
<xs:annotation>					<xs:documentation>any documentation</xs:documentation>
```

```text
</xs:annotation>			</xs:any>
```

```text
</xs:choice>
```

```text
</xs:group>
```

```text
<xs:attributeGroup name = "attr_group">
```

```text
<xs:anyAttribute id = "anyID" namespace = "http:\bla.bla.bla" processContents = "skip">
```

```text
<xs:annotation>
```

```text
<xs:documentation>any attribute documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
</xs:anyAttribute>
```

```text
</xs:attributeGroup>
```

```text
</xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDany or XSDanyAttribute.</p><p>maxOccurs - to multiplicity upper range. The unbounded value maps to an asterisk in UML.</p><p>minOccurs – to multiplicity lower range.</p><p>annotation maps to Attribute documentation.</p><p style="text-align: left;">Other properties map to TaggedValues.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="42e81994-14c5-406a-a105-cada8b3179da"><ac:parameter ac:name="title">any and anyAttribute XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;any</pre><pre>	id = ID</pre><pre>	maxOccurs = (nonNegativeInteger | unbounded) : 1</pre><pre>	minOccurs = nonNegativeInteger : 1</pre><pre>	namespace = ((##any | ##other)| List of (anyURI | (##targetNamespace |</pre><pre>##local)) ) : ##any <br />	processContents = (lax | skip | strict) : strict</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/any&gt;</pre><pre>&lt;anyAttribute</pre><pre>	id = ID</pre><pre>	namespace = ((##any | ##other) | List of (anyURI | (##targetNamespace |</pre><pre>##local)) ) : ##any</pre><pre>	processContents = (lax | skip | strict) : strict</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)<br />&lt;/anyAttribute&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="2cc53c1f-17ef-4a45-914f-c08c33c319de"><ac:parameter ac:name="title">XML representations of the four basic types of wildcard</ac:parameter><ac:rich-text-body><pre>&lt;xs:any processContents = &quot;skip&quot;/&gt;</pre><pre>&lt;xs:any namespace = &quot;##other&quot; processContents=&quot;lax&quot;/&gt;</pre><pre>&lt;xs:any namespace = &quot;<a href="http://www.w3.org/1999/XSL/Transform">http://www.w3.org/1999/XSL/Transform</a>&quot;/&gt;</pre><pre>&lt;xs:any namespace = &quot;##targetNamespace&quot;/&gt;</pre><pre>&lt;xs:anyAttribute namespace = &quot;<a href="http://www.w3.org/XML/1998/namespace">http://www.w3.org/XML/1998/namespace</a>&quot;/&gt;</pre></ac:rich-text-body></ac:structured-macro><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 123 any and anyAttribute UML Model Example.png" /></ac:image></h6><h6 style="text-align: center;">any and anyAttribute UML model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e6e231b0-6ed2-4baf-826d-28b25624a0cd"><ac:parameter ac:name="title">any and anyAttribute XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;?xml version='1.0' encoding='Cp1252'?&gt;<br /><br /></pre><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot;&gt;</pre><pre>	&lt;xs:group name = &quot;my_type&quot; &gt;<br />		&lt;xs:choice&gt;</pre><pre>			&lt;xs:any id = &quot;anyID&quot; namespace = &quot;<a href="http://bla">http://bla</a>&quot; processContents = &quot;strict&quot; minOccurs = &quot;0&quot; maxOccurs = &quot;1&quot; &gt;</pre><pre>				&lt;xs:annotation&gt;<br />					&lt;xs:documentation&gt;any documentation&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;<br />			&lt;/xs:any&gt;</pre><pre>		&lt;/xs:choice&gt;</pre><pre>	&lt;/xs:group&gt;</pre><pre>	&lt;xs:attributeGroup name = &quot;attr_group&quot;&gt;</pre><pre>		&lt;xs:anyAttribute id = &quot;anyID&quot; namespace = &quot;http:\bla.bla.bla&quot; processContents = &quot;skip&quot;&gt;</pre><pre>			&lt;xs:annotation&gt;</pre><pre>				&lt;xs:documentation&gt;any attribute documentation&lt;/xs:documentation&gt;</pre><pre>			&lt;/xs:annotation&gt;</pre><pre>		&lt;/xs:anyAttribute&gt;</pre><pre>	&lt;/xs:attributeGroup&gt;</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459826 space=CDMP2024xR1 version=4 -->
## PAGE 00006: Attribute

- page_id: `170459826`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459826/Attribute
- version_number: 4
- version_date: `2024-05-08T13:11:35.459+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

- XML schema attribute maps to UML Attribute with stereotype XSDattribute.
- default maps to initial UML Attribute or AssociationEnd value.
- annotation – to UML Attribute or AssociationEnd documentation.
- name – to UML Attribute or AssociationEnd name.
- type or content simpleType – to UML Attribute or AssociationEnd type.

#### PANEL: Other attributes or elements maps to corresponding tagged values

Other attributes or elements maps to corresponding tagged values

```text
<attribute
```

```text
default = string
```

```text
fixed = string
```

```text
form = (qualified | unqualified)
```

```text
id = ID
```

```text
name = NCName
```

```text
ref = QName
```

```text
type = QName
```

```text
use = (optional | prohibited | required ) optional
```

```text
{any attributes with non-schema namespace ...} >
```

```text
Content: (annotation?,(simpleType?))</attribute>
```

Example

```text
]]>
```

Ref value is generated from ref or refString TaggedValue. One of ref or name must be present, but not both.

If ref is present, then all of <simpleType>, form and type must be absent. Type and <simpleType> must not both be present.

[IMAGE alt='' src='']

Example of attribute UML model (1).

<xs:schema xmlns:nm = "[http://nomagic.com](http://nomagic.com)" xmlns:xs = ["http://www.w3.org/2001/XMLSchema"](http://www.w3.org/2001/XMLSchema) targetNamespace =["http://nomagic.com"](http://nomagic.com/)

#### PANEL: Example of attribute UML code

Example of attribute UML code

```text
<xs:attribute name = "name" type = "xs:string" default = "minde"
```

```text
fixed = "fixed_value" form = "qualified" use "optional" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >name attribute documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
</xs:attribute>
```

```text
<xs:attribute name = "address" fixed = "fixed_value" form =
```

```text
"qualified" use = "optional" >  		<xs:annotation >
```

```text
<xs:documentation >surname attribute
```

```text
documentation‹/xs:documentation>		</xs:annotation> 		<xs:simpleType >
```

```text
<xs:restriction base = "xs:string" />
```

```text
‹/xs:simpleType> 	</xs:attribute>
```

```text
<xs:attribute name = "surname" type    "xs:string" />
```

```text
<xs:attributeGroup name = "attr_group" >
```

```text
<xs:attribute ref    "nm:name" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >reference
```

```text
documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
</xs:attribute>
```

```text
<xs:attribute ref = "nm:surname" />
```

```text
</xs:attributeGroup> </xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ul><li>XML schema attribute maps to UML Attribute with stereotype XSDattribute.</li><li>default maps to initial UML Attribute or AssociationEnd value.</li><li>annotation – to UML Attribute or AssociationEnd documentation.</li><li>name – to UML Attribute or AssociationEnd name.</li><li>type or content simpleType – to UML Attribute or AssociationEnd type.<br /><br /></li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="dd9dfa8d-0f4f-4757-9b3c-076e88c23b62"><ac:parameter ac:name="title">Other attributes or elements maps to corresponding tagged values</ac:parameter><ac:rich-text-body><pre>&lt;attribute </pre><pre>	default = string  </pre><pre>	fixed = string  </pre><pre>	form = (qualified | unqualified)</pre><pre>	id = ID </pre><pre>	name = NCName</pre><pre>	ref = QName</pre><pre>	type = QName  </pre><pre>	use = (optional | prohibited | required ) optional </pre><pre>	{any attributes with non-schema namespace ...} &gt;</pre><pre>	Content: (annotation?,(simpleType?))<br />&lt;/attribute&gt;</pre></ac:rich-text-body></ac:structured-macro><p>Example</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a5dcb2fb-e366-44d9-b53b-867fb83784ce"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[<xs:attribute name="age" type="xs:positiveInteger" use="required"/>]]></ac:plain-text-body></ac:structured-macro><p>Ref value is generated from ref or refString TaggedValue. One of ref or name must be present, but not both.</p><p>If ref is present, then all of &lt;simpleType&gt;, form and type must be absent. Type and &lt;simpleType&gt; must not both be present.</p><p><ac:image><ri:attachment ri:filename="Figure 49 Example of Attribute UML Model.png"><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Attribute" /></ri:attachment></ac:image></p><p>Example of attribute UML model (1).</p><p>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; xmlns:xs = <a href="http://www.w3.org/2001/XMLSchema">&quot;http://www.w3.org/2001/XMLSchema&quot;</a> targetNamespace =<a href="http://nomagic.com/"> &quot;http://nomagic.com&quot;</a></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ffe53df7-0713-40b6-8972-6bfdbd423ca2"><ac:parameter ac:name="title">Example of attribute UML code</ac:parameter><ac:rich-text-body><pre>	&lt;xs:attribute name = &quot;name&quot; type = &quot;xs:string&quot; default = &quot;minde&quot;</pre><pre>fixed = &quot;fixed_value&quot; form = &quot;qualified&quot; use &quot;optional&quot; &gt;</pre><pre>		&lt;xs:annotation &gt;</pre><pre>			&lt;xs:documentation &gt;name attribute <br />documentation&lt;/xs:documentation&gt;</pre><pre>		&lt;/xs:annotation&gt;</pre><pre>	&lt;/xs:attribute&gt;</pre><pre>	&lt;xs:attribute name = &quot;address&quot; fixed = &quot;fixed_value&quot; form =</pre><pre>&quot;qualified&quot; use = &quot;optional&quot; &gt; <br /> 		&lt;xs:annotation &gt;</pre><pre>			&lt;xs:documentation &gt;surname attribute</pre><pre>documentation‹/xs:documentation&gt;<br />		&lt;/xs:annotation&gt; <br />		&lt;xs:simpleType &gt;</pre><pre>			&lt;xs:restriction base = &quot;xs:string&quot; /&gt;</pre><pre>		‹/xs:simpleType&gt; <br />	&lt;/xs:attribute&gt;</pre><pre>	&lt;xs:attribute name = &quot;surname&quot; type    &quot;xs:string&quot; /&gt;</pre><pre>	&lt;xs:attributeGroup name = &quot;attr_group&quot; &gt;</pre><pre>		&lt;xs:attribute ref    &quot;nm:name&quot; &gt;</pre><pre>			&lt;xs:annotation &gt;</pre><pre>				&lt;xs:documentation &gt;reference</pre><pre>documentation&lt;/xs:documentation&gt;</pre><pre>			&lt;/xs:annotation&gt;</pre><pre>		&lt;/xs:attribute&gt;</pre><pre>		&lt;xs:attribute ref = &quot;nm:surname&quot; /&gt;</pre><pre>	&lt;/xs:attributeGroup&gt; <br />&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=170459844 space=CDMP2024xR1 version=5 -->
## PAGE 00007: AttributeGroup

- page_id: `170459844`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459844/AttributeGroup
- version_number: 5
- version_date: `2024-05-08T14:21:23.364+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

An Attribute Group maps to a simple UML Class with the stereotype XSDattributeGroup.

- name – to UML Class name
- annotation – to UML Class documentation
- attribute – to inner UML Attribute or AssociationEnd with XSDattribute
- stereotype.
- attributeGroup - the inner attributeGroup must only be reference. This reference maps to Attribute or AssociationEnd with the type of referenced attributeGroup. The opposite Association End kind must be aggregated and it must be navigable.
- anyAttribute – to inner UML Attribute with stereotype XSDanyAttribute .

If the reference is generated, a name is not generated.

When an **<attributeGroup>**appears as a daughter of **<schema> or <redefine>,**it corresponds to an attribute group definition, shown below. When it appears as a daughter of **<complexType> or <attributeGroup>,**it does not correspond to any component as such.

###### [IMAGE alt='' src='']

###### attributeGroup UML model example.

#### PANEL: attributeGroup UML model example with associated XML

attributeGroup UML model example with associated XML

```text
<xs:schema xmlns:nm = "http://nomagic.com" xmlns:xs = "http://www.w3.org/2001/XMLSchema" targetNamespace = "http://nomagic.com"
```

```text
<xs:attributeGroup name = "global_attr_group">
```

```text
<xs:attribute name = "address" type = "xs:string" />	</xs:attributeGroup>
```

```text
<xs:attributeGroup name = "attr_group_name" >
```

```text
<xs:annotation>
```

```text
<xs:documentation>attribute group documentation</xs:documentation>		</xs:annotation>
```

```text
<xs:attribute name = "surname" type = "xs:string"/>
```

```text
<xs:attribute name = "name" type = "xs:string" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >name attribute documentation</xs:documentation>
```

```text
</xs:annotation>		</xs:attribute>
```

```text
<xs:attributeGroup ref = "nm:global_attr_group2" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >reference documentation</xs:documentation>
```

```text
</xs:annotation>		</xs:attributeGroup>		<xs:anyAttribute />
```

```text
</xs:attributeGroup>
```

```text
<xs:attributeGroup name = "global_attr_group2" >		<xs:attribute name = "city" type = "xs:string"/>	</xs:attributeGroup>
```

```text
</xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An Attribute Group maps to a simple UML Class with the stereotype XSDattributeGroup.</p><ul><li>name – to UML Class name</li><li>annotation – to UML Class documentation</li><li>attribute – to inner UML Attribute or AssociationEnd with XSDattribute</li><li>stereotype.</li><li>attributeGroup - the inner attributeGroup must only be reference. This reference maps to Attribute or AssociationEnd with the type of referenced attributeGroup. The opposite Association End kind must be aggregated and it must be navigable.</li><li>anyAttribute – to inner UML Attribute with stereotype <em>XSDanyAttribute</em>.</li></ul><p>If the reference is generated, a name is not generated.</p><p>When an <strong><u>&lt;attributeGroup&gt;</u> </strong>appears as a daughter of <strong> <u>&lt;schema&gt;</u> or <u>&lt;redefine&gt;,</u> </strong>it corresponds to an attribute group definition, shown below. When it appears as a daughter of <strong><u>&lt;complexType&gt;</u>  or <u>&lt;attributeGroup&gt;,</u> </strong>it does not correspond to any component  as such.</p><h6><ac:image ac:height="250"><ri:attachment ri:filename="Figure 61 attributeGroup UML Model Example.png" /></ac:image></h6><h6 style="text-align: center;">attributeGroup UML model example.</h6><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="8b1f1691-7cda-4088-acd4-5f288d2da77f"><ac:parameter ac:name="title">attributeGroup UML model example with associated XML</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.comn">http://nomagic.com&quot;</a> xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLScheman">http://www.w3.org/2001/XMLSchema&quot;</a> targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot;</pre><pre>	&lt;xs:attributeGroup name = &quot;global_attr_group&quot;&gt;</pre><pre>		&lt;xs:attribute name = &quot;address&quot; type = &quot;xs:string&quot; /&gt;<br />	&lt;/xs:attributeGroup&gt;</pre><pre>	&lt;xs:attributeGroup name = &quot;attr_group_name&quot; &gt;</pre><pre>		&lt;xs:annotation&gt;</pre><pre>			&lt;xs:documentation&gt;attribute group documentation&lt;/xs:documentation&gt;<br />		&lt;/xs:annotation&gt;</pre><pre>		&lt;xs:attribute name = &quot;surname&quot; type = &quot;xs:string&quot;/&gt;</pre><pre>		&lt;xs:attribute name = &quot;name&quot; type = &quot;xs:string&quot; &gt;</pre><pre>			&lt;xs:annotation &gt;</pre><pre>				&lt;xs:documentation &gt;name attribute documentation&lt;/xs:documentation&gt;</pre><pre>			&lt;/xs:annotation&gt;<br />		&lt;/xs:attribute&gt;</pre><pre>		&lt;xs:attributeGroup ref = &quot;nm:global_attr_group2&quot; &gt;</pre><pre>			&lt;xs:annotation &gt;</pre><pre>				&lt;xs:documentation &gt;reference documentation&lt;/xs:documentation&gt;</pre><pre>			&lt;/xs:annotation&gt;<br />		&lt;/xs:attributeGroup&gt;<br />		&lt;xs:anyAttribute /&gt;</pre><pre>	&lt;/xs:attributeGroup&gt;</pre><pre>	&lt;xs:attributeGroup name = &quot;global_attr_group2&quot; &gt;<br />		&lt;xs:attribute name = &quot;city&quot; type = &quot;xs:string&quot;/&gt;<br />	&lt;/xs:attributeGroup&gt;</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459699 space=CDMP2024xR1 version=6 -->
## PAGE 00008: Basic concepts

- page_id: `170459699`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459699/Basic+concepts
- version_number: 6
- version_date: `2024-05-08T13:19:17.249+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Entity-relationship (ER) modeling and diagrams
- labels: []

### NORMALIZED CONTENT

An entity is a thing capable of an existence. An entity usually refers to some aspect of the real world, which can be distinguished from other aspects of the real world (a person, place, customer transaction, order, etc.).

An entity is represented by a box shape on the diagram. An entity has two compartments where properties (columns) of the entity can be specified. The upper compartment holds the primary key properties of the entity; the lower compartment holds other properties.

A relationship between entities describes how entities are associated. Relationships are represented by lines, connecting entities. Relationship end adornments indicate multiplicities of these ends. Multiplicity is the number of entity instances that can be associated with a number of another entity instances. Relationship multiplicity is represented by three symbols, the so-called “crow's foot notation” or “Information Engineering notation”.

The following table shows symbols of the relationship multiplicity.

| Name | Value | Notation |
| --- | --- | --- |
| Zero | Zero |  |
| Vertical | One |  |
| Crow's foot | Many |  |

Multiplicity lower bounds and upper bounds are paired into one adornment, as shown in the following table. Note that any lower bound, which is more that 0 is treated as 1 (this also includes lower bounds greater than 1, such as 2.). Also, any upper bound which is greater than 1 is treated as Many (this also includes upper bounds less than unlimited, such as 7.).

| Min | Max | Read as | Figure |
| --- | --- | --- | --- |
| 0 | 1 | One (optional) |  |
| 1 | 1 | One (mandatory) |  |
| 0 | Many | Many (optional) |  |
| 1 | Many | Many (mandatory) |  |

[IMAGE alt='' src='']

###### Basic ER diagram example.

#### NOTE: Note

Note

- Some authors use Entity Type term to signify the description of a set of entities and Entity Instance term to signify concrete exemplar from that set. Entity term used in this manual corresponds to Entity Type .
- Data modeling world frequently uses term Cardinality to denote the allowable numbers of entity instances, which can be associated. But with the rise of the UML, the more correct term Multiplicity was introduced and term Cardinality is only used to denote concrete numbers of entity instances, which are associated. Hence in the example Person [0..1]------
- -[0..*] Book, the ranges [0..1] and [0..*] are called multiplicities. And if we have person “John Doe” associated with books “Moby Dick” and “Origin of Species”, we have a cardinality of 2 for loaned books role (and 1 on an opposite end - current reader role). Note that cardinality is always concrete number while multiplicity denotes range of possible cardinalities.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An entity is a thing capable of an existence. An entity usually refers to some aspect of the real world, which can be distinguished from other aspects of the real world (a person, place, customer transaction, order, etc.).</p><p>An entity is represented by a box shape on the diagram. An entity has two compartments where properties (columns) of the entity can be specified. The upper compartment holds the primary key properties of the entity; the lower compartment holds other properties.</p><p>A relationship between entities describes how entities are associated. Relationships are represented by lines, connecting entities. Relationship end adornments indicate multiplicities of these ends. Multiplicity is the number of entity instances that can be associated with a number of another entity instances. Relationship multiplicity is represented by three symbols, the so-called “crow's foot notation” or “Information Engineering notation”.</p><p>The following table shows symbols of the relationship multiplicity.</p><table class="relative-table wrapped" style="width: 69.9945%;"><colgroup><col style="width: 42.9451%;" /><col style="width: 24.9216%;" /><col style="width: 32.1333%;" /></colgroup><tbody><tr><th style="text-align: left;">Name</th><th style="text-align: left;">Value</th><th style="text-align: left;">Notation</th></tr><tr><td>Zero</td><td>Zero</td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="Zero Notation.png" /></ac:image></p></div></td></tr><tr><td>Vertical</td><td>One</td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="Vertical Notation.png" /></ac:image></p></div></td></tr><tr><td><p>Crow's foot</p></td><td>Many</td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="Crow's Foot Notation.png" /></ac:image></p></div></td></tr></tbody></table><p>Multiplicity lower bounds and upper bounds are paired into one adornment, as shown in the following table. Note that any lower bound, which is more that 0 is treated as 1 (this also includes lower bounds greater than 1, such as 2.). Also, any upper bound which is greater than 1 is treated as Many (this also includes upper bounds less than unlimited, such as 7.).</p><table class="relative-table wrapped" style="width: 70.1042%;"><colgroup><col style="width: 17.7617%;" /><col style="width: 25.3511%;" /><col style="width: 24.7285%;" /><col style="width: 32.1587%;" /></colgroup><tbody><tr><th>Min</th><th>Max</th><th>Read as</th><th>Figure</th></tr><tr><td>0</td><td>1</td><td>One (optional)</td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="One Optional Pairing.png" /></ac:image></p></div></td></tr><tr><td>1</td><td>1</td><td>One (mandatory)</td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="One Mandatory Pairing.png" /></ac:image></p></div></td></tr><tr><td>0</td><td>Many</td><td>Many (optional)</td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="Many Optional Pairing.png" /></ac:image></p></div></td></tr><tr><td colspan="1">1</td><td colspan="1">Many</td><td colspan="1">Many (mandatory)</td><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="Many Mandatory Pairing.png" /></ac:image></p></div></td></tr></tbody></table><p><ac:image ac:align="center"><ri:attachment ri:filename="Basic ER Diagram Example.png" /></ac:image></p><h6 style="text-align: center;">Basic ER diagram example.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b767ba70-1442-4a55-8ae0-36e002775508"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>Some authors use <strong>Entity Type </strong>term to signify the description of a set of entities and <strong>Entity </strong><strong>Instance </strong>term to signify concrete exemplar from that set. <strong>Entity </strong>term used in this manual corresponds to <strong>Entity Type</strong>.</li><li>Data modeling world frequently uses term Cardinality to denote the allowable numbers of entity instances, which can be associated. But with the rise of the UML, the more correct term <strong>Multiplicity </strong>was introduced and term <strong>Cardinality </strong>is only used to denote concrete numbers of entity instances, which are associated. Hence in the example Person [0..1]------</li><li>-[0..*] Book, the ranges [0..1] and [0..*] are called multiplicities. And if we have person “John Doe” associated with books “Moby Dick” and “Origin of Species”, we have a cardinality of 2 for loaned books role (and 1 on an opposite end - current reader role). Note that cardinality is always concrete number while multiplicity denotes range of possible cardinalities.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459716 space=CDMP2024xR1 version=6 -->
## PAGE 00009: Business entity-relationship diagrams

- page_id: `170459716`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459716/Business+entity-relationship+diagrams
- version_number: 6
- version_date: `2024-05-08T13:19:52.412+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Entity-relationship (ER) modeling and diagrams
- labels: []

### NORMALIZED CONTENT

A Business ER diagram is a simplified version of the ER diagram. The Business ER diagram shows entities only as boxes (without structure) and the relationships between them. It is useful for high-level, abstract domain modeling that provides a structure for business data or defines business terminology.

You can draw these diagrams using the same ER diagram simply by suppressing both the primary key and column compartments on all the entities. A more convenient way to do this is to select all the entities (hold down **ALT** and click all relevant entities) and use the **Suppress All**button on the **Shape Editing** toolbar of the diagram.

[IMAGE alt='' src='']

###### Multi-selecting all entities by pressing ALT and clicking all relevant entities.

[IMAGE alt='' src='']

###### Using the Suppress All button on the Shape Editing toolbar of the diagram to only show entities as boxes (without structure) and the relationships between them.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Business ER diagram is a simplified version of the ER diagram. The Business ER diagram shows entities only as boxes (without structure) and the relationships between them. It is useful for high-level, abstract domain modeling that provides a structure for business data or defines business terminology.</p><p>You can draw these diagrams using the same ER diagram simply by suppressing both the primary key and column compartments on all the entities. A more convenient way to do this is to select all the entities (hold down <strong>ALT</strong> and click all relevant entities) and use the <strong>Suppress All </strong>button on the <strong>Shape Editing</strong> toolbar of the diagram.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 143 Suppress Button (Before).png" /></ac:image></p><h6 style="text-align: center;">Multi-selecting all entities by pressing ALT and clicking all relevant entities.</h6><p style="text-align: center;"><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 144 Suppress Button (After).png" /></ac:image></p><h6 style="text-align: center;">Using the Suppress All button on the Shape Editing toolbar of the diagram to only show entities as boxes (without structure) and the relationships between them.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=170459693 space=CDMP2024xR1 version=2 -->
## PAGE 00010: Cameo Data Modeler Plugin

- page_id: `170459693`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459693/Cameo+Data+Modeler+Plugin
- version_number: 2
- version_date: `2024-05-08T15:00:32.628+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

1

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1c4fd5e2-dbb2-4bad-8992-b30598e0ba72"><ac:parameter ac:name="depth">1</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170459768 space=CDMP2024xR1 version=6 -->
## PAGE 00011: Code engineering set

- page_id: `170459768`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459768/Code+engineering+set
- version_number: 6
- version_date: `2024-05-08T13:56:07.110+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support > Database code engineering
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

224087190

#### CONTENT-COLUMN: Note

224087192

224087189

**On this page**

33

#### CONTENT-BLOCK: Note

224087191

You can create code engineering sets for database scripts in the same manner as CE sets for other code types (see [CONFLUENCE_PAGE title='Code engineering set' space='MD2024x Refresh1 Refresh1 Refresh1'] in MagicDraw User Guide). Right-click the Code engineering Sets, New, DDL, and then the appropriate database flavor. When the CE set is created, you can add database model elements to it, after which DDL script file(s) can be generated OR you can add the script files to the CE set and reverse-engineer them into the database models. In addition to reversing from files, there is Reverse from the DB radio button. Once it is switched, the options for JDBC connection configuring appear, allowing you to set up a connection to the live database.

| Box name | Description |
| --- | --- |
| Recently Used | Contains the list of the recently used reverse templates. Choose the one you need and click Apply. |
| DB Connection URL | The connection URL for the selected profile. |
| Driver Files | Contains .jar and .zip files or directories with JDBC driver’s classes.To choose the files or directories you want to add or remove, click the ... button. The Select Files and/or Directories dialog appears.NoteIf the driver file is empty, the Driver Class is searched from the classpath. |
| Driver Class | Contains the connection driver class.Click the ... button to display the list of available driver classes available in the selected driver files.NoteThe system searches for driver classes only in the files selected in the Driver Files list. |
| Username | Type the username to connect to the database. |
| Password | Type the password to connect to the database. |
| Catalog | Contains the name of the selected Catalog.To retrieve the list of available Catalogs from the database, click the ... button and select the catalog. The catalog name appears in the Catalog textbox.NoteThe list of catalogs can be retrieved only when all other properties in this dialog box are correctly defined. |
| Schema | Contains a name of the selected Schema.To retrieve the list of available Schemas from the database, click the ... button and select the schema. The schema name appears in the Schema textbox.NoteThe list of schemas can be retrieved only when all other properties in this dialog box are correctly defined. |
| Property Name | The name of the JDBC driver property.NoteIf using Oracle drivers, while retrieving db info from Oracle dbTo retrieve comments on table and column, set property as remarks=true.To connect to a db as sysdba, set property as internal_logon=sysdba. |
| Debug JDBC Driver | If selected, all output from a JDBC driver will be directed to Message Window. |
| Reload Driver | The Reload Driver check box is selected by default. If you do not want that driver to be reloaded, clear the check box. |

##### Properties of Code Engineering Set for DDL

Two separate properties sets are stored as the properties of code engineering set for DDL:

- Properties for DDL script generation
- Properties for DDL script reverse engineering

###### [IMAGE alt='' src='']

###### DDL properties in CG Properties Editor dialog.

| Property name | Value list | Description |
| --- | --- | --- |
| Properties for DDL generation |  |  |
| Default attribute multiplicity | 0, 0..1, any entered by user | If the attribute multiplicity is not specified, the value of this property is used. |
| Generate Null constraint | True, false (default) | If true, generates a NULL constraint for the column attribute with [0..1] multiplicity. If the DBMS you use supports NULL, you can enable this to generate NULL constraints.See also: GenerateNotNullConstraint, AttributeDefaultMultiplicity |
| Generate extended index name | True, false (default) | If true, generates an index name of the form: TableName_IndexName. |
| Generate extended trigger name | True, false (default) | If true, generates a trigger name of the form: TableName_TriggerName. |
| Generate index for primary key | True (default), false | If the DBMS you use requires explicit indexes for the primary key, you can enable explicit index creation using this flag.See also: GenerateIndexForUnique |
| Generate index for unique | True (default), false | If the DBMS you use requires explicit indexes for the primary key or unique columns, you can enable explicit index creation using this flag. See also: GenerateIndexForPK |
| Generate not Null constraint | True (default), false | If true, generates a NOT NULL constraint for the column attribute with [1] multiplicity. If you set a GenerateNullConstraint, you may not wish to generate the NOT NULL constraint.See also: GenerateNullConstraint, AttributeDefaultMultiplicity |
| Generate qualified names | True (default), false | If the value of the Generate Qualified Names check box is true, the package name is generated before the table or view name.For example: «Database» package “MQOnline” includes «Table» class “libraries”. If the check box Generate Qualified Names is selected as true in the generated source, it would be written as CREATE TABLE MQOnline.libraries.If the check box Generate Qualified Names is selected as false, in the generated source it would be written as CREATE TABLE libraries. |
| Generate quoted identifiers | True, false (default) | Specifies whether DDL code generator should generate quoted names of identifiers. |
| Object creation mode | The Object Creation Mode combo box has the following options.only CREATE statementsDROP & CREATE statementsCREATE OR REPLACE statements (only for Oracle dialect;default for this dialect)DROP IF EXISTS & CREATE statements (only for MySQL dialect; default for this dialect). |  |
| Properties for DDL script reverse engineering |  |  |
| Column default nullability | Dialect default (default), not specified, NULL, NOT NULL | If column has no NULL or NOT NULL constraint specified, the value of this property is used. |
| Create catalog sets current catalog | True (default), false | Specifies whether create catalog statement changes current catalog name. |
| Create schema sets current schema | True (default), false | Specifies whether create schema statement changes current schema name. |
| Default catalog name | DefaultCatalogNone (default), DefaultCatalogPackage, any entered by the user | Specifies current database name. Used when DDL script does not specify database name explicitly. |
| Default schema name | DefaultSchemaNone (default), DefaultSchemaPackage, any entered by the user | Specifies current schema name. Used when DDL script does not specify schema name explicitly. |
| Drop statements | Deferred (default), Immediate, Ignored | Specifies whether execution of drop statements may be deferred, must be executed, or must be ignored. Deferred drop may be enabled if elements are recreated later. This will save existing views. Attribute stereotypes, multiplicity and default value are not always dropped immediately. |
| Map Null / not Null constraints to | Stereotypes (default), Multiplicity | When parsing DDLs, the null / not null constraints are modeled as either stereotype tag values or multiplicity. |
| Map foreign keys | True (default), false | An association with «FK» stereotype on the association end is created, to represent a Foreign Key. |
| Map indexes | True (default), false | A constraint with «Index» stereotype is added into the table, to represent the index. |
| Map triggers | True (default), false | An opaque behavior with «Trigger» stereotype is added into the table to represent a trigger. |
| Map views | True (default), false | A class with «ViewTable» stereotype is created to represent the view. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a57c8334-4b37-4f86-a4a6-c43e0e8c6947"><ac:parameter ac:name="id">224087190</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d34493c4-a166-4be9-94fa-303036b8841d"><ac:parameter ac:name="id">224087192</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c3e8d0b3-0edb-4e10-9662-08c035d537cc"><ac:parameter ac:name="id">224087189</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="63958346-cb61-474e-93bd-73eeafecb1e8"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="55cc1960-63cb-43d9-8173-6aa4bf5bf334"><ac:parameter ac:name="id">224087191</ac:parameter><ac:rich-text-body><p>You can create code engineering sets for database scripts in the same manner as CE sets for other code types (see <ac:link><ri:page ri:space-key="MD2024x Refresh1 Refresh1 Refresh1" ri:content-title="Code engineering set" /></ac:link> in MagicDraw User Guide). Right-click the Code engineering Sets, New, DDL, and then the appropriate database flavor. When the CE set is created, you can add database model elements to it, after which DDL script file(s) can be generated OR you can add the script files to the CE set and reverse-engineer them into the database models. In addition to reversing from files, there is Reverse from the DB radio button. Once it is switched, the options for JDBC connection configuring appear, allowing you to set up a connection to the live database.</p><table class="relative-table wrapped" style="width: 99.8354%;"><colgroup><col style="width: 17.6397%;" /><col style="width: 82.3603%;" /></colgroup><tbody><tr><th>Box name</th><th>Description</th></tr><tr><td><p><strong>Recently Used<br /></strong></p></td><td>Contains the list of the recently used reverse templates. Choose the one you need and click <strong>Apply</strong>.</td></tr><tr><td><p><strong>DB Connection URL</strong></p></td><td>The connection URL for the selected profile.</td></tr><tr><td><strong>Driver Files </strong></td><td><div class="content-wrapper"><p>Contains .jar and .zip files or directories with JDBC driver’s classes.</p><p>To choose the files or directories you want to add or remove, click the <strong>...</strong> button. The <strong>Select Files and/or Directories </strong>dialog appears.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f9e94ae4-8d58-4ba7-aad2-ca5b93107736"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>If the driver file is empty, the Driver Class is searched from the classpath.</p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td><strong>Driver Class</strong></td><td><div class="content-wrapper"><p>Contains the connection driver class.</p><p>Click the <strong>... </strong>button to display the list of available driver classes available in the selected driver files.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="17976abf-656b-4009-8f87-cc9b9eb97475"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The system searches for driver classes only in the files selected in the <strong>Driver Files </strong>list.</p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td><strong>Username</strong></td><td>Type the username to connect to the database.</td></tr><tr><td><strong>Password</strong></td><td>Type the password to connect to the database.</td></tr><tr><td><strong>Catalog</strong></td><td><div class="content-wrapper"><p>Contains the name of the selected Catalog.</p><p>To retrieve the list of available Catalogs from the database, click the <strong>...</strong> button and select the catalog. The catalog name appears in the <strong>Catalog </strong>textbox.</p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a30ebcfb-a623-4192-9cf2-a8300c15074f"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The list of catalogs can be retrieved only when all other properties in this dialog box are correctly defined.</p></ac:rich-text-body></ac:structured-macro><p><strong class="auto-cursor-target"> </strong></p></div></td></tr><tr><td><strong>Schema</strong></td><td><div class="content-wrapper"><p>Contains a name of the selected Schema.</p><p>To retrieve the list of available Schemas from the database, click the <strong>... </strong>button and select the schema. The schema name appears in the <strong>Schema </strong>textbox.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f1a75a70-07ad-421f-bda7-9f691d49f52f"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The list of schemas can be retrieved only when all other properties in this dialog box are correctly defined.</p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td><p><strong>Property Name</strong></p></td><td><div class="content-wrapper"><p>The name of the JDBC driver property.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4553d7dd-60b7-4822-b61d-d461b43de1b3"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>If using Oracle drivers, while retrieving db info from Oracle db</p><ul><li>To retrieve comments on table and column, set property as remarks=true.</li><li>To connect to a db as sysdba, set property as internal_logon=sysdba.</li></ul></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td><strong>Debug JDBC Driver</strong></td><td><p>If selected, all output from a JDBC driver will be directed to Message Window.</p></td></tr><tr><td><strong>Reload Driver</strong></td><td><p>The Reload Driver check box is selected by default. If you do not want that driver to be reloaded, clear the check box.</p></td></tr></tbody></table><p><br /></p><h3>Properties of Code Engineering Set for DDL</h3><p>Two separate properties sets are stored as the properties of code engineering set for DDL:</p><ul><li>Properties for DDL script generation</li><li>Properties for DDL script reverse engineering</li></ul><h6 style="text-align: center;"><ac:image><ri:attachment ri:filename="Figure 32 DDL Properties in CG Properties Editor Dialog.png" /></ac:image></h6><h6 style="text-align: center;">DDL properties in CG Properties Editor dialog.</h6><table class="relative-table wrapped" style="width: 99.8903%;"><colgroup><col style="width: 25.206%;" /><col style="width: 24.6566%;" /><col style="width: 50.1374%;" /></colgroup><tbody><tr><th>Property name</th><th>Value list</th><th>Description</th></tr><tr><td colspan="3"><strong>Properties for DDL generation</strong></td></tr><tr><td><p><strong>Default attribute multiplicity</strong></p></td><td><p><strong>0, 0..1</strong>, any entered by user</p></td><td><p>If the attribute multiplicity is not specified, the value of this property is used.</p></td></tr><tr><td><p><strong>Generate Null constraint</strong></p></td><td><strong>True</strong>, <strong>false </strong>(default)</td><td><p>If true, generates a NULL constraint for the column attribute with [0..1] multiplicity. If the DBMS you use supports NULL, you can enable this to generate NULL constraints.</p>See also: GenerateNotNullConstraint, AttributeDefaultMultiplicity</td></tr><tr><td><strong>Generate extended index name</strong></td><td><strong>True</strong>, <strong>false </strong>(default)</td><td>If true, generates an index name of the form: TableName_IndexName.</td></tr><tr><td><strong>Generate extended trigger name</strong></td><td><div class="content-wrapper"><p><strong>True</strong>, <strong>false </strong>(default)</p></div></td><td>If true, generates a trigger name of the form: TableName_TriggerName.</td></tr><tr><td><p><strong>Generate index for primary key</strong></p></td><td><strong>True </strong>(default), <strong>false</strong></td><td><p>If the DBMS you use requires explicit indexes for the primary key, you can enable explicit index creation using this flag.</p>See also: GenerateIndexForUnique</td></tr><tr><td><p><strong>Generate index for unique</strong></p></td><td><strong>True </strong>(default), <strong>false</strong></td><td>If the DBMS you use requires explicit indexes for the primary key or unique columns, you can enable explicit index creation using this flag. See also: GenerateIndexForPK</td></tr><tr><td><strong>Generate not Null constraint</strong></td><td><strong>True </strong>(default), <strong>false</strong></td><td><p>If true, generates a NOT NULL constraint for the column attribute with [1] multiplicity. If you set a GenerateNullConstraint, you may not wish to generate the NOT NULL constraint.</p>See also: GenerateNullConstraint, AttributeDefaultMultiplicity</td></tr><tr><td><strong>Generate qualified names</strong></td><td><strong>True </strong>(default), <strong>false</strong></td><td><p>If the value of the Generate Qualified Names check box is true, the package name is generated before the table or view name.</p><p>For example: «Database» package “MQOnline” includes «Table» class “libraries”. If the check box Generate Qualified Names is selected as true in the generated source, it would be written as CREATE TABLE MQOnline.libraries.</p><p>If the check box Generate Qualified Names is selected as false, in the generated source it would be written as CREATE TABLE libraries.</p></td></tr><tr><td><strong>Generate quoted identifiers</strong></td><td><strong>True</strong>, <strong>false </strong>(default)</td><td>Specifies whether DDL code generator should generate quoted names of identifiers.</td></tr><tr><td><strong>Object creation mode</strong></td><td colspan="2"><p>The Object Creation Mode combo box has the following options.</p><ul><li>only CREATE statements</li><li>DROP &amp; CREATE statements</li><li>CREATE OR REPLACE statements (only for Oracle dialect;default for this dialect)</li><li>DROP IF EXISTS &amp; CREATE statements (only for MySQL dialect; default for this dialect).</li></ul></td></tr><tr><td colspan="3"><strong>Properties for DDL script reverse engineering</strong></td></tr><tr><td colspan="1"><strong>Column default nullability</strong></td><td><strong>Dialect default </strong>(default), <strong>not specified</strong>, <strong>NULL</strong>, <strong>NOT NULL</strong></td><td>If column has no NULL or NOT NULL constraint specified, the value of this property is used.</td></tr><tr><td colspan="1"><strong>Create catalog sets current catalog</strong></td><td><strong>True </strong>(default), <strong>false</strong></td><td>Specifies whether create catalog statement changes current catalog name.</td></tr><tr><td colspan="1"><strong>Create schema sets current schema</strong></td><td><strong>True </strong>(default), <strong>false</strong></td><td>Specifies whether create schema statement changes current schema name.</td></tr><tr><td colspan="1"><strong>Default catalog name</strong></td><td><strong>DefaultCatalogNone </strong>(default), <strong>DefaultCatalogPackage</strong>, any entered by the user</td><td>Specifies current database name. Used when DDL script does not specify database name explicitly.</td></tr><tr><td colspan="1"><strong>Default schema name</strong></td><td><strong>DefaultSchemaNone </strong>(default), <strong>DefaultSchemaPackage</strong>, any entered by the user</td><td>Specifies current schema name. Used when DDL script does not specify schema name explicitly.</td></tr><tr><td colspan="1"><strong>Drop statements</strong></td><td><p><strong>Deferred </strong>(default), <strong>Immediate</strong>, <strong>Ignored</strong></p></td><td>Specifies whether execution of drop statements may be deferred, must be executed, or must be ignored. Deferred drop may be enabled if elements are recreated later. This will save existing views. Attribute stereotypes, multiplicity and default value are not always dropped immediately.</td></tr><tr><td colspan="1"><strong>Map Null / not Null constraints to</strong></td><td><p><strong>Stereotypes </strong>(default)<strong>, Multiplicity</strong></p></td><td>When parsing DDLs, the null / not null constraints are modeled as either stereotype tag values or multiplicity.</td></tr><tr><td colspan="1"><strong>Map foreign keys</strong></td><td><strong>True </strong>(default), <strong>false</strong></td><td>An association with «FK» stereotype on the association end is created, to represent a Foreign Key.</td></tr><tr><td colspan="1"><strong>Map indexes</strong></td><td><strong>True </strong>(default), <strong>false</strong></td><td>A constraint with «Index» stereotype is added into the table, to represent the index.</td></tr><tr><td colspan="1"><strong>Map triggers</strong></td><td><strong>True </strong>(default), <strong>false</strong></td><td>An opaque behavior with «Trigger» stereotype is added into the table to represent a trigger.</td></tr><tr><td colspan="1"><strong>Map views</strong></td><td><strong>True </strong>(default), <strong>false</strong></td><td>A class with «ViewTable» stereotype is created to represent the view.</td></tr></tbody></table></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459742 space=CDMP2024xR1 version=1 -->
## PAGE 00012: Common SQL element properties

- page_id: `170459742`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459742/Common+SQL+element+properties
- version_number: 1
- version_date: `2023-09-21T12:46:56.125+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support > Database modeling
- labels: []

### NORMALIZED CONTENT

These properties are common and available for all SQL model elements in their Specification windows.

| Property name | Description |
| --- | --- |
| Name | Name of this SQL model element. |
| Label | Label of SQL model element. Can be used for various referring purposes (both human and code referral). |
| Description | Longer text, describing this SQL element in more detail. |
| TODO | Additional remarks about the further modifications, necessary for this element. |

In addition to these SQL properties, some common, useful UML model properties are shown in the Specification windows (only in the Expert mode).

| Property name | Description |
| --- | --- |
| Qualified Name | Fully qualified name of this model element - names of all owning parent elements and this element, concatenated using “::” separators. |
| Owner | Model element, directly owning this element. |
| Applied Stereotype | Stereotypes, applied on this model element, extending element data over and above the standard UML functionality. SQL extension stereotypes can be seen here (implementing SQL model features, described in this document) as well as any additional extensions. |
| Image | Custom image can be set on each model element if necessary. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>These properties are common and available for all SQL model elements in their Specification windows.</p><p><br /></p><table class="relative-table" style="width: 66.9022%;"><colgroup><col style="width: 11.7846%;" /><col style="width: 88.2155%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td>Name</td><td>Name of this SQL model element.</td></tr><tr><td>Label</td><td>Label of SQL model element. Can be used for various referring purposes (both human and code referral).</td></tr><tr><td>Description</td><td>Longer text, describing this SQL element in more detail.</td></tr><tr><td>TODO</td><td>Additional remarks about the further modifications, necessary for this element.</td></tr></tbody></table><p><br /></p><p>In addition to these SQL properties, some common, useful UML model properties are shown in the Specification windows (only in the Expert mode).</p><p><br /></p><table class="relative-table" style="width: 99.9457%;"><colgroup><col style="width: 8.32245%;" /><col style="width: 91.6775%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td>Qualified Name</td><td>Fully qualified name of this model element - names of all owning parent elements and this element, concatenated using “::” separators.</td></tr><tr><td>Owner</td><td>Model element, directly owning this element.</td></tr><tr><td>Applied Stereotype</td><td><p>Stereotypes, applied on this model element, extending element data over and above the standard UML functionality. SQL extension stereotypes can be seen here (implementing SQL model features, described in this document) as well as any additional extensions.</p></td></tr><tr><td>Image</td><td>Custom image can be set on each model element if necessary.</td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459836 space=CDMP2024xR1 version=5 -->
## PAGE 00013: ComplexType

- page_id: `170459836`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459836/ComplexType
- version_number: 5
- version_date: `2024-05-08T14:21:11.389+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Complex type maps to UML Class with the stereotype XSDcomplexType.

- abstract - to UML Class abstract value(true | false).
- annotation - to UML Class documentation.
- attribute – to inner UML Class Attribute or UML Association End.
- attributeGroup – to UML AssociationEnd or UML Attribute with type XSDattributeGroup.
- name – to UML Class name.

This class also can have the stereotypes XSDsimpleContent, XSDcomplexContent, XSDall, XSDchoice, and XSDsequence.

No stereotype – the same as “XSDsequence”.

A generalization between a complex type and another type has the stereotype XSDrestriction or XSDextension. We assume the stereotype XSDextension if the generalizations do not have stereotypes.

Some complex mapping:

- complexType with simpleContent – to UML Class. This class must be derived from another class and must have stereotype XSDsimpleContent.
- complexType with complexContent – to UML Class. This class must be derived from another class and must have stereotype XSDcomplexContent.

#### PANEL: complexType with group, all, choice or sequence – to UML class with appropriate stereotype

complexType with group, all, choice or sequence – to UML class with appropriate stereotype

```text
<complexType
```

```text
abstract = boolean : false
```

```text
block = (#all | List of (extension | restriction))
```

```text
final = (#all | List of (extension | restriction)) 	id = ID
```

```text
mixed = boolean : false
```

```text
name = NCName
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?,(simpleContent | complexContent | ((group | al ((attribute | attributeGroup)*, anyAttribute?))))
```

```text
</complexType>
```

When you choose the <simpleContent> alternative, the following elements are relevant, and the remaining property mappings are as below. Note that you must either choose <restriction> or <extension> as the content of <simpleContent>.

#### PANEL: <restriction> chosen as the content of <simpleContent>

<restriction> chosen as the content of <simpleContent>

```text
<simpleContent
```

```text
id = ID
```

```text
{any attributes with non-schema namespace…}> Content: (annotation?, (restriction | extension))	</simpleContent>
```

```text
<restriction
```

```text
base = OName
```

```text
id = ID
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, (simpleType?, (minExclusive | minInclusive  | maxExclusive |
```

```text
maxlnclusive | totalDigits | fractionDigits | length | minLength | maxLength
```

```text
whitespace | pattern) *)?, ((attribute | attributeGroup)*, anyAttribute?))
```

```text
</restriction><extension
```

```text
base = OName
```

```text
id = ID
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, ((attribute | attributeGroup)*, anyAttribute?))
```

```text
</extension>
```

```text
<attributeGroup
```

```text
id = ID
```

```text
ref = OName
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</attributeGroup>
```

```text
<anyAttribute
```

When the <complexContent> alternative is chosen, the following elements are relevant (as are the<attributeGroup> and <anyAttribute> elements, not repeated here), and the additional property mappings appear below. Note that you must choose either <restriction> or <extension> as the content of <complexContent>, but their content models differ in this case from the case above when they occur as children of<simpleContent>.

The property mappings below are also used in the case where the third alternative (neither <simpleContent> nor <complexContent>) is chosen. This case is understood as shorthand for complex content restricting the **ur type definition**. The details of the mappings should be modified as necessary.

#### PANEL: Sample of either <restriction> or <extension> must be chosen as the content of <complexContent>

Sample of either <restriction> or <extension> must be chosen as the content of <complexContent>

```text
<complexContent
```

```text
id = ID
```

```text
mixed = boolean
```

```text
{any attributes with non-schema namespace…}>	Content: (annotation?, (restriction | extension))
```

```text
</complexContent>
```

```text
<restriction
```

```text
base = OName
```

```text
id = ID
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, (group | all | choice | sequence)?, ((attribute | attributeGroup)*, anyAttribute?))
```

```text
</restriction>
```

```text
<extension
```

```text
base = OName
```

```text
id = ID
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, ((group | all | choice | sequence)?, ((attribute | attributeGroup)*, anyAttribute?)))
```

```text
</extension>
```

###### [IMAGE alt='' src='']Example of complexType UML model.

#### PANEL: Example of complexType UML model with associated XML

Example of complexType UML model with associated XML

```text
<?xml version=’1.0’ encoding = ‘Cp1252’?›
```

```text
<xs:schema xmlns:nm = "http://nomagic.com" xmlns:xs = "http://www.w3.org/2001/XMLSchema" targetNamespace = "http://nomagic.com" >
```

```text
<xs:complexType name = "my_Type2" block = "extension" final = "extension" mixed = "true" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >my_type2
```

```text
Documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
<xs:complexContent id = "contentID" mixed = "false" >			<xs:extension base = "nm:my_Type">
```

```text
<xs:attribute name = "surname" type = "xs:string" />
```

```text
</xs:extension>
```

```text
</xs:complexContent> 	</xs:complexType>
```

```text
<xs:complexType name = "my_Type3" >
```

```text
<xs:complexContent >
```

```text
<xs:restriction base = "nm:my_Type">
```

```text
<xs:all >
```

```text
<xs:element name = "order" type = "xs:string"/>
```

```text
<xs:element name = "order1" type = "xs:string"/>
```

```text
</xs:all> 			</xs:restriction>
```

```text
</xs:complexContent>	</xs:complexType>
```

```text
<xs:complexType name = "my_Type4">
```

```text
<xs:simpleContent >
```

```text
<xs:restriction base = "xs:string" >
```

```text
<xs:minLength value = "2" />
```

```text
</xs:restriction>
```

```text
</xs:simpleContent> </xs:complexType>
```

```text
<xs:complexType name = "my_Type5">
```

```text
<xs:simpleContent >
```

```text
<xs:extension base = "xs:string">
```

```text
<xs:attribute name = "attri" type = "xs:string"/>
```

```text
</xs:extension>
```

```text
</xs:simpleContent>	</xs:complexType>
```

```text
<xs:complexType name = "my_Type" abstract = "true" block = "extension" final = "extension" id = "myTypeID" mixed = "true" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >my_type documentation</xs:documentation>		</xs:annotation>
```

```text
<xs:attribute name = "name" type = "xs:string" />		<xs:attributeGroup ref = "nm:attr_group" />
```

```text
<xs:anyAttribute/>	</xs:complexType>
```

```text
<xs:attributeGroup name = "attr_group" />
```

```text
</xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Complex type maps to UML Class with the stereotype XSDcomplexType.</p><ul><li>abstract -  to UML Class abstract value(true | false).</li><li>annotation - to UML Class documentation.</li><li>attribute – to inner UML Class Attribute or UML Association End.</li><li>attributeGroup – to UML AssociationEnd or UML Attribute with type XSDattributeGroup.</li><li>name – to UML Class name.</li></ul><p>This class also can have the stereotypes XSDsimpleContent, XSDcomplexContent, XSDall, XSDchoice, and XSDsequence.</p><p>No stereotype – the same as “XSDsequence”.</p><p>A generalization between a complex type and another type has the stereotype XSDrestriction or XSDextension. We assume the stereotype XSDextension if the generalizations do not have stereotypes.</p><p>Some complex mapping:</p><ul><li>complexType with simpleContent – to UML Class. This class must be derived from another class and must have stereotype XSDsimpleContent.</li><li>complexType with complexContent – to UML Class. This class must be derived from another class and must have stereotype XSDcomplexContent.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f92f6153-0e31-448a-bb79-2e4348d3dd17"><ac:parameter ac:name="title">complexType with group, all, choice or sequence – to UML class with appropriate stereotype</ac:parameter><ac:rich-text-body><pre>&lt;complexType</pre><pre>	abstract = boolean : false</pre><pre>	block = (#all | List of (extension | restriction))</pre><pre>	final = (#all | List of (extension | restriction)) <br />	id = ID</pre><pre>	mixed = boolean : false</pre><pre>	name = NCName</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?,(simpleContent | complexContent | ((group | al <br />((attribute | attributeGroup)*, anyAttribute?))))</pre><pre>&lt;/complexType&gt;</pre></ac:rich-text-body></ac:structured-macro><p>When you choose the &lt;simpleContent&gt; alternative, the following elements are relevant, and the remaining property mappings are as below. Note that you must either choose &lt;restriction&gt; or &lt;extension&gt; as the content of &lt;simpleContent&gt;.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="009944e0-e6b7-4f4f-bccc-2516e12bba3c"><ac:parameter ac:name="title">&lt;restriction&gt; chosen as the content of &lt;simpleContent&gt;</ac:parameter><ac:rich-text-body><pre>&lt;simpleContent</pre><pre>	id = ID</pre><pre>	{any attributes with non-schema namespace…}&gt; Content: (annotation?, (restriction | extension))<br />	&lt;/simpleContent&gt;</pre><pre>&lt;restriction</pre><pre>	base = OName</pre><pre>	id = ID</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, (simpleType?, (minExclusive | minInclusive  | maxExclusive |</pre><pre>maxlnclusive | totalDigits | fractionDigits | length | minLength | maxLength</pre><pre>whitespace | pattern) *)?, ((attribute | attributeGroup)*, anyAttribute?))</pre><pre>&lt;/restriction&gt;<br />&lt;extension</pre><pre>	base = OName</pre><pre>	id = ID</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, ((attribute | attributeGroup)*, anyAttribute?))</pre><pre>&lt;/extension&gt;</pre><pre>&lt;attributeGroup</pre><pre>	id = ID</pre><pre>	ref = OName</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/attributeGroup&gt;</pre><pre>&lt;anyAttribute</pre></ac:rich-text-body></ac:structured-macro><p>When the <u>&lt;complexContent&gt;</u> alternative is chosen, the following elements are relevant (as are the<u> &lt;attributeGroup&gt;</u> and <u>&lt;anyAttribute&gt;</u> elements, not repeated here), and the additional property mappings appear below. Note that you must choose either <u>&lt;restriction&gt;</u> or <u>&lt;extension&gt;</u> as the content of <u>&lt;complexContent&gt;,</u> but their content models differ in this case from the case above when they occur as children of<u> &lt;simpleContent&gt;.</u></p><p>The property mappings below are also used in the case where the third alternative (neither <u>&lt;simpleContent&gt;</u> nor <u>&lt;complexContent&gt;)</u> is chosen. This case is understood as shorthand for complex content restricting the <strong>ur type definition</strong>. The details of the mappings should be modified as necessary.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ef0542e8-9728-4810-a738-c090574a1549"><ac:parameter ac:name="title">Sample of either &lt;restriction&gt; or &lt;extension&gt; must be chosen as the content of &lt;complexContent&gt;</ac:parameter><ac:rich-text-body><pre>&lt;complexContent</pre><pre>	id = ID</pre><pre>	mixed = boolean</pre><pre>	{any attributes with non-schema namespace…}&gt;<br />	Content: (annotation?, (restriction | extension))</pre><pre>&lt;/complexContent&gt;</pre><pre>&lt;restriction</pre><pre>	base = OName</pre><pre>	id = ID</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, (group | all | choice | sequence)?, ((attribute | attributeGroup)*, anyAttribute?))</pre><pre>&lt;/restriction&gt;</pre><pre>&lt;extension</pre><pre>	base = OName</pre><pre>	id = ID</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, ((group | all | choice | sequence)?, ((attribute | attributeGroup)*, anyAttribute?)))</pre><pre>&lt;/extension&gt;</pre></ac:rich-text-body></ac:structured-macro><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 58 complexType UML Model Example.png" /></ac:image>Example of complexType UML model.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="1b502a09-1a14-42cb-bc44-e3052fedd33f"><ac:parameter ac:name="title">Example of complexType UML model with associated XML</ac:parameter><ac:rich-text-body><pre>&lt;?xml version=’1.0’ encoding = ‘Cp1252’?›</pre><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; &gt;</pre><pre>	&lt;xs:complexType name = &quot;my_Type2&quot; block = &quot;extension&quot; final = &quot;extension&quot; mixed = &quot;true&quot; &gt;</pre><pre>		&lt;xs:annotation &gt;</pre><pre>			&lt;xs:documentation &gt;my_type2</pre><pre>Documentation&lt;/xs:documentation&gt;</pre><pre>		&lt;/xs:annotation&gt;</pre><pre>		&lt;xs:complexContent id = &quot;contentID&quot; mixed = &quot;false&quot; &gt;<br />			&lt;xs:extension base = &quot;nm:my_Type&quot;&gt;</pre><pre>				&lt;xs:attribute name = &quot;surname&quot; type = &quot;xs:string&quot; /&gt;</pre><pre>			&lt;/xs:extension&gt;</pre><pre>		&lt;/xs:complexContent&gt; <br />	&lt;/xs:complexType&gt;</pre><pre>	&lt;xs:complexType name = &quot;my_Type3&quot; &gt;</pre><pre>		&lt;xs:complexContent &gt;</pre><pre>			&lt;xs:restriction base = &quot;nm:my_Type&quot;&gt;</pre><pre>				&lt;xs:all &gt;</pre><pre>					&lt;xs:element name = &quot;order&quot; type = &quot;xs:string&quot;/&gt;</pre><pre>					&lt;xs:element name = &quot;order1&quot; type = &quot;xs:string&quot;/&gt;</pre><pre>				&lt;/xs:all&gt; <br />			&lt;/xs:restriction&gt;</pre><pre>		&lt;/xs:complexContent&gt;<br />	&lt;/xs:complexType&gt;</pre><pre>	&lt;xs:complexType name = &quot;my_Type4&quot;&gt;</pre><pre>		&lt;xs:simpleContent &gt;</pre><pre>			&lt;xs:restriction base = &quot;xs:string&quot; &gt;</pre><pre>				&lt;xs:minLength value = &quot;2&quot; /&gt;</pre><pre>			&lt;/xs:restriction&gt;</pre><pre>		&lt;/xs:simpleContent&gt; &lt;/xs:complexType&gt;</pre><pre>	&lt;xs:complexType name = &quot;my_Type5&quot;&gt;</pre><pre>		&lt;xs:simpleContent &gt;</pre><pre>			&lt;xs:extension base = &quot;xs:string&quot;&gt;</pre><pre>				&lt;xs:attribute name = &quot;attri&quot; type = &quot;xs:string&quot;/&gt;</pre><pre>			&lt;/xs:extension&gt;</pre><pre>		&lt;/xs:simpleContent&gt;<br />	&lt;/xs:complexType&gt;</pre><pre>	&lt;xs:complexType name = &quot;my_Type&quot; abstract = &quot;true&quot; block = &quot;extension&quot; final = &quot;extension&quot; id = &quot;myTypeID&quot; mixed = &quot;true&quot; &gt;</pre><pre>		&lt;xs:annotation &gt;</pre><pre>			&lt;xs:documentation &gt;my_type documentation&lt;/xs:documentation&gt;<br />		&lt;/xs:annotation&gt;</pre><pre>		&lt;xs:attribute name = &quot;name&quot; type = &quot;xs:string&quot; /&gt;<br />		&lt;xs:attributeGroup ref = &quot;nm:attr_group&quot; /&gt;</pre><pre>		&lt;xs:anyAttribute/&gt;<br />	&lt;/xs:complexType&gt;</pre><pre>	&lt;xs:attributeGroup name = &quot;attr_group&quot; /&gt;</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459921 space=CDMP2024xR1 version=5 -->
## PAGE 00014: Compositors

- page_id: `170459921`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459921/Compositors
- version_number: 5
- version_date: `2024-05-08T14:25:51.027+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Complex type maps to UML Class with the stereotype XSDcomplexType. In order to have a group in a complex type, the same UML Class must also have the XSDall, XSDchoice or XSDsequence stereotype.

A UML model can have a ModelClass with only a single stereotype XSDall, XSDchoice, or XSDsequence. In this case, the class maps to the inner part of another group.

Element order in a sequence group is very important. These elements are ordered according to the values of TaggedValue sequenceOrder.

#### PANEL: compositors XML representation summary

compositors XML representation summary

```text
<all
```

```text
id = ID
```

```text
maxOccurs = 1 : 1
```

```text
minOccurs = (0 | 1) : 1
```

```text
{any attributes with non-schema namespace...}>	Content: (annotation?, element*)</all>
```

```text
<choice
```

```text
id = ID
```

```text
maxOccurs = (nonNegativeInteger | unbounded):1
```

```text
minOccurs = nonNegativeInteger : 1 	{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, (element | group | choice | sequence | any)*)
```

```text
</choice>
```

```text
<sequence
```

```text
id = ID
```

```text
maxOccurs = (nonNegativeInteger | unbounded) : 1
```

```text
minOccurs = nonNegativeInteger : 1
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, (element | group | choice | sequence | any)*)</sequence>
```

#### PANEL: XML representations for the three kinds of model group

XML representations for the three kinds of model group

```text
<xs:all>
```

```text
<xs:element ref="cats"/>	<xs:element ref="dogs"/></xs:all>
```

```text
<xs:sequence> 	<xs:choice>
```

```text
<xs:element ref="left"/>		<xs:element ref="right"/>	</xs:choice>
```

```text
<xs:element ref="landmark"/></xs:sequence>
```

###### [IMAGE alt='' src='']

###### compositors UML model example.

#### PANEL: compositors XML code sample

compositors XML code sample

```text
<?xml version ='1.0' encoding = 'Cp1252'?>
```

```text
<xs:schema xmlns:nm = "http://nomagic.com" xmlns:xs = "http://www.w3.org/2001/XMLSchema" targetNamespace = "http://nomagic.com">
```

```text
<xs:group name = "myGroup" >
```

```text
<xs:annotation>
```

```text
<xs:documentation>my group documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
<xs:sequence minOccurs = "2" maxOccurs = "1">
```

```text
<xs:choice>
```

```text
<xs:element name = "number" type = "xs:string" />			</xs:choice>
```

```text
<xs:group ref = "nm:myGroup3" minOccurs = "0" maxOccurs = "1" >
```

```text
<xs:annotation >
```

```text
<xs:documentation>ref documentation</xs:documentation>
```

```text
</xs:annotation>			</xs:group>
```

```text
<xs:group ref = "nm:myGroup2" minOccurs = "0" maxOccurs = "unbounded" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >another ref documentation</xs:documentation>
```

```text
‹/xs:annotation>			</xs:group>
```

```text
<xs:element name = "name" type = "xs:string" />			<xs:element name = "name2" type = "xs:string" />			<xs:element name = "name1" type = "xs:string" />
```

```text
<xs:any id = "anyID" namespace = "value" minOccurs = "0" maxOccurs = "1" />
```

```text
</xs:sequence>
```

```text
</xs:group>
```

```text
<xs:group name = "myGroup3" >
```

```text
<xs:choice >
```

```text
<xs:element name = "address" type = "xs:string" />		</xs:choice>
```

```text
</xs:group>
```

```text
<xs:group name = "myGroup2" >
```

```text
<xs:all>
```

```text
<xs:element name = "surname" type = "xs:string" />		</xs:all>
```

```text
</xs:group></xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Complex type maps to UML Class with the stereotype XSDcomplexType. In order to have a group in a complex type, the same UML Class must also have the XSDall, XSDchoice or XSDsequence stereotype.</p><p>A UML model can have a ModelClass with only a single stereotype XSDall, XSDchoice, or XSDsequence. In this case, the class maps to the inner part of another group.</p><p style="text-align: left;">Element order in a sequence group is very important. These elements are ordered according to the values of TaggedValue sequenceOrder.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c913a113-286b-47fa-afc3-cd1277d02bcb"><ac:parameter ac:name="title">compositors XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;all</pre><pre>	id = ID</pre><pre>	maxOccurs = 1 : 1</pre><pre>	minOccurs = (0 | 1) : 1</pre><pre>	{any attributes with non-schema namespace...}&gt;<br />	Content: (annotation?, element*)<br />&lt;/all&gt;</pre><pre>&lt;choice</pre><pre>	id = ID</pre><pre>	maxOccurs = (nonNegativeInteger | unbounded):1</pre><pre>	minOccurs = nonNegativeInteger : 1 <br />	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, (element | group | choice | sequence | any)*)</pre><pre>&lt;/choice&gt; </pre><pre>&lt;sequence</pre><pre>	id = ID</pre><pre>	maxOccurs = (nonNegativeInteger | unbounded) : 1 </pre><pre>	minOccurs = nonNegativeInteger : 1</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, (element | group | choice | sequence | any)*)<br />&lt;/sequence&gt; </pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ab0275ed-f556-4428-9b86-679fc17f68a8"><ac:parameter ac:name="title">XML representations for the three kinds of model group</ac:parameter><ac:rich-text-body><pre>&lt;xs:all&gt;</pre><pre>	&lt;xs:element ref=&quot;cats&quot;/&gt;<br />	&lt;xs:element ref=&quot;dogs&quot;/&gt;<br />&lt;/xs:all&gt;</pre><pre><br />&lt;xs:sequence&gt; <br />	&lt;xs:choice&gt;</pre><pre>		&lt;xs:element ref=&quot;left&quot;/&gt;<br />		&lt;xs:element ref=&quot;right&quot;/&gt;<br />	&lt;/xs:choice&gt;</pre><pre>	&lt;xs:element ref=&quot;landmark&quot;/&gt;<br />&lt;/xs:sequence&gt;</pre></ac:rich-text-body></ac:structured-macro><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 116 compositors UML Model Example.png" /></ac:image></h6><h6 style="text-align: center;">compositors UML model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="145c46f8-3625-43d8-948f-509797ebcf12"><ac:parameter ac:name="title">compositors XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;?xml version ='1.0' encoding = 'Cp1252'?&gt;</pre><pre><br />&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.comm">http://nomagic.com&quot;</a> xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; targetNamespace = &quot;<a href="http://nomagic.comm">http://nomagic.com&quot;</a>&gt;</pre><pre>	&lt;xs:group name = &quot;myGroup&quot; &gt;</pre><pre>		&lt;xs:annotation&gt;</pre><pre>			&lt;xs:documentation&gt;my group documentation&lt;/xs:documentation&gt;</pre><pre>		&lt;/xs:annotation&gt;</pre><pre>		&lt;xs:sequence minOccurs = &quot;2&quot; maxOccurs = &quot;1&quot;&gt;</pre><pre>			&lt;xs:choice&gt;</pre><pre>				&lt;xs:element name = &quot;number&quot; type = &quot;xs:string&quot; /&gt;<br />			&lt;/xs:choice&gt;</pre><pre>			&lt;xs:group ref = &quot;nm:myGroup3&quot; minOccurs = &quot;0&quot; maxOccurs = &quot;1&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation&gt;ref documentation&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;<br />			&lt;/xs:group&gt;</pre><pre>			&lt;xs:group ref = &quot;nm:myGroup2&quot; minOccurs = &quot;0&quot; maxOccurs = &quot;unbounded&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;another ref documentation&lt;/xs:documentation&gt;</pre><pre>				‹/xs:annotation&gt;<br />			&lt;/xs:group&gt;</pre><pre>			&lt;xs:element name = &quot;name&quot; type = &quot;xs:string&quot; /&gt;<br />			&lt;xs:element name = &quot;name2&quot; type = &quot;xs:string&quot; /&gt;<br />			&lt;xs:element name = &quot;name1&quot; type = &quot;xs:string&quot; /&gt;</pre><pre>			&lt;xs:any id = &quot;anyID&quot; namespace = &quot;value&quot; minOccurs = &quot;0&quot; maxOccurs = &quot;1&quot; /&gt;</pre><pre>		&lt;/xs:sequence&gt;</pre><pre>	&lt;/xs:group&gt;</pre><pre>	&lt;xs:group name = &quot;myGroup3&quot; &gt;</pre><pre>		&lt;xs:choice &gt;</pre><pre>			&lt;xs:element name = &quot;address&quot; type = &quot;xs:string&quot; /&gt;<br />		&lt;/xs:choice&gt;</pre><pre>	&lt;/xs:group&gt;</pre><pre>	&lt;xs:group name = &quot;myGroup2&quot; &gt;</pre><pre>		&lt;xs:all&gt;</pre><pre>			&lt;xs:element name = &quot;surname&quot; type = &quot;xs:string&quot; /&gt;<br />		&lt;/xs:all&gt;</pre><pre>	&lt;/xs:group&gt;<br />&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459757 space=CDMP2024xR1 version=5 -->
## PAGE 00015: Constraints

- page_id: `170459757`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459757/Constraints
- version_number: 5
- version_date: `2024-05-08T13:52:25.858+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support > Database modeling
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

121806521

#### CONTENT-COLUMN: Note

121806523

121806519

**On this page**

33

#### CONTENT-BLOCK: Note

121806522

Tables have a multitude of constraints between them. These constraints enforce the proper business semantics for the data in the database tables (relationships between data in different tables, semantical constraints of the data in the table). These available constraint types are as follows.

- Primary key constraints - specifying column (or a combination of columns), which uniquely identify the row in the table.
- Unique constraints. They are very similar to primary key constraints - uniquely identify the row in the table. One of the unique constraints of the table is designated as primary.
- Foreign key constraints, which establish relationships between two tables.
- Nullability constraints (NOT NULL constraint) - a simple constraint on the column, indicating that column must have value
- Check constraints establish additional checking conditions on values in the column / table.
- Assertions provide more global check than a check constraint - spanning multiple tables.
- Indexes are not constraints per se, but they are covered in this section because they are modeled similarly.

The primary keys, unique and check constraints, indexes can be modeled in two ways. One way is easy and simple but does not cover all the options provided by SQL. Another way is tedious, but provides full SQL coverage.

##### Implicit primary key, unique, check constraint, and index modeling

#### NOTE: Note

Note

- SQL Primary Key (when implicitly modeled) is modeled as an additional «PrimaryKeyMember» stereotype applied on the SQL column. This variant is shown in the diagram as an additional «pk» keyword on the column in the diagram.
- SQL Unique Constraint (when implicitly modeled) is modeled as an additional «UniqueMember» stereotype applied on the SQL column. This variant is shown in the diagram as an additional «unique» keyword on the column in the diagram.
- SQL Check Constraint (when implicitly modeled) is modeled as an additional «CheckMember» stereotype applied on the SQL column. This variant is shown in the diagram as an additional «chk» keyword on the column in the diagram.
- SQL Index (when implicitly modeled) is modeled as an additional «IndexMember» stereotype applied on the SQL column. This variant is shown in the diagram as an additional «idx» keyword on the column in the diagram.

An easy way of modeling this kind of constraint is applying the «PrimaryKeyMember», «UniqueMember», «CheckMember», or «IndexMember» stereotype on the necessary column. PK, unique, and index markers can be applied on the column via its shortcut menu as shown in the following figure.

[IMAGE alt='' src='']

###### Quick application of PK, Unique, and Index markers.

To apply a check constraint marker on a column

1. Open the Specification window of the column.
2. Define the Condition property value in the In Check Constraint property group.

Thusly marked column is considered as a member of one-column constraint, specified in-line. It is by default an unnamed constraint. To specify its name, you need to define the **Primary Key Name**, the **Unique Key Names**, the **Check Name**, or the **Index Names**property value in the column Specification window.

In the SQL script (in CREATE TABLE, ADD COLUMN statements) this would correspond to the following part of the column specification.

```text
[  ] ...
[ [] ... ]
 ::=
| UNIQUE| PRIMARY KEY
| CHECK '('')']]>
```

If primary key, unique constraint or index must span several columns (in this case constraint is not in-line, near the column definition, but as a separate definition at the bottom of the table definition), all the columns must be marked with the appropriate «UniqueMember» / «IndexMember» stereotype and all must have the same name. Column can participate in several unique. Various cases of quick constraint modeling are depicted in the following figure.

[IMAGE alt='' src='']

###### Various situations, modeled with quick constraint notation.

##### Explicit primary key, unique, check constraint, and index modeling

#### NOTE: Note

Note

- SQL Unique Constraint (when explicitly modeled) is modeled as UML Constraint with «UniqueConstraint» stereotype applied.
- SQL Check Constraint (when explicitly modeled) is modeled as UML Constraint with «CheckConstraint» stereotype applied.
- SQL Index (when explicitly modeled) is modeled as UML Constraint with «Index» stereotype applied.

The quick, implicit way to model constraints does not cover some cases, allowed by SQL. Constraints in SQL can be marked as DEFERABLE, INITIALY DEFERRED; constraint in the database can be in active state (enforced) or disabled. Indexes have various configuration parameters.

Modeling with the help of «XYZMember» stereotypes does not allow to specify this additional information. In this case modeling with explicit constraint model elements is necessary. This can be done from the Specification window of table. There are separate tabs for creating these constraint elements: **Unique Constrains**(allows creating both primary keys and unique constraints), **Check Constraints**, **Indices**. Once created, additional properties of the constraints can be specified.

Besides the standard SQL element properties, primary key and unique constraint have following properties

| Property name | Description |
| --- | --- |
| Members | Columns, constrained by this constraint (must come from the same table where constraint is located.) |
| Inline | Whether constraint is defined near the column definition, or separately, at the bottom of the bale definition. Only one-column constraints can be inline. |
| Deferable | Marks the constraint as deferrable. |
| Initially Deferred | Marks the constraint as initially deferred. |
| Enforced | Whether constraint is actively checked in the database (can be changed with the SQL statements). |

Check constraints have the same properties as primary key and unique constraints, and additionally have following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Condition | Condition to be checked |

Besides the standard SQL element properties, index has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Members | Member columns of this index |
| Member Increment Type | For each member column, ASC or DESC ordering direction |
| Unique | Index is used to enforce uniqueness |
| System Generated | Index is system-generated. |
| Clustered | The index is clustered. Only one index per table can be clustered. Non- clustered indexes are stored separately and do not affect layout of the data in the table. Clustered index governs the table data layout (table data pages are leafs of the index tree). |
| Fill Factor | Hash table fill factor of the index |
| Included Members | Additional member columns of the index. No sorting is done by these columns, however their data is included into index - this provides fast retrieval. This feature is very database-specific (AFAIK only MS SQL Server has those). |
| Included Member Increment Type |  |

##### Foreign keys

#### NOTE: Note

Note

- SQL Foreign Key (when modeled with UML Association relationship) is modeled as UML Association with the «FK» stereotype applied on the end of the association (UML Property), which points to the referenced table
- SQL Foreign Key (when modeled with UML Constraint) is modeled as UML Constraint with «ForeignKey» stereotype applied.

[IMAGE alt='' src='']

###### Foreign key example.

Foreign keys describe relationships between two tables. At the detailed understanding level, foreign key is a constraint on the (group of) columns in the source / referencing table, such that for each row in the source table their value combination (tuple) is equal to the value combination (tuple) of the (group of) columns for some row in the target / referenced table.

Foreign keys also have the two ways to be modeled. The main way is described below.

The main way to model foreign keys is to draw association relationship from the referencing table to the referenced table. The relationship can be simply draw in the diagram from the smart manipulator or from the button in the diagram toolbar.

When the FK association is drawn, the following dialog pops up.

###### [IMAGE alt='' src='']Foreign key dialog.

Note that you have to have the necessary columns in the tables (PK or unique columns in target table, referencing FK columns in the source table) before drawing the FK relationship. In this dialog, select the referenced columns (of the target table) in the first column of the table, and corresponding referencing columns (of the source table). Additionally, foreign key name can be specified.

When dialog is OK’d, foreign key association is created; «FK» stereotype is applied on the referencing association end and the selected column information is stored in tags.

If foreign key information has to be changes, this is done in the Specification window of the FK property. Besides the standard SQL element properties foreign key has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Inline | The same functionality as for the explicitly modeled PK, unique constraints. |
| Deferable |  |
| Initially Deferred |  |
| Enabled |  |
| Match | Specifies how the columns in the referenced table and columns in the referencing table are matched (SIMPLE, FULL, PARTIAL match). |
| On Delete | Referential integrity enforcement action that is performed when the data in the referenced table is deleted (NO ACTION, RESTRICT, CASCADE, SET NULL, SET DEFAULT). |
| On Update | Referential integrity enforcement action that is performed when the data in the referenced table is updated (NO ACTION, RESTRICT, CASCADE, SET NULL, SET DEFAULT). |
| Referencing Members | Member columns of the constraint (from the same table where constraint is located). FK constrains values of these columns to point to the data in the referenced tables. |
| Referenced Members | The set of the columns in the referenced (target) table, to which referencing columns are matched. There are 6 ways to specify this set - choose one.Referenced Members field explicitly lists the target columns.Referenced Unique Constraint / Index points to the constraint or index in the target table, and referenced member columns are members of this constraint / index.(by Name) option is used when constraint / index is no explicitly modeled with model element but is just a marking on the column.Referenced Table always points to the target table of the FK (field is not editable, to change it, reconnect the association). If the referenced members column list is not specified in any other way, then referenced columns are taken from the PK of the referenced table. |
| Referenced Table |  |
| Referenced Unique Constraint |  |
| Referenced (by Name) Unique Constraint |  |
| Referenced Unique Index |  |
| Referenced (by Name) Unique Index |  |

The alternative way of modeling a foreign key is creating a UML constraint with the «ForeignKey» stereotype applied. This way is less desired than the main way, because it does not visualize relationship between tables. It is just a constraint in the table. This method may be used when human-readability is not critical, e.g., when database layout is generated with some custom automated script / transformation in the model.

To create a constraint with the «ForeignKey» stereotype

1. Select a table in the Containment tree.
2. Do one of the following.

- Right-click the selected element and from its shortcut menu select New Element > Explicit Foreign Key .
- Open the Explicit Foreign Keys tab in the table’s Specification window.

Besides the standard SQL element properties and properties that are available for other explicit constraints (that is, PK, unique, check constraints), explicit foreign key has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Match | Specifies how the columns in the referenced table and columns in the referencing table are matched (SIMPLE, FULL, PARTIAL match). |
| On Delete | Referential integrity enforcement action that is performed when the data in the referenced table is deleted (NO ACTION, RESTRICT, CASCADE, SET NULL, SET DEFAULT). |
| On Update | Referential integrity enforcement action that is performed when the data in the referenced table is updated (NO ACTION, RESTRICT, CASCADE, SET NULL, SET DEFAULT). |
| Referencing Members | Member columns of the constraint (from the same table where constraint is located). FK constrains values of these columns to point to the data in the referenced tables. |
| Referenced Members | The set of the columns in the referenced (target) table, to which referencing columns are matched. There are 6 ways to specify this set - choose one.Referenced Members field explicitly lists the target columns.Referenced Table field just specifies the target table, referenced columns are then taken from the PK of the table.Referenced Unique Constraint / Index points to the constraint or index in the target table, and referenced member columns are members of this constraint / index.(by Name) option is used when constraint / index is no explicitly modeled with model element but is just a marking on the column. |
| Referenced Table |  |
| Referenced Unique Constraint |  |
| Referenced (by Name) Unique Constraint |  |
| Referenced Unique Index |  |
| Referenced (by Name) Unique Index |  |

##### Nullability constraint

#### NOTE: Note

Note

SQL NOT NULL constraint (if modeled explicitly, which is rare) is modeled as UML Constraint with «NotNullConstraint» stereotype applied.

Nullability, or NOT NULL constraint forces the condition that the column must have value. Implicit NOT NULL constraint is modeled with the **nullable**field of the column (set nullable=false to specify NOT NULL). This is a usual and quick way to model these constraints.

Usually, there is no need to model these constraints explicitly - create a separate model element for them. But in the more complex cases these constraints can be created by hand and the «NotNullConstraint» stereotype applied on them. This allows specifying non-inline constraints, or named constraints, or deferred constraints or inactive constraints.

NOT NULL constraint does not have any additional properties in the Specification window besides the properties that all table constraints have.

##### Assertion

#### NOTE: Note

Note

SQL Assertion is modeled as UML Constraint with «Assertion» stereotype applied.

Assertion constraints are very similar to check constraints, but instead of being local to the table, they are global to the database. Assertions check some condition that must hold through several tables. Assertions are modeler as explicit constraints; there is no shorthand modeling form - assertion is always an explicit UML constraint.

To create an assertion

1. Select a schema or a database element in the Containment tree.
2. Right-click the selected element and from its shortcut menu select New Element > Assertion .

Besides the standard SQL element properties assertion has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Search Condition | The assertion body condition |
| Constrained Tables | List of the tables on which assertion runs |

##### Triggers

#### NOTE: Note

Note

SQL Trigger is modeled as UMLOpaqueBehavior with the «Trigger» stereotype applied.

Trigger describes some action that must be performed when some particular data manipulation action is being performed in the database table. Trigger can be fired when data is added, deleted or changed in the table and perform some action (update some other table, calculate additional values, validate data being updated or even change the data that is being updated).

Trigger is always defined for some table. You can define triggers in the **Triggers**tab of the table Specification window. Trigger has an event type (on what actions trigger is fired, that is, on insert, on update, or on delete), action time (before, after, instead of), and an actual body describing the actions.

Besides the standard SQL element properties, trigger has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Action Time | Specifies moment of time when trigger action is performed (before the specified event, after event, insteadof event). |
| On Insert | The event that causes trigger firing. |
| On Update |  |
| On Delete |  |
| Trigger Column | List of columns, which causes trigger fire on update (must be from the same table as trigger is located). Used with On Update triggers to specify that only some column updates cause trigger fire. |
| Language | Trigger implementation language (should be SQL). |
| Body | Trigger body text (operations that are performed on trigger fire). |
| Time Stamp | Trigger creation timestamp. |
| Action Granularity | Specifies whether trigger fires once per executed statement, or once per each affected row. |
| When | Specifies additional precondition for trigger firing. |
| New Row | These fields can be used for defining variable names for holding new row / table values and old row / table values - for referencing in trigger body.REFERENCING ((NEW\|OLD) (TABLE\|ROW) AS <name>)+ |
| New Table |  |
| Old Row |  |
| Old Table |  |
| Additional Actions | Additional action statements. This option is rarely used - it is non-standard and supported only by some databases. Usually, triggers have just one body. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="6ec9c7c6-7ed9-4bfc-8d8f-2c077aac4fdc"><ac:parameter ac:name="id">121806521</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="9a0f7d85-17a3-4467-b738-5e6a7e257fe3"><ac:parameter ac:name="id">121806523</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7f84f733-54e7-4459-b012-183bc7a5d9cf"><ac:parameter ac:name="id">121806519</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="40dcbcc3-517a-4628-bf35-6d5f48f4e4c7"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4c3fb463-ecb6-4588-94aa-dc490b0e1173"><ac:parameter ac:name="id">121806522</ac:parameter><ac:rich-text-body><p>Tables have a multitude of constraints between them. These constraints enforce the proper business semantics for the data in the database tables (relationships between data in different tables, semantical constraints of the data in the table). These available constraint types are as follows.</p><ul><li>Primary key constraints - specifying column (or a combination of columns), which uniquely identify the row in the table.</li><li>Unique constraints. They are very similar to primary key constraints - uniquely identify the row in the table. One of the unique constraints of the table is designated as primary.</li><li>Foreign key constraints, which establish relationships between two tables.</li><li>Nullability constraints (NOT NULL constraint) - a simple constraint on the column, indicating that column must have value</li><li>Check constraints establish additional checking conditions on values in the column / table.</li><li>Assertions provide more global check than a check constraint - spanning multiple tables.</li><li>Indexes are not constraints per se, but they are covered in this section because they are modeled similarly.</li></ul><p>The primary keys, unique and check constraints, indexes can be modeled in two ways. One way is easy and simple but does not cover all the options provided by SQL. Another way is tedious, but provides full SQL coverage.</p><h3>Implicit primary key, unique, check constraint, and index modeling</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="81510b26-33a4-4503-bb35-de0a54111d87"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>SQL Primary Key (when implicitly modeled) is modeled as an additional «PrimaryKeyMember» stereotype applied on the SQL column. This variant is shown in the diagram as an additional «pk» keyword on the column in the diagram.</li><li>SQL Unique Constraint (when implicitly modeled) is modeled as an additional «UniqueMember» stereotype applied on the SQL column. This variant is shown in the diagram as an additional «unique» keyword on the column in the diagram.</li><li>SQL Check Constraint (when implicitly modeled) is modeled as an additional «CheckMember» stereotype applied on the SQL column. This variant is shown in the diagram as an additional «chk» keyword on the column in the diagram.</li><li>SQL Index (when implicitly modeled) is modeled as an additional «IndexMember» stereotype applied on the SQL column. This variant is shown in the diagram as an additional «idx» keyword on the column in the diagram.</li></ul></ac:rich-text-body></ac:structured-macro><p>An easy way of modeling this kind of constraint is applying the «PrimaryKeyMember», «UniqueMember», «CheckMember», or «IndexMember» stereotype on the necessary column. PK, unique, and index markers can be applied on the column via its shortcut menu as shown in the following figure.</p><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 26 Quick Application of PK, Unique, and Index Markers.png" /></ac:image></p><h6 style="text-align: center;">Quick application of PK, Unique, and Index markers.</h6><p>To apply a check constraint marker on a column</p><hr /><ol><li>Open the Specification window of the column.</li><li>Define the Condition property value in the In Check Constraint property group.</li></ol><p>Thusly marked column is considered as a member of one-column constraint, specified in-line. It is by default an unnamed constraint. To specify its name, you need to define the <strong>Primary Key Name</strong>, the <strong>Unique Key Names</strong>, the <strong>Check Name</strong>, or the <strong>Index Names </strong>property value in the column Specification window.</p><p>In the SQL script (in CREATE TABLE, ADD COLUMN statements) this would correspond to the following part of the column specification.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="da21a7ac-1f73-4ca6-ab62-7d87f1e36058"><ac:plain-text-body><![CDATA[<column name> [ <data type> ] ...
[ [<constraint name>] <constraint>... ]
<constraint> ::=
| UNIQUE| PRIMARY KEY
| CHECK '('<condition>')']]></ac:plain-text-body></ac:structured-macro><p>If primary key, unique constraint or index must span several columns (in this case constraint is not in-line, near the column definition, but as a separate definition at the bottom of the table definition), all the columns must be marked with the appropriate «UniqueMember» / «IndexMember» stereotype and all must have the same name. Column can participate in several unique. Various cases of quick constraint modeling are depicted in the following figure.</p><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 27 Various Situations, Modeled with Quick Constraint Notation.png" /></ac:image></p><h6 style="text-align: center;">Various situations, modeled with quick constraint notation.</h6><h3>Explicit primary key, unique, check constraint, and index modeling</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f4c5387c-1150-4539-97ff-b5dd271d2dc2"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>SQL Unique Constraint (when explicitly modeled) is modeled as UML Constraint with «UniqueConstraint» stereotype applied.</li><li>SQL Check Constraint (when explicitly modeled) is modeled as UML Constraint with «CheckConstraint» stereotype applied.</li><li>SQL Index (when explicitly modeled) is modeled as UML Constraint with «Index» stereotype applied.</li></ul></ac:rich-text-body></ac:structured-macro><p>The quick, implicit way to model constraints does not cover some cases, allowed by SQL. Constraints in SQL can be marked as DEFERABLE, INITIALY DEFERRED; constraint in the database can be in active state (enforced) or disabled. Indexes have various configuration parameters.</p><p>Modeling with the help of «XYZMember» stereotypes does not allow to specify this additional information. In this case modeling with explicit constraint model elements is necessary. This can be done from the Specification window of table. There are separate tabs for creating these constraint elements: <strong>Unique Constrains </strong>(allows creating both primary keys and unique constraints), <strong>Check Constraints</strong>, <strong>Indices</strong>. Once created, additional properties of the constraints can be specified.</p><p>Besides the standard SQL element properties, primary key and unique constraint have following properties</p><table class="relative-table wrapped" style="width: 99.5063%;"><colgroup><col style="width: 18.4694%;" /><col style="width: 81.5306%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Members</strong></td><td>Columns, constrained by this constraint (must come from the same table where constraint is located.)</td></tr><tr><td><strong>Inline</strong></td><td>Whether constraint is defined near the column definition, or separately, at the bottom of the bale definition. Only one-column constraints can be inline.</td></tr><tr><td><strong>Deferable</strong></td><td><p>Marks the constraint as deferrable.</p></td></tr><tr><td><strong>Initially Deferred</strong></td><td>Marks the constraint as initially deferred.</td></tr><tr><td><strong>Enforced</strong></td><td>Whether constraint is actively checked in the database (can be changed with the SQL statements).</td></tr></tbody></table><p>Check constraints have the same properties as primary key and unique constraints, and additionally have following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.0126%;"><colgroup><col style="width: 18.5615%;" /><col style="width: 81.4385%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Condition</strong></td><td>Condition to be checked</td></tr></tbody></table><p>Besides the standard SQL element properties, index has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.5063%;"><colgroup><col style="width: 18.4685%;" /><col style="width: 81.5315%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Members</strong></td><td>Member columns of this index</td></tr><tr><td><p><strong>Member</strong> <strong>Increment Type<br /></strong></p></td><td>For each member column, ASC or DESC ordering direction</td></tr><tr><td><strong>Unique</strong></td><td>Index is used to enforce uniqueness</td></tr><tr><td><strong>System Generated</strong></td><td>Index is system-generated.</td></tr><tr><td><strong>Clustered</strong></td><td>The index is clustered. Only one index per table can be clustered. Non- clustered indexes are stored separately and do not affect layout of the data in the table. Clustered index governs the table data layout (table data pages are leafs of the index tree).</td></tr><tr><td><strong>Fill Factor</strong></td><td>Hash table fill factor of the index</td></tr><tr><td><strong>Included Members</strong></td><td rowspan="2">Additional member columns of the index. No sorting is done by these columns, however their data is included into index - this provides fast retrieval. This feature is very database-specific (AFAIK only MS SQL Server has those).</td></tr><tr><td><strong>Included Member Increment Type</strong></td></tr></tbody></table><h3>Foreign keys</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b3617f09-dcce-4821-8c7b-359bfc9da702"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>SQL Foreign Key (when modeled with UML Association relationship) is modeled as UML Association with the «FK» stereotype applied on the end of the association (UML Property), which points to the referenced table</li><li>SQL Foreign Key (when modeled with UML Constraint) is modeled as UML Constraint with «ForeignKey» stereotype applied.</li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 28 Foreign Key Example.png" /></ac:image></p><h6 style="text-align: center;">Foreign key example.</h6><p>Foreign keys describe relationships between two tables. At the detailed understanding level, foreign key is a constraint on the (group of) columns in the source / referencing table, such that for each row in the source table their value combination (tuple) is equal to the value combination (tuple) of the (group of) columns for some row in the target / referenced table.</p><p>Foreign keys also have the two ways to be modeled. The main way is described below.</p><p>The main way to model foreign keys is to draw association relationship from the referencing table to the referenced table. The relationship can be simply draw in the diagram from the smart manipulator or from the button in the diagram toolbar.</p><p>When the FK association is drawn, the following dialog pops up.</p><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 29 Foreign Key Dialog.png" /></ac:image>Foreign key dialog.</h6><p>Note that you have to have the necessary columns in the tables (PK or unique columns in target table, referencing FK columns in the source table) before drawing the FK relationship. In this dialog, select the referenced columns (of the target table) in the first column of the table, and corresponding referencing columns (of the source table). Additionally, foreign key name can be specified.</p><p>When dialog is OK’d, foreign key association is created; «FK» stereotype is applied on the referencing association end and the selected column information is stored in tags.</p><p>If foreign key information has to be changes, this is done in the Specification window of the FK property. Besides the standard SQL element properties foreign key has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.8903%;"><colgroup><col style="width: 18.7262%;" /><col style="width: 81.2738%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><p><strong>Inline                     </strong></p></td><td rowspan="4">The same functionality as for the explicitly modeled PK, unique constraints.<br /><br /><br /></td></tr><tr><td><strong>Deferable</strong></td></tr><tr><td><strong>Initially Deferred</strong></td></tr><tr><td><strong>Enabled</strong></td></tr><tr><td><strong>Match</strong></td><td>Specifies how the columns in the referenced table and columns in the referencing table are matched (SIMPLE, FULL, PARTIAL match).</td></tr><tr><td><strong>On Delete</strong></td><td>Referential integrity enforcement action that is performed when the data in the referenced table is deleted (NO ACTION, RESTRICT, CASCADE, SET NULL, SET DEFAULT).</td></tr><tr><td><strong>On Update</strong></td><td>Referential integrity enforcement action that is performed when the data in the referenced table is updated (NO ACTION, RESTRICT, CASCADE, SET NULL, SET DEFAULT).</td></tr><tr><td><strong>Referencing Members</strong></td><td>Member columns of the constraint (from the same table where constraint is located). FK constrains values of these columns to point to the data in the referenced tables.</td></tr><tr><td><strong>Referenced Members</strong></td><td rowspan="6"><p>The set of the columns in the referenced (target) table, to which referencing columns are matched. There are 6 ways to specify this set - choose one.</p><p>Referenced Members field explicitly lists the target columns.</p><p>Referenced Unique Constraint / Index points to the constraint or index in the target table, and referenced member columns are members of this constraint / index.</p><p>(by Name) option is used when constraint / index is no explicitly modeled with model element but is just a marking on the column.</p><p>Referenced Table always points to the target table of the FK (field is not editable, to change it, reconnect the association). If the referenced members column list is not specified in any other way, then referenced columns are taken from the PK of the referenced table.</p></td></tr><tr><td><strong>Referenced Table</strong></td></tr><tr><td><strong>Referenced Unique Constraint</strong></td></tr><tr><td><strong>Referenced (by Name) Unique Constraint</strong></td></tr><tr><td><strong>Referenced Unique Index</strong></td></tr><tr><td><strong>Referenced (by Name) Unique Index</strong></td></tr></tbody></table><p>The alternative way of modeling a foreign key is creating a UML constraint with the «ForeignKey» stereotype applied. This way is less desired than the main way, because it does not visualize relationship between tables. It is just a constraint in the table. This method may be used when human-readability is not critical, e.g., when database layout is generated with some custom automated script / transformation in the model.</p><p>To create a constraint with the «ForeignKey» stereotype</p><hr /><ol><li>Select a table in the Containment tree.</li><li>Do one of the following.</li></ol><ul><li>Right-click the selected element and from its shortcut menu select <strong>New Element </strong>&gt;<strong> Explicit Foreign Key</strong>.</li><li>Open the <strong>Explicit Foreign Keys </strong>tab in the table’s Specification window.</li></ul><p>Besides the standard SQL element properties and properties that are available for other explicit constraints (that is, PK, unique, check constraints), explicit foreign key has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 19.0362%;" /><col style="width: 80.9638%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Match</strong></td><td>Specifies how the columns in the referenced table and columns in the referencing table are matched (SIMPLE, FULL, PARTIAL match).</td></tr><tr><td><strong>On Delete</strong></td><td>Referential integrity enforcement action that is performed when the data in the referenced table is deleted (NO ACTION, RESTRICT, CASCADE, SET NULL, SET DEFAULT).</td></tr><tr><td><strong>On Update</strong></td><td>Referential integrity enforcement action that is performed when the data in the referenced table is updated (NO ACTION, RESTRICT, CASCADE, SET NULL, SET DEFAULT).</td></tr><tr><td><strong>Referencing Members</strong></td><td>Member columns of the constraint (from the same table where constraint is located). FK constrains values of these columns to point to the data in the referenced tables.</td></tr><tr><td><strong>Referenced Members</strong></td><td rowspan="6"><p>The set of the columns in the referenced (target) table, to which referencing columns are matched. There are 6 ways to specify this set - choose one.</p><p>Referenced Members field explicitly lists the target columns.</p><p>Referenced Table field just specifies the target table, referenced columns are then taken from the PK of the table.</p><p>Referenced Unique Constraint / Index points to the constraint or index in the target table, and referenced member columns are members of this constraint / index.</p><p>(by Name) option is used when constraint / index is no explicitly modeled with model element but is just a marking on the column.</p></td></tr><tr><td><strong>Referenced Table</strong></td></tr><tr><td><strong>Referenced Unique Constraint</strong></td></tr><tr><td><strong>Referenced (by Name) Unique Constraint</strong></td></tr><tr><td><strong>Referenced Unique Index</strong></td></tr><tr><td><strong>Referenced (by Name) Unique Index</strong></td></tr></tbody></table><p><br /></p><h3>Nullability constraint</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c1b61f47-b54e-4ba8-be76-aa665e7e4ca4"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL NOT NULL constraint (if modeled explicitly, which is rare) is modeled as UML Constraint with «NotNullConstraint» stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>Nullability, or NOT NULL constraint forces the condition that the column must have value. Implicit NOT NULL constraint is modeled with the <strong>nullable </strong>field of the column (set nullable=false to specify NOT NULL). This is a usual and quick way to model these constraints.</p><p>Usually, there is no need to model these constraints explicitly - create a separate model element for them. But in the more complex cases these constraints can be created by hand and the «NotNullConstraint» stereotype applied on them. This allows specifying non-inline constraints, or named constraints, or deferred constraints or inactive constraints.</p><p>NOT NULL constraint does not have any additional properties in the Specification window besides the properties that all table constraints have.</p><h3>Assertion</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2275a2d1-3092-400c-ae06-0906c5a10c77"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Assertion is modeled as UML Constraint with «Assertion» stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>Assertion constraints are very similar to check constraints, but instead of being local to the table, they are global to the database. Assertions check some condition that must hold through several tables. Assertions are modeler as explicit constraints; there is no shorthand modeling form - assertion is always an explicit UML constraint.</p><p>To create an assertion</p><hr /><ol><li>Select a schema or a database element in the Containment tree.</li><li>Right-click the selected element and from its shortcut menu select <strong>New Element </strong>&gt; <strong>Assertion</strong>.</li></ol><p>Besides the standard SQL element properties assertion has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.4515%;"><colgroup><col style="width: 19.5263%;" /><col style="width: 80.4737%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Search Condition</strong></td><td>The assertion body condition</td></tr><tr><td><strong>Constrained Tables</strong></td><td>List of the tables on which assertion runs</td></tr></tbody></table><p><br /></p><h3>Triggers</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="baea96e8-bb87-4246-9b3f-755d99a18262"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Trigger is modeled as UMLOpaqueBehavior with the «Trigger» stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>Trigger describes some action that must be performed when some particular data manipulation action is being performed in the database table. Trigger can be fired when data is added, deleted or changed in the table and perform some action (update some other table, calculate additional values, validate data being updated or even change the data that is being updated).</p><p>Trigger is always defined for some table. You can define triggers in the <strong>Triggers </strong>tab of the table Specification window. Trigger has an event type (on what actions trigger is fired, that is, on insert, on update, or on delete), action time (before, after, instead of), and an actual body describing the actions.</p><p>Besides the standard SQL element properties, trigger has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 19.708%;" /><col style="width: 80.292%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Action Time</strong></td><td>Specifies moment of time when trigger action is performed (before the specified event, after event, insteadof event).</td></tr><tr><td><strong>On Insert</strong></td><td rowspan="3">The event that causes trigger firing.</td></tr><tr><td><strong>On Update</strong></td></tr><tr><td><strong>On Delete</strong></td></tr><tr><td><strong>Trigger Column</strong></td><td>List of columns, which causes trigger fire on update (must be from the same table as trigger is located). Used with On Update triggers to specify that only some column updates cause trigger fire.</td></tr><tr><td><strong>Language</strong></td><td>Trigger implementation language (should be SQL).</td></tr><tr><td><strong>Body</strong></td><td>Trigger body text (operations that are performed on trigger fire).</td></tr><tr><td><strong>Time Stamp</strong></td><td>Trigger creation timestamp.</td></tr><tr><td><strong>Action Granularity</strong></td><td>Specifies whether trigger fires once per executed statement, or once per each affected row.</td></tr><tr><td><strong>When</strong></td><td>Specifies additional precondition for trigger firing.</td></tr><tr><td><strong>New Row</strong></td><td rowspan="4"><p>These fields can be used for defining variable names for holding new row / table values and old row / table values - for referencing in trigger body.</p><p>REFERENCING ((NEW|OLD) (TABLE|ROW) AS &lt;name&gt;)+</p></td></tr><tr><td><strong>New Table</strong></td></tr><tr><td><strong>Old Row</strong></td></tr><tr><td><strong>Old Table</strong></td></tr><tr><td><strong>Additional Actions</strong></td><td>Additional action statements. This option is rarely used - it is non-standard and supported only by some databases. Usually, triggers have just one body.</td></tr></tbody></table></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459721 space=CDMP2024xR1 version=1 -->
## PAGE 00016: Constraints between relationships

- page_id: `170459721`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459721/Constraints+between+relationships
- version_number: 1
- version_date: `2023-09-21T12:46:55.550+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Entity-relationship (ER) modeling and diagrams
- labels: []

### NORMALIZED CONTENT

You can place XOR constraints (there is also a rarely used OR constraint) between relationships using the corresponding toolbar button. Note that constraints must join relationships having at least one common end, never arbitrary relationships.

Current implementation of constraints does not allow placing a constraint on more than 2 relationships.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can place XOR constraints (there is also a rarely used OR constraint) between relationships using the corresponding toolbar button. Note that constraints must join relationships having at least one common end, never arbitrary relationships.</p><p>Current implementation of constraints does not allow placing a constraint on more than 2 relationships.</p>
````

<!--NOMAGIC_PAGE id=170459767 space=CDMP2024xR1 version=1 -->
## PAGE 00017: Database code engineering

- page_id: `170459767`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459767/Database+code+engineering
- version_number: 1
- version_date: `2023-09-21T12:46:57.083+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support
- labels: []

### NORMALIZED CONTENT

Cameo Data Modeler provides code engineering capabilities, database script generation, and reverse engineering. A database model can be generated in the DDL script, which can then be run on the database engine to create database structures. Conversely, the database engine can export database structures into the DDL script, which can then be reverse-engineered into the database model. In addition, Cameo Data Modeler enables reverse engineering directly from a live database through the **JDBC**connection.

Cameo Data Modeler code engineering supports the following database dialects for script generation and reversing:

- Standard SQL
- Oracle
- MS SQL Server
- DB2
- MySQL
- PostgreSQL
- Sybase
- Pervasive
- Cloudscape / Derby
- MS Access
- Pointbase

As mentioned earlier, database modeling was significantly extended in version v17.0.1. However, database code engineering stayed at the same level as before. Currently, not all database concepts that can be modeled can be subsequently generated or reverse engineered. This situation will be amended in the future.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cameo Data Modeler provides code engineering capabilities, database script generation, and reverse engineering. A database model can be generated in the DDL script, which can then be run on the database engine to create database structures. Conversely, the database engine can export database structures into the DDL script, which can then be reverse-engineered into the database model. In addition, Cameo Data Modeler enables reverse engineering directly from a live database through the <strong>JDBC </strong>connection.</p><p>Cameo Data Modeler code engineering supports the following database dialects for script generation and reversing:</p><ul><li>Standard SQL</li><li>Oracle</li><li>MS SQL Server</li><li>DB2</li><li>MySQL</li><li>PostgreSQL</li><li>Sybase</li><li>Pervasive</li><li>Cloudscape / Derby</li><li>MS Access</li><li>Pointbase</li></ul><p>As mentioned earlier, database modeling was significantly extended in version v17.0.1. However, database code engineering stayed at the same level as before. Currently, not all database concepts that can be modeled can be subsequently generated or reverse engineered. This situation will be amended in the future.</p>
````

<!--NOMAGIC_PAGE id=170459741 space=CDMP2024xR1 version=2 -->
## PAGE 00018: Database modeling

- page_id: `170459741`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459741/Database+modeling
- version_number: 2
- version_date: `2024-05-08T13:49:42.462+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support
- labels: []

### NORMALIZED CONTENT

This chapter covers modeling various SQL elements in detail and with examples.

1

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This chapter covers modeling various SQL elements in detail and with examples.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="2f499acd-0aeb-444a-b85e-908b73ae3470"><ac:parameter ac:name="depth">1</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=170459737 space=CDMP2024xR1 version=1 -->
## PAGE 00019: Database support

- page_id: `170459737`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459737/Database+support
- version_number: 1
- version_date: `2023-09-21T12:46:55.950+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Important

398273683

#### CONTENT-COLUMN: Important

398273685

#### CONTENT-BLOCK: Important

398273684

The Cameo Data Modeler plugin brings the following features:

- IMM Relational profile for SQL modeling support (the profile is named according to the OMG working group name).
- Extension profile for Oracle.
- SQL diagram, Oracle SQL diagram and customizations for profiles.
- Code engineering (generation / reverse) features for working with database generation scripts.
- Primitive type libraries for database flavors.
- Template for new Database project creation.
- Sample, demonstrating database modeling features.
- UML / ER to SQL (Oracle and generic) and SQL to UML transformations and accompanying traceability features.
- Entity-Relationship and SQL report.
- Helper functionality for SQL diagrams - notation switch.

The Cameo Data Modeler plugin provides support for database modeling and code engineering. It supports modeling of database concepts at the level of SQL:1999 (SQL3) standard. A few rarely used concepts, such as collation or translation, are not supported.

#### WARNING: Important

Important

**DISCLAIMER**. In v17.0.1 SQL **modeling**was significantly extended and reworked. The new profile for SQL modeling covers more SQL concepts than the old Generic DDL and Oracle DDL profiles previously used for SQL modeling. However, the **code engineering**features (script generation and reverse engineering) were not upgraded yet - code engineering capabilities are almost the same as in v17.0. There is currently a skew between the modeling and code engineering features. Something that can be modeled with the help of the current profile cannot yet be not generated / reversed to / from database script.

398273682

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3709e64c-e727-44c8-ac64-510b9cc0ff4f"><ac:parameter ac:name="id">398273683</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="17119c8b-5891-45e5-bf5c-9cf93bf15d32"><ac:parameter ac:name="id">398273685</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a620cf9a-d780-41d5-bf2e-41bb232af54b"><ac:parameter ac:name="id">398273684</ac:parameter><ac:rich-text-body><p>The Cameo Data Modeler plugin brings the following features:</p><ul><li>IMM Relational profile for SQL modeling support (the profile is named according to the OMG working group name).</li><li>Extension profile for Oracle.</li><li>SQL diagram, Oracle SQL diagram and customizations for profiles.</li><li>Code engineering (generation / reverse) features for working with database generation scripts.</li><li>Primitive type libraries for database flavors.</li><li>Template for new Database project creation.</li><li>Sample, demonstrating database modeling features.</li><li>UML / ER to SQL (Oracle and generic) and SQL to UML transformations and accompanying traceability features.</li><li>Entity-Relationship and SQL report.</li><li>Helper functionality for SQL diagrams - notation switch.</li></ul><p>The Cameo Data Modeler plugin provides support for database modeling and code engineering. It supports modeling of database concepts at the level of SQL:1999 (SQL3) standard. A few rarely used concepts, such as collation or translation, are not supported.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="1d6f0799-8995-4182-9a75-cca4b149a5cf"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><p><span style="color: rgb(153,51,0);"><strong>DISCLAIMER</strong>.</span> In v17.0.1 SQL <strong>modeling </strong>was significantly extended and reworked. The new profile for SQL modeling covers more SQL concepts than the old Generic DDL and Oracle DDL profiles previously used for SQL modeling. However, the <strong>code engineering </strong>features (script generation and reverse engineering) were not upgraded yet - code engineering capabilities are almost the same as in v17.0. There is currently a skew between the modeling and code engineering features. Something that can be modeled with the help of the current profile cannot yet be not generated / reversed to / from database script.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6dcd9207-e31b-4ead-975f-52436b7fffe0"><ac:parameter ac:name="id">398273682</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="c79f2e9e-6e77-4883-b96a-e6358533af8a" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459771 space=CDMP2024xR1 version=6 -->
## PAGE 00020: DDL dialects

- page_id: `170459771`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459771/DDL+dialects
- version_number: 6
- version_date: `2024-05-08T13:58:15.144+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support > Database code engineering
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

32303714

#### CONTENT-COLUMN: Note

32303716

32303713

**On this page**

33

#### CONTENT-BLOCK: Note

32303715

This section reviews Cameo Data Modeler support for DDL script flavors from different vendors.

##### Standard SQL2

For SQL2 statements supported by Cameo Data Modeler, see [CONFLUENCE_PAGE title='Supported SQL statements' space='CDMP2024x'].

The MagicDraw UML schema package is located within a database package. The database definition statement is not part of the SQL2 standard; it is an analogue of a Database (a Catalog).

#### NOTE: Note

Note

A Catalog has no explicit definition statement. If a database package for a Catalog does not exist, it should be created (when it is referred for the first time).

##### Oracle

Cameo Data Modeler Oracle DDL script generation is based on the Velocity engine. This enables you to change a generated DDL script by changing the velocity template. In this chapter we introduce how Oracle DDL generation works in MagicDraw and how to change a template for specific things.

It is necessary to understand the Velocity Template Language to edit or create templates. You can download the Velocity documentation from [http://click.apache.org/docs/velocity/VelocityUsersGuide.pdf](http://click.apache.org/docs/velocity/VelocityUsersGuide.pdf).[http://click.sourceforge.net/docs/velocity/Velocity-](http://click.sourceforge.net/docs/velocity/Velocity-)

For more information about Oracle DDL generation and customization, see [CONFLUENCE_PAGE title='Oracle DDL generation and customization' space='DEVGTWRT'] in the MagicDraw User Guide.

###### Oracle dialect

For more information about Oracle DDL 11g, see [http://download.oracle.com/docs/cd/B28359_01/server.111/b28286/toc.htm](http://download.oracle.com/docs/cd/B28359_01/server.111/b28286/toc.htm).

The Oracle dialect has CREATE DATABASE, CREATE INDEX, and CREATE TRIGGER statements that are not part of SQL2 standard but are taken into account while reversing the DDL script of this dialect.

This dialect has some syntax differences from SQL2 standard because of extensions (e.g. some schema definition statements can have STORAGE clause). These extensions are ignored while reversing.

Code engineering features for Oracle dialect are more extensive than code engineering for other dialects. In addition to the concepts supported by Standard SQL generation, Oracle generation supports the generation and reverse of the following items:

- Sequences
- Synonym
- Structured user-defined types (with methods, map & order functions)
- Function and procedure
- Users, roles grants
- Materialized views

##### Cloudscape

Informix Cloudscape v3.5 dialect has no database definition statement. It uses a database package with the name specified by the CurrentDatabaseName property.

This dialect has CREATE INDEX and CREATE TRIGGER statements that are not part of a SQL2 standard but should be taken into account while reversing the DDL script of this dialect. This dialect has some syntax differences from SQL2 standard because of extensions (e.g. some schema definition statements can have a PROPERTIES clause). These extensions are ignored while reversing.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="105371ac-da20-4fec-b267-f3607164d018"><ac:parameter ac:name="id">32303714</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="900659d0-ebb3-4754-8d7d-58f6af4c7c12"><ac:parameter ac:name="id">32303716</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="73a64f09-fc63-4a0d-b6a6-b3789145855e"><ac:parameter ac:name="id">32303713</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="41e6cd0c-e5c9-46b5-8011-65f92ed28bb6"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="81ecd48b-3e07-47ba-a222-24e974af8e49"><ac:parameter ac:name="id">32303715</ac:parameter><ac:rich-text-body><p><br /></p><p>This section reviews Cameo Data Modeler support for DDL script flavors from different vendors.</p><h3>Standard SQL2</h3><p>For SQL2 statements supported by Cameo Data Modeler, see <ac:link><ri:page ri:space-key="CDMP2024x" ri:content-title="Supported SQL statements" /></ac:link>.</p><p>The MagicDraw UML schema package is located within a database package. The database definition statement is not part of the SQL2 standard; it is an analogue of a Database (a Catalog).</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5eae2f0d-79ef-409b-a3c9-9c4e0e755171"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>A Catalog has no explicit definition statement. If a database package for a Catalog does not exist, it should be created (when it is referred for the first time).</p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">Oracle</h3><p>Cameo Data Modeler Oracle DDL script generation is based on the Velocity engine. This enables you to change a generated DDL script by changing the velocity template. In this chapter we introduce how Oracle DDL generation works in MagicDraw and how to change a template for specific things.</p><p>It is necessary to understand the Velocity Template Language to edit or create templates. You can download the Velocity documentation from <a href="http://click.apache.org/docs/velocity/VelocityUsersGuide.pdf">http://click.apache.org/docs/velocity/VelocityUsersGuide.pdf</a>.<a href="http://click.sourceforge.net/docs/velocity/Velocity-"> </a></p><p>For more information about Oracle DDL generation and customization, see <ac:link><ri:page ri:space-key="DEVGTWRT" ri:content-title="Oracle DDL generation and customization" /></ac:link> in the MagicDraw User Guide.</p><h4>Oracle dialect</h4><p>For more information about Oracle DDL 11g, see <a href="http://download.oracle.com/docs/cd/B28359_01/server.111/b28286/toc.htm">http://download.oracle.com/docs/cd/B28359_01/server.111/b28286/toc.htm</a>.</p><p>The Oracle dialect has CREATE DATABASE, CREATE INDEX, and CREATE TRIGGER statements that are not part of SQL2 standard but are taken into account while reversing the DDL script of this dialect.</p><p>This dialect has some syntax differences from SQL2 standard because of extensions (e.g. some schema definition statements can have STORAGE clause). These extensions are ignored while reversing.</p><p>Code engineering features for Oracle dialect are more extensive than code engineering for other dialects. In addition to the concepts supported by Standard SQL generation, Oracle generation supports the generation and reverse of the following items:</p><ul><li>Sequences</li><li>Synonym</li><li>Structured user-defined types (with methods, map &amp; order functions)</li><li>Function and procedure</li><li>Users, roles grants</li><li>Materialized views</li></ul><h3>Cloudscape</h3><p>Informix Cloudscape v3.5 dialect has no database definition statement. It uses a database package with the name specified by the CurrentDatabaseName property.</p><p>This dialect has CREATE INDEX and CREATE TRIGGER statements that are not part of a SQL2 standard but should be taken into account while reversing the DDL script of this dialect. This dialect has some syntax differences from SQL2 standard because of extensions (e.g. some schema definition statements can have a PROPERTIES clause). These extensions are ignored while reversing.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459825 space=CDMP2024xR1 version=1 -->
## PAGE 00021: Defined stereotypes

- page_id: `170459825`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459825/Defined+stereotypes
- version_number: 1
- version_date: `2023-09-21T12:46:59.073+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

| Stereotype name | Base Stereotype | Applies on | Defined TagDefinitions |
| --- | --- | --- | --- |
| XSDcomponent |  | ClassAttributeAssociationEndBindingGeneralizationCommentComponent | id – stringDetails: The base and abstract stereotype for all XML Schema stereotypes used in UML profile |
| XSDattribute | XSDcomponent | Attribute | fixed – some fixed element valueform – (qualified \| unqualified)refString – string representation of reference to other attribute.ref – actual reference to other attributeuse – (optional \| prohibited \| required) : optional |
| XSDelement | XSDcomponent | AttributeAssociationEnd | abstract – (true \| false)block - (extension \| restriction \| substitution)final - (extension \| restriction)fixed – some fixed element valueform - (qualified \| unqualified)nillable – (true \| false)refString – string representation of reference to other attribute.ref – actual reference to other attributesubstitutionGroup – actual reference to UML ModelElementsubstitutionGroupString – string representation of substitution groupkey_unique_keyRef – a list of referenced UML AttributessequenceOrder – a number in sequence order |
| XSDcomplexType | XSDcomponent | Class | block – (extension \| restriction)final – (extension \| restriction)mixed – (true \| false) |
| XSDsimpleContent |  | Class | simpleContentId – string |
| XSDcomplexContent |  | Class | complexContentId – stringcomplexContentMixed |
| XSDgroup | XSDcomponent | Class |  |
| XSDgroupRef | XSDcomponent | AttributeAssociationEnd | sequenceOrder – a number in sequence order |
| XSDall |  | Class | allId – stringmaxOccursminOccurs |
| XSDchoice |  | Class | choiceId – stringmaxOccursminOccurssequenceOrder – a number in sequence order |
| XSDsequence |  | Class | sequenceId – stringmaxOccursminOccurssequenceOrder – a number in sequence order |
| XSDrestriction | XSDcomponent | Generalization |  |
| XSDextension | XSDcomponent | Generalization |  |
| XSDattributeGroup | XSDcomponent | Class |  |
| XSDsimpleType | XSDcomponent | Class | final - (#all \| (list \| union \| restriction)) |
| XSDlist | XSDcomponent | Class | listId - string |
| XSDunion | XSDcomponent | Class | unionId - string |
| XSDannotation | XSDcomponent | Comment | appInfoSourceappInfoContentsourcexml:lang |
| XSDany | XSDcomponent | Attribute | namespace – stringprocessContents - (lax \| skip \| strict); default strictsequenceOrder – a number in sequence order |
| XSDanyAttribute | XSDcomponent | Attribute | namespace – stringprocessContents - (lax \| skip \| strict); default strict |
| XSDschema | XSDcomponent | Class | attributeFormDefaultblockDefaultelementFormDefaultfinalDefaulttargetNamespace – reference to some ModelPackageversionxml:lang |
| XSDnotation | XSDcomponent | Attribute | publicsystem |
| XSDredefine | XSDcomponent | Class |  |
| XSDimport | XSDcomponent«import» | Permission | schemaLocation |
| XSDinclude | XSDcomponent | Component |  |
| XSDminExclusive | XSDcomponent | Attribute | fixed = boolean : false |
| XSDminInclusive | XSDcomponent | Attribute | fixed = boolean : false |
| XSDmaxExclusive | XSDcomponent | Attribute | fixed = boolean : false |
| XSDmaxInclusive | XSDcomponent | Attribute | fixed = boolean : false |
| XSDtotalDigits | XSDcomponent | Attribute | fixed = boolean : false |
| XSDfractionDigits | XSDcomponent | Attribute | fixed = boolean : false |
| XSDlength | XSDcomponent | Attribute | fixed = boolean : false |
| XSDminLength | XSDcomponent | Attribute | fixed = boolean : false |
| XSDmaxLength | XSDcomponent | Attribute | fixed = boolean : false |
| XSDwhiteSpace | XSDcomponent | Attribute | fixed = boolean : falsevalue |
| XSDpattern | XSDcomponent | Attribute |  |
| XSDenumeration | XSDcomponent | Attribute |  |
| XSDunique |  | Attribute | selectorfield |
| XSDkey |  | Attribute | selectorfield |
| XSDkeyref |  | Attribute | selectorfieldrefer – UML AttributereferString - String |
| XSDnamespace |  | ModelPackage |  |
| xmlns |  | Permission |  |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><table class="relative-table" style="width: 99.9451%;"><colgroup><col style="width: 14.212%;" /><col style="width: 11.6859%;" /><col style="width: 10.022%;" /><col style="width: 64.0802%;" /></colgroup><tbody><tr><th><strong>Stereotype name</strong></th><th><p>Base Stereotype</p></th><th>Applies on</th><th>Defined TagDefinitions</th></tr><tr><td><strong>XSDcomponent</strong></td><td><br /></td><td><p>Class</p><p>Attribute</p><p>AssociationEnd</p><p>Binding</p><p>Generalization</p><p>Comment</p><p>Component</p></td><td><p>id – string</p><p>Details: The base and abstract stereotype for all XML Schema stereotypes used in UML profile</p></td></tr><tr><td><strong>XSDattribute</strong></td><td>XSDcomponent</td><td>Attribute</td><td><p>fixed – some fixed element value</p><p>form – (qualified | unqualified)</p><p>refString – string representation of reference to other attribute.</p><p>ref – actual reference to other attribute</p><p>use – (optional | prohibited | required) : optional</p></td></tr><tr><td><strong>XSDelement</strong></td><td>XSDcomponent</td><td><p>Attribute</p><p>AssociationEnd</p></td><td><p>abstract – (true | false)</p><p>block - (extension | restriction | substitution)</p><p>final - (extension | restriction)</p><p>fixed – some fixed element value</p><p>form - (qualified | unqualified)</p><p>nillable – (true | false)</p><p>refString – string representation of reference to other attribute.</p><p>ref – actual reference to other attribute</p><p>substitutionGroup – actual reference to UML ModelElement</p><p>substitutionGroupString – string representation of substitution group</p><p>key_unique_keyRef – a list of referenced UML Attributes</p><p>sequenceOrder – a number in sequence order</p></td></tr><tr><td><strong>XSDcomplexType</strong></td><td>XSDcomponent</td><td>Class</td><td><p>block – (extension | restriction)</p><p>final – (extension | restriction)</p><p>mixed – (true | false)</p></td></tr><tr><td><p><strong>XSDsimpleContent</strong></p></td><td><br /></td><td>Class</td><td>simpleContentId – string</td></tr><tr><td><p><strong>XSDcomplexContent</strong></p></td><td><br /></td><td>Class</td><td><p>complexContentId – string</p><p>complexContentMixed</p></td></tr><tr><td><strong>XSDgroup</strong></td><td>XSDcomponent</td><td>Class</td><td><br /></td></tr><tr><td><strong>XSDgroupRef</strong></td><td>XSDcomponent</td><td><p>Attribute</p><p>AssociationEnd</p></td><td>sequenceOrder – a number in sequence order</td></tr><tr><td><strong>XSDall</strong></td><td><br /></td><td>Class</td><td><p>allId – string</p><p>maxOccurs</p><p>minOccurs</p></td></tr><tr><td><strong>XSDchoice</strong></td><td><br /></td><td>Class</td><td><p>choiceId – string</p><p>maxOccurs</p><p>minOccurs</p><p>sequenceOrder – a number in sequence order</p></td></tr><tr><td><strong>XSDsequence</strong></td><td><br /></td><td>Class</td><td><p>sequenceId – string</p><p>maxOccurs</p><p>minOccurs</p><p>sequenceOrder – a number in sequence order</p></td></tr><tr><td><strong>XSDrestriction</strong></td><td>XSDcomponent</td><td>Generalization</td><td><br /></td></tr><tr><td><strong>XSDextension</strong></td><td>XSDcomponent</td><td>Generalization</td><td><br /></td></tr><tr><td><p><strong>XSDattributeGroup</strong></p></td><td>XSDcomponent</td><td>Class</td><td><br /></td></tr><tr><td><strong>XSDsimpleType</strong></td><td>XSDcomponent</td><td>Class</td><td>final - (#all | (list | union | restriction))</td></tr><tr><td><strong>XSDlist</strong></td><td>XSDcomponent</td><td>Class</td><td>listId - string</td></tr><tr><td><strong>XSDunion</strong></td><td>XSDcomponent</td><td>Class</td><td>unionId - string</td></tr><tr><td><strong>XSDannotation</strong></td><td>XSDcomponent</td><td>Comment</td><td><p>appInfoSource</p><p>appInfoContent</p><p>source</p><p>xml:lang</p></td></tr><tr><td><strong>XSDany</strong></td><td>XSDcomponent</td><td>Attribute</td><td><p>namespace – string</p><p>processContents - (lax | skip | strict); default strict</p><p>sequenceOrder – a number in sequence order</p></td></tr><tr><td colspan="1"><strong>XSDanyAttribute</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1"><p>namespace – string</p><p>processContents - (lax | skip | strict); default strict</p></td></tr><tr><td colspan="1"><strong>XSDschema</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Class</td><td colspan="1"><p>attributeFormDefault</p><p>blockDefault</p><p>elementFormDefault</p><p>finalDefault</p><p>targetNamespace – reference to some ModelPackage</p><p>version</p><p>xml:lang</p></td></tr><tr><td colspan="1"><strong>XSDnotation</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1"><p>public</p><p>system</p></td></tr><tr><td colspan="1"><strong>XSDredefine</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Class</td><td colspan="1"><br /></td></tr><tr><td colspan="1"><strong>XSDimport</strong></td><td colspan="1"><p>XSDcomponent</p><p>«import»</p></td><td colspan="1">Permission</td><td colspan="1">schemaLocation</td></tr><tr><td colspan="1"><strong>XSDinclude</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Component</td><td colspan="1"><br /></td></tr><tr><td colspan="1"><strong>XSDminExclusive</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1">fixed = boolean : false</td></tr><tr><td colspan="1"><strong>XSDminInclusive</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1">fixed = boolean : false</td></tr><tr><td colspan="1"><p><strong>XSDmaxExclusive</strong></p></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1">fixed = boolean : false</td></tr><tr><td colspan="1"><strong>XSDmaxInclusive</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1">fixed = boolean : false</td></tr><tr><td colspan="1"><strong>XSDtotalDigits</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1">fixed = boolean : false</td></tr><tr><td colspan="1"><strong>XSDfractionDigits</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1">fixed = boolean : false</td></tr><tr><td colspan="1"><strong>XSDlength</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1">fixed = boolean : false</td></tr><tr><td colspan="1"><strong>XSDminLength</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1">fixed = boolean : false</td></tr><tr><td colspan="1"><strong>XSDmaxLength</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1">fixed = boolean : false</td></tr><tr><td colspan="1"><strong>XSDwhiteSpace</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1"><p>fixed = boolean : false</p><p>value</p></td></tr><tr><td colspan="1"><strong>XSDpattern</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1"><br /></td></tr><tr><td colspan="1"><strong>XSDenumeration</strong></td><td colspan="1">XSDcomponent</td><td colspan="1">Attribute</td><td colspan="1"><br /></td></tr><tr><td colspan="1"><strong>XSDunique</strong></td><td colspan="1"><br /></td><td colspan="1">Attribute</td><td colspan="1"><p>selector</p><p>field</p></td></tr><tr><td colspan="1"><strong>XSDkey</strong></td><td colspan="1"><br /></td><td colspan="1">Attribute</td><td colspan="1"><p>selector</p><p>field</p></td></tr><tr><td colspan="1"><strong>XSDkeyref</strong></td><td colspan="1"><br /></td><td colspan="1">Attribute</td><td colspan="1"><p>selector</p><p>field</p><p>refer – UML Attribute</p>referString - String</td></tr><tr><td colspan="1"><strong>XSDnamespace</strong></td><td colspan="1"><br /></td><td colspan="1">ModelPackage</td><td colspan="1"><br /></td></tr><tr><td colspan="1"><strong>xmlns</strong></td><td colspan="1"><br /></td><td colspan="1">Permission</td><td colspan="1"><br /></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459830 space=CDMP2024xR1 version=5 -->
## PAGE 00022: Element

- page_id: `170459830`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459830/Element
- version_number: 5
- version_date: `2024-05-08T14:20:53.047+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to UML Attribute or UML AssociationEnd with stereotype XSDelement.

- annotation – to UML Attribute or UML AssociationEnd documentation.
- default - to initial UML Attribute or UML AssociationEnd value.
- maxOccurs - to multiplicity upper range. Value unbounded maps to asterisk in UML.
- minOccurs – to multiplicity lower range.
- name – to UML Attribute or UML AssociationEnd name.
- type or content (simpleType | complexType) – to UML Attribute or UML AssociationEnd type.

Other properties maps to corresponding tagged values.

#### PANEL: XML representation summary as element Element Information Item

XML representation summary as element Element Information Item

```text
<element
```

```text
abstract = boolean : false
```

```text
block = (#all | List of (extension | restriction | substitution))
```

```text
default = string
```

```text
final = (#all | List of (extension | restriction))
```

```text
fixed = string
```

```text
form = (qualified | unqualified) id = ID
```

```text
maxOccurs = (nonNegativeInteger | unbounded) : 1
```

```text
minOccurs = nonNegativeInteger : 1
```

```text
name = NCName
```

```text
nillable = boolean : false
```

```text
ref = oName
```

```text
substitutionGroup = Oname  type = OName
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, ((simpleType | complexType)?, (unique | key | keyr
```

```text
</element>
```

ref value is generated from ref or refString TaggedValue. One of ref or name must be present, but not both.

If ref is present, then all of <complexType>, <simpleType>, <key>, <keyref>, <unique>, nillable, default, fixed, form, block and type must be absent, i.e. only minOccurs, maxOccurs, and id are allowed in addition to ref, along with <annotation>.

#### PANEL: XML representation summary as element Element Information Item (Continued)

XML representation summary as element Element Information Item (Continued)

```text
<xs:element name = "PurchaseOrder" type = "PurchaseOrderType"/>
```

```text

```

```text
<xs:element name = "gift"›
```

```text
<xs:complexType>
```

```text
<xs:sequence>
```

```text
<xs:element name = "birthday" type = "xs:date"/>
```

```text
<xs:element ref = "PurchaseOrder"/>
```

```text
</xs:complexType>
```

```text
</xs:element>
```

###### [IMAGE alt='' src='']Example of element UML Model.

#### PANEL: XML representation summary as element Element Information Item (Continued)

XML representation summary as element Element Information Item (Continued)

```text
<xs:schema xmlns:nm = "http://nomagic.com" xmlns:xs =
```

```text
"http://www.w3.org/2001/XMLSchema" targetNamespace = "http://nomagic.com" >
```

```text
<xs:element name = "name" type = "xs:string" default = "minde" id = "elementID" abstract = "true" block = "extension" final = "restriction" fixed = "fixedValue" form = "qualified" nillable = "true" substitutionGroup = "nm:count" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >element name documentation</xs:documentation> 		</xs:annotation>
```

```text
</xs:element>
```

```text
<xs:element name = "count" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >element count documentation</xs:documentation>		</xs:annotation>
```

```text
<xs:simpleType>
```

```text
<xs:restriction base = "xs:number" />
```

```text
</xs:simpleType> 	</xs:element>
```

```text
<xs:element name = "hour" type = "xs:integer" />
```

```text
<xs:element name = "minute" type = "xs:integer" substitutionGroup "nm:count" />
```

```text
<xs:element name = "surname" type = "xs:string" minOccurs "1" maxOccurs = "unbounded" />
```

```text
<xs:complexType name = "some_type" >
```

```text
<xs:all >
```

```text
<xs:element ref = "nm:hour" minOccurs = "0" maxOccurs = "1" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >hour ref documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
</xs:element>
```

```text
<xs:element ref = "nm:minute" minOccurs = "0" maxOccurs  "1" />
```

```text
</xs:all>
```

```text
</xs:complexType>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to UML Attribute or UML AssociationEnd with stereotype XSDelement.</p><ul><li>annotation – to UML Attribute or UML AssociationEnd documentation.</li><li>default - to initial UML Attribute or UML AssociationEnd value.</li><li>maxOccurs - to multiplicity upper range. Value unbounded maps to asterisk in UML.</li><li>minOccurs – to multiplicity lower range.</li><li>name – to UML Attribute or UML AssociationEnd name.</li><li>type or content (simpleType | complexType) – to UML Attribute or UML AssociationEnd type.</li></ul><p>Other properties maps to corresponding tagged values.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="4f3ae3e3-1f6c-4219-87d5-0a75eff30204"><ac:parameter ac:name="title">XML representation summary as element Element Information Item</ac:parameter><ac:rich-text-body><pre>&lt;element</pre><pre>	abstract = boolean : false</pre><pre>	block = (#all | List of (extension | restriction | substitution))</pre><pre>	default = string </pre><pre>	final = (#all | List of (extension | restriction))</pre><pre>	fixed = string</pre><pre>	form = (qualified | unqualified) id = ID</pre><pre>	maxOccurs = (nonNegativeInteger | unbounded) : 1</pre><pre>	minOccurs = nonNegativeInteger : 1</pre><pre>	name = NCName </pre><pre>	nillable = boolean : false</pre><pre> 	ref = oName</pre><pre>	substitutionGroup = Oname  type = OName</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, ((simpleType | complexType)?, (unique | key | keyr</pre><pre>&lt;/element&gt;</pre></ac:rich-text-body></ac:structured-macro><p>ref value is generated from ref or refString TaggedValue. One of ref or name must be present, but not both.</p><p>If ref is present, then all of <u>&lt;complexType&gt;,</u> <u>&lt;simpleType&gt;,</u> <u>&lt;key&gt;,</u> <u>&lt;keyref&gt;,</u> <u>&lt;unique&gt;,</u> nillable, default, fixed, form, block and type must be absent, i.e. only minOccurs, maxOccurs, and id are allowed in addition to ref, along with <u>&lt;annotation&gt;.</u></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e67a01fb-8183-4afb-8e00-c545bdba80a8"><ac:parameter ac:name="title">XML representation summary as element Element Information Item (Continued)</ac:parameter><ac:rich-text-body><pre>&lt;xs:element name = &quot;PurchaseOrder&quot; type = &quot;PurchaseOrderType&quot;/&gt;</pre><pre><br /></pre><pre>&lt;xs:element name = &quot;gift&quot;›</pre><pre>	&lt;xs:complexType&gt;</pre><pre>		&lt;xs:sequence&gt;</pre><pre>			&lt;xs:element name = &quot;birthday&quot; type = &quot;xs:date&quot;/&gt;</pre><pre>			&lt;xs:element ref = &quot;PurchaseOrder&quot;/&gt;<br /><br /></pre><pre>	&lt;/xs:complexType&gt;</pre><pre>&lt;/xs:element&gt;</pre></ac:rich-text-body></ac:structured-macro><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 53 Element UML Model Example.png" /></ac:image>Example of element UML Model.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="95317c57-b4fc-4f13-8805-e1699db9f9fb"><ac:parameter ac:name="title">XML representation summary as element Element Information Item (Continued)</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; xmlns:xs =</pre><pre>&quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; &gt;</pre><pre>	&lt;xs:element name = &quot;name&quot; type = &quot;xs:string&quot; default = &quot;minde&quot; id = &quot;elementID&quot; <br />abstract = &quot;true&quot; block = &quot;extension&quot; final = &quot;restriction&quot; fixed = &quot;fixedValue&quot; form = <br />&quot;qualified&quot; nillable = &quot;true&quot; substitutionGroup = &quot;nm:count&quot; &gt;</pre><pre>		&lt;xs:annotation &gt;</pre><pre>			&lt;xs:documentation &gt;element name documentation&lt;/xs:documentation&gt; <br />		&lt;/xs:annotation&gt;</pre><pre>	&lt;/xs:element&gt;</pre><pre>	&lt;xs:element name = &quot;count&quot; &gt;</pre><pre>		&lt;xs:annotation &gt;</pre><pre>			&lt;xs:documentation &gt;element count documentation&lt;/xs:documentation&gt;<br />		&lt;/xs:annotation&gt;</pre><pre>		&lt;xs:simpleType&gt;</pre><pre>			&lt;xs:restriction base = &quot;xs:number&quot; /&gt;</pre><pre>		&lt;/xs:simpleType&gt; <br />	&lt;/xs:element&gt;</pre><pre>	&lt;xs:element name = &quot;hour&quot; type = &quot;xs:integer&quot; /&gt;</pre><pre>	&lt;xs:element name = &quot;minute&quot; type = &quot;xs:integer&quot; substitutionGroup &quot;nm:count&quot; /&gt;</pre><pre>	&lt;xs:element name = &quot;surname&quot; type = &quot;xs:string&quot; minOccurs &quot;1&quot; maxOccurs = &quot;unbounded&quot; /&gt;</pre><pre>	&lt;xs:complexType name = &quot;some_type&quot; &gt;</pre><pre>		&lt;xs:all &gt;</pre><pre>			&lt;xs:element ref = &quot;nm:hour&quot; minOccurs = &quot;0&quot; maxOccurs = &quot;1&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;hour ref documentation&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;</pre><pre>			&lt;/xs:element&gt;</pre><pre>			&lt;xs:element ref = &quot;nm:minute&quot; minOccurs = &quot;0&quot; maxOccurs  &quot;1&quot; /&gt;</pre><pre>		&lt;/xs:all&gt;</pre><pre>	&lt;/xs:complexType&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459698 space=CDMP2024xR1 version=1 -->
## PAGE 00023: Entity-relationship (ER) modeling and diagrams

- page_id: `170459698`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459698/Entity-relationship+ER+modeling+and+diagrams
- version_number: 1
- version_date: `2023-09-21T12:46:55.131+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide
- labels: []

### NORMALIZED CONTENT

398024456

398024459

398024457

The Cameo Data Modeler plugin brings in the following components.

- Entity relationship profile.
- Entity relationship diagram.
- Template for new ER project creation.
- Sample, demonstrating ER modeling features.
- ER to SQL (Oracle and Generic) transformation and accompanying traceability features.
- Entity-Relationship and SQL report.

The entity-relationship diagram, as the name suggests, allows you to specify entities and relationships between them. It is useful for abstract domain modeling, to provide structure for data in the domain. It is much more abstract and implementation-independent than the SQL diagram, which shows the concrete implementation of the data structure in the database.

398024455

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="c9db0976-757b-44a3-a2d9-2ac6f96c5ca7"><ac:parameter ac:name="id">398024456</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="5683abe1-bdd9-42eb-907e-89ef11d14d1d"><ac:parameter ac:name="id">398024459</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5bd51af3-87c9-49ed-a9de-82d36d3ddfe3"><ac:parameter ac:name="id">398024457</ac:parameter><ac:rich-text-body><p>The Cameo Data Modeler plugin brings in the following components.</p><ul><li>Entity relationship profile.</li><li>Entity relationship diagram.</li><li>Template for new ER project creation.</li><li>Sample, demonstrating ER modeling features.</li><li>ER to SQL (Oracle and Generic) transformation and accompanying traceability features.</li><li>Entity-Relationship and SQL report.</li></ul><p>The entity-relationship diagram, as the name suggests, allows you to specify entities and relationships between them. It is useful for abstract domain modeling, to provide structure for data in the domain. It is much more abstract and implementation-independent than the SQL diagram, which shows the concrete implementation of the data structure in the database.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2550e75c-9852-4b39-883c-bc8653560161"><ac:parameter ac:name="id">398024455</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="2f723bc4-99ae-4414-b48a-0bd69bbd0088" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459820 space=CDMP2024xR1 version=5 -->
## PAGE 00024: Entity-relationship and SQL reports

- page_id: `170459820`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459820/Entity-relationship+and+SQL+reports
- version_number: 5
- version_date: `2024-05-08T14:19:46.640+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide
- labels: []

### NORMALIZED CONTENT

MagicDraw provides a report template for generating reports of the data models. The report template is suitable for reporting both ER and SQL models. If your project contains both ER and SQL models, you can produce a unified report covering both models.

The report can be generated using the Report Wizard feature.

To generate a report

1. On the Tools menu, click Report Wizard .
2. In the Select Template area, select Data Modeling > Entity-Relationship and DDL Report and then click Next > .
3. Click Next > again.

#### NOTE: Note

Note

In this step, you can edit report variables. To start editing variables, click the **Variable**button.

4. In the **Select Element Scope**area, define the scope for the report, using the buttons placed between the two lists, and then click **Next >**.

5. In the **Output Options**area, define the appropriate options.

6. Click **Generate**. Wait a moment while the report is generated (generation time depends on the selected scope).

The Report Wizard produces an .rtf file. This file contains sections for each reported model entity, its attributes, relationships with other entities (both simple relationships and generalization / specialization relationships), and keys. The SQL part of the file contains sections for each table (with its columns, constraints, indexes, and triggers), standalone sequence, global procedure or function, user-defined type (with its attributes and methods), and authorization identifier (users, groups, roles, and permissions).

The report has a standard beginning, including a cover page, table of contents, and a table of figures. You can customize sections (such as “Purpose”, “Scope”, “Overview”, and “Revision History”) by changing the predefined report variables. See the 3rd step of the report generation procedure, described above. The report also has an appendix containing all the diagrams in your model.

If the model contains both ER and SQL models and is linked by traceability references, the report will link (with active references) the appropriate report sections of entities and tables that are traceable in the model.

###### [IMAGE alt='' src='']Fragment of ER model report example.

###### [IMAGE alt='' src='']Fragment of SQL model report example.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>MagicDraw provides a report template for generating reports of the data models. The report template is suitable for reporting both ER and SQL models. If your project contains both ER and SQL models, you can produce a unified report covering both models.</p><p>The report can be generated using the Report Wizard feature.</p><p><br /></p><p>To generate a report</p><hr /><ol><li>On the <strong>Tools </strong>menu, click <strong>Report Wizard</strong>.</li><li>In the <strong>Select Template </strong>area, select <strong>Data Modeling </strong>&gt; <strong>Entity-Relationship and DDL Report</strong> and then click <strong>Next &gt;</strong>.</li><li>Click <strong>Next &gt; </strong>again.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2c1b0150-19a4-41c2-92c9-06008cd38283"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>In this step, you can edit report variables. To start editing variables, click the <strong>Variable </strong>button.</p></ac:rich-text-body></ac:structured-macro><p>      4. In the <strong>Select Element Scope </strong>area, define the scope for the report, using the buttons placed between the two lists, and then click <strong>Next &gt;</strong>.</p><p>      5. In the <strong>Output Options </strong>area, define the appropriate options.</p><p>      6. Click <strong>Generate</strong>. Wait a moment while the report is generated (generation time depends on the selected scope).</p><p>The Report Wizard produces an .rtf file. This file contains sections for each reported model entity, its attributes, relationships with other entities (both simple relationships and generalization / specialization relationships), and keys. The SQL part of the file contains sections for each table (with its columns, constraints, indexes, and triggers), standalone sequence, global procedure or function, user-defined type (with its attributes and methods), and authorization identifier (users, groups, roles, and permissions).</p><p>The report has a standard beginning, including a cover page, table of contents, and a table of figures. You can customize sections (such as “Purpose”, “Scope”, “Overview”, and “Revision History”) by changing the predefined report variables. See the 3rd step of the report generation procedure, described above. The report also has an appendix containing all the diagrams in your model.</p><p>If the model contains both ER and SQL models and is linked by traceability references, the report will link (with active references) the appropriate report sections of entities and tables that are traceable in the model.</p><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 46 Fragment of ER Model Report Example.png" /></ac:image>Fragment of ER model report example.</h6><p><br /></p><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 47 Fragment of SQL Model Report Example.png" /></ac:image>Fragment of SQL model report example.</h6>
````

<!--NOMAGIC_PAGE id=170459898 space=CDMP2024xR1 version=1 -->
## PAGE 00025: Enumeration

- page_id: `170459898`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459898/Enumeration
- version_number: 1
- version_date: `2023-09-21T12:47:02.877+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDenumeration.

- value – to Attribute name.

#### PANEL: enumeration XML representation summary

enumeration XML representation summary

```text
<enumeration 	id = ID
```

```text
value = anySimpleType
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</enumeration>
```

#### PANEL: enumeration XML code sample

enumeration XML code sample

```text
The following example is a datatype definition for a user-derived datatype which limits the values of dates to the three US holidays enumerated. This datatype definition would appear in a schema authored by an 'end-user' and shows how to define a datatype by enumerating the values in its value space. The enumerated values must be type-valid literals for the base type.
```

```text

```

```text
<simpleType name='holidays'>
```

```text
<annotation>
```

```text
<documentation>some US holidays</documentation>
```

```text
</annotation>
```

```text
<restriction base='gMonthDay'>
```

```text
<enumeration value='--01-01'>
```

```text
<annotation>
```

```text
<documentation>New Year's day</documentation>
```

```text
</annotation>		</enumeration>
```

```text
<enumeration value='--07-04'>
```

```text
<annotation>
```

```text
<documentation>4th of July</documentation>
```

```text
</annotation>		</enumeration>		<enumeration value='--12-25'>
```

```text
<annotation>				<documentation>Christmas</documentation>
```

```text
</annotation>
```

```text
</enumeration>
```

```text
</restriction></simpleType>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDenumeration.</p><ul><li style="text-align: left;">value – to Attribute name.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="cc963537-f621-4853-ab57-28d81a8bc13a"><ac:parameter ac:name="title">enumeration XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;enumeration <br />	id = ID</pre><pre>	value = anySimpleType</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/enumeration&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="111278b3-1a13-406b-b093-94b6ec002dba"><ac:parameter ac:name="title">enumeration XML code sample</ac:parameter><ac:rich-text-body><pre>The following example is a datatype definition for a user-derived datatype which limits the values of dates to the three US holidays <br />enumerated. This datatype definition would appear in a schema authored by an 'end-user' and shows how to define a datatype by <br />enumerating the values in its value space. The enumerated values must be type-valid literals for the base type.</pre><pre> </pre><pre>&lt;simpleType name='holidays'&gt;</pre><pre>	&lt;annotation&gt;</pre><pre>		&lt;documentation&gt;some US holidays&lt;/documentation&gt;</pre><pre>	&lt;/annotation&gt;</pre><pre>	&lt;restriction base='gMonthDay'&gt;</pre><pre>		&lt;enumeration value='--01-01'&gt;</pre><pre>			&lt;annotation&gt;</pre><pre>				&lt;documentation&gt;New Year's day&lt;/documentation&gt;</pre><pre>			&lt;/annotation&gt;<br />		&lt;/enumeration&gt;</pre><pre>		&lt;enumeration value='--07-04'&gt;</pre><pre>			&lt;annotation&gt;</pre><pre>				&lt;documentation&gt;4th of July&lt;/documentation&gt;</pre><pre>			&lt;/annotation&gt;<br />		&lt;/enumeration&gt;<br />		&lt;enumeration value='--12-25'&gt;</pre><pre>			&lt;annotation&gt;<br />				&lt;documentation&gt;Christmas&lt;/documentation&gt;</pre><pre>			&lt;/annotation&gt;</pre><pre>		&lt;/enumeration&gt;</pre><pre>	&lt;/restriction&gt;<br />&lt;/simpleType&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459796 space=CDMP2024xR1 version=5 -->
## PAGE 00026: ER to SQL (generic / Oracle) transformations

- page_id: `170459796`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459796/ER+to+SQL+generic+Oracle+transformations
- version_number: 5
- version_date: `2024-05-08T14:02:12.572+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Transformations
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

291911505

#### CONTENT-COLUMN: Note

291911508

291911504

**On this page**

33

#### CONTENT-BLOCK: Note

291911507

Both generic and Oracle transformation flavors are very similar, so they will be described together. These transformations are based on and are very similar to the UML to SQL(Generic / Oracle) transformations with several extensions relevant to ER modeling.

This chapter only describes the extended behavior of ER to SQL(Generic / Oracle) transformations.

The full transformation feature set includes:

- conversion of many-to-many relationships into an intermediate table
- three different methods of transforming generalizations into table layouts
- autogenerating primary keys, unique constraints and indexes
- generating additional tables for multivalue attributes
- type remapping between UML and database worlds
- sequence generation
- package hierarchy flattening

For more information, see [CONFLUENCE_PAGE title='UML to SQL transformation' space='CDMP2024x Refresh1 Refresh1 Refresh1R1'].

#### NOTE: Note

Note

Please note that the SQL model produced by the transformation is usually not optimal (e.g. all generalizations are transformed using the same chosen strategy, while different strategies are chosen for each particular case at the discretion of the DBA). It is frequently advisable to refine / edit the produced model after the transformation.

##### Identifying relationships

Identifying relationships are transformed the same way as the UML to SQL transformation. The foreign key of the transformation will be included into the primary key of the dependent entity (the one at the multiple end of the relationship). The difference in an ER to SQL transformation case is that the ER model eliminates guessing which relationships are identifying and which ones are not. In UML to SQL transformation guesses, which UML associations should identify using a heuristic method, composition associations are treated as identifying. This heuristic is controlled by the **Treat compositions as identifying**transformation property. In ER models, identifying relationships are explicitly marked as such; there is no need to guess. “Identifying Relationships and Dependent Entities” on page 9 specifies how identifying relationships are modeled.

##### Key transformation

Keys in ER models are transformed into constraints in a DDL model. The rules for key transformations into DDL constraints are:

1. The Primary key of the entity in the ER model is transformed into a primary key constraint in the SQL model.

2. The Alternative keys of the entities in the ER model are transformed into unique constraints in the SQL model.

3. The Inversion entries of the entities in the ER model are transformed into indexes in the SQL model.

4. If a key or entry in ER model has a name (**identifier**tag), this information is preserved in the SQL model. The corresponding key / index will also have a name in the SQL model.

Let's review an example of key modeling, described in [CONFLUENCE_PAGE title='Key modeling' space='CDMP2024x Refresh1 Refresh1 Refresh1R1']. After the transformation, the three entities of the ER model are transformed into the three tables of the SQL model, respectively.

###### [IMAGE alt='' src='']TBD screenshot example of key transformation results.

##### Virtual entity transformation

Virtual entities of ER models can be transformed into different elements of SQL models as:

- Tables (ordinary, non-virtual entities).
- SQL views (the ER to SQL(Oracle) transformation has an additional choice of simple views or materialized views).

The choice is controlled by the **Virtual Entities Transformed To**transformation property.

##### Tracing between data model layers

After the transformation, a relationship is established between the logical data model layer, represented by the ER model, and the physical data model layer, represented by the SQL model. You can navigate between the connected elements both forward (ER -> SQL) and backward (SQL -> ER) using the dedicated submenu **Go To** on the element’s shortcut menu.

To go forward to the corresponding element

1. Right-click the element.
2. On its shortcut menu, click Go To > Traceability > Model Transformations > Transformed T o .

To go backward to the corresponding element

1. Right-click the element.
2. On its shortcut menu, click Go To > Traceability > Model Transformations > Transformed From .

The same tracing information is visible in the element’s Specification window and **Properties**panel under the **Traceability**tab. This information is also reflected in the Entity-Relationship and SQL Report using navigable references between the report sections. You can also depict traceability information in a relation map or in a tabular format using the capabilities of the custom dependency matrix feature.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d91246f3-eea8-4b84-a32e-d5b516667e10"><ac:parameter ac:name="id">291911505</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c2285f1c-1fc9-4101-9c2a-368052ddbb05"><ac:parameter ac:name="id">291911508</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="964e94a6-672d-4902-b4aa-b2ed5a2a6983"><ac:parameter ac:name="id">291911504</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="bc55642f-175a-4fb0-989e-5db87eef609c"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a85409ef-0e41-4bb6-aec2-a0f5c8633d29"><ac:parameter ac:name="id">291911507</ac:parameter><ac:rich-text-body><p>Both generic and Oracle transformation flavors are very similar, so they will be described together. These transformations are based on and are very similar to the UML to SQL(Generic / Oracle) transformations with several extensions relevant to ER modeling.</p><p>This chapter only describes the extended behavior of ER to SQL(Generic / Oracle) transformations.</p><p>The full transformation feature set includes:</p><ul><li>conversion of many-to-many relationships into an intermediate table</li><li>three different methods of transforming generalizations into table layouts</li><li>autogenerating primary keys, unique constraints and indexes</li><li>generating additional tables for multivalue attributes</li><li>type remapping between UML and database worlds</li><li>sequence generation</li><li>package hierarchy flattening</li></ul><p>For more information, see <ac:link><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="UML to SQL transformation" /></ac:link>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ce92d4be-dc1d-4dee-8c1f-69c720e204b9"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>Please note that the SQL model produced by the transformation is usually not optimal (e.g. all generalizations are transformed using the same chosen strategy, while different strategies are chosen for each particular case at the discretion of the DBA). It is frequently advisable to refine / edit the produced model after the transformation.</p></ac:rich-text-body></ac:structured-macro><h3>Identifying relationships</h3><p>Identifying relationships are transformed the same way as the UML to SQL transformation. The foreign key of the transformation will be included into the primary key of the dependent entity (the one at the multiple end of the relationship). The difference in an ER to SQL transformation case is that the ER model eliminates guessing which relationships are identifying and which ones are not. In UML to SQL transformation guesses, which UML associations should identify using a heuristic method, composition associations are treated as identifying. This heuristic is controlled by the <strong>Treat compositions as identifying </strong>transformation property. In ER models, identifying relationships are explicitly marked as such; there is no need to guess. “Identifying Relationships and Dependent Entities” on page 9 specifies how identifying relationships are modeled.</p><h3>Key transformation</h3><p>Keys in ER models are transformed into constraints in a DDL model. The rules for key transformations into DDL constraints are:</p><p>1. The Primary key of the entity in the ER model is transformed into a primary key constraint in the SQL model.</p><p>2. The Alternative keys of the entities in the ER model are transformed into unique constraints in the SQL model.</p><p>3. The Inversion entries of the entities in the ER model are transformed into indexes in the SQL model.</p><p>4. If a key or entry in ER model has a name (<strong>identifier </strong>tag), this information is preserved in the SQL model. The corresponding key / index will also have a name in the SQL model.</p><p>Let's review an example of key modeling, described in <ac:link><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Key modeling" /></ac:link>. After the transformation, the three entities of the ER model are transformed into the three tables of the SQL model, respectively.</p><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 41 TBD Screenshot Example of Key Transformation Results.png" /></ac:image>TBD screenshot example of key transformation results.</h6><h3>Virtual entity transformation</h3><p>Virtual entities of ER models can be transformed into different elements of SQL models as:</p><ul><li>Tables (ordinary, non-virtual entities).</li><li>SQL views (the ER to SQL(Oracle) transformation has an additional choice of simple views or materialized views).</li></ul><p>The choice is controlled by the <strong>Virtual Entities Transformed To </strong>transformation property.</p><h3>Tracing between data model layers</h3><p>After the transformation, a relationship is established between the logical data model layer, represented by the ER model, and the physical data model layer, represented by the SQL model. You can navigate between the connected elements both forward (ER -&gt; SQL) and backward (SQL -&gt; ER) using the dedicated submenu <strong>Go To</strong> on the element’s shortcut menu.</p><p>To go forward to the corresponding element</p><hr /><ol><li>Right-click the element.</li><li>On its shortcut menu, click <strong>Go To </strong>&gt; <strong>Traceability </strong>&gt; <strong>Model Transformations </strong>&gt; <strong>Transformed T</strong><strong>o</strong>.</li></ol><p><br /></p><p>To go backward to the corresponding element</p><hr /><ol><li>Right-click the element.</li><li style="text-align: left;">On its shortcut menu, click <strong>Go To </strong>&gt; <strong>Traceability </strong>&gt; <strong>Model Transformations </strong>&gt; <strong>Transformed From</strong>.</li></ol><p><br /></p><p>The same tracing information is visible in the element’s Specification window and <strong>Properties </strong>panel under the <strong>Traceability </strong>tab. This information is also reflected in the Entity-Relationship and SQL Report using navigable references between the report sections. You can also depict traceability information in a relation map or in a tabular format using the capabilities of the custom dependency matrix feature.</p><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459880 space=CDMP2024xR1 version=1 -->
## PAGE 00027: FractionDigits

- page_id: `170459880`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459880/FractionDigits
- version_number: 1
- version_date: `2023-09-21T12:47:01.996+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDfractionDigits. The name and type of such an attribute do not make sense.

- value – to Attribute initial value.

#### PANEL: fractionDigits XML representation summary

fractionDigits XML representation summary

```text
<fractionDigits
```

```text
fixed = boolean : false
```

```text
id = ID
```

```text
value = nonNegativeInteger
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</fractionDigits>
```

#### PANEL: fractionDigits XML code sample

fractionDigits XML code sample

```text
The following is the definition of a user-derived datatype which could be used to represent the magnitude of a person's body temperature on the Celsius scale. This definition would appear in a schema authored by an end-user and shows how to define a datatype by specifying facet values which constrain the range of the base type.
```

```text
<simpleType name='celsiusBodyTemp'>
```

```text
<restriction base='decimal'>
```

```text
<totalDigits value='4'/>
```

```text
<fractionDigits value='1'/>
```

```text
<minInclusive value='36.4'/>
```

```text
<maxInclusive value='40.5'/>
```

```text
</restriction>
```

```text
</simpleType>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDfractionDigits. The name and type of such an attribute do not make sense.</p><ul><li style="text-align: left;">value – to Attribute initial value.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="0e240d4b-ee6e-40da-8542-80976a19b276"><ac:parameter ac:name="title">fractionDigits XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;fractionDigits</pre><pre>	fixed = boolean : false</pre><pre>	id = ID</pre><pre>	value = nonNegativeInteger</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/fractionDigits&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f1fc8b07-dd35-4015-995b-05ee11bcbb9d"><ac:parameter ac:name="title">fractionDigits XML code sample</ac:parameter><ac:rich-text-body><pre>The following is the definition of a user-derived datatype which could be used to represent the magnitude of a person's body <br />temperature on the Celsius scale. This definition would appear in a schema authored by an end-user and shows how to define <br />a datatype by specifying facet values which constrain the range of the base type.<br /><br /></pre><pre>&lt;simpleType name='celsiusBodyTemp'&gt;</pre><pre>	&lt;restriction base='decimal'&gt;</pre><pre>		&lt;totalDigits value='4'/&gt;</pre><pre>		&lt;fractionDigits value='1'/&gt;</pre><pre>		&lt;minInclusive value='36.4'/&gt;</pre><pre>		&lt;maxInclusive value='40.5'/&gt;</pre><pre>	&lt;/restriction&gt;</pre><pre>&lt;/simpleType&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459722 space=CDMP2024xR1 version=6 -->
## PAGE 00028: Generalization and specialization

- page_id: `170459722`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459722/Generalization+and+specialization
- version_number: 6
- version_date: `2024-05-08T13:44:41.065+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Entity-relationship (ER) modeling and diagrams
- labels: []

### NORMALIZED CONTENT

An ER diagram has a support for generalization / specialization modeling. Generalization and Specialization are really the same relationship, with a different direction of classification. Generalization is bottom-up, while specialization is top-down. Thus, they use the same model element.

Generalizations can be joined into generalization sets (trees of generalizations), which allow specifying additional properties on a group of generalizations - such as disjointness and completeness constraints.

[IMAGE alt='' src='']

###### Example of generalization in ER diagram.

Disjointness and completeness constraints are specified using the **Is Disjoint**(*true*for disjoint, *false*for overlapping specialization) and **Is Covering**(*true*for total, *false*for partial specialization) properties. They can be set in either the relationship shortcut menu or the Specification window.

There are 4 combinations of these two settings. The “breadloaf” symbol joining generalizations into a tree shows these 4 variations (See the following figures).

[IMAGE alt='' src='']

###### Example of overlapping and partial specialization in ER diagram.

[IMAGE alt='' src='']

###### Example of overlapping and total specialization in ER diagram.

[IMAGE alt='' src='']

###### Example of disjoint and partial specialization in ER diagram.

[IMAGE alt='' src='']

###### Example of disjoint and total specialization in ER diagram.

#### NOTE: Note

Note

UML terminology (covering / not covering) is used for the completeness property name in the Specification window. Other names, more familiar for data modelers, are total / partial and complete / incomplete. These terms are analogous and can be used interchangeably.

In the specialization hierarchies, there can be several ways to assign an entity instance to a specific entity subtype. You can determine it when you decide to which subtype a given instance belongs (user-defined specialization). You can also determine it by actual data values of an entity instance (attribute-defined specialization). The latter case can be further subdivided into two subcases - simple attribute-based discrimination (when discrimination is performed by doing simple attribute value comparison) and more complex predicate-based discrimination (when discrimination is specified using more complex, explicitly specified conditions).

Examples of these two cases are shown in the following figures.

[IMAGE alt='' src='']

###### Example of attribute-based discriminator in ER diagram.

[IMAGE alt='' src='']

###### Example of a predicate-based discriminator in an ER diagram.

Discriminators are modeled as special constraints placed on individual generalization relationships. The easiest way to access them is from the shortcut menu of the generalization.

The predicate-based discriminator is simpler; just fill in the **Specification**field of the predicate with an appropriate expression text.

The attribute-based discriminator is more complex. First, specify the columns by which you will sort the entities into the corresponding subclasses. This is done by filling in the **Discriminator**field of the generalization set (you can specify one or several columns there). Then, fill in the **Template**field of the predicate. This template field holds an instance specification used as a template or etalon to differentiate the entity instances into appropriate subclasses. Fill in the slots for the same columns you indicated on the generalization set.

#### NOTE: Note

Note

The category (also known as union) concept is currently not explicitly supported. Total (but not partial) categories can be “simulated” using the total specialization tree, just visually reversed.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An ER diagram has a support for generalization / specialization modeling. Generalization and Specialization are really the same relationship, with a different direction of classification. Generalization is bottom-up, while specialization is top-down. Thus, they use the same model element.</p><p>Generalizations can be joined into generalization sets (trees of generalizations), which allow specifying additional properties on a group of generalizations - such as disjointness and completeness constraints.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 3 Generalization in ER Diagram.png" /></ac:image></p><h6 style="text-align: center;">Example of generalization in ER diagram.</h6><p>Disjointness and completeness constraints are specified using the <strong>Is Disjoint </strong>(<em>true </em>for disjoint, <em>false </em>for overlapping specialization) and <strong>Is Covering </strong>(<em>true </em>for total, <em>false </em>for partial specialization) properties. They can be set in either the relationship shortcut menu or the Specification window.</p><p>There are 4 combinations of these two settings. The “breadloaf” symbol joining generalizations into a tree shows these 4 variations (See the following figures).</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 4 Overlapping and Partial Specialization in ER Diagram.png" /></ac:image></p><h6 style="text-align: center;">Example of overlapping and partial specialization in ER diagram.</h6><p style="text-align: center;"><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Figure 5 Overlapping and Total Specialization in ER Diagram.png" /></ac:image></p><h6 style="text-align: center;">Example of overlapping and total specialization in ER diagram.</h6><p style="text-align: center;"><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Figure 6 Disjoint and Partial Specialization in ER Diagram.png" /></ac:image></p><h6 style="text-align: center;">Example of disjoint and partial specialization in ER diagram.</h6><p style="text-align: center;"><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Figure 7 Disjoint and Total Specialization in ER Diagram.png" /></ac:image></p><h6 style="text-align: center;">Example of disjoint and total specialization in ER diagram.</h6><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b45fd844-fae4-459e-b0a9-d0e26c8f51dc"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>UML terminology (covering / not covering) is used for the completeness property name in the Specification window. Other names, more familiar for data modelers, are total / partial and complete / incomplete. These terms are analogous and can be used interchangeably.</p></ac:rich-text-body></ac:structured-macro><p>In the specialization hierarchies, there can be several ways to assign an entity instance to a specific entity subtype. You can determine it when you decide to which subtype a given instance belongs (user-defined specialization). You can also determine it by actual data values of an entity instance (attribute-defined specialization). The latter case can be further subdivided into two subcases - simple attribute-based discrimination (when discrimination is performed by doing simple attribute value comparison) and more complex predicate-based discrimination (when discrimination is specified using more complex, explicitly specified conditions).</p><p style="text-align: left;">Examples of these two cases are shown in the following figures.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Figure 8 Attribute-based Discriminator in ER Diagram.png" /></ac:image></p><h6 style="text-align: center;">Example of attribute-based discriminator in ER diagram.</h6><p style="text-align: center;"><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Figure 9 Predicate-based Discriminator in ER Diagram.png" /></ac:image></p><h6 style="text-align: center;">Example of a predicate-based discriminator in an ER diagram.</h6><p>Discriminators are modeled as special constraints placed on individual generalization relationships. The easiest way to access them is from the shortcut menu of the generalization.</p><p>The predicate-based discriminator is simpler; just fill in the <strong>Specification </strong>field of the predicate with an appropriate expression text.</p><p>The attribute-based discriminator is more complex. First, specify the columns by which you will sort the entities into the corresponding subclasses. This is done by filling in the <strong>Discriminator </strong>field of the generalization set (you can specify one or several columns there). Then, fill in the <strong>Template </strong>field of the predicate. This template field holds an instance specification used as a template or etalon to differentiate the entity instances into appropriate subclasses. Fill in the slots for the same columns you indicated on the generalization set.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3aee853b-c72e-474b-b837-0e4f2ab6fede"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The category (also known as union) concept is currently not explicitly supported. Total (but not partial) categories can be “simulated” using the total specialization tree, just visually reversed.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459697 space=CDMP2024xR1 version=6 -->
## PAGE 00029: Getting started

- page_id: `170459697`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459697/Getting+started
- version_number: 6
- version_date: `2024-05-08T13:17:33.111+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide
- labels: []

### NORMALIZED CONTENT

The Cameo Data Modeler plugin is an add-on for MagicDraw Standard, Professional, and Architect Editions. It is purchased separately; however, it is free of charge for MagicDraw Enterprise Edition. The Cameo Data Modeler plugin replaces the previous (free) Data Modeling Notations plugin that supported the business entity-relationship diagram (a simplified version of an entity- relationship diagram), for high level, abstract domain data modeling. This plugin repackages database and XML schema modeling functionality, previously available only in MagicDraw Architect and Enterprise editions.

- [CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='CDMP2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Cameo Data Modeler plugin is an add-on for MagicDraw Standard, Professional, and Architect Editions. It is purchased separately; however, it is free of charge for MagicDraw Enterprise Edition. The Cameo Data Modeler plugin replaces the previous (free) Data Modeling Notations plugin that supported the business entity-relationship diagram (a simplified version of an entity- relationship diagram), for high level, abstract domain data modeling. This plugin repackages database and XML schema modeling functionality, previously available only in MagicDraw Architect and Enterprise editions.</p><ul><li class="auto-cursor-target"><ac:link><ri:page ri:space-key="CDMP2024xR1" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[Installing Cameo Data Modeler Plugin]]></ac:plain-text-link-body></ac:link></li></ul>
````

<!--NOMAGIC_PAGE id=170459927 space=CDMP2024xR1 version=5 -->
## PAGE 00030: Group

- page_id: `170459927`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459927/Group
- version_number: 5
- version_date: `2024-05-08T14:26:08.604+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to UML Class with the stereotype XSDgroup.

This class may also have the stereotype XSDall, XSDsequence or XSDchoice.

If a group has the ref attribute, the group definition maps to the UML Attribute or the UML Association End. The UML Attribute must have XSDgroupRef**stereotype. This stereotype may be omitted for the AssociationEnd.

#### PANEL: group XML representation summary

group XML representation summary

```text
<group
```

```text
name = NCName>
```

```text
Content: (annotation?, (all | choice | sequence))
```

```text
</group><group
```

```text
ref = OName
```

```text
maxOccurs = (nonNegativeInteger | unbounded) : 1
```

```text
minOccurs = nonNegativeInteger : 1>
```

```text
Content: (annotation?)
```

```text
</group>
```

#### PANEL: group XML code sample

group XML code sample

```text
<xs:group name="myModelGroup">	<xs:sequence>
```

```text
<xs:element ref="someThing"/>		...
```

```text
</xs:sequence></xs:group>
```

```text
<xs:complexType name="trivial">	<xs:group ref="myModelGroup"/>	<xs:attribute…/></xs:complexType>
```

```text
<xs:complexType name="moreSo">	<xs:choice>
```

```text
<xs:element ref="anotherThing"/>		<xs:group ref="myModelGroup"/>	</xs:choice>
```

```text
<xs:attribute…/></xs:complexType>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to UML Class with the stereotype XSDgroup.</p><p>This class may also have the stereotype XSDall, XSDsequence or XSDchoice.</p><p style="text-align: left;">If a group has the ref attribute, the group definition maps to the UML Attribute or the UML Association End. The UML Attribute must have XSDgroupRef<em> </em>stereotype. This stereotype may be omitted for the AssociationEnd.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="d765330c-9614-46b3-98c1-df2e4339d7d8"><ac:parameter ac:name="title">group XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;group</pre><pre>	name = NCName&gt;</pre><pre>	Content: (annotation?, (all | choice | sequence))</pre><pre>&lt;/group&gt;<br />&lt;group</pre><pre>	ref = OName</pre><pre>	maxOccurs = (nonNegativeInteger | unbounded) : 1</pre><pre>	minOccurs = nonNegativeInteger : 1&gt;</pre><pre>  	Content: (annotation?)</pre><pre>&lt;/group&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e9b73bb3-40ee-494f-9bea-ced795054a0d"><ac:parameter ac:name="title">group XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;xs:group name=&quot;myModelGroup&quot;&gt;<br />	&lt;xs:sequence&gt;</pre><pre>		&lt;xs:element ref=&quot;someThing&quot;/&gt;<br />		...</pre><pre>	&lt;/xs:sequence&gt;<br />&lt;/xs:group&gt;<br /><br /></pre><pre>&lt;xs:complexType name=&quot;trivial&quot;&gt;<br />	&lt;xs:group ref=&quot;myModelGroup&quot;/&gt;<br />	&lt;xs:attribute…/&gt;<br />&lt;/xs:complexType&gt;<br /><br /></pre><pre>&lt;xs:complexType name=&quot;moreSo&quot;&gt;<br />	&lt;xs:choice&gt;</pre><pre>		&lt;xs:element ref=&quot;anotherThing&quot;/&gt;<br />		&lt;xs:group ref=&quot;myModelGroup&quot;/&gt;<br />	&lt;/xs:choice&gt;</pre><pre>	&lt;xs:attribute…/&gt;<br />&lt;/xs:complexType&gt;</pre></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=170459798 space=CDMP2024xR1 version=4 -->
## PAGE 00031: Identifying relationships

- page_id: `170459798`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459798/Identifying+relationships
- version_number: 4
- version_date: `2024-05-08T13:11:34.729+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Transformations > ER to SQL (generic / Oracle) transformations
- labels: []

### NORMALIZED CONTENT

Identifying relationships are transformed in the same way as in the UML to SQL transformation, that is, the foreign key of the transformation gets to be included into the primary key of the dependent entity (the one at the multiple end of the relationship). The difference in ER to SQL transformation case is that the ER model eliminates guessing, which relationships are identifying and which ones are not. UML to SQL transformation guesses, which UML associations should be identifying, by using a heuristic method - composition associations are treated as identifying (this heuristic is controlled by the **Treat compositions as identifying**transformation property). In ER models, identifying relationships are explicitly marked as such, hence there is no need to guess (See [CONFLUENCE_PAGE title='Identifying relationships and dependent entities' space='CDMP2024x Refresh1 Refresh1 Refresh1R1'] that specifies how identifying relationships is modeled).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Identifying relationships are transformed in the same way as in the UML to SQL transformation, that is, the foreign key of the transformation gets to be included into the primary key of the dependent entity (the one at the multiple end of the relationship). The difference in ER to SQL transformation case is that the ER model eliminates guessing, which relationships are identifying and which ones are not. UML to SQL transformation guesses, which UML associations should be identifying, by using a heuristic method - composition associations are treated as identifying (this heuristic is controlled by the <strong>Treat compositions as identifying </strong>transformation property). In ER models, identifying relationships are explicitly marked as such, hence there is no need to guess (See <ac:link><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Identifying relationships and dependent entities" /></ac:link> that specifies how identifying relationships is modeled).</p>
````

<!--NOMAGIC_PAGE id=170459719 space=CDMP2024xR1 version=6 -->
## PAGE 00032: Identifying relationships and dependent entities

- page_id: `170459719`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459719/Identifying+relationships+and+dependent+entities
- version_number: 6
- version_date: `2024-05-08T13:43:59.280+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Entity-relationship (ER) modeling and diagrams
- labels: []

### NORMALIZED CONTENT

One-to-many and (very rarely) one-to-one relationships can be declared as “identifying” relationships. An identifying relationship is a “stronger” version of the relationship, indicating that the entity at the multiple end of the relationship cannot exist without the entity on the other end.

You can create these relationships using the buttons on the diagram pallet, as well as turn an existing relationship into an identifying one and back again. To do this, either change the **Is Identifying**property value in the relationship Specification window or select the appropriate check box on its shortcut menu.

An identifying relationship is drawn as a solid line. Non-identifying relationships use heavy dashes.

Dependent / independent entities are a closely related concept. Dependent entities occur at the multiple end of the identifying relationship. They cannot exist without the independent entity at the other end. In addition, every inherited entity (if you are doing ER modeling) is considered to be dependent. A dependent entity's primary key includes the other entity's key as part. This is implied, not shown in the model. Dependent entities are automatically recognized and drawn with rounded corners.

[IMAGE alt='' src='']

###### Example of identifying relationship and dependent entity in the ER diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>One-to-many and (very rarely) one-to-one relationships can be declared as “identifying” relationships. An identifying relationship is a “stronger” version of the relationship, indicating that the entity at the multiple end of the relationship cannot exist without the entity on the other end.</p><p>You can create these relationships using the buttons on the diagram pallet, as well as turn an existing relationship into an identifying one and back again. To do this, either change the <strong>Is Identifying </strong>property value in the relationship Specification window or select the appropriate check box on its shortcut menu.</p><p>An identifying relationship is drawn as a solid line. Non-identifying relationships use heavy dashes.</p><p>Dependent / independent entities are a closely related concept. Dependent entities occur at the multiple end of the identifying relationship. They cannot exist without the independent entity at the other end. In addition, every inherited entity (if you are doing ER modeling) is considered to be dependent. A dependent entity's primary key includes the other entity's key as part. This is implied, not shown in the model. Dependent entities are automatically recognized and drawn with rounded corners.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="image2017-9-8_16-26-22.png" /></ac:image></p><h6 style="text-align: center;">Example of identifying relationship and dependent entity in the ER diagram.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=170459951 space=CDMP2024xR1 version=5 -->
## PAGE 00033: Import

- page_id: `170459951`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459951/Import
- version_number: 5
- version_date: `2024-05-08T14:27:43.375+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Permission with the stereotype XSDimport. The permission client must be the schema class stereotypes*«XSDschema*» Component, supplier namespace Package *XSDnamespace*.

- namespace maps to the supplier name.
- annotation maps to the UML Attribute documentation.
- schemaLocation maps to the TaggedValue.

#### PANEL: import XML representation summary

import XML representation summary

```text
<import
```

```text
id = ID
```

```text
namespace = anyURI
```

```text
schemaLocation = anyURI
```

```text
{any attributes with non-schema namespace…}>	Content: (annotation?)
```

```text
</import>
```

In the following example, the same namespace may be used both for real work, and in the course of defining schema components in terms of foreign components.

#### PANEL: The treatment of references as internal references to the names being defined in a schema document

The treatment of references as internal references to the names being defined in a schema document

```text
<schema xmlns="http://www.w3.org/2001/XMLSchema" xmlns:html="http://www.w3.org/1999/xhtml" targetNamespace="uri:mywork" xmlns:my="uri:mywork">
```

```text
<import namespace="http://www.w3.org/1999/xhtml"/>
```

```text
<annotation>
```

```text
<documentation>
```

```text
<html:p>[Some documentation for my schema]</html:p>		</documentation>
```

```text
</annotation>
```

```text
…
```

```text
<complexType name="myType">
```

```text
<sequence>
```

```text
<element ref="html:p" minOccurs="0"/>		</sequence>
```

```text
…
```

```text
</complexType>
```

```text
<element name="myElt" type="my:myType"/>
```

```text
</schema>
```

The treatment of references as ·**QNames**· implies that since the target namespace and the XML Schema namespace differ (with the exception of the schema for schemas), then without massive redeclaration of the default namespace either the internal references to the names being defined in a schema document or the schema declaration and definition elements themselves must be explicitly qualified. This example shows the first option, while most other examples in this specification showed the second.

###### [IMAGE alt='' src='']import UML model example.

#### PANEL: import XML code sample

import XML code sample

```text
<xs:schema xmlns:nm = "http://nomagic.com" xmlns:xs = "http://www.w3.org/2001/XMLSchema" targetNamespace = "http://nomagic.com"›
```

```text
<xs:import namespace = "http://www.w3.org/1999/xhtml" schemaLocation = "http://www.w3.org/1999/xhtml" />
```

```text
</xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Permission with the stereotype XSDimport. The permission client must be the schema class stereotypes<em> «XSDschema</em>» Component, supplier namespace Package <em>XSDnamespace</em>.</p><ul><li>namespace maps to the supplier name.</li><li>annotation maps to the UML Attribute documentation.</li><li>schemaLocation maps to the TaggedValue.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="bb3f5623-ac5b-4d0c-a277-0009751a54b8"><ac:parameter ac:name="title">import XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;import</pre><pre>	id = ID</pre><pre>	namespace = anyURI</pre><pre>	schemaLocation = anyURI</pre><pre>	{any attributes with non-schema namespace…}&gt;<br />	Content: (annotation?)</pre><pre>&lt;/import&gt;</pre></ac:rich-text-body></ac:structured-macro><p>In the following example, the same namespace may be used both for real work, and in the course of defining schema components in terms of foreign components.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="aa4f9a1c-bdf8-47e7-99fd-e0638c333905"><ac:parameter ac:name="title">The treatment of references as internal references to the names being defined in a schema document</ac:parameter><ac:rich-text-body><pre>&lt;schema xmlns=&quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; xmlns:html=&quot;<a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a>&quot; targetNamespace=&quot;uri:mywork&quot; <br />xmlns:my=&quot;uri:mywork&quot;&gt;</pre><pre><br />	&lt;import namespace=&quot;<a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a>&quot;/&gt;</pre><pre><br />	&lt;annotation&gt;</pre><pre>		&lt;documentation&gt;</pre><pre>			&lt;html:p&gt;[Some documentation for my schema]&lt;/html:p&gt;<br />		&lt;/documentation&gt;</pre><pre>	&lt;/annotation&gt;</pre><pre>	…</pre><pre>	&lt;complexType name=&quot;myType&quot;&gt;</pre><pre>		&lt;sequence&gt;</pre><pre>			&lt;element ref=&quot;html:p&quot; minOccurs=&quot;0&quot;/&gt;<br />		&lt;/sequence&gt;</pre><pre>		…</pre><pre>	&lt;/complexType&gt;</pre><pre><br />	&lt;element name=&quot;myElt&quot; type=&quot;my:myType&quot;/&gt;</pre><pre>&lt;/schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p>The treatment of references as ·<strong>QNames</strong>· implies that since the target namespace and the XML Schema namespace differ (with the exception of the schema for schemas), then without massive redeclaration of the default namespace either the internal references to the names being defined in a schema document or the schema declaration and definition elements themselves must be explicitly qualified. This example shows the first option, while most other examples in this specification showed the second.</p><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 139 import UML Model Example.png" /></ac:image>import UML model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e860fb9d-f856-475e-bc7f-9088444b01eb"><ac:parameter ac:name="title">import XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot;›</pre><pre>	&lt;xs:import namespace = &quot;<a href="http://www.w3.org/1999/xhtmln">http://www.w3.org/1999/xhtml&quot;</a> schemaLocation = &quot;<a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a>&quot; /&gt;</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=170459736 space=CDMP2024xR1 version=1 -->
## PAGE 00034: Importing CA ERwin® data modeler projects

- page_id: `170459736`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459736/Importing+CA+ERwin%C2%AE+data+modeler+projects
- version_number: 1
- version_date: `2023-09-21T12:46:55.886+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Entity-relationship (ER) modeling and diagrams
- labels: []

### NORMALIZED CONTENT

1276634702

1276634704

1276634701

**On this page**

33

1276634703

The Cameo Data Modeler Plugin for MagicDraw provides import functionality for data models created using the CA ERwin® Data Modeler (henceforth will be referred as ERwin). ERwin is one of the leaders in the data modeling tools market.

Data models produced in ERwin have a two-layer structure, consisting of tightly synchronized logical and physical layers. The physical layer semantically corresponds to the SQL modeling / diagramming / generation functionality in MagicDraw. The logical layer corresponds to ER diagrams implemented by the Cameo Data Modeler Plugin.

The import functionality only imports logical layer data from ERwin into ER diagrams / data models in MagicDraw. The Cameo Data Modeler Plugin does not yet support importing physical layer data.

##### Importing data models

Cameo Data Modeler supports model files produced in ERwin version 7.x. It is recommended that you use the newest v7.3 since it has been heavily tested. Data models in ERwin must be saved in the *.xml format (choose the **XML Standard File**option in the **Save As**dialog).

To import an ERwin model

1. Start MagicDraw.
2. Click File > Import From > CA ERwin Data Modeler v7.x . The Open file dialog will open.
3. Select an ERwin model file (*.xml). A new MagicDraw project will be created and a logical model will be imported from the ERwin model file into that project.

After a successful import, you can proceed to edit or manage the model using MagicDraw features.

If you want to include the ER model as part of a larger project in MagicDraw, you can use either module linking functionality (click **File**> **Use Module**) to attach the ER model to your main project model or project import functionality (click **File**> **Import From**> **Another MagicDraw Project**) to transfer the contents of this ER model to your main project model.

If you want to update an imported and edited ER model (for example, you made changes to the ERwin model and want to import those changes into MagicDraw again), you can use the merge functionality (click **Tools**> **Project Merge**) to import the ERwin model into a new ER model and merge it with the model you have imported earlier.

##### Imported elements

Import mapping reviews and notes are in the following table.

| ERwin | Cameo Data Modeler | Comments |
| --- | --- | --- |
| Any element | Any Element | For each element, its name, definition, and notes are imported.Definitions are imported as MagicDraw documentation (special UML comments). Notes are imported as UML comments. |
| Entity | Entity |  |
| Attribute | Attribute | The Null / Not Null setting is imported as UML multiplicities [0..1] / [1].Attribute constraints and default value information is imported.Domain information is not imported because domains are not supported.Attribute type information is imported - the standard primitive types are mapped to the UML primitive types.Other types (those not found in the model) are created on the fly. |
| Key | Key Marking on Attributes | There is no separate standalone model element for a key in the Cameo Data Modeler ER diagrams. Instead, attributes belonging to a key are marked by applying a stereotype to them (PK, AK, or IE) as necessary. |
| Relationship | Association relationship | Simple relationships are mapped to UML associations.Verb phrases are mapped to role names.Cardinality and null / not null settings are mapped to UML multiplicities ([0..1], [1], [0..*], [1..*]).Referential integrity information is stored in a special stereotype / tag.Key information is not imported since the current ER diagrams do not support FK modeling. |
|  | Generalization relationship | ERwin relationships participating in the generalization tree are mapped to UML generalizations.Generalizations are joined into generalization trees.Complete / incomplete and overlapping / exclusive settings are imported / supported.Discriminating columns are imported / supported.Referential integrity information is stored in a special stereotype / tag.Verb phrase information is not imported. |
| Default Value | Instance Specification | A standalone UML instance specification is created to hold value definition. This instance specification is (or can be) then referenced from attributes, default value fields. |
| Domain | - | Domains are not yet supported in Cameo Data Modeler. |
| Validation Rule | Constraint | The Validation rule is stored as constraint body text. |
| Display | ER diagram | Due to geometric constraints and element size changes, the diagram layout will be slightly different.Paths between elements can be re-routed. |
| User Defined Properties Dictionary | Profile / Stereotypes / Tags | A custom UML profile is created for the user's property definitions. |
| User Defined Properties | Tag Values | A custom profile generated from the UDP dictionary is applied and user property information is stored in the tag values of the applied custom stereotypes. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3bdfb118-d506-482e-a0e9-cf99e81ec16b"><ac:parameter ac:name="id">1276634702</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="3f767494-e1fd-4dd3-a28e-d74ed34952ee"><ac:parameter ac:name="id">1276634704</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="555e79f6-6ced-416e-9dc0-68acb862e5f8"><ac:parameter ac:name="id">1276634701</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="8876e9ef-4433-42eb-9a28-13b57941d9c9"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="084383ad-ae67-4fbd-81a6-c1d7e6ae46ad"><ac:parameter ac:name="id">1276634703</ac:parameter><ac:rich-text-body><p>The Cameo Data Modeler Plugin for MagicDraw provides import functionality for data models created using the CA ERwin® Data Modeler (henceforth will be referred as ERwin). ERwin is one of the leaders in the data modeling tools market.</p><p>Data models produced in ERwin have a two-layer structure, consisting of tightly synchronized logical and physical layers. The physical layer semantically corresponds to the SQL modeling / diagramming / generation functionality in MagicDraw. The logical layer corresponds to ER diagrams implemented by the Cameo Data Modeler Plugin.</p><p>The import functionality only imports logical layer data from ERwin into ER diagrams / data models in MagicDraw. The Cameo Data Modeler Plugin does not yet support importing physical layer data.</p><p><br /></p><h3>Importing data models</h3><p>Cameo Data Modeler supports model files produced in ERwin version 7.x. It is recommended that you use the newest v7.3 since it has been heavily tested. Data models in ERwin must be saved in the *.xml format (choose the <strong>XML Standard File </strong>option in the <strong>Save As </strong>dialog).</p><p><br /></p><p>To import an ERwin model</p><hr /><ol><li>Start MagicDraw.</li><li>Click <strong>File </strong>&gt; <strong>Import From </strong>&gt; <strong>CA ERwin Data Modeler v7.x</strong>. The <strong>Open file </strong>dialog will open.</li><li>Select an ERwin model file (*.xml). A new MagicDraw project will be created and a logical model will be imported from the ERwin model file into that project.</li></ol><p>After a successful import, you can proceed to edit or manage the model using MagicDraw features.</p><p>If you want to include the ER model as part of a larger project in MagicDraw, you can use either module linking functionality (click <strong>File </strong>&gt; <strong>Use Module</strong>) to attach the ER model to your main project model or project import functionality (click <strong>File </strong>&gt; <strong>Import From </strong>&gt; <strong>Another MagicDraw Project</strong>) to transfer the contents of this ER model to your main project model.</p><p>If you want to update an imported and edited ER model (for example, you made changes to the ERwin model and want to import those changes into MagicDraw again), you can use the merge functionality (click <strong>Tools </strong>&gt; <strong>Project Merge</strong>) to import the ERwin model into a new ER model and merge it with the model you have imported earlier.</p><p><br /></p><h3>Imported elements</h3><p>Import mapping reviews and notes are in the following table.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 13.4148%;" /><col style="width: 10.7423%;" /><col style="width: 75.8429%;" /></colgroup><tbody><tr><th><strong>ERwin</strong></th><th><p><strong>Cameo Data Modeler</strong></p></th><th>Comments</th></tr><tr><td>Any element</td><td>Any Element</td><td><ul><li>For each element, its name, definition, and notes are imported.</li><li>Definitions are imported as MagicDraw documentation (special UML comments). Notes are imported as UML comments.</li></ul></td></tr><tr><td>Entity</td><td>Entity</td><td><br /></td></tr><tr><td>Attribute</td><td>Attribute</td><td><ul><li>The <strong>Null </strong>/ <strong>Not Null </strong>setting is imported as UML multiplicities [0..1] / [1].</li><li>Attribute constraints and default value information is imported.</li><li>Domain information is not imported because domains are not supported.</li><li>Attribute type information is imported - the standard primitive types are mapped to the UML primitive types.</li><li>Other types (those not found in the model) are created on the fly.</li></ul></td></tr><tr><td>Key</td><td><p>Key Marking on Attributes</p></td><td><ul><li>There is no separate standalone model element for a key in the Cameo Data Modeler ER diagrams. Instead, attributes belonging to a key are marked by applying a stereotype to them (PK, AK, or IE) as necessary.</li></ul></td></tr><tr><td>Relationship</td><td>Association relationship</td><td><ul><li><p>Simple relationships are mapped to UML associations.</p></li><li><p>Verb phrases are mapped to role names.</p></li><li><p>Cardinality and null / not null settings are mapped to UML multiplicities ([0..1], [1], [0..*], [1..*]).</p></li><li><p>Referential integrity information is stored in a special stereotype / tag.</p></li><li><p>Key information is not imported since the current ER diagrams do not support FK modeling.</p></li></ul></td></tr><tr><td><br /></td><td>Generalization relationship</td><td><ul class="_mce_tagged_br"><li>ERwin relationships participating in the generalization tree are mapped to UML generalizations.</li><li>Generalizations are joined into generalization trees.</li><li>Complete / incomplete and overlapping / exclusive settings are imported / supported.</li><li>Discriminating columns are imported / supported.</li><li>Referential integrity information is stored in a special stereotype / tag.</li><li>Verb phrase information is not imported.</li></ul></td></tr><tr><td>Default Value</td><td><p>Instance Specification</p></td><td><ul><li>A standalone UML instance specification is created to hold value definition. This instance specification is (or can be) then referenced from attributes, default value fields.</li></ul></td></tr><tr><td>Domain</td><td>-</td><td><ul><li><p>Domains are not yet supported in Cameo Data Modeler.</p></li></ul></td></tr><tr><td>Validation Rule</td><td>Constraint</td><td><ul><li>The Validation rule is stored as constraint body text.</li></ul></td></tr><tr><td>Display</td><td>ER diagram</td><td><ul><li>Due to geometric constraints and element size changes, the diagram layout will be slightly different.</li><li>Paths between elements can be re-routed.</li></ul></td></tr><tr><td>User Defined Properties Dictionary</td><td><p>Profile / Stereotypes / Tags</p></td><td><ul><li>A custom UML profile is created for the user's property definitions.</li></ul></td></tr><tr><td><p>User Defined Properties</p></td><td>Tag Values</td><td><ul><li>A custom profile generated from the UDP dictionary is applied and user property information is stored in the tag values of the applied custom stereotypes.</li></ul></td></tr></tbody></table></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459956 space=CDMP2024xR1 version=5 -->
## PAGE 00035: Include

- page_id: `170459956`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459956/Include
- version_number: 5
- version_date: `2024-05-08T14:27:51.464+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Component with the stereotype XSDinclude. This component must be added into an xsd file component.

- annotation maps to the UML Component documentation
- schemaLocation maps to the UML Component name.

#### PANEL: include XML representation summary

include XML representation summary

```text
<include
```

```text
id = ID
```

```text
schemaLocation = anyURI
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</include>
```

###### [IMAGE alt='' src='']

###### include UML model example.

#### PANEL: include XML code sample

include XML code sample

```text
<xs:schema xmlns:nm = "http://nomagic.com" xmlns:xs = "http://www.w3.org/2001/XMLSchema" targetNamespace = "http://nomagic.com">	<xs:include schemaLocation = "http://nomagic.com/schema.xsd" /></xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Component with the stereotype XSDinclude. This component must be added into an xsd file component.</p><ul><li>annotation maps to the UML Component documentation</li><li style="text-align: left;">schemaLocation maps to the UML Component name.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b6d9ae78-cc28-4cc5-86c8-719fdbca0786"><ac:parameter ac:name="title">include XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;include</pre><pre>	id = ID</pre><pre>	schemaLocation = anyURI</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/include&gt;</pre></ac:rich-text-body></ac:structured-macro><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 141 include UML Model Example.png" /></ac:image></h6><h6 style="text-align: center;">include UML model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="779f4f21-1657-4460-80c3-5d6151cec40c"><ac:parameter ac:name="title">include XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot;&gt;<br />	&lt;xs:include schemaLocation = &quot;<a href="http://nomagic.com/schema.xsd">http://nomagic.com/schema.xsd</a>&quot; /&gt;<br />&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459695 space=CDMP2024xR1 version=7 -->
## PAGE 00036: Installation, licensing, and system requirements

- page_id: `170459695`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459695/Installation+licensing+and+system+requirements
- version_number: 7
- version_date: `2024-05-08T13:14:33.159+02:00`
- ancestors: Cameo Data Modeler Plugin
- labels: []

### NORMALIZED CONTENT

738643392

738643394

738643393

For information regarding installation, licensing, and system requirements, visit the [CONFLUENCE_PAGE title='Installation, Licensing, and System Requirements Documentation' space='IL2024xR1'] page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="923d002d-ee16-47ea-b6f9-a12215375fb1"><ac:parameter ac:name="id">738643392</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4fda1575-39ea-47f2-874e-ab0672249077"><ac:parameter ac:name="id">738643394</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="43a005b7-8bd9-4bfc-bb91-436e523467e3"><ac:parameter ac:name="id">738643393</ac:parameter><ac:rich-text-body><p class="with-breadcrumbs">For information regarding installation, licensing, and system requirements, visit the <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Installation, Licensing, and System Requirements Documentation" /><ac:plain-text-link-body><![CDATA[Installation, licensing, and system requirements]]></ac:plain-text-link-body></ac:link> page.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459903 space=CDMP2024xR1 version=5 -->
## PAGE 00037: Key

- page_id: `170459903`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459903/Key
- version_number: 5
- version_date: `2024-05-08T14:24:03.535+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute added into some UML Class.

- name – to Attribute name.
- id – to TaggedValue.

#### PANEL: key mapping to UML attributes

key mapping to UML attributes

```text
<key
```

```text
id = ID
```

```text
name = NCName
```

```text
{any attributes with non-schema namespace …}>	Content: (annotation?, (selector, field+))
```

```text
</key>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute added into some UML Class.</p><ul><li>name – to Attribute name.</li><li>id – to TaggedValue.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="8433f545-5a95-4cd5-be9f-2b27c9e769db"><ac:parameter ac:name="title">key mapping to UML attributes</ac:parameter><ac:rich-text-body><pre>&lt;key</pre><pre>	id = ID</pre><pre>	name = NCName </pre><pre>	{any attributes with non-schema namespace …}&gt;<br />	Content: (annotation?, (selector, field+))</pre><pre>&lt;/key&gt;</pre></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=170459730 space=CDMP2024xR1 version=6 -->
## PAGE 00038: Key modeling

- page_id: `170459730`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459730/Key+modeling
- version_number: 6
- version_date: `2024-05-08T13:45:13.225+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Entity-relationship (ER) modeling and diagrams
- labels: []

### NORMALIZED CONTENT

Entity keys are marked by applying the corresponding stereotype («PrimaryKey», «AlternativeKey») on the necessary column(s). This can be done from the column's shortcut menu.

[IMAGE alt='' src='']

###### Example of key usage in an ER diagram.

Primary key columns are grouped into a separate compartment. When the «PrimaryKey» stereotype is applied / unapplied, the column migrates between the two compartments.

In rare cases, you may need to specify several alternative keys on the same entry. In this case, you will fill the “Id” tag field of the key column with key identifier(s). Columns with the same Id are considered to belong to the same key. Overlapping alternative keys can be specified in the same manner (a column can have several ids specified).

[IMAGE alt='' src='']

###### Example of multiple overlapping alternative keys in ER diagram.

Inversion entries are specified analogously. An inversion entry is a non-unique (combination of) column(s), frequently used to search for the entity. Marking columns as IE provides hints to database implementers about which indexes to specify.

[IMAGE alt='' src='']

###### Example of inversion entry in ER diagram.

#### NOTE: Note

Note

Although an ER profile carries the «ForeignKey» stereotype, this stereotype is currently unused. It is reserved for future automatic foreign key derivation functionality. Users should not specify FK columns explicitly on their entities (FKs are implied), unless they are needed for a specific purpose. **Use at your own risk.**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Entity keys are marked by applying the corresponding stereotype («PrimaryKey», «AlternativeKey») on the necessary column(s). This can be done from the column's shortcut menu.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 10 Key Usage in ER Diagram.png" /></ac:image></p><h6 style="text-align: center;">Example of key usage in an ER diagram.</h6><p><br /></p><p>Primary key columns are grouped into a separate compartment. When the «PrimaryKey» stereotype is applied / unapplied, the column migrates between the two compartments.</p><p>In rare cases, you may need to specify several alternative keys on the same entry. In this case, you will fill the “Id” tag field of the key column with key identifier(s). Columns with the same Id are considered to belong to the same key. Overlapping alternative keys can be specified in the same manner (a column can have several ids specified).</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 11 Multiple Overlapping Alternative Keys in ER Diagram.png" /></ac:image></p><h6 style="text-align: center;">Example of multiple overlapping alternative keys in ER diagram.</h6><p><br /></p><p>Inversion entries are specified analogously. An inversion entry is a non-unique (combination of) column(s), frequently used to search for the entity. Marking columns as IE provides hints to database implementers about which indexes to specify.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 12 Inversion Entry in ER Diagram.png" /></ac:image></p><h6 style="text-align: center;">Example of inversion entry in ER diagram.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="67f2233a-7aab-41d3-9e3e-d75cb289e155"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>Although an ER profile carries the «ForeignKey» stereotype, this stereotype is currently unused. It is reserved for future automatic foreign key derivation functionality. Users should not specify FK columns explicitly on their entities (FKs are implied), unless they are needed for a specific purpose. <strong>Use at your own risk.</strong></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459799 space=CDMP2024xR1 version=5 -->
## PAGE 00039: Key transformation

- page_id: `170459799`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459799/Key+transformation
- version_number: 5
- version_date: `2024-05-08T14:03:01.571+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Transformations > ER to SQL (generic / Oracle) transformations
- labels: []

### NORMALIZED CONTENT

Keys in ER models are transformed into constraints in a DDL model. These are the rules for key transformations into DDL constraints as follows.

1. The Primary key of the entity in the ER model is transformed into a primary key constraint in the SQL model.
2. The Alternative keys of the entities in the ER model are transformed into unique constraints in the SQL model.
3. The Inversion entries of the entities in the ER model are transformed into indexes in the SQL model.
4. If key or entry in ER model has a name ( identifier tag), this information is preserved in the SQL model. The corresponding key / index will also have a name in the SQL model.

Let's review an example of key modeling, which has been described in [CONFLUENCE_PAGE title='Key modeling' space='']. After the transformation, the three entities of the ER model are transformed into the three tables of the SQL model respectively.

[IMAGE alt='' src='']

###### TBD screenshot example of key transformation results.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Keys in ER models are transformed into constraints in a DDL model. These are the rules for key transformations into DDL constraints as follows.</p><ol><li>The Primary key of the entity in the ER model is transformed into a primary key constraint in the SQL model.</li><li>The Alternative keys of the entities in the ER model are transformed into unique constraints in the SQL model.</li><li>The Inversion entries of the entities in the ER model are transformed into indexes in the SQL model.</li><li>If key or entry in ER model has a name (<strong>identifier </strong>tag), this information is preserved in the SQL model. The corresponding key / index will also have a name in the SQL model.</li></ol><p>Let's review an example of key modeling, which has been described in <ac:link><ri:page ri:content-title="Key modeling" /></ac:link>. After the transformation, the three entities of the ER model are transformed into the three tables of the SQL model respectively.</p><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 41 TBD Screenshot Example of Key Transformation Results.png" /></ac:image></p><h6 style="text-align: center;">TBD screenshot example of key transformation results.</h6>
````

<!--NOMAGIC_PAGE id=170459905 space=CDMP2024xR1 version=5 -->
## PAGE 00040: Keyref

- page_id: `170459905`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459905/Keyref
- version_number: 5
- version_date: `2024-05-08T14:24:14.220+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute added into some UML Class.

- refer – to value of “refer” or “referString” TaggedValue.
- name – to Attribute name.
- id – to TaggedValue.

#### PANEL: keyref Mapping to UML attributes

keyref Mapping to UML attributes

```text
<keyref
```

```text
id = ID
```

```text
name = NCName	refer = OName 	{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, (selector, field+))
```

```text
</keyref>
```

[IMAGE alt='' src='']

###### keyref UML model example.

#### PANEL: keyref XML code sample

keyref XML code sample

```text
<xs:schema xmlns:nm = "http://nomagic.com" xmlns:xs = "http://www.w3.org/2001/XMLSchema" targetNamespace = "http://nomagic.com" >	<xs:element name = "vehicle">
```

```text
<xs:complexType>			<xs:all />
```

```text
<xs:attribute name = "plateNumber" type = "xs:integer" />			<xs:attribute name = "state" type = "nm:twoLetterCode" />
```

```text
</xs:complexType>
```

```text
</xs:element>
```

```text
<xs:element name = "state">
```

```text
<xs:complexType>
```

```text
<xs:sequence>
```

```text
<xs:element name = "code" type = "nm:twoLetterCode" /›				<xs:element ref = "nm:vehicle" maxOccurs = "unbounded" />
```

```text
<xs:element ref = "nm:person" maxOccurs = "unbounded" />
```

```text
</xs:sequence>		</xs:complexType>
```

```text
<xs:unique name = "reg" >
```

```text
<xs:annotation >
```

```text
<xs:documentation>unique documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
<xs:selector xpath = ".//vehicle" />
```

```text
<xs:field xpath = "@plateNumber" />
```

```text
</xs:unique>
```

```text
</xs:element>
```

```text
<xs:element name = "person">  		<xs:complexType>
```

```text
<xs:sequence>
```

```text
<xs:element name = "car">
```

```text
<xs:complexType>
```

```text
<xs:sequence />
```

```text
<xs:attribute name "regPlate" type = "xs:integer" />
```

```text
<xs:attribute name = "regState" type = "nm:twoLetterCode" />
```

```text
</xs:complexType>
```

```text
</xs:element>
```

```text
</xs:sequence>		</xs:complexType>
```

```text
</xs:element>
```

```text
<xs:element name = "root">  		<xs:complexType>
```

```text
<xs:sequence>				<xs:element ref = "nm:state" maxOccurs = "unbounded" />
```

```text
</xs:sequence>		</xs:complexType>
```

```text
<xs:key name = "state" >
```

```text
<xs:selector xpath = ".//state" />
```

```text
<xs:field xpath = "code"
```

```text
</xs:key>
```

```text
<xs:keyref name = "vehicleState" refer = "nm:state" >			<xs:selector xpath = ".//vehicle" />
```

```text
<xs:field xpath = "@state" />
```

```text
</xs:keyref>
```

```text
<xs:key name = "regKey">			<xs:annotation>
```

```text
<xs:documentation>key documentation</xs:documentation>			</xs:annotation>			<xs:selector xpath = ".//vehicle" />
```

```text
<xs:field xpath = "@state" />
```

```text
<xs:field xpath = "@plateNumber" />
```

```text
</xs:key>
```

```text
<xs:keyref name = "carRef" refer = "nm:regKey">
```

```text
<xs:annotation>				<xs:documentation>key ref documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
<xs:selector xpath = ".//car" />  			<xs:field xpath = "@regState" />  			<xs:field xpath = "@regPlate" />
```

```text
</xs:keyref>
```

```text
</xs:element>
```

```text
<xs:simpleType name = "twoLetterCode">		<xs:restriction base = "xs:string" />	</xs:simpleType>
```

```text
</xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute added into some UML Class.</p><ul><li>refer – to value of “refer” or “referString” TaggedValue.</li><li>name – to Attribute name.</li><li>id – to TaggedValue.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3f484fb0-38e9-4e6d-b08c-1033432f2da4"><ac:parameter ac:name="title">keyref Mapping to UML attributes</ac:parameter><ac:rich-text-body><pre>&lt;keyref</pre><pre>	id = ID</pre><pre>	name = NCName<br />	refer = OName <br />	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, (selector, field+))</pre><pre>&lt;/keyref&gt;</pre></ac:rich-text-body></ac:structured-macro><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 101 keyref UML Model Example 1.png" /></ac:image></p><h6 style="text-align: center;">keyref UML model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="75a7974a-210f-4db6-a320-e1d719fa6097"><ac:parameter ac:name="title">keyref XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; &gt;<br />	&lt;xs:element name = &quot;vehicle&quot;&gt;</pre><pre>		&lt;xs:complexType&gt;<br />			&lt;xs:all /&gt;</pre><pre>			&lt;xs:attribute name = &quot;plateNumber&quot; type = &quot;xs:integer&quot; /&gt;<br />			&lt;xs:attribute name = &quot;state&quot; type = &quot;nm:twoLetterCode&quot; /&gt;</pre><pre>		&lt;/xs:complexType&gt;</pre><pre>	&lt;/xs:element&gt;</pre><pre>	&lt;xs:element name = &quot;state&quot;&gt;</pre><pre>		&lt;xs:complexType&gt;</pre><pre>			&lt;xs:sequence&gt;</pre><pre>				&lt;xs:element name = &quot;code&quot; type = &quot;nm:twoLetterCode&quot; /›<br />				&lt;xs:element ref = &quot;nm:vehicle&quot; maxOccurs = &quot;unbounded&quot; /&gt;</pre><pre>				&lt;xs:element ref = &quot;nm:person&quot; maxOccurs = &quot;unbounded&quot; /&gt;</pre><pre>			&lt;/xs:sequence&gt;<br />		&lt;/xs:complexType&gt;</pre><pre>		&lt;xs:unique name = &quot;reg&quot; &gt;</pre><pre>			&lt;xs:annotation &gt;</pre><pre>				&lt;xs:documentation&gt;unique documentation&lt;/xs:documentation&gt;</pre><pre>			&lt;/xs:annotation&gt;</pre><pre>			&lt;xs:selector xpath = &quot;.//vehicle&quot; /&gt;</pre><pre>			&lt;xs:field xpath = &quot;@plateNumber&quot; /&gt;</pre><pre>		&lt;/xs:unique&gt;</pre><pre>	&lt;/xs:element&gt;</pre><pre>	&lt;xs:element name = &quot;person&quot;&gt; <br /> 		&lt;xs:complexType&gt;</pre><pre>			&lt;xs:sequence&gt;</pre><pre>				&lt;xs:element name = &quot;car&quot;&gt;</pre><pre>					&lt;xs:complexType&gt;</pre><pre>						&lt;xs:sequence /&gt;</pre><pre>						&lt;xs:attribute name &quot;regPlate&quot; type = &quot;xs:integer&quot; /&gt;</pre><pre>						&lt;xs:attribute name = &quot;regState&quot; type = &quot;nm:twoLetterCode&quot; /&gt;</pre><pre>					&lt;/xs:complexType&gt;</pre><pre>				&lt;/xs:element&gt;</pre><pre>			&lt;/xs:sequence&gt;<br />		&lt;/xs:complexType&gt;</pre><pre>	&lt;/xs:element&gt;</pre><pre>	&lt;xs:element name = &quot;root&quot;&gt; <br /> 		&lt;xs:complexType&gt;</pre><pre>			&lt;xs:sequence&gt;<br />				&lt;xs:element ref = &quot;nm:state&quot; maxOccurs = &quot;unbounded&quot; /&gt;</pre><pre>			&lt;/xs:sequence&gt;<br />		&lt;/xs:complexType&gt;</pre><pre>		&lt;xs:key name = &quot;state&quot; &gt;</pre><pre>			&lt;xs:selector xpath = &quot;.//state&quot; /&gt;</pre><pre>			&lt;xs:field xpath = &quot;code&quot;</pre><pre>		&lt;/xs:key&gt;</pre><pre>		&lt;xs:keyref name = &quot;vehicleState&quot; refer = &quot;nm:state&quot; &gt;<br />			&lt;xs:selector xpath = &quot;.//vehicle&quot; /&gt;</pre><pre>			&lt;xs:field xpath = &quot;@state&quot; /&gt;</pre><pre>		&lt;/xs:keyref&gt;</pre><pre>		&lt;xs:key name = &quot;regKey&quot;&gt;<br />			&lt;xs:annotation&gt;</pre><pre>				&lt;xs:documentation&gt;key documentation&lt;/xs:documentation&gt;<br />			&lt;/xs:annotation&gt;<br />			&lt;xs:selector xpath = &quot;.//vehicle&quot; /&gt;</pre><pre>			&lt;xs:field xpath = &quot;@state&quot; /&gt;</pre><pre>			&lt;xs:field xpath = &quot;@plateNumber&quot; /&gt;</pre><pre>		&lt;/xs:key&gt;</pre><pre>		&lt;xs:keyref name = &quot;carRef&quot; refer = &quot;nm:regKey&quot;&gt;</pre><pre>			&lt;xs:annotation&gt;<br />				&lt;xs:documentation&gt;key ref documentation&lt;/xs:documentation&gt;</pre><pre>			&lt;/xs:annotation&gt;</pre><pre>			&lt;xs:selector xpath = &quot;.//car&quot; /&gt; <br /> 			&lt;xs:field xpath = &quot;@regState&quot; /&gt; <br /> 			&lt;xs:field xpath = &quot;@regPlate&quot; /&gt;</pre><pre>		&lt;/xs:keyref&gt;</pre><pre>	&lt;/xs:element&gt;</pre><pre>	&lt;xs:simpleType name = &quot;twoLetterCode&quot;&gt;<br />		&lt;xs:restriction base = &quot;xs:string&quot; /&gt;<br />	&lt;/xs:simpleType&gt;</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459883 space=CDMP2024xR1 version=1 -->
## PAGE 00041: Length

- page_id: `170459883`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459883/Length
- version_number: 1
- version_date: `2023-09-21T12:47:02.155+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDlength. The name and type of such an attribute do not make sense.

- value – to Attribute initial value.

#### PANEL: Length XML representation summary

Length XML representation summary

```text
<length
```

```text
fixed = boolean : false
```

```text
id = ID
```

```text
value = nonNegativeInteger
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</length>
```

#### PANEL: Length XML code sample

Length XML code sample

```text
The following is the definition of a user-derived datatype to represent product codes which must be exactly 8 characters in length. By fixing the value of the length facet, we ensure that the type derived from productCode can change or set the values of other facets, such as pattern, but cannot change the length.
```

```text
<simpleType name= 'productCode' >
```

```text
<restriction base='string'>
```

```text
<length value='8' fixed='true'/>
```

```text
</restriction>
```

```text
</simpleType>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDlength. The name and type of such an attribute do not make sense.</p><ul><li style="text-align: left;">value – to Attribute initial value.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="2e7c356e-473c-4395-bd83-6ba97779be72"><ac:parameter ac:name="title">Length XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;length</pre><pre>	fixed = boolean : false</pre><pre>	id = ID</pre><pre>	value = nonNegativeInteger</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/length&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9cda1f73-6de9-46b6-9a92-2b5e35c34640"><ac:parameter ac:name="title"> Length XML code sample</ac:parameter><ac:rich-text-body><pre>The following is the definition of a user-derived datatype to represent product codes which must be exactly 8 characters in length. <br />By fixing the value of the length facet, we ensure that the type derived from productCode can change or set the values of other facets, <br />such as pattern, but cannot change the length.<br /><br /></pre><pre>&lt;simpleType name= 'productCode' &gt;</pre><pre>	&lt;restriction base='string'&gt;</pre><pre>		&lt;length value='8' fixed='true'/&gt;</pre><pre>	&lt;/restriction&gt;</pre><pre>&lt;/simpleType&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459858 space=CDMP2024xR1 version=5 -->
## PAGE 00042: List

- page_id: `170459858`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459858/List
- version_number: 5
- version_date: `2024-05-08T14:21:52.933+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

- The UML Class must have the additional stereotype XSDlist.
- Binding between this class and XSD:list must be provided.
- “itemsType” maps to UML TemplateArgument from Binding.

[IMAGE alt='' src='']

###### List model example.

#### PANEL: List XML code sample

List XML code sample

```text
<?xml version=1.0, encoding=’UTF-8’?›
```

```text
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">	<xs:simpleType name="my_number_list2" >
```

```text
<xs:list >
```

```text
<xs:simpleType>
```

```text
<xs:restriction base="xs:string" />			</xs:simpleType›
```

```text
</xs:list>
```

```text
</xs:simpleType>
```

```text
<xs:simpleType name="my_number_list" >		<xs:annotation >
```

```text
<xs:documentation >my list documentation</xs:documentation>		</xs:annotation>
```

```text
<xs:list itemType="xs:boolean" />
```

```text
</xs:simpleType>
```

```text
</xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ul><li>The UML Class must have the additional stereotype XSDlist.</li><li>Binding between this class and XSD:list must be provided.</li><li>“itemsType” maps to UML TemplateArgument from Binding.</li></ul><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 71 List Example Model.png" /></ac:image></p><h6 style="text-align: center;">List model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="bf178920-bb72-431d-b746-65e3b26b324b"><ac:parameter ac:name="title">List XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;?xml version=1.0, encoding=’UTF-8’?›</pre><pre>&lt;xs:schema xmlns:xs=&quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot;&gt;<br />	&lt;xs:simpleType name=&quot;my_number_list2&quot; &gt;</pre><pre>		&lt;xs:list &gt;</pre><pre>			&lt;xs:simpleType&gt;</pre><pre>				&lt;xs:restriction base=&quot;xs:string&quot; /&gt;<br />			&lt;/xs:simpleType›</pre><pre>		&lt;/xs:list&gt;</pre><pre>	&lt;/xs:simpleType&gt;</pre><pre>	&lt;xs:simpleType name=&quot;my_number_list&quot; &gt;<br />		&lt;xs:annotation &gt;</pre><pre>			&lt;xs:documentation &gt;my list documentation&lt;/xs:documentation&gt;<br />		&lt;/xs:annotation&gt;</pre><pre>		&lt;xs:list itemType=&quot;xs:boolean&quot; /&gt;</pre><pre>	&lt;/xs:simpleType&gt;</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459868 space=CDMP2024xR1 version=1 -->
## PAGE 00043: MaxExclusive

- page_id: `170459868`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459868/MaxExclusive
- version_number: 1
- version_date: `2023-09-21T12:47:01.318+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDmaxExclusive. The name and type of such an attribute do not make sense.

- value – to Attribute initial value.

#### PANEL: maxExclusive XML representation summary

maxExclusive XML representation summary

```text
<maxExclusive
```

```text
fixed = boolean : false
```

```text
id = ID
```

```text
value = anySimpleType
```

```text
{any attributes with non-schema namespace…}>	Content: (annotation?)
```

```text
</maxExclusive>
```

```text
{value} must be in the value space of {base type definition}.
```

#### PANEL: maxExclusive XML code sample

maxExclusive XML code sample

```text
The following is the definition of a user-derived datatype which limits values to integers less than or equal to 100, using maxExclusive.
```

```text
<simpleType name='less-than-one-hundred-and-one'›
```

```text
<restriction base='integer'›
```

```text
<maxExclusive value='101'/>
```

```text
</restriction>
```

```text
</simpleType›
```

```text
Note that the value space of this datatype is identical to the previous one (named 'one­-hundred-or-less').
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDmaxExclusive. The name and type of such an attribute do not make sense.</p><ul><li><p style="text-align: left;">value – to Attribute initial value.</p></li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="83aad944-9d58-4426-85b6-ffac3d86b496"><ac:parameter ac:name="title">maxExclusive XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;maxExclusive</pre><pre>	fixed = boolean : false</pre><pre>	id = ID</pre><pre>	value = anySimpleType</pre><pre>	{any attributes with non-schema namespace…}&gt;<br />	Content: (annotation?)</pre><pre>&lt;/maxExclusive&gt;</pre><pre>{value} must be in the value space of {base type definition}. </pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="d355d9c1-f918-4935-bd31-d9dd88c74e0f"><ac:parameter ac:name="title">maxExclusive XML code sample</ac:parameter><ac:rich-text-body><pre>The following is the definition of a user-derived datatype which limits values to integers less than or equal to 100, using maxExclusive.</pre><pre>&lt;simpleType name='less-than-one-hundred-and-one'›</pre><pre>	&lt;restriction base='integer'›</pre><pre>		&lt;maxExclusive value='101'/&gt;</pre><pre>	&lt;/restriction&gt;</pre><pre>&lt;/simpleType›</pre><pre>Note that the value space of this datatype is identical to the previous one (named 'one­-hundred-or-less').</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459874 space=CDMP2024xR1 version=1 -->
## PAGE 00044: MaxInclusive

- page_id: `170459874`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459874/MaxInclusive
- version_number: 1
- version_date: `2023-09-21T12:47:01.658+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDmaxInclusive. The name and type of such an attribute do not make sense.

- value – to Attribute initial value.

#### PANEL: maxInclusive XML representation summary

maxInclusive XML representation summary

```text
<maxInclusive
```

```text
fixed = boolean:false
```

```text
id = ID
```

```text
value = anySimpleType
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (Annotation?)
```

```text
</maxInclusive>
```

```text
{value} must be in the value space of {base type definition}.
```

#### PANEL: maxInclusive XML code sample.

maxInclusive XML code sample.

```text
The following is the definition of a user-derived datatype which limits values to integers less than or equal to 100,using maxInclusive.
```

```text
<simpleType name='one-hundred-or-less'>
```

```text
<restriction base='integer'>
```

```text
<maxInclusive value='100'/>
```

```text
</restriction>
```

```text
</simpleType>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDmaxInclusive. The name and type of such an attribute do not make sense.</p><ul><li>value – to Attribute initial value.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="4189b8e6-4c85-49be-baa5-d3c13be2b17a"><ac:parameter ac:name="title">maxInclusive XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;maxInclusive</pre><pre>	fixed = boolean:false</pre><pre>	id = ID</pre><pre>	value = anySimpleType</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (Annotation?)</pre><pre>&lt;/maxInclusive&gt;</pre><pre>{value} must be in the value space of {base type definition}. </pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="2f3e6e25-ea51-4cb6-b306-2f50da6ce9a6"><ac:parameter ac:name="title">maxInclusive XML code sample.</ac:parameter><ac:rich-text-body><pre>The following is the definition of a user-derived datatype which limits values to integers less than or equal to 100,<br />using maxInclusive.<br /><br /></pre><pre>&lt;simpleType name='one-hundred-or-less'&gt;</pre><pre>	&lt;restriction base='integer'&gt;</pre><pre>		&lt;maxInclusive value='100'/&gt;</pre><pre>	&lt;/restriction&gt;</pre><pre>&lt;/simpleType&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459889 space=CDMP2024xR1 version=1 -->
## PAGE 00045: MaxLength

- page_id: `170459889`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459889/MaxLength
- version_number: 1
- version_date: `2023-09-21T12:47:02.436+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDmaxLength. The name and type of such an attribute do not make sense.

- value – to Attribute initial value.

#### PANEL: maxLength XML representation summary

maxLength XML representation summary

```text
<maxLength
```

```text
fixed = boolean : false
```

```text
id = ID
```

```text
value = nonNegativeInteger
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</maxLength>
```

#### PANEL: maxLength XML code sample

maxLength XML code sample

```text
The following is the definition of a user-derived datatype which might be used to accept form input with an upper limit to the number of characters that are acceptable.<simpleType name='form-input'>	<restriction base='string'>		<maxLength value='50'/>	</restriction></simpleType>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDmaxLength. The name and type of such an attribute do not make sense.</p><ul><li style="text-align: left;">value – to Attribute initial value.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="67580705-52b0-4224-b7e8-d0318da36137"><ac:parameter ac:name="title">maxLength XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;maxLength</pre><pre>	fixed = boolean : false</pre><pre>	id = ID</pre><pre>	value = nonNegativeInteger</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/maxLength&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="87dbf8d0-599d-4de1-8ed6-441752537c61"><ac:parameter ac:name="title">maxLength XML code sample</ac:parameter><ac:rich-text-body><pre>The following is the definition of a user-derived datatype which might be used to accept form input with an upper limit to the number <br />of characters that are acceptable.<br /><br />&lt;simpleType name='form-input'&gt;<br />	&lt;restriction base='string'&gt;<br />		&lt;maxLength value='50'/&gt;<br />	&lt;/restriction&gt;<br />&lt;/simpleType&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459864 space=CDMP2024xR1 version=1 -->
## PAGE 00046: MinExclusive

- page_id: `170459864`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459864/MinExclusive
- version_number: 1
- version_date: `2023-09-21T12:47:01.127+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDminExclusive. The name and type of such an attribute do not make sense.

- value – to Attribute initial value.

#### PANEL: minExclusive XML representation summary

minExclusive XML representation summary

```text
<minExclusive
```

```text
fixed = boolean : false
```

```text
id = ID
```

```text
value = anySimpleType
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</minExclusive>
```

```text
{value} must be in the value space of {base type definition}.
```

#### PANEL: minExclusive XML code sample

minExclusive XML code sample

```text
The following is the definition of a user-derived datatype which limits values to integers greater than or equal to 100, using minExclusive.
```

```text
<simpleType name= 'more- than-ninety-nine'>
```

```text
<restriction base= 'integer'>		<minExclusive value= '99'/>	</restriction>
```

```text
</simpleType>
```

```text
Note that the value space of this datatype is identical to the previous one (named 'one-­hundred-or-more').
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDminExclusive. The name and type of such an attribute do not make sense.</p><ul><li>value – to Attribute initial value.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="13a246b5-bcac-4403-9805-e8e403e1da8f"><ac:parameter ac:name="title">minExclusive XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;minExclusive</pre><pre>	fixed = boolean : false</pre><pre>	id = ID</pre><pre>	value = anySimpleType</pre><pre>	{any attributes with non-schema namespace…}&gt; </pre><pre>	Content: (annotation?)</pre><pre>&lt;/minExclusive&gt;</pre><pre>{value} must be in the value space of {base type definition}.</pre></ac:rich-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="20e78d56-b4c3-431c-879c-f31c5d2b56c4"><ac:parameter ac:name="title">minExclusive XML code sample</ac:parameter><ac:rich-text-body><pre>The following is the definition of a user-derived datatype which limits values to integers greater than or equal to 100, using minExclusive.</pre><pre>&lt;simpleType name= 'more- than-ninety-nine'&gt;</pre><pre>	&lt;restriction base= 'integer'&gt;<br />		&lt;minExclusive value= '99'/&gt;<br />	&lt;/restriction&gt;</pre><pre>&lt;/simpleType&gt;</pre><pre>Note that the value space of this datatype is identical to the previous one (named 'one-­hundred-or-more').</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459871 space=CDMP2024xR1 version=1 -->
## PAGE 00047: MinInclusive

- page_id: `170459871`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459871/MinInclusive
- version_number: 1
- version_date: `2023-09-21T12:47:01.464+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDminInclusive. The name and type of such an attribute do not make sense.

- value – to Attribute initial value.

#### PANEL: minInclusive XML representation summary

minInclusive XML representation summary

```text
<minInclusive
```

```text
fixed = boolean : false
```

```text
id = ID
```

```text
value = anySimpleType
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</minInclusive>
```

```text
{value} must be in the value space of {base type definition}.
```

#### PANEL: minInclusive XML code sample

minInclusive XML code sample

```text
The following is the definition of a user-derived datatype which limits values to integers greater than or equal to 100, using minInclusive.
```

```text
<simpleType name='one-hundred-or-more'>
```

```text
<restriction base='integer'>
```

```text
<minInclusive value='100'/>
```

```text
</restriction>
```

```text
</simpleType>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDminInclusive. The name and type of such an attribute do not make sense.</p><ul><li>value – to Attribute initial value.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="6ac49131-0401-40c3-98b4-f899fa8a3730"><ac:parameter ac:name="title">minInclusive XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;minInclusive</pre><pre>	fixed = boolean : false</pre><pre>	id = ID</pre><pre>	value = anySimpleType</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/minInclusive&gt;</pre><pre>{value} <a>must be</a> in the value space of {base type definition}.</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9d4aef4f-7050-4297-a905-4a3a5ad27080"><ac:parameter ac:name="title">minInclusive XML code sample</ac:parameter><ac:rich-text-body><pre>The following is the definition of a user-derived datatype which limits values to integers greater than or equal to 100, using minInclusive.</pre><pre>&lt;simpleType name='one-hundred-or-more'&gt;</pre><pre>	&lt;restriction base='integer'&gt;</pre><pre>		&lt;minInclusive value='100'/&gt;</pre><pre>	&lt;/restriction&gt;</pre><pre>&lt;/simpleType&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459886 space=CDMP2024xR1 version=1 -->
## PAGE 00048: MinLength

- page_id: `170459886`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459886/MinLength
- version_number: 1
- version_date: `2023-09-21T12:47:02.288+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDminLength. The name and type of such an attribute do not make sense.

- value – to Attribute initial value.

#### PANEL: minLength XML representation summary

minLength XML representation summary

```text
<minLength
```

```text
fixed = Boolean : false
```

```text
id = ID
```

```text
value = nonNegativeInteger
```

```text
{any attributes with non-schema namespace…}› 	Content: (annotation?)
```

```text
</minLength>
```

#### PANEL: minLength XML code sample

minLength XML code sample

```text
The following is the definition of a user-derived datatype which requires strings to have at least one character (i.e., the empty string is not in the value space of this datatype).
```

```text
<simpleType name='non-empty-string'›
```

```text
<restriction base='string'>
```

```text
<minLength value='1'/>
```

```text
</restriction>
```

```text
</simpleType›
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDminLength. The name and type of such an attribute do not make sense.</p><ul><li style="text-align: left;">value – to Attribute initial value.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b8b5045b-721c-4487-ab1a-c2bf73b03b33"><ac:parameter ac:name="title">minLength XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;minLength</pre><pre>	fixed = Boolean : false</pre><pre>	id = ID</pre><pre>	value = nonNegativeInteger</pre><pre>	{any attributes with non-schema namespace…}› <br />	Content: (annotation?)</pre><pre>&lt;/minLength&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="5ebeaf5f-7c50-44f1-b4f3-b58daa8c5a8c"><ac:parameter ac:name="title">minLength XML code sample</ac:parameter><ac:rich-text-body><pre>The following is the definition of a user-derived datatype which requires strings to have at least one character (i.e., the empty <br />string is not in the value space of this datatype).<br /><br /></pre><pre>&lt;simpleType name='non-empty-string'›</pre><pre>	&lt;restriction base='string'&gt;</pre><pre>		&lt;minLength value='1'/&gt;</pre><pre>	&lt;/restriction&gt;</pre><pre>&lt;/simpleType›</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459750 space=CDMP2024xR1 version=6 -->
## PAGE 00049: Modeling types

- page_id: `170459750`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459750/Modeling+types
- version_number: 6
- version_date: `2024-05-08T13:51:40.398+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support > Database modeling
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

56260855

#### CONTENT-COLUMN: Note

56260859

56260853

**On this page**

43

#### CONTENT-BLOCK: Note

56260857

Cameo Data Modeler provides the standard type libraries as well as ability to model user defined types (structured user defined types and composites - multiset, array data types). The types can then be used to specify columns of the tables and / or parameters of procedures and functions. There is also a special mechanism for using types with modifiers. This mechanism is common in the MagicDraw, however some explanation is necessary on how to use it in database modeling.

##### **Predefined type libraries**

Cameo Data Modeler provides predefined type libraries for database flavors it supports. Besides the standard SQL type library, there are type libraries for Oracle, DB2, MS SQL, MySQL, PostgreSQL, Sybase, Cloudscape (Derby), Pervasive, MS Access and Pointbase. The standard SQL type library is the main type library, and type libraries for each flavor import (a subset of) types from it and define additional types, specific for that flavor.

The necessary type library is imported when you create the Database or Schema element in your model and choose a flavor for it (See the Database flavor selection dialog in [CONFLUENCE_PAGE title='Top level elements' space='CDMP2024x']).

##### Type usage

[IMAGE alt='' src='']

###### Type specifying. Library type and modifier vs. separately modeled type.

Usage of a simple SQL type, such as **boolean**, is very simple. If you want to set it as a type of a column or operation parameter, you just need to specify it in the **type**field. However, there are types (such as **varchar**or **numeric**) in SQL, which require additional data. There are two mechanisms to specify these kinds of types: either use the library type+ type modifier mechanism or create your own type element.

Let's take the standard **varchar**type as an example. It must have the maximum length data provided at each usage. Semantically there are many different types, one for each length limit - **varchar(20)**, **varchar(53)**, **varchar(255)**etc. Now the standard type library cannot provide myriad of different **varchar**types. Library only provides the **varchar**type definition.

To specify that column is of **varchar(20)**

1. Set the type field of the column to varchar type from the library.
2. Set the type modifier field of the column to “ (20) ” (no quotes). Note that type modifier is a simple string - whatever is entered in this field, will be used in script generation verbatim, without additional checks. An example of more complex type modifier would be “ (10, 2) ” type modifier for numeric data type.

Alternative way to specify that column is of **varchar(20)**is to explicitly create a separate type in the model.

To specify that column is of varchar(20) in the alternative way

1. Create the necessary type (use one of the buttons in the SQL diagram, Primitive Types toolbar) - character string, fixed precision, integer, approximate, boolean, binary, date or XML types. In our case this would be character string type.
2. Set the length data in the dedicated tag (look up the length tag in the Tags section of the Specification window). Note that this is numeric field - you need to input number 20, and not the “(20)” string as was the case with type modifiers.
3. The name of your type can be whatever you like. For example, varchar_of_20 . The name is not important.
4. Inherit (draw generalization relationship) your type from the appropriate type from the type library. In this case, inherit varchar_of_20 from varchar form the library. This information will be used for determining the proper type name during script generation (Therefore, in the generated script, you will see the proper type reference - varchar(20) ).
5. This created type can now be specified in the type field of the column(s).

There would be one type in the model for each **varchar**length that you use in your database.

The second way is more tedious - you need to create quite a few types. Therefore, by default, the first way is used. But the second way has several advantages, that may outweigh it’s deficiencies. First - there is one spot where parameters of the type can be changed. You can easily widen the varchar(20) fields to varchar(40) by editing just one place in the model. Secondly, you can define some additional parameters of the type - such as character set.

##### **User defined types**

###### [IMAGE alt='' src='']

###### Examples of user defined types.

Besides the primitive / built-in types of the database, user can define additional types for his own schema.

###### Distinct type

#### NOTE: Note

Note

SQL Distinct type is modeled as UML DataType with «DistinctUserDe- finedType» stereotype applied. For the sake of compactness, refer- ences are displayed with the «distinct» keyword (instead of the long form - «DistinctUserDefinedType») on the diagram.

Distinct type definition allows to redefine some primitive type in order to enforce the non-assignability rules. For example, two distinct types **Meters**and **Yards**can be defined on the base primitive type **float**. With this definition, system would enforce checks that yard fields / columns are not assigned to meter fields / columns without a conversion (explicit cast).

Besides the standard SQL element properties, distinct type has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Predefined Representation | Points to some base primitive type. |

###### Domain

#### NOTE: Note

Note

SQL Domain is modeled as UML DataType with «Domain» stereotype applied. For the sake of compactness, domains are displayed with the «domain» keyword on the diagram.

Domain allows to define a more narrow set of values than the base primitive type allows. This narrowing is done by assigning additional constraints on the domain. Columns, whose types are set to the domain, can only assume values from this more narrow subset.

Besides the standard SQL element properties, domain has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Predefined Representation | Points to some base primitive type. |
| Default Value | Default value for the column if no value is specified. |

###### **Structured user defined type**

#### NOTE: Note

Note

SQL Structured User Defined Type is modeled as UML DataType with «StructuredUserDefinedType» stereotype applied. For the sake of com- pactness, domains are displayed with the «structured» keyword (instead of the long form - «StructuredUserDefinedType») on the diagram.

Structured UDT defines a composite datatype. Each value of this type is a tuple of several values; each position in a tuple has a name. Structured UDT value is analogous to one row of the table. Structured UDTs allow single inheritance (multiple inheritance is not supported). Inheritance (subtype-supertype relationship) can be modeled using UML Generalization relationships.

Besides the standard SQL element properties, structured UDT has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Instantiable | Defines |
| Final | Default value for the column if no value is specified. |
| Super | Shows base data types. This is a derived field, it is not editable. To make changes, use UML Generalization relationships. |

Parts of the structured UDT (properties) are called attributes (compare - parts of the table definition are called columns). Attributes of structured UDT are created like columns of the table, that is, via the **Attribute Definitions**tab in the structured UDT Specification window or using an appropriate smart manipulation button on its shape.

Besides the standard SQL element properties, attribute has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Type | Collectively these two fields describe the type of the attribute. The same considerations as for column type modeling apply. |
| Type Modifier |  |
| Default Value | Carries the default value of the attribute. |
| Scope Check | Marks this attribute as scope checked to a particular table and allows choosing particular referential integrity ensuring action (RESTRICT CASCADE, etc). |
| Scope Checked |  |

Besides attributes, Structured UDTs have a collection of methods - operations, performing actions on values of this type. Methods are covered in a separate section with stored procedures and functions (see [CONFLUENCE_PAGE title='Routines' space='CDMP2024x Refresh1 Refresh1 Refresh1R1'] section).

###### Array type

#### NOTE: Note

Note

SQL Array type is modeled as UML DataType with «ArrayDataType» stereotype applied. For the sake of compactness, arrays are displayed with the «array» keyword (instead of the long form - «ArrayDataType») on the diagram.

Array type defines an array (that is, list of values, with the indexed, O(1) access to the n-th element) of the values of elementary type. Besides the standard SQL element properties, array type has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Element | The elementary type of the set elements. |
| Max Cardinality | The size limit of the array. |

###### **Multiset type**

#### NOTE: Note

Note

SQL Multiset type is modeled as UML DataType with «MultisetDataType» stereotype applied. For the sake of compactness, multisets are displayed with the «multiset» keyword (instead of the long form - «MultisetDataType») on the diagram.

Multiset type defines a set of elements of the elementary type. Besides the standard SQL element properties, multiset has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Element | The elementary type of the set elements. |

###### **Reference types**

#### NOTE: Note

Note

SQL Reference type is modeled as UML DataType with «ReferenceDataType» stereotype applied. For the sake of compactness, references are displayed with the «ref» keyword (instead of the long form - «ReferenceDataType») on the diagram.

Reference type defines a pointer to the data of the referred type. Besides the standard SQL element properties, reference type has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Referenced Type | The type of the data that is being referenced. |
| Scope Table | Limit the references to the data of the particular table. |

###### Row type

#### NOTE: Note

Note

SQL Row Data Type is modeled as UML DataType with «RowDataType» stereotype applied. For the sake of compactness, row data types are displayed with the «row» keyword (instead of the long form - «RowDataType») on the diagram.

Represents one row of the table. The difference from structured UDT is that row type represents a value stored in the table, while structured UDT represents “free-floating” value during computation. For example, it is meaningful to take address for the row, but not of the structured UDT value.

Parts of the row data type (properties) are called fields (compare - parts of the table definition are called columns). Fields for row data type are created like columns of the table, that is, via the **Fields**tab in the row data type Specification window or using an appropriate smart manipulation button on its shape.

Besides the standard SQL element properties, field has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Type | Collectively these two fields describe the type of the field. The same considerations as for column type modeling apply. |
| Type Modifier |  |
| Scope Check | Marks this field as scope checked to a particular table and allows choosing particular referential integrity ensuring action (RESTRICT CASCADE, etc). |
| Scope Checked |  |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a1f0817c-38a1-48be-8825-722bae5311ee"><ac:parameter ac:name="id">56260855</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="2b8fb2f4-a026-49a9-b245-4fefb86290c1"><ac:parameter ac:name="id">56260859</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="08240a83-e2f4-4e19-a703-8fd5ba89e61b"><ac:parameter ac:name="id">56260853</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="aa0188f9-000b-4d62-91be-7fe4e1cb12e8"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0ea926e6-41aa-4026-b775-297cc4661cda"><ac:parameter ac:name="id">56260857</ac:parameter><ac:rich-text-body><p>Cameo Data Modeler provides the standard type libraries as well as ability to model user defined types (structured user defined types and composites - multiset, array data types). The types can then be used to specify columns of the tables and / or parameters of procedures and functions. There is also a special mechanism for using types with modifiers. This mechanism is common in the MagicDraw, however some explanation is necessary on how to use it in database modeling.</p><h3><strong>Predefined type libraries</strong></h3><p>Cameo Data Modeler provides predefined type libraries for database flavors it supports. Besides the standard SQL type library, there are type libraries for Oracle, DB2, MS SQL, MySQL, PostgreSQL, Sybase, Cloudscape (Derby), Pervasive, MS Access and Pointbase. The standard SQL type library is the main type library, and type libraries for each flavor import (a subset of) types from it and define additional types, specific for that flavor.</p><p>The necessary type library is imported when you create the Database or Schema element in your model and choose a flavor for it (See the Database flavor selection dialog in <ac:link><ri:page ri:space-key="CDMP2024x" ri:content-title="Top level elements" /></ac:link>).</p><h3>Type usage</h3><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 21 Type Specifying. Library Type and Modifier vs. Separately Modeled Type.png" /></ac:image></p><h6 style="text-align: center;">Type specifying. Library type and modifier vs. separately modeled type.</h6><p>Usage of a simple SQL type, such as <strong>boolean</strong>, is very simple. If you want to set it as a type of a column or operation parameter, you just need to specify it in the <strong>type </strong>field. However, there are types (such as <strong>varchar </strong>or <strong>numeric</strong>) in SQL, which require additional data. There are two mechanisms to specify these kinds of types: either use the library type+ type modifier mechanism or create your own type element.</p><p>Let's take the standard <strong>varchar </strong>type as an example. It must have the maximum length data provided at each usage. Semantically there are many different types, one for each length limit - <strong>varchar(20)</strong>, <strong>varchar(53)</strong>, <strong>varchar(255) </strong>etc. Now the standard type library cannot provide myriad of different <strong>varchar </strong>types. Library only provides the <strong>varchar </strong>type definition.</p><p><br /></p><p>To specify that column is of <strong>varchar(20)</strong></p><hr /><ol><li>Set the <strong>type </strong>field of the column to <strong>varchar </strong>type from the library.</li><li>Set the <strong>type modifier </strong>field of the column to “<strong>(20)</strong>” (no quotes). Note that type modifier is a simple string - whatever is entered in this field, will be used in script generation verbatim, without additional checks. An example of more complex type modifier would be “<strong>(10, 2)</strong>” type modifier for <strong>numeric </strong>data type.</li></ol><p>Alternative way to specify that column is of <strong>varchar(20) </strong>is to explicitly create a separate type in the model.</p><p><br /></p><p>To specify that column is of varchar(20) in the alternative way</p><hr /><ol><li>Create the necessary type (use one of the buttons in the SQL diagram, Primitive Types toolbar) - character string, fixed precision, integer, approximate, boolean, binary, date or XML types. In our case this would be character string type.</li><li>Set the length data in the dedicated tag (look up the <strong>length </strong>tag in the <strong>Tags </strong>section of the Specification window). Note that this is numeric field - you need to input number 20, and not the “(20)” string as was the case with type modifiers.</li><li>The name of your type can be whatever you like. For example, <strong>varchar_of_20</strong>. The name is not important.</li><li>Inherit (draw generalization relationship) your type from the appropriate type from the type library. In this case, inherit <strong>varchar_of_20 </strong>from <strong>varchar </strong>form the library. This information will be used for determining the proper type name during script generation (Therefore, in the generated script, you will see the proper type reference - <strong>varchar(20)</strong>).</li><li>This created type can now be specified in the <strong>type </strong>field of the column(s).</li></ol><p>There would be one type in the model for each <strong>varchar </strong>length that you use in your database.</p><p>The second way is more tedious - you need to create quite a few types. Therefore, by default, the first way is used. But the second way has several advantages, that may outweigh it’s deficiencies. First - there is one spot where parameters of the type can be changed. You can easily widen the varchar(20) fields to varchar(40) by editing just one place in the model. Secondly, you can define some additional parameters of the type - such as character set.</p><h3><strong>User defined types</strong></h3><h6 style="text-align: center;"><ac:image><ri:attachment ri:filename="Figure 22 Examples of User Defined Types.png" /></ac:image></h6><h6 style="text-align: center;">Examples of user defined types.</h6><p>Besides the primitive / built-in types of the database, user can define additional types for his own schema.</p><h4>Distinct type</h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c973d125-fee5-481a-a32c-636fe003ee79"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body>SQL Distinct type is modeled as UML DataType with «DistinctUserDe- finedType» stereotype applied. For the sake of compactness, refer- ences are displayed with the «distinct» keyword (instead of the long form - «DistinctUserDefinedType») on the diagram.</ac:rich-text-body></ac:structured-macro><p>Distinct type definition allows to redefine some primitive type in order to enforce the non-assignability rules. For example, two distinct types <strong>Meters </strong>and <strong>Yards </strong>can be defined on the base primitive type <strong>float</strong>. With this definition, system would enforce checks that yard fields / columns are not assigned to meter fields / columns without a conversion (explicit cast).</p><p>Besides the standard SQL element properties, distinct type has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.7806%;"><colgroup><col style="width: 21.828%;" /><col style="width: 78.172%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><p><strong>Predefined Representation</strong></p></td><td>Points to some base primitive type.</td></tr></tbody></table><h4>Domain</h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a248e1ff-b54a-4aa8-b663-0207e9c8ae5c"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Domain is modeled as UML DataType with «Domain» stereotype applied. For the sake of compactness, domains are displayed with the «domain» keyword on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Domain allows to define a more narrow set of values than the base primitive type allows. This narrowing is done by assigning additional constraints on the domain. Columns, whose types are set to the domain, can only assume values from this more narrow subset.</p><p>Besides the standard SQL element properties, domain has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.7806%;"><colgroup><col style="width: 21.993%;" /><col style="width: 78.007%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><p><strong>Predefined <strong>Representation</strong><br /></strong></p></td><td>Points to some base primitive type.</td></tr><tr><td><strong>Default Value</strong></td><td>Default value for the column if no value is specified.</td></tr></tbody></table><h4><strong>Structured user defined type</strong></h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9bdbface-3fed-47c4-a725-d473e161583c"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Structured User Defined Type is modeled as UML DataType with «StructuredUserDefinedType» stereotype applied. For the sake of com- pactness, domains are displayed with the «structured» keyword (instead of the long form - «StructuredUserDefinedType») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Structured UDT defines a composite datatype. Each value of this type is a tuple of several values; each position in a tuple has a name. Structured UDT value is analogous to one row of the table. Structured UDTs allow single inheritance (multiple inheritance is not supported). Inheritance (subtype-supertype relationship) can be modeled using UML Generalization relationships.</p><p>Besides the standard SQL element properties, structured UDT has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.5612%;"><colgroup><col style="width: 22.591%;" /><col style="width: 77.409%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><p><strong>Instantiable</strong></p></td><td><p>Defines</p></td></tr><tr><td><p><strong>Final</strong></p></td><td><p>Default value for the column if no value is specified.</p></td></tr><tr><td><p><strong>Super</strong></p></td><td><p>Shows base data types. This is a derived field, it is not editable. To make changes, use UML Generalization relationships.</p></td></tr></tbody></table><p>Parts of the structured UDT (properties) are called attributes (compare - parts of the table definition are called columns). Attributes of structured UDT are created like columns of the table, that is, via the <strong>Attribute Definitions </strong>tab in the structured UDT Specification window or using an appropriate smart manipulation button on its shape.</p><p>Besides the standard SQL element properties, attribute has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.616%;"><colgroup><col style="width: 22.7438%;" /><col style="width: 77.2562%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Type</strong></td><td rowspan="2"><p>Collectively these two fields describe the type of the attribute. The same considerations as for column type modeling apply.</p></td></tr><tr><td><strong>Type Modifier</strong></td></tr><tr><td><strong>Default Value</strong></td><td>Carries the default value of the attribute.</td></tr><tr><td><strong>Scope Check</strong></td><td rowspan="2"><p>Marks this attribute as scope checked to a particular table and allows choosing particular referential integrity ensuring action (RESTRICT CASCADE, etc).</p></td></tr><tr><td><strong>Scope Checked</strong></td></tr></tbody></table><p>Besides attributes, Structured UDTs have a collection of methods - operations, performing actions on values of this type. Methods are covered in a separate section with stored procedures and functions (see <ac:link><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Routines" /></ac:link> section).</p><h4>Array type</h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="195d4354-a730-4f84-a798-718d8708749f"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Array type is modeled as UML DataType with «ArrayDataType» stereotype applied. For the sake of compactness, arrays are displayed with the «array» keyword (instead of the long form - «ArrayDataType») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Array type defines an array (that is, list of values, with the indexed, O(1) access to the n-th element) of the values of elementary type. Besides the standard SQL element properties, array type has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 23.0533%;" /><col style="width: 76.9467%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><p><strong>Element</strong></p></td><td><p>The elementary type of the set elements.</p></td></tr><tr><td><p><strong>Max Cardinality</strong></p></td><td><p>The size limit of the array.</p></td></tr></tbody></table><p><br /></p><h4><strong>Multiset type</strong></h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1b4008e4-b7d7-4b12-931a-e96b2611ddde"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Multiset type is modeled as UML DataType with «MultisetDataType» stereotype applied. For the sake of compactness, multisets are displayed with the «multiset» keyword (instead of the long form - «MultisetDataType») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Multiset type defines a set of elements of the elementary type. Besides the standard SQL element properties, multiset has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 23.0853%;" /><col style="width: 76.9147%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><p><strong>Element</strong></p></td><td><p>The elementary type of the set elements.</p></td></tr></tbody></table><p><br /></p><h4><strong>Reference types</strong></h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6ca2dc2c-339e-49f4-84f1-07b3f488edb6"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Reference type is modeled as UML DataType with «ReferenceDataType» stereotype applied. For the sake of compactness, references are displayed with the «ref» keyword (instead of the long form - «ReferenceDataType») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Reference type defines a pointer to the data of the referred type. Besides the standard SQL element properties, reference type has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 23.1009%;" /><col style="width: 76.8991%;" /></colgroup><tbody><tr><th><p><strong>Property name</strong></p></th><th><p><strong>Description</strong></p></th></tr><tr><td><p><strong>Referenced Type</strong></p></td><td><p>The type of the data that is being referenced.</p></td></tr><tr><td><p><strong>Scope Table</strong></p></td><td><p>Limit the references to the data of the particular table.</p></td></tr></tbody></table><p><br /></p><h4>Row type</h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="65020c0f-fa8e-413a-9918-9511a0c20a87"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Row Data Type is modeled as UML DataType with «RowDataType» stereotype applied. For the sake of compactness, row data types are displayed with the «row» keyword (instead of the long form - «RowDataType») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Represents one row of the table. The difference from structured UDT is that row type represents a value stored in the table, while structured UDT represents “free-floating” value during computation. For example, it is meaningful to take address for the row, but not of the structured UDT value.</p><p>Parts of the row data type (properties) are called fields (compare - parts of the table definition are called columns). Fields for row data type are created like columns of the table, that is, via the <strong>Fields </strong>tab in the row data type Specification window or using an appropriate smart manipulation button on its shape.</p><p>Besides the standard SQL element properties, field has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 23.6061%;" /><col style="width: 76.3939%;" /></colgroup><tbody><tr><th><p> <strong>Property name</strong></p></th><th><p> <strong>Description</strong></p></th></tr><tr><td><p><strong>T</strong><strong>ype</strong></p></td><td rowspan="2"><p>Collectively these two fields describe the type of the field. The same considerations as for column type modeling apply.</p></td></tr><tr><td><p><strong>T</strong><strong>ype Modifier</strong></p></td></tr><tr><td><strong>Scope Check</strong></td><td rowspan="2"><p>Marks this field as scope checked to a particular table and allows choosing particular referential integrity ensuring action (RESTRICT CASCADE, etc).</p></td></tr><tr><td><strong>Scope Checked</strong></td></tr></tbody></table></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459941 space=CDMP2024xR1 version=5 -->
## PAGE 00050: Notation

- page_id: `170459941`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459941/Notation
- version_number: 5
- version_date: `2024-05-08T14:27:21.044+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDnotation. This attribute must be added into the UML class with the stereotype XSDschema.

- name maps to UML Attribute name
- annotation maps to UML Attribute documentation

#### PANEL: notation XML representation summary

notation XML representation summary

```text
<notation
```

```text
id = ID
```

```text
name = NCName	public =  anyURI
```

```text
system = anyURI
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</notation>
```

#### PANEL: XML representation of a notation declaration

XML representation of a notation declaration

```text
<xs:notation name="jpeg" public="image/jpeg" system="viewer.exe">
```

###### [IMAGE alt='' src='']

###### notation UML model example.

#### PANEL: notation XML code sample

notation XML code sample

```text
<xs:schema xmlns:nm = "http://nomagic.com" xmlns:xs = "http://www.w3.org/2001/XMLSchema" targetNamespace = "http://nomagic.com">
```

```text
<xs:notation name = "jpeg" public = "image/jpeg" system = "viewer.exe"/>
```

```text
</xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDnotation. This attribute must be added into the UML class with the stereotype XSDschema.</p><ul><li>name maps to UML Attribute name</li><li style="text-align: left;">annotation maps to UML Attribute documentation</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e6251254-c408-4c2a-90ec-a8d34fc95895"><ac:parameter ac:name="title">notation XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;notation</pre><pre>	id = ID</pre><pre>	name = NCName<br />	public =  anyURI</pre><pre>	system = anyURI</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/notation&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="23cb0e59-9553-4083-882d-7e33eac26c7d"><ac:parameter ac:name="title">XML representation of a notation declaration</ac:parameter><ac:rich-text-body><pre>&lt;xs:notation name=&quot;jpeg&quot; public=&quot;image/jpeg&quot; system=&quot;viewer.exe&quot;&gt;</pre></ac:rich-text-body></ac:structured-macro><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 132 notation UML Model Example.png" /></ac:image></h6><h6 style="text-align: center;">notation UML model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3d53c347-f765-4bf6-85d2-4319ebec30b6"><ac:parameter ac:name="title">notation XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.comu">http://nomagic.com&quot;</a> xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLSchema%22">http://www.w3.org/2001/XMLSchema&quot;</a> targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot;&gt;</pre><pre>	&lt;xs:notation name = &quot;jpeg&quot; public = &quot;image/jpeg&quot; system = &quot;viewer.exe&quot;/&gt;</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459766 space=CDMP2024xR1 version=1 -->
## PAGE 00051: Oracle database modeling extensions

- page_id: `170459766`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459766/Oracle+database+modeling+extensions
- version_number: 1
- version_date: `2023-09-21T12:46:57.014+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support > Database modeling
- labels: []

### NORMALIZED CONTENT

When the Oracle flavor is chosen for database top level element (schema or database), additional Oracle extensions are brought in. Elements that are in the scope of this schema or database element obtain additional Oracle-specific properties in the Specification windows (under the separate **Oracle**property group). These properties carry an additional information, that is then used when generating DDL scripts for Oracle.

Most often there is just one **Additional Properties**property - allowing entering free-form text that is then used when generating (this can be used to specify any extension texts - such as tablespace options for tables).

Oracle extensions provide means to model synonyms. Synonym is mapped as follows.

- Element of the same type (that is, table, materialized view, stored procedure, sequence) as the one being aliased is created. It is stereotyped as appropriate, but have no other data - just its name is important.
- Additionally, stereotype «OraSynonym» will be applied on the element. It has ref:Element[1] tag for pointing to the element being aliased. Synonyms of synonyms are handled in the same way.

Oracle extensions provide means to model materialized views. Materialized view can be created from Oracle SQL diagram. It is an ordinary SQL view, but with the additional «OraMaterializedView» stereotype applied (in diagrams, a shortened keyword «materialized» is used for the sake of compactness).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>When the Oracle flavor is chosen for database top level element (schema or database), additional Oracle extensions are brought in. Elements that are in the scope of this schema or database element obtain additional Oracle-specific properties in the Specification windows (under the separate <strong>Oracle </strong>property group). These properties carry an additional information, that is then used when generating DDL scripts for Oracle.</p><p>Most often there is just one <strong>Additional Properties </strong>property - allowing entering free-form text that is then used when generating (this can be used to specify any extension texts - such as tablespace options for tables).</p><p>Oracle extensions provide means to model synonyms. Synonym is mapped as follows.</p><ul><li>Element of the same type (that is, table, materialized view, stored procedure, sequence) as the one being aliased is created. It is stereotyped as appropriate, but have no other data - just its name is important.</li><li>Additionally, stereotype «OraSynonym»  will be applied on the element. It has ref:Element[1] tag for pointing to the element being aliased. Synonyms of synonyms are handled in the same way.</li></ul><p>Oracle extensions provide means to model materialized views. Materialized view can be created from Oracle SQL diagram. It is an ordinary SQL view, but with the additional «OraMaterializedView» stereotype applied (in diagrams, a shortened keyword «materialized» is used for the sake of compactness).</p>
````

<!--NOMAGIC_PAGE id=170459895 space=CDMP2024xR1 version=1 -->
## PAGE 00052: Pattern

- page_id: `170459895`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459895/Pattern
- version_number: 1
- version_date: `2023-09-21T12:47:02.744+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype *XSDpattern*. The name and type of such an attribute do not make sense.

- value – to Attribute initial value or TaggedValue with name ‘value’.

#### PANEL: pattern XML representation summary

pattern XML representation summary

```text
<pattern
```

```text
id = ID
```

```text
value = anySimpleType
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</pattern>
```

```text
{value} must be a valid regular expression.
```

#### PANEL: pattern XML code sample

pattern XML code sample

```text
The following is the definition of a user-derived datatype which is a better representation of postal codes in the United States, by limiting strings to those which are matched by a specific regular expression.
```

```text
<simpleType name='better-us-zipcode'>
```

```text
<restriction base='string'>
```

```text
<pattern value='[0-9]{5}(-[0-9]{4})?'/>
```

```text
</restriction>
```

```text
</simpleType>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype <em>XSDpattern</em>. The name and type of such an attribute do not make sense.</p><ul><li>value – to Attribute initial value or TaggedValue with name ‘value’.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="04cc49c4-154f-4d66-ad1c-9f2e08ef6fa7"><ac:parameter ac:name="title">pattern XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;pattern</pre><pre>	id = ID</pre><pre>	value = anySimpleType</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/pattern&gt;</pre><pre>{value} must be a valid regular expression.</pre></ac:rich-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="4038943d-291a-47a0-b373-4d8666daea14"><ac:parameter ac:name="title">pattern XML code sample</ac:parameter><ac:rich-text-body><pre>The following is the definition of a user-derived datatype which is a better representation of postal codes in the United States, by limiting strings to <br />those which are matched by a specific regular expression.<br /><br /></pre><pre>&lt;simpleType name='better-us-zipcode'&gt;</pre><pre>	&lt;restriction base='string'&gt;</pre><pre>		&lt;pattern value='[0-9]{5}(-[0-9]{4})?'/&gt;</pre><pre>	&lt;/restriction&gt;</pre><pre>&lt;/simpleType&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459946 space=CDMP2024xR1 version=5 -->
## PAGE 00053: Redefine

- page_id: `170459946`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459946/Redefine
- version_number: 5
- version_date: `2024-05-08T14:27:33.428+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Class with the stereotype XSDredefine. This class has inner UML Classes as redefined elements. Every redefined element must be derived from other UML classes with stereotypes XSDsimpleType, XSDcomplexType, XSDgroup, or XSDattributeGroup. The name of this class shall match the “schemaLocation” value.

If two “redefine” with the same schema location appears, they shall be merged into the same class with the name “schemaLocation”.

The Redefine Class must be the inner class of the XSDschema Class.

- annotation - to the XSDredefine UML Class documentation
- schemaLocation – to the XSDredefine UML Class name.

#### PANEL: redefine XML representation summary

redefine XML representation summary

```text
<redefine
```

```text
id = ID
```

```text
schemaLocation = anyURI
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation | (simpleType | complexType | group | attributeGroup))*
```

```text
</redefine>
```

#### PANEL: Schema corresponding to v2.xsd with the personName type redefined

Schema corresponding to v2.xsd with the personName type redefined

```text
v1.xsd:
```

```text
<xs:complexType name="personName">
```

```text
<xs:sequence>
```

```text
<xs:element name="title" minOccurs="0"/>
```

```text
<xs:element name="forename" minOccurs="0" maxOccurs="unbounded"/>		</xs:sequence>
```

```text
</xs:complexType>
```

```text
<xs:element name="addressee" type="personName"/>
```

```text
v2.xsd:
```

```text
<xs:redefine schemaLocation="v1.xsd">
```

```text
<xs:complexType name="personName">
```

```text
<xs:complexContent>
```

```text
<xs:extension base="personName">
```

```text
<xs:sequence>
```

```text
<xs:element name="generation" minOccurs="0"/>
```

```text
</xs:sequence>				</xs:extension>			</xs:complexContent>		</xs:complexType>	</xs:redefine>
```

```text
<xs:element name="author" type="personName"/>
```

The schema corresponding to *v2.xsd*has everything specified by *v1.xsd*, with the *personName*type redefined, as well as everything it specifies. According to this schema, elements constrained by the *personName*type may end with a *generation*element. This includes not only the *author*element, but also the *addressee*element.

###### [IMAGE alt='' src='']

###### redefine UML model example.

#### PANEL: redefine XML code sample

redefine XML code sample

```text
<?xml version=’1.0’ encoding=’UTF-8’?
```

```text
<xs:schema xmlns:nm="http://nomagic.com" xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://nomagic.com">
```

```text
<xs:redefine schemaLocation="http://nomagic.com">
```

```text
<xs:simpleType name="string">
```

```text
<xs:annotation>
```

```text
<xs:documentation>my documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
<xs:restriction base="xs:string" />
```

```text
</xs:simpleType>
```

```text
</xs:redefine>
```

```text
</xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Class with the stereotype XSDredefine. This class has inner UML Classes as redefined elements. Every redefined element must be derived from other UML classes with stereotypes XSDsimpleType, XSDcomplexType, XSDgroup, or XSDattributeGroup. The name of this class shall match the “schemaLocation” value.</p><p>If two “redefine” with the same schema location appears, they shall be merged into the same class with the name “schemaLocation”.</p><p>The Redefine Class must be the inner class of the XSDschema Class.</p><ul><li>annotation - to the XSDredefine UML Class documentation</li><li style="text-align: left;">schemaLocation – to the XSDredefine UML Class name.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="61c235b6-e0a4-4d7c-b4b7-30ae412cba2b"><ac:parameter ac:name="title">redefine XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;redefine</pre><pre>	id = ID</pre><pre>	schemaLocation = anyURI</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation | (simpleType | complexType | group | attributeGroup))*</pre><pre>&lt;/redefine&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="4a8510cc-fe2d-4e79-9aec-e7705472e494"><ac:parameter ac:name="title">Schema corresponding to v2.xsd with the personName type redefined</ac:parameter><ac:rich-text-body><pre>v1.xsd:</pre><pre>	&lt;xs:complexType name=&quot;personName&quot;&gt;</pre><pre>		&lt;xs:sequence&gt;</pre><pre>			&lt;xs:element name=&quot;title&quot; minOccurs=&quot;0&quot;/&gt;</pre><pre>			&lt;xs:element name=&quot;forename&quot; minOccurs=&quot;0&quot; maxOccurs=&quot;unbounded&quot;/&gt;<br />		&lt;/xs:sequence&gt;</pre><pre>	&lt;/xs:complexType&gt;<br /><br /></pre><pre>	&lt;xs:element name=&quot;addressee&quot; type=&quot;personName&quot;/&gt;<br /><br /></pre><pre>v2.xsd:</pre><pre>	&lt;xs:redefine schemaLocation=&quot;v1.xsd&quot;&gt;</pre><pre>		&lt;xs:complexType name=&quot;personName&quot;&gt;</pre><pre>			&lt;xs:complexContent&gt;</pre><pre>				&lt;xs:extension base=&quot;personName&quot;&gt;</pre><pre>					&lt;xs:sequence&gt;</pre><pre>						&lt;xs:element name=&quot;generation&quot; minOccurs=&quot;0&quot;/&gt;</pre><pre>					&lt;/xs:sequence&gt;<br />				&lt;/xs:extension&gt;<br />			&lt;/xs:complexContent&gt;<br />		&lt;/xs:complexType&gt;<br />	&lt;/xs:redefine&gt;<br /><br /></pre><pre>	&lt;xs:element name=&quot;author&quot; type=&quot;personName&quot;/&gt;</pre></ac:rich-text-body></ac:structured-macro><p style="text-align: left;">The schema corresponding to <em>v2.xsd </em>has everything specified by <em>v1.xsd </em>, with the <em>personName </em>type redefined, as well as everything it specifies. According to this schema, elements constrained by the <em>personName </em>type may end with a <em>generation </em>element. This includes not only the <em>author </em>element, but also the <em>addressee </em>element.</p><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 135 redefine UML Model Example.png" /></ac:image></h6><h6 style="text-align: center;">redefine UML model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="abae87a2-c5c3-4eb9-a876-98a2efc42343"><ac:parameter ac:name="title">redefine XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;?xml version=’1.0’ encoding=’UTF-8’?<br /><br /></pre><pre>&lt;xs:schema xmlns:nm=&quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; xmlns:xs=&quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; targetNamespace=&quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot;&gt;</pre><pre>	&lt;xs:redefine schemaLocation=&quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot;&gt;</pre><pre>		&lt;xs:simpleType name=&quot;string&quot;&gt;</pre><pre>			&lt;xs:annotation&gt;</pre><pre>				&lt;xs:documentation&gt;my documentation&lt;/xs:documentation&gt;</pre><pre>			&lt;/xs:annotation&gt;</pre><pre>			&lt;xs:restriction base=&quot;xs:string&quot; /&gt;</pre><pre>		&lt;/xs:simpleType&gt;</pre><pre>	&lt;/xs:redefine&gt;</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459851 space=CDMP2024xR1 version=5 -->
## PAGE 00054: Restriction

- page_id: `170459851`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459851/Restriction
- version_number: 5
- version_date: `2024-05-08T14:21:39.055+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

To specify restriction, a generalization must be used between this class and a super class. This generalization either has or does not have the *XSDrestriction*stereotype. Restriction id and annotation maps to Generalization properties.

In order to have an inner simpleType element, the parent of this Generalization must be the inner Class of the outer UML Class.

[IMAGE alt='' src='']

###### Restriction model example.

#### PANEL: Restriction XML code sample

Restriction XML code sample

```text
<xs:schema xmlns:nm = "http://nomagic.com" xmlns:xs = "http://www.w3.org/2001/XMLSchema" targetNamespace = "http://nomagic.com" >	<xs:simpleType name = "farenheitWaterTemp" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >documentation of simple type</xs:documentation>
```

```text
</xs:annotation>
```

```text
<xs:restriction base = "xs:number" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >documentation of restriction</xs:documentation>
```

```text
</xs:annotation>
```

```text
<xs:pattern id = "pattern_id" value = "[0-9]{5}(-[0-9]{4})?" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >patterndoc</xs:documentation>
```

```text
</xs:annotation>			</xs:pattern>
```

```text
<xs:whiteSpace id = "white_spaceid" fixed = "true" value = "preserve" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >white spacedoc</xs:documentation>
```

```text
</xs:annotation>			</xs:whiteSpace>
```

```text
<xs:whiteSpace id = "white_spaceid" fixed = "true" value = "preserve" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >white spacedoc</xs:documentation>
```

```text
</xs:annotation>			</xs:whiteSpace>
```

```text
<xs:maxLength id = "maxlengthID" fixed = "false" value = "50" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >max length documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
</xs:maxLength>
```

```text
<xs:minLength id = "minlengthID" fixed = "true" value = "2" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >min length documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
</xs:minLength>
```

```text
<xs:length id = "lengthID" fixed = "true" value = "10" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >length documentation</xs:documentation>
```

```text
</xs:annotation>			</xs:length>
```

```text
<xs:fractionDigits id = "fractionDigitsID" fixed = "true" value = "1" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >fraction digits documentation</xs:documentation>
```

```text
</xs:annotation>			</xs:fractionDigits>
```

```text
<xs:totalDigits id = "totalDigitsID" fixed = "false" value = "8" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >total digitsid</xs:documentation>
```

```text
</xs:annotation> 			</xs:totalDigits>
```

```text
<xs:maxInclusive id = "maxinclusiveid" fixed = "true" value = "100" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >max inclusive documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
</xs:maxInclusive>
```

```text
<xs:minInclusive id = "mininclusiveid" fixed = "true" value = "100" >				<xs:annotation >
```

```text
<xs:documentation >min inclusive documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
</xs:minInclusive>
```

```text
<xs:maxExclusive id = "maxexclusiveid" fixed = "true" value = "101" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >max exclusive documentation</xs:documentation>
```

```text
</xs:annotation>			</xs:maxExclusive>
```

```text
<xs:minExclusive id = "id" fixed = "true" value = "99" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >min exclusive documentation</xs:documentation>
```

```text
</xs:annotation>			</xs:minExclusive>
```

```text
</xs:restriction>
```

```text
</xs:simpleType>
```

```text
<xs:simpleType name = "dayTime" >		<xs:annotation >
```

```text
<xs:documentation >day time documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
<xs:restriction >
```

```text
<xs:annotation >
```

```text
<xs:documentation >restriction documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
<xs:simpleType >
```

```text
<xs:restriction base = "xs:number" />			</xs:simpleType>
```

```text
<xs:enumeration value = "day" >
```

```text
<xs:annotation >					<xs:documentation >day value</xs:documentation>
```

```text
</xs:annotation>			‹/xs:enumeration>
```

```text
<xs:enumeration value = "night" >
```

```text
<xs:annotation >					<xs:documentation >night valuec</xs:documentation>
```

```text
</xs:annotation>			</xs:enumeration>
```

```text
</xs:restriction>
```

```text
</xs:simpleType>
```

```text
<xs:simpleType name = " sex" final = "restriction" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >documentation of simple type restriction</xs:documentation>
```

```text
</xs:annotation>
```

```text
<xs:restriction base = "xs:string" >
```

```text
<xs:enumeration id = "some id" value = "male" /> 			<xs:enumeration value = "female" >
```

```text
<xs:annotation > 					<xs:documentation >female value</xs:documentation>
```

```text
</xs:annotation>
```

```text
</xs:enumeration>
```

```text
</xs:restriction>	</xs:simpleType>
```

```text
</xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To specify restriction, a generalization must be used between this class and a super class. This generalization either has or does not have the <em>XSDrestriction </em>stereotype. Restriction id and annotation maps to Generalization properties.</p><p>In order to have an inner simpleType element, the parent of this Generalization must be the inner Class of the outer UML Class.</p><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 66 Restriction Example Model.png" /></ac:image></p><h6 style="text-align: center;">Restriction model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="56176579-0ae0-4cd1-a2e7-df58b7661826"><ac:parameter ac:name="title">Restriction XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; &gt;<br />	&lt;xs:simpleType name = &quot;farenheitWaterTemp&quot; &gt;</pre><pre>		&lt;xs:annotation &gt;</pre><pre>			&lt;xs:documentation &gt;documentation of simple type&lt;/xs:documentation&gt;</pre><pre>		&lt;/xs:annotation&gt;</pre><pre>		&lt;xs:restriction base = &quot;xs:number&quot; &gt;</pre><pre>			&lt;xs:annotation &gt;</pre><pre>				&lt;xs:documentation &gt;documentation of restriction&lt;/xs:documentation&gt;</pre><pre>			&lt;/xs:annotation&gt;</pre><pre>			&lt;xs:pattern id = &quot;pattern_id&quot; value = &quot;[0-9]{5}(-[0-9]{4})?&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;patterndoc&lt;/xs:documentation&gt;<br /><br /></pre><pre>				&lt;/xs:annotation&gt;<br />			&lt;/xs:pattern&gt;</pre><pre>			&lt;xs:whiteSpace id = &quot;white_spaceid&quot; fixed = &quot;true&quot; value = &quot;preserve&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;white spacedoc&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;<br />			&lt;/xs:whiteSpace&gt;</pre><pre>			&lt;xs:whiteSpace id = &quot;white_spaceid&quot; fixed = &quot;true&quot; value = &quot;preserve&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;white spacedoc&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;<br />			&lt;/xs:whiteSpace&gt;</pre><pre>			&lt;xs:maxLength id = &quot;maxlengthID&quot; fixed = &quot;false&quot; value = &quot;50&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;max length documentation&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;</pre><pre>			&lt;/xs:maxLength&gt;</pre><pre>			&lt;xs:minLength id = &quot;minlengthID&quot; fixed = &quot;true&quot; value = &quot;2&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;min length documentation&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;</pre><pre>			&lt;/xs:minLength&gt;</pre><pre>			&lt;xs:length id = &quot;lengthID&quot; fixed = &quot;true&quot; value = &quot;10&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;length documentation&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;<br />			&lt;/xs:length&gt;</pre><pre>			&lt;xs:fractionDigits id = &quot;fractionDigitsID&quot; fixed = &quot;true&quot; value = &quot;1&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;fraction digits documentation&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;<br />			&lt;/xs:fractionDigits&gt;</pre><pre>			&lt;xs:totalDigits id = &quot;totalDigitsID&quot; fixed = &quot;false&quot; value = &quot;8&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;total digitsid&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt; <br />			&lt;/xs:totalDigits&gt;</pre><pre>			&lt;xs:maxInclusive id = &quot;maxinclusiveid&quot; fixed = &quot;true&quot; value = &quot;100&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;max inclusive documentation&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;</pre><pre>			&lt;/xs:maxInclusive&gt;</pre><pre>			&lt;xs:minInclusive id = &quot;mininclusiveid&quot; fixed = &quot;true&quot; value = &quot;100&quot; &gt;<br />				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;min inclusive documentation&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;</pre><pre>			&lt;/xs:minInclusive&gt;</pre><pre>			&lt;xs:maxExclusive id = &quot;maxexclusiveid&quot; fixed = &quot;true&quot; value = &quot;101&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;max exclusive documentation&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;<br />			&lt;/xs:maxExclusive&gt;</pre><pre>			&lt;xs:minExclusive id = &quot;id&quot; fixed = &quot;true&quot; value = &quot;99&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;</pre><pre>					&lt;xs:documentation &gt;min exclusive documentation&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;<br />			&lt;/xs:minExclusive&gt;</pre><pre>		&lt;/xs:restriction&gt;</pre><pre>	&lt;/xs:simpleType&gt;</pre><pre>	&lt;xs:simpleType name = &quot;dayTime&quot; &gt;<br />		&lt;xs:annotation &gt;</pre><pre>			&lt;xs:documentation &gt;day time documentation&lt;/xs:documentation&gt;</pre><pre>		&lt;/xs:annotation&gt;</pre><pre>		&lt;xs:restriction &gt;</pre><pre>			&lt;xs:annotation &gt;</pre><pre>				&lt;xs:documentation &gt;restriction documentation&lt;/xs:documentation&gt;</pre><pre>			&lt;/xs:annotation&gt;</pre><pre>			&lt;xs:simpleType &gt;</pre><pre>				&lt;xs:restriction base = &quot;xs:number&quot; /&gt;<br />			&lt;/xs:simpleType&gt;</pre><pre>			&lt;xs:enumeration value = &quot;day&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;<br />					&lt;xs:documentation &gt;day value&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;<br />			‹/xs:enumeration&gt;</pre><pre>			&lt;xs:enumeration value = &quot;night&quot; &gt;</pre><pre>				&lt;xs:annotation &gt;<br />					&lt;xs:documentation &gt;night valuec&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;<br />			&lt;/xs:enumeration&gt;</pre><pre>		&lt;/xs:restriction&gt;</pre><pre>	&lt;/xs:simpleType&gt;</pre><pre>	&lt;xs:simpleType name = &quot; sex&quot; final = &quot;restriction&quot; &gt;</pre><pre>		&lt;xs:annotation &gt;</pre><pre>			&lt;xs:documentation &gt;documentation of simple type restriction&lt;/xs:documentation&gt;</pre><pre>		&lt;/xs:annotation&gt;</pre><pre>		&lt;xs:restriction base = &quot;xs:string&quot; &gt;</pre><pre>			&lt;xs:enumeration id = &quot;some id&quot; value = &quot;male&quot; /&gt; <br />			&lt;xs:enumeration value = &quot;female&quot; &gt;</pre><pre>				&lt;xs:annotation &gt; <br />					&lt;xs:documentation &gt;female value&lt;/xs:documentation&gt;</pre><pre>				&lt;/xs:annotation&gt;</pre><pre>			&lt;/xs:enumeration&gt;</pre><pre>		&lt;/xs:restriction&gt;<br />	&lt;/xs:simpleType&gt;</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459762 space=CDMP2024xR1 version=6 -->
## PAGE 00055: Routines

- page_id: `170459762`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459762/Routines
- version_number: 6
- version_date: `2024-05-08T13:52:52.342+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support > Database modeling
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

125674665

#### CONTENT-COLUMN: Note

125674667

125674663

**On this page**

33

#### CONTENT-BLOCK: Note

125674666

[IMAGE alt='' src='']

###### Routines example.

SQL supports several different kinds of routines. There are global routines, that are not bound to a particular type but belongs to the schema. There are two kinds of these routines - Procedures and Functions. And there are routines, that are bound to a particular structured user defined type - Methods. Each routine kind can have several parameters. Parameters have type and direction (**in**, **out**, **inout**). Functions and methods in SQL have return types - this is formalized in UML models by having an additional parameter with **return**direction kind.

There is an UML limitation, that UML does not allow to place UML operations (which are used to model SQL procedures and functions) directly in the UML packages (which are used to model SQL schemas). For this reason global routines are placed into a special container class - GLOBALS (see [CONFLUENCE_PAGE title='Top level elements' space='CDMP2024x Refresh1 Refresh1 Refresh1R1']).

Routines can be external (written in some other languages and attached to database engine) or SQL routines. In the latter case, body of the routine can be specified in the model. Due to UML specifics, there are two ways to specify the routine body - by filling the UML **method**field or by filling the UML **bodyCondition**field of the operation. These two ways are visible in the Specification window under the field names **Source (as method)**and **Source (as body condition)**. When specifying routine body, specify only one of these fields.

To use “as method” way

1. Right-click the GLOBALS element in the Containment tree and from its shortcut menu select New Element > Source . A source element (a UML OpaqueBehavior with the «Source» stereotype applied) under the GLOBALS element will be created in your schema.
2. In the Specification window of routine, edit the Source (as method) property value and in the opened dialog select the source element you’ve just created.

To use “as body condition” way, you simply have to fill the field. The routine body model element (in this case, UML Constraint - holding UML OpaqueExpression) shall be created under your routine model element.

Besides the standard SQL element properties, all 3 kinds of routines have the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Specific Name | Additional name for the routine, uniquely identifying it throughout the system. |
| Deterministic | Specifies whether routine is deterministic (always gives the same output with the same data input). |
| Parameter Style | SQL or GENERAL. |
| SQL Data Access | Specifies how routine accesses SQL data (NO SQL \| CONTAINS SQL \| READS SQL DATA \| MODIFIES SQL DATA). |
| Source (as method) | Fields holding routine body text (choose only one). |
| Source (as body condition) |  |
| Creation TS | Routine creation and last edit timestamps. |
| Last Altered TS |  |
| Authorization ID | Authorization identifier which owns this routine (owner of the schema at routine creation time). |
| Security | Determines the authorization identifier under which this routine runs. Typically set to “INVOKER”, “DEFINER”, “IMPLEMENTATION DEPENDENT”. |
| External Name | The name of the external language routine implementation method (if routine is non-SQL routine). |

##### Procedure

#### NOTE: Note

Note

SQL Procedure is modeled as UML Operation with «Procedure» stereotype applied. For the sake of compactness, procedures are displayed with the «proc» keyword (instead of the long form - «Procedure») on the diagram.

Procedure is an operation that can be SQL-invoked and performs some actions depending on the parameters supplied. Procedures are global for schema - they are created under the GLOBALS model element.

Besides the standard properties of SQL routines (see [CONFLUENCE_PAGE title='Routines' space='CDMP2024x Refresh1 Refresh1 Refresh1R1']), procedure has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Max Result Sets | If result set count is returned by procedure is dynamic, this value limits count thereof (DYMANIC RESULT SETS <max> clause). |
| Old Save Point | Savepoint level indicator for procedure (false means that new savepoint must be established before the procedure is run.). |

##### Function

#### NOTE: Note

Note

SQL Function is modeled as UML Operation with «Function» or «BuiltInFunction» or «UserDefinedFunction» stereotype applied. By default the «UserDefinedFunction» is used, however if another kind can be freely used if it is necessary for modeling needs (e.g. if we are modeling some built in library and want to specify that functions are built-in and not user defined).

For the sake of compactness, functions are displayed with the «func» keyword (instead of the long form) on the diagram.

Function describes some operation that calculates and returns some value depending on the parameters supplied. Functions are global for schema - they are created under the GLOBALS model element.

Besides the standard properties of SQL routines (see [CONFLUENCE_PAGE title='Routines' space='CDMP2024x Refresh1 Refresh1 Refresh1R1']), function has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Null Call | Specifies that function returns NULL when called with NULL parameter value (RETURNS NULL ON NULL INPUT clause). |
| Type Preserving | Specifies that function does not change the type of the supplied parameter (returns the same object). |
| Transform Group | Allows to specify TRANSFORM GROUP <groups> clause - single or multiple. |

##### Method

#### NOTE: Note

Note

SQL Method is modeled as UML Operation with «Method» stereotype applied. For the sake of compactness, methods are displayed with the «func» keyword (instead of the long form - «Method») on the diagram.

Method is a function of the structured user defined type. It is created inside the structured UDT.

Besides the properties of SQL functions (see [CONFLUENCE_PAGE title='Routines' space='CDMP2024x Refresh1 Refresh1 Refresh1R1']), method has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Constructor | Specifies that function is a constructor (used to construct values of the enclosing structured UDT). |
| Overriding | Specifies that function is overriding the same-named function from the parent structured UDT. |

##### Parameter

#### NOTE: Note

Note

SQL Parameter is modeled as UML Parameter with «Parameter» stereotype applied.

This model element specifies data inputs / outputs into routine calculations. Parameter has a type, direction (in / out / inout for usual parameters and a single parameter with direction return for functions) and default value.

Besides the standard SQL element properties, parameter has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Type | Type of the parameter. |
| Type Modifier |  |
| Default Value | Default value (used when value is not supplied during routine invocation). |
| Direction | Direction of data flow through the parameter (into the routine, out of the routine or both). |
| Locator | AS LOCATOR modifier of the type. Specifies that instead of value, means to locate value are transferred. |
| String Type Option | Only valid when parameter type is XML type. Specifies underlying string datatype. |
| Cast Type | Additional options, specifying that return parameter is cast from another type (possibly with locator indication). |
| Cast Locator |  |

##### Cursor and routine result table

#### NOTE: Note

Note

SQL Cursor is modeled as UML Parameter with the «Cursor» stereotype applied.

When routine does not return a scalar value but a collection of the table values, cursor is used, instead of the parameter. Cursor has a type. This type must be some table type instead of the scalar types used for parameters. It can be an actual table / view from the model, if the cursor returns values from that table, or (if cursor returns data from some SELECT statement) can be a synthetic table. A Routine Result Table model element is used for this purpose (UML Class with «RoutineResultTable» stereotype applied). Its modeling is exactly the same as the normal tables - this is just an ephemeral table.

Besides the standard SQL element properties, cursor has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Type | Type of the cursor. Should point to the routine result table. |
| Type Modifier |  |
| Direction | Direction of data flow through the parameter (into the routine, out of the routine, routine result). |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="c4457ff8-dc3a-4992-badf-cdd38bf0e120"><ac:parameter ac:name="id">125674665</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="554b8c2d-3a5e-40a5-a4ca-ca20f2ab4b69"><ac:parameter ac:name="id">125674667</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0d3243d9-eeac-4282-b15c-3312a593feb2"><ac:parameter ac:name="id">125674663</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="3a250c82-04f4-42be-b0bf-7019bae19187"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="259e9a30-662b-470a-8ebd-af2aebdfcedb"><ac:parameter ac:name="id">125674666</ac:parameter><ac:rich-text-body><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 30 Routines Example.png" /></ac:image></p><h6 style="text-align: center;">Routines example.</h6><p>SQL supports several different kinds of routines. There are global routines, that are not bound to a particular type but belongs to the schema. There are two kinds of these routines - Procedures and Functions. And there are routines, that are bound to a particular structured user defined type - Methods. Each routine kind can have several parameters. Parameters have type and direction (<strong>in</strong>, <strong>out</strong>, <strong>inout</strong>). Functions and methods in SQL have return types - this is formalized in UML models by having an additional parameter with <strong>return </strong>direction kind.</p><p>There is an UML limitation, that UML does not allow to place UML operations (which are used to model SQL procedures and functions) directly in the UML packages (which are used to model SQL schemas). For this reason global routines are placed into a special container class - GLOBALS (see <ac:link ac:anchor="GLOBALS"><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Top level elements" /><ac:plain-text-link-body><![CDATA[GLOBALS]]></ac:plain-text-link-body></ac:link>).</p><p>Routines can be external (written in some other languages and attached to database engine) or SQL routines. In the latter case, body of the routine can be specified in the model. Due to UML specifics, there are two ways to specify the routine body - by filling the UML <strong>method </strong>field or by filling the UML <strong>bodyCondition </strong>field of the operation. These two ways are visible in the Specification window under the field names <strong>Source (as method) </strong>and <strong>Source (as body condition)</strong>. When specifying routine body, specify only one of these fields.</p><p><br /></p><p>To use “as method” way</p><hr /><ol><li>Right-click the GLOBALS element in the Containment tree and from its shortcut menu select <strong>New Element </strong>&gt; <strong>Source</strong>. A source element (a UML OpaqueBehavior with the «Source» stereotype applied) under the GLOBALS element will be created in your schema.</li><li>In the Specification window of routine, edit the <strong>Source (as method) </strong>property value and in the opened dialog select the source element you’ve just created.</li></ol><p>To use “as body condition” way, you simply have to fill the field. The routine body model element (in this case, UML Constraint - holding UML OpaqueExpression) shall be created under your routine model element.</p><p>Besides the standard SQL element properties, all 3 kinds of routines have the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 22.8208%;" /><col style="width: 77.1792%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Specific Name</strong></td><td>Additional name for the routine, uniquely identifying it throughout the system.</td></tr><tr><td><strong>Deterministic</strong></td><td>Specifies whether routine is deterministic (always gives the same output with the same data input).</td></tr><tr><td><strong>Parameter Style</strong></td><td>SQL or GENERAL.</td></tr><tr><td><strong>SQL Data Access</strong></td><td><p>Specifies how routine accesses SQL data (NO SQL | CONTAINS SQL | READS SQL DATA | MODIFIES SQL DATA).</p></td></tr><tr><td><p><strong>Source (as method)</strong></p></td><td>Fields holding routine body text (choose only one).</td></tr><tr><td><strong>Source (as body condition)</strong></td><td><br /></td></tr><tr><td><strong>Creation TS</strong></td><td><p>Routine creation and last edit timestamps.</p></td></tr><tr><td><p><strong>Last Altered TS</strong></p></td><td><br /></td></tr><tr><td><strong>Authorization ID</strong></td><td>Authorization identifier which owns this routine (owner of the schema at routine creation time).</td></tr><tr><td><strong>Security</strong></td><td><p>Determines the authorization identifier under which this routine runs. Typically set to “INVOKER”, “DEFINER”, “IMPLEMENTATION DEPENDENT”.</p></td></tr><tr><td><strong>External Name</strong></td><td>The name of the external language routine implementation method (if routine is non-SQL routine).</td></tr></tbody></table><p><br /></p><h3>Procedure</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3631e340-ffcf-447a-b682-1018bed01abe"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Procedure is modeled as UML Operation with «Procedure» stereotype applied. For the sake of compactness, procedures are displayed with the «proc» keyword (instead of the long form - «Procedure») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Procedure is an operation that can be SQL-invoked and performs some actions depending on the parameters supplied. Procedures are global for schema - they are created under the GLOBALS model element.</p><p>Besides the standard properties of SQL routines (see <ac:link><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Routines" /></ac:link>), procedure has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 22.8418%;" /><col style="width: 77.1582%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Max Result Sets</strong></td><td>If result set count is returned by procedure is dynamic, this value limits count thereof (DYMANIC RESULT SETS &lt;max&gt; clause).</td></tr><tr><td><strong>Old Save Point</strong></td><td>Savepoint level indicator for procedure (false means that new savepoint must be established before the procedure is run.).</td></tr></tbody></table><p><br /></p><h3>Function</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dc47c3b5-b76c-413a-8967-28ef069aa256"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Function is modeled as UML Operation with «Function» or «BuiltInFunction» or «UserDefinedFunction» stereotype applied. By default the «UserDefinedFunction» is used, however if another kind can be freely used if it is necessary for modeling needs (e.g. if we are modeling some built in library and want to specify that functions are built-in and not user defined).</p><p>For the sake of compactness, functions are displayed with the «func» keyword (instead of the long form) on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Function describes some operation that calculates and returns some value depending on the parameters supplied. Functions are global for schema - they are created under the GLOBALS model element.</p><p>Besides the standard properties of SQL routines (see <ac:link><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Routines" /></ac:link>), function has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.8903%;"><colgroup><col style="width: 22.9002%;" /><col style="width: 77.0998%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Null Call</strong></td><td>Specifies that function returns NULL when called with NULL parameter value (RETURNS NULL ON NULL INPUT clause).</td></tr><tr><td><strong>Type Preserving</strong></td><td>Specifies that function does not change the type of the supplied parameter (returns the same object).</td></tr><tr><td><strong>Transform Group</strong></td><td>Allows to specify TRANSFORM GROUP &lt;groups&gt; clause - single or multiple.</td></tr></tbody></table><p><br /></p><h3>Method</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c1d89e1c-be44-4bfb-8404-2fdc3c838d35"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Method is modeled as UML Operation with «Method» stereotype applied. For the sake of compactness, methods are displayed with the «func» keyword (instead of the long form - «Method») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Method is a function of the structured user defined type. It is created inside the structured UDT.</p><p>Besides the properties of SQL functions (see <ac:link><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Routines" /></ac:link>), method has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 23.0276%;" /><col style="width: 76.9724%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Constructor</strong></td><td>Specifies that function is a constructor (used to construct values of the enclosing structured UDT).</td></tr><tr><td><strong>Overriding</strong></td><td>Specifies that function is overriding the same-named function from the parent structured UDT.</td></tr></tbody></table><h3>Parameter</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="04c40d24-c5d3-48e8-b787-43ae1ed34cf5"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Parameter is modeled as UML Parameter with «Parameter» stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>This model element specifies data inputs / outputs into routine calculations. Parameter has a type, direction (in / out / inout for usual parameters and a single parameter with direction return for functions) and default value.</p><p>Besides the standard SQL element properties, parameter has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 23.2345%;" /><col style="width: 76.7655%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Type</strong></td><td rowspan="2">Type of the parameter.</td></tr><tr><td><strong>Type Modifier</strong></td></tr><tr><td><strong>Default Value</strong></td><td>Default value (used when value is not supplied during routine invocation).</td></tr><tr><td><strong>Direction</strong></td><td>Direction of data flow through the parameter (into the routine, out of the routine or both).</td></tr><tr><td><strong>Locator</strong></td><td>AS LOCATOR modifier of the type. Specifies that instead of value, means to locate value are transferred.</td></tr><tr><td><strong>String Type Option</strong></td><td>Only valid when parameter type is XML type. Specifies underlying string datatype.</td></tr><tr><td><strong>Cast Type</strong></td><td rowspan="2">Additional options, specifying that return parameter is cast from another type (possibly with locator indication).</td></tr><tr><td><strong>Cast Locator</strong></td></tr></tbody></table><p><br /></p><h3>Cursor and routine result table</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2712c800-d093-465b-9c30-780d1ab06a93"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Cursor is modeled as UML Parameter with the «Cursor» stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>When routine does not return a scalar value but a collection of the table values, cursor is used, instead of the parameter. Cursor has a type. This type must be some table type instead of the scalar types used for parameters. It can be an actual table / view from the model, if the cursor returns values from that table, or (if cursor returns data from some SELECT statement) can be a synthetic table. A Routine Result Table model element is used for this purpose (UML Class with «RoutineResultTable» stereotype applied). Its modeling is exactly the same as the normal tables - this is just an ephemeral table.</p><p>Besides the standard SQL element properties, cursor has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 23.4413%;" /><col style="width: 76.5587%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Type</strong></td><td rowspan="2">Type of the cursor. Should point to the routine result table.</td></tr><tr><td><strong>Type Modifier</strong></td></tr><tr><td><strong>Direction</strong></td><td>Direction of data flow through the parameter (into the routine, out of the routine, routine result).</td></tr></tbody></table></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459936 space=CDMP2024xR1 version=5 -->
## PAGE 00056: Schema

- page_id: `170459936`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459936/Schema
- version_number: 5
- version_date: `2024-05-08T14:27:08.312+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Class with the stereotype XSDschema.

All schema global attributes and elements are mapped to the UML Attributes of this class.

The name of this class should match the file name or must be assigned to the component representing the file. The “xmlns” xml tags maps to a permission link with the stereotype «xmlns» and name, representing a given prefix.

The permission client is the schema class and supplier package with its name equal to the “xmlns” value.

#### PANEL: schema XML representation summary

schema XML representation summary

```text
<schema
```

```text
attributeFormDefault = (qualified | unqualified) : unqualified	blockDefault = (#all | List of (extension | restriction | substitution)) : ''
```

```text
elementFormDefault = (qualified | unqualified) : unqualified	finalDefault = (#all | List of (extension | restriction)) : ''
```

```text
id = ID
```

```text
targetNamespace = anyURI
```

```text
version = token
```

```text
xml:lang = language
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: ((include | import | redefine | annotation)*, (((simpleType | complexType | group | attriuteGroup) | element | attribute | notation), annotation*)*)
```

```text
</schema>
```

#### PANEL: XML representation of the skeleton of a schema

XML representation of the skeleton of a schema

```text
<xs:schema
```

```text
xmlns:xs="http://www.w3.org/2001/XMLSchema"	targetNamespace="http://www.example.com/example">
```

```text
…
```

```text
</xs:schema>
```

###### [IMAGE alt='' src='']

###### schema UML model example.

#### PANEL: schema XML code sample

schema XML code sample

```text
<xs:schema xmlns:nm = "http://nomagic.com"xmlns:xs = "http://www.w3.org/2001/XMLSchema"xmlns = "http://nomagic.com"attributeFormDefault = "qualified"blockDefault = "extension"
```

```text
elementFormDefault = "unqualified"finalDefault = "extension"
```

```text
targetNamespace = "http://nomagic.com"version = "1.2"
```

```text
xml:lang = "EN" />
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Class with the stereotype XSDschema.</p><p>All schema global attributes and elements are mapped to the UML Attributes of this class.</p><p>The name of this class should match the file name or must be assigned to the component representing the file. The “xmlns” xml tags maps to a permission link with the stereotype «xmlns» and name, representing a given prefix.</p><p style="text-align: left;">The permission client is the schema class and supplier package with its name equal to the “xmlns” value.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e13b4431-a0fa-4221-b30e-e8f77efba510"><ac:parameter ac:name="title">schema XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;schema</pre><pre>	attributeFormDefault = (qualified | unqualified) : unqualified<br />	blockDefault = (#all | List of (extension | restriction | substitution)) : ''</pre><pre>	elementFormDefault = (qualified | unqualified) : unqualified<br />	finalDefault = (#all | List of (extension | restriction)) : ''</pre><pre>	id = ID</pre><pre>	targetNamespace = anyURI</pre><pre>	version = token</pre><pre>	xml:lang = language</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: ((include | import | redefine | annotation)*, (((simpleType | complexType | group | attriuteGroup) | element | <br />attribute | notation), annotation*)*)</pre><pre>&lt;/schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ada6028f-0024-47d4-b823-7f6ac977c566"><ac:parameter ac:name="title">XML representation of the skeleton of a schema</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema</pre><pre>	xmlns:xs=&quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot;<br />	targetNamespace=&quot;<a href="http://www.example.com/example">http://www.example.com/example</a>&quot;&gt;</pre><pre>	…</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 128 Schema UML Model Example.png" /></ac:image></h6><h6 style="text-align: center;">schema UML model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="74262c93-d878-4502-b2ee-1d30d762d199"><ac:parameter ac:name="title">schema XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot;<br />xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot;<br />xmlns = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot;<br />attributeFormDefault = &quot;qualified&quot;<br />blockDefault = &quot;extension&quot;</pre><pre>elementFormDefault = &quot;unqualified&quot;<br />finalDefault = &quot;extension&quot;</pre><pre>targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot;<br />version = &quot;1.2&quot;</pre><pre>xml:lang = &quot;EN&quot; /&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459911 space=CDMP2024xR1 version=4 -->
## PAGE 00057: Selector and field

- page_id: `170459911`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459911/Selector+and+field
- version_number: 4
- version_date: `2024-05-08T14:25:26.009+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Sample of XML representations for the three kinds of identity-constraint definitions

36447579

#### CONTENT-COLUMN: Sample of XML representations for the three kinds of identity-constraint definitions

36447582

#### CONTENT-BLOCK: Sample of XML representations for the three kinds of identity-constraint definitions

36447580

Maps to UML TaggedValues named “selector” and “field” of a UML Attribute representing key, keyRef, or unique. The “selector” tag has a value representing the “xpath” and “field," a list of values representing the field “xpath”. ID values shall be skipped and annotation documentation will be applied to the tagged value according to the annotation rule. For the values annotation field, documentation shall be merged into one.

#### PANEL: selector and field mapping to UML attributes

selector and field mapping to UML attributes

```text
<selector	id = ID
```

```text
xpath = a subset of XPath expression, see below
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</selector>
```

```text
<field
```

```text
id = ID
```

```text
xpath = a subset of XPath expression, see below
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</field>
```

#### PANEL: selector and field XML code sample

selector and field XML code sample

```text
<xs:key name = "fullName">
```

```text
<xs:selector xpath=".//person"/>	<xs:field xpath="forename"/>	<xs:field xpath="surname"/></xs:key>
```

```text
<xs:keyref name="personRef" refer="fullName">	<xs:selector xpath=".//personPointer"/>	<xs:field xpath="@first"/>
```

```text
<xs:field xpath="@1ast"/>
```

```text
</xs:keyref>
```

```text
<xs:unique name="nearlyID">	<xs:selector xpath=".//*"/>	<xs:field xpath="@id"/></xs:unique>
```

##### XML representations for the three kinds of identity-constraint definitions

#### PANEL: Sample of XML representations for the three kinds of identity-constraint definitions

Sample of XML representations for the three kinds of identity-constraint definitions

```text
<xs:element name="state">
```

```text
<xs:complexType>
```

```text
<xs:sequence>
```

```text
<xs:element name="code" type="twoLetterCode"/>			<xs:element ref="vehicle" maxOccurs="unbounded"/>			<xs:element ref="person" maxOccurs="unbounded"/>		</xs:sequence>
```

```text
</xs:complexType>
```

```text
<xs:key name="reg"> <!-- vehicles are keyed by their plate within states -->
```

```text
<xs:selector xpath=".//vehicle"/>
```

```text
<xs:field xpath="@plateNumber"/>
```

```text
</xs:key>
```

```text
</xs:element><xs:element name="root">	<xs:complexType>
```

```text
<xs:sequence>
```

```text
…
```

```text
<xs:element ref="state" maxOccurs="unbounded"/>
```

```text
…
```

```text
</xs:sequence> 	</xs:complexType>
```

```text
<xs:key name="state"> <!-- states are keyed by their code --> 		<xs:selector xpath=" .//state"/>
```

```text
<xs:field xpath="code"/>
```

```text
</xs:key>
```

```text
<xs:keyref name="vehicleState" refer="state"> <!-- every vehicle refers to its state -->		<xs:selector xpath=".//vehicle"/>
```

```text
<xs:field xpath="@state"/>
```

```text
</xs:keyref>
```

```text
<xs:key name="regKey"> <!-- vehicles are keyed by a pair of state and plate-->
```

```text
<xs:selector xpath=".//vehicle"/>		<xs:field xpath="@state"/>
```

```text
<xs:field xpath="@plateNumber"/>	</xs:key>
```

```text
<xs:keyref name="carRef" refer="regKey"› <!-- people's cars are a reference -->
```

```text
<xs:selector xpath=".//car"/>		<xs:field xpath="@regState"/>		<xs:field xpath="@regPlate"/>	</xs:keyref>
```

```text
</xs:element>
```

```text
<xs:element name="person"›	<xs:complexType>
```

```text
<xs:seguence>
```

```text
...
```

```text
<xs:element name="car">				<xs:complexType>
```

```text
<xs:attribute name="regState" type="twoLetterCode"/>					<xs:attribute name="regPlate" type="xs:integer"/> 				</xs:complexType>
```

```text
</xs:element>
```

```text
</xs:sequence>
```

```text
</xs:complexType>
```

```text
</xs:element>
```

A state element is defined, which contains a code child and some vehicle and person children. A vehicle in turn has a plateNumber attribute, which is an integer, and a state attribute. State's code s are a key for them within the document. Vehicle's plateNumber s are a key for them within states, and state and plateNumber is asserted to be a key for vehicle within the document as a whole. Furthermore, a person element has an empty car child, with regState and regPlate attributes, which are then asserted together to refer to vehicles via the carRef constraint. The requirement that a vehicle's state match its containing state's code is not expressed here.

For selector and field UML model example, see [CONFLUENCE_PAGE title='Keyref' space='CDMP2024x Refresh1 Refresh1R1'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="1338a28a-78f4-46d6-b164-3bc40eeac190"><ac:parameter ac:name="id">36447579</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="f5dd89da-92cc-4986-b470-e6c6609db908"><ac:parameter ac:name="id">36447582</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="bb787edf-e238-4024-bb90-0f5487fb5fb7"><ac:parameter ac:name="id">36447580</ac:parameter><ac:rich-text-body><p>Maps to UML TaggedValues named “selector” and “field” of a UML Attribute representing key, keyRef, or unique. The “selector” tag has a value representing the “xpath” and “field,&quot; a list of values representing the field “xpath”. ID values shall be skipped and annotation documentation will be applied to the tagged value according to the annotation rule. For the values annotation field, documentation shall be merged into one.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3fa6b78b-691f-4bc5-b79f-7632618eb973"><ac:parameter ac:name="title">selector and field mapping to UML attributes</ac:parameter><ac:rich-text-body><pre>&lt;selector<br />	id = ID</pre><pre>	xpath = a subset of XPath expression, see below</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/selector&gt;</pre><pre>&lt;field</pre><pre>	id = ID</pre><pre>	xpath = a subset of XPath expression, see below</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/field&gt;</pre></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="df7e780d-8467-4baf-9ac2-96bbe7bfe986"><ac:parameter ac:name="title">selector and field XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;xs:key name = &quot;fullName&quot;&gt;</pre><pre>	&lt;xs:selector xpath=&quot;.//person&quot;/&gt;<br />	&lt;xs:field xpath=&quot;forename&quot;/&gt;<br />	&lt;xs:field xpath=&quot;surname&quot;/&gt;<br />&lt;/xs:key&gt;<br /><br /></pre><pre>&lt;xs:keyref name=&quot;personRef&quot; refer=&quot;fullName&quot;&gt;<br />	&lt;xs:selector xpath=&quot;.//personPointer&quot;/&gt;<br />	&lt;xs:field xpath=&quot;@first&quot;/&gt;</pre><pre>	&lt;xs:field xpath=&quot;@1ast&quot;/&gt;</pre><pre>&lt;/xs:keyref&gt;<br /><br /></pre><pre>&lt;xs:unique name=&quot;nearlyID&quot;&gt;<br />	&lt;xs:selector xpath=&quot;.//*&quot;/&gt;<br />	&lt;xs:field xpath=&quot;@id&quot;/&gt;<br />&lt;/xs:unique&gt;<br /><br /><br /></pre></ac:rich-text-body></ac:structured-macro><h3>XML representations for the three kinds of identity-constraint definitions</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="feefb804-d771-4c41-9118-d6d910f5a816"><ac:parameter ac:name="title">Sample of XML representations for the three kinds of identity-constraint definitions</ac:parameter><ac:rich-text-body><pre>&lt;xs:element name=&quot;state&quot;&gt;</pre><pre>	&lt;xs:complexType&gt;</pre><pre>		&lt;xs:sequence&gt;</pre><pre>			&lt;xs:element name=&quot;code&quot; type=&quot;twoLetterCode&quot;/&gt;<br />			&lt;xs:element ref=&quot;vehicle&quot; maxOccurs=&quot;unbounded&quot;/&gt;<br />			&lt;xs:element ref=&quot;person&quot; maxOccurs=&quot;unbounded&quot;/&gt;<br />		&lt;/xs:sequence&gt;</pre><pre>	&lt;/xs:complexType&gt;</pre><pre><br />	&lt;xs:key name=&quot;reg&quot;&gt; &lt;!-- vehicles are keyed by their plate within states --&gt;</pre><pre>		&lt;xs:selector xpath=&quot;.//vehicle&quot;/&gt;</pre><pre>		&lt;xs:field xpath=&quot;@plateNumber&quot;/&gt;</pre><pre>	&lt;/xs:key&gt;</pre><pre>&lt;/xs:element&gt;<br /><br />&lt;xs:element name=&quot;root&quot;&gt;<br />	&lt;xs:complexType&gt;</pre><pre>		&lt;xs:sequence&gt;</pre><pre>			…</pre><pre>			&lt;xs:element ref=&quot;state&quot; maxOccurs=&quot;unbounded&quot;/&gt;</pre><pre>			…</pre><pre>		&lt;/xs:sequence&gt; <br />	&lt;/xs:complexType&gt;<br /><br /></pre><pre>	&lt;xs:key name=&quot;state&quot;&gt; &lt;!-- states are keyed by their code --&gt; <br />		&lt;xs:selector xpath=&quot; .//state&quot;/&gt;</pre><pre>		&lt;xs:field xpath=&quot;code&quot;/&gt;</pre><pre>	&lt;/xs:key&gt;<br /><br /></pre><pre>	&lt;xs:keyref name=&quot;vehicleState&quot; refer=&quot;state&quot;&gt; &lt;!-- every vehicle refers to its state --&gt;<br />		&lt;xs:selector xpath=&quot;.//vehicle&quot;/&gt;</pre><pre>		&lt;xs:field xpath=&quot;@state&quot;/&gt;</pre><pre>	&lt;/xs:keyref&gt;<br /><br /></pre><pre>	&lt;xs:key name=&quot;regKey&quot;&gt; &lt;!-- vehicles are keyed by a pair of state and plate--&gt;</pre><pre>		&lt;xs:selector xpath=&quot;.//vehicle&quot;/&gt;<br />		&lt;xs:field xpath=&quot;@state&quot;/&gt;</pre><pre>		&lt;xs:field xpath=&quot;@plateNumber&quot;/&gt;<br />	&lt;/xs:key&gt;<br /><br /></pre><pre>	&lt;xs:keyref name=&quot;carRef&quot; refer=&quot;regKey&quot;› &lt;!-- people's cars are a reference --&gt;</pre><pre>		&lt;xs:selector xpath=&quot;.//car&quot;/&gt;<br />		&lt;xs:field xpath=&quot;@regState&quot;/&gt;<br />		&lt;xs:field xpath=&quot;@regPlate&quot;/&gt;<br />	&lt;/xs:keyref&gt;</pre><pre>&lt;/xs:element&gt;<br /><br /></pre><pre>&lt;xs:element name=&quot;person&quot;›<br />	&lt;xs:complexType&gt;</pre><pre>		&lt;xs:seguence&gt;</pre><pre>...</pre><pre>			&lt;xs:element name=&quot;car&quot;&gt;<br />				&lt;xs:complexType&gt;</pre><pre>					&lt;xs:attribute name=&quot;regState&quot; type=&quot;twoLetterCode&quot;/&gt;<br />					&lt;xs:attribute name=&quot;regPlate&quot; type=&quot;xs:integer&quot;/&gt; <br />				&lt;/xs:complexType&gt;</pre><pre>			&lt;/xs:element&gt;</pre><pre>		&lt;/xs:sequence&gt;</pre><pre>	&lt;/xs:complexType&gt;</pre><pre>&lt;/xs:element&gt;</pre></ac:rich-text-body></ac:structured-macro><p>A state element is defined, which contains a code child and some vehicle and person children. A vehicle in turn has a plateNumber attribute, which is an integer, and a state attribute. State's code s are a key for them within the document. Vehicle's plateNumber s are a key for them within states, and state and plateNumber is asserted to be a key for vehicle within the document as a whole. Furthermore, a person element has an empty car child, with regState and regPlate attributes, which are then asserted together to refer to vehicles via the carRef constraint. The requirement that a vehicle's state match its containing state's code is not expressed here.</p><p>For selector and field UML model example, see <ac:link><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1R1" ri:content-title="Keyref" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459753 space=CDMP2024xR1 version=5 -->
## PAGE 00058: Sequences and autoincrement columns

- page_id: `170459753`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459753/Sequences+and+autoincrement+columns
- version_number: 5
- version_date: `2024-05-08T13:52:09.158+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support > Database modeling
- labels: []

### NORMALIZED CONTENT

- SQL Sequence is modeled as UML Property with «Sequence» stereotype applied. For the sake of compactness, sequences are displayed with the «seq» keyword (instead of the long form - «Sequence») on the diagram.
- Autoincrement parameters (start value, increment, etc.) data is stored as a separate model element - UML OpaqueExpression, with «IdentitySpecifier» stereotype applied. This element is set as defaultValue of the Property - either sequence property (when standalone sequences are modeled) or column property (when autoincrement table columns are modeled).

SQL has facilities to generate sequences of numbers (0, 1, 2, 3, ...). These sequences are often used to fill in values for identifier columns - to uniquely number the row data in the table. There are 2 separate facilities.

- Standalone sequence object. This generator is not tied to any other object. Programer must explicitly query it to get the next value from the sequence and then use the retrieved value appropriately (usually in the INSERT statement to insert value for id column). Usually there are separate sequences for each table; sometimes the same sequence is reused for several columns.
- Autoincrement columns. Column of the table can be designated as autoincrement. When row is inserted into the table, if value of such column is not explicitly provided, one is generated automatically.

###### [IMAGE alt='' src=''] Example of sequence and autoincrement column modeling.

Cameo Data Modeler has modeling support for both kinds of sequences.

To create a standalone sequence

Do one of the following:

- Select the GLOBALS element shape on a diagram pane and click an appropriate smart manipulation button.
- Right-click the GLOBALS element in the Containment tree and on its shortcut menu, select New Element > Sequence .

Since a standalone sequence is modeled as a UML Property, it cannot be placed directly into the Schema package.

Autoincrement columns are also supported. To mark a column as autoincrement, you must switch the **Default Value**property value type from value expression to identity specifier.

To mark a column as autoincrement

1. Open the column Specification window.
2. Select the Default Value property.
3. Click the black-arrowed button next to the property value and select Value Specification > IdentitySpecifier as shown in the following figure.

[IMAGE alt='' src='']

###### Marking column as autoincrement.

After the switching, the Autoincrement property group appears in the Specification window of the column allowing to specify autoincrement data (start value, increment, etc.).

###### [IMAGE alt='' src='']

###### Additional properties in autoincrement column’s Specification window.

Besides the standard SQL element properties and sequences, an autoincrement column has the following properties available in the **Autoincrement**property group of the Specification window.

| Property name | Description |
| --- | --- |
| Start Value | Starting value of the sequence counter. |
| Increment | Delta value of the sequence counter (can be negative - to count down). |
| Minimum | Lower bound of the counter (if any). |
| Maximum | Upper bound of the counter (if any) |
| Cycle Option | The counter can “wrap around” when it reaches the maximum (or minimum - for downwards counters) |

Additionally, sequence has an **Identity**field and column has the **Default Value**field, where textual representation of the counter options can be entered. This feature can be used for nice displaying of the counter configuration in the diagrams (the start, inc, min, max field data is normally not visible in the diagram). Some notation convention should be adopted how to map the counter data into the text representation. For example, it could be: {<start>, <inc>, <min>-<max>, <c>}. Then the counter from 0 with +1 increment, min max of 0 and 1000 and cycle option would be displayed as “{0, +1, 0-1000, C}” string. At the moment this text representation is not automatically connected to the counter field values, so synchronization has to be done by hand.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e93a6b90-5be5-4eb3-8e7e-f7c712cf8653"><ac:rich-text-body><ul><li>SQL Sequence is modeled as UML Property with «Sequence» stereotype applied. For the sake of compactness, sequences are displayed with the «seq» keyword (instead of the long form - «Sequence») on the diagram.</li><li>Autoincrement parameters (start value, increment, etc.) data is stored as a separate model element - UML OpaqueExpression, with «IdentitySpecifier» stereotype applied. This element is set as <strong>defaultValue </strong>of the Property - either sequence property (when standalone sequences are modeled) or column property (when autoincrement table columns are modeled).</li></ul></ac:rich-text-body></ac:structured-macro><p>SQL has facilities to generate sequences of numbers (0, 1, 2, 3, ...). These sequences are often used to fill in values for identifier columns - to uniquely number the row data in the table. There are 2 separate facilities.</p><ul><li>Standalone sequence object. This generator is not tied to any other object. Programer must explicitly query it to get the next value from the sequence and then use the retrieved value appropriately (usually in the INSERT statement to insert value for id column). Usually there are separate sequences for each table; sometimes the same sequence is reused for several columns.</li><li>Autoincrement columns. Column of the table can be designated as autoincrement. When row is inserted into the table, if value of such column is not explicitly provided, one is generated automatically.</li></ul><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 23 Example of Sequence and Autoincrement Column Modeling.png" /></ac:image> Example of sequence and autoincrement column modeling.</h6><p>Cameo Data Modeler has modeling support for both kinds of sequences.</p><p><br /></p><p>To create a standalone sequence</p><hr /><p style="margin-left: 30.0px;">Do one of the following:</p><ul><li>Select the GLOBALS element shape on a diagram pane and click an appropriate smart manipulation button.</li><li>Right-click the GLOBALS element in the Containment tree and on its shortcut menu, select <strong>New Element </strong>&gt; <strong>Sequence</strong>.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3bfddfcb-79c3-4f65-86ef-97319f0cca5d"><ac:rich-text-body><p>Since a standalone sequence is modeled as a UML Property, it cannot be placed directly into the Schema package.</p></ac:rich-text-body></ac:structured-macro><p>Autoincrement columns are also supported. To mark a column as autoincrement, you must switch the <strong>Default Value </strong>property value type from value expression to identity specifier.</p><p><br /></p><p>To mark a column as autoincrement</p><hr /><ol><li>Open the column Specification window.</li><li>Select the <strong>Default Value </strong>property.</li><li>Click the black-arrowed button next to the property value and select <strong>Value Specification </strong>&gt;<strong> IdentitySpecifier </strong>as shown in the following figure.</li></ol><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 24 Marking Column as Autoincrement.png" /></ac:image></p><h6>Marking column as autoincrement.</h6><p>After the switching, the Autoincrement property group appears in the Specification window of the column allowing to specify autoincrement data (start value, increment, etc.).</p><h6 style="text-align: left;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 25 Additional Properties in Autoincrement Column’s Specification Window.png" /></ac:image></h6><h6 style="text-align: left;">Additional properties in autoincrement column’s Specification window.</h6><p style="text-align: left;"><br /></p><p style="text-align: left;">Besides the standard SQL element properties and sequences, an autoincrement column has the following properties available in the <strong>Autoincrement </strong>property group of the Specification window.</p><table class="relative-table wrapped" style="width: 85.299%;"><colgroup><col style="width: 13.0577%;" /><col style="width: 86.9423%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td>Start Value</td><td>Starting value of the sequence counter.</td></tr><tr><td>Increment</td><td>Delta value of the sequence counter (can be negative - to count down).</td></tr><tr><td>Minimum</td><td>Lower bound of the counter (if any).</td></tr><tr><td>Maximum</td><td>Upper bound of the counter (if any)</td></tr><tr><td>Cycle Option</td><td>The counter can “wrap around” when it reaches the maximum (or minimum - for downwards counters)</td></tr></tbody></table><p>Additionally, sequence has an <strong>Identity </strong>field and column has the <strong>Default Value </strong>field, where textual representation of the counter options can be entered. This feature can be used for nice displaying of the counter configuration in the diagrams (the start, inc, min, max field data is normally not visible in the diagram). Some notation convention should be adopted how to map the counter data into the text representation. For example, it could be: {&lt;start&gt;, &lt;inc&gt;, &lt;min&gt;-&lt;max&gt;, &lt;c&gt;}. Then the counter from 0 with +1 increment, min max of 0 and 1000 and cycle option would be displayed as “{0, +1, 0-1000, C}” string. At the moment this text representation is not automatically connected to the counter field values, so synchronization has to be done by hand.</p>
````

<!--NOMAGIC_PAGE id=170459848 space=CDMP2024xR1 version=1 -->
## PAGE 00059: SimpleType

- page_id: `170459848`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459848/SimpleType
- version_number: 1
- version_date: `2023-09-21T12:47:00.318+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to UML Class with stereotype XSDsimpleType.

#### PANEL: XML representation summary, simpleType Element information item

XML representation summary, simpleType Element information item

```text
<simpleType
```

```text
final = (#all | (list | union | restriction))
```

```text
id = ID
```

```text
name = NCName
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, (restriction | list | union))
```

```text
</simpleType>
```

```text
<restriction
```

```text
base = OName
```

```text
id = ID
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, (simpleType?, (minExclusive | minlnclusive | maxExclusive | maxInclusive | totalDigits | fractionDigits | length | minLength | maxLength | whiteSpace | pattern)*))
```

```text
</restriction>
```

```text
<list
```

```text
id = ID
```

```text
itemType = OName
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, (simpleType?))
```

```text
</list>
```

```text
<union 	id = ID
```

```text
memberTypes = List of OName
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, (simpleType*))
```

```text
</union>
```

#### PANEL: XML representation of a simpleType definition

XML representation of a simpleType definition

```text
<xs:simpleType name="farenheitWaterTemp"›	<xs:restriction base="xs:number">		<xs:fractionDigits value="2"/>		<xs:minExclusive value="0.00"/>		<xs:maxExclusive value="100.00"/>	</xs:restriction></xs:simpleType>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to UML Class with stereotype XSDsimpleType.</p><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ba971af8-171d-4ec3-a246-8a549e551cef"><ac:parameter ac:name="title">XML representation summary, simpleType Element information item</ac:parameter><ac:rich-text-body><pre>&lt;simpleType</pre><pre>	final = (#all | (list | union | restriction))</pre><pre>	id = ID</pre><pre>	name = NCName</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, (restriction | list | union))</pre><pre>&lt;/simpleType&gt;</pre><pre>&lt;restriction</pre><pre>	base = OName</pre><pre>	id = ID</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, (simpleType?, (minExclusive | minlnclusive | maxExclusive | maxInclusive | totalDigits | fractionDigits | length | minLength | maxLength | whiteSpace | pattern)*))</pre><pre>&lt;/restriction&gt;</pre><pre>&lt;list</pre><pre>	id = ID</pre><pre>	itemType = OName</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, (simpleType?))</pre><pre>&lt;/list&gt;</pre><pre>&lt;union <br />	id = ID</pre><pre>	memberTypes = List of OName</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, (simpleType*))</pre><pre>&lt;/union&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="63e78ee9-fc70-4303-9ca7-35ce6563cb41"><ac:parameter ac:name="title">XML representation of a simpleType definition</ac:parameter><ac:rich-text-body><pre class="auto-cursor-target">&lt;xs:simpleType name=&quot;farenheitWaterTemp&quot;›<br />	&lt;xs:restriction base=&quot;xs:number&quot;&gt;<br />		&lt;xs:fractionDigits value=&quot;2&quot;/&gt;<br />		&lt;xs:minExclusive value=&quot;0.00&quot;/&gt;<br />		&lt;xs:maxExclusive value=&quot;100.00&quot;/&gt;<br />	&lt;/xs:restriction&gt;<br />&lt;/xs:simpleType&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459738 space=CDMP2024xR1 version=6 -->
## PAGE 00060: SQL diagrams

- page_id: `170459738`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459738/SQL+diagrams
- version_number: 6
- version_date: `2024-05-08T13:49:24.226+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support
- labels: []

### NORMALIZED CONTENT

Cameo Data Modeler provides **SQL Diagram**, a specialized diagram for database modeling that enables you to create and depict various SQL elements. It is located under the **Data Modeling**diagram subgroup.

In addition to the main SQL diagram, there is a slightly modified diagram for Oracle databases, **Oracle SQL Diagram**. It is located under the same **Data Modeling**diagram subgroup. This diagram is only slightly modified. It has an additional diagram button for Materialized View modeling. Other than that, it is identical to the main SQL diagram. If you are not modeling materialized views, you can freely use the generic diagram type instead of the specialized one for Oracle modeling.

##### **Crow’s Foot Notation in SQL Diagrams**

Once you apply the Cameo Data Modeler plugin to MagicDraw, you can display the crow’s foot notation or use standard UML notation of associations (displaying multiplicities in text format) in the SQL diagram.

To display Multiplicities or crow’s foot notation in a SQL diagram

1. Create the SQL diagram.
2. Draw two tables.
3. Create columns for the tables and some of them as primary keys.
4. Connect the table elements with the Foreign Key relationship.
5. Define Name , PK , and FK in the open Foreign Key dialog box.
6. Open the Project Options dialog box.
7. Select the General project options branch.
8. Change the Show relationship ends as property to either No special notation or Crow’s feet . Multiplicities or crow’s foot notation in the following figures will then be displayed on the Foreign Key ends.

[IMAGE alt='' src='']

###### Multiplicities on a Foreign Key relationship in an SQL diagram.

[IMAGE alt='' src='']

###### Crow’s foot notation for a Foreign Key relationship in an SQL diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cameo Data Modeler provides <strong>SQL Diagram</strong>, a specialized diagram for database modeling that enables you to create and depict various SQL elements. It is located under the <strong>Data Modeling </strong>diagram subgroup.</p><p>In addition to the main SQL diagram, there is a slightly modified diagram for Oracle databases, <strong>Oracle SQL Diagram</strong>. It is located under the same <strong>Data Modeling </strong>diagram subgroup. This diagram is only slightly modified. It has an additional diagram button for Materialized View modeling. Other than that, it is identical to the main SQL diagram. If you are not modeling materialized views, you can freely use the generic diagram type instead of the specialized one for Oracle modeling.</p><h3><strong>Crow’s Foot Notation in SQL Diagrams</strong></h3><p>Once you apply the Cameo Data Modeler plugin to MagicDraw, you can display the crow’s foot notation or use standard UML notation of associations (displaying multiplicities in text format) in the SQL diagram.</p><p>To display Multiplicities or crow’s foot notation in a SQL diagram</p><hr /><ol><li>Create the SQL diagram.</li><li>Draw two tables.</li><li>Create columns for the tables and some of them as primary keys.</li><li>Connect the table elements with the Foreign Key relationship.</li><li>Define <strong>Name</strong>, <strong>PK</strong>, and <strong>FK </strong>in the open <strong>Foreign Key </strong>dialog box.</li><li>Open the <strong>Project Options </strong>dialog box.</li><li>Select the <strong>General project options </strong>branch.</li><li>Change the <strong>Show relationship ends as </strong>property to either <strong>No special notation </strong>or <strong>Crow’s feet</strong>. Multiplicities or crow’s foot notation in the following figures will then be displayed on the Foreign Key ends.</li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 14 Multiplicities on Foreign Key Relationship in SQL Diagram.png" /></ac:image></p><h6 style="text-align: center;">Multiplicities on a Foreign Key relationship in an SQL diagram.</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 15 Crow’s Foot Notation for Foreign Key Relationship in SQL Diagram.png" /></ac:image></p><h6 style="text-align: center;">Crow’s foot notation for a Foreign Key relationship in an SQL diagram.</h6>
````

<!--NOMAGIC_PAGE id=170459803 space=CDMP2024xR1 version=5 -->
## PAGE 00061: SQL to UML transformation

- page_id: `170459803`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459803/SQL+to+UML+transformation
- version_number: 5
- version_date: `2024-05-08T14:17:40.576+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Transformations
- labels: []

### NORMALIZED CONTENT

33727203

33727205

33727204

SQL models and diagrams will be transformed into the platform-independent UML models and UML class diagrams. You can apply the SQL to UML transformation to SQL models of any database flavor.

##### **T****yp****e mapping**

After transformation, SQL types should be converted to UML types if types are specified in the SQL model for elements. There is a type mapping from SQL types to UML types.

Mapping rules are based on dependencies, which contain the **SQL to UML Type Map**profile. This profile is automatically attached when SQL to UML transformation is performed.

##### **T****ransformatio****n results**

The SQL stereotypes are discarded from tables, views, fields, and associations (except the PK stereotype). Views are discarded in a transformed class diagram.

There are additional properties to choose for SQL to UML transformation in **Model Transformation Wizard**. For more information about the wizard, see [CONFLUENCE_PAGE title='Model Transformation Wizard' space='MD2024x Refresh1 Refresh1 Refresh1'] in the MagicDraw User Guide.

[IMAGE alt='' src='']

###### Model transformation wizard for SQL to UML transformation with Specify transformation details wizard step.

| Option name | Type | Description |
| --- | --- | --- |
| Use PK | Check box | If set to “true”, appropriate columns with the primary key stereotype are marked after transformation. |
| Use IE | Check box | If set to “true”, indexed columns with the inverted entity stereotype are marked after transformation. |
| Use AK | Check box | If set to “true”, unique columns with the alternative key stereotype are marked after transformation. |

The «IE» stereotype is applied to the columns in the UML model from *indexes*in the SQL.

The «AK» stereotypes are applied to the columns in the UML model from *unique*constraints in the SQL.

If the *unique*or *index*of the SQL contains more than one column, the **group**tag is created on the corresponding columns. The value of the tag is the name of the *unique / index*.

If the PK, *unique*constraint or *index*of the SQL contains more than one column, the **orderInXXGroup**tag is created on the corresponding columns. The value of the tag is the place number of the column in the PK, unique constraint or index (first column gets tag value=1, second column - 2, etc).

###### [IMAGE alt='' src='']TBD 3 SQL before transformation.

###### [IMAGE alt='' src='']TBD 3 SQL after transformation.

There are some foreign key cases when an association with multiplicities is created in a class diagram after transformation, as shown below:****

###### **Transforming foreign key, when the «unique» stereotype is set**

###### [IMAGE alt='' src='']Transforming foreign key when the «unique» stereotype is set before transformation.

###### [IMAGE alt='' src='']Transforming foreign key when the «unique» stereotype is set after transformation.

###### **Transforming foreign key, when the «not null» stereotype is set**

###### [IMAGE alt='' src='']Transforming foreign key when the «not null» stereotype is set before transformation.

###### [IMAGE alt='' src='']Transforming foreign key when the «not null» stereotype is set after transformation.

###### **Transforming foreign key, when the «null» stereotype is set**

###### [IMAGE alt='' src='']Transforming foreign key when the «null» stereotype is set before transformation.

###### [IMAGE alt='' src='']Transforming foreign key when the «null» stereotype is set after transformation.

###### **Transforming foreign key, when the «unique» and the «not null» stereotypes are set**

[IMAGE alt='' src='']

###### Transforming foreign key, when the «unique» and the «not null» stereotypes are set before transformation.

###### [IMAGE alt='' src='']Transforming foreign key, when the «unique» and the «not null» stereotypes are set after transformation.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="bef0c5d5-e063-4249-abaa-2b6cdca9a8a1"><ac:parameter ac:name="id">33727203</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="6f54c671-4d3d-4494-876c-7024358c120a"><ac:parameter ac:name="id">33727205</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e8c413c6-2ec7-41fb-a1a0-ab8b238c9909"><ac:parameter ac:name="id">33727204</ac:parameter><ac:rich-text-body><p>SQL models and diagrams will be transformed into the platform-independent UML models and UML class diagrams. You can apply the SQL to UML transformation to SQL models of any database flavor.</p><h3><strong>T</strong><strong>yp</strong><strong>e mapping</strong></h3><p>After transformation, SQL types should be converted to UML types if types are specified in the SQL model for elements. There is a type mapping from SQL types to UML types.</p><p>Mapping rules are based on dependencies, which contain the <strong>SQL to UML Type Map </strong>profile. This profile is automatically attached when SQL to UML transformation is performed.</p><h3><strong>T</strong><strong>ransformatio</strong><strong>n results</strong></h3><p>The SQL stereotypes are discarded from tables, views, fields, and associations (except the PK stereotype). Views are discarded in a transformed class diagram.</p><p>There are additional properties to choose for SQL to UML transformation in <strong>Model Transformation Wizard</strong>. For more information about the wizard, see <ac:link><ri:page ri:space-key="MD2024x Refresh1 Refresh1 Refresh1" ri:content-title="Model Transformation Wizard" /></ac:link> in the MagicDraw User Guide.</p><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 42 Model Transformation Wizard for SQL to UML Transformation with Specify Transformation Details Wizard Step.png" /></ac:image></p><h6 style="text-align: center;">Model transformation wizard for SQL to UML transformation with Specify transformation details wizard step.</h6><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 22.0611%;" /><col style="width: 20.1236%;" /><col style="width: 57.8153%;" /></colgroup><tbody><tr><th>Option name</th><th>Type</th><th>Description</th></tr><tr><td><strong>Use PK</strong></td><td>Check box</td><td><p>If set to “true”, appropriate columns with the primary key stereotype are marked after transformation.</p></td></tr><tr><td><strong>Use IE</strong></td><td>Check box</td><td>If set to “true”, indexed columns with the inverted entity stereotype are marked after transformation.</td></tr><tr><td><strong>Use AK</strong></td><td>Check box</td><td>If set to “true”, unique columns with the alternative key stereotype are marked after transformation.</td></tr></tbody></table><p class="auto-cursor-target">The «IE» stereotype is applied to the columns in the UML model from <em>indexes </em>in the SQL.</p><p>The «AK» stereotypes are applied to the columns in the UML model from <em>unique </em>constraints in the SQL.</p><p>If the <em>unique </em>or <em>index </em>of the SQL contains more than one column, the <strong>group </strong>tag is created on the corresponding columns. The value of the tag is the name of the <em>unique / index</em>.</p><p>If the PK, <em>unique </em>constraint or <em>index </em>of the SQL contains more than one column, the <strong>orderInXXGroup </strong>tag is created on the corresponding columns. The value of the tag is the place number of the column in the PK, unique constraint or index (first column gets tag value=1, second column - 2, etc).</p><p><br /></p><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="(1) TBD 3 SQL Screenshots before Transformation.png" /></ac:image>TBD 3 SQL before transformation.</h6><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="(2) TBD 3 SQL Screenshots after Transformation.png" /></ac:image>TBD 3 SQL after transformation.</h6><p><br /></p><p>There are some foreign key cases when an association with multiplicities is created in a class diagram after transformation, as shown below:<strong><br /></strong></p><h4><strong>Transforming foreign key, when the «unique» stereotype is set</strong></h4><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="(3) Transforming foreign key when the «unique» stereotype is set (before transformation).png" /></ac:image>Transforming foreign key when the «unique» stereotype is set before transformation.</h6><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="(4) Transforming foreign key when the «unique» stereotype is set (after transformation).png" /></ac:image>Transforming foreign key when the «unique» stereotype is set after transformation.</h6><h4 style="text-align: left;"><strong>Transforming foreign key, when the «not null» stereotype is set</strong></h4><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="(5) Transforming foreign key when the «not null» stereotype is set before transformation.png" /></ac:image>Transforming foreign key when the «not null» stereotype is set before transformation.</h6><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="(6) Transforming foreign ke, when the «not null» stereotype is set after transformation.png" /></ac:image>Transforming foreign key when the «not null» stereotype is set after transformation.</h6><h4 style="text-align: left;"><strong>Transforming foreign key, when the «null» stereotype is set</strong></h4><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="(7) Transforming foreign key when the «null» stereotype is set before transformation.png" /></ac:image>Transforming foreign key when the «null» stereotype is set before transformation.</h6><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="(8) Transforming foreign key when the «null» stereotype is set after transformation.png" /></ac:image>Transforming foreign key when the «null» stereotype is set after transformation.</h6><h4><strong>Transforming foreign key, when the «unique» and the «not null» stereotypes are set</strong></h4><p><ac:image ac:height="250"><ri:attachment ri:filename="(9) Transforming foreign key, when the «unique» and the «not null» stereotypes are set before transformation.png" /></ac:image></p><h6 style="text-align: center;">Transforming foreign key, when the «unique» and the «not null» stereotypes are set before transformation.</h6><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="(10) Transforming foreign key, when the «unique» and the «not null» stereotypes are set after transformation.png" /></ac:image>Transforming foreign key, when the «unique» and the «not null» stereotypes are set after transformation.</h6></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459770 space=CDMP2024xR1 version=1 -->
## PAGE 00062: Supported SQL statements

- page_id: `170459770`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459770/Supported+SQL+statements
- version_number: 1
- version_date: `2023-09-21T12:46:57.272+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support > Database code engineering
- labels: []

### NORMALIZED CONTENT

This section lists the SQL statements supported in the Cameo Data Modeler plugin. They are parsed and mapped into model constructs.

The following table provides SQL2 SQL schema statements and their support status in the Cameo Data Modeler plugin**. Yes**indicates that a statement can be generated into a DLL script from model constructs and reverse engineered from a script into model constructs.

| SQL schema statement | Supported | (Yes/No) |
| --- | --- | --- |
| SQL schema definition statement | Schema definition | Yes |
| Table definition | Yes |  |
| View definition | Yes |  |
| Alter table statement | Yes |  |
| Grant statement | No |  |
| Domain definition | No |  |
| Assertion definition | No |  |
| Character set definition | No |  |
| Collation definition | No |  |
| Translation definition | No |  |
| SQL schema manipulation statement | Drop table statement | Yes |
| Drop view statement | Yes |  |
| Revoke statement | No |  |
| Alter domain statement | No |  |
| Drop assertion statement | No |  |
| Drop domain statement | No |  |
| Drop character set statement | No |  |
| Drop collation statement | No |  |
| Drop translation statement | No |  |

Some SQL schema statements (e.g. schema definition, table definition) allow implicit catalog names and unqualified schema names. In addition to SQL schema statements, the following SQL session statements must be supported:

- Set catalog statement - sets the current default catalog name.
- Set schema statement - sets the current default unqualified schema name.

Cameo Data Modeler supports the following widely used dialect statements that are not part of SQL2:

- Database definition statement (CREATE DATABASE) that creates a database
- Index statements (CREATE INDEX, DROP INDEX) that create or remove an index on a table
- Trigger statements (CREATE TRIGGER, DROP TRIGGER) that create or remove trigger(s) on a table

The following table provides details on mapping on the supported SQL schema manipulation statements into SQL constructs.

| DDL Statement or Concept | Action, model Item | Description | Visible |
| --- | --- | --- | --- |
| Alter table statement | Modify class | Elements: table name and alter table action. Alter table action – one of: add column, add table constraint, alter column, drop table constraint, drop column. | Yes |
| Add column definition | Define attribute | Elements: column definition. | Yes |
| Add table constraint definition | Define method | Elements: table constraint definition. | Yes |
| Alter column definition | Modify attribute | Elements: mandatory column name, default clause (for add default statement only). | Yes |
| Drop table constraint definition | Delete method | Elements: constraint name, drop behavior | Yes |
| Drop column definition | Delete attribute | Elements: column name, drop behavior | Yes |
| Drop schema statement | Delete package | Elements: schema name, drop behavior | Yes |
| Drop table statement | Delete class | Elements: table name, drop behavior | Yes |
| Drop view statement | Delete class | Elements: table name, drop behavior | Yes |
| Drop behavior | Action property | Modifiers: CASCADE, RESTRICT | No |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section lists the SQL statements supported in the Cameo Data Modeler plugin. They are parsed and mapped into model constructs.</p><p>The following table provides SQL2 SQL schema statements and their support status in the Cameo Data Modeler plugin<strong>. Yes </strong>indicates that a statement can be generated into a DLL script from model constructs and reverse engineered from a script into model constructs.</p><table class="relative-table" style="width: 99.9451%;"><colgroup><col style="width: 24.1424%;" /><col style="width: 32.1142%;" /><col style="width: 43.7434%;" /></colgroup><tbody><tr><th><strong>SQL schema statement</strong></th><th><strong>Supported</strong></th><th><strong>(Yes/No)</strong></th></tr><tr><td rowspan="10"><strong>SQL schema definition statement</strong><br /><br /><br /><br /><br /><br /><br /><br /><br /></td><td>Schema definition</td><td>Yes</td></tr><tr><td>Table definition</td><td>Yes</td></tr><tr><td>View definition</td><td>Yes</td></tr><tr><td>Alter table statement</td><td>Yes</td></tr><tr><td>Grant statement</td><td>No</td></tr><tr><td>Domain definition</td><td>No</td></tr><tr><td>Assertion definition</td><td>No</td></tr><tr><td>Character set definition</td><td>No</td></tr><tr><td>Collation definition</td><td>No</td></tr><tr><td>Translation definition</td><td>No</td></tr><tr><td rowspan="9"><strong>SQL schema manipulation statement</strong><br /><br /><br /><br /><br /><br /><br /><br /><br /></td><td>Drop table statement</td><td>Yes</td></tr><tr><td>Drop view statement</td><td>Yes</td></tr><tr><td>Revoke statement</td><td>No</td></tr><tr><td>Alter domain statement</td><td>No</td></tr><tr><td>Drop assertion statement</td><td>No</td></tr><tr><td>Drop domain statement</td><td>No</td></tr><tr><td>Drop character set statement</td><td>No</td></tr><tr><td>Drop collation statement</td><td>No</td></tr><tr><td>Drop translation statement</td><td>No</td></tr></tbody></table><p>Some SQL schema statements (e.g. schema definition, table definition) allow implicit catalog names and unqualified schema names. In addition to SQL schema statements, the following SQL session statements must be supported:</p><ul><li>Set catalog statement - sets the current default catalog name.</li><li>Set schema statement - sets the current default unqualified schema name.</li></ul><p>Cameo Data Modeler supports the following widely used dialect statements that are not part of SQL2:</p><ul><li>Database definition statement (CREATE DATABASE) that creates a database</li><li>Index statements (CREATE INDEX, DROP INDEX) that create or remove an index on a table</li><li>Trigger statements (CREATE TRIGGER, DROP TRIGGER) that create or remove trigger(s) on a table</li></ul><p>The following table provides details on mapping on the supported SQL schema manipulation statements into SQL constructs.</p><table class="relative-table" style="width: 99.9451%;"><colgroup><col style="width: 20.8027%;" /><col style="width: 14.9844%;" /><col style="width: 54.9359%;" /><col style="width: 9.27695%;" /></colgroup><tbody><tr><th><p><strong>DDL Statement or Concept</strong></p></th><th><p><strong>Action, model Item<br /></strong></p><p><br /></p></th><th><p><strong>Description</strong></p></th><th><p><strong>Visible</strong></p></th></tr><tr><td><strong>Alter table statement</strong></td><td>Modify class</td><td>Elements: table name and alter table action. Alter table action – one of: add column, add table constraint, alter column, drop table constraint, drop column.</td><td>Yes</td></tr><tr><td><strong>Add column definition</strong></td><td>Define attribute</td><td>Elements: column definition.</td><td>Yes</td></tr><tr><td><p><strong>Add table constraint definition</strong></p></td><td>Define method</td><td>Elements: table constraint definition.</td><td>Yes</td></tr><tr><td><strong>Alter column definition</strong></td><td>Modify attribute</td><td>Elements: mandatory column name, default clause (for add default statement only).</td><td>Yes</td></tr><tr><td><p><strong>Drop table constraint definition</strong></p></td><td>Delete method</td><td>Elements: constraint name, drop behavior</td><td>Yes</td></tr><tr><td><strong>Drop column definition </strong></td><td>Delete attribute</td><td>Elements: column name, drop behavior</td><td>Yes</td></tr><tr><td><strong>Drop schema statement</strong></td><td>Delete package</td><td>Elements: schema name, drop behavior</td><td>Yes</td></tr><tr><td><strong>Drop table statement</strong></td><td>Delete class</td><td>Elements: table name, drop behavior</td><td>Yes</td></tr><tr><td><strong>Drop view statement</strong></td><td>Delete class</td><td>Elements: table name, drop behavior</td><td>Yes</td></tr><tr><td><strong>Drop behavior</strong></td><td>Action property</td><td>Modifiers: CASCADE, RESTRICT</td><td>No</td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459747 space=CDMP2024xR1 version=5 -->
## PAGE 00063: Tables, columns, views, and columns

- page_id: `170459747`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459747/Tables+columns+views+and+columns
- version_number: 5
- version_date: `2024-05-08T13:50:09.015+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support > Database modeling
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

56082483

#### CONTENT-COLUMN: Note

56082487

56082480

**On this page**

42

#### CONTENT-BLOCK: Note

56082486

Tables and their constituent columns are the main elements for describing database data structures. Table stores multiple rows of data each consisting of several columns. Each cell holds one data value (or is empty). All values of one column are of the same type. Correspondingly each table description consists of the table name and a set of column descriptions. Additionally there are various kinds of constraints (including the all- important primary key and foreign key constraints), that can be applied on tables and triggers, specifying additional actions to be performed during data manipulation.

See [CONFLUENCE_PAGE title='Constraints' space='CDMP2024x Refresh1 Refresh1 Refresh1R1'] and [Triggers](https://docs.nomagic.com/display/CDMP2024x Refresh1 Refresh1 Refresh1/Constraints#Constraints-Triggers) for triggers. There can be various kinds of tables as follows.

33

The following figure illustrates various kinds of tables that can be modeled on the diagram.

[IMAGE alt='' src='']

###### Various kinds of tables: persistent tables, temporary tables, and views.

Tables can have generalization relationships between them. These relationships correspond to the following SQL syntax in the create table statement.

```text
OF  [UNDER ]]]>
```

There can be at most 1 outgoing generalization. Generalizations are not widely supported in database management systems. As of v17.0.1 Cameo Data Modeler supports modeling of these structures. Generation of corresponding script code is not supported yet.

##### **Persistent table**

#### NOTE: Note

Note

SQL Persistent Table is modeled as UML Class with the «Persistent- Table» stereotype applied. For the sake of compactness, these tables are displayed with the «table» keyword (instead of the long form - «PersistentTable») on the diagram.

Persistent table is the most often used kind of table. Besides the standard SQL element properties, persistent table has the following properties available in the Specification window (these properties are only available in Expert mode).

| Property name | Description |
| --- | --- |
| User-defined type | Points to structured user defined type, which serves as a base for the row type of the table. |
| Supertable | Points to the parent (base) table. Can only be used together with userdefined type. |
| Self Ref Column Generation | Describes the self-referencing column generation options. Can only be used together with user-defined type. Corresponds to the following subclause of SQL create table statement [SYSTEM GENERATED\|USER GENERATED\|DERIVED]]]> |
| ReferencingForeign Keys | This is back reference from foreign keys, referencing this table. This field is for information purposes only. If you want to change it, change Referenced Table field of the foreign key instead. |
| Insertable | These are two derived (non editable) fields, describing table data editing capabilities. At the moment calculation of these properties is not implemented - they are always set to false. |
| Updatable |  |

##### Temporary table

#### NOTE: Note

Note

SQL Temporary Table is modeled as UML Class with the «Temporar- yTable» stereotype applied. For the sake of compactness, these tables are displayed with the «temporary» keyword (instead of the long form - «TemporaryTable») on the diagram.

Temporary table is a kind of table, where data is held only temporary. There are two kinds of temporary tables. Local temporary table persists for the duration of user session and is visible only for the creator user. Global temporary table is long lived and visible for all users. Note that **data**in the global temporary table is different for different users and does not persist throughout user sessions (only global table definition persists).

Temporary tables are created using SQL create table statement (using TEMPORARY option).

```text
...
[ON COMMIT (PRESERVE | DELETE) ROWS]]]>
```

Besides the standard SQL element properties and persistent table properties (see [Persistent table](https://docs.nomagic.com/display/CDMP2024x Refresh1 Refresh1 Refresh1/Tables%2C+columns%2C+views%2C+and+columns#Tables,columns,views,andcolumns-Persistenttable)), temporary table has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Local | Marks the table as local or global temporary table. |
| Delete On Commit | Regulates whether data is deleted or retained on commit. |

##### View (derived table)

#### NOTE: Note

Note

SQL View is modeled as UML Class with the «ViewTable» stereotype applied. For the sake of compactness, views are displayed with the «view» keyword (instead of the long form - «ViewTable») on the dia- gram.

View is a table, whose data is derived from data of other tables (by applying some SQL query). Views are created using SQL create view statement.

```text
[]
AS 
[ WITH [ CASCADED | LOCAL ] CHECK OPTION ]]]>
```

Note that since column definition list is optional in SQL syntax, specifying column definitions in the view is also optional (columns can be inferred from query expression of the view). However, it is often a good idea to include column definitions, since this allows to see view data structure on the diagram / in the model at a glance, without parsing the query expression text.

Besides the standard SQL element properties and persistent table properties (see [Persistent table](https://docs.nomagic.com/display/CDMP2024x Refresh1 Refresh1 Refresh1/Tables%2C+columns%2C+views%2C+and+columns#Tables,columns,views,andcolumns-Persistenttable)), view has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Query Expression | A query expression, defining how data is calculated / retrieved for this view. This is an SQL SELECT statement. |
| Check Type | Describes how check is performed on the data update through the view. Only meaningful for updateable views (which is rare). |

Query expression of the view modeling deserves a special attention. Query expression, defining the view, is not just a simple string, but a (stereotyped) UML model element. By default query expression model object is stored within the view definition itself. There is a special constraint, automatically created inside the view, to hold this expression. When the view is created, **Query Expression**field (which is a tag of stereotype, applied on the view) is automatically pointed to this expression.

So by default you just need to fill in the **Body**text of the expression. To do that you need to double-click on the **Query Expression**field. This opens Specification window for the expression itself, where **Body**can be filled in. This is the default, no-hassle way to specify view. It is easy. But it has one deficiency. Views created this way do not have any model references to the underlying table model elements. This may be undesirable from the dependency tracking standpoint (in the dependency analysis). To remedy this, you can draw an additional **Dependency**relationships between the view and base tables.

There is also another way to model the query expression, defining the view. If you click on the **...**button of the **Query Expression**field, this action opens the element selection dialog, allowing to retarget the **Query Expression**pointer choose another expression object, located somewhere else in the model. For example view definition expression can be located inside the **Abstraction**relationship, drawn from the view to the base table (**Mapping**field of the **Abstraction**).

To model view queries using abstractions

1. Draw an abstraction relationship between a View and a Table.
2. In the abstraction’s Specification window, fill in the Mapping cell. This will be an inner UML OpaqueExpression model element with language and body cells. Set language to “SQL” and fill in the body with the necessary “SELECT ...” expression text.
3. Further open the Specification window of the mapping expression, and apply the «QueryExpressionDefault» stereotype.
4. Open the Specification window of the view. Click the ... button in the Query Expression cell. In the element Selection dialog navigate to the abstraction relationship and select the expression inside of it.

This way to model view query expressions is rather tedious - so it is not recommended for modeling novices. But it has an advantage of capturing the real relationship in the model between the view and the constituent table(s). Also query expression can be shown on the abstraction relationship (using note mechanism) instead of showing expression on the view.

In the following figure, you can see a diagram that illustrates the alternative way of view modeling.

[IMAGE alt='' src='']

###### Alternative notation for modeling view derivation from tables.

##### Column

#### NOTE: Note

Note

SQL Column is modeled as UML Property with «Column» stereotype applied. For the sake of compactness, columns are displayed with the «col» keyword (instead of the long form - «Column») on the diagram.

Column model element describes one column of the table. In the most frequent case it’s just a name of the column and a type. Additionally, column can carry default value specification, column constraints.

Column definition syntax in SQL (in CREATE TABLE, ADD COLUMN statements) is as follows.

```text
[  ]
[ DEFAULT  |
GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY
[ ‘(‘  ‘)’ ] |
GENERATED ALWAYS AS ]
[ ... ]]]>
```

Besides the standard SQL element properties, column has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Type | Collectively these two fields describe the type of the column. Type could be any of the primitive types from the library or user defined type. Modifier provides additional parameters for the type - such as width of the character type (when type=varchar and modifier=”(20)” - column is of varchar(20) type). See Type Usage section for details. |
| Type Modifier |  |
| Nullable | Marks column as nullable or not. Basically this is an in-line nullability constraint. See Constraints section for details. |
| Default Value | Carries the default value of the column. This is normally an opaque expression, allowing to specify the value of the column. However it can be switched to Identity Specifier. In this case it describes the autoincrement options of the column. See section. |
| Is Derived | Standard UML field, used to mark the column as derived (GENERATED ALWAYS AS <expression>). It works together with Default Value field. |
| Scope Check | Marks this column as scope checked to a particular table and allows choosing particular referential integrity ensuring action (RESTRICT CASCADE, etc). |
| Scope Checked |  |
| Implementation Dependent | Marks this column as implementation dependent. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="fb229b98-9ef2-4fdc-837d-0a90426c8a96"><ac:parameter ac:name="id">56082483</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="286b3331-fc02-4d21-bae3-294a727251d8"><ac:parameter ac:name="id">56082487</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="230f2609-62fa-4797-8a17-4f9049b8a22d"><ac:parameter ac:name="id">56082480</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="3efc6cc9-fa28-4bbc-8e5c-1ba3c7538218"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">2</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="16e79a7f-5c5d-4910-b950-1f04643cf96a"><ac:parameter ac:name="id">56082486</ac:parameter><ac:rich-text-body><p>Tables and their constituent columns are the main elements for describing database data structures. Table stores multiple rows of data each consisting of several columns. Each cell holds one data value (or is empty). All values of one column are of the same type. Correspondingly each table description consists of the table name and a set of column descriptions. Additionally there are various kinds of constraints (including the all- important primary key and foreign key constraints), that can be applied on tables and triggers, specifying additional actions to be performed during data manipulation.</p><p>See <ac:link><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Constraints" /></ac:link> and <span class="toc-item-body"><a class="toc-link" href="https://docs.nomagic.com/display/CDMP2024x Refresh1 Refresh1 Refresh1/Constraints#Constraints-Triggers">Triggers</a></span> for triggers. There can be various kinds of tables as follows.</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="7da68089-3a2c-422c-8844-1f266c145b26"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p><p>The following figure illustrates various kinds of tables that can be modeled on the diagram.</p><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 19 Various Kinds of Tables (Persistent Tables, Temporary Tables, and Views).png" /></ac:image></p><h6 style="text-align: center;">Various kinds of tables: persistent tables, temporary tables, and views.</h6><p>Tables can have generalization relationships between them. These relationships correspond to the following SQL syntax in the create table statement.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="1c376cbf-686d-447c-a1fe-c1b4805d927c"><ac:plain-text-body><![CDATA[CREATE TABLE <name> OF <UDT name> [UNDER <supertable>]]]></ac:plain-text-body></ac:structured-macro><p>There can be at most 1 outgoing generalization. Generalizations are not widely supported in database management systems. As of v17.0.1 Cameo Data Modeler supports modeling of these structures. Generation of corresponding script code is not supported yet.</p><h3><strong>Persistent table</strong></h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4dfccce4-b3f1-41da-9ace-1c26c98beff4"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Persistent Table is modeled as UML Class with the «Persistent- Table» stereotype applied. For the sake of compactness, these tables are displayed with the «table» keyword (instead of the long form - «PersistentTable») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Persistent table is the most often used kind of table. Besides the standard SQL element properties, persistent table has the following properties available in the Specification window (these properties are only available in Expert mode).</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 12.8171%;" /><col style="width: 87.1829%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><p><strong>User-defined type</strong></p></td><td><p>Points to structured user defined type, which serves as a base for the row type of the table.</p></td></tr><tr><td><strong>Supertable</strong></td><td><p>Points to the parent (base) table. Can only be used together with userdefined type.</p></td></tr><tr><td><p><strong>Self Ref Column Generation</strong></p></td><td><div class="content-wrapper"><p>Describes the self-referencing column generation options. Can only be used together with user-defined type. Corresponds to the following subclause of SQL create table statement</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="65e67183-32a0-47c6-b774-d31f699af423"><ac:plain-text-body><![CDATA[REF IS <column name> [SYSTEM GENERATED|USER
GENERATED|DERIVED]]]></ac:plain-text-body></ac:structured-macro></div></td></tr><tr><td><p><strong>Referencing</strong></p><strong>Foreign Keys</strong></td><td>This is back reference from foreign keys, referencing this table. This field is for information purposes only. If you want to change it, change <strong>Referenced Table </strong>field of the foreign key instead.</td></tr><tr><td><strong>Insertable</strong></td><td rowspan="2"><p>These are two derived (non editable) fields, describing table data editing capabilities. At the moment calculation of these properties is not implemented - they are always set to false.<strong><br /></strong></p></td></tr><tr><td><strong>Updatable</strong></td></tr></tbody></table><h3>Temporary table</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e13b8c5b-1765-4552-9cb9-4e5f753737bf"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Temporary Table is modeled as UML Class with the «Temporar- yTable» stereotype applied. For the sake of compactness, these tables are displayed with the «temporary» keyword (instead of the long form - «TemporaryTable») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Temporary table is a kind of table, where data is held only temporary. There are two kinds of temporary tables. Local temporary table persists for the duration of user session and is visible only for the creator user. Global temporary table is long lived and visible for all users. Note that <strong>data </strong>in the global temporary table is different for different users and does not persist throughout user sessions (only global table definition persists).</p><p>Temporary tables are created using SQL create table statement (using TEMPORARY option).</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2c94213e-2bc4-461b-8a41-a4ec919d7338"><ac:plain-text-body><![CDATA[CREATE (GLOBAL | LOCAL) TEMPORARY TABLE <table name> ...
[ON COMMIT (PRESERVE | DELETE) ROWS]]]></ac:plain-text-body></ac:structured-macro><p>Besides the standard SQL element properties and persistent table properties (see <span class="toc-item-body"><a href="https://docs.nomagic.com/display/CDMP2024x Refresh1 Refresh1 Refresh1/Tables%2C+columns%2C+views%2C+and+columns#Tables,columns,views,andcolumns-Persistenttable" class="toc-link">Persistent table</a></span>), temporary table has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.7806%;"><colgroup><col style="width: 13.3058%;" /><col style="width: 86.6942%;" /></colgroup><tbody><tr><th><strong>Property name</strong></th><th>Description</th></tr><tr><td><strong>Local</strong></td><td>Marks the table as local or global temporary table.</td></tr><tr><td><p><strong>Delete On Commit<br /></strong></p></td><td><p>Regulates whether data is deleted or retained on commit.</p></td></tr></tbody></table><h3>View (derived table)</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bda9d58d-8ed4-4e2c-a725-bddb7c55c9c5"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL View is modeled as UML Class with the «ViewTable» stereotype applied. For the sake of compactness, views are displayed with the «view» keyword (instead of the long form - «ViewTable») on the dia- gram.</p></ac:rich-text-body></ac:structured-macro><p>View is a table, whose data is derived from data of other tables (by applying some SQL query). Views are created using SQL create view statement.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="766ff465-9118-4544-88c1-a1708abe18c1"><ac:plain-text-body><![CDATA[CREATE VIEW <name> [<view column list>]
AS <query expression>
[ WITH [ CASCADED | LOCAL ] CHECK OPTION ]]]></ac:plain-text-body></ac:structured-macro><p>Note that since column definition list is optional in SQL syntax, specifying column definitions in the view is also optional (columns can be inferred from query expression of the view). However, it is often a good idea to include column definitions, since this allows to see view data structure on the diagram / in the model at a glance, without parsing the query expression text.</p><p>Besides the standard SQL element properties and persistent table properties (see <span class="toc-item-body"><a href="https://docs.nomagic.com/display/CDMP2024x Refresh1 Refresh1 Refresh1/Tables%2C+columns%2C+views%2C+and+columns#Tables,columns,views,andcolumns-Persistenttable" class="toc-link">Persistent table</a></span>), view has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 14.2724%;" /><col style="width: 85.7276%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Query Expression</strong></td><td>A query expression, defining how data is calculated / retrieved for this view. This is an SQL SELECT statement.</td></tr><tr><td><strong>Check Type</strong></td><td>Describes how check is performed on the data update through the view. Only meaningful for updateable views (which is rare).</td></tr></tbody></table><p>Query expression of the view modeling deserves a special attention. Query expression, defining the view, is not just a simple string, but a (stereotyped) UML model element. By default query expression model object is stored within the view definition itself. There is a special constraint, automatically created inside the view, to hold this expression. When the view is created, <strong>Query Expression </strong>field (which is a tag of stereotype, applied on the view) is automatically pointed to this expression.</p><p>So by default you just need to fill in the <strong>Body </strong>text of the expression. To do that you need to double-click on the <strong>Query Expression </strong>field. This opens Specification window for the expression itself, where <strong>Body </strong>can be filled in. This is the default, no-hassle way to specify view. It is easy. But it has one deficiency. Views created this way do not have any model references to the underlying table model elements. This may be undesirable from the dependency tracking standpoint (in the dependency analysis). To remedy this, you can draw an additional <strong>Dependency </strong>relationships between the view and base tables.</p><p>There is also another way to model the query expression, defining the view. If you click on the <strong>... </strong>button of the <strong>Query Expression </strong>field, this action opens the element selection dialog, allowing to retarget the <strong>Query Expression </strong>pointer choose another expression object, located somewhere else in the model. For example view definition expression can be located inside the <strong>Abstraction </strong>relationship, drawn from the view to the base table (<strong>Mapping </strong>field of the <strong>Abstraction</strong>).</p><p>To model view queries using abstractions</p><hr /><ol><li>Draw an abstraction relationship between a View and a Table.</li><li>In the abstraction’s Specification window, fill in the <strong>Mapping </strong>cell. This will be an inner UML OpaqueExpression model element with language and body cells. Set language to “SQL” and fill in the body with the necessary “SELECT ...” expression text.</li><li>Further open the Specification window of the mapping expression, and apply the «QueryExpressionDefault» stereotype.</li><li>Open the Specification window of the view. Click the <strong>... </strong>button in the <strong>Query Expression </strong>cell. In the element Selection dialog navigate to the abstraction relationship and select the expression inside of it.</li></ol><p>This way to model view query expressions is rather tedious - so it is not recommended for modeling novices. But it has an advantage of capturing the real relationship in the model between the view and the constituent table(s). Also query expression can be shown on the abstraction relationship (using note mechanism) instead of showing expression on the view.</p><p>In the following figure, you can see a diagram that illustrates the alternative way of view modeling.</p><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 20 Alternative Notation for Modeling View Derivation from Tables.png" /></ac:image></p><h6 style="text-align: center;">Alternative notation for modeling view derivation from tables.</h6><h3>Column</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="12e81c94-5434-4176-b962-86aeabf73110"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Column is modeled as UML Property with «Column» stereotype applied. For the sake of compactness, columns are displayed with the «col» keyword (instead of the long form - «Column») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Column model element describes one column of the table. In the most frequent case it’s just a name of the column and a type. Additionally, column can carry default value specification, column constraints.</p><p>Column definition syntax in SQL (in CREATE TABLE, ADD COLUMN statements) is as follows.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="61a17d82-bc0d-4e34-9de4-8fa8ca8037f9"><ac:plain-text-body><![CDATA[<column name> [ <data type> ]
[ DEFAULT <value expression> |
GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY
[ ‘(‘ <sequence options> ‘)’ ] |
GENERATED ALWAYS AS <expression>]
[ <column constraint definition>... ]]]></ac:plain-text-body></ac:structured-macro><p>Besides the standard SQL element properties, column has the following properties available in the Specification window.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 14.7071%;" /><col style="width: 85.2929%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><strong>Type</strong></td><td rowspan="2"><p>Collectively these two fields describe the type of the column. Type could be any of the primitive types from the library or user defined type. Modifier provides additional parameters for the type - such as width of the character type (when type=varchar and modifier=”(20)” - column is of varchar(20) type). See Type Usage section for details.</p></td></tr><tr><td><p><strong>Type Modifier</strong></p></td></tr><tr><td><strong>Nullable</strong></td><td>Marks column as nullable or not. Basically this is an in-line nullability constraint. See Constraints section for details.</td></tr><tr><td><strong>Default Value</strong></td><td>Carries the default value of the column. This is normally an opaque expression, allowing to specify the value of the column. However it can be switched to Identity Specifier. In this case it describes the autoincrement options of the column. See <ac:link><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Sequences and autoincrement columns" /></ac:link> section.</td></tr><tr><td><strong>Is Derived</strong></td><td>Standard UML field, used to mark the column as derived (GENERATED ALWAYS AS &lt;expression&gt;). It works together with Default Value field.</td></tr><tr><td><strong>Scope Check</strong></td><td rowspan="2">Marks this column as scope checked to a particular table and allows choosing particular referential integrity ensuring action (RESTRICT CASCADE, etc).</td></tr><tr><td><p><strong>Scope Checked</strong></p></td></tr><tr><td><p><strong>Implementation Dependent<br /></strong></p></td><td>Marks this column as implementation dependent.</td></tr></tbody></table></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459743 space=CDMP2024xR1 version=5 -->
## PAGE 00064: Top level elements

- page_id: `170459743`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459743/Top+level+elements
- version_number: 5
- version_date: `2024-05-08T13:49:55.282+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Database support > Database modeling
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

39512518

#### CONTENT-COLUMN: Note

39512520

39512517

**On this page**

33

#### CONTENT-BLOCK: Note

39512519

There are several top-level model elements, that serve as the containers for other model elements of the database model: Database, Schema, and Catalog.

Top level elements are not strictly necessary to begin database modeling. You can start modeling database elements (like tables) in the standard UML package (even directly under root ‘Data’ model element). But top level elements help to provide context for those other elements and their naming and positioning in the database. So, at least one top level element should be present - either Schema element or Database element. Optimally both Database and Schema element should be present in the model (Schema package inside the Database package). Catalog modeling is less important, it can be skipped. Not all databases have support for catalogs.

When top-level element is created (either on the diagram or in the containment tree), a special dialog is shown for selecting database flavor.

[IMAGE alt='' src='']

###### Database flavor selection dialog.

When DB flavor is chosen, the necessary profile for that DB flavor is attached to the project (providing standard data types for that DBMS and / or additional stereotypes for modeling extensions of that DB flavor). Then profile application relationship is created from the package that is being created (Database, Schema) to the attached DB profile. This marks the top level element as belonging to this DB flavor, Other DB elements, created under that top level element will be automatically considered as belonging to this DB flavor.

If you would like to switch database flavor after creating a top level element, you can do this in the following way.

To switch database flavor after creating a top level element

#### WARNING: Important

Important

You must have the necessary module attached to your project (Use **File>Use Module**menu then choose the necessary module from your **<install.root>\profiles**predefined location.).

1. Right-click the top level element.
2. From the shortcut menu, select Apply Profiles .
3. Select the check box near the needed profile and clear the check box near the old profile.
4. Click Apply .

Top level elements can be explicitly drawn on the diagram.

[IMAGE alt='' src='']

###### Database top level containers (database and schema) on the diagram pane.

However, showing top level elements on the diagram, and nesting their contents inside them is often clumsy, and consumes valuable diagram space. Showing them on the diagram pane is not necessary; it is enough to create them in the Containment tree (using the **New Element**command on the shortcut menu). Then, place your diagram inside the created containers, and the elements that you will be creating in your diagram, will go into the necessary container. See the following figure (logically equivalent to the previous one), showing a top level element just in the Containment tree and not displayed on the diagram pane.

[IMAGE alt='' src='']

###### Database top level containers (database and schema) in Containment tree, but not on diagram pane.

There is also one additional complication, steming from the limitations of UML. UML does not allow placing UML properties (which are used for SQL sequence modeling), or operations (which are used for SQL stored procedure & function modeling) directly into packages. Properties and operations can only occur in classes. A special model element was introduced to work around this limitation - GLOBALS element (based on UML class). This intermediate element can be placed directly inside the top level element (usually Schema, but can also be placed under Database) and then the necessary database elements - sequences, stored procedures can be placed inside it.

##### Database

#### NOTE: Note

Note

Database is modeled as UML Package with Database stereotype applied.

Database is a top level element, representing entire database within DBMS. Besides the standard SQL element properties, database has the following properties available in the Specification window.

| Property name | Description |
| --- | --- |
| Vendor | Specifies the vendor and the version of the database software. These fields are used for information purposes only. They do not affect the generation or further modeling. |
| Version |  |

##### Schema

#### NOTE: Note

Note

SQL Schema is modeled as UML Package with Schema stereotype applied.

Schema element represents a collection of database elements - tables, indexes, stored procedures, etc. - grouped for particular purpose (such as data structures for some particular application).

##### Catalog

#### NOTE: Note

Note

SQL Catalog is modeled as UML Package with Catalog stereotype applied.

Catalog element represents intermediate grouping level between database and schema. Catalogs are also reused for Oracle DB modeling - to implement Oracle packages.

##### GLOBALS

#### NOTE: Note

Note

GLOBALS is modeled as UML Class with the «Globals» stereotype applied.

GLOBALS element is a special intermediate element to work around limitation of UML. UML does not allow placing UML properties (which are used for SQL sequence modeling), or UML operations (which are used for SQL stored procedure & function modeling) directly into packages. Properties and operations can only occur in classes.

To work around this limitation, GLOBALS element (based on UML class) was introduced. This intermediate element can be placed directly inside the top level element (usually Schema, but can also be placed under Database) and then the necessary database elements - sequences, stored procedures and functions can be placed inside it.

Name of GLOBALS model element is not important, but for the sake of tidiness it should be named “GLOBALS”. There should be at most one such element per the container (Schema, Database, Package). This model element does not carry any additional useful properties; it serves just as a carrier of inner elements - sequences and routines.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="0d558fed-9a86-4de9-a226-5b6da71e9a61"><ac:parameter ac:name="id">39512518</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="f1b5a646-3c73-45a3-9c98-da3692e3692f"><ac:parameter ac:name="id">39512520</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f9332065-3645-4b57-aaa2-48adf32a3ffb"><ac:parameter ac:name="id">39512517</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="c4996792-ed79-48d2-a6e2-86c554bbf1cc"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="300d53ab-c5bf-4cc8-b9ad-3e65f8fe80f1"><ac:parameter ac:name="id">39512519</ac:parameter><ac:rich-text-body><p>There are several top-level model elements, that serve as the containers for other model elements of the database model: Database, Schema, and Catalog.</p><p>Top level elements are not strictly necessary to begin database modeling. You can start modeling database elements (like tables) in the standard UML package (even directly under root ‘Data’ model element). But top level elements help to provide context for those other elements and their naming and positioning in the database. So, at least one top level element should be present - either Schema element or Database element. Optimally both Database and Schema element should be present in the model (Schema package inside the Database package). Catalog modeling is less important, it can be skipped. Not all databases have support for catalogs.</p><p>When top-level element is created (either on the diagram or in the containment tree), a special dialog is shown for selecting database flavor.</p><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 16 Database Flavor Selection Dialog.png" /></ac:image></p><h6 style="text-align: center;">Database flavor selection dialog.</h6><p>When DB flavor is chosen, the necessary profile for that DB flavor is attached to the project (providing standard data types for that DBMS and / or additional stereotypes for modeling extensions of that DB flavor). Then profile application relationship is created from the package that is being created (Database, Schema) to the attached DB profile. This marks the top level element as belonging to this DB flavor, Other DB elements, created under that top level element will be automatically considered as belonging to this DB flavor.</p><p>If you would like to switch database flavor after creating a top level element, you can do this in the following way.</p><p>To switch database flavor after creating a top level element</p><hr /><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="83b50fdc-8e51-4e34-9d37-c9021db43568"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><p>You must have the necessary module attached to your project (Use <strong>File&gt;Use Module </strong>menu then choose the necessary module from your <strong>&lt;install.root&gt;\profiles </strong>predefined location.).</p></ac:rich-text-body></ac:structured-macro><ol><li>Right-click the top level element.</li><li>From the shortcut menu, select <strong>Apply Profiles</strong>.</li><li>Select the check box near the needed profile and clear the check box near the old profile.</li><li>Click <strong>Apply</strong>.</li></ol><p>Top level elements can be explicitly drawn on the diagram.</p><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 17 Database Top Level Containers (Database and Schema) on Diagram Pane.png" /></ac:image></p><h6 style="text-align: center;">Database top level containers (database and schema) on the diagram pane.</h6><p>However, showing top level elements on the diagram, and nesting their contents inside them is often clumsy, and consumes valuable diagram space. Showing them on the diagram pane is not necessary; it is enough to create them in the Containment tree (using the <strong>New Element </strong>command on the shortcut menu). Then, place your diagram inside the created containers, and the elements that you will be creating in your diagram, will go into the necessary container. See the following figure (logically equivalent to the previous one), showing a top level element just in the Containment tree and not displayed on the diagram pane.</p><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 18 Database Top Level Containers (database and schema) in Containment Tree But Not on Diagram Pane.png" /></ac:image></p><h6 style="text-align: center;">Database top level containers (database and schema) in Containment tree, but not on diagram pane.</h6><p>There is also one additional complication, steming from the limitations of UML. UML does not allow placing UML properties (which are used for SQL sequence modeling), or operations (which are used for SQL stored procedure &amp; function modeling) directly into packages. Properties and operations can only occur in classes. A special model element was introduced to work around this limitation - GLOBALS element (based on UML class). This intermediate element can be placed directly inside the top level element (usually Schema, but can also be placed under Database) and then the necessary database elements - sequences, stored procedures can be placed inside it.</p><h3>Database</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3dda3d38-2812-40ce-9991-2c7f2e1090bf"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>Database is modeled as UML Package with Database stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">Database is a top level element, representing entire database within DBMS. Besides the standard SQL element properties, database has the following properties available in the Specification window.</p><p class="auto-cursor-target"><br /></p><table class="relative-table wrapped" style="width: 69.9945%;"><colgroup><col style="width: 13.1699%;" /><col style="width: 86.8301%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td>Vendor</td><td rowspan="2">Specifies the vendor and the version of the database software. These fields are used for information purposes only. They do not affect the generation or further modeling.</td></tr><tr><td>Version</td></tr></tbody></table><h3>Schema</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="fc2874e2-294d-447a-bb17-934300e3f1f1"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Schema is modeled as UML Package with Schema stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>Schema element represents a collection of database elements - tables, indexes, stored procedures, etc. - grouped for particular purpose (such as data structures for some particular application).</p><h3>Catalog</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f313eab9-1191-47bc-9553-6ce47e39e995"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Catalog is modeled as UML Package with Catalog stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>Catalog element represents intermediate grouping level between database and schema. Catalogs are also reused for Oracle DB modeling - to implement Oracle packages.</p><h3>GLOBALS</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4116fdc8-79e8-48d7-8fd2-eef1428934c3"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>GLOBALS is modeled as UML Class with the «Globals» stereotype applied.</p></ac:rich-text-body></ac:structured-macro><p>GLOBALS element is a special intermediate element to work around limitation of UML. UML does not allow placing UML properties (which are used for SQL sequence modeling), or UML operations (which are used for SQL stored procedure &amp; function modeling) directly into packages. Properties and operations can only occur in classes.</p><p>To work around this limitation, GLOBALS element (based on UML class) was introduced. This intermediate element can be placed directly inside the top level element (usually Schema, but can also be placed under Database) and then the necessary database elements - sequences, stored procedures and functions can be placed inside it.</p><p>Name of GLOBALS model element is not important, but for the sake of tidiness it should be named “GLOBALS”. There should be at most one such element per the container (Schema, Database, Package). This model element does not carry any additional useful properties; it serves just as a carrier of inner elements - sequences and routines.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459877 space=CDMP2024xR1 version=1 -->
## PAGE 00065: TotalDigits

- page_id: `170459877`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459877/TotalDigits
- version_number: 1
- version_date: `2023-09-21T12:47:01.811+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDtotalDigits. The name and type of such an attribute do not make sense.

- value – to Attribute initial value.

#### PANEL: totalDigits XML representation summary

totalDigits XML representation summary

```text
<totalDigits
```

```text
fixed = boolean : false
```

```text
id = ID
```

```text
value = positiveInteger
```

```text
{any attributes with non-schema namespace…}>	Content: (annotation?)
```

```text
</totalDigits>
```

#### PANEL: totalDigits XML code sample

totalDigits XML code sample

```text
The following is the definition of a user-derived datatype which could be used to represent monetary amounts, such as in a financial management application which does not have figures of $1M or more and only allows whole cents. This definition would appear in a schema authored by an 'end-user' and shows how to define a datatype by specifying facet values which constrain the range of the base type in a manner specific to the base type. (different than specifying max/min values as before).
```

```text
<simpleType name='amount'>
```

```text
<restriction base='decimal'>
```

```text
<totalDigits value='8'/>
```

```text
<fractionDigits value='2' fixed='true'/>
```

```text
</restriction>
```

```text
</simpleType>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDtotalDigits. The name and type of such an attribute do not make sense.</p><ul><li style="text-align: left;">value – to Attribute initial value.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c7ce6d15-e0a0-4c99-8e16-cf7ca0eb9ad9"><ac:parameter ac:name="title">totalDigits XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;totalDigits</pre><pre>	fixed = boolean : false</pre><pre>	id = ID</pre><pre>	value = positiveInteger</pre><pre>	{any attributes with non-schema namespace…}&gt;<br />	Content: (annotation?)</pre><pre>&lt;/totalDigits&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="7dc675bc-a1be-4556-8a92-bb2262cfa52e"><ac:parameter ac:name="title"> totalDigits XML code sample</ac:parameter><ac:rich-text-body><pre>The following is the definition of a user-derived datatype which could be used to represent monetary amounts, such as in a financial <br />management application which does not have figures of $1M or more and only allows whole cents. This definition would appear in a <br />schema authored by an 'end-user' and shows how to define a datatype by specifying facet values which constrain the range of the <br />base type in a manner specific to the base type. (different than specifying max/min values as before).<br /><br /></pre><pre>&lt;simpleType name='amount'&gt;</pre><pre>	&lt;restriction base='decimal'&gt;</pre><pre>		&lt;totalDigits value='8'/&gt;</pre><pre>		&lt;fractionDigits value='2' fixed='true'/&gt;</pre><pre>	&lt;/restriction&gt;</pre><pre>&lt;/simpleType&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459802 space=CDMP2024xR1 version=1 -->
## PAGE 00066: Tracing between data model layers

- page_id: `170459802`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459802/Tracing+between+data+model+layers
- version_number: 1
- version_date: `2023-09-21T12:46:58.305+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Transformations > ER to SQL (generic / Oracle) transformations
- labels: []

### NORMALIZED CONTENT

After the transformation, a relationship is established between the logical data model layer, which is represented by the ER model, and the physical data model layer, which is represented by a SQL model respectively. It is possible to navigate between the connected elements in the forward (ER -> SQL) and backward (SQL -> ER) directions using the dedicated submenu - **Go To**- on the element’s shortcut menu.

To go to the corresponding element in the forward direction

1. Right-click the element.
2. On it’s shortcut menu, click Go To > Traceability > Model Transformations > Transformed T o .

To go to the corresponding element in the backward direction

1. Right-click the element.
2. On it’s shortcut menu, click Go To > Traceability > Model Transformations > Transformed From .

The same tracing information is visible in the element’s Specification window and **Properties**panel under the **Traceability**tab. This information is also reflected in the Entity-Relationship and SQL Report using navigable references between the report section. Traceability information can also be depicted in a relation map or in a tabular format using the capabilities of the custom dependency matrix feature.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>After the transformation, a relationship is established between the logical data model layer, which is represented by the ER model, and the physical data model layer, which is represented by a SQL model respectively. It is possible to navigate between the connected elements in the forward (ER -&gt; SQL) and backward (SQL -&gt; ER) directions using the dedicated submenu - <strong>Go To </strong>- on the element’s shortcut menu.</p><p>To go to the corresponding element in the forward direction</p><hr /><ol><li>Right-click the element.</li><li>On it’s shortcut menu, click <strong>Go To </strong>&gt; <strong>Traceability </strong>&gt; <strong>Model Transformations </strong>&gt; <strong>Transformed T</strong><strong>o</strong>.</li></ol><p><br /></p><p>To go to the corresponding element in the backward direction</p><hr /><ol><li>Right-click the element.</li><li style="text-align: left;">On it’s shortcut menu, click <strong>Go To </strong>&gt; <strong>Traceability </strong>&gt; <strong>Model Transformations </strong>&gt; <strong>Transformed From</strong>.</li></ol><p>The same tracing information is visible in the element’s Specification window and <strong>Properties </strong>panel under the <strong>Traceability </strong>tab. This information is also reflected in the Entity-Relationship and SQL Report using navigable references between the report section. Traceability information can also be depicted in a relation map or in a tabular format using the capabilities of the custom dependency matrix feature.</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=170459783 space=CDMP2024xR1 version=6 -->
## PAGE 00067: Transformation procedure

- page_id: `170459783`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459783/Transformation+procedure
- version_number: 6
- version_date: `2024-05-08T14:00:37.904+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Transformations > UML to SQL transformation
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Example

237267523

#### CONTENT-COLUMN: Example

237267526

237267521

**On this page**

43

#### CONTENT-BLOCK: Example

237267525

UML to SQL (Generic / Oracle) transformation is based on the same copy mechanism as the other transformations are. It copies the source model part to the destination (unless the in-place transformation is performed), remaps types, and then performs model reorganization to turn the model into an SQL model.

To transform a UML model to SQL

1. Open the UML model you want to transform or create a new one.
2. Open the Model Transformation Wizard . Do one of the following.

- 
  - On the main menu, click Tools > Model Transformations .
  - Select the package in the Model Browser and click Tools > Transform on its shortcut menu.

3. Perform the steps of the wizard.

3.1 Select the transformation type.

3.2 Select the transformation source and specify the location wherein the output should be placed. If you open the wizard from the shortcut menu of a package, this package and all its content will be automatically selected as the source.

3.3 Check type mappings. You can select the transformation type map profile in this step.

3.4 Specify transformation details.

4. Click****Finish****when you are done.

##### **Conversio****n****o****f classes**

UML classes from the source model are converted into tables.

Each property of the source class becomes a column in the result table. If a property in the UML model had the explicit multiplicity specified, nullable=true (for [0..1] multiplicity in source property) and nullable=false (for [1] multiplicity in source property) marking is applied on result columns.

Operations contained in the source class are not copied into the result table.

##### **Primary keys autogeneration**

If a UML class in the source model had no primary key (it is declared by applying an appropriate stereotype), an ID column is generated and marked as the primary key (PK).

#### TIP: Tip

Tip

You can turn off the automatic generation of PKs during the model transformation. For this, click to clear the **Autogenerate PK**check box in the **Transformation Details**pane (the 4th step of the **Model Transformation Wizard**)

In this case, you must specify PKs and FKs manually after the model transformation.

The **Autogenerated PK name template**transformation property governs the name of the generated ID column. The %t pattern in the name template is expanded to the current table name.

The **Autogenerated PK type**transformation property determines the type of the ID column. The default type is integer.

##### **Sequence autogeneration**

#### NOTE: Note

Note

This feature is only available in UML to SQL (Oracle) transformations. Generic SQL models do not have sequence support yet.

For each single-column PK in the destination a sequence object can be generated.

The **Autogenerate Sequences**transformation property governs the sequence autogeneration. Possible choices for setting the property value are as follows.

1. Do not generate sequences choice switches sequence generation off.
2. Generate sequences for all single-column PKs choice switches sequence generation on.
3. Generate sequences for all autogenerated PKs choice switches sequence generation on but only for those PKs that there automatically generated by the tool (but not for PKs which were declared by the user).

##### **Conversion of associations**

One-to-one and one-to-many associations between classes in the source UML model are converted to foreign key relationships and to foreign key columns in the table, which is at the multiple end.

The **Autogenerated FK column name template**transformation property governs the name of the generated FK column. A name template can use the following patterns.

- %t is replaced by the name of the table, the foreign key is pointing to.
- %k is replaced by the key name, this foreign key is pointing to.
- %r is replaced by the name of the relationship role, which is realized by this foreign key.

Note that the type of the FK column matches the type of the PK column, to which this key is pointing.

Many-to-Many associations are transformed into the intermediate table. An intermediate table is generated for an association and has two FK relationships pointing to the tables at association ends. FK are generated in the same way as for one-to-many associations.

The **Autogenerated table name template**transformation property governs the name of the generated intermediate table (%t1 and %t2 are replaced by the names of the tables at relationship ends).

You can create your own **Autogenerated FK constraint name template**. It makes easier to find FKs in the generated code. Also, it is helpful if you have some naming convention at your company.

You can use the same described patterns to specify the FK name template. For example, if you define the FK constraint name template as “fk_%r”, appropriate relations in the model will look like it is depicted in the following figure.

###### [IMAGE alt='' src='']Example of transformation when FK name template is used.

The same sample in the, for example, SQL code will look as follows.

```text

```

To create the FK constraint name template

1. In the Transformation Details (the 4th step of the Model Transformation Wizard ), click the Autogenerated FK constraint name template specification cell. The Edit button appears.
2. Click the Edit button and, in the opened Autogenerated FK constraint name template dialog, define the FK name template. You can use specific names and patterns, such as %t (a table name) or %r (a relationship role) in the name template definition.
3. Click OK when you are done and continue the transformation setup process.

##### **Conversio****n****o****f identifying associations**

Some relationships in the source model are treated as identifying relationships. In case of identifying a relationship, the objects of the class, which is at the multiple end of the association, are not independent, that is, they can exist only in association with the objects at the singular end of the association. In the resulting SQL model, the FK of these relationships is included into the PK of the table.

The PK of the dependent table is composite and contains the following two columns as a result.

1. ID column of the table
2. FK to the independent table

Unfortunately, UML models lack model data and notation to specify, which associations are identified. Hence transformation has to guess this. It uses the following heuristics - the composite associations are treated as identifying, while the other associations are not.

The **Treat composition relationships as identifying**transformation property governs these heuristics. If this property set to false, all associations are treated as not identifying.

##### **Conversion of multivalued properties**

In UML models, properties can be multi-valued (e.g. [0..7], [2..*]). However, in databases columns they can be only single-valued. Transformation uses two strategies to handle multi-valued properties in the source model.

If the upper multiplicity limit is small and fixed, e.g., [0..3], then columns are simply multiplied the necessary number of times. The result table will have multiple columns with sequence numbers appended to their names (like “phone1”, “phone2”, and “phone3” columns in the result for a single phone[0..3] property in the source).

The **Max Duplicated Columns**transformation property governs the maximum number of columns, that are generated using this strategy.

If the upper multiplicity upper bound is larger than this limit or unlimited, then an auxiliary value table is generated for such multi-valued properties. This table is FK-related to the main table of the class, and holds a “value” column for storing property values.

The **Value table name**transformation property governs the name of the generated table (%t in this property is replaced by the name of the table and %r - by the property name). So, the table name template “%t_%r_VALUES” gives a “Person_Phone_VALUES” table name for the Person::phone property).

##### **Conversion of generalizations**

In UML, generalizations are used extensively, while SQL domain lacks the concept of generalizations. Hence during the transformation, generalization trees are transformed into different concepts to simulate the generalization approximately.

There are three different strategies for simulating generalizations in the result domain as follows.

1. Multiple Tables, Decomposed Object strategy.
2. Multiple Tables, Copy Down strategy.
3. One Table, Merged strategy.

Specify the strategy for converting generalization trees in the **Generalization Tree transformation strategy** transformation property.

****

###### **Multiple tables, decomposed object strategy**

This strategy consists of the following actions.

1. Each class is converted to a separate table.
2. Direct (not inherited) properties of the class are converted to the columns of the table.
3. A foreign key to the table of the base class is created. The table of the base class carries the inherited columns.
4. Primary keys of all the classes participating in a hierarchy tree are the same (there can be several hierarchy trees in the same transformation source, and each one is handled separately). PK of the specific tables is also an FK to the parent table.

This strategy is the closest one to UML and fits nicely from theoretical standpoint since there is no data duplication. The only problem of this approach is the performance of data retrieval and storage. During the storing operation, objects are decomposed into several parts, each stored in a different table (that is why the strategy is called Decomposed Object strategy), and for retrieving the object you have to query several tables (with resulting multi-level joins).

###### **Multiple tables, Copy Down strategy**

This strategy consists of the following actions.

1. Each class is converted to a separate table.
2. The table of each class holds columns for properties of that class AND all the columns, copied from the base class (that is why this strategy is called Copy Down strategy).

As a result each table possesses the complete column set to carry data about an object of particular type. All the data of the object is stored in one table.

The weak point of this strategy is that the association relationships between tables are copied down also. Hence each association in the source can produce many foreign keys in the target. Writing SQL queries against this database layout is not very convenient. Also, if you want to retrieve all the objects of the particular class, you have to query several tables and union the results.

###### **One table, merged strategy**

This strategy consists of the following actions.

1. All the classes in the generalization hierarchy are folded into one large table.
2. All the properties of all the classes become table columns (note that columns that were mandatory in the specific classes become optional in the merged table).
3. A separate selector column is generated, which indicates the type of the object carried by the particular line.

The **Selector Column Name**, **Selector Column Type**and **Selector Column Type Modifier**transformation properties determine the selector column format.

This strategy is suitable for very small hierarchies usually of just one hierarchy level with a couple of specialization classes, each adding a small number of properties to the base class. E.g., general class “VehicleRegistration” and a couple of subclasses: “CarRegistration” and “TruckRegistration”.

This strategy suites simple cases well. It is simple and fast. However, it does not scale for larger hierarchies and produces sparse tables (tables with many null values in the unused columns) in this case.

###### **Conclusions and future improvements**

Note that all hierarchies from the transformation source are converted using the same method. You cannot choose different strategies for each particular case of the generalization tree. This is considered as a future improvement for the transformations.

##### **Conversion of DataTypes**

You can choose two strategies to transform datatype of data to SQL as follows:

- To transform datatypes to structured user defined types . This is a default case.

###### [IMAGE alt='' src='']Example of datatype transformation to structured user defined types.

The same sample in the Oracle SQL code will look as follows.

```text

```

- To expand datatypes into separate columns at the point of usage. Each property of a class having a datatype as a type is expanded into a set of columns—one column per each attribute of the datatype (including inherited attributes). Column types are copied from the source datatype attribute types (modulo the transformation type mapping). If the original datatype attribute is multivalued, the resulting column is further modified in the same manner as multivalued class attributes. The datatype expansion is recursive.

###### [IMAGE alt='' src='']Example of DataType transformation to separate columns.

The same sample in the Oracle SQL code will look as follows.

```text

```

On the conversion of DataTypes into separate columns at the point of usage, you can define names of the columns. By default, the format “%r_%a” is used, where %r is a name of a class attribute and %a is a name of a DataType attribute. In the example depicted in the preceding figure, column names are constructed according to the default template, like rect_upperLeft_X, rect_lowerRight_Y and so on.

To select a strategy for the DataType transformation

1. In the Transformation Details (the 4th step of the Model Transformation Wizard ), set the Expand datatypes value to

- 
  - False to transform datatypes to structured user defined types.
  - T rue to expand datatypes into separate columns at the point of usage

2. Continue the transformation setup process.

To define a template name for columns

1. In the Transformation Details (the 4th step of the Model Transformation Wizard ), click the Expanded datatype column name template specification cell. The Edit button appears.
2. Click the Edit button and, in the opened Expanded datatype column name template dialog, define the column name. In the column name definition, you can use specific convenient names and the following patterns.

- %r - a name of a class attribute
- %a - a name of a datatype attribute
- %t - a name of table

3. Click OK when you are done and continue the transformation setup process.

The column name template is defined in the **Expanded datatype column name template**property.

##### **Conversio****n****o****f enumerations**

When transforming enumerations, you can choose two following strategies:

****•****To transform the enumeration to **check constraints** at the point of usage. This is the default case. Every class attribute of the enumeration type in the transformation source is transformed to the table column of a char type.

###### [IMAGE alt='' src='']Example of enumeration transformation to check constraints.

The same sample in the SQL code will look as follows.

```text

```

To transform enumerations to **lookup tables**. This strategy can handle the more complex enumerations, for example, enumerations having their own attributes. The lookup table is automatically populated with enumeration literal values, and INSERT statements are generated during the SQL code generation. For each attribute that enumeration source has (including inherited attributes) the column in the target table is created. Attributes are transformed using the normal transformation rules for class attributes (including the type mapping, data type expansion, if requested, and multivalue-attribute expansion). The **name**column is added to the lookup table and the primary key is automatically generated (see ). Every class attribute of the enumeration type in the transformation source is transformed to the foreign key.

###### [IMAGE alt='' src='']Example of enumeration transformation to lookup tables.

The same sample in the SQL code will look as follows.

```text

```

To select a strategy for the Enumeration transformation

1. In the Transformation Details (the 4th step of the Model Transformation Wizard ), click the Enumeration transformation strategy specification cell. The list of available strategies appears. Select one of the following.

- 
  - Check Constraints to transform the enumeration to check constraints at the point of usage.
  - Lookup Table to transform enumeration to lookup tables.

2. Continue the transformation setup process.

##### **Packag****e hierarchy reorganization**

UML models usually have a moderately deep package nesting organization, while SQL models can have at most one package level - the schemas. Hence during the transformation, packages should be reorganized.

The **Change package hierarchy**transformation property governs the package reorganization. Possible choices for setting the property value are as follows.

1. Leave intact choice switches reorganization off.
2. Flatten packages choice forces flattening of the packages of the source, leaving only the top level packages in the destination.
3. Strip packages choice removes all packages of the source.

##### **Namin****g of transformed elements**

While transforming your UML models to SQL, you can modify names of the transformed elements according to given naming rules. There are several predefined rules as follows.

- Replace spaces or special characters in the element name with the underscore sign “_”. For example, the name in source “Customer Profile” and “Terms&Conditions” could be transformed as “Customer_Profile” and “Terms_Conditions” accordingly.
- Capitalize element names after the transformation. For example, the name in source “Customer” could be transformed as “CUSTOMER”.
- Pluralize element names after transformation. For example, the name in source “Customer” could be transformed as “Customers”.
- Detect the camel case edge in element names on transformation. For example, the name in source “CustomerProfile” could be transformed as “Customer_Profile”.

To select a naming rule

1. In the Transformation Details (this is the last step of the Model Transformation Wizard ), click the Name conversion rules specification cell. The cell expands and the Edit button appears.
2. Click the Edit button. The Select Opaque Behavior «Naming Rule» dialog opens.
3. In the opened dialog, select naming rules you want to use in transforming element names. You may select more than one rule.

#### NOTE: Note

Note

- Be sure the search includes auxiliary resources! To turn on the appropriate search mode, click Include elements from modules into search results .
- To select several naming rules, click the Multiple Selection button.

Naming rules are as follows.

| Rule name | Description | Example |
| --- | --- | --- |
| CamelCaseSeparator | Detects all the occurrences in the original name of the situation where lower case letter is followed by upper case letter and insert the underscore sign '_' character between. | CustomerProfile > Customer_Profile |
| LowerCase | All Unicode letter characters in the source name are converted to their lower case version in the result name. Other character are passed through unchanged. | CUSTOMER 1 > customer 1 |
| Pluralization | All original names that do not end with character 'S' or 's' will have the 's' character appended. | Customer > Customers |
| SpecialCharacterEscape | All Unicode characters in the source name that are not letters and not numbers are converted to an underscore sign ‘_’ in the result name. Other character are passed through unchanged. | Terms&Conditions > Terms_Conditions |
| UpperCase | All Unicode letter characters in the source name are converted to their upper case version in the result name. Other character are passed through unchanged. | Customer 1 > CUSTOMER 1 |
| WhitespaceEscape | All Unicode whitespace characters in the source name are converted to an underscore sign ‘_’ in the result name. Other character are passed through unchanged. | Customer 1 > Customer_1 |

4. Click **OK**when you are done.

You can also create your custom naming rules using structured expressions or various scripts. The naming rule is an executable opaque behavior. The following procedure describes one of the possible ways to create a custom naming rule.

To create a custom naming rule

1. Create a package for the naming rule data.
2. In this package, create an Opaque Behavior with the following parameters exactly in the same order as follows:

- sourceElement : Element
- targetElement : Element
- initialName : String

The return parameter is of a java.lang.Object type.

[IMAGE alt='' src='']

###### Return parameter of a java.lang.Object type.

3. Use the **Model Transformation Profile.mdzip**module. On the main menu, click **File**> **Use Module**. The required module is located in the <install.root>\profiles\Model_Transformation_Profile.mdzip. Click **Finish**after you have selected the module.

4. In the Model Browser, select the Opaque Behavior you have created and apply the «NamingRule» stereotype on it. Open the opaque behavior’s shortcut menu and click **Stereotype**. In the opened **Select Stereotype**list, select the «NamingRule» stereotype and click **Apply**.

5. Open the opaque behavior’s Specification window and specify the **Body and Language**property. Actually, this is a property where you define your custom naming rule. Click property specification cell and then click the Edit button.

6. In the opened **Body and Language**dialog, select a language for defining your naming rule and create the rule’s body.

#### NOTE: Note

Note

- The SQL language is not suitable for defining naming rules.
- If you choose the Structured Expression language, turn on the Expert mode to get the all list of possible operations.

7. Click **OK**when you are done. The naming rule you have created appears in the **Name conversion rules**selection list.

##### **Transformin****g****documentation**

Documentation can be copied either with or without HTML formatting information. If you need to retain the formatting information, click to select the **Allow HTML in comments**check box in the **Transformation Details**pane (the 4th step of the **Model Transformation Wizard**).

The model element documentation is turned into SQL comments during the DDL script generation.

#### TIP: Tip

Tip

You can turn off the comment generation. For this, do the following:

1. From the Options menu, select Project . The Project Options dialog opens.
2. Select DDL Language Options on the left (you may need to expand the Code Engineering node). The appropriately named pane opens on the right.
3. Click to clear the Generate documentation check box.
4. Click OK .

###### [IMAGE alt='' src='']SQL comments with and without HTML formatting information.

##### **Excluding elements from transformation**

Elements can be excluded from the transformation in one of the following ways.

- By deselecting these elements in the 2nd step of the Model Transformation Wizard .
- By specifying rules for the automatic exclusion of elements in the 4th step of the wizard. These rules must be defined as executable opaque behaviors.

To define a rule for automatic elements’ exclusion

1. Create an executable opaque behavior.

2. Create an input parameter, whose type is *Element,*the abstract UML metaclass, and multiplicity is [1].

3. Create a return parameter, whose type is java.lang.Object and multiplicity is [1].

4. Specify the **Language and Body**property value for the new opaque behavior.

#### NOTE: Example

Example

Let’s say we need to exclude from the transformation all the classes with the «pendingReview» stereotype applied.

For this, we must do the following.

1. Select StructuredExpression as language of the opaque behavior body.
2. Define the body by creating a TypeTest operation, which takes the collection of elements and returns only the ones with the «pendingReview» stereotype applied (see the following figure).

For more information about the TypeTest operation, see [CONFLUENCE_PAGE title='Calling operations from the model' space='MD2024xR1 Refresh1 Refresh1'] in MagicDraw User Guide.

[IMAGE alt='' src='']

###### Defining the body by creating a TypeTest operation in the Body and Language dialog box.

To specify the rules for the automatic elements’ exclusion from the transformation

1. In the Transformation Details pane (the 4th step of the Model Transformation Wizard ), click the Elements exclusion rules specification cell. The Edit button appears.
2. Click the button and select one or more rules in the Select Opaque Behavior dialog.
3. Click OK when you are done and continue the transformation setup process.

**[IMAGE alt='' src='']**

###### Example of transformation with excluded class.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="15ada039-d996-4682-b30f-5ead452ccbaf"><ac:parameter ac:name="id">237267523</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="cd82dde4-1e64-45a0-8793-d913092f77ea"><ac:parameter ac:name="id">237267526</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ca12ba9d-2fe6-4fc6-a8af-f4ea260ed17d"><ac:parameter ac:name="id">237267521</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="939e96f3-60c1-4698-8963-e8b6cdb2fbb9"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="91765f4b-8018-46fa-91e9-925062ae75dc"><ac:parameter ac:name="id">237267525</ac:parameter><ac:rich-text-body><p>UML to SQL (Generic / Oracle) transformation is based on the same copy mechanism as the other transformations are. It copies the source model part to the destination (unless the in-place transformation is performed), remaps types, and then performs model reorganization to turn the model into an SQL model.</p><p>To transform a UML model to SQL</p><hr /><ol><li>Open the UML model you want to transform or create a new one.</li><li>Open the <strong>Model Transformation Wizard</strong>. Do one of the following.</li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li>On the main menu, click <strong>Tools </strong>&gt; <strong>Model Transformations</strong>.</li><li>Select the package in the Model Browser and click <strong>Tools </strong>&gt; <strong>Transform </strong>on its shortcut menu.</li></ul></li></ul><p>       3. Perform the steps of the wizard.</p><p style="margin-left: 60.0px;">3.1 Select the transformation type.</p><p style="margin-left: 60.0px;">3.2 Select the transformation source and specify the location wherein the output should be placed. If you open the wizard from the shortcut menu of a package, this package and all its content will be automatically selected as the source.</p><p style="margin-left: 60.0px;">3.3 Check type mappings. You can select the transformation type map profile in this step.</p><p style="margin-left: 60.0px;">3.4 Specify transformation details.</p><p style="margin-left: 30.0px;">4. Click<strong> <strong>Finish </strong></strong>when you are done.</p><h3><strong>Conversio</strong><strong>n </strong><strong>o</strong><strong>f classes</strong></h3><p>UML classes from the source model are converted into tables.</p><p>Each property of the source class becomes a column in the result table. If a property in the UML model had the explicit multiplicity specified, nullable=true (for [0..1] multiplicity in source property) and nullable=false (for [1] multiplicity in source property) marking is applied on result columns.</p><p>Operations contained in the source class are not copied into the result table.</p><h3><strong>Primary keys autogeneration</strong></h3><p>If a UML class in the source model had no primary key (it is declared by applying an appropriate stereotype), an ID column is generated and marked as the primary key (PK).</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="ce6a97be-79a2-4693-9253-698478cca69b"><ac:parameter ac:name="title">Tip</ac:parameter><ac:rich-text-body><p>You can turn off the automatic generation of PKs during the model transformation. For this, click to clear the <strong>Autogenerate PK </strong>check box in the <strong>Transformation Details </strong>pane (the 4th step of the <strong>Model Transformation Wizard</strong>)</p><p>In this case, you must specify PKs and FKs manually after the model transformation.</p></ac:rich-text-body></ac:structured-macro><p>The <strong>Autogenerated PK name template </strong>transformation property governs the name of the generated ID column. The %t pattern in the name template is expanded to the current table name.</p><p>The <strong>Autogenerated PK type </strong>transformation property determines the type of the ID column. The default type is integer.</p><h3><strong>Sequence autogeneration</strong></h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a9b71535-cba5-49bf-8da0-02e996c0bcf2"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>This feature is only available in UML to SQL (Oracle) transformations. Generic SQL models do not have sequence support yet.</p></ac:rich-text-body></ac:structured-macro><p>For each single-column PK in the destination a sequence object can be generated.</p><p>The <strong>Autogenerate Sequences </strong>transformation property governs the sequence autogeneration. Possible choices for setting the property value are as follows.</p><ol><li><strong>Do not generate sequences </strong>choice switches sequence generation off.</li><li><strong>Generate sequences for all single-column PKs </strong>choice switches sequence generation on.</li><li><strong>Generate sequences for all autogenerated PKs </strong>choice switches sequence generation on but only for those PKs that there automatically generated by the tool (but not for PKs which were declared by the user).</li></ol><h3><strong>Conversion of associations</strong></h3><p>One-to-one and one-to-many associations between classes in the source UML model are converted to foreign key relationships and to foreign key columns in the table, which is at the multiple end.</p><p>The <strong>Autogenerated FK column name template </strong>transformation property governs the name of the generated FK column. A name template can use the following patterns.</p><ul><li>%t is replaced by the name of the table, the foreign key is pointing to.</li><li>%k is replaced by the key name, this foreign key is pointing to.</li><li>%r is replaced by the name of the relationship role, which is realized by this foreign key.</li></ul><p>Note that the type of the FK column matches the type of the PK column, to which this key is pointing.</p><p>Many-to-Many associations are transformed into the intermediate table. An intermediate table is generated for an association and has two FK relationships pointing to the tables at association ends. FK are generated in the same way as for one-to-many associations.</p><p>The <strong>Autogenerated table name template </strong>transformation property governs the name of the generated intermediate table (%t1 and %t2 are replaced by the names of the tables at relationship ends).</p><p>You can create your own <strong>Autogenerated FK constraint name template</strong>. It makes easier to find FKs in the generated code. Also, it is helpful if you have some naming convention at your company.</p><p>You can use the same described patterns to specify the FK name template. For example, if you define the FK constraint name template as “fk_%r”, appropriate relations in the model will look like it is depicted in the following figure.</p><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 33 Example of Transformation when FK Name Template Is Used.png" /></ac:image>Example of transformation when FK name template is used.</h6><p>The same sample in the, for example, SQL code will look as follows.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="45b419a3-cb1a-45b1-812e-ab4e7a02c959"><ac:plain-text-body><![CDATA[CREATE SEQUENCE pets.Dog_SEQ;
CREATE SEQUENCE pets.Human_SEQ;
CREATE TABLE pets.Human
(
	Name varchar (255), 
	id integer,
	PRIMARY KEY(id)
);
CREATE TABLE pets.Dog
(
	Name varchar (255), 
	id integer,
	fk_Humanid integer NOT NULL,
	PRIMARY KEY(id),
	CONSTRAINT fk_Master FOREIGN KEY(fk_Humanid) REFERENCES pets.Human (id)
);]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p>To create the FK constraint name template</p><hr /><ol><li style="text-align: left;">In the <strong>Transformation Details </strong>(the 4th step of the <strong>Model Transformation Wizard</strong>), click the<strong> Autogenerated FK constraint name template </strong>specification cell. The Edit button appears.</li><li>Click the Edit button and, in the opened <strong>Autogenerated FK constraint name template </strong>dialog, define the FK name template. You can use specific names and patterns, such as %t (a table name) or %r (a relationship role) in the name template definition.</li><li>Click <strong>OK </strong>when you are done and continue the transformation setup process.</li></ol><h3><strong>Conversio</strong><strong>n </strong><strong>o</strong><strong>f identifying associations</strong></h3><p>Some relationships in the source model are treated as identifying relationships. In case of identifying a relationship, the objects of the class, which is at the multiple end of the association, are not independent, that is, they can exist only in association with the objects at the singular end of the association. In the resulting SQL model, the FK of these relationships is included into the PK of the table.</p><p>The PK of the dependent table is composite and contains the following two columns as a result.</p><ol><li>ID column of the table</li><li>FK to the independent table</li></ol><p>Unfortunately, UML models lack model data and notation to specify, which associations are identified. Hence transformation has to guess this. It uses the following heuristics - the composite associations are treated as identifying, while the other associations are not.</p><p>The <strong>Treat composition relationships as identifying </strong>transformation property governs these heuristics. If this property set to false, all associations are treated as not identifying.</p><h3><strong>Conversion of multivalued properties</strong></h3><p>In UML models, properties can be multi-valued (e.g. [0..7], [2..*]). However, in databases columns they can be only single-valued. Transformation uses two strategies to handle multi-valued properties in the source model.</p><p>If the upper multiplicity limit is small and fixed, e.g., [0..3], then columns are simply multiplied the necessary number of times. The result table will have multiple columns with sequence numbers appended to their names (like “phone1”, “phone2”, and “phone3” columns in the result for a single phone[0..3] property in the source).</p><p>The <strong>Max Duplicated Columns </strong>transformation property governs the maximum number of columns, that are generated using this strategy.</p><p>If the upper multiplicity upper bound is larger than this limit or unlimited, then an auxiliary value table is generated for such multi-valued properties. This table is FK-related to the main table of the class, and holds a “value” column for storing property values.</p><p>The <strong>Value table name </strong>transformation property governs the name of the generated table (%t in this property is replaced by the name of the table and %r - by the property name). So, the table name template “%t_%r_VALUES” gives a “Person_Phone_VALUES” table name for the Person::phone property).</p><h3><strong>Conversion of generalizations</strong></h3><p>In UML, generalizations are used extensively, while SQL domain lacks the concept of generalizations. Hence during the transformation, generalization trees are transformed into different concepts to simulate the generalization approximately.</p><p>There are three different strategies for simulating generalizations in the result domain as follows.</p><ol><li><strong>Multiple Tables, Decomposed Object </strong>strategy.</li><li><strong>Multiple Tables, Copy Down </strong>strategy.</li><li><strong>One Table, Merged </strong>strategy.</li></ol><p>Specify the strategy for converting generalization trees in the <strong>Generalization Tree transformation strategy</strong> transformation property.</p><p><strong> </strong></p><h4><strong>Multiple tables, decomposed object strategy</strong></h4><p>This strategy consists of the following actions.</p><ol><li>Each class is converted to a separate table.</li><li>Direct (not inherited) properties of the class are converted to the columns of the table.</li><li>A foreign key to the table of the base class is created. The table of the base class carries the inherited columns.</li><li>Primary keys of all the classes participating in a hierarchy tree are the same (there can be several hierarchy trees in the same transformation source, and each one is handled separately). PK of the specific tables is also an FK to the parent table.</li></ol><p>This strategy is the closest one to UML and fits nicely from theoretical standpoint since there is no data duplication. The only problem of this approach is the performance of data retrieval and storage. During the storing operation, objects are decomposed into several parts, each stored in a different table (that is why the strategy is called Decomposed Object strategy), and for retrieving the object you have to query several tables (with resulting multi-level joins).</p><h4><strong>Multiple tables, Copy Down strategy</strong></h4><p>This strategy consists of the following actions.</p><ol><li>Each class is converted to a separate table.</li><li>The table of each class holds columns for properties of that class AND all the columns, copied from the base class (that is why this strategy is called Copy Down strategy).</li></ol><p>As a result each table possesses the complete column set to carry data about an object of particular type. All the data of the object is stored in one table.</p><p>The weak point of this strategy is that the association relationships between tables are copied down also. Hence each association in the source can produce many foreign keys in the target. Writing SQL queries against this database layout is not very convenient. Also, if you want to retrieve all the objects of the particular class, you have to query several tables and union the results.</p><h4><strong>One table, merged strategy</strong></h4><p>This strategy consists of the following actions.</p><ol><li>All the classes in the generalization hierarchy are folded into one large table.</li><li>All the properties of all the classes become table columns (note that columns that were mandatory in the specific classes become optional in the merged table).</li><li>A separate selector column is generated, which indicates the type of the object carried by the particular line.</li></ol><p>The <strong>Selector Column Name</strong>, <strong>Selector Column Type </strong>and <strong>Selector Column Type Modifier </strong>transformation properties determine the selector column format.</p><p>This strategy is suitable for very small hierarchies usually of just one hierarchy level with a couple of specialization classes, each adding a small number of properties to the base class. E.g., general class “VehicleRegistration” and a couple of subclasses: “CarRegistration” and “TruckRegistration”.</p><p>This strategy suites simple cases well. It is simple and fast. However, it does not scale for larger hierarchies and produces sparse tables (tables with many null values in the unused columns) in this case.</p><h4><strong>Conclusions and future improvements</strong></h4><p>Note that all hierarchies from the transformation source are converted using the same method. You cannot choose different strategies for each particular case of the generalization tree. This is considered as a future improvement for the transformations.</p><p><br /></p><h3><strong>Conversion of DataTypes</strong></h3><p>You can choose two strategies to transform datatype of data to SQL as follows:</p><ul><li>To transform datatypes to <strong>structured user defined types</strong>. This is a default case.</li></ul><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 34 Example of Datatype Transformation to Structured User Defined Types.png" /></ac:image>Example of datatype transformation to structured user defined types.</h6><p>The same sample in the Oracle SQL code will look as follows.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e8bd4b46-9970-48d1-a60c-bd1bf3aa82fb"><ac:plain-text-body><![CDATA[CREATE SEQUENCE Shapes.Shape_SEQ;
CREATE OR REPLACE TYPE Shapes.integer AS OBJECT NOT FINAL INSTANTIABLE;
/
CREATE OR REPLACE TYPE Shapes.Point2D AS OBJECT
	(
	X integer,
	Y integer
	) NOT FINAL INSTANTIABLE;
/
CREATE OR REPLACE TYPE Shapes.Rectangle AS OBJECT
	(
	upperLeft Point2D,
	lowerRight Point2D
	) NOT FINAL INSTANTIABLE;
/
CREATE TABLE Shapes.Shape
(
	rect Rectangle,
	id integer,
	PRIMARY KEY(id)
);]]></ac:plain-text-body></ac:structured-macro><ul><li>To expand datatypes into <strong>separate columns </strong>at the point of usage. Each property of a class having a datatype as a type is expanded into a set of columns—one column per each attribute of the datatype (including inherited attributes). Column types are copied from the source datatype attribute types (modulo the transformation type mapping). If the original datatype attribute is multivalued, the resulting column is further modified in the same manner as multivalued class attributes. The datatype expansion is recursive.</li></ul><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 35 Example of DataType Transformation to Separate Columns.png" /></ac:image>Example of DataType transformation to separate columns.</h6><p>The same sample in the Oracle SQL code will look as follows.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="296a0f66-241e-4443-9b4d-ac0dd04c6365"><ac:plain-text-body><![CDATA[CREATE TABLE Shapes.Shape
(
	X_upperLeft_rect integer,
	Y_upperLeft_rect integer,
	X_lowerRight_rect integer,
	Y_lowerRight_rect integer,
	id integer,
	PRIMARY KEY(id)
);]]></ac:plain-text-body></ac:structured-macro><p>On the conversion of DataTypes into separate columns at the point of usage, you can define names of the columns. By default, the format “%r_%a” is used, where %r is a name of a class attribute and %a is a name of a DataType attribute. In the example depicted in the preceding figure, column names are constructed according to the default template, like rect_upperLeft_X, rect_lowerRight_Y and so on.</p><p>To select a strategy for the DataType transformation</p><hr /><p><br /></p><ol><li>In the <strong>Transformation Details </strong>(the 4th step of the <strong>Model Transformation Wizard</strong>), set the<strong> Expand datatypes </strong>value to</li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li><em>False </em>to transform datatypes to structured user defined types.</li><li><em>T</em><em>rue </em>to expand datatypes into separate columns at the point of usage</li></ul></li></ul><p>      2. Continue the transformation setup process.</p><p>To define a template name for columns</p><hr /><ol><li>In the <strong>Transformation Details </strong>(the 4th step of the <strong>Model Transformation Wizard</strong>), click the<strong> Expanded datatype column name template </strong>specification cell. The Edit button appears.</li><li>Click the Edit button and, in the opened <strong>Expanded datatype column name template </strong>dialog, define the column name. In the column name definition, you can use specific convenient names and the following patterns.</li></ol><ul><li>%r - a name of a class attribute</li><li>%a - a name of a datatype attribute</li><li>%t - a name of table</li></ul><p>      3. Click OK when you are done and continue the transformation setup process.</p><p>The column name template is defined in the <strong>Expanded datatype column name template </strong>property.</p><h3><strong>Conversio</strong><strong>n </strong><strong>o</strong><strong>f enumerations</strong></h3><p>When transforming enumerations, you can choose two following strategies:</p><p><strong><strong>• </strong></strong>To transform the enumeration to <strong>check constraints</strong> at the point of usage. This is the default case. Every class attribute of the enumeration type in the transformation source is transformed to the table column of a char type.</p><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 36 Example of Enumeration Transformation to Check Constraints.png" /></ac:image>Example of enumeration transformation to check constraints.</h6><p>The same sample in the SQL code will look as follows.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c3756428-da10-4a41-976f-70019995f945"><ac:plain-text-body><![CDATA[CREATE TABLE Enumeration_CheckConstraint.Account
(
	currency char (3),
	id_Account integer,
	CHECK(currency in ('EUR', 'JPY', 'LTL', 'USD')),
	PRIMARY KEY(id_Account)
);]]></ac:plain-text-body></ac:structured-macro><p>To transform enumerations to <strong>lookup tables</strong>. This strategy can handle the more complex enumerations, for example, enumerations having their own attributes. The lookup table is automatically populated with enumeration literal values, and INSERT statements are generated during the SQL code generation. For each attribute that enumeration source has (including inherited attributes) the column in the target table is created. Attributes are transformed using the normal transformation rules for class attributes (including the type mapping, data type expansion, if requested, and multivalue-attribute expansion). The <strong>name </strong>column is added to the lookup table and the primary key is automatically generated (see <ac:link ac:anchor="Primarykeysautogeneration"><ac:plain-text-link-body><![CDATA[Primary keys autogeneration]]></ac:plain-text-link-body></ac:link>). Every class attribute of the enumeration type in the transformation source is transformed to the foreign key.</p><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 37 Example of Enumeration Transformation to Lookup Tables.png" /></ac:image>Example of enumeration transformation to lookup tables.</h6><p>The same sample in the SQL code will look as follows.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a89065db-5a0d-4b88-8075-db436390e2bc"><ac:plain-text-body><![CDATA[CREATE TABLE Enumeration_LookupTables.Currency
(
	longDescription varchar (255),
	USDRate,
	id_Currency integer,
	name char (3) NOT NULL,
	PRIMARY KEY(id_Currency)
);
INSERT INTO Enumeration_LookupTables.Currency(id_Currency, name) VALUES(0, 'EUR');
INSERT INTO Enumeration_LookupTables.Currency(id_Currency, name) VALUES(1, 'JPY');
INSERT INTO Enumeration_LookupTables.Currency(id_Currency, name) VALUES(2, 'LTL');
INSERT INTO Enumeration_LookupTables.Currency(id_Currency, name) VALUES(3, 'USD');

CREATE SEQUENCE Enumeration_LookupTables.Currency_SEQ;

CREATE SEQUENCE Enumeration_LookupTables.Account_SEQ;

CREATE TABLE Enumeration_LookupTables.Account
(
	currency integer,
	id_Account integer,
	PRIMARY KEY(id_Account),
	FOREIGN KEY(currency) REFERENCES Enumeration_LookupTables.Currency
(id_Currency)
);]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p>To select a strategy for the Enumeration transformation</p><hr /><ol><li>In the <strong>Transformation Details </strong>(the 4th step of the <strong>Model Transformation Wizard</strong>), click the <strong>Enumeration transformation strategy </strong>specification cell. The list of available strategies appears. Select one of the following.</li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li><strong>Check Constraints </strong>to transform the enumeration to check constraints at the point of usage.</li><li><strong>Lookup Table </strong>to transform enumeration to lookup tables.</li></ul></li></ul><p>      2. Continue the transformation setup process.</p><h3><strong>Packag</strong><strong>e hierarchy reorganization</strong></h3><p>UML models usually have a moderately deep package nesting organization, while SQL models can have at most one package level - the schemas. Hence during the transformation, packages should be reorganized.</p><p>The <strong>Change package hierarchy </strong>transformation property governs the package reorganization. Possible choices for setting the property value are as follows.</p><ol><li><strong>Leave intact </strong>choice switches reorganization off.</li><li><strong>Flatten packages </strong>choice forces flattening of the packages of the source, leaving only the top level packages in the destination.</li><li><strong>Strip packages </strong>choice removes all packages of the source.</li></ol><h3><strong>Namin</strong><strong>g of transformed elements</strong></h3><p>While transforming your UML models to SQL, you can modify names of the transformed elements according to given naming rules. There are several predefined rules as follows.</p><ul><li>Replace spaces or special characters in the element name with the underscore sign “_”. For example, the name in source “Customer Profile” and “Terms&amp;Conditions” could be transformed as “Customer_Profile” and “Terms_Conditions” accordingly.</li><li>Capitalize element names after the transformation. For example, the name in source “Customer” could be transformed as “CUSTOMER”.</li><li>Pluralize element names after transformation. For example, the name in source “Customer” could be transformed as “Customers”.</li><li>Detect the camel case edge in element names on transformation. For example, the name in source “CustomerProfile” could be transformed as “Customer_Profile”.</li></ul><p><br /></p><p>To select a naming rule</p><hr /><ol><li>In the <strong>Transformation Details </strong>(this is the last step of the <strong>Model Transformation Wizard</strong>), click the <strong>Name conversion rules </strong>specification cell. The cell expands and the Edit button appears.</li><li>Click the Edit button. The <strong>Select Opaque Behavior «Naming Rule» </strong>dialog opens.</li><li>In the opened dialog, select naming rules you want to use in transforming element names. You may select more than one rule.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9d89208b-024f-45f3-a3db-0a4be8cae06f"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>Be sure the search includes auxiliary resources! To turn on the appropriate search mode, click <strong>Include elements from modules into search results</strong>.</li><li>To select several naming rules, click the <strong>Multiple Selection</strong> button.</li></ul></ac:rich-text-body></ac:structured-macro><p>Naming rules are as follows.</p><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 18.8843%;" /><col style="width: 59.3246%;" /><col style="width: 21.7911%;" /></colgroup><tbody><tr><th>Rule name</th><th>Description</th><th>Example</th></tr><tr><td>CamelCaseSeparator</td><td>Detects all the occurrences in the original name of the situation where lower case letter is followed by upper case letter and insert the underscore sign '_' character between.</td><td><p>CustomerProfile &gt; Customer_Profile</p></td></tr><tr><td>LowerCase</td><td>All Unicode letter characters in the source name are converted to their lower case version in the result name. Other character are passed through unchanged.</td><td><p>CUSTOMER 1 &gt; customer 1</p></td></tr><tr><td>Pluralization</td><td><p>All original names that do not end with character 'S' or 's' will have the 's' character appended.</p></td><td><p>Customer &gt; Customers</p></td></tr><tr><td>SpecialCharacterEscape</td><td>All Unicode characters in the source name that are not letters and not numbers are converted to an underscore sign ‘_’ in the result name. Other character are passed through unchanged.</td><td><p>Terms&amp;Conditions &gt; Terms_Conditions</p></td></tr><tr><td>UpperCase</td><td>All Unicode letter characters in the source name are converted to their upper case version in the result name. Other character are passed through unchanged.</td><td><p>Customer 1 &gt; CUSTOMER 1</p></td></tr><tr><td>WhitespaceEscape</td><td>All Unicode whitespace characters in the source name are converted to an underscore sign ‘_’ in the result name. Other character are passed through unchanged.</td><td><p>Customer 1 &gt; Customer_1</p></td></tr></tbody></table><p><br /></p><p>       4. Click <strong>OK </strong>when you are done.</p><p>You can also create your custom naming rules using structured expressions or various scripts. The naming rule is an executable opaque behavior. The following procedure describes one of the possible ways to create a custom naming rule.</p><p>To create a custom naming rule</p><hr /><ol><li>Create a package for the naming rule data.</li><li>In this package, create an Opaque Behavior with the following parameters exactly in the same order as follows:</li></ol><ul><li style="text-align: left;">sourceElement : Element</li><li style="text-align: left;">targetElement : Element</li><li>initialName : String</li></ul><p style="margin-left: 30.0px;">The return parameter is of a java.lang.Object type.</p><p style="margin-left: 30.0px;"><br /></p><p><ac:image ac:height="250"><ri:attachment ri:filename="java lang Object type Return Parameter.png" /></ac:image></p><h6>Return parameter of a java.lang.Object type.</h6><p><br /></p><p>       3. Use the <strong>Model Transformation Profile.mdzip </strong>module. On the main menu, click <strong>File </strong>&gt; <strong>Use Module</strong>. The required module is located in the &lt;install.root&gt;\profiles\Model_Transformation_Profile.mdzip. Click <strong>Finish </strong>after you have selected the module.</p><p>       4. In the Model Browser, select the Opaque Behavior you have created and apply the «NamingRule» stereotype on it. Open the opaque behavior’s shortcut menu and click <strong>Stereotype</strong>. In the opened <strong>Select Stereotype </strong>list, select the «NamingRule» stereotype and click <strong>Apply</strong>.</p><p>       5. Open the opaque behavior’s Specification window and specify the <strong>Body and Language </strong>property. Actually, this is a property where you define your custom naming rule. Click property specification cell and then click the Edit button.</p><p>       6. In the opened <strong>Body and Language </strong>dialog, select a language for defining your naming rule and create the rule’s body.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="22d4848b-96dc-40a5-b6f8-ec238f6fa23d"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>The SQL language is not suitable for defining naming rules.</li><li>If you choose the Structured Expression language, turn on the Expert mode to get the all list of possible operations.</li></ul></ac:rich-text-body></ac:structured-macro><p>        7. Click <strong>OK </strong>when you are done. The naming rule you have created appears in the <strong>Name conversion rules </strong>selection list.</p><h3><strong>Transformin</strong><strong>g </strong><strong>documentation</strong></h3><p>Documentation can be copied either with or without HTML formatting information. If you need to retain the formatting information, click to select the <strong>Allow HTML in comments </strong>check box in the <strong>Transformation Details </strong>pane (the 4th step of the <strong>Model Transformation Wizard</strong>).</p><p>The model element documentation is turned into SQL comments during the DDL script generation.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="8ca8cc63-adef-4578-9572-3b4a5f705819"><ac:parameter ac:name="title">Tip</ac:parameter><ac:rich-text-body><p>You can turn off the comment generation. For this, do the following:</p><ol><li>From the <strong>Options </strong>menu, select <strong>Project</strong>. The <strong>Project Options </strong>dialog opens.</li><li>Select <strong>DDL Language Options </strong>on the left (you may need to expand the <strong>Code Engineering </strong>node). The appropriately named pane opens on the right.</li><li>Click to clear the <strong>Generate documentation </strong>check box.</li><li>Click <strong>OK</strong>.</li></ol></ac:rich-text-body></ac:structured-macro><p><br /></p><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 38 SQL Comments with and without HTML Formatting Information.png" /></ac:image>SQL comments with and without HTML formatting information.</h6><h3><strong>Excluding elements from transformation</strong></h3><p>Elements can be excluded from the transformation in one of the following ways.</p><ul><li>By deselecting these elements in the 2nd step of the <strong>Model Transformation Wizard</strong>.</li><li>By specifying rules for the automatic exclusion of elements in the 4th step of the wizard. These rules must be defined as executable opaque behaviors.</li></ul><p>To define a rule for automatic elements’ exclusion</p><hr /><ol><li>Create an executable opaque behavior.</li></ol><p>      2. Create an input parameter, whose type is <em>Element, </em>the abstract UML metaclass, and multiplicity is [1].</p><p>      3. Create a return parameter, whose type is java.lang.Object and multiplicity is [1].</p><p>      4. Specify the <strong>Language and Body </strong>property value for the new opaque behavior.</p><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bbf14f85-87b9-4092-b3f7-842da328393d"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p>Let’s say we need to exclude from the transformation all the classes with the «pendingReview» stereotype applied.</p><p>For this, we must do the following.</p><ol><li>Select <strong>StructuredExpression </strong>as language of the opaque behavior body.</li><li>Define the body by creating a TypeTest operation, which takes the collection of elements and returns only the ones with the «pendingReview» stereotype applied (see the following figure).</li></ol><p>For more information about the TypeTest operation, see <ac:link><ri:page ri:space-key="MD2024xR1 Refresh1 Refresh1" ri:content-title="Calling operations from the model" /></ac:link> in MagicDraw User Guide.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:image ac:height="250"><ri:attachment ri:filename="Define the Body by Creating a TypeTest Operation in the Body and Language Dialog Box.png" /></ac:image></p><h6>Defining the body by creating a TypeTest operation in the Body and Language dialog box.</h6><p><br /></p><p>To specify the rules for the automatic elements’ exclusion from the transformation</p><hr /><ol><li>In the <strong>Transformation Details </strong>pane (the 4th step of the <strong>Model Transformation Wizard</strong>), click the <strong>Elements exclusion rules </strong>specification cell. The Edit button appears.</li><li>Click the button and select one or more rules in the <strong>Select Opaque Behavior </strong>dialog.</li><li>Click <strong>OK </strong>when you are done and continue the transformation setup process.</li></ol><p><strong><ac:image ac:height="250"><ri:attachment ri:filename="Figure 39 Example of Transformation with Excluded Class.png" /></ac:image></strong></p><h6>Example of transformation with excluded class.</h6></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459794 space=CDMP2024xR1 version=6 -->
## PAGE 00068: Transformation properties

- page_id: `170459794`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459794/Transformation+properties
- version_number: 6
- version_date: `2024-05-08T14:01:59.092+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Transformations > UML to SQL transformation
- labels: []

### NORMALIZED CONTENT

917354555

917354557

917354556

This is the complete list of properties available in UML to SQL(Generic / Oracle) transformation in the **Model Transformation Wizard**(For more information about this wizard, see [CONFLUENCE_PAGE title='Model Transformation Wizard' space='MD2024x Refresh1 Refresh1 Refresh1'] in MagicDraw User Guide).

[IMAGE alt='' src='']

###### Model transformation wizard for UML to SQL (Generic/Oracle) transformation with Specify transformation details wizard step.

| Property name | Description |
| --- | --- |
| Autogenerated PK name template | If the class has no PK column in the ER model, this transformation parameter for the autogenerated column name will generate the PK. You may specify the pattern for the PK name.Default "id_%t", where %t is replaced by the name of the table. |
| Autogenerated PK type template | Specifies the type of the autogenerated PKs.Default: integer. |
| Autogenerated FK name template | The foreign keys are automatically generated to implement the relationships between classes.This transformation parameter autogenerates a FK name. You may specify the pattern for the name. Default: "fk_%t%k%r", where %t is replaced by the name of the table, the foreign key is pointing. The %k is replaced by the key name, to which this foreign key points. The %r is replaced by the name of the relationship, which is realized with this foreign key. |
| Autogenerated table name template | This transformation parameter autogenerates table name. You may specify the pattern for the name. Default "%t1_%t2", where %t1 is replaced by the name of the first table, %t2 - second table. The %r pattern (name of relationship) is also supported. |
| Generated index for alternative keys | If true, generates index for «AK».Default: false |
| Index name template | If the above option is set to true, you may choose the template for the index name. Template may contain %g pattern, which will be replaced with AK group name.Default: indexof_%g |
| Change package hierarchy | Choose option for packages from transformation source: to strip all the package hierarchy, or flatten the package hierarchy down to the first level where each package is transformed into the schema.Default: Flatten packages |
| Treat composition relationship as identifying | If this option is set to true, the composition associations are treated as if the «identifying» stereotype were applied to them.Default: true |
| Default association end multiplicity | If multiplicity was not specified in model, defined multiplicity will be set after transformation.Default: 1 |
| Generalization Tree transformation strategy | Selects the strategy to be used for converting generalization trees. Default: Multiple Values, Decomposed Object |
| Selector Column Name | Name of selector column for the merged table strategy of generalization conversionDefault: typeSelectorNote: together with selector type and type modifier this gives typeSelector:char(255) column. |
| Selector Column Type | Type of the selector column for the merged table strategy of generalization conversion.Default: char |
| Selector Column Type Modifier | Type modifier of the selector column for the merged table strategy of generalization conversionDefault: 255 |
| Max Duplicated Columns | Threshold for multivalue property conversion strategies - maximum number of columns for which the column duplication strategy is used. If exceeded, auxiliary value table is used.Default:3 |
| Value Table Name | Name of the value table (to be generated when converting multivalue properties). %t pattern is expanded to table name, %r - name of the original property.Default: %t_%r_VALUES(e.g Person_phone_VALUES table will be generated forPerson::phone[0..5] property in the source) |
| Autogenerate Sequences* | Selects wherever and when sequences are generated for PKsDefault: Generate sequences for all single-column PKs |
| Autogenerated Sequence Name* | Name of the generated sequences. %t pattern is expanded to table name.Default: %t_SEQ |
| Autogenerate PK | If true, primary keys are generated automatically.For more information, see . |
| Enumeration transformation strategy | For more information, see . |
| Expand datatypes | For more information, see . |
| Expanded datatype column name template | For more information, see . |
| Name conversion rules | One or more rules for element name conversion.For more information, see . |
| FK name template | An FK name template definition. You can use specific names and patterns, such as %t (a table name) or %r (a relationship role).For more information, see . |
| Elements exclusion rules | One or more rules for elements’ exclusion from the transformation.For more information, see . |
| Allow HTML in comments | If true, SQL comments in DDL script retain HTML formatting information.For more information, see . |

* - These properties are available only for UML to SQL (Oracle) transformation.

917354554

**Related page**

- [CONFLUENCE_PAGE title='Model Transformation Wizard' space='MD2024x Refresh1 Refresh1 Refresh1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5b0bb007-3d2a-49b5-b7a4-62308ca4d937"><ac:parameter ac:name="id">917354555</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="9f4d711a-249e-421b-a969-33f795474f06"><ac:parameter ac:name="id">917354557</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9591b80c-00e8-40dc-869b-a797e6eb9364"><ac:parameter ac:name="id">917354556</ac:parameter><ac:rich-text-body><p>This is the complete list of properties available in UML to SQL(Generic / Oracle) transformation in the <strong>Model Transformation Wizard </strong>(For more information about this wizard, see <ac:link><ri:page ri:space-key="MD2024x Refresh1 Refresh1 Refresh1" ri:content-title="Model Transformation Wizard" /></ac:link> in MagicDraw User Guide).</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 40 Model Transformation Wizard for UML to SQL (Generic Oracle) Transformation Specify Transformation.png" /></ac:image></p><h6 style="text-align: center;">Model transformation wizard for UML to SQL (Generic/Oracle) transformation with Specify transformation details wizard step.</h6><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 35.5135%;" /><col style="width: 64.4865%;" /></colgroup><tbody><tr><th>Property name</th><th>Description</th></tr><tr><td><p><strong>Autogenerated PK name template</strong></p></td><td><p>If the class has no PK column in the ER model, this transformation parameter for the autogenerated column name will generate the PK. You may specify the pattern for the PK name.</p>Default &quot;id_%t&quot;, where %t is replaced by the name of the table.</td></tr><tr><td><p><strong>Autogenerated PK type template</strong></p></td><td><p>Specifies the type of the autogenerated PKs.</p><p>Default: integer.</p></td></tr><tr><td><p><strong>Autogenerated FK name template</strong></p></td><td><p>The foreign keys are automatically generated to implement the relationships between classes.</p><p>This transformation parameter autogenerates a FK name. You may specify the pattern for the name. Default: &quot;fk_%t%k%r&quot;, where %t is replaced by the name of the table, the foreign key is pointing. The %k is replaced by the key name, to which this foreign key points. The %r is replaced by the name of the relationship, which is realized with this foreign key.</p></td></tr><tr><td><strong>Autogenerated table name template</strong></td><td><p>This transformation parameter autogenerates table name. You may specify the pattern for the name. Default &quot;%t1_%t2&quot;, where %t1 is replaced by the name of the first table, %t2 - second table. The %r pattern (name of relationship) is also supported.</p></td></tr><tr><td><strong>Generated index for alternative keys</strong></td><td><p>If <em>true</em>, generates index for «AK».</p><p>Default: false</p></td></tr><tr><td><strong>Index name template</strong></td><td><p>If the above option is set to <em>true</em>, you may choose the template for the index name. Template may contain %g pattern, which will be replaced with AK group name.</p>Default: indexof_%g</td></tr><tr><td><strong>Change package hierarchy</strong></td><td><p>Choose option for packages from transformation source: to strip all the package hierarchy, or flatten the package hierarchy down to the first level where each package is transformed into the schema.</p>Default: Flatten packages</td></tr><tr><td><strong>Treat composition relationship as identifying</strong></td><td><p>If this option is set to <em>true</em>, the composition associations are treated as if the «identifying» stereotype were applied to them.</p>Default: true</td></tr><tr><td><strong>Default association end multiplicity</strong></td><td><p>If multiplicity was not specified in model, defined multiplicity will be set after transformation.</p>Default: 1</td></tr><tr><td><strong>Generalization Tree transformation strategy</strong></td><td>Selects the strategy to be used for converting generalization trees. Default: Multiple Values, Decomposed Object</td></tr><tr><td><strong>Selector Column Name</strong></td><td><p>Name of selector column for the merged table strategy of generalization conversion</p><p>Default: typeSelector</p>Note: together with selector type and type modifier this gives typeSelector:char(255) column.</td></tr><tr><td><strong>Selector Column Type</strong></td><td><p>Type of the selector column for the merged table strategy of generalization conversion.</p>Default: char</td></tr><tr><td><p><strong>Selector Column Type <strong>Modifier</strong><br /></strong></p></td><td><p>Type modifier of the selector column for the merged table strategy of generalization conversion</p>Default: 255</td></tr><tr><td><strong>Max Duplicated Columns</strong></td><td><p>Threshold for multivalue property conversion strategies - maximum number of columns for which the column duplication strategy is used. If exceeded, auxiliary value table is used.</p>Default:3</td></tr><tr><td><strong>Value Table Name</strong></td><td><p>Name of the value table (to be generated when converting multivalue properties). %t pattern is expanded to table name, %r - name of the original property.</p><p>Default: %t_%r_VALUES</p><p>(e.g Person_phone_VALUES table will be generated for</p>Person::phone[0..5] property in the source)</td></tr><tr><td><strong>Autogenerate Sequences*</strong></td><td><p>Selects wherever and when sequences are generated for PKs</p>Default: Generate sequences for all single-column PKs</td></tr><tr><td><p><strong>Autogenerated Sequence Name*<br /></strong></p></td><td><p>Name of the generated sequences. %t pattern is expanded to table name.</p>Default: %t_SEQ</td></tr><tr><td><strong>Autogenerate PK</strong></td><td><p>If <em>true</em>, primary keys are generated automatically.</p>For more information, see <ac:link ac:anchor="Primarykeysautogeneration"><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Transformation procedure" /><ac:plain-text-link-body><![CDATA[Primary keys autogeneration]]></ac:plain-text-link-body></ac:link>.</td></tr><tr><td colspan="1"><strong>Enumeration transformation strategy</strong></td><td colspan="1"><p>For more information, see <ac:link ac:anchor="Conversionofenumerations"><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Transformation procedure" /><ac:plain-text-link-body><![CDATA[Conversion of enumerations]]></ac:plain-text-link-body></ac:link>.</p></td></tr><tr><td colspan="1"><strong>Expand datatypes</strong></td><td colspan="1">For more information, see <ac:link ac:anchor="ConversionofDataTypes"><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Transformation procedure" /><ac:plain-text-link-body><![CDATA[Conversion of DataTypes]]></ac:plain-text-link-body></ac:link>.</td></tr><tr><td colspan="1"><p><strong>Expanded datatype column name template</strong></p></td><td colspan="1"><p>For more information, see <ac:link ac:anchor="ConversionofDataTypes"><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Transformation procedure" /><ac:plain-text-link-body><![CDATA[Conversion of DataTypes]]></ac:plain-text-link-body></ac:link>.</p></td></tr><tr><td colspan="1"><strong>Name conversion rules</strong></td><td colspan="1"><p>One or more rules for element name conversion.</p>For more information, see <ac:link ac:anchor="Namingoftransformedelements"><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Transformation procedure" /><ac:plain-text-link-body><![CDATA[Naming of transformed elements]]></ac:plain-text-link-body></ac:link>.</td></tr><tr><td colspan="1"><strong>FK name template</strong></td><td colspan="1"><p>An FK name template definition. You can use specific names and patterns, such as %t (a table name) or %r (a relationship role).</p>For more information, see <ac:link ac:anchor="Conversionofassociations"><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Transformation procedure" /><ac:plain-text-link-body><![CDATA[Conversion of associations]]></ac:plain-text-link-body></ac:link>.</td></tr><tr><td colspan="1"><strong>Elements exclusion rules</strong></td><td colspan="1"><p>One or more rules for elements’ exclusion from the transformation.</p>For more information, see <ac:link ac:anchor="Excludingelementsfromtransformation"><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Transformation procedure" /><ac:plain-text-link-body><![CDATA[Excluding elements from transformation]]></ac:plain-text-link-body></ac:link>.</td></tr><tr><td colspan="1"><strong>Allow HTML in comments</strong></td><td colspan="1"><p>If <em>true</em>, SQL comments in DDL script retain HTML formatting information.</p>For more information, see <ac:link ac:anchor="Transformingdocumentation"><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Transformation procedure" /><ac:plain-text-link-body><![CDATA[Transforming documentation]]></ac:plain-text-link-body></ac:link>.</td></tr></tbody></table><p>* - These properties are available only for UML to SQL (Oracle) transformation.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ef8d89af-f8bb-4861-8552-b530cd9e9429"><ac:parameter ac:name="id">917354554</ac:parameter><ac:rich-text-body><p><strong>Related page</strong></p><ul><li><ac:link><ri:page ri:space-key="MD2024x Refresh1 Refresh1 Refresh1" ri:content-title="Model Transformation Wizard" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459772 space=CDMP2024xR1 version=6 -->
## PAGE 00069: Transformations

- page_id: `170459772`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459772/Transformations
- version_number: 6
- version_date: `2024-07-09T07:31:47.017+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

226806943

#### CONTENT-COLUMN: Note

226806945

226806942

#### CONTENT-BLOCK: Note

226806944

#### NOTE: Note

Note

The transformation engine implementation code is available from the MagicDraw Standard Edition upwards. However, there are just two transformations in MagicDraw: Any-to-Any and Profile Migration transformations. The Cameo Data Modeler plugin brings in a set of transformations between various kinds of data models.

The Cameo Data Modeler plugin for MagicDraw provides a set of transformations for transforming between various kinds of data models. These include:

- UML models to SQL models (2 flavors - generic and Oracle)
- ER models to SQL models (2 flavors - generic and Oracle)
- SQL models to UML models (suitable for all flavors of databases)
- UML models to XML schema models
- XML schema models to UML models

After the transformation, you can further refine the resulting model as necessary and generate artifact files from that model. You can generate actual DDL scripts and XML schema files using the code engineering facilities.

Because the Cameo Data Modeler plugin provides more powerful modeling and generation features for an Oracle database flavor, there are two separate transformation flavors as well: ER to SQL (Generic) and ER to SQL (Oracle). There are Oracle-specific modeling extensions and code engineering features for Oracle database scripts that cover more features.

#### NOTE: Note

Note

As of version 19.0, the Generic-Oracle DDL(SQL) transformation is no longer available in MagicDraw. This transformation is no longer needed, as previously separate profiles were unified for generic SQL and Oracle SQL modeling.

Access the functionality of performing model transformations in MagicDraw through the **Model Transformations W****izard**. Use the **Model Transformations W****izard** to create new transformations.

To open the **Model Transformations Wizard**

Do one of the following:

- From the Tools menu, choose Model Transformations .
- Select one or more packages. From the shortcut menu, choose Tools > Transform .

#### NOTE: Note

Note

For more information about the **Model Transformations W****izard**, see [CONFLUENCE_PAGE title='Model Transformation Wizard' space='MD2024xR1'] in MagicDraw User Guide.

Each transformation has its own default type map for replacing data types from the source domain into the appropriate data types of the result domain. If this type map is not suitable, the default type map can be modified. An entirely different type map can be provided if necessary.

#### NOTE: Note

Note

- For more information on creating your own transformation rules or changing mapping behavior, see [CONFLUENCE_PAGE title='Transformation Type Mapping' space='MD2024xR1'] in MagicDraw User Guide.
- For more information on setting up mapping, watch the “Transformations” online demo at https://www.youtube.com/watch?v=Ls4f12ieG44&ab_channel=CATIAMBSE .

916248357

**Related pages**

- [CONFLUENCE_PAGE title='Model Transformation Wizard' space='MD2024xR1']
- [CONFLUENCE_PAGE title='Transformation Type Mapping' space='MD2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a8f22956-d1bb-45fa-8215-f950daaed218"><ac:parameter ac:name="id">226806943</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="01a6d291-4ec7-4fc6-8d83-7e0459343bb3"><ac:parameter ac:name="id">226806945</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="faeb34b0-8476-48d2-84ee-1364c1335c6b"><ac:parameter ac:name="id">226806942</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="5df3a0ef-5196-48f1-91fe-cd7f15b2ec4c" /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5ac252a8-d9e1-45dd-b271-de4fb6666d58"><ac:parameter ac:name="id">226806944</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e7144bad-617e-4c99-9835-235382353e96"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The transformation engine implementation code is available from the MagicDraw Standard Edition upwards. However, there are just two transformations in MagicDraw: Any-to-Any and Profile Migration transformations. The Cameo Data Modeler plugin brings in a set of transformations between various kinds of data models.</p></ac:rich-text-body></ac:structured-macro><p>The Cameo Data Modeler plugin for MagicDraw provides a set of transformations for transforming between various kinds of data models. These include:</p><ul><li>UML models to SQL models (2 flavors - generic and Oracle)</li><li>ER models to SQL models (2 flavors - generic and Oracle)</li><li>SQL models to UML models (suitable for all flavors of databases)</li><li>UML models to XML schema models</li><li>XML schema models to UML models</li></ul><p>After the transformation, you can further refine the resulting model as necessary and generate artifact files from that model. You can generate actual DDL scripts and XML schema files using the code engineering facilities.</p><p>Because the Cameo Data Modeler plugin provides more powerful modeling and generation features for an Oracle database flavor, there are two separate transformation flavors as well: ER to SQL (Generic) and ER to SQL (Oracle). There are Oracle-specific modeling extensions and code engineering features for Oracle database scripts that cover more features.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="de44657c-6531-4dbc-8831-c6bd8f8c13db"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>As of version 19.0, the Generic-Oracle DDL(SQL) transformation is no longer available in MagicDraw. This transformation is no longer needed, as previously separate profiles were unified for generic SQL and Oracle SQL modeling.</p></ac:rich-text-body></ac:structured-macro><p>Access the functionality of performing model transformations in MagicDraw through the <strong>Model Transformations W</strong><strong>izard</strong>. Use the <strong>Model Transformations W</strong><strong>izard</strong> to create new transformations.</p><p><br /></p><p>To open the <strong>Model Transformations Wizard</strong></p><hr /><p>Do one of the following:</p><ul><li>From the <strong>Tools </strong>menu, choose <strong>Model Transformations</strong>.</li><li>Select one or more packages. From the shortcut menu, choose <strong>Tools </strong>&gt; <strong>Transform</strong>.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="97b27465-d529-480f-ae9f-ec4e1d538e2b"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>For more information about the <strong>Model Transformations W</strong><strong>izard</strong>, see <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Model Transformation Wizard" /></ac:link> in MagicDraw User Guide.</p></ac:rich-text-body></ac:structured-macro><p>Each transformation has its own default type map for replacing data types from the source domain into the appropriate data types of the result domain. If this type map is not suitable, the default type map can be modified. An entirely different type map can be provided if necessary.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="34faea93-f762-461a-ab53-c6cc07466dbc"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>For more information on creating your own transformation rules or changing mapping behavior, see <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Transformation Type Mapping" /></ac:link> in MagicDraw User Guide.</li><li>For more information on setting up mapping, watch the “Transformations” online demo at <a href="https://www.youtube.com/watch?v=Ls4f12ieG44&amp;ab_channel=CATIAMBSE">https://www.youtube.com/watch?v=Ls4f12ieG44&amp;ab_channel=CATIAMBSE</a>.</li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f51ef3be-29a8-4e9a-812b-c53337321215"><ac:parameter ac:name="id">916248357</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Model Transformation Wizard" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Transformation Type Mapping" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459793 space=CDMP2024xR1 version=5 -->
## PAGE 00070: Type mapping

- page_id: `170459793`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459793/Type+mapping
- version_number: 5
- version_date: `2024-05-08T14:01:25.362+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Transformations > UML to SQL transformation
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

917198887

#### CONTENT-COLUMN: Note

917198890

#### CONTENT-BLOCK: Note

917198888

Default type maps of the UML to SQL (Generic / Oracle) transformations remap the types that are commonly used in the UML modeling domain (such as String) into types that are suitable for SQL domain (such as varchar).

##### **UML to SQL Type Map**

The default type map for these transformations is stored in the **UML to SQL Type Map**profile and automatically gets attached to your project at the 3rd step (the type mapping step) of the transformation wizard. If necessary it can be changed.

The Default map carries the following type conversions.

| Source Type | Result Type |
| --- | --- |
| String | varchar (default)varchar2char varyingcharacter varyingnvarcharnvarchar2nchar varyingnational char varyingnational character varyinglongvarcharlong varcharcharcharacterncharnational charnational characterlong char |
| short | smallint |
| long | number(20) |
| Integer | integer |
| int | int |
| float | float |
| double | double precision |
| date | date |
| char | char(default)characterncharnational charnational character |
| byte | number(3) |
| boolean | number(1) |

If you have a situation when one type map imports another type map, you can specify another default mapping rule. Such situation appears, for example, in the Oracle type map, inheriting from the Standard type map where the Oracle mapping rule String-->varchar2 overrides the base mapping rule String-->varchar. For more information about the type mapping, see [CONFLUENCE_PAGE title='Transformation Type Mapping' space='MD2024x Refresh1 Refresh1 Refresh1'] and [CONFLUENCE_PAGE title='Controlling Type Mapping Rule Behavior' space='MD2024x Refresh1 Refresh1 Refresh1'] in MagicDraw User Guide.

#### NOTE: Note

Note

This feature is available with MagicDraw 18.0 SP1 or later.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="af010474-e15c-4312-a2ab-4135c8941a83"><ac:parameter ac:name="id">917198887</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="2edebaee-8f09-4afe-b85b-1d80448bfc1e"><ac:parameter ac:name="id">917198890</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7953b92e-4227-4a61-b5cf-7166a9fb4786"><ac:parameter ac:name="id">917198888</ac:parameter><ac:rich-text-body><p>Default type maps of the UML to SQL (Generic / Oracle) transformations remap the types that are commonly used in the UML modeling domain (such as String) into types that are suitable for SQL domain (such as varchar).</p><h3><strong>UML to SQL Type Map</strong></h3><p>The default type map for these transformations is stored in the <strong>UML to SQL Type Map </strong>profile and automatically gets attached to your project at the 3rd step (the type mapping step) of the transformation wizard. If necessary it can be changed.</p><p>The Default map carries the following type conversions.</p><table class="relative-table wrapped" style="width: 33.0225%;"><colgroup><col style="width: 45.6794%;" /><col style="width: 54.3206%;" /></colgroup><tbody><tr><th>Source Type</th><th>Result Type</th></tr><tr><td>String</td><td><p>varchar (default)</p><p>varchar2</p><p>char varying</p><p>character varying</p><p>nvarchar</p><p>nvarchar2</p><p>nchar varying</p><p>national char varying</p><p>national character varying</p><p>longvarchar</p><p>long varchar</p><p>char</p><p>character</p><p>nchar</p><p>national char</p><p>national character</p><p>long char</p></td></tr><tr><td>short</td><td>smallint</td></tr><tr><td>long</td><td>number(20)</td></tr><tr><td>Integer</td><td>integer</td></tr><tr><td>int</td><td>int</td></tr><tr><td>float</td><td>float</td></tr><tr><td>double</td><td>double precision</td></tr><tr><td>date</td><td>date</td></tr><tr><td>char</td><td><p>char(default)</p><p>character</p><p>nchar</p><p>national char</p><p>national character</p></td></tr><tr><td>byte</td><td>number(3)</td></tr><tr><td>boolean</td><td>number(1)</td></tr></tbody></table><p>If you have a situation when one type map imports another type map, you can specify another default mapping rule. Such situation appears, for example, in the Oracle type map, inheriting from the Standard type map where the Oracle mapping rule String--&gt;varchar2 overrides the base mapping rule String--&gt;varchar. For more information about the type mapping, see <ac:link><ri:page ri:space-key="MD2024x Refresh1 Refresh1 Refresh1" ri:content-title="Transformation Type Mapping" /></ac:link> and <ac:link><ri:page ri:space-key="MD2024x Refresh1 Refresh1 Refresh1" ri:content-title="Controlling Type Mapping Rule Behavior" /></ac:link> in MagicDraw User Guide.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="af270da6-1ac2-4479-bce1-5bab6bd34328"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>This feature is available with MagicDraw 18.0 SP1 or later.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459773 space=CDMP2024xR1 version=1 -->
## PAGE 00071: UML to SQL transformation

- page_id: `170459773`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459773/UML+to+SQL+transformation
- version_number: 1
- version_date: `2023-09-21T12:46:57.467+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Transformations
- labels: []

### NORMALIZED CONTENT

237093793

237093795

237093792

true

237093794

There are two very similar UML to DDL transformations:

1. UML to SQL (Generic)
2. UML to SQL (Oracle)

These transformations convert the selected part of a UML model with class diagrams into Generic or Oracle SQL models with Oracle SQL diagrams respectively.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a67ba747-9426-4d35-849b-a5df735e4f8d"><ac:parameter ac:name="id">237093793</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="36ed12f5-1e41-490d-9110-db62e1906892"><ac:parameter ac:name="id">237093795</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="257d72ef-365f-4a72-ae27-bc11f4a2ead5"><ac:parameter ac:name="id">237093792</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="a6acd33d-c210-492f-b77e-06ab0eed36e4"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2022a36f-225f-4964-9076-7b5a0ff2dd49"><ac:parameter ac:name="id">237093794</ac:parameter><ac:rich-text-body><p>There are two very similar UML to DDL transformations:</p><ol><li>UML to SQL (Generic)</li><li>UML to SQL (Oracle)</li></ol><p>These transformations convert the selected part of a UML model with class diagrams into Generic or Oracle SQL models with Oracle SQL diagrams respectively.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459815 space=CDMP2024xR1 version=5 -->
## PAGE 00072: UML to XML schema transformation

- page_id: `170459815`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459815/UML+to+XML+schema+transformation
- version_number: 5
- version_date: `2024-05-08T14:18:47.711+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Transformations
- labels: []

### NORMALIZED CONTENT

34012851

34012854

34012852

The UML to XML Schema transformation helps create an equivalent XML schema model from a given UML model. Basically, this transformation creates a copy of a source UML model, then applies the necessary stereotypes according to the XML schema modeling rules.

##### **Type mapping**

This type map stores mapping between primitive UML data types and primitive XML Schema data types.

[IMAGE alt='' src='']

###### UML to XML schema type map.

###### [IMAGE alt='' src='']UML to XML schema type map (Continued).

##### **Transformation results**

After the UML models have been transformed to XML schema models, you will see the following results.

- For each class in the transformation destination set, the «XSDcomplexType» stereotype is applied, unless this class is derived from simple XML type (one of the basic types, or type, stereotyped with XSDsimpleType). In that case, an «XSDsimpleType» stereotype is applied. There are conditions when the «XSDcomplexType» and «XSDsimpleType» stereotypes are used, listed in the table below:

| Condition | Result |
| --- | --- |
| The class is derived from another class, stereotyped as «XSDcomplexType». | The «XSDcomplexContent» stereotype is applied on this class with «XSDextension» on the corresponding generalization relationship. |
| The class is derived from another class, stereotyped as «XSDsimpleType». | The «XSDrestriction» stereotype is applied on the corresponding generalization relationship. |
| The class is not derived from anything, and has attributes with the XSDelement tag. | The «XSDcomplexContent» stereotype is applied on this class. |
| The class is not derived from anything, and has no attributes with the XSDelement tag. | No «XXXXContent» stereotype is applied on this class - the class has an empty content. |
| The UML datatypes in the transformation source set are transformed into the classes with the «XSDsimpleType» stereotype (unless after the type map this class appears to be derived from a class with the «XSDcomplexType» stereotype). | The «XSDcomplexType» stereotype is used. |
| Each attribute of the class is not of the simple XML type (that is, one of the basic types, or type, stereotyped with the «XSDsimpleType») or has a multiplicity more than 1. | The «XSDelement» stereotype is applied. |

- For each composition association, two linking classes are stereotyped as XML schema types. The stereotype on the association end is applied the same as the rules for attributes.
- Enumerations in the UML model are transformed into the enumerations in the XML Schema model. Classes with the «XSDsimpleType» stereotype are derived by restriction from the XML string type, where all the elements of the original enumeration are converted into the attributes with an «XSDenumeration» stereotype.
- For each package in the transformation set, the «XSDnamespace» stereotype is applied.
- In each package, one additional class for the XML schema is created. The name of the schema class is constructed by taking the name of the package and then appending the .xsd to it (e.g. if the package in the source model set is named "user", name the schema class "user.xsd" in the destination package).
- The targetNamespace value is added to the schema class with the name of its parent (e.g. if the schema is placed in the "http://magicdraw.com/User" package, the targetNamespace=" http://magicdraw.com/User" is set on the schema class).
- Schema class and the namespaces http://www.w3c.org/2001/XMLSchema [XML Schema profile] and its target namespace are linked using the xmlns relationships. The names of these links are: the same as the target namespace for the link to the target namespace; and "xs" for the XML Schema namespace.
- Class diagrams are transformed into XML Schema diagrams.
- The model elements that have no meaning in the XML schemas are discarded. This includes (without limitation) behavioral features of classes, interfaces, actors, use cases, states, activities, objects, messages, stereotypes and tag definitions.
- There are additional properties to choose for UML to XML Schema transformation in the Model Transformation Wizard. For more information about the wizard, see [CONFLUENCE_PAGE title='Model Transformation Wizard' space='MD2024xR1'] in MagicDraw User Guide.

###### [IMAGE alt='' src='']Model transformation wizard for UML to XML schema transformation with Specify transformation details.

| Option name | Type | Description |
| --- | --- | --- |
| Default Compositor | Combo box | Possible choices: XSDall, XSDchoice, XSDsequenceDetermines element grouping in complex types of XML Schema.Default: XSDall |
| Default Attribute Kind | Combo box | Determines which attribute kind (XSDelement or XSDattribute UML) the attribute will be mapped to.Default: XSDelement |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="7934f669-395c-4a6e-897f-3580af0cf036"><ac:parameter ac:name="id">34012851</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="73676c16-f4c6-491f-b8b8-099d9c5d451c"><ac:parameter ac:name="id">34012854</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e4a34870-94cc-493c-82e7-51f91181eebc"><ac:parameter ac:name="id">34012852</ac:parameter><ac:rich-text-body><p>The UML to XML Schema transformation helps create an equivalent XML schema model from a given UML model. Basically, this transformation creates a copy of a source UML model, then applies the necessary stereotypes according to the XML schema modeling rules.</p><h3><strong>Type mapping</strong></h3><p>This type map stores mapping between primitive UML data types and primitive XML Schema data types.</p><p><ac:image ac:height="250"><ri:attachment ri:filename="Figure 43 UML to XML schema type map (1).png" /></ac:image></p><h6 style="text-align: center;">UML to XML schema type map.</h6><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 44 UML to XML schema type map (2).png" /></ac:image>UML to XML schema type map (Continued).</h6><h3><strong>Transformation results</strong></h3><p>After the UML models have been transformed to XML schema models, you will see the following results.</p><ul><li>For each class in the transformation destination set, the «XSDcomplexType» stereotype is applied, unless this class is derived from simple XML type (one of the basic types, or type, stereotyped with XSDsimpleType). In that case, an «XSDsimpleType» stereotype is applied. There are conditions when the «XSDcomplexType» and «XSDsimpleType» stereotypes are used, listed in the table below:</li></ul><table class="relative-table wrapped" style="width: 99.9451%;"><colgroup><col style="width: 52.3595%;" /><col style="width: 47.6405%;" /></colgroup><tbody><tr><th>Condition</th><th>Result</th></tr><tr><td>The class is derived from another class, stereotyped as «XSDcomplexType».</td><td>The «XSDcomplexContent» stereotype is applied on this class with «XSDextension» on the corresponding generalization relationship.</td></tr><tr><td>The class is derived from another class, stereotyped as «XSDsimpleType».</td><td>The «XSDrestriction» stereotype is applied on the corresponding generalization relationship.</td></tr><tr><td>The class is not derived from anything, and has attributes with the <strong>XSDelement </strong>tag.</td><td>The «XSDcomplexContent» stereotype is applied on this class.</td></tr><tr><td>The class is not derived from anything, and has no attributes with the <strong>XSDelement </strong>tag.</td><td>No «XXXXContent» stereotype is applied on this class - the class has an empty content.</td></tr><tr><td>The UML datatypes in the transformation source set are transformed into the classes with the «XSDsimpleType» stereotype (unless after the type map this class appears to be derived from a class with the «XSDcomplexType» stereotype).</td><td>The «XSDcomplexType» stereotype is used.</td></tr><tr><td>Each attribute of the class is not of the simple XML type (that is, one of the basic types, or type, stereotyped with the «XSDsimpleType») or has a multiplicity more than 1.</td><td>The «XSDelement» stereotype is applied.</td></tr></tbody></table><ul><li>For each composition association, two linking classes are stereotyped as XML schema types. The stereotype on the association end is applied the same as the rules for attributes.</li><li>Enumerations in the UML model are transformed into the enumerations in the XML Schema model. Classes with the «XSDsimpleType» stereotype are derived by restriction from the XML string type, where all the elements of the original enumeration are converted into the attributes with an «XSDenumeration» stereotype.</li><li>For each package in the transformation set, the «XSDnamespace» stereotype is applied.</li><li>In each package, one additional class for the XML schema is created. The name of the schema class is constructed by taking the name of the package and then appending the .xsd to it (e.g. if the package in the source model set is named &quot;user&quot;, name the schema class &quot;user.xsd&quot; in the destination package).</li><li>The targetNamespace value is added to the schema class with the name of its parent (e.g. if the schema is placed in the <a href="http://magicdraw.com/User">&quot;http://magicdraw.com/User&quot; </a>package, the targetNamespace=&quot; <a href="http://magicdraw.com/User">http://magicdraw.com/User&quot; </a>is set on the schema class).</li><li>Schema class and the namespaces <a href="http://www.w3c.org/2001/XMLSchema">http://www.w3c.org/2001/XMLSchema </a>[XML Schema profile] and its target namespace are linked using the xmlns relationships. The names of these links are: the same as the target namespace for the link to the target namespace; and &quot;xs&quot; for the XML Schema namespace.</li><li>Class diagrams are transformed into XML Schema diagrams.</li><li>The model elements that have no meaning in the XML schemas are discarded. This includes (without limitation) behavioral features of classes, interfaces, actors, use cases, states, activities, objects, messages, stereotypes and tag definitions.</li><li>There are additional properties to choose for UML to XML Schema transformation in the <strong>Model Transformation Wizard. </strong>For more information about the wizard, see <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Model Transformation Wizard" /></ac:link> in MagicDraw User Guide.</li></ul><p><br /></p><h6 style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Figure 45 Model Transformation Wizard for UML to XML Schema Transformation Specify Transformation Details.png" /></ac:image>Model transformation wizard for UML to XML schema transformation with Specify transformation details.</h6><p><br /></p><table class="relative-table wrapped" style="width: 99.0675%;"><colgroup><col style="width: 13.4017%;" /><col style="width: 12.903%;" /><col style="width: 73.6953%;" /></colgroup><tbody><tr><th>Option name</th><th>Type</th><th>Description</th></tr><tr><td><p><strong>Default Compositor</strong></p></td><td><strong>Combo box</strong></td><td><p>Possible choices: XSDall, XSDchoice, XSDsequence</p><p>Determines element grouping in complex types of XML Schema.</p><p>Default: XSDall</p></td></tr><tr><td><p><strong>Default Attribute Kind</strong></p></td><td><strong>Combo box</strong></td><td><p>Determines which attribute kind (XSDelement or XSDattribute UML) the attribute will be mapped to.</p><p>Default: XSDelement</p></td></tr></tbody></table></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459861 space=CDMP2024xR1 version=5 -->
## PAGE 00073: Union

- page_id: `170459861`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459861/Union
- version_number: 5
- version_date: `2024-05-08T14:22:01.528+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

- The UML Class must have the additional stereotype XSDunion.
- “memberTypes” and inner simpleTypes maps to several UML Generalizations between the simple type and members types.
- In order to have an inner simpleType element, the parent of this Generalization must be an inner Class of an outer UML Class.

###### [IMAGE alt='' src='']

###### Union model example.

#### PANEL: Union model and XML code samples

Union model and XML code samples

```text
<xs:schema xmlns:nm = "http://nomagic.com" xmlns:xs = "http://www.w3.org/2001/XMLSchema" targetNamespace = "http://nomagic.com" >	<xs:simpleType name = "my_simple_union" >
```

```text
<xs:union id = "unionID" memberTypes = "xs:string xs:number" />	</xs:simpleType>
```

```text
<xs:simpleType name = "my_simple_union2" >
```

```text
<xs:annotation >
```

```text
<xs:documentation >very important documentation</xs:documentation>
```

```text
</xs:annotation>
```

```text
<xs:union id = "unionID" memberTypes = "xs:number" >  			<xs:simpleType > 				<xs:restriction base = "xs:number" />
```

```text
</xs:simpleType> 		</xs:union>
```

```text
</xs:simpleType>
```

```text
</xs:schema>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ul><li>The UML Class must have the additional stereotype XSDunion.</li><li>“memberTypes” and inner simpleTypes maps to several UML Generalizations between the simple type and members types.</li><li>In order to have an inner simpleType element, the parent of this Generalization must be an inner Class of an outer UML Class.</li></ul><h6><ac:image ac:height="250"><ri:attachment ri:filename="Figure 73 Union Example Model and XML Code2.png" /></ac:image></h6><h6 style="text-align: center;">Union model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="52b0db29-d7c1-4a90-bc63-cf186f5700d7"><ac:parameter ac:name="title">Union model and XML code samples</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot; &gt;<br />	&lt;xs:simpleType name = &quot;my_simple_union&quot; &gt;</pre><pre>		&lt;xs:union id = &quot;unionID&quot; memberTypes = &quot;xs:string xs:number&quot; /&gt;<br />	&lt;/xs:simpleType&gt;</pre><pre>	&lt;xs:simpleType name = &quot;my_simple_union2&quot; &gt;</pre><pre>		&lt;xs:annotation &gt;</pre><pre>			&lt;xs:documentation &gt;very important documentation&lt;/xs:documentation&gt;</pre><pre>		&lt;/xs:annotation&gt;</pre><pre>		&lt;xs:union id = &quot;unionID&quot; memberTypes = &quot;xs:number&quot; &gt; <br /> 			&lt;xs:simpleType &gt; <br />				&lt;xs:restriction base = &quot;xs:number&quot; /&gt;</pre><pre>			&lt;/xs:simpleType&gt; <br />		&lt;/xs:union&gt;</pre><pre>	&lt;/xs:simpleType&gt;</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459901 space=CDMP2024xR1 version=4 -->
## PAGE 00074: Unique

- page_id: `170459901`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459901/Unique
- version_number: 4
- version_date: `2024-05-08T13:11:36.081+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute added into some UML Class.

#### PANEL: unique mapping to UML attributes

unique mapping to UML attributes

```text
<unique
```

```text
id = ID
```

```text
name = NCName
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?, (selector, field+))
```

```text
</unique>
```

For a unique UML model example, see [CONFLUENCE_PAGE title='Keyref' space='CDMP2024x Refresh1 Refresh1 Refresh1R1'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute added into some UML Class.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a188a070-bc59-48ef-beef-eceef1364911"><ac:parameter ac:name="title">unique mapping to UML attributes</ac:parameter><ac:rich-text-body><pre>&lt;unique</pre><pre>	id = ID</pre><pre>	name = NCName</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?, (selector, field+))</pre><pre>&lt;/unique&gt;</pre></ac:rich-text-body></ac:structured-macro><p>For a unique UML model example, see <ac:link><ri:page ri:space-key="CDMP2024x Refresh1 Refresh1 Refresh1R1" ri:content-title="Keyref" /></ac:link>.</p>
````

<!--NOMAGIC_PAGE id=170459696 space=CDMP2024xR1 version=1 -->
## PAGE 00075: User guide

- page_id: `170459696`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459696/User+guide
- version_number: 1
- version_date: `2023-09-21T12:46:55.061+02:00`
- ancestors: Cameo Data Modeler Plugin
- labels: []

### NORMALIZED CONTENT

The Cameo Data Modeler plugin provides data-related modeling for MagicDraw. It includes entity-relationship, database and XML schema modeling features.

This plugin enables you to draw entity-relationship diagrams using the crow's foot notation. This is a full- featured variant of the ER diagram, including extended entity-relationship concepts (such as generalization), providing a spectrum of capabilities for logical data modeling.

This plugin provides SQL database modeling / diagramming and DDL script generation / reverse features. It supports 11 flavors of databases (including Standard SQL, Oracle, DB2, Microsoft SQL Server, MySQL, PostgreSQL), has separate type libraries for them, and carries additional modeling extensions for Oracle databases. It also provides transformations from / to plain UML models and from ER models.

This plugin provides XML schema modeling / diagramming and schema file (*.xsd) generation / reversing features. Transformations to/from plain UML models are provided.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Cameo Data Modeler plugin provides data-related modeling for MagicDraw. It includes entity-relationship, database and XML schema modeling features.</p><p>This plugin enables you to draw entity-relationship diagrams using the crow's foot notation. This is a full- featured variant of the ER diagram, including extended entity-relationship concepts (such as generalization), providing a spectrum of capabilities for logical data modeling.</p><p>This plugin provides SQL database modeling / diagramming and DDL script generation / reverse features. It supports 11 flavors of databases (including Standard SQL, Oracle, DB2, Microsoft SQL Server, MySQL, PostgreSQL), has separate type libraries for them, and carries additional modeling extensions for Oracle databases. It also provides transformations from / to plain UML models and from ER models.</p><p>This plugin provides XML schema modeling / diagramming and schema file (*.xsd) generation / reversing features. Transformations to/from plain UML models are provided.</p>
````

<!--NOMAGIC_PAGE id=170459734 space=CDMP2024xR1 version=6 -->
## PAGE 00076: Virtual entities

- page_id: `170459734`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459734/Virtual+entities
- version_number: 6
- version_date: `2024-05-08T13:48:49.435+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Entity-relationship (ER) modeling and diagrams
- labels: []

### NORMALIZED CONTENT

Virtual entities can be derived from information in other entities. They are marked with the keyword «virtual» on diagrams. They can be handled in the same manner as other entities.

Virtual entities roughly correspond to views in databases.

If you need to specify exactly how virtual entities are derived from other entities, you can use Abstraction relationships from UML. You can specify the derivation expression in the Mapping field.

[IMAGE alt='' src='']

###### Example of virtual entity usage in an ER diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Virtual entities can be derived from information in other entities. They are marked with the keyword «virtual» on diagrams. They can be handled in the same manner as other entities.</p><p>Virtual entities roughly correspond to views in databases.</p><p>If you need to specify exactly how virtual entities are derived from other entities, you can use Abstraction relationships from UML. You can specify the derivation expression in the Mapping field.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 13 Virtual Entity Usage in ER Diagram.png" /></ac:image></p><h6 style="text-align: center;">Example of virtual entity usage in an ER diagram.</h6>
````

<!--NOMAGIC_PAGE id=170459801 space=CDMP2024xR1 version=5 -->
## PAGE 00077: Virtual entity transformation

- page_id: `170459801`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459801/Virtual+entity+transformation
- version_number: 5
- version_date: `2024-05-08T14:03:12.520+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Transformations > ER to SQL (generic / Oracle) transformations
- labels: []

### NORMALIZED CONTENT

919216430

919216432

919216431

Virtual entities of ER models can be transformed into the following different elements of SQL models.

- Tables (just as ordinary, non-virtual entities).
- SQL views (ER to SQL(Oracle) transformation has an additional choice of simple views or materialized views).

The choice is controlled by the **Virtual Entities Transformed To**transformation property.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5ca9c2f2-dd0f-4975-915d-4f93ceb42f3d"><ac:parameter ac:name="id">919216430</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="edc7edc1-a369-4f92-b2c6-b364df24d473"><ac:parameter ac:name="id">919216432</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3edc3f83-d22c-4209-ad4e-202110547e68"><ac:parameter ac:name="id">919216431</ac:parameter><ac:rich-text-body><p>Virtual entities of ER models can be transformed into the following different elements of SQL models.</p><ul><li>Tables (just as ordinary, non-virtual entities).</li><li>SQL views (ER to SQL(Oracle) transformation has an additional choice of simple views or materialized views).</li></ul><p>The choice is controlled by the <strong>Virtual Entities Transformed To </strong>transformation property.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459892 space=CDMP2024xR1 version=1 -->
## PAGE 00078: WhiteSpace

- page_id: `170459892`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459892/WhiteSpace
- version_number: 1
- version_date: `2023-09-21T12:47:02.611+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Attribute with the stereotype XSDwhiteSpace. The name and type of such an attribute do not make sense.

- value – to Attribute initial value.

#### PANEL: whiteSpace XML representation summary

whiteSpace XML representation summary

```text
<whiteSpace
```

```text
fixed = boolean : false
```

```text
id = ID
```

```text
value = (collapse | preserve | replace)
```

```text
{any attributes with non-schema namespace…}>
```

```text
Content: (annotation?)
```

```text
</whiteSpace>
```

#### PANEL: whiteSpace XML code sample

whiteSpace XML code sample

```text
The following example is the datatype definition for the token built-in derived datatype.
```

```text
<simpleType name='token'>
```

```text
<restriction base='normalizedString'>
```

```text
<whiteSpace value='collapse'/>
```

```text
</restriction>
```

```text
</simpleType>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Attribute with the stereotype XSDwhiteSpace. The name and type of such an attribute do not make sense.</p><ul><li style="text-align: left;">value – to Attribute initial value.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="744d5a95-b52a-4dd5-9f9f-f43876ef51ff"><ac:parameter ac:name="title">whiteSpace XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;whiteSpace</pre><pre>	fixed = boolean : false</pre><pre>	id = ID</pre><pre>	value = (collapse | preserve | replace)</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/whiteSpace&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c4463701-752f-4a2f-88f6-a7ab5ac60fbf"><ac:parameter ac:name="title">whiteSpace XML code sample</ac:parameter><ac:rich-text-body><pre>The following example is the datatype definition for the token built-in derived datatype.</pre><pre>&lt;simpleType name='token'&gt;</pre><pre>	&lt;restriction base='normalizedString'&gt;</pre><pre>		&lt;whiteSpace value='collapse'/&gt;</pre><pre>	&lt;/restriction&gt;</pre><pre>&lt;/simpleType&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170459824 space=CDMP2024xR1 version=2 -->
## PAGE 00079: XML schema mapping to UML elements

- page_id: `170459824`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459824/XML+schema+mapping+to+UML+elements
- version_number: 2
- version_date: `2024-05-08T14:20:23.709+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas
- labels: []

### NORMALIZED CONTENT

The following XML schemas are applied to UML elements for a variety of purposes:

1

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The following XML schemas are applied to UML elements for a variety of purposes:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="366a48ee-d6e0-45d1-9609-63b566cbf291"><ac:parameter ac:name="depth">1</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=170459960 space=CDMP2024xR1 version=5 -->
## PAGE 00080: XML schema namespaces

- page_id: `170459960`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459960/XML+schema+namespaces
- version_number: 5
- version_date: `2024-05-08T14:29:08.221+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > XML schemas > XML schema mapping to UML elements
- labels: []

### NORMALIZED CONTENT

Maps to a UML Package with the stereotype *XSDnamespace*. To define the “xmlns” attribute in the schema file, you must add Permission between the XSDnamespace package and XSDschema class into the model.

- The Permission name maps to the namespace shortcut.

#### PANEL: XML representation of the skeleton of a schema

XML representation of the skeleton of a schema

```text
<xs:schema
```

```text
xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="http://www.w3.org/2001/XMLSchema" 	targetNamespace="http://www.example.com/example">	…
```

```text
</xs:schema>
```

To generate these namespaces

- The UML model must have a Package with the name *http://www.w3.org/2001/XMLSchema*
- The UML model must have a Package with the name *http://www.example.com/example*
- Permission with the name “xs” must be added into the model between the XMLSchema Class and the Package *http://www.w3.org/2001/XMLSchema*
- Permission without a name must be added into the model between the XMLSchema Class and the Package *http://www.w3.org/2001/XMLSchema*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Maps to a UML Package with the stereotype <em>XSDnamespace</em>. To define the “xmlns” attribute in the schema file, you must add Permission between the XSDnamespace package and XSDschema class into the model.</p><ul><li style="text-align: left;">The Permission name maps to the namespace shortcut.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="25a3f67b-f948-4360-855f-a52180b34a0c"><ac:parameter ac:name="title">XML representation of the skeleton of a schema</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema</pre><pre>	xmlns:xs=&quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; xmlns=&quot;<a href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a>&quot; <br />	targetNamespace=&quot;<a href="http://www.example.com/example">http://www.example.com/example</a>&quot;&gt;<br />	…</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p>To generate these namespaces</p><hr /><ul><li>The UML model must have a Package with the name <a href="https://www.w3.org/2001/XMLSchema"><em>http://www.w3.org/2001/XMLSchema</em></a></li><li>The UML model must have a Package with the name <a href="https://docs.nomagic.com/www.example.com/example"><em>http://www.example.com/example</em></a></li><li>Permission with the name “xs” must be added into the model between the XMLSchema Class and the Package <a href="https://www.w3.org/2001/XMLSchema"><em>http://www.w3.org/2001/XMLSchema</em></a></li><li>Permission without a name must be added into the model between the XMLSchema Class and the Package<a href="https://www.w3.org/2001/XMLSchema"><em> http://www.w3.org/2001/XMLSchema</em></a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=170459819 space=CDMP2024xR1 version=4 -->
## PAGE 00081: XML schema to UML transformation

- page_id: `170459819`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459819/XML+schema+to+UML+transformation
- version_number: 4
- version_date: `2024-05-08T13:11:35.178+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide > Transformations
- labels: []

### NORMALIZED CONTENT

34120459

34120461

34120460

The XML Schema to UML transformation helps extract the abstract UML model from the XML schema model.

##### **T****yp****e mapping**

Type maps store mapping between primitive UML data types and primitive XML Schema data types. The same applies for UML to XML Schema Transformation in reverse as well. For XML Schema to UML element type mapping diagram, see [Type mapping](https://docs.nomagic.com/display/CDMP2024x Refresh1 Refresh1 Refresh1/UML+to+XML+schema+transformation#UMLtoXMLschematransformation-Typemapping).

##### **Transformation results**

Once the XML schema has been transformed to UML models, you will see the following:

- The XML Schema diagrams are transformed to the Class diagrams. Unnecessary stereotypes (XSDxxxx) are discarded from the classes.
- Attributes of the classes are gathered if they were spread into several different classes.
- Attributes of the classes may be realized as associations. In this case the main class gathers all the associations of the members.
- The same principle is applied when elements are in a group shared by two or more classes. Elements (attributes) are copied into both destination classes.
- The attributes with the «XSDgroupRef» stereotype are treated as if the group relationship has been drawn and transformed accordingly. They are discarded in the UML model, and the group content (elements / attributes) placed in their place.
- Simple XML schema types (classes with the «XSDsimpleType» stereotype), which after copying and type remap are derived from any data type (UML DataType), or not derived from anything and are transformed into the UML data types.
- Simple XML schema types derived by restriction from a string, restricted by enumerating string values, and are converted into enumerations in the UML diagrams.
- The classes with the «XSDschema» stereotype are not copied into a destination model.
- The «XDSkey», «XSDkeyref», and «XSDunique» stereotyped attributes are not copied into a destination model.
- The «XDSany», «XSDanyAttribute» stereotyped attributes are not copied into a destination model. The «XDSnotation» stereotyped attributes are not copied into a destination model.
- The «XDSlength», «XDSminLength», «XDSmaxLength», «XSDpattern», «XSDfractionDigits», «XSDtotalDigits», «XDSmaxExclusive», «XDSmaxInclusive», «XDSminExclusive», and «XDSminInclusive» stereotyped attributes are not copied into a destination model.
- The XML schemas (classes with the «XSDschema» stereotype) should not be transformed, but they may contain inner classes (anonymous types of schema elements). These inner classes are transformed using the usual rules for UML type transformation, as if they were not inner classes but normal XML schema types.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d66487b0-196c-49c0-8716-339063007f15"><ac:parameter ac:name="id">34120459</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="e02e92c6-6c92-4ed4-8f19-40b8c76351c5"><ac:parameter ac:name="id">34120461</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="52440dbf-7dfd-4c40-9a88-2d63fbcdb252"><ac:parameter ac:name="id">34120460</ac:parameter><ac:rich-text-body><p>The XML Schema to UML transformation helps extract the abstract UML model from the XML schema model.</p><h3><strong>T</strong><strong>yp</strong><strong>e mapping</strong></h3><p>Type maps store mapping between primitive UML data types and primitive XML Schema data types. The same applies for UML to XML Schema Transformation in reverse as well. For XML Schema to UML element type mapping diagram, see <span class="toc-item-body"><a href="https://docs.nomagic.com/display/CDMP2024x Refresh1 Refresh1 Refresh1/UML+to+XML+schema+transformation#UMLtoXMLschematransformation-Typemapping" class="toc-link">Type mapping</a></span>.</p><h3><strong>Transformation results</strong></h3><p>Once the XML schema has been transformed to UML models, you will see the following:</p><ul><li>The XML Schema diagrams are transformed to the Class diagrams. Unnecessary stereotypes (XSDxxxx) are discarded from the classes.</li><li>Attributes of the classes are gathered if they were spread into several different classes.</li><li>Attributes of the classes may be realized as associations. In this case the main class gathers all the associations of the members.</li><li>The same principle is applied when elements are in a group shared by two or more classes. Elements (attributes) are copied into both destination classes.</li><li>The attributes with the «XSDgroupRef» stereotype are treated as if the group relationship has been drawn and transformed accordingly. They are discarded in the UML model, and the group content (elements / attributes) placed in their place.</li><li>Simple XML schema types (classes with the «XSDsimpleType» stereotype), which after copying and type remap are derived from any data type (UML DataType), or not derived from anything and are transformed into the UML data types.</li><li>Simple XML schema types derived by restriction from a string, restricted by enumerating string values, and are converted into enumerations in the UML diagrams.</li><li>The classes with the «XSDschema» stereotype are not copied into a destination model.</li><li>The «XDSkey», «XSDkeyref», and «XSDunique» stereotyped attributes are not copied into a destination model.</li><li>The «XDSany», «XSDanyAttribute» stereotyped attributes are not copied into a destination model. The «XDSnotation» stereotyped attributes are not copied into a destination model.</li><li>The «XDSlength», «XDSminLength», «XDSmaxLength», «XSDpattern», «XSDfractionDigits», «XSDtotalDigits», «XDSmaxExclusive», «XDSmaxInclusive», «XDSminExclusive», and «XDSminInclusive» stereotyped attributes are not copied into a destination model.</li><li>The XML schemas (classes with the «XSDschema» stereotype) should not be transformed, but they may contain inner classes (anonymous types of schema elements). These inner classes are transformed using the usual rules for UML type transformation, as if they were not inner classes but normal XML schema types.</li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170459823 space=CDMP2024xR1 version=5 -->
## PAGE 00082: XML schemas

- page_id: `170459823`
- space_key: `CDMP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CDMP2024xR1/pages/170459823/XML+schemas
- version_number: 5
- version_date: `2024-05-08T14:20:08.140+02:00`
- ancestors: Cameo Data Modeler Plugin > User guide
- labels: []

### NORMALIZED CONTENT

34795249

34795251

34795250

For more information about defining data types to be used in XML Schemas and other XML specifications, see [XML Schema: Datatypes](http://www.w3.org/TR/xmlschema-2/).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="7e2c593e-0139-4b1d-a690-08b2799936ac"><ac:parameter ac:name="id">34795249</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ebb39a47-b826-4507-82fd-6cab7db47855"><ac:parameter ac:name="id">34795251</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="30f82500-31e9-45fe-bc9a-571d8753b02e"><ac:parameter ac:name="id">34795250</ac:parameter><ac:rich-text-body><p>For more information about defining data types to be used in XML Schemas and other XML specifications, see <a href="http://www.w3.org/TR/xmlschema-2/">XML Schema: Datatypes</a>.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````
