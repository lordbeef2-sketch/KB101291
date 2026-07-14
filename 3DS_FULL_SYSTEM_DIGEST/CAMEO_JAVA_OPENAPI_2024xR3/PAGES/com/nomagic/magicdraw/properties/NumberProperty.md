# JAVA OPENAPI: NumberProperty (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/properties/NumberProperty.html
- source_path: `com/nomagic/magicdraw/properties/NumberProperty.html`
- source_sha256: `6a2249ce689502c286ca295de6eaa45430102b3e8c669c3e1fefc403bb774745`
- captured_utc: `2026-07-14T16:55:28.762163+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class NumberProperty

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.properties.Property](Property.html)
com.nomagic.magicdraw.properties.NumberProperty

All Implemented Interfaces:
`[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classNumberProperty
extends [Property](Property.html)

The property for storing and editing some number value in Double, Float or Int formats.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[DOUBLE](#DOUBLE)`
Number type is double.
`static final int`
`[FLOAT](#FLOAT)`
Number type is float.
`static final int`
`[INT](#INT)`
Number type is integer.
`static final int`
`[LONG](#LONG)`
Number type is long.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PATTERN](#PATTERN)`
Patters which is used to format the number.
Fields inherited from class com.nomagic.magicdraw.properties.[Property](Property.html)
`[DEFAULT_PROPERTY_RESOURCE_PROVIDER](Property.html#DEFAULT_PROPERTY_RESOURCE_PROVIDER), [EDITABLE](Property.html#EDITABLE), [NULL](Property.html#NULL), [NULL_ID_PROPERTY_RESOURCE_PROVIDER](Property.html#NULL_ID_PROPERTY_RESOURCE_PROVIDER), [TO](Property.html#TO), [UNDEFINED](Property.html#UNDEFINED), [VALUE](Property.html#VALUE), [VALUE_ANNOTATIONS](Property.html#VALUE_ANNOTATIONS)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[NumberProperty](#%3Cinit%3E())()`
Default constructor for INT property.
`[NumberProperty](#%3Cinit%3E(java.lang.String,double,double,double))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 double value,
 double low,
 double high)`
The property constructor.
`[NumberProperty](#%3Cinit%3E(java.lang.String,float,double,double))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 float value,
 double low,
 double high)`
The property constructor.
`[NumberProperty](#%3Cinit%3E(java.lang.String,int,double,double))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 int value,
 double low,
 double high)`
The property constructor.
`[NumberProperty](#%3Cinit%3E(java.lang.String,long,double,double))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 long value,
 double low,
 double high)`
The property constructor.
`[NumberProperty](#%3Cinit%3E(java.lang.String,java.lang.Double,int,double,double))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) value,
 int type,
 double low,
 double high)`
The property constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.properties.PropertyVisitor))([PropertyVisitor](PropertyVisitor.html) v)`
Accepts the given visitor.
`[NumberProperty](NumberProperty.html)`
`[clone](#clone())()`
Clones the property.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getClassType](#getClassType())()`
Returns property class type.
`double`
`[getDouble](#getDouble())()`
Returns value as double (primitive type).
`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`
`[getDoubleObject](#getDoubleObject())()`
Returns value as Double object.
`float`
`[getFloat](#getFloat())()`
Returns value as float (primitive type).
`double`
`[getHighRange](#getHighRange())()`
Returns the highest range of the value.
`int`
`[getInteger](#getInteger())()`
Returns value as int (primitive type).
`long`
`[getLong](#getLong())()`
Returns value as long (primitive type).
`double`
`[getLowRange](#getLowRange())()`
Returns the lowest range of the number value.
`int`
`[getNumberType](#getNumberType())()`
Returns type of the number.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPattern](#getPattern(com.nomagic.magicdraw.properties.Property))([Property](Property.html) property)`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStringRepresentation](#getStringRepresentation(int,java.lang.Double))(int type,
 [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) value)`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStringRepresentation](#getStringRepresentation(int,java.lang.Double,java.lang.String))(int type,
 [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) value,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pattern)`

`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue())()`
Returns properties value.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getValueStringRepresentation](#getValueStringRepresentation())()`
Returns value's string representation.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[hasError](#hasError(com.nomagic.magicdraw.properties.NumberProperty,java.lang.String))([NumberProperty](NumberProperty.html) property,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newNumber)`

`boolean`
`[isSoftRange](#isSoftRange())()`

`protected boolean`
`[isValueCompatible](#isValueCompatible(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`

`void`
`[setHighRange](#setHighRange(double))(double range)`
Returns the highest range of the value.
`void`
`[setLowRange](#setLowRange(double))(double range)`
Returns the lowest range of the value.
`void`
`[setNumberType](#setNumberType(int))(int type)`
Sets type of the number.
`void`
`[setSoftRange](#setSoftRange(boolean))(boolean softRange)`

`void`
`[setValue](#setValue(double))(double value)`
Sets value as primitive double type.
`void`
`[setValue](#setValue(float))(float value)`
Sets value as primitive float type.
`void`
`[setValue](#setValue(int))(int value)`
Sets value as primitive integer.
`void`
`[setValue](#setValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets new property value.
`static [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`
`[toDouble](#toDouble(java.lang.Number))([Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) number)`
Methods inherited from class com.nomagic.magicdraw.properties.[Property](Property.html)
`[_getValue](Property.html#_getValue()), [_isFrozen](Property.html#_isFrozen()), [_setFrozen](Property.html#_setFrozen(boolean)), [_setValue](Property.html#_setValue(java.lang.Object)), [addAnnotation](Property.html#addAnnotation(java.lang.String,java.lang.String)), [addPropertyChangeListener](Property.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addSource](Property.html#addSource(java.lang.Object)), [addSources](Property.html#addSources(java.util.Collection)), [areEqualByValue](Property.html#areEqualByValue(com.nomagic.magicdraw.properties.Property)), [areValuesEqual](Property.html#areValuesEqual(java.lang.Object,java.lang.Object)), [checkFrozen](Property.html#checkFrozen()), [checkFrozen](Property.html#checkFrozen(java.util.function.Supplier)), [createCellEditor](Property.html#createCellEditor(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory)), [createTableCellRenderer](Property.html#createTableCellRenderer(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory)), [equals](Property.html#equals(java.lang.Object)), [firePropertyChange](Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateDefaultDescriptionID](Property.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)), [getAdditionalProperties](Property.html#getAdditionalProperties()), [getAdditionalProperty](Property.html#getAdditionalProperty(java.lang.String)), [getAnnotation](Property.html#getAnnotation(java.lang.String)), [getAnnotations](Property.html#getAnnotations()), [getDescription](Property.html#getDescription()), [getDescriptionID](Property.html#getDescriptionID()), [getFirstElementFromSources](Property.html#getFirstElementFromSources()), [getGroup](Property.html#getGroup()), [getID](Property.html#getID()), [getIntroductoryVersion](Property.html#getIntroductoryVersion()), [getName](Property.html#getName()), [getNonEditableReason](Property.html#getNonEditableReason()), [getProjectFromSourcesOrActive](Property.html#getProjectFromSourcesOrActive()), [getPureDescription](Property.html#getPureDescription()), [getResourceProvider](Property.html#getResourceProvider()), [getResourceProviderID](Property.html#getResourceProviderID()), [getSortableValueStringRepresentation](Property.html#getSortableValueStringRepresentation()), [getSourceAsElement](Property.html#getSourceAsElement()), [getSources](Property.html#getSources()), [getSourcesAsStream](Property.html#getSourcesAsStream()), [getUndefinedString](Property.html#getUndefinedString()), [getUndefinedString](Property.html#getUndefinedString(com.nomagic.magicdraw.properties.Property)), [hashCode](Property.html#hashCode()), [isEditable](Property.html#isEditable()), [isUndefinedState](Property.html#isUndefinedState()), [removeAnnotation](Property.html#removeAnnotation(java.lang.String)), [removePropertyChangeListener](Property.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setAdditionalProperties](Property.html#setAdditionalProperties(java.util.Map)), [setAdditionalProperty](Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)), [setAnnotations](Property.html#setAnnotations(java.util.Map)), [setDescription](Property.html#setDescription(java.lang.String)), [setDescriptionID](Property.html#setDescriptionID(java.lang.String)), [setEditable](Property.html#setEditable(boolean)), [setGroup](Property.html#setGroup(java.lang.String)), [setID](Property.html#setID(java.lang.String)), [setIntroductoryVersion](Property.html#setIntroductoryVersion(java.lang.String)), [setNonEditableReason](Property.html#setNonEditableReason(java.lang.String)), [setResourceProvider](Property.html#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)), [setResourceProviderID](Property.html#setResourceProviderID(java.lang.String)), [setSources](Property.html#setSources(java.util.Collection)), [setUndefinedState](Property.html#setUndefinedState(boolean)), [toString](Property.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
PATTERN
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PATTERN
Patters which is used to format the number. This pattern should be set to the additional properties of NumberProperty
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.NumberProperty.PATTERN)
INT
public static final int INT
Number type is integer.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.NumberProperty.INT)
DOUBLE
public static final int DOUBLE
Number type is double.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.NumberProperty.DOUBLE)
FLOAT
public static final int FLOAT
Number type is float.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.NumberProperty.FLOAT)
LONG
public static final int LONG
Number type is long.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.NumberProperty.LONG)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
NumberProperty
public NumberProperty()
Default constructor for INT property. Value of the property will be 0. ID will be empty string.
NumberProperty
public NumberProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) value,
 int type,
 double low,
 double high)
The property constructor.
Parameters:
`id` - the ID of property.
`value` - the number value of the property.
`type` - the number type (INT, DOUBLE or FLOAT).
`low` - lowest range of the number.
`high` - highest range of the number.
NumberProperty
public NumberProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 int value,
 double low,
 double high)
The property constructor. Type of number will be INT.
Parameters:
`id` - the ID of property.
`value` - the value of the property.
`low` - lowest range of the number.
`high` - highest range of the number.
NumberProperty
public NumberProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 float value,
 double low,
 double high)
The property constructor. Type of number will be [`FLOAT`](#FLOAT).
Parameters:
`id` - the ID of property.
`value` - the value of the property.
`low` - lowest range of the number.
`high` - highest range of the number.
NumberProperty
public NumberProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 double value,
 double low,
 double high)
The property constructor. Type of number will be DOUBLE.
Parameters:
`id` - the ID of property.
`value` - the value of the property.
`low` - lowest range of the number.
`high` - highest range of the number.
NumberProperty
public NumberProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 long value,
 double low,
 double high)
The property constructor. Type of number will be LONG.
Parameters:
`id` - the ID of property.
`value` - the value of the property.
`low` - lowest range of the number.
`high` - highest range of the number.
 ============ METHOD DETAIL ========== 
Method Details
getValueStringRepresentation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getValueStringRepresentation()
Returns value's string representation.
Overrides:
`[getValueStringRepresentation](Property.html#getValueStringRepresentation())` in class `[Property](Property.html)`
Returns:
the string representation of the number.
getPattern
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPattern([Property](Property.html) property)
getStringRepresentation
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStringRepresentation(int type,
 @CheckForNull
 [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) value,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pattern)
getStringRepresentation
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStringRepresentation(int type,
 @CheckForNull
 [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) value)
toDouble
@CheckForNullpublic static [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) toDouble([Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) number)
accept
public void accept([PropertyVisitor](PropertyVisitor.html) v)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from class: `[Property](Property.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))`
Accepts the given visitor.
Specified by:
`[accept](PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Overrides:
`[accept](Property.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in class `[Property](Property.html)`
Parameters:
`v` - the PropertyVisitor.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
getInteger
public int getInteger()
Returns value as int (primitive type).
Returns:
property value as int. 0 if value is null
getLong
public long getLong()
Returns value as long (primitive type).
Returns:
property value as long. 0 if value is null
getDouble
public double getDouble()
Returns value as double (primitive type).
Returns:
property value as double. 0 if value is null
getFloat
public float getFloat()
Returns value as float (primitive type).
Returns:
property value as float. 0 if value is null
getDoubleObject
@CheckForNullpublic [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getDoubleObject()
Returns value as Double object.
Returns:
property value as Double.
setValue
public void setValue(int value)
Sets value as primitive integer.
Parameters:
`value` - a new integer value.
setValue
public void setValue(double value)
Sets value as primitive double type.
Parameters:
`value` - a new double value.
setValue
public void setValue(float value)
Sets value as primitive float type.
Parameters:
`value` - a new float value.
setValue
public void setValue(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Description copied from class: `[Property](Property.html#setValue(java.lang.Object))`
Sets new property value.
 Will fire a `PropertyChangeEvent` with propertyName - property
 ID, newValue and oldValue.
Overrides:
`[setValue](Property.html#setValue(java.lang.Object))` in class `[Property](Property.html)`
Parameters:
`value` - a new property value.
isValueCompatible
protected boolean isValueCompatible([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Overrides:
`[isValueCompatible](Property.html#isValueCompatible(java.lang.Object))` in class `[Property](Property.html)`
Returns:
true if given object can be assigned as value to this property
getValue
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getValue()
Description copied from class: `[Property](Property.html#getValue())`
Returns properties value.
Overrides:
`[getValue](Property.html#getValue())` in class `[Property](Property.html)`
Returns:
value of the property.
getClassType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getClassType()
Returns property class type.
Specified by:
`[getClassType](PropertyVisitorAcceptor.html#getClassType())` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Overrides:
`[getClassType](Property.html#getClassType())` in class `[Property](Property.html)`
Returns:
PropertyID.NUMBER_PROPERTY
See Also:
[`PropertyID.NUMBER_PROPERTY`](PropertyID.html#NUMBER_PROPERTY)
getNumberType
public int getNumberType()
Returns type of the number.
Returns:
number type - INT, DOUBLE or FLOAT.
setNumberType
public void setNumberType(int type)
Sets type of the number.
Parameters:
`type` - the number type - INT, DOUBLE or FLOAT.
getLowRange
public double getLowRange()
Returns the lowest range of the number value.
Returns:
lowest range.
getHighRange
public double getHighRange()
Returns the highest range of the value.
Returns:
highest range.
setLowRange
public void setLowRange(double range)
Returns the lowest range of the value.
Parameters:
`range` - the lowest range.
setHighRange
public void setHighRange(double range)
Returns the highest range of the value.
Parameters:
`range` - the highest range.
hasError
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) hasError([NumberProperty](NumberProperty.html) property,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) newNumber)
 throws [NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)
Throws:
`[NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)`
isSoftRange
public boolean isSoftRange()
Returns:
Property is not allowed to cross the range boundaries.
setSoftRange
public void setSoftRange(boolean softRange)
Parameters:
`softRange` - Property is allowed to cross the range boundaries. Default is false.
clone
public [NumberProperty](NumberProperty.html) clone()
Description copied from class: `[Property](Property.html#clone())`
Clones the property. Clone is not deep, the clone will have the same instance of value.
 The clone will not have registered PropertyChangeListeners.
Overrides:
`[clone](Property.html#clone())` in class `[Property](Property.html)`
Returns:
the cloned property.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class NumberProperty">Class NumberProperty</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="Property.html" title="class in com.nomagic.magicdraw.properties">com.nomagic.magicdraw.properties.Property</a>
<div class="inheritance">com.nomagic.magicdraw.properties.NumberProperty</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">NumberProperty</span>
<span class="extends-implements">extends <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span></div>
<div class="block">The property for storing and editing some number value in Double, Float or Int formats.</div>
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
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOUBLE">DOUBLE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number type is double.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FLOAT">FLOAT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number type is float.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INT">INT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number type is integer.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LONG">LONG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number type is long.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PATTERN">PATTERN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Patters which is used to format the number.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.properties.Property">Fields inherited from class com.nomagic.magicdraw.properties.<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></h3>
<code><a href="Property.html#DEFAULT_PROPERTY_RESOURCE_PROVIDER">DEFAULT_PROPERTY_RESOURCE_PROVIDER</a>, <a href="Property.html#EDITABLE">EDITABLE</a>, <a href="Property.html#NULL">NULL</a>, <a href="Property.html#NULL_ID_PROPERTY_RESOURCE_PROVIDER">NULL_ID_PROPERTY_RESOURCE_PROVIDER</a>, <a href="Property.html#TO">TO</a>, <a href="Property.html#UNDEFINED">UNDEFINED</a>, <a href="Property.html#VALUE">VALUE</a>, <a href="Property.html#VALUE_ANNOTATIONS">VALUE_ANNOTATIONS</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">NumberProperty</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Default constructor for INT property.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,double,double,double)">NumberProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 double value,
 double low,
 double high)</code></div>
<div class="col-last odd-row-color">
<div class="block">The property constructor.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,float,double,double)">NumberProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 float value,
 double low,
 double high)</code></div>
<div class="col-last even-row-color">
<div class="block">The property constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,int,double,double)">NumberProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 int value,
 double low,
 double high)</code></div>
<div class="col-last odd-row-color">
<div class="block">The property constructor.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,long,double,double)">NumberProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 long value,
 double low,
 double high)</code></div>
<div class="col-last even-row-color">
<div class="block">The property constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Double,int,double,double)">NumberProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value,
 int type,
 double low,
 double high)</code></div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a><wbr/>(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> v)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts the given visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NumberProperty.html" title="class in com.nomagic.magicdraw.properties">NumberProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property class type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDouble()">getDouble</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns value as double (primitive type).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDoubleObject()">getDoubleObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns value as Double object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>float</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFloat()">getFloat</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns value as float (primitive type).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHighRange()">getHighRange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the highest range of the value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInteger()">getInteger</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns value as int (primitive type).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLong()">getLong</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns value as long (primitive type).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLowRange()">getLowRange</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the lowest range of the number value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberType()">getNumberType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns type of the number.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPattern(com.nomagic.magicdraw.properties.Property)">getPattern</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringRepresentation(int,java.lang.Double)">getStringRepresentation</a><wbr/>(int type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringRepresentation(int,java.lang.Double,java.lang.String)">getStringRepresentation</a><wbr/>(int type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasError(com.nomagic.magicdraw.properties.NumberProperty,java.lang.String)">hasError</a><wbr/>(<a href="NumberProperty.html" title="class in com.nomagic.magicdraw.properties">NumberProperty</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newNumber)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSoftRange()">isSoftRange</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isValueCompatible(java.lang.Object)">isValueCompatible</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHighRange(double)">setHighRange</a><wbr/>(double range)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the highest range of the value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLowRange(double)">setLowRange</a><wbr/>(double range)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the lowest range of the value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNumberType(int)">setNumberType</a><wbr/>(int type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets type of the number.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSoftRange(boolean)">setSoftRange</a><wbr/>(boolean softRange)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(double)">setValue</a><wbr/>(double value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets value as primitive double type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(float)">setValue</a><wbr/>(float value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets value as primitive float type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(int)">setValue</a><wbr/>(int value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets value as primitive integer.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(java.lang.Object)">setValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toDouble(java.lang.Number)">toDouble</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> number)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.properties.Property">Methods inherited from class com.nomagic.magicdraw.properties.<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></h3>
<code><a href="Property.html#_getValue()">_getValue</a>, <a href="Property.html#_isFrozen()">_isFrozen</a>, <a href="Property.html#_setFrozen(boolean)">_setFrozen</a>, <a href="Property.html#_setValue(java.lang.Object)">_setValue</a>, <a href="Property.html#addAnnotation(java.lang.String,java.lang.String)">addAnnotation</a>, <a href="Property.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="Property.html#addSource(java.lang.Object)">addSource</a>, <a href="Property.html#addSources(java.util.Collection)">addSources</a>, <a href="Property.html#areEqualByValue(com.nomagic.magicdraw.properties.Property)">areEqualByValue</a>, <a href="Property.html#areValuesEqual(java.lang.Object,java.lang.Object)">areValuesEqual</a>, <a href="Property.html#checkFrozen()">checkFrozen</a>, <a href="Property.html#checkFrozen(java.util.function.Supplier)">checkFrozen</a>, <a href="Property.html#createCellEditor(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory)">createCellEditor</a>, <a href="Property.html#createTableCellRenderer(com.nomagic.magicdraw.properties.ui.jideui.RendererEditorFactory)">createTableCellRenderer</a>, <a href="Property.html#equals(java.lang.Object)">equals</a>, <a href="Property.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="Property.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Property)">generateDefaultDescriptionID</a>, <a href="Property.html#getAdditionalProperties()">getAdditionalProperties</a>, <a href="Property.html#getAdditionalProperty(java.lang.String)">getAdditionalProperty</a>, <a href="Property.html#getAnnotation(java.lang.String)">getAnnotation</a>, <a href="Property.html#getAnnotations()">getAnnotations</a>, <a href="Property.html#getDescription()">getDescription</a>, <a href="Property.html#getDescriptionID()">getDescriptionID</a>, <a href="Property.html#getFirstElementFromSources()">getFirstElementFromSources</a>, <a href="Property.html#getGroup()">getGroup</a>, <a href="Property.html#getID()">getID</a>, <a href="Property.html#getIntroductoryVersion()">getIntroductoryVersion</a>, <a href="Property.html#getName()">getName</a>, <a href="Property.html#getNonEditableReason()">getNonEditableReason</a>, <a href="Property.html#getProjectFromSourcesOrActive()">getProjectFromSourcesOrActive</a>, <a href="Property.html#getPureDescription()">getPureDescription</a>, <a href="Property.html#getResourceProvider()">getResourceProvider</a>, <a href="Property.html#getResourceProviderID()">getResourceProviderID</a>, <a href="Property.html#getSortableValueStringRepresentation()">getSortableValueStringRepresentation</a>, <a href="Property.html#getSourceAsElement()">getSourceAsElement</a>, <a href="Property.html#getSources()">getSources</a>, <a href="Property.html#getSourcesAsStream()">getSourcesAsStream</a>, <a href="Property.html#getUndefinedString()">getUndefinedString</a>, <a href="Property.html#getUndefinedString(com.nomagic.magicdraw.properties.Property)">getUndefinedString</a>, <a href="Property.html#hashCode()">hashCode</a>, <a href="Property.html#isEditable()">isEditable</a>, <a href="Property.html#isUndefinedState()">isUndefinedState</a>, <a href="Property.html#removeAnnotation(java.lang.String)">removeAnnotation</a>, <a href="Property.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="Property.html#setAdditionalProperties(java.util.Map)">setAdditionalProperties</a>, <a href="Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)">setAdditionalProperty</a>, <a href="Property.html#setAnnotations(java.util.Map)">setAnnotations</a>, <a href="Property.html#setDescription(java.lang.String)">setDescription</a>, <a href="Property.html#setDescriptionID(java.lang.String)">setDescriptionID</a>, <a href="Property.html#setEditable(boolean)">setEditable</a>, <a href="Property.html#setGroup(java.lang.String)">setGroup</a>, <a href="Property.html#setID(java.lang.String)">setID</a>, <a href="Property.html#setIntroductoryVersion(java.lang.String)">setIntroductoryVersion</a>, <a href="Property.html#setNonEditableReason(java.lang.String)">setNonEditableReason</a>, <a href="Property.html#setResourceProvider(com.nomagic.magicdraw.properties.PropertyResourceProvider)">setResourceProvider</a>, <a href="Property.html#setResourceProviderID(java.lang.String)">setResourceProviderID</a>, <a href="Property.html#setSources(java.util.Collection)">setSources</a>, <a href="Property.html#setUndefinedState(boolean)">setUndefinedState</a>, <a href="Property.html#toString()">toString</a></code></div>
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
<section class="detail" id="PATTERN">
<h3>PATTERN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PATTERN</span></div>
<div class="block">Patters which is used to format the number. This pattern should be set to the additional properties of NumberProperty</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.NumberProperty.PATTERN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INT">
<h3>INT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">INT</span></div>
<div class="block">Number type is integer.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.NumberProperty.INT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOUBLE">
<h3>DOUBLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DOUBLE</span></div>
<div class="block">Number type is double.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.NumberProperty.DOUBLE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FLOAT">
<h3>FLOAT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">FLOAT</span></div>
<div class="block">Number type is float.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.NumberProperty.FLOAT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LONG">
<h3>LONG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">LONG</span></div>
<div class="block">Number type is long.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.NumberProperty.LONG">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;()">
<h3>NumberProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NumberProperty</span>()</div>
<div class="block">Default constructor for INT property. Value of the property will be 0. ID will be empty string.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Double,int,double,double)">
<h3>NumberProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NumberProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value,
 int type,
 double low,
 double high)</span></div>
<div class="block">The property constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the ID of property.</dd>
<dd><code>value</code> - the number value of the property.</dd>
<dd><code>type</code> - the number type (INT, DOUBLE or FLOAT).</dd>
<dd><code>low</code> - lowest range of the number.</dd>
<dd><code>high</code> - highest range of the number.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,int,double,double)">
<h3>NumberProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NumberProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 int value,
 double low,
 double high)</span></div>
<div class="block">The property constructor. Type of number will be INT.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the ID of property.</dd>
<dd><code>value</code> - the value of the property.</dd>
<dd><code>low</code> - lowest range of the number.</dd>
<dd><code>high</code> - highest range of the number.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,float,double,double)">
<h3>NumberProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NumberProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 float value,
 double low,
 double high)</span></div>
<div class="block">The property constructor. Type of number will be <a href="#FLOAT"><code>FLOAT</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the ID of property.</dd>
<dd><code>value</code> - the value of the property.</dd>
<dd><code>low</code> - lowest range of the number.</dd>
<dd><code>high</code> - highest range of the number.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,double,double,double)">
<h3>NumberProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NumberProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 double value,
 double low,
 double high)</span></div>
<div class="block">The property constructor. Type of number will be DOUBLE.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the ID of property.</dd>
<dd><code>value</code> - the value of the property.</dd>
<dd><code>low</code> - lowest range of the number.</dd>
<dd><code>high</code> - highest range of the number.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,long,double,double)">
<h3>NumberProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NumberProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 long value,
 double low,
 double high)</span></div>
<div class="block">The property constructor. Type of number will be LONG.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the ID of property.</dd>
<dd><code>value</code> - the value of the property.</dd>
<dd><code>low</code> - lowest range of the number.</dd>
<dd><code>high</code> - highest range of the number.</dd>
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
<section class="detail" id="getValueStringRepresentation()">
<h3>getValueStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValueStringRepresentation</span>()</div>
<div class="block">Returns value's string representation.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#getValueStringRepresentation()">getValueStringRepresentation</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Returns:</dt>
<dd>the string representation of the number.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPattern(com.nomagic.magicdraw.properties.Property)">
<h3>getPattern</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPattern</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStringRepresentation(int,java.lang.Double,java.lang.String)">
<h3>getStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStringRepresentation</span><wbr/><span class="parameters">(int type,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStringRepresentation(int,java.lang.Double)">
<h3>getStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStringRepresentation</span><wbr/><span class="parameters">(int type,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="toDouble(java.lang.Number)">
<h3>toDouble</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">toDouble</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a> number)</span></div>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.properties.PropertyVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> v)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="Property.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">Property</a></code></span></div>
<div class="block">Accepts the given visitor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="Property.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Parameters:</dt>
<dd><code>v</code> - the PropertyVisitor.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInteger()">
<h3>getInteger</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getInteger</span>()</div>
<div class="block">Returns value as int (primitive type).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property value as int. 0 if value is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLong()">
<h3>getLong</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getLong</span>()</div>
<div class="block">Returns value as long (primitive type).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property value as long. 0 if value is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDouble()">
<h3>getDouble</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getDouble</span>()</div>
<div class="block">Returns value as double (primitive type).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property value as double. 0 if value is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFloat()">
<h3>getFloat</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">float</span> <span class="element-name">getFloat</span>()</div>
<div class="block">Returns value as float (primitive type).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property value as float. 0 if value is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDoubleObject()">
<h3>getDoubleObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getDoubleObject</span>()</div>
<div class="block">Returns value as Double object.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property value as Double.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(int)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Sets value as primitive integer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - a new integer value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(double)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block">Sets value as primitive double type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - a new double value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(float)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(float value)</span></div>
<div class="block">Sets value as primitive float type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - a new float value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="Property.html#setValue(java.lang.Object)">Property</a></code></span></div>
<div class="block">Sets new property value.
 Will fire a <code>PropertyChangeEvent</code> with propertyName - property
 ID, newValue and oldValue.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#setValue(java.lang.Object)">setValue</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
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
<dt>Overrides:</dt>
<dd><code><a href="Property.html#isValueCompatible(java.lang.Object)">isValueCompatible</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Returns:</dt>
<dd>true if given object can be assigned as value to this property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue()">
<h3>getValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="Property.html#getValue()">Property</a></code></span></div>
<div class="block">Returns properties value.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#getValue()">getValue</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Returns:</dt>
<dd>value of the property.</dd>
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
<dt>Overrides:</dt>
<dd><code><a href="Property.html#getClassType()">getClassType</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Returns:</dt>
<dd>PropertyID.NUMBER_PROPERTY</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="PropertyID.html#NUMBER_PROPERTY"><code>PropertyID.NUMBER_PROPERTY</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNumberType()">
<h3>getNumberType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getNumberType</span>()</div>
<div class="block">Returns type of the number.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>number type - INT, DOUBLE or FLOAT.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNumberType(int)">
<h3>setNumberType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNumberType</span><wbr/><span class="parameters">(int type)</span></div>
<div class="block">Sets type of the number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the number type - INT, DOUBLE or FLOAT.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLowRange()">
<h3>getLowRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getLowRange</span>()</div>
<div class="block">Returns the lowest range of the number value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>lowest range.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHighRange()">
<h3>getHighRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getHighRange</span>()</div>
<div class="block">Returns the highest range of the value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>highest range.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLowRange(double)">
<h3>setLowRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLowRange</span><wbr/><span class="parameters">(double range)</span></div>
<div class="block">Returns the lowest range of the value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>range</code> - the lowest range.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHighRange(double)">
<h3>setHighRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHighRange</span><wbr/><span class="parameters">(double range)</span></div>
<div class="block">Returns the highest range of the value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>range</code> - the highest range.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasError(com.nomagic.magicdraw.properties.NumberProperty,java.lang.String)">
<h3>hasError</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">hasError</span><wbr/><span class="parameters">(<a href="NumberProperty.html" title="class in com.nomagic.magicdraw.properties">NumberProperty</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newNumber)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSoftRange()">
<h3>isSoftRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSoftRange</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Property is not allowed to cross the range boundaries.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSoftRange(boolean)">
<h3>setSoftRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSoftRange</span><wbr/><span class="parameters">(boolean softRange)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>softRange</code> - Property is allowed to cross the range boundaries. Default is false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="NumberProperty.html" title="class in com.nomagic.magicdraw.properties">NumberProperty</a></span> <span class="element-name">clone</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="Property.html#clone()">Property</a></code></span></div>
<div class="block">Clones the property. Clone is not deep, the clone will have the same instance of value.
 The clone will not have registered PropertyChangeListeners.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="Property.html#clone()">clone</a></code> in class <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></dd>
<dt>Returns:</dt>
<dd>the cloned property.</dd>
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
