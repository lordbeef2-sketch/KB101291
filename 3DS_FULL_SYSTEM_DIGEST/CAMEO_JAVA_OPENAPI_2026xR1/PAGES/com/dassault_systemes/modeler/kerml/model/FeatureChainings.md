# JAVA OPENAPI: FeatureChainings (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/FeatureChainings.html
- source_path: `com/dassault_systemes/modeler/kerml/model/FeatureChainings.html`
- source_sha256: `84f6fd9bb7e65dceddc01132b2ec98cb9c9cf82a3ed3ffc02d089af493657a6c`
- captured_utc: `2026-07-14T16:44:47.531835+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class FeatureChainings

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.FeatureChainings

@OpenApiAllpublic classFeatureChainings
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`FeatureChaining`](kerml/FeatureChaining.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[FeatureChainings](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Feature](kerml/Feature.html)`
`[createAnonymousChainedFeature](#createAnonymousChainedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature...))([Feature](kerml/Feature.html)... chainingFeatures)`
Creates an anonymous feature with the given chaining features.
`static [FeatureChaining](kerml/FeatureChaining.html)`
`[createFeatureChaining](#createFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.KerMLElementsFactory))([Element](kerml/Element.html) owner,
 [Feature](kerml/Feature.html) chainingFeature,
 [KerMLElementsFactory](KerMLElementsFactory.html) factory)`
Creates a FeatureChaining relationship owned by the given element.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getChainingFeatureOrSelf](#getChainingFeatureOrSelf(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Returns the chaining feature list or the feature itself if no chaining exists.
`static [Feature](kerml/Feature.html)`
`[getFirstChainingFeature](#getFirstChainingFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) chainedFeature)`
Returns the first chaining feature of the given feature.
`static <T extends [Subsetting](kerml/Subsetting.html)> 
T`
`[getIncomingSubsettingToAnonymousFeature](#getIncomingSubsettingToAnonymousFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Class))([Feature](kerml/Feature.html) anonymous,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> subsettingClass)`
Returns the incoming subsetting relationship to an anonymous feature.
`static [Feature](kerml/Feature.html)`
`[getLastChainingFeature](#getLastChainingFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) chainedFeature)`
Returns the last chaining feature of the given feature.
`static <R extends [Relationship](kerml/Relationship.html)> 
[Feature](kerml/Feature.html)`
`[setSimpleOrChainedRelationshipTarget](#setSimpleOrChainedRelationshipTarget(R,java.util.List,java.util.function.Consumer))(R relationship,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> referenced,
 [Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[Feature](kerml/Feature.html)> relationshipTargetSetter)`
Set the target of given relationship as chained owned anonymous feature or regular reference.
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Feature](kerml/Feature.html)>`
`[streamOfChainingFeatureOrSelf](#streamOfChainingFeatureOrSelf(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Returns a stream of chaining features or the feature itself if no chaining exists.
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Feature](kerml/Feature.html)>`
`[streamOfChainingFeatures](#streamOfChainingFeatures(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) chainedFeature)`
Returns a stream of chaining features of the given feature.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
FeatureChainings
public FeatureChainings()
 ============ METHOD DETAIL ========== 
Method Details
setSimpleOrChainedRelationshipTarget
@CheckForNullpublic static <R extends [Relationship](kerml/Relationship.html)> [Feature](kerml/Feature.html) setSimpleOrChainedRelationshipTarget(R relationship,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> referenced,
 [Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[Feature](kerml/Feature.html)> relationshipTargetSetter)
Set the target of given relationship as chained owned anonymous feature or regular reference.
Parameters:
`relationship` - relationship
`referenced` - simple or chained reference to the target
`relationshipTargetSetter` - relationship target setter
Returns:
anonymous feature if reference is chained, otherwise first feature from a given list
streamOfChainingFeatureOrSelf
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Feature](kerml/Feature.html)> streamOfChainingFeatureOrSelf([Feature](kerml/Feature.html) feature)
Returns a stream of chaining features or the feature itself if no chaining exists.
Parameters:
`feature` - feature
Returns:
stream of chaining features or self
getChainingFeatureOrSelf
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getChainingFeatureOrSelf([Feature](kerml/Feature.html) feature)
Returns the chaining feature list or the feature itself if no chaining exists.
Parameters:
`feature` - feature
Returns:
list of chaining features or singleton list of feature
getIncomingSubsettingToAnonymousFeature
@CheckForNullpublic static <T extends [Subsetting](kerml/Subsetting.html)> T getIncomingSubsettingToAnonymousFeature([Feature](kerml/Feature.html) anonymous,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> subsettingClass)
Returns the incoming subsetting relationship to an anonymous feature.
Type Parameters:
`T` - subsetting type
Parameters:
`anonymous` - anonymous feature
`subsettingClass` - expected subsetting class
Returns:
incoming subsetting, or null
streamOfChainingFeatures
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Feature](kerml/Feature.html)> streamOfChainingFeatures([Feature](kerml/Feature.html) chainedFeature)
Returns a stream of chaining features of the given feature.
Parameters:
`chainedFeature` - feature with chaining
Returns:
stream of chaining features
getFirstChainingFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getFirstChainingFeature([Feature](kerml/Feature.html) chainedFeature)
Returns the first chaining feature of the given feature.
Parameters:
`chainedFeature` - feature
Returns:
first chaining feature, or null
getLastChainingFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getLastChainingFeature([Feature](kerml/Feature.html) chainedFeature)
Returns the last chaining feature of the given feature.
Parameters:
`chainedFeature` - feature
Returns:
last chaining feature, or null
createAnonymousChainedFeature
public static [Feature](kerml/Feature.html) createAnonymousChainedFeature([Feature](kerml/Feature.html)... chainingFeatures)
Creates an anonymous feature with the given chaining features.
Parameters:
`chainingFeatures` - features to chain
Returns:
created anonymous feature
createFeatureChaining
public static [FeatureChaining](kerml/FeatureChaining.html) createFeatureChaining([Element](kerml/Element.html) owner,
 [Feature](kerml/Feature.html) chainingFeature,
 [KerMLElementsFactory](KerMLElementsFactory.html) factory)
Creates a FeatureChaining relationship owned by the given element.
Parameters:
`owner` - owner of the chaining
`chainingFeature` - feature to chain
`factory` - factory for creating elements
Returns:
created FeatureChaining

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class FeatureChainings">Class FeatureChainings</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.FeatureChainings</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">FeatureChainings</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureChaining</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">FeatureChainings</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createAnonymousChainedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature...)">createAnonymousChainedFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>... chainingFeatures)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an anonymous feature with the given chaining features.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChaining</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.KerMLElementsFactory)">createFeatureChaining</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> owner,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> chainingFeature,
 <a href="KerMLElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLElementsFactory</a> factory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a FeatureChaining relationship owned by the given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getChainingFeatureOrSelf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getChainingFeatureOrSelf</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the chaining feature list or the feature itself if no chaining exists.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstChainingFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getFirstChainingFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> chainedFeature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first chaining feature of the given feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIncomingSubsettingToAnonymousFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Class)">getIncomingSubsettingToAnonymousFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> anonymous,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; subsettingClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the incoming subsetting relationship to an anonymous feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastChainingFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getLastChainingFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> chainedFeature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the last chaining feature of the given feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;R extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;<br/><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSimpleOrChainedRelationshipTarget(R,java.util.List,java.util.function.Consumer)">setSimpleOrChainedRelationshipTarget</a><wbr/>(R relationship,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; referenced,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; relationshipTargetSetter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set the target of given relationship as chained owned anonymous feature or regular reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#streamOfChainingFeatureOrSelf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">streamOfChainingFeatureOrSelf</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a stream of chaining features or the feature itself if no chaining exists.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#streamOfChainingFeatures(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">streamOfChainingFeatures</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> chainedFeature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a stream of chaining features of the given feature.</div>
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
<h3>FeatureChainings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">FeatureChainings</span>()</div>
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
<section class="detail" id="setSimpleOrChainedRelationshipTarget(R,java.util.List,java.util.function.Consumer)">
<h3 id="setSimpleOrChainedRelationshipTarget(com.dassault_systemes.modeler.kerml.model.kerml.Relationship,java.util.List,java.util.function.Consumer)">setSimpleOrChainedRelationshipTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;R extends <a href="kerml/Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a>&gt;</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">setSimpleOrChainedRelationshipTarget</span><wbr/><span class="parameters">(R relationship,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; referenced,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; relationshipTargetSetter)</span></div>
<div class="block">Set the target of given relationship as chained owned anonymous feature or regular reference.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationship</code> - relationship</dd>
<dd><code>referenced</code> - simple or chained reference to the target</dd>
<dd><code>relationshipTargetSetter</code> - relationship target setter</dd>
<dt>Returns:</dt>
<dd>anonymous feature if reference is chained, otherwise first feature from a given list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="streamOfChainingFeatureOrSelf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>streamOfChainingFeatureOrSelf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">streamOfChainingFeatureOrSelf</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns a stream of chaining features or the feature itself if no chaining exists.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - feature</dd>
<dt>Returns:</dt>
<dd>stream of chaining features or self</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChainingFeatureOrSelf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getChainingFeatureOrSelf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getChainingFeatureOrSelf</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns the chaining feature list or the feature itself if no chaining exists.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - feature</dd>
<dt>Returns:</dt>
<dd>list of chaining features or singleton list of feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIncomingSubsettingToAnonymousFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Class)">
<h3>getIncomingSubsettingToAnonymousFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">getIncomingSubsettingToAnonymousFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> anonymous,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; subsettingClass)</span></div>
<div class="block">Returns the incoming subsetting relationship to an anonymous feature.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - subsetting type</dd>
<dt>Parameters:</dt>
<dd><code>anonymous</code> - anonymous feature</dd>
<dd><code>subsettingClass</code> - expected subsetting class</dd>
<dt>Returns:</dt>
<dd>incoming subsetting, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="streamOfChainingFeatures(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>streamOfChainingFeatures</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">streamOfChainingFeatures</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> chainedFeature)</span></div>
<div class="block">Returns a stream of chaining features of the given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>chainedFeature</code> - feature with chaining</dd>
<dt>Returns:</dt>
<dd>stream of chaining features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstChainingFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getFirstChainingFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getFirstChainingFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> chainedFeature)</span></div>
<div class="block">Returns the first chaining feature of the given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>chainedFeature</code> - feature</dd>
<dt>Returns:</dt>
<dd>first chaining feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastChainingFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getLastChainingFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getLastChainingFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> chainedFeature)</span></div>
<div class="block">Returns the last chaining feature of the given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>chainedFeature</code> - feature</dd>
<dt>Returns:</dt>
<dd>last chaining feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAnonymousChainedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature...)">
<h3>createAnonymousChainedFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">createAnonymousChainedFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>... chainingFeatures)</span></div>
<div class="block">Creates an anonymous feature with the given chaining features.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>chainingFeatures</code> - features to chain</dd>
<dt>Returns:</dt>
<dd>created anonymous feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFeatureChaining(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.KerMLElementsFactory)">
<h3>createFeatureChaining</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureChaining.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChaining</a></span> <span class="element-name">createFeatureChaining</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> owner,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> chainingFeature,
 <a href="KerMLElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLElementsFactory</a> factory)</span></div>
<div class="block">Creates a FeatureChaining relationship owned by the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - owner of the chaining</dd>
<dd><code>chainingFeature</code> - feature to chain</dd>
<dd><code>factory</code> - factory for creating elements</dd>
<dt>Returns:</dt>
<dd>created FeatureChaining</dd>
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
