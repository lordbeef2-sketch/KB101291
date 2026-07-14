# JAVA OPENAPI: PathConnector (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/paths/PathConnector.html
- source_path: `com/nomagic/magicdraw/uml/symbols/paths/PathConnector.html`
- source_sha256: `d74d9780bc735bfc4d8e16752577a8c18014442fda82ec786cd379afb48d5d0f`
- captured_utc: `2026-07-14T16:56:01.267522+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.paths](package-summary.html)

## Class PathConnector

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
com.nomagic.magicdraw.uml.symbols.paths.PathConnector

All Implemented Interfaces:
`[BaseElement](../../BaseElement.html)`, `[MDElement](../../MDElement.html)`, `[ModelElementProvider](../../ModelElementProvider.html)`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`[PathElement](PathElement.html)`, `[ShapeElement](../shapes/ShapeElement.html)`

@OpenApipublic abstract classPathConnector
extends [PresentationElement](../PresentationElement.html)

This class is base class for presentation elements connectible by some path element.
 This means that instance of this class can have incoming or outgoing path elements.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[showsProxy](#showsProxy)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DEFAULT_LINE_WIDTH](../PresentationElement.html#DEFAULT_LINE_WIDTH), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [HANDLE_SIZE](../PresentationElement.html#HANDLE_SIZE), [MAX_LINE_WIDTH](../PresentationElement.html#MAX_LINE_WIDTH), [MIN_LINE_WIDTH](../PresentationElement.html#MIN_LINE_WIDTH), [peStyle](../PresentationElement.html#peStyle), [SHADOW_WIDTH](../PresentationElement.html#SHADOW_WIDTH), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PathConnector](#%3Cinit%3E())()`

`[PathConnector](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) v)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../../Visitor.html) visitor)`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
`boolean`
`[addConnectedPathElement](#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](PathElement.html) element)`
Adds a new path element, and recalculates its position.
`protected boolean`
`[checkShowsProxy](#checkShowsProxy())()`

`void`
`[clearShowsProxy](#clearShowsProxy())()`

`[PathConnector](PathConnector.html)`
`[clone](#clone())()`

`protected void`
`[createSmartListenerConfig](#createSmartListenerConfig(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)`

`void`
`[dispose](#dispose())()`
disposes ends of links when link is deleted
`protected void`
`[disposeConnectedPaths](#disposeConnectedPaths())()`

`[PresentationElement](../PresentationElement.html)`
`[findSymbolForEnd](#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [PresentationElement](../PresentationElement.html)> preferredEndType,
 boolean asClient)`
Find symbol for the Path end (client or supplier)
`protected [PresentationElement](../PresentationElement.html)`
`[findSymbolForEnd](#findSymbolForEnd(java.util.stream.Stream,boolean))([Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[PresentationElement](../PresentationElement.html)> elements,
 boolean asClient)`

`[PathElement](PathElement.html)`
`[getConnectedPathElement](#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`
Return a connected path with a given model element
`final int`
`[getConnectedPathElementCount](#getConnectedPathElementCount())()`
Returns number of connected path elements.
`final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](PathElement.html)>`
`[getConnectedPathElements](#getConnectedPathElements())()`
Returns connected path elements.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](PathElement.html)>`
`[getConnectedPathElements](#getConnectedPathElements(boolean))(boolean incoming)`
Returns connected path elements by direction.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](PathElement.html)>`
`[getConnectedPathElements](#getConnectedPathElements(boolean,boolean))(boolean incoming,
 boolean excludeToSelf)`
Returns connected path elements by direction with an option to exclude paths to self
`int`
`[getPreferredArrowLength](#getPreferredArrowLength())()`

`final boolean`
`[isShowsProxy](#isShowsProxy())()`

`final void`
`[movePathElement](#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean))([PathElement](PathElement.html) path,
 boolean notify)`
Calculates position of a path element.
`protected abstract void`
`[movePathElement](#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector))([PathElement](PathElement.html) element,
 [PathConnector](PathConnector.html) requestor)`
Calculates position of a path element.
`void`
`[movePathElements](#movePathElements())()`

`boolean`
`[removeConnectedPathElement](#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](PathElement.html) link)`
Removes path element.
`boolean`
`[sAddConnectedPathElement](#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](PathElement.html) element)`
Adds a new path element.
`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](PathElement.html)>`
`[selectPathsForMoving](#selectPathsForMoving(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../PresentationElement.html)> subPresentationElements)`
Select paths to move with current symbol from deep structure.
`void`
`[setParent](#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) parent)`
Sets parent for this view.
`void`
`[setVisibility](#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility))(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)`
Sets element visibility flag.
`boolean`
`[sRemoveConnectedPathElement](#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](PathElement.html) element)`
Removes path element.
`void`
`[sSetConnectedPathElements](#sSetConnectedPathElements(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](PathElement.html)> paths)`
Sets new path elements.
`void`
`[sSetVisibility](#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility))(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)`
Sets element visibility flag.
`protected boolean`
`[supportsVisibleConnectedPathElementsIfSelfInvisible](#supportsVisibleConnectedPathElementsIfSelfInvisible())()`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[addPresentationElement](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addPresentationElement](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)), [addPresentationElementWithoutResize](../PresentationElement.html#addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addProperty](../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [adjustBoundsBeforeChange](../PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)), [adjustChildBounds](../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [adjustChildBoundsForMoving](../PresentationElement.html#adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [alwaysShowTooltip](../PresentationElement.html#alwaysShowTooltip()), [applyProperties](../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [askDeleteDataConfirmation](../PresentationElement.html#askDeleteDataConfirmation()), [atInsert](../PresentationElement.html#atInsert()), [atInsertChildren](../PresentationElement.html#atInsertChildren()), [autosizeAndResizeManipulatedParent](../PresentationElement.html#autosizeAndResizeManipulatedParent()), [autosizeAndResizeParent](../PresentationElement.html#autosizeAndResizeParent()), [beforeDelete](../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)), [boundsChanged](../PresentationElement.html#boundsChanged()), [boundsChanged](../PresentationElement.html#boundsChanged(java.awt.Rectangle)), [canAddChild](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)), [canAddChild](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [canAddInstance](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canAddInstance](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [canBeDisposedOnUpdate](../PresentationElement.html#canBeDisposedOnUpdate()), [canChangeElementOwner](../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canFill](../PresentationElement.html#canFill()), [canHavePaths](../PresentationElement.html#canHavePaths()), [changeProperties](../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [checkElementOwnerOnChange](../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [checkProxyVisibility](../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [childrenForMoving](../PresentationElement.html#childrenForMoving()), [collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)), [collectSubShowingPresentationElements](../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)), [coversPoint](../PresentationElement.html#coversPoint(int,int)), [coversPoint](../PresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [createFillStrategy](../PresentationElement.html#createFillStrategy()), [createPresentationElementStyle](../PresentationElement.html#createPresentationElementStyle()), [createPropertyChangeListener](../PresentationElement.html#createPropertyChangeListener()), [disposeChildren](../PresentationElement.html#disposeChildren()), [disposePropertyChangeListener](../PresentationElement.html#disposePropertyChangeListener()), [draw](../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawBackground](../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbol](../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbolBackground](../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [dynamicFillColor](../PresentationElement.html#dynamicFillColor()), [dynamicLineColor](../PresentationElement.html#dynamicLineColor()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth(int)), [dynamicPaintShadow](../PresentationElement.html#dynamicPaintShadow()), [dynamicStroke](../PresentationElement.html#dynamicStroke()), [dynamicStroke](../PresentationElement.html#dynamicStroke(int)), [dynamicStroke](../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)), [dynamicStyleFillColor](../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)), [dynamicStyleLineColor](../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)), [dynamicStyleTextColor](../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency()), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)), [dynamicStyleValue](../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)), [dynamicTextAlignment](../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)), [dynamicTextColor](../PresentationElement.html#dynamicTextColor()), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)), [findOwnerForChildElement](../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [findOwnerForElement](../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)), [findPresentationElement](../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)), [firePropertyChange](../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateID](../PresentationElement.html#generateID()), [getAbstractDiagramPresentationElement](../PresentationElement.html#getAbstractDiagramPresentationElement()), [getActualElement](../PresentationElement.html#getActualElement()), [getAdditionalRenderersToNotifyOnPropertiesChange](../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()), [getAssignableModelElementsClasses](../PresentationElement.html#getAssignableModelElementsClasses()), [getBounds](../PresentationElement.html#getBounds()), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getBoundsToRepaint](../PresentationElement.html#getBoundsToRepaint()), [getBoundsWithChildrenOnEdge](../PresentationElement.html#getBoundsWithChildrenOnEdge()), [getCenterlinePoint](../PresentationElement.html#getCenterlinePoint()), [getCenterlinePointX](../PresentationElement.html#getCenterlinePointX()), [getCenterlinePointY](../PresentationElement.html#getCenterlinePointY()), [getChildPresentationElementForContextMenu](../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)), [getChildrenWithSymbolProperties](../PresentationElement.html#getChildrenWithSymbolProperties()), [getConfiguration](../PresentationElement.html#getConfiguration()), [getDiagramPresentationElement](../PresentationElement.html#getDiagramPresentationElement()), [getDiagramSurface](../PresentationElement.html#getDiagramSurface()), [getDrawComparator](../PresentationElement.html#getDrawComparator()), [getDynamicConfigurations](../PresentationElement.html#getDynamicConfigurations()), [getDynamicStyleOwner](../PresentationElement.html#getDynamicStyleOwner()), [getEffectiveStyleDelegate](../PresentationElement.html#getEffectiveStyleDelegate()), [getEffectiveStyleOwner](../PresentationElement.html#getEffectiveStyleOwner()), [getElement](../PresentationElement.html#getElement()), [getElementsForRelationshipConnecting](../PresentationElement.html#getElementsForRelationshipConnecting()), [getElementToConnectRelationship](../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFillColor](../PresentationElement.html#getFillColor()), [getFont](../PresentationElement.html#getFont()), [getFontHeight](../PresentationElement.html#getFontHeight()), [getFontRenderContext](../PresentationElement.html#getFontRenderContext()), [getHumanName](../PresentationElement.html#getHumanName()), [getHumanType](../PresentationElement.html#getHumanType()), [getIntersection](../PresentationElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getLineColor](../PresentationElement.html#getLineColor()), [getLineWidth](../PresentationElement.html#getLineWidth()), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point)), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getManipulationBounds](../PresentationElement.html#getManipulationBounds(java.awt.Point)), [getManipulationPreferredDimension](../PresentationElement.html#getManipulationPreferredDimension()), [getMiddlePoint](../PresentationElement.html#getMiddlePoint()), [getMiddlePoint](../PresentationElement.html#getMiddlePoint(java.awt.Point)), [getMiddlePointX](../PresentationElement.html#getMiddlePointX()), [getMiddlePointX](../PresentationElement.html#getMiddlePointX(java.awt.Point)), [getMiddlePointY](../PresentationElement.html#getMiddlePointY()), [getMiddlePointY](../PresentationElement.html#getMiddlePointY(java.awt.Point)), [getMinimumDimension](../PresentationElement.html#getMinimumDimension()), [getModelElement](../PresentationElement.html#getModelElement()), [getModelElementsForRelationshipConnecting](../PresentationElement.html#getModelElementsForRelationshipConnecting()), [getModelElementToConnectRelationship](../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [getModelElementToMove](../PresentationElement.html#getModelElementToMove()), [getNotCopyBounds](../PresentationElement.html#getNotCopyBounds()), [getNotZoomedTolerance](../PresentationElement.html#getNotZoomedTolerance()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getOwnStyleDelegate](../PresentationElement.html#getOwnStyleDelegate()), [getParent](../PresentationElement.html#getParent()), [getParentSymbolStyleOwner](../PresentationElement.html#getParentSymbolStyleOwner()), [getPreferredBounds](../PresentationElement.html#getPreferredBounds()), [getPreferredDimension](../PresentationElement.html#getPreferredDimension()), [getPreferredDimensionForAutosize](../PresentationElement.html#getPreferredDimensionForAutosize()), [getPreferredSize](../PresentationElement.html#getPreferredSize()), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(int)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementCount](../PresentationElement.html#getPresentationElementCount()), [getPresentationElementIndex](../PresentationElement.html#getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getPresentationElements](../PresentationElement.html#getPresentationElements()), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getProjectImpl](../PresentationElement.html#getProjectImpl()), [getProperty](../PresentationElement.html#getProperty(java.lang.String)), [getPropertyManager](../PresentationElement.html#getPropertyManager()), [getPropertyManagerName](../PresentationElement.html#getPropertyManagerName()), [getRenderer](../PresentationElement.html#getRenderer()), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [getStyle](../PresentationElement.html#getStyle()), [getSymbolRenderer](../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getTextColor](../PresentationElement.html#getTextColor()), [getTolerance](../PresentationElement.html#getTolerance()), [getVisibility](../PresentationElement.html#getVisibility()), [getVisiblePresentationElements](../PresentationElement.html#getVisiblePresentationElements()), [handleModelDelete](../PresentationElement.html#handleModelDelete()), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [hasManipulator](../PresentationElement.html#hasManipulator()), [hasSharedModelElement](../PresentationElement.html#hasSharedModelElement()), [initialize](../PresentationElement.html#initialize()), [initializeAndAutosize](../PresentationElement.html#initializeAndAutosize()), [internalApplyProperties](../PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [internalBeforeUpdate](../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)), [internalCreatePropertyChangeListener](../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)), [internalGetBoundsShape](../PresentationElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [internalGetModelElementToConnectRelationship](../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [internalGetPresentationElementStroke](../PresentationElement.html#internalGetPresentationElementStroke(int)), [internalGetSpecificFont](../PresentationElement.html#internalGetSpecificFont()), [internalGetSpecificTextColor](../PresentationElement.html#internalGetSpecificTextColor()), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalSilentApply](../PresentationElement.html#internalSilentApply()), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(float)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)), [internalUpdatePresentationElement](../PresentationElement.html#internalUpdatePresentationElement()), [intersects](../PresentationElement.html#intersects(int,int,int,int)), [intersects](../PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [invalidate](../PresentationElement.html#invalidate()), [isCanChildrenChangeEdge](../PresentationElement.html#isCanChildrenChangeEdge()), [isChildVisible](../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isContentHidden](../PresentationElement.html#isContentHidden()), [isCreateElementListener](../PresentationElement.html#isCreateElementListener()), [isDetectable](../PresentationElement.html#isDetectable()), [isDisposed](../PresentationElement.html#isDisposed()), [isLayouting](../PresentationElement.html#isLayouting()), [isMovableByMoveManager](../PresentationElement.html#isMovableByMoveManager()), [isNotNull](../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isPreserveProportionsWhenGrowing](../PresentationElement.html#isPreserveProportionsWhenGrowing()), [isSelected](../PresentationElement.html#isSelected()), [isShowElementTypeAsLabel](../PresentationElement.html#isShowElementTypeAsLabel()), [isSnapToGrid](../PresentationElement.html#isSnapToGrid()), [isSortable](../PresentationElement.html#isSortable()), [isSuitableToConnectRelationship](../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [isTextEditable](../PresentationElement.html#isTextEditable()), [isUseFillColor](../PresentationElement.html#isUseFillColor()), [isUseFillColorByProperty](../PresentationElement.html#isUseFillColorByProperty()), [isUseGradientForFill](../PresentationElement.html#isUseGradientForFill()), [isVisible](../PresentationElement.html#isVisible()), [isVisibleInDiagram](../PresentationElement.html#isVisibleInDiagram()), [isVisibleOrShrunken](../PresentationElement.html#isVisibleOrShrunken()), [movePathElementsRecursively](../PresentationElement.html#movePathElementsRecursively()), [mustShowContextMenu](../PresentationElement.html#mustShowContextMenu()), [notifyCreated](../PresentationElement.html#notifyCreated()), [notifyDiagramFrameSizeChange](../PresentationElement.html#notifyDiagramFrameSizeChange()), [notifyRepaintManager](../PresentationElement.html#notifyRepaintManager(boolean)), [onChildAdd](../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onChildRemove](../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onDiagramSurfaceSet](../PresentationElement.html#onDiagramSurfaceSet()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [onFontChange](../PresentationElement.html#onFontChange()), [onParentChange](../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [paintAdornments](../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintAdornmentsBackground](../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildren](../PresentationElement.html#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenAndAdornments](../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenBackground](../PresentationElement.html#paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelf](../PresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelfBackground](../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [preDisposeOnUpdate](../PresentationElement.html#preDisposeOnUpdate()), [prepareForLineDrawing](../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)), [prepareForShadowDrawing](../PresentationElement.html#prepareForShadowDrawing(java.awt.Graphics2D)), [prepareForTextDrawing](../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)), [propertyChange](../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)), [recreateListeners](../PresentationElement.html#recreateListeners()), [recursiveAutosize](../PresentationElement.html#recursiveAutosize()), [registerInSortManager](../PresentationElement.html#registerInSortManager()), [rememberBounds](../PresentationElement.html#rememberBounds()), [rememberBounds](../PresentationElement.html#rememberBounds(java.awt.Rectangle)), [removeFromSortManager](../PresentationElement.html#removeFromSortManager()), [removeItSelfOnUpdate](../PresentationElement.html#removeItSelfOnUpdate()), [removePresentationElement](../PresentationElement.html#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [resizeParent](../PresentationElement.html#resizeParent()), [sAddPresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sAddPresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)), [selectChildrenForMoving](../PresentationElement.html#selectChildrenForMoving()), [selectObjectsForMoving](../PresentationElement.html#selectObjectsForMoving()), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setBounds](../PresentationElement.html#setBounds(int,int,int,int)), [setBounds](../PresentationElement.html#setBounds(java.awt.Rectangle)), [setCreateElementListener](../PresentationElement.html#setCreateElementListener(boolean)), [setDummyResizeMode](../PresentationElement.html#setDummyResizeMode(boolean)), [setElement](../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setFillColor](../PresentationElement.html#setFillColor(java.awt.Color)), [setFont](../PresentationElement.html#setFont(java.awt.Font)), [setLayouting](../PresentationElement.html#setLayouting(boolean)), [setLineColor](../PresentationElement.html#setLineColor(java.awt.Color)), [setLineWidth](../PresentationElement.html#setLineWidth(int)), [setLoadedVisibility](../PresentationElement.html#setLoadedVisibility(boolean)), [setLocation](../PresentationElement.html#setLocation(int,int)), [setLocation](../PresentationElement.html#setLocation(java.awt.Point)), [setModelElement](../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [setNeedRecreateListeners](../PresentationElement.html#setNeedRecreateListeners(boolean)), [setPresentationElements](../PresentationElement.html#setPresentationElements(java.util.List)), [setPropertyManagerName](../PresentationElement.html#setPropertyManagerName(java.lang.String)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [setSize](../PresentationElement.html#setSize(int,int)), [setSize](../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)), [setSize](../PresentationElement.html#setSize(java.awt.Dimension)), [setTextColor](../PresentationElement.html#setTextColor(java.awt.Color)), [setTextEditable](../PresentationElement.html#setTextEditable(boolean)), [setUseFillColor](../PresentationElement.html#setUseFillColor(boolean)), [setVisible](../PresentationElement.html#setVisible(boolean)), [silentApply](../PresentationElement.html#silentApply()), [silentApply](../PresentationElement.html#silentApply(boolean)), [simpleSetBounds](../PresentationElement.html#simpleSetBounds(int,int,int,int)), [simpleSetBounds](../PresentationElement.html#simpleSetBounds(java.awt.Rectangle)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Point,float)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)), [snapViewToGrid](../PresentationElement.html#snapViewToGrid(float)), [sortObjectsByX](../PresentationElement.html#sortObjectsByX(java.util.List)), [sortObjectsByY](../PresentationElement.html#sortObjectsByY(java.util.List)), [sRemovePresentationElement](../PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetBounds](../PresentationElement.html#sSetBounds(int,int,int,int)), [sSetBounds](../PresentationElement.html#sSetBounds(java.awt.Rectangle)), [sSetElement](../PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [sSetLocation](../PresentationElement.html#sSetLocation(int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(java.awt.Point)), [sSetModelElement](../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [sSetParent](../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetParentForAll](../PresentationElement.html#sSetParentForAll(java.util.Collection)), [sSetPresentationElements](../PresentationElement.html#sSetPresentationElements(java.util.List)), [sSetSize](../PresentationElement.html#sSetSize(int,int)), [sSetSize](../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)), [sSetSize](../PresentationElement.html#sSetSize(java.awt.Dimension)), [sSetVisible](../PresentationElement.html#sSetVisible(boolean)), [tryToDeleteModelElementUponRemoval](../PresentationElement.html#tryToDeleteModelElementUponRemoval()), [update](../PresentationElement.html#update()), [updateAfterLoad](../PresentationElement.html#updateAfterLoad()), [updateLabelsIgnoringSuspendableLater](../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)), [updateLater](../PresentationElement.html#updateLater()), [updateModelByView](../PresentationElement.html#updateModelByView()), [updateModelByViewInternal](../PresentationElement.html#updateModelByViewInternal()), [updateViewAfterPropertyChange](../PresentationElement.html#updateViewAfterPropertyChange()), [useParentProperties](../PresentationElement.html#useParentProperties()), [useParentStyle](../PresentationElement.html#useParentStyle())`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../BaseElement.html)
`[canAdd](../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.uml.[MDElement](../../MDElement.html)
`[getProject](../../MDElement.html#getProject())`
Methods inherited from interface com.nomagic.magicdraw.utils.[NameOwner](../../../utils/NameOwner.html)
`[getName](../../../utils/NameOwner.html#getName())`

============ FIELD DETAIL =========== 
Field Details
showsProxy
@CheckForNullprotected [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) showsProxy
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PathConnector
public PathConnector()
PathConnector
public PathConnector(@CheckForNull
 [PresentationElement](../PresentationElement.html) v)
 ============ METHOD DETAIL ========== 
Method Details
clone
public [PathConnector](PathConnector.html) clone()
Specified by:
`[clone](../../BaseElement.html#clone())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`[clone](../PresentationElement.html#clone())` in class `[PresentationElement](../PresentationElement.html)`
getConnectedPathElements
@OpenApipublic final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](PathElement.html)> getConnectedPathElements()
Returns connected path elements. If element has no path elements returns empty list.
Returns:
connected path elements. Collection is unmodifiable.
getConnectedPathElements
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](PathElement.html)> getConnectedPathElements(boolean incoming)
Returns connected path elements by direction.
Parameters:
`incoming` - true if incoming paths should be selected, false if outgoing.
Returns:
connected path elements.
getConnectedPathElements
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](PathElement.html)> getConnectedPathElements(boolean incoming,
 boolean excludeToSelf)
Returns connected path elements by direction with an option to exclude paths to self
Parameters:
`incoming` - true if incoming paths should be selected, false if outgoing.
`excludeToSelf` - true if paths with a source equal to target should not be added to the list, false to include them
Returns:
connected path elements.
getConnectedPathElementCount
@OpenApipublic final int getConnectedPathElementCount()
Returns number of connected path elements.
Returns:
number of connected path elements.
sSetConnectedPathElements
public void sSetConnectedPathElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](PathElement.html)> paths)
Sets new path elements.
Parameters:
`paths` - list of path elements.
addConnectedPathElement
public boolean addConnectedPathElement([PathElement](PathElement.html) element)
Adds a new path element, and recalculates its position.
Parameters:
`element` - element to be added.
Returns:
true if an element was added
sAddConnectedPathElement
public boolean sAddConnectedPathElement([PathElement](PathElement.html) element)
Adds a new path element.
Parameters:
`element` - element to be added.
Returns:
true if an element was added
sRemoveConnectedPathElement
public boolean sRemoveConnectedPathElement([PathElement](PathElement.html) element)
Removes path element.
Parameters:
`element` - element to remove.
Returns:
true if an element was removed
removeConnectedPathElement
public boolean removeConnectedPathElement([PathElement](PathElement.html) link)
Removes path element.
Parameters:
`link` - element to remove.
Returns:
true if an element was removed
movePathElements
public void movePathElements()
Overrides:
`[movePathElements](../PresentationElement.html#movePathElements())` in class `[PresentationElement](../PresentationElement.html)`
movePathElement
protected abstract void movePathElement([PathElement](PathElement.html) element,
 @CheckForNull
 [PathConnector](PathConnector.html) requestor)
Calculates position of a path element.
Parameters:
`element` - element which position will be calculated.
`requestor` - the requestor of this path moving. Implementations may check to avoid endless loops.
movePathElement
public final void movePathElement([PathElement](PathElement.html) path,
 boolean notify)
Calculates position of a path element.
Parameters:
`path` - path element to calculate.
`notify` - true if both ends of path element should be calculated.
dispose
public void dispose()
Description copied from class: `[PresentationElement](../PresentationElement.html#dispose())`
disposes ends of links when link is deleted
Specified by:
`[dispose](../../BaseElement.html#dispose())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`[dispose](../PresentationElement.html#dispose())` in class `[PresentationElement](../PresentationElement.html)`
disposeConnectedPaths
protected void disposeConnectedPaths()
accept
@OpenApipublic void accept([Visitor](../../Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
 See "Visitor" pattern for more details.
Specified by:
`[accept](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../../MDElement.html)`
Overrides:
`accept` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
sSetVisibility
public void sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)
Description copied from class: `[PresentationElement](../PresentationElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility))`
Sets element visibility flag.
Overrides:
`[sSetVisibility](../PresentationElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`visibility` - flag value
supportsVisibleConnectedPathElementsIfSelfInvisible
protected boolean supportsVisibleConnectedPathElementsIfSelfInvisible()
setVisibility
public void setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)
Description copied from class: `[PresentationElement](../PresentationElement.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility))`
Sets element visibility flag.
Overrides:
`[setVisibility](../PresentationElement.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`visibility` - flag value
setParent
public void setParent([PresentationElement](../PresentationElement.html) parent)
Description copied from class: `[PresentationElement](../PresentationElement.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Sets parent for this view.
 For adding symbols to other symbols use
 [`PresentationElement.addPresentationElement(PresentationElement)`](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)) or
 [`PresentationElement.sAddPresentationElement(PresentationElement)`](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))}
Overrides:
`[setParent](../PresentationElement.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`parent` - parent view
getPreferredArrowLength
public int getPreferredArrowLength()
selectPathsForMoving
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](PathElement.html)> selectPathsForMoving([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../PresentationElement.html)> subPresentationElements)
Description copied from class: `[PresentationElement](../PresentationElement.html#selectPathsForMoving(java.util.List))`
Select paths to move with current symbol from deep structure.
 Some paths can be connected to current symbol, but owned in some deep child of this symbol.
Overrides:
`[selectPathsForMoving](../PresentationElement.html#selectPathsForMoving(java.util.List))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`subPresentationElements` - sub children of this symbol
Returns:
paths to move together with current symbol
getConnectedPathElement
@CheckForNullpublic [PathElement](PathElement.html) getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement element)
Return a connected path with a given model element
Parameters:
`element` - element
Returns:
connected path element of given element
checkShowsProxy
protected boolean checkShowsProxy()
Overrides:
`[checkShowsProxy](../PresentationElement.html#checkShowsProxy())` in class `[PresentationElement](../PresentationElement.html)`
isShowsProxy
public final boolean isShowsProxy()
Overrides:
`[isShowsProxy](../PresentationElement.html#isShowsProxy())` in class `[PresentationElement](../PresentationElement.html)`
clearShowsProxy
public void clearShowsProxy()
Overrides:
`[clearShowsProxy](../PresentationElement.html#clearShowsProxy())` in class `[PresentationElement](../PresentationElement.html)`
findSymbolForEnd
@CheckForNullpublic [PresentationElement](../PresentationElement.html) findSymbolForEnd([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [PresentationElement](../PresentationElement.html)> preferredEndType,
 boolean asClient)
Find symbol for the Path end (client or supplier)
Parameters:
`element` - path end element
`preferredEndType` - preferred end type
`asClient` - search for a client element if true
Returns:
found symbol or null
findSymbolForEnd
@CheckForNullprotected [PresentationElement](../PresentationElement.html) findSymbolForEnd([Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[PresentationElement](../PresentationElement.html)> elements,
 boolean asClient)
createSmartListenerConfig
protected void createSmartListenerConfig([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)
Overrides:
`[createSmartListenerConfig](../PresentationElement.html#createSmartListenerConfig(java.util.List))` in class `[PresentationElement](../PresentationElement.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.paths</a></div>
<h1 class="title" title="Class PathConnector">Class PathConnector</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code>, <code><a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">PathConnector</span>
<span class="extends-implements">extends <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span></div>
<div class="block">This class is base class for presentation elements connectible by some path element.
 This means that instance of this class can have incoming or outgoing path elements.</div>
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
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#showsProxy">showsProxy</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#DASHED_STROKE">DASHED_STROKE</a>, <a href="../PresentationElement.html#DEFAULT_LINE_WIDTH">DEFAULT_LINE_WIDTH</a>, <a href="../PresentationElement.html#DOTTED_STROKE">DOTTED_STROKE</a>, <a href="../PresentationElement.html#HANDLE_SIZE">HANDLE_SIZE</a>, <a href="../PresentationElement.html#MAX_LINE_WIDTH">MAX_LINE_WIDTH</a>, <a href="../PresentationElement.html#MIN_LINE_WIDTH">MIN_LINE_WIDTH</a>, <a href="../PresentationElement.html#peStyle">peStyle</a>, <a href="../PresentationElement.html#SHADOW_WIDTH">SHADOW_WIDTH</a>, <a href="../PresentationElement.html#SOLID_STROKE">SOLID_STROKE</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PathConnector</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PathConnector</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> v)</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a><wbr/>(<a href="../../Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method accepts a visitor, and calls method "visit&lt;class name&gt;(this)" of a visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addConnectedPathElement</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a new path element, and recalculates its position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkShowsProxy()">checkShowsProxy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowsProxy()">clearShowsProxy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">disposes ends of links when link is deleted</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#disposeConnectedPaths()">disposeConnectedPaths</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">findSymbolForEnd</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; preferredEndType,
 boolean asClient)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find symbol for the Path end (client or supplier)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findSymbolForEnd(java.util.stream.Stream,boolean)">findSymbolForEnd</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements,
 boolean asClient)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">getConnectedPathElement</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a connected path with a given model element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectedPathElementCount()">getConnectedPathElementCount</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns number of connected path elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectedPathElements()">getConnectedPathElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns connected path elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectedPathElements(boolean)">getConnectedPathElements</a><wbr/>(boolean incoming)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns connected path elements by direction.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a><wbr/>(boolean incoming,
 boolean excludeToSelf)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns connected path elements by direction with an option to exclude paths to self</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreferredArrowLength()">getPreferredArrowLength</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowsProxy()">isShowsProxy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)">movePathElement</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 boolean notify)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates position of a path element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element,
 <a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> requestor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Calculates position of a path element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePathElements()">movePathElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">removeConnectedPathElement</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> link)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes path element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sAddConnectedPathElement</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a new path element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#selectPathsForMoving(java.util.List)">selectPathsForMoving</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; subPresentationElements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Select paths to move with current symbol from deep structure.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets parent for this view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a><wbr/>(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets element visibility flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sRemoveConnectedPathElement</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes path element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetConnectedPathElements(java.util.List)">sSetConnectedPathElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt; paths)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new path elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a><wbr/>(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets element visibility flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#supportsVisibleConnectedPathElementsIfSelfInvisible()">supportsVisibleConnectedPathElementsIfSelfInvisible</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a>, <a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">addPresentationElement</a>, <a href="../PresentationElement.html#addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElementWithoutResize</a>, <a href="../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="../PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">adjustBoundsBeforeChange</a>, <a href="../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBounds</a>, <a href="../PresentationElement.html#adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBoundsForMoving</a>, <a href="../PresentationElement.html#alwaysShowTooltip()">alwaysShowTooltip</a>, <a href="../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">applyProperties</a>, <a href="../PresentationElement.html#askDeleteDataConfirmation()">askDeleteDataConfirmation</a>, <a href="../PresentationElement.html#atInsert()">atInsert</a>, <a href="../PresentationElement.html#atInsertChildren()">atInsertChildren</a>, <a href="../PresentationElement.html#autosizeAndResizeManipulatedParent()">autosizeAndResizeManipulatedParent</a>, <a href="../PresentationElement.html#autosizeAndResizeParent()">autosizeAndResizeParent</a>, <a href="../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">beforeDelete</a>, <a href="../PresentationElement.html#boundsChanged()">boundsChanged</a>, <a href="../PresentationElement.html#boundsChanged(java.awt.Rectangle)">boundsChanged</a>, <a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddChild</a>, <a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddInstance</a>, <a href="../PresentationElement.html#canBeDisposedOnUpdate()">canBeDisposedOnUpdate</a>, <a href="../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeElementOwner</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">canChangeParent</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../PresentationElement.html#canFill()">canFill</a>, <a href="../PresentationElement.html#canHavePaths()">canHavePaths</a>, <a href="../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">changeProperties</a>, <a href="../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a>, <a href="../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">checkProxyVisibility</a>, <a href="../PresentationElement.html#childrenForMoving()">childrenForMoving</a>, <a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)">collectSubShowingPresentationElements</a>, <a href="../PresentationElement.html#coversPoint(int,int)">coversPoint</a>, <a href="../PresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">coversPoint</a>, <a href="../PresentationElement.html#createFillStrategy()">createFillStrategy</a>, <a href="../PresentationElement.html#createPresentationElementStyle()">createPresentationElementStyle</a>, <a href="../PresentationElement.html#createPropertyChangeListener()">createPropertyChangeListener</a>, <a href="../PresentationElement.html#disposeChildren()">disposeChildren</a>, <a href="../PresentationElement.html#disposePropertyChangeListener()">disposePropertyChangeListener</a>, <a href="../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a>, <a href="../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawBackground</a>, <a href="../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbol</a>, <a href="../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbolBackground</a>, <a href="../PresentationElement.html#dynamicFillColor()">dynamicFillColor</a>, <a href="../PresentationElement.html#dynamicLineColor()">dynamicLineColor</a>, <a href="../PresentationElement.html#dynamicLineWidth()">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicLineWidth(int)">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicPaintShadow()">dynamicPaintShadow</a>, <a href="../PresentationElement.html#dynamicStroke()">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(int)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)">dynamicStyleFillColor</a>, <a href="../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)">dynamicStyleLineColor</a>, <a href="../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)">dynamicStyleTextColor</a>, <a href="../PresentationElement.html#dynamicStyleTransparency()">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)">dynamicStyleValue</a>, <a href="../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">dynamicTextAlignment</a>, <a href="../PresentationElement.html#dynamicTextColor()">dynamicTextColor</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a>, <a href="../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOwnerForChildElement</a>, <a href="../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a>, <a href="../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">findPresentationElement</a>, <a href="../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../PresentationElement.html#generateID()">generateID</a>, <a href="../PresentationElement.html#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>, <a href="../PresentationElement.html#getActualElement()">getActualElement</a>, <a href="../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()">getAdditionalRenderersToNotifyOnPropertiesChange</a>, <a href="../PresentationElement.html#getAssignableModelElementsClasses()">getAssignableModelElementsClasses</a>, <a href="../PresentationElement.html#getBounds()">getBounds</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getBoundsToRepaint()">getBoundsToRepaint</a>, <a href="../PresentationElement.html#getBoundsWithChildrenOnEdge()">getBoundsWithChildrenOnEdge</a>, <a href="../PresentationElement.html#getCenterlinePoint()">getCenterlinePoint</a>, <a href="../PresentationElement.html#getCenterlinePointX()">getCenterlinePointX</a>, <a href="../PresentationElement.html#getCenterlinePointY()">getCenterlinePointY</a>, <a href="../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)">getChildPresentationElementForContextMenu</a>, <a href="../PresentationElement.html#getChildrenWithSymbolProperties()">getChildrenWithSymbolProperties</a>, <a href="../PresentationElement.html#getConfiguration()">getConfiguration</a>, <a href="../PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="../PresentationElement.html#getDiagramSurface()">getDiagramSurface</a>, <a href="../PresentationElement.html#getDrawComparator()">getDrawComparator</a>, <a href="../PresentationElement.html#getDynamicConfigurations()">getDynamicConfigurations</a>, <a href="../PresentationElement.html#getDynamicStyleOwner()">getDynamicStyleOwner</a>, <a href="../PresentationElement.html#getEffectiveStyleDelegate()">getEffectiveStyleDelegate</a>, <a href="../PresentationElement.html#getEffectiveStyleOwner()">getEffectiveStyleOwner</a>, <a href="../PresentationElement.html#getElement()">getElement</a>, <a href="../PresentationElement.html#getElementsForRelationshipConnecting()">getElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementToConnectRelationship</a>, <a href="../PresentationElement.html#getFillColor()">getFillColor</a>, <a href="../PresentationElement.html#getFont()">getFont</a>, <a href="../PresentationElement.html#getFontHeight()">getFontHeight</a>, <a href="../PresentationElement.html#getFontRenderContext()">getFontRenderContext</a>, <a href="../PresentationElement.html#getHumanName()">getHumanName</a>, <a href="../PresentationElement.html#getHumanType()">getHumanType</a>, <a href="../PresentationElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="../PresentationElement.html#getLineColor()">getLineColor</a>, <a href="../PresentationElement.html#getLineWidth()">getLineWidth</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getManipulationBounds(java.awt.Point)">getManipulationBounds</a>, <a href="../PresentationElement.html#getManipulationPreferredDimension()">getManipulationPreferredDimension</a>, <a href="../PresentationElement.html#getMiddlePoint()">getMiddlePoint</a>, <a href="../PresentationElement.html#getMiddlePoint(java.awt.Point)">getMiddlePoint</a>, <a href="../PresentationElement.html#getMiddlePointX()">getMiddlePointX</a>, <a href="../PresentationElement.html#getMiddlePointX(java.awt.Point)">getMiddlePointX</a>, <a href="../PresentationElement.html#getMiddlePointY()">getMiddlePointY</a>, <a href="../PresentationElement.html#getMiddlePointY(java.awt.Point)">getMiddlePointY</a>, <a href="../PresentationElement.html#getMinimumDimension()">getMinimumDimension</a>, <a href="../PresentationElement.html#getModelElement()">getModelElement</a>, <a href="../PresentationElement.html#getModelElementsForRelationshipConnecting()">getModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">getModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#getModelElementToMove()">getModelElementToMove</a>, <a href="../PresentationElement.html#getNotCopyBounds()">getNotCopyBounds</a>, <a href="../PresentationElement.html#getNotZoomedTolerance()">getNotZoomedTolerance</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getOwnStyleDelegate()">getOwnStyleDelegate</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a>, <a href="../PresentationElement.html#getPreferredBounds()">getPreferredBounds</a>, <a href="../PresentationElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="../PresentationElement.html#getPreferredDimensionForAutosize()">getPreferredDimensionForAutosize</a>, <a href="../PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="../PresentationElement.html#getPresentationElementAt(int)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementCount()">getPresentationElementCount</a>, <a href="../PresentationElement.html#getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getPresentationElementIndex</a>, <a href="../PresentationElement.html#getPresentationElements()">getPresentationElements</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getProjectImpl()">getProjectImpl</a>, <a href="../PresentationElement.html#getProperty(java.lang.String)">getProperty</a>, <a href="../PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="../PresentationElement.html#getPropertyManagerName()">getPropertyManagerName</a>, <a href="../PresentationElement.html#getRenderer()">getRenderer</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#getStyle()">getStyle</a>, <a href="../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSymbolRenderer</a>, <a href="../PresentationElement.html#getTextColor()">getTextColor</a>, <a href="../PresentationElement.html#getTolerance()">getTolerance</a>, <a href="../PresentationElement.html#getVisibility()">getVisibility</a>, <a href="../PresentationElement.html#getVisiblePresentationElements()">getVisiblePresentationElements</a>, <a href="../PresentationElement.html#handleModelDelete()">handleModelDelete</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#hasManipulator()">hasManipulator</a>, <a href="../PresentationElement.html#hasSharedModelElement()">hasSharedModelElement</a>, <a href="../PresentationElement.html#initialize()">initialize</a>, <a href="../PresentationElement.html#initializeAndAutosize()">initializeAndAutosize</a>, <a href="../PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a>, <a href="../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)">internalBeforeUpdate</a>, <a href="../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">internalCreatePropertyChangeListener</a>, <a href="../PresentationElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a>, <a href="../PresentationElement.html#internalGetSpecificFont()">internalGetSpecificFont</a>, <a href="../PresentationElement.html#internalGetSpecificTextColor()">internalGetSpecificTextColor</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalSilentApply()">internalSilentApply</a>, <a href="../PresentationElement.html#internalSnapToGrid(float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#internalUpdatePresentationElement()">internalUpdatePresentationElement</a>, <a href="../PresentationElement.html#intersects(int,int,int,int)">intersects</a>, <a href="../PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a>, <a href="../PresentationElement.html#invalidate()">invalidate</a>, <a href="../PresentationElement.html#isCanChildrenChangeEdge()">isCanChildrenChangeEdge</a>, <a href="../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildVisible</a>, <a href="../PresentationElement.html#isContentHidden()">isContentHidden</a>, <a href="../PresentationElement.html#isCreateElementListener()">isCreateElementListener</a>, <a href="../PresentationElement.html#isDetectable()">isDetectable</a>, <a href="../PresentationElement.html#isDisposed()">isDisposed</a>, <a href="../PresentationElement.html#isLayouting()">isLayouting</a>, <a href="../PresentationElement.html#isMovableByMoveManager()">isMovableByMoveManager</a>, <a href="../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNotNull</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isParentOf</a>, <a href="../PresentationElement.html#isPreserveProportionsWhenGrowing()">isPreserveProportionsWhenGrowing</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#isShowElementTypeAsLabel()">isShowElementTypeAsLabel</a>, <a href="../PresentationElement.html#isSnapToGrid()">isSnapToGrid</a>, <a href="../PresentationElement.html#isSortable()">isSortable</a>, <a href="../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">isSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#isTextEditable()">isTextEditable</a>, <a href="../PresentationElement.html#isUseFillColor()">isUseFillColor</a>, <a href="../PresentationElement.html#isUseFillColorByProperty()">isUseFillColorByProperty</a>, <a href="../PresentationElement.html#isUseGradientForFill()">isUseGradientForFill</a>, <a href="../PresentationElement.html#isVisible()">isVisible</a>, <a href="../PresentationElement.html#isVisibleInDiagram()">isVisibleInDiagram</a>, <a href="../PresentationElement.html#isVisibleOrShrunken()">isVisibleOrShrunken</a>, <a href="../PresentationElement.html#movePathElementsRecursively()">movePathElementsRecursively</a>, <a href="../PresentationElement.html#mustShowContextMenu()">mustShowContextMenu</a>, <a href="../PresentationElement.html#notifyCreated()">notifyCreated</a>, <a href="../PresentationElement.html#notifyDiagramFrameSizeChange()">notifyDiagramFrameSizeChange</a>, <a href="../PresentationElement.html#notifyRepaintManager(boolean)">notifyRepaintManager</a>, <a href="../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildAdd</a>, <a href="../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildRemove</a>, <a href="../PresentationElement.html#onDiagramSurfaceSet()">onDiagramSurfaceSet</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#onFontChange()">onFontChange</a>, <a href="../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">onParentChange</a>, <a href="../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornments</a>, <a href="../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornmentsBackground</a>, <a href="../PresentationElement.html#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildren</a>, <a href="../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenAndAdornments</a>, <a href="../PresentationElement.html#paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenBackground</a>, <a href="../PresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelf</a>, <a href="../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelfBackground</a>, <a href="../PresentationElement.html#preDisposeOnUpdate()">preDisposeOnUpdate</a>, <a href="../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)">prepareForLineDrawing</a>, <a href="../PresentationElement.html#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a>, <a href="../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)">prepareForTextDrawing</a>, <a href="../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a>, <a href="../PresentationElement.html#recreateListeners()">recreateListeners</a>, <a href="../PresentationElement.html#recursiveAutosize()">recursiveAutosize</a>, <a href="../PresentationElement.html#registerInSortManager()">registerInSortManager</a>, <a href="../PresentationElement.html#rememberBounds()">rememberBounds</a>, <a href="../PresentationElement.html#rememberBounds(java.awt.Rectangle)">rememberBounds</a>, <a href="../PresentationElement.html#removeFromSortManager()">removeFromSortManager</a>, <a href="../PresentationElement.html#removeItSelfOnUpdate()">removeItSelfOnUpdate</a>, <a href="../PresentationElement.html#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">removePresentationElement</a>, <a href="../PresentationElement.html#resizeParent()">resizeParent</a>, <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sAddPresentationElement</a>, <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">sAddPresentationElement</a>, <a href="../PresentationElement.html#selectChildrenForMoving()">selectChildrenForMoving</a>, <a href="../PresentationElement.html#selectObjectsForMoving()">selectObjectsForMoving</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setBounds(int,int,int,int)">setBounds</a>, <a href="../PresentationElement.html#setBounds(java.awt.Rectangle)">setBounds</a>, <a href="../PresentationElement.html#setCreateElementListener(boolean)">setCreateElementListener</a>, <a href="../PresentationElement.html#setDummyResizeMode(boolean)">setDummyResizeMode</a>, <a href="../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a>, <a href="../PresentationElement.html#setFillColor(java.awt.Color)">setFillColor</a>, <a href="../PresentationElement.html#setFont(java.awt.Font)">setFont</a>, <a href="../PresentationElement.html#setLayouting(boolean)">setLayouting</a>, <a href="../PresentationElement.html#setLineColor(java.awt.Color)">setLineColor</a>, <a href="../PresentationElement.html#setLineWidth(int)">setLineWidth</a>, <a href="../PresentationElement.html#setLoadedVisibility(boolean)">setLoadedVisibility</a>, <a href="../PresentationElement.html#setLocation(int,int)">setLocation</a>, <a href="../PresentationElement.html#setLocation(java.awt.Point)">setLocation</a>, <a href="../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">setModelElement</a>, <a href="../PresentationElement.html#setNeedRecreateListeners(boolean)">setNeedRecreateListeners</a>, <a href="../PresentationElement.html#setPresentationElements(java.util.List)">setPresentationElements</a>, <a href="../PresentationElement.html#setPropertyManagerName(java.lang.String)">setPropertyManagerName</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#setSize(int,int)">setSize</a>, <a href="../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)">setSize</a>, <a href="../PresentationElement.html#setSize(java.awt.Dimension)">setSize</a>, <a href="../PresentationElement.html#setTextColor(java.awt.Color)">setTextColor</a>, <a href="../PresentationElement.html#setTextEditable(boolean)">setTextEditable</a>, <a href="../PresentationElement.html#setUseFillColor(boolean)">setUseFillColor</a>, <a href="../PresentationElement.html#setVisible(boolean)">setVisible</a>, <a href="../PresentationElement.html#silentApply()">silentApply</a>, <a href="../PresentationElement.html#silentApply(boolean)">silentApply</a>, <a href="../PresentationElement.html#simpleSetBounds(int,int,int,int)">simpleSetBounds</a>, <a href="../PresentationElement.html#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Point,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapViewToGrid(float)">snapViewToGrid</a>, <a href="../PresentationElement.html#sortObjectsByX(java.util.List)">sortObjectsByX</a>, <a href="../PresentationElement.html#sortObjectsByY(java.util.List)">sortObjectsByY</a>, <a href="../PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sRemovePresentationElement</a>, <a href="../PresentationElement.html#sSetBounds(int,int,int,int)">sSetBounds</a>, <a href="../PresentationElement.html#sSetBounds(java.awt.Rectangle)">sSetBounds</a>, <a href="../PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">sSetElement</a>, <a href="../PresentationElement.html#sSetLocation(int,int)">sSetLocation</a>, <a href="../PresentationElement.html#sSetLocation(java.awt.Point)">sSetLocation</a>, <a href="../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">sSetModelElement</a>, <a href="../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a>, <a href="../PresentationElement.html#sSetParentForAll(java.util.Collection)">sSetParentForAll</a>, <a href="../PresentationElement.html#sSetPresentationElements(java.util.List)">sSetPresentationElements</a>, <a href="../PresentationElement.html#sSetSize(int,int)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(java.awt.Dimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetVisible(boolean)">sSetVisible</a>, <a href="../PresentationElement.html#tryToDeleteModelElementUponRemoval()">tryToDeleteModelElementUponRemoval</a>, <a href="../PresentationElement.html#update()">update</a>, <a href="../PresentationElement.html#updateAfterLoad()">updateAfterLoad</a>, <a href="../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)">updateLabelsIgnoringSuspendableLater</a>, <a href="../PresentationElement.html#updateLater()">updateLater</a>, <a href="../PresentationElement.html#updateModelByView()">updateModelByView</a>, <a href="../PresentationElement.html#updateModelByViewInternal()">updateModelByViewInternal</a>, <a href="../PresentationElement.html#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a>, <a href="../PresentationElement.html#useParentProperties()">useParentProperties</a>, <a href="../PresentationElement.html#useParentStyle()">useParentStyle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../BaseElement.html#isSelfChangeable()">isSelfChangeable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></h3>
<code><a href="../../MDElement.html#getProject()">getProject</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.utils.NameOwner">Methods inherited from interface com.nomagic.magicdraw.utils.<a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></h3>
<code><a href="../../../utils/NameOwner.html#getName()">getName</a></code></div>
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
<section class="detail" id="showsProxy">
<h3>showsProxy</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">showsProxy</span></div>
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
<h3>PathConnector</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PathConnector</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>PathConnector</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PathConnector</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> v)</span></div>
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
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#clone()">clone</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#clone()">clone</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectedPathElements()">
<h3>getConnectedPathElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</span> <span class="element-name">getConnectedPathElements</span>()</div>
<div class="block">Returns connected path elements. If element has no path elements returns empty list.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>connected path elements. Collection is unmodifiable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectedPathElements(boolean)">
<h3>getConnectedPathElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</span> <span class="element-name">getConnectedPathElements</span><wbr/><span class="parameters">(boolean incoming)</span></div>
<div class="block">Returns connected path elements by direction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>incoming</code> - true if incoming paths should be selected, false if outgoing.</dd>
<dt>Returns:</dt>
<dd>connected path elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectedPathElements(boolean,boolean)">
<h3>getConnectedPathElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</span> <span class="element-name">getConnectedPathElements</span><wbr/><span class="parameters">(boolean incoming,
 boolean excludeToSelf)</span></div>
<div class="block">Returns connected path elements by direction with an option to exclude paths to self</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>incoming</code> - true if incoming paths should be selected, false if outgoing.</dd>
<dd><code>excludeToSelf</code> - true if paths with a source equal to target should not be added to the list, false to include them</dd>
<dt>Returns:</dt>
<dd>connected path elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectedPathElementCount()">
<h3>getConnectedPathElementCount</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">int</span> <span class="element-name">getConnectedPathElementCount</span>()</div>
<div class="block">Returns number of connected path elements.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>number of connected path elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetConnectedPathElements(java.util.List)">
<h3>sSetConnectedPathElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetConnectedPathElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt; paths)</span></div>
<div class="block">Sets new path elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>paths</code> - list of path elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>addConnectedPathElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addConnectedPathElement</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element)</span></div>
<div class="block">Adds a new path element, and recalculates its position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to be added.</dd>
<dt>Returns:</dt>
<dd>true if an element was added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>sAddConnectedPathElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">sAddConnectedPathElement</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element)</span></div>
<div class="block">Adds a new path element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to be added.</dd>
<dt>Returns:</dt>
<dd>true if an element was added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>sRemoveConnectedPathElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">sRemoveConnectedPathElement</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element)</span></div>
<div class="block">Removes path element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to remove.</dd>
<dt>Returns:</dt>
<dd>true if an element was removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>removeConnectedPathElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">removeConnectedPathElement</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> link)</span></div>
<div class="block">Removes path element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>link</code> - element to remove.</dd>
<dt>Returns:</dt>
<dd>true if an element was removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePathElements()">
<h3>movePathElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">movePathElements</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#movePathElements()">movePathElements</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">
<h3>movePathElement</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">void</span> <span class="element-name">movePathElement</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element,
 @CheckForNull
 <a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> requestor)</span></div>
<div class="block">Calculates position of a path element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element which position will be calculated.</dd>
<dd><code>requestor</code> - the requestor of this path moving. Implementations may check to avoid endless loops.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)">
<h3>movePathElement</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">movePathElement</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 boolean notify)</span></div>
<div class="block">Calculates position of a path element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - path element to calculate.</dd>
<dd><code>notify</code> - true if both ends of path element should be calculated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#dispose()">PresentationElement</a></code></span></div>
<div class="block">disposes ends of links when link is deleted</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#dispose()">dispose</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#dispose()">dispose</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disposeConnectedPaths()">
<h3>disposeConnectedPaths</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">disposeConnectedPaths</span>()</div>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.Visitor)">
<h3>accept</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../../Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">MDElement</a></code></span></div>
<div class="block">Method accepts a visitor, and calls method "visit&lt;class name&gt;(this)" of a visitor.
 See "Visitor" pattern for more details.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a></code> in interface <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>accept</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">
<h3>sSetVisibility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetVisibility</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">PresentationElement</a></code></span></div>
<div class="block">Sets element visibility flag.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visibility</code> - flag value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="supportsVisibleConnectedPathElementsIfSelfInvisible()">
<h3>supportsVisibleConnectedPathElementsIfSelfInvisible</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">supportsVisibleConnectedPathElementsIfSelfInvisible</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">
<h3>setVisibility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisibility</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">PresentationElement</a></code></span></div>
<div class="block">Sets element visibility flag.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visibility</code> - flag value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>setParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParent</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PresentationElement</a></code></span></div>
<div class="block">Sets parent for this view.
 For adding symbols to other symbols use
 <a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>PresentationElement.addPresentationElement(PresentationElement)</code></a> or
 <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>PresentationElement.sAddPresentationElement(PresentationElement)</code></a>}</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>parent</code> - parent view</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreferredArrowLength()">
<h3>getPreferredArrowLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPreferredArrowLength</span>()</div>
</section>
</li>
<li>
<section class="detail" id="selectPathsForMoving(java.util.List)">
<h3>selectPathsForMoving</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</span> <span class="element-name">selectPathsForMoving</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; subPresentationElements)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#selectPathsForMoving(java.util.List)">PresentationElement</a></code></span></div>
<div class="block">Select paths to move with current symbol from deep structure.
 Some paths can be connected to current symbol, but owned in some deep child of this symbol.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#selectPathsForMoving(java.util.List)">selectPathsForMoving</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>subPresentationElements</code> - sub children of this symbol</dd>
<dt>Returns:</dt>
<dd>paths to move together with current symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>getConnectedPathElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></span> <span class="element-name">getConnectedPathElement</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
<div class="block">Return a connected path with a given model element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>connected path element of given element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkShowsProxy()">
<h3>checkShowsProxy</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">checkShowsProxy</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#checkShowsProxy()">checkShowsProxy</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowsProxy()">
<h3>isShowsProxy</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">isShowsProxy</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#isShowsProxy()">isShowsProxy</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearShowsProxy()">
<h3>clearShowsProxy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowsProxy</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#clearShowsProxy()">clearShowsProxy</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">
<h3>findSymbolForEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">findSymbolForEnd</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; preferredEndType,
 boolean asClient)</span></div>
<div class="block">Find symbol for the Path end (client or supplier)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - path end element</dd>
<dd><code>preferredEndType</code> - preferred end type</dd>
<dd><code>asClient</code> - search for a client element if true</dd>
<dt>Returns:</dt>
<dd>found symbol or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findSymbolForEnd(java.util.stream.Stream,boolean)">
<h3>findSymbolForEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">findSymbolForEnd</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements,
 boolean asClient)</span></div>
</section>
</li>
<li>
<section class="detail" id="createSmartListenerConfig(java.util.List)">
<h3>createSmartListenerConfig</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createSmartListenerConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
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
