# JAVA OPENAPI: ISpecificationComponent (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/ui/dialogs/specifications/ISpecificationComponent.html
- source_path: `com/nomagic/magicdraw/ui/dialogs/specifications/ISpecificationComponent.html`
- source_sha256: `e4d9d28dab1a9222d263917866ca15b1e87f835a7990fd620666dc6fb9693d09`
- captured_utc: `2026-07-14T16:46:01.353819+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dialogs.specifications](package-summary.html)

## Interface ISpecificationComponent

@OpenApiAllpublic interfaceISpecificationComponent
The interface of specification component.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[dispose](#dispose())()`
Method is called when the component is disposed.
`[JComponent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JComponent.html)`
`[getComponent](#getComponent())()`
Returns the GUI component.
`void`
`[propertyChanged](#propertyChanged(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.beans.PropertyChangeEvent))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) event)`
This method gets called when a property is of the element is changed.
`void`
`[updateComponent](#updateComponent())()`
Method is called when component should be updated.

============ METHOD DETAIL ========== 
Method Details
getComponent
[JComponent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JComponent.html) getComponent()
Returns the GUI component.
Returns:
component.
propertyChanged
void propertyChanged([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) event)
This method gets called when a property is of the element is changed.
Parameters:
`element` - element which is represented by component.
`event` - a PropertyChangeEvent object describing the event source and the property that has changed.
updateComponent
void updateComponent()
Method is called when component should be updated.
 Implementation must check if component really needs to be updated.
dispose
void dispose()
Method is called when the component is disposed.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dialogs.specifications</a></div>
<h1 class="title" title="Interface ISpecificationComponent">Interface ISpecificationComponent</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ISpecificationComponent</span></div>
<div class="block">The interface of specification component.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called when the component is disposed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JComponent.html" title="class or interface in javax.swing">JComponent</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getComponent()">getComponent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the GUI component.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#propertyChanged(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.beans.PropertyChangeEvent)">propertyChanged</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> event)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method gets called when a property is of the element is changed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#updateComponent()">updateComponent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called when component should be updated.</div>
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
<section class="detail" id="getComponent()">
<h3>getComponent</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JComponent.html" title="class or interface in javax.swing">JComponent</a></span> <span class="element-name">getComponent</span>()</div>
<div class="block">Returns the GUI component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>component.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertyChanged(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.beans.PropertyChangeEvent)">
<h3>propertyChanged</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">propertyChanged</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> event)</span></div>
<div class="block">This method gets called when a property is of the element is changed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element which is represented by component.</dd>
<dd><code>event</code> - a PropertyChangeEvent object describing the event source and the property that has changed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateComponent()">
<h3>updateComponent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">updateComponent</span>()</div>
<div class="block">Method is called when component should be updated.
 Implementation must check if component really needs to be updated.</div>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">Method is called when the component is disposed.</div>
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
