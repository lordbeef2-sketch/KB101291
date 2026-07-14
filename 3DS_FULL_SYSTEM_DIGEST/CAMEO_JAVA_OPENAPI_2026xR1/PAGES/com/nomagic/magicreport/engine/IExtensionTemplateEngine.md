# JAVA OPENAPI: IExtensionTemplateEngine (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/IExtensionTemplateEngine.html
- source_path: `com/nomagic/magicreport/engine/IExtensionTemplateEngine.html`
- source_sha256: `d5bd7b06ce0a64d72bbdef37b4597386f2e63abd4bae270fe55aaf9908f3d865`
- captured_utc: `2026-07-14T16:46:11.739957+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Interface IExtensionTemplateEngine

All Known Implementing Classes:
`[DefaultTemplateEngine](velocity/DefaultTemplateEngine.html)`, `[DocBookEngine](velocity/DocBookEngine.html)`, `[DOCXEngine](velocity/DOCXEngine.html)`, `[HTMLEngine](velocity/HTMLEngine.html)`, `[LaTeXEngine](velocity/LaTeXEngine.html)`, `[PPTXEngine](velocity/PPTXEngine.html)`, `[RTFEngine](velocity/RTFEngine.html)`, `[TextEngine](velocity/TextEngine.html)`, `[XLSXEngine](velocity/XLSXEngine.html)`, `[XMLEngine](velocity/XMLEngine.html)`

@OpenApiAllpublic interfaceIExtensionTemplateEngine

The IExtensionTemplateEngine is used by an extension template engine. It provides the following type of
 functionality:
 Custom Class Loader

Since:
Mar 11, 2008

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html)`
`[getClassLoader](#getClassLoader())()`
Returns the class loader for the engine.
`void`
`[setClassLoader](#setClassLoader(java.lang.ClassLoader))([ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html) loader)`
Sets the class loader for this engine.

============ METHOD DETAIL ========== 
Method Details
getClassLoader
[ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html) getClassLoader()
Returns the class loader for the engine. This method will return null in such implementations if this class
 was loaded by the application class loader.
Returns:
the class loader that loaded the class or interface represented by this object.
setClassLoader
void setClassLoader([ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html) loader)
Sets the class loader for this engine. The class loader must be set before a template is evaluated. This
 method allows the creator of the template to provide the appropriate class loader to code running in the
 template when loading classes and resources.
Parameters:
`loader` - Class loader for this engine

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Interface IExtensionTemplateEngine">Interface IExtensionTemplateEngine</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="velocity/DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code>, <code><a href="velocity/DocBookEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DocBookEngine</a></code>, <code><a href="velocity/DOCXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine</a></code>, <code><a href="velocity/HTMLEngine.html" title="class in com.nomagic.magicreport.engine.velocity">HTMLEngine</a></code>, <code><a href="velocity/LaTeXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">LaTeXEngine</a></code>, <code><a href="velocity/PPTXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">PPTXEngine</a></code>, <code><a href="velocity/RTFEngine.html" title="class in com.nomagic.magicreport.engine.velocity">RTFEngine</a></code>, <code><a href="velocity/TextEngine.html" title="class in com.nomagic.magicreport.engine.velocity">TextEngine</a></code>, <code><a href="velocity/XLSXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">XLSXEngine</a></code>, <code><a href="velocity/XMLEngine.html" title="class in com.nomagic.magicreport.engine.velocity">XMLEngine</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IExtensionTemplateEngine</span></div>
<div class="block">The IExtensionTemplateEngine is used by an extension template engine. It provides the following type of
 functionality:
 <ul>
<li>Custom Class Loader</li>
</ul></div>
<dl class="notes">
<dt>Since:</dt>
<dd>Mar 11, 2008</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getClassLoader()">getClassLoader</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the class loader for the engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setClassLoader(java.lang.ClassLoader)">setClassLoader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> loader)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the class loader for this engine.</div>
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
<section class="detail" id="getClassLoader()">
<h3>getClassLoader</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a></span> <span class="element-name">getClassLoader</span>()</div>
<div class="block">Returns the class loader for the engine. This method will return null in such implementations if this class
 was loaded by the application class loader.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the class loader that loaded the class or interface represented by this object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClassLoader(java.lang.ClassLoader)">
<h3>setClassLoader</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setClassLoader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> loader)</span></div>
<div class="block">Sets the class loader for this engine. The class loader must be set before a template is evaluated. This
 method allows the creator of the template to provide the appropriate class loader to code running in the
 template when loading classes and resources.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>loader</code> - Class loader for this engine</dd>
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
