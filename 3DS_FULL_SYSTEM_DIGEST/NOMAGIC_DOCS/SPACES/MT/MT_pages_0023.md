# NOMAGIC DOCUMENTATION SPACE: Modeling Tools

<!--NOMAGIC_SPACE key=MT chunk=23 -->

<!--NOMAGIC_PAGE id=272729622 space=MT version=1 -->
## PAGE 03486: (2026x) Modeling types

- page_id: `272729622`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272729622/2026x+Modeling+types
- version_number: 1
- version_date: `2025-11-25T13:35:25.093+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) Data-related modeling > (2026x) Database support > (2026x) Database modeling
- labels: ['msosa']

### NORMALIZED CONTENT

Cameo Data Modeler provides the standard type libraries as well as ability to model user defined types (structured user defined types and composites - multiset, array data types). The types can then be used to specify columns of the tables and / or parameters of procedures and functions. There is also a special mechanism for using types with modifiers. This mechanism is common in the MagicDraw, however some explanation is necessary on how to use it in database modeling.

##### Predefined type libraries

Cameo Data Modeler provides predefined type libraries for database flavors it supports. Besides the standard SQL type library, there are type libraries for Oracle, DB2, MS SQL, MySQL, PostgreSQL, Sybase, Cloudscape (Derby), Pervasive, MS Access and Pointbase. The standard SQL type library is the main type library, and type libraries for each flavor import (a subset of) types from it and define additional types, specific for that flavor.

The necessary type library is imported when you create the Database or Schema element in your model and choose a flavor for it (See the Database flavor selection dialog in [CONFLUENCE_PAGE title='(2026x) Top level elements' space='']).

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

###### [IMAGE alt='' src='']Examples of user defined types.

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

Besides attributes, Structured UDTs have a collection of methods - operations, performing actions on values of this type. Methods are covered in a separate section with stored procedures and functions (see [CONFLUENCE_PAGE title='(2026x) Routines' space=''] section).

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
<p>Cameo Data Modeler provides the standard type libraries as well as ability to model user defined types (structured user defined types and composites - multiset, array data types). The types can then be used to specify columns of the tables and / or parameters of procedures and functions. There is also a special mechanism for using types with modifiers. This mechanism is common in the MagicDraw, however some explanation is necessary on how to use it in database modeling.</p><h3>Predefined type libraries</h3><p>Cameo Data Modeler provides predefined type libraries for database flavors it supports. Besides the standard SQL type library, there are type libraries for Oracle, DB2, MS SQL, MySQL, PostgreSQL, Sybase, Cloudscape (Derby), Pervasive, MS Access and Pointbase. The standard SQL type library is the main type library, and type libraries for each flavor import (a subset of) types from it and define additional types, specific for that flavor.</p><p>The necessary type library is imported when you create the Database or Schema element in your model and choose a flavor for it (See the Database flavor selection dialog in <ac:link><ri:page ri:content-title="(2026x) Top level elements" /></ac:link>).</p><h3>Type usage</h3><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure 21 Type Specifying. Library Type and Modifier vs. Separately Modeled Type.png"><ri:page ri:content-title="(2026x) Modeling types" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Type specifying. Library type and modifier vs. separately modeled type.</h6><p>Usage of a simple SQL type, such as <strong>boolean</strong>, is very simple. If you want to set it as a type of a column or operation parameter, you just need to specify it in the <strong>type </strong>field. However, there are types (such as <strong>varchar </strong>or <strong>numeric</strong>) in SQL, which require additional data. There are two mechanisms to specify these kinds of types: either use the library type+ type modifier mechanism or create your own type element.</p><p>Let's take the standard <strong>varchar </strong>type as an example. It must have the maximum length data provided at each usage. Semantically there are many different types, one for each length limit - <strong>varchar(20)</strong>, <strong>varchar(53)</strong>, <strong>varchar(255) </strong>etc. Now the standard type library cannot provide myriad of different <strong>varchar </strong>types. Library only provides the <strong>varchar </strong>type definition.</p><p><br /></p><p>To specify that column is of <strong>varchar(20)</strong></p><hr /><ol><li data-uuid="a935c724-e86c-4bf7-a391-ecd63de5d5f4">Set the <strong>type </strong>field of the column to <strong>varchar </strong>type from the library.</li><li data-uuid="e0fb3cdc-3fdf-4afc-9555-3147e7050b6f">Set the <strong>type modifier </strong>field of the column to “<strong>(20)</strong>” (no quotes). Note that type modifier is a simple string - whatever is entered in this field, will be used in script generation verbatim, without additional checks. An example of more complex type modifier would be “<strong>(10, 2)</strong>” type modifier for <strong>numeric </strong>data type.</li></ol><p>Alternative way to specify that column is of <strong>varchar(20) </strong>is to explicitly create a separate type in the model.</p><p><br /></p><p>To specify that column is of varchar(20) in the alternative way</p><hr /><ol><li data-uuid="00bfe2a1-b0be-4ae3-bf39-df693350c403">Create the necessary type (use one of the buttons in the SQL diagram, Primitive Types toolbar) - character string, fixed precision, integer, approximate, boolean, binary, date or XML types. In our case this would be character string type.</li><li data-uuid="6f4a799b-b745-4135-9684-491e7d804321">Set the length data in the dedicated tag (look up the <strong>length </strong>tag in the <strong>Tags </strong>section of the Specification window). Note that this is numeric field - you need to input number 20, and not the “(20)” string as was the case with type modifiers.</li><li data-uuid="b436fef3-a828-4d6e-aa34-ddcdca67e26f">The name of your type can be whatever you like. For example, <strong>varchar_of_20</strong>. The name is not important.</li><li data-uuid="0e32743c-393d-4c23-a370-5fc99a629720">Inherit (draw generalization relationship) your type from the appropriate type from the type library. In this case, inherit <strong>varchar_of_20 </strong>from <strong>varchar </strong>form the library. This information will be used for determining the proper type name during script generation (Therefore, in the generated script, you will see the proper type reference - <strong>varchar(20)</strong>).</li><li data-uuid="0016cce4-ebd0-48a8-a793-6d74e91a545b">This created type can now be specified in the <strong>type </strong>field of the column(s).</li></ol><p>There would be one type in the model for each <strong>varchar </strong>length that you use in your database.</p><p>The second way is more tedious - you need to create quite a few types. Therefore, by default, the first way is used. But the second way has several advantages, that may outweigh it’s deficiencies. First - there is one spot where parameters of the type can be changed. You can easily widen the varchar(20) fields to varchar(40) by editing just one place in the model. Secondly, you can define some additional parameters of the type - such as character set.</p><h3><strong>User defined types</strong></h3><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="Figure 22 Examples of User Defined Types.png"><ri:page ri:content-title="(2026x) Modeling types" /></ri:attachment></ac:image>Examples of user defined types.</h6><p>Besides the primitive / built-in types of the database, user can define additional types for his own schema.</p><h4>Distinct type</h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c973d125-fee5-481a-a32c-636fe003ee79"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body>SQL Distinct type is modeled as UML DataType with «DistinctUserDe- finedType» stereotype applied. For the sake of compactness, refer- ences are displayed with the «distinct» keyword (instead of the long form - «DistinctUserDefinedType») on the diagram.</ac:rich-text-body></ac:structured-macro><p>Distinct type definition allows to redefine some primitive type in order to enforce the non-assignability rules. For example, two distinct types <strong>Meters </strong>and <strong>Yards </strong>can be defined on the base primitive type <strong>float</strong>. With this definition, system would enforce checks that yard fields / columns are not assigned to meter fields / columns without a conversion (explicit cast).</p><p>Besides the standard SQL element properties, distinct type has the following properties available in the Specification window.</p><table class="relative-table" style="width: 99.7806%;"><colgroup class=""><col class="" style="width: 21.828%;" /><col class="" style="width: 78.172%;" /></colgroup><tbody class=""><tr class=""><th>Property name</th><th>Description</th></tr><tr class=""><td><p><strong>Predefined Representation</strong></p></td><td>Points to some base primitive type.</td></tr></tbody></table><h4>Domain</h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a248e1ff-b54a-4aa8-b663-0207e9c8ae5c"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Domain is modeled as UML DataType with «Domain» stereotype applied. For the sake of compactness, domains are displayed with the «domain» keyword on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Domain allows to define a more narrow set of values than the base primitive type allows. This narrowing is done by assigning additional constraints on the domain. Columns, whose types are set to the domain, can only assume values from this more narrow subset.</p><p>Besides the standard SQL element properties, domain has the following properties available in the Specification window.</p><table class="relative-table" style="width: 99.7806%;"><colgroup class=""><col class="" style="width: 21.993%;" /><col class="" style="width: 78.007%;" /></colgroup><tbody class=""><tr class=""><th>Property name</th><th>Description</th></tr><tr class=""><td><p><strong>Predefined Representation<br /></strong></p></td><td>Points to some base primitive type.</td></tr><tr class=""><td><strong>Default Value</strong></td><td>Default value for the column if no value is specified.</td></tr></tbody></table><h4><strong>Structured user defined type</strong></h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9bdbface-3fed-47c4-a725-d473e161583c"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Structured User Defined Type is modeled as UML DataType with «StructuredUserDefinedType» stereotype applied. For the sake of com- pactness, domains are displayed with the «structured» keyword (instead of the long form - «StructuredUserDefinedType») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Structured UDT defines a composite datatype. Each value of this type is a tuple of several values; each position in a tuple has a name. Structured UDT value is analogous to one row of the table. Structured UDTs allow single inheritance (multiple inheritance is not supported). Inheritance (subtype-supertype relationship) can be modeled using UML Generalization relationships.</p><p>Besides the standard SQL element properties, structured UDT has the following properties available in the Specification window.</p><table class="relative-table" style="width: 99.5612%;"><colgroup class=""><col class="" style="width: 22.591%;" /><col class="" style="width: 77.409%;" /></colgroup><tbody class=""><tr class=""><th>Property name</th><th>Description</th></tr><tr class=""><td><p><strong>Instantiable</strong></p></td><td><p>Defines</p></td></tr><tr class=""><td><p><strong>Final</strong></p></td><td><p>Default value for the column if no value is specified.</p></td></tr><tr class=""><td><p><strong>Super</strong></p></td><td><p>Shows base data types. This is a derived field, it is not editable. To make changes, use UML Generalization relationships.</p></td></tr></tbody></table><p>Parts of the structured UDT (properties) are called attributes (compare - parts of the table definition are called columns). Attributes of structured UDT are created like columns of the table, that is, via the <strong>Attribute Definitions </strong>tab in the structured UDT Specification window or using an appropriate smart manipulation button on its shape.</p><p>Besides the standard SQL element properties, attribute has the following properties available in the Specification window.</p><table class="relative-table" style="width: 99.616%;"><colgroup class=""><col class="" style="width: 22.7438%;" /><col class="" style="width: 77.2562%;" /></colgroup><tbody class=""><tr class=""><th>Property name</th><th>Description</th></tr><tr class=""><td><strong>Type</strong></td><td rowspan="2"><p>Collectively these two fields describe the type of the attribute. The same considerations as for column type modeling apply.</p></td></tr><tr class=""><td><strong>Type Modifier</strong></td></tr><tr class=""><td><strong>Default Value</strong></td><td>Carries the default value of the attribute.</td></tr><tr class=""><td><strong>Scope Check</strong></td><td rowspan="2"><p>Marks this attribute as scope checked to a particular table and allows choosing particular referential integrity ensuring action (RESTRICT CASCADE, etc).</p></td></tr><tr class=""><td><strong>Scope Checked</strong></td></tr></tbody></table><p>Besides attributes, Structured UDTs have a collection of methods - operations, performing actions on values of this type. Methods are covered in a separate section with stored procedures and functions (see <ac:link><ri:page ri:content-title="(2026x) Routines" /></ac:link> section).</p><h4>Array type</h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="195d4354-a730-4f84-a798-718d8708749f"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Array type is modeled as UML DataType with «ArrayDataType» stereotype applied. For the sake of compactness, arrays are displayed with the «array» keyword (instead of the long form - «ArrayDataType») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Array type defines an array (that is, list of values, with the indexed, O(1) access to the n-th element) of the values of elementary type. Besides the standard SQL element properties, array type has the following properties available in the Specification window.</p><table class="relative-table" style="width: 99.9451%;"><colgroup class=""><col class="" style="width: 23.0533%;" /><col class="" style="width: 76.9467%;" /></colgroup><tbody class=""><tr class=""><th>Property name</th><th>Description</th></tr><tr class=""><td><p><strong>Element</strong></p></td><td><p>The elementary type of the set elements.</p></td></tr><tr class=""><td><p><strong>Max Cardinality</strong></p></td><td><p>The size limit of the array.</p></td></tr></tbody></table><p><br /></p><h4><strong>Multiset type</strong></h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1b4008e4-b7d7-4b12-931a-e96b2611ddde"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Multiset type is modeled as UML DataType with «MultisetDataType» stereotype applied. For the sake of compactness, multisets are displayed with the «multiset» keyword (instead of the long form - «MultisetDataType») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Multiset type defines a set of elements of the elementary type. Besides the standard SQL element properties, multiset has the following properties available in the Specification window.</p><table class="relative-table" style="width: 99.9451%;"><colgroup class=""><col class="" style="width: 23.0853%;" /><col class="" style="width: 76.9147%;" /></colgroup><tbody class=""><tr class=""><th>Property name</th><th>Description</th></tr><tr class=""><td><p><strong>Element</strong></p></td><td><p>The elementary type of the set elements.</p></td></tr></tbody></table><p><br /></p><h4><strong>Reference types</strong></h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6ca2dc2c-339e-49f4-84f1-07b3f488edb6"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Reference type is modeled as UML DataType with «ReferenceDataType» stereotype applied. For the sake of compactness, references are displayed with the «ref» keyword (instead of the long form - «ReferenceDataType») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Reference type defines a pointer to the data of the referred type. Besides the standard SQL element properties, reference type has the following properties available in the Specification window.</p><table class="relative-table" style="width: 99.9451%;"><colgroup class=""><col class="" style="width: 23.1009%;" /><col class="" style="width: 76.8991%;" /></colgroup><tbody class=""><tr class=""><th><p><strong>Property name</strong></p></th><th><p><strong>Description</strong></p></th></tr><tr class=""><td><p><strong>Referenced Type</strong></p></td><td><p>The type of the data that is being referenced.</p></td></tr><tr class=""><td><p><strong>Scope Table</strong></p></td><td><p>Limit the references to the data of the particular table.</p></td></tr></tbody></table><p><br /></p><h4>Row type</h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="65020c0f-fa8e-413a-9918-9511a0c20a87"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>SQL Row Data Type is modeled as UML DataType with «RowDataType» stereotype applied. For the sake of compactness, row data types are displayed with the «row» keyword (instead of the long form - «RowDataType») on the diagram.</p></ac:rich-text-body></ac:structured-macro><p>Represents one row of the table. The difference from structured UDT is that row type represents a value stored in the table, while structured UDT represents “free-floating” value during computation. For example, it is meaningful to take address for the row, but not of the structured UDT value.</p><p>Parts of the row data type (properties) are called fields (compare - parts of the table definition are called columns). Fields for row data type are created like columns of the table, that is, via the <strong>Fields </strong>tab in the row data type Specification window or using an appropriate smart manipulation button on its shape.</p><p>Besides the standard SQL element properties, field has the following properties available in the Specification window.</p><table class="relative-table" style="width: 99.9451%;"><colgroup class=""><col class="" style="width: 23.6061%;" /><col class="" style="width: 76.3939%;" /></colgroup><tbody class=""><tr class=""><th><p> <strong>Property name</strong></p></th><th><p> <strong>Description</strong></p></th></tr><tr class=""><td><p><strong>T</strong><strong>ype</strong></p></td><td rowspan="2"><p>Collectively these two fields describe the type of the field. The same considerations as for column type modeling apply.</p></td></tr><tr class=""><td><p><strong>T</strong><strong>ype Modifier</strong></p></td></tr><tr class=""><td><strong>Scope Check</strong></td><td rowspan="2"><p>Marks this field as scope checked to a particular table and allows choosing particular referential integrity ensuring action (RESTRICT CASCADE, etc).</p></td></tr><tr class=""><td><strong>Scope Checked</strong></td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=272733709 space=MT version=1 -->
## PAGE 03487: (2026x) Models Migration

- page_id: `272733709`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733709/2026x+Models+Migration
- version_number: 1
- version_date: `2025-11-25T13:42:48.691+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) Migration User Guides > (2026x) UPDM projects migration manual > (2026x) UPDM 2.0 Migration to UPDM 2.1
- labels: ['msosa']

### NORMALIZED CONTENT

##### Data Mappings

The following table describes data mapping between UPDM 2.0 and UPDM 2.1.

###### Element mappings

| UPDM 2.0 | UPDM 2.1 | Comments |
| --- | --- | --- |
| Organization [InstanceSpecification] | ActualOrganization |  |

###### Element property mappings

| UPDM 2.0 | UPDM 2.1 | Comments |  |  |
| --- | --- | --- | --- | --- |
| UPDM Element | URI/URL | UPDM Element | URI |  |

###### Element metaclass mappings

| UPDM 2.0 [Metaclass] | UPDM 2.1 [Metaclass] |
| --- | --- |
| Exchange Element [DataType] | Exchange Element [Class] |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><h3>Data Mappings</h3><p>The following table describes data mapping between UPDM 2.0 and UPDM 2.1.</p><h4>Element mappings</h4><table><colgroup><col /><col /><col /></colgroup><tbody><tr><th>UPDM 2.0</th><th>UPDM 2.1</th><th>Comments</th></tr><tr><td>Organization [InstanceSpecification]</td><td>ActualOrganization</td><td><br /></td></tr></tbody></table><h4>Element property mappings</h4><table><colgroup><col /><col /><col /><col /><col /></colgroup><tbody><tr><th style="text-align: center;" colspan="2">UPDM 2.0</th><th style="text-align: center;" colspan="2">UPDM 2.1</th><th>Comments</th></tr><tr><td colspan="1"><span>UPDM Element</span></td><td>URI/URL</td><td>UPDM Element</td><td colspan="1"><span>URI</span></td><td><br /></td></tr></tbody></table><h4>Element metaclass mappings</h4><table><colgroup><col /><col /></colgroup><tbody><tr><th>UPDM 2.0 [Metaclass]</th><th>UPDM 2.1 [Metaclass]</th></tr><tr><td>Exchange Element [DataType]</td><td> Exchange Element [Class]</td></tr></tbody></table><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272729671 space=MT version=2 -->
## PAGE 03488: (2026x) Modifying BPMN Matrices

- page_id: `272729671`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272729671/2026x+Modifying+BPMN+Matrices
- version_number: 2
- version_date: `2025-11-25T14:47:26.391+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Using Cameo Business Modeler Plugin > (2026x) Using BPMN Tables and Matrices
- labels: ['msosa']

### NORMALIZED CONTENT

To change a row or column scope, do one of the following

- In the Model Browser, select one or more elements you wish to see on your matrix and drag them to the Row Scope/Column Scope box in the Criteria area.
- Click the ... button next to the Row Scope/Column Scope box and in the opened dialog select what elements you wish to see on your matrix. Click OK .

To change resource assignment to an Activity for BPMN Resources Usage Matrix, do one of the following

- Double-click the cell to create/remove a relationship between Activity and resource.
- Right-click the cell and from the shortcut menu select Resource .

To save a BPMN Matrices as *.csv

- On the BPMN Matrix toolbar, click the Export button to save your matrix as a Comma Separated Values ( .csv) file. The file can be opened with MS Excel.

**Related diagrams**

- BPMN Resources Usage Matrices
- BPMN Data Usage Matrices

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Creating diagrams' space='']

**Related external resource**

- Dependency Matrix

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>To change a row or column scope, do one of the following</p><hr /><ul><li data-uuid="03b2ae16-f393-467e-be6b-e7b425b40378">In the Model Browser, select one or more elements you wish to see on your matrix and drag them to the <strong>Row Scope/Column Scope</strong> box in the <strong>Criteria</strong> area.</li><li data-uuid="47f7612d-2c6f-4a75-8182-b9d098dd0723">Click the ... button next to the <strong>Row Scope/Column Scope</strong> box and in the opened dialog select what elements you wish to see on your matrix. Click <strong>OK</strong>.</li></ul><p><br /></p><p>To change resource assignment to an Activity for BPMN Resources Usage Matrix, do one of the following</p><hr /><ul><li data-uuid="5e1e499d-a960-4e06-9a96-0741ef32ad68">Double-click the cell to create/remove a relationship between Activity and resource.</li><li data-uuid="380a85fd-92c0-485b-8904-53614fbb46ca">Right-click the cell and from the shortcut menu select <strong>Resource</strong>.</li></ul><p><br /></p><p>To save a BPMN Matrices as *.csv</p><hr /><ul><li data-uuid="17dd3bb2-7328-4382-8627-0685a2324c54">On the BPMN Matrix toolbar, click the <strong>Export</strong> button to save your matrix as a Comma Separated Values ( .csv) file. The file can be opened with MS Excel.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related diagrams</strong></p><ul><li data-uuid="971ad8f1-1b01-4b09-821f-ff1413314708"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Resources+Usage+Matrices">BPMN Resources Usage Matrices</a></li><li data-uuid="997a27d2-085c-472a-98a8-20efb27b8dc9"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Data+Usage+Matrices">BPMN Data Usage Matrices</a></li></ul><p><strong>Related procedures</strong></p><ul><li data-uuid="81094d90-6313-4a6b-9ad8-1cbee47d0136"><ac:link><ri:page ri:content-title="(2026x) Creating diagrams" /><ac:plain-text-link-body><![CDATA[Creating a Diagram]]></ac:plain-text-link-body></ac:link></li></ul><p><strong>Related external resource</strong></p><ul><li data-uuid="3098ab01-d75e-4f1b-acac-2d30dec6e6a4"><a href="https://docs.nomagic.com/display/MT/(2026x) Dependency+Matrix">Dependency Matrix</a></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272729675 space=MT version=2 -->
## PAGE 03489: (2026x) Modifying BPMN Table

- page_id: `272729675`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272729675/2026x+Modifying+BPMN+Table
- version_number: 2
- version_date: `2025-11-25T14:47:24.435+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Using Cameo Business Modeler Plugin > (2026x) Using BPMN Tables and Matrices
- labels: ['msosa']

### NORMALIZED CONTENT

To create a new element in a BPMN table

- Click the Add New button on the Table Edit toolbar.

To add an existing element to a BPMN table, do one of the following

- In the Containment tree, select one or more Resources and drag them to the table. Hold down Shift to select multiple elements that are grouped together.Hold down Ctrl to select multiple elements that are not grouped together.
- Click the Add Existing button on the Table Edit toolbar. The select element dialog opens, select element you need to add to the table and click OK .

Multiple Selection

To remove an element from a BPMN table

- Select the element in the table and click the Delete From Table button on the Table Edit toolbar.

To delete an element from both a BPMN table and the model

- Select the element in the table and click the Delete button on the Table Edit toolbar.

To display columns of the table

1. On the Table Edit toolbar, click Show Columns .
2. From the menu, select properties to be shown in the table.

To edit element property value in a cell

The property can be edited if it is not locked.

1. Click a cell.
2. Do one of the following:
  - Edit the value directly in the selected cell.
  - Click the ... button. The property value editor dialog opens.

To export a BPMN table to the *.html, *.csv, or *.xlsx format

1. On the BPMN table toolbar, click Export . The Choose file dialog opens.
2. Do one of the following:
  - Browse for a location to save a table in.
  - Type the exported table name.
  - Select the exported table format.
3. Click Save .

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Creating diagrams' space='']

**Related external resource**

- Generic table

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>To create a new element in a BPMN table</p><hr /><ul><li data-uuid="2f715df1-5f31-46e7-bf82-5afb8d0bb862">Click the <strong>Add New</strong> button on the Table Edit toolbar.</li></ul><p><br /></p><p>To add an existing element to a BPMN table, do one of the following</p><hr /><ul><li data-uuid="f8e06236-368e-458e-b758-1a2d9fb18f2e"><p class="auto-cursor-target">In the Containment tree, select one or more Resources and drag them to the table.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="9aaab316-cff6-4b41-8d7f-4d2cdf7bbdc1"><ac:rich-text-body><ul><li>Hold down Shift to select multiple elements that are grouped together.</li><li>Hold down Ctrl to select multiple elements that are not grouped together.</li></ul></ac:rich-text-body></ac:structured-macro></li><li data-uuid="7d43b206-fb69-4264-b79e-e1ff9fec6217">Click the <strong>Add Existing</strong> button on the Table Edit toolbar. The select element dialog opens, select element you need to add to the table and click <strong>OK</strong>.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5220443a-7e52-48be-8c07-f9f92b61300d"><ac:rich-text-body>To select more than one element, click the <strong>Multiple Selection</strong> button.</ac:rich-text-body></ac:structured-macro><p><br /></p><p>To remove an element from a BPMN table</p><hr /><ul><li data-uuid="a8605759-bf4f-4599-a0e3-1566ca7d1a1f">Select the element in the table and click the <strong>Delete From Table</strong> button on the Table Edit toolbar.</li></ul><p><br /></p><p>To delete an element from both a BPMN table and the model</p><hr /><ul><li data-uuid="c6e92206-5e5b-48b0-a771-8f6a0ab5ecf7">Select the element in the table and click the <strong>Delete</strong> button on the Table Edit toolbar.</li></ul><p><br /></p><p>To display columns of the table</p><hr /><ol><li data-uuid="5882b0b7-5d0c-4775-bc60-c39c965a4632">On the Table Edit toolbar, click <strong>Show Columns</strong>.</li><li data-uuid="9b42ca8c-0853-4c91-a46c-1fe9a86a3957">From the menu, select properties to be shown in the table.</li></ol><p><br /></p><p>To edit element property value in a cell</p><hr /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="12fb2e56-77b8-40e7-b5f4-2b012e9fe6c0"><ac:rich-text-body>The property can be edited if it is not locked.</ac:rich-text-body></ac:structured-macro><ol><li data-uuid="32854be3-02d9-4e49-851b-d10495470815">Click a cell.</li><li data-uuid="84ce43fa-121a-489c-a2d1-d50febd613c8">Do one of the following:<ul><li>Edit the value directly in the selected cell.</li><li>Click the <strong>...</strong> button. The property value editor dialog opens.</li></ul></li></ol><p><br /></p><p>To export a BPMN table to the *.html, *.csv, or *.xlsx format</p><hr /><ol><li data-uuid="ee3915ea-21dc-45ba-8228-57fcf041ca39">On the BPMN table toolbar, click <strong>Export</strong>. The <strong>Choose file</strong> dialog opens.</li><li data-uuid="27625245-88f1-43e9-b26f-d104b7a784dc">Do one of the following:<ul><li>Browse for a location to save a table in.</li><li>Type the exported table name.</li><li>Select the exported table format.</li></ul></li><li data-uuid="a636f5e5-781d-409f-ba1a-ca56ba80753a">Click <strong>Save</strong>.</li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related procedures</strong></p><ul><li data-uuid="256f4aef-05a2-4ac7-86a7-01dbc497bf93"><ac:link><ri:page ri:content-title="(2026x) Creating diagrams" /><ac:plain-text-link-body><![CDATA[Creating a Diagram]]></ac:plain-text-link-body></ac:link></li></ul><p><strong>Related external resource</strong></p><ul><li data-uuid="006accbc-d9f4-4569-b95a-5d30c3ec52c3"><a href="https://docs.nomagic.com/display/MT/(2026x) Generic+table">Generic table</a></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272736161 space=MT version=1 -->
## PAGE 03490: (2026x) Modifying criteria through the legend

- page_id: `272736161`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272736161/2026x+Modifying+criteria+through+the+legend
- version_number: 1
- version_date: `2025-11-25T13:46:48.250+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) Procedures > (2026x) Managing traceability and impact analysis > (2026x) Traceability relation maps
- labels: ['criteria-color', 'select-criteria', 'modify-criteria', 'msosa']

### NORMALIZED CONTENT

You can change the style of the criteria relationships and select other criteria through the map legend.

To change the criteria style

1. Double-click the Legend. The Relation Criteria dialog opens.
2. In the Relation Criterion area, select the criteria for which you want to change the style.
3. Select the Style cell and click [ATTACHMENT filename='unnamed_to_change_criteria_style.png'] .
4. In the Style dialog, choose the line color and style.
5. Click OK , when you are done.

To select other criteria

1. Double-click the Legend.
2. In the Relation Criteria dialog choose the Simple Navigation property group.
3. Click to clear the Show Relations Criteria Available Only for Context check box. The list of available criteria is displayed.
4. Select the preferred criteria.
5. Click OK , when you are done.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can <span class="confluence-link">change the style of the criteria relationships</span> and <span class="confluence-link">select other criteria</span> through the map legend.</p><p><br /></p><p>To change the criteria style</p><hr /><ol><li>Double-click the Legend. The <strong>Relation Criteria</strong> dialog opens.</li><li>In the Relation Criterion area, select the criteria for which you want to change the style.</li><li>Select the Style cell and click <ac:image><ri:attachment ri:filename="unnamed_to_change_criteria_style.png"><ri:page ri:content-title="(2026x) Modifying criteria through the legend" /></ri:attachment></ac:image>.</li><li>In the <strong>Style</strong> dialog, choose the line color and style.</li><li>Click <strong>OK</strong>, when you are done.</li></ol><p><br /></p><p>To select other criteria</p><hr /><ol><li>Double-click the Legend.</li><li>In the <strong>Relation Criteria</strong> dialog choose the <strong>Simple Navigation</strong> property group.</li><li>Click to clear the <strong>Show Relations Criteria Available Only for Context</strong> check box. The list of available criteria is displayed.</li><li>Select the preferred criteria.</li><li>Click <strong>OK</strong>, when you are done.</li></ol><p><br /></p>
````

<!--NOMAGIC_PAGE id=272739381 space=MT version=1 -->
## PAGE 03491: (2026x) Modifying CV-5 table

- page_id: `272739381`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272739381/2026x+Modifying+CV-5+table
- version_number: 1
- version_date: `2025-11-25T13:51:19.872+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) DoDAF 2.0 > (2026x) Capability viewpoint > (2026x) CV-5 Capability to Organizational Development Mapping
- labels: ['remove-resources-from-cv-5', 'remove-capabilities-from-cv-5', 'modify-cv-5', 'add-capabilities-in-cv-5', 'add-resources-in-cv-5', 'msosa']

### NORMALIZED CONTENT

To add/ remove Capabilities in/from a CV-5 table

1. In the table toolbar, click the Add/ Remove Columns button.
2. In the Select Capability dialog, choose Capabilities to add or remove them from a table.
3. Click **OK** when you are done. Capabilities are removed only from the table. They are not removed from the model.AnExhibitsrelationship between the context element and a removed Capability is removed from the model.AnExhibitsrelationship between the context element and an added Capability is added in the model.

To add/ remove Actual Resources in/from a CV-5 table

1. Click the cell you want to edit.
2. Do one of the following:
  - To add an Actual Resource, select an Actual Resource and click the + button . The [CONFLUENCE_PAGE title='(2026x) Actual Resources Deployment Wizard' space=''] opens .
  - To remove an Actual Resource, select an Actual Resource and click the - button. [ATTACHMENT filename='Dr_table_remove_resources.png']

For more information about table management, see [CONFLUENCE_PAGE title='(2026x) Managing tables' space=''].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To add/ remove Capabilities in/from a CV-5 table</p><hr /><ol><li>In the table toolbar, click the <strong>Add/ Remove Columns</strong> button.</li><li>In the <strong>Select Capability</strong> dialog, choose Capabilities to add or remove them from a table.</li><li><p>Click <strong>OK</strong> when you are done.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2d011e40-d6f0-489d-a540-5965a4e1da96"><ac:rich-text-body><ul><li><ac:inline-comment-marker ac:ref="17718719-b135-4d27-a550-a22f56c2a41a">Capabilities are removed only from the table. They are not removed from the model.</ac:inline-comment-marker></li><li><ac:inline-comment-marker ac:ref="17718719-b135-4d27-a550-a22f56c2a41a">An </ac:inline-comment-marker><span style="color: rgb(51,51,51);"><ac:inline-comment-marker ac:ref="17718719-b135-4d27-a550-a22f56c2a41a">E</ac:inline-comment-marker>xhibits </span>relationship between the context element and a removed Capability is removed from the model.</li><li><ac:inline-comment-marker ac:ref="cc2bb72c-2c28-4ee3-9dc0-7cca6c2c55cf">An</ac:inline-comment-marker><span style="color: rgb(51,51,51);"><ac:inline-comment-marker ac:ref="cc2bb72c-2c28-4ee3-9dc0-7cca6c2c55cf"> Exhibits </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="cc2bb72c-2c28-4ee3-9dc0-7cca6c2c55cf">relationship between the context element and an added Capability is added in the model.</ac:inline-comment-marker></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p>To add/ remove Actual Resources in/from a CV-5 table</p><hr /><ol><li>Click the cell you want to edit.</li><li>Do one of the following:<br /><ul><li>To add an Actual Resource, select an Actual Resource and click the <strong>+</strong> button . The <strong><ac:link><ri:page ri:content-title="(2026x) Actual Resources Deployment Wizard" /></ac:link></strong> <ac:inline-comment-marker ac:ref="e117bf66-55db-47b5-b39c-27043d43ae66">opens</ac:inline-comment-marker>.</li><li>To remove an Actual Resource, select an Actual Resource and click the<strong> -</strong> button.<br /><ac:image><ri:attachment ri:filename="Dr_table_remove_resources.png"><ri:page ri:content-title="(2026x) Modifying CV-5 table" /></ri:attachment></ac:image></li></ul></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="e9caf57d-acd0-4a93-a52f-8fe9ec6678ff"><ac:rich-text-body><p>For more information about table management, see <ac:link><ri:page ri:content-title="(2026x) Managing tables" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p> </p>
````

<!--NOMAGIC_PAGE id=272731545 space=MT version=1 -->
## PAGE 03492: (2026x) Modifying NCV-5 table

- page_id: `272731545`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731545/2026x+Modifying+NCV-5+table
- version_number: 1
- version_date: `2025-11-25T13:39:12.602+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Capability Viewpoint > (2026x) NCV-5 Capability to Organisational Deployment Mapping
- labels: ['msosa']

### NORMALIZED CONTENT

Please refer to Section [CONFLUENCE_PAGE title='(2026x) Managing tables' space=''], if you are looking for the following table handling features:

- Delete the selected row.
- Delete the selected row from the table.
- Move the selected row up.
- Move the selected row down.
- Export a table to a plain text file format (.cvs) or a Hypertext Markup Language format (.html).
- Generate a report.

To add/ remove columns to a NCV-5 table

1. In the table toolbar, click the Add/ Remove Columns button. The element Selection dialog will open.
2. Select capabilities to add or remove from a table. For the detailed information about the element Selection dialog see Section [CONFLUENCE_PAGE title='(2026x) Selecting elements' space=''] .
3. Click OK when you are finished.

- Capabilities will be removed only from the table. They will not be removed from the model.
- An Exhibits relationship between the context element and a removed Capability will be removed from the model.
- An Exhibits relationship between the context element and an added Capability will be added in the model.

To add/ remove resources to a NCV-5 table

1. Click the cell you want to edit.
2. The + and - buttons will appear at the right of the cell as it is shown in the following figure.
3. Do one of the following:
  - Click the + button to add a resource. The Deployment Milestones creation wizard will open.
  - Select a resource you want to remove and click the - button.

The Resource will be removed from the table, but not from the model.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Please refer to Section <ac:link><ri:page ri:content-title="(2026x) Managing tables" /></ac:link>, if you are looking for the following table handling features:</p><ul><li>Delete the selected row.</li><li>Delete the selected row from the table.</li><li>Move the selected row up.</li><li>Move the selected row down.</li><li>Export a table to a plain text file format (.cvs) or a Hypertext Markup Language format (.html).</li><li>Generate a report.</li></ul><p><br /></p><p>To add/ remove columns to a NCV-5 table</p><hr /><ol><li>In the table toolbar, click the <strong>Add/ Remove Columns</strong> button. The element Selection dialog will open.</li><li>Select capabilities to add or remove from a table. For the detailed information about the element Selection dialog see Section <ac:link><ri:page ri:content-title="(2026x) Selecting elements" /></ac:link>.</li><li class="auto-cursor-target">Click <strong>OK</strong> when you are finished.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e7a45f6d-fd36-4c0e-9c3a-de30e4fc98b1"><ac:rich-text-body><ul><li>Capabilities will be removed only from the table. They will not be removed from the model.</li><li>An Exhibits relationship between the context element and a removed Capability will be removed from the model.</li><li>An Exhibits relationship between the context element and an added Capability will be added in the model.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p>To add/ remove resources to a NCV-5 table</p><hr /><ol><li>Click the cell you want to edit.</li><li>The <strong>+</strong> and<strong> -</strong> buttons will appear at the right of the cell as it is shown in the following figure.</li><li>Do one of the following:<ul><li>Click the <strong>+</strong> button to add a resource. The <strong>Deployment Milestones</strong> creation wizard will open.</li><li>Select a resource you want to remove and click the <strong>-</strong> button.</li></ul></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e6232554-f254-485e-aeb7-3abc634bfd8e"><ac:rich-text-body><p>The Resource will be removed from the table, but not from the model.</p></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=272736383 space=MT version=1 -->
## PAGE 03493: (2026x) Modifying relationships in Dependency Matrix

- page_id: `272736383`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272736383/2026x+Modifying+relationships+in+Dependency+Matrix
- version_number: 1
- version_date: `2025-11-25T13:47:12.645+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Diagrams > (2026x) Analysis diagrams > (2026x) Dependency Matrix > (2026x) Using Dependency Matrix
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

You can edit relationships and element properties directly in matrices. Clicking the selected cell allows for

- Creating or deleting relationships between elements.
- Defining or removing element properties or tags.

This feature not only facilitates management of ordinary relationships between elements, but also allows for a faster creation of traceability links between elements, for example, between requirements and the architecture or requirements and test cases. Such an improvement saves huge amounts of time in comparison to linking elements in diagrams. It significantly increases applicability and usability of matrices.

To create a new relationship between model elements in the dependency matrix, do one of the following

Commands on the shortcut menu of the cell, for creating a new relationship, depend on criteria specified in the **Criteria** area of the matrix:

- Possible relationship types correspond to the types specified as dependency criteria (see solid-line boxes in the following figure).
- Possible directions correspond to the directions specified in the Direction drop-down list (see dashed-line boxes in the following figure).

- Double-click the cell. If only one relationship type and direction is available, the relationship is created instantly. If several relationship types or directions are available, the shortcut menu opens. If you see the warning stating that the dependency criterion cannot be applied, it means that:row/column elements cannot be modified.relations between the row/column element types cannot be created according to the:constraints from the UML Meta Model (modeling tool main menu > **Help**).[CONFLUENCE_PAGE title='Creating Custom Rules for Relationships' space=''].[IMAGE alt='' src='']

- Right-click the cell. In the shortcut menu, under Create New (Row To Column) or Create New (Column To Row) , select a relationship type you need to create. [ATTACHMENT filename='create_relationship_in_dependency_matrix.png']

If you have specified to display in the matrix, relationships with both directions, the shortcut menu of the cell will look like the one in the following figure.

[IMAGE alt='' src='']

Thus make sure you have selected a relationship type with relevant direction.

To create multiple relationships between model elements simultaneously in the dependency matrix

1. Press and hold Ctrl on your keyboard to be able to select multiple row and column elements.
2. Do one of the following:
  - Double-click the cell while holding Ctrl. If only one relationship type and direction is available, the relationship is created instantly. If several relationship types or directions are available, the shortcut menu opens.
  - Right-click the cell. The shortcut menu opens.
3. From the shortcut menu, select the relationship type to create.

[IMAGE alt='' src='']

To remove a relationship between model elements from the dependency matrix

1. Do one of the following:
  - Double-click the cell. If only one relationship type and direction is available, the relationship is removed instantly. If several relationship types or directions are available, the shortcut menu opens.
  - Right-click the cell. The shortcut menu opens.
2. From the shortcut menu, under **Delete**, select the relationship you need to remove. The relationship is removed both from the matrix and the model.

[IMAGE alt='' src='']

To remove all relationships of a cell

1. Double-click or right-click the cell. The shortcut menu opens.
2. From the shortcut menu, under Delete , select Delete All . The relationships are removed both from the matrix and the model.

To remove relationship(s) of multiple cells

1. Press Ctrl and select multiple row and column elements.
2. Double-click or right-click the last active cell. The shortcut menu opens.
3. In the shortcut menu, under Delete , do one of the following:

- Select the specific relationship type to remove.
- Click Delete All to remove all relationships at once. [ATTACHMENT filename='dependency_matrix_shortcut_menu.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can edit relationships and element properties directly in matrices. Clicking the selected cell allows for</p><ul><li>Creating or deleting relationships between elements.</li><li>Defining or removing element properties or tags.</li></ul><p>This feature not only facilitates management of ordinary relationships between elements, but also allows for a faster creation of traceability links between elements, for example, between requirements and the architecture or requirements and test cases. Such an improvement saves huge amounts of time in comparison to linking elements in diagrams. It significantly increases applicability and usability of matrices.</p><p><br /></p><p>To create a new relationship between model elements in the dependency matrix, do one of the following</p><hr /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="390f7d05-1836-4981-b1cd-dbaae68f6665"><ac:rich-text-body><p>Commands on the shortcut menu of the cell, for creating a new relationship, depend on criteria specified in the <strong>Criteria</strong> area of the matrix:</p><ul><li>Possible relationship types correspond to the types specified as dependency criteria (see solid-line boxes in the following figure). </li><li>Possible directions correspond to the directions specified in the <strong>Direction</strong> drop-down list (see dashed-line boxes in the following figure).</li></ul></ac:rich-text-body></ac:structured-macro><ul><li class="auto-cursor-target"><p class="auto-cursor-target">Double-click the cell. If only one relationship type and direction is available, the relationship is created instantly. If several relationship types or directions are available, the shortcut menu opens.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="7a758098-3eb3-49a8-833f-451503e6f086"><ac:rich-text-body><p>If you see the warning stating that the dependency criterion cannot be applied, it means that:</p><ul><li>row/column elements cannot be modified.</li><li>relations between the row/column element types cannot be created according to the:<ul><li><ac:inline-comment-marker ac:ref="2044fdeb-b972-4f74-ad48-fec16df831bd">constraints from the UML Meta Model (modeling tool main menu &gt; <strong>Help</strong>).</ac:inline-comment-marker></li><li><ac:link><ri:page ri:content-title="Creating Custom Rules for Relationships" /><ac:plain-text-link-body><![CDATA[DSL relationship rules]]></ac:plain-text-link-body></ac:link>.</li></ul></li></ul><p style="margin-left: 30.0px;"><ac:image><ri:attachment ri:filename="dependency_criteria_cannot_be_created.png"><ri:page ri:content-title="(2026x) Modifying relationships in Dependency Matrix" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><ul><li>Right-click the cell. In the shortcut menu, under <strong>Create New (Row To Column)</strong> or <strong>Create New (Column To Row)</strong>, select a relationship type you need to create.<br /><ac:image><ri:attachment ri:filename="create_relationship_in_dependency_matrix.png"><ri:page ri:content-title="(2026x) Modifying relationships in Dependency Matrix" /></ri:attachment></ac:image></li></ul><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7027181f-903d-405f-8283-1d9e02602c6f"><ac:rich-text-body><p>If you have specified to display in the matrix, relationships with both directions, the shortcut menu of the cell will look like the one in the following figure.</p><p><ac:image><ri:attachment ri:filename="Dep_matrix_new_rel_both_dirs.png"><ri:page ri:content-title="(2026x) Modifying relationships in Dependency Matrix" /></ri:attachment></ac:image></p><p>Thus make sure you have selected a relationship type with relevant direction.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To <ac:inline-comment-marker ac:ref="cfc5f798-8f51-469e-909b-c5e0afe786b6">create</ac:inline-comment-marker> multiple relationships between model elements <ac:inline-comment-marker ac:ref="f3929fd9-0264-4890-abdf-d04cf56358f0">simultaneously</ac:inline-comment-marker> in the dependency matrix</p><hr /><ol><li>Press and hold <ac:inline-comment-marker ac:ref="84db0397-a9d9-4ba9-b738-5b7b8097ef7c">Ctrl</ac:inline-comment-marker> on your keyboard to be able to select multiple row and column elements.</li><li>Do one of the following:<ul><li>Double-click the cell while holding Ctrl. If only one relationship type and direction is available, the relationship is created instantly. If several relationship types or directions are available, the shortcut menu opens.</li><li>Right-click the cell. The shortcut menu opens.</li></ul></li><li>From the shortcut menu, select the relationship type to create. </li></ol><p style="margin-left: 60.0px;"><ac:image><ri:attachment ri:filename="creating_multiple_relationships_in_dependency_matrix.png"><ri:page ri:content-title="(2026x) Modifying relationships in Dependency Matrix" /></ri:attachment></ac:image></p><p style="margin-left: 60.0px;"><br /></p><p>To remove a relationship between model elements from the dependency matrix</p><hr /><ol><li>Do one of the following:<br /><ul><li>Double-click the cell. If only one relationship type and direction is available, the relationship is removed instantly. If several relationship types or directions are available, the shortcut menu opens. </li><li>Right-click the cell. The shortcut menu opens.</li></ul></li><li><p>From the shortcut menu, under <strong>Delete</strong>, select the relationship you need to remove. The relationship is removed both from the matrix and the model.</p></li></ol><p style="margin-left: 60.0px;"><ac:image><ri:attachment ri:filename="delete_relationship_in_dependency_matrix.png"><ri:page ri:content-title="(2026x) Modifying relationships in Dependency Matrix" /></ri:attachment></ac:image> </p><p>To remove all relationships of a cell</p><hr /><ol><li>Double-click or right-click the cell. The shortcut menu opens.</li><li>From the shortcut menu, under <strong>Delete</strong>, select <strong>Delete All</strong>. The relationships are removed both from the matrix and the model.<br /><br /></li></ol><p>To remove relationship(s) of multiple cells</p><hr /><ol><li>Press Ctrl and select multiple row and column elements.</li><li>Double-click or right-click the last active cell. The shortcut menu opens.</li><li>In the shortcut menu, under <strong>Delete</strong>, do one of the following:</li></ol><ul><li>Select the specific relationship type to remove.</li><li>Click <strong>Delete All </strong>to remove all relationships at once.<br /><br /><ac:image><ri:attachment ri:filename="dependency_matrix_shortcut_menu.png"><ri:page ri:content-title="(2026x) Modifying relationships in Dependency Matrix" /></ri:attachment></ac:image></li></ul>
````

<!--NOMAGIC_PAGE id=272738074 space=MT version=2 -->
## PAGE 03494: (2026x) Modifying requirement text

- page_id: `272738074`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738074/2026x+Modifying+requirement+text
- version_number: 2
- version_date: `2025-11-25T14:41:30.404+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) SysML v1 modeling > (2026x) Requirements management
- labels: ['mcse', 'msosa']

### NORMALIZED CONTENT

The requirement always contains two properties: id and text. This section describes how to modify the text property of the requirement.

[IMAGE alt='' src='']

###### The*Stopping Distance* Requirement shape with filled Text property.

##### Editing the requirement text

You can edit the requirement text directly on shapes and in cells, or use the **Text** dialog.

To open the edit mode of the requirement text, do one of the following

- On the [CONFLUENCE_PAGE title='(2026x) Understanding the user interface' space=''] , select the Text box on the Requirement shape. Click the text box again. The edit mode opens on the shape.
- In the Requirements table, double-click the Text cell. The edit mode opens on the cell.
- In the Requirements table, double-click the Text cell, and select [ATTACHMENT filename='edit_button_in_specification_window.png'] . The Text dialog opens.
- [CONFLUENCE_PAGE title='(2026x) Specification window' space=''] of the Requirement, select the Text property, and click [ATTACHMENT filename='edit_button_in_specification_window.png'] . The Text dialog opens.

##### switchSwitching the requirement text to HTML or Plain text

You can change the requirement text to HTML or Plain text directly on the Requirement shape or in the **Text** dialog.

To switch the requirement text to HTML or Plain text directly on the Requirement shape

1. On the diagram pane, select the text box on the Requirement shape.
2. Click one of the following buttons appearing on the lower left corner of the shape:
  - HTML - converts the text to HTML text. [ATTACHMENT filename='switch_to_html_text.png']
  - Plain - converts the text to plain text. [ATTACHMENT filename='switch_to_plain_text.png']

To switch the requirement text to HTML or Plain text in the **Text** dialog

1. Open the Text dialog:
  - In the Requirements table, double-click the Text cell, and select [ATTACHMENT filename='edit_button_in_specification_window.png'] .
  - [CONFLUENCE_PAGE title='(2026x) Specification window' space=''] of the Requirement, select the Text property, and click [ATTACHMENT filename='edit_button_in_specification_window.png'] .
2. In the Text dialog tootbar, do one of the following:
  - Select the HTML check box to convert the text to HTML text. [ATTACHMENT filename='html_text_in_text_dialog.png']
  - Clear the HTML check box to convert the text to plain text. [ATTACHMENT filename='plain_text_in_text_dialog.png']
3. Click OK .

##### Modifying the requirement text

You can modify the Requirement text in the following ways:

- 
- 
- 
- 

###### richRich text formatting

If you , you can use the toolbar in the **Text** dialog to format it as rich text.

To open the rich text formatting toolbar

- On the [CONFLUENCE_PAGE title='(2026x) Understanding the user interface' space=''] , select the Text box on the Requirement shape. Click the text box again.
- In the Requirements table, double-click the Requirement Text cell, and select [ATTACHMENT filename='edit_button_in_specification_window.png'] .
- [CONFLUENCE_PAGE title='(2026x) Specification window' space=''] of the Requirement, select the Text property, and click [ATTACHMENT filename='edit_button_in_specification_window.png'] . If the Requirement text is in HTML format, the rich text formatting toolbar appears as shown in the following image. [ATTACHMENT filename='rich_text_formatting_toolbar.png']

#### INFO: HTML text editors

HTML text editors

Learn more about how to work with HTML texts:

- [CONFLUENCE_PAGE title='(2026x) Advanced HTML Editor dialog' space='']
- HTML editor

###### glossaryUsing Glossary terms

You can use the terms from the Glossary Table to ensure the same definitions of the concepts. [CONFLUENCE_PAGE title='(2026x) Glossary table' space='']>]]>

If you want to extract a Constraint from a Requirement, you must use the special condition terms when defining the Requirement text.

The full procedure for extracting a Constraint from a Requirement is provided in the section [CONFLUENCE_PAGE title='(2026x) Extracting Constraint from Requirement' space=''].

true[CONFLUENCE_PAGE title='(2026x) Extracting Constraint from Requirement' space='']

###### hyperlinkDefining hyperlinks

You can add a hyperlink on the requirement text. How to add hyperlinks in text read in the [CONFLUENCE_PAGE title='(2026x) Hyperlinks in texts' space=''] page.

###### imageInserting images into HTML text

true[CONFLUENCE_PAGE title='(2026x) Inserting images into HTML text' space='']

**Related pages**

- [CONFLUENCE_PAGE title='(2026x) Extracting Constraint from Requirement' space='']
- [CONFLUENCE_PAGE title='(2026x) Advanced HTML Editor dialog' space='']
- [CONFLUENCE_PAGE title='(2026x) HTML editor' space='']
- [CONFLUENCE_PAGE title='(2026x) Text Box' space='']
- [CONFLUENCE_PAGE title='(2026x) Basic tasks in tables' space='']
- [CONFLUENCE_PAGE title='(2026x) Defining hyperlinks' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The requirement always contains two properties: id and text. This section describes how to modify the text property of the requirement.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="text_property_requirement.png"><ri:page ri:content-title="(2026x) Modifying requirement text" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The<em> Stopping Distance</em> Requirement shape with filled Text property.</h6><h3>Editing the requirement text</h3><p>You can edit the requirement text directly on shapes and in cells, or use the <strong>Text</strong> dialog.</p><p>To open the edit mode of the requirement text, do one of the following</p><hr /><ul><li>On the <ac:link><ri:page ri:content-title="(2026x) Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram pane]]></ac:plain-text-link-body></ac:link>, select the Text box on the Requirement shape. Click the text box again. The edit mode opens on the shape.</li><li>In the Requirements table, double-click the Text cell. The edit mode opens on the cell.</li><li>In the Requirements table, double-click the Text cell, and select <ac:image ac:title="Edit " ac:thumbnail="true" ac:alt="Edit " ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:content-title="(2026x) Modifying requirement text" /></ri:attachment></ac:image>. The <strong>Text</strong> dialog opens.</li><li><ac:link><ri:page ri:content-title="(2026x) Specification window" /><ac:plain-text-link-body><![CDATA[Open Specification window]]></ac:plain-text-link-body></ac:link> of the Requirement, select the Text property, and click <ac:image ac:title="Edit " ac:thumbnail="true" ac:alt="Edit " ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:content-title="(2026x) Modifying requirement text" /></ri:attachment></ac:image>. The <strong>Text</strong> dialog opens.</li></ul><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="902903b8-4326-48d0-b34c-cb984bb43785"><ac:parameter ac:name="">switch</ac:parameter></ac:structured-macro>Switching the requirement text to HTML or Plain text</h3><p>You can change the requirement text to HTML or Plain text directly on the Requirement shape or in the <strong>Text</strong> dialog.</p><p><br /></p><p>To switch the requirement text to HTML or Plain text directly on the Requirement shape</p><hr /><ol><li>On the diagram pane, select the text box on the Requirement shape.</li><li>Click one of the following buttons appearing on the lower left corner of the shape:<ul><li><strong>HTML</strong> - converts the text to HTML text.<br /><ac:image><ri:attachment ri:filename="switch_to_html_text.png"><ri:page ri:content-title="(2026x) Modifying requirement text" /></ri:attachment></ac:image></li><li><strong>Plain</strong> - converts the text to plain text.<br /><ac:image ac:thumbnail="true" ac:height="139"><ri:attachment ri:filename="switch_to_plain_text.png"><ri:page ri:content-title="(2026x) Modifying requirement text" /></ri:attachment></ac:image></li></ul></li></ol><p><br /></p><p>To switch the requirement text to HTML or Plain text in the <strong>Text</strong> dialog</p><hr /><ol><li>Open the <strong>Text</strong> dialog:<br /><ul><li>In the Requirements table, double-click the Text cell, and select <ac:image ac:title="Edit " ac:thumbnail="true" ac:alt="Edit " ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:content-title="(2026x) Modifying requirement text" /></ri:attachment></ac:image>.</li><li><ac:link><ri:page ri:content-title="(2026x) Specification window" /><ac:plain-text-link-body><![CDATA[Open Specification window]]></ac:plain-text-link-body></ac:link> of the Requirement, select the Text property, and click <ac:image ac:title="Edit " ac:thumbnail="true" ac:alt="Edit " ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:content-title="(2026x) Modifying requirement text" /></ri:attachment></ac:image>.</li></ul></li><li>In the <strong>Text</strong> dialog tootbar, do one of the following:<br /><ul><li>Select the <strong>HTML</strong> check box to convert the text to HTML text.<br /><ac:image><ri:attachment ri:filename="html_text_in_text_dialog.png"><ri:page ri:content-title="(2026x) Modifying requirement text" /></ri:attachment></ac:image></li><li>Clear the <strong>HTML</strong> check box to convert the text to plain text.<br /><ac:image><ri:attachment ri:filename="plain_text_in_text_dialog.png"><ri:page ri:content-title="(2026x) Modifying requirement text" /></ri:attachment></ac:image></li></ul></li><li>Click <strong>OK</strong>.<br /><br /></li></ol><h3>Modifying the requirement text</h3><p>You can modify the Requirement text in the following ways:</p><ul><li><ac:link ac:anchor="rich"><ac:plain-text-link-body><![CDATA[Rich text formatting]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="glossary"><ac:plain-text-link-body><![CDATA[Using Glossary terms]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="hyperlink"><ac:plain-text-link-body><![CDATA[Defining Hyperlinks]]></ac:plain-text-link-body></ac:link></li><li><p><ac:link ac:anchor="image"><ac:plain-text-link-body><![CDATA[Inserting images into HTML text]]></ac:plain-text-link-body></ac:link></p></li></ul><h4><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="897b2415-539f-47a8-b859-1ed336917947"><ac:parameter ac:name="">rich</ac:parameter></ac:structured-macro>Rich text formatting</h4><p>If you <ac:link ac:anchor="switch"><ac:plain-text-link-body><![CDATA[switch the requirement text to HTML]]></ac:plain-text-link-body></ac:link>, you can use the toolbar in the <strong>Text</strong> dialog to format it as rich text.</p><p><br /></p><p>To open the rich text formatting toolbar</p><hr /><ul><li>On the <ac:link><ri:page ri:content-title="(2026x) Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram pane]]></ac:plain-text-link-body></ac:link>, select the Text box on the Requirement shape. Click the text box again.</li><li>In the Requirements table, double-click the Requirement Text cell, and select <ac:image ac:title="Edit " ac:thumbnail="true" ac:alt="Edit " ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:content-title="(2026x) Modifying requirement text" /></ri:attachment></ac:image>.</li><li><ac:link><ri:page ri:content-title="(2026x) Specification window" /><ac:plain-text-link-body><![CDATA[Open Specification window]]></ac:plain-text-link-body></ac:link> of the Requirement, select the Text property, and click <ac:image ac:title="Edit " ac:thumbnail="true" ac:alt="Edit " ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:content-title="(2026x) Modifying requirement text" /></ri:attachment></ac:image>.<br />If the Requirement text is in HTML format, the rich text formatting toolbar appears as shown in the following image.<br /><ac:image><ri:attachment ri:filename="rich_text_formatting_toolbar.png"><ri:page ri:content-title="(2026x) Modifying requirement text" /></ri:attachment></ac:image><br /><br /></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2558b809-3a73-4ca0-9837-780ceb765587"><ac:parameter ac:name="title">HTML text editors</ac:parameter><ac:rich-text-body><p>Learn more about how to work with HTML texts:</p><ul><li><ac:link><ri:page ri:content-title="(2026x) Advanced HTML Editor dialog" /></ac:link></li><li><a href="https://docs.nomagic.com/display/MT/(2026x) HTML+editor" rel="nofollow">HTML editor</a></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><h4><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="cd74e719-40a4-4aa9-afd4-0c8f83725f11"><ac:parameter ac:name="">glossary</ac:parameter></ac:structured-macro>Using Glossary terms</h4><p>You can use the terms from the Glossary Table to ensure the same definitions of the concepts. <ac:link><ri:page ri:content-title="(2026x) Glossary table" /><ac:plain-text-link-body><![CDATA[How to work with Glossary table >>]]></ac:plain-text-link-body></ac:link></p><p>If you want to extract a Constraint from a Requirement, you must use the special condition terms when defining the Requirement text.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d9d288ea-41be-4a29-ad93-a7ed28cfd26f"><ac:rich-text-body><p>The full procedure for extracting a Constraint from a Requirement is provided in the section <ac:link><ri:page ri:content-title="(2026x) Extracting Constraint from Requirement" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="2558f3f7-faed-4672-84f9-29b89e3d08a4"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:content-title="(2026x) Extracting Constraint from Requirement" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p><h4><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="76ef6479-4057-47f5-9992-fe0ca51e7185"><ac:parameter ac:name="">hyperlink</ac:parameter></ac:structured-macro>Defining hyperlinks</h4><p>You can add a hyperlink on the requirement text. How to add hyperlinks in text read in the <ac:link><ri:page ri:content-title="(2026x) Hyperlinks in texts" /><ac:plain-text-link-body><![CDATA[Hyperlinks in text]]></ac:plain-text-link-body></ac:link> page.</p><p><br /></p><p><br /></p><h4><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="c2489dd0-e0f4-460b-9766-0d87c0544b0c"><ac:parameter ac:name="">image</ac:parameter></ac:structured-macro>Inserting images into HTML text</h4><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="679142f3-12df-4fc9-ae1e-fb1d48048a2a"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:content-title="(2026x) Inserting images into HTML text" /></ac:link></ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Extracting Constraint from Requirement" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Advanced HTML Editor dialog" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) HTML editor" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Text Box" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Basic tasks in tables" /></ac:link></li><li><span class="confluence-link"><ac:link><ri:page ri:content-title="(2026x) Defining hyperlinks" /></ac:link></span></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272733880 space=MT version=1 -->
## PAGE 03495: (2026x) Modifying the content of a diagram overview shape

- page_id: `272733880`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733880/2026x+Modifying+the+content+of+a+diagram+overview+shape
- version_number: 1
- version_date: `2025-11-25T13:43:09.581+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Diagramming > (2026x) Overviewing other diagrams
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

569357971

569357974

569357972

Once the diagram overview shape is created, you can modify its content: add more element shapes or remove no more needed ones by using the **Compartment Edit** dialog.

To open the **Compartment Edit** dialog, do one of the following

- From the diagram overview shape shortcut menu, select Edit Compartments .
- Select the diagram overview shape, click the “...” Compartments button and from the menu, select **Edit Compartments**.

To modify the content of the diagram over view shape

1. In the Compartment Edit dialog, use the > , >> , < , and << buttons to move the items among the Hidden and Selected lists.
2. Click OK when you are finished.

569357970

**Related pages**

- [CONFLUENCE_PAGE title='(2026x) Creating a diagram overview shape' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="300fa4fb-9c0a-46c2-9b1c-1a02a0dd20d6"><ac:parameter ac:name="id">569357971</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fb24a557-72c4-4ec0-82a0-a187c73728d0"><ac:parameter ac:name="id">569357974</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="83c6f44a-6ad3-4973-9af1-a8a53b1b321e"><ac:parameter ac:name="id">569357972</ac:parameter><ac:rich-text-body><p>Once the diagram overview shape is created, you can modify its content: add more element shapes or remove no more needed ones by using the <strong>Compartment Edit</strong> dialog.</p><p> </p><p>To open the <strong>Compartment Edit</strong> dialog, do one of the following</p><hr /><ul><li>From the diagram overview shape shortcut menu, select <strong>Edit Compartments</strong>.</li><li><p>Select the diagram overview shape, click the “...” Compartments button and from the menu, select <strong>Edit Compartments</strong>.</p></li></ul><p> </p><p>To modify the content of the diagram over view shape</p><hr /><ol><li>In the <strong>Compartment Edit</strong> dialog, use the <strong>&gt;</strong>, <strong>&gt;&gt;</strong>, <strong>&lt;</strong>, and <strong>&lt;&lt;</strong> buttons to move the items among the <strong>Hidden</strong> and <strong>Selected</strong> lists.</li><li>Click <strong>OK</strong> when you are finished.</li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ace33605-f236-4beb-84c9-a2bd9eab42a0"><ac:parameter ac:name="id">569357970</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Creating a diagram overview shape" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732063 space=MT version=1 -->
## PAGE 03496: (2026x) MOF support

- page_id: `272732063`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732063/2026x+MOF+support
- version_number: 1
- version_date: `2025-11-25T13:40:14.173+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Working with projects
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

305770370

305770372

305770371

The modeling tool allows export to/import from UML models from/to MOF (both CMOF and EMOF) XMI files. MOF 2.0 and 2.4 (MOF 2.4.1 to be more specific) are supported.

For more information about the MOF domain model, see **Meta Object Facility (MOF) Core Specification** for [MOF 2.0](http://www.omg.org/spec/MOF/2.0/PDF/) or [MOF 2.4.1](http://www.omg.org/spec/MOF/2.4.1/PDF/).

305770369

**Related pages**

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="b0ba1323-36fb-421d-aca5-0d102eafc969"><ac:parameter ac:name="id">305770370</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="bc5f7076-9a6c-4139-a6ee-3eb00b9bd6f3"><ac:parameter ac:name="id">305770372</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f82394bc-6744-40a8-9a9b-39a782811a4f"><ac:parameter ac:name="id">305770371</ac:parameter><ac:rich-text-body><p>The modeling tool allows export to/import from UML models from/to MOF (both CMOF and EMOF) XMI files. MOF 2.0 and 2.4 (MOF 2.4.1 to be more specific) are supported.</p><p>For more information about the MOF domain model, see <strong>Meta Object Facility (MOF) Core Specification</strong> for <a href="http://www.omg.org/spec/MOF/2.0/PDF/">MOF 2.0</a> or <a href="http://www.omg.org/spec/MOF/2.4.1/PDF/">MOF 2.4.1</a>.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="db594629-84dd-4839-b93f-2842c8b110c2"><ac:parameter ac:name="id">305770369</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><strong><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="244a960e-0b53-4202-b5ee-b68a22135c29" /><br /></strong></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272737619 space=MT version=1 -->
## PAGE 03497: (2026x) Monitor template folder and reset to defaults options

- page_id: `272737619`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272737619/2026x+Monitor+template+folder+and+reset+to+defaults+options
- version_number: 1
- version_date: `2025-11-25T13:48:51.292+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Report Wizard > (2026x) Configuring Report Wizard > (2026x) Report Wizard Environment options
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

You can select the Report Wizard options for monitoring template folder, and resetting to defaults options in the **Environment Options** dialog.

[IMAGE alt='' src='']

###### The Monitor template folder and Reset to Defaults options of Report Wizard in the Environment Options dialog.

###### Monitor template folder

You can either enable or disable the MRZIP template file automatic deployment option in the Report Wizard environment options by selecting or clearing the **Monitor template folder** check box.

###### Reset to defaults

The modeling tool allows you to configure the report engine settings in three levels: Environment Options, global *config.xml*, and template *config.xml*. The template*config.xml* configuration settings will override the **Environment Options** configuration settings, which will override the global *config.xml* configuration settings.

If you have made changes to the settings in the Report Wizard's **Environment Options** dialog, but would then like to cancel them, you can click [IMAGE alt='' src=''] to reset data to the default settings.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can select the Report Wizard options for monitoring template folder, and resetting to defaults options in the <strong>Environment Options</strong> dialog.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="ReportWizard_options.png"><ri:page ri:content-title="(2026x) Monitor template folder and reset to defaults options" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The Monitor template folder and Reset to Defaults options of Report Wizard in the Environment Options dialog.</h6><h4>Monitor template folder</h4><p>You can either enable or disable the MRZIP template file automatic deployment option in the Report Wizard environment options by selecting or clearing the <strong>Monitor template folder</strong> check box.</p><h4>Reset to defaults</h4><p>The modeling tool allows you to configure the report engine settings in three levels: Environment Options, global <em>config.xml</em>, and template <em>config.xml</em>. The template<em> config.xml</em> configuration settings will override the <strong>Environment Options</strong> configuration settings, which will override the global <em>config.xml</em> configuration settings.</p><p>If you have made changes to the settings in the Report Wizard's <strong>Environment Options</strong> dialog, but would then like to cancel them, you can click <ac:image><ri:attachment ri:filename="Rese_to_Defaults_button.png"><ri:page ri:content-title="(2026x) Monitor template folder and reset to defaults options" /></ri:attachment></ac:image> to reset data to the default settings.</p>
````

<!--NOMAGIC_PAGE id=272739786 space=MT version=1 -->
## PAGE 03498: (2026x) Most common shortcut keys

- page_id: `272739786`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272739786/2026x+Most+common+shortcut+keys
- version_number: 1
- version_date: `2025-11-25T13:51:57.914+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) Getting started
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

The following table outlines the most commonly used shortcut keys:

| What do you want to do? | Shortcut keys |  |
| --- | --- | --- |
|  | Windows | OS X |
| Open the Find dialog | Ctrl+Shift+F | Cmd+Shift+F |
| Open the Quick Find dialog | Ctrl+Alt+F | Cmd+Alt+F |
| Open the Find and Replace dialog | Ctrl+R | Cmd+R |
| Remove both symbols from an active diagram and element from the model | Ctrl+D | Cmd+D |
| Remove only a symbol from an active diagram, but not the model element | Delete | Del |
| Select all shapes on an active diagram | Ctrl+A | Cmd+A |
| Select an element in the Containment treeSwitch from List to Tree view in the Select Element dialog | Alt+B | Alt+B |
| Zoom in/out Model Browser | Ctrl+Mouse scroll wheelCtrl+Numpad +/- | Cmd+Mouse scroll wheelCmd+Numpad +/- |
| Add more symbols to selection | Shift+Left mouse button | Shift+Left mouse button |
| Select elements of the same type | Alt+Left mouse button | Alt+Left mouse button |
| Open a list of possible elements to assign when typing on a symbol | Ctrl+Spacebar | Ctrl+Spacebar |
| Add a new line in the compartment of a shape, for example, create an attribute for a class | Shift+Enter | Shift+Enter |
| Open element's Specification window | Enter | Enter |
| Open element's Symbol Properties dialog | Alt+Enter | Alt+Enter |
| Open the Report Wizard | Ctrl+Shift+G | Cmd+Shift+G |
| See the list of recently opened diagrams | F12 | – |
| Cut a selected item | Ctrl+X | Cmd+X |
| Copy a shape or text | Ctrl+C | Cmd+C |
| Copy a shape | Drag the shape to the empty place on the diagram, while holding down Ctrl | – |
| Paste | Ctrl+V | Cmd+V |
| Paste with New Element | Ctrl+E | Cmd+E |
| Save | Ctrl+S | Cmd+S |
| Commit changes to the server | Ctrl+K | Cmd+K |
| Undo | Ctrl+Z | Cmd+Z |
| Redo | Ctrl+Y | Cmd+Y |
| Print | Ctrl+P | Cmd+P |
| Assign a shortcut key to print a report | Alt+ number 1 to 9 | Alt+ number 1 to 9 |
| Turn on the Full Screen mode | F11 | – |
| Open a recently closed diagram | Ctrl+Shift+T | – |
| Paste a symbol style | Ctrl+Shift+V | Cmd+Shift+V |
| Reverse path direction | Draw the path while holding down Alt | Draw the path while holding down Alt |
| Reorder elements/properties in a list, tree, and Specification window | Ctrl+UpCtrl+Down | Alt+UpAlt+Down |
| Select a previous or next result in a tree | Shift+F3F3 | Shift+F3F3 |

**Related pages**

- [CONFLUENCE_PAGE title='(2026x) Assigning shortcut keys' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target">The following table outlines the most commonly used shortcut keys:</p><table><colgroup class=""><col class="" /><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><td class="highlight-grey" data-highlight-colour="grey"><p style="text-align: center;"><strong>What do you want to do?</strong></p></td><td class="highlight-grey" colspan="2" data-highlight-colour="grey"><p style="text-align: center;"><strong>Shortcut keys</strong></p></td></tr><tr class=""><td class="highlight-grey" data-highlight-colour="grey"><p><br /></p></td><td class="highlight-grey" style="text-align: left;" data-highlight-colour="grey"><p><strong>Windows<br /></strong></p></td><td class="highlight-grey" style="text-align: left;" data-highlight-colour="grey"><p><strong>OS X<br /></strong></p></td></tr><tr class=""><td><p>Open the <strong>Find</strong> dialog</p></td><td><p>Ctrl+Shift+F</p></td><td><p>Cmd+Shift+F</p></td></tr><tr class=""><td><p>Open the <strong>Quick Find</strong> dialog</p></td><td><p>Ctrl+Alt+F</p></td><td><p>Cmd+Alt+F</p></td></tr><tr class=""><td><p>Open the <strong>Find and Replace</strong> dialog</p></td><td><p>Ctrl+R</p></td><td><p>Cmd+R</p></td></tr><tr class=""><td><p>Remove both symbols from an active <br />diagram and element from the model</p></td><td><p>Ctrl+D</p></td><td><p>Cmd+D</p></td></tr><tr class=""><td><p>Remove only a symbol from an active <br />diagram, but not the model element</p></td><td><p>Delete</p></td><td><p>Del</p></td></tr><tr class=""><td><p>Select all shapes on an active diagram</p></td><td><p>Ctrl+A</p></td><td><p>Cmd+A</p></td></tr><tr class=""><td><p>Select an element in the Containment tree</p><p>Switch from <strong>List</strong> to<strong> Tree</strong> view in the <strong>Select Element</strong> dialog</p></td><td><p>Alt+B</p></td><td><p>Alt+B</p></td></tr><tr class=""><td colspan="1">Zoom in/out Model Browser</td><td colspan="1"><p>Ctrl+Mouse scroll wheel</p><p>Ctrl+Numpad +/-</p></td><td colspan="1"><p>Cmd+Mouse scroll wheel</p><p>Cmd+Numpad +/-</p></td></tr><tr class=""><td><p>Add more symbols to selection</p></td><td><p>Shift+Left mouse button</p></td><td><p>Shift+Left mouse button</p></td></tr><tr class=""><td><p>Select elements of the same type</p></td><td><p>Alt+Left mouse button</p></td><td><p>Alt+Left mouse button</p></td></tr><tr class=""><td><p>Open a list of possible elements to <br />assign when typing on a symbol</p></td><td><p>Ctrl+Spacebar</p></td><td><p>Ctrl+Spacebar</p></td></tr><tr class=""><td><p>Add a new line in the compartment of <br />a shape, for example, create an attribute for a class</p></td><td><p>Shift+Enter</p></td><td><p>Shift+Enter</p></td></tr><tr class=""><td><p>Open element's Specification window</p></td><td><p>Enter</p></td><td><p>Enter</p></td></tr><tr class=""><td><p>Open element's <strong>Symbol</strong> <strong>Properties</strong> dialog</p></td><td><p>Alt+Enter</p></td><td><p>Alt+Enter</p></td></tr><tr class=""><td><p>Open the <strong>Report Wizard</strong></p></td><td><p>Ctrl+Shift+G</p></td><td><p>Cmd+Shift+G</p></td></tr><tr class=""><td><p>See the list of recently opened diagrams</p></td><td><p>F12</p></td><td><p>–</p></td></tr><tr class=""><td><p>Cut a selected item</p></td><td><p>Ctrl+X</p></td><td><p>Cmd+X</p></td></tr><tr class=""><td><p>Copy a shape or text</p></td><td><p>Ctrl+C</p></td><td><p>Cmd+C</p></td></tr><tr class=""><td><p>Copy a shape</p></td><td><p>Drag the shape to the empty place <br />on the diagram, while holding down Ctrl</p></td><td><p>–</p></td></tr><tr class=""><td><p>Paste</p></td><td><p>Ctrl+V</p></td><td><p>Cmd+V</p></td></tr><tr class=""><td><p>Paste with New Element</p></td><td><p>Ctrl+E</p></td><td><p>Cmd+E</p></td></tr><tr class=""><td><p>Save</p></td><td><p>Ctrl+S</p></td><td><p>Cmd+S</p></td></tr><tr class=""><td><p>Commit changes to the server</p></td><td><p>Ctrl+K</p></td><td><p>Cmd+K</p></td></tr><tr class=""><td><p>Undo</p></td><td><p>Ctrl+Z</p></td><td><p>Cmd+Z</p></td></tr><tr class=""><td><p>Redo</p></td><td><p>Ctrl+Y</p></td><td><p>Cmd+Y</p></td></tr><tr class=""><td><p>Print</p></td><td><p>Ctrl+P</p></td><td><p>Cmd+P</p></td></tr><tr class=""><td><p>Assign a shortcut key to print a report</p></td><td><p>Alt+ number 1 to 9</p></td><td><p>Alt+ number 1 to 9</p></td></tr><tr class=""><td colspan="1">Turn on the Full Screen mode</td><td colspan="1">F11</td><td colspan="1">–</td></tr><tr class=""><td colspan="1">Open a recently closed diagram</td><td colspan="1">Ctrl+Shift+T</td><td colspan="1">–</td></tr><tr class=""><td colspan="1">Paste a symbol style</td><td colspan="1">Ctrl+Shift+V</td><td colspan="1">Cmd+Shift+V</td></tr><tr class=""><td colspan="1">Reverse path direction</td><td colspan="1">Draw the path while holding down Alt</td><td colspan="1"><span>Draw the path while holding down Alt</span></td></tr><tr class=""><td colspan="1">Reorder elements/properties in a list, tree, and Specification window</td><td colspan="1"><p>Ctrl+Up</p><p>Ctrl+Down</p></td><td colspan="1"><p>Alt+Up</p><p>Alt+Down</p></td></tr><tr class=""><td colspan="1">Select a previous or next result in a tree</td><td colspan="1"><p>Shift+F3</p><p>F3</p></td><td colspan="1"><p>Shift+F3</p><p>F3</p></td></tr></tbody></table><p><br /></p><p><strong>Related pages</strong></p><ul><li data-uuid="156d346b-5947-4381-a334-d430c0a22658"><ac:link><ri:page ri:content-title="(2026x) Assigning shortcut keys" /></ac:link></li></ul>
````

<!--NOMAGIC_PAGE id=272735231 space=MT version=1 -->
## PAGE 03499: (2026x) MRZIP file automatic deployment

- page_id: `272735231`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272735231/2026x+MRZIP+file+automatic+deployment
- version_number: 1
- version_date: `2025-11-25T13:45:08.156+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Report Wizard
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

An MRZIP file is a report template package file. You can place an MRZIP file into your template folder *<user folder>/AppData/Local/.<modeling tool name>/<version>/data/reports*, and the modeling tool will automatically deploy the template into the **Report Wizard** dialog.

The following three figures show you how Report Wizard can automatically deploy an MRZIP file.

[IMAGE alt='' src='']

###### Copying the MRZIP file into a template folder.

[IMAGE alt='' src='']

###### Automatic deployment of the MRZIP file.

###### [IMAGE alt='' src=''] 
Report Template installed in the Report Wizard dialog.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An MRZIP file is a report template package file. You can place an MRZIP file into your template folder <em style="line-height: 1.42857;">&lt;user folder&gt;/AppData/Local/.&lt;modeling tool name&gt;/&lt;version&gt;/data/reports</em>, and the modeling tool will automatically deploy the template into the <strong>Report Wizard</strong> dialog.</p><p>The following three figures show you how Report Wizard can automatically deploy an MRZIP file.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Copying MRZIP File 190.png"><ri:page ri:content-title="(2026x) MRZIP file automatic deployment" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Copying the MRZIP file into a template folder.</h6><p style="margin-left: 30.0px;"><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Deploying MRZIP File 190.png"><ri:page ri:content-title="(2026x) MRZIP file automatic deployment" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Automatic deployment of the MRZIP file.</h6><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="select-report-template.png"><ri:page ri:content-title="(2026x) MRZIP file automatic deployment" /></ri:attachment></ac:image><br />Report Template installed in the Report Wizard dialog.</h6>
````

<!--NOMAGIC_PAGE id=272738141 space=MT version=2 -->
## PAGE 03500: (2026x) Multilevel with Owner Number

- page_id: `272738141`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738141/2026x+Multilevel+with+Owner+Number
- version_number: 2
- version_date: `2025-11-25T14:45:50.477+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Business Process Model and Notation Concepts > (2026x) Numbering Elements > (2026x) Numbering Schemas
- labels: ['msosa']

### NORMALIZED CONTENT

1486746984

1486746985

1486746985

**Description**

A Multilevel with Owner Number numbering schema provides multilevel element numbering. An Element owner (BPMN Process, BPMN Collaboration, or Choreography) number is displayed before the element number.

**Example**

[IMAGE alt='' src='']

###### Multilevel Numbering style with element owner number

A Multilevel with Owner Number numbering schema is the default schema for all BPMN diagram elements.

1486746983

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Using BPMN Element Numbers

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="0ec98f44-0b0d-4fa7-86ff-9891e7eb97f6"><ac:parameter ac:name="id">1486746984</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b6d909c8-148e-4742-9f71-e50645ffc989"><ac:parameter ac:name="id">1486746985</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3dd89910-ef7c-460f-9a32-50c0986f3c60"><ac:parameter ac:name="id">1486746985</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>A Multilevel with Owner Number numbering schema provides multilevel element numbering. An Element owner (BPMN Process, BPMN Collaboration, or Choreography) number is displayed before the element number.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="element_numbering_multilevel.png"><ri:page ri:content-title="(2026x) Multilevel with Owner Number" /></ri:attachment></ac:image></p><h6>Multilevel Numbering style with element owner number</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c26a9a48-25c2-49b1-b7f4-2eb2f75b5282"><ac:rich-text-body><p>A Multilevel with Owner Number numbering schema is the default schema for all BPMN diagram elements.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="33c0d413-6cc8-4aad-8250-e52220694a6a"><ac:parameter ac:name="id">1486746983</ac:parameter><ac:rich-text-body><p><strong>Related diagrams</strong></p><ul><li><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/MT/(2026x) Using+BPMN+Element+Numbers">Using BPMN Element Numbers</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272738138 space=MT version=2 -->
## PAGE 03501: (2026x) Multilevel without Owner Number

- page_id: `272738138`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738138/2026x+Multilevel+without+Owner+Number
- version_number: 2
- version_date: `2025-11-25T14:45:51.629+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Business Process Model and Notation Concepts > (2026x) Numbering Elements > (2026x) Numbering Schemas
- labels: ['msosa']

### NORMALIZED CONTENT

1486775001

1486775002

1486775002

**Description**

A Multilevel without Owner Number numbering schema provides multilevel element numbering. An Element owner (BPMN Process, BPMN Collaboration, or Choreography) number is not included in the element number.

**Example**

[IMAGE alt='' src='']

###### Multilevel Numbering style without element owner number

When a Multilevel without element number numbering schema is used, the numbers in a project are not unique. Elements with the same number can exist in multiple diagrams.

1486775000

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Using BPMN Element Numbers

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ffe74047-d10a-4443-9ab6-6671389d48c2"><ac:parameter ac:name="id">1486775001</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="57970f5d-1863-4eae-b434-8d9c220de394"><ac:parameter ac:name="id">1486775002</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="de259261-64d5-4857-adca-2cc4390e622c"><ac:parameter ac:name="id">1486775002</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>A Multilevel without Owner Number numbering schema provides multilevel element numbering. An Element owner (BPMN Process, BPMN Collaboration, or Choreography) number is not included in the element number.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="element_numbering_multilevel_II.png"><ri:page ri:content-title="(2026x) Multilevel without Owner Number" /></ri:attachment></ac:image></p><h6>Multilevel Numbering style without element owner number</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="47f86cd7-cfac-410d-a52b-3266d8d1fbfe"><ac:rich-text-body><p>When a Multilevel without element number numbering schema is used, the numbers in a project are not unique. Elements with the same number can exist in multiple diagrams.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8f78d165-9bc9-4e21-99fd-90e5b56780d6"><ac:parameter ac:name="id">1486775000</ac:parameter><ac:rich-text-body><p><strong>Related diagrams</strong></p><ul><li><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/MT/(2026x) Using+BPMN+Element+Numbers">Using BPMN Element Numbers</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272738416 space=MT version=2 -->
## PAGE 03502: (2026x) Multiple Boundary Event

- page_id: `272738416`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738416/2026x+Multiple+Boundary+Event
- version_number: 2
- version_date: `2025-11-25T14:45:08.571+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Business Process Model and Notation Concepts > (2026x) BPMN Process Diagram > (2026x) Boundary Events
- labels: ['msosa']

### NORMALIZED CONTENT

**Description**

A Multiple Boundary Event indicates that there are multiple triggers assigned to the Event. Only one of the specified triggers is required. The Event that occurred changes a normal flow into an exception flow.

**Notation**

- Multiple Boundary Event (Cancel Activity - True) [ATTACHMENT filename='boundary_event_multiple.png']
- Multiple Boundary Event (Cancel Activity - False) [ATTACHMENT filename='boundary_event_multiple_false.png']

**Related elements**

- Boundary Events
- Activities

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- [CONFLUENCE_PAGE title='(2026x) Creating and Using a BPMN Event' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>A Multiple Boundary Event indicates that there are multiple triggers assigned to the Event. Only one of the specified triggers is required. The Event that occurred changes a normal flow into an exception flow.</p><p><strong>Notation</strong></p><ul><li data-uuid="b3766468-324f-4518-8c02-44ed9bab5e5c">Multiple Boundary Event (Cancel Activity - True)<br /><ac:image ac:thumbnail="true" ac:height="55"><ri:attachment ri:filename="boundary_event_multiple.png"><ri:page ri:content-title="(2026x) Multiple Boundary Event" /></ri:attachment></ac:image></li><li data-uuid="9427ac32-4729-4e63-8686-d64f7b186415">Multiple Boundary Event (Cancel Activity - False)<br /><ac:image><ri:attachment ri:filename="boundary_event_multiple_false.png"><ri:page ri:content-title="(2026x) Multiple Boundary Event" /></ri:attachment></ac:image></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link" data-uuid="6ad5b49f-cce4-4c17-93e0-34e9828a2b0e"><a href="https://docs.nomagic.com/display/MT/(2026x) Boundary+Events">Boundary Events</a></li><li data-uuid="269a663c-e9f9-48ae-bdbc-04069fd2d70d"><a href="https://docs.nomagic.com/display/MT/(2026x) Activities">Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link" data-uuid="3d9979b2-635f-4085-bc55-c51e5ef393e3"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Process+Diagram">BPMN Process Diagram</a></li><li data-uuid="4ca52c1f-2716-4729-9545-e0c264ae3c41"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li data-uuid="908dd7d5-e29f-4d91-b05f-aa0b2d19a3d8"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li data-uuid="1eeed4e8-fa33-42aa-8c66-307b198e559b"><ac:link><ri:page ri:content-title="(2026x) Creating and Using a BPMN Event" /><ac:plain-text-link-body><![CDATA[Creating and Using an Event]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272738335 space=MT version=2 -->
## PAGE 03503: (2026x) Multiple Catching Intermediate Event

- page_id: `272738335`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738335/2026x+Multiple+Catching+Intermediate+Event
- version_number: 2
- version_date: `2025-11-25T14:44:48.657+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Business Process Model and Notation Concepts > (2026x) BPMN Process Diagram > (2026x) Intermediate Catch Event
- labels: ['msosa']

### NORMALIZED CONTENT

**Description**

A Multiple Catching Intermediate Event signifies that multiple types of events can be caught. Only one of the defined event triggers is required.

**Notation**

[IMAGE alt='' src='']

**Related element**

- Intermediate Catch Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- [CONFLUENCE_PAGE title='(2026x) Creating and Using a BPMN Event' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>A Multiple Catching Intermediate Event signifies that multiple types of events can be caught. Only one of the defined event triggers is required.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_catch_event_multiple.png"><ri:page ri:content-title="(2026x) Multiple Catching Intermediate Event" /></ri:attachment></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related element</strong></p><ul><li class="ancestor-link parent-link" data-uuid="2b55bbf2-a710-4ee6-a4dd-eace5e7330ec"><a href="https://docs.nomagic.com/display/MT/(2026x) Intermediate+Catch+Event">Intermediate Catch Event</a></li></ul><p class="ancestor-link parent-link"><strong>Related diagrams</strong></p><ul><li class="ancestor-link" data-uuid="ed1b3111-ad49-443e-a34f-14c697190478"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Process+Diagram">BPMN Process Diagram</a></li><li data-uuid="19ac5237-1650-4eb7-8bbb-f2e1756eed21"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li data-uuid="552d8f05-c027-4108-a82c-4a0dc9f1d071"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li data-uuid="e1f6a8ac-40cd-43c5-b773-3c8a6ae956fd"><ac:link><ri:page ri:content-title="(2026x) Creating and Using a BPMN Event" /><ac:plain-text-link-body><![CDATA[Creating and Using an Event]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272738458 space=MT version=2 -->
## PAGE 03504: (2026x) Multiple End Event

- page_id: `272738458`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738458/2026x+Multiple+End+Event
- version_number: 2
- version_date: `2025-11-25T14:45:17.293+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Business Process Model and Notation Concepts > (2026x) BPMN Process Diagram > (2026x) End Events
- labels: ['msosa']

### NORMALIZED CONTENT

**Description**

A Multiple End Event shows that there are multiple consequences of ending a process and all of them occur, for example, multiple messages might be sent.

**Notation**

[IMAGE alt='' src='']

**Related element**

- End Events

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- [CONFLUENCE_PAGE title='(2026x) Creating and Using a BPMN Event' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>A Multiple End Event shows that there are multiple consequences of ending a process and all of them occur, for example, multiple messages might be sent.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="end_event_multiple.png"><ri:page ri:content-title="(2026x) Multiple End Event" /></ri:attachment></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related element</strong></p><ul><li class="ancestor-link parent-link" data-uuid="8ef3ba7a-2918-4929-a6f3-9d8e8758019b"><a href="https://docs.nomagic.com/display/MT/(2026x) End+Events">End Events</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link" data-uuid="11ed4980-e669-4659-a166-db5c896e5408"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Process+Diagram">BPMN Process Diagram</a></li><li data-uuid="873fd3f8-f250-4794-92be-858eaa291632"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li data-uuid="7b6da85a-c2cf-462f-a358-c023137821a9"><ac:link><ri:page ri:content-title="(2026x) Creating and Using a BPMN Event" /><ac:plain-text-link-body><![CDATA[Creating and Using an Event]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272730189 space=MT version=1 -->
## PAGE 03505: (2026x) Multiple layout template

- page_id: `272730189`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730189/2026x+Multiple+layout+template
- version_number: 1
- version_date: `2025-11-25T13:36:38.230+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Diagramming > (2026x) Layout templates
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

#### CONTENT-LAYER: Composite Structure Diagram as a layout template

59508979

#### CONTENT-COLUMN: Composite Structure Diagram as a layout template

59508981

#### CONTENT-BLOCK: Composite Structure Diagram as a layout template

59508980

You can represent the same Class with a different appearance according to the context of Class usage in the Composite Structure diagram. To accomplish this, define multiple diagrams for the same Class element with different names, and set them as layout templates. The diagram names identify the differences between layout templates and simplify layout template selection when applying it. The procedures below explain how to create and apply multiple layout templates.

To create multiple layout templates

1. Create the Class diagram with a name that identifies the layout template name.
2. Define the appearance of Class and its Ports shapes in the Class diagram.[CONFLUENCE_PAGE title='(2026x) Defining layout template' space='']How to define the layout template >>
3. Set that Class diagram as the layout template. [CONFLUENCE_PAGE title='(2026x) Setting diagram as layout template' space='']How to set the Class diagram as layout template >>
4. Repeat steps 1, 2, and 3 until you have the required number of layout templates of the same Class element.
5. Apply multiple layout templates to other diagrams. [CONFLUENCE_PAGE title='(2026x) Applying layout template' space='']>]]>

The example below shows how the port's position on the*Modem Card* Block is represented differently: on the left side and on the right side of the Block shape. According to the illustration, the names of the Block Definition Diagrams are appropriate: *DefinitionPortsRight* and *DefinitionPortsLeft*. You can find the same layout templates when trying to apply one of those layout templates for the Part shape in the Internal Block Diagram.

###### [IMAGE alt='' src='']Two different layout templates of the Modem Card Block can be found as selection when applying it in any Internal Block Diagram. The illustration displays concepts from SysML v1 Plugin.

#### INFO: Composite Structure Diagram as a layout template

Composite Structure Diagram as a layout template

- From the version 19.0 SP1, you can define the appearance and layout of a Part Property with its Ports in the Composite Structure Diagram and set this diagram as layout template.
- If a Composite Structure Diagram displays several Part Properties, [CONFLUENCE_PAGE title='(2026x) Creating layout template' space=''] directly from a particular Part Property. It's appearance and layout will be copied to the template automatically.

59508978

**Sample model**

The sample model used in the figure of this page is **Modem Cable**: *[Modem Cable Layout Templates.mdzip](https://docs.nomagic.com/download/attachments/9915051/Modem%20Cable%20Layout%20Templates.mdzip?version=1&modificationDate=1481817717837&api=v2).*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="127d6ed2-2017-45d0-b33c-dc9598a4a087"><ac:parameter ac:name="id">59508979</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="5c2d8e4a-e17a-4be4-af8a-88499dbd0bed"><ac:parameter ac:name="id">59508981</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="07961580-8846-4631-a77f-8353ba57a8fb"><ac:parameter ac:name="id">59508980</ac:parameter><ac:rich-text-body><p>You can represent the same Class with a different appearance according to the context of Class usage in the Composite Structure diagram. To accomplish this, define multiple diagrams for the same Class element with different names, and set them as layout templates. The diagram names identify the differences between layout templates and simplify layout template selection when applying it. The procedures below explain how to create and apply multiple layout templates.</p><p><br /></p><p>To create multiple layout templates</p><hr /><ol><li>Create the Class diagram with a name that identifies the layout template name.</li><li><p>Define the appearance of Class and its Ports shapes in the Class diagram.<ac:link><ri:page ri:content-title="(2026x) Defining layout template" /><ac:link-body> <span class="confluence-link">How to define the layout template &gt;&gt;</span></ac:link-body></ac:link></p></li><li><p>Set that Class diagram as the layout template. <ac:link><ri:page ri:content-title="(2026x) Setting diagram as layout template" /><ac:link-body><span class="confluence-link">How to set the Class diagram as layout template &gt;&gt;</span></ac:link-body></ac:link></p></li><li>Repeat steps 1, 2, and 3 until you have the required number of layout templates of the same Class element.</li><li>Apply multiple layout templates to other diagrams. <span class="confluence-link"><ac:link><ri:page ri:content-title="(2026x) Applying layout template" /><ac:plain-text-link-body><![CDATA[How to apply layout template >>]]></ac:plain-text-link-body></ac:link></span></li></ol><p><br /></p><p>The example below shows how the port's position on the<em> Modem Card</em> Block is represented differently: on the left side and on the right side of the Block shape. According to the illustration, the names of the Block Definition Diagrams are appropriate: <em>DefinitionPortsRight</em> and <em>DefinitionPortsLeft</em>. You can find the same layout templates when trying to apply one of those layout templates for the Part shape in the Internal Block Diagram.</p><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="multiple_layout_templates.png"><ri:page ri:content-title="(2026x) Multiple layout template" /></ri:attachment></ac:image>Two different layout templates of the Modem Card Block can be found as selection when applying it in any Internal Block Diagram. The illustration displays concepts from SysML v1 Plugin.</h6><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="136bf21e-c771-40e3-b5f7-62d0f1b41818"><ac:parameter ac:name="title">Composite Structure Diagram as a layout template</ac:parameter><ac:rich-text-body><ul><li>From the version 19.0 SP1, you can define the appearance and layout of a Part Property with its Ports in the Composite Structure Diagram and set this diagram as layout template.</li><li>If a Composite Structure Diagram displays several Part Properties, <ac:link><ri:page ri:content-title="(2026x) Creating layout template" /><ac:plain-text-link-body><![CDATA[create a layout template]]></ac:plain-text-link-body></ac:link> directly from a particular Part Property. It's appearance and layout will be copied to the template automatically.</li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2972e541-5d83-4f05-b947-d083ad86e23e"><ac:parameter ac:name="id">59508978</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Sample model</strong></p><p>The sample model used in the figure of this page is <strong>Modem Cable</strong>: <span class="confluence-link"><em><a href="https://docs.nomagic.com/download/attachments/9915051/Modem%20Cable%20Layout%20Templates.mdzip?version=1&amp;modificationDate=1481817717837&amp;api=v2">Modem Cable Layout Templates.mdzip</a>.</em></span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272735276 space=MT version=1 -->
## PAGE 03506: (2026x) Multiple rules for the same source type

- page_id: `272735276`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272735276/2026x+Multiple+rules+for+the+same+source+type
- version_number: 1
- version_date: `2025-11-25T13:45:11.422+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Tools > (2026x) Model Transformation Wizard > (2026x) Controlling Type Mapping Rule Behavior
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

There can be multiple mapping rules for the same source type. For example, *String* > *varchar* and *String* > *nvarchar*. In this case, one of the rules must be marked as default by setting the **default** tag value on it to true.

The type map having several rules for the same type and without any one set as default cannot be used.

During the initial transformation, only the default rules for each source type come into play. E.g., if the user has a property with the *String* type, this will be transformed to property having the *varchar* type set.

However, during the transformation update, all rules come into play. If the destination type is one of the acceptable types according to the map, it is not changed. Otherwise it is replaced with the default mapping.

Regarding the example above, let’s say that after the initial transformation, the user changes the type of the property in the destination model from *varchar* to *nvarchar* (as a post-transformation refinement process). If the user now runs a transformation update, this change will not be overwritten, since *nvarchar* is an acceptable 
type as there is a *String* > *nvarchar* mapping in the type map as well. If on the other hand the user sets the type of this property to number, this would be reset the during transformation update, and the type will be forced back to *varchar*, as there is no *String* > *number* mapping.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>There can be multiple mapping rules for the same source type. For example, <em style="letter-spacing: 0.0px;">String</em> &gt; <em style="letter-spacing: 0.0px;">varchar</em> and <em style="letter-spacing: 0.0px;">String</em> &gt; <em style="letter-spacing: 0.0px;">nvarchar</em>. In this case, one of the rules must be marked as default by setting the <strong style="letter-spacing: 0.0px;">default</strong> tag value on it to true.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="d9149275-80af-4072-a7bd-0618d247baa8"><ac:rich-text-body><p>The type map having several rules for the same type and without any one set as default cannot be used.</p></ac:rich-text-body></ac:structured-macro><p>During the initial transformation, only the default rules for each source type come into play. E.g., if the user has a property with the <em>String</em> type, this will be transformed to property having the <em>varchar</em> type set.</p><p>However, during the transformation update, all rules come into play. If the destination type is one of the acceptable types according to the map, it is not changed. Otherwise it is replaced with the default mapping.</p><p>Regarding the example above, let’s say that after the initial transformation, the user changes the type of the property in the destination model from <em>varchar</em> to <em>nvarchar</em> (as a post-transformation refinement process). If the user now runs a transformation update, this change will not be overwritten, since <em>nvarchar</em> is an acceptable <br />type as there is a <em>String</em> &gt; <em>nvarchar</em> mapping in the type map as well. If on the other hand the user sets the type of this property to number, this would be reset the during transformation update, and the type will be forced back to <em>varchar</em>, as there is no <em>String</em> &gt; <em>number</em> mapping.</p>
````

<!--NOMAGIC_PAGE id=272737882 space=MT version=2 -->
## PAGE 03507: (2026x) Multiple Start Event

- page_id: `272737882`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272737882/2026x+Multiple+Start+Event
- version_number: 2
- version_date: `2025-11-25T14:44:40.394+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Business Process Model and Notation Concepts > (2026x) BPMN Process Diagram > (2026x) Start Events
- labels: ['msosa']

### NORMALIZED CONTENT

**Description**

A Multiple Start Event indicates that there are multiple ways to trigger a process. However, only one is required.

**Notation**

- Interrupting Multiple Start Event [ATTACHMENT filename='start_event_multiple_interr.png']
- Non-interrupting Multiple Start Event [ATTACHMENT filename='start_event_multiple_noninterr.png']

**Related element**

- Start Events

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- [CONFLUENCE_PAGE title='(2026x) Creating and Using a BPMN Event' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>A Multiple Start Event indicates that there are multiple ways to trigger a process. However, only one is required.</p><p><strong>Notation</strong></p><ul><li data-uuid="bc69b347-0051-4b3d-9bed-64d398a644d6">Interrupting Multiple Start Event<br /><ac:image><ri:attachment ri:filename="start_event_multiple_interr.png"><ri:page ri:content-title="(2026x) Multiple Start Event" /></ri:attachment></ac:image></li><li data-uuid="b96973c6-b5a8-4530-a73e-43b37fe5e092">Non-interrupting Multiple Start Event<br /><ac:image ac:thumbnail="true" ac:height="55"><ri:attachment ri:filename="start_event_multiple_noninterr.png"><ri:page ri:content-title="(2026x) Multiple Start Event" /></ri:attachment></ac:image></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related element</strong></p><ul><li class="ancestor-link parent-link" data-uuid="e59575bf-945c-43aa-9a51-c5c88370f053"><a href="https://docs.nomagic.com/display/MT/(2026x) Start+Events">Start Events</a></li></ul><p class="ancestor-link parent-link"><strong>Related diagrams</strong></p><ul><li class="ancestor-link" data-uuid="5e5ac68d-5978-4374-9835-ad4bd6e25ff9"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Process+Diagram">BPMN Process Diagram</a></li><li data-uuid="93998dc4-af82-486a-b034-7beb5daa38e7"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li data-uuid="ba791288-a954-41cf-bbdd-41f2e119ba7d"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li data-uuid="72f7a0a3-e474-45db-a5ea-a6dc44dc4eea"><ac:link><ri:page ri:content-title="(2026x) Creating and Using a BPMN Event" /><ac:plain-text-link-body><![CDATA[Creating and Using an Event]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272738392 space=MT version=2 -->
## PAGE 03508: (2026x) Multiple Throwing Intermediate Event

- page_id: `272738392`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738392/2026x+Multiple+Throwing+Intermediate+Event
- version_number: 2
- version_date: `2025-11-25T14:44:58.436+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Business Process Model and Notation Concepts > (2026x) BPMN Process Diagram > (2026x) Intermediate Throwing Event
- labels: ['msosa']

### NORMALIZED CONTENT

**Description**

A Multiple Throwing Intermediate Event signifies that multiple types of events are thrown. All of the defined triggers will be thrown by this event.

**Notation**

[IMAGE alt='' src='']

**Related element**

- Intermediate Throwing Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- [CONFLUENCE_PAGE title='(2026x) Creating and Using a BPMN Event' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>A Multiple Throwing Intermediate Event signifies that multiple types of events are thrown. All of the defined triggers will be thrown by this event.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_throwing_event_multiple.png"><ri:page ri:content-title="(2026x) Multiple Throwing Intermediate Event" /></ri:attachment></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related element</strong></p><ul><li class="ancestor-link parent-link" data-uuid="20f55186-738c-44a5-bb80-6531b9e3c2bf"><a href="https://docs.nomagic.com/display/MT/(2026x) Intermediate+Throwing+Event">Intermediate Throwing Event</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link" data-uuid="c59a32bb-be42-4ddf-91a5-dd189fc7070f"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Process+Diagram">BPMN Process Diagram</a></li><li data-uuid="7f4db39e-fa27-46de-b83f-1e2bf8b07ff6"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li data-uuid="221306c7-059c-4cc7-92a4-b78dffa469d6"><ac:link><ri:page ri:content-title="(2026x) Creating and Using a BPMN Event" /><ac:plain-text-link-body><![CDATA[Creating and Using an Event]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272730122 space=MT version=1 -->
## PAGE 03509: (2026x) NAF

- page_id: `272730122`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730122/2026x+NAF
- version_number: 1
- version_date: `2025-11-25T13:36:33.778+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling
- labels: ['msosa']

### NORMALIZED CONTENT

664862839

664862842

664862840

According to modeling needs, there are the following NAF templates for different purposes:

- **NAF Project**- creating a NAF project will switch the application to the NAF graphical user interface and use the NAF model templates.
- **NAF Project Template with Process Guide**- using this template, you will get a new NAF project enhanced with a modeling guide. The modeling guide helps you to build the architecture by providing summary information about the NAF structure and the architecture creation process.

All NAF views are described in the following sections:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="8dfce412-a5eb-4f75-a76d-2c4945454c73"><ac:parameter ac:name="id">664862839</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4d41cfbb-a2ba-4179-92cc-0e57804b3e2f"><ac:parameter ac:name="id">664862842</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3a5a99b7-610b-4d5b-892c-575c095e81b1"><ac:parameter ac:name="id">664862840</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><span style="color: rgb(62,63,64);">According to modeling needs, there are the following NAF templates for different purposes:</span></p><ul><li><span style="color: rgb(62,63,64);"><strong>NAF Project</strong><span> </span>- creating a NAF project will switch the application to the NAF graphical user interface and use the NAF model templates.</span></li><li><span style="color: rgb(62,63,64);"><strong>NAF Project Template with Process Guide</strong><span> </span>- using this template, you will get a new NAF project enhanced with a modeling guide. The modeling guide helps you to build the architecture by providing summary information about the NAF structure and the architecture creation process.</span></li></ul><p>All NAF views are described in the following sections:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="a27e85fb-d3e5-4987-8232-5d1349576e8f" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272730242 space=MT version=1 -->
## PAGE 03510: (2026x) NAF 4.0

- page_id: `272730242`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730242/2026x+NAF+4.0
- version_number: 1
- version_date: `2025-11-25T13:36:43.125+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling
- labels: ['naf-4', 'nato-architecture-framework', 'msosa']

### NORMALIZED CONTENT

769279849

769279851

769279850

The NATO Architecture Framework (NAF) is a standard for developing Enterprise Architectures. An Enterprise Architecture is a model of a current or future state of an enterprise. An enterprise could be an organization, a system (including human factors), or a project. The purpose of enterprise architecture is to capture the complex dependencies that exist in large-scale systems of systems so as to aid with decision support. NAF provides a standard way to model the architecture.

According to modeling needs, there are the following NAF 4.0 templates for different purposes:

- **NAF 4.0 Project** - creating a NAF 4.0 project will switch the application to the NAF 4.0 graphical user interface and use the NAF 4.0 model templates.
- **NAF 4.0 Project Template with Process Guide** - using this template, you will get a new NAF 4.0 project enhanced with a modeling guide. The modeling guide helps you to build the architecture by providing summary information about the NAF structure and the architecture creation process.

[IMAGE alt='' src='']

800600

769279848

**NAF 4.0 viewpoints**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="628db6c1-e207-44cb-96ba-2de9aca8c153"><ac:parameter ac:name="id">769279849</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="5791c30f-784c-48fd-b772-93d28e80e722"><ac:parameter ac:name="id">769279851</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="af9c19bf-73df-45c2-a3fd-442a7e985f88"><ac:parameter ac:name="id">769279850</ac:parameter><ac:rich-text-body><p>The NATO <span class="wp-glossary wpg-tooltip">Architecture Framework</span> (NAF) is a standard for developing Enterprise Architectures. An Enterprise Architecture is a model of a current or future state of an enterprise. An enterprise could be an organization, a <span class="wp-glossary wpg-tooltip">system</span> (including human factors), or a project. The purpose of enterprise architecture is to capture the complex dependencies that exist in large-scale systems of systems so as to aid with decision support. NAF provides a standard way to model the architecture.</p><p><span style="color: rgb(62,63,64);">According to modeling needs, there are the following NAF 4.0 templates for different purposes:</span></p><ul><li><span style="color: rgb(62,63,64);"><strong>NAF 4.0 Project</strong> - creating a NAF 4.0 project will switch the application to the NAF 4.0 graphical user interface and use the NAF 4.0 model templates.</span></li><li><span style="color: rgb(62,63,64);"><strong>NAF 4.0 Project Template with Process Guide</strong> - using this template, you will get a new NAF 4.0 project enhanced with a modeling guide. The modeling guide helps you to build the architecture by providing summary information about the NAF structure and the architecture creation process.</span></li></ul><p><ac:image ac:title="NAF 4.0 Viewpoints and Views" ac:alt="NAF 4.0 Viewpoints and Views"><ri:attachment ri:filename="viewpoints-views_naf4.png"><ri:page ri:content-title="(2026x) NAF 4.0" /></ri:attachment></ac:image></p><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="a8f2f393-ea58-4796-9db9-ff07eddbf5c6"><ac:parameter ac:name="width">800</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=9amaJGkw9xk" /></ac:parameter><ac:parameter ac:name="height">600</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1fddfa53-696e-419c-afce-a8df0b33eb5d"><ac:parameter ac:name="id">769279848</ac:parameter><ac:rich-text-body><p><strong>NAF 4.0 viewpoints</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="70e28586-4366-4836-960c-bfef5f2ca2bb" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272733249 space=MT version=1 -->
## PAGE 03511: (2026x) NATO All View Viewpoint

- page_id: `272733249`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733249/2026x+NATO+All+View+Viewpoint
- version_number: 1
- version_date: `2025-11-25T13:41:51.813+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF
- labels: ['msosa']

### NORMALIZED CONTENT

664966376

664966378

664966377

There are some overarching aspects of architectures that relate to all views. These overarching aspects are captured in the NATO All View (NAV). The NAV products provide information pertinent to the entire architecture but do not represent a distinct view of the architecture. NAV subviews set the scope and context of the architecture. The scope includes the subject area and timeframe for the architecture. The setting in which the architecture exists comprises the interrelated conditions that compose the context for the architecture. These conditions include doctrine, tactics, techniques and procedures, relevant goals and vision statements, concepts of operations, scenarios, and environmental conditions.

664966374

**Views**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="1ea859bb-7123-4154-b8b2-fa694d3ba4bd"><ac:parameter ac:name="id">664966376</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c32df575-1820-4c70-ab6b-2b97941f0c7d"><ac:parameter ac:name="id">664966378</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b16e2ab2-a297-4bed-9b9a-4b56e10caae8"><ac:parameter ac:name="id">664966377</ac:parameter><ac:rich-text-body><p>There are some overarching aspects of architectures that relate to all views. These overarching aspects are captured in the NATO All View (NAV). The NAV products provide information pertinent to the entire architecture but do not represent a distinct view of the architecture. NAV subviews set the scope and context of the architecture. The scope includes the subject area and timeframe for the architecture. The setting in which the architecture exists comprises the interrelated conditions that compose the context for the architecture. These conditions include doctrine, tactics, techniques and procedures, relevant goals and vision statements, concepts of operations, scenarios, and environmental conditions.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ad9bb53c-9a9d-4e13-8bab-45ac2b2660a9"><ac:parameter ac:name="id">664966374</ac:parameter><ac:rich-text-body><p><strong>Views</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f461bd3f-dbff-44cf-bc02-3deb92e8d811" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731284 space=MT version=1 -->
## PAGE 03512: (2026x) NATO Capability Viewpoint

- page_id: `272731284`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731284/2026x+NATO+Capability+Viewpoint
- version_number: 1
- version_date: `2025-11-25T13:38:41.190+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF
- labels: ['msosa']

### NORMALIZED CONTENT

668203034

668203036

668203035

The NATO Capability View (NCV) supports the process of analyzing and optimizing the delivery of military capabilities in line with NATO‘s strategic intent. The NCV achieves this by capturing essential elements of NATO‘s strategic vision and concepts and NATO‘s capability planning process, and decomposing this data into a capability taxonomy. The taxonomy is augmented with schedule data and measures of effectiveness to enable the analysis of capability gaps and overlaps. The NCV further details the dependencies between military capabilities, enabling 
capability options to be built in a more coherent manner and effective trade-offs to be conducted across NATO common funded programmes.

668203033

**Views**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a82db89f-25a4-4151-aa48-d4ba04d2f40f"><ac:parameter ac:name="id">668203034</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="43c24e98-0c62-4b4a-9389-1e540aeeede3"><ac:parameter ac:name="id">668203036</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b4d1a72f-8011-4aff-b419-c79ce1d24240"><ac:parameter ac:name="id">668203035</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The NATO Capability View (NCV) supports the process of analyzing and optimizing the delivery of military capabilities in line with NATO‘s strategic intent. The NCV achieves this by capturing essential elements of NATO‘s strategic vision and concepts and NATO‘s capability planning process, and decomposing this data into a capability taxonomy. The taxonomy is augmented with schedule data and measures of effectiveness to enable the analysis of capability gaps and overlaps. The NCV further details the dependencies between military capabilities, enabling<br />capability options to be built in a more coherent manner and effective trade-offs to be conducted across NATO common funded programmes.</p><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="bdbfe801-97db-4028-b95f-fb30b8478177"><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=xD91EYVU-bM" /></ac:parameter></ac:structured-macro>  <ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="c662a95d-1b50-48a6-bd99-a750714426b4"><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=LB1Ure3ravQ" /></ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="28965a23-6c52-4824-9ea8-02f3d96b7143"><ac:parameter ac:name="id">668203033</ac:parameter><ac:rich-text-body><p><strong>Views</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="73ad8146-70e8-435a-9c95-cbe830a9678f" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731557 space=MT version=1 -->
## PAGE 03513: (2026x) NATO Operational Viewpoint

- page_id: `272731557`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731557/2026x+NATO+Operational+Viewpoint
- version_number: 1
- version_date: `2025-11-25T13:39:14.266+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF
- labels: ['msosa']

### NORMALIZED CONTENT

750529842

750529844

750529843

The NOV is a description of the tasks and activities, operational elements, and information exchanges required to accomplish NATO missions. The NOV contains graphical and textual products that comprise an identification of the nodes, their assigned tasks and activities, and dependencies between nodes. It defines the types of information exchanged, which tasks and activities are supported by the information exchanges, and the operational details of information exchanges.

750529841

**Views**

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="07712d33-1f7a-4c8d-bae4-24c67fdda732"><ac:parameter ac:name="id">750529842</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="cd72dfda-2684-41bd-8aea-d385f8c67a38"><ac:parameter ac:name="id">750529844</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="81eddc1d-ed04-4186-86c7-e0a0075d7a91"><ac:parameter ac:name="id">750529843</ac:parameter><ac:rich-text-body><p>The NOV is a description of the tasks and activities, operational elements, and information exchanges required to accomplish NATO missions. The NOV contains graphical and textual products that comprise an identification of the nodes, their assigned tasks and activities, and dependencies between nodes. It defines the types of information exchanged, which tasks and activities are supported by the information exchanges, and the operational details of information exchanges.</p><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="99b8c7c0-49af-4ecc-929f-17777e8e052a"><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=jrpPuZ8Vf74" /></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c813ef36-0f47-4dfa-8720-20f293c335d4"><ac:parameter ac:name="id">750529841</ac:parameter><ac:rich-text-body><p><strong>Views</strong></p><p><strong><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="a9b765e5-4ad6-44a6-b947-1e87ca347cff" /></strong></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731427 space=MT version=1 -->
## PAGE 03514: (2026x) NATO Programme Viewpoint

- page_id: `272731427`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731427/2026x+NATO+Programme+Viewpoint
- version_number: 1
- version_date: `2025-11-25T13:38:54.164+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF
- labels: ['msosa']

### NORMALIZED CONTENT

734801879

734801881

734801880

Programme views are introduced in the NAF Version 3 to describe the relationships between NATO capability requirements and the various programmes and projects being implemented. They provide programmatic details and highlight the dependencies between capability management and the NATO acquisition process. This information can be further leveraged to show the impact of acquisition decisions on the architecture.

734801878

**Views**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f8cb3d2a-4c71-4af9-9f10-a67e63c5e795"><ac:parameter ac:name="id">734801879</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fc33e12e-0477-4b55-bc61-4beafcd469dd"><ac:parameter ac:name="id">734801881</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="aad16fcd-3444-4995-8552-954e6473e59f"><ac:parameter ac:name="id">734801880</ac:parameter><ac:rich-text-body><p>Programme views are introduced in the NAF Version 3 to describe the relationships between NATO capability requirements and the various programmes and projects being implemented. They provide programmatic details and highlight the dependencies between capability management and the NATO acquisition process. This information can be further leveraged to show the impact of acquisition decisions on the architecture.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7cabc614-9a6b-46b8-8943-6748725b402c"><ac:parameter ac:name="id">734801878</ac:parameter><ac:rich-text-body><p><strong>Views</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e5b42e60-078b-4e0b-a8ca-33e0f38e3688" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732765 space=MT version=1 -->
## PAGE 03515: (2026x) NATO Service-Oriented Viewpoint

- page_id: `272732765`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732765/2026x+NATO+Service-Oriented+Viewpoint
- version_number: 1
- version_date: `2025-11-25T13:41:13.421+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF
- labels: ['msosa']

### NORMALIZED CONTENT

762035537

762035539

762035538

The NSOV is added to the NAF to support building architectures based on the concept of a Service-Oriented Architecture (SOA), which is fundamental to the NNEC paradigm. The NSOV is a description of services needed to directly support the operational domain as described in the NATO Operational View. A service, within the NSOV, is understood in its broadest sense, as a unit of work through which a provider provides a useful result to a consumer. NSOV focuses strictly on identifying and describing services. The view also supports the description of service taxonomies, service orchestrations, a mapping of services to operational activities, and a description of various forms of service behavior.

762035536

**Views**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3319a13d-62c7-4ceb-a552-0c21039164d4"><ac:parameter ac:name="id">762035537</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ee65752d-59e2-4b28-aa36-96c23e7ad747"><ac:parameter ac:name="id">762035539</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2c9aa00a-f8da-4232-bb78-6dd0ba84048d"><ac:parameter ac:name="id">762035538</ac:parameter><ac:rich-text-body><p>The NSOV is added to the NAF to support building architectures based on the concept of a Service-Oriented Architecture (SOA), which is fundamental to the NNEC paradigm. The NSOV is a description of services needed to directly support the operational domain as described in the NATO Operational View. A service, within the NSOV, is understood in its broadest sense, as a unit of work through which a provider provides a useful result to a consumer. NSOV focuses strictly on identifying and describing services. The view also supports the description of service taxonomies, service orchestrations, a mapping of services to operational activities, and a description of various forms of service behavior.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8b922e2d-82c6-4817-beca-4a9d50495d45"><ac:parameter ac:name="id">762035536</ac:parameter><ac:rich-text-body><p><strong>Views</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="43865117-5499-4b2d-b855-23e0d0bd8b56" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272730124 space=MT version=1 -->
## PAGE 03516: (2026x) NATO Systems Viewpoint

- page_id: `272730124`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730124/2026x+NATO+Systems+Viewpoint
- version_number: 1
- version_date: `2025-11-25T13:36:33.881+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF
- labels: ['msosa']

### NORMALIZED CONTENT

764579150

764579153

764579151

The NSV is a set of graphical and textual products that describes systems and interconnections providing for or supporting NATO processes. The NSV associates systems resources to the NOV and/or the NSOV. These systems are the resources that are used to construct the services of the NSOV, and support the operational activities and facilitate the exchange of information among operational nodes as defined in the NOV.

764579149

**Views**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ee94a29e-03ab-419e-a575-0ab1107dad94"><ac:parameter ac:name="id">764579150</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="e09aefa7-89a9-4815-baad-9cded28303da"><ac:parameter ac:name="id">764579153</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e59395d1-67ed-4328-a830-d3b6cea51f3d"><ac:parameter ac:name="id">764579151</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The NSV is a set of graphical and textual products that describes systems and interconnections providing for or supporting NATO processes. The NSV associates systems resources to the NOV and/or the NSOV. These systems are the resources that are used to construct the services of the NSOV, and support the operational activities and facilitate the exchange of information among operational nodes as defined in the NOV.</p><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="3f2d8bd4-b5bf-4e5b-b114-1604a594cf3c"><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=qvL33ckmJJY" /></ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="758d2e59-5673-4bd5-b577-e8e995ea2014"><ac:parameter ac:name="id">764579149</ac:parameter><ac:rich-text-body><p><strong>Views</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d93af2e7-9046-4b99-adeb-9490bc1f9c81" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272730229 space=MT version=1 -->
## PAGE 03517: (2026x) NATO Technical Viewpoint

- page_id: `272730229`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730229/2026x+NATO+Technical+Viewpoint
- version_number: 1
- version_date: `2025-11-25T13:36:41.248+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF
- labels: ['msosa']

### NORMALIZED CONTENT

765062204

765062206

765062205

The NTV provides the technical implementation guidelines upon which engineering specifications are based and common building blocks are established. The NTV includes a collection of the technical standards, implementation conventions, standards options, rules, and criteria organized into profiles that govern systems and services, and their elements for a given architecture.

765062202

**Views**

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9f2d766e-2d68-4009-8ed2-fa109d3cada3"><ac:parameter ac:name="id">765062204</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="5a44562d-9d30-4cff-bf8a-dba954651dbf"><ac:parameter ac:name="id">765062206</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1ade4440-0c42-471a-9f8c-c47b2fdf607d"><ac:parameter ac:name="id">765062205</ac:parameter><ac:rich-text-body><p>The NTV provides the technical implementation guidelines upon which engineering specifications are based and common building blocks are established. The NTV includes a collection of the technical standards, implementation conventions, standards options, rules, and criteria organized into profiles that govern systems and services, and their elements for a given architecture.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3ea7fb5a-6485-4fd7-a865-22e423f4eb23"><ac:parameter ac:name="id">765062202</ac:parameter><ac:rich-text-body><p><strong>Views</strong></p><p><strong><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="a581d41c-9f07-4aa8-82b2-d562ccc1328c" /></strong></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272733251 space=MT version=1 -->
## PAGE 03518: (2026x) NAV-1 Overview and Summary Information

- page_id: `272733251`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733251/2026x+NAV-1+Overview+and+Summary+Information
- version_number: 1
- version_date: `2025-11-25T13:41:51.975+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO All View Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

667950767

667950769

667950768

**Description**

The overview and summary information contained within the NAV-1 product provides an executive-level summary information in a consistent form that allows for quick reference and comparison between architectural descriptions. NAV-1 includes assumptions, constraints, and limitations that may affect high-level decisions relating to an architecture. In an enterprise repository environment, individual architectures are mapped against enterprise phases to provide context between the architectures. NAV-1 is usually a structured text product. Organizations may create a template for the NAV-1 that can then be used to create a consistent set of information across different architecture-based projects.

**Implementation**

NAV-1 can be represented:

- Using a report, which is automatically generated from all data. Since only a partial NAV-1 report can be generated, the rest of data must be filled in manually.
- Using a NAV-1 diagram which is based on the UML Class diagram.

**Sample**

[IMAGE alt='' src='']

###### Fragment of NAV-1 Overview and Summary Information report

667950766

**Related elements**

- [CONFLUENCE_PAGE title='Architectural Description' space='MED']
- [CONFLUENCE_PAGE title='Architecture Metadata' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Generating document based reports' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="23c814b8-baa3-4b7f-85e2-062cfa1564a6"><ac:parameter ac:name="id">667950767</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="f19fef55-a34c-454d-bf8f-f1156772cf01"><ac:parameter ac:name="id">667950769</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="eb22f619-ba06-4246-845a-7506303a7ac9"><ac:parameter ac:name="id">667950768</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The overview and summary information contained within the NAV-1 product provides an executive-level summary information in a consistent form that allows for quick reference and comparison between architectural descriptions. NAV-1 includes assumptions, constraints, and limitations that may affect high-level decisions relating to an architecture. In an enterprise repository environment, individual architectures are mapped against enterprise phases to provide context between the architectures. NAV-1 is usually a structured text product. Organizations may create a template for the NAV-1 that can then be used to create a consistent set of information across different architecture-based projects.</p><p><strong>Implementation</strong></p><p>NAV-1 can be represented:</p><ul><li>Using a report, which is automatically generated from all data. Since only a partial NAV-1 report can be generated, the rest of data must be filled in manually.</li><li>Using a NAV-1 diagram which is based on the UML Class diagram.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nav_1.jpg"><ri:page ri:content-title="(2026x) NAV-1 Overview and Summary Information" /></ri:attachment></ac:image></p><h6>Fragment of NAV-1 Overview and Summary Information report</h6><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3e836516-da12-45b4-8445-cde82018d8be"><ac:parameter ac:name="id">667950766</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Architectural Description" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Architecture Metadata" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Generating document based reports" /><ac:plain-text-link-body><![CDATA[Generating reports]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272733258 space=MT version=1 -->
## PAGE 03519: (2026x) NAV-2 Integrated Dictionary

- page_id: `272733258`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733258/2026x+NAV-2+Integrated+Dictionary
- version_number: 1
- version_date: `2025-11-25T13:41:52.567+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO All View Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

668142597

668142599

668142598

**Description**

The NAV-2 presents all the metadata used in an architecture. An NAV-2 presents all the data as a hierarchy and provides a text definition for each one by displaying the following properties:

- The name used for this element in the architecture
- Alternative names for this element, for example, if the element is listed in the NATO ontology it may have multiple names
- A brief description of the element

**Implementation**

NAV-2 can be represented:

- Using a report, which is automatically generated from all data.
- An AV-2 table. If you have NAV-2 diagrams from previous versions, they will bemigrated into the NAV-1 diagram when loading the project with UPDM 17.0.2.

**Sample**

[IMAGE alt='' src='']

###### NAV-2 Integrated Dictionary

[IMAGE alt='' src='']

###### Fragment of NAV-2 Integrated Dictionary report

668142596

**Related elements**

- [CONFLUENCE_PAGE title='Definition' space='MED']
- [CONFLUENCE_PAGE title='Alias' space='MED']
- [CONFLUENCE_PAGE title='Same As' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Generating document based reports' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="64628376-abf9-4b55-bcb8-6d34e359b8f9"><ac:parameter ac:name="id">668142597</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="76b44a0e-0ecb-400d-82af-90abdb40d72f"><ac:parameter ac:name="id">668142599</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="418bb541-54f4-4585-aa35-5d1a9098dd37"><ac:parameter ac:name="id">668142598</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NAV-2 presents all the metadata used in an architecture. An NAV-2 presents all the data as a hierarchy and provides a text definition for each one by displaying the following properties:</p><ul><li>The name used for this element in the architecture</li><li>Alternative names for this element, for example, if the element is listed in the NATO ontology it may have multiple names</li><li>A brief description of the element</li></ul><p><strong>Implementation</strong></p><p>NAV-2 can be represented:</p><ul><li>Using a report, which is automatically generated from all data.</li><li><p class="auto-cursor-target">An AV-2 table.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="074e8cda-a308-4e86-a734-e03e78f5a981"><ac:rich-text-body>If you have NAV-2 diagrams from previous versions, they will bemigrated into the NAV-1 diagram when loading the project with UPDM 17.0.2.</ac:rich-text-body></ac:structured-macro></li></ul><p class="auto-cursor-target"><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nav_2.jpg"><ri:page ri:content-title="(2026x) NAV-2 Integrated Dictionary" /></ri:attachment></ac:image></p><h6>NAV-2 Integrated Dictionary</h6><p><ac:image><ri:attachment ri:filename="Nav_2_report.jpg"><ri:page ri:content-title="(2026x) NAV-2 Integrated Dictionary" /></ri:attachment></ac:image></p><h6>Fragment of NAV-2 Integrated Dictionary report</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e5ca088e-52c3-4211-a6ce-fe9c9fa11245"><ac:parameter ac:name="id">668142596</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Definition" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Alias" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Same As" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Generating document based reports" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272736905 space=MT version=2 -->
## PAGE 03520: (2026x) Navigating between different levels of abstraction

- page_id: `272736905`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272736905/2026x+Navigating+between+different+levels+of+abstraction
- version_number: 2
- version_date: `2025-11-25T14:43:09.020+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Model analysis > (2026x) Traceability
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

1977021339

1977021341

1977021340

During the development process and in order to understand the system fast, navigating between elements from different levels of abstraction is necessary. Navigating from one element to another is easy using the modeling tool's GUI capabilities of the traceability feature, if there is at least one traceability relation between them.

| To navigate between different levels of abstraction, use the following features: |  |
| --- | --- |
| Element’s Specification window | Open the element’s Specification window and select the Traceability property group, and then right-click on the property. Choose Open Specification and select an element (if there is more than one related element). The Specification window of this element will be opened. |
| Element’s Properties panel | Open the element’s Properties panel, select the Traceability tab, and then right-click on the property. Choose Open Specification and select an element (if there is more than one related element). The Specification window of this element will be opened. |
| Go To submenu on element’s shortcut menu | From the element’s shortcut menu, select Go To > Traceability > Specification/ Realization/Other . Choose a property and then select an element. The element will be selected in the Containment tree. |

###### Selecting an element to open specification

1977021338

**Related pages**

- Traceability

- 
  - Creating traceability relations
  - Traceability relations representation
  - Navigating between different levels of abstraction
  - Analyzing traceability relations
  - Predefined traceability rules
  - Custom traceability rules

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="2aa0c09b-29d0-4c4a-8c0a-24d34057adba"><ac:parameter ac:name="id">1977021339</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="02a33ee5-2dec-4b45-bc7a-e5dcd218a4a8"><ac:parameter ac:name="id">1977021341</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2fa8011b-5e89-4983-99fe-a5e56ea3796e"><ac:parameter ac:name="id">1977021340</ac:parameter><ac:rich-text-body><div class="layoutArea"><div class="column"><p><span>During the development process and in order to understand the system fast, navigating between elements from different levels of abstraction is necessary. Navigating from one element to another is easy using the modeling tool's GUI capabilities of the traceability feature, if there is at least one traceability relation between them.</span></p><p><span> <br /> </span></p><table class="relative-table wrapped" style="width: 98.913%;"><colgroup> <col style="width: 26.4431%;" /> <col style="width: 73.5569%;" /> </colgroup><tbody><tr><th colspan="2">To navigate between different levels of abstraction, use the following features:</th></tr><tr><td><div class="layoutArea"><div class="column"><p><span>Element’s <strong>Specification</strong> window</span></p></div></div></td><td><div class="layoutArea"><div class="column"><p><span>Open the element’s <strong>Specification</strong> window and select the </span> <strong>Traceability </strong><span>property group, and then right-click on the property. Choose </span> <strong>Open Specification</strong> <span>and select an element (if there is more than one related element). The Specification window of this element will be opened. </span></p></div></div></td></tr><tr><td><div class="layoutArea"><div class="column"><p><span>Element’s </span> <strong>Properties </strong> <span>panel</span></p></div></div></td><td><div class="layoutArea"><div class="column"><p><span>Open the element’s </span> <strong>Properties </strong><span>panel, select the </span> <strong>Traceability </strong><span>tab, and then right-click on the property. Choose </span> <strong>Open Specification</strong> <span>and select an element (if there is more than one related element). The Specification window of this element will be opened.</span></p></div></div></td></tr><tr><td><div class="layoutArea"><div class="column"><div class="layoutArea"><div class="column"><p><strong>Go To </strong> <span>submenu on element’s shortcut menu</span></p></div></div></div></div></td><td><div class="layoutArea"><div class="column"><p><span>From the element’s shortcut menu, select </span> <strong>Go To &gt; Traceability &gt; Specification/ Realization/Other</strong> <span>. Choose a property and then select an element. The element will be selected in the Containment tree.</span></p></div></div></td></tr></tbody></table><p><span> <br /> </span></p><div class="page" title="Page 524"><ac:image ac:align="center"><ri:attachment ri:filename="selecting_element_to_open_specification.png"><ri:page ri:content-title="(2026x) Navigating between different levels of abstraction" /></ri:attachment></ac:image></div><div class="page" title="Page 524"><div class="layoutArea"><div class="column"><h6 style="text-align: center;"><span>  Selecting an element to open specification </span></h6></div></div></div></div></div></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="79cf8371-0bdb-4c1a-96c1-88b909865a1c"><ac:parameter ac:name="id">1977021338</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><a href="https://docs.nomagic.com/display/MT/(2026x) Traceability">Traceability</a></li></ul><ul class="list-children not-expandable"><li style="list-style-type: none;background-image: none;"><ul class="list-children not-expandable"><li> <a href="https://docs.nomagic.com/display/MT/(2026x) Creating+traceability+relations">Creating traceability relations</a></li><li> <a href="https://docs.nomagic.com/display/MT/(2026x) Traceability+relations+representation">Traceability relations representation</a></li><li class="current"> <a href="https://docs.nomagic.com/display/MT/(2026x) Navigating+between+different+levels+of+abstraction">Navigating between different levels of abstraction</a></li><li> <a href="https://docs.nomagic.com/display/MT/(2026x) Analyzing+traceability+relations">Analyzing traceability relations</a></li><li> <a href="https://docs.nomagic.com/display/MT/(2026x) Predefined+traceability+rules">Predefined traceability rules</a></li><li> <a href="https://docs.nomagic.com/display/MT/(2026x) Custom+traceability+rules">Custom traceability rules</a></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272730309 space=MT version=1 -->
## PAGE 03521: (2026x) Navigation among aspect diagrams

- page_id: `272730309`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730309/2026x+Navigation+among+aspect+diagrams
- version_number: 1
- version_date: `2025-11-25T13:36:54.898+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Diagramming > (2026x) Diagram aspects
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

581451485

581451487

581451486

When elements have an internal structure, the [CONFLUENCE_PAGE title='(2026x) Displaying rake icon' space=''] appears on the element shape. If those elements belong to an aspect diagram, the rake icon navigates to the same aspect internal structure of the selected element. If there is no internal diagram of the same aspect, then any diagram of another aspect or diagram without aspect is opened.

The figure below demonstrates the *electrical* Internal Block diagram of the *Climate Control Hardware*. The rake icon on the part typed by *Control System* Block indicates that it contains an inner structure. There are four Internal Block diagrams for the *Control System* in the model*.* Although, after double-clicking on that part shape typed by *Control System* Block, the rake icon navigates exactly to the *electrical* Internal Block diagram of the *Control System.*

[IMAGE alt='' src='']

###### The navigation among aspect diagrams via rake icon. The illustration displays concepts from SysML v1 Plugin.

581451484

**Sample model**

The model used in the figures of this page is the **Diagram aspects** sample model:

- Download [ATTACHMENT filename='diagram aspects.mdzip'].
- Find in the modeling tool: *<modeling tool installation directory>\samples\SysML v1\diagram aspects.mdzip.*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="69210b66-aa50-48f6-8733-5b64efd65294"><ac:parameter ac:name="id">581451485</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ed6ee1d1-54b6-4174-8099-37c4a253b6f1"><ac:parameter ac:name="id">581451487</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="66994a85-5204-49af-8e76-9279e3c3ebb8"><ac:parameter ac:name="id">581451486</ac:parameter><ac:rich-text-body><p>When elements have an internal structure, the <ac:link><ri:page ri:content-title="(2026x) Displaying rake icon" /><ac:plain-text-link-body><![CDATA[rake icon]]></ac:plain-text-link-body></ac:link> appears on the element shape. If those elements belong to an aspect diagram, the rake icon navigates to the same aspect internal structure of the selected element. If there is no internal diagram of the same aspect, then any diagram of another aspect or diagram without aspect is opened.</p><p>The figure below demonstrates the <em>electrical</em> Internal Block diagram of the <em>Climate Control Hardware</em>. The rake icon on the part typed by <em>Control System</em> Block indicates that it contains an inner structure. There are four Internal Block diagrams for the <em>Control System</em> in the model<em>.</em> Although, after double-clicking on that part shape typed by <em>Control System</em> Block, the rake icon navigates exactly to the <em>electrical</em> Internal Block diagram of the <em>Control System.</em></p><p><ac:image ac:align="center"><ri:attachment ri:filename="rake_icon_in_aspect_diagram.png"><ri:page ri:content-title="(2026x) Navigation among aspect diagrams" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The navigation among aspect diagrams via rake icon. The illustration displays concepts from SysML v1 Plugin.</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="76a9bdeb-a3e3-4f77-87c9-74f630e9f4ad"><ac:parameter ac:name="id">581451484</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Sample model</strong></p><p>The model used in the figures of this page is the <strong>Diagram aspects</strong> sample model:</p><ul><li><span class="confluence-link"><span style="color:var(--ds-text,#333333);"><span class="confluence-link"><span style="color:var(--ds-text,#333333);">Download <ac:link><ri:attachment ri:filename="diagram aspects.mdzip"><ri:page ri:content-title="(2026x) Sample models" /></ri:attachment></ac:link>. </span></span></span></span></li><li><span class="confluence-link"><span style="color:var(--ds-text,#333333);"><span class="confluence-link">Find in the modeling tool: <em><span style="color:var(--ds-text,#333333);">&lt;modeling tool installation directory&gt;\<span style="color:var(--ds-text,#333333);">samples\SysML v1</span><span style="color:var(--ds-text,#333333);">\<span style="color:var(--ds-text,#333333);">diagram aspects</span>.mdzip.</span></span></em></span></span></span><span class="confluence-link"><span style="color:var(--ds-text,#333333);"><span class="confluence-link"><span style="color:var(--ds-text,#333333);"><br /></span></span></span></span></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272739223 space=MT version=2 -->
## PAGE 03522: (2026x) Navigation Between BPMN Diagrams

- page_id: `272739223`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272739223/2026x+Navigation+Between+BPMN+Diagrams
- version_number: 2
- version_date: `2025-11-25T14:47:09.256+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Using Cameo Business Modeler Plugin > (2026x) Using BPMN Process Diagram
- labels: ['msosa']

### NORMALIZED CONTENT

You can navigate to

- higher level BPMN diagrams
- related Process diagrams

To navigate to a higher level BPMN diagrams

- At the bottom left corner of the diagram pane, on the toolbar, click the [ATTACHMENT filename='up_button.png'] button and select higher level BPMN diagram.

To navigate to a related Process diagrams

- At the bottom left corner of the diagram pane, on the toolbar, click the [ATTACHMENT filename='related.png'] button and select related process diagram.

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Creating diagrams' space='']
- Creating and Using Tasks
- Creating and Using SubProcesses
- Using Activities
- [CONFLUENCE_PAGE title='(2026x) Creating and Using a BPMN Event' space='']
- Creating and Using a Sequence Flow
- Creating and Using Data Items

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>You can navigate to</p><ul><li data-uuid="32d24341-8b46-44dd-80a5-a6784e426224">higher level BPMN diagrams</li><li data-uuid="cba14dc8-2a8b-4e6e-93e1-606aeac3c847">related Process diagrams</li></ul><p>To navigate to a higher level BPMN diagrams</p><hr /><ul><li data-uuid="cd0a0fb8-600b-4466-8218-051cd24a36bd">At the bottom left corner of the diagram pane, on the toolbar, click the <ac:image><ri:attachment ri:filename="up_button.png"><ri:page ri:content-title="(2026x) Navigation Between BPMN Diagrams" /></ri:attachment></ac:image> button and select higher level BPMN diagram.</li></ul><p><br /></p><p>To navigate to a related Process diagrams</p><hr /><ul><li data-uuid="e4f843bb-9408-4541-a6c2-29779adf443b">At the bottom left corner of the diagram pane, on the toolbar, click the <ac:image><ri:attachment ri:filename="related.png"><ri:page ri:content-title="(2026x) Navigation Between BPMN Diagrams" /></ri:attachment></ac:image>button and select related process diagram.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related diagrams</strong></p><ul><li data-uuid="5f848fff-d001-42e2-8e92-4586ee5ccffc"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Process+Diagram">BPMN Process Diagram</a></li><li data-uuid="8e5cb7a5-5b31-4a71-bd5f-02d472a50f70"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li data-uuid="80ab7886-6f19-4e9c-96dd-a3ef297519c0"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li data-uuid="469406cc-ea15-4679-abbc-b3a7771d2f45"><ac:link><ri:page ri:content-title="(2026x) Creating diagrams" /><ac:plain-text-link-body><![CDATA[Creating a Diagram]]></ac:plain-text-link-body></ac:link></li><li data-uuid="14117a4d-37d4-42ef-bc44-3a0e71671266"><a href="https://docs.nomagic.com/display/MT/(2026x) Creating+and+Using+Tasks">Creating and Using Tasks</a></li><li data-uuid="91a5c9c9-ba3c-4233-907b-4925227e0a21"><a href="https://docs.nomagic.com/display/MT/(2026x) Creating+and+Using+SubProcesses">Creating and Using SubProcesses</a></li><li data-uuid="628382a9-127d-499d-ae25-4fb9afe0874a"><a href="https://docs.nomagic.com/display/MT/(2026x) Using+Activities">Using Activities</a></li><li data-uuid="4aab2ced-2002-49ef-9415-b3529e096aaf"><ac:link><ri:page ri:content-title="(2026x) Creating and Using a BPMN Event" /><ac:plain-text-link-body><![CDATA[Creating and Using an Event]]></ac:plain-text-link-body></ac:link></li><li data-uuid="45d1cb4d-ea77-49be-9c95-1788143de075"><a href="https://docs.nomagic.com/display/MT/(2026x) Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li><li data-uuid="d6febadf-52ec-4164-a8ca-c6a0ffddb158"><a href="https://docs.nomagic.com/display/MT/(2026x) Creating+and+Using+Data+Items">Creating and Using Data Items</a></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272736421 space=MT version=1 -->
## PAGE 03523: (2026x) Navigation from cell

- page_id: `272736421`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272736421/2026x+Navigation+from+cell
- version_number: 1
- version_date: `2025-11-25T13:47:17.114+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Diagrams > (2026x) Analysis diagrams > (2026x) Dependency Matrix > (2026x) Using Dependency Matrix
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

To select a relationship in the [CONFLUENCE_PAGE title='(2026x) Containment tab' space='']

1. Right-click the cell. The shortcut menu opens.
2. On the shortcut menu, under **Navigate**, select the relationship. The relationship is highlighted in the Containment Tree. 
[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To select a relationship in the <ac:link><ri:page ri:content-title="(2026x) Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link></p><hr /><ol><li>Right-click the cell. The shortcut menu opens.</li><li><p>On the shortcut menu, under <strong>Navigate</strong>, select the relationship. The relationship is highlighted in the Containment Tree.<br /><ac:image><ri:attachment ri:filename="Dep_matrix_select_in_Cont_tree.png"><ri:page ri:content-title="(2026x) Navigation from cell" /></ri:attachment></ac:image></p></li></ol><p> </p>
````

<!--NOMAGIC_PAGE id=272730194 space=MT version=1 -->
## PAGE 03524: (2026x) Navigation to layout templates

- page_id: `272730194`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730194/2026x+Navigation+to+layout+templates
- version_number: 1
- version_date: `2025-11-25T13:36:38.652+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Diagramming > (2026x) Layout templates
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

You can navigate from the layout template usage to definition by using the Open Template command. This command provides different options in the following situations:

- Open Template without drop-down arrow appears when only one layout template is available for the selected element.
- Open Template with drop-down arrow appears when multiple layout templates are available for the selected element. The multiple layout templates are listed according to the following rules:
  - If you set the default layout template, it is always the first in the list, and other templates are listed alphabetically. [CONFLUENCE_PAGE title='(2026x) Setting layout template as default' space='']
  - If you haven't set the default layout template, all layout templates are listed alphabetically.

To open the layout template diagram

- Right click the Part Property or Class shape and select Display > Layout Template > **Open Template**. Then select the name of the desired layout template if more than one template is available.
- Select the Part Property or Class shape, click [ATTACHMENT filename='display_icon.png'] , and select Layout Template > Open Template . Then select the name of the desired layout template if more than one template is available.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can navigate from the layout template usage to definition by using the Open Template command. This command provides different options in the following situations:</p><ul><li><strong>Open Template</strong> without drop-down arrow appears when only one layout template is available for the selected element.</li><li><strong>Open Template</strong> with drop-down arrow appears when multiple layout templates are available for the selected element. The multiple layout templates are listed according to the following rules:<ul><li>If you set the default layout template, it is always the first in the list, and other templates are listed alphabetically. <span class="confluence-link"><ac:link><ri:page ri:content-title="(2026x) Setting layout template as default" /><ac:plain-text-link-body><![CDATA[Click to learn how to set the default layout template.]]></ac:plain-text-link-body></ac:link></span></li><li>If you haven't set the default layout template, all layout templates are listed alphabetically.</li></ul></li></ul><p><br /></p><p>To open the layout template diagram</p><hr /><ul><li>Right click the Part Property or Class shape and select <strong>Display</strong> &gt; <strong>Layout Template</strong> &gt;<span><strong> Open Template</strong>. <span style="color: rgb(62,63,64);">Then select the name of the desired layout template if more than one template is available.</span></span></li><li>Select the Part Property or Class shape, click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="display_icon.png"><ri:page ri:content-title="_buttons" /></ri:attachment></ac:image>, and select <strong>Layout Template</strong> &gt; <strong>Open Template</strong>. <span style="color: rgb(62,63,64);">Then select the name of the desired layout template if more than one template is available.</span></li></ul>
````

<!--NOMAGIC_PAGE id=272731291 space=MT version=1 -->
## PAGE 03525: (2026x) NCV-1 Capability Vision

- page_id: `272731291`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731291/2026x+NCV-1+Capability+Vision
- version_number: 1
- version_date: `2025-11-25T13:38:41.895+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Capability Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

668348773

668348776

668348775

**Description**

NCV-1 addresses the enterprise concerns associated with the overall vision for transformational endeavors and thus defines the strategic context for a group of Enterprise capabilities. The purpose of an NCV-1 is to provide a strategic context for the capabilities described in the Architecture. It also provides a high-level scope for the Architecture that is more general than the scenario-based scope defined in an NOV-1. The Views are high-level and describe capabilities using terminology that is easily understood by non-technical readers (though they may make extensive use of military terminology and acronyms that are clearly defined in the NAV-2 View). It should be noted that visions for capabilities of the enterprise should therefore be placed within entities stereotyped as «EnterpriseVision».

**Implementation**

NCV-1 can be represented using a NCV-1 diagram which is based on the UML Class diagram.

**Sample**

**[IMAGE alt='' src='']**

###### NCV-1 Capability Vision

668348772

**Related elements**

- [CONFLUENCE_PAGE title='Enterprise Goal' space='MED']
- [CONFLUENCE_PAGE title='Enterprise Vision' space='MED']
- [CONFLUENCE_PAGE title='Strategic Phase' space='MED']
- [CONFLUENCE_PAGE title='Whole Life Enterprise' space='MED']
- [CONFLUENCE_PAGE title='Structural Part' space='MED']
- [CONFLUENCE_PAGE title='Temporal Part' space='MED']
- [CONFLUENCE_PAGE title='Capability' space='MED']
- [CONFLUENCE_PAGE title='Exhibits' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5e1a0e0b-f3e9-47f1-8afe-6f128f47461e"><ac:parameter ac:name="id">668348773</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="457a7d16-dcc6-4edd-89bf-049d628eb6ab"><ac:parameter ac:name="id">668348776</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1a78e1ef-e52d-4b23-a25e-5023945689dd"><ac:parameter ac:name="id">668348775</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>NCV-1 addresses the enterprise concerns associated with the overall vision for transformational endeavors and thus defines the strategic context for a group of Enterprise capabilities. The purpose of an NCV-1 is to provide a strategic context for the capabilities described in the Architecture. It also provides a high-level scope for the Architecture that is more general than the scenario-based scope defined in an NOV-1. The Views are high-level and describe capabilities using terminology that is easily understood by non-technical readers (though they may make extensive use of military terminology and acronyms that are clearly defined in the NAV-2 View). It should be noted that visions for capabilities of the enterprise should therefore be placed within entities stereotyped as «EnterpriseVision».</p><p><strong>Implementation</strong></p><p>NCV-1 can be represented using a NCV-1 diagram which is based on the UML Class diagram.</p><p><strong>Sample</strong></p><p><strong><ac:image><ri:attachment ri:filename="Ncv_1.jpg"><ri:page ri:content-title="(2026x) NCV-1 Capability Vision" /></ri:attachment></ac:image></strong></p><h6>NCV-1 Capability Vision</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="721d2279-c712-4611-9be6-b44b8a824a48"><ac:parameter ac:name="id">668348772</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Enterprise Goal" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Enterprise Vision" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Strategic Phase" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Whole Life Enterprise" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Structural Part" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Temporal Part" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Exhibits" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f2551271-64cc-4985-bd6f-045a1ba10e3a" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731286 space=MT version=1 -->
## PAGE 03526: (2026x) NCV-2 Capability Taxonomy

- page_id: `272731286`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731286/2026x+NCV-2+Capability+Taxonomy
- version_number: 1
- version_date: `2025-11-25T13:38:41.432+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Capability Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

671106146

671106149

671106147

**Description**

The NCV-2 Product models capability taxonomies. The view presents a hierarchy of capabilities. These capabilities may be presented in context of an Enterprise Phase, for example, it can show the required capabilities for current and future enterprises.

**Implementation**

NCV-2 can be represented using a NCV-2 diagram which is based on the UML Class diagram.

If your project has migrated from any earlier than 17.0.1 version, the oldNCV-5 View representation based on the UML Class diagram is loaded as the NCV-2 Capability Taxonomy diagram.

**Sample**

[IMAGE alt='' src='']

###### NCV-2 Capability Taxonomy

671106145

**Related elements**

- [CONFLUENCE_PAGE title='Capability' space='MED']
- [CONFLUENCE_PAGE title='Exhibits' space='MED']
- [CONFLUENCE_PAGE title='Environment' space='MED']
- [CONFLUENCE_PAGE title='Environment Property' space='MED']
- [CONFLUENCE_PAGE title='Location' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="6f15bad5-c853-4b32-8577-ca061bf7b3bd"><ac:parameter ac:name="id">671106146</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="9f1cb965-4bc3-4455-bb2e-e2f611f106c6"><ac:parameter ac:name="id">671106149</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4e194535-221f-430a-8893-470a0984987c"><ac:parameter ac:name="id">671106147</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NCV-2 Product models capability taxonomies. The view presents a hierarchy of capabilities. These capabilities may be presented in context of an Enterprise Phase, for example, it can show the required capabilities for current and future enterprises.</p><p><strong>Implementation</strong></p><p>NCV-2 can be represented using a NCV-2 diagram which is based on the UML Class diagram.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="97649483-0ef9-4a78-8af1-23c3eeddb245"><ac:rich-text-body>If your project has migrated from any earlier than 17.0.1 version, the oldNCV-5 View representation based on the UML Class diagram is loaded as the NCV-2 Capability Taxonomy diagram.</ac:rich-text-body></ac:structured-macro><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Ncv_2.jpg"><ri:page ri:content-title="(2026x) NCV-2 Capability Taxonomy" /></ri:attachment></ac:image></p><h6>NCV-2 Capability Taxonomy</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="fa196828-15fb-412a-a52a-3cea0f43d755"><ac:parameter ac:name="id">671106145</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Exhibits" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Environment" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Environment Property" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Location" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="de776430-8e70-46d3-8532-b781b0dad9be" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731296 space=MT version=1 -->
## PAGE 03527: (2026x) NCV-3 Capability Phasing

- page_id: `272731296`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731296/2026x+NCV-3+Capability+Phasing
- version_number: 1
- version_date: `2025-11-25T13:38:42.449+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Capability Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

671392471

671392474

671392473

**Description**

NCV-3 addresses the planned achievement of capability at different points in time or during specific periods of time, i.e. capability phasing. NCV-3 Views support the Capability Audit process by providing a method to identify gaps or duplication in capability provision. The view indicates capability increments, which should be associated with delivery milestones within acquisition projects (when the increments are associated with capability deliveries).

**Implementation**

NCV-3 can be represented using a NCV-3 diagram which is realized as a time based diagram.

**Sample**

**[IMAGE alt='' src='']**

###### NCV-3 Capability Phasing

To increase the diagram readability, use legends. To learn how to use legends, see [CONFLUENCE_PAGE title='(2026x) Legends' space=''] chapter.

****

**Related views**

The View is created by analyzing programmatic project data to determine when the projects providing elements of military capability are to be delivered, upgraded and/or withdrawn (this data may be provided in part by a Programme Timelines (NPV-2) View). Then the capability increments identified are structured according to the required capabilities determined in the Capability Taxonomy (NCV-2) View and the Enterprise Phases (from NCV1).

671392470

**Related elements**

- [CONFLUENCE_PAGE title='Capability' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Exhibits' space='MED']
- [CONFLUENCE_PAGE title='Actual Project Milestone' space='MED']
- [CONFLUENCE_PAGE title='Actual Project' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Customizing Gantt chart properties' space='']
- [CONFLUENCE_PAGE title='(2026x) Legends' space='']
- [CONFLUENCE_PAGE title='(2026x) Filtering table data' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3b42c37e-ea92-4a7f-82c6-505092ecd97a"><ac:parameter ac:name="id">671392471</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d417a569-a726-40ed-b945-f42729eb4a20"><ac:parameter ac:name="id">671392474</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f20d8f82-8074-4eb8-9861-4710e8f4672e"><ac:parameter ac:name="id">671392473</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>NCV-3 addresses the planned achievement of capability at different points in time or during specific periods of time, i.e. capability phasing. NCV-3 Views support the Capability Audit process by providing a method to identify gaps or duplication in capability provision. The view indicates capability increments, which should be associated with delivery milestones within acquisition projects (when the increments are associated with capability deliveries).</p><p><strong>Implementation</strong></p><p>NCV-3 can be represented using a NCV-3 diagram which is realized as a time based diagram.</p><p><strong>Sample</strong></p><p><strong><ac:image><ri:attachment ri:filename="Ncv_3.png"><ri:page ri:content-title="(2026x) NCV-3 Capability Phasing" /></ri:attachment></ac:image></strong></p><h6>NCV-3 Capability Phasing</h6><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="75afd5de-6ef8-4057-9de7-b210546f3adf"><ac:rich-text-body><p>To increase the diagram readability, use legends. To learn how to use legends, see <ac:link><ri:page ri:content-title="(2026x) Legends" /></ac:link> chapter.</p></ac:rich-text-body></ac:structured-macro><p><strong><br /></strong></p><p><strong>Related views</strong></p><p>The View is created by analyzing programmatic project data to determine when the projects providing elements of military capability are to be delivered, upgraded and/or withdrawn (this data may be provided in part by a Programme Timelines (NPV-2) View). Then the capability increments identified are structured according to the required capabilities determined in the Capability Taxonomy (NCV-2) View and the Enterprise Phases (from NCV1).</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f6d0c899-8697-4023-a0f8-35e1a5ab1155"><ac:parameter ac:name="id">671392470</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Exhibits" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Project Milestone" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Project" /></ac:link></li></ul><p><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="c341881f-7f45-4f7c-a0da-d9bde5f6d9ac" /></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Customizing Gantt chart properties" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Legends" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Filtering table data" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731311 space=MT version=1 -->
## PAGE 03528: (2026x) NCV-4 Capability Dependencies

- page_id: `272731311`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731311/2026x+NCV-4+Capability+Dependencies
- version_number: 1
- version_date: `2025-11-25T13:38:44.856+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Capability Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

671535912

671535914

671535913

**Description**

The NCV-4 Product describes the dependencies between planned capabilities. It also defines logical groupings of capabilities (capability clusters). The NCV-4 View provides a means of analyzing the dependencies between capabilities. The groupings of capabilities are logical, and the purpose of the groupings is to guide enterprise management.

**Implementation**

NCV-4 can be represented using a NCV-4 diagram which is based on the UML Class diagram.

**Sample**

[IMAGE alt='' src='']

###### NCV-4 Capability Dependencies

**Related views**

The Capability Dependencies (NCV-4) View describes the relationships between capabilities (capabilities may be reused from an NCV-2). It also defines logical groupings of capabilities. This contrasts with the NCV-2 which also deals with relationships between Capabilities, but the NCV-2 only addresses the specialization-generalization relationship (for example, capability taxonomy).

671535911

**Related elements**

- [CONFLUENCE_PAGE title='Capability' space='MED']
- [CONFLUENCE_PAGE title='Capability Role' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="189f9572-edbc-4710-8500-f33a50248016"><ac:parameter ac:name="id">671535912</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fd3663f3-7c48-4993-a0fa-7a0707a7a4dd"><ac:parameter ac:name="id">671535914</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="51f780b1-86bf-4f06-9fd0-dc8894d973fd"><ac:parameter ac:name="id">671535913</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NCV-4 Product describes the dependencies between planned capabilities. It also defines logical groupings of capabilities (capability clusters). The NCV-4 View provides a means of analyzing the dependencies between capabilities. The groupings of capabilities are logical, and the purpose of the groupings is to guide enterprise management.</p><p><strong>Implementation</strong></p><p>NCV-4 can be represented using a NCV-4 diagram which is based on the UML Class diagram.</p><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Ncv_4.png"><ri:page ri:content-title="(2026x) NCV-4 Capability Dependencies" /></ri:attachment></ac:image></p><h6>NCV-4 Capability Dependencies</h6><p><strong>Related views</strong></p><p>The Capability Dependencies (NCV-4) View describes the relationships between capabilities (capabilities may be reused from an NCV-2). It also defines logical groupings of capabilities. This contrasts with the NCV-2 which also deals with relationships between Capabilities, but the NCV-2 only addresses the specialization-generalization relationship (for example, capability taxonomy).</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="07167bb4-3be9-40f4-a753-d19861819709"><ac:parameter ac:name="id">671535911</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Role" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="8e67c2d5-95ad-4da0-a381-b72a0e87f9c3" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731416 space=MT version=1 -->
## PAGE 03529: (2026x) NCV-5 Capability to Organisational Deployment Mapping

- page_id: `272731416`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731416/2026x+NCV-5+Capability+to+Organisational+Deployment+Mapping
- version_number: 1
- version_date: `2025-11-25T13:38:53.260+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Capability Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

674073284

674073286

674073285

**Description**

The NCV-5 defines Capability to Organisational Deployment Mapping. It addresses the fulfillment of capability requirements, in particular by network enabled capabilities. The NCV-5 View is used to support the capability management process and, in particular, assist the planning of fielding.

**Implementation**

NCV-5 can be represented using:

- NCV-5 table. If your project has migrated from any earlier than 17.0.1 version, theold NCV-5 View representation based on the UML Class diagram is loaded as the NCV-2 Capability Taxonomy diagram.
- NCV-5 spreadsheet report.

**Sample**

[IMAGE alt='' src='']

###### NCV-5 Capability to Organization Deployment Mapping

| Icon | View | Relationship |
| --- | --- | --- |
|  |  | Capability Phasing is defined in NCV-1. |
|  |  | Capabilities shown in NCV-5 table are usually modeled in NCV-2 Capability Taxonomy. |
|  |  | The timing is based on project milestones from NPV1 which indicate when capability configuration will be delivered to an organization. |
|  |  | Actual Organizational Resources related to deployment of Capability Configurations are taken from NOV-4 Organizational Relationships Chart. |

674073283

**Related elements**

- [CONFLUENCE_PAGE title='Capability' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Exhibits' space='MED']
- [CONFLUENCE_PAGE title='Actual Organization' space='MED']
- [CONFLUENCE_PAGE title='Actual Post' space='MED']
- [CONFLUENCE_PAGE title='Actual Project Milestone' space='MED']
- [CONFLUENCE_PAGE title='Actual Project' space='MED']
- [CONFLUENCE_PAGE title='Strategic Phase' space='MED']
- [CONFLUENCE_PAGE title='Whole Life Enterprise' space='MED']

**Related procedures**

**Related references**

- [CONFLUENCE_PAGE title='(2026x) Actual Resources Deployment Wizard' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d9b340e9-fa58-4354-ab17-72b0e6830ae8"><ac:parameter ac:name="id">674073284</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="10d4e47e-d190-4c0a-8312-82389fb10709"><ac:parameter ac:name="id">674073286</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b2715916-ad66-4176-b861-2cfe5899af26"><ac:parameter ac:name="id">674073285</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NCV-5 defines Capability to Organisational Deployment Mapping. It addresses the fulfillment of capability requirements, in particular by network enabled capabilities. The NCV-5 View is used to support the capability management process and, in particular, assist the planning of fielding.</p><p><strong>Implementation</strong></p><p>NCV-5 can be represented using:</p><ul><li><p class="auto-cursor-target">NCV-5 table.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ab3c067f-8118-4505-b5e2-d52fe6e564f5"><ac:rich-text-body>If your project has migrated from any earlier than 17.0.1 version, theold NCV-5 View representation based on the UML Class diagram is loaded as the NCV-2 Capability Taxonomy diagram.</ac:rich-text-body></ac:structured-macro></li><li>NCV-5 spreadsheet report.</li></ul><p class="auto-cursor-target"><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Ncv_5.png"><ri:page ri:content-title="(2026x) NCV-5 Capability to Organisational Deployment Mapping" /></ri:attachment></ac:image></p><h6>NCV-5 Capability to Organization Deployment Mapping</h6><table class="wrapped"><colgroup><col /><col /><col /></colgroup><tbody><tr><th>Icon</th><th>View</th><th>Relationship</th></tr><tr><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="59"><ri:attachment ri:filename="Nvc_1_icon.png"><ri:page ri:content-title="(2026x) NCV-5 Capability to Organisational Deployment Mapping" /></ri:attachment></ac:image></p></div></td><td><ac:link><ri:page ri:content-title="(2026x) NCV-1 Capability Vision" /></ac:link></td><td><p>Capability Phasing is defined in NCV-1.</p></td></tr><tr><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="59"><ri:attachment ri:filename="Nvc_2_icon.png"><ri:page ri:content-title="(2026x) NCV-5 Capability to Organisational Deployment Mapping" /></ri:attachment></ac:image></p></div></td><td><ac:link><ri:page ri:content-title="(2026x) NCV-2 Capability Taxonomy" /></ac:link></td><td><p>Capabilities shown in NCV-5 table are usually modeled in NCV-2 Capability Taxonomy.</p></td></tr><tr><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="58"><ri:attachment ri:filename="Npv_1_icon.png"><ri:page ri:content-title="(2026x) NCV-5 Capability to Organisational Deployment Mapping" /></ri:attachment></ac:image></p></div></td><td><ac:link><ri:page ri:content-title="(2026x) NPV-2 Programme to Capability Mapping" /></ac:link></td><td><p>The timing is based on project milestones from NPV1 which indicate when capability configuration will be delivered to an organization.</p></td></tr><tr><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="50"><ri:attachment ri:filename="Nov_4_icon.png"><ri:page ri:content-title="(2026x) NCV-5 Capability to Organisational Deployment Mapping" /></ri:attachment></ac:image></p></div></td><td><ac:link><ri:page ri:content-title="(2026x) NOV-4 Organizational Relationships Chart" /></ac:link></td><td><p>Actual Organizational Resources related to deployment of Capability Configurations are taken from NOV-4 Organizational Relationships Chart.</p></td></tr></tbody></table></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="15ef9eb8-e6c8-4d3e-80f0-cbee33825132"><ac:parameter ac:name="id">674073283</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Exhibits" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Project Milestone" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Project" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Strategic Phase" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Whole Life Enterprise" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="94ccb724-2b27-4c16-a438-11f14383eda6" /></p><p><br /><strong>Related references</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Actual Resources Deployment Wizard" /><ac:plain-text-link-body><![CDATA[Deployment Milestones Wizard]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731411 space=MT version=1 -->
## PAGE 03530: (2026x) NCV-6 Capability to Operational Activity Mapping

- page_id: `272731411`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731411/2026x+NCV-6+Capability+to+Operational+Activity+Mapping
- version_number: 1
- version_date: `2025-11-25T13:38:52.689+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Capability Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

675545526

675545529

675545527

**Description**

The NCV-6 Product describes the mapping between the capabilities required by an Enterprise and the operational activities that those capabilities support.

**Implementation**

NCV-6 can be represented using a NCV-6 diagram which is an editable Dependency Matrix. The Capabilities will be used as row elements and the Operational Activities will be used as column elements.

**Sample**

[IMAGE alt='' src='']

###### NCV-6 Capability to Operational Activity Mapping

**Related views**

The NCV-6 View provides a bridge between capability analyses using NCVs and operational activities analyzed using NOVs. Specifically, it identifies how operational activities can be performed using various available capability elements. It is similar in function to the NSV-5 which maps system functions to operational activities.

675545525

**Related elements**

- [CONFLUENCE_PAGE title='Capability' space='MED']
- [CONFLUENCE_PAGE title='Standard Operational Activity' space='MED']
- [CONFLUENCE_PAGE title='Maps To Capability' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Using Implied Relations' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="08988305-b883-4843-9005-65390333cae6"><ac:parameter ac:name="id">675545526</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="f0ee0e5c-853e-416a-bdd9-6782cd1c222e"><ac:parameter ac:name="id">675545529</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="04c10fa5-f4bf-47a2-a33f-767b2d1fb502"><ac:parameter ac:name="id">675545527</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NCV-6 Product describes the mapping between the capabilities required by an Enterprise and the operational activities that those capabilities support.</p><p><strong>Implementation</strong></p><p>NCV-6 can be represented using a NCV-6 diagram which is an editable Dependency Matrix. The Capabilities will be used as row elements and the Operational Activities will be used as column elements.</p><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nvc_6.png"><ri:page ri:content-title="(2026x) NCV-6 Capability to Operational Activity Mapping" /></ri:attachment></ac:image></p><h6>NCV-6 Capability to Operational Activity Mapping</h6><p><strong>Related views</strong></p><p>The NCV-6 View provides a bridge between capability analyses using NCVs and operational activities analyzed using NOVs. Specifically, it identifies how operational activities can be performed using various available capability elements. It is similar in function to the NSV-5 which maps system functions to operational activities.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="28328109-be03-4646-a5cc-b3769a167536"><ac:parameter ac:name="id">675545525</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Standard Operational Activity" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Maps To Capability" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d4e422d9-c16b-425d-a2db-5d5505d24fc6" /></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Using Implied Relations" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731435 space=MT version=1 -->
## PAGE 03531: (2026x) NCV-7 Capability to Service Mapping

- page_id: `272731435`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731435/2026x+NCV-7+Capability+to+Service+Mapping
- version_number: 1
- version_date: `2025-11-25T13:38:55.998+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Capability Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

675844727

**Description**

The NCV-7 Product describes the mapping between the capabilities required by an Enterprise and services as defined for SOA.

**Implementation**

NCV-7 can be represented using a NCV-6 diagram which is an editable Dependency Matrix. The Service Interfaces will be used as the row elements and the Capabilities will be used as the column elements.

**Sample**

[IMAGE alt='' src='']

###### NCV-7 Capability to Service Mapping

**Related elements**

- [CONFLUENCE_PAGE title='Service Interface' space='MED']
- [CONFLUENCE_PAGE title='Capability' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Using Implied Relations' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3d1d2c0c-338f-43b8-b6c3-f52ed57d9ae7"><ac:parameter ac:name="id">675844727</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NCV-7 Product describes the mapping between the capabilities required by an Enterprise and services as defined for SOA.</p><p><strong>Implementation</strong></p><p>NCV-7 can be represented using a NCV-6 diagram which is an editable Dependency Matrix. The Service Interfaces will be used as the row elements and the Capabilities will be used as the column elements.</p><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Ncv_7.png"><ri:page ri:content-title="(2026x) NCV-7 Capability to Service Mapping" /></ri:attachment></ac:image></p><h6>NCV-7 Capability to Service Mapping</h6></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related elements</strong></p><ul><li data-uuid="c67dca19-9622-4ec2-9389-e7bec8b6d489"><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Interface" /></ac:link></li><li data-uuid="b3b55a39-3368-43c0-81ac-8310fa6ff3d9"><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="86c97888-c8d1-4494-a92e-4e1d0280a6be" /></p><ul><li data-uuid="ed938b50-8400-423e-aeac-7b80b67f4b9a"><ac:link><ri:page ri:content-title="(2026x) Using Implied Relations" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272733051 space=MT version=2 -->
## PAGE 03532: (2026x) Nested properties export to the Modelica file

- page_id: `272733051`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733051/2026x+Nested+properties+export+to+the+Modelica+file
- version_number: 2
- version_date: `2025-11-25T14:42:01.492+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) SysML v1 modeling > (2026x) Exporting to External Simulation Models > (2026x) Modelica export > (2026x) Advanced Modelica features
- labels: ['mcse', 'msosa']

### NORMALIZED CONTENT

When using a [CONFLUENCE_PAGE title='(2026x) Partial model export to the Modelica file' space=''], the nested properties can also be exported to the Modelica file.Nested properties are exported in the following rules:

- If nested properties are not displayed (Structure [CONFLUENCE_PAGE title='(2026x) SysML v1 specific compartments' space=''] is disabled), all of them are exported. For example, see the figure below where the vaporGenerationPlant Part Property contains four nested parts (Heating, Evaporation, Radiation, VaporGenerationPlantCalculation) that are exported to the Modelica file. 
[IMAGE alt='' src='']
- If any of the nested elements are displayed (Structure [CONFLUENCE_PAGE title='(2026x) SysML v1 specific compartments' space=''] is enabled), only they are exported, skipping any hidden elements. In the example below, only Heating and Radiation nested parts of the vaporGenerationPlant Part Property are exported to the Modelica file, while any ports and connectors are skipped. [CONFLUENCE_PAGE title='(2026x) Displaying parts and ports in SysML v1' space='']>]]> [IMAGE alt='' src='']

To export nested properties, use the procedure described in the [Partial model export to the Modelica file](https://docs.nomagic.com/display/MT/(2026x) Partial+model+export+to+the+Modelica+file#PartialmodelexporttotheModelicafile-ProcedureofpartialexporttotheModelicafile)page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">When using a <ac:link><ri:page ri:content-title="(2026x) Partial model export to the Modelica file" /><ac:plain-text-link-body><![CDATA[partial model export]]></ac:plain-text-link-body></ac:link>, the nested properties can <span style="color: rgb(62,63,64);">also</span> be exported to the Modelica file. </span><span style="color: rgb(62,63,64);">Nested properties are exported in the following rules:</span></p><ul><li><span style="color: rgb(62,63,64);">If nested properties are not displayed (Structure <ac:link><ri:page ri:content-title="(2026x) SysML v1 specific compartments" /><ac:plain-text-link-body><![CDATA[Compartment]]></ac:plain-text-link-body></ac:link> is disabled), all of them are exported. For example, see the figure below where the vaporGenerationPlant Part Property contains four nested parts (Heating, Evaporation, Radiation, VaporGenerationPlantCalculation) that are exported to the Modelica file.<br /><ac:image><ri:attachment ri:filename="all_nested_parts_exported_to_modelica.png"><ri:page ri:content-title="(2026x) Nested properties export to the Modelica file" /></ri:attachment></ac:image><br /></span></li><li><span style="color: rgb(62,63,64);">If any of the nested elements are displayed (Structure <ac:link><ri:page ri:content-title="(2026x) SysML v1 specific compartments" /><ac:plain-text-link-body><![CDATA[Compartment]]></ac:plain-text-link-body></ac:link> is enabled), only they are exported, skipping any hidden elements. In the example below, only Heating and Radiation nested parts of the vaporGenerationPlant Part Property are exported to the Modelica file, while any ports and connectors are skipped. <ac:link><ri:page ri:content-title="(2026x) Displaying parts and ports in SysML v1" /><ac:plain-text-link-body><![CDATA[Learn how to display parts and ports >>]]></ac:plain-text-link-body></ac:link><br /><br /></span><span style="color: rgb(62,63,64);"><ac:image><ri:attachment ri:filename="displayed_nested_parts_exported_to_modelica.png"><ri:page ri:content-title="(2026x) Nested properties export to the Modelica file" /></ri:attachment></ac:image><br /></span></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3be444d5-e46b-47a1-86ac-86be36356272"><ac:rich-text-body><p>To export nested properties, use the procedure described in the <span style="letter-spacing: 0.0px;"><a href="https://docs.nomagic.com/display/MT/(2026x) Partial+model+export+to+the+Modelica+file#PartialmodelexporttotheModelicafile-ProcedureofpartialexporttotheModelicafile">Partial model export to the Modelica file </a>page.</span></p></ac:rich-text-body></ac:structured-macro><p /><p><br /></p>
````

<!--NOMAGIC_PAGE id=272736969 space=MT version=1 -->
## PAGE 03533: (2026x) Nesting additional elements in a hierarchical table

- page_id: `272736969`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272736969/2026x+Nesting+additional+elements+in+a+hierarchical+table
- version_number: 1
- version_date: `2025-11-25T13:48:10.717+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Diagrams > (2026x) Tables > (2026x) Basic tasks in tables > (2026x) Hierarchy in tables
- labels: ['nested-instances', 'nested-elements', 'add-nested', 'msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

Apart from displaying elements hierarchically, you can also build a hierarchy by nesting additional elements within the selected elementdirectly in the table. The **Complete** tree view is enabled in the table by default.

To build a custom hierarchy

Do one of the following:

- In the table, right-click the specific element to nest an additional element within, select Add Nested in the drop-down menu, and specify the type of the element to create, e.g., Requirement. [ATTACHMENT filename='add_nested_shortcut_menu.png']
- Select the specific table element to nest an additional element within, click the Add Nested button in the table [CONFLUENCE_PAGE title='(2026x) Toolbars' space=''] , and specify the type of the element to create, e.g., Requirement. [ATTACHMENT filename='add_nested_button_in_toolbar.png']

Please note that the **Add Nested** button is available in the table toolbar of the [CONFLUENCE_PAGE title='(2026x) Requirement Table' space=''] only.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:inline-comment-marker ac:ref="1e4c5158-a786-413a-8dc8-7378fcd3da3a">Apart</ac:inline-comment-marker> from displaying elements hierarchically, you can also build a hierarchy by nesting additional elements within the selected <ac:inline-comment-marker ac:ref="1edd7864-7546-43b5-b8c9-299f8ba3bf92">element </ac:inline-comment-marker>directly in the table. The <strong>Complete</strong> tree view is enabled in the table by default. </p><p><br /></p><p>To build a custom hierarchy </p><hr /><p>Do one of the following:</p><ul><li>In the table, right-click the specific element to nest an additional element within, select <strong>Add Nested</strong> in the drop-down menu, and specify the type of the element to create, e.g., Requirement. <br /><ac:image><ri:attachment ri:filename="add_nested_shortcut_menu.png"><ri:page ri:content-title="(2026x) Nesting additional elements in a hierarchical table" /></ri:attachment></ac:image><br /><br /></li><li><span style="color: rgb(62,63,64);">Select the specific table element to nest an additional element within, </span>click the<strong> Add Nested </strong>button in the table <ac:link><ri:page ri:content-title="(2026x) Toolbars" /><ac:plain-text-link-body><![CDATA[toolbar]]></ac:plain-text-link-body></ac:link>, and specify the type of the element to create, e.g., Requirement. <br /><ac:image><ri:attachment ri:filename="add_nested_button_in_toolbar.png"><ri:page ri:content-title="(2026x) Nesting additional elements in a hierarchical table" /></ri:attachment></ac:image><br /><br /></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="36407ace-3c7c-486b-ba5e-e0e2ee3c5eb8"><ac:rich-text-body><p>Please note that the <strong>Add Nested</strong> button is available in the table toolbar of the <ac:link><ri:page ri:content-title="(2026x) Requirement Table" /><ac:plain-text-link-body><![CDATA[Requirement table]]></ac:plain-text-link-body></ac:link> only.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=272732990 space=MT version=1 -->
## PAGE 03534: (2026x) Nesting image shapes

- page_id: `272732990`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732990/2026x+Nesting+image+shapes
- version_number: 1
- version_date: `2025-11-25T13:41:40.209+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Diagramming
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

570155581

570155583

570155582

You can now drag an image to any element in a diagram as a nested element.

To drag an image to an element

1. Select an image in the diagram pane.
2. Drag it to the image shape.

Dragged images will be nested by the following elements: Package, Model, Subsystem, Instance, Node, Part, Combined Fragment, Composite State (State diagram), Interruptible Activity Region, Structured Activity Node, Expansion Region, and Conditional Node (Activity diagram).

[IMAGE alt='' src='']

570155579

**Related pages**

- [CONFLUENCE_PAGE title='(2026x) Diagramming' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="66b43a9a-d477-41c4-ab7d-c6ca79b25ade"><ac:parameter ac:name="id">570155581</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="7a839c52-98b6-4bd5-bd7d-0bf5352b7972"><ac:parameter ac:name="id">570155583</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="de0093b4-f14a-436d-86a1-36bec4b43ebe"><ac:parameter ac:name="id">570155582</ac:parameter><ac:rich-text-body><p>You can now drag an image to any element in a diagram as a nested element.</p><p><br /></p><p>To drag an image to an element</p><hr /><ol><li>Select an image in the diagram pane.</li><li>Drag it to the image shape.</li></ol><p><br /></p><p>Dragged images will be nested by the following elements: Package, Model, Subsystem, Instance, Node, Part, Combined Fragment, Composite State (State diagram), Interruptible Activity Region, Structured Activity Node, Expansion Region, and Conditional Node (Activity diagram).</p><p><ac:image ac:title="Examples of Images Nested to the Products Package and Server Component" ac:alt="Examples of Images Nested to the Products Package and Server Component"><ri:attachment ri:filename="nesting_image.png"><ri:page ri:content-title="(2026x) Nesting image shapes" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="07e86cb4-2c0c-4e38-bbfa-17098f556409"><ac:parameter ac:name="id">570155579</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Diagramming" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732728 space=MT version=1 -->
## PAGE 03535: (2026x) Nesting parts that are association ends

- page_id: `272732728`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732728/2026x+Nesting+parts+that+are+association+ends
- version_number: 1
- version_date: `2025-11-25T13:41:11.967+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Diagrams > (2026x) UML diagrams > (2026x) Composite Structure diagram
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

In this section you will find the description on how to nest a Part to another Part in the Composite Structure diagram. Until the modeling tool version 17.0.2, nesting of parts was not available if a Part was a property of an [CONFLUENCE_PAGE title='Association' space='MED'], that is, if the Part represented the [CONFLUENCE_PAGE title='Association End' space='MED'].

If a classifier has an association connection with another classifier, the Association End in the classifier is referenced as a property. In a Composite Structure diagram, a Part is representation of a property. So the Part can represent the property that is an Association end too. If the Association End is composite, parts are represented in a nested structure. 
 
 
[IMAGE alt='' src='']

See an example in the preceding figure. In the [CONFLUENCE_PAGE title='(2026x) Class diagram' space=''], the Class *FuelTankAssembly* is connected with the Class *FuelInjector* with the composite Association. In the Composite Structure diagram, the same Association is represented in the following way: the Part with the type *FuelInjector* is nested into the Part with the type *FuelTankAssembly*. By dragging and dropping the Part with *FuelInjector* to the Part with the *CombustionEngine*, changes the Association in the Class diagram - the *FuelInjector* will be connected with the *CombustionEngine*.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>In this section you will find the description on how to nest a Part to another Part in the Composite Structure diagram. Until the modeling tool version 17.0.2, nesting of parts was not available if a Part was a property of an <ac:link><ri:page ri:space-key="MED" ri:content-title="Association" /></ac:link>, that is, if the Part represented the <ac:link><ri:page ri:space-key="MED" ri:content-title="Association End" /></ac:link>.</p><p>If a classifier has an association connection with another classifier, the Association End in the classifier is referenced as a property. In a Composite Structure diagram, a Part is representation of a property. So the Part can represent the property that is an Association end too. If the Association End is composite, parts are represented in a nested structure. <br class="atl-forced-newline" /><br class="atl-forced-newline" /><br class="atl-forced-newline" /><ac:image ac:title="Example of part movement in Composite Structure diagram and results representation in Class diagram" ac:alt="Example of part movement in Composite Structure diagram and results representation in Class diagram"><ri:attachment ri:filename="nested_part.png"><ri:page ri:content-title="(2026x) Nesting parts that are association ends" /></ri:attachment></ac:image><br class="atl-forced-newline" /><br /></p><p>See an example in the preceding figure. In the <ac:link><ri:page ri:content-title="(2026x) Class diagram" /></ac:link>, the Class <em>FuelTankAssembly</em> is connected with the Class <em>FuelInjector</em> with the composite Association. In the Composite Structure diagram, the same Association is represented in the following way: the Part with the type <em>FuelInjector</em> is nested into the Part with the type <em>FuelTankAssembly</em>. By dragging and dropping the Part with <em>FuelInjector</em> to the Part with the <em>CombustionEngine</em>, changes the Association in the Class diagram - the <em>FuelInjector</em> will be connected with the <em>CombustionEngine</em>. <br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><p><br /></p><p style="text-align: center;"><br /></p>
````

<!--NOMAGIC_PAGE id=272738068 space=MT version=1 -->
## PAGE 03536: (2026x) Nesting requirements in the Requirements Table

- page_id: `272738068`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738068/2026x+Nesting+requirements+in+the+Requirements+Table
- version_number: 1
- version_date: `2025-11-25T13:49:33.427+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) SysML v1 modeling > (2026x) Requirements management
- labels: ['mcse', 'msosa']

### NORMALIZED CONTENT

If you want to import nested structure of requirements, you must define the Owner property before the import, with the name or id of the requirement that owns it in the Excel file. When importing a nested structure of requirements from an Excel file you need to map the Owner column (defined in the excel file) with the Owner property. [CONFLUENCE_PAGE title='(2026x) Importing data from Excel and CSV files' space='']>]]>

To nest Requirement

1. Select a Requirement you want to nest in the Requirements Table.
2. Click the Nest button on the table toolbar. The selected Requirement is owned by the requirement in the previous row.

To unnest Requirement

1. Select a Requirement you want to unnest in the Requirements Table.
2. Click the Unnest button on the table toolbar. The selected requirement is owned by the owner of the current one.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="bdc03c90-34b9-4212-b7c8-057e1bb1f1ca"><ac:rich-text-body><p>If you want to import nested structure of requirements, you must define the Owner property before the import, with the name or id of the requirement that owns it in the Excel file. When importing a nested structure of requirements from an Excel file you need to map the Owner column (defined in the excel file) with the Owner property. <ac:link><ri:page ri:content-title="(2026x) Importing data from Excel and CSV files" /><ac:plain-text-link-body><![CDATA[Learn more how to import data from Excel/CSV file >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To nest Requirement</p><hr /><ol><li data-uuid="ef5e7a46-431b-4dba-bf1b-c816250a2900">Select a Requirement you want to nest in the Requirements Table.</li><li data-uuid="6f52a99b-c24d-475b-9491-dca3e56e4adb">Click the <strong>Nest </strong>button on the table toolbar.<br />The selected Requirement is owned by the requirement in the previous row.</li></ol><p><br /></p><p>To unnest Requirement</p><hr /><ol><li data-uuid="bda3da64-a324-4fa5-8d6b-332484b47177">Select a Requirement you want to unnest in the Requirements Table.</li><li data-uuid="25e6bb79-35a6-430b-842c-ccd981211656">Click the <strong>Unnest </strong>button on the table toolbar.<br />The selected requirement is owned by the owner of the current one.</li></ol><p><br /></p>
````

<!--NOMAGIC_PAGE id=272733628 space=MT version=1 -->
## PAGE 03537: (2026x) Networking diagram

- page_id: `272733628`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733628/2026x+Networking+diagram
- version_number: 1
- version_date: `2025-11-25T13:42:38.191+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Diagrams > (2026x) Extension diagrams
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

#### CONTENT-LAYER: Functionality Availability

2453242345

INLINE

#### CONTENT-COLUMN: Functionality Availability

1234634634

INLINE

#### CONTENT-BLOCK: Functionality Availability

342346575

INLINE

#### NOTE: Functionality Availability

Functionality Availability

This feature is available in Standard, Professional, Architect, and Enterprise editions.

The Networking diagram provides a visual display of the network topology. The*Networking Profile*contains[CONFLUENCE_PAGE title='Stereotype' space='MED']for the network description. Elements with icons can be drawn on the diagram pane. The Networking diagram is commonly used to depict hardware nodes as well as the connections between them.

[IMAGE alt='' src='']

###### Example of the Network diagram*System Network*

940934834908

INLINE

**Related Pages:**

- [CONFLUENCE_PAGE title='(2026x) UML diagrams' space='']
- [CONFLUENCE_PAGE title='(2026x) Extension diagrams' space='']
- [CONFLUENCE_PAGE title='(2026x) Diagramming' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3d9e1083-cb60-416d-9802-e5fde45f0277"><ac:parameter ac:name="id">2453242345</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="42c7076c-207a-4460-9683-6d51f47317a0"><ac:parameter ac:name="id">1234634634</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="88a78ad5-2d8e-4e7f-917a-03e320e58fcc"><ac:parameter ac:name="id">342346575</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ce52db42-5307-42b7-bb41-0ae23699d8ad"><ac:parameter ac:name="title">Functionality Availability</ac:parameter><ac:rich-text-body><p><span style="color: rgb(0,0,0);">This feature is available in Standard, Professional, Architect, and Enterprise editions.<br /></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span>The Networking diagram provides a visual display of the network topology. The </span><em>Networking Profile</em><span> contains </span><ac:link><ri:page ri:space-key="MED" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotypes]]></ac:plain-text-link-body></ac:link><span> for the network description. Elements with icons can be drawn on the diagram pane. The Networking diagram is commonly used to depict hardware nodes as well as the connections between them.</span></p><p><span><br /></span></p><p><ac:image ac:align="center" ac:width="600"><ri:attachment ri:filename="Screen Shot 2017-07-13 at 12.06.04 PM.png"><ri:page ri:content-title="(2026x) Networking diagram" /></ri:attachment></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(112,112,112);">Example of the Network diagram </span><em style="text-align: center;">System Network</em></h6></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="047c774b-9afe-4aa7-ae05-debe2f9eeb13"><ac:parameter ac:name="id">940934834908</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related Pages:</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) UML diagrams" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Extension diagrams" /><ac:plain-text-link-body><![CDATA[Extension diagram]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Diagramming" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=272738493 space=MT version=1 -->
## PAGE 03538: (2026x) New elements

- page_id: `272738493`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738493/2026x+New+elements
- version_number: 1
- version_date: `2025-11-25T13:50:15.095+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) Migration User Guides > (2026x) UPDM projects migration manual > (2026x) UPDM 2.1 migration to UAF 1.1 > (2026x) Model migration > (2026x) Elements mapping
- labels: ['msosa']

### NORMALIZED CONTENT

| UAF 1.1 | Description |
| --- | --- |
| Achieved Effect | A dependency relationship that exists between an Actual State (e.g., observed/measured during testing) of an element that attempts to achieve a Desired Effect and an Achiever. |
| Achiever | An Actual Resource, Actual Project or Actual Enterprise Phase that can deliver a Desired Effect. |
| Actual Condition | The Actual State of an environment or location describing its situation. |
| Actual Enduring Task | An actual undertaking recognized by an enterprise as being essential to achieving its goals - i.e. a strategic specification of what the enterprise does. |
| Actual Enterprise Phase | An Actual State that describes the phase of an Enterprise endeavour. |
| Actual Environment | The Actual State that describes the circumstances of an Environment. |
| Actual Project Role | An Actual Project that is applied to a Project Role. |
| Actual Resource | Role in an Organization, where the role carries the authority to undertake a function - though the Actual Organizational Resource given the role has the responsibility. |
| Actual Resource Role | An instance of a System Resource. |
| Actual Responsibility | The duty required of a Person or Organization. |
| Actual Responsible Resource | An abstract grouping of responsible Organizational Resources. |
| Actual Service | An instance of a Service Specification. |
| Actual State | Abstract element that applies temporal extent to a set of elements realized as Instance Specifications. |
| Architecture | An abstract element that represents a generic architecture. Subtypes are Logical Architecture and Physical Architecture. |
| Asset | Asset as applied to Security views, an abstract element that indicates the types of elements that can be considered as a subject for security analysis. |
| Asset Role | Asset Role as applied to Security views, an abstract element that indicates the type of elements that can be considered as a subject for security analysis in the particular context. |
| Capability For Task | An abstraction relationship that asserts that a Capability is required in order for an Enterprise to conduct a phase of an Enduring Task. |
| Competence To Conduct | An abstraction relationship used to associate a Function with a specific set of Competencies needed to conduct the Function |
| Concern | Interest in an Enterprise Phase (Enterprise Phase is synonym for System in ISO 42010) relevant to one or more of its stakeholders. |
| Consumes | A Consumes relationship is an abstraction relationship that asserts that a service in someway contributes or assists in the execution of an Operational Activity. |
| Data Role | A usage of Data Element that exists in the context of an Resource Asset. It also allows the representation of the whole-part aggregation of Data Elements. |
| Enhances | A dependency relationship relating the Tailored Security Control to a Security Control. |
| Fielded Capability | An actual, fully-realized capability. A Fielded Capability is typed by a Capability Configuration. |
| Information Role | A usage of Information Element that exists in the context of an Operational Asset. It also allows the representation of the whole-part aggregation of Information Elements. |
| Measurable Element | Abstract grouping for elements that can be measured by applying Measurement Sets to them. |
| Mitigation Role | An abstract element that indicates the types of elements that can be considered as a subject for mitigating against a risk. |
| Operational Interface | A declaration that specifies a contract between the Nodes it is related to and any other Nodes it can interact with. |
| Operational Mitigation | A set of security measures intended to address against specific cyber risks. Comprises a subset of Security Controls that are required to protect the asset at node (Operational Role). |
| Operational Asset | An abstract element used to group the elements of Operational Agent and Information Element allowing them to own Information Roles. |
| Operational Signal | An Operational Signal is a specification of a kind of communication between operational performers in which a reaction is asynchronously triggered in the receiver without a reply. |
| Organization In Enterprise | An abstraction relationship relating an Actual Organization to an Actual Enterprise Phase to denote that the Actual Organization plays a role or is a stakeholder in an Actual Enterprise Phase. |
| Performs In Context | An abstraction relationship that relates an Operational Action to a Operational Role, or a Function Action to a Resource Role. It indicates that the action can be carried out by the role when used in a specific context or configuration. |
| Project Activity | An activity carried out during a project. |
| Project Activity Action | The Project Activity Action is defined as a call behavior action that invokes the activity that needs to be preformed. |
| Project Role | Usage of a Project in the context of another Project. Creates a whole-part relationship. |
| Protects | A dependency that asserts that a Security Control is required to protect an Asset. |
| Protects In Context | A dependency relationship that relates a Security Control Action to a Operational Role, or a Resource Role. It indicates that Security Control is required to protect an Asset in a specific context or configuration. |
| Protocol Stack | A sub-type of Protocol that contains the Protocol Layers, defining a complete stack. |
| Required Service Level | A sub type of Actual Service that details a specific service level required of the provider. |
| Resource Asset | An abstract element used to group the elements of Resource Performer and Data Element allowing them to own Data Roles |
| Resource Interface | A declaration that specifies a contract between the System Resources it is related to and any other System Resources it can interact with. It is also intended to be an implementation of a specification of an Interface in the Business and/or Service layer. |
| Resource Mitigation | A set of security measures intended to address specific cyber risks. Comprises a subset of Tailored Security Controls that are used to protect the asset at resource (Resource Role). |
| Resource Signal | A Resource Signal is a specification of a kind of communication between resources (ResourcePerformers) in which a reaction is asynchronously triggered in the receiver without a reply. |
| Risk | A statement of the impact of an event on Assets. It represents a constraint on an Asset in terms of adverse effects, with an associated measure of the likelihood of the event’s occurrence. Software related security risks are those risks that arise from the loss of confidentiality, integrity, or availability of information or information systems. |
| Security Constraint | A type of rule that captures a formal statement to define access control policy language. |
| Security Control | A type of Operational Activity that specifies a safeguard or countermeasure prescribed for Operational Performer. It is intended to protect the confidentiality, integrity, and availability of its information. |
| Security Control Action | A call of a Security Control in the context of another Security Control. It is used to show how a set of Security Controls can be used to protect an asset at node (Operation Role). |
| Security Control Family | An element that organizes security controls into a family. |
| Security Endave | An element that is a collection of information systems connected by one or more internal networks under the control of a single authority and security policy. The systems may be structured by physical proximity or by function, independent of location. |
| Security Process | The security-related procedure that satisfies the security control requirement. |
| Security Process Action | A call of a Security Control in the context of another Security Control. It is used to show how a set of Security Controls can be used to protect an asset at node (Node Role). |
| Service Connector | A channel for exchange between two Service Specifications. Where one acts as the consumer of the other. |
| Service Specification | The specification of a set of functionality provided by one element for the use of others. |
| Service Specification Role | Usage of a Service Specification in the context of another Service Specification. Creates a whole-part relationship. |
| Subject Of Risk | An abstract grouping of elements that can be the subject of a Risk. |
| Subject Of Security Constraint | An abstract grouping of elements that can be the subject of a Security Constraint. |
| Tailored Security Control | A type of Function that implements a Security Control, it specifies a safeguard or countermeasure prescribed for a System Resource. It is intended to protect the confidentiality, integrity, and availability of its information. |
| Technology | A sub type of Resource Artifact that indicates a technology domain, i.e. nuclear, mechanical, electronic, mobile telephony etc. |
| Version Succession | A dependency relationship between two Version Of Configurations that denotes that one Version Of Configuration follows from another. |
| Versioned Element | An abstract grouping of System Resource and Service Specification that allows Version Of Configuration to be related to Actual Project Milestones. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><table class="relative-table"><colgroup><col style="width: 295.0px;" /> <col style="width: 1527.0px;" /> </colgroup><tbody><tr><th colspan="1">UAF 1.1</th><th colspan="1">Description</th></tr><tr><td>Achieved Effect</td><td>A dependency relationship that exists between an Actual State (e.g., observed/measured during testing) of an element that attempts to achieve a Desired Effect and an Achiever.</td></tr><tr><td>Achiever</td><td>An Actual Resource, Actual Project or Actual Enterprise Phase that can deliver a Desired Effect.</td></tr><tr><td>Actual Condition</td><td>The Actual State of an environment or location describing its situation.</td></tr><tr><td>Actual Enduring Task</td><td>An actual undertaking recognized by an enterprise as being essential to achieving its goals - i.e. a strategic specification of what the enterprise does.</td></tr><tr><td>Actual Enterprise Phase</td><td>An Actual State that describes the phase of an Enterprise endeavour.</td></tr><tr><td>Actual Environment</td><td>The Actual State that describes the circumstances of an Environment.</td></tr><tr><td>Actual Project Role</td><td>An Actual Project that is applied to a Project Role.</td></tr><tr><td>Actual Resource</td><td>Role in an Organization, where the role carries the authority to undertake a function - though the Actual Organizational Resource given the role has the responsibility.</td></tr><tr><td>Actual Resource Role</td><td>An instance of a System Resource.</td></tr><tr><td>Actual Responsibility</td><td>The duty required of a Person or Organization.</td></tr><tr><td>Actual Responsible Resource</td><td>An abstract grouping of responsible Organizational Resources.</td></tr><tr><td>Actual Service</td><td>An instance of a Service Specification.</td></tr><tr><td>Actual State</td><td>Abstract element that applies temporal extent to a set of elements realized as Instance Specifications.</td></tr><tr><td>Architecture</td><td>An abstract element that represents a generic architecture. Subtypes are Logical Architecture and Physical Architecture.</td></tr><tr><td>Asset</td><td>Asset as applied to Security views, an abstract element that indicates the types of elements that can be considered as a subject for security analysis.</td></tr><tr><td colspan="1">Asset Role</td><td colspan="1"><span style="color: rgb(62,63,64);">Asset Role as applied to Security views, an abstract element that indicates the type of elements that can be considered as a subject for security analysis in the particular context.</span></td></tr><tr><td>Capability For Task</td><td>An abstraction relationship that asserts that a Capability is required in order for an Enterprise to conduct a phase of an Enduring Task.</td></tr><tr><td>Competence To Conduct</td><td>An abstraction relationship used to associate a Function with a specific set of Competencies needed to conduct the Function</td></tr><tr><td>Concern</td><td>Interest in an Enterprise Phase (Enterprise Phase is synonym for System in ISO 42010) relevant to one or more of its stakeholders.</td></tr><tr><td>Consumes</td><td> A Consumes relationship is an abstraction relationship that asserts that a service in someway contributes or assists in the execution of an Operational Activity.</td></tr><tr><td colspan="1"><span style="color: rgb(62,63,64);">Data Role</span></td><td colspan="1"><span style="color: rgb(62,63,64);">A usage of Data Element that exists in the context of an Resource Asset. It also allows the representation of the whole-part aggregation of Data Elements.</span></td></tr><tr><td>Enhances</td><td>A dependency relationship relating the Tailored Security Control to a Security Control.</td></tr><tr><td>Fielded Capability</td><td>An actual, fully-realized capability. A Fielded Capability is typed by a Capability Configuration.</td></tr><tr><td colspan="1"><span style="color: rgb(62,63,64);">Information Role</span></td><td colspan="1"><span style="color: rgb(62,63,64);">A usage of Information Element that exists in the context of an Operational Asset. It also allows the representation of the whole-part aggregation of Information Elements. </span></td></tr><tr><td>Measurable Element</td><td>Abstract grouping for elements that can be measured by applying Measurement Sets to them.</td></tr><tr><td>Mitigation Role</td><td>An abstract element that indicates the types of elements that can be considered as a subject for mitigating against a risk.</td></tr><tr><td>Operational Interface</td><td>A declaration that specifies a contract between the Nodes it is related to and any other Nodes it can interact with.</td></tr><tr><td>Operational Mitigation</td><td>A set of security measures intended to address against specific cyber risks. Comprises a subset of Security Controls that are required to protect the asset at node (Operational Role).</td></tr><tr><td colspan="1">Operational Asset</td><td colspan="1"><span style="color: rgb(62,63,64);">An abstract element used to group the elements of Operational Agent and Information Element allowing them to own Information Roles.</span></td></tr><tr><td colspan="1">Operational Signal</td><td colspan="1">An Operational Signal is a specification of a kind of communication between operational performers in which a reaction is asynchronously triggered in the receiver without a reply.</td></tr><tr><td>Organization In Enterprise</td><td>An abstraction relationship relating an Actual Organization to an Actual Enterprise Phase to denote that the Actual Organization plays a role or is a stakeholder in an Actual Enterprise Phase.</td></tr><tr><td>Performs In Context</td><td>An abstraction relationship that relates an Operational Action to a Operational Role, or a Function Action to a Resource Role. It indicates that the action can be carried out by the role when used in a specific context or configuration.</td></tr><tr><td colspan="1">Project Activity</td><td colspan="1">An activity carried out during a project.</td></tr><tr><td>Project Activity Action</td><td>The Project Activity Action is defined as a call behavior action that invokes the activity that needs to be preformed.</td></tr><tr><td>Project Role</td><td>Usage of a Project in the context of another Project. Creates a whole-part relationship.</td></tr><tr><td>Protects</td><td>A dependency that asserts that a Security Control is required to protect an Asset.</td></tr><tr><td>Protects In Context</td><td>A dependency relationship that relates a Security Control Action to a Operational Role, or a Resource Role. It indicates that Security Control is required to protect an Asset in a specific context or configuration.</td></tr><tr><td>Protocol Stack</td><td>A sub-type of Protocol that contains the Protocol Layers, defining a complete stack.</td></tr><tr><td>Required Service Level</td><td>A sub type of Actual Service that details a specific service level required of the provider.</td></tr><tr><td colspan="1"><span style="color: rgb(62,63,64);">Resource Asset</span></td><td colspan="1"><span style="color: rgb(62,63,64);">An abstract element used to group the elements of Resource Performer and Data Element allowing them to own Data Roles</span></td></tr><tr><td>Resource Interface</td><td>A declaration that specifies a contract between the System Resources it is related to and any other System Resources it can interact with. It is also intended to be an implementation of a specification of an Interface in the Business and/or Service layer.</td></tr><tr><td>Resource Mitigation</td><td>A set of security measures intended to address specific cyber risks. Comprises a subset of Tailored Security Controls that are used to protect the asset at resource (Resource Role).</td></tr><tr><td colspan="1">Resource Signal</td><td colspan="1">A Resource Signal is a specification of a kind of communication between resources (ResourcePerformers) in which a reaction is asynchronously triggered in the receiver without a reply.</td></tr><tr><td>Risk</td><td>A statement of the impact of an event on Assets. It represents a constraint on an Asset in terms of adverse effects, with an associated measure of the likelihood of the event’s occurrence. Software related security risks are those risks that arise from the loss of confidentiality, integrity, or availability of information or information systems.</td></tr><tr><td>Security Constraint</td><td>A type of rule that captures a formal statement to define access control policy language.</td></tr><tr><td>Security Control</td><td>A type of Operational Activity that specifies a safeguard or countermeasure prescribed for Operational Performer. It is intended to protect the confidentiality, integrity, and availability of its information.</td></tr><tr><td>Security Control Action</td><td>A call of a Security Control in the context of another Security Control. It is used to show how a set of Security Controls can be used to protect an asset at node (Operation Role).</td></tr><tr><td>Security Control Family</td><td>An element that organizes security controls into a family.</td></tr><tr><td>Security Endave</td><td>An element that is a collection of information systems connected by one or more internal networks under the control of a single authority and security policy. The systems may be structured by physical proximity or by function, independent of location.</td></tr><tr><td colspan="1">Security Process</td><td colspan="1">The security-related procedure that satisfies the security control requirement.</td></tr><tr><td colspan="1"><span>Security Process Action</span></td><td colspan="1">A call of a Security Control in the context of another Security Control. It is used to show how a set of Security Controls can be used to protect an asset at node (Node Role).</td></tr><tr><td>Service Connector</td><td>A channel for exchange between two Service Specifications. Where one acts as the consumer of the other.</td></tr><tr><td>Service Specification</td><td>The specification of a set of functionality provided by one element for the use of others.</td></tr><tr><td>Service Specification Role</td><td>Usage of a Service Specification in the context of another Service Specification. Creates a whole-part relationship.</td></tr><tr><td>Subject Of Risk</td><td>An abstract grouping of elements that can be the subject of a Risk.</td></tr><tr><td>Subject Of Security Constraint</td><td>An abstract grouping of elements that can be the subject of a Security Constraint.</td></tr><tr><td>Tailored Security Control</td><td>A type of Function that implements a Security Control, it specifies a safeguard or countermeasure prescribed for a System Resource. It is intended to protect the confidentiality, integrity, and availability of its information.</td></tr><tr><td>Technology</td><td>A sub type of Resource Artifact that indicates a technology domain, i.e. nuclear, mechanical, electronic, mobile telephony etc.</td></tr><tr><td>Version Succession</td><td>A dependency relationship between two Version Of Configurations that denotes that one Version Of Configuration follows from another.</td></tr><tr><td>Versioned Element</td><td>An abstract grouping of System Resource and Service Specification that allows Version Of Configuration to be related to Actual Project Milestones.</td></tr></tbody></table><p class="auto-cursor-target"> </p>
````

<!--NOMAGIC_PAGE id=272738732 space=MT version=1 -->
## PAGE 03539: (2026x) New elements in 19.0

- page_id: `272738732`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738732/2026x+New+elements+in+19.0
- version_number: 1
- version_date: `2025-11-25T13:50:30.792+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) Migration User Guides > (2026x) UAF projects migration manual > (2026x) Migration from UPDM 3 (UAF 1.0 beta) to UAF 1.1 > (2026x) Migration from UPDM 3 (UAF 1.0 beta) to UAF 1.0
- labels: ['msosa']

### NORMALIZED CONTENT

540206759

540206762

540206761

The new UAF elements are introduced in the 19.0 version:

- [CONFLUENCE_PAGE title='Operational Signal' space='MED']
- [CONFLUENCE_PAGE title='Project Activity' space='MED']
- [CONFLUENCE_PAGE title='Project Activity Action' space='MED']
- [CONFLUENCE_PAGE title='Resource Signal' space='MED']
- [CONFLUENCE_PAGE title='Security Process' space='MED']
- [CONFLUENCE_PAGE title='Security Process Action' space='MED']

540206758

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Working with Projects Processes diagram' space='']
- [CONFLUENCE_PAGE title='(2026x) Working with Projects Process Flow diagram' space='']
- [CONFLUENCE_PAGE title='(2026x) Working with Security Processes diagram' space='']
- [CONFLUENCE_PAGE title='(2026x) Working with Security Process Flow (Resources) diagram' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ab49e73b-94ec-4aee-90f5-e37b53431979"><ac:parameter ac:name="id">540206759</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="f920f9c4-4edd-4958-bfdc-87f61d310af3"><ac:parameter ac:name="id">540206762</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f09c4046-f079-4f3a-b37e-7cce683930d8"><ac:parameter ac:name="id">540206761</ac:parameter><ac:rich-text-body><div>The new UAF elements are introduced in the 19.0 version:</div><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Signal" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Project Activity" /></ac:link></li><li><span> <ac:link><ri:page ri:space-key="MED" ri:content-title="Project Activity Action" /></ac:link></span></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Signal" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Security Process" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Security Process Action" /></ac:link></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="15244083-78cb-43e6-8d3e-d43afd90892e"><ac:parameter ac:name="id">540206758</ac:parameter><ac:rich-text-body><p><strong>Related procedures</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Working with Projects Processes diagram" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Working with Projects Process Flow diagram" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Working with Security Processes diagram" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Working with Security Process Flow (Resources) diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272733644 space=MT version=1 -->
## PAGE 03540: (2026x) New elements in UAF 1.1

- page_id: `272733644`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733644/2026x+New+elements+in+UAF+1.1
- version_number: 1
- version_date: `2025-11-25T13:42:39.692+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) Migration User Guides > (2026x) UAF projects migration manual > (2026x) Migration from UAF 1.0 to UAF 1.1
- labels: ['msosa']

### NORMALIZED CONTENT

| UAF 1.1 | Description |
| --- | --- |
| DataRole* | A usage of DataElement that exists in the context of an ResourceAsset. It also allows the representation of the whole-part aggregation of DataElements. |
| OperationalAsset | An abstract element used to group the elements of OperationalAgent and InformationElement allowing them to own InformationRoles. |
| ResourceAsset | An abstract element used to group the elements of ResourcePerformer and DataElement allowing them to own DataRoles |

* For more information, see [CONFLUENCE_PAGE title='(2026x) Mapping solutions and issues' space=''].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><table class="relative-table"><colgroup><col /><col /></colgroup><tbody><tr><th colspan="1">UAF 1.1</th><th colspan="1">Description</th></tr><tr><td><ac:inline-comment-marker ac:ref="5ceef1b7-e33c-47d2-8205-88fa07854def">DataRole*</ac:inline-comment-marker></td><td>A usage of DataElement that exists in the context of an ResourceAsset. It also allows the representation of the whole-part aggregation of DataElements.</td></tr><tr><td><ac:inline-comment-marker ac:ref="ed22cf6d-6e0d-42c0-bdab-819e47012f48">OperationalAsset</ac:inline-comment-marker></td><td>An abstract element used to group the elements of OperationalAgent and InformationElement allowing them to own InformationRoles.</td></tr><tr><td colspan="1"><ac:inline-comment-marker ac:ref="1b16c926-e0eb-48cf-a38d-5e58347cd27f">ResourceAsset</ac:inline-comment-marker></td><td colspan="1">An abstract element used to group the elements of ResourcePerformer and DataElement allowing them to own DataRoles</td></tr></tbody></table><p class="auto-cursor-target">* For more information, see <ac:link><ri:page ri:content-title="(2026x) Mapping solutions and issues" /></ac:link>.</p>
````

<!--NOMAGIC_PAGE id=272738424 space=MT version=2 -->
## PAGE 03541: (2026x) None End Event

- page_id: `272738424`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738424/2026x+None+End+Event
- version_number: 2
- version_date: `2025-11-25T14:45:10.734+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Business Process Model and Notation Concepts > (2026x) BPMN Process Diagram > (2026x) End Events
- labels: ['msosa']

### NORMALIZED CONTENT

**Description**

A None Start Event does not have a defined result.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Boundary Events
- Activities
- End Events

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- [CONFLUENCE_PAGE title='(2026x) Creating and Using a BPMN Event' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>A None Start Event does not have a defined result.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="end_event.png"><ri:page ri:content-title="(2026x) None End Event" /></ri:attachment></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related elements</strong></p><ul><li data-uuid="f00c2c54-4ac7-45ed-90a5-f602382148b0"><a href="https://docs.nomagic.com/display/MT/(2026x) Boundary+Events">Boundary Events</a></li><li data-uuid="4d5d6c61-1229-45e4-a2fa-f3ba556a9394"><a href="https://docs.nomagic.com/display/MT/(2026x) Activities">Activities</a></li><li class="ancestor-link parent-link" data-uuid="fc4476e1-2fac-4acb-94da-a664d665e700"><a href="https://docs.nomagic.com/display/MT/(2026x) End+Events">End Events</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link" data-uuid="344c45a8-2737-4fd1-9147-e03b8584c42e"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Process+Diagram">BPMN Process Diagram</a></li><li data-uuid="87b96a40-c01c-4da6-a106-0a0a6917571c"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li data-uuid="c58ce00e-3a46-4e59-823f-848eed61b2dd"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li data-uuid="fc3d6890-fad6-4632-8c1d-2ab2073512ec"><ac:link><ri:page ri:content-title="(2026x) Creating and Using a BPMN Event" /><ac:plain-text-link-body><![CDATA[Creating and Using an Event]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272737886 space=MT version=2 -->
## PAGE 03542: (2026x) None Intermediate Event

- page_id: `272737886`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272737886/2026x+None+Intermediate+Event
- version_number: 2
- version_date: `2025-11-25T14:44:42.299+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Business Process Model and Notation Concepts > (2026x) BPMN Process Diagram > (2026x) Intermediate Catch Event
- labels: ['msosa']

### NORMALIZED CONTENT

**Description**

A None Intermediate Event does not have a defined trigger.

This event is used to model methodologies that use events to indicate some changes in a state of process.

**Notation**

[IMAGE alt='' src='']

**Related element**

- Intermediate Catch Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- [CONFLUENCE_PAGE title='(2026x) Creating and Using a BPMN Event' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>A None Intermediate Event does not have a defined trigger.</p><p>This event is used to model methodologies that use events to indicate some changes in a state of process.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_catch_event.png"><ri:page ri:content-title="(2026x) None Intermediate Event" /></ri:attachment></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related element</strong></p><ul><li class="ancestor-link parent-link" data-uuid="7ea03f7f-00a6-4e09-8c7b-441004fca057"><a href="https://docs.nomagic.com/display/MT/(2026x) Intermediate+Catch+Event">Intermediate Catch Event</a></li></ul><p class="ancestor-link parent-link"><strong>Related diagrams</strong></p><ul><li class="ancestor-link" data-uuid="0ef4c170-e937-4d7b-98c9-72ceed804c17"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Process+Diagram">BPMN Process Diagram</a></li><li data-uuid="30ee5db3-bb8c-4121-bdf3-b5bca2a9c23f"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li data-uuid="6261ff65-1b5c-4d50-afae-e93e1715cfb3"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li data-uuid="c0ce4734-0154-4163-babc-2698ba50c6c1"><ac:link><ri:page ri:content-title="(2026x) Creating and Using a BPMN Event" /><ac:plain-text-link-body><![CDATA[Creating and Using an Event]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272737726 space=MT version=2 -->
## PAGE 03543: (2026x) None Start Event

- page_id: `272737726`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272737726/2026x+None+Start+Event
- version_number: 2
- version_date: `2025-11-25T14:44:32.505+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Business Process Model and Notation Concepts > (2026x) BPMN Process Diagram > (2026x) Start Events
- labels: ['msosa']

### NORMALIZED CONTENT

**Description**

A None Start Event does not have a defined trigger that invokes the start of a process.

**Notation**

[IMAGE alt='' src='']

**Related element**

- Start Events

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- [CONFLUENCE_PAGE title='(2026x) Creating and Using a BPMN Event' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>A None Start Event does not have a defined trigger that invokes the start of a process.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="start_event.png"><ri:page ri:content-title="(2026x) None Start Event" /></ri:attachment></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related element</strong></p><ul><li class="ancestor-link parent-link" data-uuid="128c4e97-f54b-41da-b1ea-565b351ccad5"><a href="https://docs.nomagic.com/display/MT/(2026x) Start+Events">Start Events</a></li></ul><p class="ancestor-link parent-link"><strong>Related diagrams</strong></p><ul><li class="ancestor-link" data-uuid="1f826a76-0870-4694-b9e7-65d9bfdf3a70"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Process+Diagram">BPMN Process Diagram</a></li><li data-uuid="50581d7c-d6c6-40ff-a556-e9873707dc05"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li data-uuid="cec20b8f-26f7-447c-a499-9d18e7a8a39c"><a href="https://docs.nomagic.com/display/MT/(2026x) BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li data-uuid="55384a74-8823-4069-9884-fcee9983775e"><ac:link><ri:page ri:content-title="(2026x) Creating and Using a BPMN Event" /><ac:plain-text-link-body><![CDATA[Creating and Using an Event]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272730070 space=MT version=1 -->
## PAGE 03544: (2026x) Notation

- page_id: `272730070`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730070/2026x+Notation
- version_number: 1
- version_date: `2025-11-25T13:36:31.535+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) Data-related modeling > (2026x) XML schemas > (2026x) XML schema mapping to UML elements
- labels: ['msosa']

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
<p>Maps to a UML Attribute with the stereotype XSDnotation. This attribute must be added into the UML class with the stereotype XSDschema.</p><ul><li>name maps to UML Attribute name</li><li style="text-align: left;">annotation maps to UML Attribute documentation</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e6251254-c408-4c2a-90ec-a8d34fc95895"><ac:parameter ac:name="title">notation XML representation summary</ac:parameter><ac:rich-text-body><pre>&lt;notation</pre><pre>	id = ID</pre><pre>	name = NCName<br />	public =  anyURI</pre><pre>	system = anyURI</pre><pre>	{any attributes with non-schema namespace…}&gt;</pre><pre>	Content: (annotation?)</pre><pre>&lt;/notation&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="23cb0e59-9553-4083-882d-7e33eac26c7d"><ac:parameter ac:name="title">XML representation of a notation declaration</ac:parameter><ac:rich-text-body><pre>&lt;xs:notation name=&quot;jpeg&quot; public=&quot;image/jpeg&quot; system=&quot;viewer.exe&quot;&gt;</pre></ac:rich-text-body></ac:structured-macro><h6 style="text-align: center;"><ac:image><ri:attachment ri:filename="Figure 132 notation UML Model Example.png"><ri:page ri:content-title="(2026x) Notation" /></ri:attachment></ac:image></h6><h6 style="text-align: center;">notation UML model example.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3d53c347-f765-4bf6-85d2-4319ebec30b6"><ac:parameter ac:name="title">notation XML code sample</ac:parameter><ac:rich-text-body><pre>&lt;xs:schema xmlns:nm = &quot;<a href="http://nomagic.comu">http://nomagic.com&quot;</a> xmlns:xs = &quot;<a href="http://www.w3.org/2001/XMLSchema%22">http://www.w3.org/2001/XMLSchema&quot;</a> targetNamespace = &quot;<a href="http://nomagic.com">http://nomagic.com</a>&quot;&gt;</pre><pre>	&lt;xs:notation name = &quot;jpeg&quot; public = &quot;image/jpeg&quot; system = &quot;viewer.exe&quot;/&gt;</pre><pre>&lt;/xs:schema&gt;</pre></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=272732652 space=MT version=1 -->
## PAGE 03545: (2026x) Notification window

- page_id: `272732652`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732652/2026x+Notification+window
- version_number: 1
- version_date: `2025-11-25T13:41:08.483+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Working with projects
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

The Notification window displays various notification messages regarding any important information you may need to review, such as errors in the model, missing features, etc. Any notification that is displayed in the tool, even after it is closed, can be reviewed in the Notification window at any moment.

[IMAGE alt='' src='']

##### Opening the Notification window

To open the Notification window, do one of the following

- On the Main menu, click Window > Notification Window .
- On the keyboard, click Ctrl+M.
- Click the [ATTACHMENT filename='error_notification_icon.png'] button on the bottom right corner of a notification.
- Click either of the following icons on the Status line: [IMAGE alt='' src=''][IMAGE alt='' src=''][IMAGE alt='' src='']. If you cannot see the Notification window icon on the Status line, it means there are no new notifications since the last time the Notification window was viewed.

##### Descriptionof Notification window areas

The**Notification Window**consists of the following areas:

44

[IMAGE alt='' src='']

###### Toolbar

The toolbar allows you to manage notifications. All buttons are described in the following table.

| Button icon | Button name | Description |
| --- | --- | --- |
|  | Open Configuration | Click to open the Notifications options in the Environment Options dialog to manage Notification display time, Minimal severity level, etc., for the tool. |
|  | Scroll to the Start | Click to scroll to the top of the Notification area.The button is disabled if there are too few notifications in the Notification area to scroll. |
|  | Scroll to the End | Click to scroll to the end of the Notification area. The button is disabled if there are too few notifications in the Notification area to scroll. |
|  | Lock Position | Click to lock the Notification area at a specific position it is scrolled to. Once the Notification window is reopened, the Notification area will remain fixed in the set position. |
|  | Clear Messages | Click to remove all notifications from the Notification area.To see past notifications once they have been cleared, use the Show Full History button. |
|  | Show Full History | Click to display past notifications that have appeared in the project. By default, the notifications of the last 30 days are displayed. You can change the number of days the notifications are stored in history via the Retain History option (Environment Options > Notifications). |
|  | Find | Click to open the Find menu, which contains:Close button. Click it to close the Find menu.Search field. Input the search word/phrase you want to look for in the Notification area.Find Next button. Click to highlight the next instance of the searched word.Find Previous button. Click to highlight the previous instance of the searched word.Highlight button. Click to highlight all instances of the searched word.The search highlights only the visible results. To highlight the result not only in the notification name but also in the notification message, display the full notification message by clicking the More... button next to the notification name.Match Case check box. Select it to make the search case-sensitive. |

###### Notification area

The Notification area displays:

- The timestamp of the notification.
- The notification name.
- The notification message. To view the full notification message, click More... next to the notification name. Click Less... to hide the notification message. The notification message may contain:
  - A link to the element with the error in the Containment tree.
  - A link to the documentation for more information.

[IMAGE alt='' src='']

###### Tabs

The Notification window contains two tabs:

- The Project tab contains all project-specific notifications.
- The Environment tab contains all non-project-specific notifications.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Notification window displays various notification messages regarding any important information you may need to review, such as errors in the model, missing features, etc. Any notification that is displayed in the tool, even after it is closed, can be reviewed in the Notification window at any moment.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="notification_window.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image></p><h3>Opening the Notification window</h3><p>To open the Notification window, do one of the following</p><hr /><ul><li>On the Main menu, click <strong>Window</strong> &gt; <strong>Notification Window</strong>.</li><li>On the keyboard, click Ctrl+M.</li><li>Click the <ac:image><ri:attachment ri:filename="error_notification_icon.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image> button on the bottom right corner of a notification.</li><li><p class="auto-cursor-target">Click either of the following icons on the Status line: <ac:image><ri:attachment ri:filename="status_bar_notification_icon.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image><ac:image><ri:attachment ri:filename="status_bar_notification_icon_2.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image><ac:image><ri:attachment ri:filename="status_bar_notification_icon_3.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="54be35c9-73e3-4ecf-9da4-0ecd22548a14"><ac:rich-text-body><p>If you cannot see the Notification window icon on the Status line, it means there are no new notifications since the last time the Notification window was viewed.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><h3 class="auto-cursor-target"><span style="font-size: 16.0px;letter-spacing: -0.006em;">Description </span><span style="font-size: 16.0px;letter-spacing: -0.006em;">of Notification window areas</span></h3><p><span style="color: rgb(51,51,51);">The<span> <strong>Notification Window </strong></span>consists of the following areas:</span></p><p><span style="color: rgb(51,51,51);"><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="9d455318-677a-4423-8af1-7c1471f0fd37"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">4</ac:parameter></ac:structured-macro></span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="notification_window_areas.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image></p><h4>Toolbar</h4><p><span style="color: rgb(51,51,51);">The toolbar allows you to manage notifications. All buttons are described in the following table.</span></p><table class="relative-table wrapped" style="width: 89.0896%;"><colgroup><col style="width: 9.13447%;" /><col style="width: 15.3806%;" /><col style="width: 75.4986%;" /></colgroup><tbody><tr><th>Button icon</th><th colspan="1">Button name</th><th>Description</th></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="open_configuration_icon.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image></p></div></td><td colspan="1">Open Configuration</td><td>Click to open the <strong>Notifications</strong> options in the <strong>Environment Options </strong>dialog to manage Notification display time, Minimal severity level, etc., for the tool.</td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="scroll_to_the_start_icon.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image></p></div></td><td colspan="1">Scroll to the Start</td><td><div class="content-wrapper"><p>Click to scroll to the top of the Notification area.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d112bcb0-427e-40ff-b29a-e1bf39b4c321"><ac:rich-text-body><p>The button is disabled if there are too few notifications in the Notification area to scroll.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="scroll_to_the_end_icon.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image></p></div></td><td colspan="1">Scroll to the End</td><td><div class="content-wrapper"><p>Click to scroll to the end of the Notification area. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="06c2ccc0-fd5f-494a-bef9-f1bcedc7c366"><ac:rich-text-body><p>The button is disabled if there are too few notifications in the Notification area to scroll.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="lock_position_icon.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image></p></div></td><td colspan="1">Lock Position</td><td>Click to lock the Notification area at a specific position it is scrolled to. Once the Notification window is reopened, the Notification area will remain fixed in the set position.</td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="clear_messages_icon.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image></p></div></td><td colspan="1">Clear Messages</td><td><div class="content-wrapper"><p>Click to remove all notifications from the Notification area.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="1177d168-b42b-4688-a933-94484cfdcec4"><ac:rich-text-body><p>To see past notifications once they have been cleared, use the <strong>Show Full History</strong> <ac:image><ri:attachment ri:filename="show_full_history_icon.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image> button.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="show_full_history_icon.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image></p></div></td><td colspan="1">Show Full History</td><td><div class="content-wrapper"><p>Click to display past notifications that have appeared in the project. By default, the notifications of the last 30 days are displayed. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f4e12866-4976-4b55-8929-c5cea091f1af"><ac:rich-text-body><p>You can change the number of days the notifications are stored in history via the <strong>Retain History</strong> option (<strong>Environment Options &gt; </strong><strong>Notifications</strong>).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="find_icon.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image></p></div></td><td colspan="1">Find</td><td colspan="1"><div class="content-wrapper"><p>Click to open the <strong>Find </strong>menu, which contains:</p><p><ac:image><ri:attachment ri:filename="find_menu.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image></p><ul><li><strong>Close</strong> <ac:image><ri:attachment ri:filename="find_close_button.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image> button. Click it to close the Find menu.</li><li><strong>Search field</strong>. Input the search word/phrase you want to look for in the Notification area.</li><li><strong>Find Next</strong> button. Click to highlight the next instance of the searched word.</li><li><strong>Find Previous</strong> button. Click to highlight the previous instance of the searched word.</li><li><strong>Highlight</strong> button. Click to highlight all instances of the searched word.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="31cfc4a6-f416-4c94-b762-a6208cfac6ee"><ac:rich-text-body><p>The search highlights only the visible results. To highlight the result not only in the notification name but also in the notification message, display the full notification message by clicking the <strong>More...</strong> button next to the notification name.</p></ac:rich-text-body></ac:structured-macro><ul><li><strong>Match Case</strong> check box. Select it to make the search case-sensitive.</li></ul></div></td></tr></tbody></table><h4 class="auto-cursor-target">Notification area</h4><p>The Notification area displays:</p><ul><li class="auto-cursor-target">The timestamp of the notification.</li><li class="auto-cursor-target">The notification name.</li><li class="auto-cursor-target">The notification message. To view the full notification message, click <strong>More...</strong> next to the notification name. Click <strong>Less...</strong> to hide the notification message.<br />The notification message may contain:<ul><li class="auto-cursor-target">A link to the element with the error in the Containment tree.</li><li class="auto-cursor-target">A link to the documentation for more information. </li></ul></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="notification_area.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image></p><h4 class="auto-cursor-target">Tabs</h4><p>The Notification window contains two tabs:</p><ul><li>The <strong>Project </strong>tab contains all project-specific notifications.</li><li>The <strong>Environment </strong>tab contains all non-project-specific notifications.</li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="notification_tabs.png"><ri:page ri:content-title="(2026x) Notification window" /></ri:attachment></ac:image></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=272731559 space=MT version=1 -->
## PAGE 03546: (2026x) NOV-1 High-Level Operational Concept Description

- page_id: `272731559`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731559/2026x+NOV-1+High-Level+Operational+Concept+Description
- version_number: 1
- version_date: `2025-11-25T13:39:14.664+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Operational Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

750592101

750592103

750592102

**Description**

The purpose of High-level Operational Concept Description is to provide a high-level graphical and textual description of operational concept (high level organizations, missions, geographic configuration, connectivity, etc) of what the architecture is supposed to do, and how it is supposed to do it. The NOV-1, along with the corresponding NAV-1 product is intended to serve as an executive summary of the architecture.

**Implementation**

NOV-1 can be represented using:

- Link to an external document.
- NOV-1 diagram which is based on the UML Composite Structure diagram.
- NOV-1 Free Form diagram which is based on the UML Class diagram.
- UML Composite Structure Diagram.

**Sample**

[IMAGE alt='' src='']

###### NOV-1 High-Level Operational Concept Graphic

750592100

**Related elements**

- [CONFLUENCE_PAGE title='High Level Operational Concept' space='MED']
- [CONFLUENCE_PAGE title='Concept Role' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3daae913-1f89-4535-a9f8-b512d572c349"><ac:parameter ac:name="id">750592101</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c15771cb-ba8c-4e8d-9c04-7eacd273dd4a"><ac:parameter ac:name="id">750592103</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3d14e433-6b8d-4f99-807c-fa9e642abb54"><ac:parameter ac:name="id">750592102</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The purpose of High-level Operational Concept Description is to provide a high-level graphical and textual description of operational concept (high level organizations, missions, geographic configuration, connectivity, etc) of what the architecture is supposed to do, and how it is supposed to do it. The NOV-1, along with the corresponding NAV-1 product is intended to serve as an executive summary of the architecture.</p><p><strong>Implementation</strong></p><p>NOV-1 can be represented using:</p><ul><li>Link to an external document.</li><li>NOV-1 diagram which is based on the UML Composite Structure diagram.</li><li>NOV-1 Free Form diagram which is based on the UML Class diagram.</li><li>UML Composite Structure Diagram.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nov_1_high_level.png"><ri:page ri:content-title="(2026x) NOV-1 High-Level Operational Concept Description" /></ri:attachment></ac:image></p><h6>NOV-1 High-Level Operational Concept Graphic</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="eba83ef0-240e-450c-ae53-c9d1bfdcfbb8"><ac:parameter ac:name="id">750592100</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="High Level Operational Concept" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Concept Role" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="cdb093c1-f065-40e7-a128-a4666bba1e7b" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731570 space=MT version=1 -->
## PAGE 03547: (2026x) NOV-2 Operational Node Connectivity Description

- page_id: `272731570`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731570/2026x+NOV-2+Operational+Node+Connectivity+Description
- version_number: 1
- version_date: `2025-11-25T13:39:16.571+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Operational Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

751195321

751195324

751195323

**Description**

The Operational Node Connectivity Description is intended to track the need to exchange information from specific operational nodes (that play a key role in the architecture) to others. An NOV-2 does not depict the connectivity between the nodes. NAF modifies the NOV-2 in two ways. First it recommends that an NOV-2 diagram shows the platforms or geographic locations at which operational nodes are deployed. Secondly it provides additional information about each needline in the form of a requirements specification. There are now four types of needlines identified as follows:

1. InformationExchange.
2. EnergyFlow.
3. MaterielFlow.
4. MovementOfPeople.

In addition, NAF permits service-oriented architectures. Instead of needlines between nodes, it is possible simply to show which services the nodes provide and consume. Finally, NAF again permits known resources to be shown in a NOV-2. However, this must be clearly shown as a KnownResource in a NOV-2 model. LogicalArchitecture, which is the container class for all the nodes and KnownResources, is introduced.

**Implementation**

NOV-2 can be represented using:

- NOV-2 diagram which is based on the UML Class diagram.
- NOV-2 diagram which is based on the UML Composite Structure diagram.
- UML Class diagram.
- UML Composite Structure diagram.
- SysML Block Definition diagram.
- SysML Internal Block diagram.

**Sample**

[IMAGE alt='' src='']

###### NOV-2 Operational Node Connectivity Description

[IMAGE alt='' src='']

###### NOV-2 Operational Node Internal Connectivity Description

**Related views**

An NOV-2 is highly related with an NOV-5. Operational Nodes shown in the NOV-2 are the performers of the Operational Activities modeled in the NOV-5. NOV-2 focuses on the Operational Nodes, with the activities being a secondary adornment. The NOV-5, on the other hand, places first-order attention on operational activities and only second-order attention on Nodes, which can be shown as annotations or swim-lanes on the activities.

Information flows can be modeled either in the NOV-2 or NOV-5. In both cases they are highly associated and in general should be reused between these views.

The NOV-2 displays the Capabilities required by Nodes from NCV-2. That is an association between two abstraction levels of user requirements where the NOV is more specific than the StV and a Node is more specific concept than a Capability.

The other important mapping is between NOV-2 and NSV-1. The specification Node and implementation Resource are subjects to map here. One NOV-2 product can have several implementations in the NSV-1.

751195320

**Related elements**

- [CONFLUENCE_PAGE title='Operational Performer' space='MED']
- [CONFLUENCE_PAGE title='Operational Architecture' space='MED']
- [CONFLUENCE_PAGE title='Operational Exchange' space='MED']
- [CONFLUENCE_PAGE title='Operational Information' space='MED']
- [CONFLUENCE_PAGE title='Operational Port' space='MED']
- [CONFLUENCE_PAGE title='Operational Role' space='MED']
- [CONFLUENCE_PAGE title='Operational Connector' space='MED']
- [CONFLUENCE_PAGE title='Capability' space='MED']
- [CONFLUENCE_PAGE title='Exhibits' space='MED']
- [CONFLUENCE_PAGE title='Actual Location' space='MED']
- [CONFLUENCE_PAGE title='Location' space='MED']
- [CONFLUENCE_PAGE title='Natural Resource' space='MED']
- [CONFLUENCE_PAGE title='Is Capable To Perform' space='MED']
- [CONFLUENCE_PAGE title='Operational Activity' space='MED']
- [CONFLUENCE_PAGE title='Known Resource' space='MED']
- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']
- [CONFLUENCE_PAGE title='Problem Domain' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="7483a186-9469-4e3c-bdde-ac1eda27705d"><ac:parameter ac:name="id">751195321</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="0be96cf8-5554-4364-a125-357e71892719"><ac:parameter ac:name="id">751195324</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="59587587-69ae-47eb-a3f9-0eab4ffe9bb2"><ac:parameter ac:name="id">751195323</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The Operational Node Connectivity Description is intended to track the need to exchange information from specific operational nodes (that play a key role in the architecture) to others. An NOV-2 does not depict the connectivity between the nodes. NAF modifies the NOV-2 in two ways. First it recommends that an NOV-2 diagram shows the platforms or geographic locations at which operational nodes are deployed. Secondly it provides additional information about each needline in the form of a requirements specification. There are now four types of needlines identified as follows:</p><ol><li>InformationExchange.</li><li>EnergyFlow.</li><li>MaterielFlow.</li><li><p>MovementOfPeople.</p></li></ol><p>In addition, NAF permits service-oriented architectures. Instead of needlines between nodes, it is possible simply to show which services the nodes provide and consume. Finally, NAF again permits known resources to be shown in a NOV-2. However, this must be clearly shown as a KnownResource in a NOV-2 model. LogicalArchitecture, which is the container class for all the nodes and KnownResources, is introduced.</p><p><strong>Implementation</strong></p><p>NOV-2 can be represented using:</p><ul><li>NOV-2 diagram which is based on the UML Class diagram.</li><li>NOV-2 diagram which is based on the UML Composite Structure diagram.</li><li>UML Class diagram.</li><li>UML Composite Structure diagram.</li><li>SysML Block Definition diagram.</li><li>SysML Internal Block diagram.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nov_2.png"><ri:page ri:content-title="(2026x) NOV-2 Operational Node Connectivity Description" /></ri:attachment></ac:image></p><h6>NOV-2 Operational Node Connectivity Description</h6><p><ac:image><ri:attachment ri:filename="Nov_2_example.png"><ri:page ri:content-title="(2026x) NOV-2 Operational Node Connectivity Description" /></ri:attachment></ac:image></p><h6>NOV-2 Operational Node Internal Connectivity Description</h6><p><strong>Related views</strong></p><p>An NOV-2 is highly related with an NOV-5. Operational Nodes shown in the NOV-2 are the performers of the Operational Activities modeled in the NOV-5. NOV-2 focuses on the Operational Nodes, with the activities being a secondary adornment. The NOV-5, on the other hand, places first-order attention on operational activities and only second-order attention on Nodes, which can be shown as annotations or swim-lanes on the activities.</p><p>Information flows can be modeled either in the NOV-2 or NOV-5. In both cases they are highly associated and in general should be reused between these views.</p><p>The NOV-2 displays the Capabilities required by Nodes from NCV-2. That is an association between two abstraction levels of user requirements where the NOV is more specific than the StV and a Node is more specific concept than a Capability.</p><p>The other important mapping is between NOV-2 and NSV-1. The specification Node and implementation Resource are subjects to map here. One NOV-2 product can have several implementations in the NSV-1.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e6879873-8de8-4164-82a8-ba271f53179b"><ac:parameter ac:name="id">751195320</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Performer" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Architecture" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Exchange" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Information" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Port" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Role" /></ac:link></li><li><span style="color: rgb(62,63,64);"><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Connector" /></ac:link></span></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Exhibits" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Location" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Location" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Natural Resource" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Is Capable To Perform" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Activity" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Known Resource" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Problem Domain" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="24467877-f44e-4234-89b5-0c2d91d78715" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731578 space=MT version=1 -->
## PAGE 03548: (2026x) NOV-3 Operational Information Requirements

- page_id: `272731578`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731578/2026x+NOV-3+Operational+Information+Requirements
- version_number: 1
- version_date: `2025-11-25T13:39:17.600+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Operational Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

757316014

757316016

757316015

**Description**

Information exchanges express the relationship across the three basic architecture data elements of an NOV (operational activities, operational nodes, and information flow) with a focus on the specific aspects of the information flow and the information content.

The Information Exchanges of the NOV-3 should remain at a high level of aggregation to represent actual information workflow products that are used at the operational nodes shown in the NOV-2 (and not their subordinate operational nodes).

**Implementation**

NOV-3 can be represented using:

- NOV-3 table.
- NOV-3 role-based table. A role-based table represents exchanges between Node Roles(node usages).
- NOV-3 spreadsheet report.

**Sample**

[IMAGE alt='' src='']

###### NOV-3 Operational Information Requirements

**Related views**

An NOV-3 is initially constructed from the information contained in the NATO Operational Node Connectivity Description (NOV-2).

757316013

**Related elements**

- [CONFLUENCE_PAGE title='Operational Performer' space='MED']
- [CONFLUENCE_PAGE title='Operational Exchange' space='MED']
- [CONFLUENCE_PAGE title='Operational Information' space='MED']
- [CONFLUENCE_PAGE title='Natural Resource' space='MED']
- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Operational Activity' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Displaying Custom Measurements' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="26568d02-5509-49dc-b44c-b2d603832c49"><ac:parameter ac:name="id">757316014</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="bbf28d17-560a-40eb-a834-f7a3ed3f7c60"><ac:parameter ac:name="id">757316016</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="96317893-e4a8-4c37-b5a9-971baea7d076"><ac:parameter ac:name="id">757316015</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>Information exchanges express the relationship across the three basic architecture data elements of an NOV (operational activities, operational nodes, and information flow) with a focus on the specific aspects of the information flow and the information content.</p><p>The Information Exchanges of the NOV-3 should remain at a high level of aggregation to represent actual information workflow products that are used at the operational nodes shown in the NOV-2 (and not their subordinate operational nodes).</p><p><strong>Implementation</strong></p><p>NOV-3 can be represented using:</p><ul><li>NOV-3 table.</li><li><p class="auto-cursor-target">NOV-3 role-based table.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="89c1dc9a-b681-4cf2-8aaf-7ea90c1a8f73"><ac:rich-text-body>A role-based table represents exchanges between Node Roles(node usages).</ac:rich-text-body></ac:structured-macro></li><li>NOV-3 spreadsheet report.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nov_3.png"><ri:page ri:content-title="(2026x) NOV-3 Operational Information Requirements" /></ri:attachment></ac:image></p><h6>NOV-3 Operational Information Requirements</h6><p><strong>Related views</strong></p><p>An NOV-3 is initially constructed from the information contained in the NATO Operational Node Connectivity Description (NOV-2).</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d8744e7e-4066-420b-9960-611ee3f17c78"><ac:parameter ac:name="id">757316013</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Performer" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Exchange" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Information" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Natural Resource" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Activity" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="fc15d18c-c2a3-46a5-943d-fb4ca1b594ee" /></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Displaying Custom Measurements" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732844 space=MT version=1 -->
## PAGE 03549: (2026x) NOV-4 Organizational Relationships Chart

- page_id: `272732844`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732844/2026x+NOV-4+Organizational+Relationships+Chart
- version_number: 1
- version_date: `2025-11-25T13:41:18.850+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Operational Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

758339179

758339181

758339180

**Description**

The NATO Organizational Relationships Chart illustrates the command structure or relationships (as opposed to relationships with respect to a business process flow) among human roles, organizations, or organization types that are the key players in architecture. NAF divides The NOV-4 in two views: an NOV-4 Typical and an NOV-4 Actual.

**Implementation**

NOV-4 can be represented using:

- NOV-4 diagram which is based on the UML Class diagram.
- UML Class diagram.
- SysML Block Definition diagram.

**Sample**

[IMAGE alt='' src='']

###### NOV-4 Organizational Relationships Chart

758339178

**Related elements**

- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']
- [CONFLUENCE_PAGE title='Person' space='MED']
- [CONFLUENCE_PAGE title='Command' space='MED']
- [CONFLUENCE_PAGE title='Competence' space='MED']
- [CONFLUENCE_PAGE title='Provides Competence' space='MED']
- [CONFLUENCE_PAGE title='Requires Competence' space='MED']
- [CONFLUENCE_PAGE title='Actual Organization' space='MED']
- [CONFLUENCE_PAGE title='Actual Post' space='MED']
- [CONFLUENCE_PAGE title='Actual Person' space='MED']
- [CONFLUENCE_PAGE title='Fills Post' space='MED']
- [CONFLUENCE_PAGE title='Actual Resource Relationship' space='MED']
- [CONFLUENCE_PAGE title='Actual Organization Role' space='MED']
- [CONFLUENCE_PAGE title='Operational Activity' space='MED']
- [CONFLUENCE_PAGE title='Owns Process' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Instantiating structures' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d31ac5c1-5ced-4d05-bcd8-6a28c4b8deca"><ac:parameter ac:name="id">758339179</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="79da0ccd-f831-4f3c-b3b7-a8568475e791"><ac:parameter ac:name="id">758339181</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="17bdbe28-aab0-4f31-aff4-55000de992a7"><ac:parameter ac:name="id">758339180</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NATO Organizational Relationships Chart illustrates the command structure or relationships (as opposed to relationships with respect to a business process flow) among human roles, organizations, or organization types that are the key players in architecture. NAF divides The NOV-4 in two views: an NOV-4 Typical and an NOV-4 Actual.</p><p><strong>Implementation</strong></p><p>NOV-4 can be represented using:</p><ul><li>NOV-4 diagram which is based on the UML Class diagram.</li><li>UML Class diagram.</li><li>SysML Block Definition diagram.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nov_4.png"><ri:page ri:content-title="(2026x) NOV-4 Organizational Relationships Chart" /></ri:attachment></ac:image></p><h6>NOV-4 Organizational Relationships Chart</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="50d1ffde-7aa4-46ce-a778-d25b70a505c4"><ac:parameter ac:name="id">758339178</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Person" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Command" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Competence" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Provides Competence" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Requires Competence" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Person" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Fills Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Resource Relationship" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Organization Role" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Activity" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Owns Process" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e90decce-f83b-4894-82de-a9a105d8c6bf" /></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Instantiating structures" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732838 space=MT version=1 -->
## PAGE 03550: (2026x) NOV-5 Operational Activity Model

- page_id: `272732838`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732838/2026x+NOV-5+Operational+Activity+Model
- version_number: 1
- version_date: `2025-11-25T13:41:18.325+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Operational Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

758835411

758835413

758835412

**Description**

The NATO Operational Activity Model describes the operations that are normally conducted in the course of achieving a mission or a business goal, from a net-centric perspective. It describes capabilities, operational activities (or tasks), input and output (I/O) flows between activities, and I/O flows to/from activities that are outside the scope of the architecture. It is imperative that the levels-of-detail between the NOV-2, NOV-3, and NOV-5 remain cohesive. For example, if one diagram of NOV-2 operational nodes is developed that shows aggregated organizations only, then it is imperative that the corresponding NOV-5 product be developed to show only those operational activities that are meaningful with respect to these operational nodes. Similarly, the information exchanges of NOV-3 should remain at a high level of aggregation to represent actual information workflow products that are used at the operational nodes depicted in NOV-2 (and not their subordinate operational nodes). The net-centric NOV-5 may be used in the following ways:

- Delineate lines of dependency on external activities when coupled with an NOV-2.
- Highlight information flows to depict the status of the information's refinement (raw, preprocessed, fused, etc.).
- Provide the critical foundation for depicting Task, Post, Process, and Use (TPPU) activity sequencing and timing in the NOV-6a, NOV-6b, and NOV-6c.
- Identify critical mission threads and operational information exchanges by annotating which activities are critical, for example, identify the activities in the model that are critical.

**Implementation**

NOV-5 can be represented using:

- NOV-5 diagram for Operational Activity hierarchies. This diagram is based on the UML Class diagram.
- NOV-5 diagram for Operational Activity flows. This diagram is based on the UML Activity diagram.
- UML Class diagram.
- UML Activity diagram.
- SysML Block diagram.
- SysML Activity diagram.

**Sample**

[IMAGE alt='' src='']

###### NOV-5 Operational Activity hierarchy Model

[IMAGE alt='' src='']

###### NOV-5 Operational Activity Model

**Related views**

The NOV-5 and NOV-2 are, to a degree, complements of each other. An NOV-5 focuses on the operational activities whereas NOV-2 focuses on the operational nodes. Due to the relationship between nodes and operational activities, these types of view should normally be developed together.

To maintain this independence from implementation, the logical Nodes in an NOV-2 are used to represent the structure which carries out the Operational Activities. Operational Activities are realized as Functions (NSV-4) which are the “how” to the Operational Activities’ “what”, for example, they are specified in terms of the resources that carry them out.

The activities described in an NOV-5 may be Standard Operational Activities which are defined in the NCV-6 (which also maps the activities to corresponding capabilities).

758835409

**Related elements**

- [CONFLUENCE_PAGE title='Operational Activity' space='MED']
- [CONFLUENCE_PAGE title='Operational Parameter' space='MED']
- [CONFLUENCE_PAGE title='Standard Operational Activity' space='MED']
- [CONFLUENCE_PAGE title='Operational Performer' space='MED']
- [CONFLUENCE_PAGE title='Is Capable To Perform' space='MED']
- [CONFLUENCE_PAGE title='Operational Activity Action' space='MED']
- [CONFLUENCE_PAGE title='Operational Activity Edge' space='MED']
- [CONFLUENCE_PAGE title='Operational Exchange' space='MED']
- [CONFLUENCE_PAGE title='Operational Information' space='MED']
- [CONFLUENCE_PAGE title='Natural Resource' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Creating Process Flow Diagrams From Compositions or Aggregations Defined in Process Diagrams' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="2a46a64c-2749-41ca-9165-69f4bd2dd864"><ac:parameter ac:name="id">758835411</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="9d8ec3a7-230f-4dba-bb60-6b7185c9dc08"><ac:parameter ac:name="id">758835413</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="97caaee9-6525-4b1c-a084-0e95f9e51cad"><ac:parameter ac:name="id">758835412</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NATO Operational Activity Model describes the operations that are normally conducted in the course of achieving a mission or a business goal, from a net-centric perspective. It describes capabilities, operational activities (or tasks), input and output (I/O) flows between activities, and I/O flows to/from activities that are outside the scope of the architecture. It is imperative that the levels-of-detail between the NOV-2, NOV-3, and NOV-5 remain cohesive. For example, if one diagram of NOV-2 operational nodes is developed that shows aggregated organizations only, then it is imperative that the corresponding NOV-5 product be developed to show only those operational activities that are meaningful with respect to these operational nodes. Similarly, the information exchanges of NOV-3 should remain at a high level of aggregation to represent actual information workflow products that are used at the operational nodes depicted in NOV-2 (and not their subordinate operational nodes). The net-centric NOV-5 may be used in the following ways:</p><ul><li>Delineate lines of dependency on external activities when coupled with an NOV-2.</li><li>Highlight information flows to depict the status of the information's refinement (raw, preprocessed, fused, etc.).</li><li>Provide the critical foundation for depicting Task, Post, Process, and Use (TPPU) activity sequencing and timing in the NOV-6a, NOV-6b, and NOV-6c.</li><li>Identify critical mission threads and operational information exchanges by annotating which activities are critical, for example, identify the activities in the model that are critical.</li></ul><p><strong>Implementation</strong></p><p>NOV-5 can be represented using:</p><ul><li>NOV-5 diagram for Operational Activity hierarchies. This diagram is based on the UML Class diagram.</li><li>NOV-5 diagram for Operational Activity flows. This diagram is based on the UML Activity diagram.</li><li>UML Class diagram.</li><li>UML Activity diagram.</li><li>SysML Block diagram.</li><li>SysML Activity diagram.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nov_5.png"><ri:page ri:content-title="(2026x) NOV-5 Operational Activity Model" /></ri:attachment></ac:image></p><h6>NOV-5 Operational Activity hierarchy Model</h6><p><ac:image><ri:attachment ri:filename="Nov_5_op.png"><ri:page ri:content-title="(2026x) NOV-5 Operational Activity Model" /></ri:attachment></ac:image></p><h6>NOV-5 Operational Activity Model</h6><p><strong>Related views</strong></p><p>The NOV-5 and NOV-2 are, to a degree, complements of each other. An NOV-5 focuses on the operational activities whereas NOV-2 focuses on the operational nodes. Due to the relationship between nodes and operational activities, these types of view should normally be developed together.</p><p>To maintain this independence from implementation, the logical Nodes in an NOV-2 are used to represent the structure which carries out the Operational Activities. Operational Activities are realized as Functions (NSV-4) which are the “how” to the Operational Activities’ “what”, for example, they are specified in terms of the resources that carry them out.</p><p>The activities described in an NOV-5 may be Standard Operational Activities which are defined in the NCV-6 (which also maps the activities to corresponding capabilities).</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f0514a64-d1f6-4617-bea7-8ea2c6d414c7"><ac:parameter ac:name="id">758835409</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Activity" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Parameter" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Standard Operational Activity" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Performer" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Is Capable To Perform" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Activity Action" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Activity Edge" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Exchange" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Information" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Natural Resource" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="50b3ac05-eaba-4ddf-8a2f-8492498e077b" /></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Creating Process Flow Diagrams From Compositions or Aggregations Defined in Process Diagrams" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732755 space=MT version=1 -->
## PAGE 03551: (2026x) NOV-6a Operational Node Parametric

- page_id: `272732755`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732755/2026x+NOV-6a+Operational+Node+Parametric
- version_number: 1
- version_date: `2025-11-25T13:41:12.681+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Operational Viewpoint > (2026x) NOV-6a Operational Rule Model
- labels: ['msosa']

### NORMALIZED CONTENT

498037010

498037012

498037011

**Description**

A Parametric diagram includes the usage of a [CONFLUENCE_PAGE title='Constraint Block' space='MED'] to constrain the properties of another Operational Performer. It contains [CONFLUENCE_PAGE title='Constraint Property' space='MED'] and constraint parameters as well as other properties from within that internal block context. All properties displayed, other than the constraints themselves, must either be bound directly to a constraint parameter or contain a property that is bound to a constraint parameter (through any number of containment levels). A constraint block generally contain many constraints, each of them containing many constraint parameters.

498037009

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Working with Parametric diagram' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="13521878-25b1-445e-a67c-a99569a42667"><ac:parameter ac:name="id">498037010</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="940e5d6e-ed07-4842-9817-92928bb978c5"><ac:parameter ac:name="id">498037012</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e0df61e8-e39b-4d81-9838-9dfeef4960f0"><ac:parameter ac:name="id">498037011</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>A Parametric diagram includes the usage of a <ac:link><ri:page ri:space-key="MED" ri:content-title="Constraint Block" /><ac:plain-text-link-body><![CDATA[constraint block]]></ac:plain-text-link-body></ac:link> to constrain the properties of another Operational Performer. It contains <ac:link><ri:page ri:space-key="MED" ri:content-title="Constraint Property" /><ac:plain-text-link-body><![CDATA[constraint properties]]></ac:plain-text-link-body></ac:link> and constraint parameters as well as other properties from within that internal block context. All properties displayed, other than the constraints themselves, must either be bound directly to a constraint parameter or contain a property that is bound to a constraint parameter (through any number of containment levels). A constraint block generally contain many constraints, each of them containing many constraint parameters.</p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="64902fd8-ca53-4522-bc6d-a3a227893c9e"><ac:parameter ac:name="id">498037009</ac:parameter><ac:rich-text-body><p><strong>Related procedures</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Working with Parametric diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732752 space=MT version=1 -->
## PAGE 03552: (2026x) NOV-6a Operational Rule Model

- page_id: `272732752`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732752/2026x+NOV-6a+Operational+Rule+Model
- version_number: 1
- version_date: `2025-11-25T13:41:12.578+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Operational Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

759905799

759905801

759905800

**Description**

The NATO Operational Rule Model specifies operational or business rules that are constraints on an enterprise, a mission, operation, business, or an architecture. While other NOV views (for example, NOV-1, NOV-2, and NOV5) describe the structure of a business—what the business can do—for the most part, they do not describe what the business must do, or what it cannot do. At the mission level, an NOV-6a may consist of doctrine, guidance, rules of engagement, and so forth. At the operation level, rules may include such things as a military Operational Plan (OPLAN). At lower levels, an NOV-6a describes the rules under which the architecture or its nodes behave under specified conditions. Such rules can be expressed in a textual form, for example, “If (these conditions) exist, and (this event) occurs, then (perform these actions).” At a top level, rules should at least embody the concepts of operations defined in an NOV-1, and should provide guidelines for the development and definition of more detailed rules and behavioral definitions that will occur later in the architecture definition process.

**Implementation**

NOV-6a can be represented using:

- NOV-6a table.
- [CONFLUENCE_PAGE title='(2026x) NOV-6a Operational Node Parametric' space=''] .
- NOV-6a spreadsheet report.

**Sample**

[IMAGE alt='' src='']

###### NOV-6a Operational Rule Model

**Related views**

An NOV-6a constrains the structure elements of NOV-1, NOV-2, and NOV-5. NOV-6a can also be used to extend the capture of business requirements by constraining the structure and validity of the NOV-7 elements.

As the View name implies, the rules captured in an NOV-6a are operational (for example, mission-oriented) whereas resource-oriented rules are defined in an NSV-10 (NOV-6 is the “what” to NSV-10’s “how”).

**Constraint owner**

You can choose where all the constraints will be stored through the**Project Options**.

To select a constraint owner

1. In the main menu, click Options > Project . The Project Options dialog opens.
2. Go to General > UAF , and in the Default Constraint Owners property group, choose a needed owner.

759905797

**Related elements**

- [CONFLUENCE_PAGE title='Operational Constraint' space='MED']
- [CONFLUENCE_PAGE title='Operational Performer' space='MED']
- [CONFLUENCE_PAGE title='Operational Activity' space='MED']
- [CONFLUENCE_PAGE title='Operational Exchange' space='MED']
- [CONFLUENCE_PAGE title='Operational Information' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d1d89863-8134-4c9c-a45f-93578d15a4db"><ac:parameter ac:name="id">759905799</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c66708d3-8223-47b1-a5a4-da22712a7386"><ac:parameter ac:name="id">759905801</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="91fadde4-5f31-405a-b672-edccb2b40dd7"><ac:parameter ac:name="id">759905800</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NATO Operational Rule Model specifies operational or business rules that are constraints on an enterprise, a mission, operation, business, or an architecture. While other NOV views (for example, NOV-1, NOV-2, and NOV5) describe the structure of a business—what the business can do—for the most part, they do not describe what the business must do, or what it cannot do. At the mission level, an NOV-6a may consist of doctrine, guidance, rules of engagement, and so forth. At the operation level, rules may include such things as a military Operational Plan (OPLAN). At lower levels, an NOV-6a describes the rules under which the architecture or its nodes behave under specified conditions. Such rules can be expressed in a textual form, for example, “If (these conditions) exist, and (this event) occurs, then (perform these actions).” At a top level, rules should at least embody the concepts of operations defined in an NOV-1, and should provide guidelines for the development and definition of more detailed rules and behavioral definitions that will occur later in the architecture definition process.</p><p><strong>Implementation</strong></p><p>NOV-6a can be represented using:</p><ul><li>NOV-6a table.</li><li><ac:link><ri:page ri:content-title="(2026x) NOV-6a Operational Node Parametric" /><ac:plain-text-link-body><![CDATA[NOV-6a Operational Node Parametric diagram]]></ac:plain-text-link-body></ac:link>.</li><li>NOV-6a spreadsheet report.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nov_6a.png"><ri:page ri:content-title="(2026x) NOV-6a Operational Rule Model" /></ri:attachment></ac:image></p><h6>NOV-6a Operational Rule Model</h6><p><strong>Related views</strong></p><p>An NOV-6a constrains the structure elements of NOV-1, NOV-2, and NOV-5. NOV-6a can also be used to extend the capture of business requirements by constraining the structure and validity of the NOV-7 elements.</p><p>As the View name implies, the rules captured in an NOV-6a are operational (for example, mission-oriented) whereas resource-oriented rules are defined in an NSV-10 (NOV-6 is the “what” to NSV-10’s “how”).</p><p style=""><strong>Constraint owner</strong></p><p style="">You can choose where all the constraints will be stored through the<span> </span><strong>Project Options</strong>.</p><p style="">To select a constraint owner</p><hr style="" /><ol style=""><li>In the main menu, click<span> </span><strong>Options</strong><span> </span>&gt;<span> </span><strong>Project</strong>. The<span> </span><strong>Project Options</strong><span> </span>dialog opens.</li><li>Go to<span> </span><strong>General</strong><span> </span>&gt;<span> </span><strong>UAF</strong>, and in the<span> </span><strong>Default Constraint Owners</strong><span> </span>property group, choose a needed owner.</li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="edd08f41-5c1f-4bfb-8292-cb754b01353a"><ac:parameter ac:name="id">759905797</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Constraint" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Performer" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Activity" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Exchange" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Information" /></ac:link></li></ul><p><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="814e781e-ef97-4283-a96c-62cb45e9b6da" /></p><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272733361 space=MT version=1 -->
## PAGE 03553: (2026x) NOV-6b Operational State Transition Description

- page_id: `272733361`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733361/2026x+NOV-6b+Operational+State+Transition+Description
- version_number: 1
- version_date: `2025-11-25T13:42:12.470+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Operational Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

761180499

761180501

761180500

**Description**

The NATO Operational State Transition Description is a graphical method of describing how an operational node or activity responds to various events by changing its state. The diagram represents the sets of events to which the architecture will respond (by taking an action to move to a new state) as a function of its current state. Each transition specifies an event and an action. The explicit sequencing of activities in response to external and internal events is not fully expressed in an NOV-5. An NOV-6b can be used to describe the explicit sequencing of the operational activities.

Alternatively, an NOV-6b can be used to reflect the explicit sequencing of actions internal to a single operational activity or the sequencing of operational activities with respect to a specific operational node. In a net-centric architecture, the NOV-6b is used to describe the set of state transitions for providers and consumers in the NetCentric Environment (NCE) in response to the posting of information to the NCE or retrieving of information from the NCE.

**Implementation**

NOV-6b can be represented using a UML State Machine diagram.

**Sample**

**[IMAGE alt='' src='']**

###### NOV-6b Operational State Transition Description

**Related views**

An NOV-6b can be used to describe the detailed sequencing of activities or work flow in the business process. The NOV-6b is particularly useful for describing critical sequencing of behaviors and timing of operational activities that cannot be adequately described in the Activity Model (NOV-5).

761180498

**Related elements**

- [CONFLUENCE_PAGE title='Operational State Description' space='MED']
- [CONFLUENCE_PAGE title='Operational Performer' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Allocate Activities to State Internal Behaviors' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="13945735-efb9-4976-bbeb-f497555c16db"><ac:parameter ac:name="id">761180499</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="6e7324af-c2f2-4ac9-bc41-3b06f383f3fb"><ac:parameter ac:name="id">761180501</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="98a111b7-8ea0-4778-8570-54850efc20a9"><ac:parameter ac:name="id">761180500</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NATO Operational State Transition Description is a graphical method of describing how an operational node or activity responds to various events by changing its state. The diagram represents the sets of events to which the architecture will respond (by taking an action to move to a new state) as a function of its current state. Each transition specifies an event and an action. The explicit sequencing of activities in response to external and internal events is not fully expressed in an NOV-5. An NOV-6b can be used to describe the explicit sequencing of the operational activities.</p><p>Alternatively, an NOV-6b can be used to reflect the explicit sequencing of actions internal to a single operational activity or the sequencing of operational activities with respect to a specific operational node. In a net-centric architecture, the NOV-6b is used to describe the set of state transitions for providers and consumers in the NetCentric Environment (NCE) in response to the posting of information to the NCE or retrieving of information from the NCE.</p><p><strong>Implementation</strong></p><p>NOV-6b can be represented using a UML State Machine diagram.</p><p><strong>Sample</strong></p><p><strong><ac:image><ri:attachment ri:filename="Nov_6b.png"><ri:page ri:content-title="(2026x) NOV-6b Operational State Transition Description" /></ri:attachment></ac:image></strong></p><h6>NOV-6b Operational State Transition Description</h6><p><strong>Related views</strong></p><p>An NOV-6b can be used to describe the detailed sequencing of activities or work flow in the business process. The NOV-6b is particularly useful for describing critical sequencing of behaviors and timing of operational activities that cannot be adequately described in the Activity Model (NOV-5).</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f36a2bee-3a02-4d3a-b132-940e3c0e45bb"><ac:parameter ac:name="id">761180498</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational State Description" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Performer" /></ac:link></li></ul><p><strong>Related procedures</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Allocate Activities to State Internal Behaviors" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272733358 space=MT version=1 -->
## PAGE 03554: (2026x) NOV-6c Operational Event-Trace Description

- page_id: `272733358`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733358/2026x+NOV-6c+Operational+Event-Trace+Description
- version_number: 1
- version_date: `2025-11-25T13:42:11.964+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Operational Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

**Description**

The NATO Operational Event-Trace Description provides a time-ordered examination of the information exchanges between participating operational nodes as a result of a particular operational thread or scenario. Each event-trace diagram should have an accompanying description that defines the particular scenario or situation and represent a specific capability. The NOV-6c is also used in conjunction with an NOV-5 to depict process flow (such as an IDEF3 model). A process flow model captures precedence and causality relations between situations and events by providing a structured method for expressing knowledge about how a process or organization works. A process flow model should be annotated with the names of the operational nodes responsible for conducting those activities. The net-centric NOV-6c describes the business and mission processes that need to be executed to achieve NetCentric Operations (NCO). The ability to discover, access, and understand information and capabilities from the NCE, where and when they are needed, is supported by the NOV-6c and can be decomposed to the level of specificity required for the subject architecture. In the NCE, the NOV-6c may depict the following:

- Exchanges between the Service Functionality Providers and Service Consumers, the Service Consumers and external Service Functionality Providers, and between the Service Functionality Providers and Unanticipated Users.
- Sequences that describe the timeline for the availability of information for any of its refinement states (raw, preprocessed, fused, etc.).
- Handling, methodologies, and the Enterprise Information Environment (EIE) infrastructure components that
- support the operational concepts of post before processing.
- Illustration of one-to-many, many-to-one, and many-to-many exchanges between Service Functionality Providers and Service Consumers found in the net-centric NOV-3.

**Implementation**

NOV-6c can be represented using a NOV-6c diagram which is based on the UML Sequence diagram.

**Sample**

[IMAGE alt='' src='']

###### NOV-6c Operational Event-Trace Description

**Related views**

The NOV-6c can be used by itself or in conjunction with an Operational State Transition Description (NOV-6b) to describe the dynamic behavior of processes.

The information content of messages that connect life-lines in an NOV-6c View Product may be related, in modeling terms, with the information flows (NOV-3, NOV-5) and information entities (NOV-7) modeled in other views.

**Related elements**

- [CONFLUENCE_PAGE title='Interaction' space='MED']
- [CONFLUENCE_PAGE title='Operational Message' space='MED']
- [CONFLUENCE_PAGE title='Operational Exchange' space='MED']
- [CONFLUENCE_PAGE title='Operational Performer' space='MED']
- [CONFLUENCE_PAGE title='Operational Role' space='MED']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>The NATO Operational Event-Trace Description provides a time-ordered examination of the information exchanges between participating operational nodes as a result of a particular operational thread or scenario. Each event-trace diagram should have an accompanying description that defines the particular scenario or situation and represent a specific capability. The NOV-6c is also used in conjunction with an NOV-5 to depict process flow (such as an IDEF3 model). A process flow model captures precedence and causality relations between situations and events by providing a structured method for expressing knowledge about how a process or organization works. A process flow model should be annotated with the names of the operational nodes responsible for conducting those activities. The net-centric NOV-6c describes the business and mission processes that need to be executed to achieve NetCentric Operations (NCO). The ability to discover, access, and understand information and capabilities from the NCE, where and when they are needed, is supported by the NOV-6c and can be decomposed to the level of specificity required for the subject architecture. In the NCE, the NOV-6c may depict the following:</p><ul><li data-uuid="668d8db2-fe96-474f-a17a-060dcfd32a1d">Exchanges between the Service Functionality Providers and Service Consumers, the Service Consumers and external Service Functionality Providers, and between the Service Functionality Providers and Unanticipated Users.</li><li data-uuid="5e1c36a5-ef1d-47fc-bbf8-c66cc74e54b3">Sequences that describe the timeline for the availability of information for any of its refinement states (raw, preprocessed, fused, etc.).</li><li data-uuid="a0a11732-2ee1-482d-a31a-75ff2865b396">Handling, methodologies, and the Enterprise Information Environment (EIE) infrastructure components that</li><li data-uuid="c4869deb-12bf-4859-8f34-c2a3779ccad2">support the operational concepts of post before processing.</li><li data-uuid="5ffad97d-4c00-477b-ac41-392bb8957acf">Illustration of one-to-many, many-to-one, and many-to-many exchanges between Service Functionality Providers and Service Consumers found in the net-centric NOV-3.</li></ul><p><strong>Implementation</strong></p><p>NOV-6c can be represented using a NOV-6c diagram which is based on the UML Sequence diagram.</p><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nov_6c.png"><ri:page ri:content-title="(2026x) NOV-6c Operational Event-Trace Description" /></ri:attachment></ac:image></p><h6>NOV-6c Operational Event-Trace Description</h6><p><strong>Related views</strong></p><p>The NOV-6c can be used by itself or in conjunction with an Operational State Transition Description (NOV-6b) to describe the dynamic behavior of processes.</p><p>The information content of messages that connect life-lines in an NOV-6c View Product may be related, in modeling terms, with the information flows (NOV-3, NOV-5) and information entities (NOV-7) modeled in other views.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related elements</strong></p><ul><li data-uuid="840e7669-49ee-4dda-a9ec-ec5c771a77da"><ac:link><ri:page ri:space-key="MED" ri:content-title="Interaction" /></ac:link></li><li data-uuid="7c303d83-63e1-49eb-9af1-5754e53bcf85"><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Message" /></ac:link></li><li data-uuid="85d732a7-f244-4fd9-82be-a264d16bba8e"><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Exchange" /></ac:link></li><li data-uuid="bf05c97b-a125-45e4-b555-7c4978f78142"><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Performer" /></ac:link></li><li data-uuid="bfa0f3d3-e4f9-40a4-83dd-3b02412f7a0c"><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Role" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272732774 space=MT version=1 -->
## PAGE 03555: (2026x) NOV-7 Information Model

- page_id: `272732774`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732774/2026x+NOV-7+Information+Model
- version_number: 1
- version_date: `2025-11-25T13:41:13.899+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Operational Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

761710076

761710079

761710078

**Description**

An information model is a representation of a domain object model according to its information aspect. In other words, it is a model of the information about the concepts in the universe of discourse, relevant to the architecture effort. For example, if the operational domain recognizes the existence of a concept called ‘weapons platform’, then the information model would contain information objects that reflect what we want to know about weapons platforms and what we want to communicate about weapons platforms to others. As such, the information model is inherently of a conceptual nature (for example, we could dispense with the word ‘conceptual’ in ‘conceptual information model’). Conceptual information models address the information aspect of the universe of discourse. They are not intended to reflect data storage solutions.

**Cameo Data Modeler plugin integration**

You can use the Entity Relationship diagram for conceptual, logical, and physical data modeling in NOV-7.

Note that the Entity Relationship diagram is supported in OV-7. It allows for using the information engineering notation within this view.

**Implementation**

NOV-7 can be represented using:

- NOV-7 diagram which is based on the UML Class diagram.
- UML Class diagram.
- SysML Block Definition diagram.

**Sample**

[IMAGE alt='' src='']

###### NOV-7 Information Model

**Related views**

An Operational Information Entity within an NOV-7 may be an Information Element in an NOV-3 or an Activity Flow Object in an NOV-5.

Note that NAF talks about ‘information’ in the Operational Viewpoint and ‘data’ in the System Viewpoint. The intention of this is that NOV-7 describes information or data of importance to the business (for example, information products that might be referred to in doctrine, SOPs, etc.) whereas NSV-11 describes data relevant at the system level.

761710075

**Related elements**

- [CONFLUENCE_PAGE title='Information Model' space='MED']
- [CONFLUENCE_PAGE title='(2026x) Association' space='']
- Property
- [CONFLUENCE_PAGE title='Operational Information' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="baf14ab7-8e7d-48d2-a07b-47470e2ce5e6"><ac:parameter ac:name="id">761710076</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="45936773-9f3d-4368-9d03-308d029960b7"><ac:parameter ac:name="id">761710079</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="54f6d1f4-4abe-4099-8ac7-c6f508a10933"><ac:parameter ac:name="id">761710078</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>An information model is a representation of a domain object model according to its information aspect. In other words, it is a model of the information about the concepts in the universe of discourse, relevant to the architecture effort. For example, if the operational domain recognizes the existence of a concept called ‘weapons platform’, then the information model would contain information objects that reflect what we want to know about weapons platforms and what we want to communicate about weapons platforms to others. As such, the information model is inherently of a conceptual nature (for example, we could dispense with the word ‘conceptual’ in ‘conceptual information model’). Conceptual information models address the information aspect of the universe of discourse. They are not intended to reflect data storage solutions.</p><p><strong>Cameo Data Modeler plugin integration</strong></p><p>You can use the Entity Relationship diagram for conceptual, logical, and physical data modeling in NOV-7.</p><p>Note that the Entity Relationship diagram is supported in OV-7. It allows for using the information engineering notation within this view.</p><p><strong>Implementation</strong></p><p>NOV-7 can be represented using:</p><ul><li>NOV-7 diagram which is based on the UML Class diagram.</li><li>UML Class diagram.</li><li>SysML Block Definition diagram.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nov_7.png"><ri:page ri:content-title="(2026x) NOV-7 Information Model" /></ri:attachment></ac:image></p><h6>NOV-7 Information Model</h6><p><strong>Related views</strong></p><p>An Operational Information Entity within an NOV-7 may be an Information Element in an NOV-3 or an Activity Flow Object in an NOV-5.</p><p>Note that NAF talks about ‘information’ in the Operational Viewpoint and ‘data’ in the System Viewpoint. The intention of this is that NOV-7 describes information or data of importance to the business (for example, information products that might be referred to in doctrine, SOPs, etc.) whereas NSV-11 describes data relevant at the system level.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9813c095-0fa4-444b-b11f-f6ea63c1128e"><ac:parameter ac:name="id">761710075</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Information Model" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Association" /></ac:link></li><li>Property</li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Information" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="31419c45-3664-405d-a07b-a26d1ab6de99" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731429 space=MT version=1 -->
## PAGE 03556: (2026x) NPV-1 Programme Portfolio Relationships

- page_id: `272731429`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731429/2026x+NPV-1+Programme+Portfolio+Relationships
- version_number: 1
- version_date: `2025-11-25T13:38:54.772+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Programme Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

734940616

734940618

734940617

**Description**

NPV-1 view products represent an organizational perspective on programmes.

**Implementation**

NPV-1 can be represented using:

- NPV-1 Programme Portfolio relationship diagram which is based on the UML Class diagram.
- NPV-1 Responsibility Matrix which is an editable Dependency Matrix.
- NPV-1 realized as a Gantt Chart.

**Sample**

[IMAGE alt='' src='']

###### NPV-1 Programme Portfolio Relationships

[IMAGE alt='' src='']

###### NPV-1 Programme to Capability Mapping

**Related views**

In essence, the NPV-1 is an organizational breakdown consisting of actual organizations (see NOV-4). The view is strongly linked with the NCV-4 which shows capability clusters and dependencies.

734940615

**Related elements**

- [CONFLUENCE_PAGE title='Actual Organization' space='MED']
- [CONFLUENCE_PAGE title='Actual Post' space='MED']
- [CONFLUENCE_PAGE title='Actual Project' space='MED']
- [CONFLUENCE_PAGE title='Actual Project Milestone' space='MED']
- [CONFLUENCE_PAGE title='Actual Project Milestone Role' space='MED']
- [CONFLUENCE_PAGE title='Milestone Dependency' space='MED']
- [CONFLUENCE_PAGE title='Responsible For' space='MED']
- [CONFLUENCE_PAGE title='Project Milestone' space='MED']
- [CONFLUENCE_PAGE title='Project Milestone Role' space='MED']
- [CONFLUENCE_PAGE title='Project Sequence' space='MED']
- [CONFLUENCE_PAGE title='Project Status' space='MED']
- [CONFLUENCE_PAGE title='Project Theme' space='MED']
- [CONFLUENCE_PAGE title='Project' space='MED']
- [CONFLUENCE_PAGE title='Status Indicators' space='MED']

**Related procedures**

**Related references**

- [CONFLUENCE_PAGE title='(2026x) Project Status Application Wizard' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="4a4aa77b-f55b-4e6f-bda9-061c8f82ac50"><ac:parameter ac:name="id">734940616</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="3bea196e-ffa9-4276-b3ff-3fd6e54ae0a0"><ac:parameter ac:name="id">734940618</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="72fe72d6-55be-48e7-8dca-68ad8f3ffef5"><ac:parameter ac:name="id">734940617</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>NPV-1 view products represent an organizational perspective on programmes.</p><p><strong>Implementation</strong></p><p>NPV-1 can be represented using:</p><ul><li>NPV-1 Programme Portfolio relationship diagram which is based on the UML Class diagram.</li><li>NPV-1 Responsibility Matrix which is an editable Dependency Matrix.</li><li>NPV-1 realized as a Gantt Chart.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Npv_1_mapping.jpg"><ri:page ri:content-title="(2026x) NPV-1 Programme Portfolio Relationships" /></ri:attachment></ac:image></p><h6>NPV-1 Programme Portfolio Relationships</h6><p><ac:image><ri:attachment ri:filename="Npv_1.png"><ri:page ri:content-title="(2026x) NPV-1 Programme Portfolio Relationships" /></ri:attachment></ac:image></p><h6>NPV-1 Programme to Capability Mapping</h6><p><strong>Related views</strong></p><p>In essence, the NPV-1 is an organizational breakdown consisting of actual organizations (see NOV-4). The view is strongly linked with the NCV-4 which shows capability clusters and dependencies.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a34e8634-2aef-42b2-8c0f-bd5c3d676369"><ac:parameter ac:name="id">734940615</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Project" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Project Milestone" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Project Milestone Role" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Milestone Dependency" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Responsible For" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Project Milestone" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Project Milestone Role" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Project Sequence" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Project Status" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Project Theme" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Project" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Status Indicators" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="46c54d87-6df5-421d-9a30-62783f164b92" /></p><p><br /><strong>Related references</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Project Status Application Wizard" /></ac:link></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272731564 space=MT version=1 -->
## PAGE 03557: (2026x) NPV-2 Programme to Capability Mapping

- page_id: `272731564`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272731564/2026x+NPV-2+Programme+to+Capability+Mapping
- version_number: 1
- version_date: `2025-11-25T13:39:15.363+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Programme Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

736401501

736401503

736401502

**Description**

The NPV-2 view provides a timeline perspective on programmes.

**Implementation**

NPV-2 can be represented using a NPV-2 diagram which is a non-editable Dependency Matrix. Capabilities will be used as row elements and Actual Projects will be used as column elements.

**Sample**

[IMAGE alt='' src='']

###### NPV-2 Project to Capability Mapping

**Related views**

This model is analogous to the NSV-5 System Function to Operational Activity Traceability Matrix, but provides the interface between Capability and Project Models rather than Operational to System Models.

736401499

**Related elements**

- [CONFLUENCE_PAGE title='Capability' space='MED']
- [CONFLUENCE_PAGE title='Project' space='MED']
- [CONFLUENCE_PAGE title='Maps To Capability' space='MED']
- [CONFLUENCE_PAGE title='(2026x) Dependency' space='']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="cb4bd45a-2b45-4d3c-9a28-a3f1b33c13f4"><ac:parameter ac:name="id">736401501</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d370e31f-dc2a-4118-9b96-22d90ce49644"><ac:parameter ac:name="id">736401503</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9cbad42d-49c2-4f3c-8694-1359ac975835"><ac:parameter ac:name="id">736401502</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NPV-2 view provides a timeline perspective on programmes.</p><p><strong>Implementation</strong></p><p>NPV-2 can be represented using a NPV-2 diagram which is a non-editable Dependency Matrix. Capabilities will be used as row elements and Actual Projects will be used as column elements.</p><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Npv_2.jpg"><ri:page ri:content-title="(2026x) NPV-2 Programme to Capability Mapping" /></ri:attachment></ac:image></p><h6>NPV-2 Project to Capability Mapping</h6><p><strong>Related views</strong></p><p>This model is analogous to the NSV-5 System Function to Operational Activity Traceability Matrix, but provides the interface between Capability and Project Models rather than Operational to System Models.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="eed34e9b-3d08-4e89-9c68-bf10d234fc99"><ac:parameter ac:name="id">736401499</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Project" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Maps To Capability" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Dependency" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="cddb46f4-f31f-4dfc-8a81-0e2768cb73a2" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732767 space=MT version=1 -->
## PAGE 03558: (2026x) NSOV-1 Service Taxonomy

- page_id: `272732767`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732767/2026x+NSOV-1+Service+Taxonomy
- version_number: 1
- version_date: `2025-11-25T13:41:13.545+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Service-Oriented Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

762762340

762762342

762762341

**Description**

NSOV-1 is a service taxonomy, describing a specialization hierarchy of services (note these are classes of services, rather than the service implementations). There is no prescribed representation for this view, other than the ability to show multiple inheritances. The view may optionally show properties (for example, service availability) and constraints on those properties, though this is covered in detail in NSOV-2.

**Implementation**

NSOV-1 can be represented using a NSOV-1 diagram which is based on the UML Class diagram.

**Sample**

[IMAGE alt='' src='']

###### NSOV-1 Service Taxonomy

**Related views**

The Services Interfaces in NSOV-1 can realize Capabilities (from NCV-2) and also support the Operational Activities (from NOV-5).

762762339

**Related elements**

- [CONFLUENCE_PAGE title='Service Interface' space='MED']
- [CONFLUENCE_PAGE title='Capability' space='MED']
- [CONFLUENCE_PAGE title='Expose' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="24e6aefd-a603-40a3-ab13-37b4df68b19e"><ac:parameter ac:name="id">762762340</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c833d526-b83a-4619-9b03-d1fadae2b6c0"><ac:parameter ac:name="id">762762342</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a9645394-3d34-4c21-a61e-b8866c3c8c2e"><ac:parameter ac:name="id">762762341</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>NSOV-1 is a service taxonomy, describing a specialization hierarchy of services (note these are classes of services, rather than the service implementations). There is no prescribed representation for this view, other than the ability to show multiple inheritances. The view may optionally show properties (for example, service availability) and constraints on those properties, though this is covered in detail in NSOV-2.</p><p><strong>Implementation</strong></p><p>NSOV-1 can be represented using a NSOV-1 diagram which is based on the UML Class diagram.</p><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsov_1.png"><ri:page ri:content-title="(2026x) NSOV-1 Service Taxonomy" /></ri:attachment></ac:image></p><h6>NSOV-1 Service Taxonomy</h6><p><strong>Related views</strong></p><p>The Services Interfaces in NSOV-1 can realize Capabilities (from NCV-2) and also support the Operational Activities (from NOV-5).</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="882c57f3-cd2a-47ff-84aa-778fe2b6e05d"><ac:parameter ac:name="id">762762339</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Interface" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Expose" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="2125d045-5ca1-424a-97d3-f04b5bef5405" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272733388 space=MT version=1 -->
## PAGE 03559: (2026x) NSOV-2 Service Definitions

- page_id: `272733388`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733388/2026x+NSOV-2+Service+Definitions
- version_number: 1
- version_date: `2025-11-25T13:42:19.941+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Service-Oriented Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

762900493

762900496

762900494

**Description**

The NSOV-2 view specifies the properties of services and defines the interface of the service explicitly. NMM supports specific stereotypes to manage interfaces, ports as well as asynchronous messages and synchronous operations handling as part of the service interface. It should be noted that only one interface of a service may be exposed to the surrounding environment and that this is the interface that can be accessed by a service consumer.

**Implementation**

NSOV-2 can be represented using

- Report which is automatically generated from all data.
- NSOV-2 diagram which is based on the UML Class diagram

**Sample**

[IMAGE alt='' src='']

###### NSOV-2 Service Definition

**Constraint owner**

You can choose where all the constraints will be stored through the**Project Options**.

To select a constraint owner

1. In the main menu, click Options > Project . The Project Options dialog opens.
2. Go to General > UAF , and in the Default Constraint Owners property group, choose a needed owner.

762900492

**Related elements**

- [CONFLUENCE_PAGE title='Service Interface' space='MED']
- [CONFLUENCE_PAGE title='Service Method' space='MED']
- Flow Property
- [CONFLUENCE_PAGE title='Service Parameter' space='MED']
- [CONFLUENCE_PAGE title='Resource Port' space='MED']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5afe6f06-43b1-4ba9-b9cf-a047009bf058"><ac:parameter ac:name="id">762900493</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="9e34bde9-b07b-4dd5-aac7-d4bba920a7c4"><ac:parameter ac:name="id">762900496</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c2186be6-b072-451a-b83f-7d74f9163074"><ac:parameter ac:name="id">762900494</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NSOV-2 view specifies the properties of services and defines the interface of the service explicitly. NMM supports specific stereotypes to manage interfaces, ports as well as asynchronous messages and synchronous operations handling as part of the service interface. It should be noted that only one interface of a service may be exposed to the surrounding environment and that this is the interface that can be accessed by a service consumer.</p><p><strong>Implementation</strong></p><p>NSOV-2 can be represented using</p><ul><li>Report which is automatically generated from all data.</li><li>NSOV-2 diagram which is based on the UML Class diagram</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsov_2.png"><ri:page ri:content-title="(2026x) NSOV-2 Service Definitions" /></ri:attachment></ac:image></p><h6>NSOV-2 Service Definition</h6><p style=""><strong>Constraint owner</strong></p><p style="">You can choose where all the constraints will be stored through the<span> </span><strong>Project Options</strong>.</p><p style="">To select a constraint owner</p><hr style="" /><ol style=""><li>In the main menu, click<span> </span><strong>Options</strong><span> </span>&gt;<span> </span><strong>Project</strong>. The<span> </span><strong>Project Options</strong><span> </span>dialog opens.</li><li>Go to<span> </span><strong>General</strong><span> </span>&gt;<span> </span><strong>UAF</strong>, and in the<span> </span><strong>Default Constraint Owners</strong><span> </span>property group, choose a needed owner.</li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="aac13ac3-c7fb-43a4-88e0-24361089b004"><ac:parameter ac:name="id">762900492</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Interface" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Method" /></ac:link></li><li>Flow Property</li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Parameter" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Port" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732789 space=MT version=1 -->
## PAGE 03560: (2026x) NSOV-3 Services to Operational Activities Mapping

- page_id: `272732789`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732789/2026x+NSOV-3+Services+to+Operational+Activities+Mapping
- version_number: 1
- version_date: `2025-11-25T13:41:14.644+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Service-Oriented Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

763353994

763353996

763353995

**Description**

This view specifies how services can be combined and sequenced to provide a ‘higher level’ service. Note that there might be several instances (products) of this view since there are generally several different possible service combinations.

The view is best presented by means of a UML composite structure diagram, but other possibilities also exist. It should be noted that no decision concerning the implementation of the service is actually made in this view; for example, the orchestration is a requirement specification rather than a design. In fact, none of the service subviews describe the implementation of the services, this is covered in the NSV-12 view.

**Implementation**

NSOV-3 can be represented using:

- An NSOV-3 Services to Operational Activities Mapping diagram which is a non-editable Dependency Matrix. Service Interfaces will be used as row elements, and Operational Activities will be used as column elements.
- An [CONFLUENCE_PAGE title='(2026x) Working with NSOV-3 Services to Service Contracts Mapping matrix' space=''] matrix. The Services to Service Contracts Mapping matrix depicts mapping between the Services or their specializations and the Service Contracts they govern.

**Sample**

[IMAGE alt='' src='']

###### NSOV-3 Services to Operational Activities Mapping

763353993

**Related elements**

- [CONFLUENCE_PAGE title='Expose' space='MED']
- [CONFLUENCE_PAGE title='Maps To Capability' space='MED']
- [CONFLUENCE_PAGE title='Operational Activity' space='MED']
- [CONFLUENCE_PAGE title='Service Interface' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="44f3ad7c-8648-40b4-af1f-d47b5586baeb"><ac:parameter ac:name="id">763353994</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4db71632-a80f-4061-8193-6b18d4f8a879"><ac:parameter ac:name="id">763353996</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0df4a692-b9c9-45cb-a55b-02c75de59a85"><ac:parameter ac:name="id">763353995</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>This view specifies how services can be combined and sequenced to provide a ‘higher level’ service. Note that there might be several instances (products) of this view since there are generally several different possible service combinations.</p><p>The view is best presented by means of a UML composite structure diagram, but other possibilities also exist. It should be noted that no decision concerning the implementation of the service is actually made in this view; for example, the orchestration is a requirement specification rather than a design. In fact, none of the service subviews describe the implementation of the services, this is covered in the NSV-12 view.</p><p><strong>Implementation</strong></p><p>NSOV-3 can be represented using:</p><ul><li>An NSOV-3 Services to Operational Activities Mapping diagram which is a non-editable Dependency Matrix. Service Interfaces will be used as row elements, and Operational Activities will be used as column elements.</li><li>An <ac:link><ri:page ri:content-title="(2026x) Working with NSOV-3 Services to Service Contracts Mapping matrix" /><ac:plain-text-link-body><![CDATA[NSOV-3 Services to Service Contracts Mapping]]></ac:plain-text-link-body></ac:link> matrix. <span style="color: rgb(62,63,64);">The<span> </span></span><span style="color: rgb(62,63,64);">Services to Service Contracts Mapping</span><span style="color: rgb(62,63,64);"> matrix depicts mapping between the Services or their specializations and the Service Contracts they govern.</span></li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsov_3.png"><ri:page ri:content-title="(2026x) NSOV-3 Services to Operational Activities Mapping" /></ri:attachment></ac:image></p><h6>NSOV-3 Services to Operational Activities Mapping</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4fa10aad-bfbf-4ea4-ad3a-eafaeb17320d"><ac:parameter ac:name="id">763353993</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Expose" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Maps To Capability" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Activity" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Interface" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="7cbcbdd3-953d-4c92-8bfd-feddfd0a3399" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272733400 space=MT version=1 -->
## PAGE 03561: (2026x) NSOV-4 Service Orchestration

- page_id: `272733400`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733400/2026x+NSOV-4+Service+Orchestration
- version_number: 1
- version_date: `2025-11-25T13:42:22.646+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Service-Oriented Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

**Description**

This view shows how operational activities can be supported by various services, for example, within a given scenario, certain defined operational activities within nodes defined as part of NOV-2 can be supported by a given set of services.

**Implementation**

NSOV-4 can be represented using a NSOV-4 diagram which is based on the UML Sequence diagram.

**Sample**

[IMAGE alt='' src='']

###### NSOV-4 Service Orchestration

**Related elements**

- [CONFLUENCE_PAGE title='Interaction' space='MED']
- [CONFLUENCE_PAGE title='Service Message' space='MED']
- [CONFLUENCE_PAGE title='Service Interface' space='MED']
- Flow Property

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>This view shows how operational activities can be supported by various services, for example, within a given scenario, certain defined operational activities within nodes defined as part of NOV-2 can be supported by a given set of services.</p><p><strong>Implementation</strong></p><p>NSOV-4 can be represented using a NSOV-4 diagram which is based on the UML Sequence diagram.</p><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsov_4.png"><ri:page ri:content-title="(2026x) NSOV-4 Service Orchestration" /></ri:attachment></ac:image></p><h6>NSOV-4 Service Orchestration</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related elements</strong></p><ul><li data-uuid="0ad20017-f84b-4cfc-8c16-3e8e3d520c6e"><ac:link><ri:page ri:space-key="MED" ri:content-title="Interaction" /></ac:link></li><li data-uuid="3cb41d77-932d-46db-a918-a8b317d0198a"><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Message" /></ac:link></li><li data-uuid="b1030217-10bd-4b81-bea5-711c217b9ac7"><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Interface" /></ac:link></li><li data-uuid="2674df45-2354-41f2-a114-c8693a66d9eb">Flow Property </li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272732949 space=MT version=1 -->
## PAGE 03562: (2026x) NSOV-5 Service Behaviour Definition

- page_id: `272732949`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732949/2026x+NSOV-5+Service+Behaviour+Definition
- version_number: 1
- version_date: `2025-11-25T13:41:31.247+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Service-Oriented Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

764190441

764190443

764190442

**Description**

This view enables the description of a service by means of a state-diagram, an activity model or by an event-trace description. In order to fully define the sequencing of messages and operations that form part of the service interface, event-trace descriptions are useful. In order to fully define the handling that takes place in a service due to possible different internal states, a state description is also useful. For all of these descriptions standard UML entities provide the best means of representation.

**Implementation**

NSOV-5 can be represented using:

- NSOV-5 diagram for the Operational Activity flows. This diagram is based on the UML Activity diagram.
- NSOV-5 diagram based on the UML Clas diagram.
- UML Activity diagram.
- SysML Activity diagram.
- UML Class diagram.

**Sample**

[IMAGE alt='' src='']

###### Service Behaviour Definition

[IMAGE alt='' src='']

###### Fragment of NSOV-5 Service Behaviour

**Related views**

An NSOV-5 is the key behavioral specification for services. It is equivalent in nature to the NOV-5 and NSV-4. It specifies a set of functions that a service implementation is expected to perform.

An NSOV-5 specifies the required functionality that an implementation of a service is expected to have – the implementation is represented in the NSV-1 and NSV-4.

764190440

**Related elements**

- [CONFLUENCE_PAGE title='Service Function' space='MED']
- [CONFLUENCE_PAGE title='Service Function Action' space='MED']
- [CONFLUENCE_PAGE title='Function Edge' space='MED']
- [CONFLUENCE_PAGE title='Service Method' space='MED']
- [CONFLUENCE_PAGE title='Service Parameter' space='MED']
- [CONFLUENCE_PAGE title='Service Interface' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Creating Process Flow Diagrams From Compositions or Aggregations Defined in Process Diagrams' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="02a1394d-93aa-49ea-82d3-95510846fd2f"><ac:parameter ac:name="id">764190441</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ec83681e-2f3d-4e9e-974d-d0c785cf57b5"><ac:parameter ac:name="id">764190443</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="88762772-ed79-47ed-a892-47a9a9f341c4"><ac:parameter ac:name="id">764190442</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>This view enables the description of a service by means of a state-diagram, an activity model or by an event-trace description. In order to fully define the sequencing of messages and operations that form part of the service interface, event-trace descriptions are useful. In order to fully define the handling that takes place in a service due to possible different internal states, a state description is also useful. For all of these descriptions standard UML entities provide the best means of representation.</p><p><strong>Implementation</strong></p><p>NSOV-5 can be represented using:</p><ul><li>NSOV-5 diagram for the Operational Activity flows. This diagram is based on the UML Activity diagram.</li><li>NSOV-5 diagram based on the UML Clas diagram.</li><li>UML Activity diagram.</li><li>SysML Activity diagram.</li><li>UML Class diagram.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsov_5.png"><ri:page ri:content-title="(2026x) NSOV-5 Service Behaviour Definition" /></ri:attachment></ac:image></p><h6>Service Behaviour Definition</h6><p><ac:image><ri:attachment ri:filename="Nsov_5_example.png"><ri:page ri:content-title="(2026x) NSOV-5 Service Behaviour Definition" /></ri:attachment></ac:image></p><h6>Fragment of NSOV-5 Service Behaviour</h6><p><strong>Related views</strong></p><p>An NSOV-5 is the key behavioral specification for services. It is equivalent in nature to the NOV-5 and NSV-4. It specifies a set of functions that a service implementation is expected to perform.</p><p>An NSOV-5 specifies the required functionality that an implementation of a service is expected to have – the implementation is represented in the NSV-1 and NSV-4.</p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="76e77d8f-764a-4b25-be53-ca8af682ee6c"><ac:parameter ac:name="id">764190440</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Function" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Function Action" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Function Edge" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Method" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Parameter" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Interface" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="630612f5-14ca-485c-b193-badfc5a4a12a" /></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Creating Process Flow Diagrams From Compositions or Aggregations Defined in Process Diagrams" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732857 space=MT version=1 -->
## PAGE 03563: (2026x) NSV-1 System Interface Description

- page_id: `272732857`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732857/2026x+NSV-1+System+Interface+Description
- version_number: 1
- version_date: `2025-11-25T13:41:21.038+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

765149297

765149299

765149298

**Description**

System interface description (NSV-1) addresses the composition and interaction of resources. For NMM, NSV-1 incorporates the human elements Posts, Organizations, and Roles.

A resource interaction is a simplified representation of a pathway or network, usually depicted graphically as a connector (for example, a line with possible amplifying information).

In addition, the Capability Configuration concept is used as a wrapper to bring together resources to satisfy a Capability.

**Implementation**

NSV-1 can be represented using the following:

- NSV-1 diagram, which is based on the UML Class diagram.
- NSV-1 diagram, which is based on the UML Composite Structure diagram.
- UML Class diagram.
- UML Composite Structure diagram.
- SysML Block Definition diagram.
- SysML Internal Block diagram.

**Sample**

[IMAGE alt='' src='']

###### NSV-1 System Interface Description

[IMAGE alt='' src='']

###### NSV-1 System Interface Internal Description

**Related views**

An NSV-1 can optionally be adorned with nodes initially specified in an NOV-2. This way, traceability can be established from the logical NOV structure to the physical NSV structure.

As depicted in the NSV-1, an interaction indicates that information passes from one resource to another. In the case of systems, this can be expanded into further detail in an NSV-2. Resource Exchanges are summarized in a Resource Exchanges Matrix (NSV-3).

The functions performed by the resources are specified in an NSV-4 Resource Functionality Description but may optionally be overlaid on the Resources in the NSV-1.

An Operational View (NOV) suite may specify a set of requirements – either as a specific operational plan or a scenario for procurement. As NOV-2 and NOV-5 specify the logical structure and behavior, NSV-1 and NSV-4 specify the physical structure and behavior (to the level of detail required by the architectural stakeholders).

765149296

**Related elements**

- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']
- [CONFLUENCE_PAGE title='Resource Role' space='MED']
- [CONFLUENCE_PAGE title='Resource Interface' space='MED']
- [CONFLUENCE_PAGE title='Resource Port' space='MED']
- [CONFLUENCE_PAGE title='Resource Connector' space='MED']
- [CONFLUENCE_PAGE title='Capability' space='MED']
- [CONFLUENCE_PAGE title='Exhibits' space='MED']
- [CONFLUENCE_PAGE title='Fielded Capability' space='MED']
- [CONFLUENCE_PAGE title='Resource Port' space='MED']
- [CONFLUENCE_PAGE title='Resource Exchange Kind' space='MED']
- [CONFLUENCE_PAGE title='Control' space='MED']
- [CONFLUENCE_PAGE title='Resource Information' space='MED']
- [CONFLUENCE_PAGE title='Natural Resource' space='MED']
- [CONFLUENCE_PAGE title='System in UAF' space='MED']

**Related procedures**

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="fdbe6fae-3657-486f-94f3-a53080982c3c"><ac:parameter ac:name="id">765149297</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="05cddadb-08c3-49f4-aaa1-489bb45b5a19"><ac:parameter ac:name="id">765149299</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b94a7d39-7c6a-48c6-b673-3117c17e8656"><ac:parameter ac:name="id">765149298</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>System interface description (NSV-1) addresses the composition and interaction of resources. For NMM, NSV-1 incorporates the human elements Posts, Organizations, and Roles.</p><p>A resource interaction is a simplified representation of a pathway or network, usually depicted graphically as a connector (for example, a line with possible amplifying information).</p><p>In addition, the Capability Configuration concept is used as a wrapper to bring together resources to satisfy a Capability.</p><p><strong>Implementation</strong></p><p>NSV-1 can be represented using the following:</p><ul><li>NSV-1 diagram, which is based on the UML Class diagram.</li><li>NSV-1 diagram, which is based on the UML Composite Structure diagram.</li><li>UML Class diagram.</li><li>UML Composite Structure diagram.</li><li>SysML Block Definition diagram.</li><li>SysML Internal Block diagram.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsv_1.png"><ri:page ri:content-title="(2026x) NSV-1 System Interface Description" /></ri:attachment></ac:image></p><h6>NSV-1 System Interface Description</h6><p><ac:image><ri:attachment ri:filename="Nvs_1_internal.png"><ri:page ri:content-title="(2026x) NSV-1 System Interface Description" /></ri:attachment></ac:image></p><h6>NSV-1 System Interface Internal Description</h6><p><strong>Related views</strong></p><p>An NSV-1 can optionally be adorned with nodes initially specified in an NOV-2. This way, traceability can be established from the logical NOV structure to the physical NSV structure.</p><p>As depicted in the NSV-1, an interaction indicates that information passes from one resource to another. In the case of systems, this can be expanded into further detail in an NSV-2. Resource Exchanges are summarized in a Resource Exchanges Matrix (NSV-3).</p><p>The functions performed by the resources are specified in an NSV-4 Resource Functionality Description but may optionally be overlaid on the Resources in the NSV-1.</p><p>An Operational View (NOV) suite may specify a set of requirements – either as a specific operational plan or a scenario for procurement. As NOV-2 and NOV-5 specify the logical structure and behavior, NSV-1 and NSV-4 specify the physical structure and behavior (to the level of detail required by the architectural stakeholders).</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8174705f-5047-4e6c-9841-59f6acf26b40"><ac:parameter ac:name="id">765149296</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Role" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Interface" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Port" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Connector" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Exhibits" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Fielded Capability" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Port" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Exchange Kind" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Control" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Information" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Natural Resource" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="System in UAF" /></ac:link></li></ul><p><strong>Related procedures</strong></p><p><strong><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="c32f793b-1cd6-4bbb-a807-5563ed249c7b" /></strong></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732971 space=MT version=1 -->
## PAGE 03564: (2026x) NSV-10a Systems Parametric

- page_id: `272732971`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732971/2026x+NSV-10a+Systems+Parametric
- version_number: 1
- version_date: `2025-11-25T13:41:36.613+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint > (2026x) NSV-10a Systems Rule Model
- labels: ['msosa']

### NORMALIZED CONTENT

498158595

498158597

498158596

**Description**

A Parametric diagram includes the usage of a [CONFLUENCE_PAGE title='Constraint Block' space='MED'] to constrain the properties of another Capability Configuration. It contains [CONFLUENCE_PAGE title='Constraint Property' space='MED'] and constraint parameters as well as other properties from within that internal block context. All properties displayed, other than the constraints themselves, must either be bound directly to a constraint parameter or contain a property that is bound to a constraint parameter (through any number of containment levels). A constraint block generally contain many constraints, each of them containing many constraint parameters.

498158594

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Working with Parametric diagram' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a29407c4-6498-4598-b0cf-b50ff9d76edf"><ac:parameter ac:name="id">498158595</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="555c05b8-a5f3-403f-9993-125a4d8205b9"><ac:parameter ac:name="id">498158597</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="157914c0-5b70-4049-ac99-e16140e95218"><ac:parameter ac:name="id">498158596</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>A Parametric diagram includes the usage of a <ac:link><ri:page ri:space-key="MED" ri:content-title="Constraint Block" /><ac:plain-text-link-body><![CDATA[constraint block]]></ac:plain-text-link-body></ac:link> to constrain the properties of another Capability Configuration. It contains <ac:link><ri:page ri:space-key="MED" ri:content-title="Constraint Property" /><ac:plain-text-link-body><![CDATA[constraint properties]]></ac:plain-text-link-body></ac:link> and constraint parameters as well as other properties from within that internal block context. All properties displayed, other than the constraints themselves, must either be bound directly to a constraint parameter or contain a property that is bound to a constraint parameter (through any number of containment levels). A constraint block generally contain many constraints, each of them containing many constraint parameters.</p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4182ff6e-b8c6-4b39-9efc-d14eb73f6a06"><ac:parameter ac:name="id">498158594</ac:parameter><ac:rich-text-body><p><strong>Related procedures</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Working with Parametric diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732955 space=MT version=1 -->
## PAGE 03565: (2026x) NSV-10a Systems Rule Model

- page_id: `272732955`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732955/2026x+NSV-10a+Systems+Rule+Model
- version_number: 1
- version_date: `2025-11-25T13:41:32.113+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

768201070

768201072

768201071

**Description**

The purpose the NSV-10a Systems Rule Model is to specify functional and non-functional constraints on the implementation aspects of the architecture (for example, the structural and behavioral elements of the NSV viewpoint). NSV-10a describes constraints on the resources, functions, data and ports that make up the NSV physical architecture.

The constraints are specified in text and may be functional or structural (for example, non-functional).

**Implementation**

NSV-10a can be represented using:

- NSV-10a table.
- [CONFLUENCE_PAGE title='(2026x) NSV-10a Systems Parametric' space=''] .
- NSV-10a spreadsheet report.

**Sample**

[IMAGE alt='' src='']

###### NSV-10a Systems Rule Model

**Related views**

NSV-10a describes constraints on resources, functions, and data that make up the NSV physical architecture. Where a Resource Constraint is based on some standard, then that standard should be listed in the Standards Profile (NTV-1).

**Constraint owner**

You can choose where all the constraints will be stored through the**Project Options**.

To select a constraint owner

1. In the main menu, click Options > Project . The Project Options dialog opens.
2. Go to General > UAF , and in the Default Constraint Owners property group, choose a needed owner.

768201069

**Related elements**

- [CONFLUENCE_PAGE title='Resource Constraint' space='MED']
- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']
- [CONFLUENCE_PAGE title='Function' space='MED']
- [CONFLUENCE_PAGE title='Resource Exchange Kind' space='MED']
- [CONFLUENCE_PAGE title='Resource Information' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="bca72abc-dae5-4d94-9551-8bf4b6a4e2b3"><ac:parameter ac:name="id">768201070</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="06d5f81e-3883-4c7a-a46a-ed3ad1ca549f"><ac:parameter ac:name="id">768201072</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="204801a7-b490-4fff-9997-45740e8e5c69"><ac:parameter ac:name="id">768201071</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The purpose the NSV-10a Systems Rule Model is to specify functional and non-functional constraints on the implementation aspects of the architecture (for example, the structural and behavioral elements of the NSV viewpoint). NSV-10a describes constraints on the resources, functions, data and ports that make up the NSV physical architecture.</p><p>The constraints are specified in text and may be functional or structural (for example, non-functional).</p><p><strong>Implementation</strong></p><p>NSV-10a can be represented using:</p><ul><li>NSV-10a table.</li><li><ac:link><ri:page ri:content-title="(2026x) NSV-10a Systems Parametric" /><ac:plain-text-link-body><![CDATA[NSV-10a Systems Parametric diagram]]></ac:plain-text-link-body></ac:link>.</li><li>NSV-10a spreadsheet report.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsv_10a.png"><ri:page ri:content-title="(2026x) NSV-10a Systems Rule Model" /></ri:attachment></ac:image></p><h6>NSV-10a Systems Rule Model</h6><p><strong>Related views</strong></p><p>NSV-10a describes constraints on resources, functions, and data that make up the NSV physical architecture. Where a Resource Constraint is based on some standard, then that standard should be listed in the Standards Profile (NTV-1).</p><p style=""><strong>Constraint owner</strong></p><p style="">You can choose where all the constraints will be stored through the<span> </span><strong>Project Options</strong>.</p><p style="">To select a constraint owner</p><hr style="" /><ol style=""><li>In the main menu, click<span> </span><strong>Options</strong><span> </span>&gt;<span> </span><strong>Project</strong>. The<span> </span><strong>Project Options</strong><span> </span>dialog opens.</li><li>Go to<span> </span><strong>General</strong><span> </span>&gt;<span> </span><strong>UAF</strong>, and in the<span> </span><strong>Default Constraint Owners</strong><span> </span>property group, choose a needed owner.</li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5d8af39a-66c1-40e0-acc1-191a1a47696f"><ac:parameter ac:name="id">768201069</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Constraint" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Function" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Exchange Kind" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Information" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="aa420a73-31e2-4bda-9bb0-8584d47d1029" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272733405 space=MT version=1 -->
## PAGE 03566: (2026x) NSV-10b Systems State Transition Description

- page_id: `272733405`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733405/2026x+NSV-10b+Systems+State+Transition+Description
- version_number: 1
- version_date: `2025-11-25T13:42:23.280+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

**Description**

The NATO Systems State Transition Description (NSV-10b) is a graphical method of describing a ResourceType’s (or Function’s) response to various events by changing its state. The diagram basically represents the sets of events to which the subjects will respond (by taking an action to move to a new state) as a function of its current state. Each transition specifies an event and an action.

**Implementation**

NSV-10b can be represented using a NSV-10b diagram which is based on the UML State Machine diagram.

**Sample**

[IMAGE alt='' src='']

###### NSV-10b Systems State Transition Description

**Related views**

An NSV-10a describes constraints on resources, functions, and data that make up the NSV physical architecture.

Where a Resource Constraint is based on some standard, then that standard should be listed in the Standards Profile (NTV-1).

**Related elements**

- [CONFLUENCE_PAGE title='Resource State Description' space='MED']
- [CONFLUENCE_PAGE title='State' space='MED']
- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Allocate Activities to State Internal Behaviors' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>The NATO Systems State Transition Description (NSV-10b) is a graphical method of describing a ResourceType’s (or Function’s) response to various events by changing its state. The diagram basically represents the sets of events to which the subjects will respond (by taking an action to move to a new state) as a function of its current state. Each transition specifies an event and an action.</p><p><strong>Implementation</strong></p><p>NSV-10b can be represented using a NSV-10b diagram which is based on the UML State Machine diagram.</p><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsv_10b.png"><ri:page ri:content-title="(2026x) NSV-10b Systems State Transition Description" /></ri:attachment></ac:image></p><h6>NSV-10b Systems State Transition Description</h6><p><strong>Related views</strong></p><p>An NSV-10a describes constraints on resources, functions, and data that make up the NSV physical architecture.</p><p>Where a Resource Constraint is based on some standard, then that standard should be listed in the Standards Profile (NTV-1).</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related elements</strong></p><ul><li data-uuid="2bccfa85-5ec7-4dac-9ecc-cbb132098100"><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource State Description" /></ac:link></li><li data-uuid="f554129b-c68b-4ee5-a62c-17cee4bb94b4"><ac:link><ri:page ri:space-key="MED" ri:content-title="State" /></ac:link></li><li data-uuid="888dc1ec-5128-4d7c-bb61-1d45fafa69e8"><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li data-uuid="b042d332-e4db-4cc8-b581-078af478ae02"><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li data-uuid="a2bc65d5-c95c-4e79-9329-a94b423d2be1"><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li data-uuid="7a4a0b10-4cb3-4eef-8cb0-20f738eb9476"><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li data-uuid="24040f0d-8db0-46f5-890f-7d1e05a63960"><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li></ul><p><strong>Related procedures</strong></p><ul><li data-uuid="b03dfc41-f657-43aa-8f45-7e7706a2919f"><ac:link><ri:page ri:content-title="(2026x) Allocate Activities to State Internal Behaviors" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272738150 space=MT version=1 -->
## PAGE 03567: (2026x) NSV-10c Systems Event-Trace Description

- page_id: `272738150`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738150/2026x+NSV-10c+Systems+Event-Trace+Description
- version_number: 1
- version_date: `2025-11-25T13:49:45.415+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

**Description**

The NATO Systems Event-Trace Description provides a time-ordered examination of the interactions between functional resources. Each event-trace diagram will have an accompanying description that defines the particular scenario or situation. The NSV-10c is valuable for moving to the next level of detail from the initial solution design, to help define a sequence of functions and system data interfaces, and to ensure that each participating Resource or System Port role has the necessary information it needs, at the right time, in order to perform its assigned functionality.

**Implementation**

NSV-10c can be represented using a NSV-10c diagram which is based on the UML Sequence diagram.

**Sample**

**[IMAGE alt='' src='']**

###### NSV-10c Systems Event-Trace Description

You can also create NSV-10c Business Process Diagram (BPD). In order to do that, use the Cameo Business Modeler plugin. For more information on how to model the business process diagram, see [CONFLUENCE_PAGE title='(2026x) BPMN Process Diagram' space=''].

**Related views**

The NSV-10c is typically used in conjunction with the Resource State Transition Description (NSV-10b) to describe the dynamic behavior of resources.

The data content of ‘messages’ that connect life-lines in an NSV-10c View Product may be related, in modelling terms, with resource interactions (NSV-1, 3), data flows (NSV-4, 6) and data schema entities (NSV-11) modeled in other views.

**Related elements**

- [CONFLUENCE_PAGE title='Interaction' space='MED']
- [CONFLUENCE_PAGE title='Resource Message' space='MED']
- [CONFLUENCE_PAGE title='Resource Role' space='MED']
- [CONFLUENCE_PAGE title='Resource Exchange Kind' space='MED']
- [CONFLUENCE_PAGE title='Resource Information' space='MED']
- [CONFLUENCE_PAGE title='Natural Resource' space='MED']
- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>The NATO Systems Event-Trace Description provides a time-ordered examination of the interactions between functional resources. Each event-trace diagram will have an accompanying description that defines the particular scenario or situation. The NSV-10c is valuable for moving to the next level of detail from the initial solution design, to help define a sequence of functions and system data interfaces, and to ensure that each participating Resource or System Port role has the necessary information it needs, at the right time, in order to perform its assigned functionality.</p><p><strong>Implementation</strong></p><p>NSV-10c can be represented using a NSV-10c diagram which is based on the UML Sequence diagram.</p><p><strong>Sample</strong></p><p><strong><ac:image><ri:attachment ri:filename="Nsv_10c.png"><ri:page ri:content-title="(2026x) NSV-10c Systems Event-Trace Description" /></ri:attachment></ac:image></strong></p><h6>NSV-10c Systems Event-Trace Description</h6><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2a264c11-eb3d-4814-afd7-cb081162830c"><ac:rich-text-body><p>You can also create NSV-10c Business Process Diagram (BPD). In order to do that, use the Cameo Business Modeler plugin. For more information on how to model the business process diagram, see <ac:link><ri:page ri:content-title="(2026x) BPMN Process Diagram" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><strong>Related views</strong></p><p>The NSV-10c is typically used in conjunction with the Resource State Transition Description (NSV-10b) to describe the dynamic behavior of resources.</p><p>The data content of ‘messages’ that connect life-lines in an NSV-10c View Product may be related, in modelling terms, with resource interactions (NSV-1, 3), data flows (NSV-4, 6) and data schema entities (NSV-11) modeled in other views.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related elements</strong></p><ul><li data-uuid="701feaf8-5c6d-4d3e-a63c-fba55412e2bb"><ac:link><ri:page ri:space-key="MED" ri:content-title="Interaction" /></ac:link></li><li data-uuid="77f4cd42-6b0a-4a07-a6d7-1bb390649569"><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Message" /></ac:link></li><li data-uuid="90fa4333-eaa1-4073-bcd4-9c1cd7f11239"><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Role" /></ac:link></li><li data-uuid="70373582-0298-4ce5-9316-fc26e61e2d78"><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Exchange Kind" /></ac:link></li><li data-uuid="7c7c62cf-2dd7-4b8d-b73d-fc7772df13e9"><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Information" /></ac:link></li><li data-uuid="ff351fd8-6880-4e61-b48f-65b71b052921"><ac:link><ri:page ri:space-key="MED" ri:content-title="Natural Resource" /></ac:link></li><li data-uuid="418be055-c0c2-42ee-95e2-ea2d6a85bcd3"><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li data-uuid="38dee76a-d69d-424d-a858-2dda48c1709b"><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li data-uuid="ec948f10-57a6-4c93-9b5a-cefb613abd0c"><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li data-uuid="e492b54e-76e3-4217-96fc-946098d30b6a"><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li data-uuid="fdbcf40d-dd34-45eb-827c-2b31ade6d319"><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272738144 space=MT version=1 -->
## PAGE 03568: (2026x) NSV-11 Systems Data Model

- page_id: `272738144`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738144/2026x+NSV-11+Systems+Data+Model
- version_number: 1
- version_date: `2025-11-25T13:49:44.462+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

768604598

768604600

768604599

**Description**

The NSV-11 View defines the structure of the various kinds of system data that are utilized by the systems in the Architecture. The Physical Schema is one of the Architectural Products closest to actual system design in the Framework. NSV-11 is used to describe how the information represented in the Information Model (NOV-7) is actually implemented. While the mapping between the logical and physical data models is relatively straightforward, the relationship between the components of each model (for example, entity types in the logical model versus relational tables in the physical model) is frequently one-to-many or many-to-many.

**Cameo Data Modeler plugin integration**

You can use the Entity Relationship diagram for conceptual, logical, and physical data modeling in NSV-11. It supports the information engineering notation within this view.

Note that the Entity Relationship diagram is supported in SV-11. It allows for using the information engineering notation within this view.

**Implementation**

NSV-11 can be represented using:

- NSV-11 diagram which is based on the UML Class diagram.
- UML Class diagram.
- SysML Block Definition diagram.

**Sample**

[IMAGE alt='' src='']

###### NSV-11 Physical Schema

**Related views**

The Physical Schema is one of the Architectural Products closest to actual system design in the Framework. An NSV-11 is used to describe how information represented in the Information Model (NOV-7) is actually implemented.

768604597

**Related elements**

- Property
- [CONFLUENCE_PAGE title='(2026x) Association' space='']
- [CONFLUENCE_PAGE title='Resource Information' space='MED']
- [CONFLUENCE_PAGE title='Information Model' space='MED']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a3ef7d08-6998-4842-bbf4-a310261216a8"><ac:parameter ac:name="id">768604598</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b7d5e422-6886-4736-adbc-7d7facc4d894"><ac:parameter ac:name="id">768604600</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="60f82cb1-b940-4ff0-b05a-b7d933a8dbf4"><ac:parameter ac:name="id">768604599</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NSV-11 View defines the structure of the various kinds of system data that are utilized by the systems in the Architecture. The Physical Schema is one of the Architectural Products closest to actual system design in the Framework. NSV-11 is used to describe how the information represented in the Information Model (NOV-7) is actually implemented. While the mapping between the logical and physical data models is relatively straightforward, the relationship between the components of each model (for example, entity types in the logical model versus relational tables in the physical model) is frequently one-to-many or many-to-many.</p><p><strong>Cameo Data Modeler plugin integration</strong></p><p>You can use the Entity Relationship diagram for conceptual, logical, and physical data modeling in NSV-11. It supports the information engineering notation within this view.</p><p>Note that the Entity Relationship diagram is supported in SV-11. It allows for using the information engineering notation within this view.</p><p><strong>Implementation</strong></p><p>NSV-11 can be represented using:</p><ul><li>NSV-11 diagram which is based on the UML Class diagram.</li><li>UML Class diagram.</li><li>SysML Block Definition diagram.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsv_11.png"><ri:page ri:content-title="(2026x) NSV-11 Systems Data Model" /></ri:attachment></ac:image></p><h6>NSV-11 Physical Schema</h6><p><strong>Related views</strong></p><p>The Physical Schema is one of the Architectural Products closest to actual system design in the Framework. An NSV-11 is used to describe how information represented in the Information Model (NOV-7) is actually implemented.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="12536a8a-86ec-4aac-a23c-9cb8263a2374"><ac:parameter ac:name="id">768604597</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li>Property</li><li><ac:link><ri:page ri:content-title="(2026x) Association" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Information" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Information Model" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732966 space=MT version=1 -->
## PAGE 03569: (2026x) NSV-12 Service Provision

- page_id: `272732966`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732966/2026x+NSV-12+Service+Provision
- version_number: 1
- version_date: `2025-11-25T13:41:35.905+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

768735273

768735275

768735274

**Description**

This view is used to describe how a service is implemented by one or more systems. A particular implementation of a service can be seen as a capability configuration that is associated with this service. By providing this information, a clear connection between a service, as described in the NSOV diagrams, and systems that implement it can be defined.

**Implementation**

NSV-12 can be represented using a NSV-12 diagram which is an editable Dependency Matrix. The Service Interfaces will be used as the row elements and the Resources will be used as the column elements.

**Sample**

**[IMAGE alt='' src='']**

###### NSV-12 Service Provision

**Related views**

The service attributes defined in NSOV-1 can be given values in an NSV-12 and related to the environment under which those values are true.

768735272

**Related elements**

- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']
- [CONFLUENCE_PAGE title='Service Interface' space='MED']
- [CONFLUENCE_PAGE title='Resource Port' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="c5abb6d8-2ee8-4aef-b839-f47cc11d6436"><ac:parameter ac:name="id">768735273</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="e6b8a321-f084-4aa1-a858-3d626adfac95"><ac:parameter ac:name="id">768735275</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="36913e61-9005-4c6d-a59b-909b72a81732"><ac:parameter ac:name="id">768735274</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>This view is used to describe how a service is implemented by one or more systems. A particular implementation of a service can be seen as a capability configuration that is associated with this service. By providing this information, a clear connection between a service, as described in the NSOV diagrams, and systems that implement it can be defined.</p><p><strong>Implementation</strong></p><p>NSV-12 can be represented using a NSV-12 diagram which is an editable Dependency Matrix. The Service Interfaces will be used as the row elements and the Resources will be used as the column elements.</p><p><strong>Sample</strong></p><p><strong><ac:image><ri:attachment ri:filename="Nsv_12.png"><ri:page ri:content-title="(2026x) NSV-12 Service Provision" /></ri:attachment></ac:image></strong></p><h6>NSV-12 Service Provision</h6><p><strong>Related views</strong></p><p>The service attributes defined in NSOV-1 can be given values in an NSV-12 and related to the environment under which those values are true.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f45c5562-f562-45e4-a6cc-22f2404b94a9"><ac:parameter ac:name="id">768735272</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Service Interface" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Port" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="010f5368-54d9-47ad-8c31-012ad08df440" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732870 space=MT version=1 -->
## PAGE 03570: (2026x) NSV-2 System Communications Description

- page_id: `272732870`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732870/2026x+NSV-2+System+Communications+Description
- version_number: 1
- version_date: `2025-11-25T13:41:22.545+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

765711401

765711403

765711402

**Description**

NSV-2 represents the specific communication systems pathways or networks and the details of their configurations through which the nodes and systems interface. This subview focuses on the physical, infrastructural, communications aspects of the system interfaces as defined in NSV-1. The graphical presentation and/or supporting text should describe all pertinent communications attributes, such as geographic location, bandwidth constraints, security, encryption, standards and protocols.

**Implementation**

NSV-2 can be represented using:

- NSV-2 diagram which is based on the UML Class diagram.
- NSV-2 diagram which is based on the UML Composite Structure diagram.
- UML Class diagram.
- UML Composite Structure diagram.
- SysML Block Definition diagram.
- SysML Internal Block diagram.

**Sample**

[IMAGE alt='' src='']

###### NSV-2 System Internal Communications Description

**Related views**

Any protocol and Standard referred to in an NSV-2 diagram must be defined in the NTV-1 Technical Standards Profile.

765711399

**Related elements**

- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']
- [CONFLUENCE_PAGE title='Resource Port' space='MED']
- [CONFLUENCE_PAGE title='Resource Connector' space='MED']
- [CONFLUENCE_PAGE title='Resource Role' space='MED']
- [CONFLUENCE_PAGE title='Resource Interface' space='MED']
- [CONFLUENCE_PAGE title='Protocol' space='MED']
- [CONFLUENCE_PAGE title='Standard' space='MED']
- [CONFLUENCE_PAGE title='Resource Port' space='MED']
- [CONFLUENCE_PAGE title='Resource Exchange Kind' space='MED']
- [CONFLUENCE_PAGE title='Control' space='MED']
- [CONFLUENCE_PAGE title='Resource Information' space='MED']
- [CONFLUENCE_PAGE title='Natural Resource' space='MED']
- [CONFLUENCE_PAGE title='System in UAF' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ca35d602-eb88-4769-ba6e-7679f7d892f6"><ac:parameter ac:name="id">765711401</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b800166b-c9df-4986-a97a-d44d39997825"><ac:parameter ac:name="id">765711403</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="bb6e8669-6baa-4cec-9592-bb5bced9dec5"><ac:parameter ac:name="id">765711402</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>NSV-2 represents the specific communication systems pathways or networks and the details of their configurations through which the nodes and systems interface. This subview focuses on the physical, infrastructural, communications aspects of the system interfaces as defined in NSV-1. The graphical presentation and/or supporting text should describe all pertinent communications attributes, such as geographic location, bandwidth constraints, security, encryption, standards and protocols.</p><p><strong>Implementation</strong></p><p>NSV-2 can be represented using:</p><ul><li>NSV-2 diagram which is based on the UML Class diagram.</li><li>NSV-2 diagram which is based on the UML Composite Structure diagram.</li><li>UML Class diagram.</li><li>UML Composite Structure diagram.</li><li>SysML Block Definition diagram.</li><li>SysML Internal Block diagram.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsv_2.png"><ri:page ri:content-title="(2026x) NSV-2 System Communications Description" /></ri:attachment></ac:image></p><h6>NSV-2 System Internal Communications Description</h6><p><strong>Related views</strong></p><p>Any protocol and Standard referred to in an NSV-2 diagram must be defined in the NTV-1 Technical Standards Profile.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="34d3df2b-095c-49da-a9e8-023bb7a9d076"><ac:parameter ac:name="id">765711399</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Port" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Connector" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Role" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Interface" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Protocol" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Standard" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Port" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Exchange Kind" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Control" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Information" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Natural Resource" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="System in UAF" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="c4aa02e0-099f-487b-b932-1224750d62d5" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272732890 space=MT version=1 -->
## PAGE 03571: (2026x) NSV-3 System to System Matrix

- page_id: `272732890`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272732890/2026x+NSV-3+System+to+System+Matrix
- version_number: 1
- version_date: `2025-11-25T13:41:24.327+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

765860130

765860132

765860131

**Description**

The NATO System to System Matrix provides a tabular summary of the resource interactions specified in the NSV1 for the Architecture. An NSV-3 Product allows a quick overview of all the resource interactions specified in one or more NSV-1 diagrams. The NSV-3 can be organized in a number of ways to emphasize the association of groups of system pairs in context with the architecture’s purpose.

**Implementation**

NSV-3 can be represented using a NSV-3 diagram which is an editable Dependency Matrix. Rows and Columns in the matrix represent the Resources.

**Sample**

**[IMAGE alt='' src='']**

###### NSV-3 System to System Matrix

****

**Related views**

NSV-3 is a summary description of the resource interactions that are identified in NSV-1.

765860129

**Related elements**

- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']
- [CONFLUENCE_PAGE title='Resource Information' space='MED']
- [CONFLUENCE_PAGE title='Resource Exchange Kind' space='MED']
- [CONFLUENCE_PAGE title='Natural Resource' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Using Implied Relations' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="326af6b9-54d6-4606-ae30-3aba45600dc4"><ac:parameter ac:name="id">765860130</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="36a5e2a2-b874-4a33-bbf1-8c0411456497"><ac:parameter ac:name="id">765860132</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9f9dd9a7-7a5f-4566-a461-575c02a122f1"><ac:parameter ac:name="id">765860131</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NATO System to System Matrix provides a tabular summary of the resource interactions specified in the NSV1 for the Architecture. An NSV-3 Product allows a quick overview of all the resource interactions specified in one or more NSV-1 diagrams. The NSV-3 can be organized in a number of ways to emphasize the association of groups of system pairs in context with the architecture’s purpose.</p><p><strong>Implementation</strong></p><p>NSV-3 can be represented using a NSV-3 diagram which is an editable Dependency Matrix. Rows and Columns in the matrix represent the Resources.</p><p><strong>Sample</strong></p><p><strong><ac:image><ri:attachment ri:filename="Nsv_3.jpg"><ri:page ri:content-title="(2026x) NSV-3 System to System Matrix" /></ri:attachment></ac:image></strong></p><h6>NSV-3 System to System Matrix</h6><p><strong><br /></strong></p><p><strong>Related views</strong></p><p>NSV-3 is a summary description of the resource interactions that are identified in NSV-1.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7c8fd135-b7f7-4f12-8dfc-ec6651df9077"><ac:parameter ac:name="id">765860129</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Information" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Exchange Kind" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Natural Resource" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d9363ca3-6418-4ac1-8c4a-469e61db4f90" /></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Using Implied Relations" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272730126 space=MT version=1 -->
## PAGE 03572: (2026x) NSV-4 System Functionality Description

- page_id: `272730126`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730126/2026x+NSV-4+System+Functionality+Description
- version_number: 1
- version_date: `2025-11-25T13:36:33.987+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

766168444

766168446

766168445

**Description**

The NATO System Functionality Descriptions (NSV-4) address human and system functionality. The primary purposes of NSV-4 are to develop a clear description of the necessary data flows that are input (consumed) by and output (produced) by each resource, ensure that the functional connectivity is complete, and ensure that the functional decomposition reaches an appropriate level of detail. The System Functionality Description provides detailed information regarding the allocation of functions to resources and flow of data between functions. The NSV-4 is the systems view counterpart.

**Implementation**

NSV-4 can be represented using:

- NSV-4 diagram for Function hierarchies. This diagram is based on the UML Class diagram.
- NSV-4 diagram for Function flows. This diagram is based on the UML Activity diagram.
- UML Class diagram.
- UML Activity diagram.
- SysML Block diagram.
- SysML Activity diagram.

**Sample**

[IMAGE alt='' src='']

###### Fragment of NSV-4 System Functionality Description Flow

You can also create NSV-4 Business Process Diagram (BPD). In order to do that, use the Cameo Business Modeler plugin. For more information on how to model the business process diagram, see [CONFLUENCE_PAGE title='(2026x) BPMN Process Diagram' space=''].

**Related views**

An NSV-4 is the behavioral counterpart to the NSV-1 (in the same way that NOV-5 is the structural counterpart to NOV-2).

The functions are likely to be related to Operational Activities captured in an NOV-5. Although there is a correlation between the Operational Activity Model (NOV-5) and the functional hierarchy of NSV-4, it need not be a one-toone mapping, hence, the need for a Function to Operational Activity Traceability Matrix (NSV-5), which provides that mapping.

766168443

**Related elements**

- [CONFLUENCE_PAGE title='Function' space='MED']
- [CONFLUENCE_PAGE title='Operational Activity' space='MED']
- [CONFLUENCE_PAGE title='Standard Operational Activity' space='MED']
- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']
- [CONFLUENCE_PAGE title='Is Capable To Perform' space='MED']
- [CONFLUENCE_PAGE title='Function Action' space='MED']
- [CONFLUENCE_PAGE title='Function Edge' space='MED']
- [CONFLUENCE_PAGE title='Resource Exchange Kind' space='MED']
- [CONFLUENCE_PAGE title='Resource Information' space='MED']
- [CONFLUENCE_PAGE title='Natural Resource' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Creating Process Flow Diagrams From Compositions or Aggregations Defined in Process Diagrams' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="54da28d9-765a-4214-8aa5-da2be2299c4c"><ac:parameter ac:name="id">766168444</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="0935ebce-abc7-4be5-bd59-1b4915cda423"><ac:parameter ac:name="id">766168446</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b75e86f3-bac6-4d92-9a77-72c8d704fbea"><ac:parameter ac:name="id">766168445</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NATO System Functionality Descriptions (NSV-4) address human and system functionality. The primary purposes of NSV-4 are to develop a clear description of the necessary data flows that are input (consumed) by and output (produced) by each resource, ensure that the functional connectivity is complete, and ensure that the functional decomposition reaches an appropriate level of detail. The System Functionality Description provides detailed information regarding the allocation of functions to resources and flow of data between functions. The NSV-4 is the systems view counterpart.</p><p><strong>Implementation</strong></p><p>NSV-4 can be represented using:</p><ul><li>NSV-4 diagram for Function hierarchies. This diagram is based on the UML Class diagram.</li><li>NSV-4 diagram for Function flows. This diagram is based on the UML Activity diagram.</li><li>UML Class diagram.</li><li>UML Activity diagram.</li><li>SysML Block diagram.</li><li>SysML Activity diagram.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsv_4.png"><ri:page ri:content-title="(2026x) NSV-4 System Functionality Description" /></ri:attachment></ac:image></p><h6>Fragment of NSV-4 System Functionality Description Flow</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="64a17d3d-4d07-4046-b031-0489791e76a7"><ac:rich-text-body><p>You can also create NSV-4 Business Process Diagram (BPD). In order to do that, use the Cameo Business Modeler plugin. For more information on how to model the business process diagram, see <ac:link><ri:page ri:content-title="(2026x) BPMN Process Diagram" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><strong>Related views</strong></p><p>An NSV-4 is the behavioral counterpart to the NSV-1 (in the same way that NOV-5 is the structural counterpart to NOV-2).</p><p>The functions are likely to be related to Operational Activities captured in an NOV-5. Although there is a correlation between the Operational Activity Model (NOV-5) and the functional hierarchy of NSV-4, it need not be a one-toone mapping, hence, the need for a Function to Operational Activity Traceability Matrix (NSV-5), which provides that mapping.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d7464a86-0fb4-48ec-95f2-f68a0d8d4eba"><ac:parameter ac:name="id">766168443</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Function" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Activity" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Standard Operational Activity" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Is Capable To Perform" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Function Action" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Function Edge" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Exchange Kind" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Information" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Natural Resource" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="5f760382-fea1-491c-9af8-e30afa22931d" /></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Creating Process Flow Diagrams From Compositions or Aggregations Defined in Process Diagrams" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272730154 space=MT version=1 -->
## PAGE 03573: (2026x) NSV-5 System Function to Operational Activity Traceability Matrix

- page_id: `272730154`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730154/2026x+NSV-5+System+Function+to+Operational+Activity+Traceability+Matrix
- version_number: 1
- version_date: `2025-11-25T13:36:35.041+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

766568710

766568712

766568711

**Description**

The NATO System Function to Operational Activity Traceability Matrix (NSV-5) addresses the linkage between functions described in an NSV-4 and Operational Activities specified in an NOV-5. The NSV-5 View depicts the mapping of functions (and, optionally, the functional resources that provide them) to operational activities and thus identifies the transformation of an operational need into a purposeful action performed by a system or solution.

**Implementation**

NSV-5 can be represented using a NSV-5 diagram which is an editable Dependency Matrix. The Functions will be used as the row elements and the Operational Activities will be used as the column elements.

**Sample**

[IMAGE alt='' src='']

###### NSV-5 System Function to Operational Activity Traceability Matrix

**Related views**

An NSV-5 addresses the linkage between the functions described in an NSV-4 and the Operational Activities specified in an NOV-5.

766568709

**Related elements**

- [CONFLUENCE_PAGE title='Function' space='MED']
- [CONFLUENCE_PAGE title='Operational Activity' space='MED']
- [CONFLUENCE_PAGE title='Implements' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Working with Resources to Capabilities Mapping matrix' space='']
- [CONFLUENCE_PAGE title='(2026x) Using Implied Relations' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="34f717ed-3b02-499b-9f72-1275c13335d9"><ac:parameter ac:name="id">766568710</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="836482f0-c58c-4037-97f2-61bccf6d71f0"><ac:parameter ac:name="id">766568712</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8c8368ff-e230-4056-a179-2b1e0a20ba87"><ac:parameter ac:name="id">766568711</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NATO System Function to Operational Activity Traceability Matrix (NSV-5) addresses the linkage between functions described in an NSV-4 and Operational Activities specified in an NOV-5. The NSV-5 View depicts the mapping of functions (and, optionally, the functional resources that provide them) to operational activities and thus identifies the transformation of an operational need into a purposeful action performed by a system or solution. </p><p><strong>Implementation</strong></p><p>NSV-5 can be represented using a NSV-5 diagram which is an editable Dependency Matrix. The Functions will be used as the row elements and the Operational Activities will be used as the column elements.</p><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsv_5.png"><ri:page ri:content-title="(2026x) NSV-5 System Function to Operational Activity Traceability Matrix" /></ri:attachment></ac:image></p><h6>NSV-5 System Function to Operational Activity Traceability Matrix</h6><p><strong>Related views</strong></p><p>An NSV-5 addresses the linkage between the functions described in an NSV-4 and the Operational Activities specified in an NOV-5.</p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1db63a18-8a73-41d9-9ba4-6c392a741cc3"><ac:parameter ac:name="id">766568709</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Function" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Operational Activity" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Implements" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="be521848-3946-4e8f-97d4-875d6dc43cb2" /></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Working with Resources to Capabilities Mapping matrix" /><ac:plain-text-link-body><![CDATA[Resources to Capabilities Mapping matrix]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Using Implied Relations" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272730161 space=MT version=1 -->
## PAGE 03574: (2026x) NSV-6 Systems Data Exchange Matrix

- page_id: `272730161`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730161/2026x+NSV-6+Systems+Data+Exchange+Matrix
- version_number: 1
- version_date: `2025-11-25T13:36:36.306+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

766732557

766732559

766732558

**Description**

The NATO Systems Data Exchange Matrix specifies the characteristics of the system data exchanged between systems. The focus is on data crossing the system boundary. An NSV-6 focuses on the specific aspects of the system data flow and the system data content in a tabular format.

The term System Data Exchange does not refer to one NMM element. A data exchange as described in NSV-6 is a combination of a System Port Connector and the Data Elements 
that flow across it. Any properties shown in an NSV-6 table will be properties of the System Port Connector.

**Implementation**

NSV-6 can be represented using:

- NSV-6 table.
- NSV-6 role-based table. A role-based table represents exchanges between Resource Roles(resource usages).
- NSV-6 spreadsheet report.

**Sample**

[IMAGE alt='' src='']

###### Systems Data Exchange Matrix

**Related views**

NSV-6 is the physical equivalent of the logical NOV-3 table and provides detailed information on the system connections which implement the information exchanges specified in an NOV-3.

766732556

**Related elements**

- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']
- [CONFLUENCE_PAGE title='Resource Information' space='MED']
- [CONFLUENCE_PAGE title='Resource Exchange Kind' space='MED']
- [CONFLUENCE_PAGE title='Natural Resource' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f1e2a4fc-8738-4ee4-a24d-37490ca068b3"><ac:parameter ac:name="id">766732557</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="cad4591c-3235-4c00-bc04-5895b8e6babb"><ac:parameter ac:name="id">766732559</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="76bc5be0-0a09-4f2e-8bc1-2707ba48e951"><ac:parameter ac:name="id">766732558</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NATO Systems Data Exchange Matrix specifies the characteristics of the system data exchanged between systems. The focus is on data crossing the system boundary. An NSV-6 focuses on the specific aspects of the system data flow and the system data content in a tabular format.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="93cc86eb-97cf-44d0-9175-2d7cc1992077"><ac:rich-text-body><p>The term System Data Exchange does not refer to one NMM element. A data exchange as described in NSV-6 is a combination of a System Port Connector and the Data Elements<br />that flow across it. Any properties shown in an NSV-6 table will be properties of the System Port Connector.</p></ac:rich-text-body></ac:structured-macro><p><strong>Implementation</strong></p><p>NSV-6 can be represented using:</p><ul><li>NSV-6 table.</li><li><p class="auto-cursor-target">NSV-6 role-based table.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dedc7abb-7cb5-485c-b2e4-3cb21736b6d2"><ac:rich-text-body>A role-based table represents exchanges between Resource Roles(resource usages).</ac:rich-text-body></ac:structured-macro></li><li>NSV-6 spreadsheet report.</li></ul><p class="auto-cursor-target"><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsv_6.png"><ri:page ri:content-title="(2026x) NSV-6 Systems Data Exchange Matrix" /></ri:attachment></ac:image></p><h6>Systems Data Exchange Matrix</h6><p><strong>Related views</strong></p><p>NSV-6 is the physical equivalent of the logical NOV-3 table and provides detailed information on the system connections which implement the information exchanges specified in an NOV-3.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="73e94de6-2528-4d7f-a77e-97e8121be618"><ac:parameter ac:name="id">766732556</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Information" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Exchange Kind" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Natural Resource" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="6fe1f672-1a61-4263-8b56-d56252cdc8f3" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272738108 space=MT version=1 -->
## PAGE 03575: (2026x) NSV-7 System Typical Quality Requirements Description

- page_id: `272738108`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738108/2026x+NSV-7+System+Typical+Quality+Requirements+Description
- version_number: 1
- version_date: `2025-11-25T13:49:39.698+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

767034446

767034448

767034447

**Description**

The NSV-7 is the System Typical Quality Requirements Matrix and depicts the performance characteristics of a Functional Resource (system, role, or capability configuration). The System Typical Quality Requirements Matrix expands on the information presented in an NSV-1 by depicting the characteristics of the Functional Resources shown in the NSV-1. The System Typical Quality Requirements Matrix View specifies qualitative and quantitative characteristics of functional resources and the performance parameters of each resource. The performance parameters are selected by the architect and end user community.

**Implementation**

NSV-7 can be represented using:

- NSV-7 typical parameters table
- NSV-7 actual parameters table
- [CONFLUENCE_PAGE title='(2026x) Working with hierarchical Typical Measurements table' space='']
- [CONFLUENCE_PAGE title='(2026x) Working with hierarchical Actual Measurements table' space='']
- NSV-7 actual parameters spreadsheet report

**Sample**

[IMAGE alt='' src='']

###### NSV-7 Typical table

[IMAGE alt='' src='']

###### NSV-7 Actual table

**Related views**

- [CONFLUENCE_PAGE title='(2026x) NSV-1 System Interface Description' space=''] . The Resource Performance Parameters Matrix expands on the information presented in an NSV-1 by depicting the characteristics of the Resources shown in the NSV-1.
- [CONFLUENCE_PAGE title='(2026x) NSV-2 System Communications Description' space='']. NSV-7 expands on the information presented in an NSV-2 by depicting the characteristics of the Resources shown in the NSV-2.

767034445

**Related elements**

- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='System in UAF' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']
- [CONFLUENCE_PAGE title='Measurement Set' space='MED']
- [CONFLUENCE_PAGE title='Actual Property Set' space='MED']
- [CONFLUENCE_PAGE title='Measurement' space='MED']
- [CONFLUENCE_PAGE title='Actual Measurement' space='MED']

**Related procedures**

- [CONFLUENCE_PAGE title='(2026x) Working with Typical Measurements table' space='']
- [CONFLUENCE_PAGE title='(2026x) Creating Actual Measurements table' space='']
- [CONFLUENCE_PAGE title='(2026x) Working with hierarchical Typical Measurements table' space='']
- [CONFLUENCE_PAGE title='(2026x) Working with hierarchical Actual Measurements table' space='']
- [CONFLUENCE_PAGE title='(2026x) Generating an Actual Measurements table from a Typical Measurements table' space='']
- [CONFLUENCE_PAGE title='(2026x) Generating document based reports' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="07071a0a-da60-4c4f-ac1a-aa78ee7d6b44"><ac:parameter ac:name="id">767034446</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="822f8f93-2779-4e9e-83b8-d9488bb8656b"><ac:parameter ac:name="id">767034448</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3aeff1da-f1d9-45f9-8697-a1bb00a2a0f5"><ac:parameter ac:name="id">767034447</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NSV-7 is the System Typical Quality Requirements Matrix and depicts the performance characteristics of a Functional Resource (system, role, or capability configuration). The System Typical Quality Requirements Matrix expands on the information presented in an NSV-1 by depicting the characteristics of the Functional Resources shown in the NSV-1. The System Typical Quality Requirements Matrix View specifies qualitative and quantitative characteristics of functional resources and the performance parameters of each resource. The performance parameters are selected by the architect and end user community.</p><p><strong>Implementation</strong></p><p>NSV-7 can be represented using:</p><ul><li>NSV-7 typical parameters table</li><li>NSV-7 actual parameters table</li><li><ac:link><ri:page ri:content-title="(2026x) Working with hierarchical Typical Measurements table" /><ac:plain-text-link-body><![CDATA[Hierarchical Typical Measurements table]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Working with hierarchical Actual Measurements table" /><ac:plain-text-link-body><![CDATA[Hierarchical Actual Measurements table]]></ac:plain-text-link-body></ac:link></li><li>NSV-7 actual parameters spreadsheet report</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Nsv_7_typical.png"><ri:page ri:content-title="(2026x) NSV-7 System Typical Quality Requirements Description" /></ri:attachment></ac:image></p><h6>NSV-7 Typical table</h6><p><ac:image><ri:attachment ri:filename="Nsv_7_actual.png"><ri:page ri:content-title="(2026x) NSV-7 System Typical Quality Requirements Description" /></ri:attachment></ac:image></p><h6>NSV-7 Actual table</h6><p><strong>Related views</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) NSV-1 System Interface Description" /></ac:link>. <span>The Resource Performance Parameters Matrix expands on the information presented in an NSV-1 by depicting the characteristics of the Resources shown in the NSV-1.</span></li><li><span><ac:link><ri:page ri:content-title="(2026x) NSV-2 System Communications Description" /></ac:link>. <span>NSV-7 expands on the information presented in an NSV-2 by depicting the characteristics of the Resources shown in the NSV-2.</span></span></li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="58cf0f90-7afb-43bb-8445-e86712a33282"><ac:parameter ac:name="id">767034445</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="System in UAF" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Measurement Set" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Property Set" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Measurement" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Actual Measurement" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Working with Typical Measurements table" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Creating Actual Measurements table" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Working with hierarchical Typical Measurements table" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Working with hierarchical Actual Measurements table" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Generating an Actual Measurements table from a Typical Measurements table" /></ac:link></li><li><ac:link><ri:page ri:content-title="(2026x) Generating document based reports" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272730168 space=MT version=1 -->
## PAGE 03576: (2026x) NSV-8 System Evolution Description

- page_id: `272730168`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730168/2026x+NSV-8+System+Evolution+Description
- version_number: 1
- version_date: `2025-11-25T13:36:36.923+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

767472191

767472193

767472192

**Description**

The NATO System Evolution Description view presents a whole lifecycle view of a resource, describing how its configuration changes over time. The NSV-8 provides an overview of how a capability configuration structure changes over time. It shows the structure of several capability configurations mapped against a timeline.

**Implementation**

SV-8 can be represented using a SV-8 diagram which is realized as a time based diagram.

**Sample**

**[IMAGE alt='' src='']**

###### NSV-8 System Evolution Description

**Related views**

| Icon | View | Relationship |
| --- | --- | --- |
|  |  |  |
|  |  | The changes depicted in the NSV-8 View are derived from the project milestones that are shown using an NPV-1. When the NPV-1 is used to model project timelines for capability acquisition projects, there is likely to be a close relationship between these two Views. |

767472189

**Related elements**

- [CONFLUENCE_PAGE title='Whole Life Configuration' space='MED']
- [CONFLUENCE_PAGE title='Version Of Configuration' space='MED']
- [CONFLUENCE_PAGE title='Resource Role' space='MED']
- [CONFLUENCE_PAGE title='Resource Interface' space='MED']

**Related procedures**

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="7362eaeb-db0b-420a-bd39-6fe787b0f516"><ac:parameter ac:name="id">767472191</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="1f8bc010-e40e-4837-883c-cc3a3674ed4c"><ac:parameter ac:name="id">767472193</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="06a5115b-e2db-4ec5-8cdc-80d197aa5bf8"><ac:parameter ac:name="id">767472192</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NATO System Evolution Description view presents a whole lifecycle view of a resource, describing how its configuration changes over time. The NSV-8 provides an overview of how a capability configuration structure changes over time. It shows the structure of several capability configurations mapped against a timeline.</p><p><strong>Implementation</strong></p><p>SV-8 can be represented using a SV-8 diagram which is realized as a time based diagram.</p><p><strong>Sample</strong></p><p><strong><ac:image><ri:attachment ri:filename="Nsv_8.png"><ri:page ri:content-title="(2026x) NSV-8 System Evolution Description" /></ri:attachment></ac:image></strong></p><h6>NSV-8 System Evolution Description</h6><p><strong>Related views</strong></p><table class="relative-table wrapped" style="width: 100.0%;"><colgroup><col style="width: 5.67376%;" /><col style="width: 23.7195%;" /><col style="width: 70.6068%;" /></colgroup><tbody><tr><th>Icon</th><th>View</th><th>Relationship</th></tr><tr><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="56"><ri:attachment ri:filename="Nsv_1_icon.png"><ri:page ri:content-title="(2026x) NSV-8 System Evolution Description" /></ri:attachment></ac:image></p></div></td><td><ac:link><ri:page ri:content-title="(2026x) NSV-1 System Interface Description" /></ac:link></td><td><br /></td></tr><tr><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="58"><ri:attachment ri:filename="Npv_1_icon.png"><ri:page ri:content-title="(2026x) NSV-8 System Evolution Description" /></ri:attachment></ac:image></p></div></td><td><ac:link><ri:page ri:content-title="(2026x) NPV-1 Programme Portfolio Relationships" /></ac:link></td><td><p>The changes depicted in the NSV-8 View are derived from the project milestones that are shown using an NPV-1. When the NPV-1 is used to model project timelines for capability acquisition projects, there is likely to be a close relationship between these two Views.</p></td></tr></tbody></table></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="608f90f6-330b-4d20-af56-2163b0264bb7"><ac:parameter ac:name="id">767472189</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Whole Life Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Version Of Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Role" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Interface" /></ac:link></li></ul><p><strong>Related procedures</strong></p><p><strong><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="6c07ef13-c456-40df-9865-065fcacf6346" /></strong></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272730236 space=MT version=1 -->
## PAGE 03577: (2026x) NSV-9 Technology Forecast

- page_id: `272730236`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730236/2026x+NSV-9+Technology+Forecast
- version_number: 1
- version_date: `2025-11-25T13:36:42.228+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Systems Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

767951070

767951072

767951071

**Description**

The NATO Technology Forecast defines the underlying current and expected supporting technologies and skills. Expected supporting technologies and skills are those that can be reasonably forecast given the current state of technology and skills, and expected improvements/ trends. New technologies and skills will be tied to specific time periods, which can correlate against the time periods used in NSV-8 milestones and linked to Enterprise Phases. NSV-9 provides a summary of emerging technologies and skills that impact the Resources that constitute the Architecture. The NSV-9 provides descriptions of relevant: emerging capabilities, industry trends, predictions of the availability and readiness of specific hardware and software products, and current and possible future skills In addition to providing an inventory of trends, capabilities and products, the NSV-9 also includes an assessment of the potential impact of these items on the architecture.

**Implementation**

NSV-9 can be represented using a NSV-9 table.

**Sample**

**[IMAGE alt='' src='']**

###### NSV-9 Technology Forecast****

**Related views**

The specific time periods selected (and the trends being tracked) will be coordinated with the Architecture transition plans (see NSV-8). That is, insertion of new capabilities and upgrading / re-training of existing resources may depend on or be driven by the availability of new technology and associated skills.

If standards are an integral part of the technologies important to the evolution of a given Architecture, then it may be convenient to combine the NSV-9 with the Technical Standards Forecast (NTV-2).

767951069

**Related elements**

- [CONFLUENCE_PAGE title='Forecast' space='MED']
- [CONFLUENCE_PAGE title='Resource Artifact' space='MED']
- [CONFLUENCE_PAGE title='Software' space='MED']
- [CONFLUENCE_PAGE title='Capability Configuration' space='MED']
- [CONFLUENCE_PAGE title='Organization' space='MED']
- [CONFLUENCE_PAGE title='Post' space='MED']
- [CONFLUENCE_PAGE title='Protocol' space='MED']
- [CONFLUENCE_PAGE title='Standard' space='MED']

**Related procedures**

**Related references**

- [CONFLUENCE_PAGE title='(2026x) Time Periods dialog' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="c841143b-cd1f-4461-90e6-79c6a9d7faa1"><ac:parameter ac:name="id">767951070</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d4428877-2a90-4567-9c29-41c8037b4957"><ac:parameter ac:name="id">767951072</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="171070fa-475a-4970-a7d0-7c1e928e0df9"><ac:parameter ac:name="id">767951071</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The NATO Technology Forecast defines the underlying current and expected supporting technologies and skills. Expected supporting technologies and skills are those that can be reasonably forecast given the current state of technology and skills, and expected improvements/ trends. New technologies and skills will be tied to specific time periods, which can correlate against the time periods used in NSV-8 milestones and linked to Enterprise Phases. NSV-9 provides a summary of emerging technologies and skills that impact the Resources that constitute the Architecture. The NSV-9 provides descriptions of relevant: emerging capabilities, industry trends, predictions of the availability and readiness of specific hardware and software products, and current and possible future skills In addition to providing an inventory of trends, capabilities and products, the NSV-9 also includes an assessment of the potential impact of these items on the architecture.</p><p><strong>Implementation</strong></p><p>NSV-9 can be represented using a NSV-9 table.</p><p><strong>Sample</strong></p><p><strong><ac:image><ri:attachment ri:filename="Nsv_9.png"><ri:page ri:content-title="(2026x) NSV-9 Technology Forecast" /></ri:attachment></ac:image></strong></p><h6>NSV-9 Technology Forecast<strong><br /></strong></h6><p><strong>Related views</strong></p><p>The specific time periods selected (and the trends being tracked) will be coordinated with the Architecture transition plans (see NSV-8). That is, insertion of new capabilities and upgrading / re-training of existing resources may depend on or be driven by the availability of new technology and associated skills.</p><p>If standards are an integral part of the technologies important to the evolution of a given Architecture, then it may be convenient to combine the NSV-9 with the Technical Standards Forecast (NTV-2).</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f9d570ce-7e15-4ffc-a0b3-6da96f1ff577"><ac:parameter ac:name="id">767951069</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Forecast" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Resource Artifact" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Software" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Capability Configuration" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Organization" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Post" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Protocol" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Standard" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="2761ff5d-c301-407c-a131-6d08881e0e6b" /></p><p><br /><strong>Related references</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Time Periods dialog" /></ac:link></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272730231 space=MT version=1 -->
## PAGE 03578: (2026x) NTV-1 Technical Standards Profile

- page_id: `272730231`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272730231/2026x+NTV-1+Technical+Standards+Profile
- version_number: 1
- version_date: `2025-11-25T13:36:41.710+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Technical Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

768880835

768880837

768880836

**Description**

A NTV-1 defines the technical and non-technical standards, guidance, and policy applicable to the architecture.

As well as identifying applicable technical standards, the NTV-1 may document the policies and standards that apply to the operational or business context.

**Implementation**

NTV-1 can be represented by a NTV-1 table.

**Sample**

###### [IMAGE alt='' src=''] 
NTV-1 Technical Standards Profile

**Related views**

A NTV-1 serves as the bridge between the NSV and NTV. The NSV-9 forecasts relate to the NTV-1 in that a timed technology forecast may contribute to the decision to retire or phase out the use of a certain standard in connection with a system element.

768880834

**Related elements**

- [CONFLUENCE_PAGE title='Standard' space='MED']
- [CONFLUENCE_PAGE title='Protocol' space='MED']

**Related procedures**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="39386701-62fb-428c-9953-4359a5c2ec3f"><ac:parameter ac:name="id">768880835</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="a3f5429d-c923-4719-b1e2-208e65f1c448"><ac:parameter ac:name="id">768880837</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="26e63079-e17f-46a7-b4f4-0f630d22340f"><ac:parameter ac:name="id">768880836</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>A NTV-1 defines the technical and non-technical standards, guidance, and policy applicable to the architecture.</p><p>As well as identifying applicable technical standards, the NTV-1 may document the policies and standards that apply to the operational or business context.</p><p><strong>Implementation</strong></p><p>NTV-1 can be represented by a NTV-1 table.</p><p><strong>Sample</strong></p><h6><ac:image><ri:attachment ri:filename="Ntv_1.png"><ri:page ri:content-title="(2026x) NTV-1 Technical Standards Profile" /></ri:attachment></ac:image><br />NTV-1 Technical Standards Profile</h6><p><strong>Related views</strong></p><p>A NTV-1 serves as the bridge between the NSV and NTV. The NSV-9 forecasts relate to the NTV-1 in that a timed technology forecast may contribute to the decision to retire or phase out the use of a certain standard in connection with a system element.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2ac59a2b-19f2-4186-8f18-ed48a0ecabf9"><ac:parameter ac:name="id">768880834</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Standard" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Protocol" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="9ce4abf2-bd44-4372-9928-4efdf97dc7ee" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272738161 space=MT version=1 -->
## PAGE 03579: (2026x) NTV-2 Technical Standards Forecast

- page_id: `272738161`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738161/2026x+NTV-2+Technical+Standards+Forecast
- version_number: 1
- version_date: `2025-11-25T13:49:48.359+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) UAF 1.3 modeling > (2026x) NAF > (2026x) NATO Technical Viewpoint
- labels: ['msosa']

### NORMALIZED CONTENT

769061045

769061047

769061046

**Description**

The forecast for evolutionary changes in the standards needs to be correlated against the time periods mentioned in the NSV-8 and NSV-9 views.

A Technical Standards Forecast is a detailed description of emerging standards relevant to the systems and business processes covered by the architecture. The forecast should be tailored to focus on areas that are related to the purpose for which a given architecture description is being built, and should identify issues that will affect the architecture.

A NTV-2 complements and expands on the Standards Profile (NTV-1) product and should be used when more than one emerging standard time-period is applicable to the architecture. For standards advice refer to the JSP 602 series of documents.

One of the prime purposes of this Product is to identify critical technology standards, their fragility, and the impact of these standards on the future development and maintainability of the Architecture and its constituent elements.

**Implementation**

NTV-2 can be represented using a NTV-2 table.

**Sample**

[IMAGE alt='' src='']

###### NTV-2 Technical Standards Forecast

**Related views**

A NTV-2 delineates the standards that will potentially impact the relevant system elements (from NSV-1, NSV-2, NSV-4, NSV-6, and NOV-7) and relates them to the time periods that are listed in the NSV-8 and NSV-9. A system’s evolution, specified in the NSV-8, may be tied to a future standard listed in the NTV-2. A timed technology forecast from the NSV-9 is related to a NTV-2 standards forecast in the following manner: a certain technology may be dependent on a NTV-2 standard (for example, a standard listed in NTV-2 may not be adopted until a certain technology becomes available).

769061044

**Related elements**

- [CONFLUENCE_PAGE title='Standard' space='MED']
- [CONFLUENCE_PAGE title='Protocol' space='MED']
- [CONFLUENCE_PAGE title='Forecast' space='MED']

**Related procedures**

**Related references**

- [CONFLUENCE_PAGE title='(2026x) Time Periods dialog' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="51eb8769-8c14-4068-8602-8ddab56e4fb9"><ac:parameter ac:name="id">769061045</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="077c1c67-a620-44a4-80e1-43aad2c05388"><ac:parameter ac:name="id">769061047</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="60e1be50-1605-430a-b29c-c666735e7836"><ac:parameter ac:name="id">769061046</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>The forecast for evolutionary changes in the standards needs to be correlated against the time periods mentioned in the NSV-8 and NSV-9 views.</p><p>A Technical Standards Forecast is a detailed description of emerging standards relevant to the systems and business processes covered by the architecture. The forecast should be tailored to focus on areas that are related to the purpose for which a given architecture description is being built, and should identify issues that will affect the architecture.</p><p>A NTV-2 complements and expands on the Standards Profile (NTV-1) product and should be used when more than one emerging standard time-period is applicable to the architecture. For standards advice refer to the JSP 602 series of documents.</p><p>One of the prime purposes of this Product is to identify critical technology standards, their fragility, and the impact of these standards on the future development and maintainability of the Architecture and its constituent elements.</p><p><strong>Implementation</strong></p><p>NTV-2 can be represented using a NTV-2 table.</p><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="Ntv_2.png"><ri:page ri:content-title="(2026x) NTV-2 Technical Standards Forecast" /></ri:attachment></ac:image></p><h6>NTV-2 Technical Standards Forecast</h6><p><strong>Related views</strong></p><p>A NTV-2 delineates the standards that will potentially impact the relevant system elements (from NSV-1, NSV-2, NSV-4, NSV-6, and NOV-7) and relates them to the time periods that are listed in the NSV-8 and NSV-9. A system’s evolution, specified in the NSV-8, may be tied to a future standard listed in the NTV-2. A timed technology forecast from the NSV-9 is related to a NTV-2 standards forecast in the following manner: a certain technology may be dependent on a NTV-2 standard (for example, a standard listed in NTV-2 may not be adopted until a certain technology becomes available).</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9710acf1-0066-40c2-a2d4-25525d6f4a1d"><ac:parameter ac:name="id">769061044</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Standard" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Protocol" /></ac:link></li><li><ac:link><ri:page ri:space-key="MED" ri:content-title="Forecast" /></ac:link></li></ul><p><br /><strong>Related procedures</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="c318e991-df09-4ddf-9408-c362f1453909" /></p><p><br /><strong>Related references</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Time Periods dialog" /></ac:link></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272738133 space=MT version=1 -->
## PAGE 03580: (2026x) Numbering Elements

- page_id: `272738133`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738133/2026x+Numbering+Elements
- version_number: 1
- version_date: `2025-11-25T13:49:42.316+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Business Process Model and Notation Concepts
- labels: ['msosa']

### NORMALIZED CONTENT

Cameo Business Modeler offers an automatic numbering feature to number specific types of BPMN elements.

Each element number is saved in an ID property of element specification.

[IMAGE alt='' src='']

###### BPMN Process Diagram showing element numbers

Numbering elements are described in the following sections:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cameo Business Modeler offers an automatic numbering feature to number specific types of BPMN elements.</p><p>Each element number is saved in an ID property of element specification.</p><p><ac:image><ri:attachment ri:filename="element_numbering.png"><ri:page ri:content-title="(2026x) Numbering Elements" /></ri:attachment></ac:image></p><h6>BPMN Process Diagram showing element numbers</h6><p>Numbering elements are described in the following sections:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="870a1867-d60b-4393-be38-eafdef2c714a" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=272738136 space=MT version=1 -->
## PAGE 03581: (2026x) Numbering Schemas

- page_id: `272738136`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738136/2026x+Numbering+Schemas
- version_number: 1
- version_date: `2025-11-25T13:49:42.799+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Business Process Model and Notation Concepts > (2026x) Numbering Elements
- labels: ['msosa']

### NORMALIZED CONTENT

Types of numbering schemas predefined for BPMN elements are as follows:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Types of numbering schemas predefined for BPMN elements are as follows:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="c6e3a3b5-177e-4043-b45d-24848a97f6f0" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=272736809 space=MT version=1 -->
## PAGE 03582: (2026x) Object Constraint Language

- page_id: `272736809`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272736809/2026x+Object+Constraint+Language
- version_number: 1
- version_date: `2025-11-25T13:47:46.025+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Tools > (2026x) Executable concepts
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

Object Constraint Language (OCL) is a formal language used to express constraints. OCL typically specify the invariant conditions that must hold for the system being modeled.

Expressions can be used in a number of places in the UML model:

- To specify the initial value of an attribute or association end.
- To specify the derivation rule for an attribute or association end.
- To specify the body of an operation.
- To indicate an instance in a dynamic diagram.
- To indicate a condition in a dynamic diagram.
- To indicate the actual parameter values in a dynamic diagram.

There are four types of constraints:

- An invariant is a constraint that states a condition that must always be met by all instances of the class, type, or interface. The invariant is described using an expression that evaluates to true if the invariant is met. Invariants must be true all the time.
- A *precondition* to an operation is a restriction that must be true at the moment the operation is going to be executed. The obligations are specified by the postconditions.
- A *postcondition* to an operation is a restriction that must be true at the moment the operation has just been executed.
- A *guard* is a constraint that must be true before a state transition discharged.

You can use derived properties in the OCL expressions. Scripts having multiple parameters can now be defined using OCL in structured expressions or [CONFLUENCE_PAGE title='Opaque Behavior' space='MED']

##### Invariants on attributes

The simplest constraint is an invariant on an attribute. Suppose a model contains a class *Customer* with an attribute age, then the following constraint restricts the value of the attribute:

```text
= 18]]>
```

##### Invariants on associations

One may also put constraints on the associated objects. Suppose a model contains the class Customer that has an association to the class Salesperson with the role name salesrep and multiplicity 1, then the following constraint restricts the value of the attribute knowledge level of the associated instance of Salesperson:

```text
= 5]]>
```

##### Collections of objects

In most cases the multiplicity of an association is not 1, but more than 1. Evaluating a constraint in these cases will result in a collection of instances of the associated class. Constraints can be put on either the collection itself, e.g. limiting the size, or on the elements of the collection. Suppose in a model the association between 
Salesperson and Customer has the role name clients and multiplicity 1..* on the side of the Customer class, then we might restrict this relationship by the following constraints:

```text
size() <= 100 and clients->forAll(c: Customer | c.age >= 40)]]>
```

##### Pre- and postconditions

In the pre- and postconditions the parameters of the operation can be used. Furthermore, there is a special keyword result which denotes the return value of the operation. It can be used in the postcondition only. For example an operation sell was added to the Salesperson class.

```text
includes( item )
post: not self.sellableItems->includes( item ) and result = item.price]]>
```

##### Derivation Rules

Models often define derived attributes and associations. A derived element does not stand alone. The value of a derived element must always be determined from other (base) values in the model. Omitting the way to derive the element value results in an incomplete model. Using OCL, the derivation can be expressed in a derivation rule. In the following example, the value of a derived element usedServices is defined to be all services that have generated transactions on the account:

```text
asSet()]]>
```

##### Initial Values

In the model information, the initial value of an attribute or association role can be specified by an OCL expression. In the following examples, the initial value for the attribute points is 0, and for the association end transactions, it is an empty set:

```text

```

##### Body of Query Operations

The class diagram can introduce a number of query operations. The query operations are operations that have no side effects, i.e. do not change the state of any instance in the system. The execution of a query operation results in a value or set of values without any alterations in the state of the system. The query operations can 
be introduced in the class diagram, but can only be fully defined by specifying the result of the operation. Using OCL, the result can be given in a single expression, called a body expression. In fact, OCL is a full query language, comparable to SQL. The use of body expressions is an illustration thereof.

The next example states that the operation *getCustomerName* will always result in the name of the card owner associated with the loyalty account:

```text

```

To check OCL syntax according to OCL grammar

1. In the constraint Specification window, click the Specification property value.
2. Click the ... button in the property value cell. The Edit Specification window opens.
3. In the Language list, click OCL and select the Check OCL syntax check box. In the Body box, incorrect expression will be underlined in red. [ATTACHMENT filename='edit_specifications_OCL.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Object Constraint Language (OCL) is a formal language used to express constraints. OCL typically specify the invariant conditions that must hold for the system being modeled.</p><p>Expressions can be used in a number of places in the UML model:</p><ul><li>To specify the initial value of an attribute or association end.</li><li>To specify the derivation rule for an attribute or association end.</li><li>To specify the body of an operation.</li><li>To indicate an instance in a dynamic diagram.</li><li>To indicate a condition in a dynamic diagram.</li><li>To indicate the actual parameter values in a dynamic diagram.</li></ul><p>There are four types of constraints:</p><ul><li>An <em>invariant</em> is a constraint that states a condition that must always be met by all instances of the class, type, or interface. The invariant is described using an expression that evaluates to true if the invariant is met. Invariants must be true all the time.</li><li><p>A <em>precondition</em> to an operation is a restriction that must be true at the moment the operation is going to be executed. The obligations are specified by the postconditions.</p></li><li><p>A <em>postcondition</em> to an operation is a restriction that must be true at the moment the operation has just been executed.</p></li><li><p>A <em>guard</em> is a constraint that must be true before a state transition discharged.</p></li></ul><p>You can use derived properties in the OCL expressions. Scripts having multiple parameters can now be defined using OCL in structured expressions or <ac:link><ri:page ri:space-key="MED" ri:content-title="Opaque Behavior" /><ac:plain-text-link-body><![CDATA[Opaque Behaviors]]></ac:plain-text-link-body></ac:link></p><h3>Invariants on attributes</h3><p>The simplest constraint is an invariant on an attribute. Suppose a model contains a class <em>Customer</em> with an attribute age, then the following constraint restricts the value of the attribute:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="682e7b0c-576b-4de3-ba4a-310862f03110"><ac:plain-text-body><![CDATA[context Customer inv :
age >= 18]]></ac:plain-text-body></ac:structured-macro><h3>Invariants on associations </h3><p>One may also put constraints on the associated objects. Suppose a model contains the class Customer that has an association to the class Salesperson with the role name salesrep and multiplicity 1, then the following constraint restricts the value of the attribute knowledge level of the associated instance of Salesperson:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="36a0a52d-ffbc-42e2-9b70-b830c487b6c6"><ac:plain-text-body><![CDATA[context Customer inv :
salesrep.knowledgelevel >= 5]]></ac:plain-text-body></ac:structured-macro><h3>Collections of objects </h3><p>In most cases the multiplicity of an association is not 1, but more than 1. Evaluating a constraint in these cases will result in a collection of instances of the associated class. Constraints can be put on either the collection itself, e.g. limiting the size, or on the elements of the collection. Suppose in a model the association between <br />Salesperson and Customer has the role name clients and multiplicity 1..* on the side of the Customer class, then we might restrict this relationship by the following constraints:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="97076dca-8f1e-45c1-947f-36edb4b23a7b"><ac:plain-text-body><![CDATA[context Salesperson inv :
clients->size() <= 100 and clients->forAll(c: Customer | c.age >= 40)]]></ac:plain-text-body></ac:structured-macro><h3>Pre- and postconditions </h3><p>In the pre- and postconditions the parameters of the operation can be used. Furthermore, there is a special keyword result which denotes the return value of the operation. It can be used in the postcondition only. For example an operation sell was added to the Salesperson class.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="415ed3e7-b1b8-416a-ae0b-01d1f442a132"><ac:plain-text-body><![CDATA[context Salesperson::sell( item: Thing ): Real
pre : self.sellableItems->includes( item )
post: not self.sellableItems->includes( item ) and result = item.price]]></ac:plain-text-body></ac:structured-macro><h3>Derivation Rules </h3><p>Models often define derived attributes and associations. A derived element does not stand alone. The value of a derived element must always be determined from other (base) values in the model. Omitting the way to derive the element value results in an incomplete model. Using OCL, the derivation can be expressed in a derivation rule. In the following example, the value of a derived element usedServices is defined to be all services that have generated transactions on the account:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="00a5f40c-ff91-4e9f-a654-5661b33cd6e8"><ac:plain-text-body><![CDATA[context LoyaltyAccount::usedServices : Set(Services)
derive : transactions.service->asSet()]]></ac:plain-text-body></ac:structured-macro><h3 style="height: 20.0px;">Initial Values </h3><p>In the model information, the initial value of an attribute or association role can be specified by an OCL expression. In the following examples, the initial value for the attribute points is 0, and for the association end transactions, it is an empty set:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="cd8f4832-fb72-4a5d-8ad9-b451366a40c0"><ac:plain-text-body><![CDATA[context LoyaltyAccount::points : Integer
init: 0
context LoyaltyAccount::transactions : Set(Transaction)
init: Set{}]]></ac:plain-text-body></ac:structured-macro><h3>Body of Query Operations</h3><p>The class diagram can introduce a number of query operations. The query operations are operations that have no side effects, i.e. do not change the state of any instance in the system. The execution of a query operation results in a value or set of values without any alterations in the state of the system. The query operations can <br />be introduced in the class diagram, but can only be fully defined by specifying the result of the operation. Using OCL, the result can be given in a single expression, called a body expression. In fact, OCL is a full query language, comparable to SQL. The use of body expressions is an illustration thereof.</p><p>The next example states that the operation <em>getCustomerName</em> will always result in the name of the card owner associated with the loyalty account:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ee723e5a-7c11-45fc-b562-66ae12ac64a2"><ac:plain-text-body><![CDATA[context LoyaltyAccount::getCustomerName() : String
body: Membership.card.owner.name]]></ac:plain-text-body></ac:structured-macro><p> </p><p>To check OCL syntax according to OCL grammar</p><hr /><ol><li>In the constraint Specification window, click the Specification property value.</li><li>Click the <strong>...</strong> button in the property value cell. The <strong>Edit</strong> <strong>Specification</strong> window opens.</li><li>In the Language list, click <strong>OCL</strong> and select the <strong>Check OCL syntax</strong> check box. In the Body box, incorrect expression will be underlined in red.<br /><ac:image ac:title="Checking OCL syntax" ac:alt="Checking OCL syntax"><ri:attachment ri:filename="edit_specifications_OCL.png"><ri:page ri:content-title="(2026x) Object Constraint Language" /></ri:attachment></ac:image> </li></ol></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272733625 space=MT version=1 -->
## PAGE 03583: (2026x) Object diagram

- page_id: `272733625`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272733625/2026x+Object+diagram
- version_number: 1
- version_date: `2025-11-25T13:42:37.946+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Diagrams > (2026x) UML diagrams
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

307526412

307526414

307526413

**Overview** 
 An Object diagram falls under the structural diagramming family.An Object diagram is an instance of a Class diagram that shows a complete or a partial view of the structure. This type of diagram displays instances of classifiers and links (instances of associations) between them.

**Purpose**

An Object diagram is usually used in the early phases of a project to model examples that show a possible snapshot of the system execution, for example, what the system can look like at some point in time. Additionally, it focuses on the attributes of a set of objects and helps to analyze how these objects relate to each other.****

**Usage**

An Object diagram can be used to:

- represent a class instance
- describe the static aspect of the system
- understand the behavior of a particular object
- analyze object relations
- perform forward and reverse engineering on chosen systems.

**Summary**

Object diagrams are valuable because they:

- can be used to model test cases in order to validate the Class diagram
- support the investigation of requirements by modeling examples from the problem domain
- examine a specific iteration of a general system
- later in the project, model test cases to see whether the created Class diagram is correct and complete
- allows users to get a high-level overview of the system.

[IMAGE alt='' src='']

###### Example of an Object diagram

307526411

**Related pages**

- [CONFLUENCE_PAGE title='(2026x) Creating diagrams' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="28eae8a0-e997-46c3-86b8-0e81e7bd7fa4"><ac:parameter ac:name="id">307526412</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="92cc77b3-f5fe-48ad-ac5a-1865b061fdc6"><ac:parameter ac:name="id">307526414</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="04d3c839-451d-4304-9eb9-251110425ce4"><ac:parameter ac:name="id">307526413</ac:parameter><ac:rich-text-body><p><strong>Overview</strong><br class="atl-forced-newline" /> <span style="color: rgb(62,63,64);">An Object diagram falls under the structural diagramming family. </span>An Object diagram is an instance of a Class diagram that shows a complete or a partial view of the structure. This type of diagram displays instances of classifiers and links (instances of associations) between them.</p><p><strong>Purpose</strong></p><p>An Object diagram is usually used in the early phases of a project to model examples that show a possible snapshot of the system execution, for example, what the system can look like at some point in time. Additionally, it focuses on the attributes of a set of objects and helps to analyze how these objects relate to each other.<strong><br /></strong></p><p><strong>Usage</strong></p><p>An Object diagram can be used to:</p><ul><li>represent a class instance</li><li>describe the static aspect of the system</li><li>understand the behavior of a particular object</li><li>analyze object relations</li><li>perform forward and reverse engineering on chosen systems.</li></ul><p><strong>Summary</strong></p><p>Object diagrams are valuable because they:</p><ul><li>can be used to model test cases in order to validate the Class diagram</li><li>support the investigation of requirements by modeling examples from the problem domain</li><li>examine a specific iteration of a general system</li><li>later in the project, model test cases to see whether the created Class diagram is correct and complete</li><li>allows users to get a high-level overview of the system.</li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="object_diagram_example.png"><ri:page ri:content-title="(2026x) Object diagram" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Example of an Object diagram</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a385354a-54dd-4b49-9f89-50ea746fcae1"><ac:parameter ac:name="id">307526411</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Creating diagrams" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272738105 space=MT version=2 -->
## PAGE 03584: (2026x) Objective

- page_id: `272738105`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272738105/2026x+Objective
- version_number: 2
- version_date: `2025-11-25T14:46:03.474+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) BPMN modeling > (2026x) Supportive Diagrams Concepts > (2026x) Business Motivation Diagram > (2026x) Ends Concepts
- labels: ['msosa']

### NORMALIZED CONTENT

1487168407

1487168408

1487168408

**Description**

An Objective is a statement of an attainable, time-targeted, and measurable target that the enterprise seeks to meet in order to achieve its Goals.

**Notation**

[IMAGE alt='' src='']

1487168406

**Related elements**

- Ends Concepts
- End Concept Relationships

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="8b9d09ad-5138-4bb6-a91a-585ac6fcadc0"><ac:parameter ac:name="id">1487168407</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="be845ae5-0e50-47e6-b655-0047de117273"><ac:parameter ac:name="id">1487168408</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2aa734ee-6893-498c-a0eb-19e01dc091c0"><ac:parameter ac:name="id">1487168408</ac:parameter><ac:rich-text-body><p><strong>Description</strong></p><p>An Objective is a statement of an attainable, time-targeted, and measurable target that the enterprise seeks to meet in order to achieve its Goals.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="objective.png"><ri:page ri:content-title="(2026x) Objective" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e8e1aeb2-cdd6-4028-a830-373fe5945bbd"><ac:parameter ac:name="id">1487168406</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MT/(2026x) Ends+Concepts">Ends Concepts</a></li><li><a href="https://docs.nomagic.com/display/MT/(2026x) End+Concept+Relationships">End Concept Relationships</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/MT/(2026x) Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=272735798 space=MT version=1 -->
## PAGE 03585: (2026x) Opaque objects

- page_id: `272735798`
- space_key: `MT`
- source_url: https://docs.nomagic.com/spaces/MT/pages/272735798/2026x+Opaque+objects
- version_number: 1
- version_date: `2025-11-25T13:45:57.882+01:00`
- ancestors: Versions of Modeling Tools Documentation > (2026x) Modeling Tools Documentation > (2026x) General modeling features > (2026x) Macro engine
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

Macro Engine creates opaque objects to represent the elements. Through these opaque objects, you can access the elements, retrieve, or assign values to them instead of using OpenAPI to do it.

All examples given in this section is written in Javascript.

**On this page**

##### Getting an Opaque Object

You can get an opaque object of an existing element by using either:

```text
(i) AutomatonMacroAPI.getOpaqueObjectByPath(String path)
```

```text
(ii) AutomatonMacroAPI.getOpaqueObject(Element element)
```

If the above methods cannot find the element, they will return null.

****

**(i) getOpaqueObjectByPath(String path)**

To use getOpaqueObjectByPath(String path), for example, type:

```text

```

**(ii) getOpaqueObject(Element element)**

To use getOpaqueObject(Element element), for example, type:

```text

```

```text
You can also use two other methods to get an opaque object as follows:
```

```text
(iii) AutomatonMacroAPI.getModelData()(iv) AutomatonMacroAPI.getSelectedElementFromContainmentTree()
```

**(iii) getModelData()**

This method will obtain an opaque object of the model Data in the Containment tree.

**(iv) getSelectedElementFromContainmentTree()** 
This method will obtain an opaque object of the selected element in the Containment tree. 
Macro Engine uses methods (iii) getModelData() and (iv) getSelectedElementFromContainmentTree() to retrieve opaque objects in order to identify the defined scope in its recording mechanism.

##### Getting Element Property Values

Once you have obtained an opaque object, you can get the property value of the element by using any of the following methods:

```text
(i) <variableName>.get<PropertyName>()             (ii) <variableName>.<PropertyName>             (iii) <variableName>._automatonGetValue(String realPropertyName, String stereotypePath)
```

The <variableName> is the name of a macro variable that stores the opaque object. The <PropertyName> is the name of the property that appears in the Specification dialog.

The <variableName> is the name of a macro variable that stores the opaque object. The <PropertyName> is the name of the property that appears in the Specification dialog.

You need to capitalize the first letter of <PropertyName> and replace the whitespace with an underscore. If a duplicate property name occurs, you can refer to the right property name by using the following additional information: <SterotypeName>_<PropertyName><RunningNumber>.

[IMAGE alt='' src='']

If there are two stereotypes applied to the same element, see above figure, you can differentiate one from the other, for example, by specifying <PropertyName> as StereotypeA_PropertyA1 and StereotypeA_PropertyA2 in the macro.

You can also use the method _automatonGetValue to get a property value. If you want to get the value of a PropertyA from SterotypeA in PackageA., for example, you can use _automatonGetValue(“PropertyA”, “PackageA::StereotypeA”).

A realPropertyName is the real property name that is used in OpenAPI. A stereotypePath is the path of a stereotype that contains the property. This property will not be needed if it is in the Element itself.

If you refer to a property that does not exist, Macro Engine may or may not throw an error, depending on which language library you use. For example, if you use Javascript to call the property that does not exist, Macro Engine will not throw an error. But if you use JRuby, it will throw an exception to report the error condition: org.jruby.exceptions.RaiseException.

If the value of a property is an element, Macro Engine will convert it to an opaque object and you can call it, for example, by typing classA.Owner.Name.

If a property has more than one value, Macro Engine will convert the values to a list of opaque objects. If you need to get a value from the list, you can call the method of the class java.util.List, for example, by typing:

```text
(i) classA.Applied_Stereotype.get(<index>).Nameor(ii) classA.Applied_Stereotype.add(anotherOpaque)If a property is read-only, an exception will be thrown.
```

###### Getting Element Property Value Examples

The following are some examples of how to get an element property value using the methods given in the section above: 
to use get<PropertyName>, for example, type:

```text

```

to use <PropertyName>, for example, type:

```text

```

```text
to use _automatonGetValue, for example, type:
```

```text

```

to use a SysML Element, for example, type:

```text

```

##### Setting Element Property Values

You can assign values to an element by using any of the following methods:

```text
(i) <variableName>.set<PropertyName>(Object value)    (ii) <variableName>.<PropertyName> = value; and then call persist()    (iii) <variableName>._automatonSetValue(String realPropertyName, String stereotypePath, Object value)
```

The value of an element can be a primitive data type, an opaque object, or an element. If you use a setter to set the value, for example, _automatonSetValue() or change the value on a list, it will be saved in the element automatically.

If you use <variableName>.<PropertyName> = value to set the value, you must call persist() to persist the change to the element. You need to first set the data, call persist(), and finally call a getter method in order to set the data and retrieve them. This process will force an opaque object to retrieve the current value from a model and overwrite the value that you have just specified in the opaque object.

If you use JRuby, do not capitalize the first letter of <PropertyName> in <variableName>.<PropertyName>.

###### Setting Element Property Value Examples

The following are some examples of how to set an element property value by using the methods given in section above. 
to use set<PropertyName>(value), for example, type:

```text

```

to use <PropertyName> = value), for example, type:

```text

```

to use _automatonSetValue, for example, type:

```text

```

to set an opaque object to another opaque object, for example, type:

```text

```

The table below lists the supported element properties in Macro Engine.

| Property | Type | Support Operation |
| --- | --- | --- |
| Active Hyperlink | String | Read |
| All General Classifiers | List<AutomatonOpaqueObject> | Read |
| All Realizing Elements | List<AutomatonOpaqueObject> | Read |
| All Specific Classifiers | List<AutomatonOpaqueObject> | Read |
| All Specifying Elements | List<AutomatonOpaqueObject> | Read |
| Applied Stereotype | List<AutomatonOpaqueObject> | Read |
| Applied_Stereotype_Instance | N/A | Read |
| Attribute | List<AutomatonOpaqueObject> | Read |
| Base Classifier | List<AutomatonOpaqueObject> | Read |
| Class | AutomatonOpaqueObject | Read |
| Classifier Behavior | AutomatonOpaqueObject | Read |
| Client Dependency | List<AutomatonOpaqueObject> | Read |
| Collaboration Use | List<AutomatonOpaqueObject> | Read |
| Element | ID | N/A - |
| Extension | List<AutomatonOpaqueObject> | Read |
| Feature | List<AutomatonOpaqueObject> | Read |
| Generalization | List<AutomatonOpaqueObject> | Read |
| Image | N/A | - |
| Imported Member | List<AutomatonOpaqueObject> | Read |
| Inherited Member | List<AutomatonOpaqueObject> | Read |
| Interface Realization | List<AutomatonOpaqueObject> | Read |
| Is Leaf | Boolean | Read/Write |
| Is Final Specialization | Boolean | Read/Write |
| Is Active | Boolean | Read/Write |
| Is Abstract | Boolean | Read/Write |
| Member | List<AutomatonOpaqueObject> | Read |
| Name | String | Read/Write |
| Name Expression | AutomatonOpaqueObject | Read |
| Namespace | AutomatonOpaqueObject | Read |
| Nested Classifier | List<AutomatonOpaqueObject> | Read |
| Owned Attribute | List<AutomatonOpaqueObject> | Read |
| Owned Connector | List<AutomatonOpaqueObject> | Read |
| Owned Comment | List<AutomatonOpaqueObject> | Read |
| Owned Diagram | List<AutomatonOpaqueObject> | Read |
| Owned Element | List<AutomatonOpaqueObject> | Read |
| Owned Member | List<AutomatonOpaqueObject> | Read |
| Owned Operation | List<AutomatonOpaqueObject> | Read |
| Owned Port | List<AutomatonOpaqueObject> | Read |
| Owned Reception | List<AutomatonOpaqueObject> | Read |
| Owned Rule | List<AutomatonOpaqueObject> | Read |
| Owned Template Signature | AutomatonOpaqueObject | Read |
| Owned Trigger | List<AutomatonOpaqueObject> | Read |
| Owned Use Case | List<AutomatonOpaqueObject> | Read |
| Owning Package | List<AutomatonOpaqueObject> | Read |
| Owning Template Parameter | N/A | - |
| Owner | AutomatonOpaqueObject | Read/Write |
| Package | AutomatonOpaqueObject | Read |
| Package Import | List<AutomatonOpaqueObject> | Read |
| Part | List<AutomatonOpaqueObject> | Read |
| Participates In Activity | List<AutomatonOpaqueObject> | Read |
| Participates In Interaction | List<AutomatonOpaqueObject> | Read |
| Powertype Extent | List<AutomatonOpaqueObject> | Read |
| Qualified Name | List<AutomatonOpaqueObject> | Read |
| Realized Interface | N/A | - |
| Realizing Component | List<AutomatonOpaqueObject> | Read |
| Realizing Element | List<AutomatonOpaqueObject> | Read |
| Redefined Classifier | List<AutomatonOpaqueObject> | Read |
| Redefined Element | List<AutomatonOpaqueObject> | Read |
| Redefinition Context | List<AutomatonOpaqueObject> | Read |
| Representation | N/A | - |
| Role | List<AutomatonOpaqueObject> | Read |
| Specific Classifier | List<AutomatonOpaqueObject> | Read |
| Specifying Component | List<AutomatonOpaqueObject> | Read |
| Specifying Element | List<AutomatonOpaqueObject> | Read |
| Supplier Dependency | List<AutomatonOpaqueObject> | Read |
| Template Binding | List<AutomatonOpaqueObject> | Read |
| Template Parameter | N/A | - |
| To Do | String | Read/Write |
| Use Case | List<AutomatonOpaqueObject | Read/Write |
| Visibility | String | Read/Write |

##### Getting the Child of an Element

You can get the child of an Element by typing the following:

- <variableName>._getChild(String childElementName)

If the above method cannot find the childElementName, it will throw an error.

To get the child of an element named ClassB from ClassA, for example, type:

```text

```

##### Getting the Owner of an Element

You can get the owner of an element by typing the following:

- <variableName>._getOwner()

If the above method cannot find the owner, for example Model Data, it will throw an error. 
To get the owner of an element named ClassA, for example, type:

```text

```

##### Creating a New Element

You can create a new element by using its Meta-class name, such as a Class in Standard UML or a Requirement in SysML by using the following method:

- AutomatonMacroAPI.createElement(String metaClassName)

This method will return an opaque object of the created element. If the method cannot find the Meta-class, it will throw an exception.

To create a new Class & Requirement element (Javascript), for example, type:

```text

```

##### Creating a Relationship Between Elements

You can create a relationship between elements by typing:

- AutomatonMacroAPI.createRelationship(AutomatonOpaqueObject opque1, AutomatonOpaqueObject opque2, String relationName)

To create a Copy & Abstraction relationship between Element1 and Element2 (Javascript), for example, type:

```text

```

##### Removing an Element

You can remove an Element from the modeling tool by typing the following:

- AutomatonMacroAPI.removeElement(AutomatonOpaqueObject opaqueObj)

To remove an Element1 (Javascript), for example, type:

```text

```

##### Adding a Stereotype to an Element

You can apply a stereotype to an element by typing either:

(i) AutomatonMacroAPI.addStereotype(AutomatonOpaqueObject opaque, AutomatonOpaqueObject opaqueStereotype) 
(ii)AutomatonMacroAPI.addStereotypeByStereotypeName(AutomatonOpaqueObject opaque, String stereotypeName)

To add a StererotypeA to ClassA (Javascript), for example, type:

```text

```

##### Removing a Stereotype from an Element

You can remove a Stereotype from an element by typing either:

(i) AutomatonMacroAPI.removeStereotype(AutomatonOpaqueObject opaque, AutomatonOpaqueObject opaqueStereotype) 
(ii) AutomatonMacroAPI.removeStereotypeByStereotypeName(AutomatonOpaqueObject opaque, String stereotypeName)

To remove a StereotypeA from ClassA (Javascript), for example, type:

```text

```

##### Printing Element Details

If you want to know the method that is used in the opaque object of an element, you can print the element details by typing the following:

- AutomatonMacroAPI.printElementDetail(AutomatonOpaqueObject opaque);

This method will print the field, constructor, and method that belong to the opaque object in the Message dialog.

To print the details of ClassA, for example, type:

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>Macro Engine creates opaque objects to represent the elements. Through these opaque objects, you can access the elements, retrieve, or assign values to them instead of using OpenAPI to do it.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="75174b41-78b9-499f-8f6a-a6e55293e9db"><ac:rich-text-body><p><span>All examples given in this section is written in Javascript.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="48feebf2-c42c-4a1f-9b8c-8a9e31b7b027" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><ac:inline-comment-marker ac:ref="8329afc6-5f98-48b7-a979-71f138b84abb">Getting</ac:inline-comment-marker> an Opaque Object</h3><p>You can get an opaque object of an existing element by using either: </p><pre>    (i) AutomatonMacroAPI.getOpaqueObjectByPath(String path)</pre><pre>    (ii) AutomatonMacroAPI.getOpaqueObject(Element element)        </pre><p><br /></p><p>If the above methods cannot find the element, they will return null.</p><p><strong><br /></strong></p><p><strong>(i) getOpaqueObjectByPath(String path)</strong></p><p>To use getOpaqueObjectByPath(String path), for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="fe88d047-37c2-4118-ae66-a67aec5c41c1"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[AutomatonMacroAPI.getOpaqueObjectByPath ("PackageA::Element2");]]></ac:plain-text-body></ac:structured-macro><p><strong style="line-height: 1.42857;">(ii) getOpaqueObject(Element element)</strong></p><p>To use getOpaqueObject(Element element), for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="79b9a446-ece7-445e-8685-b918badad92d"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var element = com.nomagic.magicdraw.uml.Finder.byQualifiedName().find(Application.getInstance().getProject(), "PackageB::ClassB");
var a = AutomatonMacroAPI.getOpaqueObject(element);]]></ac:plain-text-body></ac:structured-macro><pre>You can also use two other methods to get an opaque object as follows:</pre><pre style="margin-left: 30.0px;">(iii) AutomatonMacroAPI.getModelData()<br />(iv) AutomatonMacroAPI.getSelectedElementFromContainmentTree()</pre><p><strong>(iii) getModelData()</strong></p><p>This method will obtain an opaque object of the model Data in the Containment tree.</p><p><strong>(iv) getSelectedElementFromContainmentTree()</strong><br />This method will obtain an opaque object of the selected element in the Containment tree.<br />Macro Engine uses methods (iii) getModelData() and (iv) getSelectedElementFromContainmentTree() to retrieve opaque objects in order to identify the defined scope in its recording mechanism.</p><h3>Getting Element Property Values</h3><p>Once you have obtained an opaque object, you can get the property value of the element by using any of the following methods:</p><pre>             (i) &lt;variableName&gt;.get&lt;PropertyName&gt;()<br />             (ii) &lt;variableName&gt;.&lt;PropertyName&gt;<br />             (iii) &lt;variableName&gt;._automatonGetValue(String realPropertyName, String stereotypePath)</pre><p>The &lt;variableName&gt; is the name of a macro variable that stores the opaque object. The &lt;PropertyName&gt; is the name of the property that appears in the Specification dialog.</p><p>The &lt;variableName&gt; is the name of a macro variable that stores the opaque object. The &lt;PropertyName&gt; is the name of the property that appears in the Specification dialog.</p><p>You need to capitalize the first letter of &lt;PropertyName&gt; and replace the whitespace with an underscore. If a duplicate property name occurs, you can refer to the right property name by using the following additional information: &lt;SterotypeName&gt;_&lt;PropertyName&gt;&lt;RunningNumber&gt;.</p><p style="margin-left: 30.0px;"><ac:image ac:title="A Duplicate Property in Stereotype" ac:alt="A Duplicate Property in Stereotype"><ri:attachment ri:filename="Fig 21.PNG"><ri:page ri:content-title="(2026x) Opaque objects" /></ri:attachment></ac:image></p><p>If there are two stereotypes applied to the same element, see above figure, you can differentiate one from the other, for example, by specifying &lt;PropertyName&gt; as StereotypeA_PropertyA1 and StereotypeA_PropertyA2 in the macro.</p><p>You can also use the method _automatonGetValue to get a property value. If you want to get the value of a PropertyA from SterotypeA in PackageA., for example, you can use _automatonGetValue(“PropertyA”, “PackageA::StereotypeA”).</p><p>A realPropertyName is the real property name that is used in OpenAPI. A stereotypePath is the path of a stereotype that contains the property. This property will not be needed if it is in the Element itself.</p><p>If you refer to a property that does not exist, Macro Engine may or may not throw an error, depending on which language library you use. For example, if you use Javascript to call the property that does not exist, Macro Engine will not throw an error. But if you use JRuby, it will throw an exception to report the error condition: org.jruby.exceptions.RaiseException.</p><p>If the value of a property is an element, Macro Engine will convert it to an opaque object and you can call it, for example, by typing classA.Owner.Name.</p><p>If a property has more than one value, Macro Engine will convert the values to a list of opaque objects. If you need to get a value from the list, you can call the method of the class java.util.List, for example, by typing:</p><pre>(i) classA.<span style="color: rgb(23,43,77);">Applied_Stereotype</span>.get(&lt;index&gt;).Name<br />or<br />(ii) classA.<span style="color: rgb(23,43,77);">Applied_Stereotype</span>.add(anotherOpaque)<br />If a property is read-only, an exception will be thrown.</pre><h4>Getting Element Property Value Examples</h4><p>The following are some examples of how to get an element property value using the methods given in the section above:<br />to use get&lt;PropertyName&gt;, for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="636c686e-ea8a-404f-a7fc-a7f52dd8eb62"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var classA = AutomatonMacroAPI.getOpaqueObjectByPath ("MyClass");
Application.getInstance().getGUILog().log(classA.getName());]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p>to use &lt;PropertyName&gt;, for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e7a3525a-d86c-4f41-874f-10dd1ac1eab1"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var classA = AutomatonMacroAPI.getOpaqueObjectByPath("MyClass");
Application.getInstance().getGUILog().log(classA.Name);]]></ac:plain-text-body></ac:structured-macro><pre>to use _automatonGetValue, for example, type:</pre><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c5863035-d827-4e34-966d-d074963779ce"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var reqA = AutomatonMacroAPI.getOpaqueObjectByPath("MyRequirements");
Application.getInstance().getGUILog().log(reqA._automatonGetValue("PropertyA", "PackageA::StereotypeA");]]></ac:plain-text-body></ac:structured-macro><p>to use a SysML Element, for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="62bb8269-bb67-4048-b7fc-4d60dcfbd8c0"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var reqA = AutomatonMacroAPI.getOpaqueObjectByPath("MyRequirements");
Application.getInstance().getGUILog().log(reqA.getID());]]></ac:plain-text-body></ac:structured-macro><h3><span style="color: rgb(0,0,0);">Setting Element Property Values</span></h3><p>You can assign values to an element by using any of the following methods:</p><pre>    (i) &lt;variableName&gt;.set&lt;PropertyName&gt;(Object value)<br />    (ii) &lt;variableName&gt;.&lt;PropertyName&gt; = value; and then call persist()<br />    (iii) &lt;variableName&gt;._automatonSetValue(String realPropertyName, String stereotypePath, Object value)</pre><p>The value of an element can be a primitive data type, an opaque object, or an element. If you use a setter to set the value, for example, _automatonSetValue() or change the value on a list, it will be saved in the element automatically.</p><p>If you use &lt;variableName&gt;.&lt;PropertyName&gt; = value to set the value, you must call persist() to persist the change to the element. You need to first set the data, call persist(), and finally call a getter method in order to set the data and retrieve them. This process will force an opaque object to retrieve the current value from a model and overwrite the value that you have just specified in the opaque object.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="5fd143f5-ee2c-4bf2-b2ff-e4baf2a7c488"><ac:rich-text-body><p><span>If you use JRuby, do not capitalize the first letter of &lt;PropertyName&gt; in &lt;variableName&gt;.&lt;PropertyName&gt;.</span></p></ac:rich-text-body></ac:structured-macro><h4>Setting Element Property Value Examples</h4><p>The following are some examples of how to set an element property value by using the methods given in section above.<br />to use set&lt;PropertyName&gt;(value), for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2fd778f7-7a8f-4e3a-8794-7df3750a6667"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var classB = AutomatonMacroAPI.getOpaqueObjectByPath("Element2");
classB.setName("NewElementName")]]></ac:plain-text-body></ac:structured-macro><p>to use &lt;PropertyName&gt; = value), for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="be6c0b04-80aa-4687-8549-9edfc9746fb4"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var classB = AutomatonMacroAPI.getOpaqueObjectByPath("Element2");
classB.Name = "NewElementName";
classB.Is_Abstract = true;
classB.persist();]]></ac:plain-text-body></ac:structured-macro><p>to use _automatonSetValue, for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="66456a70-680f-4700-9f20-008fa6cbc381"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var classB = AutomatonMacroAPI.getOpaqueObjectByPath("Element2");
classB._automatonSetValue("PropertyA", "PackageA::StereotypeA", "Demo String value");]]></ac:plain-text-body></ac:structured-macro><p>to set an opaque object to another opaque object, for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f16048ae-77dd-4448-bbb6-f85adb7e12db"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var ele1 = AutomatonMacroAPI.getOpaqueObjectByPath("Element1");
var ele2 = AutomatonMacroAPI.getOpaqueObjectByPath("Element2");
ele1.setPackaged_Element(ele2);]]></ac:plain-text-body></ac:structured-macro><p>The table below lists the supported element properties in Macro Engine.</p><table style="margin-left: 30.0px;"><thead style="margin-left: 30.0px;"><tr style="margin-left: 30.0px;"><th style="margin-left: 30.0px;"><div class="tablesorter-header-inner">Property</div></th><th style="margin-left: 30.0px;"><div class="tablesorter-header-inner">Type</div></th><th style="margin-left: 30.0px;"><div class="tablesorter-header-inner">Support Operation</div></th></tr></thead><tbody style="margin-left: 30.0px;"><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">Active Hyperlink</td><td style="margin-left: 30.0px;">String</td><td style="margin-left: 30.0px;">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">All General Classifiers</td><td style="margin-left: 30.0px;">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;"><p><span>Read</span></p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">All Realizing Elements</td><td style="margin-left: 30.0px;">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">All Specific Classifiers</td><td style="margin-left: 30.0px;">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">All Specifying Elements</td><td style="margin-left: 30.0px;">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">Applied Stereotype</td><td style="margin-left: 30.0px;">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">Applied_Stereotype_Instance</td><td style="margin-left: 30.0px;">N/A</td><td style="margin-left: 30.0px;">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">Attribute</td><td style="margin-left: 30.0px;">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">Base Classifier</td><td style="margin-left: 30.0px;">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">Class</td><td style="margin-left: 30.0px;">AutomatonOpaqueObject</td><td style="margin-left: 30.0px;">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">Classifier Behavior</td><td style="margin-left: 30.0px;">AutomatonOpaqueObject</td><td style="margin-left: 30.0px;">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">Client Dependency</td><td style="margin-left: 30.0px;">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">Collaboration Use</td><td style="margin-left: 30.0px;">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;">Element</td><td style="margin-left: 30.0px;">ID</td><td style="margin-left: 30.0px;">N/A -</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Extension</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Feature</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Generalization</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Image</td><td style="margin-left: 30.0px;" colspan="1">N/A</td><td style="margin-left: 30.0px;" colspan="1"> -</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Imported Member</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1"> Inherited Member</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read </td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Interface Realization</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Is Leaf</td><td style="margin-left: 30.0px;" colspan="1">Boolean</td><td style="margin-left: 30.0px;" colspan="1">Read/Write</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Is Final Specialization</td><td style="margin-left: 30.0px;" colspan="1">Boolean</td><td style="margin-left: 30.0px;" colspan="1">Read/Write</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Is Active</td><td style="margin-left: 30.0px;" colspan="1">Boolean</td><td style="margin-left: 30.0px;" colspan="1">Read/Write</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Is Abstract</td><td style="margin-left: 30.0px;" colspan="1">Boolean</td><td style="margin-left: 30.0px;" colspan="1">Read/Write</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Member</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Name</td><td style="margin-left: 30.0px;" colspan="1">String</td><td style="margin-left: 30.0px;" colspan="1">Read/Write</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Name Expression</td><td style="margin-left: 30.0px;" colspan="1">AutomatonOpaqueObject</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Namespace</td><td style="margin-left: 30.0px;" colspan="1">AutomatonOpaqueObject</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Nested Classifier</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owned Attribute</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owned Connector</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owned Comment</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owned Diagram</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owned Element</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owned Member</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owned Operation</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1"> Owned Port</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read </td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owned Reception</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owned Rule</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owned Template Signature</td><td style="margin-left: 30.0px;" colspan="1">AutomatonOpaqueObject</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owned Trigger</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owned Use Case</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owning Package</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owning Template Parameter</td><td style="margin-left: 30.0px;" colspan="1">N/A</td><td style="margin-left: 30.0px;" colspan="1">-</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Owner</td><td style="margin-left: 30.0px;" colspan="1">AutomatonOpaqueObject</td><td style="margin-left: 30.0px;" colspan="1">Read/Write</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Package</td><td style="margin-left: 30.0px;" colspan="1">AutomatonOpaqueObject</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Package Import</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Part</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Participates In Activity</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Participates In Interaction</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Powertype Extent</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Qualified Name</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Realized Interface</td><td style="margin-left: 30.0px;" colspan="1">N/A</td><td style="margin-left: 30.0px;" colspan="1"> -</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Realizing Component</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Realizing Element</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Redefined Classifier</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Redefined Element</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Redefinition Context</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Representation</td><td style="margin-left: 30.0px;" colspan="1">N/A</td><td style="margin-left: 30.0px;" colspan="1">-</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Role</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Specific Classifier</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Specifying Component</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Specifying Element</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Supplier Dependency</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Template Binding</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject&gt;</td><td style="margin-left: 30.0px;" colspan="1">Read</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Template Parameter</td><td style="margin-left: 30.0px;" colspan="1">N/A</td><td style="margin-left: 30.0px;" colspan="1"> -</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">To Do</td><td style="margin-left: 30.0px;" colspan="1">String</td><td style="margin-left: 30.0px;" colspan="1">Read/Write</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Use Case</td><td style="margin-left: 30.0px;" colspan="1">List&lt;AutomatonOpaqueObject</td><td style="margin-left: 30.0px;" colspan="1">Read/Write</td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;" colspan="1">Visibility</td><td style="margin-left: 30.0px;" colspan="1">String</td><td style="margin-left: 30.0px;" colspan="1">Read/Write</td></tr></tbody></table><h3>Getting the Child of an Element</h3><p>You can get the child of an Element by typing the following:</p><ul><li><pre>&lt;variableName&gt;._getChild(String childElementName)</pre></li></ul><p>If the above method cannot find the childElementName, it will throw an error.</p><p><br /></p><p>To get the child of an element named ClassB from ClassA, for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="cffc47a1-44a3-4aaa-8300-02fc5ddcdfeb"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var classA = AutomatonMacroAPI.getOpaqueObjectByPath("ClassA");
var classB = classA._getChild("ClassB");]]></ac:plain-text-body></ac:structured-macro><h3>Getting the Owner of an Element</h3><p>You can get the owner of an element by typing the following:</p><ul><li>&lt;variableName&gt;._getOwner()</li></ul><p>If the above method cannot find the owner, for example Model Data, it will throw an error.<br />To get the owner of an element named ClassA, for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="93b2f36d-3f7a-4a1c-9c87-1a9cef082f80"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var classA = AutomatonMacroAPI.getOpaqueObjectByPath("ClassA");
var classB = classA._getOwner();]]></ac:plain-text-body></ac:structured-macro><h3><span style="color: rgb(0,0,0);">Creating a New Element</span></h3><p>You can create a new element by using its Meta-class name, such as a Class in Standard UML or a Requirement in SysML by using the following method:</p><ul><li>AutomatonMacroAPI.createElement(String metaClassName)</li></ul><p>This method will return an opaque object of the created element. If the method cannot find the Meta-class, it will throw an exception.</p><p>To create a new Class &amp; Requirement element (Javascript), for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="182e1a3a-3338-4982-b0d4-6ff2c3584dda"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[AutomatonMacroAPI.createElement("Class");
AutomatonMacroAPI.createElement("Requirement");]]></ac:plain-text-body></ac:structured-macro><h3><span style="color: rgb(0,0,0);">Creating a Relationship Between Elements</span></h3><p>You can create a relationship between elements by typing:</p><ul><li>AutomatonMacroAPI.createRelationship(AutomatonOpaqueObject opque1, AutomatonOpaqueObject opque2, String relationName)</li></ul><p>To create a Copy &amp; Abstraction relationship between Element1 and Element2 (Javascript), for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="723d1771-b096-426b-972d-f335fcc80ec0"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var a = AutomatonMacroAPI.getOpaqueObjectByPath("Element1");
var b = AutomatonMacroAPI.getOpaqueObjectByPath("Element2");
AutomatonMacroAPI.createRelationship(a, b, "Copy"); 
AutomatonMacroAPI.createRelationship(a, b, "Abstraction");]]></ac:plain-text-body></ac:structured-macro><h3><span style="color: rgb(0,0,0);">Removing an Element</span></h3><p>You can remove an Element from the modeling tool by typing the following:</p><ul><li>AutomatonMacroAPI.removeElement(AutomatonOpaqueObject opaqueObj)</li></ul><p>To remove an Element1 (Javascript), for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="b5562de9-7a04-47c1-a4e4-6a36d2918096"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var a = AutomatonMacroAPI.getOpaqueObjectByPath("Element1");
AutomatonMacroAPI.removeElement(a);]]></ac:plain-text-body></ac:structured-macro><h3><span style="color: rgb(0,0,0);">Adding a Stereotype to an Element</span></h3><p>You can apply a stereotype to an element by typing either:</p><p style="margin-left: 30.0px;">(i) AutomatonMacroAPI.addStereotype(AutomatonOpaqueObject opaque, AutomatonOpaqueObject opaqueStereotype)<br />(ii)AutomatonMacroAPI.addStereotypeByStereotypeName(AutomatonOpaqueObject opaque, String stereotypeName)</p><p>To add a StererotypeA to ClassA (Javascript), for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="06ce36b0-5b82-4a81-99f7-54286a8f5661"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var classA = AutomatonMacroAPI.getOpaqueObjectByPath("ClassA");
var stereotypeA = AutomatonMacroAPI.getOpaqueObjectByPath("StereotypeA");
AutomatonMacroAPI.addStereotype(classA, stereotypeA);]]></ac:plain-text-body></ac:structured-macro><h3><span style="color: rgb(0,0,0);">Removing a Stereotype from an Element</span></h3><p>You can remove a Stereotype from an element by typing either:</p><p style="margin-left: 30.0px;"> (i) AutomatonMacroAPI.removeStereotype(AutomatonOpaqueObject opaque, AutomatonOpaqueObject opaqueStereotype)<br />(ii) AutomatonMacroAPI.removeStereotypeByStereotypeName(AutomatonOpaqueObject opaque, String stereotypeName)</p><p>To remove a StereotypeA from ClassA (Javascript), for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a292ad88-b730-4526-a832-0388338a51b1"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var classA = AutomatonMacroAPI.getOpaqueObjectByPath("ClassA");
var stereotypeA = AutomatonMacroAPI.getOpaqueObjectByPath("StereotypeA");
AutomatonMacroAPI.removeStereotype(classA, stereotypeA);]]></ac:plain-text-body></ac:structured-macro><h3><span style="color: rgb(0,0,0);">Printing Element Details</span></h3><p>If you want to know the method that is used in the opaque object of an element, you can print the element details by typing the following:</p><ul><li>AutomatonMacroAPI.printElementDetail(AutomatonOpaqueObject opaque);</li></ul><p>This method will print the field, constructor, and method that belong to the opaque object in the Message dialog.</p><p>To print the details of ClassA, for example, type:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4a678ae7-1721-47f9-84ec-7fff867d393b"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[var classA = AutomatonMacroAPI.getOpaqueObjectByPath("ClassA");
AutomatonMacroAPI.printElementDetail(classA);]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````
