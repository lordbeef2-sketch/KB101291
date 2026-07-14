# JAVA OPENAPI: DiagramPropertiesShape (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/shapes/DiagramPropertiesShape.html
- source_path: `com/nomagic/magicdraw/uml/symbols/shapes/DiagramPropertiesShape.html`
- source_sha256: `dac6c3bb2ad48fb58bb72777c2141495e6ce6c9975ab0b239f36d97cddfa740e`
- captured_utc: `2026-07-14T16:56:03.473548+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.shapes](package-summary.html)

## Class DiagramPropertiesShape

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](../paths/PathConnector.html)
[com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement](ShapeElement.html)
com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView
com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView
[com.nomagic.magicdraw.uml.symbols.shapes.TextBoxView](TextBoxView.html)
com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape

All Implemented Interfaces:
`[BaseElement](../../BaseElement.html)`, `[MDElement](../../MDElement.html)`, `[ModelElementProvider](../../ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`, `com.nomagic.magicdraw.uml.symbols.shapes.PlainTextOrHTMLChangeable`, `com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider`, `com.nomagic.magicdraw.uml.symbols.Wrapable`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApipublic classDiagramPropertiesShape
extends [TextBoxView](TextBoxView.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BGCOLOR](#BGCOLOR)`

`static final int`
`[BORDER_WIDTH](#BORDER_WIDTH)`

`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[DEFAULT_KEYWORDS](#DEFAULT_KEYWORDS)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_NAME](#DIAGRAM_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_TYPE](#DIAGRAM_TYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DOCUMENTATION](#DOCUMENTATION)`

`static final int`
`[FREE_SPACE](#FREE_SPACE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PENCOLOR](#PENCOLOR)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TAG_DELIMITER](#TAG_DELIMITER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TAG_NAME](#TAG_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TAG_VALUE](#TAG_VALUE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_FILE](#TEMPLATE_FILE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TXTCOLOR](#TXTCOLOR)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`CONTAINER_SHAPE_INSETS, SHAPE_DISTANCE_FROM_EDGE`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.[ShapeElement](ShapeElement.html)
`[BORDER_ELEMENT_MARGIN_ALL](ShapeElement.html#BORDER_ELEMENT_MARGIN_ALL), [BORDER_ELEMENT_MARGIN_BOTTOM](ShapeElement.html#BORDER_ELEMENT_MARGIN_BOTTOM), [BORDER_ELEMENT_MARGIN_LEFT](ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT), [BORDER_ELEMENT_MARGIN_LEFT_RIGHT](ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT_RIGHT), [BORDER_ELEMENT_MARGIN_MODES](ShapeElement.html#BORDER_ELEMENT_MARGIN_MODES), [BORDER_ELEMENT_MARGIN_NONE](ShapeElement.html#BORDER_ELEMENT_MARGIN_NONE), [BORDER_ELEMENT_MARGIN_RIGHT](ShapeElement.html#BORDER_ELEMENT_MARGIN_RIGHT), [BORDER_ELEMENT_MARGIN_TOP](ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP), [BORDER_ELEMENT_MARGIN_TOP_BOTTOM](ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP_BOTTOM), [BOTTOM_EDGE](ShapeElement.html#BOTTOM_EDGE), [INSIDE_EDGE_POSITION](ShapeElement.html#INSIDE_EDGE_POSITION), [LEFT_EDGE](ShapeElement.html#LEFT_EDGE), [NEED_AUTOSIZE_FULL](ShapeElement.html#NEED_AUTOSIZE_FULL), [NEED_AUTOSIZE_LAYOUT](ShapeElement.html#NEED_AUTOSIZE_LAYOUT), [NEED_AUTOSIZE_NONE](ShapeElement.html#NEED_AUTOSIZE_NONE), [NO_EDGE](ShapeElement.html#NO_EDGE), [NULL_INSETS](ShapeElement.html#NULL_INSETS), [ON_EDGE_POSITION](ShapeElement.html#ON_EDGE_POSITION), [OUTSIDE_EDGE_POSITION](ShapeElement.html#OUTSIDE_EDGE_POSITION), [RIGHT_EDGE](ShapeElement.html#RIGHT_EDGE), [SPACE](ShapeElement.html#SPACE), [SPACE_INSETS](ShapeElement.html#SPACE_INSETS), [SPACE_INSETS_EMPTY_TOP_BOTTOM](ShapeElement.html#SPACE_INSETS_EMPTY_TOP_BOTTOM), [TOP_EDGE](ShapeElement.html#TOP_EDGE)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[showsProxy](../paths/PathConnector.html#showsProxy)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DEFAULT_LINE_WIDTH](../PresentationElement.html#DEFAULT_LINE_WIDTH), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [HANDLE_SIZE](../PresentationElement.html#HANDLE_SIZE), [MAX_LINE_WIDTH](../PresentationElement.html#MAX_LINE_WIDTH), [MIN_LINE_WIDTH](../PresentationElement.html#MIN_LINE_WIDTH), [peStyle](../PresentationElement.html#peStyle), [SHADOW_WIDTH](../PresentationElement.html#SHADOW_WIDTH), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramPropertiesShape](#%3Cinit%3E())()`

`[DiagramPropertiesShape](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) parent)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../../Visitor.html) visitor)`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
`void`
`[atInsert](#atInsert())()`
Invalidates object at insert
`boolean`
`[canBeAutosized](#canBeAutosized())()`

`boolean`
`[canBeDeleted](#canBeDeleted())()`
Checks if an element can be deleted from a project.
`boolean`
`[canChangeParent](#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [PresentationElement](../PresentationElement.html)> movedTogether,
 [BaseElement](../../BaseElement.html) newParent,
 boolean changeElementParent)`
Returns true, if element can change parent.
`boolean`
`[canDisplayHTMLText](#canDisplayHTMLText())()`

`boolean`
`[canHavePaths](#canHavePaths())()`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[constructStandardModeText](#constructStandardModeText(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> keywords)`

`protected void`
`[createSmartListenerConfig](#createSmartListenerConfig(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)`

`protected com.nomagic.magicdraw.uml.symbols.shapes.TextAreaView`
`[createTextArea](#createTextArea())()`

`void`
`[dispose](#dispose())()`
disposes ends of links when link is deleted
`[Diagram](../../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)`
`[getElement](#getElement())()`
Returns model element of this presentation element.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHTMLTemplateFileName](#getHTMLTemplateFileName())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHumanName](#getHumanName())()`
Returns human representation of the data type
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getSelectedTags](#getSelectedTags())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[insertTaggedValues](#insertTaggedValues(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) source)`

`void`
`[internalApplyProperties](#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)`
Applies properties from given property manager
`protected void`
`[internalSpecificUpdate](#internalSpecificUpdate())()`
Specific to every shape and model element update operation.
`boolean`
`[isHTMLText](#isHTMLText())()`

`boolean`
`[isInInitialPositionOnFrame](#isInInitialPositionOnFrame())()`
Indicates if diagram properties shape is in the initial position and not moved by the user.
`boolean`
`[isUseCustomHTML](#isUseCustomHTML())()`

`void`
`[makeFreeSpaceInDiagram](#makeFreeSpaceInDiagram())()`

`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)`
Listens for property change it can be: data was edited text box was edited
`static void`
`[updateModificationTime](#updateModificationTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Update diagram modification time
`void`
`[updateViewAfterPropertyChange](#updateViewAfterPropertyChange())()`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.[TextBoxView](TextBoxView.html)
`[canFill](TextBoxView.html#canFill()), [checkShowsProxy](TextBoxView.html#checkShowsProxy()), [draw](TextBoxView.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [getDefaultDimension](TextBoxView.html#getDefaultDimension()), [getDynamicStyleOwner](TextBoxView.html#getDynamicStyleOwner()), [getParentSymbolStyleOwner](TextBoxView.html#getParentSymbolStyleOwner()), [internalSilentApply](TextBoxView.html#internalSilentApply()), [isLabelMode](TextBoxView.html#isLabelMode()), [isTextBoxLabelMode](TextBoxView.html#isTextBoxLabelMode(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [mustShowContextMenu](TextBoxView.html#mustShowContextMenu()), [needAdjustToMaximumDimension](TextBoxView.html#needAdjustToMaximumDimension()), [resizeParent](TextBoxView.html#resizeParent()), [rotateBoundsForHeaderOrientation](TextBoxView.html#rotateBoundsForHeaderOrientation(java.awt.Rectangle)), [setForcedToBeFillable](TextBoxView.html#setForcedToBeFillable(boolean)), [setHeaderOrientationVertical](TextBoxView.html#setHeaderOrientationVertical(boolean)), [setLabelMode](TextBoxView.html#setLabelMode(boolean)), [setVisibility](TextBoxView.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [sSetVisibility](TextBoxView.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [useParentStyle](TextBoxView.html#useParentStyle())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView
`internalGetHeaderInsets, minimumSizeForShrinkingIgnoringOrientation, paintSelf, providesHorizontalCenterline, providesVerticalCenterline, snapsToCenterlines`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView
`clone, editName, getName, getNameLabel, getTextObject, getUserText, hasText, internalGetSelfManipulationPreferredSize, isHeaderOrientationVertical, isWrapEnabled, setAutosize, setHTMLText, setName, setTextObject, setWrapEnabled, sSetAutosize, sSetHeaderOrientationVertical, sSetHTMLText, sSetName, sSetTextObject, sSetWrapEnabled`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
`addExtraChildrenPrefSizePadding, adjustBoundsBeforeChange, autosize, autosizeAndResizeParent, calculateMinY, calculateOvalShapePreferredSize, canAddInstance, correctChildrenVector, coversPoint, createBoundsShape, createStateForUpdateOperation, doInternalLayoutChildren, getAdditionalHeaderHeightForPreferredBounds, getChildrenBoundsForPreferredBounds, getHeaderBoundsForPreferredBounds, getHeaderDistanceFromTopForOvalShape, getHeaderInsets, getHeaderMaxYForShrinkableShape, getHeaderObject, getHeaderVerticalPosition, getHeaderVerticalPositionForLayout, getOvalShapeAvailableWidth, getPreferredBounds, getPresentationElementAt, getProxyPresentationElementsStream, getStereotypesToDisplay, internalGetHeaderBoundsForPreferredBounds, internalLayoutChildren, internalPostSpecificUpdate, internalPostUpdatePresentationElement, internalPreSpecificUpdate, internalUpdatePresentationElement, invalidate, isBorderVisible, isChildLayoutable, isContentHidden, isOvalShape, isParentShowsProxy, minimumDimension, minimumDimensionForShrinking, minimumSizeIgnoringOrientation, paintChildren, preferredDimension, preferredSizeIgnoringOrientation, setHeaderObject, setHeaderVerticalPosition, setTextEditable, sSetHeaderVerticalPosition, switchWidthHeightIfVerticalOrientation`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`addPresentationElement, addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, canAddChild, canMoveChildOutside, childrenBoundsForReshape, clearShowsProxy, constructLayoutHelper, getChildrenBounds, getChildrenInsets, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getRemovableChildren, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalAppendChildRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildrenBackground, prefDimensionByManipulatedChildren, recursiveAutosize, removePresentationElement, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.[ShapeElement](ShapeElement.html)
`[addBreakPoints](ShapeElement.html#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [adjustBounds](ShapeElement.html#adjustBounds(java.awt.Rectangle)), [adjustOnEdge](ShapeElement.html#adjustOnEdge()), [adjustOnEdge](ShapeElement.html#adjustOnEdge(java.awt.Rectangle,int,int,int)), [adjustOnEdgeChildren](ShapeElement.html#adjustOnEdgeChildren()), [autosize](ShapeElement.html#autosize()), [calculateAdjustOnEdgeLocation](ShapeElement.html#calculateAdjustOnEdgeLocation(java.awt.Rectangle)), [calculateAndGetMinimumShrinkingDimension](ShapeElement.html#calculateAndGetMinimumShrinkingDimension(int,int)), [calculateAndGetPreferredDimension](ShapeElement.html#calculateAndGetPreferredDimension()), [calculateEdge](ShapeElement.html#calculateEdge()), [calculateMinimumDimension](ShapeElement.html#calculateMinimumDimension()), [calculateOnEdgeBounds](ShapeElement.html#calculateOnEdgeBounds()), [calculatePreferredDimension](ShapeElement.html#calculatePreferredDimension()), [calculatePreferredDimension](ShapeElement.html#calculatePreferredDimension(int,int)), [clearOldRect](ShapeElement.html#clearOldRect()), [edgeChanged](ShapeElement.html#edgeChanged()), [ensureDimension](ShapeElement.html#ensureDimension(boolean)), [ensurePreferredDimensionIfShrinkable](ShapeElement.html#ensurePreferredDimensionIfShrinkable()), [ensurePreferredDimensionIfShrinkable](ShapeElement.html#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)), [findFreePlaceForShapeOnBorder](ShapeElement.html#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)), [getBorderElementMargin](ShapeElement.html#getBorderElementMargin()), [getBounds](ShapeElement.html#getBounds()), [getCenterlineableInnerParts](ShapeElement.html#getCenterlineableInnerParts(int)), [getDimensionForShrinking](ShapeElement.html#getDimensionForShrinking(int,int)), [getEdgeLine](ShapeElement.html#getEdgeLine(int)), [getFixedConnectionPoints](ShapeElement.html#getFixedConnectionPoints()), [getHeaderInsetReduce](ShapeElement.html#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)), [getInsetsForOnEdgeShapes](ShapeElement.html#getInsetsForOnEdgeShapes()), [getIntersection](ShapeElement.html#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getIntersection](ShapeElement.html#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)), [getIntersection](ShapeElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getLoadedDimension](ShapeElement.html#getLoadedDimension()), [getMiddlePoint](ShapeElement.html#getMiddlePoint()), [getMiddlePoint](ShapeElement.html#getMiddlePoint(java.awt.Point)), [getMiddlePointX](ShapeElement.html#getMiddlePointX()), [getMiddlePointX](ShapeElement.html#getMiddlePointX(java.awt.Point)), [getMiddlePointY](ShapeElement.html#getMiddlePointY()), [getMiddlePointY](ShapeElement.html#getMiddlePointY(java.awt.Point)), [getMinimumDimension](ShapeElement.html#getMinimumDimension()), [getNearestEdge](ShapeElement.html#getNearestEdge(int,int)), [getNearestEdge](ShapeElement.html#getNearestEdge(java.awt.Rectangle)), [getNeedAutosizeFlag](ShapeElement.html#getNeedAutosizeFlag()), [getNotCopyBounds](ShapeElement.html#getNotCopyBounds()), [getOnEdge](ShapeElement.html#getOnEdge()), [getOnEdgeCornerDistance](ShapeElement.html#getOnEdgeCornerDistance()), [getOnEdgePosition](ShapeElement.html#getOnEdgePosition()), [getPreferredDimension](ShapeElement.html#getPreferredDimension()), [getPreferredDimensionForAutosize](ShapeElement.html#getPreferredDimensionForAutosize()), [getReshapeMode](ShapeElement.html#getReshapeMode()), [getSizeForDrawing](ShapeElement.html#getSizeForDrawing()), [getSuspendShapeAutoResizeMode](ShapeElement.html#getSuspendShapeAutoResizeMode()), [hasManipulator](ShapeElement.html#hasManipulator()), [initialize](ShapeElement.html#initialize()), [internalGetBoundsShape](ShapeElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [intersects](ShapeElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [isAutosized](ShapeElement.html#isAutosized()), [isCenterlineInner](ShapeElement.html#isCenterlineInner()), [isHorizontalCenterlineProvider](ShapeElement.html#isHorizontalCenterlineProvider()), [isOnEdge](ShapeElement.html#isOnEdge()), [isShapeOnEdge](ShapeElement.html#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isShrinkable](ShapeElement.html#isShrinkable()), [isSnapShapesOnBorderToGrid](ShapeElement.html#isSnapShapesOnBorderToGrid()), [isSnapToGrid](ShapeElement.html#isSnapToGrid()), [isUseFixedConnectionPoints](ShapeElement.html#isUseFixedConnectionPoints()), [isVerticalCenterlineProvider](ShapeElement.html#isVerticalCenterlineProvider()), [layoutChildren](ShapeElement.html#layoutChildren()), [maximumDimension](ShapeElement.html#maximumDimension(java.awt.Dimension)), [minimumOrMinimumShrinkableDimension](ShapeElement.html#minimumOrMinimumShrinkableDimension(java.awt.Dimension)), [moveLinksToSelf](ShapeElement.html#moveLinksToSelf()), [movePathElement](ShapeElement.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)), [movePathElements](ShapeElement.html#movePathElements()), [onChildEdgeChange](ShapeElement.html#onChildEdgeChange(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)), [prepareForShadowDrawing](ShapeElement.html#prepareForShadowDrawing(java.awt.Graphics2D)), [resetCalculatePreferredRegardingChildren](ShapeElement.html#resetCalculatePreferredRegardingChildren()), [setBorderElementMargin](ShapeElement.html#setBorderElementMargin(java.lang.String)), [setCalculatePreferredRegardingChildren](ShapeElement.html#setCalculatePreferredRegardingChildren(boolean)), [setLoadedDimension](ShapeElement.html#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)), [setMinimumDimension](ShapeElement.html#setMinimumDimension(int,int)), [setNeedAutosizeFlag](ShapeElement.html#setNeedAutosizeFlag(byte)), [setOldRect](ShapeElement.html#setOldRect(java.awt.Rectangle)), [setOnEdge](ShapeElement.html#setOnEdge(int)), [setPreferredDimension](ShapeElement.html#setPreferredDimension(int,int)), [setReshapeMode](ShapeElement.html#setReshapeMode(com.nomagic.magicdraw.uml.symbols.ReshapeMode)), [setSnapShapesOnBorderToGrid](ShapeElement.html#setSnapShapesOnBorderToGrid(boolean)), [setSuspendShapeAutoResizeMode](ShapeElement.html#setSuspendShapeAutoResizeMode(java.lang.String)), [setUseFixedConnectionPoints](ShapeElement.html#setUseFixedConnectionPoints(boolean)), [shouldDrawShadow](ShapeElement.html#shouldDrawShadow()), [simpleSetBounds](ShapeElement.html#simpleSetBounds(int,int,int,int,boolean)), [simpleSetBounds](ShapeElement.html#simpleSetBounds(java.awt.Rectangle)), [sSetBorderElementMargin](ShapeElement.html#sSetBorderElementMargin(java.lang.String)), [sSetBounds](ShapeElement.html#sSetBounds(java.awt.Rectangle)), [sSetSuspendShapeAutoResizeMode](ShapeElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)), [toString](ShapeElement.html#toString()), [updateLater](ShapeElement.html#updateLater())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[addConnectedPathElement](../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [disposeConnectedPaths](../paths/PathConnector.html#disposeConnectedPaths()), [findSymbolForEnd](../paths/PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)), [findSymbolForEnd](../paths/PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)), [getConnectedPathElement](../paths/PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [getConnectedPathElementCount](../paths/PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)), [getPreferredArrowLength](../paths/PathConnector.html#getPreferredArrowLength()), [isShowsProxy](../paths/PathConnector.html#isShowsProxy()), [movePathElement](../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)), [removeConnectedPathElement](../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sAddConnectedPathElement](../paths/PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [selectPathsForMoving](../paths/PathConnector.html#selectPathsForMoving(java.util.List)), [setParent](../paths/PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sRemoveConnectedPathElement](../paths/PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sSetConnectedPathElements](../paths/PathConnector.html#sSetConnectedPathElements(java.util.List)), [supportsVisibleConnectedPathElementsIfSelfInvisible](../paths/PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[addPresentationElement](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addProperty](../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [adjustChildBounds](../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [alwaysShowTooltip](../PresentationElement.html#alwaysShowTooltip()), [applyProperties](../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [askDeleteDataConfirmation](../PresentationElement.html#askDeleteDataConfirmation()), [atInsertChildren](../PresentationElement.html#atInsertChildren()), [autosizeAndResizeManipulatedParent](../PresentationElement.html#autosizeAndResizeManipulatedParent()), [beforeDelete](../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)), [boundsChanged](../PresentationElement.html#boundsChanged()), [boundsChanged](../PresentationElement.html#boundsChanged(java.awt.Rectangle)), [canAddChild](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)), [canAddInstance](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDisposedOnUpdate](../PresentationElement.html#canBeDisposedOnUpdate()), [canChangeElementOwner](../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [changeProperties](../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [checkElementOwnerOnChange](../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [checkProxyVisibility](../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [childrenForMoving](../PresentationElement.html#childrenForMoving()), [collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)), [collectSubShowingPresentationElements](../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)), [coversPoint](../PresentationElement.html#coversPoint(int,int)), [createFillStrategy](../PresentationElement.html#createFillStrategy()), [createPresentationElementStyle](../PresentationElement.html#createPresentationElementStyle()), [createPropertyChangeListener](../PresentationElement.html#createPropertyChangeListener()), [disposeChildren](../PresentationElement.html#disposeChildren()), [disposePropertyChangeListener](../PresentationElement.html#disposePropertyChangeListener()), [drawBackground](../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbol](../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbolBackground](../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [dynamicFillColor](../PresentationElement.html#dynamicFillColor()), [dynamicLineColor](../PresentationElement.html#dynamicLineColor()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth(int)), [dynamicPaintShadow](../PresentationElement.html#dynamicPaintShadow()), [dynamicStroke](../PresentationElement.html#dynamicStroke()), [dynamicStroke](../PresentationElement.html#dynamicStroke(int)), [dynamicStroke](../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)), [dynamicStyleFillColor](../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)), [dynamicStyleLineColor](../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)), [dynamicStyleTextColor](../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency()), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)), [dynamicStyleValue](../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)), [dynamicTextAlignment](../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)), [dynamicTextColor](../PresentationElement.html#dynamicTextColor()), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [findOwnerForChildElement](../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [findOwnerForElement](../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)), [findPresentationElement](../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)), [firePropertyChange](../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateID](../PresentationElement.html#generateID()), [getAbstractDiagramPresentationElement](../PresentationElement.html#getAbstractDiagramPresentationElement()), [getActualElement](../PresentationElement.html#getActualElement()), [getAdditionalRenderersToNotifyOnPropertiesChange](../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()), [getAssignableModelElementsClasses](../PresentationElement.html#getAssignableModelElementsClasses()), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getBoundsToRepaint](../PresentationElement.html#getBoundsToRepaint()), [getBoundsWithChildrenOnEdge](../PresentationElement.html#getBoundsWithChildrenOnEdge()), [getCenterlinePoint](../PresentationElement.html#getCenterlinePoint()), [getCenterlinePointX](../PresentationElement.html#getCenterlinePointX()), [getCenterlinePointY](../PresentationElement.html#getCenterlinePointY()), [getChildPresentationElementForContextMenu](../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)), [getChildrenWithSymbolProperties](../PresentationElement.html#getChildrenWithSymbolProperties()), [getConfiguration](../PresentationElement.html#getConfiguration()), [getDiagramPresentationElement](../PresentationElement.html#getDiagramPresentationElement()), [getDiagramSurface](../PresentationElement.html#getDiagramSurface()), [getDrawComparator](../PresentationElement.html#getDrawComparator()), [getDynamicConfigurations](../PresentationElement.html#getDynamicConfigurations()), [getEffectiveStyleDelegate](../PresentationElement.html#getEffectiveStyleDelegate()), [getEffectiveStyleOwner](../PresentationElement.html#getEffectiveStyleOwner()), [getElementsForRelationshipConnecting](../PresentationElement.html#getElementsForRelationshipConnecting()), [getElementToConnectRelationship](../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFillColor](../PresentationElement.html#getFillColor()), [getFont](../PresentationElement.html#getFont()), [getFontHeight](../PresentationElement.html#getFontHeight()), [getFontRenderContext](../PresentationElement.html#getFontRenderContext()), [getHumanType](../PresentationElement.html#getHumanType()), [getLineColor](../PresentationElement.html#getLineColor()), [getLineWidth](../PresentationElement.html#getLineWidth()), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point)), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getManipulationBounds](../PresentationElement.html#getManipulationBounds(java.awt.Point)), [getModelElement](../PresentationElement.html#getModelElement()), [getModelElementsForRelationshipConnecting](../PresentationElement.html#getModelElementsForRelationshipConnecting()), [getModelElementToConnectRelationship](../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [getModelElementToMove](../PresentationElement.html#getModelElementToMove()), [getNotZoomedTolerance](../PresentationElement.html#getNotZoomedTolerance()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getOwnStyleDelegate](../PresentationElement.html#getOwnStyleDelegate()), [getParent](../PresentationElement.html#getParent()), [getPreferredSize](../PresentationElement.html#getPreferredSize()), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(int)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementCount](../PresentationElement.html#getPresentationElementCount()), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getProjectImpl](../PresentationElement.html#getProjectImpl()), [getProperty](../PresentationElement.html#getProperty(java.lang.String)), [getPropertyManager](../PresentationElement.html#getPropertyManager()), [getPropertyManagerName](../PresentationElement.html#getPropertyManagerName()), [getRenderer](../PresentationElement.html#getRenderer()), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [getStyle](../PresentationElement.html#getStyle()), [getSymbolRenderer](../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getTextColor](../PresentationElement.html#getTextColor()), [getTolerance](../PresentationElement.html#getTolerance()), [getVisibility](../PresentationElement.html#getVisibility()), [getVisiblePresentationElements](../PresentationElement.html#getVisiblePresentationElements()), [handleModelDelete](../PresentationElement.html#handleModelDelete()), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [hasSharedModelElement](../PresentationElement.html#hasSharedModelElement()), [initializeAndAutosize](../PresentationElement.html#initializeAndAutosize()), [internalBeforeUpdate](../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)), [internalCreatePropertyChangeListener](../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [internalGetModelElementToConnectRelationship](../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [internalGetPresentationElementStroke](../PresentationElement.html#internalGetPresentationElementStroke(int)), [internalGetSpecificFont](../PresentationElement.html#internalGetSpecificFont()), [internalGetSpecificTextColor](../PresentationElement.html#internalGetSpecificTextColor()), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(float)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)), [intersects](../PresentationElement.html#intersects(int,int,int,int)), [isChildVisible](../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isCreateElementListener](../PresentationElement.html#isCreateElementListener()), [isDetectable](../PresentationElement.html#isDetectable()), [isDisposed](../PresentationElement.html#isDisposed()), [isLayouting](../PresentationElement.html#isLayouting()), [isMovableByMoveManager](../PresentationElement.html#isMovableByMoveManager()), [isNotNull](../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isPreserveProportionsWhenGrowing](../PresentationElement.html#isPreserveProportionsWhenGrowing()), [isSelected](../PresentationElement.html#isSelected()), [isShowElementTypeAsLabel](../PresentationElement.html#isShowElementTypeAsLabel()), [isSortable](../PresentationElement.html#isSortable()), [isSuitableToConnectRelationship](../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [isTextEditable](../PresentationElement.html#isTextEditable()), [isUseFillColor](../PresentationElement.html#isUseFillColor()), [isUseFillColorByProperty](../PresentationElement.html#isUseFillColorByProperty()), [isUseGradientForFill](../PresentationElement.html#isUseGradientForFill()), [isVisible](../PresentationElement.html#isVisible()), [isVisibleInDiagram](../PresentationElement.html#isVisibleInDiagram()), [isVisibleOrShrunken](../PresentationElement.html#isVisibleOrShrunken()), [movePathElementsRecursively](../PresentationElement.html#movePathElementsRecursively()), [notifyCreated](../PresentationElement.html#notifyCreated()), [notifyDiagramFrameSizeChange](../PresentationElement.html#notifyDiagramFrameSizeChange()), [notifyRepaintManager](../PresentationElement.html#notifyRepaintManager(boolean)), [onChildAdd](../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onChildRemove](../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onDiagramSurfaceSet](../PresentationElement.html#onDiagramSurfaceSet()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [onFontChange](../PresentationElement.html#onFontChange()), [onParentChange](../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [paintAdornments](../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintAdornmentsBackground](../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenAndAdornments](../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelfBackground](../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [preDisposeOnUpdate](../PresentationElement.html#preDisposeOnUpdate()), [prepareForLineDrawing](../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)), [prepareForTextDrawing](../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)), [recreateListeners](../PresentationElement.html#recreateListeners()), [registerInSortManager](../PresentationElement.html#registerInSortManager()), [rememberBounds](../PresentationElement.html#rememberBounds()), [rememberBounds](../PresentationElement.html#rememberBounds(java.awt.Rectangle)), [removeFromSortManager](../PresentationElement.html#removeFromSortManager()), [removeItSelfOnUpdate](../PresentationElement.html#removeItSelfOnUpdate()), [sAddPresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [selectChildrenForMoving](../PresentationElement.html#selectChildrenForMoving()), [selectObjectsForMoving](../PresentationElement.html#selectObjectsForMoving()), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setBounds](../PresentationElement.html#setBounds(int,int,int,int)), [setCreateElementListener](../PresentationElement.html#setCreateElementListener(boolean)), [setElement](../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setFont](../PresentationElement.html#setFont(java.awt.Font)), [setLayouting](../PresentationElement.html#setLayouting(boolean)), [setLineColor](../PresentationElement.html#setLineColor(java.awt.Color)), [setLineWidth](../PresentationElement.html#setLineWidth(int)), [setLoadedVisibility](../PresentationElement.html#setLoadedVisibility(boolean)), [setLocation](../PresentationElement.html#setLocation(int,int)), [setLocation](../PresentationElement.html#setLocation(java.awt.Point)), [setModelElement](../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [setNeedRecreateListeners](../PresentationElement.html#setNeedRecreateListeners(boolean)), [setPropertyManagerName](../PresentationElement.html#setPropertyManagerName(java.lang.String)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [setSize](../PresentationElement.html#setSize(int,int)), [setSize](../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)), [setSize](../PresentationElement.html#setSize(java.awt.Dimension)), [setTextColor](../PresentationElement.html#setTextColor(java.awt.Color)), [setUseFillColor](../PresentationElement.html#setUseFillColor(boolean)), [setVisible](../PresentationElement.html#setVisible(boolean)), [silentApply](../PresentationElement.html#silentApply()), [silentApply](../PresentationElement.html#silentApply(boolean)), [simpleSetBounds](../PresentationElement.html#simpleSetBounds(int,int,int,int)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Point,float)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)), [snapViewToGrid](../PresentationElement.html#snapViewToGrid(float)), [sortObjectsByX](../PresentationElement.html#sortObjectsByX(java.util.List)), [sortObjectsByY](../PresentationElement.html#sortObjectsByY(java.util.List)), [sSetBounds](../PresentationElement.html#sSetBounds(int,int,int,int)), [sSetElement](../PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [sSetLocation](../PresentationElement.html#sSetLocation(int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(java.awt.Point)), [sSetModelElement](../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [sSetParent](../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetParentForAll](../PresentationElement.html#sSetParentForAll(java.util.Collection)), [sSetSize](../PresentationElement.html#sSetSize(int,int)), [sSetSize](../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)), [sSetSize](../PresentationElement.html#sSetSize(java.awt.Dimension)), [sSetVisible](../PresentationElement.html#sSetVisible(boolean)), [tryToDeleteModelElementUponRemoval](../PresentationElement.html#tryToDeleteModelElementUponRemoval()), [update](../PresentationElement.html#update()), [updateAfterLoad](../PresentationElement.html#updateAfterLoad()), [updateLabelsIgnoringSuspendableLater](../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)), [updateModelByView](../PresentationElement.html#updateModelByView()), [updateModelByViewInternal](../PresentationElement.html#updateModelByViewInternal()), [useParentProperties](../PresentationElement.html#useParentProperties())`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, addPropertyChangeListener, canAdd, canAddChild, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../BaseElement.html)
`[canAdd](../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape
`asPresentationElement, getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY`
Methods inherited from interface com.nomagic.magicdraw.uml.[MDElement](../../MDElement.html)
`[getProject](../../MDElement.html#getProject())`

============ FIELD DETAIL =========== 
Field Details
TAG_DELIMITER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TAG_DELIMITER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.TAG_DELIMITER)
TAG_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TAG_NAME
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.TAG_NAME)
TAG_VALUE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TAG_VALUE
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.TAG_VALUE)
DIAGRAM_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_NAME
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.DIAGRAM_NAME)
DIAGRAM_TYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_TYPE
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.DIAGRAM_TYPE)
DOCUMENTATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DOCUMENTATION
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.DOCUMENTATION)
BGCOLOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BGCOLOR
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.BGCOLOR)
TXTCOLOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TXTCOLOR
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.TXTCOLOR)
PENCOLOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PENCOLOR
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.PENCOLOR)
FREE_SPACE
public static final int FREE_SPACE
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.FREE_SPACE)
TEMPLATE_FILE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TEMPLATE_FILE
DEFAULT_KEYWORDS
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> DEFAULT_KEYWORDS
BORDER_WIDTH
public static final int BORDER_WIDTH
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.BORDER_WIDTH)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramPropertiesShape
public DiagramPropertiesShape()
DiagramPropertiesShape
public DiagramPropertiesShape(@CheckForNull
 [PresentationElement](../PresentationElement.html) parent)
 ============ METHOD DETAIL ========== 
Method Details
isUseCustomHTML
public boolean isUseCustomHTML()
canDisplayHTMLText
public boolean canDisplayHTMLText()
Specified by:
`canDisplayHTMLText` in interface `com.nomagic.magicdraw.uml.symbols.shapes.PlainTextOrHTMLChangeable`
Overrides:
`[canDisplayHTMLText](TextBoxView.html#canDisplayHTMLText())` in class `[TextBoxView](TextBoxView.html)`
isHTMLText
public boolean isHTMLText()
Specified by:
`isHTMLText` in interface `com.nomagic.magicdraw.uml.symbols.shapes.PlainTextOrHTMLChangeable`
Overrides:
`isHTMLText` in class `com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView`
createTextArea
protected com.nomagic.magicdraw.uml.symbols.shapes.TextAreaView createTextArea()
Overrides:
`createTextArea` in class `com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView`
updateViewAfterPropertyChange
public void updateViewAfterPropertyChange()
Overrides:
`[updateViewAfterPropertyChange](../PresentationElement.html#updateViewAfterPropertyChange())` in class `[PresentationElement](../PresentationElement.html)`
internalSpecificUpdate
protected void internalSpecificUpdate()
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
Specific to every shape and model element update operation. Must be overridden in subclasses if you need to do specific tasks.
 !!! Important - all resizing, paths moving and so on is done in updatePresentationElement and should not be done in specific update.
Overrides:
`internalSpecificUpdate` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
See Also:
`AbstractHeaderShapeView.internalUpdatePresentationElement()`
atInsert
public void atInsert()
Description copied from class: `[PresentationElement](../PresentationElement.html#atInsert())`
Invalidates object at insert
Specified by:
`[atInsert](../../BaseElement.html#atInsert())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`[atInsert](../PresentationElement.html#atInsert())` in class `[PresentationElement](../PresentationElement.html)`
dispose
public void dispose()
Description copied from class: `[PresentationElement](../PresentationElement.html#dispose())`
disposes ends of links when link is deleted
Specified by:
`[dispose](../../BaseElement.html#dispose())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`[dispose](../paths/PathConnector.html#dispose())` in class `[PathConnector](../paths/PathConnector.html)`
getHTMLTemplateFileName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHTMLTemplateFileName()
constructStandardModeText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) constructStandardModeText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> keywords)
accept
public void accept([Visitor](../../Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
 See "Visitor" pattern for more details.
Specified by:
`[accept](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../../MDElement.html)`
Overrides:
`[accept](TextBoxView.html#accept(com.nomagic.magicdraw.uml.Visitor))` in class `[TextBoxView](TextBoxView.html)`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
canBeAutosized
public boolean canBeAutosized()
Overrides:
`[canBeAutosized](TextBoxView.html#canBeAutosized())` in class `[TextBoxView](TextBoxView.html)`
getElement
public [Diagram](../../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) getElement()
Description copied from class: `[PresentationElement](../PresentationElement.html#getElement())`
Returns model element of this presentation element. Some presentation elements (for example
 TextBoxes) do not have model elements.
Specified by:
`[getElement](../../ModelElementProvider.html#getElement())` in interface `[ModelElementProvider](../../ModelElementProvider.html)`
Overrides:
`[getElement](../PresentationElement.html#getElement())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
model element of this presentation element.
insertTaggedValues
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) insertTaggedValues([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) source)
getSelectedTags
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getSelectedTags()
Returns:
names of selected for displaying tag definitions names, including some hardcoded constants like DIAGRAM_NAME etc.
canHavePaths
public boolean canHavePaths()
Overrides:
`[canHavePaths](ShapeElement.html#canHavePaths())` in class `[ShapeElement](ShapeElement.html)`
Returns:
true if symbol can have connected paths. Return false here.
canBeDeleted
public boolean canBeDeleted()
Description copied from interface: `[BaseElement](../../BaseElement.html#canBeDeleted())`
Checks if an element can be deleted from a project.
 Element cannot be deleted if it is not isEditable(),
 parent is not set, or parent does not allow to remove this element.
Specified by:
`[canBeDeleted](../../BaseElement.html#canBeDeleted())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`canBeDeleted` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Returns:
true, if an element can be deleted from a project.
See Also:
[`BaseElement.isEditable()`](../../BaseElement.html#isEditable())
updateModificationTime
public static void updateModificationTime([Diagram](../../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Update diagram modification time
Parameters:
`diagram` - diagram
getHumanName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHumanName()
Description copied from class: `[PresentationElement](../PresentationElement.html#getHumanName())`
Returns human representation of the data type
Specified by:
`[getHumanName](../../BaseElement.html#getHumanName())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`getHumanName` in class `com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView`
Returns:
the name of the data
makeFreeSpaceInDiagram
public void makeFreeSpaceInDiagram()
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)
Description copied from class: `[PresentationElement](../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent))`
Listens for property change it can be: data was edited text box was edited
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
Overrides:
`[propertyChange](../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent))` in class `[PresentationElement](../PresentationElement.html)`
internalApplyProperties
public void internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)
Description copied from class: `[PresentationElement](../PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))`
Applies properties from given property manager
Overrides:
`[internalApplyProperties](TextBoxView.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))` in class `[TextBoxView](TextBoxView.html)`
Parameters:
`changer` - new properties
createSmartListenerConfig
protected void createSmartListenerConfig([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)
Overrides:
`[createSmartListenerConfig](../paths/PathConnector.html#createSmartListenerConfig(java.util.List))` in class `[PathConnector](../paths/PathConnector.html)`
canChangeParent
public boolean canChangeParent([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [PresentationElement](../PresentationElement.html)> movedTogether,
 @CheckForNull
 [BaseElement](../../BaseElement.html) newParent,
 boolean changeElementParent)
Description copied from class: `[PresentationElement](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean))`
Returns true, if element can change parent.
Overrides:
`[canChangeParent](TextBoxView.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean))` in class `[TextBoxView](TextBoxView.html)`
Parameters:
`movedTogether` - collection of the elements, whose will change the parent together with this.
`newParent` - new symbol parent
`changeElementParent` - change element parent
Returns:
true if parent of symbol can be changed
isInInitialPositionOnFrame
public boolean isInInitialPositionOnFrame()
Indicates if diagram properties shape is in the initial position and not moved by the user.
Returns:
true if diagram properties shape is in initial position, false otherwise.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.shapes</a></div>
<h1 class="title" title="Class DiagramPropertiesShape">Class DiagramPropertiesShape</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</a>
<div class="inheritance"><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView
<div class="inheritance"><a href="TextBoxView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">com.nomagic.magicdraw.uml.symbols.shapes.TextBoxView</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape</div>
</div>
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
<dd><code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.PlainTextOrHTMLChangeable</code>, <code>com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider</code>, <code>com.nomagic.magicdraw.uml.symbols.Wrapable</code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramPropertiesShape</span>
<span class="extends-implements">extends <a href="TextBoxView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TextBoxView</a></span></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BGCOLOR">BGCOLOR</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BORDER_WIDTH">BORDER_WIDTH</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_KEYWORDS">DEFAULT_KEYWORDS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_NAME">DIAGRAM_NAME</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_TYPE">DIAGRAM_TYPE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DOCUMENTATION">DOCUMENTATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FREE_SPACE">FREE_SPACE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PENCOLOR">PENCOLOR</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TAG_DELIMITER">TAG_DELIMITER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TAG_NAME">TAG_NAME</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TAG_VALUE">TAG_VALUE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_FILE">TEMPLATE_FILE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TXTCOLOR">TXTCOLOR</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView">Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</h3>
<code>CONTAINER_SHAPE_INSETS, SHAPE_DISTANCE_FROM_EDGE</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></h3>
<code><a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_ALL">BORDER_ELEMENT_MARGIN_ALL</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_BOTTOM">BORDER_ELEMENT_MARGIN_BOTTOM</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT">BORDER_ELEMENT_MARGIN_LEFT</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT_RIGHT">BORDER_ELEMENT_MARGIN_LEFT_RIGHT</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_MODES">BORDER_ELEMENT_MARGIN_MODES</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_NONE">BORDER_ELEMENT_MARGIN_NONE</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_RIGHT">BORDER_ELEMENT_MARGIN_RIGHT</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP">BORDER_ELEMENT_MARGIN_TOP</a>, <a href="ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP_BOTTOM">BORDER_ELEMENT_MARGIN_TOP_BOTTOM</a>, <a href="ShapeElement.html#BOTTOM_EDGE">BOTTOM_EDGE</a>, <a href="ShapeElement.html#INSIDE_EDGE_POSITION">INSIDE_EDGE_POSITION</a>, <a href="ShapeElement.html#LEFT_EDGE">LEFT_EDGE</a>, <a href="ShapeElement.html#NEED_AUTOSIZE_FULL">NEED_AUTOSIZE_FULL</a>, <a href="ShapeElement.html#NEED_AUTOSIZE_LAYOUT">NEED_AUTOSIZE_LAYOUT</a>, <a href="ShapeElement.html#NEED_AUTOSIZE_NONE">NEED_AUTOSIZE_NONE</a>, <a href="ShapeElement.html#NO_EDGE">NO_EDGE</a>, <a href="ShapeElement.html#NULL_INSETS">NULL_INSETS</a>, <a href="ShapeElement.html#ON_EDGE_POSITION">ON_EDGE_POSITION</a>, <a href="ShapeElement.html#OUTSIDE_EDGE_POSITION">OUTSIDE_EDGE_POSITION</a>, <a href="ShapeElement.html#RIGHT_EDGE">RIGHT_EDGE</a>, <a href="ShapeElement.html#SPACE">SPACE</a>, <a href="ShapeElement.html#SPACE_INSETS">SPACE_INSETS</a>, <a href="ShapeElement.html#SPACE_INSETS_EMPTY_TOP_BOTTOM">SPACE_INSETS_EMPTY_TOP_BOTTOM</a>, <a href="ShapeElement.html#TOP_EDGE">TOP_EDGE</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="../paths/PathConnector.html#showsProxy">showsProxy</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DiagramPropertiesShape</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement)">DiagramPropertiesShape</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#atInsert()">atInsert</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invalidates object at insert</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canBeAutosized()">canBeAutosized</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canBeDeleted()">canBeDeleted</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if an element can be deleted from a project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">canChangeParent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether,
 <a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent,
 boolean changeElementParent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if element can change parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canDisplayHTMLText()">canDisplayHTMLText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canHavePaths()">canHavePaths</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#constructStandardModeText(java.util.Collection)">constructStandardModeText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; keywords)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.uml.symbols.shapes.TextAreaView</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTextArea()">createTextArea</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">disposes ends of links when link is deleted</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model element of this presentation element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getHTMLTemplateFileName()">getHTMLTemplateFileName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHumanName()">getHumanName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns human representation of the data type</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedTags()">getSelectedTags</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#insertTaggedValues(java.lang.String)">insertTaggedValues</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies properties from given property manager</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSpecificUpdate()">internalSpecificUpdate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Specific to every shape and model element update operation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHTMLText()">isHTMLText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInInitialPositionOnFrame()">isInInitialPositionOnFrame</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if diagram properties shape is in the initial position and not moved by the user.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseCustomHTML()">isUseCustomHTML</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#makeFreeSpaceInDiagram()">makeFreeSpaceInDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens for property change it can be: data was edited text box was edited</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#updateModificationTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">updateModificationTime</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Update diagram modification time</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.TextBoxView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.<a href="TextBoxView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TextBoxView</a></h3>
<code><a href="TextBoxView.html#canFill()">canFill</a>, <a href="TextBoxView.html#checkShowsProxy()">checkShowsProxy</a>, <a href="TextBoxView.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a>, <a href="TextBoxView.html#getDefaultDimension()">getDefaultDimension</a>, <a href="TextBoxView.html#getDynamicStyleOwner()">getDynamicStyleOwner</a>, <a href="TextBoxView.html#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a>, <a href="TextBoxView.html#internalSilentApply()">internalSilentApply</a>, <a href="TextBoxView.html#isLabelMode()">isLabelMode</a>, <a href="TextBoxView.html#isTextBoxLabelMode(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isTextBoxLabelMode</a>, <a href="TextBoxView.html#mustShowContextMenu()">mustShowContextMenu</a>, <a href="TextBoxView.html#needAdjustToMaximumDimension()">needAdjustToMaximumDimension</a>, <a href="TextBoxView.html#resizeParent()">resizeParent</a>, <a href="TextBoxView.html#rotateBoundsForHeaderOrientation(java.awt.Rectangle)">rotateBoundsForHeaderOrientation</a>, <a href="TextBoxView.html#setForcedToBeFillable(boolean)">setForcedToBeFillable</a>, <a href="TextBoxView.html#setHeaderOrientationVertical(boolean)">setHeaderOrientationVertical</a>, <a href="TextBoxView.html#setLabelMode(boolean)">setLabelMode</a>, <a href="TextBoxView.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a>, <a href="TextBoxView.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a>, <a href="TextBoxView.html#useParentStyle()">useParentStyle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractTextBoxView</h3>
<code>internalGetHeaderInsets, minimumSizeForShrinkingIgnoringOrientation, paintSelf, providesHorizontalCenterline, providesVerticalCenterline, snapsToCenterlines</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView</h3>
<code>clone, editName, getName, getNameLabel, getTextObject, getUserText, hasText, internalGetSelfManipulationPreferredSize, isHeaderOrientationVertical, isWrapEnabled, setAutosize, setHTMLText, setName, setTextObject, setWrapEnabled, sSetAutosize, sSetHeaderOrientationVertical, sSetHTMLText, sSetName, sSetTextObject, sSetWrapEnabled</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</h3>
<code>addExtraChildrenPrefSizePadding, adjustBoundsBeforeChange, autosize, autosizeAndResizeParent, calculateMinY, calculateOvalShapePreferredSize, canAddInstance, correctChildrenVector, coversPoint, createBoundsShape, createStateForUpdateOperation, doInternalLayoutChildren, getAdditionalHeaderHeightForPreferredBounds, getChildrenBoundsForPreferredBounds, getHeaderBoundsForPreferredBounds, getHeaderDistanceFromTopForOvalShape, getHeaderInsets, getHeaderMaxYForShrinkableShape, getHeaderObject, getHeaderVerticalPosition, getHeaderVerticalPositionForLayout, getOvalShapeAvailableWidth, getPreferredBounds, getPresentationElementAt, getProxyPresentationElementsStream, getStereotypesToDisplay, internalGetHeaderBoundsForPreferredBounds, internalLayoutChildren, internalPostSpecificUpdate, internalPostUpdatePresentationElement, internalPreSpecificUpdate, internalUpdatePresentationElement, invalidate, isBorderVisible, isChildLayoutable, isContentHidden, isOvalShape, isParentShowsProxy, minimumDimension, minimumDimensionForShrinking, minimumSizeIgnoringOrientation, paintChildren, preferredDimension, preferredSizeIgnoringOrientation, setHeaderObject, setHeaderVerticalPosition, setTextEditable, sSetHeaderVerticalPosition, switchWidthHeightIfVerticalOrientation</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</h3>
<code>addPresentationElement, addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, canAddChild, canMoveChildOutside, childrenBoundsForReshape, clearShowsProxy, constructLayoutHelper, getChildrenBounds, getChildrenInsets, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getRemovableChildren, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalAppendChildRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildrenBackground, prefDimensionByManipulatedChildren, recursiveAutosize, removePresentationElement, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></h3>
<code><a href="ShapeElement.html#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addBreakPoints</a>, <a href="ShapeElement.html#adjustBounds(java.awt.Rectangle)">adjustBounds</a>, <a href="ShapeElement.html#adjustOnEdge()">adjustOnEdge</a>, <a href="ShapeElement.html#adjustOnEdge(java.awt.Rectangle,int,int,int)">adjustOnEdge</a>, <a href="ShapeElement.html#adjustOnEdgeChildren()">adjustOnEdgeChildren</a>, <a href="ShapeElement.html#autosize()">autosize</a>, <a href="ShapeElement.html#calculateAdjustOnEdgeLocation(java.awt.Rectangle)">calculateAdjustOnEdgeLocation</a>, <a href="ShapeElement.html#calculateAndGetMinimumShrinkingDimension(int,int)">calculateAndGetMinimumShrinkingDimension</a>, <a href="ShapeElement.html#calculateAndGetPreferredDimension()">calculateAndGetPreferredDimension</a>, <a href="ShapeElement.html#calculateEdge()">calculateEdge</a>, <a href="ShapeElement.html#calculateMinimumDimension()">calculateMinimumDimension</a>, <a href="ShapeElement.html#calculateOnEdgeBounds()">calculateOnEdgeBounds</a>, <a href="ShapeElement.html#calculatePreferredDimension()">calculatePreferredDimension</a>, <a href="ShapeElement.html#calculatePreferredDimension(int,int)">calculatePreferredDimension</a>, <a href="ShapeElement.html#clearOldRect()">clearOldRect</a>, <a href="ShapeElement.html#edgeChanged()">edgeChanged</a>, <a href="ShapeElement.html#ensureDimension(boolean)">ensureDimension</a>, <a href="ShapeElement.html#ensurePreferredDimensionIfShrinkable()">ensurePreferredDimensionIfShrinkable</a>, <a href="ShapeElement.html#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)">ensurePreferredDimensionIfShrinkable</a>, <a href="ShapeElement.html#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)">findFreePlaceForShapeOnBorder</a>, <a href="ShapeElement.html#getBorderElementMargin()">getBorderElementMargin</a>, <a href="ShapeElement.html#getBounds()">getBounds</a>, <a href="ShapeElement.html#getCenterlineableInnerParts(int)">getCenterlineableInnerParts</a>, <a href="ShapeElement.html#getDimensionForShrinking(int,int)">getDimensionForShrinking</a>, <a href="ShapeElement.html#getEdgeLine(int)">getEdgeLine</a>, <a href="ShapeElement.html#getFixedConnectionPoints()">getFixedConnectionPoints</a>, <a href="ShapeElement.html#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)">getHeaderInsetReduce</a>, <a href="ShapeElement.html#getInsetsForOnEdgeShapes()">getInsetsForOnEdgeShapes</a>, <a href="ShapeElement.html#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="ShapeElement.html#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)">getIntersection</a>, <a href="ShapeElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="ShapeElement.html#getLoadedDimension()">getLoadedDimension</a>, <a href="ShapeElement.html#getMiddlePoint()">getMiddlePoint</a>, <a href="ShapeElement.html#getMiddlePoint(java.awt.Point)">getMiddlePoint</a>, <a href="ShapeElement.html#getMiddlePointX()">getMiddlePointX</a>, <a href="ShapeElement.html#getMiddlePointX(java.awt.Point)">getMiddlePointX</a>, <a href="ShapeElement.html#getMiddlePointY()">getMiddlePointY</a>, <a href="ShapeElement.html#getMiddlePointY(java.awt.Point)">getMiddlePointY</a>, <a href="ShapeElement.html#getMinimumDimension()">getMinimumDimension</a>, <a href="ShapeElement.html#getNearestEdge(int,int)">getNearestEdge</a>, <a href="ShapeElement.html#getNearestEdge(java.awt.Rectangle)">getNearestEdge</a>, <a href="ShapeElement.html#getNeedAutosizeFlag()">getNeedAutosizeFlag</a>, <a href="ShapeElement.html#getNotCopyBounds()">getNotCopyBounds</a>, <a href="ShapeElement.html#getOnEdge()">getOnEdge</a>, <a href="ShapeElement.html#getOnEdgeCornerDistance()">getOnEdgeCornerDistance</a>, <a href="ShapeElement.html#getOnEdgePosition()">getOnEdgePosition</a>, <a href="ShapeElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="ShapeElement.html#getPreferredDimensionForAutosize()">getPreferredDimensionForAutosize</a>, <a href="ShapeElement.html#getReshapeMode()">getReshapeMode</a>, <a href="ShapeElement.html#getSizeForDrawing()">getSizeForDrawing</a>, <a href="ShapeElement.html#getSuspendShapeAutoResizeMode()">getSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#hasManipulator()">hasManipulator</a>, <a href="ShapeElement.html#initialize()">initialize</a>, <a href="ShapeElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a>, <a href="ShapeElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a>, <a href="ShapeElement.html#isAutosized()">isAutosized</a>, <a href="ShapeElement.html#isCenterlineInner()">isCenterlineInner</a>, <a href="ShapeElement.html#isHorizontalCenterlineProvider()">isHorizontalCenterlineProvider</a>, <a href="ShapeElement.html#isOnEdge()">isOnEdge</a>, <a href="ShapeElement.html#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isShapeOnEdge</a>, <a href="ShapeElement.html#isShrinkable()">isShrinkable</a>, <a href="ShapeElement.html#isSnapShapesOnBorderToGrid()">isSnapShapesOnBorderToGrid</a>, <a href="ShapeElement.html#isSnapToGrid()">isSnapToGrid</a>, <a href="ShapeElement.html#isUseFixedConnectionPoints()">isUseFixedConnectionPoints</a>, <a href="ShapeElement.html#isVerticalCenterlineProvider()">isVerticalCenterlineProvider</a>, <a href="ShapeElement.html#layoutChildren()">layoutChildren</a>, <a href="ShapeElement.html#maximumDimension(java.awt.Dimension)">maximumDimension</a>, <a href="ShapeElement.html#minimumOrMinimumShrinkableDimension(java.awt.Dimension)">minimumOrMinimumShrinkableDimension</a>, <a href="ShapeElement.html#moveLinksToSelf()">moveLinksToSelf</a>, <a href="ShapeElement.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a>, <a href="ShapeElement.html#movePathElements()">movePathElements</a>, <a href="ShapeElement.html#onChildEdgeChange(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">onChildEdgeChange</a>, <a href="ShapeElement.html#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a>, <a href="ShapeElement.html#resetCalculatePreferredRegardingChildren()">resetCalculatePreferredRegardingChildren</a>, <a href="ShapeElement.html#setBorderElementMargin(java.lang.String)">setBorderElementMargin</a>, <a href="ShapeElement.html#setCalculatePreferredRegardingChildren(boolean)">setCalculatePreferredRegardingChildren</a>, <a href="ShapeElement.html#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)">setLoadedDimension</a>, <a href="ShapeElement.html#setMinimumDimension(int,int)">setMinimumDimension</a>, <a href="ShapeElement.html#setNeedAutosizeFlag(byte)">setNeedAutosizeFlag</a>, <a href="ShapeElement.html#setOldRect(java.awt.Rectangle)">setOldRect</a>, <a href="ShapeElement.html#setOnEdge(int)">setOnEdge</a>, <a href="ShapeElement.html#setPreferredDimension(int,int)">setPreferredDimension</a>, <a href="ShapeElement.html#setReshapeMode(com.nomagic.magicdraw.uml.symbols.ReshapeMode)">setReshapeMode</a>, <a href="ShapeElement.html#setSnapShapesOnBorderToGrid(boolean)">setSnapShapesOnBorderToGrid</a>, <a href="ShapeElement.html#setSuspendShapeAutoResizeMode(java.lang.String)">setSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#setUseFixedConnectionPoints(boolean)">setUseFixedConnectionPoints</a>, <a href="ShapeElement.html#shouldDrawShadow()">shouldDrawShadow</a>, <a href="ShapeElement.html#simpleSetBounds(int,int,int,int,boolean)">simpleSetBounds</a>, <a href="ShapeElement.html#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a>, <a href="ShapeElement.html#sSetBorderElementMargin(java.lang.String)">sSetBorderElementMargin</a>, <a href="ShapeElement.html#sSetBounds(java.awt.Rectangle)">sSetBounds</a>, <a href="ShapeElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)">sSetSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#toString()">toString</a>, <a href="ShapeElement.html#updateLater()">updateLater</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addConnectedPathElement</a>, <a href="../paths/PathConnector.html#disposeConnectedPaths()">disposeConnectedPaths</a>, <a href="../paths/PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">findSymbolForEnd</a>, <a href="../paths/PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)">findSymbolForEnd</a>, <a href="../paths/PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">getConnectedPathElement</a>, <a href="../paths/PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="../paths/PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getPreferredArrowLength()">getPreferredArrowLength</a>, <a href="../paths/PathConnector.html#isShowsProxy()">isShowsProxy</a>, <a href="../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)">movePathElement</a>, <a href="../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">removeConnectedPathElement</a>, <a href="../paths/PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sAddConnectedPathElement</a>, <a href="../paths/PathConnector.html#selectPathsForMoving(java.util.List)">selectPathsForMoving</a>, <a href="../paths/PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a>, <a href="../paths/PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sRemoveConnectedPathElement</a>, <a href="../paths/PathConnector.html#sSetConnectedPathElements(java.util.List)">sSetConnectedPathElements</a>, <a href="../paths/PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible()">supportsVisibleConnectedPathElementsIfSelfInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a>, <a href="../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBounds</a>, <a href="../PresentationElement.html#alwaysShowTooltip()">alwaysShowTooltip</a>, <a href="../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">applyProperties</a>, <a href="../PresentationElement.html#askDeleteDataConfirmation()">askDeleteDataConfirmation</a>, <a href="../PresentationElement.html#atInsertChildren()">atInsertChildren</a>, <a href="../PresentationElement.html#autosizeAndResizeManipulatedParent()">autosizeAndResizeManipulatedParent</a>, <a href="../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">beforeDelete</a>, <a href="../PresentationElement.html#boundsChanged()">boundsChanged</a>, <a href="../PresentationElement.html#boundsChanged(java.awt.Rectangle)">boundsChanged</a>, <a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../PresentationElement.html#canBeDisposedOnUpdate()">canBeDisposedOnUpdate</a>, <a href="../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeElementOwner</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">changeProperties</a>, <a href="../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a>, <a href="../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">checkProxyVisibility</a>, <a href="../PresentationElement.html#childrenForMoving()">childrenForMoving</a>, <a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)">collectSubShowingPresentationElements</a>, <a href="../PresentationElement.html#coversPoint(int,int)">coversPoint</a>, <a href="../PresentationElement.html#createFillStrategy()">createFillStrategy</a>, <a href="../PresentationElement.html#createPresentationElementStyle()">createPresentationElementStyle</a>, <a href="../PresentationElement.html#createPropertyChangeListener()">createPropertyChangeListener</a>, <a href="../PresentationElement.html#disposeChildren()">disposeChildren</a>, <a href="../PresentationElement.html#disposePropertyChangeListener()">disposePropertyChangeListener</a>, <a href="../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawBackground</a>, <a href="../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbol</a>, <a href="../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbolBackground</a>, <a href="../PresentationElement.html#dynamicFillColor()">dynamicFillColor</a>, <a href="../PresentationElement.html#dynamicLineColor()">dynamicLineColor</a>, <a href="../PresentationElement.html#dynamicLineWidth()">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicLineWidth(int)">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicPaintShadow()">dynamicPaintShadow</a>, <a href="../PresentationElement.html#dynamicStroke()">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(int)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)">dynamicStyleFillColor</a>, <a href="../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)">dynamicStyleLineColor</a>, <a href="../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)">dynamicStyleTextColor</a>, <a href="../PresentationElement.html#dynamicStyleTransparency()">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)">dynamicStyleValue</a>, <a href="../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">dynamicTextAlignment</a>, <a href="../PresentationElement.html#dynamicTextColor()">dynamicTextColor</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOwnerForChildElement</a>, <a href="../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a>, <a href="../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">findPresentationElement</a>, <a href="../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../PresentationElement.html#generateID()">generateID</a>, <a href="../PresentationElement.html#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>, <a href="../PresentationElement.html#getActualElement()">getActualElement</a>, <a href="../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()">getAdditionalRenderersToNotifyOnPropertiesChange</a>, <a href="../PresentationElement.html#getAssignableModelElementsClasses()">getAssignableModelElementsClasses</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getBoundsToRepaint()">getBoundsToRepaint</a>, <a href="../PresentationElement.html#getBoundsWithChildrenOnEdge()">getBoundsWithChildrenOnEdge</a>, <a href="../PresentationElement.html#getCenterlinePoint()">getCenterlinePoint</a>, <a href="../PresentationElement.html#getCenterlinePointX()">getCenterlinePointX</a>, <a href="../PresentationElement.html#getCenterlinePointY()">getCenterlinePointY</a>, <a href="../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)">getChildPresentationElementForContextMenu</a>, <a href="../PresentationElement.html#getChildrenWithSymbolProperties()">getChildrenWithSymbolProperties</a>, <a href="../PresentationElement.html#getConfiguration()">getConfiguration</a>, <a href="../PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="../PresentationElement.html#getDiagramSurface()">getDiagramSurface</a>, <a href="../PresentationElement.html#getDrawComparator()">getDrawComparator</a>, <a href="../PresentationElement.html#getDynamicConfigurations()">getDynamicConfigurations</a>, <a href="../PresentationElement.html#getEffectiveStyleDelegate()">getEffectiveStyleDelegate</a>, <a href="../PresentationElement.html#getEffectiveStyleOwner()">getEffectiveStyleOwner</a>, <a href="../PresentationElement.html#getElementsForRelationshipConnecting()">getElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementToConnectRelationship</a>, <a href="../PresentationElement.html#getFillColor()">getFillColor</a>, <a href="../PresentationElement.html#getFont()">getFont</a>, <a href="../PresentationElement.html#getFontHeight()">getFontHeight</a>, <a href="../PresentationElement.html#getFontRenderContext()">getFontRenderContext</a>, <a href="../PresentationElement.html#getHumanType()">getHumanType</a>, <a href="../PresentationElement.html#getLineColor()">getLineColor</a>, <a href="../PresentationElement.html#getLineWidth()">getLineWidth</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getManipulationBounds(java.awt.Point)">getManipulationBounds</a>, <a href="../PresentationElement.html#getModelElement()">getModelElement</a>, <a href="../PresentationElement.html#getModelElementsForRelationshipConnecting()">getModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">getModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#getModelElementToMove()">getModelElementToMove</a>, <a href="../PresentationElement.html#getNotZoomedTolerance()">getNotZoomedTolerance</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getOwnStyleDelegate()">getOwnStyleDelegate</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="../PresentationElement.html#getPresentationElementAt(int)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementCount()">getPresentationElementCount</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getProjectImpl()">getProjectImpl</a>, <a href="../PresentationElement.html#getProperty(java.lang.String)">getProperty</a>, <a href="../PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="../PresentationElement.html#getPropertyManagerName()">getPropertyManagerName</a>, <a href="../PresentationElement.html#getRenderer()">getRenderer</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#getStyle()">getStyle</a>, <a href="../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSymbolRenderer</a>, <a href="../PresentationElement.html#getTextColor()">getTextColor</a>, <a href="../PresentationElement.html#getTolerance()">getTolerance</a>, <a href="../PresentationElement.html#getVisibility()">getVisibility</a>, <a href="../PresentationElement.html#getVisiblePresentationElements()">getVisiblePresentationElements</a>, <a href="../PresentationElement.html#handleModelDelete()">handleModelDelete</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#hasSharedModelElement()">hasSharedModelElement</a>, <a href="../PresentationElement.html#initializeAndAutosize()">initializeAndAutosize</a>, <a href="../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)">internalBeforeUpdate</a>, <a href="../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">internalCreatePropertyChangeListener</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a>, <a href="../PresentationElement.html#internalGetSpecificFont()">internalGetSpecificFont</a>, <a href="../PresentationElement.html#internalGetSpecificTextColor()">internalGetSpecificTextColor</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalSnapToGrid(float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#intersects(int,int,int,int)">intersects</a>, <a href="../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildVisible</a>, <a href="../PresentationElement.html#isCreateElementListener()">isCreateElementListener</a>, <a href="../PresentationElement.html#isDetectable()">isDetectable</a>, <a href="../PresentationElement.html#isDisposed()">isDisposed</a>, <a href="../PresentationElement.html#isLayouting()">isLayouting</a>, <a href="../PresentationElement.html#isMovableByMoveManager()">isMovableByMoveManager</a>, <a href="../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNotNull</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isParentOf</a>, <a href="../PresentationElement.html#isPreserveProportionsWhenGrowing()">isPreserveProportionsWhenGrowing</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#isShowElementTypeAsLabel()">isShowElementTypeAsLabel</a>, <a href="../PresentationElement.html#isSortable()">isSortable</a>, <a href="../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">isSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#isTextEditable()">isTextEditable</a>, <a href="../PresentationElement.html#isUseFillColor()">isUseFillColor</a>, <a href="../PresentationElement.html#isUseFillColorByProperty()">isUseFillColorByProperty</a>, <a href="../PresentationElement.html#isUseGradientForFill()">isUseGradientForFill</a>, <a href="../PresentationElement.html#isVisible()">isVisible</a>, <a href="../PresentationElement.html#isVisibleInDiagram()">isVisibleInDiagram</a>, <a href="../PresentationElement.html#isVisibleOrShrunken()">isVisibleOrShrunken</a>, <a href="../PresentationElement.html#movePathElementsRecursively()">movePathElementsRecursively</a>, <a href="../PresentationElement.html#notifyCreated()">notifyCreated</a>, <a href="../PresentationElement.html#notifyDiagramFrameSizeChange()">notifyDiagramFrameSizeChange</a>, <a href="../PresentationElement.html#notifyRepaintManager(boolean)">notifyRepaintManager</a>, <a href="../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildAdd</a>, <a href="../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildRemove</a>, <a href="../PresentationElement.html#onDiagramSurfaceSet()">onDiagramSurfaceSet</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#onFontChange()">onFontChange</a>, <a href="../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">onParentChange</a>, <a href="../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornments</a>, <a href="../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornmentsBackground</a>, <a href="../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenAndAdornments</a>, <a href="../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelfBackground</a>, <a href="../PresentationElement.html#preDisposeOnUpdate()">preDisposeOnUpdate</a>, <a href="../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)">prepareForLineDrawing</a>, <a href="../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)">prepareForTextDrawing</a>, <a href="../PresentationElement.html#recreateListeners()">recreateListeners</a>, <a href="../PresentationElement.html#registerInSortManager()">registerInSortManager</a>, <a href="../PresentationElement.html#rememberBounds()">rememberBounds</a>, <a href="../PresentationElement.html#rememberBounds(java.awt.Rectangle)">rememberBounds</a>, <a href="../PresentationElement.html#removeFromSortManager()">removeFromSortManager</a>, <a href="../PresentationElement.html#removeItSelfOnUpdate()">removeItSelfOnUpdate</a>, <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sAddPresentationElement</a>, <a href="../PresentationElement.html#selectChildrenForMoving()">selectChildrenForMoving</a>, <a href="../PresentationElement.html#selectObjectsForMoving()">selectObjectsForMoving</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setBounds(int,int,int,int)">setBounds</a>, <a href="../PresentationElement.html#setCreateElementListener(boolean)">setCreateElementListener</a>, <a href="../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a>, <a href="../PresentationElement.html#setFont(java.awt.Font)">setFont</a>, <a href="../PresentationElement.html#setLayouting(boolean)">setLayouting</a>, <a href="../PresentationElement.html#setLineColor(java.awt.Color)">setLineColor</a>, <a href="../PresentationElement.html#setLineWidth(int)">setLineWidth</a>, <a href="../PresentationElement.html#setLoadedVisibility(boolean)">setLoadedVisibility</a>, <a href="../PresentationElement.html#setLocation(int,int)">setLocation</a>, <a href="../PresentationElement.html#setLocation(java.awt.Point)">setLocation</a>, <a href="../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">setModelElement</a>, <a href="../PresentationElement.html#setNeedRecreateListeners(boolean)">setNeedRecreateListeners</a>, <a href="../PresentationElement.html#setPropertyManagerName(java.lang.String)">setPropertyManagerName</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#setSize(int,int)">setSize</a>, <a href="../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)">setSize</a>, <a href="../PresentationElement.html#setSize(java.awt.Dimension)">setSize</a>, <a href="../PresentationElement.html#setTextColor(java.awt.Color)">setTextColor</a>, <a href="../PresentationElement.html#setUseFillColor(boolean)">setUseFillColor</a>, <a href="../PresentationElement.html#setVisible(boolean)">setVisible</a>, <a href="../PresentationElement.html#silentApply()">silentApply</a>, <a href="../PresentationElement.html#silentApply(boolean)">silentApply</a>, <a href="../PresentationElement.html#simpleSetBounds(int,int,int,int)">simpleSetBounds</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Point,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapViewToGrid(float)">snapViewToGrid</a>, <a href="../PresentationElement.html#sortObjectsByX(java.util.List)">sortObjectsByX</a>, <a href="../PresentationElement.html#sortObjectsByY(java.util.List)">sortObjectsByY</a>, <a href="../PresentationElement.html#sSetBounds(int,int,int,int)">sSetBounds</a>, <a href="../PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">sSetElement</a>, <a href="../PresentationElement.html#sSetLocation(int,int)">sSetLocation</a>, <a href="../PresentationElement.html#sSetLocation(java.awt.Point)">sSetLocation</a>, <a href="../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">sSetModelElement</a>, <a href="../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a>, <a href="../PresentationElement.html#sSetParentForAll(java.util.Collection)">sSetParentForAll</a>, <a href="../PresentationElement.html#sSetSize(int,int)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(java.awt.Dimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetVisible(boolean)">sSetVisible</a>, <a href="../PresentationElement.html#tryToDeleteModelElementUponRemoval()">tryToDeleteModelElementUponRemoval</a>, <a href="../PresentationElement.html#update()">update</a>, <a href="../PresentationElement.html#updateAfterLoad()">updateAfterLoad</a>, <a href="../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)">updateLabelsIgnoringSuspendableLater</a>, <a href="../PresentationElement.html#updateModelByView()">updateModelByView</a>, <a href="../PresentationElement.html#updateModelByViewInternal()">updateModelByViewInternal</a>, <a href="../PresentationElement.html#useParentProperties()">useParentProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, addPropertyChangeListener, canAdd, canAddChild, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../BaseElement.html#isSelfChangeable()">isSelfChangeable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape">Methods inherited from interface com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</h3>
<code>asPresentationElement, getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></h3>
<code><a href="../../MDElement.html#getProject()">getProject</a></code></div>
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
<section class="detail" id="TAG_DELIMITER">
<h3>TAG_DELIMITER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TAG_DELIMITER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.TAG_DELIMITER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TAG_NAME">
<h3>TAG_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TAG_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.TAG_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TAG_VALUE">
<h3>TAG_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TAG_VALUE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.TAG_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_NAME">
<h3>DIAGRAM_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.DIAGRAM_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_TYPE">
<h3>DIAGRAM_TYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_TYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.DIAGRAM_TYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOCUMENTATION">
<h3>DOCUMENTATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOCUMENTATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.DOCUMENTATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BGCOLOR">
<h3>BGCOLOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BGCOLOR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.BGCOLOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TXTCOLOR">
<h3>TXTCOLOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TXTCOLOR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.TXTCOLOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PENCOLOR">
<h3>PENCOLOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PENCOLOR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.PENCOLOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FREE_SPACE">
<h3>FREE_SPACE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">FREE_SPACE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.FREE_SPACE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_FILE">
<h3>TEMPLATE_FILE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_FILE</span></div>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_KEYWORDS">
<h3>DEFAULT_KEYWORDS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">DEFAULT_KEYWORDS</span></div>
</section>
</li>
<li>
<section class="detail" id="BORDER_WIDTH">
<h3>BORDER_WIDTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">BORDER_WIDTH</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.DiagramPropertiesShape.BORDER_WIDTH">Constant Field Values</a></li>
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
<h3>DiagramPropertiesShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramPropertiesShape</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>DiagramPropertiesShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramPropertiesShape</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span></div>
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
<section class="detail" id="isUseCustomHTML()">
<h3>isUseCustomHTML</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseCustomHTML</span>()</div>
</section>
</li>
<li>
<section class="detail" id="canDisplayHTMLText()">
<h3>canDisplayHTMLText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canDisplayHTMLText</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>canDisplayHTMLText</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.PlainTextOrHTMLChangeable</code></dd>
<dt>Overrides:</dt>
<dd><code><a href="TextBoxView.html#canDisplayHTMLText()">canDisplayHTMLText</a></code> in class <code><a href="TextBoxView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TextBoxView</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isHTMLText()">
<h3>isHTMLText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isHTMLText</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isHTMLText</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.PlainTextOrHTMLChangeable</code></dd>
<dt>Overrides:</dt>
<dd><code>isHTMLText</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTextArea()">
<h3>createTextArea</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.TextAreaView</span> <span class="element-name">createTextArea</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createTextArea</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateViewAfterPropertyChange()">
<h3>updateViewAfterPropertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateViewAfterPropertyChange</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalSpecificUpdate()">
<h3>internalSpecificUpdate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalSpecificUpdate</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></span></div>
<div class="block">Specific to every shape and model element update operation. Must be overridden in subclasses if you need to do specific tasks.
 !!! Important - all resizing, paths moving and so on is done in updatePresentationElement and should not be done in specific update.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalSpecificUpdate</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>AbstractHeaderShapeView.internalUpdatePresentationElement()</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="atInsert()">
<h3>atInsert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">atInsert</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#atInsert()">PresentationElement</a></code></span></div>
<div class="block">Invalidates object at insert</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#atInsert()">atInsert</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#atInsert()">atInsert</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
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
<dd><code><a href="../paths/PathConnector.html#dispose()">dispose</a></code> in class <code><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHTMLTemplateFileName()">
<h3>getHTMLTemplateFileName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHTMLTemplateFileName</span>()</div>
</section>
</li>
<li>
<section class="detail" id="constructStandardModeText(java.util.Collection)">
<h3>constructStandardModeText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructStandardModeText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; keywords)</span></div>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.Visitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../../Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">MDElement</a></code></span></div>
<div class="block">Method accepts a visitor, and calls method "visit&lt;class name&gt;(this)" of a visitor.
 See "Visitor" pattern for more details.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a></code> in interface <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="TextBoxView.html#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a></code> in class <code><a href="TextBoxView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TextBoxView</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeAutosized()">
<h3>canBeAutosized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canBeAutosized</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="TextBoxView.html#canBeAutosized()">canBeAutosized</a></code> in class <code><a href="TextBoxView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TextBoxView</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></span> <span class="element-name">getElement</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getElement()">PresentationElement</a></code></span></div>
<div class="block">Returns model element of this presentation element. Some presentation elements (for example
 TextBoxes) do not have model elements.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../ModelElementProvider.html#getElement()">getElement</a></code> in interface <code><a href="../../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getElement()">getElement</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>model element of this presentation element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="insertTaggedValues(java.lang.String)">
<h3>insertTaggedValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">insertTaggedValues</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSelectedTags()">
<h3>getSelectedTags</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getSelectedTags</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>names of selected for displaying tag definitions names, including some hardcoded constants like DIAGRAM_NAME etc.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canHavePaths()">
<h3>canHavePaths</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canHavePaths</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#canHavePaths()">canHavePaths</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if symbol can have connected paths. Return false here.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeDeleted()">
<h3>canBeDeleted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canBeDeleted</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../BaseElement.html#canBeDeleted()">BaseElement</a></code></span></div>
<div class="block">Checks if an element can be deleted from a project.
 Element cannot be deleted if it is not isEditable(),
 parent is not set, or parent does not allow to remove this element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#canBeDeleted()">canBeDeleted</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>canBeDeleted</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Returns:</dt>
<dd>true, if an element can be deleted from a project.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../BaseElement.html#isEditable()"><code>BaseElement.isEditable()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateModificationTime(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>updateModificationTime</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">updateModificationTime</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Update diagram modification time</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHumanName()">
<h3>getHumanName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanName</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getHumanName()">PresentationElement</a></code></span></div>
<div class="block">Returns human representation of the data type</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#getHumanName()">getHumanName</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>getHumanName</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.TextShapeView</code></dd>
<dt>Returns:</dt>
<dd>the name of the data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeFreeSpaceInDiagram()">
<h3>makeFreeSpaceInDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">makeFreeSpaceInDiagram</span>()</div>
</section>
</li>
<li>
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)">PresentationElement</a></code></span></div>
<div class="block">Listens for property change it can be: data was edited text box was edited</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">
<h3>internalApplyProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalApplyProperties</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">PresentationElement</a></code></span></div>
<div class="block">Applies properties from given property manager</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="TextBoxView.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a></code> in class <code><a href="TextBoxView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TextBoxView</a></code></dd>
<dt>Parameters:</dt>
<dd><code>changer</code> - new properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSmartListenerConfig(java.util.List)">
<h3>createSmartListenerConfig</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createSmartListenerConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../paths/PathConnector.html#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a></code> in class <code><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">
<h3>canChangeParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canChangeParent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether,
 @CheckForNull
 <a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent,
 boolean changeElementParent)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">PresentationElement</a></code></span></div>
<div class="block">Returns true, if element can change parent.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="TextBoxView.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">canChangeParent</a></code> in class <code><a href="TextBoxView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">TextBoxView</a></code></dd>
<dt>Parameters:</dt>
<dd><code>movedTogether</code> - collection of the elements, whose will change the parent together with this.</dd>
<dd><code>newParent</code> - new symbol parent</dd>
<dd><code>changeElementParent</code> - change element parent</dd>
<dt>Returns:</dt>
<dd>true if parent of symbol can be changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInInitialPositionOnFrame()">
<h3>isInInitialPositionOnFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInInitialPositionOnFrame</span>()</div>
<div class="block">Indicates if diagram properties shape is in the initial position and not moved by the user.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram properties shape is in initial position, false otherwise.</dd>
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
