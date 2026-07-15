# JAVA OPENAPI: Links (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml2/Links.html
- source_path: `com/nomagic/magicdraw/uml2/Links.html`
- source_sha256: `49709d701250e5abfea8e8e3cc9ea3ca2475ea4bd708bda6523e9ebfee8d860a`
- captured_utc: `2026-07-14T16:58:33.382240+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2](package-summary.html)

## Class Links

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.Links

public classLinks
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Convenient static methods to work with Link (InstanceSpecification) elements.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Links](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html)`
`[findRelatedAssociation](#findRelatedAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot))([Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot)`
Association property of Slot defining feature
`static [Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html)`
`[findRelatedAssociation](#findRelatedAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) value)`
If owning slot defining feature is association member end - returns that association
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html)>`
`[findRelatedLinks](#findRelatedLinks(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceValue))([InstanceValue](../../uml2/ext/magicdraw/classes/mdkernel/InstanceValue.html) instanceValue)`
If Instance value corresponds to connected instance, returns link which connects two instances.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html)>`
`[findRelatedLinks](#findRelatedLinks(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot))([Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot)`
If slot value corresponds to connected instance, returns link which connects two instances.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html)>`
`[getAssociationsOfLink](#getAssociationsOfLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance)`
Gets Association classifier from InstanceSpecification, if exists.
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getClientElement](#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link)`
Return client element from InstanceSpecification (link)
 Custom way to get relationship info from Link
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getSupplierElement](#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link)`
Returns supplier element from InstanceSpecification (Link)
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>`
`[hasCorrectClassifier](#hasCorrectClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link)`
Checks if link is connected to instances according to its association;
 Check is done by checking if instance values has classifiers same as association member end types
`static boolean`
`[isLink](#isLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance)`
Checks if InstanceSpecification is Link.
`static void`
`[moveSlotReference](#moveSlotReference(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) stableEnd,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) movedEnd,
 [InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) source,
 [InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) destination,
 [InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) stableInstance)`
Updates slots when link ends were changed
`static void`
`[setConnectedInstance](#setConnectedInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) memberEnd)`

`static void`
`[setLinkClientElement](#setLinkClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`
Sets client element from InstanceSpecification (link)
`static void`
`[setLinkSupplierElement](#setLinkSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)`
Sets supplier element for InstanceSpecification (link)
 Custom way to make Link behavior as relationship - add client and supplier info to the slots
`static void`
`[synchronizeLinkSlotValuesByType](#synchronizeLinkSlotValuesByType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link)`
During link end change, sometimes opposite side instance values are defined, and they need to be switched
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Links
public Links()
 ============ METHOD DETAIL ========== 
Method Details
getClientElement
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getClientElement([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link)
Return client element from InstanceSpecification (link)
 Custom way to get relationship info from Link
Parameters:
`link` - link
Returns:
Client element
getSupplierElement
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getSupplierElement([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link)
Returns supplier element from InstanceSpecification (Link)
Parameters:
`link` - link
Returns:
supplier element
setConnectedInstance
public static void setConnectedInstance([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) memberEnd)
synchronizeLinkSlotValuesByType
public static void synchronizeLinkSlotValuesByType([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link)
During link end change, sometimes opposite side instance values are defined, and they need to be switched
Parameters:
`link` - synchronized link
hasCorrectClassifier
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Classifier](../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> hasCorrectClassifier([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link)
Checks if link is connected to instances according to its association;
 Check is done by checking if instance values has classifiers same as association member end types
Parameters:
`link` - link (only links are analyzed)
Returns:
empty list if OK, wrong classifiers if not
moveSlotReference
public static void moveSlotReference([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) stableEnd,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) movedEnd,
 [InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) source,
 [InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) destination,
 [InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) stableInstance)
Updates slots when link ends were changed
Parameters:
`stableEnd` - association member end, which is representing link end does not move
`movedEnd` - association member end, which is representing link end moves
`source` - disconnected instance
`destination` - connected instance
`stableInstance` - stable instance (which end was not changed)
setLinkClientElement
public static void setLinkClientElement([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
Sets client element from InstanceSpecification (link)
Parameters:
`link` - link
`value` - new client value
setLinkSupplierElement
public static void setLinkSupplierElement([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) link,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) value)
Sets supplier element for InstanceSpecification (link)
 Custom way to make Link behavior as relationship - add client and supplier info to the slots
Parameters:
`link` - link
`value` - new supplier value
isLink
public static boolean isLink(@CheckForNull
 [InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance)
Checks if InstanceSpecification is Link.
Parameters:
`instance` - instance to check
Returns:
true if it is Link element - it has Association as classifier or has a Link symbol in diagram
getAssociationsOfLink
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html)> getAssociationsOfLink([InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html) instance)
Gets Association classifier from InstanceSpecification, if exists.
Parameters:
`instance` - Link instance
Returns:
Associations or empty collection
findRelatedLinks
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html)> findRelatedLinks(@CheckForNull
 [Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot)
If slot value corresponds to connected instance, returns link which connects two instances.
Parameters:
`slot` - instance slot
Returns:
connecting links
findRelatedLinks
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InstanceSpecification](../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html)> findRelatedLinks(@CheckForNull
 [InstanceValue](../../uml2/ext/magicdraw/classes/mdkernel/InstanceValue.html) instanceValue)
If Instance value corresponds to connected instance, returns link which connects two instances.
Parameters:
`instanceValue` - instance value
Returns:
connecting links
findRelatedAssociation
@CheckForNullpublic static [Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) findRelatedAssociation(@CheckForNull
 [ValueSpecification](../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) value)
If owning slot defining feature is association member end - returns that association
Parameters:
`value` - slot instance value
Returns:
association which property is defining feature for instance value owning slot or `null`
findRelatedAssociation
@CheckForNullpublic static [Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) findRelatedAssociation(@CheckForNull
 [Slot](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html) slot)
Association property of Slot defining feature
Parameters:
`slot` - slot
Returns:
Association of defining feature or `null`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2</a></div>
<h1 class="title" title="Class Links">Class Links</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.Links</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">Links</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Convenient static methods to work with Link (InstanceSpecification) elements.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Links</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findRelatedAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">findRelatedAssociation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Association property of Slot defining feature</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findRelatedAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">findRelatedAssociation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">If owning slot defining feature is association member end - returns that association</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findRelatedLinks(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceValue)">findRelatedLinks</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a> instanceValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">If Instance value corresponds to connected instance, returns link which connects two instances.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findRelatedLinks(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">findRelatedLinks</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">If slot value corresponds to connected instance, returns link which connects two instances.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssociationsOfLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">getAssociationsOfLink</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets Association classifier from InstanceSpecification, if exists.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">getClientElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return client element from InstanceSpecification (link)
 Custom way to get relationship info from Link</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">getSupplierElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns supplier element from InstanceSpecification (Link)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasCorrectClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">hasCorrectClassifier</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if link is connected to instances according to its association;
 Check is done by checking if instance values has classifiers same as association member end types</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">isLink</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if InstanceSpecification is Link.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#moveSlotReference(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">moveSlotReference</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> stableEnd,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> movedEnd,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> source,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> destination,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> stableInstance)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Updates slots when link ends were changed</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setConnectedInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">setConnectedInstance</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> memberEnd)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setLinkClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setLinkClientElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets client element from InstanceSpecification (link)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setLinkSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setLinkSupplierElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets supplier element for InstanceSpecification (link)
 Custom way to make Link behavior as relationship - add client and supplier info to the slots</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#synchronizeLinkSlotValuesByType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">synchronizeLinkSlotValuesByType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">During link end change, sometimes opposite side instance values are defined, and they need to be switched</div>
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
<h3>Links</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Links</span>()</div>
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
<section class="detail" id="getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>getClientElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getClientElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link)</span></div>
<div class="block">Return client element from InstanceSpecification (link)
 Custom way to get relationship info from Link</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>link</code> - link</dd>
<dt>Returns:</dt>
<dd>Client element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>getSupplierElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getSupplierElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link)</span></div>
<div class="block">Returns supplier element from InstanceSpecification (Link)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>link</code> - link</dd>
<dt>Returns:</dt>
<dd>supplier element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConnectedInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>setConnectedInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setConnectedInstance</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> memberEnd)</span></div>
</section>
</li>
<li>
<section class="detail" id="synchronizeLinkSlotValuesByType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>synchronizeLinkSlotValuesByType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">synchronizeLinkSlotValuesByType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link)</span></div>
<div class="block">During link end change, sometimes opposite side instance values are defined, and they need to be switched</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>link</code> - synchronized link</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasCorrectClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>hasCorrectClassifier</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">hasCorrectClassifier</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link)</span></div>
<div class="block">Checks if link is connected to instances according to its association;
 Check is done by checking if instance values has classifiers same as association member end types</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>link</code> - link (only links are analyzed)</dd>
<dt>Returns:</dt>
<dd>empty list if OK, wrong classifiers if not</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="moveSlotReference(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>moveSlotReference</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">moveSlotReference</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> stableEnd,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> movedEnd,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> source,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> destination,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> stableInstance)</span></div>
<div class="block">Updates slots when link ends were changed</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stableEnd</code> - association member end, which is representing link end does not move</dd>
<dd><code>movedEnd</code> - association member end, which is representing link end moves</dd>
<dd><code>source</code> - disconnected instance</dd>
<dd><code>destination</code> - connected instance</dd>
<dd><code>stableInstance</code> - stable instance (which end was not changed)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLinkClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setLinkClientElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setLinkClientElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
<div class="block">Sets client element from InstanceSpecification (link)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>link</code> - link</dd>
<dd><code>value</code> - new client value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLinkSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setLinkSupplierElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setLinkSupplierElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> link,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
<div class="block">Sets supplier element for InstanceSpecification (link)
 Custom way to make Link behavior as relationship - add client and supplier info to the slots</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>link</code> - link</dd>
<dd><code>value</code> - new supplier value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>isLink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLink</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance)</span></div>
<div class="block">Checks if InstanceSpecification is Link.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - instance to check</dd>
<dt>Returns:</dt>
<dd>true if it is Link element - it has Association as classifier or has a Link symbol in diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssociationsOfLink(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>getAssociationsOfLink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;</span> <span class="element-name">getAssociationsOfLink</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> instance)</span></div>
<div class="block">Gets Association classifier from InstanceSpecification, if exists.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - Link instance</dd>
<dt>Returns:</dt>
<dd>Associations or empty collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findRelatedLinks(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">
<h3>findRelatedLinks</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</span> <span class="element-name">findRelatedLinks</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot)</span></div>
<div class="block">If slot value corresponds to connected instance, returns link which connects two instances.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slot</code> - instance slot</dd>
<dt>Returns:</dt>
<dd>connecting links</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findRelatedLinks(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceValue)">
<h3>findRelatedLinks</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a>&gt;</span> <span class="element-name">findRelatedLinks</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a> instanceValue)</span></div>
<div class="block">If Instance value corresponds to connected instance, returns link which connects two instances.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instanceValue</code> - instance value</dd>
<dt>Returns:</dt>
<dd>connecting links</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findRelatedAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>findRelatedAssociation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></span> <span class="element-name">findRelatedAssociation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</span></div>
<div class="block">If owning slot defining feature is association member end - returns that association</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - slot instance value</dd>
<dt>Returns:</dt>
<dd>association which property is defining feature for instance value owning slot or <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findRelatedAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">
<h3>findRelatedAssociation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></span> <span class="element-name">findRelatedAssociation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> slot)</span></div>
<div class="block">Association property of Slot defining feature</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>slot</code> - slot</dd>
<dt>Returns:</dt>
<dd>Association of defining feature or <code>null</code></dd>
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
