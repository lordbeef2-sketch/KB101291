# JAVA OPENAPI: InstanceSpecifications (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml2/InstanceSpecifications.html
- source_path: `com/nomagic/magicdraw/uml2/InstanceSpecifications.html`
- source_sha256: `89cf854645652bde16cc56763dbb4be6def45ce58049644a6a489cae4e571ba7`
- captured_utc: `2026-07-14T16:56:06.313579+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2](package-summary.html)

## Class InstanceSpecifications

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.InstanceSpecifications

public classInstanceSpecifications
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Convenience static methods that operate on or return InstanceSpecification elements.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[InstanceSpecifications](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html)>`
`[collectInstancesOf](#collectInstancesOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html)> instances)`
Collect all instances of given classifier.
`static void`
`[createSlotsForDefaultValues](#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean createAll)`
Creates slots for properties of all assigned classifiers to instance.
`static void`
`[createSlotsForDefaultValues](#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier,
 boolean createAll)`
Creates slots for properties of given classifier.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html)>`
`[getLinksBetweenInstances](#getLinksBetweenInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) client,
 [InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) supplier)`
Returns links found between client and supplier instances
`static [Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html)`
`[getNestedSlot](#getNestedSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.util.List,int))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instanceSpecification,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)> path,
 int index)`

`static [Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html)`
`[getSlot](#getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instanceSpecification,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property)`
Returns existing slot for a given property in given instance, if any
`static [Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html)`
`[getSlot](#getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 boolean createSlotIfNotExists,
 boolean createDefaultValue)`
Returns existing of creates a new Slot for the given property
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getValueBySlot](#getValueBySlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot))([Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot)`
Retrieves values of slots as object, not as ValueSpecifications.
`static boolean`
`[isDefiningFeatureSuitable](#isDefiningFeatureSuitable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instanceSpecification,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) definingFeature)`
Method to check if instance owns definingFeature (property) directly or indirectly
`static boolean`
`[isInstanceSpecificationCompatibleWithType](#isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean))([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) type,
 [InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean checkInherited)`
Checks if given instance specification is compatible with given Type.
`static void`
`[setClassifiers](#setClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,java.util.Collection,boolean))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 boolean createSlots)`
Set classifiers for instance.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
InstanceSpecifications
public InstanceSpecifications()
 ============ METHOD DETAIL ========== 
Method Details
getSlot
@CheckForNullpublic static [Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) getSlot([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instanceSpecification,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property)
Returns existing slot for a given property in given instance, if any
Parameters:
`instanceSpecification` - instance
`property` - definingFeature of slot
Returns:
slot or null
isDefiningFeatureSuitable
public static boolean isDefiningFeatureSuitable([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instanceSpecification,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) definingFeature)
Method to check if instance owns definingFeature (property) directly or indirectly
Parameters:
`instanceSpecification` - instanceSpecification
`definingFeature` - definingFeature/property
Returns:
true if instance has property, else false
getSlot
@CheckForNullpublic static [Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) getSlot([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 boolean createSlotIfNotExists,
 boolean createDefaultValue)
Returns existing of creates a new Slot for the given property
Parameters:
`instance` - instance specification
`property` - feature
`createSlotIfNotExists` - create a new slot if needed
`createDefaultValue` - fill slot value from property default value
Returns:
slot
getNestedSlot
@CheckForNullpublic static [Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) getNestedSlot([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instanceSpecification,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)> path,
 int index)
createSlotsForDefaultValues
public static void createSlotsForDefaultValues([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier,
 boolean createAll)
Creates slots for properties of given classifier.
Parameters:
`instance` - instance to create slots for
`classifier` - classifier of the instance
`createAll` - true, to create slots for all properties (even without default value)
createSlotsForDefaultValues
public static void createSlotsForDefaultValues([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean createAll)
Creates slots for properties of all assigned classifiers to instance.
Parameters:
`instance` - instance
`createAll` - true, to create slots for all properties (even without default value)
isInstanceSpecificationCompatibleWithType
public static boolean isInstanceSpecificationCompatibleWithType(@CheckForNull
 [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) type,
 [InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 boolean checkInherited)
Checks if given instance specification is compatible with given Type. Instance is compatible if its classifiers
 are compatible with given type.
Parameters:
`type` - instance compatibility will be checked against this type
`instance` - instance to check for compatible classifiers
`checkInherited` - if set to true, then classifiers derived/realized from given type will be treated as compatible.
Returns:
true if instance is compatible with given type
getLinksBetweenInstances
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html)> getLinksBetweenInstances([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) client,
 [InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) supplier)
Returns links found between client and supplier instances
Parameters:
`client` - instance
`supplier` - instance
Returns:
links
collectInstancesOf
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html)> collectInstancesOf([Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html) classifier,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html)> instances)
Collect all instances of given classifier. Instances of derived classifiers are also collected.
Parameters:
`classifier` - classifier
Returns:
the passed in collection, appended with instances of the classifier and its' subtypes
getValueBySlot
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getValueBySlot(@CheckForNull
 [Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot)
Retrieves values of slots as object, not as ValueSpecifications.
 Takes into account multiplicity of slot's defining feature. Collection is returned if slot multiplicity is many.
Parameters:
`slot` - slot
Returns:
value of slot
setClassifiers
public static void setClassifiers([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> classifiers,
 boolean createSlots)
Set classifiers for instance. Method replaces the classifiers, does not append to the current value
Parameters:
`instance` - instance to set classifiers for
`classifiers` - classifiers
`createSlots` - true if slots with default values needs to be created
See Also:
[`createSlotsForDefaultValues(InstanceSpecification, boolean)`](#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2</a></div>
<h1 class="title" title="Class InstanceSpecifications">Class InstanceSpecifications</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.InstanceSpecifications</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">InstanceSpecifications</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Convenience static methods that operate on or return InstanceSpecification elements.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">InstanceSpecifications</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInstancesOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">collectInstancesOf</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt; instances)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect all instances of given classifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">createSlotsForDefaultValues</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean createAll)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates slots for properties of all assigned classifiers to instance.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean)">createSlotsForDefaultValues</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 boolean createAll)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates slots for properties of given classifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getLinksBetweenInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">getLinksBetweenInstances</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> client,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> supplier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns links found between client and supplier instances</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNestedSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.util.List,int)">getNestedSlot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instanceSpecification,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt; path,
 int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">getSlot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instanceSpecification,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns existing slot for a given property in given instance, if any</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean)">getSlot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean createSlotIfNotExists,
 boolean createDefaultValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns existing of creates a new Slot for the given property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueBySlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">getValueBySlot</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves values of slots as object, not as ValueSpecifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDefiningFeatureSuitable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">isDefiningFeatureSuitable</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instanceSpecification,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> definingFeature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Method to check if instance owns definingFeature (property) directly or indirectly</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">isInstanceSpecificationCompatibleWithType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean checkInherited)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given instance specification is compatible with given Type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,java.util.Collection,boolean)">setClassifiers</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 boolean createSlots)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set classifiers for instance.</div>
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
<h3>InstanceSpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">InstanceSpecifications</span>()</div>
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
<section class="detail" id="getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>getSlot</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></span> <span class="element-name">getSlot</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instanceSpecification,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property)</span></div>
<div class="block">Returns existing slot for a given property in given instance, if any</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instanceSpecification</code> - instance</dd>
<dd><code>property</code> - definingFeature of slot</dd>
<dt>Returns:</dt>
<dd>slot or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDefiningFeatureSuitable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>isDefiningFeatureSuitable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDefiningFeatureSuitable</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instanceSpecification,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> definingFeature)</span></div>
<div class="block">Method to check if instance owns definingFeature (property) directly or indirectly</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instanceSpecification</code> - instanceSpecification</dd>
<dd><code>definingFeature</code> - definingFeature/property</dd>
<dt>Returns:</dt>
<dd>true if instance has property, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,boolean,boolean)">
<h3>getSlot</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></span> <span class="element-name">getSlot</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 boolean createSlotIfNotExists,
 boolean createDefaultValue)</span></div>
<div class="block">Returns existing of creates a new Slot for the given property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - instance specification</dd>
<dd><code>property</code> - feature</dd>
<dd><code>createSlotIfNotExists</code> - create a new slot if needed</dd>
<dd><code>createDefaultValue</code> - fill slot value from property default value</dd>
<dt>Returns:</dt>
<dd>slot</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,java.util.List,int)">
<h3>getNestedSlot</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></span> <span class="element-name">getNestedSlot</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instanceSpecification,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt; path,
 int index)</span></div>
</section>
</li>
<li>
<section class="detail" id="createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,boolean)">
<h3>createSlotsForDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createSlotsForDefaultValues</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 boolean createAll)</span></div>
<div class="block">Creates slots for properties of given classifier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - instance to create slots for</dd>
<dd><code>classifier</code> - classifier of the instance</dd>
<dd><code>createAll</code> - true, to create slots for all properties (even without default value)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">
<h3>createSlotsForDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createSlotsForDefaultValues</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean createAll)</span></div>
<div class="block">Creates slots for properties of all assigned classifiers to instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - instance</dd>
<dd><code>createAll</code> - true, to create slots for all properties (even without default value)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInstanceSpecificationCompatibleWithType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)">
<h3>isInstanceSpecificationCompatibleWithType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstanceSpecificationCompatibleWithType</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> type,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 boolean checkInherited)</span></div>
<div class="block">Checks if given instance specification is compatible with given Type. Instance is compatible if its classifiers
 are compatible with given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - instance compatibility will be checked against this type</dd>
<dd><code>instance</code> - instance to check for compatible classifiers</dd>
<dd><code>checkInherited</code> - if set to true, then classifiers derived/realized from given type will be treated as compatible.</dd>
<dt>Returns:</dt>
<dd>true if instance is compatible with given type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLinksBetweenInstances(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>getLinksBetweenInstances</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</span> <span class="element-name">getLinksBetweenInstances</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> client,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> supplier)</span></div>
<div class="block">Returns links found between client and supplier instances</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>client</code> - instance</dd>
<dd><code>supplier</code> - instance</dd>
<dt>Returns:</dt>
<dd>links</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInstancesOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier,java.util.Collection)">
<h3>collectInstancesOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</span> <span class="element-name">collectInstancesOf</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt; instances)</span></div>
<div class="block">Collect all instances of given classifier. Instances of derived classifiers are also collected.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dt>Returns:</dt>
<dd>the passed in collection, appended with instances of the classifier and its' subtypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueBySlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">
<h3>getValueBySlot</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValueBySlot</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot)</span></div>
<div class="block">Retrieves values of slots as object, not as ValueSpecifications.
 Takes into account multiplicity of slot's defining feature. Collection is returned if slot multiplicity is many.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slot</code> - slot</dd>
<dt>Returns:</dt>
<dd>value of slot</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClassifiers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,java.util.Collection,boolean)">
<h3>setClassifiers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setClassifiers</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt; classifiers,
 boolean createSlots)</span></div>
<div class="block">Set classifiers for instance. Method replaces the classifiers, does not append to the current value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - instance to set classifiers for</dd>
<dd><code>classifiers</code> - classifiers</dd>
<dd><code>createSlots</code> - true if slots with default values needs to be created</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#createSlotsForDefaultValues(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,boolean)"><code>createSlotsForDefaultValues(InstanceSpecification, boolean)</code></a></li>
</ul>
</dd>
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
