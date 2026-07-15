# JAVA OPENAPI: TreeLayouterOptionsGroup (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/core/options/TreeLayouterOptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/TreeLayouterOptionsGroup.html`
- source_sha256: `3140195373723d859fae67c720bf7b5238373c77bf624121beb160ec489ca2c0`
- captured_utc: `2026-07-14T16:51:16.177137+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class TreeLayouterOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classTreeLayouterOptionsGroup
extends [AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)

Organic Layouter options group.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BALLOON](#BALLOON)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BORDER_CENTERED](#BORDER_CENTERED)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BORDER_DISTRIBUTED](#BORDER_DISTRIBUTED)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CENTER_ROOT](#CENTER_ROOT)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIRECTED](#DIRECTED)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIRECTED_ROOT](#DIRECTED_ROOT)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[HORIZONTAL_VERTICAL](#HORIZONTAL_VERTICAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ID](#ID)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NODE_CENTERED](#NODE_CENTERED)`
Fields inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[ALIGNMENT_BOTTOM](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_BOTTOM), [ALIGNMENT_CENTER](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_CENTER), [ALIGNMENT_TOP](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_TOP), [LAYOUT_LABEL_CONSIDERATION](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION), [LAYOUT_LABEL_CONSIDERATION_FULL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_FULL), [LAYOUT_LABEL_CONSIDERATION_NONE](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_NONE), [LAYOUT_LABEL_CONSIDERATION_PARTIAL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_PARTIAL), [MAX_INT_VALUE](AbstractDiagramLayouterOptionsGroup.html#MAX_INT_VALUE), [SHAPE_ALIGNMENT](AbstractDiagramLayouterOptionsGroup.html#SHAPE_ALIGNMENT)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TreeLayouterOptionsGroup](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addProperty](#addProperty(com.nomagic.magicdraw.properties.Property))([Property](../../properties/Property.html) property)`
Adds property to this group.
`double`
`[getCompactnessFactor](#getCompactnessFactor())()`
Get compactness factor.
`int`
`[getHorizontalSpacing](#getHorizontalSpacing())()`
Get The minimal horizontal distance between adjacent shapes.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLayoutStyle](#getLayoutStyle())()`
Get string layout representation.
`boolean`
`[getMakeSubTrees](#getMakeSubTrees())()`
Get Make Sub trees property value.
`int`
`[getMinimalLayerDistance](#getMinimalLayerDistance())()`
Get the minimal distance between shapes that reside in adjacent layers.
`int`
`[getMinimalLinkLength](#getMinimalLinkLength())()`
Get the minimal length of a path that connects two shapes that lie on separate circles.
`int`
`[getMinimalShapeDistance](#getMinimalShapeDistance())()`
Get the minimal distance between borders of two adjacent shapes on a common circle.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getOrientation](#getOrientation())()`
Get main layout orientation.
`boolean`
`[getOrthogonalLinkRouting](#getOrthogonalLinkRouting())()`
Get Orthogonal Link Routing.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPortStyle](#getPortStyle())()`
Get Port Style property value.
`int`
`[getPreferredChildWedge](#getPreferredChildWedge())()`
Get the angular range of the sector that will be reserved for children of a shape.
`int`
`[getPreferredRootWedge](#getPreferredRootWedge())()`
Get the angular range of the sector that will be reserved around the root shape to accommodate attached subtrees.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRootShapePosition](#getRootShapePosition())()`
Get Root Shape Position property value.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getShapeAlignment](#getShapeAlignment())()`
Gets shape alignment option value.
`int`
`[getVerticalSpacing](#getVerticalSpacing())()`
Get The minimal vertical distance between adjacent shapes.
`protected void`
`[initCommonDefaultValues](#initCommonDefaultValues())()`

`void`
`[setCompactnessFactor](#setCompactnessFactor(double))(double d)`
Set compactness factor.
`void`
`[setHorizontalSpacing](#setHorizontalSpacing(int))(int d)`
Set The minimal horizontal distance between adjacent shapes.
`void`
`[setLayoutStyle](#setLayoutStyle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)`
Set layout style property value..
`void`
`[setMakeSubTrees](#setMakeSubTrees(boolean))(boolean b)`
Set Make Sub trees property value to set the inheritance paths are joined into inheritance arcs.
`void`
`[setMinimalLayerDistance](#setMinimalLayerDistance(int))(int d)`
Set the minimal distance between shapes that reside in adjacent layers.
`void`
`[setMinimalLinkLength](#setMinimalLinkLength(int))(int d)`
Set the minimal length of a path that connects two shapes that lie on separate circles.
`void`
`[setMinimalShapeDistance](#setMinimalShapeDistance(int))(int d)`
Set the minimal distance between borders of two adjacent shapes on a common circle.
`void`
`[setOrientation](#setOrientation(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)`
Set main layout orientation.
`void`
`[setOrthogonalLinkRouting](#setOrthogonalLinkRouting(boolean))(boolean b)`
Set Orthogonal Link Routing.
`void`
`[setPortStyle](#setPortStyle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)`
Set Port Style property value.
`void`
`[setPreferredChildWedge](#setPreferredChildWedge(int))(int d)`
Set the angular range of the sector that will be reserved for children of a shape.
`void`
`[setPreferredRootWedge](#setPreferredRootWedge(int))(int d)`
Set the angular range of the sector that will be reserved around the root shape to accommodate attached subtrees.
`void`
`[setRootShapePosition](#setRootShapePosition(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)`
Set Root Shape Position property value.
`void`
`[setShapeAlignment](#setShapeAlignment(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)`
Sets shape alignment.
`void`
`[setVerticalSpacing](#setVerticalSpacing(int))(int d)`
Set The minimal vertical distance between adjacent shapes.
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
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.ID)
DIRECTED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIRECTED
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.DIRECTED)
BALLOON
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BALLOON
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.BALLOON)
HORIZONTAL_VERTICAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) HORIZONTAL_VERTICAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.HORIZONTAL_VERTICAL)
NODE_CENTERED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NODE_CENTERED
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.NODE_CENTERED)
BORDER_CENTERED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BORDER_CENTERED
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.BORDER_CENTERED)
BORDER_DISTRIBUTED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BORDER_DISTRIBUTED
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.BORDER_DISTRIBUTED)
DIRECTED_ROOT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIRECTED_ROOT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.DIRECTED_ROOT)
CENTER_ROOT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CENTER_ROOT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.CENTER_ROOT)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TreeLayouterOptionsGroup
public TreeLayouterOptionsGroup()
 ============ METHOD DETAIL ========== 
Method Details
initCommonDefaultValues
protected void initCommonDefaultValues()
Overrides:
`[initCommonDefaultValues](AbstractDiagramLayouterOptionsGroup.html#initCommonDefaultValues())` in class `[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)`
getLayoutStyle
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLayoutStyle()
Get string layout representation.
Returns:
string.
setLayoutStyle
public void setLayoutStyle([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)
Set layout style property value..
Parameters:
`s` - the new layout style
getMinimalLayerDistance
public int getMinimalLayerDistance()
Get the minimal distance between shapes that reside in adjacent layers.
Returns:
int value.
setMinimalLayerDistance
public void setMinimalLayerDistance(int d)
Set the minimal distance between shapes that reside in adjacent layers.
Parameters:
`d` - int value.
getMinimalShapeDistance
public int getMinimalShapeDistance()
Get the minimal distance between borders of two adjacent shapes on a common circle. The smaller the distance, the more compact resulting layout.
Returns:
int value.
setMinimalShapeDistance
public void setMinimalShapeDistance(int d)
Set the minimal distance between borders of two adjacent shapes on a common circle. The smaller the distance, the more compact resulting layout.
Parameters:
`d` - value.
getOrientation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getOrientation()
Get main layout orientation.
Returns:
value.
setOrientation
public void setOrientation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)
Set main layout orientation.
Parameters:
`s` - value.
getPortStyle
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPortStyle()
Get Port Style property value.
 Determines the way how paths are attached to shapes.
 Border Centered. Paths are attached to the center of the border of corresponding shapes.
 Border Distributed. Path attachment points are distributed along the border of corresponding shapes.
Returns:
a mode how paths are attached to shapes
setPortStyle
public void setPortStyle([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)
Set Port Style property value.
 Determines the way how paths are attached to shapes.
 Border Centered. Paths are attached to the center of the border of corresponding shapes.
 Border Distributed. Path attachment points are distributed along the border of corresponding shapes.
Parameters:
`s` - the new port style to set
setOrthogonalLinkRouting
public void setOrthogonalLinkRouting(boolean b)
Set Orthogonal Link Routing.
 If selected, all paths are routed orthogonally in a bus-like fashion. If not selected, paths are routed as straight line segments.
Parameters:
`b` - boolean.
getOrthogonalLinkRouting
public boolean getOrthogonalLinkRouting()
Get Orthogonal Link Routing.
 If selected, all paths are routed orthogonally in a bus-like fashion. If not selected, paths are routed as straight line segments.
Returns:
true if links are router orthogonally, false otherwise
getRootShapePosition
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRootShapePosition()
Get Root Shape Position property value.
 Directed Root. Chooses a shape with in-degree zero if present. A good choice for directed rooted trees.
 Center Root. Chooses the root shape in such a way that the depth of the resulting tree is minimized.
Returns:
String.
setRootShapePosition
public void setRootShapePosition([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)
Set Root Shape Position property value.
 Directed Root. Chooses a shape with indegree zero if present. A good choice for directed rooted trees.
 Center Root. Chooses the root shape in such a way that the depth of the resulting tree is minimized.
Parameters:
`s` - the shape positioning value
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
getPreferredRootWedge
public int getPreferredRootWedge()
Get the angular range of the sector that will be reserved around the root shape to accommodate attached subtrees.
Returns:
int
setPreferredRootWedge
public void setPreferredRootWedge(int d)
Set the angular range of the sector that will be reserved around the root shape to accommodate attached subtrees.
Parameters:
`d` - int.
getMinimalLinkLength
public int getMinimalLinkLength()
Get the minimal length of a path that connects two shapes that lie on separate circles. The smaller the chosen value, the more compact the resulting layout.
Returns:
the minimal length of the path
setMinimalLinkLength
public void setMinimalLinkLength(int d)
Set the minimal length of a path that connects two shapes that lie on separate circles. The smaller the chosen value, the more compact the resulting layout.
Parameters:
`d` - the new minimal path length
getCompactnessFactor
public double getCompactnessFactor()
Get compactness factor.
 Adjusting this value can lead to a variety of differing layouts. For small values, the resulting layout will use much space and shapes tend to be far away from each other. Values around 0.5 lead to evenly distributed shapes, whereas values near 1.0 produce highly compact layouts.
Returns:
compactness factor of the graph
setCompactnessFactor
public void setCompactnessFactor(double d)
Set compactness factor.
Parameters:
`d` - value.
getHorizontalSpacing
public int getHorizontalSpacing()
Get The minimal horizontal distance between adjacent shapes.
Returns:
int.
setHorizontalSpacing
public void setHorizontalSpacing(int d)
Set The minimal horizontal distance between adjacent shapes.
Parameters:
`d` - int value.
getVerticalSpacing
public int getVerticalSpacing()
Get The minimal vertical distance between adjacent shapes.
Returns:
int.
setVerticalSpacing
public void setVerticalSpacing(int d)
Set The minimal vertical distance between adjacent shapes.
Parameters:
`d` - int value.
setMakeSubTrees
public void setMakeSubTrees(boolean b)
Set Make Sub trees property value to set the inheritance paths are joined into inheritance arcs.
Parameters:
`b` - true to create tree sets, false otherwise
getMakeSubTrees
public boolean getMakeSubTrees()
Get Make Sub trees property value.
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
setShapeAlignment
public void setShapeAlignment([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)
Sets shape alignment.
Parameters:
`s` - shape alignment to set.
getShapeAlignment
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getShapeAlignment()
Gets shape alignment option value.
Returns:
shape alignment option value.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class TreeLayouterOptionsGroup">Class TreeLayouterOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance"><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup</div>
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
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TreeLayouterOptionsGroup</span>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BALLOON">BALLOON</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BORDER_CENTERED">BORDER_CENTERED</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BORDER_DISTRIBUTED">BORDER_DISTRIBUTED</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CENTER_ROOT">CENTER_ROOT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIRECTED">DIRECTED</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIRECTED_ROOT">DIRECTED_ROOT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HORIZONTAL_VERTICAL">HORIZONTAL_VERTICAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ID">ID</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NODE_CENTERED">NODE_CENTERED</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TreeLayouterOptionsGroup</a>()</code></div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCompactnessFactor()">getCompactnessFactor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get compactness factor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHorizontalSpacing()">getHorizontalSpacing</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get The minimal horizontal distance between adjacent shapes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLayoutStyle()">getLayoutStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get string layout representation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMakeSubTrees()">getMakeSubTrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Make Sub trees property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimalLayerDistance()">getMinimalLayerDistance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the minimal distance between shapes that reside in adjacent layers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimalLinkLength()">getMinimalLinkLength</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the minimal length of a path that connects two shapes that lie on separate circles.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimalShapeDistance()">getMinimalShapeDistance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the minimal distance between borders of two adjacent shapes on a common circle.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrientation()">getOrientation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get main layout orientation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrthogonalLinkRouting()">getOrthogonalLinkRouting</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Orthogonal Link Routing.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPortStyle()">getPortStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Port Style property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreferredChildWedge()">getPreferredChildWedge</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the angular range of the sector that will be reserved for children of a shape.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreferredRootWedge()">getPreferredRootWedge</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the angular range of the sector that will be reserved around the root shape to accommodate attached subtrees.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRootShapePosition()">getRootShapePosition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Root Shape Position property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShapeAlignment()">getShapeAlignment</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets shape alignment option value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVerticalSpacing()">getVerticalSpacing</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get The minimal vertical distance between adjacent shapes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initCommonDefaultValues()">initCommonDefaultValues</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCompactnessFactor(double)">setCompactnessFactor</a><wbr/>(double d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set compactness factor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHorizontalSpacing(int)">setHorizontalSpacing</a><wbr/>(int d)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set The minimal horizontal distance between adjacent shapes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayoutStyle(java.lang.String)">setLayoutStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set layout style property value..</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMakeSubTrees(boolean)">setMakeSubTrees</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Make Sub trees property value to set the inheritance paths are joined into inheritance arcs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMinimalLayerDistance(int)">setMinimalLayerDistance</a><wbr/>(int d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the minimal distance between shapes that reside in adjacent layers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMinimalLinkLength(int)">setMinimalLinkLength</a><wbr/>(int d)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the minimal length of a path that connects two shapes that lie on separate circles.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMinimalShapeDistance(int)">setMinimalShapeDistance</a><wbr/>(int d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the minimal distance between borders of two adjacent shapes on a common circle.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOrientation(java.lang.String)">setOrientation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set main layout orientation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOrthogonalLinkRouting(boolean)">setOrthogonalLinkRouting</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Orthogonal Link Routing.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPortStyle(java.lang.String)">setPortStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Port Style property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPreferredChildWedge(int)">setPreferredChildWedge</a><wbr/>(int d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the angular range of the sector that will be reserved for children of a shape.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPreferredRootWedge(int)">setPreferredRootWedge</a><wbr/>(int d)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the angular range of the sector that will be reserved around the root shape to accommodate attached subtrees.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRootShapePosition(java.lang.String)">setRootShapePosition</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Root Shape Position property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShapeAlignment(java.lang.String)">setShapeAlignment</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets shape alignment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVerticalSpacing(int)">setVerticalSpacing</a><wbr/>(int d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set The minimal vertical distance between adjacent shapes.</div>
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
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIRECTED">
<h3>DIRECTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIRECTED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.DIRECTED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BALLOON">
<h3>BALLOON</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BALLOON</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.BALLOON">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HORIZONTAL_VERTICAL">
<h3>HORIZONTAL_VERTICAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HORIZONTAL_VERTICAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.HORIZONTAL_VERTICAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NODE_CENTERED">
<h3>NODE_CENTERED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NODE_CENTERED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.NODE_CENTERED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BORDER_CENTERED">
<h3>BORDER_CENTERED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BORDER_CENTERED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.BORDER_CENTERED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BORDER_DISTRIBUTED">
<h3>BORDER_DISTRIBUTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BORDER_DISTRIBUTED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.BORDER_DISTRIBUTED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIRECTED_ROOT">
<h3>DIRECTED_ROOT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIRECTED_ROOT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.DIRECTED_ROOT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENTER_ROOT">
<h3>CENTER_ROOT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CENTER_ROOT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TreeLayouterOptionsGroup.CENTER_ROOT">Constant Field Values</a></li>
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
<h3>TreeLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TreeLayouterOptionsGroup</span>()</div>
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
<div class="block">Get string layout representation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLayoutStyle(java.lang.String)">
<h3>setLayoutStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayoutStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Set layout style property value..</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - the new layout style</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMinimalLayerDistance()">
<h3>getMinimalLayerDistance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMinimalLayerDistance</span>()</div>
<div class="block">Get the minimal distance between shapes that reside in adjacent layers.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMinimalLayerDistance(int)">
<h3>setMinimalLayerDistance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMinimalLayerDistance</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set the minimal distance between shapes that reside in adjacent layers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - int value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMinimalShapeDistance()">
<h3>getMinimalShapeDistance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMinimalShapeDistance</span>()</div>
<div class="block">Get the minimal distance between borders of two adjacent shapes on a common circle. The smaller the distance, the more compact resulting layout.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMinimalShapeDistance(int)">
<h3>setMinimalShapeDistance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMinimalShapeDistance</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set the minimal distance between borders of two adjacent shapes on a common circle. The smaller the distance, the more compact resulting layout.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrientation()">
<h3>getOrientation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOrientation</span>()</div>
<div class="block">Get main layout orientation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOrientation(java.lang.String)">
<h3>setOrientation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOrientation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Set main layout orientation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPortStyle()">
<h3>getPortStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPortStyle</span>()</div>
<div class="block">Get Port Style property value.
 Determines the way how paths are attached to shapes.
 Border Centered. Paths are attached to the center of the border of corresponding shapes.
 Border Distributed. Path attachment points are distributed along the border of corresponding shapes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a mode how paths are attached to shapes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPortStyle(java.lang.String)">
<h3>setPortStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPortStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Set Port Style property value.
 Determines the way how paths are attached to shapes.
 Border Centered. Paths are attached to the center of the border of corresponding shapes.
 Border Distributed. Path attachment points are distributed along the border of corresponding shapes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - the new port style to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOrthogonalLinkRouting(boolean)">
<h3>setOrthogonalLinkRouting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOrthogonalLinkRouting</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Orthogonal Link Routing.
 If selected, all paths are routed orthogonally in a bus-like fashion. If not selected, paths are routed as straight line segments.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrthogonalLinkRouting()">
<h3>getOrthogonalLinkRouting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getOrthogonalLinkRouting</span>()</div>
<div class="block">Get Orthogonal Link Routing.
 If selected, all paths are routed orthogonally in a bus-like fashion. If not selected, paths are routed as straight line segments.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if links are router orthogonally, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRootShapePosition()">
<h3>getRootShapePosition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRootShapePosition</span>()</div>
<div class="block">Get Root Shape Position property value.
 Directed Root. Chooses a shape with in-degree zero if present. A good choice for directed rooted trees.
 Center Root. Chooses the root shape in such a way that the depth of the resulting tree is minimized.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>String.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRootShapePosition(java.lang.String)">
<h3>setRootShapePosition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRootShapePosition</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Set Root Shape Position property value.
 Directed Root. Chooses a shape with indegree zero if present. A good choice for directed rooted trees.
 Center Root. Chooses the root shape in such a way that the depth of the resulting tree is minimized.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - the shape positioning value</dd>
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
<section class="detail" id="getPreferredRootWedge()">
<h3>getPreferredRootWedge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPreferredRootWedge</span>()</div>
<div class="block">Get the angular range of the sector that will be reserved around the root shape to accommodate attached subtrees.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPreferredRootWedge(int)">
<h3>setPreferredRootWedge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPreferredRootWedge</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set the angular range of the sector that will be reserved around the root shape to accommodate attached subtrees.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - int.</dd>
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
<dd>the minimal length of the path</dd>
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
<dd><code>d</code> - the new minimal path length</dd>
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
<dd>compactness factor of the graph</dd>
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
<section class="detail" id="getHorizontalSpacing()">
<h3>getHorizontalSpacing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getHorizontalSpacing</span>()</div>
<div class="block">Get The minimal horizontal distance between adjacent shapes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHorizontalSpacing(int)">
<h3>setHorizontalSpacing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHorizontalSpacing</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set The minimal horizontal distance between adjacent shapes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - int value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVerticalSpacing()">
<h3>getVerticalSpacing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getVerticalSpacing</span>()</div>
<div class="block">Get The minimal vertical distance between adjacent shapes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVerticalSpacing(int)">
<h3>setVerticalSpacing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVerticalSpacing</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set The minimal vertical distance between adjacent shapes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - int value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMakeSubTrees(boolean)">
<h3>setMakeSubTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMakeSubTrees</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Make Sub trees property value to set the inheritance paths are joined into inheritance arcs.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - true to create tree sets, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMakeSubTrees()">
<h3>getMakeSubTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getMakeSubTrees</span>()</div>
<div class="block">Get Make Sub trees property value.</div>
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
<section class="detail" id="setShapeAlignment(java.lang.String)">
<h3>setShapeAlignment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShapeAlignment</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Sets shape alignment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - shape alignment to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getShapeAlignment()">
<h3>getShapeAlignment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getShapeAlignment</span>()</div>
<div class="block">Gets shape alignment option value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>shape alignment option value.</dd>
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
