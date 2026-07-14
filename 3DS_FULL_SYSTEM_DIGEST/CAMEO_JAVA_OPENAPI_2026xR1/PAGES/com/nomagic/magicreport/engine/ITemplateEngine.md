# JAVA OPENAPI: ITemplateEngine (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/ITemplateEngine.html
- source_path: `com/nomagic/magicreport/engine/ITemplateEngine.html`
- source_sha256: `697b962883cf2ffa48fa9e97f30ee6795ba575a7db943f7ca5e16520163d7c6b`
- captured_utc: `2026-07-14T16:46:11.906959+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Interface ITemplateEngine

All Known Implementing Classes:
`[AbstractTemplateEngine](AbstractTemplateEngine.html)`, `[DefaultTemplateEngine](velocity/DefaultTemplateEngine.html)`, `[DocBookEngine](velocity/DocBookEngine.html)`, `[DOCXEngine](velocity/DOCXEngine.html)`, `[HTMLEngine](velocity/HTMLEngine.html)`, `[LaTeXEngine](velocity/LaTeXEngine.html)`, `[PPTXEngine](velocity/PPTXEngine.html)`, `[RTFEngine](velocity/RTFEngine.html)`, `[TextEngine](velocity/TextEngine.html)`, `[XLSXEngine](velocity/XLSXEngine.html)`, `[XMLEngine](velocity/XMLEngine.html)`

@OpenApiAllpublic interfaceITemplateEngine

Provides an interface for template engine.

Since:
Jun 11, 2007

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[abort](#abort())()`
Called by the application to abort current evaluation context.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[addContext](#addContext(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Adds a name/value pair to the context.
`void`
`[addInvalidReferenceHandler](#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler))([IInvalidReferenceHandler](IInvalidReferenceHandler.html) handler)`
Add an invalid reference event handler to the engine.
`void`
`[addReferenceInsertionHandler](#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler))([IReferenceInsertionHandler](IReferenceInsertionHandler.html) handler)`
Add a reference insertion event handler to the engine.
`[Template](../Template.html)`
`[createTemplate](#createTemplate())()`
Creates a new and empty [`Template`](../Template.html) for generating report by this engine.
`[Template](../Template.html)`
`[createTemplate](#createTemplate(java.io.File,java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output)`
Creates a new [`Template`](../Template.html) object.
`void`
`[destroy](#destroy())()`
Called by the application or [`TemplateEngineFactory`](../TemplateEngineFactory.html) to inform this engine
 that it should destroy any resources that it has allocated.
`void`
`[evaluate](#evaluate(com.nomagic.magicreport.Template))([Template](../Template.html) template)`
Merge a template with current context and rendered stream into the writer.
`[IContext](IContext.html)`
`[getContext](#getContext())()`
Return context of this engine.
`[IFormatter](../format/IFormatter.html)`
`[getFormatter](#getFormatter())()`
Returns a formatter that can be used to create the object layout, and formats of state
 [`InsertionHandler`](velocity/InsertionHandler.html).
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[IInvalidReferenceHandler](IInvalidReferenceHandler.html)>`
`[getInvalidReferenceHandler](#getInvalidReferenceHandler())()`
Return a [`IInvalidReferenceHandler`](IInvalidReferenceHandler.html) of this engine.
`[Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html)`
`[getProperties](#getProperties())()`
Returns the current properties of engine.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getProperty](#getProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)`
Return an engine Runtime property.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[IReferenceInsertionHandler](IReferenceInsertionHandler.html)>`
`[getReferenceInsertionHandler](#getReferenceInsertionHandler())()`
Return a [`IInvalidReferenceHandler`](IInvalidReferenceHandler.html) of this engine.
`void`
`[setProperty](#setProperty(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Set an engine Runtime property.

============ METHOD DETAIL ========== 
Method Details
createTemplate
[Template](../Template.html) createTemplate()
Creates a new and empty [`Template`](../Template.html) for generating report by this engine.
Returns:
an instance of [`Template`](../Template.html)
See Also:
[`createTemplate(File, File)`](#createTemplate(java.io.File,java.io.File))
createTemplate
[Template](../Template.html) createTemplate([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Creates a new [`Template`](../Template.html) object.
Parameters:
`input` - template file.
`output` - output file.
Returns:
an instance of [`Template`](../Template.html)
Throws:
`[FileNotFoundException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/FileNotFoundException.html)` - if the file does not exist, is a directory rather than a regular file,
 or for some other reason cannot be opened.
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
getFormatter
[IFormatter](../format/IFormatter.html) getFormatter()
Returns a formatter that can be used to create the object layout, and formats of state
 [`InsertionHandler`](velocity/InsertionHandler.html).
Returns:
a formatter
getContext
[IContext](IContext.html) getContext()
Return context of this engine.
Returns:
a context of engine.
addContext
[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) addContext([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Adds a name/value pair to the context.
Parameters:
`name` - The name to key the provided value with.
`value` - The corresponding value.
Returns:
The old object or null if there was no old object.
getProperty
[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)
Return an engine Runtime property.
Parameters:
`key` - the property key
Returns:
the value in this property list with the specified key value.
See Also:
[`setProperty(String, Object)`](#setProperty(java.lang.String,java.lang.Object))
setProperty
void setProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Set an engine Runtime property.
Parameters:
`key` - the key to be placed into this property list.
`value` - the value corresponding to key.
See Also:
[`getProperty(String)`](#getProperty(java.lang.String))
getProperties
[Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) getProperties()
Returns the current properties of engine.
Returns:
the engine properties
addReferenceInsertionHandler
void addReferenceInsertionHandler([IReferenceInsertionHandler](IReferenceInsertionHandler.html) handler)
Add a reference insertion event handler to the engine.
Parameters:
`handler` - ReferenceInsertionEventHandler
addInvalidReferenceHandler
void addInvalidReferenceHandler([IInvalidReferenceHandler](IInvalidReferenceHandler.html) handler)
Add an invalid reference event handler to the engine.
Parameters:
`handler` - IInvalidReferenceHandler
getInvalidReferenceHandler
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[IInvalidReferenceHandler](IInvalidReferenceHandler.html)> getInvalidReferenceHandler()
Return a [`IInvalidReferenceHandler`](IInvalidReferenceHandler.html) of this engine.
Returns:
invalid reference handler for this engine.
getReferenceInsertionHandler
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[IReferenceInsertionHandler](IReferenceInsertionHandler.html)> getReferenceInsertionHandler()
Return a [`IInvalidReferenceHandler`](IInvalidReferenceHandler.html) of this engine.
Returns:
reference insertion handler for this engine.
evaluate
void evaluate([Template](../Template.html) template)
 throws [TemplateException](../TemplateException.html)
Merge a template with current context and rendered stream into the writer.
Parameters:
`template` - Template being evaluated
Throws:
`[ParseErrorException](../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../InitializationEngineException.html)` - when engine initialize error
`[TemplateException](../TemplateException.html)` - other error
destroy
void destroy()
Called by the application or [`TemplateEngineFactory`](../TemplateEngineFactory.html) to inform this engine
 that it should destroy any resources that it has allocated.
abort
void abort()
Called by the application to abort current evaluation context.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Interface ITemplateEngine">Interface ITemplateEngine</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></code>, <code><a href="velocity/DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code>, <code><a href="velocity/DocBookEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DocBookEngine</a></code>, <code><a href="velocity/DOCXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine</a></code>, <code><a href="velocity/HTMLEngine.html" title="class in com.nomagic.magicreport.engine.velocity">HTMLEngine</a></code>, <code><a href="velocity/LaTeXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">LaTeXEngine</a></code>, <code><a href="velocity/PPTXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">PPTXEngine</a></code>, <code><a href="velocity/RTFEngine.html" title="class in com.nomagic.magicreport.engine.velocity">RTFEngine</a></code>, <code><a href="velocity/TextEngine.html" title="class in com.nomagic.magicreport.engine.velocity">TextEngine</a></code>, <code><a href="velocity/XLSXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">XLSXEngine</a></code>, <code><a href="velocity/XMLEngine.html" title="class in com.nomagic.magicreport.engine.velocity">XMLEngine</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ITemplateEngine</span></div>
<div class="block">Provides an interface for template engine.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 11, 2007</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#abort()">abort</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called by the application to abort current evaluation context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addContext(java.lang.String,java.lang.Object)">addContext</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a name/value pair to the context.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)">addInvalidReferenceHandler</a><wbr/>(<a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine">IInvalidReferenceHandler</a> handler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Add an invalid reference event handler to the engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)">addReferenceInsertionHandler</a><wbr/>(<a href="IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a> handler)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Add a reference insertion event handler to the engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../Template.html" title="class in com.nomagic.magicreport">Template</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTemplate()">createTemplate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Creates a new and empty <a href="../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> for generating report by this engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../Template.html" title="class in com.nomagic.magicreport">Template</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createTemplate(java.io.File,java.io.File)">createTemplate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> output)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Creates a new <a href="../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#destroy()">destroy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called by the application or <a href="../TemplateEngineFactory.html" title="class in com.nomagic.magicreport"><code>TemplateEngineFactory</code></a> to inform this engine
 that it should destroy any resources that it has allocated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#evaluate(com.nomagic.magicreport.Template)">evaluate</a><wbr/>(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Merge a template with current context and rendered stream into the writer.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getContext()">getContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return context of this engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../format/IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFormatter()">getFormatter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a formatter that can be used to create the object layout, and formats of state
 <a href="velocity/InsertionHandler.html" title="class in com.nomagic.magicreport.engine.velocity"><code>InsertionHandler</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine">IInvalidReferenceHandler</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInvalidReferenceHandler()">getInvalidReferenceHandler</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return a <a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IInvalidReferenceHandler</code></a> of this engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProperties()">getProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the current properties of engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProperty(java.lang.String)">getProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return an engine Runtime property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getReferenceInsertionHandler()">getReferenceInsertionHandler</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return a <a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IInvalidReferenceHandler</code></a> of this engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setProperty(java.lang.String,java.lang.Object)">setProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set an engine Runtime property.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="createTemplate()">
<h3>createTemplate</h3>
<div class="member-signature"><span class="return-type"><a href="../Template.html" title="class in com.nomagic.magicreport">Template</a></span> <span class="element-name">createTemplate</span>()</div>
<div class="block">Creates a new and empty <a href="../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> for generating report by this engine.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an instance of <a href="../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createTemplate(java.io.File,java.io.File)"><code>createTemplate(File, File)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplate(java.io.File,java.io.File)">
<h3>createTemplate</h3>
<div class="member-signature"><span class="return-type"><a href="../Template.html" title="class in com.nomagic.magicreport">Template</a></span> <span class="element-name">createTemplate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> output)</span>
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Creates a new <a href="../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - template file.</dd>
<dd><code>output</code> - output file.</dd>
<dt>Returns:</dt>
<dd>an instance of <a href="../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/FileNotFoundException.html" title="class or interface in java.io">FileNotFoundException</a></code> - if the file does not exist, is a directory rather than a regular file,
            or for some other reason cannot be opened.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFormatter()">
<h3>getFormatter</h3>
<div class="member-signature"><span class="return-type"><a href="../format/IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></span> <span class="element-name">getFormatter</span>()</div>
<div class="block">Returns a formatter that can be used to create the object layout, and formats of state
 <a href="velocity/InsertionHandler.html" title="class in com.nomagic.magicreport.engine.velocity"><code>InsertionHandler</code></a>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a formatter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContext()">
<h3>getContext</h3>
<div class="member-signature"><span class="return-type"><a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></span> <span class="element-name">getContext</span>()</div>
<div class="block">Return context of this engine.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a context of engine.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addContext(java.lang.String,java.lang.Object)">
<h3>addContext</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">addContext</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Adds a name/value pair to the context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - The name to key the provided value with.</dd>
<dd><code>value</code> - The corresponding value.</dd>
<dt>Returns:</dt>
<dd>The old object or null if there was no old object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperty(java.lang.String)">
<h3>getProperty</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div class="block">Return an engine Runtime property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - the property key</dd>
<dt>Returns:</dt>
<dd>the value in this property list with the specified key value.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setProperty(java.lang.String,java.lang.Object)"><code>setProperty(String, Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProperty(java.lang.String,java.lang.Object)">
<h3>setProperty</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Set an engine Runtime property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - the key to be placed into this property list.</dd>
<dd><code>value</code> - the value corresponding to key.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getProperty(java.lang.String)"><code>getProperty(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperties()">
<h3>getProperties</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></span> <span class="element-name">getProperties</span>()</div>
<div class="block">Returns the current properties of engine.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the engine properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)">
<h3>addReferenceInsertionHandler</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addReferenceInsertionHandler</span><wbr/><span class="parameters">(<a href="IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a> handler)</span></div>
<div class="block">Add a reference insertion event handler to the engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>handler</code> - ReferenceInsertionEventHandler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)">
<h3>addInvalidReferenceHandler</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addInvalidReferenceHandler</span><wbr/><span class="parameters">(<a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine">IInvalidReferenceHandler</a> handler)</span></div>
<div class="block">Add an invalid reference event handler to the engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>handler</code> - IInvalidReferenceHandler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInvalidReferenceHandler()">
<h3>getInvalidReferenceHandler</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine">IInvalidReferenceHandler</a>&gt;</span> <span class="element-name">getInvalidReferenceHandler</span>()</div>
<div class="block">Return a <a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IInvalidReferenceHandler</code></a> of this engine.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>invalid reference handler for this engine.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReferenceInsertionHandler()">
<h3>getReferenceInsertionHandler</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a>&gt;</span> <span class="element-name">getReferenceInsertionHandler</span>()</div>
<div class="block">Return a <a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IInvalidReferenceHandler</code></a> of this engine.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>reference insertion handler for this engine.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="evaluate(com.nomagic.magicreport.Template)">
<h3>evaluate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">evaluate</span><wbr/><span class="parameters">(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span>
       throws <span class="exceptions"><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Merge a template with current context and rendered stream into the writer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - Template being evaluated</dd>
<dt>Throws:</dt>
<dd><code><a href="../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
<dd><code><a href="../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - when engine initialize error</dd>
<dd><code><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="destroy()">
<h3>destroy</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">destroy</span>()</div>
<div class="block">Called by the application or <a href="../TemplateEngineFactory.html" title="class in com.nomagic.magicreport"><code>TemplateEngineFactory</code></a> to inform this engine
 that it should destroy any resources that it has allocated.</div>
</section>
</li>
<li>
<section class="detail" id="abort()">
<h3>abort</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">abort</span>()</div>
<div class="block">Called by the application to abort current evaluation context.</div>
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
