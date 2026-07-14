# JAVA OPENAPI: ParametersParams (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/ParametersParams.html
- source_path: `com/dassault_systemes/modeler/kerml/model/ParametersParams.html`
- source_sha256: `d495bcc54b51db7566432b7167525165f9102f3bba68bd8052ef326326265d1f`
- captured_utc: `2026-07-14T16:44:48.009843+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class ParametersParams

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.ParametersParams

@OpenApiAllpublic classParametersParams
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Params class for working with [`Parameters`](Parameters.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ParametersParams](#%3Cinit%3E(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[FeatureDirectionKind](kerml/FeatureDirectionKind.html)`
`[getDirection](#getDirection())()`

`[Type](kerml/Type.html)`
`[getType](#getType())()`

`boolean`
`[isIncludeReturn](#isIncludeReturn())()`

`boolean`
`[isOwned](#isOwned())()`

`static boolean`
`[isStepOrBehavior](#isStepOrBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`

`boolean`
`[isTypeStepOrBehavior](#isTypeStepOrBehavior())()`

`[ParametersParams](ParametersParams.html)`
`[setDirection](#setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind))([FeatureDirectionKind](kerml/FeatureDirectionKind.html) direction)`

`[ParametersParams](ParametersParams.html)`
`[setIncludeReturn](#setIncludeReturn(boolean))(boolean includeReturn)`

`[ParametersParams](ParametersParams.html)`
`[setOwned](#setOwned(boolean))(boolean owned)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ParametersParams
public ParametersParams([Type](kerml/Type.html) type)
 ============ METHOD DETAIL ========== 
Method Details
getType
public [Type](kerml/Type.html) getType()
isTypeStepOrBehavior
public boolean isTypeStepOrBehavior()
setOwned
public [ParametersParams](ParametersParams.html) setOwned(boolean owned)
isOwned
public boolean isOwned()
isIncludeReturn
public boolean isIncludeReturn()
setIncludeReturn
public [ParametersParams](ParametersParams.html) setIncludeReturn(boolean includeReturn)
getDirection
public [FeatureDirectionKind](kerml/FeatureDirectionKind.html) getDirection()
setDirection
public [ParametersParams](ParametersParams.html) setDirection([FeatureDirectionKind](kerml/FeatureDirectionKind.html) direction)
isStepOrBehavior
public static boolean isStepOrBehavior(@CheckForNull
 [Type](kerml/Type.html) type)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class ParametersParams">Class ParametersParams</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.ParametersParams</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ParametersParams</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Params class for working with <a href="Parameters.html" title="class in com.dassault_systemes.modeler.kerml.model"><code>Parameters</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.dassault_systemes.modeler.kerml.model.kerml.Type)">ParametersParams</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirection()">getDirection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isIncludeReturn()">isIncludeReturn</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOwned()">isOwned</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStepOrBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isStepOrBehavior</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeStepOrBehavior()">isTypeStepOrBehavior</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ParametersParams.html" title="class in com.dassault_systemes.modeler.kerml.model">ParametersParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)">setDirection</a><wbr/>(<a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a> direction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ParametersParams.html" title="class in com.dassault_systemes.modeler.kerml.model">ParametersParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIncludeReturn(boolean)">setIncludeReturn</a><wbr/>(boolean includeReturn)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ParametersParams.html" title="class in com.dassault_systemes.modeler.kerml.model">ParametersParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOwned(boolean)">setOwned</a><wbr/>(boolean owned)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="&lt;init&gt;(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>ParametersParams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ParametersParams</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
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
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">getType</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isTypeStepOrBehavior()">
<h3>isTypeStepOrBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeStepOrBehavior</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setOwned(boolean)">
<h3>setOwned</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ParametersParams.html" title="class in com.dassault_systemes.modeler.kerml.model">ParametersParams</a></span> <span class="element-name">setOwned</span><wbr/><span class="parameters">(boolean owned)</span></div>
</section>
</li>
<li>
<section class="detail" id="isOwned()">
<h3>isOwned</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOwned</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isIncludeReturn()">
<h3>isIncludeReturn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isIncludeReturn</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setIncludeReturn(boolean)">
<h3>setIncludeReturn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ParametersParams.html" title="class in com.dassault_systemes.modeler.kerml.model">ParametersParams</a></span> <span class="element-name">setIncludeReturn</span><wbr/><span class="parameters">(boolean includeReturn)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDirection()">
<h3>getDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">getDirection</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)">
<h3>setDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ParametersParams.html" title="class in com.dassault_systemes.modeler.kerml.model">ParametersParams</a></span> <span class="element-name">setDirection</span><wbr/><span class="parameters">(<a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a> direction)</span></div>
</section>
</li>
<li>
<section class="detail" id="isStepOrBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isStepOrBehavior</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStepOrBehavior</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
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
