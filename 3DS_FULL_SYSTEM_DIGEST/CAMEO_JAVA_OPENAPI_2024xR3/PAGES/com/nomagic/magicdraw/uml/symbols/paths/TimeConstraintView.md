# JAVA OPENAPI: TimeConstraintView (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/paths/TimeConstraintView.html
- source_path: `com/nomagic/magicdraw/uml/symbols/paths/TimeConstraintView.html`
- source_sha256: `4df44c6d0ed16501fe1da4f002e2887f7722e5d2df707e6e9780c8b259ffb854`
- captured_utc: `2026-07-14T16:56:01.568528+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.paths](package-summary.html)

## Class TimeConstraintView

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](PathConnector.html)
[com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement](../shapes/ShapeElement.html)
com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels
com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels
com.nomagic.magicdraw.uml.symbols.paths.TimeConstraintView

All Implemented Interfaces:
`[BaseElement](../../BaseElement.html)`, `com.nomagic.magicdraw.uml.CompartmentSupport`, `[MDElement](../../MDElement.html)`, `[ModelElementProvider](../../ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.LabelOwner`, `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`, `com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement`, `[StereotypesDisplayModeOwner](../shapes/StereotypesDisplayModeOwner.html)`, `com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApipublic classTimeConstraintView
extends com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`CONTAINER_SHAPE_INSETS, SHAPE_DISTANCE_FROM_EDGE`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.[ShapeElement](../shapes/ShapeElement.html)
`[BORDER_ELEMENT_MARGIN_ALL](../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_ALL), [BORDER_ELEMENT_MARGIN_BOTTOM](../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_BOTTOM), [BORDER_ELEMENT_MARGIN_LEFT](../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT), [BORDER_ELEMENT_MARGIN_LEFT_RIGHT](../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT_RIGHT), [BORDER_ELEMENT_MARGIN_MODES](../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_MODES), [BORDER_ELEMENT_MARGIN_NONE](../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_NONE), [BORDER_ELEMENT_MARGIN_RIGHT](../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_RIGHT), [BORDER_ELEMENT_MARGIN_TOP](../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP), [BORDER_ELEMENT_MARGIN_TOP_BOTTOM](../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP_BOTTOM), [BOTTOM_EDGE](../shapes/ShapeElement.html#BOTTOM_EDGE), [INSIDE_EDGE_POSITION](../shapes/ShapeElement.html#INSIDE_EDGE_POSITION), [LEFT_EDGE](../shapes/ShapeElement.html#LEFT_EDGE), [NEED_AUTOSIZE_FULL](../shapes/ShapeElement.html#NEED_AUTOSIZE_FULL), [NEED_AUTOSIZE_LAYOUT](../shapes/ShapeElement.html#NEED_AUTOSIZE_LAYOUT), [NEED_AUTOSIZE_NONE](../shapes/ShapeElement.html#NEED_AUTOSIZE_NONE), [NO_EDGE](../shapes/ShapeElement.html#NO_EDGE), [NULL_INSETS](../shapes/ShapeElement.html#NULL_INSETS), [ON_EDGE_POSITION](../shapes/ShapeElement.html#ON_EDGE_POSITION), [OUTSIDE_EDGE_POSITION](../shapes/ShapeElement.html#OUTSIDE_EDGE_POSITION), [RIGHT_EDGE](../shapes/ShapeElement.html#RIGHT_EDGE), [SPACE](../shapes/ShapeElement.html#SPACE), [SPACE_INSETS](../shapes/ShapeElement.html#SPACE_INSETS), [SPACE_INSETS_EMPTY_TOP_BOTTOM](../shapes/ShapeElement.html#SPACE_INSETS_EMPTY_TOP_BOTTOM), [TOP_EDGE](../shapes/ShapeElement.html#TOP_EDGE)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](PathConnector.html)
`[showsProxy](PathConnector.html#showsProxy)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DEFAULT_LINE_WIDTH](../PresentationElement.html#DEFAULT_LINE_WIDTH), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [HANDLE_SIZE](../PresentationElement.html#HANDLE_SIZE), [MAX_LINE_WIDTH](../PresentationElement.html#MAX_LINE_WIDTH), [MIN_LINE_WIDTH](../PresentationElement.html#MIN_LINE_WIDTH), [peStyle](../PresentationElement.html#peStyle), [SHADOW_WIDTH](../PresentationElement.html#SHADOW_WIDTH), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.[StereotypesDisplayModeOwner](../shapes/StereotypesDisplayModeOwner.html)
`[DSL_STEREOTYPE_DISPLAY_MODE_ALL](../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL), [DSL_STEREOTYPE_DISPLAY_MODE_LAST](../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST), [DSL_STEREOTYPE_DISPLAY_MODE_NONE](../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE), [DSL_STEREOTYPE_DISPLAY_MODES](../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES), [STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES), [STEREOTYPE_DISPLAY_MODE_ICON](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON), [STEREOTYPES_DISPLAY_MODES](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES), [STEREOTYPES_DISPLAY_MODES_SIMPLE](../shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TimeConstraintView](#%3Cinit%3E())()`

`[TimeConstraintView](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) parent)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../../Visitor.html) visitor)`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
`void`
`[adjustBounds](#adjustBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`
Validates bounds
`boolean`
`[askDeleteDataConfirmation](#askDeleteDataConfirmation())()`
Declared as interface with default implementation for subclasses.
`boolean`
`[canBeDeleted](#canBeDeleted())()`
Checks if an element can be deleted from a project.
`boolean`
`[canChangeParent](#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [PresentationElement](../PresentationElement.html)> movedTogether,
 [BaseElement](../../BaseElement.html) newParent,
 boolean changeElementParent)`
Returns true, if element can change parent.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[constructNameText](#constructNameText())()`

`protected void`
`[createLabels](#createLabels())()`

`protected com.nomagic.magicdraw.uml.symbols.shapes.NameLabelWrapper`
`[createNameLabelWrapper](#createNameLabelWrapper())()`

`protected void`
`[createSmartListenerConfig](#createSmartListenerConfig(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)`

`protected com.nomagic.magicdraw.uml.symbols.shapes.StereotypeLabelWrapper`
`[createStereotypeLabelWrapper](#createStereotypeLabelWrapper())()`

`com.dassault_systemes.modeler.foundation.model.ModelElement`
`[findOwnerForElement](#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext))([PresentationElement](../PresentationElement.html) newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)`

`protected [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[getDefaultDimension](#getDefaultDimension())()`

`[TimeConstraint](../../../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html)`
`[getElement](#getElement())()`
Returns model element of this presentation element.
`boolean`
`[hasSharedModelElement](#hasSharedModelElement())()`
Returns true if `ModelElement` of this symbol can represented with other symbol.
`protected void`
`[internalPostUpdatePresentationElement](#internalPostUpdatePresentationElement())()`
Subclasses may override this method and do some actions after specific update and resizing are executed.
`protected void`
`[internalPreSpecificUpdate](#internalPreSpecificUpdate())()`
Subclasses may override this method and do some actions before specific update is called.
`protected boolean`
`[isSnapToGrid](#isSnapToGrid())()`

`protected void`
`[labelBoundsChanged](#labelBoundsChanged())()`
Adjust time constraint bounds according to the label position changes
`protected void`
`[minimumSizeIgnoringOrientation](#minimumSizeIgnoringOrientation(java.awt.Dimension))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) min)`

`void`
`[paintSelf](#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels
`clone, createConstraintLabelWrapper, createElementPropertiesLabelWrapper, createTaggedValueLabelWrapper, getConstraintLabelBox, getConstraintLabelWrapper, getConstraintTextMode, getDSLStereotypesDisplayMode, getElementNumberDisplayMode, getElementPropertiesLabelBox, getElementPropertiesLabelWrapper, getStereotypeLabelBox, getStereotypeLabelWrapper, getStereotypesDisplayMode, getTaggedValueLabelBox, getTaggedValueLabelWrapper, internalApplyProperties, internalSilentApply, isShowConstraints, isShowElementProperties, isShowNumberTagName, isShowTaggedValues, setConstraintTextMode, setDSLStereotypesDisplayMode, setShowConstraints, setShowElementProperties, setShowTaggedValues, setStereotypesDisplayMode, sSetConstraintTextMode, sSetDSLStereotypesDisplayMode, sSetElementNumberDisplayMode, sSetShowConstraints, sSetShowElementProperties, sSetShowNumberTagName, sSetShowTaggedValues, sSetStereotypesDisplayMode, updateAfterLoad, updateNameBox`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels
`addLabel, asPresentationElement, canAddInstance, canBeAutosized, createCompartmentElements, edgeChanged, editName, getBoundsToRepaint, getCollections, getHeaderBoundsForPreferredBounds, getLabelHandler, getName, getNameLabelBox, getNameLabelWrapper, internalAppendChildRect, isLabelWrapText, isShowName, isShowText, isWordWrap, removeLabel, setCollections, setName, setNameResizeLabel, setShowName, setSuspendLabelAutoDisplayMode, setSuspendShapeAutoResizeMode, setTextEditable, setVisibleElements, setWordWrap, simpleSetBounds, sSetElement, sSetName, sSetShowName, sSetSuspendLabelAutoDisplayMode, sSetWordWrap`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
`addExtraChildrenPrefSizePadding, adjustBoundsBeforeChange, autosize, autosizeAndResizeParent, calculateMinY, calculateOvalShapePreferredSize, correctChildrenVector, coversPoint, createBoundsShape, createStateForUpdateOperation, doInternalLayoutChildren, getAdditionalHeaderHeightForPreferredBounds, getChildrenBoundsForPreferredBounds, getHeaderDistanceFromTopForOvalShape, getHeaderInsets, getHeaderMaxYForShrinkableShape, getHeaderObject, getHeaderVerticalPosition, getHeaderVerticalPositionForLayout, getNameLabel, getOvalShapeAvailableWidth, getPreferredBounds, getPresentationElementAt, getProxyPresentationElementsStream, getStereotypesToDisplay, internalGetHeaderBoundsForPreferredBounds, internalGetHeaderInsets, internalLayoutChildren, internalPostSpecificUpdate, internalSpecificUpdate, internalUpdatePresentationElement, invalidate, isBorderVisible, isChildLayoutable, isContentHidden, isHeaderOrientationVertical, isOvalShape, isParentShowsProxy, minimumDimension, minimumDimensionForShrinking, minimumSizeForShrinkingIgnoringOrientation, paintChildren, preferredDimension, preferredSizeIgnoringOrientation, setHeaderObject, setHeaderVerticalPosition, sSetAutosize, sSetHeaderVerticalPosition, switchWidthHeightIfVerticalOrientation`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`addPresentationElement, addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, canAddChild, canMoveChildOutside, checkShowsProxy, childrenBoundsForReshape, clearShowsProxy, constructLayoutHelper, getChildrenBounds, getChildrenInsets, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getRemovableChildren, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildrenBackground, prefDimensionByManipulatedChildren, recursiveAutosize, removePresentationElement, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.[ShapeElement](../shapes/ShapeElement.html)
`[addBreakPoints](../shapes/ShapeElement.html#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [adjustOnEdge](../shapes/ShapeElement.html#adjustOnEdge()), [adjustOnEdge](../shapes/ShapeElement.html#adjustOnEdge(java.awt.Rectangle,int,int,int)), [adjustOnEdgeChildren](../shapes/ShapeElement.html#adjustOnEdgeChildren()), [autosize](../shapes/ShapeElement.html#autosize()), [calculateAdjustOnEdgeLocation](../shapes/ShapeElement.html#calculateAdjustOnEdgeLocation(java.awt.Rectangle)), [calculateAndGetMinimumShrinkingDimension](../shapes/ShapeElement.html#calculateAndGetMinimumShrinkingDimension(int,int)), [calculateAndGetPreferredDimension](../shapes/ShapeElement.html#calculateAndGetPreferredDimension()), [calculateEdge](../shapes/ShapeElement.html#calculateEdge()), [calculateMinimumDimension](../shapes/ShapeElement.html#calculateMinimumDimension()), [calculateOnEdgeBounds](../shapes/ShapeElement.html#calculateOnEdgeBounds()), [calculatePreferredDimension](../shapes/ShapeElement.html#calculatePreferredDimension()), [calculatePreferredDimension](../shapes/ShapeElement.html#calculatePreferredDimension(int,int)), [canHavePaths](../shapes/ShapeElement.html#canHavePaths()), [clearOldRect](../shapes/ShapeElement.html#clearOldRect()), [ensureDimension](../shapes/ShapeElement.html#ensureDimension(boolean)), [ensurePreferredDimensionIfShrinkable](../shapes/ShapeElement.html#ensurePreferredDimensionIfShrinkable()), [ensurePreferredDimensionIfShrinkable](../shapes/ShapeElement.html#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)), [findFreePlaceForShapeOnBorder](../shapes/ShapeElement.html#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)), [getBorderElementMargin](../shapes/ShapeElement.html#getBorderElementMargin()), [getBounds](../shapes/ShapeElement.html#getBounds()), [getCenterlineableInnerParts](../shapes/ShapeElement.html#getCenterlineableInnerParts(int)), [getDimensionForShrinking](../shapes/ShapeElement.html#getDimensionForShrinking(int,int)), [getEdgeLine](../shapes/ShapeElement.html#getEdgeLine(int)), [getFixedConnectionPoints](../shapes/ShapeElement.html#getFixedConnectionPoints()), [getHeaderInsetReduce](../shapes/ShapeElement.html#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)), [getInsetsForOnEdgeShapes](../shapes/ShapeElement.html#getInsetsForOnEdgeShapes()), [getIntersection](../shapes/ShapeElement.html#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getIntersection](../shapes/ShapeElement.html#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)), [getIntersection](../shapes/ShapeElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getLoadedDimension](../shapes/ShapeElement.html#getLoadedDimension()), [getMiddlePoint](../shapes/ShapeElement.html#getMiddlePoint()), [getMiddlePoint](../shapes/ShapeElement.html#getMiddlePoint(java.awt.Point)), [getMiddlePointX](../shapes/ShapeElement.html#getMiddlePointX()), [getMiddlePointX](../shapes/ShapeElement.html#getMiddlePointX(java.awt.Point)), [getMiddlePointY](../shapes/ShapeElement.html#getMiddlePointY()), [getMiddlePointY](../shapes/ShapeElement.html#getMiddlePointY(java.awt.Point)), [getMinimumDimension](../shapes/ShapeElement.html#getMinimumDimension()), [getNearestEdge](../shapes/ShapeElement.html#getNearestEdge(int,int)), [getNearestEdge](../shapes/ShapeElement.html#getNearestEdge(java.awt.Rectangle)), [getNeedAutosizeFlag](../shapes/ShapeElement.html#getNeedAutosizeFlag()), [getNotCopyBounds](../shapes/ShapeElement.html#getNotCopyBounds()), [getOnEdge](../shapes/ShapeElement.html#getOnEdge()), [getOnEdgeCornerDistance](../shapes/ShapeElement.html#getOnEdgeCornerDistance()), [getOnEdgePosition](../shapes/ShapeElement.html#getOnEdgePosition()), [getPreferredDimension](../shapes/ShapeElement.html#getPreferredDimension()), [getPreferredDimensionForAutosize](../shapes/ShapeElement.html#getPreferredDimensionForAutosize()), [getReshapeMode](../shapes/ShapeElement.html#getReshapeMode()), [getSizeForDrawing](../shapes/ShapeElement.html#getSizeForDrawing()), [getSuspendShapeAutoResizeMode](../shapes/ShapeElement.html#getSuspendShapeAutoResizeMode()), [hasManipulator](../shapes/ShapeElement.html#hasManipulator()), [initialize](../shapes/ShapeElement.html#initialize()), [internalGetBoundsShape](../shapes/ShapeElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [intersects](../shapes/ShapeElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [isAutosized](../shapes/ShapeElement.html#isAutosized()), [isCenterlineInner](../shapes/ShapeElement.html#isCenterlineInner()), [isHorizontalCenterlineProvider](../shapes/ShapeElement.html#isHorizontalCenterlineProvider()), [isOnEdge](../shapes/ShapeElement.html#isOnEdge()), [isShapeOnEdge](../shapes/ShapeElement.html#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isShrinkable](../shapes/ShapeElement.html#isShrinkable()), [isSnapShapesOnBorderToGrid](../shapes/ShapeElement.html#isSnapShapesOnBorderToGrid()), [isUseFixedConnectionPoints](../shapes/ShapeElement.html#isUseFixedConnectionPoints()), [isVerticalCenterlineProvider](../shapes/ShapeElement.html#isVerticalCenterlineProvider()), [layoutChildren](../shapes/ShapeElement.html#layoutChildren()), [maximumDimension](../shapes/ShapeElement.html#maximumDimension(java.awt.Dimension)), [minimumOrMinimumShrinkableDimension](../shapes/ShapeElement.html#minimumOrMinimumShrinkableDimension(java.awt.Dimension)), [moveLinksToSelf](../shapes/ShapeElement.html#moveLinksToSelf()), [movePathElement](../shapes/ShapeElement.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)), [movePathElements](../shapes/ShapeElement.html#movePathElements()), [needAdjustToMaximumDimension](../shapes/ShapeElement.html#needAdjustToMaximumDimension()), [onChildEdgeChange](../shapes/ShapeElement.html#onChildEdgeChange(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)), [prepareForShadowDrawing](../shapes/ShapeElement.html#prepareForShadowDrawing(java.awt.Graphics2D)), [providesHorizontalCenterline](../shapes/ShapeElement.html#providesHorizontalCenterline()), [providesVerticalCenterline](../shapes/ShapeElement.html#providesVerticalCenterline()), [resetCalculatePreferredRegardingChildren](../shapes/ShapeElement.html#resetCalculatePreferredRegardingChildren()), [setAutosize](../shapes/ShapeElement.html#setAutosize(boolean)), [setBorderElementMargin](../shapes/ShapeElement.html#setBorderElementMargin(java.lang.String)), [setCalculatePreferredRegardingChildren](../shapes/ShapeElement.html#setCalculatePreferredRegardingChildren(boolean)), [setLoadedDimension](../shapes/ShapeElement.html#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)), [setMinimumDimension](../shapes/ShapeElement.html#setMinimumDimension(int,int)), [setNeedAutosizeFlag](../shapes/ShapeElement.html#setNeedAutosizeFlag(byte)), [setOldRect](../shapes/ShapeElement.html#setOldRect(java.awt.Rectangle)), [setOnEdge](../shapes/ShapeElement.html#setOnEdge(int)), [setPreferredDimension](../shapes/ShapeElement.html#setPreferredDimension(int,int)), [setReshapeMode](../shapes/ShapeElement.html#setReshapeMode(com.nomagic.magicdraw.uml.symbols.ReshapeMode)), [setSnapShapesOnBorderToGrid](../shapes/ShapeElement.html#setSnapShapesOnBorderToGrid(boolean)), [setUseFixedConnectionPoints](../shapes/ShapeElement.html#setUseFixedConnectionPoints(boolean)), [shouldDrawShadow](../shapes/ShapeElement.html#shouldDrawShadow()), [simpleSetBounds](../shapes/ShapeElement.html#simpleSetBounds(int,int,int,int,boolean)), [simpleSetBounds](../shapes/ShapeElement.html#simpleSetBounds(java.awt.Rectangle)), [snapsToCenterlines](../shapes/ShapeElement.html#snapsToCenterlines()), [sSetBorderElementMargin](../shapes/ShapeElement.html#sSetBorderElementMargin(java.lang.String)), [sSetBounds](../shapes/ShapeElement.html#sSetBounds(java.awt.Rectangle)), [sSetSuspendShapeAutoResizeMode](../shapes/ShapeElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)), [sSetVisibility](../shapes/ShapeElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [toString](../shapes/ShapeElement.html#toString()), [updateLater](../shapes/ShapeElement.html#updateLater())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](PathConnector.html)
`[addConnectedPathElement](PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [dispose](PathConnector.html#dispose()), [disposeConnectedPaths](PathConnector.html#disposeConnectedPaths()), [findSymbolForEnd](PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)), [findSymbolForEnd](PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)), [getConnectedPathElement](PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [getConnectedPathElementCount](PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](PathConnector.html#getConnectedPathElements(boolean,boolean)), [getPreferredArrowLength](PathConnector.html#getPreferredArrowLength()), [isShowsProxy](PathConnector.html#isShowsProxy()), [movePathElement](PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)), [removeConnectedPathElement](PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sAddConnectedPathElement](PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [selectPathsForMoving](PathConnector.html#selectPathsForMoving(java.util.List)), [setParent](PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [setVisibility](PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [sRemoveConnectedPathElement](PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sSetConnectedPathElements](PathConnector.html#sSetConnectedPathElements(java.util.List)), [supportsVisibleConnectedPathElementsIfSelfInvisible](PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[addPresentationElement](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addProperty](../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [adjustChildBounds](../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [alwaysShowTooltip](../PresentationElement.html#alwaysShowTooltip()), [applyProperties](../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [atInsert](../PresentationElement.html#atInsert()), [atInsertChildren](../PresentationElement.html#atInsertChildren()), [autosizeAndResizeManipulatedParent](../PresentationElement.html#autosizeAndResizeManipulatedParent()), [beforeDelete](../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)), [boundsChanged](../PresentationElement.html#boundsChanged()), [boundsChanged](../PresentationElement.html#boundsChanged(java.awt.Rectangle)), [canAddChild](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)), [canAddInstance](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDisposedOnUpdate](../PresentationElement.html#canBeDisposedOnUpdate()), [canChangeElementOwner](../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canFill](../PresentationElement.html#canFill()), [changeProperties](../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [checkElementOwnerOnChange](../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [checkProxyVisibility](../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [childrenForMoving](../PresentationElement.html#childrenForMoving()), [collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)), [collectSubShowingPresentationElements](../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)), [coversPoint](../PresentationElement.html#coversPoint(int,int)), [createFillStrategy](../PresentationElement.html#createFillStrategy()), [createPresentationElementStyle](../PresentationElement.html#createPresentationElementStyle()), [createPropertyChangeListener](../PresentationElement.html#createPropertyChangeListener()), [disposeChildren](../PresentationElement.html#disposeChildren()), [disposePropertyChangeListener](../PresentationElement.html#disposePropertyChangeListener()), [draw](../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawBackground](../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbol](../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbolBackground](../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [dynamicFillColor](../PresentationElement.html#dynamicFillColor()), [dynamicLineColor](../PresentationElement.html#dynamicLineColor()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth(int)), [dynamicPaintShadow](../PresentationElement.html#dynamicPaintShadow()), [dynamicStroke](../PresentationElement.html#dynamicStroke()), [dynamicStroke](../PresentationElement.html#dynamicStroke(int)), [dynamicStroke](../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)), [dynamicStyleFillColor](../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)), [dynamicStyleLineColor](../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)), [dynamicStyleTextColor](../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency()), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)), [dynamicStyleValue](../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)), [dynamicTextAlignment](../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)), [dynamicTextColor](../PresentationElement.html#dynamicTextColor()), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [findOwnerForChildElement](../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [findPresentationElement](../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)), [firePropertyChange](../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateID](../PresentationElement.html#generateID()), [getAbstractDiagramPresentationElement](../PresentationElement.html#getAbstractDiagramPresentationElement()), [getActualElement](../PresentationElement.html#getActualElement()), [getAdditionalRenderersToNotifyOnPropertiesChange](../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()), [getAssignableModelElementsClasses](../PresentationElement.html#getAssignableModelElementsClasses()), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getBoundsWithChildrenOnEdge](../PresentationElement.html#getBoundsWithChildrenOnEdge()), [getCenterlinePoint](../PresentationElement.html#getCenterlinePoint()), [getCenterlinePointX](../PresentationElement.html#getCenterlinePointX()), [getCenterlinePointY](../PresentationElement.html#getCenterlinePointY()), [getChildPresentationElementForContextMenu](../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)), [getChildrenWithSymbolProperties](../PresentationElement.html#getChildrenWithSymbolProperties()), [getConfiguration](../PresentationElement.html#getConfiguration()), [getDiagramPresentationElement](../PresentationElement.html#getDiagramPresentationElement()), [getDiagramSurface](../PresentationElement.html#getDiagramSurface()), [getDrawComparator](../PresentationElement.html#getDrawComparator()), [getDynamicConfigurations](../PresentationElement.html#getDynamicConfigurations()), [getDynamicStyleOwner](../PresentationElement.html#getDynamicStyleOwner()), [getEffectiveStyleDelegate](../PresentationElement.html#getEffectiveStyleDelegate()), [getEffectiveStyleOwner](../PresentationElement.html#getEffectiveStyleOwner()), [getElementsForRelationshipConnecting](../PresentationElement.html#getElementsForRelationshipConnecting()), [getElementToConnectRelationship](../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFillColor](../PresentationElement.html#getFillColor()), [getFont](../PresentationElement.html#getFont()), [getFontHeight](../PresentationElement.html#getFontHeight()), [getFontRenderContext](../PresentationElement.html#getFontRenderContext()), [getHumanName](../PresentationElement.html#getHumanName()), [getHumanType](../PresentationElement.html#getHumanType()), [getLineColor](../PresentationElement.html#getLineColor()), [getLineWidth](../PresentationElement.html#getLineWidth()), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point)), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getManipulationBounds](../PresentationElement.html#getManipulationBounds(java.awt.Point)), [getModelElement](../PresentationElement.html#getModelElement()), [getModelElementsForRelationshipConnecting](../PresentationElement.html#getModelElementsForRelationshipConnecting()), [getModelElementToConnectRelationship](../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [getModelElementToMove](../PresentationElement.html#getModelElementToMove()), [getNotZoomedTolerance](../PresentationElement.html#getNotZoomedTolerance()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getOwnStyleDelegate](../PresentationElement.html#getOwnStyleDelegate()), [getParent](../PresentationElement.html#getParent()), [getParentSymbolStyleOwner](../PresentationElement.html#getParentSymbolStyleOwner()), [getPreferredSize](../PresentationElement.html#getPreferredSize()), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(int)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementCount](../PresentationElement.html#getPresentationElementCount()), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getProjectImpl](../PresentationElement.html#getProjectImpl()), [getProperty](../PresentationElement.html#getProperty(java.lang.String)), [getPropertyManager](../PresentationElement.html#getPropertyManager()), [getPropertyManagerName](../PresentationElement.html#getPropertyManagerName()), [getRenderer](../PresentationElement.html#getRenderer()), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [getStyle](../PresentationElement.html#getStyle()), [getSymbolRenderer](../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getTextColor](../PresentationElement.html#getTextColor()), [getTolerance](../PresentationElement.html#getTolerance()), [getVisibility](../PresentationElement.html#getVisibility()), [getVisiblePresentationElements](../PresentationElement.html#getVisiblePresentationElements()), [handleModelDelete](../PresentationElement.html#handleModelDelete()), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [initializeAndAutosize](../PresentationElement.html#initializeAndAutosize()), [internalBeforeUpdate](../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)), [internalCreatePropertyChangeListener](../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [internalGetModelElementToConnectRelationship](../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [internalGetPresentationElementStroke](../PresentationElement.html#internalGetPresentationElementStroke(int)), [internalGetSpecificFont](../PresentationElement.html#internalGetSpecificFont()), [internalGetSpecificTextColor](../PresentationElement.html#internalGetSpecificTextColor()), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(float)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)), [intersects](../PresentationElement.html#intersects(int,int,int,int)), [isChildVisible](../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isCreateElementListener](../PresentationElement.html#isCreateElementListener()), [isDetectable](../PresentationElement.html#isDetectable()), [isDisposed](../PresentationElement.html#isDisposed()), [isLayouting](../PresentationElement.html#isLayouting()), [isMovableByMoveManager](../PresentationElement.html#isMovableByMoveManager()), [isNotNull](../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isPreserveProportionsWhenGrowing](../PresentationElement.html#isPreserveProportionsWhenGrowing()), [isSelected](../PresentationElement.html#isSelected()), [isShowElementTypeAsLabel](../PresentationElement.html#isShowElementTypeAsLabel()), [isSortable](../PresentationElement.html#isSortable()), [isSuitableToConnectRelationship](../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [isTextEditable](../PresentationElement.html#isTextEditable()), [isUseFillColor](../PresentationElement.html#isUseFillColor()), [isUseFillColorByProperty](../PresentationElement.html#isUseFillColorByProperty()), [isUseGradientForFill](../PresentationElement.html#isUseGradientForFill()), [isVisible](../PresentationElement.html#isVisible()), [isVisibleInDiagram](../PresentationElement.html#isVisibleInDiagram()), [isVisibleOrShrunken](../PresentationElement.html#isVisibleOrShrunken()), [movePathElementsRecursively](../PresentationElement.html#movePathElementsRecursively()), [mustShowContextMenu](../PresentationElement.html#mustShowContextMenu()), [notifyCreated](../PresentationElement.html#notifyCreated()), [notifyDiagramFrameSizeChange](../PresentationElement.html#notifyDiagramFrameSizeChange()), [notifyRepaintManager](../PresentationElement.html#notifyRepaintManager(boolean)), [onChildAdd](../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onChildRemove](../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onDiagramSurfaceSet](../PresentationElement.html#onDiagramSurfaceSet()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [onFontChange](../PresentationElement.html#onFontChange()), [onParentChange](../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [paintAdornments](../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintAdornmentsBackground](../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenAndAdornments](../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelfBackground](../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [preDisposeOnUpdate](../PresentationElement.html#preDisposeOnUpdate()), [prepareForLineDrawing](../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)), [prepareForTextDrawing](../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)), [propertyChange](../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)), [recreateListeners](../PresentationElement.html#recreateListeners()), [registerInSortManager](../PresentationElement.html#registerInSortManager()), [rememberBounds](../PresentationElement.html#rememberBounds()), [rememberBounds](../PresentationElement.html#rememberBounds(java.awt.Rectangle)), [removeFromSortManager](../PresentationElement.html#removeFromSortManager()), [removeItSelfOnUpdate](../PresentationElement.html#removeItSelfOnUpdate()), [resizeParent](../PresentationElement.html#resizeParent()), [sAddPresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [selectChildrenForMoving](../PresentationElement.html#selectChildrenForMoving()), [selectObjectsForMoving](../PresentationElement.html#selectObjectsForMoving()), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setBounds](../PresentationElement.html#setBounds(int,int,int,int)), [setCreateElementListener](../PresentationElement.html#setCreateElementListener(boolean)), [setElement](../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setFont](../PresentationElement.html#setFont(java.awt.Font)), [setLayouting](../PresentationElement.html#setLayouting(boolean)), [setLineColor](../PresentationElement.html#setLineColor(java.awt.Color)), [setLineWidth](../PresentationElement.html#setLineWidth(int)), [setLoadedVisibility](../PresentationElement.html#setLoadedVisibility(boolean)), [setLocation](../PresentationElement.html#setLocation(int,int)), [setLocation](../PresentationElement.html#setLocation(java.awt.Point)), [setModelElement](../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [setNeedRecreateListeners](../PresentationElement.html#setNeedRecreateListeners(boolean)), [setPropertyManagerName](../PresentationElement.html#setPropertyManagerName(java.lang.String)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [setSize](../PresentationElement.html#setSize(int,int)), [setSize](../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)), [setSize](../PresentationElement.html#setSize(java.awt.Dimension)), [setTextColor](../PresentationElement.html#setTextColor(java.awt.Color)), [setUseFillColor](../PresentationElement.html#setUseFillColor(boolean)), [setVisible](../PresentationElement.html#setVisible(boolean)), [silentApply](../PresentationElement.html#silentApply()), [silentApply](../PresentationElement.html#silentApply(boolean)), [simpleSetBounds](../PresentationElement.html#simpleSetBounds(int,int,int,int)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Point,float)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)), [snapViewToGrid](../PresentationElement.html#snapViewToGrid(float)), [sortObjectsByX](../PresentationElement.html#sortObjectsByX(java.util.List)), [sortObjectsByY](../PresentationElement.html#sortObjectsByY(java.util.List)), [sSetBounds](../PresentationElement.html#sSetBounds(int,int,int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(java.awt.Point)), [sSetModelElement](../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [sSetParent](../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetParentForAll](../PresentationElement.html#sSetParentForAll(java.util.Collection)), [sSetSize](../PresentationElement.html#sSetSize(int,int)), [sSetSize](../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)), [sSetSize](../PresentationElement.html#sSetSize(java.awt.Dimension)), [sSetVisible](../PresentationElement.html#sSetVisible(boolean)), [tryToDeleteModelElementUponRemoval](../PresentationElement.html#tryToDeleteModelElementUponRemoval()), [update](../PresentationElement.html#update()), [updateLabelsIgnoringSuspendableLater](../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)), [updateModelByView](../PresentationElement.html#updateModelByView()), [updateModelByViewInternal](../PresentationElement.html#updateModelByViewInternal()), [updateViewAfterPropertyChange](../PresentationElement.html#updateViewAfterPropertyChange()), [useParentProperties](../PresentationElement.html#useParentProperties()), [useParentStyle](../PresentationElement.html#useParentStyle())`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, addPropertyChangeListener, canAdd, canAddChild, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../BaseElement.html)
`[canAdd](../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape
`getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY`
Methods inherited from interface com.nomagic.magicdraw.uml.CompartmentSupport
`setVisibleElements`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.LabelOwner
`getModelElement`
Methods inherited from interface com.nomagic.magicdraw.uml.[MDElement](../../MDElement.html)
`[getProject](../../MDElement.html#getProject())`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement
`addProperty, asPresentationElement, getProperty, getPropertyManager`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TimeConstraintView
public TimeConstraintView()
TimeConstraintView
public TimeConstraintView(@CheckForNull
 [PresentationElement](../PresentationElement.html) parent)
 ============ METHOD DETAIL ========== 
Method Details
createNameLabelWrapper
protected com.nomagic.magicdraw.uml.symbols.shapes.NameLabelWrapper createNameLabelWrapper()
Overrides:
`createNameLabelWrapper` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
constructNameText
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) constructNameText()
Overrides:
`constructNameText` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
createLabels
protected void createLabels()
Overrides:
`createLabels` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
createStereotypeLabelWrapper
protected com.nomagic.magicdraw.uml.symbols.shapes.StereotypeLabelWrapper createStereotypeLabelWrapper()
Overrides:
`createStereotypeLabelWrapper` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
createSmartListenerConfig
protected void createSmartListenerConfig([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)
Overrides:
`createSmartListenerConfig` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
accept
public void accept([Visitor](../../Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
 See "Visitor" pattern for more details.
Specified by:
`[accept](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../../MDElement.html)`
Overrides:
`accept` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
findOwnerForElement
public com.dassault_systemes.modeler.foundation.model.ModelElement findOwnerForElement([PresentationElement](../PresentationElement.html) newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)
Overrides:
`[findOwnerForElement](../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext))` in class `[PresentationElement](../PresentationElement.html)`
internalPreSpecificUpdate
protected void internalPreSpecificUpdate()
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
Subclasses may override this method and do some actions before specific update is called. Implementation is empty here.
Overrides:
`internalPreSpecificUpdate` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
See Also:
`AbstractHeaderShapeView.internalUpdatePresentationElement()`
askDeleteDataConfirmation
public boolean askDeleteDataConfirmation()
Description copied from class: `[PresentationElement](../PresentationElement.html#askDeleteDataConfirmation())`
Declared as interface with default implementation for subclasses. If some subclasses upon
 delete may ask about delete data object as well, they have to redefine this method and return
 true. By default all objects are removed without asking
Overrides:
`[askDeleteDataConfirmation](../PresentationElement.html#askDeleteDataConfirmation())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
confirmation status -- true if asking is necessary, false otherwise
hasSharedModelElement
public boolean hasSharedModelElement()
Description copied from class: `[PresentationElement](../PresentationElement.html#hasSharedModelElement())`
Returns true if `ModelElement` of this symbol can represented with other symbol.
 If `ModelElement` is not shared, it can be deleted together with symbol deleting.
Overrides:
`[hasSharedModelElement](../PresentationElement.html#hasSharedModelElement())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
true if element of this symbol can be represented with other symbol.
internalPostUpdatePresentationElement
protected void internalPostUpdatePresentationElement()
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
Subclasses may override this method and do some actions after specific update and resizing are executed.
 Implementation is empty here.
Overrides:
`internalPostUpdatePresentationElement` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels`
See Also:
`AbstractHeaderShapeView.internalUpdatePresentationElement()`
getElement
public [TimeConstraint](../../../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html) getElement()
Description copied from class: `[PresentationElement](../PresentationElement.html#getElement())`
Returns model element of this presentation element. Some presentation elements (for example
 TextBoxes) do not have model elements.
Specified by:
`getElement` in interface `com.nomagic.magicdraw.uml.symbols.LabelOwner`
Specified by:
`[getElement](../../ModelElementProvider.html#getElement())` in interface `[ModelElementProvider](../../ModelElementProvider.html)`
Overrides:
`[getElement](../PresentationElement.html#getElement())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
model element of this presentation element.
minimumSizeIgnoringOrientation
protected void minimumSizeIgnoringOrientation([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) min)
Overrides:
`minimumSizeIgnoringOrientation` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
paintSelf
public void paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
Specified by:
`[paintSelf](../PresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))` in class `[PresentationElement](../PresentationElement.html)`
adjustBounds
public void adjustBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
Description copied from class: `[ShapeElement](../shapes/ShapeElement.html#adjustBounds(java.awt.Rectangle))`
Validates bounds
Overrides:
`[adjustBounds](../shapes/ShapeElement.html#adjustBounds(java.awt.Rectangle))` in class `[ShapeElement](../shapes/ShapeElement.html)`
Parameters:
`bounds` - bounds
isSnapToGrid
protected boolean isSnapToGrid()
Overrides:
`[isSnapToGrid](../shapes/ShapeElement.html#isSnapToGrid())` in class `[ShapeElement](../shapes/ShapeElement.html)`
getDefaultDimension
protected [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) getDefaultDimension()
Overrides:
`[getDefaultDimension](../shapes/ShapeElement.html#getDefaultDimension())` in class `[ShapeElement](../shapes/ShapeElement.html)`
labelBoundsChanged
protected void labelBoundsChanged()
Adjust time constraint bounds according to the label position changes
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
canChangeParent
public boolean canChangeParent([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [PresentationElement](../PresentationElement.html)> movedTogether,
 @CheckForNull
 [BaseElement](../../BaseElement.html) newParent,
 boolean changeElementParent)
Description copied from class: `[PresentationElement](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean))`
Returns true, if element can change parent.
Overrides:
`[canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`movedTogether` - collection of the elements, whose will change the parent together with this.
`newParent` - new symbol parent
`changeElementParent` - change element parent
Returns:
true if parent of symbol can be changed

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.paths</a></div>
<h1 class="title" title="Class TimeConstraintView">Class TimeConstraintView</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</a>
<div class="inheritance"><a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.paths.TimeConstraintView</div>
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
<dd><code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code>com.nomagic.magicdraw.uml.CompartmentSupport</code>, <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.LabelOwner</code>, <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code>, <code>com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</code>, <code><a href="../shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code>, <code>com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider</code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TimeConstraintView</span>
<span class="extends-implements">extends com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</span></div>
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
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></h3>
<code><a href="../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_ALL">BORDER_ELEMENT_MARGIN_ALL</a>, <a href="../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_BOTTOM">BORDER_ELEMENT_MARGIN_BOTTOM</a>, <a href="../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT">BORDER_ELEMENT_MARGIN_LEFT</a>, <a href="../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT_RIGHT">BORDER_ELEMENT_MARGIN_LEFT_RIGHT</a>, <a href="../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_MODES">BORDER_ELEMENT_MARGIN_MODES</a>, <a href="../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_NONE">BORDER_ELEMENT_MARGIN_NONE</a>, <a href="../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_RIGHT">BORDER_ELEMENT_MARGIN_RIGHT</a>, <a href="../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP">BORDER_ELEMENT_MARGIN_TOP</a>, <a href="../shapes/ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP_BOTTOM">BORDER_ELEMENT_MARGIN_TOP_BOTTOM</a>, <a href="../shapes/ShapeElement.html#BOTTOM_EDGE">BOTTOM_EDGE</a>, <a href="../shapes/ShapeElement.html#INSIDE_EDGE_POSITION">INSIDE_EDGE_POSITION</a>, <a href="../shapes/ShapeElement.html#LEFT_EDGE">LEFT_EDGE</a>, <a href="../shapes/ShapeElement.html#NEED_AUTOSIZE_FULL">NEED_AUTOSIZE_FULL</a>, <a href="../shapes/ShapeElement.html#NEED_AUTOSIZE_LAYOUT">NEED_AUTOSIZE_LAYOUT</a>, <a href="../shapes/ShapeElement.html#NEED_AUTOSIZE_NONE">NEED_AUTOSIZE_NONE</a>, <a href="../shapes/ShapeElement.html#NO_EDGE">NO_EDGE</a>, <a href="../shapes/ShapeElement.html#NULL_INSETS">NULL_INSETS</a>, <a href="../shapes/ShapeElement.html#ON_EDGE_POSITION">ON_EDGE_POSITION</a>, <a href="../shapes/ShapeElement.html#OUTSIDE_EDGE_POSITION">OUTSIDE_EDGE_POSITION</a>, <a href="../shapes/ShapeElement.html#RIGHT_EDGE">RIGHT_EDGE</a>, <a href="../shapes/ShapeElement.html#SPACE">SPACE</a>, <a href="../shapes/ShapeElement.html#SPACE_INSETS">SPACE_INSETS</a>, <a href="../shapes/ShapeElement.html#SPACE_INSETS_EMPTY_TOP_BOTTOM">SPACE_INSETS_EMPTY_TOP_BOTTOM</a>, <a href="../shapes/ShapeElement.html#TOP_EDGE">TOP_EDGE</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="PathConnector.html#showsProxy">showsProxy</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#DASHED_STROKE">DASHED_STROKE</a>, <a href="../PresentationElement.html#DEFAULT_LINE_WIDTH">DEFAULT_LINE_WIDTH</a>, <a href="../PresentationElement.html#DOTTED_STROKE">DOTTED_STROKE</a>, <a href="../PresentationElement.html#HANDLE_SIZE">HANDLE_SIZE</a>, <a href="../PresentationElement.html#MAX_LINE_WIDTH">MAX_LINE_WIDTH</a>, <a href="../PresentationElement.html#MIN_LINE_WIDTH">MIN_LINE_WIDTH</a>, <a href="../PresentationElement.html#peStyle">peStyle</a>, <a href="../PresentationElement.html#SHADOW_WIDTH">SHADOW_WIDTH</a>, <a href="../PresentationElement.html#SOLID_STROKE">SOLID_STROKE</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.StereotypesDisplayModeOwner">Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.<a href="../shapes/StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></h3>
<code><a href="../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL">DSL_STEREOTYPE_DISPLAY_MODE_ALL</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST">DSL_STEREOTYPE_DISPLAY_MODE_LAST</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE">DSL_STEREOTYPE_DISPLAY_MODE_NONE</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES">DSL_STEREOTYPE_DISPLAY_MODES</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES">STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON">STEREOTYPE_DISPLAY_MODE_ICON</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE">STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT">STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT">STEREOTYPE_DISPLAY_MODE_TEXT</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON">STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES">STEREOTYPES_DISPLAY_MODES</a>, <a href="../shapes/StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE">STEREOTYPES_DISPLAY_MODES_SIMPLE</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TimeConstraintView</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement)">TimeConstraintView</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a><wbr/>(<a href="../../Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method accepts a visitor, and calls method "visit&lt;class name&gt;(this)" of a visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustBounds(java.awt.Rectangle)">adjustBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Validates bounds</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#askDeleteDataConfirmation()">askDeleteDataConfirmation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Declared as interface with default implementation for subclasses.</div>
</div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#constructNameText()">constructNameText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLabels()">createLabels</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.uml.symbols.shapes.NameLabelWrapper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createNameLabelWrapper()">createNameLabelWrapper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.uml.symbols.shapes.StereotypeLabelWrapper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStereotypeLabelWrapper()">createStereotypeLabelWrapper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.model.ModelElement</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultDimension()">getDefaultDimension</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model element of this presentation element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasSharedModelElement()">hasSharedModelElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if <code>ModelElement</code> of this symbol can represented with other symbol.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalPostUpdatePresentationElement()">internalPostUpdatePresentationElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Subclasses may override this method and do some actions after specific update and resizing are executed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalPreSpecificUpdate()">internalPreSpecificUpdate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Subclasses may override this method and do some actions before specific update is called.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSnapToGrid()">isSnapToGrid</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#labelBoundsChanged()">labelBoundsChanged</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adjust time constraint bounds according to the label position changes</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#minimumSizeIgnoringOrientation(java.awt.Dimension)">minimumSizeIgnoringOrientation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> min)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelf</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</h3>
<code>clone, createConstraintLabelWrapper, createElementPropertiesLabelWrapper, createTaggedValueLabelWrapper, getConstraintLabelBox, getConstraintLabelWrapper, getConstraintTextMode, getDSLStereotypesDisplayMode, getElementNumberDisplayMode, getElementPropertiesLabelBox, getElementPropertiesLabelWrapper, getStereotypeLabelBox, getStereotypeLabelWrapper, getStereotypesDisplayMode, getTaggedValueLabelBox, getTaggedValueLabelWrapper, internalApplyProperties, internalSilentApply, isShowConstraints, isShowElementProperties, isShowNumberTagName, isShowTaggedValues, setConstraintTextMode, setDSLStereotypesDisplayMode, setShowConstraints, setShowElementProperties, setShowTaggedValues, setStereotypesDisplayMode, sSetConstraintTextMode, sSetDSLStereotypesDisplayMode, sSetElementNumberDisplayMode, sSetShowConstraints, sSetShowElementProperties, sSetShowNumberTagName, sSetShowTaggedValues, sSetStereotypesDisplayMode, updateAfterLoad, updateNameBox</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels</h3>
<code>addLabel, asPresentationElement, canAddInstance, canBeAutosized, createCompartmentElements, edgeChanged, editName, getBoundsToRepaint, getCollections, getHeaderBoundsForPreferredBounds, getLabelHandler, getName, getNameLabelBox, getNameLabelWrapper, internalAppendChildRect, isLabelWrapText, isShowName, isShowText, isWordWrap, removeLabel, setCollections, setName, setNameResizeLabel, setShowName, setSuspendLabelAutoDisplayMode, setSuspendShapeAutoResizeMode, setTextEditable, setVisibleElements, setWordWrap, simpleSetBounds, sSetElement, sSetName, sSetShowName, sSetSuspendLabelAutoDisplayMode, sSetWordWrap</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</h3>
<code>addExtraChildrenPrefSizePadding, adjustBoundsBeforeChange, autosize, autosizeAndResizeParent, calculateMinY, calculateOvalShapePreferredSize, correctChildrenVector, coversPoint, createBoundsShape, createStateForUpdateOperation, doInternalLayoutChildren, getAdditionalHeaderHeightForPreferredBounds, getChildrenBoundsForPreferredBounds, getHeaderDistanceFromTopForOvalShape, getHeaderInsets, getHeaderMaxYForShrinkableShape, getHeaderObject, getHeaderVerticalPosition, getHeaderVerticalPositionForLayout, getNameLabel, getOvalShapeAvailableWidth, getPreferredBounds, getPresentationElementAt, getProxyPresentationElementsStream, getStereotypesToDisplay, internalGetHeaderBoundsForPreferredBounds, internalGetHeaderInsets, internalLayoutChildren, internalPostSpecificUpdate, internalSpecificUpdate, internalUpdatePresentationElement, invalidate, isBorderVisible, isChildLayoutable, isContentHidden, isHeaderOrientationVertical, isOvalShape, isParentShowsProxy, minimumDimension, minimumDimensionForShrinking, minimumSizeForShrinkingIgnoringOrientation, paintChildren, preferredDimension, preferredSizeIgnoringOrientation, setHeaderObject, setHeaderVerticalPosition, sSetAutosize, sSetHeaderVerticalPosition, switchWidthHeightIfVerticalOrientation</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</h3>
<code>addPresentationElement, addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, canAddChild, canMoveChildOutside, checkShowsProxy, childrenBoundsForReshape, clearShowsProxy, constructLayoutHelper, getChildrenBounds, getChildrenInsets, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getRemovableChildren, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildrenBackground, prefDimensionByManipulatedChildren, recursiveAutosize, removePresentationElement, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></h3>
<code><a href="../shapes/ShapeElement.html#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addBreakPoints</a>, <a href="../shapes/ShapeElement.html#adjustOnEdge()">adjustOnEdge</a>, <a href="../shapes/ShapeElement.html#adjustOnEdge(java.awt.Rectangle,int,int,int)">adjustOnEdge</a>, <a href="../shapes/ShapeElement.html#adjustOnEdgeChildren()">adjustOnEdgeChildren</a>, <a href="../shapes/ShapeElement.html#autosize()">autosize</a>, <a href="../shapes/ShapeElement.html#calculateAdjustOnEdgeLocation(java.awt.Rectangle)">calculateAdjustOnEdgeLocation</a>, <a href="../shapes/ShapeElement.html#calculateAndGetMinimumShrinkingDimension(int,int)">calculateAndGetMinimumShrinkingDimension</a>, <a href="../shapes/ShapeElement.html#calculateAndGetPreferredDimension()">calculateAndGetPreferredDimension</a>, <a href="../shapes/ShapeElement.html#calculateEdge()">calculateEdge</a>, <a href="../shapes/ShapeElement.html#calculateMinimumDimension()">calculateMinimumDimension</a>, <a href="../shapes/ShapeElement.html#calculateOnEdgeBounds()">calculateOnEdgeBounds</a>, <a href="../shapes/ShapeElement.html#calculatePreferredDimension()">calculatePreferredDimension</a>, <a href="../shapes/ShapeElement.html#calculatePreferredDimension(int,int)">calculatePreferredDimension</a>, <a href="../shapes/ShapeElement.html#canHavePaths()">canHavePaths</a>, <a href="../shapes/ShapeElement.html#clearOldRect()">clearOldRect</a>, <a href="../shapes/ShapeElement.html#ensureDimension(boolean)">ensureDimension</a>, <a href="../shapes/ShapeElement.html#ensurePreferredDimensionIfShrinkable()">ensurePreferredDimensionIfShrinkable</a>, <a href="../shapes/ShapeElement.html#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)">ensurePreferredDimensionIfShrinkable</a>, <a href="../shapes/ShapeElement.html#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)">findFreePlaceForShapeOnBorder</a>, <a href="../shapes/ShapeElement.html#getBorderElementMargin()">getBorderElementMargin</a>, <a href="../shapes/ShapeElement.html#getBounds()">getBounds</a>, <a href="../shapes/ShapeElement.html#getCenterlineableInnerParts(int)">getCenterlineableInnerParts</a>, <a href="../shapes/ShapeElement.html#getDimensionForShrinking(int,int)">getDimensionForShrinking</a>, <a href="../shapes/ShapeElement.html#getEdgeLine(int)">getEdgeLine</a>, <a href="../shapes/ShapeElement.html#getFixedConnectionPoints()">getFixedConnectionPoints</a>, <a href="../shapes/ShapeElement.html#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)">getHeaderInsetReduce</a>, <a href="../shapes/ShapeElement.html#getInsetsForOnEdgeShapes()">getInsetsForOnEdgeShapes</a>, <a href="../shapes/ShapeElement.html#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="../shapes/ShapeElement.html#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)">getIntersection</a>, <a href="../shapes/ShapeElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="../shapes/ShapeElement.html#getLoadedDimension()">getLoadedDimension</a>, <a href="../shapes/ShapeElement.html#getMiddlePoint()">getMiddlePoint</a>, <a href="../shapes/ShapeElement.html#getMiddlePoint(java.awt.Point)">getMiddlePoint</a>, <a href="../shapes/ShapeElement.html#getMiddlePointX()">getMiddlePointX</a>, <a href="../shapes/ShapeElement.html#getMiddlePointX(java.awt.Point)">getMiddlePointX</a>, <a href="../shapes/ShapeElement.html#getMiddlePointY()">getMiddlePointY</a>, <a href="../shapes/ShapeElement.html#getMiddlePointY(java.awt.Point)">getMiddlePointY</a>, <a href="../shapes/ShapeElement.html#getMinimumDimension()">getMinimumDimension</a>, <a href="../shapes/ShapeElement.html#getNearestEdge(int,int)">getNearestEdge</a>, <a href="../shapes/ShapeElement.html#getNearestEdge(java.awt.Rectangle)">getNearestEdge</a>, <a href="../shapes/ShapeElement.html#getNeedAutosizeFlag()">getNeedAutosizeFlag</a>, <a href="../shapes/ShapeElement.html#getNotCopyBounds()">getNotCopyBounds</a>, <a href="../shapes/ShapeElement.html#getOnEdge()">getOnEdge</a>, <a href="../shapes/ShapeElement.html#getOnEdgeCornerDistance()">getOnEdgeCornerDistance</a>, <a href="../shapes/ShapeElement.html#getOnEdgePosition()">getOnEdgePosition</a>, <a href="../shapes/ShapeElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="../shapes/ShapeElement.html#getPreferredDimensionForAutosize()">getPreferredDimensionForAutosize</a>, <a href="../shapes/ShapeElement.html#getReshapeMode()">getReshapeMode</a>, <a href="../shapes/ShapeElement.html#getSizeForDrawing()">getSizeForDrawing</a>, <a href="../shapes/ShapeElement.html#getSuspendShapeAutoResizeMode()">getSuspendShapeAutoResizeMode</a>, <a href="../shapes/ShapeElement.html#hasManipulator()">hasManipulator</a>, <a href="../shapes/ShapeElement.html#initialize()">initialize</a>, <a href="../shapes/ShapeElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a>, <a href="../shapes/ShapeElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a>, <a href="../shapes/ShapeElement.html#isAutosized()">isAutosized</a>, <a href="../shapes/ShapeElement.html#isCenterlineInner()">isCenterlineInner</a>, <a href="../shapes/ShapeElement.html#isHorizontalCenterlineProvider()">isHorizontalCenterlineProvider</a>, <a href="../shapes/ShapeElement.html#isOnEdge()">isOnEdge</a>, <a href="../shapes/ShapeElement.html#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isShapeOnEdge</a>, <a href="../shapes/ShapeElement.html#isShrinkable()">isShrinkable</a>, <a href="../shapes/ShapeElement.html#isSnapShapesOnBorderToGrid()">isSnapShapesOnBorderToGrid</a>, <a href="../shapes/ShapeElement.html#isUseFixedConnectionPoints()">isUseFixedConnectionPoints</a>, <a href="../shapes/ShapeElement.html#isVerticalCenterlineProvider()">isVerticalCenterlineProvider</a>, <a href="../shapes/ShapeElement.html#layoutChildren()">layoutChildren</a>, <a href="../shapes/ShapeElement.html#maximumDimension(java.awt.Dimension)">maximumDimension</a>, <a href="../shapes/ShapeElement.html#minimumOrMinimumShrinkableDimension(java.awt.Dimension)">minimumOrMinimumShrinkableDimension</a>, <a href="../shapes/ShapeElement.html#moveLinksToSelf()">moveLinksToSelf</a>, <a href="../shapes/ShapeElement.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a>, <a href="../shapes/ShapeElement.html#movePathElements()">movePathElements</a>, <a href="../shapes/ShapeElement.html#needAdjustToMaximumDimension()">needAdjustToMaximumDimension</a>, <a href="../shapes/ShapeElement.html#onChildEdgeChange(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">onChildEdgeChange</a>, <a href="../shapes/ShapeElement.html#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a>, <a href="../shapes/ShapeElement.html#providesHorizontalCenterline()">providesHorizontalCenterline</a>, <a href="../shapes/ShapeElement.html#providesVerticalCenterline()">providesVerticalCenterline</a>, <a href="../shapes/ShapeElement.html#resetCalculatePreferredRegardingChildren()">resetCalculatePreferredRegardingChildren</a>, <a href="../shapes/ShapeElement.html#setAutosize(boolean)">setAutosize</a>, <a href="../shapes/ShapeElement.html#setBorderElementMargin(java.lang.String)">setBorderElementMargin</a>, <a href="../shapes/ShapeElement.html#setCalculatePreferredRegardingChildren(boolean)">setCalculatePreferredRegardingChildren</a>, <a href="../shapes/ShapeElement.html#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)">setLoadedDimension</a>, <a href="../shapes/ShapeElement.html#setMinimumDimension(int,int)">setMinimumDimension</a>, <a href="../shapes/ShapeElement.html#setNeedAutosizeFlag(byte)">setNeedAutosizeFlag</a>, <a href="../shapes/ShapeElement.html#setOldRect(java.awt.Rectangle)">setOldRect</a>, <a href="../shapes/ShapeElement.html#setOnEdge(int)">setOnEdge</a>, <a href="../shapes/ShapeElement.html#setPreferredDimension(int,int)">setPreferredDimension</a>, <a href="../shapes/ShapeElement.html#setReshapeMode(com.nomagic.magicdraw.uml.symbols.ReshapeMode)">setReshapeMode</a>, <a href="../shapes/ShapeElement.html#setSnapShapesOnBorderToGrid(boolean)">setSnapShapesOnBorderToGrid</a>, <a href="../shapes/ShapeElement.html#setUseFixedConnectionPoints(boolean)">setUseFixedConnectionPoints</a>, <a href="../shapes/ShapeElement.html#shouldDrawShadow()">shouldDrawShadow</a>, <a href="../shapes/ShapeElement.html#simpleSetBounds(int,int,int,int,boolean)">simpleSetBounds</a>, <a href="../shapes/ShapeElement.html#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a>, <a href="../shapes/ShapeElement.html#snapsToCenterlines()">snapsToCenterlines</a>, <a href="../shapes/ShapeElement.html#sSetBorderElementMargin(java.lang.String)">sSetBorderElementMargin</a>, <a href="../shapes/ShapeElement.html#sSetBounds(java.awt.Rectangle)">sSetBounds</a>, <a href="../shapes/ShapeElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)">sSetSuspendShapeAutoResizeMode</a>, <a href="../shapes/ShapeElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a>, <a href="../shapes/ShapeElement.html#toString()">toString</a>, <a href="../shapes/ShapeElement.html#updateLater()">updateLater</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addConnectedPathElement</a>, <a href="PathConnector.html#dispose()">dispose</a>, <a href="PathConnector.html#disposeConnectedPaths()">disposeConnectedPaths</a>, <a href="PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">findSymbolForEnd</a>, <a href="PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)">findSymbolForEnd</a>, <a href="PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">getConnectedPathElement</a>, <a href="PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a>, <a href="PathConnector.html#getPreferredArrowLength()">getPreferredArrowLength</a>, <a href="PathConnector.html#isShowsProxy()">isShowsProxy</a>, <a href="PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)">movePathElement</a>, <a href="PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">removeConnectedPathElement</a>, <a href="PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sAddConnectedPathElement</a>, <a href="PathConnector.html#selectPathsForMoving(java.util.List)">selectPathsForMoving</a>, <a href="PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a>, <a href="PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a>, <a href="PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sRemoveConnectedPathElement</a>, <a href="PathConnector.html#sSetConnectedPathElements(java.util.List)">sSetConnectedPathElements</a>, <a href="PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible()">supportsVisibleConnectedPathElementsIfSelfInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a>, <a href="../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBounds</a>, <a href="../PresentationElement.html#alwaysShowTooltip()">alwaysShowTooltip</a>, <a href="../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">applyProperties</a>, <a href="../PresentationElement.html#atInsert()">atInsert</a>, <a href="../PresentationElement.html#atInsertChildren()">atInsertChildren</a>, <a href="../PresentationElement.html#autosizeAndResizeManipulatedParent()">autosizeAndResizeManipulatedParent</a>, <a href="../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">beforeDelete</a>, <a href="../PresentationElement.html#boundsChanged()">boundsChanged</a>, <a href="../PresentationElement.html#boundsChanged(java.awt.Rectangle)">boundsChanged</a>, <a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../PresentationElement.html#canBeDisposedOnUpdate()">canBeDisposedOnUpdate</a>, <a href="../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeElementOwner</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../PresentationElement.html#canFill()">canFill</a>, <a href="../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">changeProperties</a>, <a href="../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a>, <a href="../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">checkProxyVisibility</a>, <a href="../PresentationElement.html#childrenForMoving()">childrenForMoving</a>, <a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)">collectSubShowingPresentationElements</a>, <a href="../PresentationElement.html#coversPoint(int,int)">coversPoint</a>, <a href="../PresentationElement.html#createFillStrategy()">createFillStrategy</a>, <a href="../PresentationElement.html#createPresentationElementStyle()">createPresentationElementStyle</a>, <a href="../PresentationElement.html#createPropertyChangeListener()">createPropertyChangeListener</a>, <a href="../PresentationElement.html#disposeChildren()">disposeChildren</a>, <a href="../PresentationElement.html#disposePropertyChangeListener()">disposePropertyChangeListener</a>, <a href="../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a>, <a href="../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawBackground</a>, <a href="../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbol</a>, <a href="../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbolBackground</a>, <a href="../PresentationElement.html#dynamicFillColor()">dynamicFillColor</a>, <a href="../PresentationElement.html#dynamicLineColor()">dynamicLineColor</a>, <a href="../PresentationElement.html#dynamicLineWidth()">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicLineWidth(int)">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicPaintShadow()">dynamicPaintShadow</a>, <a href="../PresentationElement.html#dynamicStroke()">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(int)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)">dynamicStyleFillColor</a>, <a href="../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)">dynamicStyleLineColor</a>, <a href="../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)">dynamicStyleTextColor</a>, <a href="../PresentationElement.html#dynamicStyleTransparency()">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)">dynamicStyleValue</a>, <a href="../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">dynamicTextAlignment</a>, <a href="../PresentationElement.html#dynamicTextColor()">dynamicTextColor</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOwnerForChildElement</a>, <a href="../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">findPresentationElement</a>, <a href="../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../PresentationElement.html#generateID()">generateID</a>, <a href="../PresentationElement.html#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>, <a href="../PresentationElement.html#getActualElement()">getActualElement</a>, <a href="../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()">getAdditionalRenderersToNotifyOnPropertiesChange</a>, <a href="../PresentationElement.html#getAssignableModelElementsClasses()">getAssignableModelElementsClasses</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getBoundsWithChildrenOnEdge()">getBoundsWithChildrenOnEdge</a>, <a href="../PresentationElement.html#getCenterlinePoint()">getCenterlinePoint</a>, <a href="../PresentationElement.html#getCenterlinePointX()">getCenterlinePointX</a>, <a href="../PresentationElement.html#getCenterlinePointY()">getCenterlinePointY</a>, <a href="../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)">getChildPresentationElementForContextMenu</a>, <a href="../PresentationElement.html#getChildrenWithSymbolProperties()">getChildrenWithSymbolProperties</a>, <a href="../PresentationElement.html#getConfiguration()">getConfiguration</a>, <a href="../PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="../PresentationElement.html#getDiagramSurface()">getDiagramSurface</a>, <a href="../PresentationElement.html#getDrawComparator()">getDrawComparator</a>, <a href="../PresentationElement.html#getDynamicConfigurations()">getDynamicConfigurations</a>, <a href="../PresentationElement.html#getDynamicStyleOwner()">getDynamicStyleOwner</a>, <a href="../PresentationElement.html#getEffectiveStyleDelegate()">getEffectiveStyleDelegate</a>, <a href="../PresentationElement.html#getEffectiveStyleOwner()">getEffectiveStyleOwner</a>, <a href="../PresentationElement.html#getElementsForRelationshipConnecting()">getElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementToConnectRelationship</a>, <a href="../PresentationElement.html#getFillColor()">getFillColor</a>, <a href="../PresentationElement.html#getFont()">getFont</a>, <a href="../PresentationElement.html#getFontHeight()">getFontHeight</a>, <a href="../PresentationElement.html#getFontRenderContext()">getFontRenderContext</a>, <a href="../PresentationElement.html#getHumanName()">getHumanName</a>, <a href="../PresentationElement.html#getHumanType()">getHumanType</a>, <a href="../PresentationElement.html#getLineColor()">getLineColor</a>, <a href="../PresentationElement.html#getLineWidth()">getLineWidth</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getManipulationBounds(java.awt.Point)">getManipulationBounds</a>, <a href="../PresentationElement.html#getModelElement()">getModelElement</a>, <a href="../PresentationElement.html#getModelElementsForRelationshipConnecting()">getModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">getModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#getModelElementToMove()">getModelElementToMove</a>, <a href="../PresentationElement.html#getNotZoomedTolerance()">getNotZoomedTolerance</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getOwnStyleDelegate()">getOwnStyleDelegate</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a>, <a href="../PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="../PresentationElement.html#getPresentationElementAt(int)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementCount()">getPresentationElementCount</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getProjectImpl()">getProjectImpl</a>, <a href="../PresentationElement.html#getProperty(java.lang.String)">getProperty</a>, <a href="../PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="../PresentationElement.html#getPropertyManagerName()">getPropertyManagerName</a>, <a href="../PresentationElement.html#getRenderer()">getRenderer</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#getStyle()">getStyle</a>, <a href="../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSymbolRenderer</a>, <a href="../PresentationElement.html#getTextColor()">getTextColor</a>, <a href="../PresentationElement.html#getTolerance()">getTolerance</a>, <a href="../PresentationElement.html#getVisibility()">getVisibility</a>, <a href="../PresentationElement.html#getVisiblePresentationElements()">getVisiblePresentationElements</a>, <a href="../PresentationElement.html#handleModelDelete()">handleModelDelete</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#initializeAndAutosize()">initializeAndAutosize</a>, <a href="../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)">internalBeforeUpdate</a>, <a href="../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">internalCreatePropertyChangeListener</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a>, <a href="../PresentationElement.html#internalGetSpecificFont()">internalGetSpecificFont</a>, <a href="../PresentationElement.html#internalGetSpecificTextColor()">internalGetSpecificTextColor</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalSnapToGrid(float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#intersects(int,int,int,int)">intersects</a>, <a href="../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildVisible</a>, <a href="../PresentationElement.html#isCreateElementListener()">isCreateElementListener</a>, <a href="../PresentationElement.html#isDetectable()">isDetectable</a>, <a href="../PresentationElement.html#isDisposed()">isDisposed</a>, <a href="../PresentationElement.html#isLayouting()">isLayouting</a>, <a href="../PresentationElement.html#isMovableByMoveManager()">isMovableByMoveManager</a>, <a href="../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNotNull</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isParentOf</a>, <a href="../PresentationElement.html#isPreserveProportionsWhenGrowing()">isPreserveProportionsWhenGrowing</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#isShowElementTypeAsLabel()">isShowElementTypeAsLabel</a>, <a href="../PresentationElement.html#isSortable()">isSortable</a>, <a href="../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">isSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#isTextEditable()">isTextEditable</a>, <a href="../PresentationElement.html#isUseFillColor()">isUseFillColor</a>, <a href="../PresentationElement.html#isUseFillColorByProperty()">isUseFillColorByProperty</a>, <a href="../PresentationElement.html#isUseGradientForFill()">isUseGradientForFill</a>, <a href="../PresentationElement.html#isVisible()">isVisible</a>, <a href="../PresentationElement.html#isVisibleInDiagram()">isVisibleInDiagram</a>, <a href="../PresentationElement.html#isVisibleOrShrunken()">isVisibleOrShrunken</a>, <a href="../PresentationElement.html#movePathElementsRecursively()">movePathElementsRecursively</a>, <a href="../PresentationElement.html#mustShowContextMenu()">mustShowContextMenu</a>, <a href="../PresentationElement.html#notifyCreated()">notifyCreated</a>, <a href="../PresentationElement.html#notifyDiagramFrameSizeChange()">notifyDiagramFrameSizeChange</a>, <a href="../PresentationElement.html#notifyRepaintManager(boolean)">notifyRepaintManager</a>, <a href="../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildAdd</a>, <a href="../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildRemove</a>, <a href="../PresentationElement.html#onDiagramSurfaceSet()">onDiagramSurfaceSet</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#onFontChange()">onFontChange</a>, <a href="../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">onParentChange</a>, <a href="../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornments</a>, <a href="../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornmentsBackground</a>, <a href="../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenAndAdornments</a>, <a href="../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelfBackground</a>, <a href="../PresentationElement.html#preDisposeOnUpdate()">preDisposeOnUpdate</a>, <a href="../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)">prepareForLineDrawing</a>, <a href="../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)">prepareForTextDrawing</a>, <a href="../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a>, <a href="../PresentationElement.html#recreateListeners()">recreateListeners</a>, <a href="../PresentationElement.html#registerInSortManager()">registerInSortManager</a>, <a href="../PresentationElement.html#rememberBounds()">rememberBounds</a>, <a href="../PresentationElement.html#rememberBounds(java.awt.Rectangle)">rememberBounds</a>, <a href="../PresentationElement.html#removeFromSortManager()">removeFromSortManager</a>, <a href="../PresentationElement.html#removeItSelfOnUpdate()">removeItSelfOnUpdate</a>, <a href="../PresentationElement.html#resizeParent()">resizeParent</a>, <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sAddPresentationElement</a>, <a href="../PresentationElement.html#selectChildrenForMoving()">selectChildrenForMoving</a>, <a href="../PresentationElement.html#selectObjectsForMoving()">selectObjectsForMoving</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setBounds(int,int,int,int)">setBounds</a>, <a href="../PresentationElement.html#setCreateElementListener(boolean)">setCreateElementListener</a>, <a href="../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a>, <a href="../PresentationElement.html#setFont(java.awt.Font)">setFont</a>, <a href="../PresentationElement.html#setLayouting(boolean)">setLayouting</a>, <a href="../PresentationElement.html#setLineColor(java.awt.Color)">setLineColor</a>, <a href="../PresentationElement.html#setLineWidth(int)">setLineWidth</a>, <a href="../PresentationElement.html#setLoadedVisibility(boolean)">setLoadedVisibility</a>, <a href="../PresentationElement.html#setLocation(int,int)">setLocation</a>, <a href="../PresentationElement.html#setLocation(java.awt.Point)">setLocation</a>, <a href="../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">setModelElement</a>, <a href="../PresentationElement.html#setNeedRecreateListeners(boolean)">setNeedRecreateListeners</a>, <a href="../PresentationElement.html#setPropertyManagerName(java.lang.String)">setPropertyManagerName</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#setSize(int,int)">setSize</a>, <a href="../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)">setSize</a>, <a href="../PresentationElement.html#setSize(java.awt.Dimension)">setSize</a>, <a href="../PresentationElement.html#setTextColor(java.awt.Color)">setTextColor</a>, <a href="../PresentationElement.html#setUseFillColor(boolean)">setUseFillColor</a>, <a href="../PresentationElement.html#setVisible(boolean)">setVisible</a>, <a href="../PresentationElement.html#silentApply()">silentApply</a>, <a href="../PresentationElement.html#silentApply(boolean)">silentApply</a>, <a href="../PresentationElement.html#simpleSetBounds(int,int,int,int)">simpleSetBounds</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Point,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapViewToGrid(float)">snapViewToGrid</a>, <a href="../PresentationElement.html#sortObjectsByX(java.util.List)">sortObjectsByX</a>, <a href="../PresentationElement.html#sortObjectsByY(java.util.List)">sortObjectsByY</a>, <a href="../PresentationElement.html#sSetBounds(int,int,int,int)">sSetBounds</a>, <a href="../PresentationElement.html#sSetLocation(int,int)">sSetLocation</a>, <a href="../PresentationElement.html#sSetLocation(java.awt.Point)">sSetLocation</a>, <a href="../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">sSetModelElement</a>, <a href="../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a>, <a href="../PresentationElement.html#sSetParentForAll(java.util.Collection)">sSetParentForAll</a>, <a href="../PresentationElement.html#sSetSize(int,int)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(java.awt.Dimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetVisible(boolean)">sSetVisible</a>, <a href="../PresentationElement.html#tryToDeleteModelElementUponRemoval()">tryToDeleteModelElementUponRemoval</a>, <a href="../PresentationElement.html#update()">update</a>, <a href="../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)">updateLabelsIgnoringSuspendableLater</a>, <a href="../PresentationElement.html#updateModelByView()">updateModelByView</a>, <a href="../PresentationElement.html#updateModelByViewInternal()">updateModelByViewInternal</a>, <a href="../PresentationElement.html#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a>, <a href="../PresentationElement.html#useParentProperties()">useParentProperties</a>, <a href="../PresentationElement.html#useParentStyle()">useParentStyle</a></code></div>
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
<code>getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.CompartmentSupport">Methods inherited from interface com.nomagic.magicdraw.uml.CompartmentSupport</h3>
<code>setVisibleElements</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.LabelOwner">Methods inherited from interface com.nomagic.magicdraw.uml.symbols.LabelOwner</h3>
<code>getModelElement</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></h3>
<code><a href="../../MDElement.html#getProject()">getProject</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement">Methods inherited from interface com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</h3>
<code>addProperty, asPresentationElement, getProperty, getPropertyManager</code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>TimeConstraintView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TimeConstraintView</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>TimeConstraintView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TimeConstraintView</span><wbr/><span class="parameters">(@CheckForNull
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
<section class="detail" id="createNameLabelWrapper()">
<h3>createNameLabelWrapper</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.NameLabelWrapper</span> <span class="element-name">createNameLabelWrapper</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createNameLabelWrapper</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="constructNameText()">
<h3>constructNameText</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructNameText</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>constructNameText</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLabels()">
<h3>createLabels</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createLabels</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createLabels</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotypeLabelWrapper()">
<h3>createStereotypeLabelWrapper</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.StereotypeLabelWrapper</span> <span class="element-name">createStereotypeLabelWrapper</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createStereotypeLabelWrapper</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSmartListenerConfig(java.util.List)">
<h3>createSmartListenerConfig</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createSmartListenerConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createSmartListenerConfig</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</code></dd>
</dl>
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
<dd><code>accept</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">
<h3>findOwnerForElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.model.ModelElement</span> <span class="element-name">findOwnerForElement</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalPreSpecificUpdate()">
<h3>internalPreSpecificUpdate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalPreSpecificUpdate</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></span></div>
<div class="block">Subclasses may override this method and do some actions before specific update is called. Implementation is empty here.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalPreSpecificUpdate</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
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
<section class="detail" id="askDeleteDataConfirmation()">
<h3>askDeleteDataConfirmation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">askDeleteDataConfirmation</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#askDeleteDataConfirmation()">PresentationElement</a></code></span></div>
<div class="block">Declared as interface with default implementation for subclasses. If some subclasses upon
 delete may ask about delete data object as well, they have to redefine this method and return
 true. By default all objects are removed without asking</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#askDeleteDataConfirmation()">askDeleteDataConfirmation</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>confirmation status -- true if asking is necessary, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasSharedModelElement()">
<h3>hasSharedModelElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasSharedModelElement</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#hasSharedModelElement()">PresentationElement</a></code></span></div>
<div class="block">Returns true if <code>ModelElement</code> of this symbol can represented with other symbol.
 If <code>ModelElement</code> is not shared,  it can be deleted together with symbol deleting.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#hasSharedModelElement()">hasSharedModelElement</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if element of this symbol can be represented with other symbol.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalPostUpdatePresentationElement()">
<h3>internalPostUpdatePresentationElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalPostUpdatePresentationElement</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></span></div>
<div class="block">Subclasses may override this method and do some actions after specific update and resizing are executed.
 Implementation is empty here.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalPostUpdatePresentationElement</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels</code></dd>
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
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></span> <span class="element-name">getElement</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getElement()">PresentationElement</a></code></span></div>
<div class="block">Returns model element of this presentation element. Some presentation elements (for example
 TextBoxes) do not have model elements.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getElement</code> in interface <code>com.nomagic.magicdraw.uml.symbols.LabelOwner</code></dd>
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
<section class="detail" id="minimumSizeIgnoringOrientation(java.awt.Dimension)">
<h3>minimumSizeIgnoringOrientation</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">minimumSizeIgnoringOrientation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> min)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>minimumSizeIgnoringOrientation</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>paintSelf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintSelf</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../PresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelf</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="adjustBounds(java.awt.Rectangle)">
<h3>adjustBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">adjustBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../shapes/ShapeElement.html#adjustBounds(java.awt.Rectangle)">ShapeElement</a></code></span></div>
<div class="block">Validates bounds</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../shapes/ShapeElement.html#adjustBounds(java.awt.Rectangle)">adjustBounds</a></code> in class <code><a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>bounds</code> - bounds</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSnapToGrid()">
<h3>isSnapToGrid</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isSnapToGrid</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../shapes/ShapeElement.html#isSnapToGrid()">isSnapToGrid</a></code> in class <code><a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultDimension()">
<h3>getDefaultDimension</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getDefaultDimension</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../shapes/ShapeElement.html#getDefaultDimension()">getDefaultDimension</a></code> in class <code><a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="labelBoundsChanged()">
<h3>labelBoundsChanged</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">labelBoundsChanged</span>()</div>
<div class="block">Adjust time constraint bounds according to the label position changes</div>
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
<dd><code><a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">canChangeParent</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>movedTogether</code> - collection of the elements, whose will change the parent together with this.</dd>
<dd><code>newParent</code> - new symbol parent</dd>
<dd><code>changeElementParent</code> - change element parent</dd>
<dt>Returns:</dt>
<dd>true if parent of symbol can be changed</dd>
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
