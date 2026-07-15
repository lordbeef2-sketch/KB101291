# JAVA OPENAPI: ReadOnlyFlags (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/dependencymatrix/datamodel/cell/ReadOnlyFlags.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/datamodel/cell/ReadOnlyFlags.html`
- source_sha256: `92e8ab88789a60bdfe388f578579929a5912df5fd660a3d48228f623b7676113`
- captured_utc: `2026-07-14T16:57:53.410485+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.datamodel.cell](package-summary.html)

## Class ReadOnlyFlags

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.dependencymatrix.datamodel.cell.ReadOnlyFlags

@OpenApiAll
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public final classReadOnlyFlags
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Deprecated.
read only cell views are deprecated, to check whether the cell is editable or not you have try creating a criteria on the cell
Holds readonly information about cell: whether relations can be created or deleted between two cell elements
 
 There are only six available choices: canCreate:true/false; canEdit:true/false deleteMulti:true/false and all are made static. No other instances should be created.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [ReadOnlyFlags](ReadOnlyFlags.html)`
`[CREATE_DELETE](#CREATE_DELETE)`
Deprecated.
`static final [ReadOnlyFlags](ReadOnlyFlags.html)`
`[CREATE_DELETE_MULTI](#CREATE_DELETE_MULTI)`
Deprecated.
`static final [ReadOnlyFlags](ReadOnlyFlags.html)`
`[CREATE_NOT_DELETE](#CREATE_NOT_DELETE)`
Deprecated.
`static final [ReadOnlyFlags](ReadOnlyFlags.html)`
`[NOT_CREATE_DELETE](#NOT_CREATE_DELETE)`
Deprecated.
`static final [ReadOnlyFlags](ReadOnlyFlags.html)`
`[NOT_CREATE_DELETE_MULTI](#NOT_CREATE_DELETE_MULTI)`
Deprecated.
`static final [ReadOnlyFlags](ReadOnlyFlags.html)`
`[NOT_CREATE_NOT_DELETE](#NOT_CREATE_NOT_DELETE)`
Deprecated.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`boolean`
`[canCreate](#canCreate())()`
Deprecated.
Is it possible to create new dependencies for this cell
`boolean`
`[canDelete](#canDelete())()`
Deprecated.
Is there any dependencies to delete here
`static [ReadOnlyFlags](ReadOnlyFlags.html)`
`[getFlagObject](#getFlagObject(boolean,boolean))(boolean canCreate,
 boolean canDelete)`
Deprecated.
Returns required instance of this object according to provided flags
`static [ReadOnlyFlags](ReadOnlyFlags.html)`
`[getFlagObject](#getFlagObject(boolean,boolean,int))(boolean canCreate,
 boolean canDelete,
 int deleteCount)`
Deprecated.
returns flag object with additional info, if there are more than one delete action available
`boolean`
`[isDeleteMulti](#isDeleteMulti())()`
Deprecated.
Specific case, when it is required to know if there are one or more delete action for this cell
`boolean`
`[isEditable](#isEditable())()`
Deprecated.
is this cell can create or can delete at least one dependency
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
CREATE_DELETE
public static final [ReadOnlyFlags](ReadOnlyFlags.html) CREATE_DELETE
Deprecated.
CREATE_DELETE_MULTI
public static final [ReadOnlyFlags](ReadOnlyFlags.html) CREATE_DELETE_MULTI
Deprecated.
NOT_CREATE_DELETE
public static final [ReadOnlyFlags](ReadOnlyFlags.html) NOT_CREATE_DELETE
Deprecated.
NOT_CREATE_DELETE_MULTI
public static final [ReadOnlyFlags](ReadOnlyFlags.html) NOT_CREATE_DELETE_MULTI
Deprecated.
CREATE_NOT_DELETE
public static final [ReadOnlyFlags](ReadOnlyFlags.html) CREATE_NOT_DELETE
Deprecated.
NOT_CREATE_NOT_DELETE
public static final [ReadOnlyFlags](ReadOnlyFlags.html) NOT_CREATE_NOT_DELETE
Deprecated.
 ============ METHOD DETAIL ========== 
Method Details
canCreate
public boolean canCreate()
Deprecated.
Is it possible to create new dependencies for this cell
Returns:
`true` if it is possible to create at least one new dependency
canDelete
public boolean canDelete()
Deprecated.
Is there any dependencies to delete here
Returns:
`true` if it is possible to delete at least one dependency
isDeleteMulti
public boolean isDeleteMulti()
Deprecated.
Specific case, when it is required to know if there are one or more delete action for this cell
Returns:
`true` if there aer multiple delete actions
getFlagObject
public static [ReadOnlyFlags](ReadOnlyFlags.html) getFlagObject(boolean canCreate,
 boolean canDelete)
Deprecated.
Returns required instance of this object according to provided flags
Parameters:
`canCreate` - can relationship be created
`canDelete` - can existing relationships be deleted
Returns:
readonly flag instance
getFlagObject
public static [ReadOnlyFlags](ReadOnlyFlags.html) getFlagObject(boolean canCreate,
 boolean canDelete,
 int deleteCount)
Deprecated.
returns flag object with additional info, if there are more than one delete action available
Parameters:
`canCreate` - can relationship be created
`canDelete` - can existing relationships be deleted
`deleteCount` - probable delete action count
Returns:
readonly flag object instance
isEditable
public boolean isEditable()
Deprecated.
is this cell can create or can delete at least one dependency
Returns:
`true` if can create or can delete

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.datamodel.cell</a></div>
<h1 class="title" title="Class ReadOnlyFlags">Class ReadOnlyFlags</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.datamodel.cell.ReadOnlyFlags</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">ReadOnlyFlags</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">read only cell views are deprecated, to check whether the cell is editable or not you have try creating a criteria on the cell</div>
</div>
<div class="block">Holds readonly information about cell: whether relations can be created or deleted between two cell elements
 <p></p>
 There are only six available choices: canCreate:true/false; canEdit:true/false deleteMulti:true/false and all are made static. No other instances should be created.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CREATE_DELETE">CREATE_DELETE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>static final <a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CREATE_DELETE_MULTI">CREATE_DELETE_MULTI</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>static final <a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CREATE_NOT_DELETE">CREATE_NOT_DELETE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>static final <a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NOT_CREATE_DELETE">NOT_CREATE_DELETE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>static final <a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NOT_CREATE_DELETE_MULTI">NOT_CREATE_DELETE_MULTI</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>static final <a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NOT_CREATE_NOT_DELETE">NOT_CREATE_NOT_DELETE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#canCreate()">canCreate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Is it possible to create new dependencies for this cell</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#canDelete()">canDelete</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Is there any dependencies to delete here</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getFlagObject(boolean,boolean)">getFlagObject</a><wbr/>(boolean canCreate,
 boolean canDelete)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Returns required instance of this object according to provided flags</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getFlagObject(boolean,boolean,int)">getFlagObject</a><wbr/>(boolean canCreate,
 boolean canDelete,
 int deleteCount)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">returns flag object with additional info, if there are more than one delete action available</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isDeleteMulti()">isDeleteMulti</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Specific case, when it is required to know if there are one or more delete action for this cell</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isEditable()">isEditable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">is this cell can create or can delete at least one dependency</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="CREATE_DELETE">
<h3>CREATE_DELETE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></span> <span class="element-name">CREATE_DELETE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="CREATE_DELETE_MULTI">
<h3>CREATE_DELETE_MULTI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></span> <span class="element-name">CREATE_DELETE_MULTI</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="NOT_CREATE_DELETE">
<h3>NOT_CREATE_DELETE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></span> <span class="element-name">NOT_CREATE_DELETE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="NOT_CREATE_DELETE_MULTI">
<h3>NOT_CREATE_DELETE_MULTI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></span> <span class="element-name">NOT_CREATE_DELETE_MULTI</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="CREATE_NOT_DELETE">
<h3>CREATE_NOT_DELETE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></span> <span class="element-name">CREATE_NOT_DELETE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="NOT_CREATE_NOT_DELETE">
<h3>NOT_CREATE_NOT_DELETE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></span> <span class="element-name">NOT_CREATE_NOT_DELETE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
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
<section class="detail" id="canCreate()">
<h3>canCreate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canCreate</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Is it possible to create new dependencies for this cell</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if it is possible to create at least one new dependency</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canDelete()">
<h3>canDelete</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canDelete</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Is there any dependencies to delete here</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if it is possible to delete at least one dependency</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDeleteMulti()">
<h3>isDeleteMulti</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDeleteMulti</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Specific case, when it is required to know if there are one or more delete action for this cell</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if there aer multiple delete actions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFlagObject(boolean,boolean)">
<h3>getFlagObject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></span> <span class="element-name">getFlagObject</span><wbr/><span class="parameters">(boolean canCreate,
 boolean canDelete)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Returns required instance of this object according to provided flags</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>canCreate</code> - can relationship be created</dd>
<dd><code>canDelete</code> - can existing relationships be deleted</dd>
<dt>Returns:</dt>
<dd>readonly flag instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFlagObject(boolean,boolean,int)">
<h3>getFlagObject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a></span> <span class="element-name">getFlagObject</span><wbr/><span class="parameters">(boolean canCreate,
 boolean canDelete,
 int deleteCount)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">returns flag object with additional info, if there are more than one delete action available</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>canCreate</code> - can relationship be created</dd>
<dd><code>canDelete</code> - can existing relationships be deleted</dd>
<dd><code>deleteCount</code> - probable delete action count</dd>
<dt>Returns:</dt>
<dd>readonly flag object instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditable()">
<h3>isEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEditable</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">is this cell can create or can delete at least one dependency</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if can create or can delete</dd>
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
