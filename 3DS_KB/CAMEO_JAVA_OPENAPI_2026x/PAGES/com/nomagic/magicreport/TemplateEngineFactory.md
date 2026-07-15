# JAVA OPENAPI: TemplateEngineFactory (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/TemplateEngineFactory.html
- source_path: `com/nomagic/magicreport/TemplateEngineFactory.html`
- source_sha256: `67a14132dec334f0aa14103318ecc0df36edf4917d94964426e8971bfb83f0b7`
- captured_utc: `2026-07-14T16:58:36.053270+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport](package-summary.html)

## Class TemplateEngineFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.TemplateEngineFactory

@OpenApiAllpublic final classTemplateEngineFactory
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

This is the factory for template engine. It is the single access point for all functionality. It applied the
 singleton pattern.

Since:
Jun 12, 2007 12:23:05 AM
Version:
1.0 Jun 12, 2007

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[copy](#copy(com.nomagic.magicreport.engine.ITemplateEngine,com.nomagic.magicreport.engine.ITemplateEngine))([ITemplateEngine](engine/ITemplateEngine.html) dest,
 [ITemplateEngine](engine/ITemplateEngine.html) source)`
Copies all properties and context from source engine to destination engine.
`void`
`[copy](#copy(com.nomagic.magicreport.engine.ITemplateEngine,com.nomagic.magicreport.engine.ITemplateEngine,boolean,boolean))([ITemplateEngine](engine/ITemplateEngine.html) dest,
 [ITemplateEngine](engine/ITemplateEngine.html) source,
 boolean copyRuntimeInstance,
 boolean copyFormatterRuntimeInstance)`
Copies all properties and context from source engine to destination engine.
`[ITemplateEngine](engine/ITemplateEngine.html)`
`[createTemplateEngine](#createTemplateEngine(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [ITemplateEngine](engine/ITemplateEngine.html)> clazz)`
Create a new instance of template engine associated with given class.
`[ITemplateEngine](engine/ITemplateEngine.html)`
`[createTemplateEngine](#createTemplateEngine(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)`
Create a new instance of template engine associated with given type.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDefaultTemplateEngineClassName](#getDefaultTemplateEngineClassName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) engineName)`
Return default template engine class name.
`static [TemplateEngineFactory](TemplateEngineFactory.html)`
`[getInstance](#getInstance())()`
Return instance of this class.
`[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [ITemplateEngine](engine/ITemplateEngine.html)>`
`[getRegisterTemplateEngine](#getRegisterTemplateEngine(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension)`
Return a registered template engine class.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[]`
`[getTemplateAliasNames](#getTemplateAliasNames())()`
Return an array of the alias names of default template engine.
`[ITemplateEngine](engine/ITemplateEngine.html)`
`[getTemplateEngine](#getTemplateEngine(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [ITemplateEngine](engine/ITemplateEngine.html)> clazz)`
Return template engine associated with given class or create a new instance if it doesn't created.
`[ITemplateEngine](engine/ITemplateEngine.html)`
`[getTemplateEngine](#getTemplateEngine(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)`
Return template engine associated with given type or create a new instance if it doesn't created.
`[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [ITemplateEngine](engine/ITemplateEngine.html)>`
`[getTemplateEngineClass](#getTemplateEngineClass(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)`
Return class of template engine associated with given type.
`void`
`[registerTemplateEngine](#registerTemplateEngine(java.lang.String,java.lang.Class))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [ITemplateEngine](engine/ITemplateEngine.html)> templateEngineClass)`
Registers the given class name with the [`TemplateEngineFactory`](TemplateEngineFactory.html).
`void`
`[unregisterTemplateEngine](#unregisterTemplateEngine(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension)`
Unregister the given file extension.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
public static [TemplateEngineFactory](TemplateEngineFactory.html) getInstance()
Return instance of this class.
Returns:
instance of this class.
getDefaultTemplateEngineClassName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDefaultTemplateEngineClassName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) engineName)
Return default template engine class name.
Parameters:
`engineName` - name.
Returns:
default template engine class name.
getTemplateAliasNames
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] getTemplateAliasNames()
Return an array of the alias names of default template engine.
 `String[] aliasNames = TemplateEngineFactory.getInstance().getTemplateAliasNames();`
Returns:
an array of the alias names and description
registerTemplateEngine
public void registerTemplateEngine([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [ITemplateEngine](engine/ITemplateEngine.html)> templateEngineClass)
Registers the given class name with the [`TemplateEngineFactory`](TemplateEngineFactory.html). A newly-loaded engine class should
 call the method registerTemplateEngine to make itself known to the TemplateEngineFactory.
Parameters:
`extension` - template file extension
`templateEngineClass` - the new [`ITemplateEngine`](engine/ITemplateEngine.html) that is to be registered with the
 [`TemplateEngineFactory`](TemplateEngineFactory.html)
unregisterTemplateEngine
public void unregisterTemplateEngine([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension)
Unregister the given file extension.
Parameters:
`extension` - file extension.
getRegisterTemplateEngine
public [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [ITemplateEngine](engine/ITemplateEngine.html)> getRegisterTemplateEngine([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension)
Return a registered template engine class.
Parameters:
`extension` - template file extension
Returns:
a template engine class [`ITemplateEngine`](engine/ITemplateEngine.html)
getTemplateEngine
public [ITemplateEngine](engine/ITemplateEngine.html) getTemplateEngine([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [ITemplateEngine](engine/ITemplateEngine.html)> clazz)
 throws [InitializationEngineException](InitializationEngineException.html)
Return template engine associated with given class or create a new instance if it doesn't created.
Parameters:
`clazz` - associated class for template engine.
Returns:
template engine
Throws:
`[InitializationEngineException](InitializationEngineException.html)` - error while creating template engine.
getTemplateEngine
public [ITemplateEngine](engine/ITemplateEngine.html) getTemplateEngine([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)
 throws [InitializationEngineException](InitializationEngineException.html)
Return template engine associated with given type or create a new instance if it doesn't created. If no
 associated type found, text engine [`TextEngine`](engine/velocity/TextEngine.html) will be return
 as default engine.
Parameters:
`type` - engine type.
Returns:
template engine
Throws:
`[InitializationEngineException](InitializationEngineException.html)` - error while creating template engine.
getTemplateEngineClass
public [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [ITemplateEngine](engine/ITemplateEngine.html)> getTemplateEngineClass([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)
Return class of template engine associated with given type. If no associated type found, text engine
 [`TextEngine`](engine/velocity/TextEngine.html) will be return as default engine.
Parameters:
`type` - engine type.
Returns:
template engine class
createTemplateEngine
public [ITemplateEngine](engine/ITemplateEngine.html) createTemplateEngine([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)
 throws [InitializationEngineException](InitializationEngineException.html)
Create a new instance of template engine associated with given type. If no associated type found, text
 engine [`TextEngine`](engine/velocity/TextEngine.html) will be return as default engine.
 This method always return new instance.
Parameters:
`type` - engine type.
Returns:
template engine
Throws:
`[InitializationEngineException](InitializationEngineException.html)` - error while creating template engine.
createTemplateEngine
public [ITemplateEngine](engine/ITemplateEngine.html) createTemplateEngine([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [ITemplateEngine](engine/ITemplateEngine.html)> clazz)
 throws [InitializationEngineException](InitializationEngineException.html)
Create a new instance of template engine associated with given class.
 This method always return new instance.
Parameters:
`clazz` - engine Class.
Returns:
template engine
Throws:
`[InitializationEngineException](InitializationEngineException.html)` - error while creating template engine.
copy
public void copy([ITemplateEngine](engine/ITemplateEngine.html) dest,
 [ITemplateEngine](engine/ITemplateEngine.html) source)
Copies all properties and context from source engine to destination engine.
 This method will perform shallow copy of context. The reference to context of new engine will not remain the
 same as source engine. In order to copy, all object inside context requires implement clone() method.
Parameters:
`dest` - the destination engine.
`source` - source engine.
copy
public void copy([ITemplateEngine](engine/ITemplateEngine.html) dest,
 [ITemplateEngine](engine/ITemplateEngine.html) source,
 boolean copyRuntimeInstance,
 boolean copyFormatterRuntimeInstance)
Copies all properties and context from source engine to destination engine.
 This method will perform shallow copy of context. The reference to context of new engine will not remain the
 same as source engine. In order to copy, all object inside context requires implement clone() method.
Parameters:
`dest` - the destination engine.
`source` - source engine.
`copyRuntimeInstance` - true to copy RuntimeInstance of source to destination engine if both are instance of IRuntimeInstanceVelocityEngine
`copyFormatterRuntimeInstance` - true to copy Formatter of source to destination engine if both are instance of DefaultTemplateEngine

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport</a></div>
<h1 class="title" title="Class TemplateEngineFactory">Class TemplateEngineFactory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.TemplateEngineFactory</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">TemplateEngineFactory</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">This is the factory for template engine. It is the single access point for all functionality. It applied the
 singleton pattern.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 12, 2007 12:23:05 AM</dd>
<dt>Version:</dt>
<dd>1.0 Jun 12, 2007</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(com.nomagic.magicreport.engine.ITemplateEngine,com.nomagic.magicreport.engine.ITemplateEngine)">copy</a><wbr/>(<a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> dest,
 <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> source)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copies all properties and context from source engine to destination engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(com.nomagic.magicreport.engine.ITemplateEngine,com.nomagic.magicreport.engine.ITemplateEngine,boolean,boolean)">copy</a><wbr/>(<a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> dest,
 <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> source,
 boolean copyRuntimeInstance,
 boolean copyFormatterRuntimeInstance)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copies all properties and context from source engine to destination engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateEngine(java.lang.Class)">createTemplateEngine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>&gt; clazz)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create a new instance of template engine associated with given class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateEngine(java.lang.String)">createTemplateEngine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create a new instance of template engine associated with given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultTemplateEngineClassName(java.lang.String)">getDefaultTemplateEngineClassName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> engineName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return default template engine class name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TemplateEngineFactory.html" title="class in com.nomagic.magicreport">TemplateEngineFactory</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return instance of this class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a><wbr/>&lt;? extends <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRegisterTemplateEngine(java.lang.String)">getRegisterTemplateEngine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a registered template engine class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateAliasNames()">getTemplateAliasNames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an array of the alias names of default template engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateEngine(java.lang.Class)">getTemplateEngine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>&gt; clazz)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return template engine associated with given class or create a new instance if it doesn't created.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateEngine(java.lang.String)">getTemplateEngine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return template engine associated with given type or create a new instance if it doesn't created.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a><wbr/>&lt;? extends <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateEngineClass(java.lang.String)">getTemplateEngineClass</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return class of template engine associated with given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerTemplateEngine(java.lang.String,java.lang.Class)">registerTemplateEngine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>&gt; templateEngineClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers the given class name with the <a href="TemplateEngineFactory.html" title="class in com.nomagic.magicreport"><code>TemplateEngineFactory</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterTemplateEngine(java.lang.String)">unregisterTemplateEngine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregister the given file extension.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="TemplateEngineFactory.html" title="class in com.nomagic.magicreport">TemplateEngineFactory</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Return instance of this class.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance of this class.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultTemplateEngineClassName(java.lang.String)">
<h3>getDefaultTemplateEngineClassName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDefaultTemplateEngineClassName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> engineName)</span></div>
<div class="block">Return default template engine class name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engineName</code> - name.</dd>
<dt>Returns:</dt>
<dd>default template engine class name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateAliasNames()">
<h3>getTemplateAliasNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">getTemplateAliasNames</span>()</div>
<div class="block">Return an array of the alias names of default template engine.
 <pre>
 <code>
        String[] aliasNames = TemplateEngineFactory.getInstance().getTemplateAliasNames();
 </code>
 </pre></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array of the alias names and description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerTemplateEngine(java.lang.String,java.lang.Class)">
<h3>registerTemplateEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerTemplateEngine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>&gt; templateEngineClass)</span></div>
<div class="block">Registers the given class name with the <a href="TemplateEngineFactory.html" title="class in com.nomagic.magicreport"><code>TemplateEngineFactory</code></a>. A newly-loaded engine class should
 call the method registerTemplateEngine to make itself known to the TemplateEngineFactory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>extension</code> - template file extension</dd>
<dd><code>templateEngineClass</code> - the new <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine"><code>ITemplateEngine</code></a> that is to be registered with the
           <a href="TemplateEngineFactory.html" title="class in com.nomagic.magicreport"><code>TemplateEngineFactory</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregisterTemplateEngine(java.lang.String)">
<h3>unregisterTemplateEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">unregisterTemplateEngine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</span></div>
<div class="block">Unregister the given file extension.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>extension</code> - file extension.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRegisterTemplateEngine(java.lang.String)">
<h3>getRegisterTemplateEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>&gt;</span> <span class="element-name">getRegisterTemplateEngine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</span></div>
<div class="block">Return a registered template engine class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>extension</code> - template file extension</dd>
<dt>Returns:</dt>
<dd>a template engine class <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine"><code>ITemplateEngine</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateEngine(java.lang.Class)">
<h3>getTemplateEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></span> <span class="element-name">getTemplateEngine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>&gt; clazz)</span>
                                  throws <span class="exceptions"><a href="InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></span></div>
<div class="block">Return template engine associated with given class or create a new instance if it doesn't created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - associated class for template engine.</dd>
<dt>Returns:</dt>
<dd>template engine</dd>
<dt>Throws:</dt>
<dd><code><a href="InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while creating template engine.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateEngine(java.lang.String)">
<h3>getTemplateEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></span> <span class="element-name">getTemplateEngine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span>
                                  throws <span class="exceptions"><a href="InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></span></div>
<div class="block">Return template engine associated with given type or create a new instance if it doesn't created. If no
 associated type found, text engine <a href="engine/velocity/TextEngine.html" title="class in com.nomagic.magicreport.engine.velocity"><code>TextEngine</code></a> will be return
 as default engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - engine type.</dd>
<dt>Returns:</dt>
<dd>template engine</dd>
<dt>Throws:</dt>
<dd><code><a href="InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while creating template engine.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateEngineClass(java.lang.String)">
<h3>getTemplateEngineClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>&gt;</span> <span class="element-name">getTemplateEngineClass</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Return class of template engine associated with given type. If no associated type found, text engine
 <a href="engine/velocity/TextEngine.html" title="class in com.nomagic.magicreport.engine.velocity"><code>TextEngine</code></a> will be return as default engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - engine type.</dd>
<dt>Returns:</dt>
<dd>template engine class</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateEngine(java.lang.String)">
<h3>createTemplateEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></span> <span class="element-name">createTemplateEngine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span>
                                     throws <span class="exceptions"><a href="InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></span></div>
<div class="block">Create a new instance of template engine associated with given type. If no associated type found, text
 engine <a href="engine/velocity/TextEngine.html" title="class in com.nomagic.magicreport.engine.velocity"><code>TextEngine</code></a> will be return as default engine.
 <p>
 This method always return new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - engine type.</dd>
<dt>Returns:</dt>
<dd>template engine</dd>
<dt>Throws:</dt>
<dd><code><a href="InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while creating template engine.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateEngine(java.lang.Class)">
<h3>createTemplateEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></span> <span class="element-name">createTemplateEngine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>&gt; clazz)</span>
                                     throws <span class="exceptions"><a href="InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></span></div>
<div class="block">Create a new instance of template engine associated with given class.
 <p>
 This method always return new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - engine Class.</dd>
<dt>Returns:</dt>
<dd>template engine</dd>
<dt>Throws:</dt>
<dd><code><a href="InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while creating template engine.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(com.nomagic.magicreport.engine.ITemplateEngine,com.nomagic.magicreport.engine.ITemplateEngine)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> dest,
 <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> source)</span></div>
<div class="block">Copies all properties and context from source engine to destination engine.
 <p>
 This method will perform shallow copy of context. The reference to context of new engine will not remain the
 same as source engine. In order to copy, all object inside context requires implement clone() method.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dest</code> - the destination engine.</dd>
<dd><code>source</code> - source engine.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(com.nomagic.magicreport.engine.ITemplateEngine,com.nomagic.magicreport.engine.ITemplateEngine,boolean,boolean)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> dest,
 <a href="engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> source,
 boolean copyRuntimeInstance,
 boolean copyFormatterRuntimeInstance)</span></div>
<div class="block">Copies all properties and context from source engine to destination engine.
 <p>
 This method will perform shallow copy of context. The reference to context of new engine will not remain the
 same as source engine. In order to copy, all object inside context requires implement clone() method.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dest</code> - the destination engine.</dd>
<dd><code>source</code> - source engine.</dd>
<dd><code>copyRuntimeInstance</code> - true to copy RuntimeInstance of source to destination engine if both are instance of IRuntimeInstanceVelocityEngine</dd>
<dd><code>copyFormatterRuntimeInstance</code> - true to copy Formatter of source to destination engine if both are instance of DefaultTemplateEngine</dd>
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
