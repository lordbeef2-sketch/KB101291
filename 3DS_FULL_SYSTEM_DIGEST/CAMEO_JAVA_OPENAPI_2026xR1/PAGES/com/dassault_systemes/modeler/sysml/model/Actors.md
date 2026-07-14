# JAVA OPENAPI: Actors (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Actors.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Actors.html`
- source_sha256: `6430c40cc48242a2ba2127c9936784a9ecf2ad2850c19c84ff9b03f03b322514`
- captured_utc: `2026-07-14T16:45:02.090029+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Actors

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Actors

@OpenApiAllpublic classActors
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility methods for identifying actor parameters and actor memberships on
 requirements, cases, and related types. Actors are represented as
 [`PartUsage`](sysml/PartUsage.html) elements owned through [`ActorMembership`](sysml/ActorMembership.html).

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Actors](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](sysml/PartUsage.html)>`
`[getActorParameter](#getActorParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the actor parameters of the given type.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](sysml/PartUsage.html)>`
`[getOwnedActorParameter](#getOwnedActorParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the actor parameters owned directly by the given type.
`static boolean`
`[isActor](#isActor(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Returns whether the given feature represents an actor.
`static boolean`
`[isActor](#isActor(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Returns whether the given membership is an [`ActorMembership`](sysml/ActorMembership.html).
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Actors
public Actors()
 ============ METHOD DETAIL ========== 
Method Details
isActor
public static boolean isActor([Feature](../../kerml/model/kerml/Feature.html) feature)
Returns whether the given feature represents an actor. A feature is
 considered an actor when it is a [`PartUsage`](sysml/PartUsage.html) whose owning
 membership is an [`ActorMembership`](sysml/ActorMembership.html).
Parameters:
`feature` - the feature to test
Returns:
`true` if the feature is an actor
isActor
public static boolean isActor(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Returns whether the given membership is an [`ActorMembership`](sysml/ActorMembership.html).
Parameters:
`membership` - the membership to test
Returns:
`true` if the membership represents an actor
getActorParameter
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](sysml/PartUsage.html)> getActorParameter([Type](../../kerml/model/kerml/Type.html) type)
Returns the actor parameters of the given type. Actor parameters may be
 defined on requirements and cases, both usage and definition forms.
Parameters:
`type` - the type whose actor parameters are requested
Returns:
a list of actor parameters, or an empty list if none exist
getOwnedActorParameter
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](sysml/PartUsage.html)> getOwnedActorParameter([Type](../../kerml/model/kerml/Type.html) type)
Returns the actor parameters owned directly by the given type. Only
 requirement and case types expose actor parameters through owned
 feature memberships.
Parameters:
`type` - the type whose owned actor parameters are requested
Returns:
a list of owned actor parameters, or an empty list if none exist

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Actors">Class Actors</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Actors</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Actors</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility methods for identifying actor parameters and actor memberships on
 requirements, cases, and related types. Actors are represented as
 <a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartUsage</code></a> elements owned through <a href="sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActorMembership</code></a>.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Actors</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getActorParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getActorParameter</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the actor parameters of the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedActorParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedActorParameter</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the actor parameters owned directly by the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isActor(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isActor</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given feature represents an actor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isActor(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isActor</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given membership is an <a href="sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActorMembership</code></a>.</div>
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
<h3>Actors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Actors</span>()</div>
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
<section class="detail" id="isActor(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isActor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isActor</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns whether the given feature represents an actor. A feature is
 considered an actor when it is a <a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartUsage</code></a> whose owning
 membership is an <a href="sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActorMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the feature is an actor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isActor(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isActor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isActor</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Returns whether the given membership is an <a href="sysml/ActorMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ActorMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the membership represents an actor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActorParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getActorParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</span> <span class="element-name">getActorParameter</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the actor parameters of the given type. Actor parameters may be
 defined on requirements and cases, both usage and definition forms.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose actor parameters are requested</dd>
<dt>Returns:</dt>
<dd>a list of actor parameters, or an empty list if none exist</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedActorParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedActorParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</span> <span class="element-name">getOwnedActorParameter</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the actor parameters owned directly by the given type. Only
 requirement and case types expose actor parameters through owned
 feature memberships.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose owned actor parameters are requested</dd>
<dt>Returns:</dt>
<dd>a list of owned actor parameters, or an empty list if none exist</dd>
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
