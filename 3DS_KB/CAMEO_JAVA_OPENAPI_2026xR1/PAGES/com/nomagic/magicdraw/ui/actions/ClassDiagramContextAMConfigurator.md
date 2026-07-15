# JAVA OPENAPI: ClassDiagramContextAMConfigurator (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/ui/actions/ClassDiagramContextAMConfigurator.html
- source_path: `com/nomagic/magicdraw/ui/actions/ClassDiagramContextAMConfigurator.html`
- source_sha256: `5b54a1dd430b88ab6f580ac44bbf79df44515c3d37a7bb24b1ae6b5010291504`
- captured_utc: `2026-07-14T16:45:59.901800+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.actions](package-summary.html)

## Class ClassDiagramContextAMConfigurator

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.ui.actions.BaseDiagramContextAMConfigurator](BaseDiagramContextAMConfigurator.html)
com.nomagic.magicdraw.ui.actions.ClassDiagramContextAMConfigurator

All Implemented Interfaces:
`[ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)`, `[DiagramContextAMConfigurator](../../actions/DiagramContextAMConfigurator.html)`, `[PriorityProvider](../../../utils/PriorityProvider.html)`

@OpenApiAllpublic classClassDiagramContextAMConfigurator
extends [BaseDiagramContextAMConfigurator](BaseDiagramContextAMConfigurator.html)

Configure class diagram context menu.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.ui.actions.[BaseDiagramContextAMConfigurator](BaseDiagramContextAMConfigurator.html)
`[LayoutID](BaseDiagramContextAMConfigurator.html#LayoutID)`
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../../../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../../../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../../../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../../../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ClassDiagramContextAMConfigurator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[configureSingleSelectionActions](#configureSingleSelectionActions(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement%5B%5D,com.nomagic.magicdraw.uml.symbols.PresentationElement))([ActionsManager](../../../actions/ActionsManager.html) actionsManager,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagram,
 [PresentationElement](../../uml/symbols/PresentationElement.html)[] selected,
 [PresentationElement](../../uml/symbols/PresentationElement.html) requestSource)`

`protected [ActionsCategory](../../../actions/ActionsCategory.html)`
`[createLayoutActionsCategory](#createLayoutActionsCategory())()`
Methods inherited from class com.nomagic.magicdraw.ui.actions.[BaseDiagramContextAMConfigurator](BaseDiagramContextAMConfigurator.html)
`[configure](BaseDiagramContextAMConfigurator.html#configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement%5B%5D,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [configureDiagramActions](BaseDiagramContextAMConfigurator.html#configureDiagramActions(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)), [configureMultipleSelectionActions](BaseDiagramContextAMConfigurator.html#configureMultipleSelectionActions(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement%5B%5D)), [getPriority](BaseDiagramContextAMConfigurator.html#getPriority())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ClassDiagramContextAMConfigurator
public ClassDiagramContextAMConfigurator()
 ============ METHOD DETAIL ========== 
Method Details
createLayoutActionsCategory
protected [ActionsCategory](../../../actions/ActionsCategory.html) createLayoutActionsCategory()
Overrides:
`[createLayoutActionsCategory](BaseDiagramContextAMConfigurator.html#createLayoutActionsCategory())` in class `[BaseDiagramContextAMConfigurator](BaseDiagramContextAMConfigurator.html)`
configureSingleSelectionActions
protected void configureSingleSelectionActions([ActionsManager](../../../actions/ActionsManager.html) actionsManager,
 [DiagramPresentationElement](../../uml/symbols/DiagramPresentationElement.html) diagram,
 [PresentationElement](../../uml/symbols/PresentationElement.html)[] selected,
 [PresentationElement](../../uml/symbols/PresentationElement.html) requestSource)
Overrides:
`[configureSingleSelectionActions](BaseDiagramContextAMConfigurator.html#configureSingleSelectionActions(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement%5B%5D,com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[BaseDiagramContextAMConfigurator](BaseDiagramContextAMConfigurator.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.actions</a></div>
<h1 class="title" title="Class ClassDiagramContextAMConfigurator">Class ClassDiagramContextAMConfigurator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="BaseDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">com.nomagic.magicdraw.ui.actions.BaseDiagramContextAMConfigurator</a>
<div class="inheritance">com.nomagic.magicdraw.ui.actions.ClassDiagramContextAMConfigurator</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code>, <code><a href="../../actions/DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a></code>, <code><a href="../../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ClassDiagramContextAMConfigurator</span>
<span class="extends-implements">extends <a href="BaseDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramContextAMConfigurator</a></span></div>
<div class="block">Configure class diagram context menu.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.ui.actions.BaseDiagramContextAMConfigurator">Fields inherited from class com.nomagic.magicdraw.ui.actions.<a href="BaseDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramContextAMConfigurator</a></h3>
<code><a href="BaseDiagramContextAMConfigurator.html#LayoutID">LayoutID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ClassDiagramContextAMConfigurator</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configureSingleSelectionActions(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement%5B%5D,com.nomagic.magicdraw.uml.symbols.PresentationElement)">configureSingleSelectionActions</a><wbr/>(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> actionsManager,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>[] selected,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> requestSource)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLayoutActionsCategory()">createLayoutActionsCategory</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.actions.BaseDiagramContextAMConfigurator">Methods inherited from class com.nomagic.magicdraw.ui.actions.<a href="BaseDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramContextAMConfigurator</a></h3>
<code><a href="BaseDiagramContextAMConfigurator.html#configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement%5B%5D,com.nomagic.magicdraw.uml.symbols.PresentationElement)">configure</a>, <a href="BaseDiagramContextAMConfigurator.html#configureDiagramActions(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">configureDiagramActions</a>, <a href="BaseDiagramContextAMConfigurator.html#configureMultipleSelectionActions(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement%5B%5D)">configureMultipleSelectionActions</a>, <a href="BaseDiagramContextAMConfigurator.html#getPriority()">getPriority</a></code></div>
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
<h3>ClassDiagramContextAMConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ClassDiagramContextAMConfigurator</span>()</div>
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
<section class="detail" id="createLayoutActionsCategory()">
<h3>createLayoutActionsCategory</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></span> <span class="element-name">createLayoutActionsCategory</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="BaseDiagramContextAMConfigurator.html#createLayoutActionsCategory()">createLayoutActionsCategory</a></code> in class <code><a href="BaseDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramContextAMConfigurator</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configureSingleSelectionActions(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement[],com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>configureSingleSelectionActions</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">configureSingleSelectionActions</span><wbr/><span class="parameters">(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> actionsManager,
 <a href="../../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>[] selected,
 <a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> requestSource)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="BaseDiagramContextAMConfigurator.html#configureSingleSelectionActions(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement%5B%5D,com.nomagic.magicdraw.uml.symbols.PresentationElement)">configureSingleSelectionActions</a></code> in class <code><a href="BaseDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramContextAMConfigurator</a></code></dd>
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
