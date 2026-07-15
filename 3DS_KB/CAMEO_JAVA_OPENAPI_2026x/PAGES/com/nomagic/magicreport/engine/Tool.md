# JAVA OPENAPI: Tool (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/Tool.html
- source_path: `com/nomagic/magicreport/engine/Tool.html`
- source_sha256: `4e14833fb07abff1a1657e6545a1f26e830153e332fb1a672cf14de3748f8e2f`
- captured_utc: `2026-07-14T16:58:36.653276+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Class Tool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
com.nomagic.magicreport.engine.Tool

All Implemented Interfaces:
`[ITool](ITool.html)`, `[IVariable](../IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[ArrayTool](tools/ArrayTool.html)`, `[BookmarkTool](tools/BookmarkTool.html)`, `[ChartTool](../../reportwizard/tools/ChartTool.html)`, `[ConcurrentTool](ConcurrentTool.html)`, `[DependencyMatrixTool](../../reportwizard/tools/DependencyMatrixTool.html)`, `[DialogTool](../../reportwizard/tools/DialogTool.html)`, `[DocBookTool](../../reportwizard/tools/DocBookTool.html)`, `[GenericTableTool](../../reportwizard/tools/GenericTableTool.html)`, `[GroovyTool](../../reportwizard/tools/script/GroovyTool.html)`, `[GroupTool](tools/GroupTool.html)`, `[ImageTool](tools/ImageTool.html)`, `[ImportTool](../../reportwizard/tools/ImportTool.html)`, `[JavaDocTool](../../reportwizard/tools/doc/JavaDocTool.html)`, `[JavaScriptTool](../../reportwizard/tools/script/JavaScriptTool.html)`, `[MapTool](tools/MapTool.html)`, `[MathTool](../../reportwizard/tools/MathTool.html)`, `[ModelValidationTool](../../reportwizard/tools/ModelValidationTool.html)`, `[ProfilingTool](../../magicdraw/magicreport/tools/ProfilingTool.html)`, `[ProjectTool](../../magicdraw/magicreport/tools/ProjectTool.html)`, `[QueryTool](../../reportwizard/tools/QueryTool.html)`, `[ReportHelper](../../magicdraw/magicreport/helper/ReportHelper.html)`, `[SortTool](tools/SortTool.html)`, `[TemplateTool](tools/TemplateTool.html)`, `[TextTool](../../reportwizard/tools/TextTool.html)`

@OpenApiAllpublic classTool
extends [Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
implements [ITool](ITool.html), [Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)

A base class realizing from interface [`ITool`](ITool.html). This class provide default implementation for
 [`ITool`](ITool.html). The extended class from this class may send message or object to observer class by invoke
 [`notifyObservers(Object)`](#notifyObservers(java.lang.Object)) of class [`Observable`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html). The observer class such as
 [`AbstractTemplateEngine`](AbstractTemplateEngine.html) or graphical user interface can catch notified object and interact with user.
 This class also implement Cloneable interface with allow an object to create and return copy of this object.

Since:
Aug 3, 2007
See Also:
[Serialized Form](../../../../serialized-form.html#com.nomagic.magicreport.engine.Tool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](ITool.html)
`[ITool.HTMLString](ITool.HTMLString.html), [ITool.RetainedString](ITool.RetainedString.html), [ITool.Void](ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [IContext](IContext.html)`
`[context](#context)`
Template context.
`protected [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html)`
`[properties](#properties)`
Template engine properties.
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](ITool.html)
`[VOID](ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Tool](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[clone](#clone())()`
Creates and returns a copy of this object.
`[IContext](IContext.html)`
`[getContext](#getContext())()`
Return template context.
`[Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html)`
`[getProperties](#getProperties())()`
Return template engine properties.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getProperty](#getProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)`
Return template engine property value.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getProperty](#getProperty(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) defaultValue)`
Return template engine property value.
`void`
`[notifyObservers](#notifyObservers(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) event)`
Override `notifyObservers` by provide sequence of calling these methods.
`void`
`[setContext](#setContext(com.nomagic.magicreport.engine.IContext))([IContext](IContext.html) context)`
This method is invoked by the template engine runtime, after class has been initializing, to set the
 template context.
`void`
`[setProperties](#setProperties(java.util.Properties))([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
This method is invoked by the template engine runtime, after class has been initializing, to set the
 template properties.
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](ITool.html)
`[clearTool](ITool.html#clearTool())`

============ FIELD DETAIL =========== 
Field Details
properties
protected [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties
Template engine properties.
context
protected [IContext](IContext.html) context
Template context.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Tool
public Tool()
 ============ METHOD DETAIL ========== 
Method Details
setProperties
public void setProperties([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
This method is invoked by the template engine runtime, after class has been initializing, to set the
 template properties. Override current properties will not affect with the engine.
Specified by:
`[setProperties](ITool.html#setProperties(java.util.Properties))` in interface `[ITool](ITool.html)`
Parameters:
`properties` - template engine properties
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if properties is null
getProperties
public [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) getProperties()
Return template engine properties.
Specified by:
`[getProperties](ITool.html#getProperties())` in interface `[ITool](ITool.html)`
Returns:
template engine properties
getProperty
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)
Return template engine property value.
Parameters:
`key` - property key
Returns:
template engine value
getProperty
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) defaultValue)
Return template engine property value. If the key is not found in this property, the default value is
 return.
Parameters:
`key` - property key
`defaultValue` - default value
Returns:
template engine value
setContext
public void setContext([IContext](IContext.html) context)
This method is invoked by the template engine runtime, after class has been initializing, to set the
 template context. This method automatically called by template engine.
Specified by:
`[setContext](ITool.html#setContext(com.nomagic.magicreport.engine.IContext))` in interface `[ITool](ITool.html)`
Parameters:
`context` - template context
getContext
public [IContext](IContext.html) getContext()
Return template context.
Specified by:
`[getContext](ITool.html#getContext())` in interface `[ITool](ITool.html)`
Returns:
template context
notifyObservers
public void notifyObservers([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) event)
Override `notifyObservers` by provide sequence of calling these methods. `setChanged();
 super.notifyObservers(event);`
Overrides:
`[notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers(java.lang.Object))` in class `[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)`
Parameters:
`event` - any object.
See Also:
[`Observable.clearChanged()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged())
[`Observable.hasChanged()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged())
[`Observer.update(java.util.Observable, java.lang.Object)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html#update(java.util.Observable,java.lang.Object))
clone
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) clone()
 throws [CloneNotSupportedException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CloneNotSupportedException.html)
Creates and returns a copy of this object.
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
a clone of this instance.
Throws:
`[CloneNotSupportedException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CloneNotSupportedException.html)` - if the object's class does not support the `Cloneable`
 interface.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Class Tool">Class Tool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance">com.nomagic.magicreport.engine.Tool</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="tools/ArrayTool.html" title="class in com.nomagic.magicreport.engine.tools">ArrayTool</a></code>, <code><a href="tools/BookmarkTool.html" title="class in com.nomagic.magicreport.engine.tools">BookmarkTool</a></code>, <code><a href="../../reportwizard/tools/ChartTool.html" title="class in com.nomagic.reportwizard.tools">ChartTool</a></code>, <code><a href="ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></code>, <code><a href="../../reportwizard/tools/DependencyMatrixTool.html" title="class in com.nomagic.reportwizard.tools">DependencyMatrixTool</a></code>, <code><a href="../../reportwizard/tools/DialogTool.html" title="class in com.nomagic.reportwizard.tools">DialogTool</a></code>, <code><a href="../../reportwizard/tools/DocBookTool.html" title="class in com.nomagic.reportwizard.tools">DocBookTool</a></code>, <code><a href="../../reportwizard/tools/GenericTableTool.html" title="class in com.nomagic.reportwizard.tools">GenericTableTool</a></code>, <code><a href="../../reportwizard/tools/script/GroovyTool.html" title="class in com.nomagic.reportwizard.tools.script">GroovyTool</a></code>, <code><a href="tools/GroupTool.html" title="class in com.nomagic.magicreport.engine.tools">GroupTool</a></code>, <code><a href="tools/ImageTool.html" title="class in com.nomagic.magicreport.engine.tools">ImageTool</a></code>, <code><a href="../../reportwizard/tools/ImportTool.html" title="class in com.nomagic.reportwizard.tools">ImportTool</a></code>, <code><a href="../../reportwizard/tools/doc/JavaDocTool.html" title="class in com.nomagic.reportwizard.tools.doc">JavaDocTool</a></code>, <code><a href="../../reportwizard/tools/script/JavaScriptTool.html" title="class in com.nomagic.reportwizard.tools.script">JavaScriptTool</a></code>, <code><a href="tools/MapTool.html" title="class in com.nomagic.magicreport.engine.tools">MapTool</a></code>, <code><a href="../../reportwizard/tools/MathTool.html" title="class in com.nomagic.reportwizard.tools">MathTool</a></code>, <code><a href="../../reportwizard/tools/ModelValidationTool.html" title="class in com.nomagic.reportwizard.tools">ModelValidationTool</a></code>, <code><a href="../../magicdraw/magicreport/tools/ProfilingTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProfilingTool</a></code>, <code><a href="../../magicdraw/magicreport/tools/ProjectTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectTool</a></code>, <code><a href="../../reportwizard/tools/QueryTool.html" title="class in com.nomagic.reportwizard.tools">QueryTool</a></code>, <code><a href="../../magicdraw/magicreport/helper/ReportHelper.html" title="class in com.nomagic.magicdraw.magicreport.helper">ReportHelper</a></code>, <code><a href="tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></code>, <code><a href="tools/TemplateTool.html" title="class in com.nomagic.magicreport.engine.tools">TemplateTool</a></code>, <code><a href="../../reportwizard/tools/TextTool.html" title="class in com.nomagic.reportwizard.tools">TextTool</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Tool</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a>
implements <a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></span></div>
<div class="block">A base class realizing from interface <a href="ITool.html" title="interface in com.nomagic.magicreport.engine"><code>ITool</code></a>. This class provide default implementation for
 <a href="ITool.html" title="interface in com.nomagic.magicreport.engine"><code>ITool</code></a>. The extended class from this class may send message or object to observer class by invoke
 <a href="#notifyObservers(java.lang.Object)"><code>notifyObservers(Object)</code></a> of class <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util"><code>Observable</code></a>. The observer class such as
 <a href="AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine"><code>AbstractTemplateEngine</code></a> or graphical user interface can catch notified object and interact with user.
 <p>
 This class also implement Cloneable interface with allow an object to create and return copy of this object.</p></div>
<dl class="notes">
<dt>Since:</dt>
<dd>Aug 3, 2007</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../serialized-form.html#com.nomagic.magicreport.engine.Tool">Serialized Form</a></li>
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
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
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
<div class="col-first even-row-color"><code>protected <a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#context">context</a></code></div>
<div class="col-last even-row-color">
<div class="block">Template context.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#properties">properties</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Template engine properties.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="ITool.html#VOID">VOID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Tool</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates and returns a copy of this object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContext()">getContext</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return template context.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperties()">getProperties</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return template engine properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperty(java.lang.String)">getProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return template engine property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperty(java.lang.String,java.lang.String)">getProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> defaultValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return template engine property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#notifyObservers(java.lang.Object)">notifyObservers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> event)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Override <code>notifyObservers</code> by provide sequence of calling these methods.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a><wbr/>(<a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method is invoked by the template engine runtime, after class has been initializing, to set the
 template context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperties(java.util.Properties)">setProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method is invoked by the template engine runtime, after class has been initializing, to set the
 template properties.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="ITool.html#clearTool()">clearTool</a></code></div>
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
<section class="detail" id="properties">
<h3>properties</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></span> <span class="element-name">properties</span></div>
<div class="block">Template engine properties.</div>
</section>
</li>
<li>
<section class="detail" id="context">
<h3>context</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></span> <span class="element-name">context</span></div>
<div class="block">Template context.</div>
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
<h3>Tool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Tool</span>()</div>
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
<section class="detail" id="setProperties(java.util.Properties)">
<h3>setProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">This method is invoked by the template engine runtime, after class has been initializing, to set the
 template properties. Override current properties will not affect with the engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITool.html#setProperties(java.util.Properties)">setProperties</a></code> in interface <code><a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>properties</code> - template engine properties</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if properties is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperties()">
<h3>getProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></span> <span class="element-name">getProperties</span>()</div>
<div class="block">Return template engine properties.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITool.html#getProperties()">getProperties</a></code> in interface <code><a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code></dd>
<dt>Returns:</dt>
<dd>template engine properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperty(java.lang.String)">
<h3>getProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div class="block">Return template engine property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - property key</dd>
<dt>Returns:</dt>
<dd>template engine value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperty(java.lang.String,java.lang.String)">
<h3>getProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> defaultValue)</span></div>
<div class="block">Return template engine property value. If the key is not found in this property, the default value is
 return.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - property key</dd>
<dd><code>defaultValue</code> - default value</dd>
<dt>Returns:</dt>
<dd>template engine value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContext(com.nomagic.magicreport.engine.IContext)">
<h3>setContext</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setContext</span><wbr/><span class="parameters">(<a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a> context)</span></div>
<div class="block">This method is invoked by the template engine runtime, after class has been initializing, to set the
 template context. This method automatically called by template engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a></code> in interface <code><a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>context</code> - template context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContext()">
<h3>getContext</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></span> <span class="element-name">getContext</span>()</div>
<div class="block">Return template context.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITool.html#getContext()">getContext</a></code> in interface <code><a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code></dd>
<dt>Returns:</dt>
<dd>template context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="notifyObservers(java.lang.Object)">
<h3>notifyObservers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">notifyObservers</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> event)</span></div>
<div class="block">Override <code>notifyObservers</code> by provide sequence of calling these methods. <pre><code>
 setChanged();
 super.notifyObservers(event);
 </code></pre></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers(java.lang.Object)" title="class or interface in java.util">notifyObservers</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></code></dd>
<dt>Parameters:</dt>
<dd><code>event</code> - any object.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util"><code>Observable.clearChanged()</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util"><code>Observable.hasChanged()</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html#update(java.util.Observable,java.lang.Object)" title="class or interface in java.util"><code>Observer.update(java.util.Observable, java.lang.Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">clone</span>()
             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CloneNotSupportedException.html" title="class or interface in java.lang">CloneNotSupportedException</a></span></div>
<div class="block">Creates and returns a copy of this object.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>a clone of this instance.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CloneNotSupportedException.html" title="class or interface in java.lang">CloneNotSupportedException</a></code> - if the object's class does not support the <code>Cloneable</code>
            interface.</dd>
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
