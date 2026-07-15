# JAVA OPENAPI: ClassDiagramLayouterOptionsGroup (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/options/ClassDiagramLayouterOptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/ClassDiagramLayouterOptionsGroup.html`
- source_sha256: `bf558028c212eabbb69c6586a6a4fd05a3cae0e6ab290dee77798894cda6e04c`
- captured_utc: `2026-07-14T16:55:11.849970+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class ClassDiagramLayouterOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
[com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)
com.nomagic.magicdraw.core.options.ClassDiagramLayouterOptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classClassDiagramLayouterOptionsGroup
extends [HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)

Class Layouter options group.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ASSOCIATION_BASED](#ASSOCIATION_BASED)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[HIERARCHY_BASED](#HIERARCHY_BASED)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ID](#ID)`
Fields inherited from class com.nomagic.magicdraw.core.options.[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)
`[EDGE_ROUTINGS](HierarchicLayouterOptionsGroup.html#EDGE_ROUTINGS), [OBLIQUE](HierarchicLayouterOptionsGroup.html#OBLIQUE), [ORTHOGONAL](HierarchicLayouterOptionsGroup.html#ORTHOGONAL)`
Fields inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[ALIGNMENT_BOTTOM](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_BOTTOM), [ALIGNMENT_CENTER](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_CENTER), [ALIGNMENT_TOP](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_TOP), [LAYOUT_LABEL_CONSIDERATION](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION), [LAYOUT_LABEL_CONSIDERATION_FULL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_FULL), [LAYOUT_LABEL_CONSIDERATION_NONE](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_NONE), [LAYOUT_LABEL_CONSIDERATION_PARTIAL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_PARTIAL), [MAX_INT_VALUE](AbstractDiagramLayouterOptionsGroup.html#MAX_INT_VALUE), [SHAPE_ALIGNMENT](AbstractDiagramLayouterOptionsGroup.html#SHAPE_ALIGNMENT)`
Fields inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](OptionsGroup.html)
`[ICON_ENVIRONMENT_OPTIONS](OptionsGroup.html#ICON_ENVIRONMENT_OPTIONS)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ClassDiagramLayouterOptionsGroup](#%3Cinit%3E())()`
Construct ClassDiagramLayouterOptionsGroup
`[ClassDiagramLayouterOptionsGroup](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`boolean`
`[getBuildContainmentHierarchies](#getBuildContainmentHierarchies())()`
Get Build Containment Hierarchies property value in order organized
 classes connected by containment paths into hierarchies.
`boolean`
`[getBuildGeneralizationHierarchies](#getBuildGeneralizationHierarchies())()`
Get Build Generalization Hierarchies
`boolean`
`[getBuildRealizationHierarchies](#getBuildRealizationHierarchies())()`
Get Build Realization Hierarchies property value
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?>>`
`[getHierarchyLinks](#getHierarchyLinks())()`
Set Hierarchy Links.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLayoutType](#getLayoutType())()`
Deprecated.
has no affect anymore, will be removed in later versions.
`protected void`
`[initCommonDefaultValues](#initCommonDefaultValues())()`

`void`
`[setBuildContainmentHierarchies](#setBuildContainmentHierarchies(boolean))(boolean b)`
Set Build Containment Hierarchies property value in order to organize
 classes connected by containment paths into hierarchies.
`void`
`[setBuildGeneralizationHierarchies](#setBuildGeneralizationHierarchies(boolean))(boolean b)`
Set Build Generalization Hierarchies property value in order to organize
 classes connected by generalization paths into hierarchies.
`void`
`[setBuildRealizationHierarchies](#setBuildRealizationHierarchies(boolean))(boolean b)`
Set Build Realization Hierarchies property value in order to organize
 classes connected by realization paths into hierarchies.
`void`
`[setLayoutType](#setLayoutType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)`
Deprecated.
has no affect anymore, will be removed in later versions.
Methods inherited from class com.nomagic.magicdraw.core.options.[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)
`[addProperty](HierarchicLayouterOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)), [afterLoad](HierarchicLayouterOptionsGroup.html#afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean)), [getBackloopRouting](HierarchicLayouterOptionsGroup.html#getBackloopRouting()), [getConsiderLayoutTemplates](HierarchicLayouterOptionsGroup.html#getConsiderLayoutTemplates()), [getCopy](HierarchicLayouterOptionsGroup.html#getCopy()), [getEdgeRouting](HierarchicLayouterOptionsGroup.html#getEdgeRouting()), [getLayoutLabelConsideration](HierarchicLayouterOptionsGroup.html#getLayoutLabelConsideration()), [getLayoutOnlyTopLevel](HierarchicLayouterOptionsGroup.html#getLayoutOnlyTopLevel()), [getMakeSubTrees](HierarchicLayouterOptionsGroup.html#getMakeSubTrees()), [getMinimalFirstSegmentLength](HierarchicLayouterOptionsGroup.html#getMinimalFirstSegmentLength()), [getMinimalLayerDistance](HierarchicLayouterOptionsGroup.html#getMinimalLayerDistance()), [getMinimalLinkDistance](HierarchicLayouterOptionsGroup.html#getMinimalLinkDistance()), [getMinimalShapeDistance](HierarchicLayouterOptionsGroup.html#getMinimalShapeDistance()), [getOrientation](HierarchicLayouterOptionsGroup.html#getOrientation()), [getRemoveFalseCrossings](HierarchicLayouterOptionsGroup.html#getRemoveFalseCrossings()), [getSequencer](HierarchicLayouterOptionsGroup.html#getSequencer()), [getShapeAlignmentWithinLayer](HierarchicLayouterOptionsGroup.html#getShapeAlignmentWithinLayer()), [getUseGlobalSequencing](HierarchicLayouterOptionsGroup.html#getUseGlobalSequencing()), [getUseTransposition](HierarchicLayouterOptionsGroup.html#getUseTransposition()), [isLayoutOnlyTopLevel](HierarchicLayouterOptionsGroup.html#isLayoutOnlyTopLevel()), [setBackloopRouting](HierarchicLayouterOptionsGroup.html#setBackloopRouting(boolean)), [setConsiderLayoutTemplates](HierarchicLayouterOptionsGroup.html#setConsiderLayoutTemplates(boolean)), [setEdgeRouting](HierarchicLayouterOptionsGroup.html#setEdgeRouting(java.lang.String)), [setLayoutLabelConsideration](HierarchicLayouterOptionsGroup.html#setLayoutLabelConsideration(java.lang.String)), [setLayoutOnlyTopLevel](HierarchicLayouterOptionsGroup.html#setLayoutOnlyTopLevel(boolean)), [setMakeSubTrees](HierarchicLayouterOptionsGroup.html#setMakeSubTrees(boolean)), [setMinimalFirstSegmentLength](HierarchicLayouterOptionsGroup.html#setMinimalFirstSegmentLength(int)), [setMinimalLayerDistance](HierarchicLayouterOptionsGroup.html#setMinimalLayerDistance(int)), [setMinimalLinkDistance](HierarchicLayouterOptionsGroup.html#setMinimalLinkDistance(int)), [setMinimalShapeDistance](HierarchicLayouterOptionsGroup.html#setMinimalShapeDistance(int)), [setOrientation](HierarchicLayouterOptionsGroup.html#setOrientation(java.lang.String)), [setRemoveFalseCrossings](HierarchicLayouterOptionsGroup.html#setRemoveFalseCrossings(boolean)), [setSequencer](HierarchicLayouterOptionsGroup.html#setSequencer(java.lang.String)), [setShapeAlignmentWithinLayer](HierarchicLayouterOptionsGroup.html#setShapeAlignmentWithinLayer(java.lang.String)), [setUseGlobalSequencing](HierarchicLayouterOptionsGroup.html#setUseGlobalSequencing(boolean)), [setUseTransposition](HierarchicLayouterOptionsGroup.html#setUseTransposition(boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[getMakePreferredLayoutSize](AbstractDiagramLayouterOptionsGroup.html#getMakePreferredLayoutSize()), [getOptimizeLabelOrientations](AbstractDiagramLayouterOptionsGroup.html#getOptimizeLabelOrientations()), [isMoveToFreeSpace](AbstractDiagramLayouterOptionsGroup.html#isMoveToFreeSpace()), [setDefaultValues](AbstractDiagramLayouterOptionsGroup.html#setDefaultValues()), [setMakePreferredLayoutSize](AbstractDiagramLayouterOptionsGroup.html#setMakePreferredLayoutSize(boolean)), [setMoveToFreeSpace](AbstractDiagramLayouterOptionsGroup.html#setMoveToFreeSpace(boolean)), [setOptimizeLabelOrientations](AbstractDiagramLayouterOptionsGroup.html#setOptimizeLabelOrientations(boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
`[addInvisibleProperty](AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)), [afterLoadAdditionalAction](AbstractPropertyOptionsGroup.html#afterLoadAdditionalAction(boolean)), [beforeLoad](AbstractPropertyOptionsGroup.html#beforeLoad(boolean)), [clone](AbstractPropertyOptionsGroup.html#clone()), [createDefault](AbstractPropertyOptionsGroup.html#createDefault()), [createOptions](AbstractPropertyOptionsGroup.html#createOptions()), [createOptionsPanel](AbstractPropertyOptionsGroup.html#createOptionsPanel()), [fixProperty](AbstractPropertyOptionsGroup.html#fixProperty(java.lang.String,java.lang.Runnable)), [getOptions](AbstractPropertyOptionsGroup.html#getOptions()), [getOptionsToSave](AbstractPropertyOptionsGroup.html#getOptionsToSave()), [getProperty](AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)), [getVisibleOptions](AbstractPropertyOptionsGroup.html#getVisibleOptions()), [hasVisibleOptions](AbstractPropertyOptionsGroup.html#hasVisibleOptions()), [loadOptions](AbstractPropertyOptionsGroup.html#loadOptions(com.nomagic.magicdraw.properties.Style,boolean)), [removeProperty](AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)), [setOptions](AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)), [setPropertiesInvisible](AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)), [setPropertyInvisible](AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](OptionsGroup.html)
`[add](OptionsGroup.html#add(com.nomagic.magicdraw.core.options.OptionsGroup)), [afterSave](OptionsGroup.html#afterSave()), [canDisplay](OptionsGroup.html#canDisplay(com.nomagic.magicdraw.usermodes.UserMode)), [firstInit](OptionsGroup.html#firstInit(boolean)), [getBanner](OptionsGroup.html#getBanner()), [getChildren](OptionsGroup.html#getChildren()), [getGroupIcon](OptionsGroup.html#getGroupIcon()), [getIcon](OptionsGroup.html#getIcon()), [getId](OptionsGroup.html#getId()), [getModelingLanguage](OptionsGroup.html#getModelingLanguage()), [getName](OptionsGroup.html#getName()), [getParent](OptionsGroup.html#getParent()), [isEnabled](OptionsGroup.html#isEnabled()), [isVisible](OptionsGroup.html#isVisible()), [remove](OptionsGroup.html#remove(com.nomagic.magicdraw.core.options.OptionsGroup)), [resetCachedValues](OptionsGroup.html#resetCachedValues()), [setEnabled](OptionsGroup.html#setEnabled(boolean)), [setVisible](OptionsGroup.html#setVisible(boolean)), [sortChildren](OptionsGroup.html#sortChildren(java.util.Comparator))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ID
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ID
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ClassDiagramLayouterOptionsGroup.ID)
HIERARCHY_BASED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) HIERARCHY_BASED
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ClassDiagramLayouterOptionsGroup.HIERARCHY_BASED)
ASSOCIATION_BASED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ASSOCIATION_BASED
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ClassDiagramLayouterOptionsGroup.ASSOCIATION_BASED)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ClassDiagramLayouterOptionsGroup
public ClassDiagramLayouterOptionsGroup()
Construct ClassDiagramLayouterOptionsGroup
ClassDiagramLayouterOptionsGroup
public ClassDiagramLayouterOptionsGroup([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId)
 ============ METHOD DETAIL ========== 
Method Details
initCommonDefaultValues
protected void initCommonDefaultValues()
Overrides:
`[initCommonDefaultValues](HierarchicLayouterOptionsGroup.html#initCommonDefaultValues())` in class `[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)`
getLayoutType
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLayoutType()
Deprecated.
has no affect anymore, will be removed in later versions.
Get String representation of layout.
Returns:
string value.
setLayoutType
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setLayoutType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)
Deprecated.
has no affect anymore, will be removed in later versions.
Set layout type.
Parameters:
`s` - layout type.
setBuildGeneralizationHierarchies
public void setBuildGeneralizationHierarchies(boolean b)
Set Build Generalization Hierarchies property value in order to organize
 classes connected by generalization paths into hierarchies.
Parameters:
`b` - value.
getBuildGeneralizationHierarchies
public boolean getBuildGeneralizationHierarchies()
Get Build Generalization Hierarchies
Returns:
boolean value.
setBuildRealizationHierarchies
public void setBuildRealizationHierarchies(boolean b)
Set Build Realization Hierarchies property value in order to organize
 classes connected by realization paths into hierarchies.
Parameters:
`b` - boolean value.
getBuildRealizationHierarchies
public boolean getBuildRealizationHierarchies()
Get Build Realization Hierarchies property value
Returns:
boolean value.
setBuildContainmentHierarchies
public void setBuildContainmentHierarchies(boolean b)
Set Build Containment Hierarchies property value in order to organize
 classes connected by containment paths into hierarchies.
Parameters:
`b` - set to true to build containment paths into a hierarchy, false otherwise
getBuildContainmentHierarchies
public boolean getBuildContainmentHierarchies()
Get Build Containment Hierarchies property value in order organized
 classes connected by containment paths into hierarchies.
Returns:
boolean value
getHierarchyLinks
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?>> getHierarchyLinks()
Set Hierarchy Links.
Returns:
Set.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class ClassDiagramLayouterOptionsGroup">Class ClassDiagramLayouterOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance"><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup</a>
<div class="inheritance"><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.ClassDiagramLayouterOptionsGroup</div>
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
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ClassDiagramLayouterOptionsGroup</span>
<span class="extends-implements">extends <a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></span></div>
<div class="block">Class Layouter options group.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ASSOCIATION_BASED">ASSOCIATION_BASED</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#HIERARCHY_BASED">HIERARCHY_BASED</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ID">ID</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.<a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></h3>
<code><a href="HierarchicLayouterOptionsGroup.html#EDGE_ROUTINGS">EDGE_ROUTINGS</a>, <a href="HierarchicLayouterOptionsGroup.html#OBLIQUE">OBLIQUE</a>, <a href="HierarchicLayouterOptionsGroup.html#ORTHOGONAL">ORTHOGONAL</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></h3>
<code><a href="AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_BOTTOM">ALIGNMENT_BOTTOM</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_CENTER">ALIGNMENT_CENTER</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_TOP">ALIGNMENT_TOP</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION">LAYOUT_LABEL_CONSIDERATION</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_FULL">LAYOUT_LABEL_CONSIDERATION_FULL</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_NONE">LAYOUT_LABEL_CONSIDERATION_NONE</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_PARTIAL">LAYOUT_LABEL_CONSIDERATION_PARTIAL</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#MAX_INT_VALUE">MAX_INT_VALUE</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#SHAPE_ALIGNMENT">SHAPE_ALIGNMENT</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="OptionsGroup.html#ICON_ENVIRONMENT_OPTIONS">ICON_ENVIRONMENT_OPTIONS</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ClassDiagramLayouterOptionsGroup</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Construct ClassDiagramLayouterOptionsGroup</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">ClassDiagramLayouterOptionsGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId)</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBuildContainmentHierarchies()">getBuildContainmentHierarchies</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Build Containment Hierarchies property value in order organized
 classes connected by containment paths into hierarchies.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBuildGeneralizationHierarchies()">getBuildGeneralizationHierarchies</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Build Generalization Hierarchies</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBuildRealizationHierarchies()">getBuildRealizationHierarchies</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Build Realization Hierarchies property value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHierarchyLinks()">getHierarchyLinks</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Hierarchy Links.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getLayoutType()">getLayoutType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">has no affect anymore, will be removed in later versions.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initCommonDefaultValues()">initCommonDefaultValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBuildContainmentHierarchies(boolean)">setBuildContainmentHierarchies</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Build Containment Hierarchies property value in order to organize
 classes connected by containment paths into hierarchies.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBuildGeneralizationHierarchies(boolean)">setBuildGeneralizationHierarchies</a><wbr/>(boolean b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Build Generalization Hierarchies property value in order to organize
 classes connected by generalization paths into hierarchies.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBuildRealizationHierarchies(boolean)">setBuildRealizationHierarchies</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Build Realization Hierarchies property value in order to organize
 classes connected by realization paths into hierarchies.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setLayoutType(java.lang.String)">setLayoutType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">has no affect anymore, will be removed in later versions.</div>
</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></h3>
<code><a href="HierarchicLayouterOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="HierarchicLayouterOptionsGroup.html#afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean)">afterLoad</a>, <a href="HierarchicLayouterOptionsGroup.html#getBackloopRouting()">getBackloopRouting</a>, <a href="HierarchicLayouterOptionsGroup.html#getConsiderLayoutTemplates()">getConsiderLayoutTemplates</a>, <a href="HierarchicLayouterOptionsGroup.html#getCopy()">getCopy</a>, <a href="HierarchicLayouterOptionsGroup.html#getEdgeRouting()">getEdgeRouting</a>, <a href="HierarchicLayouterOptionsGroup.html#getLayoutLabelConsideration()">getLayoutLabelConsideration</a>, <a href="HierarchicLayouterOptionsGroup.html#getLayoutOnlyTopLevel()">getLayoutOnlyTopLevel</a>, <a href="HierarchicLayouterOptionsGroup.html#getMakeSubTrees()">getMakeSubTrees</a>, <a href="HierarchicLayouterOptionsGroup.html#getMinimalFirstSegmentLength()">getMinimalFirstSegmentLength</a>, <a href="HierarchicLayouterOptionsGroup.html#getMinimalLayerDistance()">getMinimalLayerDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#getMinimalLinkDistance()">getMinimalLinkDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#getMinimalShapeDistance()">getMinimalShapeDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#getOrientation()">getOrientation</a>, <a href="HierarchicLayouterOptionsGroup.html#getRemoveFalseCrossings()">getRemoveFalseCrossings</a>, <a href="HierarchicLayouterOptionsGroup.html#getSequencer()">getSequencer</a>, <a href="HierarchicLayouterOptionsGroup.html#getShapeAlignmentWithinLayer()">getShapeAlignmentWithinLayer</a>, <a href="HierarchicLayouterOptionsGroup.html#getUseGlobalSequencing()">getUseGlobalSequencing</a>, <a href="HierarchicLayouterOptionsGroup.html#getUseTransposition()">getUseTransposition</a>, <a href="HierarchicLayouterOptionsGroup.html#isLayoutOnlyTopLevel()">isLayoutOnlyTopLevel</a>, <a href="HierarchicLayouterOptionsGroup.html#setBackloopRouting(boolean)">setBackloopRouting</a>, <a href="HierarchicLayouterOptionsGroup.html#setConsiderLayoutTemplates(boolean)">setConsiderLayoutTemplates</a>, <a href="HierarchicLayouterOptionsGroup.html#setEdgeRouting(java.lang.String)">setEdgeRouting</a>, <a href="HierarchicLayouterOptionsGroup.html#setLayoutLabelConsideration(java.lang.String)">setLayoutLabelConsideration</a>, <a href="HierarchicLayouterOptionsGroup.html#setLayoutOnlyTopLevel(boolean)">setLayoutOnlyTopLevel</a>, <a href="HierarchicLayouterOptionsGroup.html#setMakeSubTrees(boolean)">setMakeSubTrees</a>, <a href="HierarchicLayouterOptionsGroup.html#setMinimalFirstSegmentLength(int)">setMinimalFirstSegmentLength</a>, <a href="HierarchicLayouterOptionsGroup.html#setMinimalLayerDistance(int)">setMinimalLayerDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#setMinimalLinkDistance(int)">setMinimalLinkDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#setMinimalShapeDistance(int)">setMinimalShapeDistance</a>, <a href="HierarchicLayouterOptionsGroup.html#setOrientation(java.lang.String)">setOrientation</a>, <a href="HierarchicLayouterOptionsGroup.html#setRemoveFalseCrossings(boolean)">setRemoveFalseCrossings</a>, <a href="HierarchicLayouterOptionsGroup.html#setSequencer(java.lang.String)">setSequencer</a>, <a href="HierarchicLayouterOptionsGroup.html#setShapeAlignmentWithinLayer(java.lang.String)">setShapeAlignmentWithinLayer</a>, <a href="HierarchicLayouterOptionsGroup.html#setUseGlobalSequencing(boolean)">setUseGlobalSequencing</a>, <a href="HierarchicLayouterOptionsGroup.html#setUseTransposition(boolean)">setUseTransposition</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></h3>
<code><a href="AbstractDiagramLayouterOptionsGroup.html#getMakePreferredLayoutSize()">getMakePreferredLayoutSize</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#getOptimizeLabelOrientations()">getOptimizeLabelOrientations</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#isMoveToFreeSpace()">isMoveToFreeSpace</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setDefaultValues()">setDefaultValues</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setMakePreferredLayoutSize(boolean)">setMakePreferredLayoutSize</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setMoveToFreeSpace(boolean)">setMoveToFreeSpace</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setOptimizeLabelOrientations(boolean)">setOptimizeLabelOrientations</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></h3>
<code><a href="AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#afterLoadAdditionalAction(boolean)">afterLoadAdditionalAction</a>, <a href="AbstractPropertyOptionsGroup.html#beforeLoad(boolean)">beforeLoad</a>, <a href="AbstractPropertyOptionsGroup.html#clone()">clone</a>, <a href="AbstractPropertyOptionsGroup.html#createDefault()">createDefault</a>, <a href="AbstractPropertyOptionsGroup.html#createOptions()">createOptions</a>, <a href="AbstractPropertyOptionsGroup.html#createOptionsPanel()">createOptionsPanel</a>, <a href="AbstractPropertyOptionsGroup.html#fixProperty(java.lang.String,java.lang.Runnable)">fixProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getOptions()">getOptions</a>, <a href="AbstractPropertyOptionsGroup.html#getOptionsToSave()">getOptionsToSave</a>, <a href="AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)">getProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getVisibleOptions()">getVisibleOptions</a>, <a href="AbstractPropertyOptionsGroup.html#hasVisibleOptions()">hasVisibleOptions</a>, <a href="AbstractPropertyOptionsGroup.html#loadOptions(com.nomagic.magicdraw.properties.Style,boolean)">loadOptions</a>, <a href="AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)">removeProperty</a>, <a href="AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)">setOptions</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)">setPropertiesInvisible</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean)">setPropertyInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="OptionsGroup.html#add(com.nomagic.magicdraw.core.options.OptionsGroup)">add</a>, <a href="OptionsGroup.html#afterSave()">afterSave</a>, <a href="OptionsGroup.html#canDisplay(com.nomagic.magicdraw.usermodes.UserMode)">canDisplay</a>, <a href="OptionsGroup.html#firstInit(boolean)">firstInit</a>, <a href="OptionsGroup.html#getBanner()">getBanner</a>, <a href="OptionsGroup.html#getChildren()">getChildren</a>, <a href="OptionsGroup.html#getGroupIcon()">getGroupIcon</a>, <a href="OptionsGroup.html#getIcon()">getIcon</a>, <a href="OptionsGroup.html#getId()">getId</a>, <a href="OptionsGroup.html#getModelingLanguage()">getModelingLanguage</a>, <a href="OptionsGroup.html#getName()">getName</a>, <a href="OptionsGroup.html#getParent()">getParent</a>, <a href="OptionsGroup.html#isEnabled()">isEnabled</a>, <a href="OptionsGroup.html#isVisible()">isVisible</a>, <a href="OptionsGroup.html#remove(com.nomagic.magicdraw.core.options.OptionsGroup)">remove</a>, <a href="OptionsGroup.html#resetCachedValues()">resetCachedValues</a>, <a href="OptionsGroup.html#setEnabled(boolean)">setEnabled</a>, <a href="OptionsGroup.html#setVisible(boolean)">setVisible</a>, <a href="OptionsGroup.html#sortChildren(java.util.Comparator)">sortChildren</a></code></div>
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
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ClassDiagramLayouterOptionsGroup.ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HIERARCHY_BASED">
<h3>HIERARCHY_BASED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HIERARCHY_BASED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ClassDiagramLayouterOptionsGroup.HIERARCHY_BASED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASSOCIATION_BASED">
<h3>ASSOCIATION_BASED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ASSOCIATION_BASED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.ClassDiagramLayouterOptionsGroup.ASSOCIATION_BASED">Constant Field Values</a></li>
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
<h3>ClassDiagramLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ClassDiagramLayouterOptionsGroup</span>()</div>
<div class="block">Construct ClassDiagramLayouterOptionsGroup</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>ClassDiagramLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ClassDiagramLayouterOptionsGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId)</span></div>
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
<section class="detail" id="getLayoutType()">
<h3>getLayoutType</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLayoutType</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">has no affect anymore, will be removed in later versions.</div>
</div>
<div class="block">Get String representation of layout.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>string value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLayoutType(java.lang.String)">
<h3>setLayoutType</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayoutType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">has no affect anymore, will be removed in later versions.</div>
</div>
<div class="block">Set layout type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - layout type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBuildGeneralizationHierarchies(boolean)">
<h3>setBuildGeneralizationHierarchies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBuildGeneralizationHierarchies</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Build Generalization Hierarchies property value in order to organize
 classes connected by generalization paths into hierarchies.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBuildGeneralizationHierarchies()">
<h3>getBuildGeneralizationHierarchies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getBuildGeneralizationHierarchies</span>()</div>
<div class="block">Get Build Generalization Hierarchies</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBuildRealizationHierarchies(boolean)">
<h3>setBuildRealizationHierarchies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBuildRealizationHierarchies</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Build Realization Hierarchies property value in order to organize
 classes connected by realization paths into hierarchies.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBuildRealizationHierarchies()">
<h3>getBuildRealizationHierarchies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getBuildRealizationHierarchies</span>()</div>
<div class="block">Get Build Realization Hierarchies property value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBuildContainmentHierarchies(boolean)">
<h3>setBuildContainmentHierarchies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBuildContainmentHierarchies</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Build Containment Hierarchies property value in order to organize
 classes connected by containment paths into hierarchies.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - set to true to build containment paths into a hierarchy, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBuildContainmentHierarchies()">
<h3>getBuildContainmentHierarchies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getBuildContainmentHierarchies</span>()</div>
<div class="block">Get Build Containment Hierarchies property value in order organized
 classes connected by containment paths into hierarchies.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHierarchyLinks()">
<h3>getHierarchyLinks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt;&gt;</span> <span class="element-name">getHierarchyLinks</span>()</div>
<div class="block">Set Hierarchy Links.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Set.</dd>
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
