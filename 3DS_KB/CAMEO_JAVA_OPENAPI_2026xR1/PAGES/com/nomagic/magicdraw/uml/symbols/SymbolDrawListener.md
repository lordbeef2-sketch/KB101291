# JAVA OPENAPI: SymbolDrawListener (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/symbols/SymbolDrawListener.html
- source_path: `com/nomagic/magicdraw/uml/symbols/SymbolDrawListener.html`
- source_sha256: `4bb87d3117802d9a7fe87a18ecdc86fe140b30b1cb492cd0472ef69389fd4a09`
- captured_utc: `2026-07-14T16:46:06.335885+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Interface SymbolDrawListener

@OpenApiAllpublic interfaceSymbolDrawListener

This listener is used in diagrams symbols drawing. It is notified after some symbol drawing in the diagram.
 Listeners are registered in [`SymbolDrawNotification`](SymbolDrawNotification.html).
 The notification is received only if the symbol is drawn using diagram toolbar or smart symbol manipulator.
 If symbol is created/drawn other way the listener is not notified.
 Use [`DiagramListenerAdapter`](DiagramListenerAdapter.html) to listen for all diagram related events.

See Also:
[`SymbolDrawNotification`](SymbolDrawNotification.html)
[`DiagramListenerAdapter`](DiagramListenerAdapter.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[symbolAdded](#symbolAdded(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String))([DiagramPresentationElement](DiagramPresentationElement.html) diagram,
 [PresentationElement](PresentationElement.html) symbol,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) actionID)`
Notification method.

============ METHOD DETAIL ========== 
Method Details
symbolAdded
void symbolAdded([DiagramPresentationElement](DiagramPresentationElement.html) diagram,
 [PresentationElement](PresentationElement.html) symbol,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) actionID)
Notification method. Called when symbol is drawn on diagram.
Parameters:
`diagram` - the diagram symbol added into.
`symbol` - added symbol.
`actionID` - id of action used for symbol adding(id of some toolbar action).

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Interface SymbolDrawListener">Interface SymbolDrawListener</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SymbolDrawListener</span></div>
<div class="block">This listener is used in diagrams symbols drawing. It is notified after some symbol drawing in the diagram.
 Listeners are registered in <a href="SymbolDrawNotification.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>SymbolDrawNotification</code></a>.
 The notification is received only if the symbol is drawn using diagram toolbar or smart symbol manipulator.
 If symbol is created/drawn other way the listener is not notified.
 Use <a href="DiagramListenerAdapter.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>DiagramListenerAdapter</code></a> to listen for all diagram related events.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="SymbolDrawNotification.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>SymbolDrawNotification</code></a></li>
<li><a href="DiagramListenerAdapter.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>DiagramListenerAdapter</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#symbolAdded(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">symbolAdded</a><wbr/>(<a href="DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Notification method.</div>
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
<section class="detail" id="symbolAdded(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">
<h3>symbolAdded</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">symbolAdded</span><wbr/><span class="parameters">(<a href="DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID)</span></div>
<div class="block">Notification method. Called when symbol is drawn on diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the diagram symbol added into.</dd>
<dd><code>symbol</code> - added symbol.</dd>
<dd><code>actionID</code> - id of action used for symbol adding(id of some toolbar action).</dd>
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
