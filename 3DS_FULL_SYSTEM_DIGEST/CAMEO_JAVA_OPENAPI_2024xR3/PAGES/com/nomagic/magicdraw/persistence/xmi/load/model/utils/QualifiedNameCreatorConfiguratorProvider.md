# JAVA OPENAPI: QualifiedNameCreatorConfiguratorProvider (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/persistence/xmi/load/model/utils/QualifiedNameCreatorConfiguratorProvider.html
- source_path: `com/nomagic/magicdraw/persistence/xmi/load/model/utils/QualifiedNameCreatorConfiguratorProvider.html`
- source_sha256: `8fcb10e9666a3f34d98d7f6d588763782620ebed25c3da6fcdba5a58f9f31b17`
- captured_utc: `2026-07-14T16:55:26.843138+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.persistence.xmi.load.model.utils](package-summary.html)

## Class QualifiedNameCreatorConfiguratorProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.persistence.xmi.load.model.utils.QualifiedNameCreatorConfiguratorProvider

@OpenApipublic final classQualifiedNameCreatorConfiguratorProvider
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Holds external (registered by plugins) qualified name configurators. These configurators are
 applied on element unique name creation in:
 - Import of other project into opened project.
 - Orphan proxies replacement?

See Also:
[`QualifiedNameCreatorConfigurator`](QualifiedNameCreatorConfigurator.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addConfigurator](#addConfigurator(com.nomagic.magicdraw.persistence.xmi.load.model.utils.QualifiedNameCreatorConfigurator))([QualifiedNameCreatorConfigurator](QualifiedNameCreatorConfigurator.html) configurator)`

`static [QualifiedNameCreatorConfiguratorProvider](QualifiedNameCreatorConfiguratorProvider.html)`
`[getInstance](#getInstance())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRichNameString](#getRichNameString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Get name from all configurators.
`boolean`
`[removeConfigurator](#removeConfigurator(com.nomagic.magicdraw.persistence.xmi.load.model.utils.QualifiedNameCreatorConfigurator))([QualifiedNameCreatorConfigurator](QualifiedNameCreatorConfigurator.html) configurator)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
public static [QualifiedNameCreatorConfiguratorProvider](QualifiedNameCreatorConfiguratorProvider.html) getInstance()
Returns:
Instance of Singleton
addConfigurator
public void addConfigurator([QualifiedNameCreatorConfigurator](QualifiedNameCreatorConfigurator.html) configurator)
Parameters:
`configurator` - Configurator
removeConfigurator
public boolean removeConfigurator([QualifiedNameCreatorConfigurator](QualifiedNameCreatorConfigurator.html) configurator)
Parameters:
`configurator` - Configurator
Returns:
true if removed.
getRichNameString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRichNameString([Element](../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Get name from all configurators.
Parameters:
`element` - Element
Returns:
Conjuncted String from all configurators.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.persistence.xmi.load.model.utils</a></div>
<h1 class="title" title="Class QualifiedNameCreatorConfiguratorProvider">Class QualifiedNameCreatorConfiguratorProvider</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.persistence.xmi.load.model.utils.QualifiedNameCreatorConfiguratorProvider</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">QualifiedNameCreatorConfiguratorProvider</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Holds external (registered by plugins) qualified name configurators. These configurators are
 applied on element unique name creation in:
        - Import of other project into opened project.
        - Orphan proxies replacement?</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="QualifiedNameCreatorConfigurator.html" title="interface in com.nomagic.magicdraw.persistence.xmi.load.model.utils"><code>QualifiedNameCreatorConfigurator</code></a></li>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addConfigurator(com.nomagic.magicdraw.persistence.xmi.load.model.utils.QualifiedNameCreatorConfigurator)">addConfigurator</a><wbr/>(<a href="QualifiedNameCreatorConfigurator.html" title="interface in com.nomagic.magicdraw.persistence.xmi.load.model.utils">QualifiedNameCreatorConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="QualifiedNameCreatorConfiguratorProvider.html" title="class in com.nomagic.magicdraw.persistence.xmi.load.model.utils">QualifiedNameCreatorConfiguratorProvider</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRichNameString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getRichNameString</a><wbr/>(<a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get name from all configurators.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeConfigurator(com.nomagic.magicdraw.persistence.xmi.load.model.utils.QualifiedNameCreatorConfigurator)">removeConfigurator</a><wbr/>(<a href="QualifiedNameCreatorConfigurator.html" title="interface in com.nomagic.magicdraw.persistence.xmi.load.model.utils">QualifiedNameCreatorConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="QualifiedNameCreatorConfiguratorProvider.html" title="class in com.nomagic.magicdraw.persistence.xmi.load.model.utils">QualifiedNameCreatorConfiguratorProvider</a></span> <span class="element-name">getInstance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Instance of Singleton</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addConfigurator(com.nomagic.magicdraw.persistence.xmi.load.model.utils.QualifiedNameCreatorConfigurator)">
<h3>addConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addConfigurator</span><wbr/><span class="parameters">(<a href="QualifiedNameCreatorConfigurator.html" title="interface in com.nomagic.magicdraw.persistence.xmi.load.model.utils">QualifiedNameCreatorConfigurator</a> configurator)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - Configurator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeConfigurator(com.nomagic.magicdraw.persistence.xmi.load.model.utils.QualifiedNameCreatorConfigurator)">
<h3>removeConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">removeConfigurator</span><wbr/><span class="parameters">(<a href="QualifiedNameCreatorConfigurator.html" title="interface in com.nomagic.magicdraw.persistence.xmi.load.model.utils">QualifiedNameCreatorConfigurator</a> configurator)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - Configurator</dd>
<dt>Returns:</dt>
<dd>true if removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRichNameString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getRichNameString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRichNameString</span><wbr/><span class="parameters">(<a href="../../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Get name from all configurators.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - Element</dd>
<dt>Returns:</dt>
<dd>Conjuncted String from all configurators.</dd>
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
