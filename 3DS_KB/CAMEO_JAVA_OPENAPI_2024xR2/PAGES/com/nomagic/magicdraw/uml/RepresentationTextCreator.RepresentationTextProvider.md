# JAVA OPENAPI: RepresentationTextCreator.RepresentationTextProvider (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/RepresentationTextCreator.RepresentationTextProvider.html
- source_path: `com/nomagic/magicdraw/uml/RepresentationTextCreator.RepresentationTextProvider.html`
- source_sha256: `e368dc63172f815ca37804be8ce84d859967e8a15ad2c02c053d353b3f3714ef`
- captured_utc: `2026-07-14T16:55:53.982441+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Interface RepresentationTextCreator.RepresentationTextProvider

All Superinterfaces:
`[PriorityProvider](../utils/PriorityProvider.html)`, `[PriorityProvider](../../utils/PriorityProvider.html)`

Enclosing class:
[RepresentationTextCreator](RepresentationTextCreator.html)

public static interfaceRepresentationTextCreator.RepresentationTextProviderextends [PriorityProvider](../utils/PriorityProvider.html)

Representation text provider extension point.
 Plugins may register these providers and override default element's representation text displayed in MagicDraw

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`boolean`
`[accept](#accept(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](BaseElement.html) element)`
Checks if this provider should be used to create a representation text for the given element
`default [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>,[SmartListenerConfig](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)>`
`[createAcceptableElementSmartListenerConfig](#createAcceptableElementSmartListenerConfig())()`
Returned [`SmartListenerConfig`](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html) describes on what model changes this representation
 text provider can be started/stopped using as text provider (see [`accept(BaseElement)`](#accept(com.nomagic.magicdraw.uml.BaseElement))).
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>,[SmartListenerConfig](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)>`
`[createSmartListenerConfig](#createSmartListenerConfig())()`
Returns [`SmartListenerConfig`](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html) for the provider.
`default int`
`[getPriority](#getPriority())()`
Returns a priority of text creator.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentedText](#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams))([BaseElement](BaseElement.html) element,
 [RepresentationTextParams](RepresentationTextParams.html) textParams)`
Returns representation text for a given Element.
`default boolean`
`[isHumanTypeUsed](#isHumanTypeUsed())()`
Checks if human type may be used in representation text.

============ METHOD DETAIL ========== 
Method Details
accept
boolean accept([BaseElement](BaseElement.html) element)
Checks if this provider should be used to create a representation text for the given element
Parameters:
`element` - given element
Returns:
true if this provider should be used to create representation text for the given element
getRepresentedText
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentedText([BaseElement](BaseElement.html) element,
 [RepresentationTextParams](RepresentationTextParams.html) textParams)
Returns representation text for a given Element.
Parameters:
`element` - element for which representation text has to be created.
`textParams` - parameters describing how to construct the text, what to include
Returns:
representation text for the given element.
createSmartListenerConfig
[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>,[SmartListenerConfig](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> createSmartListenerConfig()
Returns [`SmartListenerConfig`](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html) for the provider. It describes on what model changes the representation
 texts should be recalculated by explicitly calling RepresentationTextProvider#getRepresentedText(BaseElement, RepresentationTextParams)
 instead of returning a cached value that was calculated earlier.
Returns:
map of configs for this provider or an empty map
See Also:
[`SmartListenerConfig`](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)
createAcceptableElementSmartListenerConfig
default [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>,[SmartListenerConfig](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> createAcceptableElementSmartListenerConfig()
Returned [`SmartListenerConfig`](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html) describes on what model changes this representation
 text provider can be started/stopped using as text provider (see [`accept(BaseElement)`](#accept(com.nomagic.magicdraw.uml.BaseElement))).
 Usually it is simple than [`SmartListenerConfig`](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html) created by [`createSmartListenerConfig()`](#createSmartListenerConfig()).
Returns:
map of configs or an empty map
See Also:
[`SmartListenerConfig`](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)
[`accept(BaseElement)`](#accept(com.nomagic.magicdraw.uml.BaseElement))
isHumanTypeUsed
default boolean isHumanTypeUsed()
Checks if human type may be used in representation text.
Returns:
true human type is used in representation text, otherwise - false
getPriority
default int getPriority()
Returns a priority of text creator.
 The creator with bigger priority will be chosen for representation text creation if several creators accept the same Element.
Specified by:
`[getPriority](../../utils/PriorityProvider.html#getPriority())` in interface `[PriorityProvider](../../utils/PriorityProvider.html)`
Returns:
MEDIUM_PRIORITY be default
See Also:
[`PriorityProvider.MEDIUM_PRIORITY`](../../utils/PriorityProvider.html#MEDIUM_PRIORITY)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Interface RepresentationTextCreator.RepresentationTextProvider">Interface RepresentationTextCreator.RepresentationTextProvider</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></code>, <code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="RepresentationTextCreator.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextCreator</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static interface </span><span class="element-name type-name-label">RepresentationTextCreator.RepresentationTextProvider</span><span class="extends-implements">
extends <a href="../utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></span></div>
<div class="block">Representation text provider extension point.
 <p>
 Plugins may register these providers and override default element's representation text displayed in MagicDraw</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.utils.PriorityProvider">Fields inherited from interface com.nomagic.utils.<a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></h3>
<code><a href="../../utils/PriorityProvider.html#HIGH_PRIORITY">HIGH_PRIORITY</a>, <a href="../../utils/PriorityProvider.html#LOW_PRIORITY">LOW_PRIORITY</a>, <a href="../../utils/PriorityProvider.html#MEDIUM_PRIORITY">MEDIUM_PRIORITY</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.BaseElement)">accept</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if this provider should be used to create a representation text for the given element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;,<wbr/><a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createAcceptableElementSmartListenerConfig()">createAcceptableElementSmartListenerConfig</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returned <a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener"><code>SmartListenerConfig</code></a> describes on what model changes this representation
 text provider can be started/stopped using as text provider (see <a href="#accept(com.nomagic.magicdraw.uml.BaseElement)"><code>accept(BaseElement)</code></a>).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;,<wbr/><a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createSmartListenerConfig()">createSmartListenerConfig</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns <a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener"><code>SmartListenerConfig</code></a> for the provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getPriority()">getPriority</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns a priority of text creator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)">getRepresentedText</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> textParams)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns representation text for a given Element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isHumanTypeUsed()">isHumanTypeUsed</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Checks if human type may be used in representation text.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.BaseElement)">
<h3>accept</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Checks if this provider should be used to create a representation text for the given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dt>Returns:</dt>
<dd>true if this provider should be used to create representation text for the given element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresentedText(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.RepresentationTextParams)">
<h3>getRepresentedText</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentedText</span><wbr/><span class="parameters">(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a> textParams)</span></div>
<div class="block">Returns representation text for a given Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element for which representation text has to be created.</dd>
<dd><code>textParams</code> - parameters describing how to construct the text, what to include</dd>
<dt>Returns:</dt>
<dd>representation text for the given element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSmartListenerConfig()">
<h3>createSmartListenerConfig</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;,<wbr/><a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt;</span> <span class="element-name">createSmartListenerConfig</span>()</div>
<div class="block">Returns <a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener"><code>SmartListenerConfig</code></a> for the provider. It describes on what model changes the representation
 texts should be recalculated by explicitly calling RepresentationTextProvider#getRepresentedText(BaseElement, RepresentationTextParams)
 instead of returning a cached value that was calculated earlier.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of configs for this provider or an empty map</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener"><code>SmartListenerConfig</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAcceptableElementSmartListenerConfig()">
<h3>createAcceptableElementSmartListenerConfig</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;,<wbr/><a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt;</span> <span class="element-name">createAcceptableElementSmartListenerConfig</span>()</div>
<div class="block">Returned <a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener"><code>SmartListenerConfig</code></a> describes on what model changes this representation
 text provider can be started/stopped using as text provider (see <a href="#accept(com.nomagic.magicdraw.uml.BaseElement)"><code>accept(BaseElement)</code></a>).
 Usually it is simple than <a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener"><code>SmartListenerConfig</code></a> created by <a href="#createSmartListenerConfig()"><code>createSmartListenerConfig()</code></a>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of configs or an empty map</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener"><code>SmartListenerConfig</code></a></li>
<li><a href="#accept(com.nomagic.magicdraw.uml.BaseElement)"><code>accept(BaseElement)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isHumanTypeUsed()">
<h3>isHumanTypeUsed</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isHumanTypeUsed</span>()</div>
<div class="block">Checks if human type may be used in representation text.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true human type is used in representation text, otherwise - false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPriority()">
<h3>getPriority</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">int</span> <span class="element-name">getPriority</span>()</div>
<div class="block">Returns a priority of text creator.
 The creator with bigger priority will be chosen for representation text creation if several creators accept the same Element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../utils/PriorityProvider.html#getPriority()">getPriority</a></code> in interface <code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
<dt>Returns:</dt>
<dd>MEDIUM_PRIORITY be default</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../utils/PriorityProvider.html#MEDIUM_PRIORITY"><code>PriorityProvider.MEDIUM_PRIORITY</code></a></li>
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
