# JAVA OPENAPI: Payloads (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Payloads.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Payloads.html`
- source_sha256: `b0478851fd625b7ba70c970e791b8d7a6a57124b59fc039dacd5421a89818ae2`
- captured_utc: `2026-07-14T16:44:48.094844+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Payloads

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Payloads

@OpenApiAllpublic classPayloads
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with payloads in [`Flow`](kerml/Flow.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static final record`
`[Payloads.Features](Payloads.Features.html)`
Immutable container for directional payload features.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Payloads](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Feature](kerml/Feature.html)`
`[getPayload](#getPayload(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns the payload feature of the given type, if any.
`static [Feature](kerml/Feature.html)`
`[getPayload](#getPayload(com.dassault_systemes.modeler.kerml.model.PayloadsParams))([PayloadsParams](PayloadsParams.html) params)`
Resolves the payload feature for the flow-like type described by the given parameters.
`static [Payloads.Features](Payloads.Features.html)`
`[getPayloadFeatures](#getPayloadFeatures(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Type](kerml/Type.html) relationship,
 [Feature](kerml/Feature.html) end)`
Returns payload features for a relationship relative to a specific end.
`static [Payloads.Features](Payloads.Features.html)`
`[getPayloadFeaturesForBinary](#getPayloadFeaturesForBinary(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) relationship)`
Returns payload features for a binary relationship (exactly two ends).
`static boolean`
`[isPayload](#isPayload(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the given feature is a payload feature.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Payloads
public Payloads()
 ============ METHOD DETAIL ========== 
Method Details
getPayloadFeaturesForBinary
public static [Payloads.Features](Payloads.Features.html) getPayloadFeaturesForBinary([Type](kerml/Type.html) relationship)
Returns payload features for a binary relationship (exactly two ends).
 Payloads are grouped into source→target and target→source directions.
Parameters:
`relationship` - the relationship whose payloads are requested
Returns:
a Features object containing directional payload lists
getPayloadFeatures
public static [Payloads.Features](Payloads.Features.html) getPayloadFeatures([Type](kerml/Type.html) relationship,
 [Feature](kerml/Feature.html) end)
Returns payload features for a relationship relative to a specific end.
 Payloads are grouped into source→target and target→source directions.
Parameters:
`relationship` - the relationship whose payloads are requested
`end` - the end feature used as reference
Returns:
a Features object containing directional payload lists
isPayload
public static boolean isPayload([Feature](kerml/Feature.html) feature)
Checks whether the given feature is a payload feature.
Parameters:
`feature` - the feature to check
Returns:
true if the feature is a payload
getPayload
@CheckForNullpublic static [Feature](kerml/Feature.html) getPayload([Type](kerml/Type.html) type)
Returns the payload feature of the given type, if any.
Parameters:
`type` - the type to inspect
Returns:
the payload feature, or null if none exists
getPayload
@CheckForNullpublic static [Feature](kerml/Feature.html) getPayload([PayloadsParams](PayloadsParams.html) params)
Resolves the payload feature for the flow-like type described by the given parameters.
 This method performs a multi‑step lookup:
 If the type is a [`Flow`](kerml/Flow.html), its explicitly declared payload feature is returned.
Otherwise, the method attempts to locate an owned feature whose type matches the
 standard library payload type (or a redefinition of it).
If no owned payload is found, inherited features are searched, subject to standard
 library filtering rules.
If `create` is enabled in the parameters, a new payload feature is created,
 optionally redefining an inherited payload.
This method supports advanced scenarios such as:
 distinguishing between owned and inherited payloads,
respecting standard library boundaries,
creating redefining payload features when needed, and
handling both [`PayloadFeature`](kerml/PayloadFeature.html) instances and typed features.
If no payload can be resolved and creation is not requested, this method returns `null`.
Parameters:
`params` - configuration describing how payload lookup and creation should behave
Returns:
the resolved or newly created payload feature, or `null` if none exists

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Payloads">Class Payloads</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Payloads</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Payloads</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with payloads in <a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Flow</code></a></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final record </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Payloads.Features.html" title="class in com.dassault_systemes.modeler.kerml.model">Payloads.Features</a></code></div>
<div class="col-last even-row-color">
<div class="block">Immutable container for directional payload features.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Payloads</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPayload(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getPayload</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the payload feature of the given type, if any.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPayload(com.dassault_systemes.modeler.kerml.model.PayloadsParams)">getPayload</a><wbr/>(<a href="PayloadsParams.html" title="class in com.dassault_systemes.modeler.kerml.model">PayloadsParams</a> params)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Resolves the payload feature for the flow-like type described by the given parameters.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Payloads.Features.html" title="class in com.dassault_systemes.modeler.kerml.model">Payloads.Features</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPayloadFeatures(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getPayloadFeatures</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> relationship,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns payload features for a relationship relative to a specific end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Payloads.Features.html" title="class in com.dassault_systemes.modeler.kerml.model">Payloads.Features</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPayloadFeaturesForBinary(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getPayloadFeaturesForBinary</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> relationship)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns payload features for a binary relationship (exactly two ends).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPayload(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isPayload</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given feature is a payload feature.</div>
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
<h3>Payloads</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Payloads</span>()</div>
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
<section class="detail" id="getPayloadFeaturesForBinary(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getPayloadFeaturesForBinary</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Payloads.Features.html" title="class in com.dassault_systemes.modeler.kerml.model">Payloads.Features</a></span> <span class="element-name">getPayloadFeaturesForBinary</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> relationship)</span></div>
<div class="block">Returns payload features for a binary relationship (exactly two ends).
 Payloads are grouped into source→target and target→source directions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - the relationship whose payloads are requested</dd>
<dt>Returns:</dt>
<dd>a Features object containing directional payload lists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPayloadFeatures(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getPayloadFeatures</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Payloads.Features.html" title="class in com.dassault_systemes.modeler.kerml.model">Payloads.Features</a></span> <span class="element-name">getPayloadFeatures</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> relationship,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</span></div>
<div class="block">Returns payload features for a relationship relative to a specific end.
 Payloads are grouped into source→target and target→source directions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - the relationship whose payloads are requested</dd>
<dd><code>end</code> - the end feature used as reference</dd>
<dt>Returns:</dt>
<dd>a Features object containing directional payload lists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPayload(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isPayload</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPayload</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the given feature is a payload feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature to check</dd>
<dt>Returns:</dt>
<dd>true if the feature is a payload</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPayload(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getPayload</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getPayload</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the payload feature of the given type, if any.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>the payload feature, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPayload(com.dassault_systemes.modeler.kerml.model.PayloadsParams)">
<h3>getPayload</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getPayload</span><wbr/><span class="parameters">(<a href="PayloadsParams.html" title="class in com.dassault_systemes.modeler.kerml.model">PayloadsParams</a> params)</span></div>
<div class="block">Resolves the payload feature for the flow-like type described by the given parameters.
 <p>
 This method performs a multi‑step lookup:
 <ol>
<li>If the type is a <a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Flow</code></a>, its explicitly declared payload feature is returned.</li>
<li>Otherwise, the method attempts to locate an owned feature whose type matches the
       standard library payload type (or a redefinition of it).</li>
<li>If no owned payload is found, inherited features are searched, subject to standard
       library filtering rules.</li>
<li>If <code>create</code> is enabled in the parameters, a new payload feature is created,
       optionally redefining an inherited payload.</li>
</ol>
<p>
 This method supports advanced scenarios such as:
 <ul>
<li>distinguishing between owned and inherited payloads,</li>
<li>respecting standard library boundaries,</li>
<li>creating redefining payload features when needed, and</li>
<li>handling both <a href="kerml/PayloadFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>PayloadFeature</code></a> instances and typed features.</li>
</ul>
<p>
 If no payload can be resolved and creation is not requested, this method returns <code>null</code>.</p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>params</code> - configuration describing how payload lookup and creation should behave</dd>
<dt>Returns:</dt>
<dd>the resolved or newly created payload feature, or <code>null</code> if none exists</dd>
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
