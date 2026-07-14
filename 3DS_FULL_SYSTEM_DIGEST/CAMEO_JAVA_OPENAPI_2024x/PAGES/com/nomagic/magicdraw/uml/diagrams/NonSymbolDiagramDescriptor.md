# JAVA OPENAPI: NonSymbolDiagramDescriptor (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml/diagrams/NonSymbolDiagramDescriptor.html
- source_path: `com/nomagic/magicdraw/uml/diagrams/NonSymbolDiagramDescriptor.html`
- source_sha256: `7b5c38835e5d356a115ff1cff266f46fd44f68d200b6eee1ee7ac9c3b6b3bc35`
- captured_utc: `2026-07-14T16:52:10.580859+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.diagrams](package-summary.html)

## Class NonSymbolDiagramDescriptor<C extends [Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.DiagramDescriptor](../DiagramDescriptor.html)
com.nomagic.magicdraw.uml.diagrams.NonSymbolDiagramDescriptor<C>

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic abstract classNonSymbolDiagramDescriptor<C extends [Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)>
extends [DiagramDescriptor](../DiagramDescriptor.html)

Descriptor of non symbol diagram - diagram that represents custom [`Component`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html).

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[NonSymbolDiagramDescriptor](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`abstract [NonSymbolDiagramContent](NonSymbolDiagramContent.html)<[C](NonSymbolDiagramDescriptor.html)>`
`[createDiagramContent](#createDiagramContent(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([DiagramPresentationElement](../symbols/DiagramPresentationElement.html) diagramPresentationElement)`
Create diagram content for given [`DiagramPresentationElement`](../symbols/DiagramPresentationElement.html).
`abstract [AMConfigurator](../../../actions/AMConfigurator.html)`
`[getDiagramCommandBarConfigurator](#getDiagramCommandBarConfigurator())()`
Get diagram command toolbar configurator.
`final [DiagramContextAMConfigurator](../../actions/DiagramContextAMConfigurator.html)`
`[getDiagramContextConfigurator](#getDiagramContextConfigurator())()`
Diagram has no popup menu.
`final [AMConfigurator](../../../actions/AMConfigurator.html)`
`[getDiagramToolbarConfigurator](#getDiagramToolbarConfigurator())()`
Diagram has no toolbar.
`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSuperType](#getSuperType())()`
UML Class diagram is used as super type.
`final boolean`
`[isUsedForSymbols](#isUsedForSymbols())()`
This diagrams is not used for symbols.
Methods inherited from class com.nomagic.magicdraw.uml.[DiagramDescriptor](../DiagramDescriptor.html)
`[getCategory](../DiagramDescriptor.html#getCategory()), [getDiagramActions](../DiagramDescriptor.html#getDiagramActions()), [getDiagramShortcutsConfigurator](../DiagramDescriptor.html#getDiagramShortcutsConfigurator()), [getDiagramTypeId](../DiagramDescriptor.html#getDiagramTypeId()), [getPluralDiagramTypeHumanName](../DiagramDescriptor.html#getPluralDiagramTypeHumanName()), [getSingularDiagramTypeHumanName](../DiagramDescriptor.html#getSingularDiagramTypeHumanName()), [getSmallIconURL](../DiagramDescriptor.html#getSmallIconURL()), [getSVGIcon](../DiagramDescriptor.html#getSVGIcon()), [isCreatable](../DiagramDescriptor.html#isCreatable()), [setCategory](../DiagramDescriptor.html#setCategory(java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
NonSymbolDiagramDescriptor
public NonSymbolDiagramDescriptor()
 ============ METHOD DETAIL ========== 
Method Details
getSuperType
public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSuperType()
UML Class diagram is used as super type.
Specified by:
`[getSuperType](../DiagramDescriptor.html#getSuperType())` in class `[DiagramDescriptor](../DiagramDescriptor.html)`
Returns:
[`DiagramTypes.UML_CLASS_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_CLASS_DIAGRAM)
isUsedForSymbols
public final boolean isUsedForSymbols()
This diagrams is not used for symbols.
Overrides:
`[isUsedForSymbols](../DiagramDescriptor.html#isUsedForSymbols())` in class `[DiagramDescriptor](../DiagramDescriptor.html)`
Returns:
`false`.
getDiagramToolbarConfigurator
@CheckForNullpublic final [AMConfigurator](../../../actions/AMConfigurator.html) getDiagramToolbarConfigurator()
Diagram has no toolbar.
Specified by:
`[getDiagramToolbarConfigurator](../DiagramDescriptor.html#getDiagramToolbarConfigurator())` in class `[DiagramDescriptor](../DiagramDescriptor.html)`
Returns:
`null`.
getDiagramContextConfigurator
@CheckForNullpublic final [DiagramContextAMConfigurator](../../actions/DiagramContextAMConfigurator.html) getDiagramContextConfigurator()
Diagram has no popup menu.
Specified by:
`[getDiagramContextConfigurator](../DiagramDescriptor.html#getDiagramContextConfigurator())` in class `[DiagramDescriptor](../DiagramDescriptor.html)`
Returns:
`null`.
getDiagramCommandBarConfigurator
@CheckForNullpublic abstract [AMConfigurator](../../../actions/AMConfigurator.html) getDiagramCommandBarConfigurator()
Get diagram command toolbar configurator. Toolbar is presented above the custom component.
Returns:
configurator.
createDiagramContent
public abstract [NonSymbolDiagramContent](NonSymbolDiagramContent.html)<[C](NonSymbolDiagramDescriptor.html)> createDiagramContent([DiagramPresentationElement](../symbols/DiagramPresentationElement.html) diagramPresentationElement)
Create diagram content for given [`DiagramPresentationElement`](../symbols/DiagramPresentationElement.html).
Parameters:
`diagramPresentationElement` - diagram presentation element to create content.
Returns:
diagram content.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.diagrams</a></div>
<h1 class="title" title="Class NonSymbolDiagramDescriptor">Class NonSymbolDiagramDescriptor&lt;C extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a>&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">com.nomagic.magicdraw.uml.DiagramDescriptor</a>
<div class="inheritance">com.nomagic.magicdraw.uml.diagrams.NonSymbolDiagramDescriptor&lt;C&gt;</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">NonSymbolDiagramDescriptor&lt;C extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a>&gt;</span>
<span class="extends-implements">extends <a href="../DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a></span></div>
<div class="block">Descriptor of non symbol diagram - diagram that represents custom <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt"><code>Component</code></a>.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">NonSymbolDiagramDescriptor</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="NonSymbolDiagramContent.html" title="interface in com.nomagic.magicdraw.uml.diagrams">NonSymbolDiagramContent</a>&lt;<a href="NonSymbolDiagramDescriptor.html" title="type parameter in NonSymbolDiagramDescriptor">C</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createDiagramContent(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">createDiagramContent</a><wbr/>(<a href="../symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Create diagram content for given <a href="../symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>DiagramPresentationElement</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="../../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramCommandBarConfigurator()">getDiagramCommandBarConfigurator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get diagram command toolbar configurator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../../actions/DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramContextConfigurator()">getDiagramContextConfigurator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Diagram has no popup menu.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramToolbarConfigurator()">getDiagramToolbarConfigurator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Diagram has no toolbar.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSuperType()">getSuperType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">UML Class diagram is used as super type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUsedForSymbols()">isUsedForSymbols</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This diagrams is not used for symbols.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.DiagramDescriptor">Methods inherited from class com.nomagic.magicdraw.uml.<a href="../DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a></h3>
<code><a href="../DiagramDescriptor.html#getCategory()">getCategory</a>, <a href="../DiagramDescriptor.html#getDiagramActions()">getDiagramActions</a>, <a href="../DiagramDescriptor.html#getDiagramShortcutsConfigurator()">getDiagramShortcutsConfigurator</a>, <a href="../DiagramDescriptor.html#getDiagramTypeId()">getDiagramTypeId</a>, <a href="../DiagramDescriptor.html#getPluralDiagramTypeHumanName()">getPluralDiagramTypeHumanName</a>, <a href="../DiagramDescriptor.html#getSingularDiagramTypeHumanName()">getSingularDiagramTypeHumanName</a>, <a href="../DiagramDescriptor.html#getSmallIconURL()">getSmallIconURL</a>, <a href="../DiagramDescriptor.html#getSVGIcon()">getSVGIcon</a>, <a href="../DiagramDescriptor.html#isCreatable()">isCreatable</a>, <a href="../DiagramDescriptor.html#setCategory(java.lang.String)">setCategory</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>NonSymbolDiagramDescriptor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">NonSymbolDiagramDescriptor</span>()</div>
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
<section class="detail" id="getSuperType()">
<h3>getSuperType</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSuperType</span>()</div>
<div class="block">UML Class diagram is used as super type.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../DiagramDescriptor.html#getSuperType()">getSuperType</a></code> in class <code><a href="../DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a></code></dd>
<dt>Returns:</dt>
<dd><a href="../../../uml2/diagram/DiagramTypes.html#UML_CLASS_DIAGRAM"><code>DiagramTypes.UML_CLASS_DIAGRAM</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUsedForSymbols()">
<h3>isUsedForSymbols</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">isUsedForSymbols</span>()</div>
<div class="block">This diagrams is not used for symbols.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../DiagramDescriptor.html#isUsedForSymbols()">isUsedForSymbols</a></code> in class <code><a href="../DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a></code></dd>
<dt>Returns:</dt>
<dd><code>false</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramToolbarConfigurator()">
<h3>getDiagramToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="../../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></span> <span class="element-name">getDiagramToolbarConfigurator</span>()</div>
<div class="block">Diagram has no toolbar.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../DiagramDescriptor.html#getDiagramToolbarConfigurator()">getDiagramToolbarConfigurator</a></code> in class <code><a href="../DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a></code></dd>
<dt>Returns:</dt>
<dd><code>null</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContextConfigurator()">
<h3>getDiagramContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="../../actions/DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a></span> <span class="element-name">getDiagramContextConfigurator</span>()</div>
<div class="block">Diagram has no popup menu.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../DiagramDescriptor.html#getDiagramContextConfigurator()">getDiagramContextConfigurator</a></code> in class <code><a href="../DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a></code></dd>
<dt>Returns:</dt>
<dd><code>null</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramCommandBarConfigurator()">
<h3>getDiagramCommandBarConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public abstract</span> <span class="return-type"><a href="../../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></span> <span class="element-name">getDiagramCommandBarConfigurator</span>()</div>
<div class="block">Get diagram command toolbar configurator. Toolbar is presented above the custom component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>configurator.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDiagramContent(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>createDiagramContent</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a href="NonSymbolDiagramContent.html" title="interface in com.nomagic.magicdraw.uml.diagrams">NonSymbolDiagramContent</a>&lt;<a href="NonSymbolDiagramDescriptor.html" title="type parameter in NonSymbolDiagramDescriptor">C</a>&gt;</span> <span class="element-name">createDiagramContent</span><wbr/><span class="parameters">(<a href="../symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagramPresentationElement)</span></div>
<div class="block">Create diagram content for given <a href="../symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>DiagramPresentationElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramPresentationElement</code> - diagram presentation element to create content.</dd>
<dt>Returns:</dt>
<dd>diagram content.</dd>
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
