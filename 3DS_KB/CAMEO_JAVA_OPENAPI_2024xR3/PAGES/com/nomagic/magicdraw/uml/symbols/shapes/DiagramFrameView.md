# JAVA OPENAPI: DiagramFrameView (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/shapes/DiagramFrameView.html
- source_path: `com/nomagic/magicdraw/uml/symbols/shapes/DiagramFrameView.html`
- source_sha256: `81b10eb6579d53280a2381a358c04070da5c18fc89df06c7a07e4a3d60e193dc`
- captured_utc: `2026-07-14T16:56:02.996544+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.shapes](package-summary.html)

## Class DiagramFrameView

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](../paths/PathConnector.html)
[com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement](ShapeElement.html)
com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView
com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView
com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameView

All Implemented Interfaces:
`com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape`, `[BaseElement](../../BaseElement.html)`, `com.nomagic.magicdraw.uml.CompartmentSupport`, `[MDElement](../../MDElement.html)`, `[ModelElementProvider](../../ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.CompartmentContainer`, `com.nomagic.magicdraw.uml.symbols.CompartmentOwner`, `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`, `com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement`, `com.nomagic.magicdraw.uml.symbols.shapes.PortOwner`, `com.nomagic.magicdraw.uml.symbols.shapes.QualifiedNameLabelOwner`, `[StereotypesDisplayModeOwner](StereotypesDisplayModeOwner.html)`, `com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider`, `com.nomagic.magicdraw.uml.symbols.Wrapable`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApipublic classDiagramFrameView
extends com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView
implements com.nomagic.magicdraw.uml.symbols.shapes.PortOwner, com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[DIAGRAM_TYPES_FOR_PORTS_ON_FRAME](#DIAGRAM_TYPES_FOR_PORTS_ON_FRAME)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView
`SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY, SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODE_IMAGE_AND_STEREOTYPES, SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODE_STEREOTYPES, SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODES`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`CONTAINER_SHAPE_INSETS, SHAPE_DISTANCE_FROM_EDGE`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.[ShapeElement](ShapeElement.html)
`[BORDER_ELEMENT_MARGIN_ALL](ShapeElement.html#BORDER_ELEMENT_MARGIN_ALL), [BORDER_ELEMENT_MARGIN_BOTTOM](ShapeElement.html#BORDER_ELEMENT_MARGIN_BOTTOM), [BORDER_ELEMENT_MARGIN_LEFT](ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT), [BORDER_ELEMENT_MARGIN_LEFT_RIGHT](ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT_RIGHT), [BORDER_ELEMENT_MARGIN_MODES](ShapeElement.html#BORDER_ELEMENT_MARGIN_MODES), [BORDER_ELEMENT_MARGIN_NONE](ShapeElement.html#BORDER_ELEMENT_MARGIN_NONE), [BORDER_ELEMENT_MARGIN_RIGHT](ShapeElement.html#BORDER_ELEMENT_MARGIN_RIGHT), [BORDER_ELEMENT_MARGIN_TOP](ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP), [BORDER_ELEMENT_MARGIN_TOP_BOTTOM](ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP_BOTTOM), [BOTTOM_EDGE](ShapeElement.html#BOTTOM_EDGE), [INSIDE_EDGE_POSITION](ShapeElement.html#INSIDE_EDGE_POSITION), [LEFT_EDGE](ShapeElement.html#LEFT_EDGE), [NEED_AUTOSIZE_FULL](ShapeElement.html#NEED_AUTOSIZE_FULL), [NEED_AUTOSIZE_LAYOUT](ShapeElement.html#NEED_AUTOSIZE_LAYOUT), [NEED_AUTOSIZE_NONE](ShapeElement.html#NEED_AUTOSIZE_NONE), [NO_EDGE](ShapeElement.html#NO_EDGE), [NULL_INSETS](ShapeElement.html#NULL_INSETS), [ON_EDGE_POSITION](ShapeElement.html#ON_EDGE_POSITION), [OUTSIDE_EDGE_POSITION](ShapeElement.html#OUTSIDE_EDGE_POSITION), [RIGHT_EDGE](ShapeElement.html#RIGHT_EDGE), [SPACE](ShapeElement.html#SPACE), [SPACE_INSETS](ShapeElement.html#SPACE_INSETS), [SPACE_INSETS_EMPTY_TOP_BOTTOM](ShapeElement.html#SPACE_INSETS_EMPTY_TOP_BOTTOM), [TOP_EDGE](ShapeElement.html#TOP_EDGE)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[showsProxy](../paths/PathConnector.html#showsProxy)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DEFAULT_LINE_WIDTH](../PresentationElement.html#DEFAULT_LINE_WIDTH), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [HANDLE_SIZE](../PresentationElement.html#HANDLE_SIZE), [MAX_LINE_WIDTH](../PresentationElement.html#MAX_LINE_WIDTH), [MIN_LINE_WIDTH](../PresentationElement.html#MIN_LINE_WIDTH), [peStyle](../PresentationElement.html#peStyle), [SHADOW_WIDTH](../PresentationElement.html#SHADOW_WIDTH), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
Fields inherited from interface com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape
`FRAME_DISTANCE_FROM_EDGE`
Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.QualifiedNameLabelOwner
`QNAME_DISPLAY_MODE_ABOVE_NAME, QNAME_DISPLAY_MODE_BELOW_NAME, QNAME_DISPLAY_MODE_DO_NOT_DISPLAY, QNAME_DISPLAY_MODE_MERGE_WITH_NAME, QNAME_DISPLAY_MODES`
Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.[StereotypesDisplayModeOwner](StereotypesDisplayModeOwner.html)
`[DSL_STEREOTYPE_DISPLAY_MODE_ALL](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL), [DSL_STEREOTYPE_DISPLAY_MODE_LAST](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST), [DSL_STEREOTYPE_DISPLAY_MODE_NONE](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE), [DSL_STEREOTYPE_DISPLAY_MODES](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES), [STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES), [STEREOTYPE_DISPLAY_MODE_ICON](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON), [STEREOTYPES_DISPLAY_MODES](StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES), [STEREOTYPES_DISPLAY_MODES_SIMPLE](StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramFrameView](#%3Cinit%3E())()`

`[DiagramFrameView](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) parent)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../../Visitor.html) visitor)`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[adjustBoundsBeforeChange](#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rec,
 boolean autosizeOperation,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)> movedTogether)`
Validate bounds before bounds change operation
`void`
`[atInsert](#atInsert())()`
Invalidates object at insert
`void`
`[calculateFrameElementBounds](#calculateFrameElementBounds())()`

`boolean`
`[canAddInstance](#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) symbol)`
Object view has no children.
`protected boolean`
`[canFill](#canFill())()`

`protected boolean`
`[canMoveChildOutside](#canMoveChildOutside(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) element)`

`boolean`
`[coversPoint](#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
checks if object covers provided point
`protected void`
`[createSmartListenerConfig](#createSmartListenerConfig(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)`

`void`
`[dispose](#dispose())()`
disposes ends of links when link is deleted
`int`
`[getCornerArcSize](#getCornerArcSize())()`

`protected [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[getDefaultDimension](#getDefaultDimension())()`

`[Diagram](../../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)`
`[getElement](#getElement())()`
Returns model element of this presentation element.
`[EncapsulatedClassifier](../../../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html)`
`[getEncapsulatedClassifier](#getEncapsulatedClassifier())()`

`[TypedElement](../../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html)`
`[getEncapsulatedClassifierProvider](#getEncapsulatedClassifierProvider())()`

`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[getFillColor](#getFillColor())()`
Returns fill color
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getFrameElementBounds](#getFrameElementBounds())()`

`com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderView`
`[getHeaderView](#getHeaderView())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHumanName](#getHumanName())()`
Returns human representation of the data type
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHumanType](#getHumanType())()`
Returns human representation of the data type
`[PresentationElement](../PresentationElement.html)`
`[getParentSymbolStyleOwner](#getParentSymbolStyleOwner())()`
Returns parent to which this symbol delegates style attributes related functionality.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getResourceID](#getResourceID())()`

`protected com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView.StereotypeDisplayData`
`[getStereotypesToDisplay](#getStereotypesToDisplay())()`

`boolean`
`[hasBoundaryDetails](#hasBoundaryDetails())()`
Returns true if frame carries details on its border.
`void`
`[internalLayoutChildren](#internalLayoutChildren(boolean))(boolean calculatePrefSize)`

`protected void`
`[internalPostUpdatePresentationElement](#internalPostUpdatePresentationElement())()`
Subclasses may override this method and do some actions after specific update and resizing are executed.
`protected void`
`[internalSpecificUpdate](#internalSpecificUpdate())()`
Specific to every shape and model element update operation.
`boolean`
`[intersects](#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
checks whether object intersects with given rectangle
`boolean`
`[isHorizontalCenterlineProvider](#isHorizontalCenterlineProvider())()`
Indicates whether this shape provides horizontal center-lines to other shapes.
`boolean`
`[isOwningMode](#isOwningMode())()`

`boolean`
`[isSetAsDiagramFrame](#isSetAsDiagramFrame())()`

`boolean`
`[isVerticalCenterlineProvider](#isVerticalCenterlineProvider())()`
Indicates whether this shape provides vertical center-lines to other shapes.
`void`
`[layoutFrame](#layoutFrame())()`

`void`
`[layoutFrameIfSet](#layoutFrameIfSet())()`

`protected void`
`[minimumOrMinimumShrinkableDimension](#minimumOrMinimumShrinkableDimension(java.awt.Dimension))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size)`

`void`
`[minimumSizeForShrinkingIgnoringOrientation](#minimumSizeForShrinkingIgnoringOrientation(java.awt.Dimension,int,int))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size,
 int locationX,
 int locationY)`

`protected void`
`[movePathElement](#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector))([PathElement](../paths/PathElement.html) link,
 [PathConnector](../paths/PathConnector.html) requestor)`
Calculates position of a path element.
`boolean`
`[mustShowContextMenu](#mustShowContextMenu())()`

`protected void`
`[preferredSizeIgnoringOrientation](#preferredSizeIgnoringOrientation(java.awt.Dimension,int,int))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)`

`boolean`
`[providesHorizontalCenterline](#providesHorizontalCenterline())()`
Indicates if this shape can provide a horizontal centerline for other shapes to snap.
`boolean`
`[providesVerticalCenterline](#providesVerticalCenterline())()`
Indicates if this shape can provide a vertical centerline for other shapes to snap.
`protected void`
`[selfSpecificHeaderShapeDraw](#selfSpecificHeaderShapeDraw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`boolean`
`[snapsToCenterlines](#snapsToCenterlines())()`
Indicates if this shape can be snapped to centerlines.
`void`
`[sSetParent](#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) parent)`
Sets parent for this view.
`boolean`
`[useParentStyle](#useParentStyle())()`
Does this element uses parent style or has it's own?
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView
`canSuppressContent, getBooleanCompartmentPropertyValue, getConstraintAndTaggedValueAlignment, getConstraintTextMode, getDefaultElementStereotypeToHeader, getDSLStereotypesDisplayMode, getElementNumberDisplayMode, getElementPropertiesCompartmentView, getMiddlePointByIcon, getQNameDisplayMode, getSecondaryImageAndStereotypeDisplayMode, getStereotypeLabel, getStereotypesDisplayMode, internalApplyProperties, internalBeforeUpdate, internalSilentApply, isShowDerivedSign, isShowElementProperties, isShowIcon, isShowNumberTagName, isShowRakeIcon, isShowRakeSymbol, isShowTaggedValues, isShowType, propertyChange, recursiveAutosize, setConstraintAndTaggedValueAlignment, setConstraints, setConstraintTextMode, setDSLStereotypesDisplayMode, setElementNumberDisplayMode, setQNameDisplayMode, setSecondaryImageAndStereotypeDisplayMode, setShowConstraints, setShowDerivedSign, setShowElementProperties, setShowIcon, setShowNumberTagName, setShowTaggedValues, setShowType, setStereotype, setStereotypesDisplayMode, setTaggedValues, sSetConstraintAndTaggedValueAlignment, sSetConstraintTextMode, sSetDSLStereotypesDisplayMode, sSetElement, sSetElementNumberDisplayMode, sSetQNameDisplayMode, sSetSecondaryImageAndStereotypeDisplayMode, sSetShowConstraints, sSetShowDerivedSign, sSetShowElementProperties, sSetShowIcon, sSetShowNumberTagName, sSetShowTaggedValues, sSetShowType, sSetStereotypesDisplayMode, updateBorderVisibility, updateName`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView
`addCompartment, addCompartment, addPresentationElement, applyCompartmentsStyle, areBoxCompartmentsSuppressed, askDeleteDataConfirmation, asPresentationElement, autosizeShapesOnEdge, canAddChild, canChangeParent, canHideBorder, childrenBoundsForReshape, clone, createBoundsShape, createCompartmentElements, createStateForUpdateOperation, doInternalLayoutAdditionCompartment, doInternalLayoutChildren, getAdditionalCompartment, getAdditionalCompartmentContainer, getAdditionalCompartmentDescriptor, getAdditionalCompartmentInsets, getAdditionalCompartmentToLayout, getAdditionalRenderersToNotifyOnPropertiesChange, getChildrenBoundsForPreferredBounds, getChildrenInsets, getCollections, getCompartmentByID, getCompartmentIDs, getCompartments, getCompartmentsIDs, getCompartmentStyleDelegate, getConfiguredPreferredSizeForAutosize, getHeaderMaxYForShrinkableShape, getHeaderVerticalPositionForLayout, getLastHeaderShapeElementBottom, getMainCompartmentContainer, getName, getPreferredDimensionForAutosize, hasManipulatedChildrenIncludingIndirect, hasSharedModelElement, internalAddIndirectManipulatedChildrenRect, internalGetHeaderInsets, internalGetIndirectManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalPostSpecificUpdate, internalSetCollections, isBorderVisible, isChildLayoutable, isChildMovable, isMakePreferredSizeAfterPropertiesChange, isWrapEnabled, iterateCompartmentDelegates, makePreferredSizeAfterPropertiesChange, makePreferredSizeAfterPropertiesChange, onChildEdgeChange, paintSelf, removeCompartment, removeCompartment, removePresentationElement, setCollections, setCompartmentSuppressed, setHeaderObject, setMakePreferredSizeAfterPropertiesChange, setReshapeMode, setVisibleElements, setWrapEnabled, sSetCompartmentSuppressed, sSetName, sSetWrapEnabled, updateChildrenVisibility, updateCompartmentsVisibility`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
`addExtraChildrenPrefSizePadding, autosize, autosizeAndResizeParent, calculateMinY, calculateOvalShapePreferredSize, correctChildrenVector, editName, getAdditionalHeaderHeightForPreferredBounds, getHeaderBoundsForPreferredBounds, getHeaderDistanceFromTopForOvalShape, getHeaderInsets, getHeaderObject, getHeaderVerticalPosition, getNameLabel, getOvalShapeAvailableWidth, getPreferredBounds, getPresentationElementAt, getProxyPresentationElementsStream, internalGetHeaderBoundsForPreferredBounds, internalPreSpecificUpdate, internalUpdatePresentationElement, invalidate, isContentHidden, isHeaderOrientationVertical, isOvalShape, isParentShowsProxy, minimumDimension, minimumDimensionForShrinking, minimumSizeIgnoringOrientation, paintChildren, preferredDimension, setHeaderVerticalPosition, setName, setTextEditable, sSetAutosize, sSetHeaderVerticalPosition, switchWidthHeightIfVerticalOrientation`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, checkShowsProxy, clearShowsProxy, constructLayoutHelper, getChildrenBounds, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getRemovableChildren, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAppendChildRect, internalGetChildAt, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildrenBackground, prefDimensionByManipulatedChildren, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.[ShapeElement](ShapeElement.html)
`[addBreakPoints](ShapeElement.html#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [adjustBounds](ShapeElement.html#adjustBounds(java.awt.Rectangle)), [adjustOnEdge](ShapeElement.html#adjustOnEdge()), [adjustOnEdge](ShapeElement.html#adjustOnEdge(java.awt.Rectangle,int,int,int)), [adjustOnEdgeChildren](ShapeElement.html#adjustOnEdgeChildren()), [autosize](ShapeElement.html#autosize()), [calculateAdjustOnEdgeLocation](ShapeElement.html#calculateAdjustOnEdgeLocation(java.awt.Rectangle)), [calculateAndGetMinimumShrinkingDimension](ShapeElement.html#calculateAndGetMinimumShrinkingDimension(int,int)), [calculateAndGetPreferredDimension](ShapeElement.html#calculateAndGetPreferredDimension()), [calculateEdge](ShapeElement.html#calculateEdge()), [calculateMinimumDimension](ShapeElement.html#calculateMinimumDimension()), [calculateOnEdgeBounds](ShapeElement.html#calculateOnEdgeBounds()), [calculatePreferredDimension](ShapeElement.html#calculatePreferredDimension()), [calculatePreferredDimension](ShapeElement.html#calculatePreferredDimension(int,int)), [canBeAutosized](ShapeElement.html#canBeAutosized()), [canHavePaths](ShapeElement.html#canHavePaths()), [clearOldRect](ShapeElement.html#clearOldRect()), [edgeChanged](ShapeElement.html#edgeChanged()), [ensureDimension](ShapeElement.html#ensureDimension(boolean)), [ensurePreferredDimensionIfShrinkable](ShapeElement.html#ensurePreferredDimensionIfShrinkable()), [ensurePreferredDimensionIfShrinkable](ShapeElement.html#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)), [findFreePlaceForShapeOnBorder](ShapeElement.html#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)), [getBorderElementMargin](ShapeElement.html#getBorderElementMargin()), [getBounds](ShapeElement.html#getBounds()), [getCenterlineableInnerParts](ShapeElement.html#getCenterlineableInnerParts(int)), [getDimensionForShrinking](ShapeElement.html#getDimensionForShrinking(int,int)), [getEdgeLine](ShapeElement.html#getEdgeLine(int)), [getFixedConnectionPoints](ShapeElement.html#getFixedConnectionPoints()), [getHeaderInsetReduce](ShapeElement.html#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)), [getInsetsForOnEdgeShapes](ShapeElement.html#getInsetsForOnEdgeShapes()), [getIntersection](ShapeElement.html#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getIntersection](ShapeElement.html#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)), [getIntersection](ShapeElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getLoadedDimension](ShapeElement.html#getLoadedDimension()), [getMiddlePoint](ShapeElement.html#getMiddlePoint()), [getMiddlePoint](ShapeElement.html#getMiddlePoint(java.awt.Point)), [getMiddlePointX](ShapeElement.html#getMiddlePointX()), [getMiddlePointX](ShapeElement.html#getMiddlePointX(java.awt.Point)), [getMiddlePointY](ShapeElement.html#getMiddlePointY()), [getMiddlePointY](ShapeElement.html#getMiddlePointY(java.awt.Point)), [getMinimumDimension](ShapeElement.html#getMinimumDimension()), [getNearestEdge](ShapeElement.html#getNearestEdge(int,int)), [getNearestEdge](ShapeElement.html#getNearestEdge(java.awt.Rectangle)), [getNeedAutosizeFlag](ShapeElement.html#getNeedAutosizeFlag()), [getNotCopyBounds](ShapeElement.html#getNotCopyBounds()), [getOnEdge](ShapeElement.html#getOnEdge()), [getOnEdgeCornerDistance](ShapeElement.html#getOnEdgeCornerDistance()), [getOnEdgePosition](ShapeElement.html#getOnEdgePosition()), [getPreferredDimension](ShapeElement.html#getPreferredDimension()), [getReshapeMode](ShapeElement.html#getReshapeMode()), [getSizeForDrawing](ShapeElement.html#getSizeForDrawing()), [getSuspendShapeAutoResizeMode](ShapeElement.html#getSuspendShapeAutoResizeMode()), [hasManipulator](ShapeElement.html#hasManipulator()), [initialize](ShapeElement.html#initialize()), [internalGetBoundsShape](ShapeElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [isAutosized](ShapeElement.html#isAutosized()), [isCenterlineInner](ShapeElement.html#isCenterlineInner()), [isOnEdge](ShapeElement.html#isOnEdge()), [isShapeOnEdge](ShapeElement.html#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isShrinkable](ShapeElement.html#isShrinkable()), [isSnapShapesOnBorderToGrid](ShapeElement.html#isSnapShapesOnBorderToGrid()), [isSnapToGrid](ShapeElement.html#isSnapToGrid()), [isUseFixedConnectionPoints](ShapeElement.html#isUseFixedConnectionPoints()), [layoutChildren](ShapeElement.html#layoutChildren()), [maximumDimension](ShapeElement.html#maximumDimension(java.awt.Dimension)), [moveLinksToSelf](ShapeElement.html#moveLinksToSelf()), [movePathElements](ShapeElement.html#movePathElements()), [needAdjustToMaximumDimension](ShapeElement.html#needAdjustToMaximumDimension()), [prepareForShadowDrawing](ShapeElement.html#prepareForShadowDrawing(java.awt.Graphics2D)), [resetCalculatePreferredRegardingChildren](ShapeElement.html#resetCalculatePreferredRegardingChildren()), [setAutosize](ShapeElement.html#setAutosize(boolean)), [setBorderElementMargin](ShapeElement.html#setBorderElementMargin(java.lang.String)), [setCalculatePreferredRegardingChildren](ShapeElement.html#setCalculatePreferredRegardingChildren(boolean)), [setLoadedDimension](ShapeElement.html#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)), [setMinimumDimension](ShapeElement.html#setMinimumDimension(int,int)), [setNeedAutosizeFlag](ShapeElement.html#setNeedAutosizeFlag(byte)), [setOldRect](ShapeElement.html#setOldRect(java.awt.Rectangle)), [setOnEdge](ShapeElement.html#setOnEdge(int)), [setPreferredDimension](ShapeElement.html#setPreferredDimension(int,int)), [setSnapShapesOnBorderToGrid](ShapeElement.html#setSnapShapesOnBorderToGrid(boolean)), [setSuspendShapeAutoResizeMode](ShapeElement.html#setSuspendShapeAutoResizeMode(java.lang.String)), [setUseFixedConnectionPoints](ShapeElement.html#setUseFixedConnectionPoints(boolean)), [shouldDrawShadow](ShapeElement.html#shouldDrawShadow()), [simpleSetBounds](ShapeElement.html#simpleSetBounds(int,int,int,int,boolean)), [simpleSetBounds](ShapeElement.html#simpleSetBounds(java.awt.Rectangle)), [sSetBorderElementMargin](ShapeElement.html#sSetBorderElementMargin(java.lang.String)), [sSetBounds](ShapeElement.html#sSetBounds(java.awt.Rectangle)), [sSetSuspendShapeAutoResizeMode](ShapeElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)), [sSetVisibility](ShapeElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [toString](ShapeElement.html#toString()), [updateLater](ShapeElement.html#updateLater())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[addConnectedPathElement](../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [disposeConnectedPaths](../paths/PathConnector.html#disposeConnectedPaths()), [findSymbolForEnd](../paths/PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)), [findSymbolForEnd](../paths/PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)), [getConnectedPathElement](../paths/PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [getConnectedPathElementCount](../paths/PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)), [getPreferredArrowLength](../paths/PathConnector.html#getPreferredArrowLength()), [isShowsProxy](../paths/PathConnector.html#isShowsProxy()), [movePathElement](../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)), [removeConnectedPathElement](../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sAddConnectedPathElement](../paths/PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [selectPathsForMoving](../paths/PathConnector.html#selectPathsForMoving(java.util.List)), [setParent](../paths/PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [setVisibility](../paths/PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [sRemoveConnectedPathElement](../paths/PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sSetConnectedPathElements](../paths/PathConnector.html#sSetConnectedPathElements(java.util.List)), [supportsVisibleConnectedPathElementsIfSelfInvisible](../paths/PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[addPresentationElement](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addProperty](../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [adjustChildBounds](../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [alwaysShowTooltip](../PresentationElement.html#alwaysShowTooltip()), [applyProperties](../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [atInsertChildren](../PresentationElement.html#atInsertChildren()), [autosizeAndResizeManipulatedParent](../PresentationElement.html#autosizeAndResizeManipulatedParent()), [beforeDelete](../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)), [boundsChanged](../PresentationElement.html#boundsChanged()), [boundsChanged](../PresentationElement.html#boundsChanged(java.awt.Rectangle)), [canAddChild](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)), [canAddInstance](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDisposedOnUpdate](../PresentationElement.html#canBeDisposedOnUpdate()), [canChangeElementOwner](../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [changeProperties](../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [checkElementOwnerOnChange](../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [checkProxyVisibility](../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [childrenForMoving](../PresentationElement.html#childrenForMoving()), [collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)), [collectSubShowingPresentationElements](../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)), [coversPoint](../PresentationElement.html#coversPoint(int,int)), [createFillStrategy](../PresentationElement.html#createFillStrategy()), [createPresentationElementStyle](../PresentationElement.html#createPresentationElementStyle()), [createPropertyChangeListener](../PresentationElement.html#createPropertyChangeListener()), [disposeChildren](../PresentationElement.html#disposeChildren()), [disposePropertyChangeListener](../PresentationElement.html#disposePropertyChangeListener()), [draw](../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawBackground](../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbol](../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbolBackground](../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [dynamicFillColor](../PresentationElement.html#dynamicFillColor()), [dynamicLineColor](../PresentationElement.html#dynamicLineColor()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth(int)), [dynamicPaintShadow](../PresentationElement.html#dynamicPaintShadow()), [dynamicStroke](../PresentationElement.html#dynamicStroke()), [dynamicStroke](../PresentationElement.html#dynamicStroke(int)), [dynamicStroke](../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)), [dynamicStyleFillColor](../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)), [dynamicStyleLineColor](../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)), [dynamicStyleTextColor](../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency()), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)), [dynamicStyleValue](../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)), [dynamicTextAlignment](../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)), [dynamicTextColor](../PresentationElement.html#dynamicTextColor()), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [findOwnerForChildElement](../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [findOwnerForElement](../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)), [findPresentationElement](../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)), [firePropertyChange](../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateID](../PresentationElement.html#generateID()), [getAbstractDiagramPresentationElement](../PresentationElement.html#getAbstractDiagramPresentationElement()), [getActualElement](../PresentationElement.html#getActualElement()), [getAssignableModelElementsClasses](../PresentationElement.html#getAssignableModelElementsClasses()), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getBoundsToRepaint](../PresentationElement.html#getBoundsToRepaint()), [getBoundsWithChildrenOnEdge](../PresentationElement.html#getBoundsWithChildrenOnEdge()), [getCenterlinePoint](../PresentationElement.html#getCenterlinePoint()), [getCenterlinePointX](../PresentationElement.html#getCenterlinePointX()), [getCenterlinePointY](../PresentationElement.html#getCenterlinePointY()), [getChildPresentationElementForContextMenu](../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)), [getChildrenWithSymbolProperties](../PresentationElement.html#getChildrenWithSymbolProperties()), [getConfiguration](../PresentationElement.html#getConfiguration()), [getDiagramPresentationElement](../PresentationElement.html#getDiagramPresentationElement()), [getDiagramSurface](../PresentationElement.html#getDiagramSurface()), [getDrawComparator](../PresentationElement.html#getDrawComparator()), [getDynamicConfigurations](../PresentationElement.html#getDynamicConfigurations()), [getDynamicStyleOwner](../PresentationElement.html#getDynamicStyleOwner()), [getEffectiveStyleDelegate](../PresentationElement.html#getEffectiveStyleDelegate()), [getEffectiveStyleOwner](../PresentationElement.html#getEffectiveStyleOwner()), [getElementsForRelationshipConnecting](../PresentationElement.html#getElementsForRelationshipConnecting()), [getElementToConnectRelationship](../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFont](../PresentationElement.html#getFont()), [getFontHeight](../PresentationElement.html#getFontHeight()), [getFontRenderContext](../PresentationElement.html#getFontRenderContext()), [getLineColor](../PresentationElement.html#getLineColor()), [getLineWidth](../PresentationElement.html#getLineWidth()), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point)), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getManipulationBounds](../PresentationElement.html#getManipulationBounds(java.awt.Point)), [getModelElement](../PresentationElement.html#getModelElement()), [getModelElementsForRelationshipConnecting](../PresentationElement.html#getModelElementsForRelationshipConnecting()), [getModelElementToConnectRelationship](../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [getModelElementToMove](../PresentationElement.html#getModelElementToMove()), [getNotZoomedTolerance](../PresentationElement.html#getNotZoomedTolerance()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getOwnStyleDelegate](../PresentationElement.html#getOwnStyleDelegate()), [getParent](../PresentationElement.html#getParent()), [getPreferredSize](../PresentationElement.html#getPreferredSize()), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(int)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementCount](../PresentationElement.html#getPresentationElementCount()), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getProjectImpl](../PresentationElement.html#getProjectImpl()), [getProperty](../PresentationElement.html#getProperty(java.lang.String)), [getPropertyManager](../PresentationElement.html#getPropertyManager()), [getPropertyManagerName](../PresentationElement.html#getPropertyManagerName()), [getRenderer](../PresentationElement.html#getRenderer()), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [getStyle](../PresentationElement.html#getStyle()), [getSymbolRenderer](../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getTextColor](../PresentationElement.html#getTextColor()), [getTolerance](../PresentationElement.html#getTolerance()), [getVisibility](../PresentationElement.html#getVisibility()), [getVisiblePresentationElements](../PresentationElement.html#getVisiblePresentationElements()), [handleModelDelete](../PresentationElement.html#handleModelDelete()), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [initializeAndAutosize](../PresentationElement.html#initializeAndAutosize()), [internalCreatePropertyChangeListener](../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [internalGetModelElementToConnectRelationship](../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [internalGetPresentationElementStroke](../PresentationElement.html#internalGetPresentationElementStroke(int)), [internalGetSpecificFont](../PresentationElement.html#internalGetSpecificFont()), [internalGetSpecificTextColor](../PresentationElement.html#internalGetSpecificTextColor()), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(float)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)), [intersects](../PresentationElement.html#intersects(int,int,int,int)), [isChildVisible](../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isCreateElementListener](../PresentationElement.html#isCreateElementListener()), [isDetectable](../PresentationElement.html#isDetectable()), [isDisposed](../PresentationElement.html#isDisposed()), [isLayouting](../PresentationElement.html#isLayouting()), [isMovableByMoveManager](../PresentationElement.html#isMovableByMoveManager()), [isNotNull](../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isPreserveProportionsWhenGrowing](../PresentationElement.html#isPreserveProportionsWhenGrowing()), [isSelected](../PresentationElement.html#isSelected()), [isShowElementTypeAsLabel](../PresentationElement.html#isShowElementTypeAsLabel()), [isSortable](../PresentationElement.html#isSortable()), [isSuitableToConnectRelationship](../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [isTextEditable](../PresentationElement.html#isTextEditable()), [isUseFillColor](../PresentationElement.html#isUseFillColor()), [isUseFillColorByProperty](../PresentationElement.html#isUseFillColorByProperty()), [isUseGradientForFill](../PresentationElement.html#isUseGradientForFill()), [isVisible](../PresentationElement.html#isVisible()), [isVisibleInDiagram](../PresentationElement.html#isVisibleInDiagram()), [isVisibleOrShrunken](../PresentationElement.html#isVisibleOrShrunken()), [movePathElementsRecursively](../PresentationElement.html#movePathElementsRecursively()), [notifyCreated](../PresentationElement.html#notifyCreated()), [notifyDiagramFrameSizeChange](../PresentationElement.html#notifyDiagramFrameSizeChange()), [notifyRepaintManager](../PresentationElement.html#notifyRepaintManager(boolean)), [onChildAdd](../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onChildRemove](../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onDiagramSurfaceSet](../PresentationElement.html#onDiagramSurfaceSet()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [onFontChange](../PresentationElement.html#onFontChange()), [onParentChange](../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [paintAdornments](../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintAdornmentsBackground](../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenAndAdornments](../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelfBackground](../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [preDisposeOnUpdate](../PresentationElement.html#preDisposeOnUpdate()), [prepareForLineDrawing](../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)), [prepareForTextDrawing](../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)), [recreateListeners](../PresentationElement.html#recreateListeners()), [registerInSortManager](../PresentationElement.html#registerInSortManager()), [rememberBounds](../PresentationElement.html#rememberBounds()), [rememberBounds](../PresentationElement.html#rememberBounds(java.awt.Rectangle)), [removeFromSortManager](../PresentationElement.html#removeFromSortManager()), [removeItSelfOnUpdate](../PresentationElement.html#removeItSelfOnUpdate()), [resizeParent](../PresentationElement.html#resizeParent()), [sAddPresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [selectChildrenForMoving](../PresentationElement.html#selectChildrenForMoving()), [selectObjectsForMoving](../PresentationElement.html#selectObjectsForMoving()), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setBounds](../PresentationElement.html#setBounds(int,int,int,int)), [setCreateElementListener](../PresentationElement.html#setCreateElementListener(boolean)), [setElement](../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setFont](../PresentationElement.html#setFont(java.awt.Font)), [setLayouting](../PresentationElement.html#setLayouting(boolean)), [setLineColor](../PresentationElement.html#setLineColor(java.awt.Color)), [setLineWidth](../PresentationElement.html#setLineWidth(int)), [setLoadedVisibility](../PresentationElement.html#setLoadedVisibility(boolean)), [setLocation](../PresentationElement.html#setLocation(int,int)), [setLocation](../PresentationElement.html#setLocation(java.awt.Point)), [setModelElement](../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [setNeedRecreateListeners](../PresentationElement.html#setNeedRecreateListeners(boolean)), [setPropertyManagerName](../PresentationElement.html#setPropertyManagerName(java.lang.String)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [setSize](../PresentationElement.html#setSize(int,int)), [setSize](../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)), [setSize](../PresentationElement.html#setSize(java.awt.Dimension)), [setTextColor](../PresentationElement.html#setTextColor(java.awt.Color)), [setUseFillColor](../PresentationElement.html#setUseFillColor(boolean)), [setVisible](../PresentationElement.html#setVisible(boolean)), [silentApply](../PresentationElement.html#silentApply()), [silentApply](../PresentationElement.html#silentApply(boolean)), [simpleSetBounds](../PresentationElement.html#simpleSetBounds(int,int,int,int)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Point,float)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)), [snapViewToGrid](../PresentationElement.html#snapViewToGrid(float)), [sortObjectsByX](../PresentationElement.html#sortObjectsByX(java.util.List)), [sortObjectsByY](../PresentationElement.html#sortObjectsByY(java.util.List)), [sSetBounds](../PresentationElement.html#sSetBounds(int,int,int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(java.awt.Point)), [sSetModelElement](../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [sSetParentForAll](../PresentationElement.html#sSetParentForAll(java.util.Collection)), [sSetSize](../PresentationElement.html#sSetSize(int,int)), [sSetSize](../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)), [sSetSize](../PresentationElement.html#sSetSize(java.awt.Dimension)), [sSetVisible](../PresentationElement.html#sSetVisible(boolean)), [tryToDeleteModelElementUponRemoval](../PresentationElement.html#tryToDeleteModelElementUponRemoval()), [update](../PresentationElement.html#update()), [updateAfterLoad](../PresentationElement.html#updateAfterLoad()), [updateLabelsIgnoringSuspendableLater](../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)), [updateModelByView](../PresentationElement.html#updateModelByView()), [updateModelByViewInternal](../PresentationElement.html#updateModelByViewInternal()), [updateViewAfterPropertyChange](../PresentationElement.html#updateViewAfterPropertyChange()), [useParentProperties](../PresentationElement.html#useParentProperties())`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getProjectProvider, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../BaseElement.html)
`[canAdd](../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape
`getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY`
Methods inherited from interface com.nomagic.magicdraw.uml.CompartmentSupport
`setVisibleElements`
Methods inherited from interface com.nomagic.magicdraw.uml.[MDElement](../../MDElement.html)
`[getProject](../../MDElement.html#getProject())`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement
`addProperty, asPresentationElement, getProperty, getPropertyManager`

============ FIELD DETAIL =========== 
Field Details
DIAGRAM_TYPES_FOR_PORTS_ON_FRAME
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> DIAGRAM_TYPES_FOR_PORTS_ON_FRAME
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramFrameView
public DiagramFrameView()
DiagramFrameView
public DiagramFrameView(@CheckForNull
 [PresentationElement](../PresentationElement.html) parent)
 ============ METHOD DETAIL ========== 
Method Details
accept
public void accept([Visitor](../../Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
 See "Visitor" pattern for more details.
Specified by:
`[accept](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../../MDElement.html)`
Overrides:
`accept` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
selfSpecificHeaderShapeDraw
protected void selfSpecificHeaderShapeDraw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
Overrides:
`selfSpecificHeaderShapeDraw` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
canFill
protected boolean canFill()
Overrides:
`[canFill](../PresentationElement.html#canFill())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
true if symbol can be filled with some color
getFillColor
public [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) getFillColor()
Description copied from class: `[PresentationElement](../PresentationElement.html#getFillColor())`
Returns fill color
Overrides:
`[getFillColor](../PresentationElement.html#getFillColor())` in class `[PresentationElement](../PresentationElement.html)`
getCornerArcSize
public int getCornerArcSize()
getResourceID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getResourceID()
Specified by:
`[getResourceID](../../MDElement.html#getResourceID())` in interface `[MDElement](../../MDElement.html)`
Overrides:
`getResourceID` in class `com.nomagic.magicdraw.uml.MDElementImpl`
useParentStyle
public boolean useParentStyle()
Description copied from class: `[PresentationElement](../PresentationElement.html#useParentStyle())`
Does this element uses parent style or has it's own?
Overrides:
`[useParentStyle](../PresentationElement.html#useParentStyle())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
true, if element does not have style and uses parent's style.
getParentSymbolStyleOwner
public [PresentationElement](../PresentationElement.html) getParentSymbolStyleOwner()
Description copied from class: `[PresentationElement](../PresentationElement.html#getParentSymbolStyleOwner())`
Returns parent to which this symbol delegates style attributes related functionality.
Overrides:
`[getParentSymbolStyleOwner](../PresentationElement.html#getParentSymbolStyleOwner())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
parent symbol to delegate or null if this symbol does not delegate.
mustShowContextMenu
public boolean mustShowContextMenu()
Overrides:
`[mustShowContextMenu](../PresentationElement.html#mustShowContextMenu())` in class `[PresentationElement](../PresentationElement.html)`
intersects
public boolean intersects(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Description copied from class: `[PresentationElement](../PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))`
checks whether object intersects with given rectangle
Overrides:
`[intersects](ShapeElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[ShapeElement](ShapeElement.html)`
Returns:
true if object and rectangle intersects
coversPoint
public boolean coversPoint(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Description copied from class: `[PresentationElement](../PresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))`
checks if object covers provided point
Overrides:
`coversPoint` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
Returns:
true if object covers this point
adjustBoundsBeforeChange
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) adjustBoundsBeforeChange([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rec,
 boolean autosizeOperation,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)> movedTogether)
Description copied from class: `[PresentationElement](../PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection))`
Validate bounds before bounds change operation
Overrides:
`adjustBoundsBeforeChange` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
canAddInstance
public boolean canAddInstance([PresentationElement](../PresentationElement.html) symbol)
Description copied from class: `[PresentationElement](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Object view has no children.
Overrides:
`canAddInstance` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
getEncapsulatedClassifier
public [EncapsulatedClassifier](../../../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html) getEncapsulatedClassifier()
Specified by:
`getEncapsulatedClassifier` in interface `com.nomagic.magicdraw.uml.symbols.shapes.PortOwner`
getEncapsulatedClassifierProvider
public [TypedElement](../../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html) getEncapsulatedClassifierProvider()
Specified by:
`getEncapsulatedClassifierProvider` in interface `com.nomagic.magicdraw.uml.symbols.shapes.PortOwner`
createSmartListenerConfig
protected void createSmartListenerConfig([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)
Overrides:
`createSmartListenerConfig` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
getDefaultDimension
protected [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) getDefaultDimension()
Overrides:
`[getDefaultDimension](ShapeElement.html#getDefaultDimension())` in class `[ShapeElement](ShapeElement.html)`
preferredSizeIgnoringOrientation
protected void preferredSizeIgnoringOrientation([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)
Overrides:
`preferredSizeIgnoringOrientation` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
minimumOrMinimumShrinkableDimension
protected void minimumOrMinimumShrinkableDimension([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size)
Overrides:
`[minimumOrMinimumShrinkableDimension](ShapeElement.html#minimumOrMinimumShrinkableDimension(java.awt.Dimension))` in class `[ShapeElement](ShapeElement.html)`
minimumSizeForShrinkingIgnoringOrientation
public void minimumSizeForShrinkingIgnoringOrientation([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size,
 int locationX,
 int locationY)
Overrides:
`minimumSizeForShrinkingIgnoringOrientation` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
canMoveChildOutside
protected boolean canMoveChildOutside([PresentationElement](../PresentationElement.html) element)
Overrides:
`canMoveChildOutside` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
internalLayoutChildren
public void internalLayoutChildren(boolean calculatePrefSize)
Overrides:
`internalLayoutChildren` in class `com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView`
providesVerticalCenterline
public boolean providesVerticalCenterline()
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Indicates if this shape can provide a vertical centerline for other shapes to snap.
Specified by:
`providesVerticalCenterline` in interface `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Overrides:
`[providesVerticalCenterline](ShapeElement.html#providesVerticalCenterline())` in class `[ShapeElement](ShapeElement.html)`
Returns:
true if this shape provides vertical centerline, false otherwise.
providesHorizontalCenterline
public boolean providesHorizontalCenterline()
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Indicates if this shape can provide a horizontal centerline for other shapes to snap.
Specified by:
`providesHorizontalCenterline` in interface `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Overrides:
`[providesHorizontalCenterline](ShapeElement.html#providesHorizontalCenterline())` in class `[ShapeElement](ShapeElement.html)`
Returns:
true if this shape provides horizontal centerline, false otherwise.
isHorizontalCenterlineProvider
public boolean isHorizontalCenterlineProvider()
Description copied from class: `[ShapeElement](ShapeElement.html#isHorizontalCenterlineProvider())`
Indicates whether this shape provides horizontal center-lines to other shapes.
Overrides:
`[isHorizontalCenterlineProvider](ShapeElement.html#isHorizontalCenterlineProvider())` in class `[ShapeElement](ShapeElement.html)`
Returns:
true if this shape provides horizontal center-lines, false otherwise.
isVerticalCenterlineProvider
public boolean isVerticalCenterlineProvider()
Description copied from class: `[ShapeElement](ShapeElement.html#isVerticalCenterlineProvider())`
Indicates whether this shape provides vertical center-lines to other shapes.
Overrides:
`[isVerticalCenterlineProvider](ShapeElement.html#isVerticalCenterlineProvider())` in class `[ShapeElement](ShapeElement.html)`
Returns:
true if this shape provides vertical center lines, false otherwise.
movePathElement
protected void movePathElement([PathElement](../paths/PathElement.html) link,
 @CheckForNull
 [PathConnector](../paths/PathConnector.html) requestor)
Description copied from class: `[PathConnector](../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector))`
Calculates position of a path element.
Overrides:
`[movePathElement](ShapeElement.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector))` in class `[ShapeElement](ShapeElement.html)`
Parameters:
`link` - element which position will be calculated.
`requestor` - the requestor of this path moving. Implementations may check to avoid endless loops.
getStereotypesToDisplay
protected com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView.StereotypeDisplayData getStereotypesToDisplay()
Overrides:
`getStereotypesToDisplay` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
Returns:
stereotypes to display on this symbol
sSetParent
public void sSetParent([PresentationElement](../PresentationElement.html) parent)
Description copied from class: `[PresentationElement](../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Sets parent for this view.
 For adding symbols to other symbols use
 [`PresentationElement.addPresentationElement(PresentationElement)`](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)) or
 [`PresentationElement.sAddPresentationElement(PresentationElement)`](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))}
Overrides:
`[sSetParent](../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`parent` - parent view
dispose
public void dispose()
Description copied from class: `[PresentationElement](../PresentationElement.html#dispose())`
disposes ends of links when link is deleted
Specified by:
`[dispose](../../BaseElement.html#dispose())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`dispose` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
atInsert
public void atInsert()
Description copied from class: `[PresentationElement](../PresentationElement.html#atInsert())`
Invalidates object at insert
Specified by:
`[atInsert](../../BaseElement.html#atInsert())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`atInsert` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
internalSpecificUpdate
protected void internalSpecificUpdate()
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
Specific to every shape and model element update operation. Must be overridden in subclasses if you need to do specific tasks.
 !!! Important - all resizing, paths moving and so on is done in updatePresentationElement and should not be done in specific update.
Overrides:
`internalSpecificUpdate` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
See Also:
`AbstractHeaderShapeView.internalUpdatePresentationElement()`
snapsToCenterlines
public boolean snapsToCenterlines()
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Indicates if this shape can be snapped to centerlines.
Specified by:
`snapsToCenterlines` in interface `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Overrides:
`[snapsToCenterlines](ShapeElement.html#snapsToCenterlines())` in class `[ShapeElement](ShapeElement.html)`
Returns:
true if this shape can be snapped to centerlines, false otherwise.
getFrameElementBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getFrameElementBounds()
calculateFrameElementBounds
public void calculateFrameElementBounds()
hasBoundaryDetails
public boolean hasBoundaryDetails()
Returns true if frame carries details on its border.
 If the frame is plain, false is returned.
Returns:
true if frame carries details on border, false otherwise.
layoutFrameIfSet
public void layoutFrameIfSet()
Specified by:
`layoutFrameIfSet` in interface `com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape`
layoutFrame
public void layoutFrame()
getHumanType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHumanType()
Description copied from class: `[PresentationElement](../PresentationElement.html#getHumanType())`
Returns human representation of the data type
Specified by:
`[getHumanType](../../BaseElement.html#getHumanType())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`[getHumanType](../PresentationElement.html#getHumanType())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
the name of the data
getHumanName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHumanName()
Description copied from class: `[PresentationElement](../PresentationElement.html#getHumanName())`
Returns human representation of the data type
Specified by:
`[getHumanName](../../BaseElement.html#getHumanName())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`[getHumanName](../PresentationElement.html#getHumanName())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
the name of the data
internalPostUpdatePresentationElement
protected void internalPostUpdatePresentationElement()
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
Subclasses may override this method and do some actions after specific update and resizing are executed.
 Implementation is empty here.
Overrides:
`internalPostUpdatePresentationElement` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
See Also:
`AbstractHeaderShapeView.internalUpdatePresentationElement()`
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
getHeaderView
public com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderView getHeaderView()
Overrides:
`getHeaderView` in class `com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView`
isSetAsDiagramFrame
public boolean isSetAsDiagramFrame()
Specified by:
`isSetAsDiagramFrame` in interface `com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape`
isOwningMode
public boolean isOwningMode()
Specified by:
`isOwningMode` in interface `com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.shapes</a></div>
<h1 class="title" title="Class DiagramFrameView">Class DiagramFrameView</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</a>
<div class="inheritance"><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameView</div>
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
<dd><code>com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape</code>, <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code>com.nomagic.magicdraw.uml.CompartmentSupport</code>, <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.CompartmentContainer</code>, <code>com.nomagic.magicdraw.uml.symbols.CompartmentOwner</code>, <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code>, <code>com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.PortOwner</code>, <code>com.nomagic.magicdraw.uml.symbols.shapes.QualifiedNameLabelOwner</code>, <code><a href="StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code>, <code>com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider</code>, <code>com.nomagic.magicdraw.uml.symbols.Wrapable</code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramFrameView</span>
<span class="extends-implements">extends com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView
implements com.nomagic.magicdraw.uml.symbols.shapes.PortOwner, com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape</span></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_TYPES_FOR_PORTS_ON_FRAME">DIAGRAM_TYPES_FOR_PORTS_ON_FRAME</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView">Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</h3>
<code>SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY, SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODE_IMAGE_AND_STEREOTYPES, SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODE_STEREOTYPES, SECONDARY_IMAGE_AND_STEREOTYPE_DISPLAY_MODES</code></div>
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
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape">Fields inherited from interface com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape</h3>
<code>FRAME_DISTANCE_FROM_EDGE</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.QualifiedNameLabelOwner">Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.QualifiedNameLabelOwner</h3>
<code>QNAME_DISPLAY_MODE_ABOVE_NAME, QNAME_DISPLAY_MODE_BELOW_NAME, QNAME_DISPLAY_MODE_DO_NOT_DISPLAY, QNAME_DISPLAY_MODE_MERGE_WITH_NAME, QNAME_DISPLAY_MODES</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.StereotypesDisplayModeOwner">Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.<a href="StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></h3>
<code><a href="StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL">DSL_STEREOTYPE_DISPLAY_MODE_ALL</a>, <a href="StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST">DSL_STEREOTYPE_DISPLAY_MODE_LAST</a>, <a href="StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE">DSL_STEREOTYPE_DISPLAY_MODE_NONE</a>, <a href="StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES">DSL_STEREOTYPE_DISPLAY_MODES</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES">STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON">STEREOTYPE_DISPLAY_MODE_ICON</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE">STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT">STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT">STEREOTYPE_DISPLAY_MODE_TEXT</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON">STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES">STEREOTYPES_DISPLAY_MODES</a>, <a href="StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE">STEREOTYPES_DISPLAY_MODES_SIMPLE</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DiagramFrameView</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement)">DiagramFrameView</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">adjustBoundsBeforeChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rec,
 boolean autosizeOperation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Validate bounds before bounds change operation</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#atInsert()">atInsert</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invalidates object at insert</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateFrameElementBounds()">calculateFrameElementBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddInstance</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Object view has no children.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canFill()">canFill</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canMoveChildOutside(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canMoveChildOutside</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">coversPoint</a><wbr/>(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">checks if object covers provided point</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">disposes ends of links when link is deleted</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCornerArcSize()">getCornerArcSize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultDimension()">getDefaultDimension</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model element of this presentation element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEncapsulatedClassifier()">getEncapsulatedClassifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEncapsulatedClassifierProvider()">getEncapsulatedClassifierProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFillColor()">getFillColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns fill color</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFrameElementBounds()">getFrameElementBounds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderView</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHeaderView()">getHeaderView</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHumanName()">getHumanName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns human representation of the data type</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHumanType()">getHumanType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns human representation of the data type</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns parent to which this symbol delegates style attributes related functionality.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourceID()">getResourceID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView.StereotypeDisplayData</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotypesToDisplay()">getStereotypesToDisplay</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasBoundaryDetails()">hasBoundaryDetails</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if frame carries details on its border.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalLayoutChildren(boolean)">internalLayoutChildren</a><wbr/>(boolean calculatePrefSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalPostUpdatePresentationElement()">internalPostUpdatePresentationElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Subclasses may override this method and do some actions after specific update and resizing are executed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSpecificUpdate()">internalSpecificUpdate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Specific to every shape and model element update operation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a><wbr/>(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">checks whether object intersects with given rectangle</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHorizontalCenterlineProvider()">isHorizontalCenterlineProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates whether this shape provides horizontal center-lines to other shapes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOwningMode()">isOwningMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSetAsDiagramFrame()">isSetAsDiagramFrame</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isVerticalCenterlineProvider()">isVerticalCenterlineProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates whether this shape provides vertical center-lines to other shapes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#layoutFrame()">layoutFrame</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#layoutFrameIfSet()">layoutFrameIfSet</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#minimumOrMinimumShrinkableDimension(java.awt.Dimension)">minimumOrMinimumShrinkableDimension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#minimumSizeForShrinkingIgnoringOrientation(java.awt.Dimension,int,int)">minimumSizeForShrinkingIgnoringOrientation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size,
 int locationX,
 int locationY)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> link,
 <a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> requestor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates position of a path element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#mustShowContextMenu()">mustShowContextMenu</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#preferredSizeIgnoringOrientation(java.awt.Dimension,int,int)">preferredSizeIgnoringOrientation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#providesHorizontalCenterline()">providesHorizontalCenterline</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if this shape can provide a horizontal centerline for other shapes to snap.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#providesVerticalCenterline()">providesVerticalCenterline</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if this shape can provide a vertical centerline for other shapes to snap.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#selfSpecificHeaderShapeDraw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">selfSpecificHeaderShapeDraw</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#snapsToCenterlines()">snapsToCenterlines</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if this shape can be snapped to centerlines.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets parent for this view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#useParentStyle()">useParentStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Does this element uses parent style or has it's own?</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</h3>
<code>canSuppressContent, getBooleanCompartmentPropertyValue, getConstraintAndTaggedValueAlignment, getConstraintTextMode, getDefaultElementStereotypeToHeader, getDSLStereotypesDisplayMode, getElementNumberDisplayMode, getElementPropertiesCompartmentView, getMiddlePointByIcon, getQNameDisplayMode, getSecondaryImageAndStereotypeDisplayMode, getStereotypeLabel, getStereotypesDisplayMode, internalApplyProperties, internalBeforeUpdate, internalSilentApply, isShowDerivedSign, isShowElementProperties, isShowIcon, isShowNumberTagName, isShowRakeIcon, isShowRakeSymbol, isShowTaggedValues, isShowType, propertyChange, recursiveAutosize, setConstraintAndTaggedValueAlignment, setConstraints, setConstraintTextMode, setDSLStereotypesDisplayMode, setElementNumberDisplayMode, setQNameDisplayMode, setSecondaryImageAndStereotypeDisplayMode, setShowConstraints, setShowDerivedSign, setShowElementProperties, setShowIcon, setShowNumberTagName, setShowTaggedValues, setShowType, setStereotype, setStereotypesDisplayMode, setTaggedValues, sSetConstraintAndTaggedValueAlignment, sSetConstraintTextMode, sSetDSLStereotypesDisplayMode, sSetElement, sSetElementNumberDisplayMode, sSetQNameDisplayMode, sSetSecondaryImageAndStereotypeDisplayMode, sSetShowConstraints, sSetShowDerivedSign, sSetShowElementProperties, sSetShowIcon, sSetShowNumberTagName, sSetShowTaggedValues, sSetShowType, sSetStereotypesDisplayMode, updateBorderVisibility, updateName</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</h3>
<code>addCompartment, addCompartment, addPresentationElement, applyCompartmentsStyle, areBoxCompartmentsSuppressed, askDeleteDataConfirmation, asPresentationElement, autosizeShapesOnEdge, canAddChild, canChangeParent, canHideBorder, childrenBoundsForReshape, clone, createBoundsShape, createCompartmentElements, createStateForUpdateOperation, doInternalLayoutAdditionCompartment, doInternalLayoutChildren, getAdditionalCompartment, getAdditionalCompartmentContainer, getAdditionalCompartmentDescriptor, getAdditionalCompartmentInsets, getAdditionalCompartmentToLayout, getAdditionalRenderersToNotifyOnPropertiesChange, getChildrenBoundsForPreferredBounds, getChildrenInsets, getCollections, getCompartmentByID, getCompartmentIDs, getCompartments, getCompartmentsIDs, getCompartmentStyleDelegate, getConfiguredPreferredSizeForAutosize, getHeaderMaxYForShrinkableShape, getHeaderVerticalPositionForLayout, getLastHeaderShapeElementBottom, getMainCompartmentContainer, getName, getPreferredDimensionForAutosize, hasManipulatedChildrenIncludingIndirect, hasSharedModelElement, internalAddIndirectManipulatedChildrenRect, internalGetHeaderInsets, internalGetIndirectManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalPostSpecificUpdate, internalSetCollections, isBorderVisible, isChildLayoutable, isChildMovable, isMakePreferredSizeAfterPropertiesChange, isWrapEnabled, iterateCompartmentDelegates, makePreferredSizeAfterPropertiesChange, makePreferredSizeAfterPropertiesChange, onChildEdgeChange, paintSelf, removeCompartment, removeCompartment, removePresentationElement, setCollections, setCompartmentSuppressed, setHeaderObject, setMakePreferredSizeAfterPropertiesChange, setReshapeMode, setVisibleElements, setWrapEnabled, sSetCompartmentSuppressed, sSetName, sSetWrapEnabled, updateChildrenVisibility, updateCompartmentsVisibility</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</h3>
<code>addExtraChildrenPrefSizePadding, autosize, autosizeAndResizeParent, calculateMinY, calculateOvalShapePreferredSize, correctChildrenVector, editName, getAdditionalHeaderHeightForPreferredBounds, getHeaderBoundsForPreferredBounds, getHeaderDistanceFromTopForOvalShape, getHeaderInsets, getHeaderObject, getHeaderVerticalPosition, getNameLabel, getOvalShapeAvailableWidth, getPreferredBounds, getPresentationElementAt, getProxyPresentationElementsStream, internalGetHeaderBoundsForPreferredBounds, internalPreSpecificUpdate, internalUpdatePresentationElement, invalidate, isContentHidden, isHeaderOrientationVertical, isOvalShape, isParentShowsProxy, minimumDimension, minimumDimensionForShrinking, minimumSizeIgnoringOrientation, paintChildren, preferredDimension, setHeaderVerticalPosition, setName, setTextEditable, sSetAutosize, sSetHeaderVerticalPosition, switchWidthHeightIfVerticalOrientation</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</h3>
<code>addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, checkShowsProxy, clearShowsProxy, constructLayoutHelper, getChildrenBounds, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getRemovableChildren, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAppendChildRect, internalGetChildAt, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildrenBackground, prefDimensionByManipulatedChildren, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></h3>
<code><a href="ShapeElement.html#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addBreakPoints</a>, <a href="ShapeElement.html#adjustBounds(java.awt.Rectangle)">adjustBounds</a>, <a href="ShapeElement.html#adjustOnEdge()">adjustOnEdge</a>, <a href="ShapeElement.html#adjustOnEdge(java.awt.Rectangle,int,int,int)">adjustOnEdge</a>, <a href="ShapeElement.html#adjustOnEdgeChildren()">adjustOnEdgeChildren</a>, <a href="ShapeElement.html#autosize()">autosize</a>, <a href="ShapeElement.html#calculateAdjustOnEdgeLocation(java.awt.Rectangle)">calculateAdjustOnEdgeLocation</a>, <a href="ShapeElement.html#calculateAndGetMinimumShrinkingDimension(int,int)">calculateAndGetMinimumShrinkingDimension</a>, <a href="ShapeElement.html#calculateAndGetPreferredDimension()">calculateAndGetPreferredDimension</a>, <a href="ShapeElement.html#calculateEdge()">calculateEdge</a>, <a href="ShapeElement.html#calculateMinimumDimension()">calculateMinimumDimension</a>, <a href="ShapeElement.html#calculateOnEdgeBounds()">calculateOnEdgeBounds</a>, <a href="ShapeElement.html#calculatePreferredDimension()">calculatePreferredDimension</a>, <a href="ShapeElement.html#calculatePreferredDimension(int,int)">calculatePreferredDimension</a>, <a href="ShapeElement.html#canBeAutosized()">canBeAutosized</a>, <a href="ShapeElement.html#canHavePaths()">canHavePaths</a>, <a href="ShapeElement.html#clearOldRect()">clearOldRect</a>, <a href="ShapeElement.html#edgeChanged()">edgeChanged</a>, <a href="ShapeElement.html#ensureDimension(boolean)">ensureDimension</a>, <a href="ShapeElement.html#ensurePreferredDimensionIfShrinkable()">ensurePreferredDimensionIfShrinkable</a>, <a href="ShapeElement.html#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)">ensurePreferredDimensionIfShrinkable</a>, <a href="ShapeElement.html#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)">findFreePlaceForShapeOnBorder</a>, <a href="ShapeElement.html#getBorderElementMargin()">getBorderElementMargin</a>, <a href="ShapeElement.html#getBounds()">getBounds</a>, <a href="ShapeElement.html#getCenterlineableInnerParts(int)">getCenterlineableInnerParts</a>, <a href="ShapeElement.html#getDimensionForShrinking(int,int)">getDimensionForShrinking</a>, <a href="ShapeElement.html#getEdgeLine(int)">getEdgeLine</a>, <a href="ShapeElement.html#getFixedConnectionPoints()">getFixedConnectionPoints</a>, <a href="ShapeElement.html#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)">getHeaderInsetReduce</a>, <a href="ShapeElement.html#getInsetsForOnEdgeShapes()">getInsetsForOnEdgeShapes</a>, <a href="ShapeElement.html#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="ShapeElement.html#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)">getIntersection</a>, <a href="ShapeElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="ShapeElement.html#getLoadedDimension()">getLoadedDimension</a>, <a href="ShapeElement.html#getMiddlePoint()">getMiddlePoint</a>, <a href="ShapeElement.html#getMiddlePoint(java.awt.Point)">getMiddlePoint</a>, <a href="ShapeElement.html#getMiddlePointX()">getMiddlePointX</a>, <a href="ShapeElement.html#getMiddlePointX(java.awt.Point)">getMiddlePointX</a>, <a href="ShapeElement.html#getMiddlePointY()">getMiddlePointY</a>, <a href="ShapeElement.html#getMiddlePointY(java.awt.Point)">getMiddlePointY</a>, <a href="ShapeElement.html#getMinimumDimension()">getMinimumDimension</a>, <a href="ShapeElement.html#getNearestEdge(int,int)">getNearestEdge</a>, <a href="ShapeElement.html#getNearestEdge(java.awt.Rectangle)">getNearestEdge</a>, <a href="ShapeElement.html#getNeedAutosizeFlag()">getNeedAutosizeFlag</a>, <a href="ShapeElement.html#getNotCopyBounds()">getNotCopyBounds</a>, <a href="ShapeElement.html#getOnEdge()">getOnEdge</a>, <a href="ShapeElement.html#getOnEdgeCornerDistance()">getOnEdgeCornerDistance</a>, <a href="ShapeElement.html#getOnEdgePosition()">getOnEdgePosition</a>, <a href="ShapeElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="ShapeElement.html#getReshapeMode()">getReshapeMode</a>, <a href="ShapeElement.html#getSizeForDrawing()">getSizeForDrawing</a>, <a href="ShapeElement.html#getSuspendShapeAutoResizeMode()">getSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#hasManipulator()">hasManipulator</a>, <a href="ShapeElement.html#initialize()">initialize</a>, <a href="ShapeElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a>, <a href="ShapeElement.html#isAutosized()">isAutosized</a>, <a href="ShapeElement.html#isCenterlineInner()">isCenterlineInner</a>, <a href="ShapeElement.html#isOnEdge()">isOnEdge</a>, <a href="ShapeElement.html#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isShapeOnEdge</a>, <a href="ShapeElement.html#isShrinkable()">isShrinkable</a>, <a href="ShapeElement.html#isSnapShapesOnBorderToGrid()">isSnapShapesOnBorderToGrid</a>, <a href="ShapeElement.html#isSnapToGrid()">isSnapToGrid</a>, <a href="ShapeElement.html#isUseFixedConnectionPoints()">isUseFixedConnectionPoints</a>, <a href="ShapeElement.html#layoutChildren()">layoutChildren</a>, <a href="ShapeElement.html#maximumDimension(java.awt.Dimension)">maximumDimension</a>, <a href="ShapeElement.html#moveLinksToSelf()">moveLinksToSelf</a>, <a href="ShapeElement.html#movePathElements()">movePathElements</a>, <a href="ShapeElement.html#needAdjustToMaximumDimension()">needAdjustToMaximumDimension</a>, <a href="ShapeElement.html#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a>, <a href="ShapeElement.html#resetCalculatePreferredRegardingChildren()">resetCalculatePreferredRegardingChildren</a>, <a href="ShapeElement.html#setAutosize(boolean)">setAutosize</a>, <a href="ShapeElement.html#setBorderElementMargin(java.lang.String)">setBorderElementMargin</a>, <a href="ShapeElement.html#setCalculatePreferredRegardingChildren(boolean)">setCalculatePreferredRegardingChildren</a>, <a href="ShapeElement.html#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)">setLoadedDimension</a>, <a href="ShapeElement.html#setMinimumDimension(int,int)">setMinimumDimension</a>, <a href="ShapeElement.html#setNeedAutosizeFlag(byte)">setNeedAutosizeFlag</a>, <a href="ShapeElement.html#setOldRect(java.awt.Rectangle)">setOldRect</a>, <a href="ShapeElement.html#setOnEdge(int)">setOnEdge</a>, <a href="ShapeElement.html#setPreferredDimension(int,int)">setPreferredDimension</a>, <a href="ShapeElement.html#setSnapShapesOnBorderToGrid(boolean)">setSnapShapesOnBorderToGrid</a>, <a href="ShapeElement.html#setSuspendShapeAutoResizeMode(java.lang.String)">setSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#setUseFixedConnectionPoints(boolean)">setUseFixedConnectionPoints</a>, <a href="ShapeElement.html#shouldDrawShadow()">shouldDrawShadow</a>, <a href="ShapeElement.html#simpleSetBounds(int,int,int,int,boolean)">simpleSetBounds</a>, <a href="ShapeElement.html#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a>, <a href="ShapeElement.html#sSetBorderElementMargin(java.lang.String)">sSetBorderElementMargin</a>, <a href="ShapeElement.html#sSetBounds(java.awt.Rectangle)">sSetBounds</a>, <a href="ShapeElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)">sSetSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a>, <a href="ShapeElement.html#toString()">toString</a>, <a href="ShapeElement.html#updateLater()">updateLater</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addConnectedPathElement</a>, <a href="../paths/PathConnector.html#disposeConnectedPaths()">disposeConnectedPaths</a>, <a href="../paths/PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">findSymbolForEnd</a>, <a href="../paths/PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)">findSymbolForEnd</a>, <a href="../paths/PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">getConnectedPathElement</a>, <a href="../paths/PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="../paths/PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getPreferredArrowLength()">getPreferredArrowLength</a>, <a href="../paths/PathConnector.html#isShowsProxy()">isShowsProxy</a>, <a href="../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)">movePathElement</a>, <a href="../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">removeConnectedPathElement</a>, <a href="../paths/PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sAddConnectedPathElement</a>, <a href="../paths/PathConnector.html#selectPathsForMoving(java.util.List)">selectPathsForMoving</a>, <a href="../paths/PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a>, <a href="../paths/PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a>, <a href="../paths/PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sRemoveConnectedPathElement</a>, <a href="../paths/PathConnector.html#sSetConnectedPathElements(java.util.List)">sSetConnectedPathElements</a>, <a href="../paths/PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible()">supportsVisibleConnectedPathElementsIfSelfInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a>, <a href="../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBounds</a>, <a href="../PresentationElement.html#alwaysShowTooltip()">alwaysShowTooltip</a>, <a href="../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">applyProperties</a>, <a href="../PresentationElement.html#atInsertChildren()">atInsertChildren</a>, <a href="../PresentationElement.html#autosizeAndResizeManipulatedParent()">autosizeAndResizeManipulatedParent</a>, <a href="../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">beforeDelete</a>, <a href="../PresentationElement.html#boundsChanged()">boundsChanged</a>, <a href="../PresentationElement.html#boundsChanged(java.awt.Rectangle)">boundsChanged</a>, <a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../PresentationElement.html#canBeDisposedOnUpdate()">canBeDisposedOnUpdate</a>, <a href="../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeElementOwner</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">changeProperties</a>, <a href="../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a>, <a href="../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">checkProxyVisibility</a>, <a href="../PresentationElement.html#childrenForMoving()">childrenForMoving</a>, <a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)">collectSubShowingPresentationElements</a>, <a href="../PresentationElement.html#coversPoint(int,int)">coversPoint</a>, <a href="../PresentationElement.html#createFillStrategy()">createFillStrategy</a>, <a href="../PresentationElement.html#createPresentationElementStyle()">createPresentationElementStyle</a>, <a href="../PresentationElement.html#createPropertyChangeListener()">createPropertyChangeListener</a>, <a href="../PresentationElement.html#disposeChildren()">disposeChildren</a>, <a href="../PresentationElement.html#disposePropertyChangeListener()">disposePropertyChangeListener</a>, <a href="../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a>, <a href="../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawBackground</a>, <a href="../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbol</a>, <a href="../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbolBackground</a>, <a href="../PresentationElement.html#dynamicFillColor()">dynamicFillColor</a>, <a href="../PresentationElement.html#dynamicLineColor()">dynamicLineColor</a>, <a href="../PresentationElement.html#dynamicLineWidth()">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicLineWidth(int)">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicPaintShadow()">dynamicPaintShadow</a>, <a href="../PresentationElement.html#dynamicStroke()">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(int)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)">dynamicStyleFillColor</a>, <a href="../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)">dynamicStyleLineColor</a>, <a href="../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)">dynamicStyleTextColor</a>, <a href="../PresentationElement.html#dynamicStyleTransparency()">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)">dynamicStyleValue</a>, <a href="../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">dynamicTextAlignment</a>, <a href="../PresentationElement.html#dynamicTextColor()">dynamicTextColor</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOwnerForChildElement</a>, <a href="../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a>, <a href="../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">findPresentationElement</a>, <a href="../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../PresentationElement.html#generateID()">generateID</a>, <a href="../PresentationElement.html#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>, <a href="../PresentationElement.html#getActualElement()">getActualElement</a>, <a href="../PresentationElement.html#getAssignableModelElementsClasses()">getAssignableModelElementsClasses</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getBoundsToRepaint()">getBoundsToRepaint</a>, <a href="../PresentationElement.html#getBoundsWithChildrenOnEdge()">getBoundsWithChildrenOnEdge</a>, <a href="../PresentationElement.html#getCenterlinePoint()">getCenterlinePoint</a>, <a href="../PresentationElement.html#getCenterlinePointX()">getCenterlinePointX</a>, <a href="../PresentationElement.html#getCenterlinePointY()">getCenterlinePointY</a>, <a href="../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)">getChildPresentationElementForContextMenu</a>, <a href="../PresentationElement.html#getChildrenWithSymbolProperties()">getChildrenWithSymbolProperties</a>, <a href="../PresentationElement.html#getConfiguration()">getConfiguration</a>, <a href="../PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="../PresentationElement.html#getDiagramSurface()">getDiagramSurface</a>, <a href="../PresentationElement.html#getDrawComparator()">getDrawComparator</a>, <a href="../PresentationElement.html#getDynamicConfigurations()">getDynamicConfigurations</a>, <a href="../PresentationElement.html#getDynamicStyleOwner()">getDynamicStyleOwner</a>, <a href="../PresentationElement.html#getEffectiveStyleDelegate()">getEffectiveStyleDelegate</a>, <a href="../PresentationElement.html#getEffectiveStyleOwner()">getEffectiveStyleOwner</a>, <a href="../PresentationElement.html#getElementsForRelationshipConnecting()">getElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementToConnectRelationship</a>, <a href="../PresentationElement.html#getFont()">getFont</a>, <a href="../PresentationElement.html#getFontHeight()">getFontHeight</a>, <a href="../PresentationElement.html#getFontRenderContext()">getFontRenderContext</a>, <a href="../PresentationElement.html#getLineColor()">getLineColor</a>, <a href="../PresentationElement.html#getLineWidth()">getLineWidth</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getManipulationBounds(java.awt.Point)">getManipulationBounds</a>, <a href="../PresentationElement.html#getModelElement()">getModelElement</a>, <a href="../PresentationElement.html#getModelElementsForRelationshipConnecting()">getModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">getModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#getModelElementToMove()">getModelElementToMove</a>, <a href="../PresentationElement.html#getNotZoomedTolerance()">getNotZoomedTolerance</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getOwnStyleDelegate()">getOwnStyleDelegate</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="../PresentationElement.html#getPresentationElementAt(int)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementCount()">getPresentationElementCount</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getProjectImpl()">getProjectImpl</a>, <a href="../PresentationElement.html#getProperty(java.lang.String)">getProperty</a>, <a href="../PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="../PresentationElement.html#getPropertyManagerName()">getPropertyManagerName</a>, <a href="../PresentationElement.html#getRenderer()">getRenderer</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#getStyle()">getStyle</a>, <a href="../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSymbolRenderer</a>, <a href="../PresentationElement.html#getTextColor()">getTextColor</a>, <a href="../PresentationElement.html#getTolerance()">getTolerance</a>, <a href="../PresentationElement.html#getVisibility()">getVisibility</a>, <a href="../PresentationElement.html#getVisiblePresentationElements()">getVisiblePresentationElements</a>, <a href="../PresentationElement.html#handleModelDelete()">handleModelDelete</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#initializeAndAutosize()">initializeAndAutosize</a>, <a href="../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">internalCreatePropertyChangeListener</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a>, <a href="../PresentationElement.html#internalGetSpecificFont()">internalGetSpecificFont</a>, <a href="../PresentationElement.html#internalGetSpecificTextColor()">internalGetSpecificTextColor</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalSnapToGrid(float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#intersects(int,int,int,int)">intersects</a>, <a href="../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildVisible</a>, <a href="../PresentationElement.html#isCreateElementListener()">isCreateElementListener</a>, <a href="../PresentationElement.html#isDetectable()">isDetectable</a>, <a href="../PresentationElement.html#isDisposed()">isDisposed</a>, <a href="../PresentationElement.html#isLayouting()">isLayouting</a>, <a href="../PresentationElement.html#isMovableByMoveManager()">isMovableByMoveManager</a>, <a href="../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNotNull</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isParentOf</a>, <a href="../PresentationElement.html#isPreserveProportionsWhenGrowing()">isPreserveProportionsWhenGrowing</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#isShowElementTypeAsLabel()">isShowElementTypeAsLabel</a>, <a href="../PresentationElement.html#isSortable()">isSortable</a>, <a href="../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">isSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#isTextEditable()">isTextEditable</a>, <a href="../PresentationElement.html#isUseFillColor()">isUseFillColor</a>, <a href="../PresentationElement.html#isUseFillColorByProperty()">isUseFillColorByProperty</a>, <a href="../PresentationElement.html#isUseGradientForFill()">isUseGradientForFill</a>, <a href="../PresentationElement.html#isVisible()">isVisible</a>, <a href="../PresentationElement.html#isVisibleInDiagram()">isVisibleInDiagram</a>, <a href="../PresentationElement.html#isVisibleOrShrunken()">isVisibleOrShrunken</a>, <a href="../PresentationElement.html#movePathElementsRecursively()">movePathElementsRecursively</a>, <a href="../PresentationElement.html#notifyCreated()">notifyCreated</a>, <a href="../PresentationElement.html#notifyDiagramFrameSizeChange()">notifyDiagramFrameSizeChange</a>, <a href="../PresentationElement.html#notifyRepaintManager(boolean)">notifyRepaintManager</a>, <a href="../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildAdd</a>, <a href="../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildRemove</a>, <a href="../PresentationElement.html#onDiagramSurfaceSet()">onDiagramSurfaceSet</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#onFontChange()">onFontChange</a>, <a href="../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">onParentChange</a>, <a href="../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornments</a>, <a href="../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornmentsBackground</a>, <a href="../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenAndAdornments</a>, <a href="../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelfBackground</a>, <a href="../PresentationElement.html#preDisposeOnUpdate()">preDisposeOnUpdate</a>, <a href="../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)">prepareForLineDrawing</a>, <a href="../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)">prepareForTextDrawing</a>, <a href="../PresentationElement.html#recreateListeners()">recreateListeners</a>, <a href="../PresentationElement.html#registerInSortManager()">registerInSortManager</a>, <a href="../PresentationElement.html#rememberBounds()">rememberBounds</a>, <a href="../PresentationElement.html#rememberBounds(java.awt.Rectangle)">rememberBounds</a>, <a href="../PresentationElement.html#removeFromSortManager()">removeFromSortManager</a>, <a href="../PresentationElement.html#removeItSelfOnUpdate()">removeItSelfOnUpdate</a>, <a href="../PresentationElement.html#resizeParent()">resizeParent</a>, <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sAddPresentationElement</a>, <a href="../PresentationElement.html#selectChildrenForMoving()">selectChildrenForMoving</a>, <a href="../PresentationElement.html#selectObjectsForMoving()">selectObjectsForMoving</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setBounds(int,int,int,int)">setBounds</a>, <a href="../PresentationElement.html#setCreateElementListener(boolean)">setCreateElementListener</a>, <a href="../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a>, <a href="../PresentationElement.html#setFont(java.awt.Font)">setFont</a>, <a href="../PresentationElement.html#setLayouting(boolean)">setLayouting</a>, <a href="../PresentationElement.html#setLineColor(java.awt.Color)">setLineColor</a>, <a href="../PresentationElement.html#setLineWidth(int)">setLineWidth</a>, <a href="../PresentationElement.html#setLoadedVisibility(boolean)">setLoadedVisibility</a>, <a href="../PresentationElement.html#setLocation(int,int)">setLocation</a>, <a href="../PresentationElement.html#setLocation(java.awt.Point)">setLocation</a>, <a href="../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">setModelElement</a>, <a href="../PresentationElement.html#setNeedRecreateListeners(boolean)">setNeedRecreateListeners</a>, <a href="../PresentationElement.html#setPropertyManagerName(java.lang.String)">setPropertyManagerName</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#setSize(int,int)">setSize</a>, <a href="../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)">setSize</a>, <a href="../PresentationElement.html#setSize(java.awt.Dimension)">setSize</a>, <a href="../PresentationElement.html#setTextColor(java.awt.Color)">setTextColor</a>, <a href="../PresentationElement.html#setUseFillColor(boolean)">setUseFillColor</a>, <a href="../PresentationElement.html#setVisible(boolean)">setVisible</a>, <a href="../PresentationElement.html#silentApply()">silentApply</a>, <a href="../PresentationElement.html#silentApply(boolean)">silentApply</a>, <a href="../PresentationElement.html#simpleSetBounds(int,int,int,int)">simpleSetBounds</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Point,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapViewToGrid(float)">snapViewToGrid</a>, <a href="../PresentationElement.html#sortObjectsByX(java.util.List)">sortObjectsByX</a>, <a href="../PresentationElement.html#sortObjectsByY(java.util.List)">sortObjectsByY</a>, <a href="../PresentationElement.html#sSetBounds(int,int,int,int)">sSetBounds</a>, <a href="../PresentationElement.html#sSetLocation(int,int)">sSetLocation</a>, <a href="../PresentationElement.html#sSetLocation(java.awt.Point)">sSetLocation</a>, <a href="../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">sSetModelElement</a>, <a href="../PresentationElement.html#sSetParentForAll(java.util.Collection)">sSetParentForAll</a>, <a href="../PresentationElement.html#sSetSize(int,int)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(java.awt.Dimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetVisible(boolean)">sSetVisible</a>, <a href="../PresentationElement.html#tryToDeleteModelElementUponRemoval()">tryToDeleteModelElementUponRemoval</a>, <a href="../PresentationElement.html#update()">update</a>, <a href="../PresentationElement.html#updateAfterLoad()">updateAfterLoad</a>, <a href="../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)">updateLabelsIgnoringSuspendableLater</a>, <a href="../PresentationElement.html#updateModelByView()">updateModelByView</a>, <a href="../PresentationElement.html#updateModelByViewInternal()">updateModelByViewInternal</a>, <a href="../PresentationElement.html#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a>, <a href="../PresentationElement.html#useParentProperties()">useParentProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getProjectProvider, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID</code></div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="DIAGRAM_TYPES_FOR_PORTS_ON_FRAME">
<h3>DIAGRAM_TYPES_FOR_PORTS_ON_FRAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">DIAGRAM_TYPES_FOR_PORTS_ON_FRAME</span></div>
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
<h3>DiagramFrameView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramFrameView</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>DiagramFrameView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramFrameView</span><wbr/><span class="parameters">(@CheckForNull
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
<dd><code>accept</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selfSpecificHeaderShapeDraw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>selfSpecificHeaderShapeDraw</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">selfSpecificHeaderShapeDraw</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>selfSpecificHeaderShapeDraw</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canFill()">
<h3>canFill</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">canFill</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#canFill()">canFill</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if symbol can be filled with some color</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFillColor()">
<h3>getFillColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">getFillColor</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getFillColor()">PresentationElement</a></code></span></div>
<div class="block">Returns fill color</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getFillColor()">getFillColor</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCornerArcSize()">
<h3>getCornerArcSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getCornerArcSize</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getResourceID()">
<h3>getResourceID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getResourceID</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../MDElement.html#getResourceID()">getResourceID</a></code> in interface <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>getResourceID</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="useParentStyle()">
<h3>useParentStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">useParentStyle</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#useParentStyle()">PresentationElement</a></code></span></div>
<div class="block">Does this element uses parent style or has it's own?</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#useParentStyle()">useParentStyle</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true, if element does not have style and uses parent's style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentSymbolStyleOwner()">
<h3>getParentSymbolStyleOwner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getParentSymbolStyleOwner</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getParentSymbolStyleOwner()">PresentationElement</a></code></span></div>
<div class="block">Returns parent to which this symbol delegates style attributes related functionality.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>parent symbol to delegate or null if this symbol does not delegate.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="mustShowContextMenu()">
<h3>mustShowContextMenu</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">mustShowContextMenu</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#mustShowContextMenu()">mustShowContextMenu</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>intersects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">intersects</span><wbr/><span class="parameters">(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">PresentationElement</a></code></span></div>
<div class="block">checks whether object intersects with given rectangle</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if object and rectangle intersects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>coversPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">coversPoint</span><wbr/><span class="parameters">(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">PresentationElement</a></code></span></div>
<div class="block">checks if object covers provided point</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>coversPoint</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
<dt>Returns:</dt>
<dd>true if object covers this point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">
<h3>adjustBoundsBeforeChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">adjustBoundsBeforeChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rec,
 boolean autosizeOperation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">PresentationElement</a></code></span></div>
<div class="block">Validate bounds before bounds change operation</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>adjustBoundsBeforeChange</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>canAddInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddInstance</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PresentationElement</a></code></span></div>
<div class="block">Object view has no children.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>canAddInstance</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEncapsulatedClassifier()">
<h3>getEncapsulatedClassifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></span> <span class="element-name">getEncapsulatedClassifier</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getEncapsulatedClassifier</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.PortOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEncapsulatedClassifierProvider()">
<h3>getEncapsulatedClassifierProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></span> <span class="element-name">getEncapsulatedClassifierProvider</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getEncapsulatedClassifierProvider</code> in interface <code>com.nomagic.magicdraw.uml.symbols.shapes.PortOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSmartListenerConfig(java.util.List)">
<h3>createSmartListenerConfig</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createSmartListenerConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createSmartListenerConfig</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultDimension()">
<h3>getDefaultDimension</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getDefaultDimension</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#getDefaultDimension()">getDefaultDimension</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="preferredSizeIgnoringOrientation(java.awt.Dimension,int,int)">
<h3>preferredSizeIgnoringOrientation</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">preferredSizeIgnoringOrientation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>preferredSizeIgnoringOrientation</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="minimumOrMinimumShrinkableDimension(java.awt.Dimension)">
<h3>minimumOrMinimumShrinkableDimension</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">minimumOrMinimumShrinkableDimension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#minimumOrMinimumShrinkableDimension(java.awt.Dimension)">minimumOrMinimumShrinkableDimension</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="minimumSizeForShrinkingIgnoringOrientation(java.awt.Dimension,int,int)">
<h3>minimumSizeForShrinkingIgnoringOrientation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">minimumSizeForShrinkingIgnoringOrientation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size,
 int locationX,
 int locationY)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>minimumSizeForShrinkingIgnoringOrientation</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canMoveChildOutside(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>canMoveChildOutside</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">canMoveChildOutside</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>canMoveChildOutside</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalLayoutChildren(boolean)">
<h3>internalLayoutChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalLayoutChildren</span><wbr/><span class="parameters">(boolean calculatePrefSize)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalLayoutChildren</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.BaseHeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="providesVerticalCenterline()">
<h3>providesVerticalCenterline</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">providesVerticalCenterline</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code></span></div>
<div class="block">Indicates if this shape can provide a vertical centerline for other shapes to snap.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>providesVerticalCenterline</code> in interface <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code></dd>
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#providesVerticalCenterline()">providesVerticalCenterline</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if this shape provides vertical centerline, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="providesHorizontalCenterline()">
<h3>providesHorizontalCenterline</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">providesHorizontalCenterline</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code></span></div>
<div class="block">Indicates if this shape can provide a horizontal centerline for other shapes to snap.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>providesHorizontalCenterline</code> in interface <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code></dd>
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#providesHorizontalCenterline()">providesHorizontalCenterline</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if this shape provides horizontal centerline, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isHorizontalCenterlineProvider()">
<h3>isHorizontalCenterlineProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isHorizontalCenterlineProvider</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="ShapeElement.html#isHorizontalCenterlineProvider()">ShapeElement</a></code></span></div>
<div class="block">Indicates whether this shape provides horizontal center-lines to other shapes.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#isHorizontalCenterlineProvider()">isHorizontalCenterlineProvider</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if this shape provides horizontal center-lines, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVerticalCenterlineProvider()">
<h3>isVerticalCenterlineProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isVerticalCenterlineProvider</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="ShapeElement.html#isVerticalCenterlineProvider()">ShapeElement</a></code></span></div>
<div class="block">Indicates whether this shape provides vertical center-lines to other shapes.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#isVerticalCenterlineProvider()">isVerticalCenterlineProvider</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if this shape provides vertical center lines, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">
<h3>movePathElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">movePathElement</span><wbr/><span class="parameters">(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> link,
 @CheckForNull
 <a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> requestor)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">PathConnector</a></code></span></div>
<div class="block">Calculates position of a path element.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>link</code> - element which position will be calculated.</dd>
<dd><code>requestor</code> - the requestor of this path moving. Implementations may check to avoid endless loops.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStereotypesToDisplay()">
<h3>getStereotypesToDisplay</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView.StereotypeDisplayData</span> <span class="element-name">getStereotypesToDisplay</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getStereotypesToDisplay</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
<dt>Returns:</dt>
<dd>stereotypes to display on this symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>sSetParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetParent</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PresentationElement</a></code></span></div>
<div class="block">Sets parent for this view.
 For adding symbols to other symbols use
 <a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>PresentationElement.addPresentationElement(PresentationElement)</code></a> or
 <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>PresentationElement.sAddPresentationElement(PresentationElement)</code></a>}</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>parent</code> - parent view</dd>
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
<dd><code>dispose</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
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
<dd><code>atInsert</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
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
<dd><code>internalSpecificUpdate</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
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
<section class="detail" id="snapsToCenterlines()">
<h3>snapsToCenterlines</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">snapsToCenterlines</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code></span></div>
<div class="block">Indicates if this shape can be snapped to centerlines.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>snapsToCenterlines</code> in interface <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code></dd>
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#snapsToCenterlines()">snapsToCenterlines</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if this shape can be snapped to centerlines, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFrameElementBounds()">
<h3>getFrameElementBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getFrameElementBounds</span>()</div>
</section>
</li>
<li>
<section class="detail" id="calculateFrameElementBounds()">
<h3>calculateFrameElementBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">calculateFrameElementBounds</span>()</div>
</section>
</li>
<li>
<section class="detail" id="hasBoundaryDetails()">
<h3>hasBoundaryDetails</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasBoundaryDetails</span>()</div>
<div class="block">Returns true if frame carries details on its border.
 If the frame is plain, false is returned.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if frame carries details on border, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="layoutFrameIfSet()">
<h3>layoutFrameIfSet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">layoutFrameIfSet</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>layoutFrameIfSet</code> in interface <code>com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="layoutFrame()">
<h3>layoutFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">layoutFrame</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getHumanType()">
<h3>getHumanType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanType</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getHumanType()">PresentationElement</a></code></span></div>
<div class="block">Returns human representation of the data type</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#getHumanType()">getHumanType</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getHumanType()">getHumanType</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>the name of the data</dd>
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
<dd><code><a href="../PresentationElement.html#getHumanName()">getHumanName</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>the name of the data</dd>
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
<dd><code>internalPostUpdatePresentationElement</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
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
<section class="detail" id="getHeaderView()">
<h3>getHeaderView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.DiagramFrameHeaderView</span> <span class="element-name">getHeaderView</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getHeaderView</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.HeaderShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSetAsDiagramFrame()">
<h3>isSetAsDiagramFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSetAsDiagramFrame</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isSetAsDiagramFrame</code> in interface <code>com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOwningMode()">
<h3>isOwningMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOwningMode</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isOwningMode</code> in interface <code>com.dassault_systemes.modeler.magic.diagram.DiagramFrameShape</code></dd>
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
