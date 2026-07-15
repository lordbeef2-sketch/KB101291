# JAVA OPENAPI: DiagramWindow (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/ui/DiagramWindow.html
- source_path: `com/nomagic/magicdraw/ui/DiagramWindow.html`
- source_sha256: `76805e093bef53b5852994f4e9aa6834358a55ae4bb4511f3022c903ea5079cf`
- captured_utc: `2026-07-14T16:52:00.607730+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Class DiagramWindow

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>
com.nomagic.magicdraw.ui.DiagramWindow

All Implemented Interfaces:
`com.jidesoft.document.DocumentComponentListener`, `com.nomagic.magicdraw.ui.Activatable`, `[DiagramPresentationElementGetter](DiagramPresentationElementGetter.html)`, `com.nomagic.ui.CursorOwner`, `[HiDPIScalableComponent](../../ui/HiDPIScalableComponent.html)`, `[FocusListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/FocusListener.html)`, `[WindowListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApipublic classDiagramWindow
extends com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>
implements [DiagramPresentationElementGetter](DiagramPresentationElementGetter.html)

This class is base class for diagram specific windows.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)`
`[getAbstractDiagramPresentationElement](#getAbstractDiagramPresentationElement())()`
Returns the diagram of this window.
`[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)`
`[getDiagramPresentationElement](#getDiagramPresentationElement())()`
Deprecated.
use [`getAbstractDiagramPresentationElement()`](#getAbstractDiagramPresentationElement())
Methods inherited from class com.nomagic.magicdraw.ui.editorwindows.EditorWindow
`createToolbarsForAllWindows, documentComponentActivated, documentComponentClosed, documentComponentClosing, documentComponentDeactivated, documentComponentDocked, documentComponentFloated, documentComponentMoved, documentComponentMoving, documentComponentOpened, executeWithoutEventFiring, firePropertyChange, focusGained, focusLost, getDocument, getID, getLocation, getLocationOnScreen, isFloating, isHiDPIScaled, isWindowClosed, renameDocumentComponent, requestFocus, setHiDPIScaled, setLocation, setMoveListener, setWindowClosed, windowClosing`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getDiagramPresentationElement
@CheckForNull
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) getDiagramPresentationElement()
Deprecated.
use [`getAbstractDiagramPresentationElement()`](#getAbstractDiagramPresentationElement())
Returns the diagram view of this window.
 This method returns the diagram view from DiagramWindowPanel.
Specified by:
`[getDiagramPresentationElement](DiagramPresentationElementGetter.html#getDiagramPresentationElement())` in interface `[DiagramPresentationElementGetter](DiagramPresentationElementGetter.html)`
Returns:
current diagram view.
getAbstractDiagramPresentationElement
@OpenApi
@CheckForNullpublic [AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) getAbstractDiagramPresentationElement()
Returns the diagram of this window.
 This method returns the diagram from DiagramWindowPanel.
Returns:
diagram

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Class DiagramWindow">Class DiagramWindow</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.ui.DiagramWindow</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.jidesoft.document.DocumentComponentListener</code>, <code>com.nomagic.magicdraw.ui.Activatable</code>, <code><a href="DiagramPresentationElementGetter.html" title="interface in com.nomagic.magicdraw.ui">DiagramPresentationElementGetter</a></code>, <code>com.nomagic.ui.CursorOwner</code>, <code><a href="../../ui/HiDPIScalableComponent.html" title="interface in com.nomagic.ui">HiDPIScalableComponent</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/FocusListener.html" title="class or interface in java.awt.event">FocusListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html" title="class or interface in java.awt.event">WindowListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramWindow</span>
<span class="extends-implements">extends com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;
implements <a href="DiagramPresentationElementGetter.html" title="interface in com.nomagic.magicdraw.ui">DiagramPresentationElementGetter</a></span></div>
<div class="block">This class is base class for diagram specific windows.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the diagram of this window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDiagramPresentationElement()">getDiagramPresentationElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getAbstractDiagramPresentationElement()"><code>getAbstractDiagramPresentationElement()</code></a></div>
</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.editorwindows.EditorWindow">Methods inherited from class com.nomagic.magicdraw.ui.editorwindows.EditorWindow</h3>
<code>createToolbarsForAllWindows, documentComponentActivated, documentComponentClosed, documentComponentClosing, documentComponentDeactivated, documentComponentDocked, documentComponentFloated, documentComponentMoved, documentComponentMoving, documentComponentOpened, executeWithoutEventFiring, firePropertyChange, focusGained, focusLost, getDocument, getID, getLocation, getLocationOnScreen, isFloating, isHiDPIScaled, isWindowClosed, renameDocumentComponent, requestFocus, setHiDPIScaled, setLocation, setMoveListener, setWindowClosed, windowClosing</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="getDiagramPresentationElement()">
<h3>getDiagramPresentationElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></span> <span class="element-name">getDiagramPresentationElement</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getAbstractDiagramPresentationElement()"><code>getAbstractDiagramPresentationElement()</code></a></div>
</div>
<div class="block">Returns the diagram view of this window.
 This method returns the diagram view from DiagramWindowPanel.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="DiagramPresentationElementGetter.html#getDiagramPresentationElement()">getDiagramPresentationElement</a></code> in interface <code><a href="DiagramPresentationElementGetter.html" title="interface in com.nomagic.magicdraw.ui">DiagramPresentationElementGetter</a></code></dd>
<dt>Returns:</dt>
<dd>current diagram view.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractDiagramPresentationElement()">
<h3>getAbstractDiagramPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></span> <span class="element-name">getAbstractDiagramPresentationElement</span>()</div>
<div class="block">Returns the diagram of this window.
 This method returns the diagram from DiagramWindowPanel.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram</dd>
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
