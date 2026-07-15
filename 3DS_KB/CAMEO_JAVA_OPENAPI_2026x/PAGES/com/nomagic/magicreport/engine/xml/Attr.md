# JAVA OPENAPI: Attr (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/xml/Attr.html
- source_path: `com/nomagic/magicreport/engine/xml/Attr.html`
- source_sha256: `fadd11caef40f6662a4ca5ad1264342b7fc19f23eab8f50142e3109d7f496f18`
- captured_utc: `2026-07-14T16:58:38.161298+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.xml](package-summary.html)

## Class Attr

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.engine.xml.Attr

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`

@OpenApiAllpublic classAttr
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html), [Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)

An implementation of Attribute interface.

Since:
Jun 11, 2009
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.xml.Attr)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Attr](#%3Cinit%3E())()`
Construct a new, empty AttributesImpl object.
`[Attr](#%3Cinit%3E(org.xml.sax.Attributes))([Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) atts)`
Copy an existing Attributes object.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addAttribute](#addAttribute(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Add an attribute to the end of the list.
`void`
`[clear](#clear())()`
Clear the attribute list for reuse.
`int`
`[getIndex](#getIndex(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)`
Look up an attribute's index by qualified (prefixed) name.
`int`
`[getIndex](#getIndex(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName)`
Look up an attribute's index by Namespace name.
`int`
`[getLength](#getLength())()`
Return the number of attributes in the list.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getLocalName](#getLocalName(int))(int index)`
Return an attribute's local name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getQName](#getQName(int))(int index)`
Return an attribute's qualified (prefixed) name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getType](#getType(int))(int index)`
Return an attribute's type by index.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getType](#getType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)`
Look up an attribute's type by qualified (prefixed) name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getType](#getType(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName)`
Look up an attribute's type by Namespace-qualified name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getURI](#getURI(int))(int index)`
Return an attribute's Namespace URI.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getValue](#getValue(int))(int index)`
Return an attribute's value by index.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getValue](#getValue(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)`
Look up an attribute's value by qualified (prefixed) name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getValue](#getValue(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName)`
Look up an attribute's value by Namespace-qualified name.
`void`
`[removeAttribute](#removeAttribute(int))(int index)`
Remove an attribute from the list.
`void`
`[setAttribute](#setAttribute(int,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String))(int index,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Set an attribute in the list.
`void`
`[setAttributes](#setAttributes(org.xml.sax.Attributes))([Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) atts)`
Copy an entire Attributes object.
`void`
`[setLocalName](#setLocalName(int,java.lang.String))(int index,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName)`
Set the local name of a specific attribute.
`void`
`[setQName](#setQName(int,java.lang.String))(int index,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)`
Set the qualified name of a specific attribute.
`void`
`[setType](#setType(int,java.lang.String))(int index,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)`
Set the type of a specific attribute.
`void`
`[setURI](#setURI(int,java.lang.String))(int index,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri)`
Set the Namespace URI of a specific attribute.
`void`
`[setValue](#setValue(int,java.lang.String))(int index,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Set the value of a specific attribute.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Attr
public Attr()
Construct a new, empty AttributesImpl object.
Attr
public Attr([Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) atts)
Copy an existing Attributes object. This constructor is especially useful inside a
 [`startElement`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)) event.
Parameters:
`atts` - The existing Attributes object.
 ============ METHOD DETAIL ========== 
Method Details
getLength
public int getLength()
Return the number of attributes in the list.
Specified by:
`[getLength](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getLength())` in interface `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
Returns:
The number of attributes in the list.
See Also:
[`Attributes.getLength()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getLength())
getURI
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getURI(int index)
Return an attribute's Namespace URI.
Specified by:
`[getURI](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getURI(int))` in interface `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
Parameters:
`index` - The attribute's index (zero-based).
Returns:
The Namespace URI, the empty string if none is available, or null if the index is out of range.
See Also:
[`Attributes.getURI(int)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getURI(int))
getLocalName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getLocalName(int index)
Return an attribute's local name.
Specified by:
`[getLocalName](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getLocalName(int))` in interface `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
Parameters:
`index` - The attribute's index (zero-based).
Returns:
The attribute's local name, the empty string if none is available, or null if the index if out of
 range.
See Also:
[`Attributes.getLocalName(int)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getLocalName(int))
getQName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getQName(int index)
Return an attribute's qualified (prefixed) name.
Specified by:
`[getQName](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getQName(int))` in interface `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
Parameters:
`index` - The attribute's index (zero-based).
Returns:
The attribute's qualified name, the empty string if none is available, or null if the index is out
 of bounds.
See Also:
[`Attributes.getQName(int)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getQName(int))
getType
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getType(int index)
Return an attribute's type by index.
Specified by:
`[getType](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getType(int))` in interface `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
Parameters:
`index` - The attribute's index (zero-based).
Returns:
The attribute's type, "CDATA" if the type is unknown, or null if the index is out of bounds.
See Also:
[`Attributes.getType(int)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getType(int))
getValue
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getValue(int index)
Return an attribute's value by index.
Specified by:
`[getValue](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getValue(int))` in interface `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
Parameters:
`index` - The attribute's index (zero-based).
Returns:
The attribute's value or null if the index is out of bounds.
See Also:
[`Attributes.getValue(int)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getValue(int))
getIndex
public int getIndex([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName)
Look up an attribute's index by Namespace name.
 In many cases, it will be more efficient to look up the name once and use the index query methods rather
 than using the name query methods repeatedly.
Specified by:
`[getIndex](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getIndex(java.lang.String,java.lang.String))` in interface `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
Parameters:
`uri` - The attribute's Namespace URI, or the empty string if none is available.
`localName` - The attribute's local name.
Returns:
The attribute's index, or -1 if none matches.
See Also:
[`Attributes.getIndex(java.lang.String,java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getIndex(java.lang.String,java.lang.String))
getIndex
public int getIndex([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)
Look up an attribute's index by qualified (prefixed) name.
Specified by:
`[getIndex](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getIndex(java.lang.String))` in interface `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
Parameters:
`qName` - The qualified name.
Returns:
The attribute's index, or -1 if none matches.
See Also:
[`Attributes.getIndex(java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getIndex(java.lang.String))
getType
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getType([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName)
Look up an attribute's type by Namespace-qualified name.
Specified by:
`[getType](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getType(java.lang.String,java.lang.String))` in interface `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
Parameters:
`uri` - The Namespace URI, or the empty string for a name with no explicit Namespace URI.
`localName` - The local name.
Returns:
The attribute's type, or null if there is no matching attribute.
See Also:
[`Attributes.getType(java.lang.String,java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getType(java.lang.String,java.lang.String))
getType
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getType([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)
Look up an attribute's type by qualified (prefixed) name.
Specified by:
`[getType](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getType(java.lang.String))` in interface `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
Parameters:
`qName` - The qualified name.
Returns:
The attribute's type, or null if there is no matching attribute.
See Also:
[`Attributes.getType(java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getType(java.lang.String))
getValue
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getValue([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName)
Look up an attribute's value by Namespace-qualified name.
Specified by:
`[getValue](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getValue(java.lang.String,java.lang.String))` in interface `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
Parameters:
`uri` - The Namespace URI, or the empty string for a name with no explicit Namespace URI.
`localName` - The local name.
Returns:
The attribute's value, or null if there is no matching attribute.
See Also:
[`Attributes.getValue(java.lang.String,java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getValue(java.lang.String,java.lang.String))
getValue
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getValue([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)
Look up an attribute's value by qualified (prefixed) name.
Specified by:
`[getValue](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getValue(java.lang.String))` in interface `[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
Parameters:
`qName` - The qualified name.
Returns:
The attribute's value, or null if there is no matching attribute.
See Also:
[`Attributes.getValue(java.lang.String)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getValue(java.lang.String))
clear
public void clear()
Clear the attribute list for reuse. Note that little memory is freed by this call: the current array is kept
 so it can be reused.
setAttributes
public void setAttributes([Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) atts)
Copy an entire Attributes object. It may be more efficient to reuse an existing object rather than
 constantly allocating new ones.
Parameters:
`atts` - The attributes to copy.
addAttribute
public void addAttribute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Add an attribute to the end of the list. For the sake of speed, this method does no checking to see if the
 attribute is already in the list: that is the responsibility of the application.
Parameters:
`uri` - The Namespace URI, or the empty string if none is available or Namespace processing is not being
 performed.
`localName` - The local name, or the empty string if Namespace processing is not being performed.
`qName` - The qualified (prefixed) name, or the empty string if qualified names are not available.
`type` - The attribute type as a string.
`value` - The attribute value.
setAttribute
public void setAttribute(int index,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Set an attribute in the list. For the sake of speed, this method does no checking for name conflicts or
 well-formedness: such checks are the responsibility of the application.
Parameters:
`index` - The index of the attribute (zero-based).
`uri` - The Namespace URI, or the empty string if none is available or Namespace processing is not being
 performed.
`localName` - The local name, or the empty string if Namespace processing is not being performed.
`qName` - The qualified name, or the empty string if qualified names are not available.
`type` - The attribute type as a string.
`value` - The attribute value.
Throws:
`[ArrayIndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html)` - When the supplied index does not point to an attribute
 in the list.
removeAttribute
public void removeAttribute(int index)
Remove an attribute from the list.
Parameters:
`index` - The index of the attribute (zero-based).
Throws:
`[ArrayIndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html)` - When the supplied index does not point to an attribute
 in the list.
setURI
public void setURI(int index,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri)
Set the Namespace URI of a specific attribute.
Parameters:
`index` - The index of the attribute (zero-based).
`uri` - The attribute's Namespace URI, or the empty string for none.
Throws:
`[ArrayIndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html)` - When the supplied index does not point to an attribute
 in the list.
setLocalName
public void setLocalName(int index,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName)
Set the local name of a specific attribute.
Parameters:
`index` - The index of the attribute (zero-based).
`localName` - The attribute's local name, or the empty string for none.
Throws:
`[ArrayIndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html)` - When the supplied index does not point to an attribute
 in the list.
setQName
public void setQName(int index,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)
Set the qualified name of a specific attribute.
Parameters:
`index` - The index of the attribute (zero-based).
`qName` - The attribute's qualified name, or the empty string for none.
Throws:
`[ArrayIndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html)` - When the supplied index does not point to an attribute
 in the list.
setType
public void setType(int index,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)
Set the type of a specific attribute.
Parameters:
`index` - The index of the attribute (zero-based).
`type` - The attribute's type.
Throws:
`[ArrayIndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html)` - When the supplied index does not point to an attribute
 in the list.
setValue
public void setValue(int index,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Set the value of a specific attribute.
Parameters:
`index` - The index of the attribute (zero-based).
`value` - The attribute's value.
Throws:
`[ArrayIndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html)` - When the supplied index does not point to an attribute
 in the list.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.xml</a></div>
<h1 class="title" title="Class Attr">Class Attr</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.engine.xml.Attr</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Attr</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></span></div>
<div class="block">An implementation of Attribute interface.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 11, 2009</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.xml.Attr">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Attr</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Construct a new, empty AttributesImpl object.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(org.xml.sax.Attributes)">Attr</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> atts)</code></div>
<div class="col-last odd-row-color">
<div class="block">Copy an existing Attributes object.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAttribute(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">addAttribute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add an attribute to the end of the list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clear()">clear</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clear the attribute list for reuse.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIndex(java.lang.String)">getIndex</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look up an attribute's index by qualified (prefixed) name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIndex(java.lang.String,java.lang.String)">getIndex</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look up an attribute's index by Namespace name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLength()">getLength</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the number of attributes in the list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLocalName(int)">getLocalName</a><wbr/>(int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an attribute's local name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getQName(int)">getQName</a><wbr/>(int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an attribute's qualified (prefixed) name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getType(int)">getType</a><wbr/>(int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an attribute's type by index.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getType(java.lang.String)">getType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look up an attribute's type by qualified (prefixed) name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getType(java.lang.String,java.lang.String)">getType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look up an attribute's type by Namespace-qualified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getURI(int)">getURI</a><wbr/>(int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an attribute's Namespace URI.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(int)">getValue</a><wbr/>(int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an attribute's value by index.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(java.lang.String)">getValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look up an attribute's value by qualified (prefixed) name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(java.lang.String,java.lang.String)">getValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Look up an attribute's value by Namespace-qualified name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAttribute(int)">removeAttribute</a><wbr/>(int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove an attribute from the list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAttribute(int,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">setAttribute</a><wbr/>(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set an attribute in the list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAttributes(org.xml.sax.Attributes)">setAttributes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> atts)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copy an entire Attributes object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLocalName(int,java.lang.String)">setLocalName</a><wbr/>(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the local name of a specific attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setQName(int,java.lang.String)">setQName</a><wbr/>(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the qualified name of a specific attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setType(int,java.lang.String)">setType</a><wbr/>(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the type of a specific attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setURI(int,java.lang.String)">setURI</a><wbr/>(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the Namespace URI of a specific attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(int,java.lang.String)">setValue</a><wbr/>(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the value of a specific attribute.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>Attr</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Attr</span>()</div>
<div class="block">Construct a new, empty AttributesImpl object.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(org.xml.sax.Attributes)">
<h3>Attr</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Attr</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> atts)</span></div>
<div class="block">Copy an existing Attributes object. This constructor is especially useful inside a
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/ContentHandler.html#startElement(java.lang.String,java.lang.String,java.lang.String,org.xml.sax.Attributes)" title="class or interface in org.xml.sax"><code>startElement</code></a> event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>atts</code> - The existing Attributes object.</dd>
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
<section class="detail" id="getLength()">
<h3>getLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLength</span>()</div>
<div class="block">Return the number of attributes in the list.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getLength()" title="class or interface in org.xml.sax">getLength</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
<dt>Returns:</dt>
<dd>The number of attributes in the list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getLength()" title="class or interface in org.xml.sax"><code>Attributes.getLength()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getURI(int)">
<h3>getURI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getURI</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Return an attribute's Namespace URI.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getURI(int)" title="class or interface in org.xml.sax">getURI</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - The attribute's index (zero-based).</dd>
<dt>Returns:</dt>
<dd>The Namespace URI, the empty string if none is available, or null if the index is out of range.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getURI(int)" title="class or interface in org.xml.sax"><code>Attributes.getURI(int)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocalName(int)">
<h3>getLocalName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLocalName</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Return an attribute's local name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getLocalName(int)" title="class or interface in org.xml.sax">getLocalName</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - The attribute's index (zero-based).</dd>
<dt>Returns:</dt>
<dd>The attribute's local name, the empty string if none is available, or null if the index if out of
         range.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getLocalName(int)" title="class or interface in org.xml.sax"><code>Attributes.getLocalName(int)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQName(int)">
<h3>getQName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQName</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Return an attribute's qualified (prefixed) name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getQName(int)" title="class or interface in org.xml.sax">getQName</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - The attribute's index (zero-based).</dd>
<dt>Returns:</dt>
<dd>The attribute's qualified name, the empty string if none is available, or null if the index is out
         of bounds.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getQName(int)" title="class or interface in org.xml.sax"><code>Attributes.getQName(int)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType(int)">
<h3>getType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getType</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Return an attribute's type by index.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getType(int)" title="class or interface in org.xml.sax">getType</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - The attribute's index (zero-based).</dd>
<dt>Returns:</dt>
<dd>The attribute's type, "CDATA" if the type is unknown, or null if the index is out of bounds.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getType(int)" title="class or interface in org.xml.sax"><code>Attributes.getType(int)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(int)">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Return an attribute's value by index.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getValue(int)" title="class or interface in org.xml.sax">getValue</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - The attribute's index (zero-based).</dd>
<dt>Returns:</dt>
<dd>The attribute's value or null if the index is out of bounds.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getValue(int)" title="class or interface in org.xml.sax"><code>Attributes.getValue(int)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIndex(java.lang.String,java.lang.String)">
<h3>getIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIndex</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName)</span></div>
<div class="block">Look up an attribute's index by Namespace name.
 <p>
 In many cases, it will be more efficient to look up the name once and use the index query methods rather
 than using the name query methods repeatedly.
 </p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getIndex(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax">getIndex</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
<dt>Parameters:</dt>
<dd><code>uri</code> - The attribute's Namespace URI, or the empty string if none is available.</dd>
<dd><code>localName</code> - The attribute's local name.</dd>
<dt>Returns:</dt>
<dd>The attribute's index, or -1 if none matches.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getIndex(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax"><code>Attributes.getIndex(java.lang.String,java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIndex(java.lang.String)">
<h3>getIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIndex</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</span></div>
<div class="block">Look up an attribute's index by qualified (prefixed) name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getIndex(java.lang.String)" title="class or interface in org.xml.sax">getIndex</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
<dt>Parameters:</dt>
<dd><code>qName</code> - The qualified name.</dd>
<dt>Returns:</dt>
<dd>The attribute's index, or -1 if none matches.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getIndex(java.lang.String)" title="class or interface in org.xml.sax"><code>Attributes.getIndex(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType(java.lang.String,java.lang.String)">
<h3>getType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName)</span></div>
<div class="block">Look up an attribute's type by Namespace-qualified name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getType(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax">getType</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
<dt>Parameters:</dt>
<dd><code>uri</code> - The Namespace URI, or the empty string for a name with no explicit Namespace URI.</dd>
<dd><code>localName</code> - The local name.</dd>
<dt>Returns:</dt>
<dd>The attribute's type, or null if there is no matching attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getType(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax"><code>Attributes.getType(java.lang.String,java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType(java.lang.String)">
<h3>getType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</span></div>
<div class="block">Look up an attribute's type by qualified (prefixed) name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getType(java.lang.String)" title="class or interface in org.xml.sax">getType</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
<dt>Parameters:</dt>
<dd><code>qName</code> - The qualified name.</dd>
<dt>Returns:</dt>
<dd>The attribute's type, or null if there is no matching attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getType(java.lang.String)" title="class or interface in org.xml.sax"><code>Attributes.getType(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(java.lang.String,java.lang.String)">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName)</span></div>
<div class="block">Look up an attribute's value by Namespace-qualified name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getValue(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax">getValue</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
<dt>Parameters:</dt>
<dd><code>uri</code> - The Namespace URI, or the empty string for a name with no explicit Namespace URI.</dd>
<dd><code>localName</code> - The local name.</dd>
<dt>Returns:</dt>
<dd>The attribute's value, or null if there is no matching attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getValue(java.lang.String,java.lang.String)" title="class or interface in org.xml.sax"><code>Attributes.getValue(java.lang.String,java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(java.lang.String)">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</span></div>
<div class="block">Look up an attribute's value by qualified (prefixed) name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getValue(java.lang.String)" title="class or interface in org.xml.sax">getValue</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></dd>
<dt>Parameters:</dt>
<dd><code>qName</code> - The qualified name.</dd>
<dt>Returns:</dt>
<dd>The attribute's value, or null if there is no matching attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html#getValue(java.lang.String)" title="class or interface in org.xml.sax"><code>Attributes.getValue(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clear()">
<h3>clear</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clear</span>()</div>
<div class="block">Clear the attribute list for reuse. Note that little memory is freed by this call: the current array is kept
 so it can be reused.</div>
</section>
</li>
<li>
<section class="detail" id="setAttributes(org.xml.sax.Attributes)">
<h3>setAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAttributes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> atts)</span></div>
<div class="block">Copy an entire Attributes object. It may be more efficient to reuse an existing object rather than
 constantly allocating new ones.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>atts</code> - The attributes to copy.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAttribute(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>addAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAttribute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Add an attribute to the end of the list. For the sake of speed, this method does no checking to see if the
 attribute is already in the list: that is the responsibility of the application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - The Namespace URI, or the empty string if none is available or Namespace processing is not being
           performed.</dd>
<dd><code>localName</code> - The local name, or the empty string if Namespace processing is not being performed.</dd>
<dd><code>qName</code> - The qualified (prefixed) name, or the empty string if qualified names are not available.</dd>
<dd><code>type</code> - The attribute type as a string.</dd>
<dd><code>value</code> - The attribute value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAttribute(int,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>setAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAttribute</span><wbr/><span class="parameters">(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Set an attribute in the list. For the sake of speed, this method does no checking for name conflicts or
 well-formedness: such checks are the responsibility of the application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - The index of the attribute (zero-based).</dd>
<dd><code>uri</code> - The Namespace URI, or the empty string if none is available or Namespace processing is not being
           performed.</dd>
<dd><code>localName</code> - The local name, or the empty string if Namespace processing is not being performed.</dd>
<dd><code>qName</code> - The qualified name, or the empty string if qualified names are not available.</dd>
<dd><code>type</code> - The attribute type as a string.</dd>
<dd><code>value</code> - The attribute value.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html" title="class or interface in java.lang">ArrayIndexOutOfBoundsException</a></code> - When the supplied index does not point to an attribute
               in the list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAttribute(int)">
<h3>removeAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAttribute</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Remove an attribute from the list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - The index of the attribute (zero-based).</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html" title="class or interface in java.lang">ArrayIndexOutOfBoundsException</a></code> - When the supplied index does not point to an attribute
               in the list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setURI(int,java.lang.String)">
<h3>setURI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setURI</span><wbr/><span class="parameters">(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri)</span></div>
<div class="block">Set the Namespace URI of a specific attribute.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - The index of the attribute (zero-based).</dd>
<dd><code>uri</code> - The attribute's Namespace URI, or the empty string for none.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html" title="class or interface in java.lang">ArrayIndexOutOfBoundsException</a></code> - When the supplied index does not point to an attribute
               in the list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLocalName(int,java.lang.String)">
<h3>setLocalName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLocalName</span><wbr/><span class="parameters">(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName)</span></div>
<div class="block">Set the local name of a specific attribute.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - The index of the attribute (zero-based).</dd>
<dd><code>localName</code> - The attribute's local name, or the empty string for none.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html" title="class or interface in java.lang">ArrayIndexOutOfBoundsException</a></code> - When the supplied index does not point to an attribute
               in the list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setQName(int,java.lang.String)">
<h3>setQName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setQName</span><wbr/><span class="parameters">(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</span></div>
<div class="block">Set the qualified name of a specific attribute.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - The index of the attribute (zero-based).</dd>
<dd><code>qName</code> - The attribute's qualified name, or the empty string for none.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html" title="class or interface in java.lang">ArrayIndexOutOfBoundsException</a></code> - When the supplied index does not point to an attribute
               in the list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setType(int,java.lang.String)">
<h3>setType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setType</span><wbr/><span class="parameters">(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Set the type of a specific attribute.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - The index of the attribute (zero-based).</dd>
<dd><code>type</code> - The attribute's type.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html" title="class or interface in java.lang">ArrayIndexOutOfBoundsException</a></code> - When the supplied index does not point to an attribute
               in the list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(int,java.lang.String)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Set the value of a specific attribute.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - The index of the attribute (zero-based).</dd>
<dd><code>value</code> - The attribute's value.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ArrayIndexOutOfBoundsException.html" title="class or interface in java.lang">ArrayIndexOutOfBoundsException</a></code> - When the supplied index does not point to an attribute
               in the list.</dd>
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
