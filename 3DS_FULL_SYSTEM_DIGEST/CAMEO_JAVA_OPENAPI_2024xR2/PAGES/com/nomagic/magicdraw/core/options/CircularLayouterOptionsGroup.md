# JAVA OPENAPI: CircularLayouterOptionsGroup (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/core/options/CircularLayouterOptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/CircularLayouterOptionsGroup.html`
- source_sha256: `fe8708aadf16ee58e12849644061b812590d13604d4928a723b9e9b56fdc4940`
- captured_utc: `2026-07-14T16:55:11.786970+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class CircularLayouterOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
com.nomagic.magicdraw.core.options.CircularLayouterOptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classCircularLayouterOptionsGroup
extends [AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)

Compact. Each group will consist of shapes that are reachable by two link disjoint paths. Shapes that belong to more than one group will be assigned exclusively to one group.
 Isolated. Each group will consist of shapes that are reachable by two path disjoint paths.
 All shapes belonging to more than one group will be assigned to an isolated group.
 Single Cycle. All shapes will be arranged on a single circle.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COMPACT](#COMPACT)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ID](#ID)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ISOLATED](#ISOLATED)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SINGLE_CYCLE](#SINGLE_CYCLE)`
Fields inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[ALIGNMENT_BOTTOM](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_BOTTOM), [ALIGNMENT_CENTER](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_CENTER), [ALIGNMENT_TOP](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_TOP), [LAYOUT_LABEL_CONSIDERATION](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION), [LAYOUT_LABEL_CONSIDERATION_FULL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_FULL), [LAYOUT_LABEL_CONSIDERATION_NONE](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_NONE), [LAYOUT_LABEL_CONSIDERATION_PARTIAL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_PARTIAL), [MAX_INT_VALUE](AbstractDiagramLayouterOptionsGroup.html#MAX_INT_VALUE), [SHAPE_ALIGNMENT](AbstractDiagramLayouterOptionsGroup.html#SHAPE_ALIGNMENT)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CircularLayouterOptionsGroup](#%3Cinit%3E())()`
Constructs CircularLayouterOptionsGroup
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
`[getAllowOverlaps](#getAllowOverlaps())()`

`boolean`
`[getAutoCircleRadius](#getAutoCircleRadius())()`
Get the radius of each circle in the layout automatically.
`double`
`[getCompactnessFactor](#getCompactnessFactor())()`
Get compactness factor.
`int`
`[getFixedCircleRadius](#getFixedCircleRadius())()`
Get the fixed radius for all circles in the resulting layout.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLayoutStyle](#getLayoutStyle())()`
Gets the string representation of layout style.
`int`
`[getMaximalDeviationAngle](#getMaximalDeviationAngle())()`
Get the bigger the chosen value, the more compact the resulting layout.
`int`
`[getMinimalLinkLength](#getMinimalLinkLength())()`
Get the minimal length of a path that connects two shapes that lie on separate circles.
`int`
`[getMinimalShapeDistance](#getMinimalShapeDistance())()`
Get the minimal distance between borders of two adjacent shapes on a common circle.
`int`
`[getPreferredChildWedge](#getPreferredChildWedge())()`
Get the angular range of the sector that will be reserved for children of a shape.
`protected void`
`[initCommonDefaultValues](#initCommonDefaultValues())()`

`void`
`[setAllowOverlaps](#setAllowOverlaps(boolean))(boolean b)`
Set allow overlap.
`void`
`[setAutoCircleRadius](#setAutoCircleRadius(boolean))(boolean b)`
Set the radius of each circle in the layout automatically.
`void`
`[setCompactnessFactor](#setCompactnessFactor(double))(double d)`
Set compactness factor.
`void`
`[setFixedCircleRadius](#setFixedCircleRadius(int))(int d)`
Set the fixed radius for all circles in the resulting layout.
`void`
`[setLayoutStyle](#setLayoutStyle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)`
Set layout style.
`void`
`[setMaximalDeviationAngle](#setMaximalDeviationAngle(int))(int d)`
Set the bigger the chosen value, the more compact the resulting layout.
`void`
`[setMinimalLinkLength](#setMinimalLinkLength(int))(int d)`
Set the minimal length of a path that connects two shapes that lie on separate circles.
`void`
`[setMinimalShapeDistance](#setMinimalShapeDistance(int))(int d)`
Set the minimal distance between borders of two adjacent shapes on a common circle.
`void`
`[setPreferredChildWedge](#setPreferredChildWedge(int))(int d)`
Set the angular range of the sector that will be reserved for children of a shape.
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
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.CircularLayouterOptionsGroup.ID)
COMPACT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COMPACT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.CircularLayouterOptionsGroup.COMPACT)
ISOLATED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ISOLATED
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.CircularLayouterOptionsGroup.ISOLATED)
SINGLE_CYCLE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SINGLE_CYCLE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.CircularLayouterOptionsGroup.SINGLE_CYCLE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CircularLayouterOptionsGroup
public CircularLayouterOptionsGroup()
Constructs CircularLayouterOptionsGroup
 ============ METHOD DETAIL ========== 
Method Details
initCommonDefaultValues
protected void initCommonDefaultValues()
Overrides:
`[initCommonDefaultValues](AbstractDiagramLayouterOptionsGroup.html#initCommonDefaultValues())` in class `[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)`
getLayoutStyle
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLayoutStyle()
Gets the string representation of layout style.
Returns:
Layout style.
setLayoutStyle
public void setLayoutStyle([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)
Set layout style.
Parameters:
`s` - Style value.
getMinimalShapeDistance
public int getMinimalShapeDistance()
Get the minimal distance between borders of two adjacent shapes on a common circle.
Returns:
int.
setMinimalShapeDistance
public void setMinimalShapeDistance(int d)
Set the minimal distance between borders of two adjacent shapes on a common circle.
Parameters:
`d` - value.
setAutoCircleRadius
public void setAutoCircleRadius(boolean b)
Set the radius of each circle in the layout automatically.
 An automatically chosen radius is usually the smallest possible radius that obeys Minimal Node Distance.
Parameters:
`b` - boolean value.
getAutoCircleRadius
public boolean getAutoCircleRadius()
Get the radius of each circle in the layout automatically.
 An automatically chosen radius is usually the smallest possible radius that obeys Minimal Node Distance.
Returns:
boolean value.
getFixedCircleRadius
public int getFixedCircleRadius()
Get the fixed radius for all circles in the resulting layout. Minimal Node Distance will be ignored in this case.
Returns:
int value.
setFixedCircleRadius
public void setFixedCircleRadius(int d)
Set the fixed radius for all circles in the resulting layout. Minimal Node Distance will be ignored in this case.
Parameters:
`d` - value.
getPreferredChildWedge
public int getPreferredChildWedge()
Get the angular range of the sector that will be reserved for children of a shape. The remaining angular range will be automatically used to accommodate the edge that connects to the root node.
Returns:
int.
setPreferredChildWedge
public void setPreferredChildWedge(int d)
Set the angular range of the sector that will be reserved for children of a shape. The remaining angular range will be automatically used to accommodate the edge that connects to the root node.
Parameters:
`d` - value.
getMinimalLinkLength
public int getMinimalLinkLength()
Get the minimal length of a path that connects two shapes that lie on separate circles. The smaller the chosen value, the more compact the resulting layout.
Returns:
int value.
setMinimalLinkLength
public void setMinimalLinkLength(int d)
Set the minimal length of a path that connects two shapes that lie on separate circles. The smaller the chosen value, the more compact the resulting layout.
Parameters:
`d` - value.
getMaximalDeviationAngle
public int getMaximalDeviationAngle()
Get the bigger the chosen value, the more compact the resulting layout. If a value smaller than 90 degrees, the tree-edges might cross through the circularly arranged groups of shapes.
Returns:
value.
setMaximalDeviationAngle
public void setMaximalDeviationAngle(int d)
Set the bigger the chosen value, the more compact the resulting layout. If a value smaller than 90 degrees, the tree-edges might cross through the circularly arranged groups of shapes.
Parameters:
`d` - value.
getCompactnessFactor
public double getCompactnessFactor()
Get compactness factor.
 Adjusting this value can lead to a variety of differing layouts. For small values, the resulting layout will use much space and shapes tend to be far away from each other. Values around 0.5 lead to evenly distributed shapes, whereas values near 1.0 produce highly compact layouts.
Returns:
the compactness factor
setCompactnessFactor
public void setCompactnessFactor(double d)
Set compactness factor.
Parameters:
`d` - value.
setAllowOverlaps
public void setAllowOverlaps(boolean b)
Set allow overlap. Can result in more compact layout
Parameters:
`b` - value.
getAllowOverlaps
public boolean getAllowOverlaps()
addProperty
public void addProperty([Property](../../properties/Property.html) property)
Description copied from class: `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property))`
Adds property to this group. DescriptionID will be reset. To add property with description use
 [`AbstractPropertyOptionsGroup.addProperty(Property, String)`](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)) method.
Overrides:
`[addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property))` in class `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)`
Parameters:
`property` - property to be added.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class CircularLayouterOptionsGroup">Class CircularLayouterOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance"><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.CircularLayouterOptionsGroup</div>
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
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CircularLayouterOptionsGroup</span>
<span class="extends-implements">extends <a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></span></div>
<div class="block">Compact. Each group will consist of shapes that are reachable by two link disjoint paths. Shapes that belong to more than one group will be assigned exclusively to one group.
 Isolated. Each group will consist of shapes that are reachable by two path disjoint paths.
 All shapes belonging to more than one group will be assigned to an isolated group.
 Single Cycle. All shapes will be arranged on a single circle.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COMPACT">COMPACT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ID">ID</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ISOLATED">ISOLATED</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SINGLE_CYCLE">SINGLE_CYCLE</a></code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CircularLayouterOptionsGroup</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs CircularLayouterOptionsGroup</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds property to this group.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllowOverlaps()">getAllowOverlaps</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAutoCircleRadius()">getAutoCircleRadius</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the radius of each circle in the layout automatically.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCompactnessFactor()">getCompactnessFactor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get compactness factor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFixedCircleRadius()">getFixedCircleRadius</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the fixed radius for all circles in the resulting layout.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLayoutStyle()">getLayoutStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the string representation of layout style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMaximalDeviationAngle()">getMaximalDeviationAngle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the bigger the chosen value, the more compact the resulting layout.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimalLinkLength()">getMinimalLinkLength</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the minimal length of a path that connects two shapes that lie on separate circles.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimalShapeDistance()">getMinimalShapeDistance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the minimal distance between borders of two adjacent shapes on a common circle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreferredChildWedge()">getPreferredChildWedge</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the angular range of the sector that will be reserved for children of a shape.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initCommonDefaultValues()">initCommonDefaultValues</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAllowOverlaps(boolean)">setAllowOverlaps</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set allow overlap.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoCircleRadius(boolean)">setAutoCircleRadius</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the radius of each circle in the layout automatically.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCompactnessFactor(double)">setCompactnessFactor</a><wbr/>(double d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set compactness factor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFixedCircleRadius(int)">setFixedCircleRadius</a><wbr/>(int d)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the fixed radius for all circles in the resulting layout.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayoutStyle(java.lang.String)">setLayoutStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set layout style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMaximalDeviationAngle(int)">setMaximalDeviationAngle</a><wbr/>(int d)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the bigger the chosen value, the more compact the resulting layout.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMinimalLinkLength(int)">setMinimalLinkLength</a><wbr/>(int d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the minimal length of a path that connects two shapes that lie on separate circles.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMinimalShapeDistance(int)">setMinimalShapeDistance</a><wbr/>(int d)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the minimal distance between borders of two adjacent shapes on a common circle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPreferredChildWedge(int)">setPreferredChildWedge</a><wbr/>(int d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the angular range of the sector that will be reserved for children of a shape.</div>
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
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.CircularLayouterOptionsGroup.ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMPACT">
<h3>COMPACT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COMPACT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.CircularLayouterOptionsGroup.COMPACT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ISOLATED">
<h3>ISOLATED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ISOLATED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.CircularLayouterOptionsGroup.ISOLATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SINGLE_CYCLE">
<h3>SINGLE_CYCLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SINGLE_CYCLE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.CircularLayouterOptionsGroup.SINGLE_CYCLE">Constant Field Values</a></li>
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
<h3>CircularLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CircularLayouterOptionsGroup</span>()</div>
<div class="block">Constructs CircularLayouterOptionsGroup</div>
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
<div class="block">Gets the string representation of layout style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Layout style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLayoutStyle(java.lang.String)">
<h3>setLayoutStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayoutStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Set layout style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - Style value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMinimalShapeDistance()">
<h3>getMinimalShapeDistance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMinimalShapeDistance</span>()</div>
<div class="block">Get the minimal distance between borders of two adjacent shapes on a common circle.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMinimalShapeDistance(int)">
<h3>setMinimalShapeDistance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMinimalShapeDistance</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set the minimal distance between borders of two adjacent shapes on a common circle.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAutoCircleRadius(boolean)">
<h3>setAutoCircleRadius</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutoCircleRadius</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set the radius of each circle in the layout automatically.
 An automatically chosen radius is usually the smallest possible radius that obeys Minimal Node Distance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAutoCircleRadius()">
<h3>getAutoCircleRadius</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getAutoCircleRadius</span>()</div>
<div class="block">Get the radius of each circle in the layout automatically.
 An automatically chosen radius is usually the smallest possible radius that obeys Minimal Node Distance.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFixedCircleRadius()">
<h3>getFixedCircleRadius</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getFixedCircleRadius</span>()</div>
<div class="block">Get the fixed radius for all circles in the resulting layout. Minimal Node Distance will be ignored in this case.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFixedCircleRadius(int)">
<h3>setFixedCircleRadius</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFixedCircleRadius</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set the fixed radius for all circles in the resulting layout. Minimal Node Distance will be ignored in this case.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreferredChildWedge()">
<h3>getPreferredChildWedge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPreferredChildWedge</span>()</div>
<div class="block">Get the angular range of the sector that will be reserved for children of a shape. The remaining angular range will be automatically used to accommodate the edge that connects to the root node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPreferredChildWedge(int)">
<h3>setPreferredChildWedge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPreferredChildWedge</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set the angular range of the sector that will be reserved for children of a shape. The remaining angular range will be automatically used to accommodate the edge that connects to the root node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMinimalLinkLength()">
<h3>getMinimalLinkLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMinimalLinkLength</span>()</div>
<div class="block">Get the minimal length of a path that connects two shapes that lie on separate circles. The smaller the chosen value, the more compact the resulting layout.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMinimalLinkLength(int)">
<h3>setMinimalLinkLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMinimalLinkLength</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set the minimal length of a path that connects two shapes that lie on separate circles. The smaller the chosen value, the more compact the resulting layout.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMaximalDeviationAngle()">
<h3>getMaximalDeviationAngle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMaximalDeviationAngle</span>()</div>
<div class="block">Get the bigger the chosen value, the more compact the resulting layout. If a value smaller than 90 degrees, the tree-edges might cross through the circularly arranged groups of shapes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMaximalDeviationAngle(int)">
<h3>setMaximalDeviationAngle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMaximalDeviationAngle</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set the bigger the chosen value, the more compact the resulting layout. If a value smaller than 90 degrees, the tree-edges might cross through the circularly arranged groups of shapes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCompactnessFactor()">
<h3>getCompactnessFactor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getCompactnessFactor</span>()</div>
<div class="block">Get compactness factor.
 Adjusting this value can lead to a variety of differing layouts. For small values, the resulting layout will use much space and shapes tend to be far away from each other. Values around 0.5 lead to evenly distributed shapes, whereas values near 1.0 produce highly compact layouts.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the compactness factor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCompactnessFactor(double)">
<h3>setCompactnessFactor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCompactnessFactor</span><wbr/><span class="parameters">(double d)</span></div>
<div class="block">Set compactness factor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAllowOverlaps(boolean)">
<h3>setAllowOverlaps</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAllowOverlaps</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set allow overlap. Can result in more compact layout</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllowOverlaps()">
<h3>getAllowOverlaps</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getAllowOverlaps</span>()</div>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
