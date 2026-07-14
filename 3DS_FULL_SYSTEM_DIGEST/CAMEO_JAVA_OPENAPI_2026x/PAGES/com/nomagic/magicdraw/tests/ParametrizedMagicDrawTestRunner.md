# JAVA OPENAPI: ParametrizedMagicDrawTestRunner (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/tests/ParametrizedMagicDrawTestRunner.html
- source_path: `com/nomagic/magicdraw/tests/ParametrizedMagicDrawTestRunner.html`
- source_sha256: `daf2f19f11c704876c0a9f9b48167b4b9ffbbe895b30558333c227ee328f82eb`
- captured_utc: `2026-07-14T16:58:10.339674+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.tests](package-summary.html)

## Class ParametrizedMagicDrawTestRunner

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
org.junit.runner.Runner
org.junit.runners.ParentRunner<org.junit.runners.model.FrameworkMethod>
org.junit.runners.BlockJUnit4ClassRunner
junitparams.JUnitParamsRunner
com.nomagic.magicdraw.tests.ParametrizedMagicDrawTestRunner

All Implemented Interfaces:
`org.junit.runner.Describable`, `org.junit.runner.manipulation.Filterable`, `org.junit.runner.manipulation.Orderable`, `org.junit.runner.manipulation.Sortable`

@OpenApiAllpublic classParametrizedMagicDrawTestRunner
extends junitparams.JUnitParamsRunner

Test runner which starts application and checks for memory leaks after each test finish.
 To use this class annotate test class with such text:
 `@RunWith(ParametrizedMagicDrawTestRunner.class)`

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ParametrizedMagicDrawTestRunner](#%3Cinit%3E(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> aClass)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<org.junit.rules.TestRule>`
`[getTestRules](#getTestRules(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) target)`
Methods inherited from class junitparams.JUnitParamsRunner
`$, collectInitializationErrors, computeTestMethods, describeMethod, getDescription, methodInvoker, runChild`
Methods inherited from class org.junit.runners.BlockJUnit4ClassRunner
`createTest, createTest, describeChild, getChildren, isIgnored, methodBlock, possiblyExpectingExceptions, rules, testName, validateConstructor, validateFields, validateInstanceMethods, validateNoNonStaticInnerClass, validateOnlyOneConstructor, validateTestMethods, validateZeroArgConstructor, withAfters, withBefores, withPotentialTimeout`
Methods inherited from class org.junit.runners.ParentRunner
`childrenInvoker, classBlock, classRules, createTestClass, filter, getName, getRunnerAnnotations, getTestClass, order, run, runLeaf, setScheduler, sort, validatePublicVoidNoArgMethods, withAfterClasses, withBeforeClasses, withInterruptIsolation`
Methods inherited from class org.junit.runner.Runner
`testCount`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ParametrizedMagicDrawTestRunner
public ParametrizedMagicDrawTestRunner([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> aClass)
 throws org.junit.runners.model.InitializationError
Throws:
`org.junit.runners.model.InitializationError`
 ============ METHOD DETAIL ========== 
Method Details
getTestRules
protected [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<org.junit.rules.TestRule> getTestRules([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) target)
Overrides:
`getTestRules` in class `org.junit.runners.BlockJUnit4ClassRunner`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.tests</a></div>
<h1 class="title" title="Class ParametrizedMagicDrawTestRunner">Class ParametrizedMagicDrawTestRunner</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.junit.runner.Runner
<div class="inheritance">org.junit.runners.ParentRunner&lt;org.junit.runners.model.FrameworkMethod&gt;
<div class="inheritance">org.junit.runners.BlockJUnit4ClassRunner
<div class="inheritance">junitparams.JUnitParamsRunner
<div class="inheritance">com.nomagic.magicdraw.tests.ParametrizedMagicDrawTestRunner</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>org.junit.runner.Describable</code>, <code>org.junit.runner.manipulation.Filterable</code>, <code>org.junit.runner.manipulation.Orderable</code>, <code>org.junit.runner.manipulation.Sortable</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ParametrizedMagicDrawTestRunner</span>
<span class="extends-implements">extends junitparams.JUnitParamsRunner</span></div>
<div class="block">Test runner which starts application and checks for memory leaks after each test finish.
 To use this class annotate test class with such text:
 <code>@RunWith(ParametrizedMagicDrawTestRunner.class)</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class)">ParametrizedMagicDrawTestRunner</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; aClass)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;org.junit.rules.TestRule&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTestRules(java.lang.Object)">getTestRules</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-junitparams.JUnitParamsRunner">Methods inherited from class junitparams.JUnitParamsRunner</h3>
<code>$, collectInitializationErrors, computeTestMethods, describeMethod, getDescription, methodInvoker, runChild</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.junit.runners.BlockJUnit4ClassRunner">Methods inherited from class org.junit.runners.BlockJUnit4ClassRunner</h3>
<code>createTest, createTest, describeChild, getChildren, isIgnored, methodBlock, possiblyExpectingExceptions, rules, testName, validateConstructor, validateFields, validateInstanceMethods, validateNoNonStaticInnerClass, validateOnlyOneConstructor, validateTestMethods, validateZeroArgConstructor, withAfters, withBefores, withPotentialTimeout</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.junit.runners.ParentRunner">Methods inherited from class org.junit.runners.ParentRunner</h3>
<code>childrenInvoker, classBlock, classRules, createTestClass, filter, getName, getRunnerAnnotations, getTestClass, order, run, runLeaf, setScheduler, sort, validatePublicVoidNoArgMethods, withAfterClasses, withBeforeClasses, withInterruptIsolation</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.junit.runner.Runner">Methods inherited from class org.junit.runner.Runner</h3>
<code>testCount</code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.Class)">
<h3>ParametrizedMagicDrawTestRunner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ParametrizedMagicDrawTestRunner</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; aClass)</span>
                                throws <span class="exceptions">org.junit.runners.model.InitializationError</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>org.junit.runners.model.InitializationError</code></dd>
</dl>
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
<section class="detail" id="getTestRules(java.lang.Object)">
<h3>getTestRules</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;org.junit.rules.TestRule&gt;</span> <span class="element-name">getTestRules</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getTestRules</code> in class <code>org.junit.runners.BlockJUnit4ClassRunner</code></dd>
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
