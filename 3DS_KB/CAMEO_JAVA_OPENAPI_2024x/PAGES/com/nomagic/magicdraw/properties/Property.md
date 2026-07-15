# JAVA OPENAPI: Property (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/properties/Property.html
- source_path: `com/nomagic/magicdraw/properties/Property.html`
- source_sha256: `6864d0385dc637005c8a8235e000d6d7871efa62b89df1652378519086408528`
- captured_utc: `2026-07-14T16:51:26.831278+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class Property

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.properties.Property

All Implemented Interfaces:
`[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[AbstractChoiceProperty](AbstractChoiceProperty.html)`, `[BooleanProperty](BooleanProperty.html)`, `[ColorProperty](ColorProperty.html)`, `[ElementProperty](ElementProperty.html)`, `[FileProperty](FileProperty.html)`, `[FontProperty](FontProperty.html)`, `[ListProperty](ListProperty.html)`, `[NumberProperty](NumberProperty.html)`, `[PageFormatProperty](PageFormatProperty.html)`, `[StringProperty](StringProperty.html)`, `[TypeProperty](TypeProperty.html)`

@OpenApiAllpublic classProperty
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html), [PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)

This class represents some property with some value.
 This is based class, specific type properties must be derived from this class.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected static final [PropertyResourceProvider](PropertyResourceProvider.html)`
`[DEFAULT_PROPERTY_RESOURCE_PROVIDER](#DEFAULT_PROPERTY_RESOURCE_PROVIDER)`
Default property resource provider.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EDITABLE](#EDITABLE)`
"Editable" property name
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NULL](#NULL)`
Representation of null value as string.
`static final [PropertyResourceProvider](PropertyResourceProvider.html)`
`[NULL_ID_PROPERTY_RESOURCE_PROVIDER](#NULL_ID_PROPERTY_RESOURCE_PROVIDER)`
A resource provider which does not try to translate property ID.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TO](#TO)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UNDEFINED](#UNDEFINED)`
Property "undefined" state literal.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALUE](#VALUE)`
"Value" property name
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALUE_ANNOTATIONS](#VALUE_ANNOTATIONS)`
"valueAnnotations" property name
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Property](#%3Cinit%3E())()`
Constructs new property.
`[Property](#%3Cinit%3E(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
The property constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected final [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[_getValue](#_getValue())()`

`boolean`
`[_isFrozen](#_isFrozen())()`

`void`
`[_setFrozen](#_setFrozen(boolean))(boolean frozen)`
This is an internal api method to mark property as frozen.
`protected final void`
`[_setValue](#_setValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`

`void`
`[accept](#accept(com.nomagic.magicdraw.properties.PropertyVisitor))([PropertyVisitor](PropertyVisitor.html) v)`
Accepts the given visitor.
`void`
`[addAnnotation](#addAnnotation(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addPropertyChangeListener](#addPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Delegates `addPropertyChangeListener` to the
 `PropertyChangeSupport`, the member of this class,
 which adds a `PropertyChangeListener` to the listener list.
`void`
`[addSource](#addSource(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) source)`
Add source object to a project.
`void`
`[addSources](#addSources(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> sources)`
Append given sources to already existing ones.
`boolean`
`[areEqualByValue](#areEqualByValue(com.nomagic.magicdraw.properties.Property))([Property](Property.html) other)`

`protected boolean`
`[areValuesEqual](#areValuesEqual(java.lang.Object,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)`
Check if values are equal before setting new value.
`protected void`
`[checkFrozen](#checkFrozen())()`

`protected void`
`[checkFrozen](#checkFrozen(java.util.function.Supplier))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> detailsSupplier)`

`[Property](Property.html)`
`[clone](#clone())()`
Clones the property.
`[CellEditor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/CellEditor.html)`
`[createCellEditor](#createCellEditor(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory))(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory factory)`
Returns the cell editor which edits this property in swing table.
`[TableCellRenderer](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html)`
`[createTableCellRenderer](#createTableCellRenderer(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory))(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory factory)`
Returns the cell renderer which renders this property in swing table.
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`
Properties are equal if their id are equals.
`void`
`[firePropertyChange](#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)`
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[generateDefaultDescriptionID](#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property))([Property](Property.html) property)`
Generates default property description id from property id
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getAdditionalProperties](#getAdditionalProperties())()`
Return a map structure of attached tags to this property.
`<T> T`
`[getAdditionalProperty](#getAdditionalProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tag)`
Return attached "tag" like string value
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getAnnotation](#getAnnotation(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getAnnotations](#getAnnotations())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getClassType](#getClassType())()`
Returns property class type.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription())()`
Returns property description from resource provider by property description id.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescriptionID](#getDescriptionID())()`
Returns property description ID.
`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getFirstElementFromSources](#getFirstElementFromSources())()`
Looks for a first Element among sources.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getGroup](#getGroup())()`
Returns group name for property.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`
Returns property id.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getIntroductoryVersion](#getIntroductoryVersion())()`
Get application version the property was introduced in.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Returns name of the property.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getNonEditableReason](#getNonEditableReason())()`
Returns the property reason
`[Project](../core/Project.html)`
`[getProjectFromSourcesOrActive](#getProjectFromSourcesOrActive())()`
Looks for a project of property's sources
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPureDescription](#getPureDescription())()`
Returns pure description - does not goes into resource provider.
`[PropertyResourceProvider](PropertyResourceProvider.html)`
`[getResourceProvider](#getResourceProvider())()`
Returns `PropertyResourceProvider`.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getResourceProviderID](#getResourceProviderID())()`
Returns Resource provider ID.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSortableValueStringRepresentation](#getSortableValueStringRepresentation())()`

`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getSourceAsElement](#getSourceAsElement())()`
Returns source as Element if property has just one source and that source is an Element
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?>`
`[getSources](#getSources())()`
Return a collection of property sources.
`[Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getSourcesAsStream](#getSourcesAsStream())()`
Return a stream of property sources.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUndefinedString](#getUndefinedString())()`
Returns representation string for "undefined" property state
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUndefinedString](#getUndefinedString(com.nomagic.magicdraw.properties.Property))([Property](Property.html) property)`
Returns representation string for "undefined" property state.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue())()`
Returns properties value.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getValueStringRepresentation](#getValueStringRepresentation())()`
Returns value's string representation.
`int`
`[hashCode](#hashCode())()`
The hash code will be the same as ID's hash code.
`boolean`
`[isEditable](#isEditable())()`
Gets mEnabled flag's value.
`boolean`
`[isUndefinedState](#isUndefinedState())()`
Returns value undefined state flag.
`protected boolean`
`[isValueCompatible](#isValueCompatible(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`

`void`
`[removeAnnotation](#removeAnnotation(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key)`

`void`
`[removePropertyChangeListener](#removePropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Delegates `removePropertyChangeListener` to the
 `PropertyChangeSupport`, the member of this class,
 which removes a PropertyChangeListener from the listener list.
`void`
`[setAdditionalProperties](#setAdditionalProperties(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> tags)`
Replace current tags with a new ones
`void`
`[setAdditionalProperty](#setAdditionalProperty(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Attach tag like key-value information to a property
`void`
`[setAnnotations](#setAnnotations(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> annotations)`

`void`
`[setDescription](#setDescription(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)`
Set property description
`void`
`[setDescriptionID](#setDescriptionID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) descriptionID)`
Set property description ID.
`void`
`[setEditable](#setEditable(boolean))(boolean editable)`
Set mEnabled flag's value.
`void`
`[setGroup](#setGroup(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`
Sets new group name.
`final void`
`[setID](#setID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Sets property id.
`void`
`[setIntroductoryVersion](#setIntroductoryVersion(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) introductoryVersion)`
Set application version property is introduced in.
`void`
`[setNonEditableReason](#setNonEditableReason(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) reason)`
Sets the property reason
`void`
`[setResourceProvider](#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider))([PropertyResourceProvider](PropertyResourceProvider.html) provider)`
Sets PropertyResourceProvider for this property.
`void`
`[setResourceProviderID](#setResourceProviderID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourceProviderID)`
Set resource provider ID.
`void`
`[setSources](#setSources(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> sources)`
Set property's sources.
`void`
`[setUndefinedState](#setUndefinedState(boolean))(boolean value)`
Sets undefined state for this property.
`void`
`[setValue](#setValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets new property value.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Return string representation of property for debug purposes.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
TO
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TO
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.Property.TO)
VALUE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALUE
"Value" property name
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.Property.VALUE)
VALUE_ANNOTATIONS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALUE_ANNOTATIONS
"valueAnnotations" property name
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.Property.VALUE_ANNOTATIONS)
EDITABLE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EDITABLE
"Editable" property name
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.Property.EDITABLE)
UNDEFINED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UNDEFINED
Property "undefined" state literal. The [`PropertyChangeEvent.getPropertyName()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#getPropertyName()) return
 this string when state of the property changes it's "undefined" state.
See Also:
[`setUndefinedState(boolean)`](#setUndefinedState(boolean))
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.Property.UNDEFINED)
NULL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NULL
Representation of null value as string.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.Property.NULL)
DEFAULT_PROPERTY_RESOURCE_PROVIDER
protected static final [PropertyResourceProvider](PropertyResourceProvider.html) DEFAULT_PROPERTY_RESOURCE_PROVIDER
Default property resource provider.
NULL_ID_PROPERTY_RESOURCE_PROVIDER
public static final [PropertyResourceProvider](PropertyResourceProvider.html) NULL_ID_PROPERTY_RESOURCE_PROVIDER
A resource provider which does not try to translate property ID.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Property
public Property()
Constructs new property.
 Property ID will be empty string, property value - null.
Property
public Property([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
The property constructor.
Parameters:
`id` - the ID of property.
`value` - the value of the property.
 ============ METHOD DETAIL ========== 
Method Details
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Returns name of the property. Property name is taken from
 `PropertyResourceProvider` with key - Property ID.
Returns:
name of the property.
getID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getID()
Returns property id.
Returns:
property ID.
setID
public final void setID([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Sets property id.
Parameters:
`id` - a new property id.
setValue
public void setValue(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Sets new property value.
 Will fire a `PropertyChangeEvent` with propertyName - property
 ID, newValue and oldValue.
Parameters:
`value` - a new property value.
isValueCompatible
protected boolean isValueCompatible([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Returns:
true if given object can be assigned as value to this property
areValuesEqual
protected boolean areValuesEqual([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)
Check if values are equal before setting new value. If values are equal value is not changed.
Parameters:
`oldValue` - current value.
`newValue` - new value.
Returns:
true if values are equal.
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Properties are equal if their id are equals.
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Parameters:
`o` - some other Property.
hashCode
public int hashCode()
The hash code will be the same as ID's hash code.
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
property hash code.
getValue
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getValue()
Returns properties value.
Returns:
value of the property.
getValueStringRepresentation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getValueStringRepresentation()
Returns value's string representation.
Returns:
string "null" if property does not have value; `value.
 toString()` if property has value.
getSortableValueStringRepresentation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSortableValueStringRepresentation()
accept
public void accept([PropertyVisitor](PropertyVisitor.html) v)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Accepts the given visitor.
Specified by:
`[accept](PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Parameters:
`v` - the PropertyVisitor.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
createCellEditor
@CheckForNull
@NotApipublic [CellEditor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/CellEditor.html) createCellEditor(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory factory)
Returns the cell editor which edits this property in swing table.
Parameters:
`factory` - factory
Returns:
null here.
createTableCellRenderer
@CheckForNull
@NotApipublic [TableCellRenderer](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html) createTableCellRenderer(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory factory)
Returns the cell renderer which renders this property in swing table.
Parameters:
`factory` - factory
Returns:
null here.
clone
public [Property](Property.html) clone()
Clones the property. Clone is not deep, the clone will have the same instance of value.
 The clone will not have registered PropertyChangeListeners.
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
the cloned property.
setUndefinedState
public void setUndefinedState(boolean value)
Sets undefined state for this property. Notifies property
 change listeners if property undefined state changes.
Parameters:
`value` - the new value of undefined state flag.
isUndefinedState
public boolean isUndefinedState()
Returns value undefined state flag.
Returns:
value value of undefined state flag.
getClassType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getClassType()
Returns property class type.
Specified by:
`[getClassType](PropertyVisitorAcceptor.html#getClassType())` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Returns:
PropertyID.PROPERTY
See Also:
[`PropertyID.PROPERTY`](PropertyID.html#PROPERTY)
addPropertyChangeListener
public void addPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Delegates `addPropertyChangeListener` to the
 `PropertyChangeSupport`, the member of this class,
 which adds a `PropertyChangeListener` to the listener list.
Parameters:
`listener` - the `PropertyChangeListener` to be added
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
firePropertyChange
public void firePropertyChange([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new are equal and non-null.
Parameters:
`propertyName` - the programmatic name of the property that was changed.
`oldValue` - the old value of the property
`newValue` - the new value of the property
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
removePropertyChangeListener
public void removePropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Delegates `removePropertyChangeListener` to the
 `PropertyChangeSupport`, the member of this class,
 which removes a PropertyChangeListener from the listener list.
Parameters:
`listener` - the PropertyChangeListener to be removed
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Return string representation of property for debug purposes.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
string representation of the property.
getResourceProviderID
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getResourceProviderID()
Returns Resource provider ID.
Returns:
id of resource provider.
setResourceProviderID
public void setResourceProviderID(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourceProviderID)
Set resource provider ID.
Parameters:
`resourceProviderID` - resource provider id
setResourceProvider
public void setResourceProvider(@CheckForNull
 [PropertyResourceProvider](PropertyResourceProvider.html) provider)
Sets PropertyResourceProvider for this property.
Parameters:
`provider` - the given provider.
getResourceProvider
public [PropertyResourceProvider](PropertyResourceProvider.html) getResourceProvider()
Returns `PropertyResourceProvider`. If property does not have
 resource provider returns shared instance of
 `DefaultPropertyResourceProvider`.
Returns:
set `PropertyResourceProvider` or default one.
getGroup
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getGroup()
Returns group name for property. Properties with same group can be grouped in GUI.
Returns:
Returns group name for property. Can be null.
setGroup
public void setGroup(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
Sets new group name.
Parameters:
`group` - group name, can be null.
getDescriptionID
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescriptionID()
Returns property description ID.
Returns:
description id.
setDescriptionID
public void setDescriptionID(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) descriptionID)
Set property description ID.
Parameters:
`descriptionID` - description id.
setDescription
public void setDescription(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)
Set property description
Parameters:
`description` - description
getDescription
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescription()
Returns property description from resource provider by property description id. May be null.
Returns:
description of the property.
getPureDescription
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPureDescription()
Returns pure description - does not goes into resource provider.
Returns:
description
generateDefaultDescriptionID
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) generateDefaultDescriptionID([Property](Property.html) property)
Generates default property description id from property id
Parameters:
`property` - the given property.
Returns:
description id.
isEditable
public boolean isEditable()
Gets mEnabled flag's value.
Returns:
true if editing of the property is enabled, otherwise - false.
setEditable
public void setEditable(boolean editable)
Set mEnabled flag's value.
Parameters:
`editable` - new value.
getUndefinedString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUndefinedString()
Returns representation string for "undefined" property state
Returns:
"undefined" representation string
getUndefinedString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUndefinedString([Property](Property.html) property)
Returns representation string for "undefined" property state. Property can define its own "undefined"
 representation string by setting additional property `QPropertiesHelper.UNDEFINED_STRING`.
Parameters:
`property` - property for which undefined string is get.
Returns:
"undefined" representation string
getSources
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> getSources()
Return a collection of property sources. In most cases property represents a value of some object.
 In these case that object can be added as Property source if traceability is required from property to source object.
Returns:
sources
See Also:
[`setSources(java.util.Collection)`](#setSources(java.util.Collection))
[`getSourcesAsStream()`](#getSourcesAsStream())
[`getSourceAsElement()`](#getSourceAsElement())
[`getFirstElementFromSources()`](#getFirstElementFromSources())
getSourcesAsStream
public [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getSourcesAsStream()
Return a stream of property sources. In most cases property represents a value of some object.
 In these case that object can be added as Property source if traceability is required from property to source object.
Returns:
sources
See Also:
[`getSources()`](#getSources())
[`setSources(java.util.Collection)`](#setSources(java.util.Collection))
[`getSourceAsElement()`](#getSourceAsElement())
[`getFirstElementFromSources()`](#getFirstElementFromSources())
setSources
public void setSources([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> sources)
Set property's sources.
Parameters:
`sources` - sources
See Also:
[`getSources()`](#getSources())
addSources
public void addSources([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> sources)
Append given sources to already existing ones.
Parameters:
`sources` - sources to append
See Also:
[`getSources()`](#getSources())
addSource
public void addSource(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) source)
Add source object to a project.
Parameters:
`source` - source object
See Also:
[`getSources()`](#getSources())
getAdditionalProperty
@CheckForNullpublic <T> T getAdditionalProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tag)
Return attached "tag" like string value
Parameters:
`tag` - tag key
Returns:
value of given key or null
setAdditionalProperty
public void setAdditionalProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Attach tag like key-value information to a property
Parameters:
`key` - tag key
`value` - tag value
getAdditionalProperties
@CheckForNullpublic [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getAdditionalProperties()
Return a map structure of attached tags to this property.
Returns:
tags
See Also:
[`setAdditionalProperty(String, Object)`](#setAdditionalProperty(java.lang.String,java.lang.Object))
setAdditionalProperties
public void setAdditionalProperties(@CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> tags)
Replace current tags with a new ones
Parameters:
`tags` - new tags
_isFrozen
public boolean _isFrozen()
Returns:
true if property is frozen
_setFrozen
public void _setFrozen(boolean frozen)
This is an internal api method to mark property as frozen. Value of frozen property can not be changed - runtime exception will be thrown
Parameters:
`frozen` - frozen property state
getNonEditableReason
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getNonEditableReason()
Returns the property reason
Returns:
property reason, if reason is null returns empty string
setNonEditableReason
public void setNonEditableReason([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) reason)
Sets the property reason
Parameters:
`reason` - reason why property is not editable
getProjectFromSourcesOrActive
public [Project](../core/Project.html) getProjectFromSourcesOrActive()
Looks for a project of property's sources
Returns:
source's project or active project
getFirstElementFromSources
@CheckForNullpublic [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getFirstElementFromSources()
Looks for a first Element among sources.
Returns:
element
getSourceAsElement
@CheckForNullpublic [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getSourceAsElement()
Returns source as Element if property has just one source and that source is an Element
Returns:
element
areEqualByValue
public boolean areEqualByValue([Property](Property.html) other)
getIntroductoryVersion
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getIntroductoryVersion()
Get application version the property was introduced in.
Returns:
application version.
setIntroductoryVersion
public void setIntroductoryVersion(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) introductoryVersion)
Set application version property is introduced in.
Parameters:
`introductoryVersion` - current application version or `null`
checkFrozen
protected void checkFrozen()
checkFrozen
protected void checkFrozen(@CheckForNull
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> detailsSupplier)
_setValue
protected final void _setValue(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
_getValue
@CheckForNullprotected final [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) _getValue()
getAnnotations
@CheckForNullpublic [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getAnnotations()
addAnnotation
public void addAnnotation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
removeAnnotation
public void removeAnnotation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) key)
getAnnotation
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAnnotation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
setAnnotations
public void setAnnotations(@CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> annotations)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class Property">Class Property</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.properties.Property</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="AbstractChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">AbstractChoiceProperty</a></code>, <code><a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a></code>, <code><a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a></code>, <code><a href="ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a></code>, <code><a href="FileProperty.html" title="class in com.nomagic.magicdraw.properties">FileProperty</a></code>, <code><a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a></code>, <code><a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a></code>, <code><a href="NumberProperty.html" title="class in com.nomagic.magicdraw.properties">NumberProperty</a></code>, <code><a href="PageFormatProperty.html" title="class in com.nomagic.magicdraw.properties">PageFormatProperty</a></code>, <code><a href="StringProperty.html" title="class in com.nomagic.magicdraw.properties">StringProperty</a></code>, <code><a href="TypeProperty.html" title="class in com.nomagic.magicdraw.properties">TypeProperty</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Property</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a>, <a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></span></div>
<div class="block">This class represents some property with some value.
 This is based class, specific type properties must be derived from this class.</div>
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
<div class="col-first even-row-color"><code>protected static final <a href="PropertyResourceProvider.html" title="interface in com.nomagic.magicdraw.properties">PropertyResourceProvider</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_PROPERTY_RESOURCE_PROVIDER">DEFAULT_PROPERTY_RESOURCE_PROVIDER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default property resource provider.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EDITABLE">EDITABLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">"Editable" property name</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NULL">NULL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Representation of null value as string.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="PropertyResourceProvider.html" title="interface in com.nomagic.magicdraw.properties">PropertyResourceProvider</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NULL_ID_PROPERTY_RESOURCE_PROVIDER">NULL_ID_PROPERTY_RESOURCE_PROVIDER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A resource provider which does not try to translate property ID.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TO">TO</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UNDEFINED">UNDEFINED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Property "undefined" state literal.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUE">VALUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">"Value" property name</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VALUE_ANNOTATIONS">VALUE_ANNOTATIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">"valueAnnotations" property name</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Property</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs new property.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Object)">Property</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color">
<div class="block">The property constructor.</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#_getValue()">_getValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#_isFrozen()">_isFrozen</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#_setFrozen(boolean)">_setFrozen</a><wbr/>(boolean frozen)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This is an internal api method to mark property as frozen.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#_setValue(java.lang.Object)">_setValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a><wbr/>(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> v)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts the given visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAnnotation(java.lang.String,java.lang.String)">addAnnotation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Delegates <code>addPropertyChangeListener</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which adds a <code>PropertyChangeListener</code> to the listener list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSource(java.lang.Object)">addSource</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> source)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add source object to a project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSources(java.util.Collection)">addSources</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; sources)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Append given sources to already existing ones.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#areEqualByValue(com.nomagic.magicdraw.properties.Property)">areEqualByValue</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> other)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#areValuesEqual(java.lang.Object,java.lang.Object)">areValuesEqual</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if values are equal before setting new value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkFrozen()">checkFrozen</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkFrozen(java.util.function.Supplier)">checkFrozen</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; detailsSupplier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/CellEditor.html" title="class or interface in javax.swing">CellEditor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCellEditor(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory)">createCellEditor</a><wbr/>(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory factory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the cell editor which edits this property in swing table.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html" title="class or interface in javax.swing.table">TableCellRenderer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTableCellRenderer(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory)">createTableCellRenderer</a><wbr/>(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory factory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the cell renderer which renders this property in swing table.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Properties are equal if their id are equals.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)">generateDefaultDescriptionID</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Generates default property description id from property id</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAdditionalProperties()">getAdditionalProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a map structure of attached tags to this property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T&gt; T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAdditionalProperty(java.lang.String)">getAdditionalProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return attached "tag" like string value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotation(java.lang.String)">getAnnotation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotations()">getAnnotations</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property class type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property description from resource provider by property description id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescriptionID()">getDescriptionID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property description ID.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstElementFromSources()">getFirstElementFromSources</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Looks for a first Element among sources.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroup()">getGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns group name for property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIntroductoryVersion()">getIntroductoryVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get application version the property was introduced in.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns name of the property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNonEditableReason()">getNonEditableReason</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the property reason</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectFromSourcesOrActive()">getProjectFromSourcesOrActive</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Looks for a project of property's sources</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPureDescription()">getPureDescription</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns pure description - does not goes into resource provider.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyResourceProvider.html" title="interface in com.nomagic.magicdraw.properties">PropertyResourceProvider</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourceProvider()">getResourceProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns <code>PropertyResourceProvider</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourceProviderID()">getResourceProviderID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Resource provider ID.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSortableValueStringRepresentation()">getSortableValueStringRepresentation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceAsElement()">getSourceAsElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns source as Element if property has just one source and that source is an Element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSources()">getSources</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a collection of property sources.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourcesAsStream()">getSourcesAsStream</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a stream of property sources.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getUndefinedString()">getUndefinedString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns representation string for "undefined" property state</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getUndefinedString(com.nomagic.magicdraw.properties.Property)">getUndefinedString</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns representation string for "undefined" property state.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue()">getValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns properties value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueStringRepresentation()">getValueStringRepresentation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns value's string representation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The hash code will be the same as ID's hash code.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEditable()">isEditable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets mEnabled flag's value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUndefinedState()">isUndefinedState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns value undefined state flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isValueCompatible(java.lang.Object)">isValueCompatible</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAnnotation(java.lang.String)">removeAnnotation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Delegates <code>removePropertyChangeListener</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which removes a PropertyChangeListener from the listener list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAdditionalProperties(java.util.Map)">setAdditionalProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; tags)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Replace current tags with a new ones</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAdditionalProperty(java.lang.String,java.lang.Object)">setAdditionalProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Attach tag like key-value information to a property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAnnotations(java.util.Map)">setAnnotations</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; annotations)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDescription(java.lang.String)">setDescription</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set property description</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDescriptionID(java.lang.String)">setDescriptionID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> descriptionID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set property description ID.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEditable(boolean)">setEditable</a><wbr/>(boolean editable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set mEnabled flag's value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setGroup(java.lang.String)">setGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new group name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setID(java.lang.String)">setID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets property id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIntroductoryVersion(java.lang.String)">setIntroductoryVersion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> introductoryVersion)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set application version property is introduced in.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNonEditableReason(java.lang.String)">setNonEditableReason</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reason)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the property reason</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)">setResourceProvider</a><wbr/>(<a href="PropertyResourceProvider.html" title="interface in com.nomagic.magicdraw.properties">PropertyResourceProvider</a> provider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets PropertyResourceProvider for this property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setResourceProviderID(java.lang.String)">setResourceProviderID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceProviderID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set resource provider ID.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSources(java.util.Collection)">setSources</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; sources)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set property's sources.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUndefinedState(boolean)">setUndefinedState</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets undefined state for this property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(java.lang.Object)">setValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return string representation of property for debug purposes.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="TO">
<h3>TO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TO</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.Property.TO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALUE">
<h3>VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALUE</span></div>
<div class="block">"Value" property name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.Property.VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALUE_ANNOTATIONS">
<h3>VALUE_ANNOTATIONS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALUE_ANNOTATIONS</span></div>
<div class="block">"valueAnnotations" property name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.Property.VALUE_ANNOTATIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EDITABLE">
<h3>EDITABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EDITABLE</span></div>
<div class="block">"Editable" property name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.Property.EDITABLE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UNDEFINED">
<h3>UNDEFINED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UNDEFINED</span></div>
<div class="block">Property "undefined" state literal. The <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html#getPropertyName()" title="class or interface in java.beans"><code>PropertyChangeEvent.getPropertyName()</code></a> return
 this string when state of the property changes it's "undefined" state.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#setUndefinedState(boolean)"><code>setUndefinedState(boolean)</code></a></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.Property.UNDEFINED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NULL">
<h3>NULL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NULL</span></div>
<div class="block">Representation of null value as string.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.Property.NULL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_PROPERTY_RESOURCE_PROVIDER">
<h3>DEFAULT_PROPERTY_RESOURCE_PROVIDER</h3>
<div class="member-signature"><span class="modifiers">protected static final</span> <span class="return-type"><a href="PropertyResourceProvider.html" title="interface in com.nomagic.magicdraw.properties">PropertyResourceProvider</a></span> <span class="element-name">DEFAULT_PROPERTY_RESOURCE_PROVIDER</span></div>
<div class="block">Default property resource provider.</div>
</section>
</li>
<li>
<section class="detail" id="NULL_ID_PROPERTY_RESOURCE_PROVIDER">
<h3>NULL_ID_PROPERTY_RESOURCE_PROVIDER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="PropertyResourceProvider.html" title="interface in com.nomagic.magicdraw.properties">PropertyResourceProvider</a></span> <span class="element-name">NULL_ID_PROPERTY_RESOURCE_PROVIDER</span></div>
<div class="block">A resource provider which does not try to translate property ID.</div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>Property</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Property</span>()</div>
<div class="block">Constructs new property.
 Property ID will be empty string, property value - null.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Object)">
<h3>Property</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Property</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">The property constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the ID of property.</dd>
<dd><code>value</code> - the value of the property.</dd>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Returns name of the property. Property name is taken from
 <code>PropertyResourceProvider</code> with key - Property ID.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block">Returns property id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property ID.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setID(java.lang.String)">
<h3>setID</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Sets property id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - a new property id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets new property value.
 Will fire a <code>PropertyChangeEvent</code> with propertyName - property
 ID, newValue and oldValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - a new property value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isValueCompatible(java.lang.Object)">
<h3>isValueCompatible</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isValueCompatible</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if given object can be assigned as value to this property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="areValuesEqual(java.lang.Object,java.lang.Object)">
<h3>areValuesEqual</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">areValuesEqual</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block">Check if values are equal before setting new value. If values are equal value is not changed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>oldValue</code> - current value.</dd>
<dd><code>newValue</code> - new value.</dd>
<dt>Returns:</dt>
<dd>true if values are equal.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<div class="block">Properties are equal if their id are equals.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Parameters:</dt>
<dd><code>o</code> - some other Property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<div class="block">The hash code will be the same as ID's hash code.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>property hash code.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue()">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span>()</div>
<div class="block">Returns properties value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueStringRepresentation()">
<h3>getValueStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValueStringRepresentation</span>()</div>
<div class="block">Returns value's string representation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>string "null" if property does not have value; <code>value.
 toString()</code> if property has value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSortableValueStringRepresentation()">
<h3>getSortableValueStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSortableValueStringRepresentation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.properties.PropertyVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> v)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Accepts the given visitor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Parameters:</dt>
<dd><code>v</code> - the PropertyVisitor.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCellEditor(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory)">
<h3>createCellEditor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@NotApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/CellEditor.html" title="class or interface in javax.swing">CellEditor</a></span> <span class="element-name">createCellEditor</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory factory)</span></div>
<div class="block">Returns the cell editor which edits this property in swing table.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factory</code> - factory</dd>
<dt>Returns:</dt>
<dd>null here.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTableCellRenderer(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory)">
<h3>createTableCellRenderer</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@NotApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html" title="class or interface in javax.swing.table">TableCellRenderer</a></span> <span class="element-name">createTableCellRenderer</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory factory)</span></div>
<div class="block">Returns the cell renderer which renders this property in swing table.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factory</code> - factory</dd>
<dt>Returns:</dt>
<dd>null here.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span> <span class="element-name">clone</span>()</div>
<div class="block">Clones the property. Clone is not deep, the clone will have the same instance of value.
 The clone will not have registered PropertyChangeListeners.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>the cloned property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUndefinedState(boolean)">
<h3>setUndefinedState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUndefinedState</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets undefined state for this property. Notifies property
 change listeners if property undefined state changes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of undefined state flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUndefinedState()">
<h3>isUndefinedState</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUndefinedState</span>()</div>
<div class="block">Returns value undefined state flag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value value of undefined state flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassType()">
<h3>getClassType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClassType</span>()</div>
<div class="block">Returns property class type.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#getClassType()">getClassType</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Returns:</dt>
<dd>PropertyID.PROPERTY</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="PropertyID.html#PROPERTY"><code>PropertyID.PROPERTY</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addPropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Delegates <code>addPropertyChangeListener</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which adds a <code>PropertyChangeListener</code> to the listener list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the <code>PropertyChangeListener</code> to be added</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new are equal and non-null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyName</code> - the programmatic name of the property that was changed.</dd>
<dd><code>oldValue</code> - the old value of the property</dd>
<dd><code>newValue</code> - the new value of the property</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removePropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Delegates <code>removePropertyChangeListener</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which removes a PropertyChangeListener from the listener list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the PropertyChangeListener to be removed</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Return string representation of property for debug purposes.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>string representation of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourceProviderID()">
<h3>getResourceProviderID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getResourceProviderID</span>()</div>
<div class="block">Returns Resource provider ID.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>id of resource provider.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setResourceProviderID(java.lang.String)">
<h3>setResourceProviderID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setResourceProviderID</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceProviderID)</span></div>
<div class="block">Set resource provider ID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resourceProviderID</code> - resource provider id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)">
<h3>setResourceProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setResourceProvider</span><wbr/><span class="parameters">(@CheckForNull
 <a href="PropertyResourceProvider.html" title="interface in com.nomagic.magicdraw.properties">PropertyResourceProvider</a> provider)</span></div>
<div class="block">Sets PropertyResourceProvider for this property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - the given provider.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourceProvider()">
<h3>getResourceProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyResourceProvider.html" title="interface in com.nomagic.magicdraw.properties">PropertyResourceProvider</a></span> <span class="element-name">getResourceProvider</span>()</div>
<div class="block">Returns <code>PropertyResourceProvider</code>. If property does not have
 resource provider returns shared instance of
 <code>DefaultPropertyResourceProvider</code>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>set <code>PropertyResourceProvider</code> or default one.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGroup()">
<h3>getGroup</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getGroup</span>()</div>
<div class="block">Returns group name for property. Properties with same group can be grouped in GUI.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Returns  group name for property. Can be null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGroup(java.lang.String)">
<h3>setGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGroup</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
<div class="block">Sets new group name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>group</code> - group name, can be null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescriptionID()">
<h3>getDescriptionID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescriptionID</span>()</div>
<div class="block">Returns property description ID.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>description id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDescriptionID(java.lang.String)">
<h3>setDescriptionID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDescriptionID</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> descriptionID)</span></div>
<div class="block">Set property description ID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptionID</code> - description id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDescription(java.lang.String)">
<h3>setDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDescription</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</span></div>
<div class="block">Set property description</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>description</code> - description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span>()</div>
<div class="block">Returns property description from resource provider by property description id. May be null.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>description of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPureDescription()">
<h3>getPureDescription</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPureDescription</span>()</div>
<div class="block">Returns pure description - does not goes into resource provider.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)">
<h3>generateDefaultDescriptionID</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">generateDefaultDescriptionID</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</span></div>
<div class="block">Generates default property description id from property id</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - the given property.</dd>
<dt>Returns:</dt>
<dd>description id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditable()">
<h3>isEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEditable</span>()</div>
<div class="block">Gets mEnabled flag's value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if editing of the property is enabled, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEditable(boolean)">
<h3>setEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEditable</span><wbr/><span class="parameters">(boolean editable)</span></div>
<div class="block">Set mEnabled flag's value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>editable</code> - new value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUndefinedString()">
<h3>getUndefinedString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUndefinedString</span>()</div>
<div class="block">Returns representation string for "undefined" property state</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>"undefined" representation string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUndefinedString(com.nomagic.magicdraw.properties.Property)">
<h3>getUndefinedString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUndefinedString</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</span></div>
<div class="block">Returns representation string for "undefined" property state. Property can define its own "undefined"
 representation string by setting additional property <code>QPropertiesHelper.UNDEFINED_STRING</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - property for which undefined string is get.</dd>
<dt>Returns:</dt>
<dd>"undefined" representation string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSources()">
<h3>getSources</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">getSources</span>()</div>
<div class="block">Return a collection of property sources. In most cases property represents a value of some object.
 In these case that object can be added as Property source if traceability is required from property to source object.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>sources</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setSources(java.util.Collection)"><code>setSources(java.util.Collection)</code></a></li>
<li><a href="#getSourcesAsStream()"><code>getSourcesAsStream()</code></a></li>
<li><a href="#getSourceAsElement()"><code>getSourceAsElement()</code></a></li>
<li><a href="#getFirstElementFromSources()"><code>getFirstElementFromSources()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourcesAsStream()">
<h3>getSourcesAsStream</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getSourcesAsStream</span>()</div>
<div class="block">Return a stream of property sources. In most cases property represents a value of some object.
 In these case that object can be added as Property source if traceability is required from property to source object.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>sources</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getSources()"><code>getSources()</code></a></li>
<li><a href="#setSources(java.util.Collection)"><code>setSources(java.util.Collection)</code></a></li>
<li><a href="#getSourceAsElement()"><code>getSourceAsElement()</code></a></li>
<li><a href="#getFirstElementFromSources()"><code>getFirstElementFromSources()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSources(java.util.Collection)">
<h3>setSources</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSources</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; sources)</span></div>
<div class="block">Set property's sources.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sources</code> - sources</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getSources()"><code>getSources()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSources(java.util.Collection)">
<h3>addSources</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSources</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; sources)</span></div>
<div class="block">Append given sources to already existing ones.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sources</code> - sources to append</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getSources()"><code>getSources()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSource(java.lang.Object)">
<h3>addSource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSource</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> source)</span></div>
<div class="block">Add source object to a project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - source object</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getSources()"><code>getSources()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAdditionalProperty(java.lang.String)">
<h3>getAdditionalProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">T</span> <span class="element-name">getAdditionalProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag)</span></div>
<div class="block">Return attached "tag" like string value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - tag key</dd>
<dt>Returns:</dt>
<dd>value of given key or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAdditionalProperty(java.lang.String,java.lang.Object)">
<h3>setAdditionalProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAdditionalProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Attach tag like key-value information to a property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - tag key</dd>
<dd><code>value</code> - tag value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAdditionalProperties()">
<h3>getAdditionalProperties</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getAdditionalProperties</span>()</div>
<div class="block">Return a map structure of attached tags to this property.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tags</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setAdditionalProperty(java.lang.String,java.lang.Object)"><code>setAdditionalProperty(String, Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAdditionalProperties(java.util.Map)">
<h3>setAdditionalProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAdditionalProperties</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; tags)</span></div>
<div class="block">Replace current tags with a new ones</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tags</code> - new tags</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="_isFrozen()">
<h3>_isFrozen</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">_isFrozen</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if property is frozen</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="_setFrozen(boolean)">
<h3>_setFrozen</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">_setFrozen</span><wbr/><span class="parameters">(boolean frozen)</span></div>
<div class="block">This is an internal api method to mark property as frozen. Value of frozen property can not be changed - runtime exception will be thrown</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>frozen</code> - frozen property state</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNonEditableReason()">
<h3>getNonEditableReason</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNonEditableReason</span>()</div>
<div class="block">Returns the property reason</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property reason, if reason is null returns empty string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNonEditableReason(java.lang.String)">
<h3>setNonEditableReason</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNonEditableReason</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reason)</span></div>
<div class="block">Sets the property reason</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reason</code> - reason why property is not editable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectFromSourcesOrActive()">
<h3>getProjectFromSourcesOrActive</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProjectFromSourcesOrActive</span>()</div>
<div class="block">Looks for a project of property's sources</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>source's project or active project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstElementFromSources()">
<h3>getFirstElementFromSources</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getFirstElementFromSources</span>()</div>
<div class="block">Looks for a first Element among sources.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceAsElement()">
<h3>getSourceAsElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getSourceAsElement</span>()</div>
<div class="block">Returns source as Element if property has just one source and that source is an Element</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="areEqualByValue(com.nomagic.magicdraw.properties.Property)">
<h3>areEqualByValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">areEqualByValue</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> other)</span></div>
</section>
</li>
<li>
<section class="detail" id="getIntroductoryVersion()">
<h3>getIntroductoryVersion</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getIntroductoryVersion</span>()</div>
<div class="block">Get application version the property was introduced in.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>application version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIntroductoryVersion(java.lang.String)">
<h3>setIntroductoryVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIntroductoryVersion</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> introductoryVersion)</span></div>
<div class="block">Set application version property is introduced in.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>introductoryVersion</code> - current application version or <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkFrozen()">
<h3>checkFrozen</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">checkFrozen</span>()</div>
</section>
</li>
<li>
<section class="detail" id="checkFrozen(java.util.function.Supplier)">
<h3>checkFrozen</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">checkFrozen</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; detailsSupplier)</span></div>
</section>
</li>
<li>
<section class="detail" id="_setValue(java.lang.Object)">
<h3>_setValue</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">_setValue</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="_getValue()">
<h3>_getValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">_getValue</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAnnotations()">
<h3>getAnnotations</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAnnotations</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addAnnotation(java.lang.String,java.lang.String)">
<h3>addAnnotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAnnotation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeAnnotation(java.lang.String)">
<h3>removeAnnotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAnnotation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
</section>
</li>
<li>
<section class="detail" id="getAnnotation(java.lang.String)">
<h3>getAnnotation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAnnotation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAnnotations(java.util.Map)">
<h3>setAnnotations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAnnotations</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; annotations)</span></div>
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
