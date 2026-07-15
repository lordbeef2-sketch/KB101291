# JAVA OPENAPI: SortTable (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/reportwizard/tools/dialog/SortTable.html
- source_path: `com/nomagic/reportwizard/tools/dialog/SortTable.html`
- source_sha256: `f817e2293e483a52dee4f9c4c6fc4be8642dbecd23cc4f573648d1d23b79ba4e`
- captured_utc: `2026-07-14T16:46:15.400007+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.dialog](package-summary.html)

## Class SortTable

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../../../magicreport/engine/Tool.html)
[com.nomagic.magicreport.engine.tools.SortTool](../../../magicreport/engine/tools/SortTool.html)
com.nomagic.reportwizard.tools.dialog.SortTable

All Implemented Interfaces:
`[ITool](../../../magicreport/engine/ITool.html)`, `[IVariable](../../../magicreport/IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classSortTable
extends [SortTool](../../../magicreport/engine/tools/SortTool.html)

class for sort table data.

Since:
Jun 16, 2009
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.reportwizard.tools.dialog.SortTable)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from class com.nomagic.magicreport.engine.tools.[SortTool](../../../magicreport/engine/tools/SortTool.html)
`[SortTool.AscendingSort](../../../magicreport/engine/tools/SortTool.AscendingSort.html), [SortTool.DescendingSort](../../../magicreport/engine/tools/SortTool.DescendingSort.html), [SortTool.FirstNumberAscendingSort](../../../magicreport/engine/tools/SortTool.FirstNumberAscendingSort.html), [SortTool.FirstNumberDescendingSort](../../../magicreport/engine/tools/SortTool.FirstNumberDescendingSort.html), [SortTool.HumanAscendingSort](../../../magicreport/engine/tools/SortTool.HumanAscendingSort.html), [SortTool.HumanDescendingSort](../../../magicreport/engine/tools/SortTool.HumanDescendingSort.html)`
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[ITool.HTMLString](../../../magicreport/engine/ITool.HTMLString.html), [ITool.RetainedString](../../../magicreport/engine/ITool.RetainedString.html), [ITool.Void](../../../magicreport/engine/ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.engine.tools.[SortTool](../../../magicreport/engine/tools/SortTool.html)
`[CONTEXT_NAME](../../../magicreport/engine/tools/SortTool.html#CONTEXT_NAME)`
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../../../magicreport/engine/Tool.html)
`[context](../../../magicreport/engine/Tool.html#context), [properties](../../../magicreport/engine/Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[VOID](../../../magicreport/engine/ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SortTable](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getBlankValue](#getBlankValue())()`
Return the value for blank field.
`void`
`[setProperties](#setProperties(java.util.Properties))([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
method for set value to blankValue.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[sort](#sort(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)`
sort collection from JTable to ascendant collection.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)`
`[sortDesc](#sortDesc(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)`
sort collection from JTable to descendant collection.
Methods inherited from class com.nomagic.magicreport.engine.tools.[SortTool](../../../magicreport/engine/tools/SortTool.html)
`[defaultSort](../../../magicreport/engine/tools/SortTool.html#defaultSort(java.util.Collection)), [getNextToken](../../../magicreport/engine/tools/SortTool.html#getNextToken(java.lang.String,int,int)), [getValue](../../../magicreport/engine/tools/SortTool.html#getValue(java.lang.Object,java.lang.String)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,boolean)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.lang.String)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.lang.String,boolean)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.util.Collection)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.util.Collection,java.lang.String)), [humanSort](../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.util.Collection,java.lang.String,boolean)), [isForceNumber](../../../magicreport/engine/tools/SortTool.html#isForceNumber()), [setForceNumber](../../../magicreport/engine/tools/SortTool.html#setForceNumber(boolean)), [sort](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.lang.String)), [sort](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.lang.String,boolean)), [sort](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.util.Collection)), [sort](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.util.Collection,java.lang.String)), [sort](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.util.Collection,java.lang.String,boolean)), [sortByFirstNumber](../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection)), [sortByFirstNumber](../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection,java.lang.String)), [sortByFirstNumber](../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection,java.util.Collection)), [sortByFirstNumber](../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection,java.util.Collection,java.lang.String)), [sortByLocale](../../../magicreport/engine/tools/SortTool.html#sortByLocale(java.util.Collection,java.lang.String)), [sortByLocale](../../../magicreport/engine/tools/SortTool.html#sortByLocale(java.util.Collection,java.lang.String,java.lang.String))`
Methods inherited from class com.nomagic.magicreport.engine.[Tool](../../../magicreport/engine/Tool.html)
`[clone](../../../magicreport/engine/Tool.html#clone()), [getContext](../../../magicreport/engine/Tool.html#getContext()), [getProperties](../../../magicreport/engine/Tool.html#getProperties()), [getProperty](../../../magicreport/engine/Tool.html#getProperty(java.lang.String)), [getProperty](../../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](../../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)), [setContext](../../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[clearTool](../../../magicreport/engine/ITool.html#clearTool())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SortTable
public SortTable()
 ============ METHOD DETAIL ========== 
Method Details
setProperties
public void setProperties([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
method for set value to blankValue.
Specified by:
`[setProperties](../../../magicreport/engine/ITool.html#setProperties(java.util.Properties))` in interface `[ITool](../../../magicreport/engine/ITool.html)`
Overrides:
`[setProperties](../../../magicreport/engine/Tool.html#setProperties(java.util.Properties))` in class `[Tool](../../../magicreport/engine/Tool.html)`
Parameters:
`properties` - properties
See Also:
[`Tool.setProperties(java.util.Properties)`](../../../magicreport/engine/Tool.html#setProperties(java.util.Properties))
getBlankValue
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getBlankValue()
Return the value for blank field.
Returns:
value for blank field
sort
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) sort([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)
sort collection from JTable to ascendant collection.
Overrides:
`[sort](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection))` in class `[SortTool](../../../magicreport/engine/tools/SortTool.html)`
Parameters:
`collection` - collection from JTable
Returns:
new collection
See Also:
[`SortTool.sort(java.util.Collection)`](../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection))
sortDesc
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) sortDesc([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) collection)
sort collection from JTable to descendant collection.
Parameters:
`collection` - collection from JTable
Returns:
new collection

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.dialog</a></div>
<h1 class="title" title="Class SortTable">Class SortTable</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance"><a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">com.nomagic.magicreport.engine.tools.SortTool</a>
<div class="inheritance">com.nomagic.reportwizard.tools.dialog.SortTable</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../../magicreport/IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SortTable</span>
<span class="extends-implements">extends <a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></span></div>
<div class="block">class for sort table data.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 16, 2009</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.reportwizard.tools.dialog.SortTable">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.tools.SortTool">Nested classes/interfaces inherited from class com.nomagic.magicreport.engine.tools.<a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></h2>
<code><a href="../../../magicreport/engine/tools/SortTool.AscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.AscendingSort</a>, <a href="../../../magicreport/engine/tools/SortTool.DescendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.DescendingSort</a>, <a href="../../../magicreport/engine/tools/SortTool.FirstNumberAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.FirstNumberAscendingSort</a>, <a href="../../../magicreport/engine/tools/SortTool.FirstNumberDescendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.FirstNumberDescendingSort</a>, <a href="../../../magicreport/engine/tools/SortTool.HumanAscendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanAscendingSort</a>, <a href="../../../magicreport/engine/tools/SortTool.HumanDescendingSort.html" title="class in com.nomagic.magicreport.engine.tools">SortTool.HumanDescendingSort</a></code></div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="../../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.tools.SortTool">Fields inherited from class com.nomagic.magicreport.engine.tools.<a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></h3>
<code><a href="../../../magicreport/engine/tools/SortTool.html#CONTEXT_NAME">CONTEXT_NAME</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../../magicreport/engine/Tool.html#context">context</a>, <a href="../../../magicreport/engine/Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../../magicreport/engine/ITool.html#VOID">VOID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SortTable</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBlankValue()">getBlankValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the value for blank field.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperties(java.util.Properties)">setProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">method for set value to blankValue.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sort(java.util.Collection)">sort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sort collection from JTable to ascendant collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sortDesc(java.util.Collection)">sortDesc</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sort collection from JTable to descendant collection.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.tools.SortTool">Methods inherited from class com.nomagic.magicreport.engine.tools.<a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></h3>
<code><a href="../../../magicreport/engine/tools/SortTool.html#defaultSort(java.util.Collection)">defaultSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#getNextToken(java.lang.String,int,int)">getNextToken</a>, <a href="../../../magicreport/engine/tools/SortTool.html#getValue(java.lang.Object,java.lang.String)">getValue</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,boolean)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.lang.String)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.lang.String,boolean)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.util.Collection)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.util.Collection,java.lang.String)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#humanSort(java.util.Collection,java.util.Collection,java.lang.String,boolean)">humanSort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#isForceNumber()">isForceNumber</a>, <a href="../../../magicreport/engine/tools/SortTool.html#setForceNumber(boolean)">setForceNumber</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.lang.String)">sort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.lang.String,boolean)">sort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.util.Collection)">sort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.util.Collection,java.lang.String)">sort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection,java.util.Collection,java.lang.String,boolean)">sort</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection)">sortByFirstNumber</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection,java.lang.String)">sortByFirstNumber</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection,java.util.Collection)">sortByFirstNumber</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sortByFirstNumber(java.util.Collection,java.util.Collection,java.lang.String)">sortByFirstNumber</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sortByLocale(java.util.Collection,java.lang.String)">sortByLocale</a>, <a href="../../../magicreport/engine/tools/SortTool.html#sortByLocale(java.util.Collection,java.lang.String,java.lang.String)">sortByLocale</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../../magicreport/engine/Tool.html#clone()">clone</a>, <a href="../../../magicreport/engine/Tool.html#getContext()">getContext</a>, <a href="../../../magicreport/engine/Tool.html#getProperties()">getProperties</a>, <a href="../../../magicreport/engine/Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="../../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../../magicreport/engine/ITool.html#clearTool()">clearTool</a></code></div>
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
<h3>SortTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SortTable</span>()</div>
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
<section class="detail" id="setProperties(java.util.Properties)">
<h3>setProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">method for set value to blankValue.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../magicreport/engine/ITool.html#setProperties(java.util.Properties)">setProperties</a></code> in interface <code><a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../../../magicreport/engine/Tool.html#setProperties(java.util.Properties)">setProperties</a></code> in class <code><a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>properties</code> - properties</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../../magicreport/engine/Tool.html#setProperties(java.util.Properties)"><code>Tool.setProperties(java.util.Properties)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBlankValue()">
<h3>getBlankValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getBlankValue</span>()</div>
<div class="block">Return the value for blank field.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value for blank field</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sort(java.util.Collection)">
<h3>sort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">sort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</span></div>
<div class="block">sort collection from JTable to ascendant collection.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection)">sort</a></code> in class <code><a href="../../../magicreport/engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>collection</code> - collection from JTable</dd>
<dt>Returns:</dt>
<dd>new collection</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../../magicreport/engine/tools/SortTool.html#sort(java.util.Collection)"><code>SortTool.sort(java.util.Collection)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sortDesc(java.util.Collection)">
<h3>sortDesc</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">sortDesc</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection)</span></div>
<div class="block">sort collection from JTable to descendant collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection from JTable</dd>
<dt>Returns:</dt>
<dd>new collection</dd>
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
