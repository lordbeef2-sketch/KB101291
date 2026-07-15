# JAVA OPENAPI: FileSearchFactory (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/helper/file/FileSearchFactory.html
- source_path: `com/nomagic/magicreport/helper/file/FileSearchFactory.html`
- source_sha256: `742a51d5d45f1b02d356d0f5dba4d37752d4af77890d00130b624c3158892478`
- captured_utc: `2026-07-14T16:46:14.598999+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.helper.file](package-summary.html)

## Class FileSearchFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.helper.file.FileSearchFactory

@OpenApiAllpublic final classFileSearchFactory
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Create custom file search.
 Since a file can be defined in other object besides String of path or File.
 
 So, this class allow you to add custom IFileSearch class for searching file from custom object using given name and location.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[IFileSearch](IFileSearch.html)>`
`[getFileSearchClass](#getFileSearchClass())()`
Create and return all instance of IFileSearch.
`static [FileSearchFactory](FileSearchFactory.html)`
`[getInstance](#getInstance())()`
Return instance of this class.
`boolean`
`[registerFileSearchClass](#registerFileSearchClass(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [IFileSearch](IFileSearch.html)> fileSearchClass)`
Registers the given class name with the [`FileSearchFactory`](FileSearchFactory.html)
`boolean`
`[unregisterFileSearchClass](#unregisterFileSearchClass(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [IFileSearch](IFileSearch.html)> fileSearchClass)`
Unregister the given file search class.
`boolean`
`[unregisterFileSearchClass](#unregisterFileSearchClass(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) className)`
Unregister the given file search class name.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
public static [FileSearchFactory](FileSearchFactory.html) getInstance()
Return instance of this class.
Returns:
instance of this class.
registerFileSearchClass
public boolean registerFileSearchClass([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [IFileSearch](IFileSearch.html)> fileSearchClass)
Registers the given class name with the [`FileSearchFactory`](FileSearchFactory.html)
Parameters:
`fileSearchClass` - the new [`IFileSearch`](IFileSearch.html) that is to be registered with the
 [`FileSearchFactory`](FileSearchFactory.html)
Returns:
true if register successful
unregisterFileSearchClass
public boolean unregisterFileSearchClass([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [IFileSearch](IFileSearch.html)> fileSearchClass)
Unregister the given file search class.
Parameters:
`fileSearchClass` - file search class.
Returns:
true if unregister successful
unregisterFileSearchClass
public boolean unregisterFileSearchClass([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) className)
Unregister the given file search class name.
Parameters:
`className` - class name with its package e.g., com.nomagic.magicreport.helper.file.MyFileSearch
Returns:
true if unregister successful
getFileSearchClass
public [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[IFileSearch](IFileSearch.html)> getFileSearchClass()
Create and return all instance of IFileSearch.
Returns:
a list of IFileSearch instance.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.helper.file</a></div>
<h1 class="title" title="Class FileSearchFactory">Class FileSearchFactory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.helper.file.FileSearchFactory</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">FileSearchFactory</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Create custom file search.
 Since a file can be defined in other object besides String of path or File.
 
 So, this class allow you to add custom IFileSearch class for searching file from custom object using given name and location.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a href="IFileSearch.html" title="interface in com.nomagic.magicreport.helper.file">IFileSearch</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileSearchClass()">getFileSearchClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create and return all instance of IFileSearch.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="FileSearchFactory.html" title="class in com.nomagic.magicreport.helper.file">FileSearchFactory</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return instance of this class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerFileSearchClass(java.lang.Class)">registerFileSearchClass</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="IFileSearch.html" title="interface in com.nomagic.magicreport.helper.file">IFileSearch</a>&gt; fileSearchClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers the given class name with the <a href="FileSearchFactory.html" title="class in com.nomagic.magicreport.helper.file"><code>FileSearchFactory</code></a></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterFileSearchClass(java.lang.Class)">unregisterFileSearchClass</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="IFileSearch.html" title="interface in com.nomagic.magicreport.helper.file">IFileSearch</a>&gt; fileSearchClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregister the given file search class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterFileSearchClass(java.lang.String)">unregisterFileSearchClass</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> className)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregister the given file search class name.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="FileSearchFactory.html" title="class in com.nomagic.magicreport.helper.file">FileSearchFactory</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Return instance of this class.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance of this class.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerFileSearchClass(java.lang.Class)">
<h3>registerFileSearchClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">registerFileSearchClass</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="IFileSearch.html" title="interface in com.nomagic.magicreport.helper.file">IFileSearch</a>&gt; fileSearchClass)</span></div>
<div class="block">Registers the given class name with the <a href="FileSearchFactory.html" title="class in com.nomagic.magicreport.helper.file"><code>FileSearchFactory</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileSearchClass</code> - the new <a href="IFileSearch.html" title="interface in com.nomagic.magicreport.helper.file"><code>IFileSearch</code></a> that is to be registered with the
           <a href="FileSearchFactory.html" title="class in com.nomagic.magicreport.helper.file"><code>FileSearchFactory</code></a></dd>
<dt>Returns:</dt>
<dd>true if register successful</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregisterFileSearchClass(java.lang.Class)">
<h3>unregisterFileSearchClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">unregisterFileSearchClass</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="IFileSearch.html" title="interface in com.nomagic.magicreport.helper.file">IFileSearch</a>&gt; fileSearchClass)</span></div>
<div class="block">Unregister the given file search class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileSearchClass</code> - file search class.</dd>
<dt>Returns:</dt>
<dd>true if unregister successful</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregisterFileSearchClass(java.lang.String)">
<h3>unregisterFileSearchClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">unregisterFileSearchClass</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> className)</span></div>
<div class="block">Unregister the given file search class name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>className</code> - class name with its package e.g., com.nomagic.magicreport.helper.file.MyFileSearch</dd>
<dt>Returns:</dt>
<dd>true if unregister successful</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileSearchClass()">
<h3>getFileSearchClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="IFileSearch.html" title="interface in com.nomagic.magicreport.helper.file">IFileSearch</a>&gt;</span> <span class="element-name">getFileSearchClass</span>()</div>
<div class="block">Create and return all instance of IFileSearch.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of IFileSearch instance.</dd>
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
