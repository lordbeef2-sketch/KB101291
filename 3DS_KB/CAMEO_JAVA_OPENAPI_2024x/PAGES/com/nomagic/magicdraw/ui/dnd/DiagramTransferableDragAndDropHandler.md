# JAVA OPENAPI: DiagramTransferableDragAndDropHandler (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/ui/dnd/DiagramTransferableDragAndDropHandler.html
- source_path: `com/nomagic/magicdraw/ui/dnd/DiagramTransferableDragAndDropHandler.html`
- source_sha256: `eebe91a2d2e176def830a9413bad02429639776b191e2d6a5121ca11dee9ecf5`
- captured_utc: `2026-07-14T16:52:05.735795+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dnd](package-summary.html)

## Class DiagramTransferableDragAndDropHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.dnd.DiagramTransferableDragAndDropHandler

All Implemented Interfaces:
`[ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)`, `[PriorityProvider](../../utils/PriorityProvider.html)`, `[PriorityProvider](../../../utils/PriorityProvider.html)`

@OpenApiAllpublic abstract classDiagramTransferableDragAndDropHandler
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)

Drop handler to [`DiagramPresentationElement`](../../uml/symbols/DiagramPresentationElement.html) based on [`Transferable`](https://docs.oracle.com/en/java/javase/17/docs/api/java.datatransfer/java/awt/datatransfer/Transferable.html).

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../../../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../../../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../../../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../../../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramTransferableDragAndDropHandler](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`abstract void`
`[drop](#drop(java.awt.Point,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.datatransfer.Transferable))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagramPresentationElement,
 [PresentationElement](../../uml/symbols/PresentationElement.html) elementOver,
 [Transferable](https://docs.oracle.com/en/java/javase/17/docs/api/java.datatransfer/java/awt/datatransfer/Transferable.html) transferable)`
Drops calculated [`DropTarget`](DropTarget.html).
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription())()`
Returns a human-readable description of what the handler can achieve.
`abstract [DropTarget](DropTarget.html)`
`[getDropTarget](#getDropTarget(java.awt.Point,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,java.awt.datatransfer.Transferable))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagramPresentationElement,
 [Transferable](https://docs.oracle.com/en/java/javase/17/docs/api/java.datatransfer/java/awt/datatransfer/Transferable.html) transferable)`
Gets [`DropTarget`](DropTarget.html) for this handler.
`int`
`[getPriority](#getPriority())()`
Returns priority of this configurator.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramTransferableDragAndDropHandler
public DiagramTransferableDragAndDropHandler()
 ============ METHOD DETAIL ========== 
Method Details
getDropTarget
public abstract [DropTarget](DropTarget.html) getDropTarget([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagramPresentationElement,
 [Transferable](https://docs.oracle.com/en/java/javase/17/docs/api/java.datatransfer/java/awt/datatransfer/Transferable.html) transferable)
Gets [`DropTarget`](DropTarget.html) for this handler.
Parameters:
`location` - location on the diagram
`diagramPresentationElement` - diagram presentation element on which the drag is being performed
`transferable` - transferable drag&drop object
Returns:
calculated drop target for this handler
drop
public abstract void drop([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagramPresentationElement,
 [PresentationElement](../../uml/symbols/PresentationElement.html) elementOver,
 [Transferable](https://docs.oracle.com/en/java/javase/17/docs/api/java.datatransfer/java/awt/datatransfer/Transferable.html) transferable)
Drops calculated [`DropTarget`](DropTarget.html).
Parameters:
`location` - location on the diagram
`diagramPresentationElement` - diagram presentation element
`elementOver` - symbol on which drag is being performed (if drop target was not specified, passes DiagramPresentationElement)
`transferable` - transferable drag&drop object
getDescription
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescription()
Returns a human-readable description of what the handler can achieve.
 Might be used to inform user about the purpose of this handler in various GUI forms, mostly tool tips.
Returns:
description as a String or null if no description is provided
getPriority
public int getPriority()
Description copied from interface: `[ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html#getPriority())`
Returns priority of this configurator. All configurators are sorted by priority before configuration.
 This is very important if one configurator expects input from other configurators.
 In such case configurator must have lower priority than others.
Specified by:
`[getPriority](../../actions/ConfiguratorWithPriority.html#getPriority())` in interface `[ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)`
Specified by:
`[getPriority](../../../utils/PriorityProvider.html#getPriority())` in interface `[PriorityProvider](../../../utils/PriorityProvider.html)`
Returns:
priority of this configurator.
See Also:
[`PriorityProvider.HIGH_PRIORITY`](../../../utils/PriorityProvider.html#HIGH_PRIORITY)
[`PriorityProvider.MEDIUM_PRIORITY`](../../../utils/PriorityProvider.html#MEDIUM_PRIORITY)
[`PriorityProvider.LOW_PRIORITY`](../../../utils/PriorityProvider.html#LOW_PRIORITY)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dnd</a></div>
<h1 class="title" title="Class DiagramTransferableDragAndDropHandler">Class DiagramTransferableDragAndDropHandler</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dnd.DiagramTransferableDragAndDropHandler</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code>, <code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></code>, <code><a href="../../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">DiagramTransferableDragAndDropHandler</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></span></div>
<div class="block">Drop handler to <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>DiagramPresentationElement</code></a> based on <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.datatransfer/java/awt/datatransfer/Transferable.html" title="class or interface in java.awt.datatransfer"><code>Transferable</code></a>.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.utils.PriorityProvider">Fields inherited from interface com.nomagic.utils.<a href="../../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></h3>
<code><a href="../../../utils/PriorityProvider.html#HIGH_PRIORITY">HIGH_PRIORITY</a>, <a href="../../../utils/PriorityProvider.html#LOW_PRIORITY">LOW_PRIORITY</a>, <a href="../../../utils/PriorityProvider.html#MEDIUM_PRIORITY">MEDIUM_PRIORITY</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DiagramTransferableDragAndDropHandler</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#drop(java.awt.Point,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.datatransfer.Transferable)">drop</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentationElement,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> elementOver,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.datatransfer/java/awt/datatransfer/Transferable.html" title="class or interface in java.awt.datatransfer">Transferable</a> transferable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Drops calculated <a href="DropTarget.html" title="class in com.nomagic.magicdraw.ui.dnd"><code>DropTarget</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a human-readable description of what the handler can achieve.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="DropTarget.html" title="class in com.nomagic.magicdraw.ui.dnd">DropTarget</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDropTarget(java.awt.Point,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,java.awt.datatransfer.Transferable)">getDropTarget</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentationElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.datatransfer/java/awt/datatransfer/Transferable.html" title="class or interface in java.awt.datatransfer">Transferable</a> transferable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets <a href="DropTarget.html" title="class in com.nomagic.magicdraw.ui.dnd"><code>DropTarget</code></a> for this handler.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPriority()">getPriority</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns priority of this configurator.</div>
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
<h3>DiagramTransferableDragAndDropHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramTransferableDragAndDropHandler</span>()</div>
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
<section class="detail" id="getDropTarget(java.awt.Point,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,java.awt.datatransfer.Transferable)">
<h3>getDropTarget</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a href="DropTarget.html" title="class in com.nomagic.magicdraw.ui.dnd">DropTarget</a></span> <span class="element-name">getDropTarget</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentationElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.datatransfer/java/awt/datatransfer/Transferable.html" title="class or interface in java.awt.datatransfer">Transferable</a> transferable)</span></div>
<div class="block">Gets <a href="DropTarget.html" title="class in com.nomagic.magicdraw.ui.dnd"><code>DropTarget</code></a> for this handler.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - location on the diagram</dd>
<dd><code>diagramPresentationElement</code> - diagram presentation element on which the drag is being performed</dd>
<dd><code>transferable</code> - transferable drag&amp;drop object</dd>
<dt>Returns:</dt>
<dd>calculated drop target for this handler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="drop(java.awt.Point,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.datatransfer.Transferable)">
<h3>drop</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">drop</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentationElement,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> elementOver,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.datatransfer/java/awt/datatransfer/Transferable.html" title="class or interface in java.awt.datatransfer">Transferable</a> transferable)</span></div>
<div class="block">Drops calculated <a href="DropTarget.html" title="class in com.nomagic.magicdraw.ui.dnd"><code>DropTarget</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - location on the diagram</dd>
<dd><code>diagramPresentationElement</code> - diagram presentation element</dd>
<dd><code>elementOver</code> - symbol on which drag is being performed (if drop target was not specified, passes DiagramPresentationElement)</dd>
<dd><code>transferable</code> - transferable drag&amp;drop object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span>()</div>
<div class="block">Returns a human-readable description of what the handler can achieve.
 Might be used to inform user about the purpose of this handler in various GUI forms, mostly tool tips.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>description as a String or null if no description is provided</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPriority()">
<h3>getPriority</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPriority</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../actions/ConfiguratorWithPriority.html#getPriority()">ConfiguratorWithPriority</a></code></span></div>
<div class="block">Returns priority of this configurator. All configurators are sorted by priority before configuration.
 This is very important if one configurator expects input from other configurators.
 In such case configurator must have lower priority than others.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../actions/ConfiguratorWithPriority.html#getPriority()">getPriority</a></code> in interface <code><a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../../../utils/PriorityProvider.html#getPriority()">getPriority</a></code> in interface <code><a href="../../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
<dt>Returns:</dt>
<dd>priority of this configurator.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../utils/PriorityProvider.html#HIGH_PRIORITY"><code>PriorityProvider.HIGH_PRIORITY</code></a></li>
<li><a href="../../../utils/PriorityProvider.html#MEDIUM_PRIORITY"><code>PriorityProvider.MEDIUM_PRIORITY</code></a></li>
<li><a href="../../../utils/PriorityProvider.html#LOW_PRIORITY"><code>PriorityProvider.LOW_PRIORITY</code></a></li>
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
