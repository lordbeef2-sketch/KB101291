# JAVA OPENAPI: MDExtensions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/foundation/util/MDExtensions.html
- source_path: `com/nomagic/magicdraw/foundation/util/MDExtensions.html`
- source_sha256: `edb7d0889087f77c18eb87ac824f9a6d276555ecc1777cd7e7b93081d4851982`
- captured_utc: `2026-07-14T16:45:36.926493+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.foundation.util](package-summary.html)

## Class MDExtensions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.foundation.util.MDExtensions

public classMDExtensions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Helper methods to work with element extensions (MDExtension)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MDExtensions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [MDExtension](../MDExtension.html)`
`[createMDExtension](#createMDExtension(com.nomagic.magicdraw.foundation.MDObject,java.lang.String))([MDObject](../MDObject.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extensionSource)`
Creates new element extension, but only if it not yet exists
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EObject>`
`[getExtensionContents](#getExtensionContents(com.nomagic.magicdraw.foundation.MDObject,java.lang.String))([MDObject](../MDObject.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)`
Get MDExtension contents for the given element.
`static [MDExtension](../MDExtension.html)`
`[getMDExtension](#getMDExtension(com.nomagic.magicdraw.foundation.MDObject,java.lang.String))([MDObject](../MDObject.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)`
Get MDExtension for the given source.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MDExtension](../MDExtension.html)>`
`[getMDExtensions](#getMDExtensions(com.nomagic.magicdraw.foundation.MDObject))([MDObject](../MDObject.html) object)`
Get MDExtensions of element.
`static void`
`[removeExtension](#removeExtension(com.nomagic.magicdraw.foundation.MDObject,java.lang.String))([MDObject](../MDObject.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extensionSource)`
Completely removes given extension from element
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MDExtensions
public MDExtensions()
 ============ METHOD DETAIL ========== 
Method Details
getMDExtensions
@CheckForNullpublic static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MDExtension](../MDExtension.html)> getMDExtensions([MDObject](../MDObject.html) object)
Get MDExtensions of element.
Parameters:
`object` - MDObject.
Returns:
MDExtensions.
getExtensionContents
@CheckForNullpublic static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<org.eclipse.emf.ecore.EObject> getExtensionContents([MDObject](../MDObject.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)
Get MDExtension contents for the given element.
Parameters:
`object` - MDObject.
`source` - extension source string (identifier)
Returns:
contents of MDExtension
getMDExtension
@CheckForNullpublic static [MDExtension](../MDExtension.html) getMDExtension([MDObject](../MDObject.html) object,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)
Get MDExtension for the given source.
Parameters:
`object` - MDObject.
`source` - extension source.
Returns:
MDExtension of the given element with provided source set or null, if no such extension exists
createMDExtension
public static [MDExtension](../MDExtension.html) createMDExtension([MDObject](../MDObject.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extensionSource)
Creates new element extension, but only if it not yet exists
Parameters:
`object` - MDObject to create extension for
`extensionSource` - extension source string (identifier)
Returns:
existing or new created extension.
removeExtension
public static void removeExtension([MDObject](../MDObject.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extensionSource)
Completely removes given extension from element

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.foundation.util</a></div>
<h1 class="title" title="Class MDExtensions">Class MDExtensions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.foundation.util.MDExtensions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">MDExtensions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Helper methods to work with element extensions (MDExtension)</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MDExtensions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../MDExtension.html" title="interface in com.nomagic.magicdraw.foundation">MDExtension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMDExtension(com.nomagic.magicdraw.foundation.MDObject,java.lang.String)">createMDExtension</a><wbr/>(<a href="../MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extensionSource)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates new element extension, but only if it not yet exists</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;org.eclipse.emf.ecore.EObject&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtensionContents(com.nomagic.magicdraw.foundation.MDObject,java.lang.String)">getExtensionContents</a><wbr/>(<a href="../MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get MDExtension contents for the given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../MDExtension.html" title="interface in com.nomagic.magicdraw.foundation">MDExtension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMDExtension(com.nomagic.magicdraw.foundation.MDObject,java.lang.String)">getMDExtension</a><wbr/>(<a href="../MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get MDExtension for the given source.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../MDExtension.html" title="interface in com.nomagic.magicdraw.foundation">MDExtension</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMDExtensions(com.nomagic.magicdraw.foundation.MDObject)">getMDExtensions</a><wbr/>(<a href="../MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get MDExtensions of element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeExtension(com.nomagic.magicdraw.foundation.MDObject,java.lang.String)">removeExtension</a><wbr/>(<a href="../MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extensionSource)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Completely removes given extension from element</div>
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
<h3>MDExtensions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MDExtensions</span>()</div>
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
<section class="detail" id="getMDExtensions(com.nomagic.magicdraw.foundation.MDObject)">
<h3>getMDExtensions</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../MDExtension.html" title="interface in com.nomagic.magicdraw.foundation">MDExtension</a>&gt;</span> <span class="element-name">getMDExtensions</span><wbr/><span class="parameters">(<a href="../MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> object)</span></div>
<div class="block">Get MDExtensions of element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - MDObject.</dd>
<dt>Returns:</dt>
<dd>MDExtensions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtensionContents(com.nomagic.magicdraw.foundation.MDObject,java.lang.String)">
<h3>getExtensionContents</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.eclipse.emf.ecore.EObject&gt;</span> <span class="element-name">getExtensionContents</span><wbr/><span class="parameters">(<a href="../MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</span></div>
<div class="block">Get MDExtension contents for the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - MDObject.</dd>
<dd><code>source</code> - extension source string (identifier)</dd>
<dt>Returns:</dt>
<dd>contents of MDExtension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDExtension(com.nomagic.magicdraw.foundation.MDObject,java.lang.String)">
<h3>getMDExtension</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../MDExtension.html" title="interface in com.nomagic.magicdraw.foundation">MDExtension</a></span> <span class="element-name">getMDExtension</span><wbr/><span class="parameters">(<a href="../MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> object,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</span></div>
<div class="block">Get MDExtension for the given source.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - MDObject.</dd>
<dd><code>source</code> - extension source.</dd>
<dt>Returns:</dt>
<dd>MDExtension of the given element with provided source set or null, if no such extension exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMDExtension(com.nomagic.magicdraw.foundation.MDObject,java.lang.String)">
<h3>createMDExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../MDExtension.html" title="interface in com.nomagic.magicdraw.foundation">MDExtension</a></span> <span class="element-name">createMDExtension</span><wbr/><span class="parameters">(<a href="../MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extensionSource)</span></div>
<div class="block">Creates new element extension, but only if it not yet exists</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - MDObject to create extension for</dd>
<dd><code>extensionSource</code> - extension source string (identifier)</dd>
<dt>Returns:</dt>
<dd>existing or new created extension.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeExtension(com.nomagic.magicdraw.foundation.MDObject,java.lang.String)">
<h3>removeExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeExtension</span><wbr/><span class="parameters">(<a href="../MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extensionSource)</span></div>
<div class="block">Completely removes given extension from element</div>
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
