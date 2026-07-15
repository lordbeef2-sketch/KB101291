# JAVA OPENAPI: AssociationView (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/symbols/paths/AssociationView.html
- source_path: `com/nomagic/magicdraw/uml/symbols/paths/AssociationView.html`
- source_sha256: `195be13e779c2f16c7be3fcc5f45c07b4de02f90dad77dbcb8a7c63276c45d56`
- captured_utc: `2026-07-14T16:46:06.487886+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.paths](package-summary.html)

## Class AssociationView

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.core.impl.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](PathConnector.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathElement](PathElement.html)
com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView
com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype
com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView
com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView
com.nomagic.magicdraw.uml.symbols.paths.AssociationView

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.common.compartments.CompartmentSupport`, `com.dassault_systemes.modeler.foundation.diagram.symbols.LabelOwner`, `com.dassault_systemes.modeler.foundation.diagram.symbols.LineJumpDrawer`, `com.dassault_systemes.modeler.foundation.diagram.symbols.paths.PathWithEnds<com.nomagic.magicdraw.uml.symbols.shapes.LinkEndView>`, `com.dassault_systemes.modeler.foundation.diagram.symbols.shapes.SuspendShapeAutoResizeModeProvider`, `com.dassault_systemes.modeler.foundation.project.ModelElementProjectProvider`, `[BaseElement](../../BaseElement.html)`, `[MDElement](../../core/MDElement.html)`, `[ModelElementProvider](../../core/ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement`, `[StereotypesDisplayModeOwner](../shapes/StereotypesDisplayModeOwner.html)`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`[AssociationClassView](AssociationClassView.html)`, `[CommunicationPathView](CommunicationPathView.html)`, `[ExtensionView](ExtensionView.html)`

@OpenApipublic classAssociationView
extends com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView
`NON_NAVIGABILITY_DISTANCE`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathElement](PathElement.html)
`[BEZIER](PathElement.html#BEZIER), [LINE_STYLE](PathElement.html#LINE_STYLE), [OBLIQUE](PathElement.html#OBLIQUE), [RECTILINEAR](PathElement.html#RECTILINEAR)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.[StereotypesDisplayModeOwner](../shapes/StereotypesDisplayModeOwner.html)
`[DSL_STEREOTYPE_DISPLAY_MODE_ALL](../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL), [DSL_STEREOTYPE_DISPLAY_MODE_LAST](../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST), [DSL_STEREOTYPE_DISPLAY_MODE_NONE](../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE), [DSL_STEREOTYPE_DISPLAY_MODES](../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES), [STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES), [STEREOTYPE_DISPLAY_MODE_ICON](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON), [STEREOTYPES_DISPLAY_MODES](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES), [STEREOTYPES_DISPLAY_MODES_SIMPLE](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE)`
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView
`cacheActualDrawPoints, drawNavigability, getActualClientDrawPoint, getActualSupplierDrawPoint, getRoleA, getRoleB, ownsRoleA, ownsRoleB, paintSelf`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView
`calculateAlternativePoints, calculateAltPointsFromEndShapes, clone, getAltPoint1, getAltPoint2, getBoundsToRepaint, getChildPresentationElementForContextMenu, getChildrenWithSymbolProperties, getClientEndShape, getSupplierConnectionType, getSupplierEndShape, internalUpdatePresentationElement, layoutLabelOnNotifyBreakPointsChanged, notifyBreakPointsChanged, setAltPoint1, setAltPoint2, setElement, setLocationForChild, simpleSetBounds, sSetClientEndShape, sSetElement, sSetModelElementsForPathEndShapes, sSetSupplierEndShape`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype
`asPresentationElement, canDisplayConveyedInformation, createCompartmentElements, createInformationFlowSmartListenerConfig, createLabels, createStereotypeLabelWrapper, drawConveyedInformation, getCollections, getConstraintLabelBox, getConstraintLabelWrapper, getConstraintTextMode, getConveyedInformationSourceToTargetLabelWrapper, getConveyedInformationTargetToSourceLabelWrapper, getConveyedSourceToTargetLabelBox, getConveyedTargetToSourceLabelBox, getDSLStereotypesDisplayMode, getElementLabel, getElementPropertiesLabelBox, getElementPropertiesLabelWrapper, getPathAdornmentSize, getStereotypeLabelBox, getStereotypeLabelWrapper, getStereotypesDisplayMode, getTaggedValueLabelBox, getTaggedValueLabelWrapper, internalGetLogicalClientElementForConveyedInformation, isModelElementMandatory, isShowConstraints, isShowConveyedSourceToTarget, isShowConveyedTargetToSource, isShowElementLabel, paintChildren, setCollections, setConstraintTextMode, setDSLStereotypesDisplayMode, setShowConstraints, setShowConveyedSourceToTarget, setShowConveyedTargetToSource, setStereotypesDisplayMode, setVisibleElements, setVisibleElements, sSetConstraintTextMode, sSetDSLStereotypesDisplayMode, sSetShowConstraints, sSetShowConveyedSourceToTarget, sSetShowConveyedTargetToSource, sSetShowTaggedValues, sSetStereotypesDisplayMode`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView
`addLabel, addPresentationElement, canAddChild, clearShowsProxy, constructNameTextToEdit, editName, getEditTextDelegate, getLabelHandler, getManipulatedElementAt, getName, getNameLabelBox, getPresentationElementAt, getPresentationElementIndex, getPresentationElements, getProxyPresentationElementsStream, internalSilentApply, isChildVisible, isLabelWrapText, isNameWrapped, isShowNameBox, notifyBreakPointsChangedForElement, recursiveAutosize, removeLabel, removePresentationElement, sAddPresentationElement, setName, setNameResizeLabel, setNameWrapped, setPresentationElements, setShowNameBox, setSuspendLabelAutoDisplayMode, setSuspendShapeAutoResizeMode, setTextEditable, sRemovePresentationElement, sSetNameWrapped, sSetPresentationElements, sSetShowNameBox, sSetSuspendLabelAutoDisplayMode, updateChildren`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathElement](PathElement.html)
`[getAllBreakPoints](PathElement.html#getAllBreakPoints()), [getBreakPoints](PathElement.html#getBreakPoints()), [getClient](PathElement.html#getClient()), [getClientPoint](PathElement.html#getClientPoint()), [getPointOnPath](PathElement.html#getPointOnPath(java.awt.Point,java.awt.Point,java.util.List,double)), [getSupplier](PathElement.html#getSupplier()), [getSupplierPoint](PathElement.html#getSupplierPoint()), [isConnectable](PathElement.html#isConnectable(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](PathConnector.html)
`[getConnectedPathElementCount](PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](PathConnector.html#getConnectedPathElements(boolean,boolean))`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getParent](../PresentationElement.html#getParent()), [getPreferredDimension](../PresentationElement.html#getPreferredDimension()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [isSelected](../PresentationElement.html#isSelected()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [useParentStyle](../PresentationElement.html#useParentStyle())`
Methods inherited from class com.nomagic.magicdraw.uml.core.impl.MDElementImpl
`addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getResourceID, getSortKeys, hasListeners, isEditable, mdElementComputeIfAbsentProperty, mdElementGetProperty, mdElementRemoveProperty, mdElementSetOrRemoveProperty, mdElementSetProperty, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, sGetID, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../BaseElement.html)
`[canAdd](../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.symbols.LabelOwner
`getModelElement`
Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.symbols.LineJumpDrawer
`getLineWidth`
Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.symbols.paths.PathWithEnds
`asContainerLinkView`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement
`addProperty, getProperty, getPropertyManager`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.paths</a></div>
<h1 class="title" title="Class AssociationView">Class AssociationView</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.core.impl.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</a>
<div class="inheritance"><a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.paths.AssociationView</div>
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
<dd><code>com.dassault_systemes.modeler.foundation.common.compartments.CompartmentSupport</code>, <code>com.dassault_systemes.modeler.foundation.diagram.symbols.LabelOwner</code>, <code>com.dassault_systemes.modeler.foundation.diagram.symbols.LineJumpDrawer</code>, <code>com.dassault_systemes.modeler.foundation.diagram.symbols.paths.PathWithEnds&lt;com.nomagic.magicdraw.uml.symbols.shapes.LinkEndView&gt;</code>, <code>com.dassault_systemes.modeler.foundation.diagram.symbols.shapes.SuspendShapeAutoResizeModeProvider</code>, <code>com.dassault_systemes.modeler.foundation.project.ModelElementProjectProvider</code>, <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../core/MDElement.html" title="interface in com.nomagic.magicdraw.uml.core">MDElement</a></code>, <code><a href="../../core/ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml.core">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</code>, <code><a href="../shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="AssociationClassView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">AssociationClassView</a></code>, <code><a href="CommunicationPathView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">CommunicationPathView</a></code>, <code><a href="ExtensionView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ExtensionView</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">AssociationView</span>
<span class="extends-implements">extends com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView</span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView">Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView</h3>
<code>NON_NAVIGABILITY_DISTANCE</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></h3>
<code><a href="PathElement.html#BEZIER">BEZIER</a>, <a href="PathElement.html#LINE_STYLE">LINE_STYLE</a>, <a href="PathElement.html#OBLIQUE">OBLIQUE</a>, <a href="PathElement.html#RECTILINEAR">RECTILINEAR</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#DASHED_STROKE">DASHED_STROKE</a>, <a href="../PresentationElement.html#DOTTED_STROKE">DOTTED_STROKE</a>, <a href="../PresentationElement.html#SOLID_STROKE">SOLID_STROKE</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.StereotypesDisplayModeOwner">Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.<a href="../shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></h3>
<code><a href="../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL">DSL_STEREOTYPE_DISPLAY_MODE_ALL</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST">DSL_STEREOTYPE_DISPLAY_MODE_LAST</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE">DSL_STEREOTYPE_DISPLAY_MODE_NONE</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES">DSL_STEREOTYPE_DISPLAY_MODES</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES">STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON">STEREOTYPE_DISPLAY_MODE_ICON</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE">STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT">STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT">STEREOTYPE_DISPLAY_MODE_TEXT</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON">STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES">STEREOTYPES_DISPLAY_MODES</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE">STEREOTYPES_DISPLAY_MODES_SIMPLE</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.LinkWithRolesView</h3>
<code>cacheActualDrawPoints, drawNavigability, getActualClientDrawPoint, getActualSupplierDrawPoint, getRoleA, getRoleB, ownsRoleA, ownsRoleB, paintSelf</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.LinkWithEndsView</h3>
<code>calculateAlternativePoints, calculateAltPointsFromEndShapes, clone, getAltPoint1, getAltPoint2, getBoundsToRepaint, getChildPresentationElementForContextMenu, getChildrenWithSymbolProperties, getClientEndShape, getSupplierConnectionType, getSupplierEndShape, internalUpdatePresentationElement, layoutLabelOnNotifyBreakPointsChanged, notifyBreakPointsChanged, setAltPoint1, setAltPoint2, setElement, setLocationForChild, simpleSetBounds, sSetClientEndShape, sSetElement, sSetModelElementsForPathEndShapes, sSetSupplierEndShape</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.LinkWithStereotype</h3>
<code>asPresentationElement, canDisplayConveyedInformation, createCompartmentElements, createInformationFlowSmartListenerConfig, createLabels, createStereotypeLabelWrapper, drawConveyedInformation, getCollections, getConstraintLabelBox, getConstraintLabelWrapper, getConstraintTextMode, getConveyedInformationSourceToTargetLabelWrapper, getConveyedInformationTargetToSourceLabelWrapper, getConveyedSourceToTargetLabelBox, getConveyedTargetToSourceLabelBox, getDSLStereotypesDisplayMode, getElementLabel, getElementPropertiesLabelBox, getElementPropertiesLabelWrapper, getPathAdornmentSize, getStereotypeLabelBox, getStereotypeLabelWrapper, getStereotypesDisplayMode, getTaggedValueLabelBox, getTaggedValueLabelWrapper, internalGetLogicalClientElementForConveyedInformation, isModelElementMandatory, isShowConstraints, isShowConveyedSourceToTarget, isShowConveyedTargetToSource, isShowElementLabel, paintChildren, setCollections, setConstraintTextMode, setDSLStereotypesDisplayMode, setShowConstraints, setShowConveyedSourceToTarget, setShowConveyedTargetToSource, setStereotypesDisplayMode, setVisibleElements, setVisibleElements, sSetConstraintTextMode, sSetDSLStereotypesDisplayMode, sSetShowConstraints, sSetShowConveyedSourceToTarget, sSetShowConveyedTargetToSource, sSetShowTaggedValues, sSetStereotypesDisplayMode</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView</h3>
<code>addLabel, addPresentationElement, canAddChild, clearShowsProxy, constructNameTextToEdit, editName, getEditTextDelegate, getLabelHandler, getManipulatedElementAt, getName, getNameLabelBox, getPresentationElementAt, getPresentationElementIndex, getPresentationElements, getProxyPresentationElementsStream, internalSilentApply, isChildVisible, isLabelWrapText, isNameWrapped, isShowNameBox, notifyBreakPointsChangedForElement, recursiveAutosize, removeLabel, removePresentationElement, sAddPresentationElement, setName, setNameResizeLabel, setNameWrapped, setPresentationElements, setShowNameBox, setSuspendLabelAutoDisplayMode, setSuspendShapeAutoResizeMode, setTextEditable, sRemovePresentationElement, sSetNameWrapped, sSetPresentationElements, sSetShowNameBox, sSetSuspendLabelAutoDisplayMode, updateChildren</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></h3>
<code><a href="PathElement.html#getAllBreakPoints()">getAllBreakPoints</a>, <a href="PathElement.html#getBreakPoints()">getBreakPoints</a>, <a href="PathElement.html#getClient()">getClient</a>, <a href="PathElement.html#getClientPoint()">getClientPoint</a>, <a href="PathElement.html#getPointOnPath(java.awt.Point,java.awt.Point,java.util.List,double)">getPointOnPath</a>, <a href="PathElement.html#getSupplier()">getSupplier</a>, <a href="PathElement.html#getSupplierPoint()">getSupplierPoint</a>, <a href="PathElement.html#isConnectable(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">isConnectable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#useParentStyle()">useParentStyle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.core.impl.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.core.impl.MDElementImpl</h3>
<code>addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getResourceID, getSortKeys, hasListeners, isEditable, mdElementComputeIfAbsentProperty, mdElementGetProperty, mdElementRemoveProperty, mdElementSetOrRemoveProperty, mdElementSetProperty, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, sGetID, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../BaseElement.html#isSelfChangeable()">isSelfChangeable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.diagram.symbols.LabelOwner">Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.symbols.LabelOwner</h3>
<code>getModelElement</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.diagram.symbols.LineJumpDrawer">Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.symbols.LineJumpDrawer</h3>
<code>getLineWidth</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.diagram.symbols.paths.PathWithEnds">Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.symbols.paths.PathWithEnds</h3>
<code>asContainerLinkView</code></div>
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
