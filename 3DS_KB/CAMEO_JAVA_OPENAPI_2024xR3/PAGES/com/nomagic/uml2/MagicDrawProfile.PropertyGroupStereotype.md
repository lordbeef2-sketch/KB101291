# JAVA OPENAPI: MagicDrawProfile.PropertyGroupStereotype (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/MagicDrawProfile.PropertyGroupStereotype.html
- source_path: `com/nomagic/uml2/MagicDrawProfile.PropertyGroupStereotype.html`
- source_sha256: `c066fcaab7eb9d22b1ac93a4f800a2424a89ac6321c376e4d64bf919dfb4587b`
- captured_utc: `2026-07-14T16:56:12.683653+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2](package-summary.html)

## Class MagicDrawProfile.PropertyGroupStereotype

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)
com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype

Enclosing class:
[MagicDrawProfile](MagicDrawProfile.html)

public static classMagicDrawProfile.PropertyGroupStereotype
extends [ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COLUMNS](#COLUMNS)`
p {padding:0px; margin:0px;}
 
 
 
 Stores the specified table columns for showing the values of a multivalued property in the element’s Specification window, for example, **ownedOperation** in Class.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[FILTER](#FILTER)`
p {padding:0px; margin:0px;}
 
 
 
 Stores the element types (UML metaclasses and custom stereotypes) that will be displayed as property values.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROPERTIES](#PROPERTIES)`
p {padding:0px; margin:0px;}
 
 
 
 Stores a list of properties that will be visible in the property group or subgroup.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWGROUPINCOMPARTMENTEDIT](#SHOWGROUPINCOMPARTMENTEDIT)`
p {padding:0px; margin:0px;}
 
 
 
 This property allows for displaying the element properties in the **Compartment Edit** dialog > the **Element Properties** tab and in a note on a diagram either within the property group/subgroup or without it. If the value is *true*, the property name will be displayed as follows: *<property_group_name>::<property_name>*. If the value is *false*, the property name will be displayed as follows: *<property_name>*.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWGROUPINDEPENDENCYMATRIX](#SHOWGROUPINDEPENDENCYMATRIX)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWGROUPINELEMENTSPECIFICATION](#SHOWGROUPINELEMENTSPECIFICATION)`
p {padding:0px; margin:0px;}
 
 
 
 If the value is *true*, the property group/ subgroup will be visible in the element’s Specification window.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWGROUPINGOTO](#SHOWGROUPINGOTO)`
p {padding:0px; margin:0px;}
 
 
 
 If the value is *true*, the property group/ subgroup will be visible in element’s shortcut menu as a submenu under the **Go To** menu.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWGROUPINQUICKPROPERTIES](#SHOWGROUPINQUICKPROPERTIES)`
p {padding:0px; margin:0px;}
 
 
 
 If the value is *true*, the property group/ subgroup will be visible in the element’s **Properties** panel.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHOWGROUPINRELATIONMAP](#SHOWGROUPINRELATIONMAP)`
p {padding:0px; margin:0px;}
 
 
 
 If the value is *true* , the property group/ subgroup will be visible in the **Criterion Editor** dialog, when you create or edit a Relation Map diagram.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STEREOTYPE_NAME](#STEREOTYPE_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TITLEBARDESCRIPTION](#TITLEBARDESCRIPTION)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TITLEBARNAME](#TITLEBARNAME)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[USEASNODE](#USEASNODE)`
p {padding:0px; margin:0px;}
 
 
 
 If the value is *true*, the property group will be displayed in a separate tab in the element’s Specification window and/ or **Properties** panel.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[PropertyGroupStereotype](#%3Cinit%3E(com.nomagic.uml2.MagicDrawProfile))([MagicDrawProfile](MagicDrawProfile.html) profile)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addColumns](#addColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addFilter](#addFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[addProperties](#addProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`protected void`
`[clear](#clear())()`

`void`
`[clearColumns](#clearColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearFilter](#clearFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearProperties](#clearProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowGroupInCompartmentEdit](#clearShowGroupInCompartmentEdit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowGroupInDependencyMatrix](#clearShowGroupInDependencyMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowGroupInElementSpecification](#clearShowGroupInElementSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowGroupInGoTo](#clearShowGroupInGoTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowGroupInQuickProperties](#clearShowGroupInQuickProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearShowGroupInRelationMap](#clearShowGroupInRelationMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearTitleBarDescription](#clearTitleBarDescription(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearTitleBarName](#clearTitleBarName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearUseAsNode](#clearUseAsNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getColumns](#getColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getColumnsProperty](#getColumnsProperty())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](ext/magicdraw/classes/mdkernel/Element.html)>`
`[getFilter](#getFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getFilterProperty](#getFilterProperty())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getProperties](#getProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getPropertiesProperty](#getPropertiesProperty())()`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowGroupInCompartmentEditProperty](#getShowGroupInCompartmentEditProperty())()`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowGroupInDependencyMatrixProperty](#getShowGroupInDependencyMatrixProperty())()`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowGroupInElementSpecificationProperty](#getShowGroupInElementSpecificationProperty())()`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowGroupInGoToProperty](#getShowGroupInGoToProperty())()`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowGroupInQuickPropertiesProperty](#getShowGroupInQuickPropertiesProperty())()`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getShowGroupInRelationMapProperty](#getShowGroupInRelationMapProperty())()`

`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype())()`
Returns stereotype for this wrapper.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTitleBarDescription](#getTitleBarDescription(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getTitleBarDescriptionProperty](#getTitleBarDescriptionProperty())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTitleBarName](#getTitleBarName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getTitleBarNameProperty](#getTitleBarNameProperty())()`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getUseAsNodeProperty](#getUseAsNodeProperty())()`

`boolean`
`[is](#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Checks if stereotype of this wrapper is applied to given element.
`static boolean`
`[isInstance](#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isShowGroupInCompartmentEdit](#isShowGroupInCompartmentEdit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isShowGroupInDependencyMatrix](#isShowGroupInDependencyMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isShowGroupInElementSpecification](#isShowGroupInElementSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isShowGroupInGoTo](#isShowGroupInGoTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isShowGroupInQuickProperties](#isShowGroupInQuickProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isShowGroupInRelationMap](#isShowGroupInRelationMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isUseAsNode](#isUseAsNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[removeColumns](#removeColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[removeFilter](#removeFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[removeProperties](#removeProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setColumns](#setColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setFilter](#setFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](ext/magicdraw/classes/mdkernel/Element.html)> value)`

`void`
`[setProperties](#setProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> value)`

`void`
`[setShowGroupInCompartmentEdit](#setShowGroupInCompartmentEdit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setShowGroupInDependencyMatrix](#setShowGroupInDependencyMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setShowGroupInElementSpecification](#setShowGroupInElementSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setShowGroupInGoTo](#setShowGroupInGoTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setShowGroupInQuickProperties](#setShowGroupInQuickProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setShowGroupInRelationMap](#setShowGroupInRelationMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`

`void`
`[setTitleBarDescription](#setTitleBarDescription(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setTitleBarName](#setTitleBarName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setUseAsNode](#setUseAsNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)`
Methods inherited from class com.nomagic.profiles.[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)
`[apply](../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getElement](../profiles/ProfileImplementation.StereotypeWrapper.html#getElement(com.nomagic.profiles.ProfileCache,java.lang.String)), [getTagByName](../profiles/ProfileImplementation.StereotypeWrapper.html#getTagByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)), [isDerivedStereotype](../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [isSameOrDerivedStereotype](../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [toBoolean](../profiles/ProfileImplementation.StereotypeWrapper.html#toBoolean(java.lang.Object)), [toDouble](../profiles/ProfileImplementation.StereotypeWrapper.html#toDouble(java.lang.Object)), [toInteger](../profiles/ProfileImplementation.StereotypeWrapper.html#toInteger(java.lang.Object)), [toString](../profiles/ProfileImplementation.StereotypeWrapper.html#toString(java.lang.Object)), [unApply](../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
STEREOTYPE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.STEREOTYPE_NAME)
COLUMNS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COLUMNS
p {padding:0px; margin:0px;}
Stores the specified table columns for showing the values of a multivalued property in the element’s Specification window, for example, **ownedOperation** in Class.
 
**Note:** Do not specify this property, when there is more than one property assigned to the properties group and/ or subgroup, i.e., when there is more than one value added to the **Properties** property.
 
**Note:** The property group, to which the multivalued property is assigned, must be specified as a separate tab in the element’s Specification window, for example, the **Use As Node** property must be set to *true*.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.COLUMNS)
FILTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FILTER
p {padding:0px; margin:0px;}
Stores the element types (UML metaclasses and custom stereotypes) that will be displayed as property values.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.FILTER)
PROPERTIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROPERTIES
p {padding:0px; margin:0px;}
Stores a list of properties that will be visible in the property group or subgroup.
 
**Note:** Do not set this property value to *true* for the property subgroup.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.PROPERTIES)
SHOWGROUPINCOMPARTMENTEDIT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWGROUPINCOMPARTMENTEDIT
p {padding:0px; margin:0px;}
This property allows for displaying the element properties in the **Compartment Edit** dialog > the **Element Properties** tab and in a note on a diagram either within the property group/subgroup or without it. If the value is *true*, the property name will be displayed as follows: *<property_group_name>::<property_name>*. If the value is *false*, the property name will be displayed as follows: *<property_name>*.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.SHOWGROUPINCOMPARTMENTEDIT)
SHOWGROUPINDEPENDENCYMATRIX
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWGROUPINDEPENDENCYMATRIX
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.SHOWGROUPINDEPENDENCYMATRIX)
SHOWGROUPINELEMENTSPECIFICATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWGROUPINELEMENTSPECIFICATION
p {padding:0px; margin:0px;}
If the value is *true*, the property group/ subgroup will be visible in the element’s Specification window.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.SHOWGROUPINELEMENTSPECIFICATION)
SHOWGROUPINGOTO
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWGROUPINGOTO
p {padding:0px; margin:0px;}
If the value is *true*, the property group/ subgroup will be visible in element’s shortcut menu as a submenu under the **Go To** menu.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.SHOWGROUPINGOTO)
SHOWGROUPINQUICKPROPERTIES
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWGROUPINQUICKPROPERTIES
p {padding:0px; margin:0px;}
If the value is *true*, the property group/ subgroup will be visible in the element’s **Properties** panel.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.SHOWGROUPINQUICKPROPERTIES)
SHOWGROUPINRELATIONMAP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOWGROUPINRELATIONMAP
p {padding:0px; margin:0px;}
If the value is *true* , the property group/ subgroup will be visible in the **Criterion Editor** dialog, when you create or edit a Relation Map diagram.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.SHOWGROUPINRELATIONMAP)
TITLEBARDESCRIPTION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TITLEBARDESCRIPTION
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.TITLEBARDESCRIPTION)
TITLEBARNAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TITLEBARNAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.TITLEBARNAME)
USEASNODE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) USEASNODE
p {padding:0px; margin:0px;}
If the value is *true*, the property group will be displayed in a separate tab in the element’s Specification window and/ or **Properties** panel.
 
If the value is *false*, the property group will be displayed as a group in the general (default) pane of the element’s Specification window and/ or **Properties** panel.
 
**Note:** Do not set this property value to *true* for the property subgroup.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.USEASNODE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PropertyGroupStereotype
protected PropertyGroupStereotype([MagicDrawProfile](MagicDrawProfile.html) profile)
 ============ METHOD DETAIL ========== 
Method Details
getStereotype
public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getStereotype()
Description copied from class: `[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())`
Returns stereotype for this wrapper.
Specified by:
`[getStereotype](../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())` in class `[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)`
Returns:
stereotype
getColumnsProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getColumnsProperty()
getFilterProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getFilterProperty()
getPropertiesProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getPropertiesProperty()
getShowGroupInCompartmentEditProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getShowGroupInCompartmentEditProperty()
getShowGroupInDependencyMatrixProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getShowGroupInDependencyMatrixProperty()
getShowGroupInElementSpecificationProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getShowGroupInElementSpecificationProperty()
getShowGroupInGoToProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getShowGroupInGoToProperty()
getShowGroupInQuickPropertiesProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getShowGroupInQuickPropertiesProperty()
getShowGroupInRelationMapProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getShowGroupInRelationMapProperty()
getTitleBarDescriptionProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getTitleBarDescriptionProperty()
getTitleBarNameProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getTitleBarNameProperty()
getUseAsNodeProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getUseAsNodeProperty()
setColumns
public void setColumns([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> value)
clearColumns
public void clearColumns([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
addColumns
public void addColumns([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
removeColumns
public void removeColumns([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
getColumns
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getColumns([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setFilter
public void setFilter([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](ext/magicdraw/classes/mdkernel/Element.html)> value)
clearFilter
public void clearFilter([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
addFilter
public void addFilter([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](ext/magicdraw/classes/mdkernel/Element.html) value)
removeFilter
public void removeFilter([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](ext/magicdraw/classes/mdkernel/Element.html) value)
getFilter
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](ext/magicdraw/classes/mdkernel/Element.html)> getFilter([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setProperties
public void setProperties([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> value)
clearProperties
public void clearProperties([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
addProperties
public void addProperties([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
removeProperties
public void removeProperties([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
getProperties
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getProperties([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setShowGroupInCompartmentEdit
public void setShowGroupInCompartmentEdit([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearShowGroupInCompartmentEdit
public void clearShowGroupInCompartmentEdit([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
isShowGroupInCompartmentEdit
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isShowGroupInCompartmentEdit([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setShowGroupInDependencyMatrix
public void setShowGroupInDependencyMatrix([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearShowGroupInDependencyMatrix
public void clearShowGroupInDependencyMatrix([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
isShowGroupInDependencyMatrix
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isShowGroupInDependencyMatrix([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setShowGroupInElementSpecification
public void setShowGroupInElementSpecification([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearShowGroupInElementSpecification
public void clearShowGroupInElementSpecification([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
isShowGroupInElementSpecification
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isShowGroupInElementSpecification([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setShowGroupInGoTo
public void setShowGroupInGoTo([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearShowGroupInGoTo
public void clearShowGroupInGoTo([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
isShowGroupInGoTo
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isShowGroupInGoTo([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setShowGroupInQuickProperties
public void setShowGroupInQuickProperties([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearShowGroupInQuickProperties
public void clearShowGroupInQuickProperties([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
isShowGroupInQuickProperties
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isShowGroupInQuickProperties([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setShowGroupInRelationMap
public void setShowGroupInRelationMap([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearShowGroupInRelationMap
public void clearShowGroupInRelationMap([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
isShowGroupInRelationMap
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isShowGroupInRelationMap([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setTitleBarDescription
public void setTitleBarDescription([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
clearTitleBarDescription
public void clearTitleBarDescription([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
getTitleBarDescription
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTitleBarDescription([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setTitleBarName
public void setTitleBarName([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
clearTitleBarName
public void clearTitleBarName([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
getTitleBarName
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTitleBarName([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setUseAsNode
public void setUseAsNode([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) value)
clearUseAsNode
public void clearUseAsNode([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
isUseAsNode
@CheckForNullpublic [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isUseAsNode([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
clear
protected void clear()
is
public boolean is(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Description copied from class: `[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Checks if stereotype of this wrapper is applied to given element.
Specified by:
`[is](../profiles/ProfileImplementation.StereotypeWrapper.html#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))` in class `[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)`
Parameters:
`element` - element
Returns:
true if stereotype of this wrapper is applied to given element
isInstance
public static boolean isInstance(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2</a></div>
<h1 class="title" title="Class MagicDrawProfile.PropertyGroupStereotype">Class MagicDrawProfile.PropertyGroupStereotype</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation.StereotypeWrapper</a>
<div class="inheritance">com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="MagicDrawProfile.html" title="class in com.nomagic.uml2">MagicDrawProfile</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">MagicDrawProfile.PropertyGroupStereotype</span>
<span class="extends-implements">extends <a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></span></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COLUMNS">COLUMNS</a></code></div>
<div class="col-last even-row-color">
<div class="block">
 
 
 p {padding:0px; margin:0px;}
 
 
 
 Stores the specified table columns for showing the values of a multivalued property in the element’s Specification window, for example, <b>ownedOperation</b> in Class.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FILTER">FILTER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">
 
 
 p {padding:0px; margin:0px;}
 
 
 
 Stores the element types (UML metaclasses and custom stereotypes) that will be displayed as property values.
 </div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROPERTIES">PROPERTIES</a></code></div>
<div class="col-last even-row-color">
<div class="block">
 
 
 p {padding:0px; margin:0px;}
 
 
 
 Stores a list of properties that will be visible in the property group or subgroup.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOWGROUPINCOMPARTMENTEDIT">SHOWGROUPINCOMPARTMENTEDIT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">
 
 
 p {padding:0px; margin:0px;}
 
 
 
 This property allows for displaying the element properties in the <b>Compartment Edit</b> dialog &gt; the <b>Element Properties</b> tab and in a note on a diagram either within the property group/subgroup or without it. If the value is <i>true</i>, the property name will be displayed as follows: <i>&lt;property_group_name&gt;::&lt;property_name&gt;</i>. If the value is <i>false</i>, the property name will be displayed as follows: <i>&lt;property_name&gt;</i>.
 </div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOWGROUPINDEPENDENCYMATRIX">SHOWGROUPINDEPENDENCYMATRIX</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOWGROUPINELEMENTSPECIFICATION">SHOWGROUPINELEMENTSPECIFICATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">
 
 
 p {padding:0px; margin:0px;}
 
 
 
 If the value is <i>true</i>, the property group/ subgroup will be visible in the element’s Specification window.
 </div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOWGROUPINGOTO">SHOWGROUPINGOTO</a></code></div>
<div class="col-last even-row-color">
<div class="block">
 
 
 p {padding:0px; margin:0px;}
 
 
 
 If the value is <i>true</i>, the property group/ subgroup will be visible in element’s shortcut menu as a submenu under the <b>Go To</b> menu.
 </div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOWGROUPINQUICKPROPERTIES">SHOWGROUPINQUICKPROPERTIES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">
 
 
 p {padding:0px; margin:0px;}
 
 
 
 If the value is <i>true</i>, the property group/ subgroup will be visible in the element’s <b>Properties</b> panel.
 </div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOWGROUPINRELATIONMAP">SHOWGROUPINRELATIONMAP</a></code></div>
<div class="col-last even-row-color">
<div class="block">
 
 
 p {padding:0px; margin:0px;}
 
 
 
 If the value is <i>true</i> , the property group/ subgroup will be visible in the <b>Criterion Editor</b> dialog, when you create or edit a Relation Map diagram.
 </div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STEREOTYPE_NAME">STEREOTYPE_NAME</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TITLEBARDESCRIPTION">TITLEBARDESCRIPTION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TITLEBARNAME">TITLEBARNAME</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#USEASNODE">USEASNODE</a></code></div>
<div class="col-last even-row-color">
<div class="block">
 
 
 p {padding:0px; margin:0px;}
 
 
 
 If the value is <i>true</i>, the property group will be displayed in a separate tab in the element’s Specification window and/ or <b>Properties</b> panel.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.MagicDrawProfile)">PropertyGroupStereotype</a><wbr/>(<a href="MagicDrawProfile.html" title="class in com.nomagic.uml2">MagicDrawProfile</a> profile)</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addColumns</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addFilter</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">addProperties</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clear()">clear</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearColumns</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearFilter</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearProperties</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowGroupInCompartmentEdit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowGroupInCompartmentEdit</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowGroupInDependencyMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowGroupInDependencyMatrix</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowGroupInElementSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowGroupInElementSpecification</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowGroupInGoTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowGroupInGoTo</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowGroupInQuickProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowGroupInQuickProperties</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowGroupInRelationMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearShowGroupInRelationMap</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearTitleBarDescription(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearTitleBarDescription</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearTitleBarName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearTitleBarName</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearUseAsNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearUseAsNode</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getColumns</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnsProperty()">getColumnsProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getFilter</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFilterProperty()">getFilterProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getProperties</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertiesProperty()">getPropertiesProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowGroupInCompartmentEditProperty()">getShowGroupInCompartmentEditProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowGroupInDependencyMatrixProperty()">getShowGroupInDependencyMatrixProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowGroupInElementSpecificationProperty()">getShowGroupInElementSpecificationProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowGroupInGoToProperty()">getShowGroupInGoToProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowGroupInQuickPropertiesProperty()">getShowGroupInQuickPropertiesProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShowGroupInRelationMapProperty()">getShowGroupInRelationMapProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotype()">getStereotype</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns stereotype for this wrapper.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTitleBarDescription(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getTitleBarDescription</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTitleBarDescriptionProperty()">getTitleBarDescriptionProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTitleBarName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getTitleBarName</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTitleBarNameProperty()">getTitleBarNameProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUseAsNodeProperty()">getUseAsNodeProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">is</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if stereotype of this wrapper is applied to given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isInstance</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowGroupInCompartmentEdit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowGroupInCompartmentEdit</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowGroupInDependencyMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowGroupInDependencyMatrix</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowGroupInElementSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowGroupInElementSpecification</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowGroupInGoTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowGroupInGoTo</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowGroupInQuickProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowGroupInQuickProperties</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowGroupInRelationMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isShowGroupInRelationMap</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseAsNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isUseAsNode</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeColumns</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeFilter</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">removeProperties</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setColumns</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setFilter</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">setProperties</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowGroupInCompartmentEdit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowGroupInCompartmentEdit</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowGroupInDependencyMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowGroupInDependencyMatrix</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowGroupInElementSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowGroupInElementSpecification</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowGroupInGoTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowGroupInGoTo</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowGroupInQuickProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowGroupInQuickProperties</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowGroupInRelationMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setShowGroupInRelationMap</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTitleBarDescription(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setTitleBarDescription</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTitleBarName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setTitleBarName</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseAsNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">setUseAsNode</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.profiles.ProfileImplementation.StereotypeWrapper">Methods inherited from class com.nomagic.profiles.<a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></h3>
<code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">apply</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#getElement(com.nomagic.profiles.ProfileCache,java.lang.String)">getElement</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#getTagByName(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,java.lang.String)">getTagByName</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isDerivedStereotype</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isSameOrDerivedStereotype</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#toBoolean(java.lang.Object)">toBoolean</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#toDouble(java.lang.Object)">toDouble</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#toInteger(java.lang.Object)">toInteger</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#toString(java.lang.Object)">toString</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">unApply</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="STEREOTYPE_NAME">
<h3>STEREOTYPE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STEREOTYPE_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.STEREOTYPE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLUMNS">
<h3>COLUMNS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLUMNS</span></div>
<div class="block"><html>
<head>
<style>
 p {padding:0px; margin:0px;}
 </style>
</head>
<body>
 Stores the specified table columns for showing the values of a multivalued property in the element’s Specification window, for example, <b>ownedOperation</b> in Class.
 <br/><b>Note:</b> Do not specify this property, when there is more than one property assigned to the properties group and/ or subgroup, i.e., when there is more than one value added to the <b>Properties</b> property.
 <br/><b>Note:</b> The property group, to which the multivalued property is assigned, must be specified as a separate tab in the element’s Specification window, for example, the <b>Use As Node</b> property must be set to <i>true</i>.</body>
</html></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.COLUMNS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FILTER">
<h3>FILTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FILTER</span></div>
<div class="block"><html>
<head>
<style>
 p {padding:0px; margin:0px;}
 </style>
</head>
<body>
 Stores the element types (UML metaclasses and custom stereotypes) that will be displayed as property values.</body>
</html></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.FILTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROPERTIES">
<h3>PROPERTIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROPERTIES</span></div>
<div class="block"><html>
<head>
<style>
 p {padding:0px; margin:0px;}
 </style>
</head>
<body>
 Stores a list of properties that will be visible in the property group or subgroup.
 <br/><b>Note:</b> Do not set this property value to <i>true</i> for the property subgroup.</body>
</html></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.PROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWGROUPINCOMPARTMENTEDIT">
<h3>SHOWGROUPINCOMPARTMENTEDIT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWGROUPINCOMPARTMENTEDIT</span></div>
<div class="block"><html>
<head>
<style>
 p {padding:0px; margin:0px;}
 </style>
</head>
<body>
 This property allows for displaying the element properties in the <b>Compartment Edit</b> dialog &gt; the <b>Element Properties</b> tab and in a note on a diagram either within the property group/subgroup or without it. If the value is <i>true</i>, the property name will be displayed as follows: <i>&lt;property_group_name&gt;::&lt;property_name&gt;</i>. If the value is <i>false</i>, the property name will be displayed as follows: <i>&lt;property_name&gt;</i>.</body>
</html></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.SHOWGROUPINCOMPARTMENTEDIT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWGROUPINDEPENDENCYMATRIX">
<h3>SHOWGROUPINDEPENDENCYMATRIX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWGROUPINDEPENDENCYMATRIX</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.SHOWGROUPINDEPENDENCYMATRIX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWGROUPINELEMENTSPECIFICATION">
<h3>SHOWGROUPINELEMENTSPECIFICATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWGROUPINELEMENTSPECIFICATION</span></div>
<div class="block"><html>
<head>
<style>
 p {padding:0px; margin:0px;}
 </style>
</head>
<body>
 If the value is <i>true</i>, the property group/ subgroup will be visible in the element’s Specification window.</body>
</html></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.SHOWGROUPINELEMENTSPECIFICATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWGROUPINGOTO">
<h3>SHOWGROUPINGOTO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWGROUPINGOTO</span></div>
<div class="block"><html>
<head>
<style>
 p {padding:0px; margin:0px;}
 </style>
</head>
<body>
 If the value is <i>true</i>, the property group/ subgroup will be visible in element’s shortcut menu as a submenu under the <b>Go To</b> menu.</body>
</html></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.SHOWGROUPINGOTO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWGROUPINQUICKPROPERTIES">
<h3>SHOWGROUPINQUICKPROPERTIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWGROUPINQUICKPROPERTIES</span></div>
<div class="block"><html>
<head>
<style>
 p {padding:0px; margin:0px;}
 </style>
</head>
<body>
 If the value is <i>true</i>, the property group/ subgroup will be visible in the element’s <b>Properties</b> panel.</body>
</html></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.SHOWGROUPINQUICKPROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOWGROUPINRELATIONMAP">
<h3>SHOWGROUPINRELATIONMAP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOWGROUPINRELATIONMAP</span></div>
<div class="block"><html>
<head>
<style>
 p {padding:0px; margin:0px;}
 </style>
</head>
<body>
 If the value is <i>true</i> , the property group/ subgroup will be visible in the <b>Criterion Editor</b> dialog, when you create or edit a Relation Map diagram.</body>
</html></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.SHOWGROUPINRELATIONMAP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TITLEBARDESCRIPTION">
<h3>TITLEBARDESCRIPTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TITLEBARDESCRIPTION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.TITLEBARDESCRIPTION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TITLEBARNAME">
<h3>TITLEBARNAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TITLEBARNAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.TITLEBARNAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="USEASNODE">
<h3>USEASNODE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">USEASNODE</span></div>
<div class="block"><html>
<head>
<style>
 p {padding:0px; margin:0px;}
 </style>
</head>
<body>
 If the value is <i>true</i>, the property group will be displayed in a separate tab in the element’s Specification window and/ or <b>Properties</b> panel.
 <br/>If the value is <i>false</i>, the property group will be displayed as a group in the general (default) pane of the element’s Specification window and/ or <b>Properties</b> panel.
 <br/><b>Note:</b> Do not set this property value to <i>true</i> for the property subgroup.</body>
</html></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.MagicDrawProfile.PropertyGroupStereotype.USEASNODE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.MagicDrawProfile)">
<h3>PropertyGroupStereotype</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">PropertyGroupStereotype</span><wbr/><span class="parameters">(<a href="MagicDrawProfile.html" title="class in com.nomagic.uml2">MagicDrawProfile</a> profile)</span></div>
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
<section class="detail" id="getStereotype()">
<h3>getStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">ProfileImplementation.StereotypeWrapper</a></code></span></div>
<div class="block">Returns stereotype for this wrapper.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">getStereotype</a></code> in class <code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></dd>
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnsProperty()">
<h3>getColumnsProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getColumnsProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getFilterProperty()">
<h3>getFilterProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getFilterProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getPropertiesProperty()">
<h3>getPropertiesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getPropertiesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowGroupInCompartmentEditProperty()">
<h3>getShowGroupInCompartmentEditProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowGroupInCompartmentEditProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowGroupInDependencyMatrixProperty()">
<h3>getShowGroupInDependencyMatrixProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowGroupInDependencyMatrixProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowGroupInElementSpecificationProperty()">
<h3>getShowGroupInElementSpecificationProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowGroupInElementSpecificationProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowGroupInGoToProperty()">
<h3>getShowGroupInGoToProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowGroupInGoToProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowGroupInQuickPropertiesProperty()">
<h3>getShowGroupInQuickPropertiesProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowGroupInQuickPropertiesProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getShowGroupInRelationMapProperty()">
<h3>getShowGroupInRelationMapProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getShowGroupInRelationMapProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTitleBarDescriptionProperty()">
<h3>getTitleBarDescriptionProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getTitleBarDescriptionProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTitleBarNameProperty()">
<h3>getTitleBarNameProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getTitleBarNameProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getUseAsNodeProperty()">
<h3>getUseAsNodeProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getUseAsNodeProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setColumns</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumns</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearColumns</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearColumns</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addColumns</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addColumns</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeColumns</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeColumns</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getColumns(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getColumns</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getColumns</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFilter</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearFilter</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addFilter</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeFilter</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getFilter</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>setProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperties</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearProperties</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="addProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>addProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProperties</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>removeProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeProperties</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getProperties</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowGroupInCompartmentEdit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowGroupInCompartmentEdit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowGroupInCompartmentEdit</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowGroupInCompartmentEdit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowGroupInCompartmentEdit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowGroupInCompartmentEdit</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowGroupInCompartmentEdit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowGroupInCompartmentEdit</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowGroupInCompartmentEdit</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowGroupInDependencyMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowGroupInDependencyMatrix</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowGroupInDependencyMatrix</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowGroupInDependencyMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowGroupInDependencyMatrix</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowGroupInDependencyMatrix</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowGroupInDependencyMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowGroupInDependencyMatrix</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowGroupInDependencyMatrix</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowGroupInElementSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowGroupInElementSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowGroupInElementSpecification</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowGroupInElementSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowGroupInElementSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowGroupInElementSpecification</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowGroupInElementSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowGroupInElementSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowGroupInElementSpecification</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowGroupInGoTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowGroupInGoTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowGroupInGoTo</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowGroupInGoTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowGroupInGoTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowGroupInGoTo</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowGroupInGoTo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowGroupInGoTo</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowGroupInGoTo</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowGroupInQuickProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowGroupInQuickProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowGroupInQuickProperties</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowGroupInQuickProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowGroupInQuickProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowGroupInQuickProperties</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowGroupInQuickProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowGroupInQuickProperties</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowGroupInQuickProperties</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowGroupInRelationMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setShowGroupInRelationMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowGroupInRelationMap</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearShowGroupInRelationMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearShowGroupInRelationMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowGroupInRelationMap</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowGroupInRelationMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isShowGroupInRelationMap</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isShowGroupInRelationMap</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setTitleBarDescription(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setTitleBarDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTitleBarDescription</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearTitleBarDescription(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearTitleBarDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTitleBarDescription</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTitleBarDescription(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getTitleBarDescription</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTitleBarDescription</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setTitleBarName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setTitleBarName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTitleBarName</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearTitleBarName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearTitleBarName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTitleBarName</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTitleBarName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getTitleBarName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTitleBarName</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setUseAsNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Boolean)">
<h3>setUseAsNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseAsNode</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearUseAsNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearUseAsNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearUseAsNode</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isUseAsNode(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isUseAsNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isUseAsNode</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="clear()">
<h3>clear</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clear</span>()</div>
</section>
</li>
<li>
<section class="detail" id="is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>is</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">is</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">ProfileImplementation.StereotypeWrapper</a></code></span></div>
<div class="block">Checks if stereotype of this wrapper is applied to given element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">is</a></code> in class <code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if stereotype of this wrapper is applied to given element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstance</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
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
