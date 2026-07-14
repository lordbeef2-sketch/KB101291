# JAVA OPENAPI: MagicDrawApplication (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/tests/MagicDrawApplication.html
- source_path: `com/nomagic/magicdraw/tests/MagicDrawApplication.html`
- source_sha256: `570325caccf2f27fe0d3a1184a9c14c2426e77f429e70c8eb7bd71dcaa72e9f3`
- captured_utc: `2026-07-14T16:51:48.388564+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.tests](package-summary.html)

## Class MagicDrawApplication

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.tests.MagicDrawApplication

All Implemented Interfaces:
`org.junit.jupiter.api.extension.AfterAllCallback`, `org.junit.jupiter.api.extension.BeforeAllCallback`, `org.junit.jupiter.api.extension.Extension`

@OpenApiAllpublic classMagicDrawApplication
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements org.junit.jupiter.api.extension.BeforeAllCallback, org.junit.jupiter.api.extension.AfterAllCallback

Extend with this extension to run JUnit5 test group with MagicDraw application started. Usage example:

````java
@ExtendWith(MagicDrawApplication.class)
 class TestWithMagicDraw {
     @Test
     void test() {
     //your test code here
     }
 }
````

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MagicDrawApplication](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[afterAll](#afterAll(org.junit.jupiter.api.extension.ExtensionContext))(org.junit.jupiter.api.extension.ExtensionContext context)`
After all tests MagicDraw application will not be stopped as it might be needed for further test classes.
`void`
`[beforeAll](#beforeAll(org.junit.jupiter.api.extension.ExtensionContext))(org.junit.jupiter.api.extension.ExtensionContext context)`
Starts MagicDraw application before all tests.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MagicDrawApplication
public MagicDrawApplication()
 ============ METHOD DETAIL ========== 
Method Details
beforeAll
public void beforeAll(org.junit.jupiter.api.extension.ExtensionContext context)
Starts MagicDraw application before all tests.
Specified by:
`beforeAll` in interface `org.junit.jupiter.api.extension.BeforeAllCallback`
afterAll
public void afterAll(org.junit.jupiter.api.extension.ExtensionContext context)
After all tests MagicDraw application will not be stopped as it might be needed for further test classes.
 This method only prints info about the current memory usage of the application.
Specified by:
`afterAll` in interface `org.junit.jupiter.api.extension.AfterAllCallback`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.tests</a></div>
<h1 class="title" title="Class MagicDrawApplication">Class MagicDrawApplication</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.tests.MagicDrawApplication</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>org.junit.jupiter.api.extension.AfterAllCallback</code>, <code>org.junit.jupiter.api.extension.BeforeAllCallback</code>, <code>org.junit.jupiter.api.extension.Extension</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MagicDrawApplication</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements org.junit.jupiter.api.extension.BeforeAllCallback, org.junit.jupiter.api.extension.AfterAllCallback</span></div>
<div class="block">Extend with this extension to run JUnit5 test group with MagicDraw application started. Usage example:
<pre><code>
 @ExtendWith(MagicDrawApplication.class)
 class TestWithMagicDraw {
     @Test
     void test() {
     //your test code here
     }
 }
</code></pre></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MagicDrawApplication</a>()</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#afterAll(org.junit.jupiter.api.extension.ExtensionContext)">afterAll</a><wbr/>(org.junit.jupiter.api.extension.ExtensionContext context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">After all tests MagicDraw application will not be stopped as it might be needed for further test classes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#beforeAll(org.junit.jupiter.api.extension.ExtensionContext)">beforeAll</a><wbr/>(org.junit.jupiter.api.extension.ExtensionContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts MagicDraw application before all tests.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>MagicDrawApplication</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MagicDrawApplication</span>()</div>
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
<section class="detail" id="beforeAll(org.junit.jupiter.api.extension.ExtensionContext)">
<h3>beforeAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">beforeAll</span><wbr/><span class="parameters">(org.junit.jupiter.api.extension.ExtensionContext context)</span></div>
<div class="block">Starts MagicDraw application before all tests.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>beforeAll</code> in interface <code>org.junit.jupiter.api.extension.BeforeAllCallback</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="afterAll(org.junit.jupiter.api.extension.ExtensionContext)">
<h3>afterAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">afterAll</span><wbr/><span class="parameters">(org.junit.jupiter.api.extension.ExtensionContext context)</span></div>
<div class="block">After all tests MagicDraw application will not be stopped as it might be needed for further test classes.
 This method only prints info about the current memory usage of the application.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>afterAll</code> in interface <code>org.junit.jupiter.api.extension.AfterAllCallback</code></dd>
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
