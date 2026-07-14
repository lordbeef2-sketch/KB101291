# JAVA OPENAPI: SwimlaneView (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/symbols/shapes/SwimlaneView.html
- source_path: `com/nomagic/magicdraw/uml/symbols/shapes/SwimlaneView.html`
- source_sha256: `d989dfbbc1d47f453d8e71f51ba75d3bcebd29f2ed3c254898735d01921f6088`
- captured_utc: `2026-07-14T16:46:08.484912+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.shapes](package-summary.html)

## Class SwimlaneView

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.core.impl.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](../paths/PathConnector.html)
[com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement](ShapeElement.html)
com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView<[ActivityPartition](../../../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html),[SwimlaneCellView](SwimlaneCellView.html),[SwimlaneHeaderView](SwimlaneHeaderView.html)>
com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneView

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.diagram.centerlines.CenterlineableShape`, `com.dassault_systemes.modeler.foundation.diagram.symbols.shapes.SuspendShapeAutoResizeModeProvider`, `com.dassault_systemes.modeler.foundation.project.ModelElementProjectProvider`, `[BaseElement](../../BaseElement.html)`, `[MDElement](../../core/MDElement.html)`, `[ModelElementProvider](../../core/ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement`, `[StereotypesDisplayModeOwner](StereotypesDisplayModeOwner.html)`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)`

@OpenApipublic classSwimlaneView
extends com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView<[ActivityPartition](../../../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html),[SwimlaneCellView](SwimlaneCellView.html),[SwimlaneHeaderView](SwimlaneHeaderView.html)>
implements [StereotypesDisplayModeOwner](StereotypesDisplayModeOwner.html), com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView
`DEFAULT_HEADER_WIDTH, DEFAULT_TABLE_HEIGHT`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`CONTAINER_SHAPE_INSETS, SHAPE_DISTANCE_FROM_EDGE`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.[StereotypesDisplayModeOwner](StereotypesDisplayModeOwner.html)
`[DSL_STEREOTYPE_DISPLAY_MODE_ALL](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL), [DSL_STEREOTYPE_DISPLAY_MODE_LAST](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST), [DSL_STEREOTYPE_DISPLAY_MODE_NONE](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE), [DSL_STEREOTYPE_DISPLAY_MODES](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES), [STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES), [STEREOTYPE_DISPLAY_MODE_ICON](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON), [STEREOTYPES_DISPLAY_MODES](StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES), [STEREOTYPES_DISPLAY_MODES_SIMPLE](StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE)`
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView
`canBeAutosized, clone, collectHeadersRecursively, drawClosingBorder, forEachHeader, getAllCells, getAllHeaders, getCellForHeader, getCellsByHeaderModelElement, getCellsForHeader, getChildrenInsets, getDefaultDimension, getHeaders, getHorizontalHeaders, getInnerTableHeadersByHeaderModelElement, getPositionOfHeaderBounds, getPreferredManipulationHeightForHorizontalHeader, getPreferredManipulationWidthForVerticalHeader, getProxyPresentationElementsStream, getRemovableChildren, getTableHeaderByModelElement, getTableHeadersRecursively, getTableHeadersRecursively, getTableShapeStroke, getVerticalHeaders, initializeByChildren, insertHeaderAt, internalAppendChildRect, internalGetPresentationElementStroke, internalLayoutChildren, intersects, isCenterlineInner, isChildLayoutable, isDrawClosingBorder, isLastHeader, isLockLayout, minimumDimensionForShrinking, paintSelf, preferredDimension, removeHeaderFromMaps, removePresentationElement, removeTableHeader, resetMaps, setDrawClosingBorder, setLockLayout, snapsToCenterlines`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`addPresentationElement, addPresentationElement, addPresentationElementWithoutResize, adjustBoundsBeforeChange, adjustChildBoundsForMoving, autosize, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, canAddChild, canMoveChildOutside, checkShowsProxy, childrenBoundsForReshape, clearShowsProxy, constructLayoutHelper, correctChildrenVector, forEachDrawablePresentationElement, getChildrenBounds, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementAt, getPresentationElementIndex, getPresentationElements, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildren, paintChildrenBackground, prefDimensionByManipulatedChildren, recursiveAutosize, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[getConnectedPathElementCount](../paths/PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean,boolean))`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getElement](../PresentationElement.html#getElement()), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getParent](../PresentationElement.html#getParent()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [isSelected](../PresentationElement.html#isSelected()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [useParentStyle](../PresentationElement.html#useParentStyle())`
Methods inherited from class com.nomagic.magicdraw.uml.core.impl.MDElementImpl
`addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getResourceID, getSortKeys, hasListeners, isEditable, mdElementComputeIfAbsentProperty, mdElementGetProperty, mdElementRemoveProperty, mdElementSetOrRemoveProperty, mdElementSetProperty, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, sGetID`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../BaseElement.html)
`[canAdd](../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.centerlines.CenterlineableShape
`getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY`
Methods inherited from interface com.nomagic.magicdraw.utils.[NameOwner](../../../utils/NameOwner.html)
`[getName](../../../utils/NameOwner.html#getName())`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement
`addProperty, getProperty, getPropertyManager`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.shapes</a></div>
<h1 class="title" title="Class SwimlaneView">Class SwimlaneView</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.core.impl.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</a>
<div class="inheritance"><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView&lt;<a href="../../../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>,<wbr/><a href="SwimlaneCellView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SwimlaneCellView</a>,<wbr/><a href="SwimlaneHeaderView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SwimlaneHeaderView</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.SwimlaneView</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.diagram.centerlines.CenterlineableShape</code>, <code>com.dassault_systemes.modeler.foundation.diagram.symbols.shapes.SuspendShapeAutoResizeModeProvider</code>, <code>com.dassault_systemes.modeler.foundation.project.ModelElementProjectProvider</code>, <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../core/MDElement.html" title="interface in com.nomagic.magicdraw.uml.core">MDElement</a></code>, <code><a href="../../core/ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml.core">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</code>, <code><a href="StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SwimlaneView</span>
<span class="extends-implements">extends com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView&lt;<a href="../../../../uml2/ext/magicdraw/activities/mdintermediateactivities/ActivityPartition.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">ActivityPartition</a>,<wbr/><a href="SwimlaneCellView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SwimlaneCellView</a>,<wbr/><a href="SwimlaneHeaderView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SwimlaneHeaderView</a>&gt;
implements <a href="StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a>, com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView">Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView</h3>
<code>DEFAULT_HEADER_WIDTH, DEFAULT_TABLE_HEIGHT</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView">Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</h3>
<code>CONTAINER_SHAPE_INSETS, SHAPE_DISTANCE_FROM_EDGE</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#DASHED_STROKE">DASHED_STROKE</a>, <a href="../PresentationElement.html#DOTTED_STROKE">DOTTED_STROKE</a>, <a href="../PresentationElement.html#SOLID_STROKE">SOLID_STROKE</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.StereotypesDisplayModeOwner">Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.<a href="StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></h3>
<code><a href="StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL">DSL_STEREOTYPE_DISPLAY_MODE_ALL</a>, <a href="StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST">DSL_STEREOTYPE_DISPLAY_MODE_LAST</a>, <a href="StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE">DSL_STEREOTYPE_DISPLAY_MODE_NONE</a>, <a href="StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES">DSL_STEREOTYPE_DISPLAY_MODES</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES">STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON">STEREOTYPE_DISPLAY_MODE_ICON</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE">STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT">STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT">STEREOTYPE_DISPLAY_MODE_TEXT</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON">STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES">STEREOTYPES_DISPLAY_MODES</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE">STEREOTYPES_DISPLAY_MODES_SIMPLE</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView</h3>
<code>canBeAutosized, clone, collectHeadersRecursively, drawClosingBorder, forEachHeader, getAllCells, getAllHeaders, getCellForHeader, getCellsByHeaderModelElement, getCellsForHeader, getChildrenInsets, getDefaultDimension, getHeaders, getHorizontalHeaders, getInnerTableHeadersByHeaderModelElement, getPositionOfHeaderBounds, getPreferredManipulationHeightForHorizontalHeader, getPreferredManipulationWidthForVerticalHeader, getProxyPresentationElementsStream, getRemovableChildren, getTableHeaderByModelElement, getTableHeadersRecursively, getTableHeadersRecursively, getTableShapeStroke, getVerticalHeaders, initializeByChildren, insertHeaderAt, internalAppendChildRect, internalGetPresentationElementStroke, internalLayoutChildren, intersects, isCenterlineInner, isChildLayoutable, isDrawClosingBorder, isLastHeader, isLockLayout, minimumDimensionForShrinking, paintSelf, preferredDimension, removeHeaderFromMaps, removePresentationElement, removeTableHeader, resetMaps, setDrawClosingBorder, setLockLayout, snapsToCenterlines</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</h3>
<code>addPresentationElement, addPresentationElement, addPresentationElementWithoutResize, adjustBoundsBeforeChange, adjustChildBoundsForMoving, autosize, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, canAddChild, canMoveChildOutside, checkShowsProxy, childrenBoundsForReshape, clearShowsProxy, constructLayoutHelper, correctChildrenVector, forEachDrawablePresentationElement, getChildrenBounds, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementAt, getPresentationElementIndex, getPresentationElements, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildren, paintChildrenBackground, prefDimensionByManipulatedChildren, recursiveAutosize, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="../paths/PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="../paths/PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getElement()">getElement</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#useParentStyle()">useParentStyle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.core.impl.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.core.impl.MDElementImpl</h3>
<code>addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getResourceID, getSortKeys, hasListeners, isEditable, mdElementComputeIfAbsentProperty, mdElementGetProperty, mdElementRemoveProperty, mdElementSetOrRemoveProperty, mdElementSetProperty, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, sGetID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../BaseElement.html#isSelfChangeable()">isSelfChangeable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.diagram.centerlines.CenterlineableShape">Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.centerlines.CenterlineableShape</h3>
<code>getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.utils.NameOwner">Methods inherited from interface com.nomagic.magicdraw.utils.<a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></h3>
<code><a href="../../../utils/NameOwner.html#getName()">getName</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement">Methods inherited from interface com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</h3>
<code>addProperty, getProperty, getPropertyManager</code></div>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
