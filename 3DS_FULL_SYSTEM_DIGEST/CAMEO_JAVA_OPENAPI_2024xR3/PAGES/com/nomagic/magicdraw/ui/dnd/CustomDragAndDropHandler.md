# JAVA OPENAPI: CustomDragAndDropHandler (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/dnd/CustomDragAndDropHandler.html
- source_path: `com/nomagic/magicdraw/ui/dnd/CustomDragAndDropHandler.html`
- source_sha256: `a5b65717c4e2eedd9dcdeddb452236bb376ecd957ae5e5deabb4e283aaa29171`
- captured_utc: `2026-07-14T16:55:52.768429+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dnd](package-summary.html)

## Class CustomDragAndDropHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandler

@OpenApiAllpublic abstract classCustomDragAndDropHandler
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Drop Diagram Handler interface used to implement drag and drop actions for browser drops
 
 Using this interface you can implement the main methods that are responsible for drag and drop actions.
 And later register your custom drag and drop action using [`CustomDropDiagramHandlerFactory`](CustomDropDiagramHandlerFactory.html)

See Also:
[`CustomDropDiagramHandlerFactory`](CustomDropDiagramHandlerFactory.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CustomDragAndDropHandler](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`abstract boolean`
`[drop](#drop(java.awt.Point,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 [PresentationElement](../../uml/symbols/PresentationElement.html) elementOver,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> draggedElements,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagram)`
Executes the drop action
`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription())()`
Returns the description of the drop diagram handler
`abstract boolean`
`[willAcceptDrop](#willAcceptDrop(java.awt.Point,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 [PresentationElement](../../uml/symbols/PresentationElement.html) elementOver,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> draggedElements,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagram)`
Checks if drop can be executed
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CustomDragAndDropHandler
public CustomDragAndDropHandler()
 ============ METHOD DETAIL ========== 
Method Details
getDescription
public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescription()
Returns the description of the drop diagram handler
Returns:
description of drop diagram handler
willAcceptDrop
public abstract boolean willAcceptDrop([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 @CheckForNull
 [PresentationElement](../../uml/symbols/PresentationElement.html) elementOver,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> draggedElements,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagram)
Checks if drop can be executed
Parameters:
`location` - drop location
`elementOver` - presentation element on which data is dragged
`draggedElements` - dragged elements
`diagram` - diagram presentation element on which Drag and Drop action is executed
Returns:
true if element can accept dragged data, else false
drop
public abstract boolean drop([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location,
 @CheckForNull
 [PresentationElement](../../uml/symbols/PresentationElement.html) elementOver,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> draggedElements,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagram)
Executes the drop action
Parameters:
`location` - drop location
`elementOver` - presentation element on which drop is executed
`draggedElements` - dragged elements over drop target
`diagram` - diagram presentation element on which Drag and Drop action is executed
Returns:
returns true if drop was successful, else false (it is important to return true after successful action, as else this and next Drag and Drop action will be executed)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dnd</a></div>
<h1 class="title" title="Class CustomDragAndDropHandler">Class CustomDragAndDropHandler</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dnd.CustomDragAndDropHandler</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">CustomDragAndDropHandler</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Drop Diagram Handler interface used to implement drag and drop actions for browser drops
 <p></p>
 Using this interface you can implement the main methods that are responsible for drag and drop actions.
 And later register your custom drag and drop action using <a href="CustomDropDiagramHandlerFactory.html" title="class in com.nomagic.magicdraw.ui.dnd"><code>CustomDropDiagramHandlerFactory</code></a></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="CustomDropDiagramHandlerFactory.html" title="class in com.nomagic.magicdraw.ui.dnd"><code>CustomDropDiagramHandlerFactory</code></a></li>
</ul>
</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CustomDragAndDropHandler</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#drop(java.awt.Point,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">drop</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> elementOver,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; draggedElements,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Executes the drop action</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the description of the drop diagram handler</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#willAcceptDrop(java.awt.Point,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">willAcceptDrop</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> elementOver,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; draggedElements,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if drop can be executed</div>
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
<h3>CustomDragAndDropHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CustomDragAndDropHandler</span>()</div>
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
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span>()</div>
<div class="block">Returns the description of the drop diagram handler</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>description of drop diagram handler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="willAcceptDrop(java.awt.Point,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>willAcceptDrop</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">boolean</span> <span class="element-name">willAcceptDrop</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 @CheckForNull
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> elementOver,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; draggedElements,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</span></div>
<div class="block">Checks if drop can be executed</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - drop location</dd>
<dd><code>elementOver</code> - presentation element on which data is dragged</dd>
<dd><code>draggedElements</code> - dragged elements</dd>
<dd><code>diagram</code> - diagram presentation element on which Drag and Drop action is executed</dd>
<dt>Returns:</dt>
<dd>true if element can accept dragged data, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="drop(java.awt.Point,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>drop</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">boolean</span> <span class="element-name">drop</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location,
 @CheckForNull
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> elementOver,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; draggedElements,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</span></div>
<div class="block">Executes the drop action</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - drop location</dd>
<dd><code>elementOver</code> - presentation element on which drop is executed</dd>
<dd><code>draggedElements</code> - dragged elements over drop target</dd>
<dd><code>diagram</code> - diagram presentation element on which Drag and Drop action is executed</dd>
<dt>Returns:</dt>
<dd>returns true if drop was successful, else false (it is important to return true after successful action, as else this and next Drag and Drop action will be executed)</dd>
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
