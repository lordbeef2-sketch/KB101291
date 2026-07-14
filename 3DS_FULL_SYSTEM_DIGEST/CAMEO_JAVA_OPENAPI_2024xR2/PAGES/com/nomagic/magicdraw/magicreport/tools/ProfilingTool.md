# JAVA OPENAPI: ProfilingTool (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/magicreport/tools/ProfilingTool.html
- source_path: `com/nomagic/magicdraw/magicreport/tools/ProfilingTool.html`
- source_sha256: `02a6926cf7ae73d144e2e3b806ede68967d9ac257561a240b3626e1f61a31573`
- captured_utc: `2026-07-14T16:55:27.845152+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.magicreport.tools](package-summary.html)

## Class ProfilingTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html)
com.nomagic.magicreport.engine.Tool
com.nomagic.magicdraw.magicreport.tools.ProfilingTool

All Implemented Interfaces:
`com.nomagic.magicreport.engine.ITool`, `com.nomagic.magicreport.IVariable`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classProfilingTool
extends com.nomagic.magicreport.engine.Tool

Contains utilities functions for profiling MagicDraw meta-model. Context name of this class is "profiling".

Since:
November 27, 2007
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.tools.ProfilingTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.ITool
`com.nomagic.magicreport.engine.ITool.HTMLString, com.nomagic.magicreport.engine.ITool.RetainedString, com.nomagic.magicreport.engine.ITool.Void`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CONTEXT_NAME](#CONTEXT_NAME)`
Contains a context name.
Fields inherited from class com.nomagic.magicreport.engine.Tool
`context, properties`
Fields inherited from interface com.nomagic.magicreport.engine.ITool
`VOID`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProfilingTool](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDeclaringElementName](#getDeclaringElementName(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) modelName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Retrieve the name of meta-model which property name is declared.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getElementProperties](#getElementProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return Collection of element properties name.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getElementProperties](#getElementProperties(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) modelName)`
Retrieve Collection of element properties name from meta-model name.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getElementProperty](#getElementProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Retrieve property value of specified element and property name.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getGeneralizationName](#getGeneralizationName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) modelName)`
Return generalization model of modelName.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHumanPropertyName](#getHumanPropertyName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Return text representing property name.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPropertyTypeName](#getPropertyTypeName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Retrieve type of property.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPropertyTypeName](#getPropertyTypeName(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) modelName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)`
Retrieve type of property.
Methods inherited from class com.nomagic.magicreport.engine.Tool
`clone, getContext, getProperties, getProperty, getProperty, notifyObservers, setContext, setProperties`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.ITool
`clearTool`

============ FIELD DETAIL =========== 
Field Details
CONTEXT_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CONTEXT_NAME
Contains a context name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.tools.ProfilingTool.CONTEXT_NAME)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProfilingTool
public ProfilingTool()
 ============ METHOD DETAIL ========== 
Method Details
getGeneralizationName
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getGeneralizationName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) modelName)
Return generalization model of modelName.
Parameters:
`modelName` - meta-model name
Returns:
generalization model
getDeclaringElementName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDeclaringElementName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) modelName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Retrieve the name of meta-model which property name is declared.
Parameters:
`modelName` - meta-model name
`propertyName` - property name
Returns:
name of meta-model
getPropertyTypeName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPropertyTypeName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) modelName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Retrieve type of property.
Parameters:
`modelName` - meta-model name
`propertyName` - property name
Returns:
name of property type
getPropertyTypeName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPropertyTypeName([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Retrieve type of property.
Parameters:
`element` - target element
`propertyName` - property name
Returns:
name of property type
getElementProperties
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getElementProperties([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) modelName)
Retrieve Collection of element properties name from meta-model name.
Parameters:
`modelName` - meta-model name
Returns:
collection of element properties
getElementProperties
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getElementProperties([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return Collection of element properties name.
Parameters:
`element` - target element
Returns:
collection of element properties
getElementProperty
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getElementProperty([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Retrieve property value of specified element and property name.
Parameters:
`element` - target element
`propertyName` - property name
Returns:
an Object of element property name.
getHumanPropertyName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHumanPropertyName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName)
Return text representing property name.
Parameters:
`propertyName` - property name
Returns:
a human name of given `propertyName`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.magicreport.tools</a></div>
<h1 class="title" title="Class ProfilingTool">Class ProfilingTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance">com.nomagic.magicreport.engine.Tool
<div class="inheritance">com.nomagic.magicdraw.magicreport.tools.ProfilingTool</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicreport.engine.ITool</code>, <code>com.nomagic.magicreport.IVariable</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProfilingTool</span>
<span class="extends-implements">extends com.nomagic.magicreport.engine.Tool</span></div>
<div class="block">Contains utilities functions for profiling MagicDraw meta-model. Context name of this class is "profiling".</div>
<dl class="notes">
<dt>Since:</dt>
<dd>November 27, 2007</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.tools.ProfilingTool">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.ITool</h2>
<code>com.nomagic.magicreport.engine.ITool.HTMLString, com.nomagic.magicreport.engine.ITool.RetainedString, com.nomagic.magicreport.engine.ITool.Void</code></div>
</section>
</li>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONTEXT_NAME">CONTEXT_NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">Contains a context name.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.Tool</h3>
<code>context, properties</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.ITool</h3>
<code>VOID</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProfilingTool</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDeclaringElementName(java.lang.String,java.lang.String)">getDeclaringElementName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> modelName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieve the name of meta-model which property name is declared.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getElementProperties</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return Collection of element properties name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementProperties(java.lang.String)">getElementProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> modelName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieve Collection of element properties name from meta-model name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getElementProperty</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieve property value of specified element and property name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeneralizationName(java.lang.String)">getGeneralizationName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> modelName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return generalization model of modelName.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHumanPropertyName(java.lang.String)">getHumanPropertyName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return text representing property name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyTypeName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getPropertyTypeName</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieve type of property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyTypeName(java.lang.String,java.lang.String)">getPropertyTypeName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> modelName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieve type of property.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.Tool</h3>
<code>clone, getContext, getProperties, getProperty, getProperty, notifyObservers, setContext, setProperties</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.ITool</h3>
<code>clearTool</code></div>
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
<section class="detail" id="CONTEXT_NAME">
<h3>CONTEXT_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONTEXT_NAME</span></div>
<div class="block">Contains a context name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.tools.ProfilingTool.CONTEXT_NAME">Constant Field Values</a></li>
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
<h3>ProfilingTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProfilingTool</span>()</div>
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
<section class="detail" id="getGeneralizationName(java.lang.String)">
<h3>getGeneralizationName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getGeneralizationName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> modelName)</span></div>
<div class="block">Return generalization model of modelName.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modelName</code> - meta-model name</dd>
<dt>Returns:</dt>
<dd>generalization model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeclaringElementName(java.lang.String,java.lang.String)">
<h3>getDeclaringElementName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDeclaringElementName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> modelName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Retrieve the name of meta-model which property name is declared.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modelName</code> - meta-model name</dd>
<dd><code>propertyName</code> - property name</dd>
<dt>Returns:</dt>
<dd>name of meta-model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyTypeName(java.lang.String,java.lang.String)">
<h3>getPropertyTypeName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPropertyTypeName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> modelName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Retrieve type of property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modelName</code> - meta-model name</dd>
<dd><code>propertyName</code> - property name</dd>
<dt>Returns:</dt>
<dd>name of property type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyTypeName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getPropertyTypeName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPropertyTypeName</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Retrieve type of property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - target element</dd>
<dd><code>propertyName</code> - property name</dd>
<dt>Returns:</dt>
<dd>name of property type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementProperties(java.lang.String)">
<h3>getElementProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getElementProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> modelName)</span></div>
<div class="block">Retrieve Collection of element properties name from meta-model name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>modelName</code> - meta-model name</dd>
<dt>Returns:</dt>
<dd>collection of element properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getElementProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getElementProperties</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return Collection of element properties name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - target element</dd>
<dt>Returns:</dt>
<dd>collection of element properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getElementProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getElementProperty</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Retrieve property value of specified element and property name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - target element</dd>
<dd><code>propertyName</code> - property name</dd>
<dt>Returns:</dt>
<dd>an Object of element property name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHumanPropertyName(java.lang.String)">
<h3>getHumanPropertyName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanPropertyName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Return text representing property name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyName</code> - property name</dd>
<dt>Returns:</dt>
<dd>a human name of given <code>propertyName</code></dd>
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
