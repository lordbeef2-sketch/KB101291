# JAVA OPENAPI: DiagramType (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/DiagramType.html
- source_path: `com/nomagic/magicdraw/uml/DiagramType.html`
- source_sha256: `6567dad7a7a7b0e666559054ad432844841a6d27b7b8abada9af4657c5e5492b`
- captured_utc: `2026-07-14T16:55:54.735450+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class DiagramType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.AbstractDiagramType](AbstractDiagramType.html)
com.nomagic.magicdraw.uml.DiagramType

All Implemented Interfaces:
`[DiagramTypeConstants](DiagramTypeConstants.html)`, `[DiagramTypes](../../uml2/diagram/DiagramTypes.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApipublic classDiagramType
extends [AbstractDiagramType](AbstractDiagramType.html)
implements [DiagramTypeConstants](DiagramTypeConstants.html)

The `DiagramType` class represents the diagram type

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[DIAGRAMS_WITHOUT_AUTOMATIC_CONTEXT_SET](#DIAGRAMS_WITHOUT_AUTOMATIC_CONTEXT_SET)`
Fields inherited from interface com.nomagic.magicdraw.uml.[DiagramTypeConstants](DiagramTypeConstants.html)
`[STANDARD_CREATABLE_TYPES](DiagramTypeConstants.html#STANDARD_CREATABLE_TYPES), [STANDARD_NON_CREATABLE_TYPES](DiagramTypeConstants.html#STANDARD_NON_CREATABLE_TYPES), [STANDARD_TYPES](DiagramTypeConstants.html#STANDARD_TYPES)`
Fields inherited from interface com.nomagic.uml2.diagram.[DiagramTypes](../../uml2/diagram/DiagramTypes.html)
`[CONTENT_DIAGRAM](../../uml2/diagram/DiagramTypes.html#CONTENT_DIAGRAM), [DEPENDENCY_MATRIX](../../uml2/diagram/DiagramTypes.html#DEPENDENCY_MATRIX), [GENERIC_TABLE](../../uml2/diagram/DiagramTypes.html#GENERIC_TABLE), [GLOSSARY_TABLE](../../uml2/diagram/DiagramTypes.html#GLOSSARY_TABLE), [INSTANCE_TABLE](../../uml2/diagram/DiagramTypes.html#INSTANCE_TABLE), [RELATION_MAP_DIAGRAM](../../uml2/diagram/DiagramTypes.html#RELATION_MAP_DIAGRAM), [UML_ACTIVITY_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_ACTIVITY_DIAGRAM), [UML_ANY_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_ANY_DIAGRAM), [UML_BEHAVIOR_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_BEHAVIOR_DIAGRAM), [UML_CLASS_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_CLASS_DIAGRAM), [UML_COMMUNICATION_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_COMMUNICATION_DIAGRAM), [UML_COMPONENT_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_COMPONENT_DIAGRAM), [UML_COMPOSITE_STRUCTURE_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_COMPOSITE_STRUCTURE_DIAGRAM), [UML_DEPLOYMENT_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_DEPLOYMENT_DIAGRAM), [UML_INTERACTION_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_INTERACTION_DIAGRAM), [UML_INTERACTION_OVERVIEW_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_INTERACTION_OVERVIEW_DIAGRAM), [UML_OBJECT_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_OBJECT_DIAGRAM), [UML_PACKAGE_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_PACKAGE_DIAGRAM), [UML_PROFILE_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_PROFILE_DIAGRAM), [UML_PROTOCOL_STATE_MACHINE_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_PROTOCOL_STATE_MACHINE_DIAGRAM), [UML_SEQUENCE_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_SEQUENCE_DIAGRAM), [UML_STATECHART_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_STATECHART_DIAGRAM), [UML_STATIC_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_STATIC_DIAGRAM), [UML_USECASE_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_USECASE_DIAGRAM), [USER_INTERFACE_MODELING_DIAGRAM](../../uml2/diagram/DiagramTypes.html#USER_INTERFACE_MODELING_DIAGRAM)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramType](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Constructs diagram type according given diagram type string representation.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addIgnoredDiagramType](#addIgnoredDiagramType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)`
Add diagram type, which will be ignored if descriptor for this diagram type not registered.
`static void`
`[addIgnoredDiagramType](#addIgnoredDiagramType(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 boolean symbolDiagram)`
Add diagram type, which will be ignored if descriptor for this diagram type not registered.
`static void`
`[addIgnoredDiagramType](#addIgnoredDiagramType(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> diagramTypes)`
Add diagram types, which will be ignored if descriptor for this diagram type not registered.
`static void`
`[addIgnoredDiagramTypes](#addIgnoredDiagramTypes(java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> diagramTypes,
 boolean symbolDiagram)`
Add diagram types, which will be ignored if descriptor for this diagram type not registered.
`[DiagramType](DiagramType.html)`
`[clone](#clone())()`

`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?>`
`[configureContextTypeByDiagramType](#configureContextTypeByDiagramType(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.List))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> contextTypes)`
Configure owner types.
`static [DiagramType](DiagramType.html)`
`[createDiagramType](#createDiagramType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Creates diagram type of given type string representation.
`static void`
`[filterByHiddenSuggestedDSLDiagramTypes](#filterByHiddenSuggestedDSLDiagramTypes(java.lang.String,java.util.Collection))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> contextTypes)`
Filters hidden suggested DSL diagram context types.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getAbbreviatedType](#getAbbreviatedType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)`
Returns abbreviated type for given normal diagram type.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getAllDiagramTypes](#getAllDiagramTypes())()`
Returns list of all diagram types.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getAllSubtypes](#getAllSubtypes(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) root,
 boolean creatable)`
collect all subtypes of the given root diagram type.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getCreatableDiagramTypes](#getCreatableDiagramTypes())()`
Returns list of available to create (creatable) diagram types.
`static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)`
`[getDiagramActualElementType](#getDiagramActualElementType(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) owner)`

`static [DiagramType](DiagramType.html)`
`[getDiagramType](#getDiagramType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Return diagram type for a given diagram
`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getIgnoredDiagramTypes](#getIgnoredDiagramTypes())()`
Types of diagrams must be ignored.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPluralHumanName](#getPluralHumanName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Returns plural human name of the given type.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)>`
`[getPossibleDiagramOwnerTypes](#getPossibleDiagramOwnerTypes(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`

`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)>`
`[getPossibleDiagramOwnerTypes](#getPossibleDiagramOwnerTypes(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 boolean includeSuperTypeOwners)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRootType](#getRootType())()`
Returns root type of this diagram type.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRootType](#getRootType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)`
Returns root type of given diagram type.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRootUMLType](#getRootUMLType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)`
Returns root type of the UML type diagram.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getShortType](#getShortType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)`
Returns short type for given normal diagram type.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSingularHumanName](#getSingularHumanName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Returns singular human name of the given type.
`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStandardType](#getStandardType())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSuperType](#getSuperType())()`
Returns registered super type for diagram type.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSuperType](#getSuperType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) derivedType)`
Returns registered super type for given diagram type.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getType](#getType())()`
Returns the diagram type string representation
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUMLDiagramType](#getUMLDiagramType())()`
Returns UML diagram type.
`static boolean`
`[isCreatableDiagramType](#isCreatableDiagramType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Check, whether diagram type is creatable.
`boolean`
`[isEqualType](#isEqualType(com.nomagic.magicdraw.uml.DiagramType))([DiagramType](DiagramType.html) type)`
Checks if diagram type is equal to given diagram type.
`boolean`
`[isEqualType](#isEqualType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Checks if diagram type is equal to given diagram type.
`static boolean`
`[isIgnoredSymbolDiagram](#isIgnoredSymbolDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([DiagramPresentationElement](symbols/DiagramPresentationElement.html) diagramPresentationElement)`
Checks if diagram is ignored symbol diagram
`boolean`
`[isTypeOf](#isTypeOf(com.nomagic.magicdraw.uml.DiagramType))([DiagramType](DiagramType.html) type)`
Checks if diagram type is of given diagram type (analogy of `instanceof` operator)
`boolean`
`[isTypeOf](#isTypeOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Checks if diagram type is of given diagram type (analogy of `instanceof` operator)
`static boolean`
`[isTypeOf](#isTypeOf(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) unknown,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Checks if given specific type extends given generic type
`static boolean`
`[isTypeOf](#isTypeOf(java.lang.String,java.util.List))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) unknown,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> types)`

`static void`
`[registerContextTypeByDiagramTypeConfigurator](#registerContextTypeByDiagramTypeConfigurator(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator))(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator configurator)`
Registers a new context type by diagram type configurator
`static void`
`[registerDiagramType](#registerDiagramType(java.lang.String,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newType,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) superType,
 boolean creatable)`
Adds and registers new diagram type.
`static void`
`[registerHumanNames](#registerHumanNames(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newType,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) singularName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pluralName)`

`void`
`[setType](#setType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Sets the diagram type, according given diagram type string representation
`static void`
`[unregisterContextTypeByDiagramTypeConfigurator](#unregisterContextTypeByDiagramTypeConfigurator(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator))(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator configurator)`
Unregisters a new context type by diagram type configurator
`static void`
`[unregisterDiagramType](#unregisterDiagramType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
Unregisters diagram type.
Methods inherited from class com.nomagic.magicdraw.uml.[AbstractDiagramType](AbstractDiagramType.html)
`[isTypeOf](AbstractDiagramType.html#isTypeOf(java.util.List))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
DIAGRAMS_WITHOUT_AUTOMATIC_CONTEXT_SET
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> DIAGRAMS_WITHOUT_AUTOMATIC_CONTEXT_SET
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramType
@OpenApipublic DiagramType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Constructs diagram type according given diagram type string representation.
Parameters:
`type` - diagram type string representation
See Also:
[`createDiagramType(String)`](#createDiagramType(java.lang.String))
[`DiagramTypeConstants`](DiagramTypeConstants.html)
[`getAllDiagramTypes()`](#getAllDiagramTypes())
[`getCreatableDiagramTypes()`](#getCreatableDiagramTypes())
 ============ METHOD DETAIL ========== 
Method Details
getShortType
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getShortType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)
Returns short type for given normal diagram type. For example "Activity Diagram" will be "activity".
Parameters:
`diagramType` - type
Returns:
short type
getAbbreviatedType
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAbbreviatedType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)
Returns abbreviated type for given normal diagram type. For example "Activity Diagram" will be "act".
Parameters:
`diagramType` - type
Returns:
abbreviated type
getDiagramType
@OpenApipublic static [DiagramType](DiagramType.html) getDiagramType([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Return diagram type for a given diagram
Parameters:
`diagram` - diagram
Returns:
diagram type
setType
@OpenApipublic void setType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Sets the diagram type, according given diagram type string representation
Parameters:
`type` - diagram type string representation
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
[`getAllDiagramTypes()`](#getAllDiagramTypes())
[`getCreatableDiagramTypes()`](#getCreatableDiagramTypes())
getType
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getType()
Returns the diagram type string representation
Specified by:
`[getType](AbstractDiagramType.html#getType())` in class `[AbstractDiagramType](AbstractDiagramType.html)`
Returns:
diagram type string representation
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
[`getAllDiagramTypes()`](#getAllDiagramTypes())
isEqualType
@OpenApipublic boolean isEqualType([DiagramType](DiagramType.html) type)
Checks if diagram type is equal to given diagram type.
Parameters:
`type` - diagram type
Returns:
`true` if this diagram type is equal to given diagram type; otherwise - `false`.
See Also:
[`isTypeOf(DiagramType)`](#isTypeOf(com.nomagic.magicdraw.uml.DiagramType))
isEqualType
@OpenApipublic boolean isEqualType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Checks if diagram type is equal to given diagram type.
Parameters:
`type` - diagram type string representation
Returns:
`true` if this diagram type is equal to given diagram type; otherwise - `false`.
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
[`getAllDiagramTypes()`](#getAllDiagramTypes())
[`isTypeOf(String)`](#isTypeOf(java.lang.String))
isTypeOf
@OpenApipublic boolean isTypeOf([DiagramType](DiagramType.html) type)
Checks if diagram type is of given diagram type (analogy of `instanceof` operator)
Parameters:
`type` - diagram type.
Returns:
`true` if this diagram type is a 'subtype' of given diagram type or
 equal to given diagram type; otherwise - `false`.
See Also:
[`isTypeOf(String)`](#isTypeOf(java.lang.String))
isTypeOf
@OpenApipublic boolean isTypeOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Checks if diagram type is of given diagram type (analogy of `instanceof` operator)
Specified by:
`[isTypeOf](AbstractDiagramType.html#isTypeOf(java.lang.String))` in class `[AbstractDiagramType](AbstractDiagramType.html)`
Parameters:
`type` - diagram type string representation.
Returns:
`true` if this diagram type is a 'subtype' of given diagram type or
 equal to given diagram type; otherwise - `false`.
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
[`getAllDiagramTypes()`](#getAllDiagramTypes())
[`isTypeOf(DiagramType)`](#isTypeOf(com.nomagic.magicdraw.uml.DiagramType))
getRootType
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRootType()
Returns root type of this diagram type.
Returns:
root type.
clone
@OpenApipublic [DiagramType](DiagramType.html) clone()
Overrides:
`[clone](AbstractDiagramType.html#clone())` in class `[AbstractDiagramType](AbstractDiagramType.html)`
getAllDiagramTypes
@OpenApipublic static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getAllDiagramTypes()
Returns list of all diagram types.
Returns:
list of all diagram types.
See Also:
[`getCreatableDiagramTypes()`](#getCreatableDiagramTypes())
getCreatableDiagramTypes
@OpenApipublic static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getCreatableDiagramTypes()
Returns list of available to create (creatable) diagram types.
Returns:
list of available to create (creatable) diagram types.
See Also:
[`getAllDiagramTypes()`](#getAllDiagramTypes())
addIgnoredDiagramType
public static void addIgnoredDiagramType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)
Add diagram type, which will be ignored if descriptor for this diagram type not registered.
 Ignored means that it will not show messages about not loaded diagrams when is loading diagram.
Parameters:
`diagramType` - type of diagram.
addIgnoredDiagramType
public static void addIgnoredDiagramType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 boolean symbolDiagram)
Add diagram type, which will be ignored if descriptor for this diagram type not registered.
 Ignored means that it will not show messages about not loaded diagrams when is loading diagram.
Parameters:
`diagramType` - type of diagram.
`symbolDiagram` - true if diagram is symbolic
addIgnoredDiagramType
public static void addIgnoredDiagramType([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> diagramTypes)
Add diagram types, which will be ignored if descriptor for this diagram type not registered.
 Ignored means that it will not show messages about not loaded diagrams when is loading diagram.
Parameters:
`diagramTypes` - type of diagram.
addIgnoredDiagramTypes
public static void addIgnoredDiagramTypes([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> diagramTypes,
 boolean symbolDiagram)
Add diagram types, which will be ignored if descriptor for this diagram type not registered.
 Ignored means that it will not show messages about not loaded diagrams when is loading diagram.
Parameters:
`diagramTypes` - type of diagram.
`symbolDiagram` - true if diagram is symbolic
getIgnoredDiagramTypes
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getIgnoredDiagramTypes()
Types of diagrams must be ignored.
Returns:
set of diagrams types which are ignored to show warnings about missing resources.
isIgnoredSymbolDiagram
public static boolean isIgnoredSymbolDiagram([DiagramPresentationElement](symbols/DiagramPresentationElement.html) diagramPresentationElement)
Checks if diagram is ignored symbol diagram
Parameters:
`diagramPresentationElement` - diagram
Returns:
true if diagram is ignored symbol diagram
createDiagramType
@OpenApipublic static [DiagramType](DiagramType.html) createDiagramType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Creates diagram type of given type string representation.
Parameters:
`type` - diagram type string representation
Returns:
created diagram type.
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
isCreatableDiagramType
@OpenApipublic static boolean isCreatableDiagramType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Check, whether diagram type is creatable.
Parameters:
`type` - diagram type string representation
Returns:
true, if type is creatable.
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
getSuperType
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSuperType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) derivedType)
Returns registered super type for given diagram type.
Parameters:
`derivedType` - the given derived type.
Returns:
the super diagram type or null.
getSuperType
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSuperType()
Returns registered super type for diagram type.
Returns:
the super diagram type or null.
registerDiagramType
public static void registerDiagramType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newType,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) superType,
 boolean creatable)
Adds and registers new diagram type.
Parameters:
`newType` - the new diagram type.
`superType` - the 'super diagram' type of the new diagram type.
 E.g. `Interaction Diagram` is a 'super diagram' for `Collaboration Diagram` and
 `Sequence Diagram`.
`creatable` - flag indicating if the registering type diagrams will be creatable.
unregisterDiagramType
public static void unregisterDiagramType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Unregisters diagram type.
Parameters:
`type` - the diagram type.
registerHumanNames
public static void registerHumanNames([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newType,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) singularName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pluralName)
getSingularHumanName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSingularHumanName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Returns singular human name of the given type.
Parameters:
`type` - the given type.
Returns:
singular name.
getPluralHumanName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPluralHumanName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Returns plural human name of the given type.
Parameters:
`type` - the given type.
Returns:
plural name.
getUMLDiagramType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUMLDiagramType()
Returns UML diagram type.
Returns:
UML diagram type.
getStandardType
public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStandardType()
Specified by:
`[getStandardType](AbstractDiagramType.html#getStandardType())` in class `[AbstractDiagramType](AbstractDiagramType.html)`
getDiagramActualElementType
public static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) getDiagramActualElementType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) owner)
isTypeOf
public static boolean isTypeOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) unknown,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
Description copied from interface: `[DiagramTypes](../../uml2/diagram/DiagramTypes.html#isTypeOf(java.lang.String,java.lang.String))`
Checks if given specific type extends given generic type
Parameters:
`unknown` - specific type
`type` - generic type
Returns:
true if extends
isTypeOf
public static boolean isTypeOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) unknown,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> types)
getPossibleDiagramOwnerTypes
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> getPossibleDiagramOwnerTypes(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
getPossibleDiagramOwnerTypes
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> getPossibleDiagramOwnerTypes(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 boolean includeSuperTypeOwners)
Parameters:
`type` - diagram type
`includeSuperTypeOwners` - should possible owners of provided diagram type's super-type's be included
Returns:
collection of class types
getAllSubtypes
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getAllSubtypes([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) root,
 boolean creatable)
collect all subtypes of the given root diagram type. `root` is inclusive in results
Parameters:
`root` - rot diagram type of the returned result
`creatable` - if true, then only creatable types are returned
Returns:
subtypes of given rood diagram type. `root` is inclusive in results
getRootType
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRootType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)
Returns root type of given diagram type.
Returns:
root type.
getRootUMLType
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRootUMLType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)
Returns root type of the UML type diagram.
Returns:
root type one of the UML diagram type.
configureContextTypeByDiagramType
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> configureContextTypeByDiagramType([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> contextTypes)
Configure owner types. Appends allowed DSLed context types (Stereotypes), may remove passed metaclasses.
Parameters:
`project` - project
`diagramType` - diagram type
`contextTypes` - collection of java.lang.Class or Stereotype (for DSL) objects
Returns:
types
filterByHiddenSuggestedDSLDiagramTypes
public static void filterByHiddenSuggestedDSLDiagramTypes([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> contextTypes)
Filters hidden suggested DSL diagram context types.
Parameters:
`diagramType` - type of the diagram.
`contextTypes` - diagram context types.
unregisterContextTypeByDiagramTypeConfigurator
public static void unregisterContextTypeByDiagramTypeConfigurator(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator configurator)
Unregisters a new context type by diagram type configurator
Parameters:
`configurator` - configurator
registerContextTypeByDiagramTypeConfigurator
public static void registerContextTypeByDiagramTypeConfigurator(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator configurator)
Registers a new context type by diagram type configurator
Parameters:
`configurator` - configurator

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class DiagramType">Class DiagramType</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml">com.nomagic.magicdraw.uml.AbstractDiagramType</a>
<div class="inheritance">com.nomagic.magicdraw.uml.DiagramType</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml">DiagramTypeConstants</a></code>, <code><a href="../../uml2/diagram/DiagramTypes.html" title="interface in com.nomagic.uml2.diagram">DiagramTypes</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramType</span>
<span class="extends-implements">extends <a href="AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml">AbstractDiagramType</a>
implements <a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml">DiagramTypeConstants</a></span></div>
<div class="block">The <code>DiagramType</code> class represents the diagram type</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAMS_WITHOUT_AUTOMATIC_CONTEXT_SET">DIAGRAMS_WITHOUT_AUTOMATIC_CONTEXT_SET</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.DiagramTypeConstants">Fields inherited from interface com.nomagic.magicdraw.uml.<a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml">DiagramTypeConstants</a></h3>
<code><a href="DiagramTypeConstants.html#STANDARD_CREATABLE_TYPES">STANDARD_CREATABLE_TYPES</a>, <a href="DiagramTypeConstants.html#STANDARD_NON_CREATABLE_TYPES">STANDARD_NON_CREATABLE_TYPES</a>, <a href="DiagramTypeConstants.html#STANDARD_TYPES">STANDARD_TYPES</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.uml2.diagram.DiagramTypes">Fields inherited from interface com.nomagic.uml2.diagram.<a href="../../uml2/diagram/DiagramTypes.html" title="interface in com.nomagic.uml2.diagram">DiagramTypes</a></h3>
<code><a href="../../uml2/diagram/DiagramTypes.html#CONTENT_DIAGRAM">CONTENT_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#DEPENDENCY_MATRIX">DEPENDENCY_MATRIX</a>, <a href="../../uml2/diagram/DiagramTypes.html#GENERIC_TABLE">GENERIC_TABLE</a>, <a href="../../uml2/diagram/DiagramTypes.html#GLOSSARY_TABLE">GLOSSARY_TABLE</a>, <a href="../../uml2/diagram/DiagramTypes.html#INSTANCE_TABLE">INSTANCE_TABLE</a>, <a href="../../uml2/diagram/DiagramTypes.html#RELATION_MAP_DIAGRAM">RELATION_MAP_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_ACTIVITY_DIAGRAM">UML_ACTIVITY_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_ANY_DIAGRAM">UML_ANY_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_BEHAVIOR_DIAGRAM">UML_BEHAVIOR_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_CLASS_DIAGRAM">UML_CLASS_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_COMMUNICATION_DIAGRAM">UML_COMMUNICATION_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_COMPONENT_DIAGRAM">UML_COMPONENT_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_COMPOSITE_STRUCTURE_DIAGRAM">UML_COMPOSITE_STRUCTURE_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_DEPLOYMENT_DIAGRAM">UML_DEPLOYMENT_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_INTERACTION_DIAGRAM">UML_INTERACTION_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_INTERACTION_OVERVIEW_DIAGRAM">UML_INTERACTION_OVERVIEW_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_OBJECT_DIAGRAM">UML_OBJECT_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_PACKAGE_DIAGRAM">UML_PACKAGE_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_PROFILE_DIAGRAM">UML_PROFILE_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_PROTOCOL_STATE_MACHINE_DIAGRAM">UML_PROTOCOL_STATE_MACHINE_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_SEQUENCE_DIAGRAM">UML_SEQUENCE_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_STATECHART_DIAGRAM">UML_STATECHART_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_STATIC_DIAGRAM">UML_STATIC_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_USECASE_DIAGRAM">UML_USECASE_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#USER_INTERFACE_MODELING_DIAGRAM">USER_INTERFACE_MODELING_DIAGRAM</a></code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">DiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs diagram type according given diagram type string representation.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addIgnoredDiagramType(java.lang.String)">addIgnoredDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Add diagram type, which will be ignored if descriptor for this diagram type not registered.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addIgnoredDiagramType(java.lang.String,boolean)">addIgnoredDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 boolean symbolDiagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Add diagram type, which will be ignored if descriptor for this diagram type not registered.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addIgnoredDiagramType(java.util.Collection)">addIgnoredDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; diagramTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Add diagram types, which will be ignored if descriptor for this diagram type not registered.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addIgnoredDiagramTypes(java.util.Collection,boolean)">addIgnoredDiagramTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; diagramTypes,
 boolean symbolDiagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Add diagram types, which will be ignored if descriptor for this diagram type not registered.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#configureContextTypeByDiagramType(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.List)">configureContextTypeByDiagramType</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt; contextTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Configure owner types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDiagramType(java.lang.String)">createDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates diagram type of given type string representation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#filterByHiddenSuggestedDSLDiagramTypes(java.lang.String,java.util.Collection)">filterByHiddenSuggestedDSLDiagramTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; contextTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filters hidden suggested DSL diagram context types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbbreviatedType(java.lang.String)">getAbbreviatedType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns abbreviated type for given normal diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllDiagramTypes()">getAllDiagramTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns list of all diagram types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllSubtypes(java.lang.String,boolean)">getAllSubtypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> root,
 boolean creatable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">collect all subtypes of the given root diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreatableDiagramTypes()">getCreatableDiagramTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns list of available to create (creatable) diagram types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramActualElementType(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getDiagramActualElementType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getDiagramType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return diagram type for a given diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIgnoredDiagramTypes()">getIgnoredDiagramTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Types of diagrams must be ignored.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPluralHumanName(java.lang.String)">getPluralHumanName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns plural human name of the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPossibleDiagramOwnerTypes(java.lang.String)">getPossibleDiagramOwnerTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPossibleDiagramOwnerTypes(java.lang.String,boolean)">getPossibleDiagramOwnerTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 boolean includeSuperTypeOwners)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRootType()">getRootType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns root type of this diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRootType(java.lang.String)">getRootType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns root type of given diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRootUMLType(java.lang.String)">getRootUMLType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns root type of the UML type diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getShortType(java.lang.String)">getShortType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns short type for given normal diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSingularHumanName(java.lang.String)">getSingularHumanName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns singular human name of the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStandardType()">getStandardType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSuperType()">getSuperType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns registered super type for diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSuperType(java.lang.String)">getSuperType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> derivedType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns registered super type for given diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the diagram type string representation</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUMLDiagramType()">getUMLDiagramType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns UML diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreatableDiagramType(java.lang.String)">isCreatableDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check, whether diagram type is creatable.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEqualType(com.nomagic.magicdraw.uml.DiagramType)">isEqualType</a><wbr/>(<a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if diagram type is equal to given diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEqualType(java.lang.String)">isEqualType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if diagram type is equal to given diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isIgnoredSymbolDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">isIgnoredSymbolDiagram</a><wbr/>(<a href="symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentationElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if diagram is ignored symbol diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeOf(com.nomagic.magicdraw.uml.DiagramType)">isTypeOf</a><wbr/>(<a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if diagram type is of given diagram type (analogy of <code>instanceof</code> operator)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeOf(java.lang.String)">isTypeOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if diagram type is of given diagram type (analogy of <code>instanceof</code> operator)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeOf(java.lang.String,java.lang.String)">isTypeOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> unknown,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given specific type extends given generic type</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeOf(java.lang.String,java.util.List)">isTypeOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> unknown,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; types)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerContextTypeByDiagramTypeConfigurator(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator)">registerContextTypeByDiagramTypeConfigurator</a><wbr/>(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Registers a new context type by diagram type configurator</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerDiagramType(java.lang.String,java.lang.String,boolean)">registerDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> superType,
 boolean creatable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds and registers new diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerHumanNames(java.lang.String,java.lang.String,java.lang.String)">registerHumanNames</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> singularName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pluralName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setType(java.lang.String)">setType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the diagram type, according given diagram type string representation</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterContextTypeByDiagramTypeConfigurator(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator)">unregisterContextTypeByDiagramTypeConfigurator</a><wbr/>(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Unregisters a new context type by diagram type configurator</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterDiagramType(java.lang.String)">unregisterDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Unregisters diagram type.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.AbstractDiagramType">Methods inherited from class com.nomagic.magicdraw.uml.<a href="AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml">AbstractDiagramType</a></h3>
<code><a href="AbstractDiagramType.html#isTypeOf(java.util.List)">isTypeOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="DIAGRAMS_WITHOUT_AUTOMATIC_CONTEXT_SET">
<h3>DIAGRAMS_WITHOUT_AUTOMATIC_CONTEXT_SET</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">DIAGRAMS_WITHOUT_AUTOMATIC_CONTEXT_SET</span></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>DiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">DiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Constructs diagram type according given diagram type string representation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type string representation</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#createDiagramType(java.lang.String)"><code>createDiagramType(String)</code></a></li>
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
<li><a href="#getAllDiagramTypes()"><code>getAllDiagramTypes()</code></a></li>
<li><a href="#getCreatableDiagramTypes()"><code>getCreatableDiagramTypes()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getShortType(java.lang.String)">
<h3>getShortType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getShortType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">Returns short type for given normal diagram type. For example "Activity Diagram" will be "activity".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - type</dd>
<dt>Returns:</dt>
<dd>short type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbbreviatedType(java.lang.String)">
<h3>getAbbreviatedType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAbbreviatedType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">Returns abbreviated type for given normal diagram type. For example "Activity Diagram" will be "act".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - type</dd>
<dt>Returns:</dt>
<dd>abbreviated type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></span> <span class="element-name">getDiagramType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Return diagram type for a given diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram</dd>
<dt>Returns:</dt>
<dd>diagram type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setType(java.lang.String)">
<h3>setType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Sets the diagram type, according given diagram type string representation</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type string representation</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
<li><a href="#getAllDiagramTypes()"><code>getAllDiagramTypes()</code></a></li>
<li><a href="#getCreatableDiagramTypes()"><code>getCreatableDiagramTypes()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getType</span>()</div>
<div class="block">Returns the diagram type string representation</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramType.html#getType()">getType</a></code> in class <code><a href="AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml">AbstractDiagramType</a></code></dd>
<dt>Returns:</dt>
<dd>diagram type string representation</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
<li><a href="#getAllDiagramTypes()"><code>getAllDiagramTypes()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEqualType(com.nomagic.magicdraw.uml.DiagramType)">
<h3>isEqualType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEqualType</span><wbr/><span class="parameters">(<a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</span></div>
<div class="block">Checks if diagram type is equal to given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this diagram type is equal to given diagram type; otherwise - <code>false</code>.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isTypeOf(com.nomagic.magicdraw.uml.DiagramType)"><code>isTypeOf(DiagramType)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEqualType(java.lang.String)">
<h3>isEqualType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEqualType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Checks if diagram type is equal to given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type string representation</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this diagram type is equal to given diagram type; otherwise - <code>false</code>.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
<li><a href="#getAllDiagramTypes()"><code>getAllDiagramTypes()</code></a></li>
<li><a href="#isTypeOf(java.lang.String)"><code>isTypeOf(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(com.nomagic.magicdraw.uml.DiagramType)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</span></div>
<div class="block">Checks if diagram type is of given diagram type (analogy of <code>instanceof</code> operator)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type.</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this diagram type is a 'subtype' of given diagram type or
 equal to given diagram type; otherwise - <code>false</code>.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isTypeOf(java.lang.String)"><code>isTypeOf(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(java.lang.String)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Checks if diagram type is of given diagram type (analogy of <code>instanceof</code> operator)</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramType.html#isTypeOf(java.lang.String)">isTypeOf</a></code> in class <code><a href="AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml">AbstractDiagramType</a></code></dd>
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type string representation.</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this diagram type is a 'subtype' of given diagram type or
 equal to given diagram type; otherwise - <code>false</code>.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
<li><a href="#getAllDiagramTypes()"><code>getAllDiagramTypes()</code></a></li>
<li><a href="#isTypeOf(com.nomagic.magicdraw.uml.DiagramType)"><code>isTypeOf(DiagramType)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRootType()">
<h3>getRootType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRootType</span>()</div>
<div class="block">Returns root type of this diagram type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>root type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramType.html#clone()">clone</a></code> in class <code><a href="AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml">AbstractDiagramType</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllDiagramTypes()">
<h3>getAllDiagramTypes</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAllDiagramTypes</span>()</div>
<div class="block">Returns list of all diagram types.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of all diagram types.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getCreatableDiagramTypes()"><code>getCreatableDiagramTypes()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreatableDiagramTypes()">
<h3>getCreatableDiagramTypes</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getCreatableDiagramTypes</span>()</div>
<div class="block">Returns list of available to create (creatable) diagram types.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of available to create (creatable) diagram types.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getAllDiagramTypes()"><code>getAllDiagramTypes()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addIgnoredDiagramType(java.lang.String)">
<h3>addIgnoredDiagramType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addIgnoredDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">Add diagram type, which will be ignored if descriptor for this diagram type not registered.
 Ignored means that it will not show messages about not loaded diagrams when is loading diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - type of diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addIgnoredDiagramType(java.lang.String,boolean)">
<h3>addIgnoredDiagramType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addIgnoredDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 boolean symbolDiagram)</span></div>
<div class="block">Add diagram type, which will be ignored if descriptor for this diagram type not registered.
 Ignored means that it will not show messages about not loaded diagrams when is loading diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - type of diagram.</dd>
<dd><code>symbolDiagram</code> - true if diagram is symbolic</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addIgnoredDiagramType(java.util.Collection)">
<h3>addIgnoredDiagramType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addIgnoredDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; diagramTypes)</span></div>
<div class="block">Add diagram types, which will be ignored if descriptor for this diagram type not registered.
 Ignored means that it will not show messages about not loaded diagrams when is loading diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramTypes</code> - type of diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addIgnoredDiagramTypes(java.util.Collection,boolean)">
<h3>addIgnoredDiagramTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addIgnoredDiagramTypes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; diagramTypes,
 boolean symbolDiagram)</span></div>
<div class="block">Add diagram types, which will be ignored if descriptor for this diagram type not registered.
 Ignored means that it will not show messages about not loaded diagrams when is loading diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramTypes</code> - type of diagram.</dd>
<dd><code>symbolDiagram</code> - true if diagram is symbolic</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIgnoredDiagramTypes()">
<h3>getIgnoredDiagramTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getIgnoredDiagramTypes</span>()</div>
<div class="block">Types of diagrams must be ignored.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>set of diagrams types which are ignored to show warnings about missing resources.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isIgnoredSymbolDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>isIgnoredSymbolDiagram</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isIgnoredSymbolDiagram</span><wbr/><span class="parameters">(<a href="symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentationElement)</span></div>
<div class="block">Checks if diagram is ignored symbol diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramPresentationElement</code> - diagram</dd>
<dt>Returns:</dt>
<dd>true if diagram is ignored symbol diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDiagramType(java.lang.String)">
<h3>createDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></span> <span class="element-name">createDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Creates diagram type of given type string representation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type string representation</dd>
<dt>Returns:</dt>
<dd>created diagram type.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreatableDiagramType(java.lang.String)">
<h3>isCreatableDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCreatableDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Check, whether diagram type is creatable.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type string representation</dd>
<dt>Returns:</dt>
<dd>true, if type is creatable.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSuperType(java.lang.String)">
<h3>getSuperType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSuperType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> derivedType)</span></div>
<div class="block">Returns registered super type for given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>derivedType</code> - the given derived type.</dd>
<dt>Returns:</dt>
<dd>the super diagram type or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSuperType()">
<h3>getSuperType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSuperType</span>()</div>
<div class="block">Returns registered super type for diagram type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the super diagram type or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerDiagramType(java.lang.String,java.lang.String,boolean)">
<h3>registerDiagramType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">registerDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> superType,
 boolean creatable)</span></div>
<div class="block">Adds and registers new diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>newType</code> - the new diagram type.</dd>
<dd><code>superType</code> - the 'super diagram' type of the new diagram type.
                  E.g. <code>Interaction Diagram</code> is a 'super diagram' for <code>Collaboration Diagram</code> and
                  <code>Sequence Diagram</code>.</dd>
<dd><code>creatable</code> - flag indicating if the registering type diagrams will be creatable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregisterDiagramType(java.lang.String)">
<h3>unregisterDiagramType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unregisterDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Unregisters diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the  diagram type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerHumanNames(java.lang.String,java.lang.String,java.lang.String)">
<h3>registerHumanNames</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">registerHumanNames</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> singularName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pluralName)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSingularHumanName(java.lang.String)">
<h3>getSingularHumanName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSingularHumanName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Returns singular human name of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the given type.</dd>
<dt>Returns:</dt>
<dd>singular name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPluralHumanName(java.lang.String)">
<h3>getPluralHumanName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPluralHumanName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Returns plural human name of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the given type.</dd>
<dt>Returns:</dt>
<dd>plural name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUMLDiagramType()">
<h3>getUMLDiagramType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUMLDiagramType</span>()</div>
<div class="block">Returns UML diagram type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>UML diagram type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStandardType()">
<h3>getStandardType</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStandardType</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramType.html#getStandardType()">getStandardType</a></code> in class <code><a href="AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml">AbstractDiagramType</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramActualElementType(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getDiagramActualElementType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a></span> <span class="element-name">getDiagramActualElementType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owner)</span></div>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(java.lang.String,java.lang.String)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> unknown,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../uml2/diagram/DiagramTypes.html#isTypeOf(java.lang.String,java.lang.String)">DiagramTypes</a></code></span></div>
<div class="block">Checks if given specific type extends given generic type</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>unknown</code> - specific type</dd>
<dd><code>type</code> - generic type</dd>
<dt>Returns:</dt>
<dd>true if extends</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(java.lang.String,java.util.List)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> unknown,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; types)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPossibleDiagramOwnerTypes(java.lang.String)">
<h3>getPossibleDiagramOwnerTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</span> <span class="element-name">getPossibleDiagramOwnerTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPossibleDiagramOwnerTypes(java.lang.String,boolean)">
<h3>getPossibleDiagramOwnerTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</span> <span class="element-name">getPossibleDiagramOwnerTypes</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 boolean includeSuperTypeOwners)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type</dd>
<dd><code>includeSuperTypeOwners</code> - should possible owners of provided diagram type's super-type's be included</dd>
<dt>Returns:</dt>
<dd>collection of class types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllSubtypes(java.lang.String,boolean)">
<h3>getAllSubtypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAllSubtypes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> root,
 boolean creatable)</span></div>
<div class="block">collect all subtypes of the given root diagram type. <code>root</code> is inclusive in results</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - rot diagram type of the returned result</dd>
<dd><code>creatable</code> - if true, then only creatable types are returned</dd>
<dt>Returns:</dt>
<dd>subtypes of given rood diagram type. <code>root</code> is inclusive in results</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRootType(java.lang.String)">
<h3>getRootType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRootType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">Returns root type of given diagram type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>root type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRootUMLType(java.lang.String)">
<h3>getRootUMLType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRootUMLType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">Returns root type of the UML type diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>root type one of the UML diagram type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configureContextTypeByDiagramType(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.List)">
<h3>configureContextTypeByDiagramType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt;</span> <span class="element-name">configureContextTypeByDiagramType</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt; contextTypes)</span></div>
<div class="block">Configure owner types. Appends allowed DSLed context types (Stereotypes), may remove passed metaclasses.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>diagramType</code> - diagram type</dd>
<dd><code>contextTypes</code> - collection of java.lang.Class or Stereotype (for DSL) objects</dd>
<dt>Returns:</dt>
<dd>types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterByHiddenSuggestedDSLDiagramTypes(java.lang.String,java.util.Collection)">
<h3>filterByHiddenSuggestedDSLDiagramTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">filterByHiddenSuggestedDSLDiagramTypes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; contextTypes)</span></div>
<div class="block">Filters hidden suggested DSL diagram context types.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - type of the diagram.</dd>
<dd><code>contextTypes</code> - diagram context types.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregisterContextTypeByDiagramTypeConfigurator(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator)">
<h3>unregisterContextTypeByDiagramTypeConfigurator</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unregisterContextTypeByDiagramTypeConfigurator</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator configurator)</span></div>
<div class="block">Unregisters a new context type by diagram type configurator</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerContextTypeByDiagramTypeConfigurator(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator)">
<h3>registerContextTypeByDiagramTypeConfigurator</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">registerContextTypeByDiagramTypeConfigurator</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.DiagramType.ContextTypesConfigurator configurator)</span></div>
<div class="block">Registers a new context type by diagram type configurator</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
