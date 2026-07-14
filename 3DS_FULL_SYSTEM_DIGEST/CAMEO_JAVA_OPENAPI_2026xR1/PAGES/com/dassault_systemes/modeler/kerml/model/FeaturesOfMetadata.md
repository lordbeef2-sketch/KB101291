# JAVA OPENAPI: FeaturesOfMetadata (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/FeaturesOfMetadata.html
- source_path: `com/dassault_systemes/modeler/kerml/model/FeaturesOfMetadata.html`
- source_sha256: `8de475ff17596ebf7eef49404f3aa6ea34ccd31ffb620e591b2415710096bcea`
- captured_utc: `2026-07-14T16:44:47.650837+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class FeaturesOfMetadata

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.FeaturesOfMetadata

@OpenApiAllpublic classFeaturesOfMetadata
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class for dealing with Features of [`MetadataFeature`](kerml/MetadataFeature.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[FeaturesOfMetadata](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Feature](kerml/Feature.html)`
`[create](#create(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([MetadataFeature](kerml/MetadataFeature.html) metadata,
 [Feature](kerml/Feature.html) featureOfMetaclass)`
Creates a new redefining feature inside the metadata feature.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getFeaturesOf](#getFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature))([MetadataFeature](kerml/MetadataFeature.html) metadataFeature)`
Returns non-hidden features of [`MetadataFeature`](kerml/MetadataFeature.html).
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getFeaturesOfOwnedMetadata](#getFeaturesOfOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns non-hidden features of owned metadata of given [`Element`](kerml/Element.html)
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[MetadataFeature](kerml/MetadataFeature.html)>`
`[getMetadataByFeature](#getMetadataByFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.Collection))([Feature](kerml/Feature.html) feature,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[MetadataFeature](kerml/MetadataFeature.html)> metadata)`
Filters given metadata by feature: checks which metadata contains feature redefined by given feature.
`static [MetadataFeature](kerml/MetadataFeature.html)`
`[getMetadataOfFeature](#getMetadataOfFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.Collection))([Feature](kerml/Feature.html) feature,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[MetadataFeature](kerml/MetadataFeature.html)> metadata)`
Looks for metadata among given for which given Feature belongs.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Feature](kerml/Feature.html)>`
`[getRedefinableFeaturesOfMetadata](#getRedefinableFeaturesOfMetadata(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[MetadataFeature](kerml/MetadataFeature.html)> metadata)`
Returns features from metadata that can be redefined.
`static [FeatureValue](kerml/FeatureValue.html)`
`[setValue](#setValue(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Object))([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass,
 [Feature](kerml/Feature.html) featureOfMetaclass,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Set a value for given feature in the context of [`MetadataFeature`](kerml/MetadataFeature.html) owned by given Element.
`static [FeatureValue](kerml/FeatureValue.html)`
`[setValueOfMetadata](#setValueOfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Object))([MetadataFeature](kerml/MetadataFeature.html) metadata,
 [Feature](kerml/Feature.html) featureOfMetaclass,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Set a value for given feature in the context of given [`MetadataFeature`](kerml/MetadataFeature.html).
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
FeaturesOfMetadata
public FeaturesOfMetadata()
 ============ METHOD DETAIL ========== 
Method Details
getFeaturesOf
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getFeaturesOf([MetadataFeature](kerml/MetadataFeature.html) metadataFeature)
Returns non-hidden features of [`MetadataFeature`](kerml/MetadataFeature.html).
 Hidden features are "baseType", "annotatedElement".
Parameters:
`metadataFeature` - metadata
Returns:
features of metadata
getFeaturesOfOwnedMetadata
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getFeaturesOfOwnedMetadata([Element](kerml/Element.html) element)
Returns non-hidden features of owned metadata of given [`Element`](kerml/Element.html)
Parameters:
`element` - element
Returns:
features of owned metadata of Element
See Also:
[`Metadata.getOwnedMetadata(Element)`](Metadata.html#getOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element))
[`getFeaturesOf(MetadataFeature)`](#getFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature))
getMetadataOfFeature
@CheckForNullpublic static [MetadataFeature](kerml/MetadataFeature.html) getMetadataOfFeature([Feature](kerml/Feature.html) feature,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[MetadataFeature](kerml/MetadataFeature.html)> metadata)
Looks for metadata among given for which given Feature belongs.
Parameters:
`feature` - given feature
`metadata` - given metadata
Returns:
metadata of given feature
getMetadataByFeature
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[MetadataFeature](kerml/MetadataFeature.html)> getMetadataByFeature([Feature](kerml/Feature.html) feature,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[MetadataFeature](kerml/MetadataFeature.html)> metadata)
Filters given metadata by feature: checks which metadata contains feature redefined by given feature.
Parameters:
`feature` - given feature.
`metadata` - given metadata
Returns:
filtered metadata.
getRedefinableFeaturesOfMetadata
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Feature](kerml/Feature.html)> getRedefinableFeaturesOfMetadata([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[MetadataFeature](kerml/MetadataFeature.html)> metadata)
Returns features from metadata that can be redefined.
 These are non-hidden features that are not themselves metadata features.
Parameters:
`metadata` - metadata collection
Returns:
redefinable features
setValue
@CheckForNullpublic static [FeatureValue](kerml/FeatureValue.html) setValue([Element](kerml/Element.html) element,
 [Metaclass](kerml/Metaclass.html) metaclass,
 [Feature](kerml/Feature.html) featureOfMetaclass,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Set a value for given feature in the context of [`MetadataFeature`](kerml/MetadataFeature.html) owned by given Element.
 First it looks for a [`MetadataFeature`](kerml/MetadataFeature.html) matching given Metaclass owned by the given Element or creates one if needed.
 Then it looks for a redefining @[`Feature`](kerml/Feature.html) owned by [`MetadataFeature`](kerml/MetadataFeature.html) or creates one if needed.
 Then it sets a value for that redefining feature.
Parameters:
`element` - element
`metaclass` - metaclass
`featureOfMetaclass` - feature of metaclass
`value` - value, either single value, null or a [`List`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) of values
Returns:
FeatureValue referencing a value
setValueOfMetadata
@CheckForNullpublic static [FeatureValue](kerml/FeatureValue.html) setValueOfMetadata([MetadataFeature](kerml/MetadataFeature.html) metadata,
 [Feature](kerml/Feature.html) featureOfMetaclass,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Set a value for given feature in the context of given [`MetadataFeature`](kerml/MetadataFeature.html).
 It looks for a redefining @[`Feature`](kerml/Feature.html) owned by [`MetadataFeature`](kerml/MetadataFeature.html) or creates one if needed.
 Then it sets a value for that redefining feature.
Parameters:
`metadata` - metadata
`featureOfMetaclass` - feature of metaclass
`value` - value, either single value, null or a [`List`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) of values
Returns:
FeatureValue referencing a value
create
public static [Feature](kerml/Feature.html) create([MetadataFeature](kerml/MetadataFeature.html) metadata,
 [Feature](kerml/Feature.html) featureOfMetaclass)
Creates a new redefining feature inside the metadata feature.
Parameters:
`metadata` - metadata feature
`featureOfMetaclass` - feature to redefine
Returns:
created feature

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class FeaturesOfMetadata">Class FeaturesOfMetadata</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.FeaturesOfMetadata</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">FeaturesOfMetadata</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class for dealing with Features of <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">FeaturesOfMetadata</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">create</a><wbr/>(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> metadata,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> featureOfMetaclass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a new redefining feature inside the metadata feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature)">getFeaturesOf</a><wbr/>(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> metadataFeature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns non-hidden features of <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeaturesOfOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getFeaturesOfOwnedMetadata</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns non-hidden features of owned metadata of given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetadataByFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.Collection)">getMetadataByFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt; metadata)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filters given metadata by feature: checks which metadata contains feature redefined by given feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetadataOfFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.Collection)">getMetadataOfFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt; metadata)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Looks for metadata among given for which given Feature belongs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRedefinableFeaturesOfMetadata(java.util.Collection)">getRedefinableFeaturesOfMetadata</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt; metadata)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns features from metadata that can be redefined.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Object)">setValue</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> featureOfMetaclass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set a value for given feature in the context of <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a> owned by given Element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValueOfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Object)">setValueOfMetadata</a><wbr/>(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> metadata,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> featureOfMetaclass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set a value for given feature in the context of given <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a>.</div>
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
<h3>FeaturesOfMetadata</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">FeaturesOfMetadata</span>()</div>
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
<section class="detail" id="getFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature)">
<h3>getFeaturesOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getFeaturesOf</span><wbr/><span class="parameters">(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> metadataFeature)</span></div>
<div class="block">Returns non-hidden features of <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a>.
 Hidden features are "baseType", "annotatedElement".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metadataFeature</code> - metadata</dd>
<dt>Returns:</dt>
<dd>features of metadata</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeaturesOfOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getFeaturesOfOwnedMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getFeaturesOfOwnedMetadata</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns non-hidden features of owned metadata of given <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>features of owned metadata of Element</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="Metadata.html#getOwnedMetadata(com.dassault_systemes.modeler.kerml.model.kerml.Element)"><code>Metadata.getOwnedMetadata(Element)</code></a></li>
<li><a href="#getFeaturesOf(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature)"><code>getFeaturesOf(MetadataFeature)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetadataOfFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.Collection)">
<h3>getMetadataOfFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a></span> <span class="element-name">getMetadataOfFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt; metadata)</span></div>
<div class="block">Looks for metadata among given for which given Feature belongs.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - given feature</dd>
<dd><code>metadata</code> - given metadata</dd>
<dt>Returns:</dt>
<dd>metadata of given feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetadataByFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.Collection)">
<h3>getMetadataByFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt;</span> <span class="element-name">getMetadataByFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt; metadata)</span></div>
<div class="block">Filters given metadata by feature: checks which metadata contains feature redefined by given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - given feature.</dd>
<dd><code>metadata</code> - given metadata</dd>
<dt>Returns:</dt>
<dd>filtered metadata.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinableFeaturesOfMetadata(java.util.Collection)">
<h3>getRedefinableFeaturesOfMetadata</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getRedefinableFeaturesOfMetadata</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a>&gt; metadata)</span></div>
<div class="block">Returns features from metadata that can be redefined.
 These are non-hidden features that are not themselves metadata features.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metadata</code> - metadata collection</dd>
<dt>Returns:</dt>
<dd>redefinable features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Metaclass,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Metaclass.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Metaclass</a> metaclass,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> featureOfMetaclass,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Set a value for given feature in the context of <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a> owned by given Element.
 First it looks for a <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a> matching given Metaclass owned by the given Element or creates one if needed.
 Then it looks for a redefining @<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Feature</code></a> owned by <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a> or creates one if needed.
 Then it sets a value for that redefining feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>metaclass</code> - metaclass</dd>
<dd><code>featureOfMetaclass</code> - feature of metaclass</dd>
<dd><code>value</code> - value, either single value, null or a <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util"><code>List</code></a> of values</dd>
<dt>Returns:</dt>
<dd>FeatureValue referencing a value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValueOfMetadata(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Object)">
<h3>setValueOfMetadata</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></span> <span class="element-name">setValueOfMetadata</span><wbr/><span class="parameters">(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> metadata,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> featureOfMetaclass,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Set a value for given feature in the context of given <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a>.
 It looks for a redefining @<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Feature</code></a> owned by <a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataFeature</code></a> or creates one if needed.
 Then it sets a value for that redefining feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metadata</code> - metadata</dd>
<dd><code>featureOfMetaclass</code> - feature of metaclass</dd>
<dd><code>value</code> - value, either single value, null or a <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util"><code>List</code></a> of values</dd>
<dt>Returns:</dt>
<dd>FeatureValue referencing a value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(com.dassault_systemes.modeler.kerml.model.kerml.MetadataFeature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a href="kerml/MetadataFeature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataFeature</a> metadata,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> featureOfMetaclass)</span></div>
<div class="block">Creates a new redefining feature inside the metadata feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>metadata</code> - metadata feature</dd>
<dd><code>featureOfMetaclass</code> - feature to redefine</dd>
<dt>Returns:</dt>
<dd>created feature</dd>
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
