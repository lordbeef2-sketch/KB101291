# JAVA OPENAPI: OrthogonalLayouterOptionsGroup (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/core/options/OrthogonalLayouterOptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/OrthogonalLayouterOptionsGroup.html`
- source_sha256: `5c687710cec0e95796b1ae8b0a63a787a4a4038b7ecfc705ff30ced2b45eee76`
- captured_utc: `2026-07-14T16:51:15.623128+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class OrthogonalLayouterOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
com.nomagic.magicdraw.core.options.OrthogonalLayouterOptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classOrthogonalLayouterOptionsGroup
extends [AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)

Organic Layouter options group.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ID](#ID)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LAYOUT_STYLE_NORMAL](#LAYOUT_STYLE_NORMAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LAYOUT_STYLE_NORMAL_TREE](#LAYOUT_STYLE_NORMAL_TREE)`
Fields inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[ALIGNMENT_BOTTOM](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_BOTTOM), [ALIGNMENT_CENTER](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_CENTER), [ALIGNMENT_TOP](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_TOP), [LAYOUT_LABEL_CONSIDERATION](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION), [LAYOUT_LABEL_CONSIDERATION_FULL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_FULL), [LAYOUT_LABEL_CONSIDERATION_NONE](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_NONE), [LAYOUT_LABEL_CONSIDERATION_PARTIAL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_PARTIAL), [MAX_INT_VALUE](AbstractDiagramLayouterOptionsGroup.html#MAX_INT_VALUE), [SHAPE_ALIGNMENT](AbstractDiagramLayouterOptionsGroup.html#SHAPE_ALIGNMENT)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[OrthogonalLayouterOptionsGroup](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addProperty](#addProperty(com.nomagic.magicdraw.properties.Property))([Property](../../properties/Property.html) property)`
Adds property to this group.
`boolean`
`[getCrossingPostprocessing](#getCrossingPostprocessing())()`
Get Crossing Post precessing property value.
`int`
`[getGrid](#getGrid())()`
Get Grid property value.
`double`
`[getGroupLayoutQuality](#getGroupLayoutQuality())()`
Get the desired layout quality.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLayoutStyle](#getLayoutStyle())()`
Get String representation of layout style.
`boolean`
`[getLinkLengthReduction](#getLinkLengthReduction())()`
Get Link Length Reduction Property value.
`boolean`
`[getUseExistingDrawingAsSketch](#getUseExistingDrawingAsSketch())()`
Get Use Existing Drawing As Sketch property value..
`boolean`
`[getUseRandomization](#getUseRandomization())()`
Get use Randomization property value.
`protected void`
`[initCommonDefaultValues](#initCommonDefaultValues())()`

`boolean`
`[isLayoutOnlyTopLevel](#isLayoutOnlyTopLevel())()`
Check Layout Only Top Level property value.
`void`
`[setCrossingPostprocessing](#setCrossingPostprocessing(boolean))(boolean b)`
Set Crossing Post precessing property value.
`void`
`[setGrid](#setGrid(int))(int d)`
Set Grid property value.
`void`
`[setGroupLayoutQuality](#setGroupLayoutQuality(double))(double d)`
Set the desired layout quality.
`void`
`[setLayoutOnlyTopLevel](#setLayoutOnlyTopLevel(boolean))(boolean b)`
Set Layout Only Top Level property value in order to keeps the relative position of symbols inside packages and performs the top level layout.
`void`
`[setLayoutStyle](#setLayoutStyle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) style)`
Set Layout style
`void`
`[setLinkLengthReduction](#setLinkLengthReduction(boolean))(boolean b)`
Set Link Length Reduction Property value.
`void`
`[setUseExistingDrawingAsSketch](#setUseExistingDrawingAsSketch(boolean))(boolean b)`
Set Use Existing Drawing As Sketch property value..
`void`
`[setUseRandomization](#setUseRandomization(boolean))(boolean b)`
Set use Randomization property value.
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[getCopy](AbstractDiagramLayouterOptionsGroup.html#getCopy()), [getMakePreferredLayoutSize](AbstractDiagramLayouterOptionsGroup.html#getMakePreferredLayoutSize()), [getOptimizeLabelOrientations](AbstractDiagramLayouterOptionsGroup.html#getOptimizeLabelOrientations()), [isMoveToFreeSpace](AbstractDiagramLayouterOptionsGroup.html#isMoveToFreeSpace()), [setDefaultValues](AbstractDiagramLayouterOptionsGroup.html#setDefaultValues()), [setMakePreferredLayoutSize](AbstractDiagramLayouterOptionsGroup.html#setMakePreferredLayoutSize(boolean)), [setMoveToFreeSpace](AbstractDiagramLayouterOptionsGroup.html#setMoveToFreeSpace(boolean)), [setOptimizeLabelOrientations](AbstractDiagramLayouterOptionsGroup.html#setOptimizeLabelOrientations(boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
`[addInvisibleProperty](AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)), [getOptions](AbstractPropertyOptionsGroup.html#getOptions()), [getProperty](AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)), [getVisibleOptions](AbstractPropertyOptionsGroup.html#getVisibleOptions()), [removeProperty](AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)), [setOptions](AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)), [setPropertiesInvisible](AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)), [setPropertyInvisible](AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](OptionsGroup.html)
`[getGroupIcon](OptionsGroup.html#getGroupIcon()), [getIcon](OptionsGroup.html#getIcon()), [getName](OptionsGroup.html#getName())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ID
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ID
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.OrthogonalLayouterOptionsGroup.ID)
LAYOUT_STYLE_NORMAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LAYOUT_STYLE_NORMAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.OrthogonalLayouterOptionsGroup.LAYOUT_STYLE_NORMAL)
LAYOUT_STYLE_NORMAL_TREE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LAYOUT_STYLE_NORMAL_TREE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.OrthogonalLayouterOptionsGroup.LAYOUT_STYLE_NORMAL_TREE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
OrthogonalLayouterOptionsGroup
public OrthogonalLayouterOptionsGroup()
 ============ METHOD DETAIL ========== 
Method Details
initCommonDefaultValues
protected void initCommonDefaultValues()
Overrides:
`[initCommonDefaultValues](AbstractDiagramLayouterOptionsGroup.html#initCommonDefaultValues())` in class `[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)`
getLayoutStyle
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLayoutStyle()
Get String representation of layout style.
Returns:
string.
setLayoutStyle
public void setLayoutStyle([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) style)
Set Layout style
Parameters:
`style` - the given layout style.
setLinkLengthReduction
public void setLinkLengthReduction(boolean b)
Set Link Length Reduction Property value.
 If true the overall path lengths will be reduced. The cost for the reduction is an increased execution time of the layouter.
Parameters:
`b` - boolean
getLinkLengthReduction
public boolean getLinkLengthReduction()
Get Link Length Reduction Property value.
 If true the overall path lengths will be reduced. The cost for the reduction is an increased execution time of the layouter.
Returns:
boolean
setUseExistingDrawingAsSketch
public void setUseExistingDrawingAsSketch(boolean b)
Set Use Existing Drawing As Sketch property value..
 The layouter tries to "orthogonalize" the given sketch by interpreting it and without making too many modifications in respect to the original drawing.
Parameters:
`b` - true to use existing drawing as a sketch, false to layout from scratch
getUseExistingDrawingAsSketch
public boolean getUseExistingDrawingAsSketch()
Get Use Existing Drawing As Sketch property value..
 The layouter tries to "orthogonalize" the given sketch by interpreting it and without making too many modifications in respect to the original drawing.
Returns:
boolean
setCrossingPostprocessing
public void setCrossingPostprocessing(boolean b)
Set Crossing Post precessing property value.
 If true the overall number of path crossings will be reduced. The cost for the reduction is increased execution time of the layouter.
Parameters:
`b` - boolean
getCrossingPostprocessing
public boolean getCrossingPostprocessing()
Get Crossing Post precessing property value.
 If true the overall number of path crossings will be reduced. The cost for the reduction is increased execution time of the layouter.
Returns:
true if cross post processing is enabled, false otherwise
setUseRandomization
public void setUseRandomization(boolean b)
Set use Randomization property value.
 If enabled the overall layout quality will increase with high probability. The cost for this layout optimization is increased execution time and non-deterministic behavior of the layouter.
Parameters:
`b` - true to use randomization, false otherwise
getUseRandomization
public boolean getUseRandomization()
Get use Randomization property value.
 If enabled the overall layout quality will increase with high probability. The cost for this layout optimization is increased execution time and non-deterministic behavior of the layouter.
Returns:
true if use randomization is enabled, false otherwise
getGroupLayoutQuality
public double getGroupLayoutQuality()
Get the desired layout quality. Higher values result in less connection crossings and smaller layout area, but also increased computation time.
Returns:
the value of group layout quality
setGroupLayoutQuality
public void setGroupLayoutQuality(double d)
Set the desired layout quality. Higher values result in less connection crossings and smaller layout area, but also increased computation time.
Parameters:
`d` - double.
setLayoutOnlyTopLevel
public void setLayoutOnlyTopLevel(boolean b)
Set Layout Only Top Level property value in order to keeps the relative position of symbols inside packages and performs the top level layout.
Parameters:
`b` - boolean.
isLayoutOnlyTopLevel
public boolean isLayoutOnlyTopLevel()
Check Layout Only Top Level property value. It indicates position of symbols inside packages is on the top level layout.
Returns:
boolean
addProperty
public void addProperty([Property](../../properties/Property.html) property)
Description copied from class: `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property))`
Adds property to this group. DescriptionID will be reset. To add property with description use
 [`AbstractPropertyOptionsGroup.addProperty(Property, String)`](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)) method.
Overrides:
`[addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property))` in class `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)`
Parameters:
`property` - property to be added.
getGrid
public int getGrid()
Get Grid property value.
 This property defines the virtual grid spacing used by the layouter. Each shape center point lies on a grid point.
Returns:
int
setGrid
public void setGrid(int d)
Set Grid property value.
 This property defines the virtual grid spacing used by the layouter. Each shape center point lies on a grid point.
Parameters:
`d` - int

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class OrthogonalLayouterOptionsGroup">Class OrthogonalLayouterOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance"><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.OrthogonalLayouterOptionsGroup</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">OrthogonalLayouterOptionsGroup</span>
<span class="extends-implements">extends <a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></span></div>
<div class="block">Organic Layouter options group.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ID">ID</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LAYOUT_STYLE_NORMAL">LAYOUT_STYLE_NORMAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LAYOUT_STYLE_NORMAL_TREE">LAYOUT_STYLE_NORMAL_TREE</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></h3>
<code><a href="AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_BOTTOM">ALIGNMENT_BOTTOM</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_CENTER">ALIGNMENT_CENTER</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_TOP">ALIGNMENT_TOP</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION">LAYOUT_LABEL_CONSIDERATION</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_FULL">LAYOUT_LABEL_CONSIDERATION_FULL</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_NONE">LAYOUT_LABEL_CONSIDERATION_NONE</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_PARTIAL">LAYOUT_LABEL_CONSIDERATION_PARTIAL</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#MAX_INT_VALUE">MAX_INT_VALUE</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#SHAPE_ALIGNMENT">SHAPE_ALIGNMENT</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">OrthogonalLayouterOptionsGroup</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds property to this group.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCrossingPostprocessing()">getCrossingPostprocessing</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Crossing Post precessing property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGrid()">getGrid</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Grid property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroupLayoutQuality()">getGroupLayoutQuality</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the desired layout quality.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLayoutStyle()">getLayoutStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get String representation of layout style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLinkLengthReduction()">getLinkLengthReduction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Link Length Reduction Property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUseExistingDrawingAsSketch()">getUseExistingDrawingAsSketch</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Use Existing Drawing As Sketch property value..</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUseRandomization()">getUseRandomization</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get use Randomization property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initCommonDefaultValues()">initCommonDefaultValues</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLayoutOnlyTopLevel()">isLayoutOnlyTopLevel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check Layout Only Top Level property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCrossingPostprocessing(boolean)">setCrossingPostprocessing</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Crossing Post precessing property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setGrid(int)">setGrid</a><wbr/>(int d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Grid property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setGroupLayoutQuality(double)">setGroupLayoutQuality</a><wbr/>(double d)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the desired layout quality.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayoutOnlyTopLevel(boolean)">setLayoutOnlyTopLevel</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Layout Only Top Level property value in order to keeps the relative position of symbols inside packages and performs the top level layout.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayoutStyle(java.lang.String)">setLayoutStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Layout style</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLinkLengthReduction(boolean)">setLinkLengthReduction</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Link Length Reduction Property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseExistingDrawingAsSketch(boolean)">setUseExistingDrawingAsSketch</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Use Existing Drawing As Sketch property value..</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseRandomization(boolean)">setUseRandomization</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set use Randomization property value.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></h3>
<code><a href="AbstractDiagramLayouterOptionsGroup.html#getCopy()">getCopy</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#getMakePreferredLayoutSize()">getMakePreferredLayoutSize</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#getOptimizeLabelOrientations()">getOptimizeLabelOrientations</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#isMoveToFreeSpace()">isMoveToFreeSpace</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setDefaultValues()">setDefaultValues</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setMakePreferredLayoutSize(boolean)">setMakePreferredLayoutSize</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setMoveToFreeSpace(boolean)">setMoveToFreeSpace</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setOptimizeLabelOrientations(boolean)">setOptimizeLabelOrientations</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></h3>
<code><a href="AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getOptions()">getOptions</a>, <a href="AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)">getProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getVisibleOptions()">getVisibleOptions</a>, <a href="AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)">removeProperty</a>, <a href="AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)">setOptions</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)">setPropertiesInvisible</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean)">setPropertyInvisible</a></code></div>
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
<section class="detail" id="ID">
<h3>ID</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ID</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.OrthogonalLayouterOptionsGroup.ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LAYOUT_STYLE_NORMAL">
<h3>LAYOUT_STYLE_NORMAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LAYOUT_STYLE_NORMAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.OrthogonalLayouterOptionsGroup.LAYOUT_STYLE_NORMAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LAYOUT_STYLE_NORMAL_TREE">
<h3>LAYOUT_STYLE_NORMAL_TREE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LAYOUT_STYLE_NORMAL_TREE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.OrthogonalLayouterOptionsGroup.LAYOUT_STYLE_NORMAL_TREE">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;()">
<h3>OrthogonalLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OrthogonalLayouterOptionsGroup</span>()</div>
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
<section class="detail" id="initCommonDefaultValues()">
<h3>initCommonDefaultValues</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">initCommonDefaultValues</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouterOptionsGroup.html#initCommonDefaultValues()">initCommonDefaultValues</a></code> in class <code><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLayoutStyle()">
<h3>getLayoutStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLayoutStyle</span>()</div>
<div class="block">Get String representation of layout style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLayoutStyle(java.lang.String)">
<h3>setLayoutStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayoutStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> style)</span></div>
<div class="block">Set Layout style</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - the given layout style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLinkLengthReduction(boolean)">
<h3>setLinkLengthReduction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLinkLengthReduction</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Link Length Reduction Property value.
 If true the overall path lengths will be reduced. The cost for the reduction is an increased execution time of the layouter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLinkLengthReduction()">
<h3>getLinkLengthReduction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getLinkLengthReduction</span>()</div>
<div class="block">Get Link Length Reduction Property value.
 If true the overall path lengths will be reduced. The cost for the reduction is an increased execution time of the layouter.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseExistingDrawingAsSketch(boolean)">
<h3>setUseExistingDrawingAsSketch</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseExistingDrawingAsSketch</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Use Existing Drawing As Sketch property value..
 The layouter tries to "orthogonalize" the given sketch by interpreting it and without making too many modifications in respect to the original drawing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - true to use existing drawing as a sketch, false to layout from scratch</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUseExistingDrawingAsSketch()">
<h3>getUseExistingDrawingAsSketch</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getUseExistingDrawingAsSketch</span>()</div>
<div class="block">Get Use Existing Drawing As Sketch property value..
 The layouter tries to "orthogonalize" the given sketch by interpreting it and without making too many modifications in respect to the original drawing.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCrossingPostprocessing(boolean)">
<h3>setCrossingPostprocessing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCrossingPostprocessing</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Crossing Post precessing property value.
 If true the overall number of path crossings will be reduced. The cost for the reduction is increased execution time of the layouter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCrossingPostprocessing()">
<h3>getCrossingPostprocessing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getCrossingPostprocessing</span>()</div>
<div class="block">Get Crossing Post precessing property value.
 If true the overall number of path crossings will be reduced. The cost for the reduction is increased execution time of the layouter.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if cross post processing is enabled, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseRandomization(boolean)">
<h3>setUseRandomization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseRandomization</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set use Randomization property value.
 If enabled the overall layout quality will increase with high probability. The cost for this layout optimization is increased execution time and non-deterministic behavior of the layouter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - true to use randomization, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUseRandomization()">
<h3>getUseRandomization</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getUseRandomization</span>()</div>
<div class="block">Get use Randomization property value.
 If enabled the overall layout quality will increase with high probability. The cost for this layout optimization is increased execution time and non-deterministic behavior of the layouter.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if use randomization is enabled, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGroupLayoutQuality()">
<h3>getGroupLayoutQuality</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getGroupLayoutQuality</span>()</div>
<div class="block">Get the desired layout quality. Higher values result in less connection crossings and smaller layout area, but also increased computation time.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of group layout quality</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGroupLayoutQuality(double)">
<h3>setGroupLayoutQuality</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGroupLayoutQuality</span><wbr/><span class="parameters">(double d)</span></div>
<div class="block">Set the desired layout quality. Higher values result in less connection crossings and smaller layout area, but also increased computation time.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - double.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLayoutOnlyTopLevel(boolean)">
<h3>setLayoutOnlyTopLevel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayoutOnlyTopLevel</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Layout Only Top Level property value in order to keeps the relative position of symbols inside packages and performs the top level layout.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLayoutOnlyTopLevel()">
<h3>isLayoutOnlyTopLevel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLayoutOnlyTopLevel</span>()</div>
<div class="block">Check Layout Only Top Level property value. It indicates position of symbols inside packages is on the top level layout.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProperty(com.nomagic.magicdraw.properties.Property)">
<h3>addProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProperty</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">AbstractPropertyOptionsGroup</a></code></span></div>
<div class="block">Adds property to this group. DescriptionID will be reset. To add property with description use
 <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)"><code>AbstractPropertyOptionsGroup.addProperty(Property, String)</code></a> method.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a></code> in class <code><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></code></dd>
<dt>Parameters:</dt>
<dd><code>property</code> - property to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGrid()">
<h3>getGrid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getGrid</span>()</div>
<div class="block">Get Grid property value.
 This property defines the virtual grid spacing used by the layouter. Each shape center point lies on a grid point.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGrid(int)">
<h3>setGrid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGrid</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set Grid property value.
 This property defines the virtual grid spacing used by the layouter. Each shape center point lies on a grid point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - int</dd>
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
