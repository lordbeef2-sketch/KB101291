# JAVA OPENAPI: BarView (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/symbols/shapes/BarView.html
- source_path: `com/nomagic/magicdraw/uml/symbols/shapes/BarView.html`
- source_sha256: `b09997c616cea4b95141fdb52bad5551911cb7a62333acc66e2b948c8767ab47`
- captured_utc: `2026-07-14T16:46:07.344897+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.shapes](package-summary.html)

## Class BarView

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.core.impl.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](../paths/PathConnector.html)
[com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement](ShapeElement.html)
com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels
com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels
com.nomagic.magicdraw.uml.symbols.shapes.BarView

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.common.compartments.CompartmentSupport`, `com.dassault_systemes.modeler.foundation.diagram.centerlines.CenterlineableShape`, `com.dassault_systemes.modeler.foundation.diagram.symbols.LabelOwner`, `com.dassault_systemes.modeler.foundation.diagram.symbols.shapes.SuspendShapeAutoResizeModeProvider`, `com.dassault_systemes.modeler.foundation.project.ModelElementProjectProvider`, `[BaseElement](../../BaseElement.html)`, `[MDElement](../../core/MDElement.html)`, `[ModelElementProvider](../../core/ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement`, `[StereotypesDisplayModeOwner](StereotypesDisplayModeOwner.html)`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)`

@OpenApipublic classBarView
extends com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels

Creates synchronization bar view object in activity diagram.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`CONTAINER_SHAPE_INSETS, SHAPE_DISTANCE_FROM_EDGE`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.[StereotypesDisplayModeOwner](StereotypesDisplayModeOwner.html)
`[DSL_STEREOTYPE_DISPLAY_MODE_ALL](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL), [DSL_STEREOTYPE_DISPLAY_MODE_LAST](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST), [DSL_STEREOTYPE_DISPLAY_MODE_NONE](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE), [DSL_STEREOTYPE_DISPLAY_MODES](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES), [STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES), [STEREOTYPE_DISPLAY_MODE_ICON](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON), [STEREOTYPES_DISPLAY_MODES](StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES), [STEREOTYPES_DISPLAY_MODES_SIMPLE](StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE)`
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels
`clone, constructNameText, createConstraintLabelWrapper, createElementPropertiesLabelWrapper, createLabels, createNameLabelWrapper, createSmartListenerConfig, createStereotypeLabelWrapper, createTaggedValueLabelWrapper, getConstraintLabelBox, getConstraintLabelWrapper, getConstraintTextMode, getDSLStereotypesDisplayMode, getElementNumberDisplayMode, getElementPropertiesLabelBox, getElementPropertiesLabelWrapper, getStereotypeLabelBox, getStereotypeLabelWrapper, getStereotypesDisplayMode, getTaggedValueLabelBox, getTaggedValueLabelWrapper, isShowConstraints, isShowElementProperties, isShowNumberTagName, isShowTaggedValues, setConstraintTextMode, setDSLStereotypesDisplayMode, setShowConstraints, setShowElementProperties, setShowTaggedValues, setStereotypesDisplayMode, sSetConstraintTextMode, sSetDSLStereotypesDisplayMode, sSetElementNumberDisplayMode, sSetShowConstraints, sSetShowElementProperties, sSetShowNumberTagName, sSetShowTaggedValues, sSetStereotypesDisplayMode, updateAfterLoad, updateNameBox`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels
`addLabel, asPresentationElement, canAddInstance, canBeAutosized, createCompartmentElements, edgeChanged, editName, getBoundsToRepaint, getCollections, getEditTextDelegate, getHeaderBoundsForPreferredBounds, getLabelHandler, getName, getNameLabelBox, getNameLabelWrapper, internalAppendChildRect, internalPostUpdatePresentationElement, isLabelWrapText, isModelElementMandatory, isShowName, isShowText, isWordWrap, removeLabel, setCollections, setName, setNameResizeLabel, setShowName, setSuspendLabelAutoDisplayMode, setSuspendShapeAutoResizeMode, setTextEditable, setVisibleElements, setWordWrap, simpleSetBounds, sSetElement, sSetName, sSetShowName, sSetSuspendLabelAutoDisplayMode, sSetWordWrap`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
`addExtraChildrenPrefSizePadding, adjustBoundsBeforeChange, autosize, autosizeAndResizeParent, calculateMinY, calculateOvalShapePreferredSize, correctChildrenVector, coversPoint, createBoundsShape, createStateForUpdateOperation, doInternalLayoutChildren, getAdditionalHeaderHeightForPreferredBounds, getChildrenBoundsForPreferredBounds, getHeaderDistanceFromTopForOvalShape, getHeaderInsets, getHeaderMaxYForShrinkableShape, getHeaderObject, getHeaderVerticalPosition, getHeaderVerticalPositionForLayout, getNameLabel, getOvalShapeAvailableWidth, getPreferredBounds, getPresentationElementAt, getProxyPresentationElementsStream, getStereotypesToDisplay, internalGetHeaderBoundsForPreferredBounds, internalGetHeaderInsets, internalLayoutChildren, internalPostSpecificUpdate, internalPreSpecificUpdate, internalSpecificUpdate, internalUpdatePresentationElement, invalidate, isBorderVisible, isChildLayoutable, isContentHidden, isHeaderOrientationVertical, isOvalShape, isParentShowsProxy, minimumDimension, minimumDimensionForShrinking, minimumSizeForShrinkingIgnoringOrientation, paintChildren, preferredDimension, setHeaderObject, setHeaderVerticalPosition, sSetAutosize, sSetHeaderVerticalPosition, switchWidthHeightIfVerticalOrientation`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`addPresentationElement, addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, canAddChild, canMoveChildOutside, checkShowsProxy, childrenBoundsForReshape, clearShowsProxy, constructLayoutHelper, forEachDrawablePresentationElement, getChildrenBounds, getChildrenInsets, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getRemovableChildren, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildrenBackground, prefDimensionByManipulatedChildren, recursiveAutosize, removePresentationElement, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[getConnectedPathElementCount](../paths/PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean,boolean))`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getElement](../PresentationElement.html#getElement()), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getParent](../PresentationElement.html#getParent()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [isSelected](../PresentationElement.html#isSelected()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [useParentStyle](../PresentationElement.html#useParentStyle())`
Methods inherited from class com.nomagic.magicdraw.uml.core.impl.MDElementImpl
`addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getResourceID, getSortKeys, hasListeners, isEditable, mdElementComputeIfAbsentProperty, mdElementGetProperty, mdElementRemoveProperty, mdElementSetOrRemoveProperty, mdElementSetProperty, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, sGetID`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../BaseElement.html)
`[canAdd](../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.centerlines.CenterlineableShape
`getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY`
Methods inherited from interface com.dassault_systemes.modeler.foundation.common.compartments.CompartmentSupport
`setVisibleElements`
Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.symbols.LabelOwner
`getElement, getModelElement`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement
`addProperty, asPresentationElement, getProperty, getPropertyManager`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.shapes</a></div>
<h1 class="title" title="Class BarView">Class BarView</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.core.impl.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</a>
<div class="inheritance"><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.BarView</div>
</div>
</div>
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
<dd><code>com.dassault_systemes.modeler.foundation.common.compartments.CompartmentSupport</code>, <code>com.dassault_systemes.modeler.foundation.diagram.centerlines.CenterlineableShape</code>, <code>com.dassault_systemes.modeler.foundation.diagram.symbols.LabelOwner</code>, <code>com.dassault_systemes.modeler.foundation.diagram.symbols.shapes.SuspendShapeAutoResizeModeProvider</code>, <code>com.dassault_systemes.modeler.foundation.project.ModelElementProjectProvider</code>, <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../core/MDElement.html" title="interface in com.nomagic.magicdraw.uml.core">MDElement</a></code>, <code><a href="../../core/ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml.core">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</code>, <code><a href="StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">BarView</span>
<span class="extends-implements">extends com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</span></div>
<div class="block">Creates synchronization bar view object in activity diagram.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
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
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</h3>
<code>clone, constructNameText, createConstraintLabelWrapper, createElementPropertiesLabelWrapper, createLabels, createNameLabelWrapper, createSmartListenerConfig, createStereotypeLabelWrapper, createTaggedValueLabelWrapper, getConstraintLabelBox, getConstraintLabelWrapper, getConstraintTextMode, getDSLStereotypesDisplayMode, getElementNumberDisplayMode, getElementPropertiesLabelBox, getElementPropertiesLabelWrapper, getStereotypeLabelBox, getStereotypeLabelWrapper, getStereotypesDisplayMode, getTaggedValueLabelBox, getTaggedValueLabelWrapper, isShowConstraints, isShowElementProperties, isShowNumberTagName, isShowTaggedValues, setConstraintTextMode, setDSLStereotypesDisplayMode, setShowConstraints, setShowElementProperties, setShowTaggedValues, setStereotypesDisplayMode, sSetConstraintTextMode, sSetDSLStereotypesDisplayMode, sSetElementNumberDisplayMode, sSetShowConstraints, sSetShowElementProperties, sSetShowNumberTagName, sSetShowTaggedValues, sSetStereotypesDisplayMode, updateAfterLoad, updateNameBox</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels</h3>
<code>addLabel, asPresentationElement, canAddInstance, canBeAutosized, createCompartmentElements, edgeChanged, editName, getBoundsToRepaint, getCollections, getEditTextDelegate, getHeaderBoundsForPreferredBounds, getLabelHandler, getName, getNameLabelBox, getNameLabelWrapper, internalAppendChildRect, internalPostUpdatePresentationElement, isLabelWrapText, isModelElementMandatory, isShowName, isShowText, isWordWrap, removeLabel, setCollections, setName, setNameResizeLabel, setShowName, setSuspendLabelAutoDisplayMode, setSuspendShapeAutoResizeMode, setTextEditable, setVisibleElements, setWordWrap, simpleSetBounds, sSetElement, sSetName, sSetShowName, sSetSuspendLabelAutoDisplayMode, sSetWordWrap</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</h3>
<code>addExtraChildrenPrefSizePadding, adjustBoundsBeforeChange, autosize, autosizeAndResizeParent, calculateMinY, calculateOvalShapePreferredSize, correctChildrenVector, coversPoint, createBoundsShape, createStateForUpdateOperation, doInternalLayoutChildren, getAdditionalHeaderHeightForPreferredBounds, getChildrenBoundsForPreferredBounds, getHeaderDistanceFromTopForOvalShape, getHeaderInsets, getHeaderMaxYForShrinkableShape, getHeaderObject, getHeaderVerticalPosition, getHeaderVerticalPositionForLayout, getNameLabel, getOvalShapeAvailableWidth, getPreferredBounds, getPresentationElementAt, getProxyPresentationElementsStream, getStereotypesToDisplay, internalGetHeaderBoundsForPreferredBounds, internalGetHeaderInsets, internalLayoutChildren, internalPostSpecificUpdate, internalPreSpecificUpdate, internalSpecificUpdate, internalUpdatePresentationElement, invalidate, isBorderVisible, isChildLayoutable, isContentHidden, isHeaderOrientationVertical, isOvalShape, isParentShowsProxy, minimumDimension, minimumDimensionForShrinking, minimumSizeForShrinkingIgnoringOrientation, paintChildren, preferredDimension, setHeaderObject, setHeaderVerticalPosition, sSetAutosize, sSetHeaderVerticalPosition, switchWidthHeightIfVerticalOrientation</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</h3>
<code>addPresentationElement, addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, canAddChild, canMoveChildOutside, checkShowsProxy, childrenBoundsForReshape, clearShowsProxy, constructLayoutHelper, forEachDrawablePresentationElement, getChildrenBounds, getChildrenInsets, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getRemovableChildren, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildrenBackground, prefDimensionByManipulatedChildren, recursiveAutosize, removePresentationElement, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="../paths/PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="../paths/PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getElement()">getElement</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#useParentStyle()">useParentStyle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.core.impl.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.core.impl.MDElementImpl</h3>
<code>addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getResourceID, getSortKeys, hasListeners, isEditable, mdElementComputeIfAbsentProperty, mdElementGetProperty, mdElementRemoveProperty, mdElementSetOrRemoveProperty, mdElementSetProperty, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, sGetID</code></div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.common.compartments.CompartmentSupport">Methods inherited from interface com.dassault_systemes.modeler.foundation.common.compartments.CompartmentSupport</h3>
<code>setVisibleElements</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.diagram.symbols.LabelOwner">Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.symbols.LabelOwner</h3>
<code>getElement, getModelElement</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement">Methods inherited from interface com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</h3>
<code>addProperty, asPresentationElement, getProperty, getPropertyManager</code></div>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
