# JAVA OPENAPI: DiagramDescriptor (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml/DiagramDescriptor.html
- source_path: `com/nomagic/magicdraw/uml/DiagramDescriptor.html`
- source_sha256: `dbc017db2bfd9664e52921f0abbb6c0be1dbbdc389572fdd12b75d7b346f595a`
- captured_utc: `2026-07-14T16:58:27.188170+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class DiagramDescriptor

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.DiagramDescriptor

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[NonSymbolDiagramDescriptor](diagrams/NonSymbolDiagramDescriptor.html)`

@OpenApipublic abstract classDiagramDescriptor
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)

Descriptor of some extended diagram. 

 This descriptor is used to define a new diagram type in the MagicDraw application. New diagram type be extended
 from some already existing type. New diagram will have separate diagram panel with its own toolbar.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getCategory](#getCategory())()`
Diagram category name.
`[MDActionsManager](../actions/MDActionsManager.html)`
`[getDiagramActions](#getDiagramActions())()`
Returns manager of actions used in the diagram.
`abstract [DiagramContextAMConfigurator](../actions/DiagramContextAMConfigurator.html)`
`[getDiagramContextConfigurator](#getDiagramContextConfigurator())()`

`abstract [AMConfigurator](../../actions/AMConfigurator.html)`
`[getDiagramShortcutsConfigurator](#getDiagramShortcutsConfigurator())()`

`abstract [AMConfigurator](../../actions/AMConfigurator.html)`
`[getDiagramToolbarConfigurator](#getDiagramToolbarConfigurator())()`

`abstract [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDiagramTypeId](#getDiagramTypeId())()`
Return diagram type id.
`abstract [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getPluralDiagramTypeHumanName](#getPluralDiagramTypeHumanName())()`
Return diagram human name.
`abstract [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getSingularDiagramTypeHumanName](#getSingularDiagramTypeHumanName())()`
Return diagram human name.
`abstract [URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html)`
`[getSmallIconURL](#getSmallIconURL())()`
URL of small icon for diagram.
`abstract [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getSuperType](#getSuperType())()`
Returns super type of this diagram.
`abstract [ResizableIcon](../../ui/ResizableIcon.html)`
`[getSVGIcon](#getSVGIcon())()`
Resizable icon for diagram.
`abstract boolean`
`[isCreatable](#isCreatable())()`
Returns creatable flag.
`boolean`
`[isUsedForSymbols](#isUsedForSymbols())()`
Check if this diagram is used to draw symbols.
`void`
`[setCategory](#setCategory(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) category)`
Set diagram category name.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getSuperType
@OpenApipublic abstract [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getSuperType()
Returns super type of this diagram.
Returns:
String the 'super diagram' type of the diagram type.
 E.g. `Interaction Diagram` is a 'super diagram' for `Collaboration Diagram` and
 `Sequence Diagram`.
isCreatable
@OpenApipublic abstract boolean isCreatable()
Returns creatable flag.
Returns:
boolean flag indicating if the diagram will be creatable.
isUsedForSymbols
@OpenApipublic boolean isUsedForSymbols()
Check if this diagram is used to draw symbols. Some diagram may be used to display tables,
 graphs or other components (for example dependency matrix table)
Returns:
true if diagram is used to draw symbols
getDiagramToolbarConfigurator
@CheckForNull
@OpenApipublic abstract [AMConfigurator](../../actions/AMConfigurator.html) getDiagramToolbarConfigurator()
Returns:
AMConfigurator which configures described diagram toolbar.
getDiagramShortcutsConfigurator
@CheckForNull
@OpenApipublic abstract [AMConfigurator](../../actions/AMConfigurator.html) getDiagramShortcutsConfigurator()
Returns:
AMConfigurator which configures described diagram shortcuts.
getDiagramContextConfigurator
@CheckForNull
@OpenApipublic abstract [DiagramContextAMConfigurator](../actions/DiagramContextAMConfigurator.html) getDiagramContextConfigurator()
Returns:
AMConfigurator which configures described diagram context menu actions.
getDiagramTypeId
@OpenApipublic abstract [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDiagramTypeId()
Return diagram type id. It is used to identify the diagram.
Returns:
String used to identify diagram type.
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
getSingularDiagramTypeHumanName
@OpenApipublic abstract [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getSingularDiagramTypeHumanName()
Return diagram human name. It is used to show the diagram type in the UI.
Returns:
human diagram name in singular.
getPluralDiagramTypeHumanName
@OpenApipublic abstract [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getPluralDiagramTypeHumanName()
Return diagram human name. It is used to show the diagram type in the UI.
Returns:
human diagram name in plural.
getSVGIcon
@CheckForNull
@OpenApipublic abstract [ResizableIcon](../../ui/ResizableIcon.html) getSVGIcon()
Resizable icon for diagram. svg and wmf format. Used in Content diagram.
Returns:
resizable icon in svg or wmf formats.
getSmallIconURL
@CheckForNull
@OpenApipublic abstract [URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) getSmallIconURL()
URL of small icon for diagram. Used in browser and menu.
Returns:
URL to icon shown diagram in browser and menu items.
getDiagramActions
@OpenApi
@CheckForNullpublic [MDActionsManager](../actions/MDActionsManager.html) getDiagramActions()
Returns manager of actions used in the diagram.
 Later these actions must be configured for toolbar or shortcuts.
 Only one instance of action must be used in the configurators. If this rule is not applied, some problems may
 occur(for example changed by user keyboard shortcuts for action may not be saved).
Returns:
manager of actions.
getCategory
@CheckForNull
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getCategory()
Diagram category name.
Returns:
diagram category
setCategory
@OpenApipublic void setCategory(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) category)
Set diagram category name.
Parameters:
`category` - category diagram category name

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class DiagramDescriptor">Class DiagramDescriptor</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.DiagramDescriptor</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="diagrams/NonSymbolDiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml.diagrams">NonSymbolDiagramDescriptor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">DiagramDescriptor</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></span></div>
<div class="block">Descriptor of some extended diagram.<br/>
 This descriptor is used to define a new diagram type in the MagicDraw application. New diagram type be extended
 from some already existing type. New diagram will have separate diagram panel with its own toolbar.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCategory()">getCategory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Diagram category name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../actions/MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramActions()">getDiagramActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns manager of actions used in the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="../actions/DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramContextConfigurator()">getDiagramContextConfigurator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramShortcutsConfigurator()">getDiagramShortcutsConfigurator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramToolbarConfigurator()">getDiagramToolbarConfigurator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramTypeId()">getDiagramTypeId</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return diagram type id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPluralDiagramTypeHumanName()">getPluralDiagramTypeHumanName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return diagram human name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSingularDiagramTypeHumanName()">getSingularDiagramTypeHumanName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return diagram human name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSmallIconURL()">getSmallIconURL</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">URL of small icon for diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSuperType()">getSuperType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns super type of this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSVGIcon()">getSVGIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Resizable icon for diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isCreatable()">isCreatable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns creatable flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUsedForSymbols()">isUsedForSymbols</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if this diagram is used to draw symbols.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCategory(java.lang.String)">setCategory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> category)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set diagram category name.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="getSuperType()">
<h3>getSuperType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSuperType</span>()</div>
<div class="block">Returns super type of this diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>String the 'super diagram' type of the diagram type.
 E.g. <code>Interaction Diagram</code> is a 'super diagram' for <code>Collaboration Diagram</code> and
 <code>Sequence Diagram</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreatable()">
<h3>isCreatable</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type">boolean</span> <span class="element-name">isCreatable</span>()</div>
<div class="block">Returns creatable flag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean flag indicating if the diagram will be creatable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUsedForSymbols()">
<h3>isUsedForSymbols</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUsedForSymbols</span>()</div>
<div class="block">Check if this diagram is used to draw symbols. Some diagram may be used to display tables,
 graphs or other components (for example  dependency matrix table)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram is used to draw symbols</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramToolbarConfigurator()">
<h3>getDiagramToolbarConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></span> <span class="element-name">getDiagramToolbarConfigurator</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>AMConfigurator which configures described diagram toolbar.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramShortcutsConfigurator()">
<h3>getDiagramShortcutsConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></span> <span class="element-name">getDiagramShortcutsConfigurator</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>AMConfigurator which configures described diagram shortcuts.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramContextConfigurator()">
<h3>getDiagramContextConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a href="../actions/DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a></span> <span class="element-name">getDiagramContextConfigurator</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>AMConfigurator which configures described diagram context menu actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramTypeId()">
<h3>getDiagramTypeId</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramTypeId</span>()</div>
<div class="block">Return diagram type id. It is used to identify the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>String used to identify diagram type.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSingularDiagramTypeHumanName()">
<h3>getSingularDiagramTypeHumanName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSingularDiagramTypeHumanName</span>()</div>
<div class="block">Return diagram human name. It is used to show the diagram type in the UI.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>human diagram name in singular.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPluralDiagramTypeHumanName()">
<h3>getPluralDiagramTypeHumanName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPluralDiagramTypeHumanName</span>()</div>
<div class="block">Return diagram human name. It is used to show the diagram type in the UI.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>human diagram name in plural.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSVGIcon()">
<h3>getSVGIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getSVGIcon</span>()</div>
<div class="block">Resizable icon for diagram. svg and wmf format. Used in Content diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>resizable icon in svg or wmf formats.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSmallIconURL()">
<h3>getSmallIconURL</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a></span> <span class="element-name">getSmallIconURL</span>()</div>
<div class="block">URL of small icon for diagram. Used in browser and menu.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>URL to icon shown diagram in browser and menu items.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramActions()">
<h3>getDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../actions/MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">getDiagramActions</span>()</div>
<div class="block">Returns manager of actions used in the diagram.
 Later these actions must be configured for toolbar or shortcuts.
 Only one instance of action must be used in the configurators. If this rule is not applied, some problems may
 occur(for example changed by user keyboard shortcuts for action may not be saved).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager of actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCategory()">
<h3>getCategory</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCategory</span>()</div>
<div class="block">Diagram category name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram category</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCategory(java.lang.String)">
<h3>setCategory</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCategory</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> category)</span></div>
<div class="block">Set diagram category name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - category diagram category name</dd>
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
