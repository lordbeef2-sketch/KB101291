# JAVA OPENAPI: AbstractDiagramLayouterOptionsGroup (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/core/options/AbstractDiagramLayouterOptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/AbstractDiagramLayouterOptionsGroup.html`
- source_sha256: `268fd8c192fe682a01e9f10435cc8b1e9db2f02bd19080af59f49390d78b5528`
- captured_utc: `2026-07-14T16:51:15.219124+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class AbstractDiagramLayouterOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[CircularLayouterOptionsGroup](CircularLayouterOptionsGroup.html)`, `[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)`, `[OrganicLayouterOptionsGroup](OrganicLayouterOptionsGroup.html)`, `[OrganicRouterOptionsGroup](OrganicRouterOptionsGroup.html)`, `[OrthogonalLayouterOptionsGroup](OrthogonalLayouterOptionsGroup.html)`, `[OrthogonalRouterOptionsGroup](OrthogonalRouterOptionsGroup.html)`, `[TreeLayouterOptionsGroup](TreeLayouterOptionsGroup.html)`

@OpenApiAllpublic abstract classAbstractDiagramLayouterOptionsGroup
extends [AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ALIGNMENT_BOTTOM](#ALIGNMENT_BOTTOM)`
Aligns layouted shapes according their bottom y coordinate.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ALIGNMENT_CENTER](#ALIGNMENT_CENTER)`
Aligns layouted shapes according their centers.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ALIGNMENT_TOP](#ALIGNMENT_TOP)`
Aligns layouted shapes according their top y coordinate.
`protected static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[LAYOUT_LABEL_CONSIDERATION](#LAYOUT_LABEL_CONSIDERATION)`
Label consideration modes
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LAYOUT_LABEL_CONSIDERATION_FULL](#LAYOUT_LABEL_CONSIDERATION_FULL)`
Full label consideration mode.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LAYOUT_LABEL_CONSIDERATION_NONE](#LAYOUT_LABEL_CONSIDERATION_NONE)`
A mode where labels are not considered.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LAYOUT_LABEL_CONSIDERATION_PARTIAL](#LAYOUT_LABEL_CONSIDERATION_PARTIAL)`
Partial label consideration mode.
`protected static final int`
`[MAX_INT_VALUE](#MAX_INT_VALUE)`
The maximum allowed value for integer fields(e.g minimal node distance, minimal edge distance)
`protected static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[SHAPE_ALIGNMENT](#SHAPE_ALIGNMENT)`
Different ways of aligning shapes after layout.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractDiagramLayouterOptionsGroup](#%3Cinit%3E(java.lang.String,com.nomagic.magicdraw.properties.PropertyManager,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [PropertyManager](../../properties/PropertyManager.html) options,
 boolean visible)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)`
`[getCopy](#getCopy())()`

`boolean`
`[getMakePreferredLayoutSize](#getMakePreferredLayoutSize())()`
Get reset shape size property value
`boolean`
`[getOptimizeLabelOrientations](#getOptimizeLabelOrientations())()`
Get value if label orientations should be optimized
`protected void`
`[initCommonDefaultValues](#initCommonDefaultValues())()`

`boolean`
`[isMoveToFreeSpace](#isMoveToFreeSpace())()`
Checks Is Move to free space?
`void`
`[setDefaultValues](#setDefaultValues())()`
Sets default values for the properties contained in this group.
`void`
`[setMakePreferredLayoutSize](#setMakePreferredLayoutSize(boolean))(boolean b)`
Set reset shape size property value
`void`
`[setMoveToFreeSpace](#setMoveToFreeSpace(boolean))(boolean b)`
Sets status move to free space
`void`
`[setOptimizeLabelOrientations](#setOptimizeLabelOrientations(boolean))(boolean value)`
Set reset shape size property value
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
`[addInvisibleProperty](AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)), [getOptions](AbstractPropertyOptionsGroup.html#getOptions()), [getProperty](AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)), [getVisibleOptions](AbstractPropertyOptionsGroup.html#getVisibleOptions()), [removeProperty](AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)), [setOptions](AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)), [setPropertiesInvisible](AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)), [setPropertyInvisible](AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](OptionsGroup.html)
`[getGroupIcon](OptionsGroup.html#getGroupIcon()), [getIcon](OptionsGroup.html#getIcon()), [getName](OptionsGroup.html#getName())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ALIGNMENT_TOP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ALIGNMENT_TOP
Aligns layouted shapes according their top y coordinate.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.ALIGNMENT_TOP)
ALIGNMENT_CENTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ALIGNMENT_CENTER
Aligns layouted shapes according their centers.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.ALIGNMENT_CENTER)
ALIGNMENT_BOTTOM
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ALIGNMENT_BOTTOM
Aligns layouted shapes according their bottom y coordinate.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.ALIGNMENT_BOTTOM)
SHAPE_ALIGNMENT
protected static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) SHAPE_ALIGNMENT
Different ways of aligning shapes after layout.
LAYOUT_LABEL_CONSIDERATION_NONE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LAYOUT_LABEL_CONSIDERATION_NONE
A mode where labels are not considered.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.LAYOUT_LABEL_CONSIDERATION_NONE)
LAYOUT_LABEL_CONSIDERATION_PARTIAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LAYOUT_LABEL_CONSIDERATION_PARTIAL
Partial label consideration mode.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.LAYOUT_LABEL_CONSIDERATION_PARTIAL)
LAYOUT_LABEL_CONSIDERATION_FULL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LAYOUT_LABEL_CONSIDERATION_FULL
Full label consideration mode.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.LAYOUT_LABEL_CONSIDERATION_FULL)
LAYOUT_LABEL_CONSIDERATION
protected static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) LAYOUT_LABEL_CONSIDERATION
Label consideration modes
MAX_INT_VALUE
protected static final int MAX_INT_VALUE
The maximum allowed value for integer fields(e.g minimal node distance, minimal edge distance)
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.MAX_INT_VALUE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractDiagramLayouterOptionsGroup
public AbstractDiagramLayouterOptionsGroup([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [PropertyManager](../../properties/PropertyManager.html) options,
 boolean visible)
 ============ METHOD DETAIL ========== 
Method Details
setDefaultValues
public void setDefaultValues()
Description copied from class: `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html#setDefaultValues())`
Sets default values for the properties contained in this group.
 Overriding classes should set default values to the properties.
Overrides:
`[setDefaultValues](AbstractPropertyOptionsGroup.html#setDefaultValues())` in class `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)`
initCommonDefaultValues
protected void initCommonDefaultValues()
setMoveToFreeSpace
public void setMoveToFreeSpace(boolean b)
Sets status move to free space
Parameters:
`b` - new value
isMoveToFreeSpace
public boolean isMoveToFreeSpace()
Checks Is Move to free space?
Returns:
boolean
getMakePreferredLayoutSize
public boolean getMakePreferredLayoutSize()
Get reset shape size property value
Returns:
b
setMakePreferredLayoutSize
public void setMakePreferredLayoutSize(boolean b)
Set reset shape size property value
Parameters:
`b` - new value
getOptimizeLabelOrientations
public boolean getOptimizeLabelOrientations()
Get value if label orientations should be optimized
Returns:
b
setOptimizeLabelOrientations
public void setOptimizeLabelOrientations(boolean value)
Set reset shape size property value
Parameters:
`value` - new value
getCopy
public [AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html) getCopy()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class AbstractDiagramLayouterOptionsGroup">Class AbstractDiagramLayouterOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="CircularLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">CircularLayouterOptionsGroup</a></code>, <code><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></code>, <code><a href="OrganicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OrganicLayouterOptionsGroup</a></code>, <code><a href="OrganicRouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OrganicRouterOptionsGroup</a></code>, <code><a href="OrthogonalLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OrthogonalLayouterOptionsGroup</a></code>, <code><a href="OrthogonalRouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OrthogonalRouterOptionsGroup</a></code>, <code><a href="TreeLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">TreeLayouterOptionsGroup</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractDiagramLayouterOptionsGroup</span>
<span class="extends-implements">extends <a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></span></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ALIGNMENT_BOTTOM">ALIGNMENT_BOTTOM</a></code></div>
<div class="col-last even-row-color">
<div class="block">Aligns layouted shapes according their bottom y coordinate.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ALIGNMENT_CENTER">ALIGNMENT_CENTER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Aligns layouted shapes according their centers.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ALIGNMENT_TOP">ALIGNMENT_TOP</a></code></div>
<div class="col-last even-row-color">
<div class="block">Aligns layouted shapes according their top y coordinate.</div>
</div>
<div class="col-first odd-row-color"><code>protected static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LAYOUT_LABEL_CONSIDERATION">LAYOUT_LABEL_CONSIDERATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Label consideration modes</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LAYOUT_LABEL_CONSIDERATION_FULL">LAYOUT_LABEL_CONSIDERATION_FULL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Full label consideration mode.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LAYOUT_LABEL_CONSIDERATION_NONE">LAYOUT_LABEL_CONSIDERATION_NONE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A mode where labels are not considered.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LAYOUT_LABEL_CONSIDERATION_PARTIAL">LAYOUT_LABEL_CONSIDERATION_PARTIAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Partial label consideration mode.</div>
</div>
<div class="col-first odd-row-color"><code>protected static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MAX_INT_VALUE">MAX_INT_VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The maximum allowed value for integer fields(e.g minimal node distance, minimal edge distance)</div>
</div>
<div class="col-first even-row-color"><code>protected static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHAPE_ALIGNMENT">SHAPE_ALIGNMENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Different ways of aligning shapes after layout.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.magicdraw.properties.PropertyManager,boolean)">AbstractDiagramLayouterOptionsGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> options,
 boolean visible)</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCopy()">getCopy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMakePreferredLayoutSize()">getMakePreferredLayoutSize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get reset shape size property value</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptimizeLabelOrientations()">getOptimizeLabelOrientations</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get value if label orientations should be optimized</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initCommonDefaultValues()">initCommonDefaultValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMoveToFreeSpace()">isMoveToFreeSpace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks Is Move to free space?</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDefaultValues()">setDefaultValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets default values for the properties contained in this group.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMakePreferredLayoutSize(boolean)">setMakePreferredLayoutSize</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set reset shape size property value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMoveToFreeSpace(boolean)">setMoveToFreeSpace</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets status move to free space</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOptimizeLabelOrientations(boolean)">setOptimizeLabelOrientations</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set reset shape size property value</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></h3>
<code><a href="AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getOptions()">getOptions</a>, <a href="AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)">getProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getVisibleOptions()">getVisibleOptions</a>, <a href="AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)">removeProperty</a>, <a href="AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)">setOptions</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)">setPropertiesInvisible</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean)">setPropertyInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="OptionsGroup.html#getGroupIcon()">getGroupIcon</a>, <a href="OptionsGroup.html#getIcon()">getIcon</a>, <a href="OptionsGroup.html#getName()">getName</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="ALIGNMENT_TOP">
<h3>ALIGNMENT_TOP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ALIGNMENT_TOP</span></div>
<div class="block">Aligns layouted shapes according their top y coordinate.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.ALIGNMENT_TOP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ALIGNMENT_CENTER">
<h3>ALIGNMENT_CENTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ALIGNMENT_CENTER</span></div>
<div class="block">Aligns layouted shapes according their centers.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.ALIGNMENT_CENTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ALIGNMENT_BOTTOM">
<h3>ALIGNMENT_BOTTOM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ALIGNMENT_BOTTOM</span></div>
<div class="block">Aligns layouted shapes according their bottom y coordinate.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.ALIGNMENT_BOTTOM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHAPE_ALIGNMENT">
<h3>SHAPE_ALIGNMENT</h3>
<div class="member-signature"><span class="modifiers">protected static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">SHAPE_ALIGNMENT</span></div>
<div class="block">Different ways of aligning shapes after layout.</div>
</section>
</li>
<li>
<section class="detail" id="LAYOUT_LABEL_CONSIDERATION_NONE">
<h3>LAYOUT_LABEL_CONSIDERATION_NONE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LAYOUT_LABEL_CONSIDERATION_NONE</span></div>
<div class="block">A mode where labels are not considered.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.LAYOUT_LABEL_CONSIDERATION_NONE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LAYOUT_LABEL_CONSIDERATION_PARTIAL">
<h3>LAYOUT_LABEL_CONSIDERATION_PARTIAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LAYOUT_LABEL_CONSIDERATION_PARTIAL</span></div>
<div class="block">Partial label consideration mode.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.LAYOUT_LABEL_CONSIDERATION_PARTIAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LAYOUT_LABEL_CONSIDERATION_FULL">
<h3>LAYOUT_LABEL_CONSIDERATION_FULL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LAYOUT_LABEL_CONSIDERATION_FULL</span></div>
<div class="block">Full label consideration mode.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.LAYOUT_LABEL_CONSIDERATION_FULL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LAYOUT_LABEL_CONSIDERATION">
<h3>LAYOUT_LABEL_CONSIDERATION</h3>
<div class="member-signature"><span class="modifiers">protected static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">LAYOUT_LABEL_CONSIDERATION</span></div>
<div class="block">Label consideration modes</div>
</section>
</li>
<li>
<section class="detail" id="MAX_INT_VALUE">
<h3>MAX_INT_VALUE</h3>
<div class="member-signature"><span class="modifiers">protected static final</span> <span class="return-type">int</span> <span class="element-name">MAX_INT_VALUE</span></div>
<div class="block">The maximum allowed value for integer fields(e.g minimal node distance, minimal edge distance)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup.MAX_INT_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.magicdraw.properties.PropertyManager,boolean)">
<h3>AbstractDiagramLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractDiagramLayouterOptionsGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> options,
 boolean visible)</span></div>
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
<section class="detail" id="setDefaultValues()">
<h3>setDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDefaultValues</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractPropertyOptionsGroup.html#setDefaultValues()">AbstractPropertyOptionsGroup</a></code></span></div>
<div class="block">Sets default values for the properties contained in this group.
 Overriding classes should set default values to the properties.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractPropertyOptionsGroup.html#setDefaultValues()">setDefaultValues</a></code> in class <code><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initCommonDefaultValues()">
<h3>initCommonDefaultValues</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">initCommonDefaultValues</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setMoveToFreeSpace(boolean)">
<h3>setMoveToFreeSpace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMoveToFreeSpace</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Sets status move to free space</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - new value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMoveToFreeSpace()">
<h3>isMoveToFreeSpace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMoveToFreeSpace</span>()</div>
<div class="block">Checks Is Move to free space?</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMakePreferredLayoutSize()">
<h3>getMakePreferredLayoutSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getMakePreferredLayoutSize</span>()</div>
<div class="block">Get reset shape size property value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>b</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMakePreferredLayoutSize(boolean)">
<h3>setMakePreferredLayoutSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMakePreferredLayoutSize</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set reset shape size property value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - new value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOptimizeLabelOrientations()">
<h3>getOptimizeLabelOrientations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getOptimizeLabelOrientations</span>()</div>
<div class="block">Get value if label orientations should be optimized</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>b</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOptimizeLabelOrientations(boolean)">
<h3>setOptimizeLabelOrientations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOptimizeLabelOrientations</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Set reset shape size property value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - new value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCopy()">
<h3>getCopy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></span> <span class="element-name">getCopy</span>()</div>
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
