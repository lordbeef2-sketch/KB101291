# JAVA OPENAPI: Subsettings (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Subsettings.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Subsettings.html`
- source_sha256: `c3026eac2bc06dc6681ca094011017ce89d6d77742908fe064bb2389964fe79a`
- captured_utc: `2026-07-14T16:44:48.373847+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Subsettings

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Subsettings

@OpenApiAllpublic classSubsettings
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Subsetting`](kerml/Subsetting.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Subsettings](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addSubsetted](#addSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) subsettingFeature,
 [Feature](kerml/Feature.html) subsetted)`
Adds a subsetted feature to the given subsetting feature.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>>`
`[getAllSubsettedAsChains](#getAllSubsettedAsChains(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) subsetting)`
Returns all subsetted features as chains for the given subsetting feature.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>>`
`[getAllSubsettedAsChains](#getAllSubsettedAsChains(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Predicate))([Feature](kerml/Feature.html) subsetting,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Subsetting](kerml/Subsetting.html)> subsettingFilter)`
Returns all subsetted features as chains using a filter.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getAnyKindSubsetting](#getAnyKindSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type))([Feature](kerml/Feature.html) subsetted,
 [Type](kerml/Type.html) type)`
Returns all features that subset the given feature within the context of a type.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getAnyKindSubsetting](#getAnyKindSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List))([Feature](kerml/Feature.html) subsetted,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> features)`
Returns all features that subset the given feature from the provided feature list.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Subsetting](kerml/Subsetting.html)>`
`[getOwnedNotImpliedAnyKindSubsettings](#getOwnedNotImpliedAnyKindSubsettings(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) subsettingFeature)`
Returns all owned subsettings that are not implied.
`static boolean`
`[isAnyKindSubsetting](#isAnyKindSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) subsetting,
 [Feature](kerml/Feature.html) subsetted)`
Checks whether the given feature subsets another feature.
`static void`
`[setAllSubsetted](#setAllSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,boolean))([Feature](kerml/Feature.html) subsettingFeature,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>> subsetted,
 boolean set)`
Sets subsetted feature of given subsetting feature.
`static void`
`[setAllSubsetted](#setAllSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,java.util.function.Predicate,java.lang.Class,boolean,boolean))([Feature](kerml/Feature.html) subsettingFeature,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>> subsetted,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Subsetting](kerml/Subsetting.html)> subsettingFilter,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Subsetting](kerml/Subsetting.html)> subsettingType,
 boolean allowImplied,
 boolean set)`
Sets subsetted features of given subsetting feature.
`static void`
`[setAnyKindSubsetted](#setAnyKindSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) subsetting,
 [Feature](kerml/Feature.html) subsetted)`
Sets the subsetted feature for the given subsetting feature.
`static void`
`[setAnyKindSubsetted](#setAnyKindSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List))([Feature](kerml/Feature.html) subsetting,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> subsetted)`
Sets the subsetted features for the given subsetting feature.
`static void`
`[setFirstSubsetted](#setFirstSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,boolean))([Feature](kerml/Feature.html) subsettingFeature,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> subsettedAsChain,
 boolean set)`
Sets subsetted feature of given subsetting feature.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Subsettings
public Subsettings()
 ============ METHOD DETAIL ========== 
Method Details
setAnyKindSubsetted
public static void setAnyKindSubsetted([Feature](kerml/Feature.html) subsetting,
 @CheckForNull
 [Feature](kerml/Feature.html) subsetted)
Sets the subsetted feature for the given subsetting feature.
Parameters:
`subsetting` - the feature that subsets another
`subsetted` - the feature being subsetted (maybe null)
setAnyKindSubsetted
public static void setAnyKindSubsetted([Feature](kerml/Feature.html) subsetting,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> subsetted)
Sets the subsetted features for the given subsetting feature.
Parameters:
`subsetting` - the feature that subsets others
`subsetted` - list of features being subsetted
addSubsetted
public static void addSubsetted([Feature](kerml/Feature.html) subsettingFeature,
 [Feature](kerml/Feature.html) subsetted)
Adds a subsetted feature to the given subsetting feature.
Parameters:
`subsettingFeature` - the feature that subsets another
`subsetted` - the feature being added as subsetted
getAnyKindSubsetting
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getAnyKindSubsetting([Feature](kerml/Feature.html) subsetted,
 [Type](kerml/Type.html) type)
Returns all features that subset the given feature within the context of a type.
Parameters:
`subsetted` - the feature being subsetted
`type` - the type whose features are checked
Returns:
list of subsetting features
getAnyKindSubsetting
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getAnyKindSubsetting([Feature](kerml/Feature.html) subsetted,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> features)
Returns all features that subset the given feature from the provided feature list.
Parameters:
`subsetted` - the feature being subsetted
`features` - list of features to inspect
Returns:
list of subsetting features
isAnyKindSubsetting
public static boolean isAnyKindSubsetting([Feature](kerml/Feature.html) subsetting,
 [Feature](kerml/Feature.html) subsetted)
Checks whether the given feature subsets another feature.
Parameters:
`subsetting` - the feature that may be subsetting
`subsetted` - the feature being checked
Returns:
true if subsetting subsets subsetted
getOwnedNotImpliedAnyKindSubsettings
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Subsetting](kerml/Subsetting.html)> getOwnedNotImpliedAnyKindSubsettings([Feature](kerml/Feature.html) subsettingFeature)
Returns all owned subsettings that are not implied.
Parameters:
`subsettingFeature` - the feature to inspect
Returns:
list of non-implied subsettings
getAllSubsettedAsChains
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>> getAllSubsettedAsChains([Feature](kerml/Feature.html) subsetting)
Returns all subsetted features as chains for the given subsetting feature.
Parameters:
`subsetting` - the feature that subsets others
Returns:
list of feature chains
getAllSubsettedAsChains
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>> getAllSubsettedAsChains([Feature](kerml/Feature.html) subsetting,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Subsetting](kerml/Subsetting.html)> subsettingFilter)
Returns all subsetted features as chains using a filter.
Parameters:
`subsetting` - the feature that subsets others
`subsettingFilter` - filter for selecting subsettings
Returns:
list of feature chains
setFirstSubsetted
public static void setFirstSubsetted([Feature](kerml/Feature.html) subsettingFeature,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> subsettedAsChain,
 boolean set)
Sets subsetted feature of given subsetting feature.
Parameters:
`subsettingFeature` - subsetting feature
`subsettedAsChain` - subsetted feature as a chain
`set` - if set to true, find first [`Subsetting`](kerml/Subsetting.html) and update it, if false - create new [`Subsetting`](kerml/Subsetting.html)
setAllSubsetted
public static void setAllSubsetted([Feature](kerml/Feature.html) subsettingFeature,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>> subsetted,
 boolean set)
Sets subsetted feature of given subsetting feature.
Parameters:
`subsettingFeature` - subsetting feature
`subsetted` - subsetted feature chain
`set` - if set to true, find the first [`Subsetting`](kerml/Subsetting.html) and update it, if false - create new [`Subsetting`](kerml/Subsetting.html)
setAllSubsetted
public static void setAllSubsetted([Feature](kerml/Feature.html) subsettingFeature,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>> subsetted,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Subsetting](kerml/Subsetting.html)> subsettingFilter,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Subsetting](kerml/Subsetting.html)> subsettingType,
 boolean allowImplied,
 boolean set)
Sets subsetted features of given subsetting feature.
Parameters:
`subsettingFeature` - the feature that subsets others
`subsetted` - list of feature chains
`subsettingFilter` - filter for selecting relationships
`subsettingType` - type of subsetting relationship
`allowImplied` - whether implied relationships are allowed
`set` - if set to true, replace all existing subsetted with given one, if false, append given ones

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Subsettings">Class Subsettings</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Subsettings</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Subsettings</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Subsetting</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Subsettings</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">addSubsetted</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsettingFeature,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetted)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds a subsetted feature to the given subsetting feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllSubsettedAsChains(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getAllSubsettedAsChains</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetting)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all subsetted features as chains for the given subsetting feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllSubsettedAsChains(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Predicate)">getAllSubsettedAsChains</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetting,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a>&gt; subsettingFilter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all subsetted features as chains using a filter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnyKindSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">getAnyKindSubsetting</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetted,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all features that subset the given feature within the context of a type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnyKindSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">getAnyKindSubsetting</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetted,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; features)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all features that subset the given feature from the provided feature list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedNotImpliedAnyKindSubsettings(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getOwnedNotImpliedAnyKindSubsettings</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsettingFeature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all owned subsettings that are not implied.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAnyKindSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isAnyKindSubsetting</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetting,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetted)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given feature subsets another feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setAllSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,boolean)">setAllSubsetted</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsettingFeature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt; subsetted,
 boolean set)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets subsetted feature of given subsetting feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setAllSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,java.util.function.Predicate,java.lang.Class,boolean,boolean)">setAllSubsetted</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsettingFeature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt; subsetted,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a>&gt; subsettingFilter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a>&gt; subsettingType,
 boolean allowImplied,
 boolean set)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets subsetted features of given subsetting feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setAnyKindSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setAnyKindSubsetted</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetting,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetted)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the subsetted feature for the given subsetting feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setAnyKindSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">setAnyKindSubsetted</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetting,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; subsetted)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the subsetted features for the given subsetting feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setFirstSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,boolean)">setFirstSubsetted</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsettingFeature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; subsettedAsChain,
 boolean set)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets subsetted feature of given subsetting feature.</div>
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
<h3>Subsettings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Subsettings</span>()</div>
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
<section class="detail" id="setAnyKindSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setAnyKindSubsetted</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setAnyKindSubsetted</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetting,
 @CheckForNull
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetted)</span></div>
<div class="block">Sets the subsetted feature for the given subsetting feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subsetting</code> - the feature that subsets another</dd>
<dd><code>subsetted</code> - the feature being subsetted (maybe null)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAnyKindSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">
<h3>setAnyKindSubsetted</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setAnyKindSubsetted</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetting,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; subsetted)</span></div>
<div class="block">Sets the subsetted features for the given subsetting feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subsetting</code> - the feature that subsets others</dd>
<dd><code>subsetted</code> - list of features being subsetted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>addSubsetted</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addSubsetted</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsettingFeature,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetted)</span></div>
<div class="block">Adds a subsetted feature to the given subsetting feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subsettingFeature</code> - the feature that subsets another</dd>
<dd><code>subsetted</code> - the feature being added as subsetted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnyKindSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getAnyKindSubsetting</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getAnyKindSubsetting</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetted,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns all features that subset the given feature within the context of a type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subsetted</code> - the feature being subsetted</dd>
<dd><code>type</code> - the type whose features are checked</dd>
<dt>Returns:</dt>
<dd>list of subsetting features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnyKindSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">
<h3>getAnyKindSubsetting</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getAnyKindSubsetting</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetted,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; features)</span></div>
<div class="block">Returns all features that subset the given feature from the provided feature list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subsetted</code> - the feature being subsetted</dd>
<dd><code>features</code> - list of features to inspect</dd>
<dt>Returns:</dt>
<dd>list of subsetting features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAnyKindSubsetting(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isAnyKindSubsetting</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAnyKindSubsetting</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetting,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetted)</span></div>
<div class="block">Checks whether the given feature subsets another feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subsetting</code> - the feature that may be subsetting</dd>
<dd><code>subsetted</code> - the feature being checked</dd>
<dt>Returns:</dt>
<dd>true if subsetting subsets subsetted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedNotImpliedAnyKindSubsettings(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getOwnedNotImpliedAnyKindSubsettings</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a>&gt;</span> <span class="element-name">getOwnedNotImpliedAnyKindSubsettings</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsettingFeature)</span></div>
<div class="block">Returns all owned subsettings that are not implied.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subsettingFeature</code> - the feature to inspect</dd>
<dt>Returns:</dt>
<dd>list of non-implied subsettings</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllSubsettedAsChains(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getAllSubsettedAsChains</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt;</span> <span class="element-name">getAllSubsettedAsChains</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetting)</span></div>
<div class="block">Returns all subsetted features as chains for the given subsetting feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subsetting</code> - the feature that subsets others</dd>
<dt>Returns:</dt>
<dd>list of feature chains</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllSubsettedAsChains(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Predicate)">
<h3>getAllSubsettedAsChains</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt;</span> <span class="element-name">getAllSubsettedAsChains</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsetting,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a>&gt; subsettingFilter)</span></div>
<div class="block">Returns all subsetted features as chains using a filter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subsetting</code> - the feature that subsets others</dd>
<dd><code>subsettingFilter</code> - filter for selecting subsettings</dd>
<dt>Returns:</dt>
<dd>list of feature chains</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFirstSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,boolean)">
<h3>setFirstSubsetted</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setFirstSubsetted</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsettingFeature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; subsettedAsChain,
 boolean set)</span></div>
<div class="block">Sets subsetted feature of given subsetting feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subsettingFeature</code> - subsetting feature</dd>
<dd><code>subsettedAsChain</code> - subsetted feature as a chain</dd>
<dd><code>set</code> - if set to true, find first <a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Subsetting</code></a> and update it, if false - create new <a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Subsetting</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAllSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,boolean)">
<h3>setAllSubsetted</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setAllSubsetted</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsettingFeature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt; subsetted,
 boolean set)</span></div>
<div class="block">Sets subsetted feature of given subsetting feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subsettingFeature</code> - subsetting feature</dd>
<dd><code>subsetted</code> - subsetted feature chain</dd>
<dd><code>set</code> - if set to true, find the first <a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Subsetting</code></a> and update it, if false - create new <a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Subsetting</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAllSubsetted(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,java.util.function.Predicate,java.lang.Class,boolean,boolean)">
<h3>setAllSubsetted</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setAllSubsetted</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> subsettingFeature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt; subsetted,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a>&gt; subsettingFilter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="kerml/Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a>&gt; subsettingType,
 boolean allowImplied,
 boolean set)</span></div>
<div class="block">Sets subsetted features of given subsetting feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subsettingFeature</code> - the feature that subsets others</dd>
<dd><code>subsetted</code> - list of feature chains</dd>
<dd><code>subsettingFilter</code> - filter for selecting relationships</dd>
<dd><code>subsettingType</code> - type of subsetting relationship</dd>
<dd><code>allowImplied</code> - whether implied relationships are allowed</dd>
<dd><code>set</code> - if set to true, replace all existing subsetted with given one, if false, append given ones</dd>
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
