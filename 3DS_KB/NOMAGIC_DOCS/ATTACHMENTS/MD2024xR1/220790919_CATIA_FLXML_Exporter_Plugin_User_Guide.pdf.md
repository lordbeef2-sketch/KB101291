# NOMAGIC ATTACHMENT: CATIA FLXML Exporter Plugin User Guide.pdf

- attachment_id: `220790919`
- space_key: `MD2024xR1`
- parent_page_id: `169673778`
- parent_page_title: CATIA FLXML Exporter
- media_type: `application/pdf`
- reported_bytes: 2902167
- download_url: https://docs.nomagic.com/download/attachments/169673778/CATIA%20FLXML%20Exporter%20Plugin%20User%20Guide.pdf?version=1&modificationDate=1743511488943&api=v2
- payload_kind: `pdf-extracted`
- downloaded_sha256: `c389ae146b7da496e347d8922550fb6954424bf9c2e080d99e66bce40df81954`

## LAYOUT-PRESERVING PDF EXTRACTION

### PDF PAGE 1

```text
CATIA FLXML Exporter User Guide

            CATIA Magic 2022x Refresh1
```

### PDF PAGE 2

```text
Contents

CATIA Magic 2022x Refresh1............................................................................................... 1
Revisions .............................................................................................................................. 5
CATIA FLXML Exporter Plugin Presentations ....................................................................... 5

   What will the customer use this for? .................................................................................. 5
   Purpose............................................................................................................................. 5
   License.............................................................................................................................. 6
   Principles .......................................................................................................................... 6
   Packaging ......................................................................................................................... 6
   Navigation ......................................................................................................................... 7
   Navigation from a scope element (not a diagram) ............................................................. 7
   Navigation from a diagram ................................................................................................ 7
CATIA FLXML Exporter Plugin UI ......................................................................................... 9
   Accessibility ...................................................................................................................... 9
   Generate FLXML Dialog.................................................................................................... 9
   Scope Elements .............................................................................................................. 10
   List of available schemas ................................................................................................ 11
   Destination Folder ........................................................................................................... 11
   Options............................................................................................................................ 11
   Validation ........................................................................................................................ 11
CATIA FLXML Exporter Plugin Options .............................................................................. 15
   Export references out of scope elements ........................................................................ 15
   Use dependency relationships of each element .............................................................. 16
   Create non-existing interfaces for connection.................................................................. 16
   Escalate connections ...................................................................................................... 17
   Create top level ref-ref implement links ........................................................................... 17
   Manage variation point/effectivity .................................................................................... 17
   Destination folder by default ............................................................................................ 17
   Generate a preview to use in CATIA Systems Traceability.............................................. 17
   Export image (*.png) of each diagram ............................................................................. 18
   Export image (*.png) of each diagram ............................................................................. 19
CATIA FLXML Exporter Plugin RFLP Profile & Schema ..................................................... 20
   RFLPConfigurationPackage ............................................................................................ 20
   RFLPConfiguration.......................................................................................................... 20
   RFLPSchema.................................................................................................................. 20
   RFLPRule ....................................................................................................................... 20
```

### PDF PAGE 3

```text
   RFLPAttribute.................................................................................................................. 21
   RFLPValueType.............................................................................................................. 23
   Stereotype RFLPMainView ............................................................................................. 24
   Stereotype 3DXLibrary .................................................................................................... 24
   Dynamic attribute creation............................................................................................... 24
   RFLPProfile..................................................................................................................... 26
   OOTB RFLPSchema SysML to FL .................................................................................. 27
Command Line ................................................................................................................... 28
Run CATIA Magic and the CATIA FLXML Exporter plugin in command line ....................... 28
Options of the CATIA FLXML Exporter plugin in command line .......................................... 30
   New format...................................................................................................................... 30
   Old Format ...................................................................................................................... 31
   Example of the generate_flxml.properties file .................................................................. 32
   Automation of the import of the FLXML file...................................................................... 34
FLXML ................................................................................................................................ 34
   How to import FLXML in CATIA ...................................................................................... 35
   Restrictions ..................................................................................................................... 35
FLXML Constraints & CATIA FLXML Exporter Plugin Usages ............................................ 36
   FLXML Exporter configuration ......................................................................................... 36
   FLXML object unicity ....................................................................................................... 36
   Traceability...................................................................................................................... 37
   Revision .......................................................................................................................... 37
   FLXML Update ................................................................................................................ 37
   FLXML Delete ................................................................................................................. 37
   Synchronization between FL and CATIA Magic............................................................... 38
   Effectivity/ Variation Point................................................................................................ 38
   Implementation Link ........................................................................................................ 39
CATIA FLXML Plugin Limitations ........................................................................................ 41
   Some OOTB Schemas .................................................................................................... 41
   Lifecycle .......................................................................................................................... 41
   Synchronization one-way CATIA Magic-FL ..................................................................... 41
   Schematic Views ............................................................................................................. 41
   Connection between System Type Instance (or Flow Instance) ...................................... 41
   Requirement ................................................................................................................... 41
   Logical & Functional Parameters..................................................................................... 42
   FLXML Category support ................................................................................................ 42
```

### PDF PAGE 4

```text
RFLP Types .................................................................................................................... 42
```

### PDF PAGE 5

```text
CATIA FLXML Exporter Plugin Presentations

What will the customer use this for?

The CATIA FLXML Exporter Plugin will allow clients to generate FLXML from an UML/SysML/UAF
model in order to allow the Digital continuity and to initiate the Design layer from System layer.

Purpose

Ensure digital continuity and master interfaces of a System architecture in CATIA Magic with sub-
systems either developed in 3DEXPERIENCE Platform, CATIA Magic and other tools.

The aim of the CATIA FLXML Exporter Plugin is to add the export to FLXML generation in order to
transform UML/SysML/UAF … models to Functional and Logical structures in the 3DEXPERIENCE.

                                           Ensure digital continuity and master interfaces of a System
                                           architecture in CATIA Magic with sub-systems either developed in
                                           3DEXPERIENCE Platform, CATIA Magic and other tools.

                                           Initiate transition from conceptual to design layer. Mapping based
                                           conversion of CATIA Magic data format into 3DEXPERIENCE
                                           Platform data format with lifecycle management.

                                           Example of scenario supported by default by the FLXML plugin:
Creation of Logical Objects and related Functional objects, and creation of implement links between
FL objects.
```

### PDF PAGE 6

```text
Other usages of the CATIA FLXML Exporter are not recommended.

License

The CATIA FLXML Exporter Plugin is a free plugin. No check of license is done. The plugin
installation directory follow the rules is described here:
https://docs.nomagic.com/display/MD190SP4/Plugins+directories .

Principles

From a selection of scope elements and transformation schema, the FLXML Generation Engine of
the CATIA FLXML Exporter Plugin will generate a FLXML File.
Then the user will manually import the FLXML in CATIA via the appropriate menu item in Functional
Logical Design application of 3DEXPERIENCE.

Scope Elements  FLXML Generation     FLXML File
 RFLPSchema     Engine of the CATIA
                                                    Import FLXML File in CATIA
                  FLXML Exporter                    Functional & Logical Design
                         Plugin

                CATIA Magic

                                     3DEXPERIENCE CATIA

A RFLPSchema is a set of UML Elements used to generate from UML/SYSML/UAF/… elements a
FLXML stream that can be imported in the 3DEXPERIENCE.

Packaging

The CATIA FLXML Exporter Plugin is delivered for the CATIA Magic 2022x Refresh1 version. It is
compatible with previous version since the CATIA Magic 2021x Refresh2 version.
```

### PDF PAGE 7

```text
For previous support of CATIA Magic (19 or version 2021 Refresh 1 or before) see with R&D.
The CATIA FLXML Exporter is a free plugin.
The CATIA FLXML Exporter is not delivered with 3DEXPERIENCE Role/App.

Navigation

           Navigation from a scope element (not a diagram)
A scope element is not a diagram
By default all elements under a scope element are taken into account in the FLXML generation, if a
transformation rule is compliant with the element including relations.

                                            All elements under the “Logical Architecture” Block will be taken
                                            into account.

                                            With the OOTB SysML to FL schema, if the user adds an Use
                                            Case object called UC1 under the “Logical Architecture” Block,
                                            this Use Case UC1 will not have FLXML generation because there
                                            is no transformation rule for Use Case in the OOTB SysML to FL
                                            schema.
                                            The Connector relations will have FLXML generation with the
                                            OOTB SysML to FL schema.
FLXML generation transforms elements of a scope element but also other elements of the
model required in the transformation. For instance in the previous picture, to transform the
PartProperty “:Aircraft Control System“ to a Logical Instance, the property Type of this PartProperty
is used to provide the Reference of this Logical Instance.In this case the Type is the Block “Aircraft
Control System“ which is not under the scope element “Logical Architecture”.

The option “Export references outside of scope elements” has an impact on all the elements
taken into account for the generation and on the depth of navigation of the model.

A lot of elements outside of the scope elements can be treated by the engine if they are referenced
by the scope elements or elements under the scope elements.

      Navigation from a diagram
The user may decide to generate a FLXML from an IBD diagram used as scope element. The
selection can be done from Diagram Panel, the diagram itself, Search Panel, Containment Tree ….
```

### PDF PAGE 8

```text
All the elements referred by the Presentation Elements in the IBD diagram will have an FLXML
Generation.
In the example above, Block used as Type of PartProperty will have an FLXML Generation.

         In this example, the PartProperty“part1” under the “Logical Architecture” block will not be
         taken into account because this part is not in the IBD Diagram used as scope element,
         except if the option “Export references out of scope elements” is checked.
```

### PDF PAGE 9

```text
CATIA FLXML Exporter Plugin UI

Accessibility

The CATIA FLXML Exporter is accessible via the “3DEXPERIENCE” menu as shown in the image
below.

The plugin provides a contextual menu in the ContainementTree to validate the schema of
generation.

Generate FLXML Dialog

Once clicked on the action “Generate FLXML“ menu, the dialog box below will be displayed. This
dialog box will help the user to provide the required information to generate the FLXML. The first
time that the plugin is used in a project, the Export Configuration box is empty. Click new to create
one.

When a new Export Configuration is created, the specification window opens. The same window is
opened by clicking on Edit button for an existing Export Configuration. The Export Configuration is
by pre-filled with default values.
```

### PDF PAGE 10

```text
Scope Elements

                   The read-only ‘scope elements’ text box is used to enumerate the
                   scope elements to use to generate the FLXML.

                                           This list is initialized with any element selected in the Containment
                                           Tree first.
                                           If a diagram is highlighted, the selection is initialized with the
                                           diagram.
                                           Multiple elements can be selected as scope elements of the
FLXML generation.
There is not control regarding the type of the selected scope element.
If there is only one element scope element and if this element is a diagram, the scope of the FLXML
generation will be the elements in the diagram only. The layout of the FLXML element created will
be the layout of the object in the diagram.

The browse button  close to the scope elements will give access to the Selected Elements of
CATIA Magic.
```

### PDF PAGE 11

```text
    List of available schemas
This list contains the list of elements with the stereotype RFLPSchema in the current project and
used projects and profile. See RFLP Profile § for more details on the RFLPSchema type.
A RFLP Schema is a set of rules that will allow the user to transform the elements of its models to
FL objects by generating FLXML.
The RFLP Profile contains the OOTB schema SysML to FL.

    Destination Folder
The destination folder will store the files generated by the plugin. Each FLXML generation of the
plugin will create a specific destination folder in which all files created by the plugin during the
generation will be copied. The default value of Destination Folder is set by the value of the
Environment options (Options > Environment > CATIA FLXML Exporter).

    Options
The meaning of each options is described in § CATIA FLXML Exporter Plugin Options. The
default value of each option is set by the value of the Environment options (Options > Environment
> CATIA FLXML Exporter).

Validation

The first validation is about the schema used to generate FLXML.
An example of verifications is to check that mandatory attributes are not missing in the definition of
the schema.
The second validation is done when parsing the hierarchy of the scope elements by checking
mandatory information.
Validation is done on elements in the scope’s hierarchy for which compliance rules of the schema
are found, for instance :

    - A Block is mapped by default in the OTB SysML to FL schema,
    - A Slot with not mapping defined in the OTB SysML to FL schema will not be validated but

         not considered as error.

For example, a PartProperty can have a type with the System stereotype, which has not been
defined in the mapping of the chosen schema, in this case there is a validation error.
At the end of The CATIA FLXML Validation panel (see next page) is displayed. Only errors occured
during the validation process are displayed first. Moreover, the user can decide to view also the
elements transformed, not transformed and warning messages. The error annotations will be visible
in the project.

The CATIA FLXML Validation panel is different from the Validation Results Panel of CATIA Magic
(https://docs.nomagic.com/display/CRMP2021x/Validation+Results+panel).
```

### PDF PAGE 12

```text
Even if there are validation errors in the generation of the FLXML, the user may decide to generate
the FLXML. The question below will be asked to the user:

                                                                   If the user clicks on yes the FLXML file will be
                                                                   created. In that case the user will be responsible
                                                                   of what he will then import in CATIA.
```

### PDF PAGE 13

```text
The plugin will create an annotation on each element where at least one error occurred.
A clear button will allow the user to clear the content of the CATIA FLXML Validation panel and the annotations on elements (a F5 can be
required too to update CATIA Magic UI).
A tooltip on each line will provide information on the annotation.

The user can use check box Error/Information/Not transformed or Warning to filter the generation messages found during the generation of the
FLXML.
The menu Select in Containment Tree will allow the user to select the validated element in the Containment Tree.
In the FLXML Results panel the button Export Excel is present. This button allow you to export all the content of the results in an MSExcel
file. This buttons does not take care of the state of checkbox to display/filter row in the list.
```

### PDF PAGE 14

```text
On the click of the button the user will have the possibility to select the name of the result file to create.

With the MS Excel file generated the user will have the possibility to filter the content and find all the details regarding the results of a FLXML
generation.
```

### PDF PAGE 15

```text
CATIA FLXML Exporter Plugin Options

The CATIA FLXML Exporter Plugin Options are accessible in Options > Environment
Options > CATIA FLXML Exporter options.

Export references out of scope elements

Default: true.
This option is to adapt the depth of navigation in the model.
Example: Logical architecture IBD used as scope of element for the generation.
If this option is checked, the Block “Display flight parameters Systems”’ and the elements
under this block will be taken into account.
If this option is not checked, this Block will be taken into but not all the elements under this
block, the PartProperty : “Display Temperature” for instance will not be taken into account.
```

### PDF PAGE 16

```text
        Use dependency relationships of each element                                                             © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020

          Default: false
          This option behaves like the action associated to the contextual menu item “Related
          Elements/Used by” that displays related dependency usage of an element in CATIA Magic.
          In the case of the engine of the plugin, this option is only used to take into account also
          dependency relationships of each element.
          The option can be useful to retrieve automatically allocation links of an element for instance,
          because the allocation can be easily out of the scope elements. It is possible to add
          manually all this relationships as scope elements.

          This option is false by default because retrieving all these dependencies for a lot of elements
          can be time consuming.

        Create non-existing interfaces for connection

          Default: false
                                                    Interfaces must exist on both end of a connection in the FL
                                                    Modeler.
                                                    These Activity diagram and IBD diagram are not compatible
                                                    as is with the FL Modeler. This option checked to true will
                                                    indicate to the engine to generate automatically missing
                                                    interfaces for missing ports/pins.
                                                    Default references will be used to create this interface.
                                                Instead of using this option, it is recommended that
                                                the user creates missing interfaces/ports/pins
                                                manually. (to keep coherent traceability between
                                                both models ?)

16
```

### PDF PAGE 17

```text
    Escalate connections

    Default: false

                          The FL Modeler does not support relations between
                          interfaces of differenct level without having been
                          escalated to the parent level.

                                                     With this option checked to true, the engine of the      © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
                                                    plugin will automatically escalate ports and connections
                                                    as shown in the adapted IBD here.

                                                Instead of using this option, it is recommended
                                                that the user does it manually.

    Create top level ref-ref implement links

    Default: false

    In CATIA Magic it is possible to create an allocate relationship between a PartProperty and
    CallBehaviorAction. This kind of allocation relationship correspond to an OCC-OCC relation
    in the FL Modeler.

    This OCC-OCC relation requires a parent REF-REF implement link. If no mapping to create
    this REF-REF implement link exists (between Activity and Block for instance), the engine
    will try to create a top level REF-REF implement link.

    Manage variation point/effectivity

    Default: false
    This option set by default will allow the user to support to management of variation
    point/effectivity in its model.
    The CATIA FLXML Exporter plugin will generate in a sub-folder called EffectivityXML in this
    destination folder and will place XML effectivity files in it.

    Destination folder by default

    Default: user folder

    Location where the CATIA FLXML Exporter plugin will generate the outputs.

    Generate a preview to use in CATIA Systems Traceability

    Default: true

    This option is used to indicate to the plugin to create a preview (a *.rflxmlz file file) in the
    destination folder, that can be used to preview the FLXML to import then in CATIA.

    Drag & Drop the *.rflxmlz file in a folder of a Bookmark in the CATIA Systems Traceability
    Application of the 3DEXPERIENCE

17
```

### PDF PAGE 18

```text
          Then you can preview and navigate in the FL model generated in the FLXML. It is only a     © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
          preview displayed by the RFLXML connector in CATIA Systems Traceability. No FL objects
          are created at this stage, it is only a preview.

        Export image (*.png) of each diagram

          Default: false
          Require CATIA Variables: RFLP_SCH_IMPORT=1 and RFLP_IMPORT_EXPORT=1
          Not supported in the FL Connector and in the RFLXML connector in CATIA System
          Traceability (preview generated by the plugin).
          This option will allow to view image of each diagram of CATIA Magic inside CATIA.
          Tabular/Matrix and Map diagram in CATIA Magic are not supported by this option.
          Only symbol diagrams.
          With this option the user will have the possibility to view each CATIA Magic diagrams see
          new page for an example.

                          Activity Diagram as png image in a view of the Functional Reference

18
```

### PDF PAGE 19

```text
        Export image (*.png) of each diagram                                                       © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020

          Default: false.
          This option will allow to export image of elements when the CustomImageHolder have been
          set to an element transformed as FL reference in the 3DExperience.
          For instance with the option, this IBD diagram in CATIA Magic 2022x

          Will generate this logical main view in CATIA

19
```

### PDF PAGE 20

```text
    CATIA FLXML Exporter Plugin RFLP                                                                        © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
    Profile & Schema

          The RFLP Profile contains all the structures to help the user to define its mapping and also
          the OOTB schema SysML to FL.
          The diagram below shows the list of stereotypes available to define its schema of
          transformation (or reuse the OOTB SysML to FL) schema.

          RFLPConfigurationPackage

          A RFLPCOnfigurationPackage contains 0..n RFLPConfiguration, inner elements of the
          RFLPCOnfigurationPackage.

          RFLPConfiguration

          A RFLPConfiguration defines the FLXML exporter options through its attributes.

          RFLPSchema

          A RFLPSchema contains 1..n to RFLPRule, inner elements of the RFLPSchema.
          A schema is identified by its name.

          RFLPRule

          A RFLPRule contains 0..n to RFLPAttribute, inner elements of the RFLPRule.
          A RFLPRule defines the source type of the transformation, defined by the selection of 1..n
          type of element or stereotype(s).
          A RFLPRule defines the source constraint of the transformation. Sometimes the selection of
          a type/stereotype is not sufficientto indicate what is the source of the transformation. In this
          case the user can define constraint to apply to filter more the source of the transformation.
          Most of the time the constraint will be an Object Constraint Language for UML expression.

20
```

### PDF PAGE 21

```text
          A RFLPRule defines the Destination of the transformation, this destination must be a           © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
          RFLPType element. This RFLP Type element can be either the default OOTB RFLPType
          provides in the RFLP Profile or any custom RFLPType defined by a client in its projets.
          A RFLPRule defines the Destination Category of the transformation. The Destination
          Category is the category where the FLXML generated by the plugin must be placed. The
          FLXML stream is defined by a XSD with a set of categories. Not all the categories of the
          FLXML are supported in the first version of the plugin.

          Below some examples of RFLPRules extracted from the OOTB RFLPSchema SysML to FL:

        RFLPAttribute

          A RFLPAttribute contains 0..n to RFLPAttribute, inner elements of the RFLPAttribute.
          A small example of a FLXML stream showing the FLXML for a RFLVPMLLogicalReference
          is described hereafter :
          In this example the attributes are PLM_ExternalID, BoudingBox, V_Name.
          the following attributes are mandatory : PLM_ExternalID and BoudingBox.
          V_Name is not a mandatory attribute.
          The RFLPAttribute mandatory or not depends of the category/type of the RFL object to
          create.
          Position attributes (like BoundingBox) are automatically generated by the plugin and the user
          will not have to specify these attributes.

21
```

### PDF PAGE 22

```text
                                                            This RFLPRule generated the previous FLXML. You     © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
                                                            can see that only the PLM_ExternalID or V_Name
                                                            attributes are generated.
                                                            The V_Name attribute contains an attribute Type so
                                                            RFLPAttribute Type have been defined for the
          RFLPAttribute V_Name.
          A RFLPAttribute defines only one RFLPValueType. A RFLPValueType is an enumeration of
          predefined mapping with element property and other possible types for the Value.
           A RFLPAttribute can define a Value, this value can be of different type regarding the
          RFLPValueType previously selected.
          A RFLPAttribute can define 0.n Expected Types. Expected Type are used when a same
          element under the scope elements can have mutilple RFLPRule, this property is used to
          specify which destination type is expected for this property.
          For instance a Block can be transformed in multiple FL types : Logical Reference, System
          Type Reference ... below for the “Reference” RFLPAttribute of the RFLPAttribute “Relation”
          of the RFLPRule “PartProperty to RFLVPMLogicalInstance”, it is explicitely specified that it is
          a Logical Reference that it is expected, so probably will concern the RFLPRule “Block to
          RFLVPMLogicalReference”

          With the definition of a RFLAttribute the user defines a mapping between property of
          an element/tagged value of an element/… and attributes in the FLXML.

22
```

### PDF PAGE 23

```text
                                                                                             With the definition of the    © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
                                                                                             RFLAttributes PLM_ExternalID
                                                                                             and V_Name the following
                                                                                             mapping is done

    It is possible to assign tagged value to RFLPAttribute via an OCL Expression
    oclAsType(<stereotype>).<tag name>, example oclAsType(SysML::Requirement).Text

                                                 See the OOTB RFLP Schema “SysML to FL” for other
                                                 examples of definition of RFLPAttributes.
                                                 Customer Extensions and Deployment Extensions are
                                                 supported by the plugin. Below an example of usage. The
                                                 stereotypes CustomerExtension and DeplomentExtension
                                                 can help the user to specify multiple CustomerExtension
                                                 or DeplomentExtension under the Extension attribute.

                                                 The Is Tag on RFLPAttribute is used to indicate that the
                                                 sub attribute is a child FLXML tag element (an not an
                                                 attribute of the current FLXML tag)

    RFLPValueType

    Each RFLPAttribute must have a ValueType specified. The diagram below shows the list of

    possible ValueType.

    ValueType      Description
    Literal             The value provided will be a literal
    OCLExpression       The value or the element will be provided by an OCL Expression,
                        the result can be an Element or a literal
    Name                Predefined property that corresponds to the name of the Element

23
```

### PDF PAGE 24

```text
    Signature  Predefined property that corresponds to the signature of the
               Element for instance for a PartProperty the name can be empty
    Owner      but the signature is “: Block1” where Block 1 is the name of the
    Type       type of property
    ID         Predefined property that corresponds to the owner of the
               element.

               Predefined property that corresponds to the type of the element.
               Useful only for element which have the type property of course

               Predefined property that corresponds to the unique ID of the
               Element. Server ID for TWC objects. LocalID for mdzip.

     Stereotype RFLPMainView                                                                   © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020

    When a Block has multiple IBD diagrams, the user can set the Stereotype MainView to the
    IBD Diagram that he wants to be used as RFLPMainView in the FLXML. Consequently all
    positions of PresentationElements will refer to the IBD diagram set as MainView.

    The RFLPMainView can be used for any types of diagrams in CATIA Magic.

    If the RFLPMainView stereotype has not been set, by default the plugin will use the first
    diagram found. If two MainView diagrams have been set, the first MainView is taken into
    account.

    If multiple diagrams of an element has the RFLPMainView stereotype only the first diagram
    with the stereotype is taken into account.

    The user can create an RFLPAttribute called Layout with an OCL expression to indicate
    which diagram to use as layout.

     Stereotype 3DXLibrary

    This stereotype will be used to indicate to the plugin if a Block, an Activity,a Logical
    Reference or Functional Reference refers to an existing library or component in the
    3DEXPERIENCE.

    If the user wants to specify a 3DX library or component, he should indicate the
    PLM_ExternalID and the PLM_Type of this library/component in the 3DEXPERIENCE. But
    he can also use the PLM_PhysicalID to select a specific revision of a library.

    In the FLXML generated only the Type and PLM_ExternalID will be filled, in any case the
    library/component in the 3DEXPERIENCE cannot be updated by a FLXML generated by the
    CATIA FLXML exporter plugin.

     Dynamic attribute creation

    The following example explains the usage of dynamic attribute creation based on two
    Blocks called pipe1 & pipe2. These two pipes own ValueProperty with Stereotype
    ModelicaParameter. Each diameter ValueProperty has a corresponding tagged value with
    the diameter and a specific value for each pipe (0.2 for the pipe1 and 10.0 for pipe2)

24
```

### PDF PAGE 25

```text
                                                                               pipe1 ‘s diameter ValueProperty and   © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
                                                                               associate tagged value 0.2

                                                                               pipe2 ‘s diameter ValueProperty and
                                                                               associate tagged value 10.0

          As a user of the plugin:
               - I want create a Pipe instance in the FLXML called “:pipe 1” that has the Block pipe 1
                    as Type
               - I want create a Pipe instance in the FLXML called “:pipe 2” that has the Block pipe 2
                    as Type
               - I want create a FLXML attribute called C_diameter for the Pipe instance “ : pipe1”
                    mapped to the ValueProperty diameter of the Block pipe1 and provide the 0.2 value
               - I want create a FLXML attribute called C_diameter for the Pipe instance “ : pipe2”
                    mapped to the ValueProperty diameter of the Block pipe2 and provide the 10.0 value
                                                          To resolve this case, a mapping between the
                                                          ValueProperty and an Attribute DestinationType must be
                                                          defined. The ValueProperty must have the Stereotype
                                                          Attribute of the FLXML Profile. Below is a representation
                                                          of this RFLPSchema to support this scenario:

          To define a dynamic attribute the user will have:
               - To create a RFLPRule to indicate to generate a RFLPAttribute from an Element
                    source Type defined by a stereotype or some other criterias
               - For this RFLPRule mandatory define these 4 RFLPAttributes:
                         o Name : to indicate the name of the attribute to create
                         o Owner : to indicate to which owner add this RFLPAttribute created
                              dynamically
                         o Type : to indicate the type of the value RFLPAttribute to create
                         o Value : to indicate how to get the value of this attribute, can be an OCL
                              expression or a literal or …

25
```

### PDF PAGE 26

```text
               - For this RFLRule an optinal attribute, “Instance” with a value to true can be created in   © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
                    order to indicate that the RFLAttribute must be affected to all instances of the owner
                    of this RFLPAttribute if this attribute is a Reference.

        RFLPProfile

          The OOTB RFLPSchema SysML to FL is stored in the RFLP Profile since the
          RFLPSchema is an Uml Element that contains other inner elements
          (RFLPRule/RFLPAttribute). Consequently, it is CATIA Magic project (Teamwork Cloud or
          mdzip project) that store the definition of the RFLPSchema used to do the generation of
          FLXML.
          A client can decide to create a dedicated profile or used project to define its own
          RFLPSchema that will allow to generate FLXML from the elements of its projects.

26
```

### PDF PAGE 27

```text
 OOTB RFLPSchema SysML to FL

Below CATIA Magic table that list some of RFLPRule defined in the OOTB RFLPSchema “SysML to FL” located in the RFLP Profile.
```

### PDF PAGE 28

```text
Command Line

Run CATIA Magic and the CATIA FLXML Exporter
plugin in command line

The CATIA FLXML Exporter plugin can be executed in command line.
Please, read first the documentation of CATIA magic for more details on executing Cameo in
command line:
https://docs.nomagic.com/display/MD2021xR1/Running+programs+in+batch+mode
Below an example of a Windows batch file used to run the CATIAL FLXML Exporter plugin in
command line mode. The variable MAGICDRAW_HOME contains the full path to the user
Magic Draw directory.

  la u n ch co mma n d
           .txt

Argument of -Dcom.nomagic.magicdraw.commandline.action
com.dassault_systemes.flxml.exporter.commandLine.GenerateFLXMLComman
dLineAction ^
com.nomagic.magicdraw.commandline.CommandLineActionLauncher
properties="E:\data\CommandLineMagicDraw\generate_flxml.properties"
The generate_flxml.properties is a property file with the different options to run the plugin in
command line.
Each client can have its own configuration (linux/windows …) so the execution of CATIA
should be adapted regarding the client configuration.
```

### PDF PAGE 29

```text
The execution of the FLXML Generation in command line can be done on server or a client
machine.

The usage of this command line must follow the recommended usage of the plugin in
general, reminder:
The aim of the CATIA FLXML Exporter Plugin is to add the export to FLXML generation in
order to transform UML/SysML/UAF … models to Functional and Logical structures in the
3DEXPERIENCE.

                                           Ensure digital continuity and master interfaces of a System
                                           architecture in CATIA Magic with sub-systems either
                                           developed in 3DEXPERIENCE Platform, CATIA Magic and
                                           other tools.

                                           Initiate transition from conceptual to design layer. Mapping
                                           based conversion of CATIA Magic data format into
                                           3DEXPERIENCE Platform data format with lifecycle
                                           management.

Any other usage of the CATIA XML Exporter plugin, and especially on the command
line, than the one describes above has to be avoided.

The user must be aware of what he wishes to import into the 3DEXPERIENCE after a
preliminary study of his model.
```

### PDF PAGE 30

```text
      Options of the CATIA FLXML Exporter plugin in                                                            © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
      command line

          These command line option should be stored in a property file.

        New format

          Since release 2022x Refresh1, the command line usage is simplified by the use of new
          option rflp_configuration.

                project (MANDATORY project to open)
          Specify the project to open and use to generate the FLXML.
          Please follow
          https://docs.nomagic.com/display/MD2021xR1/Running+programs+in+batch+mode to
          specify the project to open.
          Example: e:\\data\\ Aircraft Avionic.mdzip .

                rflp_configuration (MANDATORY)
          RFLPConfiguration element which contains the settings of the FLXML exporter plugin.
          The element can be identified:

                              - With its qualified name
                              - With its unique Element ID in this case in the id should be specified

                                   id:<myElementID>

          It replaces the following command line options used in the 2022x release: schema,
          destination_folder, scope_elements, option_auto_ports, option_escalated_links,
          option_reference_out_of_scope_elements, option_dependency_relationships,
          option_create_top_refref_implement_links, option_manage_effectivity,
          option_export_image_for_diagrams, option_flxml_preview, option_export_element_image.

                no_flxml_if_error
          By default true.
          Sometimes error can occur in the FLXML generation due to mapping problem for instance. If
          this option is set to true, the execution in command line will stop automatically after the
          generation and the error will be displayed in the console. If this option is set to false the flxml
          file will be generated.

                log_results
          By default false.
          If this option is set to true will generate an excel file with the results of the FLXML generation
          with errors, transformed and not transformed objects. The same excel file than describes in
          the §Export FLXML Results in MS Excel file. The result MS Excel file will be place in the
          same folder than in the FLXML file.

                log_info
          By default true. The option log_results should be set to true to be taken into account.

30
```

### PDF PAGE 31

```text
          If this option is set to true the transformation and not transformed annotations will not be       © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
          generated in the log MS Excel result file.

                log_format
          By default txt. This option to indicate the output format of the log:

                              - xls : generate an MS Excel file for the log
                              - xlstxt : generate an MS Excel and text file for the log
                              - txt : generate a text file for the log.

                import_xml_file
          This option will allow the user modify the file that defined the XMLModel used by the
          CATFLEditorImportBatch . The modifications will consist modify the XmlPath (and
          ImagePath if required).
          See documentation for the description of this file.
          https://dsdoc.dsone.3ds.com/3DEXPERIENCER2021x/en/English/DSDocDSExa.htm?show
          =SadUserMap/fle-r-
          BatchForImportExport.htm&XMLToc=DSDocDS.xml&contextscope=onpremise
          Example: E:\\data\\ confImport29290.xml
          See next §.

        Old Format

          It still possible to use the 2022x format of command line properties file. In the old format, the
          RFLPConfiguration option is replaced by the following options :

                schema (MANDATORY)
          RFLP Schema to use to generate the FLXML. By default use the OOTB RFLP Schema
          SysML to FL

                destination_folder (MANDATORY)
          Root destination folder where the FLXML file will be generated.
          The CATIA FLXML Exporter plugin will then generate a folder per generation.

                scope_elements (MANDATORY)
          List of elements to use as scope elements of the FLXML Generation
          An element can be identified:

                              - With its qualified name
                              - With its unique Element ID in this case in the id should be specified

                                   id:<myElementID>
          Each element must be separated by ;
          Examples :
          White box::Logical architecture::Logical
          architecture;id:_19_0_1_1a800cf_1559826887570_81532_41786;id:_19_0_1_1a800cf_155
          9826887379_499848_41443.

          The CATIA FLXML Exporter plugin will then generate a folder per generation.

31
```

### PDF PAGE 32

```text
                option_auto_ports                                                                           © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
          By default false. Option of the plugin.
          Option to generate automatically interface in the FLXML if port or pins does not exist in the
          UML/SysML model.

                option_escalated_links
          By default false. Option of the plugin.
          Option to generate to manage the escalated link.

                option_reference_out_of_scope_elements
          By default true. Option of the plugin.
          Option to manage automatically element transformed to references located outside of the
          scope elements.

                option_dependency_relationships
          By default false. Option of the plugin.
          Discover automatically the dependency relationships for each element. Can be time
          consuming on big project.

                option_create_top_refref_implement_links
          By default false. Option of the plugin.
          Create automatically a top REF-REF implement links for an OCC-OCC link if this REF-REF
          implement does not exist.

                option_manage_effectivity
          By default false. Option of the plugin.
          If this option is set to true the CATIA FLXML Exporter plugin will generate effectivity files and
          modified the FLXML file to support the effectivity. See the PES CATIA FLXML Exporter
          Plugin Effectivity.docx.

                option_export_image_for_diagrams
          By default false. Option of the plugin.
          If this option is set to true the CATIA FLXML Exporter plugin will generate images for symbol
          diagrams to be then imported in the 3DEXPERIENCE.

                option_flxml_preview
          By default true. Option of the plugin.
          If this option is set to true the CATIA FLXML Exporter plugin will generate a RFLXML file to
          be imported in CATIA Systems Traceability of the 3DEXPERIENCE.

                option_export_element_image
          By default false. Option of the plugin.
          If this option is set to true the CATIA FLXML Exporter plugin will generate images for FL
          references of elements that have the CustomImageHolder stereotype.

        Example of the generate_flxml.properties file

32
```

### PDF PAGE 33

```text
          New format:                                                                       © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
          project=e:\\data\\Aircraft Avionic.mdzip
          rflp_configuration=Configurations::Config1
          no_flxml_if_error=false
          log_results=true
          log_format=txt
          log_info=true
          import_xml_file=E:\\data\\confImport29290.xml
          Old format:
          project=e:\\data\\Aircraft Avionic.mdzip
          schema=SysML to FL
          destination_folder=e:\\temp
          scope_elements=White box::Logical architecture::Logical
          architecture;id:_19_0_1_1a800cf_1559826887570_81532_41786;id:_19_0_1_1a800cf_155
          9826887379_499848_41443
          no_flxml_if_error=false
          log_results=true
          log_format=txt
          log_info=true
          option_auto_ports=false
          option_escalated_links=false
          option_reference_out_of_scope_elements=true
          option_dependency_relationships=false
          option_create_top_refref_implement_links=false
          option_manage_effectivity=false
          option_export_image_for_diagrams=false
          option_flxml_preview=false
          option_export_element_image=false
          import_xml_file=E:\\data\\confImport29290.xml

33
```

### PDF PAGE 34

```text
        Automation of the import of the FLXML file                                                    © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020

          As explained before, the option import_xml_file will be used to modified for each command
          line execution the XmlPath (and ImagePath if required) of the Xml Model used to import the
          FLXML in the 3DEXPERIENCE automatically via command line.

          Below the XML Model that will be modified. In yellow what the plugin will modify.
          <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
          <RFLP>

            <Repository>PLM1</Repository>
            <Server>myserver.dsone.3ds.com/3DSpace</Server>
            <UserName>myuser</UserName>
            <Password></Password>

          <LoginTicket>QTFDODQ1RkU5REQ2NDYsqdsdqsdddI4Q0YxOEJ8YXU4fGF1OHx8fDB8</
          LoginTicket>

            <Role>VPLMProjectLeader.MyCompany.3DS Collab Space</Role>
            <DataCreation>Incremental_Data</DataCreation>
            <XMLPath>e:\temp\FLXML 20211122094950\FLXML 20211122094950.xml</XMLPath>
          </RFLP>

          To avoid errors, the file passed in arguments of the command line of the plugin must be
          modifiable with rw access for the user who run the command line of the plugin.

          The user will have the possibility to automate the import via this kind of command line

          E:\Dassault Systemes\B424_Cloud\win_b64\code\bin\CATSTART.exe -run
          "CATFLEditorImportBatch.exe confImport29290.xml" -env Env.txt -direnv " E:\Dassault
          Systemes\B424_Cloud\CATEnv"

          See the documentation for more information on how to run CATIA in command line.
          https://dsdoc.dsone.3ds.com/3DEXPERIENCER2021x/en/English/DSDocDSExa.htm?show
          =ComUserMap/com-t-BatchMonitor-
          UsingCATBatchStarterRun.htm&XMLToc=DSDocDS.xml&contextscope=onpremise

          Each client can have its own configuration (linux/windows …) so the execution of CATIA
          should be adapted regarding the client configuration.

    FLXML

          The FLXML format is the basic import / export format for Functional and Logical objects in
          the 3DEXPERIENCE. The FLXML is an XML file compatible with the
          FLImportExportXMLValidation.xsd schema.

          The purpose of this document is not to explain the FLXML format. More explanations can be
          found at: (ref in the CAA doc). Examples of 3DEXPERIENCE FL structures that can be
          created via FLXML.

34
```

### PDF PAGE 35

```text
     How to import FLXML in CATIA

    FLXML file import is accessible only in CATIA and with the Functional and Logical Design
    application opened.

      Open CATIA

      Open Apps Functional & Logical Design                                                                © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020

      Click on + button + in the toolbar

      Click on « System Architecture » menu

      Click on the “From XML …” menu

      The import dialog box is displayed, see next :

                                     Below the official documentation of the FLXML import in CATIA:
                                     https://help.3ds.com/2021x/English/DSDoc/FleUserMap/fle-t-
                                     XMLImport.htm?ContextScope=onpremise

                                     The documentation regarding the Functional & Logical Design Apps
                                     is available here
    https://help.3ds.com/2021x/English/DSDoc/FleUserMap/fle-c-
    ov.htm?ContextScope=onpremise&id=b5908c3113a74ed0a9946ae541c10508#Pg0

    Restrictions

    Some verifications done in CATIA in the import will not exist in the CATIA FLXML Exporter
    Plugin. For instance:
    - The plugin will not verify that the owner reference of a RFLVPMLogicalSystemInstance is a

         RFLVPMLogicalSystemReference or a sub type of RFLVPMLogicalSystemReference.
    - The plugin will not verify that the reference of a RFLPLMFunctionalMissionInstance is a

         RFLPLMFunctionalMissionReference
    -…
    All this kind of verifications cannot be done in the plugin, only in the import of the FLXML in CATIA.

35
```

### PDF PAGE 36

```text
    FLXML Constraints & CATIA FLXML                                                           © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
    Exporter Plugin Usages

     FLXML Exporter configuration

    When clicking on New RFLPConfiguration in the plugin UI, a new element with the RFLP
    Configuration stereotype will be created in the model.

    If a RFLPConfigurationPackage already exists in the model, the new RFLPConfiguration
    element will be created inside the existing RFLPConfigurationPackage.

    If no RFLPConfigurationPackage exists, a new RFLPConfigurationPackage named
    RFLPConfigurations will be created at the root level.

    By default, a new RFLPConfiguration element is named “RFLP Configuration n”, where n is
    the number of RFLPConfiguration elements in the model. Because of the unicity constraint
    on the RFLPConfiguration name, if a RFLPConfiguration element already has the same
    name, n will be incremented until a unique name is found.

     FLXML object unicity

    The unicity of an object in the 3DEXPERIENCE and in the FLXML is guaranteed in two
    ways:

         TNR : Type Name and Revision
         Physical Id : unique identifier

    The PLM_ExternalID attribute is the Name in the TNR

    In this FLXML example, the Type is RFLVPMLogicalReference, the Name is log-40368474-
    00000001 and the revision is A.1.

    In the Plugin, by default in the OOTB mapping:

    Attribute  Description

    PLM_ExternalID Initialize with the unique identifier of the CATIA Magic Element. For

               Teamwork Cloud, the unique identifier on the server.

    V_Name     Initialize the signature of the CATIA Magic Element, name provided

               by Java API

               RepresentationTextCreator.getRepresentedText(element)

    Type       The type is provided automatically with the rule mapping

    The user can defined its own way to identify the unicity of objects.

36
```

### PDF PAGE 37

```text
          Traceability                                                                                  © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020

          FLXML Object unicity will allow to keep the traceability between CATIA Magic objects and
          FL Objects. A CATIA Systems Traceability pattern will help to create links between CATIA
          Magic objects and FL Objects and keep the traceability.

          The mechanism of branching in the 3DEXPERIENCE will modify the PLM_ExternalID,
          consequently the user will have to have to find a mechanism to keep the traceability between
          CATIA Magic Objects and FL Objects.

          Revision

          In the FLXML definition, there is a revision attribute for objects.

          The import of the FLXML in CATIA does not take into account this revision attribute in the
          import process. Only the import of the FLXML in CATIA manages the revision of objects.
          The CATIA FLXML Exporter plugin does not manage the revision of objects.

          FLXML Update

          The FLXML unicity of objects guarantees an update scenario of objects. For example this
          scenario can be managed:

               - Generate a FLXML for a simple IBD
               - Import the FLXML in the 3DEXPERIENCE
               - Add a PartProperty related to a Block in your IBD
               - Generate a new FLXML for your simple IBD, this FLXML will be used to update FL

                    objects in the 3DEXPERIENCE
               - Import the FLXML in the 3DEXPERIENCE and the FL objects are created with the

                    new Logical Instance  the unicity of FLXML objects guarantees good update of FL
                    objects.
          This scenario works in full update or incremental mode in the import of FLXML CATIA in
          CATIA.
          See PES or Specification of the import in CATIA for more explanations no the different
          modes or possibilities of import FLXML.

          FLXML Delete

          The deletion is automatically managed by the import FLXML in CATIA with the Full update
          scenario in the import of CATIA. In incremental update in the import of FLXML in CATIA,
          there is no deletion of objects.

          Below the scenario in a full update mode in CATIA.

               - Generate a FLXML for a simple IBD with 4 PartProperty
               - Import the FLXML in the 3DEXPERIENCE
               - Remove a PartProperty related to a Block in your IBD and in the Containment Tree
               - Generate a new FLXML for your simple IBD, this FLXML will be used to update FL

                    objects in the 3DEXPERIENCE
               - Import the FLXML in the 3DEXPERIENCE and verify that the PartProperty

                    transformed to a LogicalInstance is removed from the MainView and from the
                    hierarchy.

37
```

### PDF PAGE 38

```text
               Only the import of the FLXML in CATIA manages the deletion of objects. The CATIA                         © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
               FLXML Exporter plugin does not manage the deletion of objects directly.

          Synchronization between FL and CATIA Magic

          The FLXML Exporter Plugin will not synchronize CATIA Magic Models from a FLXML
          stream.

                                                                     Consequently, any changes done on the FL
                                                                     structures in CATIA after a first import in CATIA
                                                                     of the FLXML, must be reported manually if
                                                                     needed in the CATIA Magic models too.

                                                                     The synchronization is done only one-way
                                                                     CATIA Magic  3DEXPERIENCE.

          The FLXML Exporter Plugin will not allow synchronization both ways.

          Effectivity/ Variation Point

          The plugin supports the effectivity on instances with the option Manage effectivity set to true.
          In this case the plugin works in combination of the 3DEXPERIENCE ENOVIA Model
          Definition Integration plugin.
          There are some considerations in order that the effectivity is supported by the plugin:

               - Only configuration models imported by the 3DEXPERIENCE ENOVIA Model
                    Definition Integration plugin version CATIA Magic 2021x Refresh2 or above are
                    supported.

               - Only Existence Variation Point are supported
               - Only Existence Variation Point assigned to elements transformed to instance are

                    supported
               - NOT condition are not supported by the plugin
               - All feature (or type of feature) must have the 3DSElement stereotype
               - All feature (or type of feature) must have the systemName filled with the

                    corresponding name in the 3DEXPERIENCE. This taggedvalue is initialized by the
                    3DEXPERIENCE ENOVIA Model Definition Integration plugin. If they are not
                    initialize, the user must initialized them manually.

38
```

### PDF PAGE 39

```text
          The plugin will create a sub directory of the destination folder called EffectivityXML. In this    © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
          folder, all effectivity XML files will be created.
          Example of effectivity files:

           <?xml version="1.0" ?>
           <CfgEffectivityExpression

               xmlns="urn:com:dassault_systemes:config"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="urn:com:dassault_systemes:config CfgEffectivityExpression.xsd">
               <Expression Domain="ConfigChange_Variant">

                  <Context HolderType="Model" HolderName="MV-58548725-00000012">
                     <Feature Type="ConfigFeature" Name="VAR-58548725-00000021">
                         <Feature Type="ConfigFeature" Name="VV-58548725-00000073"/></Feature>

                  </Context>
               </Expression>
           </CfgEffectivityExpression>

          I there is some missing information to generate these effectivity files, the plugin will generate
          errors.
          This PES will not explain how to use/manage effectivity in CATIA Magic.

        Implementation Link

          There is a particular behavior to manage implementation link.
          The user will have to define the Client and Supplier RFPAttribute as source and destination
          of its implementation connection.
          The value of Client and Supplier RFPAttribute should be the element that will be transformed
          to a FLXML reference in the case of REF/REF implement link creation.
          The value of Client and Supplier RFPAttribute can be also the element that will be
          transformed to a FLXML instance in the case of OCC/ OCC implement link creation. In this
          case the linked REF/REF implementation link of this OCC/OCC implementation link must be
          exist previously It is possible to use also the option “Create top level ref-ref implement links”
          see the options §.

39
```

### PDF PAGE 40

```text
40

    © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020
```

### PDF PAGE 41

```text
    CATIA FLXML Plugin Limitations                                                                            © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020

          Below the limitation of the plugin in CATIA Magic2022x Refresh 1

        Some OOTB Schemas

          In CATIA Magic 2021 Refresh 2, the plugin will not provide OOTB schemas for
          Electrical/Fluidic/EEW … Only a non-exhaustive schema mapping for SysML to FL will be
          supported. This schema is provided
          in order to support the scenario below :

                                                                  Enhancement Request should be provided for
                                                                  next releases to support other OOTB
                                                                  configurations.

        Lifecycle

          The lifecycle of object will be managed in the 3DEXPERIENCE, not with the plugin. The
          assignation of the revision of an object in the FLXML will be managed by the user when
          importing the file in 3DEXPERIENCE.

        Synchronization one-way CATIA Magic-FL

          The CATIA FLXML Exporter plugin in the first version supports only one-way
          synchronization from CATIA Magic to FL. See update/delete scenarios for some
          synchronization details.

        Schematic Views

          The CATIA FLXML Exporter plugin will not support in the first version the Schematic Views
          in the FLXML.

        Connection between System Type Instance (or Flow Instance)

          The CATIA FLXML Exporter plugin will not support in the first version the FL connection
          between System Type Instance (or Flow Instance), only with System Type Exposition
          Instance (or Flow Exposition Instance). The plugin supports only connection to simple ports.
          Will be supported in next release.

        Requirement

          The CATIA FLXML Exporter plugin will not support in its first version the creation of
          implements links that correspond to traceability. For instance, if a Satisfy link exists between
          a Block and a CATIA Magic requirement, the corresponding implement link will not be
          created between the Logical Reference created by the plugin and the TRM Requirement
          synchronized with the CATIA Magic requirement via the Datahub.
          Moreover support this, means have a dependency in the CATIA FLXML Exporter plugin with
          the Datahub plugin.

41
```

### PDF PAGE 42

```text
    Note To achieve link traceability between requirements and logical references (both coming
    from CAMEO respectively using DataHub and CATIA FLXML exporter (and FLXML import)),
    patterns in System Traceability can be used.

    Logical & Functional Parameters

    The CATIA FLXML Exporter plugin will not support in its first version the creation of Logical
    and Functional Parameters.

    FLXML Category support

    Below the exhaustive list of FLXML category supported by the CATIA FLXML Exporter

    plugin. Other Categories are not supported by default.

    #  Name                                        #                        Name
                                           10               LogicalConnection
       1 FunctionalConnection

       2 FunctionalFlowExpositionInstance  11               LogicalFlowExpositionInstance
                                                            LogicalFlowInstance
       3 FunctionalFlowInstance            12               LogicalFlowReference
                                                            LogicalImplementConnection
       6 FunctionalFlowReference           13               LogicalInstance

       7 FunctionalImplementConnection     14

       8 FunctionalInstance                15                                                      © Dassault Systèmes | Confidential Information | ref.: 3DS_Document_2020

       9 FunctionalReference               16               LogicalReference

     RFLP Types

    Below the exhaustive list of RFLP types supported by the CATIA FLXML Exporter plugin.

    #  Name                                    #            Name

    1 RFLPLMFlowExpositionInstance             11 RFLVPMLogicalInstance

    2 RFLPLMFlowInstance                       12 RFLVPMLogicalReference

    3 RFLPLMFlowReference                      13 RFLVPMSystemTypeExpositionInstance

    4 RFLPLMFunctionalMissionReference         14 RFLVPMSystemTypeInstance

    5 RFLPLMFunctionalMissionInstance          15 RFLVPMSystemTypeReference

    6 RFLPLMFunctionalConnection               16 RFLVPMLogicalConnection

    7 RFLPLMFunctionalInstance                 17 RFLVPMLogicalSystemReference

    8 RFLPLMFunctionalReference                18 RFLVPMLogicalSystemInstance

    9 RFLPLMFunctionalServiceReference         19 RFLPLMImplementConnection

    10 RFLPLMFunctionalServiceInstance

    The CATIA FLXML Exporter plugin will support FL type data model customization and
    consequently supports all the sub-types of RFLP types enumerated in the table
    above.
    All attributes supported by the import of FLXML in CATIA (including standard customization
    of attributes and extension attributes) are supported.

42
```


## EXACT ATTACHMENT METADATA

````json
{
  "id": "220790919",
  "type": "attachment",
  "status": "current",
  "title": "CATIA FLXML Exporter Plugin User Guide.pdf",
  "version": {
    "by": {
      "type": "known",
      "username": "ingabe",
      "userKey": "ff80808151f3008c0152c05ba1a40003",
      "profilePicture": {
        "path": "/download/attachments/7415957/user-avatar",
        "width": 48,
        "height": 48,
        "isDefault": false
      },
      "displayName": "Inga A.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=ff80808151f3008c0152c05ba1a40003"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2025-04-01T14:44:48.943+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/220790919/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/220790919"
    }
  },
  "position": -1,
  "container": {
    "id": "169673778",
    "type": "page",
    "status": "current",
    "title": "CATIA FLXML Exporter",
    "position": 2,
    "extensions": {
      "position": 2
    },
    "_links": {
      "webui": "/spaces/MD2024xR1/pages/169673778/CATIA+FLXML+Exporter",
      "edit": "/pages/resumedraft.action?draftId=169673778",
      "tinyui": "/x/MgQdCg",
      "self": "https://docs.nomagic.com/rest/api/content/169673778"
    },
    "_expandable": {
      "container": "/rest/api/space/MD2024xR1",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/169673778/child",
      "restrictions": "/rest/api/content/169673778/restriction/byOperation",
      "history": "/rest/api/content/169673778/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/169673778/descendant",
      "space": "/rest/api/space/MD2024xR1",
      "relevantViewRestrictions": "/rest/api/content/169673778/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/pdf"
  },
  "extensions": {
    "mediaType": "application/pdf",
    "fileSize": 2902167,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/169673778/CATIA%20FLXML%20Exporter%20Plugin%20User%20Guide.pdf?version=1&modificationDate=1743511488943&api=v2",
    "webui": "/spaces/MD2024xR1/pages/169673778/CATIA+FLXML+Exporter?preview=%2F169673778%2F220790919%2FCATIA+FLXML+Exporter+Plugin+User+Guide.pdf",
    "self": "https://docs.nomagic.com/rest/api/content/220790919"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/220790919/child",
    "restrictions": "/rest/api/content/220790919/restriction/byOperation",
    "history": "/rest/api/content/220790919/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/220790919/descendant",
    "space": "/rest/api/space/MD2024xR1",
    "relevantViewRestrictions": "/rest/api/content/220790919/restriction/relevantViewRestrictions"
  }
}
````
