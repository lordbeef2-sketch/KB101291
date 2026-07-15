# JAVA OPENAPI: DiagramSurface (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml/symbols/DiagramSurface.html
- source_path: `com/nomagic/magicdraw/uml/symbols/DiagramSurface.html`
- source_sha256: `e1e8837355e7110ec9553f5db966ef27b350d682f1ae485877bb0753609c10e6`
- captured_utc: `2026-07-14T16:52:11.121867+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Interface DiagramSurface

@OpenApipublic interfaceDiagramSurface
Interface for some component that is used for diagram displaying.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[addPainter](#addPainter(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter))(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter painter)`
Registers given painter.
`void`
`[addPainter](#addPainter(com.nomagic.magicdraw.ui.DiagramSurfacePainter))([DiagramSurfacePainter](../../ui/DiagramSurfacePainter.html) painter)`
Registers given painter.
`[Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html)`
`[getCursor](#getCursor())()`
Returns diagram cursor.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[DiagramSurfacePainter](../../ui/DiagramSurfacePainter.html)>`
`[getPainters](#getPainters())()`
Returns all registered painters.
`void`
`[removePainter](#removePainter(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter))(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter painter)`
Unregisters given painter.
`void`
`[removePainter](#removePainter(com.nomagic.magicdraw.ui.DiagramSurfacePainter))([DiagramSurfacePainter](../../ui/DiagramSurfacePainter.html) painter)`
Unregisters given painter.
`void`
`[repaint](#repaint())()`
Repaints the diagram surface.
`void`
`[repaint](#repaint(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)`
Repaints the given rectangle of the diagram surface.
`void`
`[scrollRectToVisible](#scrollRectToVisible(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`
Scrolls diagram surface in order to make given part of diagram visible.
`void`
`[scrollToVisible](#scrollToVisible(int,int))(int x,
 int y)`
Scrolls diagram surface in order to make given point of diagram visible.
`void`
`[setCursor](#setCursor(java.awt.Cursor))([Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) cursor)`
Sets diagram cursor.

============ METHOD DETAIL ========== 
Method Details
repaint
@OpenApivoid repaint()
Repaints the diagram surface.
repaint
@OpenApivoid repaint([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)
Repaints the given rectangle of the diagram surface.
Parameters:
`rect` - the rectangle to repaint.
scrollRectToVisible
@OpenApivoid scrollRectToVisible([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
Scrolls diagram surface in order to make given part of diagram visible.
Parameters:
`r` - make this part of diagram visible.
scrollToVisible
@OpenApivoid scrollToVisible(int x,
 int y)
Scrolls diagram surface in order to make given point of diagram visible.
Parameters:
`x` - the x coordinate of the visible point.
`y` - the y coordinate of the visible point.
setCursor
@OpenApivoid setCursor(@CheckForNull
 [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) cursor)
Sets diagram cursor.
Parameters:
`cursor` - a new cursor for diagram.
See Also:
[`Component.setCursor(java.awt.Cursor)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setCursor(java.awt.Cursor))
getCursor
@OpenApi[Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) getCursor()
Returns diagram cursor.
Returns:
current diagram cursor.
See Also:
[`Component.getCursor()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getCursor())
addPainter
@OpenApivoid addPainter([DiagramSurfacePainter](../../ui/DiagramSurfacePainter.html) painter)
Registers given painter.
Parameters:
`painter` - the given painter
addPainter
@OpenApivoid addPainter(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter painter)
Registers given painter.
Parameters:
`painter` - the given painter
removePainter
@OpenApivoid removePainter([DiagramSurfacePainter](../../ui/DiagramSurfacePainter.html) painter)
Unregisters given painter.
Parameters:
`painter` - the given painter
removePainter
@OpenApivoid removePainter(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter painter)
Unregisters given painter.
Parameters:
`painter` - the given painter
getPainters
@OpenApi[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[DiagramSurfacePainter](../../ui/DiagramSurfacePainter.html)> getPainters()
Returns all registered painters.
Returns:
list of registered painters

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Interface DiagramSurface">Interface DiagramSurface</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DiagramSurface</span></div>
<div class="block">Interface for some component that is used for diagram displaying.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addPainter(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter)">addPainter</a><wbr/>(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter painter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Registers given painter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addPainter(com.nomagic.magicdraw.ui.DiagramSurfacePainter)">addPainter</a><wbr/>(<a href="../../ui/DiagramSurfacePainter.html" title="class in com.nomagic.magicdraw.ui">DiagramSurfacePainter</a> painter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Registers given painter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCursor()">getCursor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns diagram cursor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../ui/DiagramSurfacePainter.html" title="class in com.nomagic.magicdraw.ui">DiagramSurfacePainter</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPainters()">getPainters</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns all registered painters.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removePainter(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter)">removePainter</a><wbr/>(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter painter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Unregisters given painter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removePainter(com.nomagic.magicdraw.ui.DiagramSurfacePainter)">removePainter</a><wbr/>(<a href="../../ui/DiagramSurfacePainter.html" title="class in com.nomagic.magicdraw.ui">DiagramSurfacePainter</a> painter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Unregisters given painter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#repaint()">repaint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Repaints the diagram surface.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#repaint(java.awt.Rectangle)">repaint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Repaints the given rectangle of the diagram surface.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#scrollRectToVisible(java.awt.Rectangle)">scrollRectToVisible</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Scrolls diagram surface in order to make given part of diagram visible.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#scrollToVisible(int,int)">scrollToVisible</a><wbr/>(int x,
 int y)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Scrolls diagram surface in order to make given point of diagram visible.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setCursor(java.awt.Cursor)">setCursor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a> cursor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets diagram cursor.</div>
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
<section class="detail" id="repaint()">
<h3>repaint</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">repaint</span>()</div>
<div class="block">Repaints the diagram surface.</div>
</section>
</li>
<li>
<section class="detail" id="repaint(java.awt.Rectangle)">
<h3>repaint</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">repaint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</span></div>
<div class="block">Repaints the given rectangle of the diagram surface.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rect</code> - the rectangle to repaint.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scrollRectToVisible(java.awt.Rectangle)">
<h3>scrollRectToVisible</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">scrollRectToVisible</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span></div>
<div class="block">Scrolls diagram surface in order to make given part of diagram visible.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - make this part of diagram visible.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scrollToVisible(int,int)">
<h3>scrollToVisible</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">scrollToVisible</span><wbr/><span class="parameters">(int x,
 int y)</span></div>
<div class="block">Scrolls diagram surface in order to make given point of diagram visible.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - the x coordinate of the visible point.</dd>
<dd><code>y</code> - the y coordinate of the visible point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCursor(java.awt.Cursor)">
<h3>setCursor</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setCursor</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a> cursor)</span></div>
<div class="block">Sets diagram cursor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cursor</code> - a new cursor for diagram.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setCursor(java.awt.Cursor)" title="class or interface in java.awt"><code>Component.setCursor(java.awt.Cursor)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCursor()">
<h3>getCursor</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></span> <span class="element-name">getCursor</span>()</div>
<div class="block">Returns diagram cursor.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>current diagram cursor.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getCursor()" title="class or interface in java.awt"><code>Component.getCursor()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPainter(com.nomagic.magicdraw.ui.DiagramSurfacePainter)">
<h3>addPainter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">addPainter</span><wbr/><span class="parameters">(<a href="../../ui/DiagramSurfacePainter.html" title="class in com.nomagic.magicdraw.ui">DiagramSurfacePainter</a> painter)</span></div>
<div class="block">Registers given painter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>painter</code> - the given painter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPainter(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter)">
<h3>addPainter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">addPainter</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter painter)</span></div>
<div class="block">Registers given painter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>painter</code> - the given painter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePainter(com.nomagic.magicdraw.ui.DiagramSurfacePainter)">
<h3>removePainter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">removePainter</span><wbr/><span class="parameters">(<a href="../../ui/DiagramSurfacePainter.html" title="class in com.nomagic.magicdraw.ui">DiagramSurfacePainter</a> painter)</span></div>
<div class="block">Unregisters given painter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>painter</code> - the given painter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePainter(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter)">
<h3>removePainter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">removePainter</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.AbstractDiagramSurfacePainter painter)</span></div>
<div class="block">Unregisters given painter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>painter</code> - the given painter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPainters()">
<h3>getPainters</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../ui/DiagramSurfacePainter.html" title="class in com.nomagic.magicdraw.ui">DiagramSurfacePainter</a>&gt;</span> <span class="element-name">getPainters</span>()</div>
<div class="block">Returns all registered painters.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of registered painters</dd>
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
