# JAVA OPENAPI: AutomatonMacroAPI (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/automaton/AutomatonMacroAPI.html
- source_path: `com/nomagic/magicdraw/automaton/AutomatonMacroAPI.html`
- source_sha256: `9a3664b4b41d91623f695a91f042a40eab6c6d97a7754a1a972f9ff1466acf50`
- captured_utc: `2026-07-14T16:55:04.084882+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.automaton](package-summary.html)

## Class AutomatonMacroAPI

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.automaton.AutomatonMacroAPI

@OpenApiAllpublic classAutomatonMacroAPI
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The Class AutomatonMacroAPI. API to be called by script. WARNNING: Class signature shouldn't be changed. Some method
 signature souldn't be changed. It will impact ByteCode generation.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[METHOD_NAME_GET_PROP_VALUE](#METHOD_NAME_GET_PROP_VALUE)`
The Constant METHOD_NAME_GET_PROP_VALUE.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[METHOD_NAME_SET_PROP_VALUE](#METHOD_NAME_SET_PROP_VALUE)`
The Constant METHOD_NAME_SET_PROP_VALUE.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AutomatonMacroAPI](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[addStereotype](#addStereotype(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,com.nomagic.magicdraw.automaton.AutomatonOpaqueObject))(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoStereotype)`
Adds the stereotype.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[addStereotypeByStereotypeName](#addStereotypeByStereotypeName(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String))(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)`
Adds the stereotype by stereotype name.
`protected static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[convertGettingValue](#convertGettingValue(java.lang.Object,com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String,java.lang.String,boolean))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) result,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifierPath,
 boolean needCommitted)`
Convert element to opaque.
`protected static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[convertSettingValue](#convertSettingValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Convert opaque to element value.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[createElement](#createElement(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) metaName)`
Creates the new dsl element.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[createRelationship](#createRelationship(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String))(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject source,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject target,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) relationName)`
Creates the relationship.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getModelData](#getModelData())()`
Gets the model data.
`static com.nomagic.magicdraw.automaton.AutomatonOpaqueObject`
`[getOpaqueMetaClass](#getOpaqueMetaClass(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`

`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getOpaqueObject](#getOpaqueObject(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Gets the opaque object.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getOpaqueObjectByPath](#getOpaqueObjectByPath(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementPath)`
New dsl instance.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getPropertyValue](#getPropertyValue(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String,java.lang.String))(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifierPath)`
Gets the property value.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getPropertyValue](#getPropertyValue(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String,java.lang.String,boolean))(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifierPath,
 boolean withException)`

`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getSelectedElementFromContainmentTree](#getSelectedElementFromContainmentTree())()`
Gets the selection model.
`static void`
`[printElementDetail](#printElementDetail(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eObj)`
Prints the element detail.
`static void`
`[removeElement](#removeElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`
Removes the element.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[removeStereotype](#removeStereotype(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,com.nomagic.magicdraw.automaton.AutomatonOpaqueObject))(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoStereotype)`
Removes the stereotype.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[removeStereotypeByStereotypeName](#removeStereotypeByStereotypeName(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String))(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)`
Removes the stereotype by stereotype name.
`static void`
`[setPropertyValue](#setPropertyValue(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String,java.lang.String,java.lang.Object))(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifierPath,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets the property value.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
METHOD_NAME_GET_PROP_VALUE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) METHOD_NAME_GET_PROP_VALUE
The Constant METHOD_NAME_GET_PROP_VALUE.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.automaton.AutomatonMacroAPI.METHOD_NAME_GET_PROP_VALUE)
METHOD_NAME_SET_PROP_VALUE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) METHOD_NAME_SET_PROP_VALUE
The Constant METHOD_NAME_SET_PROP_VALUE.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.automaton.AutomatonMacroAPI.METHOD_NAME_SET_PROP_VALUE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AutomatonMacroAPI
public AutomatonMacroAPI()
 ============ METHOD DETAIL ========== 
Method Details
createElement
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) createElement([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) metaName)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Creates the new dsl element. (User script API)
Parameters:
`metaName` - the dsl meta name
Returns:
the object
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - the exception throws when cannot create Element with meta-class names **metaName**
createRelationship
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) createRelationship(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject source,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject target,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) relationName)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Creates the relationship. (User script API)
Parameters:
`source` - the source
`target` - the target
`relationName` - the relation name
Returns:
opaque object of relation element
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - the exception throws when not found a relation for **relationName**
getOpaqueObjectByPath
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getOpaqueObjectByPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementPath)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
New dsl instance. (User script API)
Parameters:
`elementPath` - the element path
Returns:
the object
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - the exception throws when not found an element for path **elementPath**
getOpaqueObject
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getOpaqueObject([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Gets the opaque object.
Parameters:
`element` - the element
Returns:
the opaque object
getPropertyValue
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getPropertyValue(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifierPath)
Gets the property value. (User script API) WARNNING: Do not change this method signature. It will impact ByteCode
 generation
Parameters:
`macroObj` - the macroObj
`name` - the name
`qualifierPath` - the qualifierPath
Returns:
the property value
getPropertyValue
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getPropertyValue(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifierPath,
 boolean withException)
setPropertyValue
public static void setPropertyValue(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifierPath,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Sets the property value. (User script API) WARNNING: Do not change this method signature. It will impact ByteCode
 generation
Parameters:
`macroObject` - the macroObject
`name` - the name
`qualifierPath` - the qualifierPath
`value` - the value
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - the exception throws when cannot set the property value
getOpaqueMetaClass
public static com.nomagic.magicdraw.automaton.AutomatonOpaqueObject getOpaqueMetaClass([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
removeElement
public static void removeElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
 throws jakarta.activation.UnsupportedDataTypeException,
[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Removes the element. (User script API)
Parameters:
`obj` - the obj
Throws:
`jakarta.activation.UnsupportedDataTypeException` - the unsupported data type exception
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - the exception throws when not found the element
addStereotype
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) addStereotype(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoStereotype)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Adds the stereotype. (User script API)
Parameters:
`marcoElement` - the element
`marcoStereotype` - the stereotype
Returns:
a new opaque object which contains getters and setters with regards to the applied stereotype's
 properties.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - the exception throws when marcoStereotype is not a stereotype
addStereotypeByStereotypeName
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) addStereotypeByStereotypeName(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Adds the stereotype by stereotype name. (User script API)
Parameters:
`marcoElement` - the marco element
`stereotypeName` - the stereotype name
Returns:
the object
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - the exception throws when not found a stereotype for stereotypeName
removeStereotype
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) removeStereotype(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoStereotype)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Removes the stereotype. (User script API)
Parameters:
`marcoElement` - the o element
`marcoStereotype` - the o stereotype
Returns:
the object
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - the exception throws when marcoStereotype is not a stereotype or element doesn't contain the
 stereotype
removeStereotypeByStereotypeName
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) removeStereotypeByStereotypeName(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Removes the stereotype by stereotype name. (User script API)
Parameters:
`marcoElement` - the marco element
`stereotypeName` - the stereotype name
Returns:
the object
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - the exception throws when marcoStereotype is not a stereotype or element doesn't contain the
 stereotypeName
getSelectedElementFromContainmentTree
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getSelectedElementFromContainmentTree()
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Gets the selection model. (User script API)
Returns:
the selection model
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - the exception
getModelData
public static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getModelData()
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Gets the model data. (User script API)
Returns:
the model data
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - the exception
printElementDetail
public static void printElementDetail([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eObj)
 throws jakarta.activation.UnsupportedDataTypeException
Prints the element detail. (User script API)
Parameters:
`eObj` - the element
Throws:
`jakarta.activation.UnsupportedDataTypeException` - the unsupported data type exception
convertSettingValue
protected static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) convertSettingValue([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Convert opaque to element value.
Parameters:
`value` - the value
Returns:
the object
convertGettingValue
protected static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) convertGettingValue([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) result,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObj,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifierPath,
 boolean needCommitted)
Convert element to opaque.
Parameters:
`result` - the result
Returns:
the object

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.automaton</a></div>
<h1 class="title" title="Class AutomatonMacroAPI">Class AutomatonMacroAPI</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.automaton.AutomatonMacroAPI</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">AutomatonMacroAPI</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The Class AutomatonMacroAPI. API to be called by script. WARNNING: Class signature shouldn't be changed. Some method
 signature souldn't be changed. It will impact ByteCode generation.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#METHOD_NAME_GET_PROP_VALUE">METHOD_NAME_GET_PROP_VALUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The Constant METHOD_NAME_GET_PROP_VALUE.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#METHOD_NAME_SET_PROP_VALUE">METHOD_NAME_SET_PROP_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The Constant METHOD_NAME_SET_PROP_VALUE.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AutomatonMacroAPI</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addStereotype(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,com.nomagic.magicdraw.automaton.AutomatonOpaqueObject)">addStereotype</a><wbr/>(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoStereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds the stereotype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addStereotypeByStereotypeName(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String)">addStereotypeByStereotypeName</a><wbr/>(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds the stereotype by stereotype name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#convertGettingValue(java.lang.Object,com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String,java.lang.String,boolean)">convertGettingValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> result,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifierPath,
 boolean needCommitted)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert element to opaque.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#convertSettingValue(java.lang.Object)">convertSettingValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert opaque to element value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createElement(java.lang.String)">createElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> metaName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates the new dsl element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createRelationship(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String)">createRelationship</a><wbr/>(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject source,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> relationName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates the relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelData()">getModelData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the model data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.automaton.AutomatonOpaqueObject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOpaqueMetaClass(java.lang.String)">getOpaqueMetaClass</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOpaqueObject(java.lang.Object)">getOpaqueObject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the opaque object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOpaqueObjectByPath(java.lang.String)">getOpaqueObjectByPath</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementPath)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">New dsl instance.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyValue(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String,java.lang.String)">getPropertyValue</a><wbr/>(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifierPath)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyValue(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String,java.lang.String,boolean)">getPropertyValue</a><wbr/>(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifierPath,
 boolean withException)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedElementFromContainmentTree()">getSelectedElementFromContainmentTree</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the selection model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#printElementDetail(java.lang.Object)">printElementDetail</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eObj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Prints the element detail.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeElement(java.lang.Object)">removeElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeStereotype(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,com.nomagic.magicdraw.automaton.AutomatonOpaqueObject)">removeStereotype</a><wbr/>(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoStereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes the stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeStereotypeByStereotypeName(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String)">removeStereotypeByStereotypeName</a><wbr/>(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes the stereotype by stereotype name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setPropertyValue(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String,java.lang.String,java.lang.Object)">setPropertyValue</a><wbr/>(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifierPath,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the property value.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="METHOD_NAME_GET_PROP_VALUE">
<h3>METHOD_NAME_GET_PROP_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">METHOD_NAME_GET_PROP_VALUE</span></div>
<div class="block">The Constant METHOD_NAME_GET_PROP_VALUE.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.automaton.AutomatonMacroAPI.METHOD_NAME_GET_PROP_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="METHOD_NAME_SET_PROP_VALUE">
<h3>METHOD_NAME_SET_PROP_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">METHOD_NAME_SET_PROP_VALUE</span></div>
<div class="block">The Constant METHOD_NAME_SET_PROP_VALUE.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.automaton.AutomatonMacroAPI.METHOD_NAME_SET_PROP_VALUE">Constant Field Values</a></li>
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
<h3>AutomatonMacroAPI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AutomatonMacroAPI</span>()</div>
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
<section class="detail" id="createElement(java.lang.String)">
<h3>createElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">createElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> metaName)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Creates the new dsl element. (User script API)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metaName</code> - the dsl meta name</dd>
<dt>Returns:</dt>
<dd>the object</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - the exception throws when cannot create Element with meta-class names <b>metaName</b></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRelationship(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String)">
<h3>createRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">createRelationship</span><wbr/><span class="parameters">(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject source,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> relationName)</span>
                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Creates the relationship. (User script API)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - the source</dd>
<dd><code>target</code> - the target</dd>
<dd><code>relationName</code> - the relation name</dd>
<dt>Returns:</dt>
<dd>opaque object of relation element</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - the exception throws when not found a relation for <b>relationName</b></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpaqueObjectByPath(java.lang.String)">
<h3>getOpaqueObjectByPath</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getOpaqueObjectByPath</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementPath)</span>
                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">New dsl instance. (User script API)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementPath</code> - the element path</dd>
<dt>Returns:</dt>
<dd>the object</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - the exception throws when not found an element for path <b>elementPath</b></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpaqueObject(java.lang.Object)">
<h3>getOpaqueObject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getOpaqueObject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Gets the opaque object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>the opaque object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyValue(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String,java.lang.String)">
<h3>getPropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getPropertyValue</span><wbr/><span class="parameters">(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifierPath)</span></div>
<div class="block">Gets the property value. (User script API) WARNNING: Do not change this method signature. It will impact ByteCode
 generation</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>macroObj</code> - the macroObj</dd>
<dd><code>name</code> - the name</dd>
<dd><code>qualifierPath</code> - the qualifierPath</dd>
<dt>Returns:</dt>
<dd>the property value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyValue(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String,java.lang.String,boolean)">
<h3>getPropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getPropertyValue</span><wbr/><span class="parameters">(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifierPath,
 boolean withException)</span></div>
</section>
</li>
<li>
<section class="detail" id="setPropertyValue(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String,java.lang.String,java.lang.Object)">
<h3>setPropertyValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setPropertyValue</span><wbr/><span class="parameters">(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifierPath,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Sets the property value. (User script API) WARNNING: Do not change this method signature. It will impact ByteCode
 generation</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>macroObject</code> - the macroObject</dd>
<dd><code>name</code> - the name</dd>
<dd><code>qualifierPath</code> - the qualifierPath</dd>
<dd><code>value</code> - the value</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - the exception throws when cannot set the property value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpaqueMetaClass(java.lang.String)">
<h3>getOpaqueMetaClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.automaton.AutomatonOpaqueObject</span> <span class="element-name">getOpaqueMetaClass</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeElement(java.lang.Object)">
<h3>removeElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span>
                          throws <span class="exceptions">jakarta.activation.UnsupportedDataTypeException,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Removes the element. (User script API)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - the obj</dd>
<dt>Throws:</dt>
<dd><code>jakarta.activation.UnsupportedDataTypeException</code> - the unsupported data type exception</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - the exception throws when not found the element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addStereotype(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,com.nomagic.magicdraw.automaton.AutomatonOpaqueObject)">
<h3>addStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">addStereotype</span><wbr/><span class="parameters">(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoStereotype)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Adds the stereotype. (User script API)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>marcoElement</code> - the element</dd>
<dd><code>marcoStereotype</code> - the stereotype</dd>
<dt>Returns:</dt>
<dd>a new opaque object which contains getters and setters with regards to the applied stereotype's
         properties.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - the exception throws when marcoStereotype is not a stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addStereotypeByStereotypeName(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String)">
<h3>addStereotypeByStereotypeName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">addStereotypeByStereotypeName</span><wbr/><span class="parameters">(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</span>
                                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Adds the stereotype by stereotype name. (User script API)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>marcoElement</code> - the marco element</dd>
<dd><code>stereotypeName</code> - the stereotype name</dd>
<dt>Returns:</dt>
<dd>the object</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - the exception throws when not found a stereotype for stereotypeName</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeStereotype(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,com.nomagic.magicdraw.automaton.AutomatonOpaqueObject)">
<h3>removeStereotype</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">removeStereotype</span><wbr/><span class="parameters">(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoStereotype)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Removes the stereotype. (User script API)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>marcoElement</code> - the o element</dd>
<dd><code>marcoStereotype</code> - the o stereotype</dd>
<dt>Returns:</dt>
<dd>the object</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - the exception throws when marcoStereotype is not a stereotype or element doesn't contain the
             stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeStereotypeByStereotypeName(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String)">
<h3>removeStereotypeByStereotypeName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">removeStereotypeByStereotypeName</span><wbr/><span class="parameters">(com.nomagic.magicdraw.automaton.AutomatonOpaqueObject marcoElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</span>
                                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Removes the stereotype by stereotype name. (User script API)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>marcoElement</code> - the marco element</dd>
<dd><code>stereotypeName</code> - the stereotype name</dd>
<dt>Returns:</dt>
<dd>the object</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - the exception throws when marcoStereotype is not a stereotype or element doesn't contain the
             stereotypeName</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedElementFromContainmentTree()">
<h3>getSelectedElementFromContainmentTree</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getSelectedElementFromContainmentTree</span>()
                                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Gets the selection model. (User script API)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the selection model</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - the exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModelData()">
<h3>getModelData</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getModelData</span>()
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Gets the model data. (User script API)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the model data</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - the exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="printElementDetail(java.lang.Object)">
<h3>printElementDetail</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">printElementDetail</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eObj)</span>
                               throws <span class="exceptions">jakarta.activation.UnsupportedDataTypeException</span></div>
<div class="block">Prints the element detail. (User script API)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eObj</code> - the element</dd>
<dt>Throws:</dt>
<dd><code>jakarta.activation.UnsupportedDataTypeException</code> - the unsupported data type exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convertSettingValue(java.lang.Object)">
<h3>convertSettingValue</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">convertSettingValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Convert opaque to element value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the value</dd>
<dt>Returns:</dt>
<dd>the object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convertGettingValue(java.lang.Object,com.nomagic.magicdraw.automaton.AutomatonOpaqueObject,java.lang.String,java.lang.String,boolean)">
<h3>convertGettingValue</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">convertGettingValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> result,
 com.nomagic.magicdraw.automaton.AutomatonOpaqueObject macroObj,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifierPath,
 boolean needCommitted)</span></div>
<div class="block">Convert element to opaque.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>result</code> - the result</dd>
<dt>Returns:</dt>
<dd>the object</dd>
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
