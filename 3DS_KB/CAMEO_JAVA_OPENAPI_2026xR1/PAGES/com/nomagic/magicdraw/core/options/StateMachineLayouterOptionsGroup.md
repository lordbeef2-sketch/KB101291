# JAVA OPENAPI: StateMachineLayouterOptionsGroup (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/core/options/StateMachineLayouterOptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/StateMachineLayouterOptionsGroup.html`
- source_sha256: `f9758d6bc66411e646ac9e099fa358acdb367ecd6bb06a8e54b16ca902c0be19`
- captured_utc: `2026-07-14T16:45:31.227418+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class StateMachineLayouterOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
[com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)
com.nomagic.magicdraw.core.options.StateMachineLayouterOptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classStateMachineLayouterOptionsGroup
extends [HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)

State machine layouter options group.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[BEZIER](#BEZIER)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ID](#ID)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ORTHOGONAL](#ORTHOGONAL)`

`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)`
`[STATE_ROUTING_STYLES](#STATE_ROUTING_STYLES)`
Fields inherited from class com.nomagic.magicdraw.core.options.[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)
`[EDGE_ROUTINGS](HierarchicLayouterOptionsGroup.html#EDGE_ROUTINGS), [OBLIQUE](HierarchicLayouterOptionsGroup.html#OBLIQUE)`
Fields inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[ALIGNMENT_BOTTOM](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_BOTTOM), [ALIGNMENT_CENTER](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_CENTER), [ALIGNMENT_TOP](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_TOP), [LAYOUT_LABEL_CONSIDERATION](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION), [LAYOUT_LABEL_CONSIDERATION_FULL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_FULL), [LAYOUT_LABEL_CONSIDERATION_NONE](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_NONE), [LAYOUT_LABEL_CONSIDERATION_PARTIAL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_PARTIAL), [MAX_INT_VALUE](AbstractDiagramLayouterOptionsGroup.html#MAX_INT_VALUE), [SHAPE_ALIGNMENT](AbstractDiagramLayouterOptionsGroup.html#SHAPE_ALIGNMENT)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[StateMachineLayouterOptionsGroup](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`com.dassault_systemes.modeler.foundation.diagram.ylayout.LayoutParams`
`[createParams](#createParams())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getEdgeRouting](#getEdgeRouting())()`
Get route style string
`protected com.nomagic.magicdraw.uml.symbols.layout.state.StateLayoutParams`
`[initDefaultOptionsValues](#initDefaultOptionsValues())()`

`void`
`[setEdgeRouting](#setEdgeRouting(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s)`
Set route style for state diagram
`com.nomagic.magicdraw.uml.symbols.layout.state.StateLayoutParams`
`[toLayoutParams](#toLayoutParams())()`
Methods inherited from class com.nomagic.magicdraw.core.options.[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)
`[addProperty](HierarchicLayouterOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)), [getBackloopRouting](HierarchicLayouterOptionsGroup.html#getBackloopRouting()), [getConsiderLayoutTemplates](HierarchicLayouterOptionsGroup.html#getConsiderLayoutTemplates()), [getCopy](HierarchicLayouterOptionsGroup.html#getCopy()), [getLayoutLabelConsideration](HierarchicLayouterOptionsGroup.html#getLayoutLabelConsideration()), [getLayoutOnlyTopLevel](HierarchicLayouterOptionsGroup.html#getLayoutOnlyTopLevel()), [getMakeSubTrees](HierarchicLayouterOptionsGroup.html#getMakeSubTrees()), [getMinimalFirstSegmentLength](HierarchicLayouterOptionsGroup.html#getMinimalFirstSegmentLength()), [getMinimalLayerDistance](HierarchicLayouterOptionsGroup.html#getMinimalLayerDistance()), [getMinimalLinkDistance](HierarchicLayouterOptionsGroup.html#getMinimalLinkDistance()), [getMinimalShapeDistance](HierarchicLayouterOptionsGroup.html#getMinimalShapeDistance()), [getOrientation](HierarchicLayouterOptionsGroup.html#getOrientation()), [getRemoveFalseCrossings](HierarchicLayouterOptionsGroup.html#getRemoveFalseCrossings()), [getSequencer](HierarchicLayouterOptionsGroup.html#getSequencer()), [getShapeAlignmentWithinLayer](HierarchicLayouterOptionsGroup.html#getShapeAlignmentWithinLayer()), [getUseGlobalSequencing](HierarchicLayouterOptionsGroup.html#getUseGlobalSequencing()), [getUseTransposition](HierarchicLayouterOptionsGroup.html#getUseTransposition()), [isLayoutOnlyTopLevel](HierarchicLayouterOptionsGroup.html#isLayoutOnlyTopLevel()), [setBackloopRouting](HierarchicLayouterOptionsGroup.html#setBackloopRouting(boolean)), [setConsiderLayoutTemplates](HierarchicLayouterOptionsGroup.html#setConsiderLayoutTemplates(boolean)), [setLayoutLabelConsideration](HierarchicLayouterOptionsGroup.html#setLayoutLabelConsideration(java.lang.String)), [setLayoutOnlyTopLevel](HierarchicLayouterOptionsGroup.html#setLayoutOnlyTopLevel(boolean)), [setMakeSubTrees](HierarchicLayouterOptionsGroup.html#setMakeSubTrees(boolean)), [setMinimalFirstSegmentLength](HierarchicLayouterOptionsGroup.html#setMinimalFirstSegmentLength(int)), [setMinimalLayerDistance](HierarchicLayouterOptionsGroup.html#setMinimalLayerDistance(int)), [setMinimalLinkDistance](HierarchicLayouterOptionsGroup.html#setMinimalLinkDistance(int)), [setMinimalShapeDistance](HierarchicLayouterOptionsGroup.html#setMinimalShapeDistance(int)), [setOrientation](HierarchicLayouterOptionsGroup.html#setOrientation(java.lang.String)), [setRemoveFalseCrossings](HierarchicLayouterOptionsGroup.html#setRemoveFalseCrossings(boolean)), [setSequencer](HierarchicLayouterOptionsGroup.html#setSequencer(java.lang.String)), [setShapeAlignmentWithinLayer](HierarchicLayouterOptionsGroup.html#setShapeAlignmentWithinLayer(java.lang.String)), [setUseGlobalSequencing](HierarchicLayouterOptionsGroup.html#setUseGlobalSequencing(boolean)), [setUseTransposition](HierarchicLayouterOptionsGroup.html#setUseTransposition(boolean))`
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
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.StateMachineLayouterOptionsGroup.ID)
BEZIER
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) BEZIER
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.StateMachineLayouterOptionsGroup.BEZIER)
ORTHOGONAL
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ORTHOGONAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.StateMachineLayouterOptionsGroup.ORTHOGONAL)
STATE_ROUTING_STYLES
public static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) STATE_ROUTING_STYLES
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
StateMachineLayouterOptionsGroup
public StateMachineLayouterOptionsGroup()
 ============ METHOD DETAIL ========== 
Method Details
initDefaultOptionsValues
protected com.nomagic.magicdraw.uml.symbols.layout.state.StateLayoutParams initDefaultOptionsValues()
Overrides:
`[initDefaultOptionsValues](HierarchicLayouterOptionsGroup.html#initDefaultOptionsValues())` in class `[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)`
toLayoutParams
public com.nomagic.magicdraw.uml.symbols.layout.state.StateLayoutParams toLayoutParams()
Overrides:
`[toLayoutParams](HierarchicLayouterOptionsGroup.html#toLayoutParams())` in class `[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)`
createParams
public com.dassault_systemes.modeler.foundation.diagram.ylayout.LayoutParams createParams()
Overrides:
`[createParams](HierarchicLayouterOptionsGroup.html#createParams())` in class `[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)`
Returns:
new default params object
getEdgeRouting
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getEdgeRouting()
Get route style string
Overrides:
`[getEdgeRouting](HierarchicLayouterOptionsGroup.html#getEdgeRouting())` in class `[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)`
Returns:
string.
setEdgeRouting
public void setEdgeRouting([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s)
Set route style for state diagram
Overrides:
`[setEdgeRouting](HierarchicLayouterOptionsGroup.html#setEdgeRouting(java.lang.String))` in class `[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)`
Parameters:
`s` - string value.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class StateMachineLayouterOptionsGroup">Class StateMachineLayouterOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance"><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup</a>
<div class="inheritance"><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.StateMachineLayouterOptionsGroup</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">StateMachineLayouterOptionsGroup</span>
<span class="extends-implements">extends <a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></span></div>
<div class="block">State machine layouter options group.</div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BEZIER">BEZIER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ID">ID</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ORTHOGONAL">ORTHOGONAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STATE_ROUTING_STYLES">STATE_ROUTING_STYLES</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.<a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></h3>
<code><a href="HierarchicLayouterOptionsGroup.html#EDGE_ROUTINGS">EDGE_ROUTINGS</a>, <a href="HierarchicLayouterOptionsGroup.html#OBLIQUE">OBLIQUE</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">StateMachineLayouterOptionsGroup</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.diagram.ylayout.LayoutParams</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createParams()">createParams</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEdgeRouting()">getEdgeRouting</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get route style string</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.uml.symbols.layout.state.StateLayoutParams</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initDefaultOptionsValues()">initDefaultOptionsValues</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEdgeRouting(java.lang.String)">setEdgeRouting</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set route style for state diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.layout.state.StateLayoutParams</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toLayoutParams()">toLayoutParams</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></h3>
<code><a href="HierarchicLayouterOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="HierarchicLayouterOptionsGroup.html#getBackloopRouting()">getBackloopRouting</a>, <a href="HierarchicLayouterOptionsGroup.html#getConsiderLayoutTemplates()">getConsiderLayoutTemplates</a>, <a href="HierarchicLayouterOptionsGroup.html#getCopy()">getCopy</a>, <a href="HierarchicLayouterOptionsGroup.html#getLayoutLabelConsideration()">getLayoutLabelConsideration</a>, <a href="HierarchicLayouterOptionsGroup.html#getLayoutOnlyTopLevel()">getLayoutOnlyTopLevel</a>, <a href="HierarchicLayouterOptionsGroup.html#getMakeSubTrees()">getMakeSubTrees</a>, <a href="HierarchicLayouterOptionsGroup.html#getMinimalFirstSegmentLength()">getMinimalFirstSegmentLength</a>, <a href="HierarchicLayouterOptionsGroup.html#getMinimalLayerDistance()">getMinimalLayerDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#getMinimalLinkDistance()">getMinimalLinkDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#getMinimalShapeDistance()">getMinimalShapeDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#getOrientation()">getOrientation</a>, <a href="HierarchicLayouterOptionsGroup.html#getRemoveFalseCrossings()">getRemoveFalseCrossings</a>, <a href="HierarchicLayouterOptionsGroup.html#getSequencer()">getSequencer</a>, <a href="HierarchicLayouterOptionsGroup.html#getShapeAlignmentWithinLayer()">getShapeAlignmentWithinLayer</a>, <a href="HierarchicLayouterOptionsGroup.html#getUseGlobalSequencing()">getUseGlobalSequencing</a>, <a href="HierarchicLayouterOptionsGroup.html#getUseTransposition()">getUseTransposition</a>, <a href="HierarchicLayouterOptionsGroup.html#isLayoutOnlyTopLevel()">isLayoutOnlyTopLevel</a>, <a href="HierarchicLayouterOptionsGroup.html#setBackloopRouting(boolean)">setBackloopRouting</a>, <a href="HierarchicLayouterOptionsGroup.html#setConsiderLayoutTemplates(boolean)">setConsiderLayoutTemplates</a>, <a href="HierarchicLayouterOptionsGroup.html#setLayoutLabelConsideration(java.lang.String)">setLayoutLabelConsideration</a>, <a href="HierarchicLayouterOptionsGroup.html#setLayoutOnlyTopLevel(boolean)">setLayoutOnlyTopLevel</a>, <a href="HierarchicLayouterOptionsGroup.html#setMakeSubTrees(boolean)">setMakeSubTrees</a>, <a href="HierarchicLayouterOptionsGroup.html#setMinimalFirstSegmentLength(int)">setMinimalFirstSegmentLength</a>, <a href="HierarchicLayouterOptionsGroup.html#setMinimalLayerDistance(int)">setMinimalLayerDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#setMinimalLinkDistance(int)">setMinimalLinkDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#setMinimalShapeDistance(int)">setMinimalShapeDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#setOrientation(java.lang.String)">setOrientation</a>, <a href="HierarchicLayouterOptionsGroup.html#setRemoveFalseCrossings(boolean)">setRemoveFalseCrossings</a>, <a href="HierarchicLayouterOptionsGroup.html#setSequencer(java.lang.String)">setSequencer</a>, <a href="HierarchicLayouterOptionsGroup.html#setShapeAlignmentWithinLayer(java.lang.String)">setShapeAlignmentWithinLayer</a>, <a href="HierarchicLayouterOptionsGroup.html#setUseGlobalSequencing(boolean)">setUseGlobalSequencing</a>, <a href="HierarchicLayouterOptionsGroup.html#setUseTransposition(boolean)">setUseTransposition</a></code></div>
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
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.StateMachineLayouterOptionsGroup.ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BEZIER">
<h3>BEZIER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BEZIER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.StateMachineLayouterOptionsGroup.BEZIER">Constant Field Values</a></li>
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
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.StateMachineLayouterOptionsGroup.ORTHOGONAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STATE_ROUTING_STYLES">
<h3>STATE_ROUTING_STYLES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">STATE_ROUTING_STYLES</span></div>
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
<h3>StateMachineLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">StateMachineLayouterOptionsGroup</span>()</div>
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
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.layout.state.StateLayoutParams</span> <span class="element-name">initDefaultOptionsValues</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="HierarchicLayouterOptionsGroup.html#initDefaultOptionsValues()">initDefaultOptionsValues</a></code> in class <code><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toLayoutParams()">
<h3>toLayoutParams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.layout.state.StateLayoutParams</span> <span class="element-name">toLayoutParams</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="HierarchicLayouterOptionsGroup.html#toLayoutParams()">toLayoutParams</a></code> in class <code><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParams()">
<h3>createParams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.diagram.ylayout.LayoutParams</span> <span class="element-name">createParams</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="HierarchicLayouterOptionsGroup.html#createParams()">createParams</a></code> in class <code><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></code></dd>
<dt>Returns:</dt>
<dd>new default params object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEdgeRouting()">
<h3>getEdgeRouting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEdgeRouting</span>()</div>
<div class="block">Get route style string</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="HierarchicLayouterOptionsGroup.html#getEdgeRouting()">getEdgeRouting</a></code> in class <code><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></code></dd>
<dt>Returns:</dt>
<dd>string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEdgeRouting(java.lang.String)">
<h3>setEdgeRouting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEdgeRouting</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Set route style for state diagram</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="HierarchicLayouterOptionsGroup.html#setEdgeRouting(java.lang.String)">setEdgeRouting</a></code> in class <code><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></code></dd>
<dt>Parameters:</dt>
<dd><code>s</code> - string value.</dd>
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
