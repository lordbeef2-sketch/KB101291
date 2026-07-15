# JAVA OPENAPI: ActivityLayouterOptionsGroup (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/core/options/ActivityLayouterOptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/ActivityLayouterOptionsGroup.html`
- source_sha256: `fe19fccbd104e4611276e1e81e44a85518c479217a4a7e115cad0a34cd0ed2f3`
- captured_utc: `2026-07-14T16:55:11.466966+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class ActivityLayouterOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
[com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)
com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[BusinessProcessLayouterOptionsGroup](BusinessProcessLayouterOptionsGroup.html)`

@OpenApiAllpublic classActivityLayouterOptionsGroup
extends [HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)

Activity Layouter options group.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[ACTIVITY_ORIENTATIONS](#ACTIVITY_ORIENTATIONS)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BOTTOM_TO_TOP](#BOTTOM_TO_TOP)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ID](#ID)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LEFT_TO_RIGHT](#LEFT_TO_RIGHT)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RIGHT_TO_LEFT](#RIGHT_TO_LEFT)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SPECIFIED_BY_DIAGRAM](#SPECIFIED_BY_DIAGRAM)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TOP_TO_BOTTOM](#TOP_TO_BOTTOM)`
Fields inherited from class com.nomagic.magicdraw.core.options.[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)
`[EDGE_ROUTINGS](HierarchicLayouterOptionsGroup.html#EDGE_ROUTINGS), [OBLIQUE](HierarchicLayouterOptionsGroup.html#OBLIQUE), [ORTHOGONAL](HierarchicLayouterOptionsGroup.html#ORTHOGONAL)`
Fields inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[ALIGNMENT_BOTTOM](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_BOTTOM), [ALIGNMENT_CENTER](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_CENTER), [ALIGNMENT_TOP](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_TOP), [LAYOUT_LABEL_CONSIDERATION](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION), [LAYOUT_LABEL_CONSIDERATION_FULL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_FULL), [LAYOUT_LABEL_CONSIDERATION_NONE](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_NONE), [LAYOUT_LABEL_CONSIDERATION_PARTIAL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_PARTIAL), [MAX_INT_VALUE](AbstractDiagramLayouterOptionsGroup.html#MAX_INT_VALUE), [SHAPE_ALIGNMENT](AbstractDiagramLayouterOptionsGroup.html#SHAPE_ALIGNMENT)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ActivityLayouterOptionsGroup](#%3Cinit%3E())()`

`[ActivityLayouterOptionsGroup](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Construct HierarchicLayouterOptionsGroup
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getOrientation](#getOrientation())()`
Get main layout orientation.
`protected void`
`[initCommonDefaultValues](#initCommonDefaultValues())()`

`void`
`[setOrientation](#setOrientation(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)`
Set main layout orientation.
Methods inherited from class com.nomagic.magicdraw.core.options.[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)
`[addProperty](HierarchicLayouterOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)), [getBackloopRouting](HierarchicLayouterOptionsGroup.html#getBackloopRouting()), [getConsiderLayoutTemplates](HierarchicLayouterOptionsGroup.html#getConsiderLayoutTemplates()), [getCopy](HierarchicLayouterOptionsGroup.html#getCopy()), [getEdgeRouting](HierarchicLayouterOptionsGroup.html#getEdgeRouting()), [getLayoutLabelConsideration](HierarchicLayouterOptionsGroup.html#getLayoutLabelConsideration()), [getLayoutOnlyTopLevel](HierarchicLayouterOptionsGroup.html#getLayoutOnlyTopLevel()), [getMakeSubTrees](HierarchicLayouterOptionsGroup.html#getMakeSubTrees()), [getMinimalFirstSegmentLength](HierarchicLayouterOptionsGroup.html#getMinimalFirstSegmentLength()), [getMinimalLayerDistance](HierarchicLayouterOptionsGroup.html#getMinimalLayerDistance()), [getMinimalLinkDistance](HierarchicLayouterOptionsGroup.html#getMinimalLinkDistance()), [getMinimalShapeDistance](HierarchicLayouterOptionsGroup.html#getMinimalShapeDistance()), [getRemoveFalseCrossings](HierarchicLayouterOptionsGroup.html#getRemoveFalseCrossings()), [getSequencer](HierarchicLayouterOptionsGroup.html#getSequencer()), [getShapeAlignmentWithinLayer](HierarchicLayouterOptionsGroup.html#getShapeAlignmentWithinLayer()), [getUseGlobalSequencing](HierarchicLayouterOptionsGroup.html#getUseGlobalSequencing()), [getUseTransposition](HierarchicLayouterOptionsGroup.html#getUseTransposition()), [isLayoutOnlyTopLevel](HierarchicLayouterOptionsGroup.html#isLayoutOnlyTopLevel()), [setBackloopRouting](HierarchicLayouterOptionsGroup.html#setBackloopRouting(boolean)), [setConsiderLayoutTemplates](HierarchicLayouterOptionsGroup.html#setConsiderLayoutTemplates(boolean)), [setEdgeRouting](HierarchicLayouterOptionsGroup.html#setEdgeRouting(java.lang.String)), [setLayoutLabelConsideration](HierarchicLayouterOptionsGroup.html#setLayoutLabelConsideration(java.lang.String)), [setLayoutOnlyTopLevel](HierarchicLayouterOptionsGroup.html#setLayoutOnlyTopLevel(boolean)), [setMakeSubTrees](HierarchicLayouterOptionsGroup.html#setMakeSubTrees(boolean)), [setMinimalFirstSegmentLength](HierarchicLayouterOptionsGroup.html#setMinimalFirstSegmentLength(int)), [setMinimalLayerDistance](HierarchicLayouterOptionsGroup.html#setMinimalLayerDistance(int)), [setMinimalLinkDistance](HierarchicLayouterOptionsGroup.html#setMinimalLinkDistance(int)), [setMinimalShapeDistance](HierarchicLayouterOptionsGroup.html#setMinimalShapeDistance(int)), [setRemoveFalseCrossings](HierarchicLayouterOptionsGroup.html#setRemoveFalseCrossings(boolean)), [setSequencer](HierarchicLayouterOptionsGroup.html#setSequencer(java.lang.String)), [setShapeAlignmentWithinLayer](HierarchicLayouterOptionsGroup.html#setShapeAlignmentWithinLayer(java.lang.String)), [setUseGlobalSequencing](HierarchicLayouterOptionsGroup.html#setUseGlobalSequencing(boolean)), [setUseTransposition](HierarchicLayouterOptionsGroup.html#setUseTransposition(boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[getMakePreferredLayoutSize](AbstractDiagramLayouterOptionsGroup.html#getMakePreferredLayoutSize()), [getOptimizeLabelOrientations](AbstractDiagramLayouterOptionsGroup.html#getOptimizeLabelOrientations()), [isMoveToFreeSpace](AbstractDiagramLayouterOptionsGroup.html#isMoveToFreeSpace()), [setDefaultValues](AbstractDiagramLayouterOptionsGroup.html#setDefaultValues()), [setMakePreferredLayoutSize](AbstractDiagramLayouterOptionsGroup.html#setMakePreferredLayoutSize(boolean)), [setMoveToFreeSpace](AbstractDiagramLayouterOptionsGroup.html#setMoveToFreeSpace(boolean)), [setOptimizeLabelOrientations](AbstractDiagramLayouterOptionsGroup.html#setOptimizeLabelOrientations(boolean))`
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
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup.ID)
TOP_TO_BOTTOM
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TOP_TO_BOTTOM
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup.TOP_TO_BOTTOM)
BOTTOM_TO_TOP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BOTTOM_TO_TOP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup.BOTTOM_TO_TOP)
LEFT_TO_RIGHT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LEFT_TO_RIGHT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup.LEFT_TO_RIGHT)
RIGHT_TO_LEFT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RIGHT_TO_LEFT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup.RIGHT_TO_LEFT)
SPECIFIED_BY_DIAGRAM
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SPECIFIED_BY_DIAGRAM
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup.SPECIFIED_BY_DIAGRAM)
ACTIVITY_ORIENTATIONS
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> ACTIVITY_ORIENTATIONS
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ActivityLayouterOptionsGroup
public ActivityLayouterOptionsGroup([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Construct HierarchicLayouterOptionsGroup
ActivityLayouterOptionsGroup
public ActivityLayouterOptionsGroup()
 ============ METHOD DETAIL ========== 
Method Details
initCommonDefaultValues
protected void initCommonDefaultValues()
Overrides:
`[initCommonDefaultValues](HierarchicLayouterOptionsGroup.html#initCommonDefaultValues())` in class `[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)`
setOrientation
public void setOrientation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)
Set main layout orientation.
Overrides:
`[setOrientation](HierarchicLayouterOptionsGroup.html#setOrientation(java.lang.String))` in class `[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)`
Parameters:
`s` - value.
getOrientation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getOrientation()
Get main layout orientation.
Overrides:
`[getOrientation](HierarchicLayouterOptionsGroup.html#getOrientation())` in class `[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)`
Returns:
value.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class ActivityLayouterOptionsGroup">Class ActivityLayouterOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance"><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup</a>
<div class="inheritance"><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup</div>
</div>
</div>
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
<dd><code><a href="BusinessProcessLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">BusinessProcessLayouterOptionsGroup</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ActivityLayouterOptionsGroup</span>
<span class="extends-implements">extends <a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></span></div>
<div class="block">Activity Layouter options group.</div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTIVITY_ORIENTATIONS">ACTIVITY_ORIENTATIONS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BOTTOM_TO_TOP">BOTTOM_TO_TOP</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ID">ID</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LEFT_TO_RIGHT">LEFT_TO_RIGHT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RIGHT_TO_LEFT">RIGHT_TO_LEFT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SPECIFIED_BY_DIAGRAM">SPECIFIED_BY_DIAGRAM</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TOP_TO_BOTTOM">TOP_TO_BOTTOM</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.<a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></h3>
<code><a href="HierarchicLayouterOptionsGroup.html#EDGE_ROUTINGS">EDGE_ROUTINGS</a>, <a href="HierarchicLayouterOptionsGroup.html#OBLIQUE">OBLIQUE</a>, <a href="HierarchicLayouterOptionsGroup.html#ORTHOGONAL">ORTHOGONAL</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ActivityLayouterOptionsGroup</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">ActivityLayouterOptionsGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrientation()">getOrientation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get main layout orientation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initCommonDefaultValues()">initCommonDefaultValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOrientation(java.lang.String)">setOrientation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set main layout orientation.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></h3>
<code><a href="HierarchicLayouterOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="HierarchicLayouterOptionsGroup.html#getBackloopRouting()">getBackloopRouting</a>, <a href="HierarchicLayouterOptionsGroup.html#getConsiderLayoutTemplates()">getConsiderLayoutTemplates</a>, <a href="HierarchicLayouterOptionsGroup.html#getCopy()">getCopy</a>, <a href="HierarchicLayouterOptionsGroup.html#getEdgeRouting()">getEdgeRouting</a>, <a href="HierarchicLayouterOptionsGroup.html#getLayoutLabelConsideration()">getLayoutLabelConsideration</a>, <a href="HierarchicLayouterOptionsGroup.html#getLayoutOnlyTopLevel()">getLayoutOnlyTopLevel</a>, <a href="HierarchicLayouterOptionsGroup.html#getMakeSubTrees()">getMakeSubTrees</a>, <a href="HierarchicLayouterOptionsGroup.html#getMinimalFirstSegmentLength()">getMinimalFirstSegmentLength</a>, <a href="HierarchicLayouterOptionsGroup.html#getMinimalLayerDistance()">getMinimalLayerDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#getMinimalLinkDistance()">getMinimalLinkDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#getMinimalShapeDistance()">getMinimalShapeDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#getRemoveFalseCrossings()">getRemoveFalseCrossings</a>, <a href="HierarchicLayouterOptionsGroup.html#getSequencer()">getSequencer</a>, <a href="HierarchicLayouterOptionsGroup.html#getShapeAlignmentWithinLayer()">getShapeAlignmentWithinLayer</a>, <a href="HierarchicLayouterOptionsGroup.html#getUseGlobalSequencing()">getUseGlobalSequencing</a>, <a href="HierarchicLayouterOptionsGroup.html#getUseTransposition()">getUseTransposition</a>, <a href="HierarchicLayouterOptionsGroup.html#isLayoutOnlyTopLevel()">isLayoutOnlyTopLevel</a>, <a href="HierarchicLayouterOptionsGroup.html#setBackloopRouting(boolean)">setBackloopRouting</a>, <a href="HierarchicLayouterOptionsGroup.html#setConsiderLayoutTemplates(boolean)">setConsiderLayoutTemplates</a>, <a href="HierarchicLayouterOptionsGroup.html#setEdgeRouting(java.lang.String)">setEdgeRouting</a>, <a href="HierarchicLayouterOptionsGroup.html#setLayoutLabelConsideration(java.lang.String)">setLayoutLabelConsideration</a>, <a href="HierarchicLayouterOptionsGroup.html#setLayoutOnlyTopLevel(boolean)">setLayoutOnlyTopLevel</a>, <a href="HierarchicLayouterOptionsGroup.html#setMakeSubTrees(boolean)">setMakeSubTrees</a>, <a href="HierarchicLayouterOptionsGroup.html#setMinimalFirstSegmentLength(int)">setMinimalFirstSegmentLength</a>, <a href="HierarchicLayouterOptionsGroup.html#setMinimalLayerDistance(int)">setMinimalLayerDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#setMinimalLinkDistance(int)">setMinimalLinkDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#setMinimalShapeDistance(int)">setMinimalShapeDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#setRemoveFalseCrossings(boolean)">setRemoveFalseCrossings</a>, <a href="HierarchicLayouterOptionsGroup.html#setSequencer(java.lang.String)">setSequencer</a>, <a href="HierarchicLayouterOptionsGroup.html#setShapeAlignmentWithinLayer(java.lang.String)">setShapeAlignmentWithinLayer</a>, <a href="HierarchicLayouterOptionsGroup.html#setUseGlobalSequencing(boolean)">setUseGlobalSequencing</a>, <a href="HierarchicLayouterOptionsGroup.html#setUseTransposition(boolean)">setUseTransposition</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></h3>
<code><a href="AbstractDiagramLayouterOptionsGroup.html#getMakePreferredLayoutSize()">getMakePreferredLayoutSize</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#getOptimizeLabelOrientations()">getOptimizeLabelOrientations</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#isMoveToFreeSpace()">isMoveToFreeSpace</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setDefaultValues()">setDefaultValues</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setMakePreferredLayoutSize(boolean)">setMakePreferredLayoutSize</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setMoveToFreeSpace(boolean)">setMoveToFreeSpace</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setOptimizeLabelOrientations(boolean)">setOptimizeLabelOrientations</a></code></div>
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
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup.ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TOP_TO_BOTTOM">
<h3>TOP_TO_BOTTOM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TOP_TO_BOTTOM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup.TOP_TO_BOTTOM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BOTTOM_TO_TOP">
<h3>BOTTOM_TO_TOP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BOTTOM_TO_TOP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup.BOTTOM_TO_TOP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LEFT_TO_RIGHT">
<h3>LEFT_TO_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LEFT_TO_RIGHT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup.LEFT_TO_RIGHT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RIGHT_TO_LEFT">
<h3>RIGHT_TO_LEFT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RIGHT_TO_LEFT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup.RIGHT_TO_LEFT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SPECIFIED_BY_DIAGRAM">
<h3>SPECIFIED_BY_DIAGRAM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SPECIFIED_BY_DIAGRAM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ActivityLayouterOptionsGroup.SPECIFIED_BY_DIAGRAM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTIVITY_ORIENTATIONS">
<h3>ACTIVITY_ORIENTATIONS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">ACTIVITY_ORIENTATIONS</span></div>
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
<h3>ActivityLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ActivityLayouterOptionsGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Construct HierarchicLayouterOptionsGroup</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ActivityLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ActivityLayouterOptionsGroup</span>()</div>
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
<dd><code><a href="HierarchicLayouterOptionsGroup.html#initCommonDefaultValues()">initCommonDefaultValues</a></code> in class <code><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOrientation(java.lang.String)">
<h3>setOrientation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOrientation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Set main layout orientation.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="HierarchicLayouterOptionsGroup.html#setOrientation(java.lang.String)">setOrientation</a></code> in class <code><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></code></dd>
<dt>Parameters:</dt>
<dd><code>s</code> - value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrientation()">
<h3>getOrientation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOrientation</span>()</div>
<div class="block">Get main layout orientation.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="HierarchicLayouterOptionsGroup.html#getOrientation()">getOrientation</a></code> in class <code><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></code></dd>
<dt>Returns:</dt>
<dd>value.</dd>
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
