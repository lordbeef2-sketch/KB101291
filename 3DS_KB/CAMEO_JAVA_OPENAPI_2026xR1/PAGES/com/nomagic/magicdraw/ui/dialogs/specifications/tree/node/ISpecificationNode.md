# JAVA OPENAPI: ISpecificationNode (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/ui/dialogs/specifications/tree/node/ISpecificationNode.html
- source_path: `com/nomagic/magicdraw/ui/dialogs/specifications/tree/node/ISpecificationNode.html`
- source_sha256: `4ee87aa8197ca6ff16895ecfb0da159f6b843b18f73f6135cb223b69b6426702`
- captured_utc: `2026-07-14T16:46:02.726837+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dialogs.specifications.tree.node](package-summary.html)

## Interface ISpecificationNode

@OpenApiAllpublic interfaceISpecificationNode
The interface of specification tree node.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ISpecificationComponent](../../ISpecificationComponent.html)`
`[createSpecificationComponent](#createSpecificationComponent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Creates specification component of the node for given element.
`void`
`[dispose](#dispose())()`
Method is called when the node is disposed.
`[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
`[getIcon](#getIcon())()`
Returns the icon of the node.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`
Returns ID of the node.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getText](#getText())()`
Returns displaying text of the node.
`void`
`[propertyChanged](#propertyChanged(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.beans.PropertyChangeEvent))([Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) event)`
This method gets called when a property of the element is changed.
`boolean`
`[updateNode](#updateNode())()`
Method is called when node should be updated.

============ METHOD DETAIL ========== 
Method Details
getID
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getID()
Returns ID of the node.
Returns:
node id.
getIcon
@CheckForNull[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) getIcon()
Returns the icon of the node.
Returns:
node icon.
getText
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getText()
Returns displaying text of the node.
Returns:
displaying text.
createSpecificationComponent
[ISpecificationComponent](../../ISpecificationComponent.html) createSpecificationComponent([Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Creates specification component of the node for given element.
Parameters:
`element` - element to create component for.
Returns:
specification component.
propertyChanged
void propertyChanged([Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) event)
This method gets called when a property of the element is changed.
Parameters:
`element` - element which represented by node.
`event` - a PropertyChangeEvent object describing the event source and the property that has changed.
updateNode
boolean updateNode()
Method is called when node should be updated.
 Implementation must check if node really needs to be updated.
Returns:
`true` if node was updated, otherwise - `false`.
dispose
void dispose()
Method is called when the node is disposed.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dialogs.specifications.tree.node</a></div>
<h1 class="title" title="Interface ISpecificationNode">Interface ISpecificationNode</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ISpecificationNode</span></div>
<div class="block">The interface of specification tree node.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../ISpecificationComponent.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications">ISpecificationComponent</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createSpecificationComponent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">createSpecificationComponent</a><wbr/>(<a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Creates specification component of the node for given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called when the node is disposed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIcon()">getIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the icon of the node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns ID of the node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns displaying text of the node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#propertyChanged(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.beans.PropertyChangeEvent)">propertyChanged</a><wbr/>(<a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> event)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method gets called when a property of the element is changed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#updateNode()">updateNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called when node should be updated.</div>
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
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block">Returns ID of the node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>node id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon()">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getIcon</span>()</div>
<div class="block">Returns the icon of the node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>node icon.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getText()">
<h3>getText</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getText</span>()</div>
<div class="block">Returns displaying text of the node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>displaying text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSpecificationComponent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>createSpecificationComponent</h3>
<div class="member-signature"><span class="return-type"><a href="../../ISpecificationComponent.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications">ISpecificationComponent</a></span> <span class="element-name">createSpecificationComponent</span><wbr/><span class="parameters">(<a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Creates specification component of the node for given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to create component for.</dd>
<dt>Returns:</dt>
<dd>specification component.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertyChanged(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.beans.PropertyChangeEvent)">
<h3>propertyChanged</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">propertyChanged</span><wbr/><span class="parameters">(<a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> event)</span></div>
<div class="block">This method gets called when a property of the element is changed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element which represented by node.</dd>
<dd><code>event</code> - a PropertyChangeEvent object describing the event source and the property that has changed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNode()">
<h3>updateNode</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">updateNode</span>()</div>
<div class="block">Method is called when node should be updated.
 Implementation must check if node really needs to be updated.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if node was updated, otherwise - <code>false</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">Method is called when the node is disposed.</div>
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
