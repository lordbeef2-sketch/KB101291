# JAVA OPENAPI: DocBookEngine (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/velocity/DocBookEngine.html
- source_path: `com/nomagic/magicreport/engine/velocity/DocBookEngine.html`
- source_sha256: `30b34055cf57c588bc6dbfafbe854487e1dc717c53f30de3bd6d5e27290c0a42`
- captured_utc: `2026-07-14T16:58:37.631293+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.velocity](package-summary.html)

## Class DocBookEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.AbstractTemplateEngine](../AbstractTemplateEngine.html)
[com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine](DefaultTemplateEngine.html)
[com.nomagic.magicreport.engine.velocity.XMLEngine](XMLEngine.html)
com.nomagic.magicreport.engine.velocity.DocBookEngine

All Implemented Interfaces:
`[IExtensionTemplateEngine](../IExtensionTemplateEngine.html)`, `com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine`, `[ITemplateEngine](../ITemplateEngine.html)`

@OpenApiAllpublic classDocBookEngine
extends [XMLEngine](XMLEngine.html)

This class provides an instance of the Velocity template engine.

Since:
Jan 30, 2013
Version:
1.0 Jan 30, 2013

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.engine.velocity.[DefaultTemplateEngine](DefaultTemplateEngine.html)
`[velocityContext](DefaultTemplateEngine.html#velocityContext)`
Fields inherited from class com.nomagic.magicreport.engine.[AbstractTemplateEngine](../AbstractTemplateEngine.html)
`[context](../AbstractTemplateEngine.html#context), [isAborted](../AbstractTemplateEngine.html#isAborted), [preProcessFile](../AbstractTemplateEngine.html#preProcessFile), [processFile](../AbstractTemplateEngine.html#processFile), [properties](../AbstractTemplateEngine.html#properties)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DocBookEngine](#%3Cinit%3E())()`
Create instance of engine.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[postProcess](#postProcess(com.nomagic.magicreport.Template))([Template](../../Template.html) template)`
Perform a post-processing after the template has been evaluated.
Methods inherited from class com.nomagic.magicreport.engine.velocity.[XMLEngine](XMLEngine.html)
`[createComment](XMLEngine.html#createComment(java.lang.String))`
Methods inherited from class com.nomagic.magicreport.engine.velocity.[DefaultTemplateEngine](DefaultTemplateEngine.html)
`[abort](DefaultTemplateEngine.html#abort()), [checkFileNotFoundException](DefaultTemplateEngine.html#checkFileNotFoundException(java.lang.Exception,java.io.File)), [clearTools](DefaultTemplateEngine.html#clearTools()), [createTemplate](DefaultTemplateEngine.html#createTemplate()), [createTemplate](DefaultTemplateEngine.html#createTemplate(java.io.File,java.io.File)), [createTemplate](DefaultTemplateEngine.html#createTemplate(java.io.File,java.io.File,boolean)), [destroy](DefaultTemplateEngine.html#destroy()), [getClassLoader](DefaultTemplateEngine.html#getClassLoader()), [getFormatter](DefaultTemplateEngine.html#getFormatter()), [getResolvedSectionName](DefaultTemplateEngine.html#getResolvedSectionName(java.lang.String)), [handleForPage](DefaultTemplateEngine.html#handleForPage(com.nomagic.magicreport.Template,java.lang.StringBuilder)), [handleForRow](DefaultTemplateEngine.html#handleForRow(com.nomagic.magicreport.Template,java.lang.StringBuilder)), [handleImport](DefaultTemplateEngine.html#handleImport(com.nomagic.magicreport.Template,java.lang.StringBuilder)), [handleIncludeSection](DefaultTemplateEngine.html#handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder)), [handleSectionBegin](DefaultTemplateEngine.html#handleSectionBegin(com.nomagic.magicreport.Template,java.lang.StringBuilder)), [isNoSpaceException](DefaultTemplateEngine.html#isNoSpaceException(java.lang.Exception)), [lineCount](DefaultTemplateEngine.html#lineCount(java.lang.String)), [preProcess](DefaultTemplateEngine.html#preProcess(com.nomagic.magicreport.Template)), [process](DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template)), [process](DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)), [processException](DefaultTemplateEngine.html#processException(com.nomagic.magicreport.Template,com.nomagic.magicreport.ParseErrorException)), [processVelocityException](DefaultTemplateEngine.html#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.MethodInvocationException)), [processVelocityException](DefaultTemplateEngine.html#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException)), [setClassLoader](DefaultTemplateEngine.html#setClassLoader(java.lang.ClassLoader)), [setFormatter](DefaultTemplateEngine.html#setFormatter(com.nomagic.magicreport.format.IFormatter)), [setLatestLocation](DefaultTemplateEngine.html#setLatestLocation(java.io.File,java.io.File)), [setLocation](DefaultTemplateEngine.html#setLocation(java.io.File,java.io.File)), [setProperty](DefaultTemplateEngine.html#setProperty(java.lang.String,java.lang.Object)), [setWriterForEvaluate](DefaultTemplateEngine.html#setWriterForEvaluate(com.nomagic.magicreport.Template)), [translate](DefaultTemplateEngine.html#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder)), [trimTrailSpace](DefaultTemplateEngine.html#trimTrailSpace(int,java.lang.StringBuilder))`
Methods inherited from class com.nomagic.magicreport.engine.[AbstractTemplateEngine](../AbstractTemplateEngine.html)
`[addContext](../AbstractTemplateEngine.html#addContext(java.lang.String,java.lang.Object)), [addInvalidReferenceHandler](../AbstractTemplateEngine.html#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)), [addObserver](../AbstractTemplateEngine.html#addObserver(java.util.Observer)), [addReferenceInsertionHandler](../AbstractTemplateEngine.html#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)), [evaluate](../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template)), [evaluate](../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)), [getConcurrentToolException](../AbstractTemplateEngine.html#getConcurrentToolException()), [getContext](../AbstractTemplateEngine.html#getContext()), [getCurrentRuntimeInstance](../AbstractTemplateEngine.html#getCurrentRuntimeInstance()), [getInvalidReferenceHandler](../AbstractTemplateEngine.html#getInvalidReferenceHandler()), [getProcessSize](../AbstractTemplateEngine.html#getProcessSize()), [getProperties](../AbstractTemplateEngine.html#getProperties()), [getProperty](../AbstractTemplateEngine.html#getProperty(java.lang.String)), [getReferenceInsertionHandler](../AbstractTemplateEngine.html#getReferenceInsertionHandler()), [isMemoryMode](../AbstractTemplateEngine.html#isMemoryMode(com.nomagic.magicreport.Template)), [notifyObservers](../AbstractTemplateEngine.html#notifyObservers(java.lang.Object)), [observers](../AbstractTemplateEngine.html#observers()), [setConcurrentToolException](../AbstractTemplateEngine.html#setConcurrentToolException(java.lang.Exception)), [setContext](../AbstractTemplateEngine.html#setContext(com.nomagic.magicreport.engine.IContext)), [setCurrentRuntimeInstance](../AbstractTemplateEngine.html#setCurrentRuntimeInstance(org.apache.velocity.runtime.RuntimeInstance))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DocBookEngine
public DocBookEngine()
Create instance of engine.
 ============ METHOD DETAIL ========== 
Method Details
postProcess
protected void postProcess([Template](../../Template.html) template)
 throws [TemplateException](../../TemplateException.html)
Perform a post-processing after the template has been evaluated.
Overrides:
`[postProcess](DefaultTemplateEngine.html#postProcess(com.nomagic.magicreport.Template))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`template` - template after evaluated.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../../TemplateException.html)` - other error while processing the template
See Also:
[`AbstractTemplateEngine.postProcess(com.nomagic.magicreport.Template)`](../AbstractTemplateEngine.html#postProcess(com.nomagic.magicreport.Template))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.velocity</a></div>
<h1 class="title" title="Class DocBookEngine">Class DocBookEngine</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.AbstractTemplateEngine</a>
<div class="inheritance"><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine</a>
<div class="inheritance"><a href="XMLEngine.html" title="class in com.nomagic.magicreport.engine.velocity">com.nomagic.magicreport.engine.velocity.XMLEngine</a>
<div class="inheritance">com.nomagic.magicreport.engine.velocity.DocBookEngine</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../IExtensionTemplateEngine.html" title="interface in com.nomagic.magicreport.engine">IExtensionTemplateEngine</a></code>, <code>com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine</code>, <code><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DocBookEngine</span>
<span class="extends-implements">extends <a href="XMLEngine.html" title="class in com.nomagic.magicreport.engine.velocity">XMLEngine</a></span></div>
<div class="block">This class provides an instance of the Velocity template engine.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jan 30, 2013</dd>
<dt>Version:</dt>
<dd>1.0 Jan 30, 2013</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine">Fields inherited from class com.nomagic.magicreport.engine.velocity.<a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></h3>
<code><a href="DefaultTemplateEngine.html#velocityContext">velocityContext</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.AbstractTemplateEngine">Fields inherited from class com.nomagic.magicreport.engine.<a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></h3>
<code><a href="../AbstractTemplateEngine.html#context">context</a>, <a href="../AbstractTemplateEngine.html#isAborted">isAborted</a>, <a href="../AbstractTemplateEngine.html#preProcessFile">preProcessFile</a>, <a href="../AbstractTemplateEngine.html#processFile">processFile</a>, <a href="../AbstractTemplateEngine.html#properties">properties</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DocBookEngine</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Create instance of engine.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#postProcess(com.nomagic.magicreport.Template)">postProcess</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Perform a post-processing after the template has been evaluated.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.velocity.XMLEngine">Methods inherited from class com.nomagic.magicreport.engine.velocity.<a href="XMLEngine.html" title="class in com.nomagic.magicreport.engine.velocity">XMLEngine</a></h3>
<code><a href="XMLEngine.html#createComment(java.lang.String)">createComment</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine">Methods inherited from class com.nomagic.magicreport.engine.velocity.<a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></h3>
<code><a href="DefaultTemplateEngine.html#abort()">abort</a>, <a href="DefaultTemplateEngine.html#checkFileNotFoundException(java.lang.Exception,java.io.File)">checkFileNotFoundException</a>, <a href="DefaultTemplateEngine.html#clearTools()">clearTools</a>, <a href="DefaultTemplateEngine.html#createTemplate()">createTemplate</a>, <a href="DefaultTemplateEngine.html#createTemplate(java.io.File,java.io.File)">createTemplate</a>, <a href="DefaultTemplateEngine.html#createTemplate(java.io.File,java.io.File,boolean)">createTemplate</a>, <a href="DefaultTemplateEngine.html#destroy()">destroy</a>, <a href="DefaultTemplateEngine.html#getClassLoader()">getClassLoader</a>, <a href="DefaultTemplateEngine.html#getFormatter()">getFormatter</a>, <a href="DefaultTemplateEngine.html#getResolvedSectionName(java.lang.String)">getResolvedSectionName</a>, <a href="DefaultTemplateEngine.html#handleForPage(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleForPage</a>, <a href="DefaultTemplateEngine.html#handleForRow(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleForRow</a>, <a href="DefaultTemplateEngine.html#handleImport(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleImport</a>, <a href="DefaultTemplateEngine.html#handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleIncludeSection</a>, <a href="DefaultTemplateEngine.html#handleSectionBegin(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleSectionBegin</a>, <a href="DefaultTemplateEngine.html#isNoSpaceException(java.lang.Exception)">isNoSpaceException</a>, <a href="DefaultTemplateEngine.html#lineCount(java.lang.String)">lineCount</a>, <a href="DefaultTemplateEngine.html#preProcess(com.nomagic.magicreport.Template)">preProcess</a>, <a href="DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template)">process</a>, <a href="DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">process</a>, <a href="DefaultTemplateEngine.html#processException(com.nomagic.magicreport.Template,com.nomagic.magicreport.ParseErrorException)">processException</a>, <a href="DefaultTemplateEngine.html#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.MethodInvocationException)">processVelocityException</a>, <a href="DefaultTemplateEngine.html#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException)">processVelocityException</a>, <a href="DefaultTemplateEngine.html#setClassLoader(java.lang.ClassLoader)">setClassLoader</a>, <a href="DefaultTemplateEngine.html#setFormatter(com.nomagic.magicreport.format.IFormatter)">setFormatter</a>, <a href="DefaultTemplateEngine.html#setLatestLocation(java.io.File,java.io.File)">setLatestLocation</a>, <a href="DefaultTemplateEngine.html#setLocation(java.io.File,java.io.File)">setLocation</a>, <a href="DefaultTemplateEngine.html#setProperty(java.lang.String,java.lang.Object)">setProperty</a>, <a href="DefaultTemplateEngine.html#setWriterForEvaluate(com.nomagic.magicreport.Template)">setWriterForEvaluate</a>, <a href="DefaultTemplateEngine.html#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder)">translate</a>, <a href="DefaultTemplateEngine.html#trimTrailSpace(int,java.lang.StringBuilder)">trimTrailSpace</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.AbstractTemplateEngine">Methods inherited from class com.nomagic.magicreport.engine.<a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></h3>
<code><a href="../AbstractTemplateEngine.html#addContext(java.lang.String,java.lang.Object)">addContext</a>, <a href="../AbstractTemplateEngine.html#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)">addInvalidReferenceHandler</a>, <a href="../AbstractTemplateEngine.html#addObserver(java.util.Observer)">addObserver</a>, <a href="../AbstractTemplateEngine.html#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)">addReferenceInsertionHandler</a>, <a href="../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template)">evaluate</a>, <a href="../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">evaluate</a>, <a href="../AbstractTemplateEngine.html#getConcurrentToolException()">getConcurrentToolException</a>, <a href="../AbstractTemplateEngine.html#getContext()">getContext</a>, <a href="../AbstractTemplateEngine.html#getCurrentRuntimeInstance()">getCurrentRuntimeInstance</a>, <a href="../AbstractTemplateEngine.html#getInvalidReferenceHandler()">getInvalidReferenceHandler</a>, <a href="../AbstractTemplateEngine.html#getProcessSize()">getProcessSize</a>, <a href="../AbstractTemplateEngine.html#getProperties()">getProperties</a>, <a href="../AbstractTemplateEngine.html#getProperty(java.lang.String)">getProperty</a>, <a href="../AbstractTemplateEngine.html#getReferenceInsertionHandler()">getReferenceInsertionHandler</a>, <a href="../AbstractTemplateEngine.html#isMemoryMode(com.nomagic.magicreport.Template)">isMemoryMode</a>, <a href="../AbstractTemplateEngine.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../AbstractTemplateEngine.html#observers()">observers</a>, <a href="../AbstractTemplateEngine.html#setConcurrentToolException(java.lang.Exception)">setConcurrentToolException</a>, <a href="../AbstractTemplateEngine.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../AbstractTemplateEngine.html#setCurrentRuntimeInstance(org.apache.velocity.runtime.RuntimeInstance)">setCurrentRuntimeInstance</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
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
<h3>DocBookEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DocBookEngine</span>()</div>
<div class="block">Create instance of engine.</div>
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
<section class="detail" id="postProcess(com.nomagic.magicreport.Template)">
<h3>postProcess</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">postProcess</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span>
                    throws <span class="exceptions"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Perform a post-processing after the template has been evaluated.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#postProcess(com.nomagic.magicreport.Template)">postProcess</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - template after evaluated.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
<dd><code><a href="../../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while initializing engine</dd>
<dd><code><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error while processing the template</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../AbstractTemplateEngine.html#postProcess(com.nomagic.magicreport.Template)"><code>AbstractTemplateEngine.postProcess(com.nomagic.magicreport.Template)</code></a></li>
</ul>
</dd>
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
