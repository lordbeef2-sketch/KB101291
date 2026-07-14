# JAVA OPENAPI: HierarchicLayouterOptionsGroup (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/core/options/HierarchicLayouterOptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/HierarchicLayouterOptionsGroup.html`
- source_sha256: `c005ca38e72747a546adc88c2e7711599179122087989937f2935bb8aa605513`
- captured_utc: `2026-07-14T16:57:52.414473+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class HierarchicLayouterOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[ActivityLayouterOptionsGroup](ActivityLayouterOptionsGroup.html)`, `[ClassDiagramLayouterOptionsGroup](ClassDiagramLayouterOptionsGroup.html)`, `[CompositeLayouterOptionsGroup](CompositeLayouterOptionsGroup.html)`, `[StateMachineLayouterOptionsGroup](StateMachineLayouterOptionsGroup.html)`

@OpenApiAllpublic classHierarchicLayouterOptionsGroup
extends [AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)

Hierarchic Layouter options group.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[EDGE_ROUTINGS](#EDGE_ROUTINGS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ID](#ID)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OBLIQUE](#OBLIQUE)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ORTHOGONAL](#ORTHOGONAL)`
Fields inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[ALIGNMENT_BOTTOM](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_BOTTOM), [ALIGNMENT_CENTER](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_CENTER), [ALIGNMENT_TOP](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_TOP), [LAYOUT_LABEL_CONSIDERATION](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION), [LAYOUT_LABEL_CONSIDERATION_FULL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_FULL), [LAYOUT_LABEL_CONSIDERATION_NONE](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_NONE), [LAYOUT_LABEL_CONSIDERATION_PARTIAL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_PARTIAL), [MAX_INT_VALUE](AbstractDiagramLayouterOptionsGroup.html#MAX_INT_VALUE), [SHAPE_ALIGNMENT](AbstractDiagramLayouterOptionsGroup.html#SHAPE_ALIGNMENT)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[HierarchicLayouterOptionsGroup](#%3Cinit%3E())()`

`[HierarchicLayouterOptionsGroup](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Construct HierarchicLayouterOptionsGroup
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addProperty](#addProperty(com.nomagic.magicdraw.properties.Property))([Property](../../properties/Property.html) property)`
Adds property to this group.
`com.dassault_systemes.modeler.foundation.diagram.ylayout.LayoutParams`
`[createParams](#createParams())()`

`boolean`
`[getBackloopRouting](#getBackloopRouting())()`
Get Back Loop Routing property value in order to enabled all paths that do not point in the main layout direction will be routed as backloops.
`boolean`
`[getConsiderLayoutTemplates](#getConsiderLayoutTemplates())()`

`[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)`
`[getCopy](#getCopy())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getEdgeRouting](#getEdgeRouting())()`
Get string representation route to oblique style with a certain number of bends.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getLayoutLabelConsideration](#getLayoutLabelConsideration())()`
Get label consideration mode
`boolean`
`[getLayoutOnlyTopLevel](#getLayoutOnlyTopLevel())()`
Gets the Layout only top level value.
`boolean`
`[getMakeSubTrees](#getMakeSubTrees())()`
Get Make Sub trees property value.
`int`
`[getMinimalFirstSegmentLength](#getMinimalFirstSegmentLength())()`
Get the minimal length of the first and last segments for orthogonal path routing, i.e.
`int`
`[getMinimalLayerDistance](#getMinimalLayerDistance())()`
Get the minimal distance between shapes that reside in adjacent layers.
`int`
`[getMinimalLinkDistance](#getMinimalLinkDistance())()`
Get the distance between adjacent pairs of horizontal path segments and between horizontal path segments and shapes.
`int`
`[getMinimalShapeDistance](#getMinimalShapeDistance())()`
Get the minimal distance between borders of two adjacent shapes on a common circle.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getOrientation](#getOrientation())()`
Get main layout orientation.
`boolean`
`[getRemoveFalseCrossings](#getRemoveFalseCrossings())()`
Get Remove False Crossings property value in order to enable a post-processing step tries to eliminate all false path crossings.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getSequencer](#getSequencer())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getShapeAlignmentWithinLayer](#getShapeAlignmentWithinLayer())()`
Get Shape position within a layer.
`boolean`
`[getUseGlobalSequencing](#getUseGlobalSequencing())()`
Get Use Global Sequencing property value.
`boolean`
`[getUseTransposition](#getUseTransposition())()`
Get the transposition property value determines a post-processing further reduces the number of path crossings.
`protected com.dassault_systemes.modeler.foundation.diagram.ylayout.hierarchical.HierarchicalLayoutParams`
`[initDefaultOptionsValues](#initDefaultOptionsValues())()`

`boolean`
`[isLayoutOnlyTopLevel](#isLayoutOnlyTopLevel())()`
Check Layout Only Top Level property value.
`void`
`[setBackloopRouting](#setBackloopRouting(boolean))(boolean b)`
Set Back Loop Routing property value in order to enabled all paths that do not point in the main layout direction will be routed as backloops.
`void`
`[setConsiderLayoutTemplates](#setConsiderLayoutTemplates(boolean))(boolean b)`
If set to true, leaves the elements that have layout templates unchanged.
`void`
`[setEdgeRouting](#setEdgeRouting(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s)`
Set string representation route to oblique style with a certain number of bends.
`void`
`[setLayoutLabelConsideration](#setLayoutLabelConsideration(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Set label consideration mode
`void`
`[setLayoutOnlyTopLevel](#setLayoutOnlyTopLevel(boolean))(boolean b)`
Set Layout Only Top Level property value in order to keeps the relative position of symbols inside packages and performs the top level layout.
`void`
`[setMakeSubTrees](#setMakeSubTrees(boolean))(boolean b)`
Set Make Sub trees property value to set the inheritance paths are joined into inheritance arcs.
`void`
`[setMinimalFirstSegmentLength](#setMinimalFirstSegmentLength(int))(int d)`
Set the minimal length of the first and last segments for orthogonal path routing, i.e.
`void`
`[setMinimalLayerDistance](#setMinimalLayerDistance(int))(int d)`
Set the minimal distance between shapes that reside in adjacent layers.
`void`
`[setMinimalLinkDistance](#setMinimalLinkDistance(int))(int d)`
Set the distance between adjacent pairs of horizontal path segments and between horizontal path segments and shapes.
`void`
`[setMinimalShapeDistance](#setMinimalShapeDistance(int))(int d)`
Set the minimal distance between borders of two adjacent shapes on a common circle.
`void`
`[setOrientation](#setOrientation(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s)`
Set main layout orientation.
`void`
`[setRemoveFalseCrossings](#setRemoveFalseCrossings(boolean))(boolean b)`
Set Remove False Crossings property value determines a post-processing step tries to eliminate all false path crossings.
`void`
`[setSequencer](#setSequencer(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s)`

`void`
`[setShapeAlignmentWithinLayer](#setShapeAlignmentWithinLayer(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Set Shape alignment within a layer.
`void`
`[setUseGlobalSequencing](#setUseGlobalSequencing(boolean))(boolean b)`
Set Use Global Sequencing property value.
`void`
`[setUseTransposition](#setUseTransposition(boolean))(boolean b)`
Set the transposition property value in order to enable a post-processing further reduces the number of path crossings.
`com.dassault_systemes.modeler.foundation.diagram.ylayout.hierarchical.HierarchicalLayoutParams`
`[toLayoutParams](#toLayoutParams())()`
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[getMakePreferredLayoutSize](AbstractDiagramLayouterOptionsGroup.html#getMakePreferredLayoutSize()), [getOptimizeLabelOrientations](AbstractDiagramLayouterOptionsGroup.html#getOptimizeLabelOrientations()), [isMoveToFreeSpace](AbstractDiagramLayouterOptionsGroup.html#isMoveToFreeSpace()), [setDefaultValues](AbstractDiagramLayouterOptionsGroup.html#setDefaultValues()), [setMakePreferredLayoutSize](AbstractDiagramLayouterOptionsGroup.html#setMakePreferredLayoutSize(boolean)), [setMoveToFreeSpace](AbstractDiagramLayouterOptionsGroup.html#setMoveToFreeSpace(boolean)), [setOptimizeLabelOrientations](AbstractDiagramLayouterOptionsGroup.html#setOptimizeLabelOrientations(boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
`[addInvisibleProperty](AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)), [getOptions](AbstractPropertyOptionsGroup.html#getOptions()), [getProperty](AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)), [getVisibleOptions](AbstractPropertyOptionsGroup.html#getVisibleOptions()), [removeProperty](AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)), [setOptions](AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)), [setPropertiesInvisible](AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)), [setPropertyInvisible](AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](OptionsGroup.html)
`[getGroupIcon](OptionsGroup.html#getGroupIcon()), [getName](OptionsGroup.html#getName())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ID
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ID
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup.ID)
OBLIQUE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OBLIQUE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup.OBLIQUE)
ORTHOGONAL
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ORTHOGONAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup.ORTHOGONAL)
EDGE_ROUTINGS
public static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> EDGE_ROUTINGS
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
HierarchicLayouterOptionsGroup
public HierarchicLayouterOptionsGroup([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Construct HierarchicLayouterOptionsGroup
HierarchicLayouterOptionsGroup
public HierarchicLayouterOptionsGroup()
 ============ METHOD DETAIL ========== 
Method Details
initDefaultOptionsValues
protected com.dassault_systemes.modeler.foundation.diagram.ylayout.hierarchical.HierarchicalLayoutParams initDefaultOptionsValues()
Overrides:
`[initDefaultOptionsValues](AbstractDiagramLayouterOptionsGroup.html#initDefaultOptionsValues())` in class `[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)`
toLayoutParams
public com.dassault_systemes.modeler.foundation.diagram.ylayout.hierarchical.HierarchicalLayoutParams toLayoutParams()
Overrides:
`[toLayoutParams](AbstractDiagramLayouterOptionsGroup.html#toLayoutParams())` in class `[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)`
createParams
public com.dassault_systemes.modeler.foundation.diagram.ylayout.LayoutParams createParams()
Specified by:
`[createParams](AbstractDiagramLayouterOptionsGroup.html#createParams())` in class `[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)`
Returns:
new default params object
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
getMinimalLinkDistance
public int getMinimalLinkDistance()
Get the distance between adjacent pairs of horizontal path segments and between horizontal path segments and shapes.
Returns:
int value.
setMinimalLinkDistance
public void setMinimalLinkDistance(int d)
Set the distance between adjacent pairs of horizontal path segments and between horizontal path segments and shapes.
Parameters:
`d` - new distance
getMinimalFirstSegmentLength
public int getMinimalFirstSegmentLength()
Get the minimal length of the first and last segments for orthogonal path routing, i.e. the length from the intersection points to the first or last bend point respectively.
Returns:
int value.
setMinimalFirstSegmentLength
public void setMinimalFirstSegmentLength(int d)
Set the minimal length of the first and last segments for orthogonal path routing, i.e. the length from the intersection points to the first or last bend point respectively.
Parameters:
`d` - new length
getOrientation
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getOrientation()
Get main layout orientation.
Returns:
value.
setOrientation
public void setOrientation([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s)
Set main layout orientation.
Parameters:
`s` - value.
getSequencer
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getSequencer()
setSequencer
public void setSequencer([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s)
getEdgeRouting
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getEdgeRouting()
Get string representation route to oblique style with a certain number of bends.
Returns:
string.
setEdgeRouting
public void setEdgeRouting([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s)
Set string representation route to oblique style with a certain number of bends.
Parameters:
`s` - string value.
setBackloopRouting
public void setBackloopRouting(boolean b)
Set Back Loop Routing property value in order to enabled all paths that do not point in the main layout direction will be routed as backloops.
Parameters:
`b` - boolean.
getBackloopRouting
public boolean getBackloopRouting()
Get Back Loop Routing property value in order to enabled all paths that do not point in the main layout direction will be routed as backloops.
Returns:
true if backloop routing is enabled, false otherwise
setShapeAlignmentWithinLayer
public void setShapeAlignmentWithinLayer([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Set Shape alignment within a layer.
getShapeAlignmentWithinLayer
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getShapeAlignmentWithinLayer()
Get Shape position within a layer.
Returns:
string.
setUseTransposition
public void setUseTransposition(boolean b)
Set the transposition property value in order to enable a post-processing further reduces the number of path crossings. The post-processing step can be rather time consuming.
Parameters:
`b` - boolean value.
getUseTransposition
public boolean getUseTransposition()
Get the transposition property value determines a post-processing further reduces the number of path crossings. The post-processing step can be rather time consuming.
Returns:
value.
setRemoveFalseCrossings
public void setRemoveFalseCrossings(boolean b)
Set Remove False Crossings property value determines a post-processing step tries to eliminate all false path crossings. A false path crossing is a path crossing between two paths that attached to the same shape.
Parameters:
`b` - boolean value.
getRemoveFalseCrossings
public boolean getRemoveFalseCrossings()
Get Remove False Crossings property value in order to enable a post-processing step tries to eliminate all false path crossings. A false path crossing is a path crossing between two paths that attached to the same shape.
Returns:
true if should remove false crossings
setUseGlobalSequencing
public void setUseGlobalSequencing(boolean b)
Set Use Global Sequencing property value.
 It can be used to activate an alternative sequencing algorithm that calculates the shapes order. This algorithm tends to give better results for complex shape nesting but may produce more crossings locally than the default algorithm.
Parameters:
`b` - boolean
getUseGlobalSequencing
public boolean getUseGlobalSequencing()
Get Use Global Sequencing property value.
 It can be used to activate an alternative sequencing algorithm that calculates the shapes order. This algorithm tends to give better results for complex shape nesting but may produce more crossings locally than the default algorithm.
Returns:
boolean
setLayoutOnlyTopLevel
public void setLayoutOnlyTopLevel(boolean b)
Set Layout Only Top Level property value in order to keeps the relative position of symbols inside packages and performs the top level layout.
Parameters:
`b` - boolean.
getLayoutOnlyTopLevel
public boolean getLayoutOnlyTopLevel()
Gets the Layout only top level value. It allows the inside of group nodes not to be layouted.
Returns:
true if only outer nodes should be layouter, false if all nodes should be layouted
isLayoutOnlyTopLevel
public boolean isLayoutOnlyTopLevel()
Check Layout Only Top Level property value. It indicates position of symbols inside packages is on the top level layout.
Returns:
true if should layout only the top level, but not inner group node structure
setMakeSubTrees
public void setMakeSubTrees(boolean b)
Set Make Sub trees property value to set the inheritance paths are joined into inheritance arcs.
Parameters:
`b` - true to make trees
getMakeSubTrees
public boolean getMakeSubTrees()
Get Make Sub trees property value.
Returns:
boolean
setLayoutLabelConsideration
public void setLayoutLabelConsideration([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Set label consideration mode
getLayoutLabelConsideration
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getLayoutLabelConsideration()
Get label consideration mode
Returns:
string.
addProperty
public void addProperty([Property](../../properties/Property.html) property)
Description copied from class: `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property))`
Adds property to this group. DescriptionID will be reset. To add property with description use
 [`AbstractPropertyOptionsGroup.addProperty(Property, String)`](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)) method.
Overrides:
`[addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property))` in class `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)`
Parameters:
`property` - property to be added.
setConsiderLayoutTemplates
public void setConsiderLayoutTemplates(boolean b)
If set to true, leaves the elements that have layout templates unchanged.
getConsiderLayoutTemplates
public boolean getConsiderLayoutTemplates()
getCopy
public [HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html) getCopy()
Overrides:
`[getCopy](AbstractDiagramLayouterOptionsGroup.html#getCopy())` in class `[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class HierarchicLayouterOptionsGroup">Class HierarchicLayouterOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance"><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ActivityLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">ActivityLayouterOptionsGroup</a></code>, <code><a href="ClassDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">ClassDiagramLayouterOptionsGroup</a></code>, <code><a href="CompositeLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">CompositeLayouterOptionsGroup</a></code>, <code><a href="StateMachineLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">StateMachineLayouterOptionsGroup</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">HierarchicLayouterOptionsGroup</span>
<span class="extends-implements">extends <a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></span></div>
<div class="block">Hierarchic Layouter options group.</div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EDGE_ROUTINGS">EDGE_ROUTINGS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ID">ID</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OBLIQUE">OBLIQUE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ORTHOGONAL">ORTHOGONAL</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">HierarchicLayouterOptionsGroup</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">HierarchicLayouterOptionsGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color">
<div class="block">Construct HierarchicLayouterOptionsGroup</div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.diagram.ylayout.LayoutParams</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createParams()">createParams</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBackloopRouting()">getBackloopRouting</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Back Loop Routing property value in order to enabled all paths that do not point in the main layout direction will be routed as backloops.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConsiderLayoutTemplates()">getConsiderLayoutTemplates</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCopy()">getCopy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEdgeRouting()">getEdgeRouting</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get string representation route to oblique style with a certain number of bends.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLayoutLabelConsideration()">getLayoutLabelConsideration</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get label consideration mode</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLayoutOnlyTopLevel()">getLayoutOnlyTopLevel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the Layout only top level value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMakeSubTrees()">getMakeSubTrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Make Sub trees property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimalFirstSegmentLength()">getMinimalFirstSegmentLength</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the minimal length of the first and last segments for orthogonal path routing, i.e.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimalLayerDistance()">getMinimalLayerDistance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the minimal distance between shapes that reside in adjacent layers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimalLinkDistance()">getMinimalLinkDistance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the distance between adjacent pairs of horizontal path segments and between horizontal path segments and shapes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimalShapeDistance()">getMinimalShapeDistance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the minimal distance between borders of two adjacent shapes on a common circle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrientation()">getOrientation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get main layout orientation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoveFalseCrossings()">getRemoveFalseCrossings</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Remove False Crossings property value in order to enable a post-processing step tries to eliminate all false path crossings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSequencer()">getSequencer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShapeAlignmentWithinLayer()">getShapeAlignmentWithinLayer</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Shape position within a layer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUseGlobalSequencing()">getUseGlobalSequencing</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Use Global Sequencing property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUseTransposition()">getUseTransposition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the transposition property value determines a post-processing further reduces the number of path crossings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.dassault_systemes.modeler.foundation.diagram.ylayout.hierarchical.HierarchicalLayoutParams</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initDefaultOptionsValues()">initDefaultOptionsValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLayoutOnlyTopLevel()">isLayoutOnlyTopLevel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check Layout Only Top Level property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBackloopRouting(boolean)">setBackloopRouting</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Back Loop Routing property value in order to enabled all paths that do not point in the main layout direction will be routed as backloops.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setConsiderLayoutTemplates(boolean)">setConsiderLayoutTemplates</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If set to true, leaves the elements that have layout templates unchanged.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEdgeRouting(java.lang.String)">setEdgeRouting</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set string representation route to oblique style with a certain number of bends.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayoutLabelConsideration(java.lang.String)">setLayoutLabelConsideration</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set label consideration mode</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayoutOnlyTopLevel(boolean)">setLayoutOnlyTopLevel</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Layout Only Top Level property value in order to keeps the relative position of symbols inside packages and performs the top level layout.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMakeSubTrees(boolean)">setMakeSubTrees</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Make Sub trees property value to set the inheritance paths are joined into inheritance arcs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMinimalFirstSegmentLength(int)">setMinimalFirstSegmentLength</a><wbr/>(int d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the minimal length of the first and last segments for orthogonal path routing, i.e.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMinimalLayerDistance(int)">setMinimalLayerDistance</a><wbr/>(int d)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the minimal distance between shapes that reside in adjacent layers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMinimalLinkDistance(int)">setMinimalLinkDistance</a><wbr/>(int d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the distance between adjacent pairs of horizontal path segments and between horizontal path segments and shapes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMinimalShapeDistance(int)">setMinimalShapeDistance</a><wbr/>(int d)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the minimal distance between borders of two adjacent shapes on a common circle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOrientation(java.lang.String)">setOrientation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set main layout orientation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRemoveFalseCrossings(boolean)">setRemoveFalseCrossings</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Remove False Crossings property value determines a post-processing step tries to eliminate all false path crossings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSequencer(java.lang.String)">setSequencer</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShapeAlignmentWithinLayer(java.lang.String)">setShapeAlignmentWithinLayer</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Shape alignment within a layer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseGlobalSequencing(boolean)">setUseGlobalSequencing</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Use Global Sequencing property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseTransposition(boolean)">setUseTransposition</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the transposition property value in order to enable a post-processing further reduces the number of path crossings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.diagram.ylayout.hierarchical.HierarchicalLayoutParams</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toLayoutParams()">toLayoutParams</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></h3>
<code><a href="AbstractDiagramLayouterOptionsGroup.html#getMakePreferredLayoutSize()">getMakePreferredLayoutSize</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#getOptimizeLabelOrientations()">getOptimizeLabelOrientations</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#isMoveToFreeSpace()">isMoveToFreeSpace</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setDefaultValues()">setDefaultValues</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setMakePreferredLayoutSize(boolean)">setMakePreferredLayoutSize</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setMoveToFreeSpace(boolean)">setMoveToFreeSpace</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setOptimizeLabelOrientations(boolean)">setOptimizeLabelOrientations</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></h3>
<code><a href="AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getOptions()">getOptions</a>, <a href="AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)">getProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getVisibleOptions()">getVisibleOptions</a>, <a href="AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)">removeProperty</a>, <a href="AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)">setOptions</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)">setPropertiesInvisible</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean)">setPropertyInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="OptionsGroup.html#getGroupIcon()">getGroupIcon</a>, <a href="OptionsGroup.html#getName()">getName</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ID</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup.ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OBLIQUE">
<h3>OBLIQUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OBLIQUE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup.OBLIQUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ORTHOGONAL">
<h3>ORTHOGONAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ORTHOGONAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup.ORTHOGONAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EDGE_ROUTINGS">
<h3>EDGE_ROUTINGS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">EDGE_ROUTINGS</span></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>HierarchicLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HierarchicLayouterOptionsGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Construct HierarchicLayouterOptionsGroup</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>HierarchicLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HierarchicLayouterOptionsGroup</span>()</div>
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
<section class="detail" id="initDefaultOptionsValues()">
<h3>initDefaultOptionsValues</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.dassault_systemes.modeler.foundation.diagram.ylayout.hierarchical.HierarchicalLayoutParams</span> <span class="element-name">initDefaultOptionsValues</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouterOptionsGroup.html#initDefaultOptionsValues()">initDefaultOptionsValues</a></code> in class <code><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toLayoutParams()">
<h3>toLayoutParams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.diagram.ylayout.hierarchical.HierarchicalLayoutParams</span> <span class="element-name">toLayoutParams</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouterOptionsGroup.html#toLayoutParams()">toLayoutParams</a></code> in class <code><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParams()">
<h3>createParams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.diagram.ylayout.LayoutParams</span> <span class="element-name">createParams</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramLayouterOptionsGroup.html#createParams()">createParams</a></code> in class <code><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></code></dd>
<dt>Returns:</dt>
<dd>new default params object</dd>
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
<section class="detail" id="getMinimalLinkDistance()">
<h3>getMinimalLinkDistance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMinimalLinkDistance</span>()</div>
<div class="block">Get the distance between adjacent pairs of horizontal path segments and between horizontal path segments and shapes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMinimalLinkDistance(int)">
<h3>setMinimalLinkDistance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMinimalLinkDistance</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set the distance between adjacent pairs of horizontal path segments and between horizontal path segments and shapes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - new distance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMinimalFirstSegmentLength()">
<h3>getMinimalFirstSegmentLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMinimalFirstSegmentLength</span>()</div>
<div class="block">Get the minimal length of the first and last segments for orthogonal path routing, i.e. the length from the intersection points to the first or last bend point respectively.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMinimalFirstSegmentLength(int)">
<h3>setMinimalFirstSegmentLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMinimalFirstSegmentLength</span><wbr/><span class="parameters">(int d)</span></div>
<div class="block">Set the minimal length of the first and last segments for orthogonal path routing, i.e. the length from the intersection points to the first or last bend point respectively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - new length</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrientation()">
<h3>getOrientation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOrientation</span>()</div>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOrientation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Set main layout orientation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSequencer()">
<h3>getSequencer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSequencer</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setSequencer(java.lang.String)">
<h3>setSequencer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSequencer</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
</section>
</li>
<li>
<section class="detail" id="getEdgeRouting()">
<h3>getEdgeRouting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEdgeRouting</span>()</div>
<div class="block">Get string representation route to oblique style with a certain number of bends.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEdgeRouting(java.lang.String)">
<h3>setEdgeRouting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEdgeRouting</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Set string representation route to oblique style with a certain number of bends.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - string value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBackloopRouting(boolean)">
<h3>setBackloopRouting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBackloopRouting</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Back Loop Routing property value in order to enabled all paths that do not point in the main layout direction will be routed as backloops.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBackloopRouting()">
<h3>getBackloopRouting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getBackloopRouting</span>()</div>
<div class="block">Get Back Loop Routing property value in order to enabled all paths that do not point in the main layout direction will be routed as backloops.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if backloop routing is enabled, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShapeAlignmentWithinLayer(java.lang.String)">
<h3>setShapeAlignmentWithinLayer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShapeAlignmentWithinLayer</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Set Shape alignment within a layer.</div>
</section>
</li>
<li>
<section class="detail" id="getShapeAlignmentWithinLayer()">
<h3>getShapeAlignmentWithinLayer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getShapeAlignmentWithinLayer</span>()</div>
<div class="block">Get Shape position within a layer.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseTransposition(boolean)">
<h3>setUseTransposition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseTransposition</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set the transposition property value in order to enable a post-processing further reduces the number of path crossings. The post-processing step can be rather time consuming.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUseTransposition()">
<h3>getUseTransposition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getUseTransposition</span>()</div>
<div class="block">Get the transposition property value determines a post-processing further reduces the number of path crossings. The post-processing step can be rather time consuming.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRemoveFalseCrossings(boolean)">
<h3>setRemoveFalseCrossings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRemoveFalseCrossings</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Remove False Crossings property value determines a post-processing step tries to eliminate all false path crossings. A false path crossing is a path crossing between two paths that attached to the same shape.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoveFalseCrossings()">
<h3>getRemoveFalseCrossings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getRemoveFalseCrossings</span>()</div>
<div class="block">Get Remove False Crossings property value in order to enable a post-processing step tries to eliminate all false path crossings. A false path crossing is a path crossing between two paths that attached to the same shape.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if should remove false crossings</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseGlobalSequencing(boolean)">
<h3>setUseGlobalSequencing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseGlobalSequencing</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Use Global Sequencing property value.
 It can be used to activate an alternative sequencing algorithm that calculates the shapes order. This algorithm tends to give better results for complex shape nesting but may produce more crossings locally than the default algorithm.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUseGlobalSequencing()">
<h3>getUseGlobalSequencing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getUseGlobalSequencing</span>()</div>
<div class="block">Get Use Global Sequencing property value.
 It can be used to activate an alternative sequencing algorithm that calculates the shapes order. This algorithm tends to give better results for complex shape nesting but may produce more crossings locally than the default algorithm.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean</dd>
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
<section class="detail" id="getLayoutOnlyTopLevel()">
<h3>getLayoutOnlyTopLevel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getLayoutOnlyTopLevel</span>()</div>
<div class="block">Gets the Layout only top level value. It allows the inside of group nodes not to be layouted.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if only outer nodes should be layouter, false if all nodes should be layouted</dd>
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
<dd>true if should layout only the top level, but not inner group node structure</dd>
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
<dd><code>b</code> - true to make trees</dd>
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
<section class="detail" id="setLayoutLabelConsideration(java.lang.String)">
<h3>setLayoutLabelConsideration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayoutLabelConsideration</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Set label consideration mode</div>
</section>
</li>
<li>
<section class="detail" id="getLayoutLabelConsideration()">
<h3>getLayoutLabelConsideration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLayoutLabelConsideration</span>()</div>
<div class="block">Get label consideration mode</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProperty(com.nomagic.magicdraw.properties.Property)">
<h3>addProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProperty</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">AbstractPropertyOptionsGroup</a></code></span></div>
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
<section class="detail" id="setConsiderLayoutTemplates(boolean)">
<h3>setConsiderLayoutTemplates</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setConsiderLayoutTemplates</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">If set to true, leaves the elements that have layout templates unchanged.</div>
</section>
</li>
<li>
<section class="detail" id="getConsiderLayoutTemplates()">
<h3>getConsiderLayoutTemplates</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getConsiderLayoutTemplates</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCopy()">
<h3>getCopy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></span> <span class="element-name">getCopy</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouterOptionsGroup.html#getCopy()">getCopy</a></code> in class <code><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></code></dd>
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
