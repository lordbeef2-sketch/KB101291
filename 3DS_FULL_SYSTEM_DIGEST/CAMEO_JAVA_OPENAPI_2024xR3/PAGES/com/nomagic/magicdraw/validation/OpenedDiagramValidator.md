# JAVA OPENAPI: OpenedDiagramValidator (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/validation/OpenedDiagramValidator.html
- source_path: `com/nomagic/magicdraw/validation/OpenedDiagramValidator.html`
- source_sha256: `e6c3db1c6c6d17a1a3d43fe209c37004e551351e45a01c0e1237422b24975e93`
- captured_utc: `2026-07-14T16:56:08.143605+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.validation](package-summary.html)

## Class OpenedDiagramValidator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.validation.DiagramValidator](DiagramValidator.html)
com.nomagic.magicdraw.validation.OpenedDiagramValidator

All Implemented Interfaces:
`com.nomagic.magicdraw.core.diagram.DiagramsChangeListener`, `[ValidationRule](ValidationRule.html)`

@OpenApiAllpublic abstract classOpenedDiagramValidator
extends [DiagramValidator](DiagramValidator.html)
implements com.nomagic.magicdraw.core.diagram.DiagramsChangeListener

Works the same as the base rule [`DiagramValidator`](DiagramValidator.html), but narrows the scope down only to currently opened diagrams.
 When creating annotations, the diagrams in scope should be retrieved by using [`DiagramValidator.getDiagrams()`](DiagramValidator.html#getDiagrams()) method.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[OpenedDiagramValidator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected boolean`
`[acceptDiagram](#acceptDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) diagram)`

`void`
`[diagramsChanged](#diagramsChanged(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)> opened,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)> closed)`
Called when opened diagrams changes.
`void`
`[dispose](#dispose())()`
Unregisters all listeners that were registered and releases other resources.
`void`
`[init](#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
This is the first method that is invoked on the implementation of the `ValidationRule` interface.
Methods inherited from class com.nomagic.magicdraw.validation.[DiagramValidator](DiagramValidator.html)
`[getAnnotations](DiagramValidator.html#getAnnotations(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)), [getDiagrams](DiagramValidator.html#getDiagrams()), [getDiagramsStream](DiagramValidator.html#getDiagramsStream()), [getPresentationElements](DiagramValidator.html#getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getPresentationElements](DiagramValidator.html#getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)), [getProject](DiagramValidator.html#getProject()), [isElementInScope](DiagramValidator.html#isElementInScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [needsRun](DiagramValidator.html#needsRun()), [needsRun](DiagramValidator.html#needsRun(java.beans.PropertyChangeEvent)), [run](DiagramValidator.html#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)), [setNeedsRun](DiagramValidator.html#setNeedsRun(boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
OpenedDiagramValidator
public OpenedDiagramValidator()
 ============ METHOD DETAIL ========== 
Method Details
acceptDiagram
protected boolean acceptDiagram([DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) diagram)
Overrides:
`[acceptDiagram](DiagramValidator.html#acceptDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))` in class `[DiagramValidator](DiagramValidator.html)`
Returns:
true if the diagram in scope should be returned by [`DiagramValidator.getDiagrams()`](DiagramValidator.html#getDiagrams()) method
init
public void init([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
Description copied from interface: `[ValidationRule](ValidationRule.html#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))`
This is the first method that is invoked on the implementation of the `ValidationRule` interface.
 Implementation can initialize internal state if required.
Specified by:
`[init](ValidationRule.html#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))` in interface `[ValidationRule](ValidationRule.html)`
Overrides:
`[init](DiagramValidator.html#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))` in class `[DiagramValidator](DiagramValidator.html)`
Parameters:
`project` - a project of the constraint
`constraint` - a constraint object
diagramsChanged
public void diagramsChanged([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)> opened,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)> closed)
Called when opened diagrams changes. Should not be called manually.
Specified by:
`diagramsChanged` in interface `com.nomagic.magicdraw.core.diagram.DiagramsChangeListener`
Parameters:
`opened` - newly opened diagrams including inner diagrams displayed within them.
`closed` - newly closed diagrams including inner diagrams, if the diagrams are no longer open in any other tab.
dispose
public void dispose()
Description copied from class: `[DiagramValidator](DiagramValidator.html#dispose())`
Unregisters all listeners that were registered and releases other resources.
Specified by:
`[dispose](ValidationRule.html#dispose())` in interface `[ValidationRule](ValidationRule.html)`
Overrides:
`[dispose](DiagramValidator.html#dispose())` in class `[DiagramValidator](DiagramValidator.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.validation</a></div>
<h1 class="title" title="Class OpenedDiagramValidator">Class OpenedDiagramValidator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="DiagramValidator.html" title="class in com.nomagic.magicdraw.validation">com.nomagic.magicdraw.validation.DiagramValidator</a>
<div class="inheritance">com.nomagic.magicdraw.validation.OpenedDiagramValidator</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.core.diagram.DiagramsChangeListener</code>, <code><a href="ValidationRule.html" title="interface in com.nomagic.magicdraw.validation">ValidationRule</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">OpenedDiagramValidator</span>
<span class="extends-implements">extends <a href="DiagramValidator.html" title="class in com.nomagic.magicdraw.validation">DiagramValidator</a>
implements com.nomagic.magicdraw.core.diagram.DiagramsChangeListener</span></div>
<div class="block">Works the same as the base rule <a href="DiagramValidator.html" title="class in com.nomagic.magicdraw.validation"><code>DiagramValidator</code></a>, but narrows the scope down only to currently opened diagrams.
 When creating annotations, the diagrams in scope should be retrieved by using <a href="DiagramValidator.html#getDiagrams()"><code>DiagramValidator.getDiagrams()</code></a> method.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">OpenedDiagramValidator</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">acceptDiagram</a><wbr/>(<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#diagramsChanged(java.util.Collection,java.util.Collection)">diagramsChanged</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; opened,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; closed)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called when opened diagrams changes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregisters all listeners that were registered and releases other resources.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">init</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This is the first method that is invoked on the implementation of the <code>ValidationRule</code> interface.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.validation.DiagramValidator">Methods inherited from class com.nomagic.magicdraw.validation.<a href="DiagramValidator.html" title="class in com.nomagic.magicdraw.validation">DiagramValidator</a></h3>
<code><a href="DiagramValidator.html#getAnnotations(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">getAnnotations</a>, <a href="DiagramValidator.html#getDiagrams()">getDiagrams</a>, <a href="DiagramValidator.html#getDiagramsStream()">getDiagramsStream</a>, <a href="DiagramValidator.html#getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getPresentationElements</a>, <a href="DiagramValidator.html#getPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">getPresentationElements</a>, <a href="DiagramValidator.html#getProject()">getProject</a>, <a href="DiagramValidator.html#isElementInScope(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isElementInScope</a>, <a href="DiagramValidator.html#needsRun()">needsRun</a>, <a href="DiagramValidator.html#needsRun(java.beans.PropertyChangeEvent)">needsRun</a>, <a href="DiagramValidator.html#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">run</a>, <a href="DiagramValidator.html#setNeedsRun(boolean)">setNeedsRun</a></code></div>
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
<h3>OpenedDiagramValidator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OpenedDiagramValidator</span>()</div>
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
<section class="detail" id="acceptDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>acceptDiagram</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">acceptDiagram</span><wbr/><span class="parameters">(<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DiagramValidator.html#acceptDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">acceptDiagram</a></code> in class <code><a href="DiagramValidator.html" title="class in com.nomagic.magicdraw.validation">DiagramValidator</a></code></dd>
<dt>Returns:</dt>
<dd>true if the diagram in scope should be returned by <a href="DiagramValidator.html#getDiagrams()"><code>DiagramValidator.getDiagrams()</code></a> method</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ValidationRule.html#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">ValidationRule</a></code></span></div>
<div class="block">This is the first method that is invoked on the implementation of the <code>ValidationRule</code> interface.
 Implementation can initialize internal state if required.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ValidationRule.html#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">init</a></code> in interface <code><a href="ValidationRule.html" title="interface in com.nomagic.magicdraw.validation">ValidationRule</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="DiagramValidator.html#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">init</a></code> in class <code><a href="DiagramValidator.html" title="class in com.nomagic.magicdraw.validation">DiagramValidator</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - a project of the constraint</dd>
<dd><code>constraint</code> - a constraint object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="diagramsChanged(java.util.Collection,java.util.Collection)">
<h3>diagramsChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">diagramsChanged</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; opened,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; closed)</span></div>
<div class="block">Called when opened diagrams changes. Should not be called manually.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>diagramsChanged</code> in interface <code>com.nomagic.magicdraw.core.diagram.DiagramsChangeListener</code></dd>
<dt>Parameters:</dt>
<dd><code>opened</code> - newly opened diagrams including inner diagrams displayed within them.</dd>
<dd><code>closed</code> - newly closed diagrams including inner diagrams, if the diagrams are no longer open in any other tab.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="DiagramValidator.html#dispose()">DiagramValidator</a></code></span></div>
<div class="block">Unregisters all listeners that were registered and releases other resources.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ValidationRule.html#dispose()">dispose</a></code> in interface <code><a href="ValidationRule.html" title="interface in com.nomagic.magicdraw.validation">ValidationRule</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="DiagramValidator.html#dispose()">dispose</a></code> in class <code><a href="DiagramValidator.html" title="class in com.nomagic.magicdraw.validation">DiagramValidator</a></code></dd>
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
