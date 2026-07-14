# JAVA OPENAPI: SimpleStyle (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/format/html/SimpleStyle.html
- source_path: `com/nomagic/magicreport/format/html/SimpleStyle.html`
- source_sha256: `3d37730e53d785898ea2cb655eaec4f23dbb9ba9fa15ea21527d0d9388feccc8`
- captured_utc: `2026-07-14T16:58:39.268305+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format.html](package-summary.html)

## Class SimpleStyle

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[javax.swing.text.SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)
com.nomagic.magicreport.format.html.SimpleStyle

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html)`, `[MutableAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html)`, `[Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html)`

Direct Known Subclasses:
`[CellStyle](CellStyle.html)`, `[ColumnStyle](ColumnStyle.html)`, `[GraphicStyle](GraphicStyle.html)`, `[ParagraphStyle](ParagraphStyle.html)`, `[RowStyle](RowStyle.html)`, `[TableStyle](TableStyle.html)`, `[TextStyle](TextStyle.html)`

@OpenApiAllpublic classSimpleStyle
extends [SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)
implements [Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html)

A straightforward implementation of Style using a SimpleAttributeSet.

Since:
Jun 1, 2009
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.format.html.SimpleStyle)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [ChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeEvent.html)`
`[changeEvent](#changeEvent)`
Only one ChangeEvent is needed per model instance since the event's only (read-only) state is the source
 property.
`protected [EventListenerList](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/EventListenerList.html)`
`[listenerList](#listenerList)`
The change listeners for the model.
Fields inherited from class javax.swing.text.[SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)
`[EMPTY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#EMPTY)`
Fields inherited from interface javax.swing.text.[AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html)
`[NameAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#NameAttribute), [ResolveAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#ResolveAttribute)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SimpleStyle](#%3Cinit%3E())()`
Creates a new style, with a null name and parent.
`[SimpleStyle](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Creates a new style.
`[SimpleStyle](#%3Cinit%3E(java.lang.String,javax.swing.text.Style))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html) parent)`
Creates a new style.
`[SimpleStyle](#%3Cinit%3E(javax.swing.text.Style))([Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html) parent)`
Creates a new style.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addAttribute](#addAttribute(java.lang.Object,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) name,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Adds an attribute.
`void`
`[addAttributes](#addAttributes(javax.swing.text.AttributeSet))([AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html) attr)`
Adds a set of attributes to the element.
`void`
`[addChangeListener](#addChangeListener(javax.swing.event.ChangeListener))([ChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeListener.html) l)`
Adds a change listener.
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)`
Compares this object to the specified object.
`protected void`
`[fireStateChanged](#fireStateChanged())()`
Notifies all listeners that have registered interest for notification on this event type.
`[ChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeListener.html)[]`
`[getChangeListeners](#getChangeListeners())()`
Returns an array of all the `ChangeListener`s added to this SimpleStyle with addChangeListener().
`<T extends [EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)> 
T[]`
`[getListeners](#getListeners(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> listenerType)`
Return an array of all the listeners of the given type that were added to this model.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Fetches the name of the style.
`int`
`[hashCode](#hashCode())()`
Returns a hashcode for this set of attributes.
`void`
`[removeAttribute](#removeAttribute(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) name)`
Removes an attribute from the set.
`void`
`[removeAttributes](#removeAttributes(java.util.Enumeration))([Enumeration](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Enumeration.html)<?> names)`
Removes a set of attributes for the element.
`void`
`[removeAttributes](#removeAttributes(javax.swing.text.AttributeSet))([AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html) attrs)`
Removes a set of attributes for the element.
`void`
`[removeChangeListener](#removeChangeListener(javax.swing.event.ChangeListener))([ChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeListener.html) l)`
Removes a change listener.
`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Changes the name of the style.
Methods inherited from class javax.swing.text.[SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#clone()), [containsAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#containsAttribute(java.lang.Object,java.lang.Object)), [containsAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#containsAttributes(javax.swing.text.AttributeSet)), [copyAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#copyAttributes()), [getAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttribute(java.lang.Object)), [getAttributeCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttributeCount()), [getAttributeNames](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttributeNames()), [getResolveParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getResolveParent()), [isDefined](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isDefined(java.lang.Object)), [isEmpty](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isEmpty()), [isEqual](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isEqual(javax.swing.text.AttributeSet)), [setResolveParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#setResolveParent(javax.swing.text.AttributeSet)), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.text.[AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html)
`[containsAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#containsAttribute(java.lang.Object,java.lang.Object)), [containsAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#containsAttributes(javax.swing.text.AttributeSet)), [copyAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#copyAttributes()), [getAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttribute(java.lang.Object)), [getAttributeCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttributeCount()), [getAttributeNames](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttributeNames()), [getResolveParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getResolveParent()), [isDefined](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#isDefined(java.lang.Object)), [isEqual](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#isEqual(javax.swing.text.AttributeSet))`
Methods inherited from interface javax.swing.text.[MutableAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html)
`[setResolveParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#setResolveParent(javax.swing.text.AttributeSet))`

============ FIELD DETAIL =========== 
Field Details
listenerList
protected [EventListenerList](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/EventListenerList.html) listenerList
The change listeners for the model.
changeEvent
protected transient [ChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeEvent.html) changeEvent
Only one ChangeEvent is needed per model instance since the event's only (read-only) state is the source
 property. The source of events generated here is always "this".
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SimpleStyle
public SimpleStyle()
Creates a new style, with a null name and parent.
SimpleStyle
public SimpleStyle([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Creates a new style.
Parameters:
`name` - the style name, null for unnamed
SimpleStyle
public SimpleStyle([Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html) parent)
Creates a new style.
Parameters:
`parent` - the parent style, null if none
SimpleStyle
public SimpleStyle([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html) parent)
Creates a new style.
Parameters:
`name` - the style name, null for unnamed
`parent` - the parent style, null if none
 ============ METHOD DETAIL ========== 
Method Details
getName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
Fetches the name of the style. A style is not required to be named, so null is returned if there is no name
 associated with the style.
Specified by:
`[getName](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html#getName())` in interface `[Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html)`
Returns:
the name
setName
public void setName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Changes the name of the style. Does nothing with a null name.
Parameters:
`name` - the new name
addChangeListener
public void addChangeListener([ChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeListener.html) l)
Adds a change listener.
Specified by:
`[addChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html#addChangeListener(javax.swing.event.ChangeListener))` in interface `[Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html)`
Parameters:
`l` - the change listener
removeChangeListener
public void removeChangeListener([ChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeListener.html) l)
Removes a change listener.
Specified by:
`[removeChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html#removeChangeListener(javax.swing.event.ChangeListener))` in interface `[Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html)`
Parameters:
`l` - the change listener
getChangeListeners
public [ChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeListener.html)[] getChangeListeners()
Returns an array of all the `ChangeListener`s added to this SimpleStyle with addChangeListener().
Returns:
all of the `ChangeListener`s added or an empty array if no listeners have been added
Since:
1.4
fireStateChanged
protected void fireStateChanged()
Notifies all listeners that have registered interest for notification on this event type. The event instance
 is lazily created using the parameters passed into the fire method.
See Also:
[`EventListenerList`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/EventListenerList.html)
getListeners
public <T extends [EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)> T[] getListeners([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> listenerType)
Return an array of all the listeners of the given type that were added to this model.
Type Parameters:
`T` - EventListener
Parameters:
`listenerType` - listener class
Returns:
all of the objects receiving *listenerType* notifications from this model
addAttribute
public void addAttribute([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) name,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Adds an attribute.
Specified by:
`[addAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#addAttribute(java.lang.Object,java.lang.Object))` in interface `[MutableAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html)`
Overrides:
`[addAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#addAttribute(java.lang.Object,java.lang.Object))` in class `[SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)`
Parameters:
`name` - the non-null attribute name
`value` - the attribute value
addAttributes
public void addAttributes([AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html) attr)
Adds a set of attributes to the element.
Specified by:
`[addAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#addAttributes(javax.swing.text.AttributeSet))` in interface `[MutableAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html)`
Overrides:
`[addAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#addAttributes(javax.swing.text.AttributeSet))` in class `[SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)`
Parameters:
`attr` - the attributes to add
removeAttribute
public void removeAttribute([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) name)
Removes an attribute from the set.
Specified by:
`[removeAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#removeAttribute(java.lang.Object))` in interface `[MutableAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html)`
Overrides:
`[removeAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#removeAttribute(java.lang.Object))` in class `[SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)`
Parameters:
`name` - the non-null attribute name
removeAttributes
public void removeAttributes([Enumeration](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Enumeration.html)<?> names)
Removes a set of attributes for the element.
Specified by:
`[removeAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#removeAttributes(java.util.Enumeration))` in interface `[MutableAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html)`
Overrides:
`[removeAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#removeAttributes(java.util.Enumeration))` in class `[SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)`
Parameters:
`names` - the attribute names
removeAttributes
public void removeAttributes([AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html) attrs)
Removes a set of attributes for the element.
Specified by:
`[removeAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#removeAttributes(javax.swing.text.AttributeSet))` in interface `[MutableAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html)`
Overrides:
`[removeAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#removeAttributes(javax.swing.text.AttributeSet))` in class `[SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)`
Parameters:
`attrs` - the attributes
hashCode
public int hashCode()
Returns a hashcode for this set of attributes.
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#hashCode())` in class `[SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)`
Returns:
a hashcode value for this set of attributes.
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)
Compares this object to the specified object. The result is `true` if the object is an equivalent
 set of attributes.
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#equals(java.lang.Object))` in class `[SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)`
Parameters:
`obj` - the object to compare this attribute set with
Returns:
`true` if the objects are equal; `false` otherwise

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format.html</a></div>
<h1 class="title" title="Class SimpleStyle">Class SimpleStyle</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">javax.swing.text.SimpleAttributeSet</a>
<div class="inheritance">com.nomagic.magicreport.format.html.SimpleStyle</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html" title="class or interface in javax.swing.text">MutableAttributeSet</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a></code>, <code><a href="ColumnStyle.html" title="class in com.nomagic.magicreport.format.html">ColumnStyle</a></code>, <code><a href="GraphicStyle.html" title="class in com.nomagic.magicreport.format.html">GraphicStyle</a></code>, <code><a href="ParagraphStyle.html" title="class in com.nomagic.magicreport.format.html">ParagraphStyle</a></code>, <code><a href="RowStyle.html" title="class in com.nomagic.magicreport.format.html">RowStyle</a></code>, <code><a href="TableStyle.html" title="class in com.nomagic.magicreport.format.html">TableStyle</a></code>, <code><a href="TextStyle.html" title="class in com.nomagic.magicreport.format.html">TextStyle</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SimpleStyle</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">SimpleAttributeSet</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a></span></div>
<div class="block">A straightforward implementation of Style using a SimpleAttributeSet.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 1, 2009</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.format.html.SimpleStyle">Serialized Form</a></li>
</ul>
</dd>
</dl>
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
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeEvent.html" title="class or interface in javax.swing.event">ChangeEvent</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#changeEvent">changeEvent</a></code></div>
<div class="col-last even-row-color">
<div class="block">Only one ChangeEvent is needed per model instance since the event's only (read-only) state is the source
 property.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/EventListenerList.html" title="class or interface in javax.swing.event">EventListenerList</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#listenerList">listenerList</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The change listeners for the model.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.text.SimpleAttributeSet">Fields inherited from class javax.swing.text.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">SimpleAttributeSet</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#EMPTY" title="class or interface in javax.swing.text">EMPTY</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.text.AttributeSet">Fields inherited from interface javax.swing.text.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#NameAttribute" title="class or interface in javax.swing.text">NameAttribute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#ResolveAttribute" title="class or interface in javax.swing.text">ResolveAttribute</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SimpleStyle</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new style, with a null name and parent.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">SimpleStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new style.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,javax.swing.text.Style)">SimpleStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a> parent)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new style.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(javax.swing.text.Style)">SimpleStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a> parent)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new style.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAttribute(java.lang.Object,java.lang.Object)">addAttribute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds an attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAttributes(javax.swing.text.AttributeSet)">addAttributes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a> attr)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a set of attributes to the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addChangeListener(javax.swing.event.ChangeListener)">addChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeListener.html" title="class or interface in javax.swing.event">ChangeListener</a> l)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a change listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Compares this object to the specified object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fireStateChanged()">fireStateChanged</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notifies all listeners that have registered interest for notification on this event type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeListener.html" title="class or interface in javax.swing.event">ChangeListener</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChangeListeners()">getChangeListeners</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns an array of all the <code>ChangeListener</code>s added to this SimpleStyle with addChangeListener().</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a>&gt;<br/>T[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getListeners(java.lang.Class)">getListeners</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; listenerType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an array of all the listeners of the given type that were added to this model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Fetches the name of the style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a hashcode for this set of attributes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAttribute(java.lang.Object)">removeAttribute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes an attribute from the set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAttributes(java.util.Enumeration)">removeAttributes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Enumeration.html" title="class or interface in java.util">Enumeration</a>&lt;?&gt; names)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a set of attributes for the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAttributes(javax.swing.text.AttributeSet)">removeAttributes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a> attrs)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a set of attributes for the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeChangeListener(javax.swing.event.ChangeListener)">removeChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeListener.html" title="class or interface in javax.swing.event">ChangeListener</a> l)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a change listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Changes the name of the style.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.text.SimpleAttributeSet">Methods inherited from class javax.swing.text.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">SimpleAttributeSet</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#clone()" title="class or interface in javax.swing.text">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#containsAttribute(java.lang.Object,java.lang.Object)" title="class or interface in javax.swing.text">containsAttribute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#containsAttributes(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">containsAttributes</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#copyAttributes()" title="class or interface in javax.swing.text">copyAttributes</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttribute(java.lang.Object)" title="class or interface in javax.swing.text">getAttribute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttributeCount()" title="class or interface in javax.swing.text">getAttributeCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttributeNames()" title="class or interface in javax.swing.text">getAttributeNames</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getResolveParent()" title="class or interface in javax.swing.text">getResolveParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isDefined(java.lang.Object)" title="class or interface in javax.swing.text">isDefined</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isEmpty()" title="class or interface in javax.swing.text">isEmpty</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isEqual(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">isEqual</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#setResolveParent(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">setResolveParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#toString()" title="class or interface in javax.swing.text">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.text.AttributeSet">Methods inherited from interface javax.swing.text.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#containsAttribute(java.lang.Object,java.lang.Object)" title="class or interface in javax.swing.text">containsAttribute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#containsAttributes(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">containsAttributes</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#copyAttributes()" title="class or interface in javax.swing.text">copyAttributes</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttribute(java.lang.Object)" title="class or interface in javax.swing.text">getAttribute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttributeCount()" title="class or interface in javax.swing.text">getAttributeCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttributeNames()" title="class or interface in javax.swing.text">getAttributeNames</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getResolveParent()" title="class or interface in javax.swing.text">getResolveParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#isDefined(java.lang.Object)" title="class or interface in javax.swing.text">isDefined</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#isEqual(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">isEqual</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.text.MutableAttributeSet">Methods inherited from interface javax.swing.text.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html" title="class or interface in javax.swing.text">MutableAttributeSet</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#setResolveParent(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">setResolveParent</a></code></div>
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
<section class="detail" id="listenerList">
<h3>listenerList</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/EventListenerList.html" title="class or interface in javax.swing.event">EventListenerList</a></span> <span class="element-name">listenerList</span></div>
<div class="block">The change listeners for the model.</div>
</section>
</li>
<li>
<section class="detail" id="changeEvent">
<h3>changeEvent</h3>
<div class="member-signature"><span class="modifiers">protected transient</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeEvent.html" title="class or interface in javax.swing.event">ChangeEvent</a></span> <span class="element-name">changeEvent</span></div>
<div class="block">Only one ChangeEvent is needed per model instance since the event's only (read-only) state is the source
 property. The source of events generated here is always "this".</div>
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
<h3>SimpleStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SimpleStyle</span>()</div>
<div class="block">Creates a new style, with a null name and parent.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>SimpleStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SimpleStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Creates a new style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the style name, null for unnamed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(javax.swing.text.Style)">
<h3>SimpleStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SimpleStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a> parent)</span></div>
<div class="block">Creates a new style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent style, null if none</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,javax.swing.text.Style)">
<h3>SimpleStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SimpleStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a> parent)</span></div>
<div class="block">Creates a new style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the style name, null for unnamed</dd>
<dd><code>parent</code> - the parent style, null if none</dd>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Fetches the name of the style. A style is not required to be named, so null is returned if there is no name
 associated with the style.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html#getName()" title="class or interface in javax.swing.text">getName</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a></code></dd>
<dt>Returns:</dt>
<dd>the name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Changes the name of the style. Does nothing with a null name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the new name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addChangeListener(javax.swing.event.ChangeListener)">
<h3>addChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeListener.html" title="class or interface in javax.swing.event">ChangeListener</a> l)</span></div>
<div class="block">Adds a change listener.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html#addChangeListener(javax.swing.event.ChangeListener)" title="class or interface in javax.swing.text">addChangeListener</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a></code></dd>
<dt>Parameters:</dt>
<dd><code>l</code> - the change listener</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeChangeListener(javax.swing.event.ChangeListener)">
<h3>removeChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeListener.html" title="class or interface in javax.swing.event">ChangeListener</a> l)</span></div>
<div class="block">Removes a change listener.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html#removeChangeListener(javax.swing.event.ChangeListener)" title="class or interface in javax.swing.text">removeChangeListener</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a></code></dd>
<dt>Parameters:</dt>
<dd><code>l</code> - the change listener</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChangeListeners()">
<h3>getChangeListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/ChangeListener.html" title="class or interface in javax.swing.event">ChangeListener</a>[]</span> <span class="element-name">getChangeListeners</span>()</div>
<div class="block">Returns an array of all the <code>ChangeListener</code>s added to this SimpleStyle with addChangeListener().</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all of the <code>ChangeListener</code>s added or an empty array if no listeners have been added</dd>
<dt>Since:</dt>
<dd>1.4</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fireStateChanged()">
<h3>fireStateChanged</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">fireStateChanged</span>()</div>
<div class="block">Notifies all listeners that have registered interest for notification on this event type. The event instance
 is lazily created using the parameters passed into the fire method.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/event/EventListenerList.html" title="class or interface in javax.swing.event"><code>EventListenerList</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getListeners(java.lang.Class)">
<h3>getListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a>&gt;</span> <span class="return-type">T[]</span> <span class="element-name">getListeners</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; listenerType)</span></div>
<div class="block">Return an array of all the listeners of the given type that were added to this model.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - EventListener</dd>
<dt>Parameters:</dt>
<dd><code>listenerType</code> - listener class</dd>
<dt>Returns:</dt>
<dd>all of the objects receiving <em>listenerType</em> notifications from this model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAttribute(java.lang.Object,java.lang.Object)">
<h3>addAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAttribute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Adds an attribute.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#addAttribute(java.lang.Object,java.lang.Object)" title="class or interface in javax.swing.text">addAttribute</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html" title="class or interface in javax.swing.text">MutableAttributeSet</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#addAttribute(java.lang.Object,java.lang.Object)" title="class or interface in javax.swing.text">addAttribute</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">SimpleAttributeSet</a></code></dd>
<dt>Parameters:</dt>
<dd><code>name</code> - the non-null attribute name</dd>
<dd><code>value</code> - the attribute value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAttributes(javax.swing.text.AttributeSet)">
<h3>addAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAttributes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a> attr)</span></div>
<div class="block">Adds a set of attributes to the element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#addAttributes(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">addAttributes</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html" title="class or interface in javax.swing.text">MutableAttributeSet</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#addAttributes(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">addAttributes</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">SimpleAttributeSet</a></code></dd>
<dt>Parameters:</dt>
<dd><code>attr</code> - the attributes to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAttribute(java.lang.Object)">
<h3>removeAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAttribute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> name)</span></div>
<div class="block">Removes an attribute from the set.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#removeAttribute(java.lang.Object)" title="class or interface in javax.swing.text">removeAttribute</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html" title="class or interface in javax.swing.text">MutableAttributeSet</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#removeAttribute(java.lang.Object)" title="class or interface in javax.swing.text">removeAttribute</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">SimpleAttributeSet</a></code></dd>
<dt>Parameters:</dt>
<dd><code>name</code> - the non-null attribute name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAttributes(java.util.Enumeration)">
<h3>removeAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAttributes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Enumeration.html" title="class or interface in java.util">Enumeration</a>&lt;?&gt; names)</span></div>
<div class="block">Removes a set of attributes for the element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#removeAttributes(java.util.Enumeration)" title="class or interface in javax.swing.text">removeAttributes</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html" title="class or interface in javax.swing.text">MutableAttributeSet</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#removeAttributes(java.util.Enumeration)" title="class or interface in javax.swing.text">removeAttributes</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">SimpleAttributeSet</a></code></dd>
<dt>Parameters:</dt>
<dd><code>names</code> - the attribute names</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAttributes(javax.swing.text.AttributeSet)">
<h3>removeAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAttributes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a> attrs)</span></div>
<div class="block">Removes a set of attributes for the element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#removeAttributes(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">removeAttributes</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html" title="class or interface in javax.swing.text">MutableAttributeSet</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#removeAttributes(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">removeAttributes</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">SimpleAttributeSet</a></code></dd>
<dt>Parameters:</dt>
<dd><code>attrs</code> - the attributes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<div class="block">Returns a hashcode for this set of attributes.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#hashCode()" title="class or interface in javax.swing.text">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">SimpleAttributeSet</a></code></dd>
<dt>Returns:</dt>
<dd>a hashcode value for this set of attributes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Compares this object to the specified object. The result is <code>true</code> if the object is an equivalent
 set of attributes.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#equals(java.lang.Object)" title="class or interface in javax.swing.text">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">SimpleAttributeSet</a></code></dd>
<dt>Parameters:</dt>
<dd><code>obj</code> - the object to compare this attribute set with</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the objects are equal; <code>false</code> otherwise</dd>
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
