# JAVA OPENAPI: SysMLUtility (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/sysml/util/SysMLUtility.html
- source_path: `com/nomagic/magicdraw/sysml/util/SysMLUtility.html`
- source_sha256: `080e0b7e9ead645cc76904859d5369d77ef877da632900202dad7655ec5a36e1`
- captured_utc: `2026-07-14T16:45:46.760625+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.sysml.util](package-summary.html)

## Class SysMLUtility

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.sysml.util.SysMLUtility

Direct Known Subclasses:
`[SysMLUtilities](SysMLUtilities.html)`

@OpenApiAllpublic classSysMLUtility
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

SysML utilities.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static enum`
`[SysMLUtility.DirectedFeature](SysMLUtility.DirectedFeature.html)`
DirectedFeature enumeration
`static enum`
`[SysMLUtility.FlowDirection](SysMLUtility.FlowDirection.html)`
Flow Direction enumeration
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SysMLUtility](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDirectionForPort](#getDirectionForPort(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return element direction
`static [SysMLUtility.DirectedFeature](SysMLUtility.DirectedFeature.html)`
`[getFeatureDirection](#getFeatureDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature))([Feature](../../../uml2/ext/magicdraw/classes/mdkernel/Feature.html) feature)`
Returns DirectedFeatures featureDirection tag value
`static [SysMLUtility.FlowDirection](SysMLUtility.FlowDirection.html)`
`[getFlowDirection](#getFlowDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return the direction from element with flow direction (Flow Port and Flow Property)
`static boolean`
`[isAtomicFlowPort](#isAtomicFlowPort(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port))([Port](../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html) port)`
Check if flowPort is atomic or not.
`static boolean`
`[isBlockNotConstraint](#isBlockNotConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if an element is a block or a derived block but not a constraint block (or derived).
`static boolean`
`[isEncapsulated](#isEncapsulated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check the isEncapsulated of element `element`.
`static boolean`
`[isInterfaceBlockNotConstraint](#isInterfaceBlockNotConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if an element is a InterfaceBlock or a derived InterfaceBlock but not a constraint block (or derived).
`static void`
`[setDirectionForFlowPort](#setDirectionForFlowPort(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,com.nomagic.magicdraw.sysml.util.SysMLUtility.FlowDirection))([Port](../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html) port,
 [SysMLUtility.FlowDirection](SysMLUtility.FlowDirection.html) direction)`
Set the direction for flowPort.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SysMLUtility
public SysMLUtility()
 ============ METHOD DETAIL ========== 
Method Details
isBlockNotConstraint
public static boolean isBlockNotConstraint(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if an element is a block or a derived block but not a constraint block (or derived).
Parameters:
`element` - the element to check
Returns:
true if element is a block but not a constraint block.
isInterfaceBlockNotConstraint
public static boolean isInterfaceBlockNotConstraint(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if an element is a InterfaceBlock or a derived InterfaceBlock but not a constraint block (or derived).
Parameters:
`element` - the element to check
Returns:
true if element is a block but not a constraint block.
isAtomicFlowPort
public static boolean isAtomicFlowPort([Port](../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html) port)
Check if flowPort is atomic or not.
Parameters:
`port` - flowPort to check
Returns:
`true` is flowPort atomic, `false` if non-atomic
setDirectionForFlowPort
public static void setDirectionForFlowPort([Port](../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html) port,
 [SysMLUtility.FlowDirection](SysMLUtility.FlowDirection.html) direction)
Set the direction for flowPort.
Parameters:
`port` - flowPort element
`direction` - flow direction
getFlowDirection
public static [SysMLUtility.FlowDirection](SysMLUtility.FlowDirection.html) getFlowDirection([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return the direction from element with flow direction (Flow Port and Flow Property)
Parameters:
`element` - element with flow direction
Returns:
flow direction, empty if direction is not set
isEncapsulated
public static boolean isEncapsulated([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check the isEncapsulated of element `element`.
Parameters:
`element` - element to check
Returns:
`true` when encapsulated, `false` when not encapsulated or value is not set.
getFeatureDirection
@CheckForNullpublic static [SysMLUtility.DirectedFeature](SysMLUtility.DirectedFeature.html) getFeatureDirection([Feature](../../../uml2/ext/magicdraw/classes/mdkernel/Feature.html) feature)
Returns DirectedFeatures featureDirection tag value
Parameters:
`feature` - DirectedFeature to check
Returns:
direction of feature
getDirectionForPort
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDirectionForPort([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return element direction
Parameters:
`element` - element from which to get direction
Returns:
element direction string

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.sysml.util</a></div>
<h1 class="title" title="Class SysMLUtility">Class SysMLUtility</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.sysml.util.SysMLUtility</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="SysMLUtilities.html" title="class in com.nomagic.magicdraw.sysml.util">SysMLUtilities</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SysMLUtility</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">SysML utilities.</div>
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
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysMLUtility.DirectedFeature.html" title="enum class in com.nomagic.magicdraw.sysml.util">SysMLUtility.DirectedFeature</a></code></div>
<div class="col-last even-row-color">
<div class="block">DirectedFeature enumeration</div>
</div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysMLUtility.FlowDirection.html" title="enum class in com.nomagic.magicdraw.sysml.util">SysMLUtility.FlowDirection</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Flow Direction enumeration</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SysMLUtility</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirectionForPort(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getDirectionForPort</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return element direction</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SysMLUtility.DirectedFeature.html" title="enum class in com.nomagic.magicdraw.sysml.util">SysMLUtility.DirectedFeature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeatureDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature)">getFeatureDirection</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns DirectedFeatures featureDirection tag value</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SysMLUtility.FlowDirection.html" title="enum class in com.nomagic.magicdraw.sysml.util">SysMLUtility.FlowDirection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFlowDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getFlowDirection</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return the direction from element with flow direction (Flow Port and Flow Property)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAtomicFlowPort(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port)">isAtomicFlowPort</a><wbr/>(<a href="../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> port)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if flowPort is atomic or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isBlockNotConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isBlockNotConstraint</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if an element is a block or a derived block but not a constraint block (or derived).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEncapsulated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isEncapsulated</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check the isEncapsulated of element <code>element</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInterfaceBlockNotConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isInterfaceBlockNotConstraint</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if an element is a InterfaceBlock or a derived InterfaceBlock but not a constraint block (or derived).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirectionForFlowPort(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,com.nomagic.magicdraw.sysml.util.SysMLUtility.FlowDirection)">setDirectionForFlowPort</a><wbr/>(<a href="../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> port,
 <a href="SysMLUtility.FlowDirection.html" title="enum class in com.nomagic.magicdraw.sysml.util">SysMLUtility.FlowDirection</a> direction)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set the direction for flowPort.</div>
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
<h3>SysMLUtility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SysMLUtility</span>()</div>
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
<section class="detail" id="isBlockNotConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isBlockNotConstraint</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isBlockNotConstraint</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if an element is a block or a derived block but not a constraint block (or derived).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if element is a block but not a constraint block.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInterfaceBlockNotConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isInterfaceBlockNotConstraint</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInterfaceBlockNotConstraint</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if an element is a InterfaceBlock or a derived InterfaceBlock but not a constraint block (or derived).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if element is a block but not a constraint block.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAtomicFlowPort(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port)">
<h3>isAtomicFlowPort</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAtomicFlowPort</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> port)</span></div>
<div class="block">Check if flowPort is atomic or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>port</code> - flowPort to check</dd>
<dt>Returns:</dt>
<dd><code>true</code> is flowPort atomic, <code>false</code> if non-atomic</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirectionForFlowPort(com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.Port,com.nomagic.magicdraw.sysml.util.SysMLUtility.FlowDirection)">
<h3>setDirectionForFlowPort</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setDirectionForFlowPort</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a> port,
 <a href="SysMLUtility.FlowDirection.html" title="enum class in com.nomagic.magicdraw.sysml.util">SysMLUtility.FlowDirection</a> direction)</span></div>
<div class="block">Set the direction for flowPort.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>port</code> - flowPort element</dd>
<dd><code>direction</code> - flow direction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFlowDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getFlowDirection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SysMLUtility.FlowDirection.html" title="enum class in com.nomagic.magicdraw.sysml.util">SysMLUtility.FlowDirection</a></span> <span class="element-name">getFlowDirection</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return the direction from element with flow direction (Flow Port and Flow Property)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element with flow direction</dd>
<dt>Returns:</dt>
<dd>flow direction, empty if direction is not set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEncapsulated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isEncapsulated</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEncapsulated</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check the isEncapsulated of element <code>element</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check</dd>
<dt>Returns:</dt>
<dd><code>true</code> when encapsulated, <code>false</code> when not encapsulated or value is not set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeatureDirection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature)">
<h3>getFeatureDirection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="SysMLUtility.DirectedFeature.html" title="enum class in com.nomagic.magicdraw.sysml.util">SysMLUtility.DirectedFeature</a></span> <span class="element-name">getFeatureDirection</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a> feature)</span></div>
<div class="block">Returns DirectedFeatures featureDirection tag value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - DirectedFeature to check</dd>
<dt>Returns:</dt>
<dd>direction of feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirectionForPort(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getDirectionForPort</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDirectionForPort</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return element direction</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element from which to get direction</dd>
<dt>Returns:</dt>
<dd>element direction string</dd>
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
