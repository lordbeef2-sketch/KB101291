# JAVA OPENAPI: Refactoring.Replacing (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/Refactoring.Replacing.html
- source_path: `com/nomagic/magicdraw/uml/Refactoring.Replacing.html`
- source_sha256: `dfa41057d6d87418c4d29cbe32be187f03821c07a93d19dc22e142557d0e3ead`
- captured_utc: `2026-07-14T16:46:05.418873+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class Refactoring.Replacing

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.Refactoring.Replacing

Enclosing class:
`[Refactoring](Refactoring.html)`

@OpenApiAllpublic static classRefactoring.Replacing
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Replaces elements in the model.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Replacing](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[replace](#replace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.ConvertElementInfo))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) elementToReplace,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) elementToReplaceWith,
 [ConvertElementInfo](ConvertElementInfo.html) info)`
Replaces an element with another element.
`static void`
`[replacePropertyType](#replacePropertyType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier,com.nomagic.magicdraw.mapping.AutomaticElementMappingRule,java.util.Map))([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [EncapsulatedClassifier](../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html) newClassifier,
 [AutomaticElementMappingRule](../mapping/AutomaticElementMappingRule.html) mappingRule,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>,[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>> manuallyMappedPorts)`
Replaces type of the property.
`static void`
`[replacePropertyType](#replacePropertyType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier,java.util.Map))([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [EncapsulatedClassifier](../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html) newClassifier,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>,[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>> manuallyMappedPorts)`
Replaces type of the property.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Replacing
public Replacing()
 ============ METHOD DETAIL ========== 
Method Details
replace
public static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) replace([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) elementToReplace,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) elementToReplaceWith,
 [ConvertElementInfo](ConvertElementInfo.html) info)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)
Replaces an element with another element.
Parameters:
`elementToReplace` - element to replace.
`elementToReplaceWith` - element with which to replace.
`info` - conversion rules.
Returns:
element with which element was replaced.
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)` - if given element is not editable (read-only).
replacePropertyType
public static void replacePropertyType([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [EncapsulatedClassifier](../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html) newClassifier,
 @CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>,[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>> manuallyMappedPorts)
Replaces type of the property. In case old and new property types owns ports,
 replaces old ports with new type ones and reconnects connectors, that where connected to the old ports.
 This way content of Composite Structure diagrams is not lost when property type is replaced.
 This method tries to map ports automatically using some default rules (basically maps ports with same name and type,
 or compatible interfaces)
Parameters:
`property` - Property with type that owns ports.
`newClassifier` - new EncapsulatedClassifier to become the type of the property
`manuallyMappedPorts` - map of manually selected ports to map. Keys of this map are old type ports, and values
 are new type ports. Ports are stored in lists, to describe full nested structure of nested
 ports. If port is not nested, than list contains only one element. Else, list is full path of
 ports starting with the port that is directly on property's old type.
 Note: if some source port was mapped automatically, but also provided in this map,
 then mapping value from this map will be used.
replacePropertyType
public static void replacePropertyType([Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) property,
 [EncapsulatedClassifier](../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html) newClassifier,
 [AutomaticElementMappingRule](../mapping/AutomaticElementMappingRule.html) mappingRule,
 @CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>,[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>> manuallyMappedPorts)
Replaces type of the property. In case old and new property types owns ports,
 replaces old ports with new type ones and reconnects connectors, that where connected to the old ports.
 This way content of Composite Structure diagrams is not lost when property type is replaced.
Parameters:
`property` - Property with type that owns ports.
`newClassifier` - new EncapsulatedClassifier to become the type of the property
`mappingRule` - [`AutomaticElementMappingRule`](../mapping/AutomaticElementMappingRule.html) describing how each old (source) port can be replaced with one of
 new (target) ports.
`manuallyMappedPorts` - map of manually selected ports to map. Keys of this map are old type ports, and values
 are new type ports. Ports are stored in lists, to describe full nested structure of nested
 ports. If port is not nested, than list contains only one element. Else, list is full path of
 ports starting with the port that is directly on property's old type.
 Note: if some source port was mapped using mappingRule, but also provided in this map,
 then mapping value from this map will be used.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class Refactoring.Replacing">Class Refactoring.Replacing</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.Refactoring.Replacing</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="Refactoring.html" title="class in com.nomagic.magicdraw.uml">Refactoring</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public static class </span><span class="element-name type-name-label">Refactoring.Replacing</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Replaces elements in the model.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Replacing</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.ConvertElementInfo)">replace</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> elementToReplace,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> elementToReplaceWith,
 <a href="ConvertElementInfo.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfo</a> info)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replaces an element with another element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replacePropertyType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier,com.nomagic.magicdraw.mapping.AutomaticElementMappingRule,java.util.Map)">replacePropertyType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a href="../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a> newClassifier,
 <a href="../mapping/AutomaticElementMappingRule.html" title="interface in com.nomagic.magicdraw.mapping">AutomaticElementMappingRule</a> mappingRule,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;&gt; manuallyMappedPorts)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replaces type of the property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replacePropertyType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier,java.util.Map)">replacePropertyType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a href="../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a> newClassifier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;&gt; manuallyMappedPorts)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replaces type of the property.</div>
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
<h3>Replacing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Replacing</span>()</div>
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
<section class="detail" id="replace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.uml.ConvertElementInfo)">
<h3>replace</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">replace</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> elementToReplace,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> elementToReplaceWith,
 <a href="ConvertElementInfo.html" title="class in com.nomagic.magicdraw.uml">ConvertElementInfo</a> info)</span>
                       throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Replaces an element with another element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementToReplace</code> - element to replace.</dd>
<dd><code>elementToReplaceWith</code> - element with which to replace.</dd>
<dd><code>info</code> - conversion rules.</dd>
<dt>Returns:</dt>
<dd>element with which element was replaced.</dd>
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given element is not editable (read-only).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="replacePropertyType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier,java.util.Map)">
<h3>replacePropertyType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">replacePropertyType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a href="../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a> newClassifier,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;&gt; manuallyMappedPorts)</span></div>
<div class="block">Replaces type of the property. In case old and new property types owns ports,
 replaces old ports with new type ones and reconnects connectors, that where connected to the old ports.
 This way content of Composite Structure diagrams is not lost when property type is replaced.
 This method tries to map ports automatically using some default rules (basically maps ports with same name and type,
 or compatible interfaces)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - Property with type that owns ports.</dd>
<dd><code>newClassifier</code> - new EncapsulatedClassifier to become the type of the property</dd>
<dd><code>manuallyMappedPorts</code> - map of manually selected ports to map. Keys of this map are old type ports, and values
                            are new type ports. Ports are stored in lists, to describe full nested structure of nested
                            ports. If port is not nested, than list contains only one element. Else, list is full path of
                            ports starting with the port that is directly on property's old type.
                            Note: if some source port was mapped automatically, but also provided in this map,
                            then mapping value from this map will be used.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="replacePropertyType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property,com.nomagic.uml2.ext.magicdraw.compositestructures.mdports.EncapsulatedClassifier,com.nomagic.magicdraw.mapping.AutomaticElementMappingRule,java.util.Map)">
<h3>replacePropertyType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">replacePropertyType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> property,
 <a href="../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a> newClassifier,
 <a href="../mapping/AutomaticElementMappingRule.html" title="interface in com.nomagic.magicdraw.mapping">AutomaticElementMappingRule</a> mappingRule,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;&gt; manuallyMappedPorts)</span></div>
<div class="block">Replaces type of the property. In case old and new property types owns ports,
 replaces old ports with new type ones and reconnects connectors, that where connected to the old ports.
 This way content of Composite Structure diagrams is not lost when property type is replaced.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - Property with type that owns ports.</dd>
<dd><code>newClassifier</code> - new EncapsulatedClassifier to become the type of the property</dd>
<dd><code>mappingRule</code> - <a href="../mapping/AutomaticElementMappingRule.html" title="interface in com.nomagic.magicdraw.mapping"><code>AutomaticElementMappingRule</code></a> describing how each old (source) port can be replaced with one of
                            new (target) ports.</dd>
<dd><code>manuallyMappedPorts</code> - map of manually selected ports to map. Keys of this map are old type ports, and values
                            are new type ports. Ports are stored in lists, to describe full nested structure of nested
                            ports. If port is not nested, than list contains only one element. Else, list is full path of
                            ports starting with the port that is directly on property's old type.
                            Note: if some source port was mapped using mappingRule, but also provided in this map,
                            then mapping value from this map will be used.</dd>
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
