# JAVA OPENAPI: Redefinitions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Redefinitions.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Redefinitions.html`
- source_sha256: `661c72a2e9e4c6265e7c8d60841a19d13faebc5ce38f651e60a299943a9b87b6`
- captured_utc: `2026-07-14T16:44:48.084845+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Redefinitions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Redefinitions

@OpenApiAllpublic classRedefinitions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Redefinition`](kerml/Redefinition.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Redefinitions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addRedefined](#addRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) redefining,
 [Feature](kerml/Feature.html) redefined)`
Adds a redefined feature to the given redefining feature.
`static boolean`
`[anySameOrRedefined](#anySameOrRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.Collection))([Feature](kerml/Feature.html) redefining,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Feature](kerml/Feature.html)> redefined)`
Checks whether the redefining feature is the same as or redefines
 any feature in the given collection.
`static <T extends [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Feature](kerml/Feature.html)>> 
void`
`[collectRedefined](#collectRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,T))([Feature](kerml/Feature.html) redefining,
 T result)`
Collects all redefined features of the given feature into the provided collection.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Feature](kerml/Feature.html)>`
`[collectRedefinedWithSelf](#collectRedefinedWithSelf(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Returns all redefined features including the feature itself.
`static [Feature](kerml/Feature.html)`
`[createRedefining](#createRedefining(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Namespace))([Feature](kerml/Feature.html) redefined,
 [Namespace](kerml/Namespace.html) namespace)`
Creates a new redefining feature for the given redefined feature.
`static [Feature](kerml/Feature.html)`
`[firstRedefined](#firstRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) redefining)`
Returns the first directly redefined feature of the given feature.
`static void`
`[forEachRedefined](#forEachRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Consumer))([Feature](kerml/Feature.html) redefining,
 [Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[Feature](kerml/Feature.html)> consumer)`
Applies the given consumer to each redefined feature of the redefining feature.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getDirectlyRedefined](#getDirectlyRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) redefining)`
Returns the directly redefined features of the given feature.
`static [Feature](kerml/Feature.html)`
`[getOrCreateOwnedRedefining](#getOrCreateOwnedRedefining(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Type](kerml/Type.html) type,
 [Feature](kerml/Feature.html) redefined)`
Returns the owned redefining feature, creating one if necessary.
`static [Feature](kerml/Feature.html)`
`[getOrCreateOwnedRedefining](#getOrCreateOwnedRedefining(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Supplier))([Type](kerml/Type.html) type,
 [Feature](kerml/Feature.html) redefined,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<org.eclipse.emf.ecore.EClass> redefiningECLassSupplier)`
Returns the owned redefining feature, creating one if necessary,
 using the supplied EClass.
`static [Feature](kerml/Feature.html)`
`[getOwnedRedefining](#getOwnedRedefining(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Type](kerml/Type.html) type,
 [Feature](kerml/Feature.html) redefined)`
Returns the owned feature of the type that redefines the given feature.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getRedefined](#getRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) redefining)`
Returns all redefined features of the given feature.
`static [Feature](kerml/Feature.html)`
`[getRedefiningOrSame](#getRedefiningOrSame(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Type](kerml/Type.html) type,
 [Feature](kerml/Feature.html) redefined)`
Returns the redefining feature of the type, or the feature itself if none exists.
`static boolean`
`[isRedefined](#isRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) redefining,
 [Feature](kerml/Feature.html) redefined)`
Checks whether the redefining feature redefines the given feature.
`static boolean`
`[isSameOrRedefined](#isSameOrRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) redefining,
 [Feature](kerml/Feature.html) redefined)`
Checks whether the redefining feature is the same as or redefines the given feature.
`static [Feature](kerml/Feature.html)`
`[matchSelfOrRedefined](#matchSelfOrRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Predicate))([Feature](kerml/Feature.html) redefining,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Feature](kerml/Feature.html)> filter)`
Returns the first feature that matches the predicate,
 searching the feature and its redefined chain.
`static void`
`[removeRedefined](#removeRedefined(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Feature](kerml/Feature.html)> features)`
Removes all redefined features from the given collection.
`static void`
`[setAllRedefined](#setAllRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,boolean))([Feature](kerml/Feature.html) redefiningFeature,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>> redefined,
 boolean set)`
Set redefined features of given redefining feature.
`static void`
`[setFirsRedefined](#setFirsRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,boolean))([Feature](kerml/Feature.html) redefining,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> redefined,
 boolean set)`
Set redefined feature of given redefining feature.
`static void`
`[setRedefined](#setRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) redefining,
 [Feature](kerml/Feature.html) redefined)`
Sets the redefined feature of the given redefining feature.
`static void`
`[setRedefined](#setRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List))([Feature](kerml/Feature.html) redefining,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> redefined)`
Sets the redefined features of the given redefining feature.
`static void`
`[traverseRedefinedFeaturesRecursively](#traverseRedefinedFeaturesRecursively(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Predicate))([Feature](kerml/Feature.html) feature,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Feature](kerml/Feature.html)> predicate)`
Traverse redefined features recursively.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Redefinitions
public Redefinitions()
 ============ METHOD DETAIL ========== 
Method Details
firstRedefined
@CheckForNullpublic static [Feature](kerml/Feature.html) firstRedefined([Feature](kerml/Feature.html) redefining)
Returns the first directly redefined feature of the given feature.
Parameters:
`redefining` - the feature that redefines another
Returns:
the first redefined feature, or null if none exist
removeRedefined
public static void removeRedefined([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Feature](kerml/Feature.html)> features)
Removes all redefined features from the given collection.
Parameters:
`features` - the features to modify
isSameOrRedefined
public static boolean isSameOrRedefined([Feature](kerml/Feature.html) redefining,
 [Feature](kerml/Feature.html) redefined)
Checks whether the redefining feature is the same as or redefines the given feature.
Parameters:
`redefining` - the redefining feature
`redefined` - the feature being checked
Returns:
true if redefining is the same as or redefines redefined
anySameOrRedefined
public static boolean anySameOrRedefined([Feature](kerml/Feature.html) redefining,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Feature](kerml/Feature.html)> redefined)
Checks whether the redefining feature is the same as or redefines
 any feature in the given collection.
Parameters:
`redefining` - the redefining feature
`redefined` - collection of features to check
Returns:
true if any match
isRedefined
public static boolean isRedefined([Feature](kerml/Feature.html) redefining,
 [Feature](kerml/Feature.html) redefined)
Checks whether the redefining feature redefines the given feature.
Parameters:
`redefining` - the redefining feature
`redefined` - the feature being checked
Returns:
true if redefining redefines redefined
collectRedefinedWithSelf
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Feature](kerml/Feature.html)> collectRedefinedWithSelf([Feature](kerml/Feature.html) feature)
Returns all redefined features including the feature itself.
Parameters:
`feature` - the feature to inspect
Returns:
collection of redefined features including self
collectRedefined
public static <T extends [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Feature](kerml/Feature.html)>> void collectRedefined([Feature](kerml/Feature.html) redefining,
 T result)
Collects all redefined features of the given feature into the provided collection.
Type Parameters:
`T` - collection type
Parameters:
`redefining` - the redefining feature
`result` - the collection to fill
getRedefined
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getRedefined([Feature](kerml/Feature.html) redefining)
Returns all redefined features of the given feature.
Parameters:
`redefining` - the redefining feature
Returns:
list of redefined features
getDirectlyRedefined
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getDirectlyRedefined([Feature](kerml/Feature.html) redefining)
Returns the directly redefined features of the given feature.
Parameters:
`redefining` - the redefining feature
Returns:
list of directly redefined features
setRedefined
public static void setRedefined([Feature](kerml/Feature.html) redefining,
 @CheckForNull
 [Feature](kerml/Feature.html) redefined)
Sets the redefined feature of the given redefining feature.
Parameters:
`redefining` - the redefining feature
`redefined` - the redefined feature, or null
setRedefined
public static void setRedefined([Feature](kerml/Feature.html) redefining,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> redefined)
Sets the redefined features of the given redefining feature.
Parameters:
`redefining` - the redefining feature
`redefined` - list of redefined features
addRedefined
public static void addRedefined([Feature](kerml/Feature.html) redefining,
 [Feature](kerml/Feature.html) redefined)
Adds a redefined feature to the given redefining feature.
Parameters:
`redefining` - the redefining feature
`redefined` - the feature to add as redefined
forEachRedefined
public static void forEachRedefined([Feature](kerml/Feature.html) redefining,
 [Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[Feature](kerml/Feature.html)> consumer)
Applies the given consumer to each redefined feature of the redefining feature.
Parameters:
`redefining` - the redefining feature
`consumer` - action applied to each redefined feature
createRedefining
public static [Feature](kerml/Feature.html) createRedefining([Feature](kerml/Feature.html) redefined,
 [Namespace](kerml/Namespace.html) namespace)
Creates a new redefining feature for the given redefined feature.
Parameters:
`redefined` - the feature to redefine
`namespace` - the namespace where the new feature will be created
Returns:
the newly created redefining feature
matchSelfOrRedefined
@CheckForNullpublic static [Feature](kerml/Feature.html) matchSelfOrRedefined([Feature](kerml/Feature.html) redefining,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Feature](kerml/Feature.html)> filter)
Returns the first feature that matches the predicate,
 searching the feature and its redefined chain.
Parameters:
`redefining` - the starting feature
`filter` - predicate to test
Returns:
matching feature, or null if none found
traverseRedefinedFeaturesRecursively
public static void traverseRedefinedFeaturesRecursively([Feature](kerml/Feature.html) feature,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Feature](kerml/Feature.html)> predicate)
Traverse redefined features recursively.
Parameters:
`feature` - feature to start.
`predicate` - test redefined feature, return false to abort operation.
getOwnedRedefining
@CheckForNullpublic static [Feature](kerml/Feature.html) getOwnedRedefining([Type](kerml/Type.html) type,
 [Feature](kerml/Feature.html) redefined)
Returns the owned feature of the type that redefines the given feature.
Parameters:
`type` - the type whose features are inspected
`redefined` - the feature being redefined
Returns:
the redefining feature, or null if none found
getOrCreateOwnedRedefining
public static [Feature](kerml/Feature.html) getOrCreateOwnedRedefining([Type](kerml/Type.html) type,
 [Feature](kerml/Feature.html) redefined)
Returns the owned redefining feature, creating one if necessary.
Parameters:
`type` - the type whose features are modified
`redefined` - the feature to redefine
Returns:
the existing or newly created redefining feature
getOrCreateOwnedRedefining
public static [Feature](kerml/Feature.html) getOrCreateOwnedRedefining([Type](kerml/Type.html) type,
 [Feature](kerml/Feature.html) redefined,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<org.eclipse.emf.ecore.EClass> redefiningECLassSupplier)
Returns the owned redefining feature, creating one if necessary,
 using the supplied EClass.
Parameters:
`type` - the type whose features are modified
`redefined` - the feature to redefine
`redefiningECLassSupplier` - supplier for the redefining feature class
Returns:
the existing or newly created redefining feature
getRedefiningOrSame
@CheckForNullpublic static [Feature](kerml/Feature.html) getRedefiningOrSame([Type](kerml/Type.html) type,
 [Feature](kerml/Feature.html) redefined)
Returns the redefining feature of the type, or the feature itself if none exists.
Parameters:
`type` - the type whose features are inspected
`redefined` - the feature being redefined
Returns:
redefining feature or the original feature
setFirsRedefined
public static void setFirsRedefined([Feature](kerml/Feature.html) redefining,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> redefined,
 boolean set)
Set redefined feature of given redefining feature.
Parameters:
`redefining` - redefining feature
`redefined` - redefined feature chain
`set` - if set to true, find the first [`Redefinition`](kerml/Redefinition.html) and update it, if false - create new [`Redefinition`](kerml/Redefinition.html)
setAllRedefined
public static void setAllRedefined([Feature](kerml/Feature.html) redefiningFeature,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>> redefined,
 boolean set)
Set redefined features of given redefining feature.
Parameters:
`redefiningFeature` - redefining feature
`redefined` - redefined features chains
`set` - if set to true, replace all existing redefined with given one, if false, append given ones

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Redefinitions">Class Redefinitions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Redefinitions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Redefinitions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Redefinition</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Redefinitions</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">addRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds a redefined feature to the given redefining feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#anySameOrRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.Collection)">anySameOrRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; redefined)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the redefining feature is the same as or redefines
 any feature in the given collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt;<br/>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,T)">collectRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 T result)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects all redefined features of the given feature into the provided collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectRedefinedWithSelf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">collectRedefinedWithSelf</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all redefined features including the feature itself.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createRedefining(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">createRedefining</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined,
 <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> namespace)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a new redefining feature for the given redefined feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#firstRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">firstRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first directly redefined feature of the given feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#forEachRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Consumer)">forEachRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; consumer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Applies the given consumer to each redefined feature of the redefining feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirectlyRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getDirectlyRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the directly redefined features of the given feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateOwnedRedefining(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getOrCreateOwnedRedefining</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned redefining feature, creating one if necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateOwnedRedefining(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Supplier)">getOrCreateOwnedRedefining</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;org.eclipse.emf.ecore.EClass&gt; redefiningECLassSupplier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned redefining feature, creating one if necessary,
 using the supplied EClass.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedRedefining(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getOwnedRedefining</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned feature of the type that redefines the given feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all redefined features of the given feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRedefiningOrSame(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getRedefiningOrSame</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the redefining feature of the type, or the feature itself if none exists.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the redefining feature redefines the given feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSameOrRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isSameOrRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the redefining feature is the same as or redefines the given feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#matchSelfOrRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Predicate)">matchSelfOrRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; filter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first feature that matches the predicate,
 searching the feature and its redefined chain.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeRedefined(java.util.Collection)">removeRedefined</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; features)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all redefined features from the given collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setAllRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,boolean)">setAllRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefiningFeature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt; redefined,
 boolean set)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set redefined features of given redefining feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setFirsRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,boolean)">setFirsRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; redefined,
 boolean set)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set redefined feature of given redefining feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the redefined feature of the given redefining feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">setRedefined</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; redefined)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the redefined features of the given redefining feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#traverseRedefinedFeaturesRecursively(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Predicate)">traverseRedefinedFeaturesRecursively</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; predicate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Traverse redefined features recursively.</div>
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
<h3>Redefinitions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Redefinitions</span>()</div>
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
<section class="detail" id="firstRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>firstRedefined</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">firstRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining)</span></div>
<div class="block">Returns the first directly redefined feature of the given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefining</code> - the feature that redefines another</dd>
<dt>Returns:</dt>
<dd>the first redefined feature, or null if none exist</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeRedefined(java.util.Collection)">
<h3>removeRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeRedefined</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; features)</span></div>
<div class="block">Removes all redefined features from the given collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>features</code> - the features to modify</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSameOrRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isSameOrRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSameOrRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</span></div>
<div class="block">Checks whether the redefining feature is the same as or redefines the given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefining</code> - the redefining feature</dd>
<dd><code>redefined</code> - the feature being checked</dd>
<dt>Returns:</dt>
<dd>true if redefining is the same as or redefines redefined</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="anySameOrRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.Collection)">
<h3>anySameOrRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">anySameOrRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; redefined)</span></div>
<div class="block">Checks whether the redefining feature is the same as or redefines
 any feature in the given collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefining</code> - the redefining feature</dd>
<dd><code>redefined</code> - collection of features to check</dd>
<dt>Returns:</dt>
<dd>true if any match</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</span></div>
<div class="block">Checks whether the redefining feature redefines the given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefining</code> - the redefining feature</dd>
<dd><code>redefined</code> - the feature being checked</dd>
<dt>Returns:</dt>
<dd>true if redefining redefines redefined</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectRedefinedWithSelf(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>collectRedefinedWithSelf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">collectRedefinedWithSelf</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns all redefined features including the feature itself.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature to inspect</dd>
<dt>Returns:</dt>
<dd>collection of redefined features including self</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,T)">
<h3 id="collectRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.Collection)">collectRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt;</span> <span class="return-type">void</span> <span class="element-name">collectRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 T result)</span></div>
<div class="block">Collects all redefined features of the given feature into the provided collection.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - collection type</dd>
<dt>Parameters:</dt>
<dd><code>redefining</code> - the redefining feature</dd>
<dd><code>result</code> - the collection to fill</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining)</span></div>
<div class="block">Returns all redefined features of the given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefining</code> - the redefining feature</dd>
<dt>Returns:</dt>
<dd>list of redefined features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirectlyRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getDirectlyRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getDirectlyRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining)</span></div>
<div class="block">Returns the directly redefined features of the given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefining</code> - the redefining feature</dd>
<dt>Returns:</dt>
<dd>list of directly redefined features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 @CheckForNull
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</span></div>
<div class="block">Sets the redefined feature of the given redefining feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefining</code> - the redefining feature</dd>
<dd><code>redefined</code> - the redefined feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">
<h3>setRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; redefined)</span></div>
<div class="block">Sets the redefined features of the given redefining feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefining</code> - the redefining feature</dd>
<dd><code>redefined</code> - list of redefined features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>addRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</span></div>
<div class="block">Adds a redefined feature to the given redefining feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefining</code> - the redefining feature</dd>
<dd><code>redefined</code> - the feature to add as redefined</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="forEachRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Consumer)">
<h3>forEachRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">forEachRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; consumer)</span></div>
<div class="block">Applies the given consumer to each redefined feature of the redefining feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefining</code> - the redefining feature</dd>
<dd><code>consumer</code> - action applied to each redefined feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRedefining(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">
<h3>createRedefining</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">createRedefining</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined,
 <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> namespace)</span></div>
<div class="block">Creates a new redefining feature for the given redefined feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefined</code> - the feature to redefine</dd>
<dd><code>namespace</code> - the namespace where the new feature will be created</dd>
<dt>Returns:</dt>
<dd>the newly created redefining feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="matchSelfOrRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Predicate)">
<h3>matchSelfOrRedefined</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">matchSelfOrRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; filter)</span></div>
<div class="block">Returns the first feature that matches the predicate,
 searching the feature and its redefined chain.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefining</code> - the starting feature</dd>
<dd><code>filter</code> - predicate to test</dd>
<dt>Returns:</dt>
<dd>matching feature, or null if none found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="traverseRedefinedFeaturesRecursively(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Predicate)">
<h3>traverseRedefinedFeaturesRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">traverseRedefinedFeaturesRecursively</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; predicate)</span></div>
<div class="block">Traverse redefined features recursively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - feature to start.</dd>
<dd><code>predicate</code> - test redefined feature, return false to abort operation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedRedefining(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getOwnedRedefining</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwnedRedefining</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</span></div>
<div class="block">Returns the owned feature of the type that redefines the given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose features are inspected</dd>
<dd><code>redefined</code> - the feature being redefined</dd>
<dt>Returns:</dt>
<dd>the redefining feature, or null if none found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateOwnedRedefining(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getOrCreateOwnedRedefining</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateOwnedRedefining</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</span></div>
<div class="block">Returns the owned redefining feature, creating one if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose features are modified</dd>
<dd><code>redefined</code> - the feature to redefine</dd>
<dt>Returns:</dt>
<dd>the existing or newly created redefining feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateOwnedRedefining(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Supplier)">
<h3>getOrCreateOwnedRedefining</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateOwnedRedefining</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;org.eclipse.emf.ecore.EClass&gt; redefiningECLassSupplier)</span></div>
<div class="block">Returns the owned redefining feature, creating one if necessary,
 using the supplied EClass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose features are modified</dd>
<dd><code>redefined</code> - the feature to redefine</dd>
<dd><code>redefiningECLassSupplier</code> - supplier for the redefining feature class</dd>
<dt>Returns:</dt>
<dd>the existing or newly created redefining feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefiningOrSame(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getRedefiningOrSame</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getRedefiningOrSame</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefined)</span></div>
<div class="block">Returns the redefining feature of the type, or the feature itself if none exists.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose features are inspected</dd>
<dd><code>redefined</code> - the feature being redefined</dd>
<dt>Returns:</dt>
<dd>redefining feature or the original feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFirsRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,boolean)">
<h3>setFirsRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setFirsRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefining,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; redefined,
 boolean set)</span></div>
<div class="block">Set redefined feature of given redefining feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefining</code> - redefining feature</dd>
<dd><code>redefined</code> - redefined feature chain</dd>
<dd><code>set</code> - if set to true, find the first <a href="kerml/Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Redefinition</code></a> and update it, if false - create new <a href="kerml/Redefinition.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Redefinition</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAllRedefined(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List,boolean)">
<h3>setAllRedefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setAllRedefined</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> redefiningFeature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;&gt; redefined,
 boolean set)</span></div>
<div class="block">Set redefined features of given redefining feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>redefiningFeature</code> - redefining feature</dd>
<dd><code>redefined</code> - redefined features chains</dd>
<dd><code>set</code> - if set to true, replace all existing redefined with given one, if false, append given ones</dd>
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
