# JAVA OPENAPI: MessageView (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/shapes/MessageView.html
- source_path: `com/nomagic/magicdraw/uml/symbols/shapes/MessageView.html`
- source_sha256: `e02ee88ba17e7c8017bc7a7f829d92176fa62b27de38611af48c3c20a143d785`
- captured_utc: `2026-07-14T16:56:03.834552+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.shapes](package-summary.html)

## Class MessageView

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](../paths/PathConnector.html)
[com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement](ShapeElement.html)
com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels
com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels
com.nomagic.magicdraw.uml.symbols.shapes.MessageView

All Implemented Interfaces:
`[BaseElement](../../BaseElement.html)`, `com.nomagic.magicdraw.uml.CompartmentSupport`, `[MDElement](../../MDElement.html)`, `[ModelElementProvider](../../ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.LabelOwner`, `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`, `[NumberedMessageView](../NumberedMessageView.html)`, `com.nomagic.magicdraw.uml.symbols.paths.PathCustomDraw`, `com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement`, `[StereotypesDisplayModeOwner](StereotypesDisplayModeOwner.html)`, `com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApipublic classMessageView
extends com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels
implements [NumberedMessageView](../NumberedMessageView.html), com.nomagic.magicdraw.uml.symbols.paths.PathCustomDraw

The `MessageView` class is used for displaying the message
 icon in Communication diagram of UML Drawing Tool.
 
 This class has the reference to the data class - `MessageData`.

Version:
1.0

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[DISTANCE_FROM_LINK](#DISTANCE_FROM_LINK)`

`static final int`
`[TO_LEFT](#TO_LEFT)`

`static final int`
`[TO_RIGHT](#TO_RIGHT)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`CONTAINER_SHAPE_INSETS, SHAPE_DISTANCE_FROM_EDGE`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.[ShapeElement](ShapeElement.html)
`[BORDER_ELEMENT_MARGIN_ALL](ShapeElement.html#BORDER_ELEMENT_MARGIN_ALL), [BORDER_ELEMENT_MARGIN_BOTTOM](ShapeElement.html#BORDER_ELEMENT_MARGIN_BOTTOM), [BORDER_ELEMENT_MARGIN_LEFT](ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT), [BORDER_ELEMENT_MARGIN_LEFT_RIGHT](ShapeElement.html#BORDER_ELEMENT_MARGIN_LEFT_RIGHT), [BORDER_ELEMENT_MARGIN_MODES](ShapeElement.html#BORDER_ELEMENT_MARGIN_MODES), [BORDER_ELEMENT_MARGIN_NONE](ShapeElement.html#BORDER_ELEMENT_MARGIN_NONE), [BORDER_ELEMENT_MARGIN_RIGHT](ShapeElement.html#BORDER_ELEMENT_MARGIN_RIGHT), [BORDER_ELEMENT_MARGIN_TOP](ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP), [BORDER_ELEMENT_MARGIN_TOP_BOTTOM](ShapeElement.html#BORDER_ELEMENT_MARGIN_TOP_BOTTOM), [BOTTOM_EDGE](ShapeElement.html#BOTTOM_EDGE), [INSIDE_EDGE_POSITION](ShapeElement.html#INSIDE_EDGE_POSITION), [LEFT_EDGE](ShapeElement.html#LEFT_EDGE), [NEED_AUTOSIZE_FULL](ShapeElement.html#NEED_AUTOSIZE_FULL), [NEED_AUTOSIZE_LAYOUT](ShapeElement.html#NEED_AUTOSIZE_LAYOUT), [NEED_AUTOSIZE_NONE](ShapeElement.html#NEED_AUTOSIZE_NONE), [NO_EDGE](ShapeElement.html#NO_EDGE), [NULL_INSETS](ShapeElement.html#NULL_INSETS), [ON_EDGE_POSITION](ShapeElement.html#ON_EDGE_POSITION), [OUTSIDE_EDGE_POSITION](ShapeElement.html#OUTSIDE_EDGE_POSITION), [RIGHT_EDGE](ShapeElement.html#RIGHT_EDGE), [SPACE](ShapeElement.html#SPACE), [SPACE_INSETS](ShapeElement.html#SPACE_INSETS), [SPACE_INSETS_EMPTY_TOP_BOTTOM](ShapeElement.html#SPACE_INSETS_EMPTY_TOP_BOTTOM), [TOP_EDGE](ShapeElement.html#TOP_EDGE)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[showsProxy](../paths/PathConnector.html#showsProxy)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DEFAULT_LINE_WIDTH](../PresentationElement.html#DEFAULT_LINE_WIDTH), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [HANDLE_SIZE](../PresentationElement.html#HANDLE_SIZE), [MAX_LINE_WIDTH](../PresentationElement.html#MAX_LINE_WIDTH), [MIN_LINE_WIDTH](../PresentationElement.html#MIN_LINE_WIDTH), [peStyle](../PresentationElement.html#peStyle), [SHADOW_WIDTH](../PresentationElement.html#SHADOW_WIDTH), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
Fields inherited from interface com.nomagic.magicdraw.uml.symbols.shapes.[StereotypesDisplayModeOwner](StereotypesDisplayModeOwner.html)
`[DSL_STEREOTYPE_DISPLAY_MODE_ALL](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_ALL), [DSL_STEREOTYPE_DISPLAY_MODE_LAST](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_LAST), [DSL_STEREOTYPE_DISPLAY_MODE_NONE](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODE_NONE), [DSL_STEREOTYPE_DISPLAY_MODES](StereotypesDisplayModeOwner.html#DSL_STEREOTYPE_DISPLAY_MODES), [STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_DO_NOT_DISPLAY_STEREOTYPES), [STEREOTYPE_DISPLAY_MODE_ICON](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_ICON), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE), [STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_SHAPE_IMAGE_AND_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT), [STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON](StereotypesDisplayModeOwner.html#STEREOTYPE_DISPLAY_MODE_TEXT_AND_ICON), [STEREOTYPES_DISPLAY_MODES](StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES), [STEREOTYPES_DISPLAY_MODES_SIMPLE](StereotypesDisplayModeOwner.html#STEREOTYPES_DISPLAY_MODES_SIMPLE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MessageView](#%3Cinit%3E())()`

`[MessageView](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) parent)`
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
`[addPresentationElement](#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,boolean))([PresentationElement](../PresentationElement.html) element,
 int index,
 boolean resize)`
If a specified object not inserted in this container then adds a new object view to the container.
`void`
`[autosize](#autosize(boolean))(boolean calculatePrefSize)`
Calculate preferred size and make this shape size at least as preferred (if size is smaller)
`void`
`[autosizeByChildren](#autosizeByChildren(boolean))(boolean calculatePrefSize)`

`boolean`
`[canAddInstance](#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) symbol)`
Object view has no children.
`boolean`
`[canChangeParent](#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [PresentationElement](../PresentationElement.html)> movedTogether,
 [BaseElement](../../BaseElement.html) newParent,
 boolean changeElementParent)`
Returns true, if element can change parent.
`boolean`
`[canHavePaths](#canHavePaths())()`

`protected boolean`
`[checkShowsProxy](#checkShowsProxy())()`

`[MessageView](MessageView.html)`
`[clone](#clone())()`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[constructMessageText](#constructMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,boolean))([Message](../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message,
 boolean showAttributesAndParameters)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[constructNameText](#constructNameText())()`

`boolean`
`[coversPoint](#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
checks if object covers provided point
`protected void`
`[createLabels](#createLabels())()`

`protected com.nomagic.magicdraw.uml.symbols.shapes.NameLabelWrapper`
`[createNameLabelWrapper](#createNameLabelWrapper())()`

`protected void`
`[createSmartListenerConfig](#createSmartListenerConfig(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)`

`com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon`
`[dynamicPathIcon](#dynamicPathIcon())()`

`com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon`
`[dynamicPathIcon](#dynamicPathIcon(com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon))(com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon pathIcon)`

`com.dassault_systemes.modeler.foundation.model.ModelElement`
`[findOwnerForElement](#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext))([PresentationElement](../PresentationElement.html) newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBoundsToRepaint](#getBoundsToRepaint())()`
Return bounds of the symbol that must be repainted.
`com.nomagic.ui.UnmodifiableInsets`
`[getChildrenInsets](#getChildrenInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel))(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)`

`[ConnectorView](../paths/ConnectorView.html)`
`[getConnector](#getConnector())()`

`int`
`[getDirection](#getDirection())()`

`[Message](../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html)`
`[getElement](#getElement())()`
Returns model element of this presentation element.
`[Message](../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html)`
`[getMessage](#getMessage())()`
Message represented by the view.
`com.nomagic.magicdraw.uml.symbols.shapes.MessageSignatureView`
`[getMessageSignatureLabelBox](#getMessageSignatureLabelBox())()`
Returns the signature view from the
 container of this message.
`com.nomagic.magicdraw.uml.symbols.shapes.MessageNameLabelWrapper`
`[getNameLabelWrapper](#getNameLabelWrapper())()`

`[Line](../../../../awt/Line.html)`
`[getNearestLinkPart](#getNearestLinkPart(int,int))(int x,
 int y)`
Returns nearest link part to specified point.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getNumber](#getNumber())()`
Returns number of the message
`com.nomagic.magicdraw.uml.symbols.MessageNumberManager`
`[getNumberManager](#getNumberManager())()`

`com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon`
`[getPathIcon](#getPathIcon())()`
get definition of custom path ending (arrow, circle, icon, etc.) and stroke (dashed, solid, etc.)
`[PresentationElement](../PresentationElement.html)`
`[getReceiver](#getReceiver())()`

`[PresentationElement](../PresentationElement.html)`
`[getSender](#getSender())()`

`[BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(boolean))(boolean line)`
This method must be overridden, if you need to use DASHED_STROKE or another one.
`[BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(boolean,int))(boolean line,
 int lineStyle)`
This method must be overridden, if you need to use DASHED_STROKE or another one.
`boolean`
`[hasSharedModelElement](#hasSharedModelElement())()`
Returns true if `ModelElement` of this symbol can represented with other symbol.
`void`
`[initialize](#initialize())()`
Initialize symbol and its children state.
`void`
`[internalApplyProperties](#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)`
Applies properties from given property manager
`void`
`[internalSilentApply](#internalSilentApply())()`
Silently applies all properties after initialization
`boolean`
`[intersects](#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
checks whether object intersects with given rectangle
`boolean`
`[isShowPredecessors](#isShowPredecessors())()`

`protected void`
`[minimumSizeIgnoringOrientation](#minimumSizeIgnoringOrientation(java.awt.Dimension))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) min)`

`void`
`[paintSelf](#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`protected void`
`[prefDimensionByManipulatedChildren](#prefDimensionByManipulatedChildren(java.awt.Dimension,int,int))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)`

`protected void`
`[preferredSizeIgnoringOrientation](#preferredSizeIgnoringOrientation(java.awt.Dimension,int,int))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)`

`protected boolean`
`[prepareForLineDrawing](#prepareForLineDrawing(java.awt.Graphics2D,boolean))([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 boolean line)`
Prepares graphics for line drawing.
`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)`
Listens for property change it can be: data was edited text box was edited
`void`
`[recursiveAutosize](#recursiveAutosize())()`
Resize recursively all symbols.
`static void`
`[resetMessagePositions](#resetMessagePositions(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](../paths/PathElement.html) path)`

`void`
`[resizeParent](#resizeParent())()`
Method that initiates parent resize to accommodate children if some child's bounds are
 changed.
`void`
`[setDirection](#setDirection(int))(int direction)`

`static void`
`[setMessageLabelNumberText](#setMessageLabelNumberText(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.shapes.MessageNameLabelWrapper))([PresentationElement](../PresentationElement.html) owner,
 com.nomagic.magicdraw.uml.symbols.shapes.MessageNameLabelWrapper nameLabelWrapper)`

`void`
`[setNumberManager](#setNumberManager(com.nomagic.magicdraw.uml.symbols.MessageNumberManager))(com.nomagic.magicdraw.uml.symbols.MessageNumberManager numberManager)`

`void`
`[setReceiver](#setReceiver(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) receiver)`

`void`
`[setSender](#setSender(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) sender)`

`void`
`[setShowPredecessors](#setShowPredecessors(boolean))(boolean show)`
Sets show predecessors list.
`void`
`[simpleSetBounds](#simpleSetBounds(java.awt.Rectangle,boolean,boolean))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect,
 boolean moveChildren,
 boolean calculatePrefSize)`
Sets bounds for this container shape view and all its components
`void`
`[sSetShowPredecessors](#sSetShowPredecessors(boolean))(boolean show)`

`void`
`[updateNameBox](#updateNameBox())()`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels
`createConstraintLabelWrapper, createElementPropertiesLabelWrapper, createStereotypeLabelWrapper, createTaggedValueLabelWrapper, getConstraintLabelBox, getConstraintLabelWrapper, getConstraintTextMode, getDSLStereotypesDisplayMode, getElementNumberDisplayMode, getElementPropertiesLabelBox, getElementPropertiesLabelWrapper, getStereotypeLabelBox, getStereotypeLabelWrapper, getStereotypesDisplayMode, getTaggedValueLabelBox, getTaggedValueLabelWrapper, isShowConstraints, isShowElementProperties, isShowNumberTagName, isShowTaggedValues, setConstraintTextMode, setDSLStereotypesDisplayMode, setShowConstraints, setShowElementProperties, setShowTaggedValues, setStereotypesDisplayMode, sSetConstraintTextMode, sSetDSLStereotypesDisplayMode, sSetElementNumberDisplayMode, sSetShowConstraints, sSetShowElementProperties, sSetShowNumberTagName, sSetShowTaggedValues, sSetStereotypesDisplayMode, updateAfterLoad`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels
`addLabel, asPresentationElement, canBeAutosized, createCompartmentElements, edgeChanged, editName, getCollections, getHeaderBoundsForPreferredBounds, getLabelHandler, getName, getNameLabelBox, internalAppendChildRect, internalPostUpdatePresentationElement, isLabelWrapText, isShowName, isShowText, isWordWrap, removeLabel, setCollections, setName, setNameResizeLabel, setShowName, setSuspendLabelAutoDisplayMode, setSuspendShapeAutoResizeMode, setTextEditable, setVisibleElements, setWordWrap, sSetElement, sSetName, sSetShowName, sSetSuspendLabelAutoDisplayMode, sSetWordWrap`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
`addExtraChildrenPrefSizePadding, adjustBoundsBeforeChange, autosizeAndResizeParent, calculateMinY, calculateOvalShapePreferredSize, correctChildrenVector, createBoundsShape, createStateForUpdateOperation, doInternalLayoutChildren, getAdditionalHeaderHeightForPreferredBounds, getChildrenBoundsForPreferredBounds, getHeaderDistanceFromTopForOvalShape, getHeaderInsets, getHeaderMaxYForShrinkableShape, getHeaderObject, getHeaderVerticalPosition, getHeaderVerticalPositionForLayout, getNameLabel, getOvalShapeAvailableWidth, getPreferredBounds, getPresentationElementAt, getProxyPresentationElementsStream, getStereotypesToDisplay, internalGetHeaderBoundsForPreferredBounds, internalGetHeaderInsets, internalLayoutChildren, internalPostSpecificUpdate, internalPreSpecificUpdate, internalSpecificUpdate, internalUpdatePresentationElement, invalidate, isBorderVisible, isChildLayoutable, isContentHidden, isHeaderOrientationVertical, isOvalShape, isParentShowsProxy, minimumDimension, minimumDimensionForShrinking, minimumSizeForShrinkingIgnoringOrientation, paintChildren, preferredDimension, setHeaderObject, setHeaderVerticalPosition, sSetAutosize, sSetHeaderVerticalPosition, switchWidthHeightIfVerticalOrientation`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, calculateAutosizeDimension, calculateAutosizeDimension, canAddChild, canMoveChildOutside, childrenBoundsForReshape, clearShowsProxy, constructLayoutHelper, getChildrenBounds, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getRemovableChildren, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildrenBackground, removePresentationElement, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.[ShapeElement](ShapeElement.html)
`[addBreakPoints](ShapeElement.html#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [adjustBounds](ShapeElement.html#adjustBounds(java.awt.Rectangle)), [adjustOnEdge](ShapeElement.html#adjustOnEdge()), [adjustOnEdge](ShapeElement.html#adjustOnEdge(java.awt.Rectangle,int,int,int)), [adjustOnEdgeChildren](ShapeElement.html#adjustOnEdgeChildren()), [autosize](ShapeElement.html#autosize()), [calculateAdjustOnEdgeLocation](ShapeElement.html#calculateAdjustOnEdgeLocation(java.awt.Rectangle)), [calculateAndGetMinimumShrinkingDimension](ShapeElement.html#calculateAndGetMinimumShrinkingDimension(int,int)), [calculateAndGetPreferredDimension](ShapeElement.html#calculateAndGetPreferredDimension()), [calculateEdge](ShapeElement.html#calculateEdge()), [calculateMinimumDimension](ShapeElement.html#calculateMinimumDimension()), [calculateOnEdgeBounds](ShapeElement.html#calculateOnEdgeBounds()), [calculatePreferredDimension](ShapeElement.html#calculatePreferredDimension()), [calculatePreferredDimension](ShapeElement.html#calculatePreferredDimension(int,int)), [clearOldRect](ShapeElement.html#clearOldRect()), [ensureDimension](ShapeElement.html#ensureDimension(boolean)), [ensurePreferredDimensionIfShrinkable](ShapeElement.html#ensurePreferredDimensionIfShrinkable()), [ensurePreferredDimensionIfShrinkable](ShapeElement.html#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)), [findFreePlaceForShapeOnBorder](ShapeElement.html#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)), [getBorderElementMargin](ShapeElement.html#getBorderElementMargin()), [getBounds](ShapeElement.html#getBounds()), [getCenterlineableInnerParts](ShapeElement.html#getCenterlineableInnerParts(int)), [getDefaultDimension](ShapeElement.html#getDefaultDimension()), [getDimensionForShrinking](ShapeElement.html#getDimensionForShrinking(int,int)), [getEdgeLine](ShapeElement.html#getEdgeLine(int)), [getFixedConnectionPoints](ShapeElement.html#getFixedConnectionPoints()), [getHeaderInsetReduce](ShapeElement.html#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)), [getInsetsForOnEdgeShapes](ShapeElement.html#getInsetsForOnEdgeShapes()), [getIntersection](ShapeElement.html#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getIntersection](ShapeElement.html#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)), [getIntersection](ShapeElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getLoadedDimension](ShapeElement.html#getLoadedDimension()), [getMiddlePoint](ShapeElement.html#getMiddlePoint()), [getMiddlePoint](ShapeElement.html#getMiddlePoint(java.awt.Point)), [getMiddlePointX](ShapeElement.html#getMiddlePointX()), [getMiddlePointX](ShapeElement.html#getMiddlePointX(java.awt.Point)), [getMiddlePointY](ShapeElement.html#getMiddlePointY()), [getMiddlePointY](ShapeElement.html#getMiddlePointY(java.awt.Point)), [getMinimumDimension](ShapeElement.html#getMinimumDimension()), [getNearestEdge](ShapeElement.html#getNearestEdge(int,int)), [getNearestEdge](ShapeElement.html#getNearestEdge(java.awt.Rectangle)), [getNeedAutosizeFlag](ShapeElement.html#getNeedAutosizeFlag()), [getNotCopyBounds](ShapeElement.html#getNotCopyBounds()), [getOnEdge](ShapeElement.html#getOnEdge()), [getOnEdgeCornerDistance](ShapeElement.html#getOnEdgeCornerDistance()), [getOnEdgePosition](ShapeElement.html#getOnEdgePosition()), [getPreferredDimension](ShapeElement.html#getPreferredDimension()), [getPreferredDimensionForAutosize](ShapeElement.html#getPreferredDimensionForAutosize()), [getReshapeMode](ShapeElement.html#getReshapeMode()), [getSizeForDrawing](ShapeElement.html#getSizeForDrawing()), [getSuspendShapeAutoResizeMode](ShapeElement.html#getSuspendShapeAutoResizeMode()), [hasManipulator](ShapeElement.html#hasManipulator()), [internalGetBoundsShape](ShapeElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [isAutosized](ShapeElement.html#isAutosized()), [isCenterlineInner](ShapeElement.html#isCenterlineInner()), [isHorizontalCenterlineProvider](ShapeElement.html#isHorizontalCenterlineProvider()), [isOnEdge](ShapeElement.html#isOnEdge()), [isShapeOnEdge](ShapeElement.html#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isShrinkable](ShapeElement.html#isShrinkable()), [isSnapShapesOnBorderToGrid](ShapeElement.html#isSnapShapesOnBorderToGrid()), [isSnapToGrid](ShapeElement.html#isSnapToGrid()), [isUseFixedConnectionPoints](ShapeElement.html#isUseFixedConnectionPoints()), [isVerticalCenterlineProvider](ShapeElement.html#isVerticalCenterlineProvider()), [layoutChildren](ShapeElement.html#layoutChildren()), [maximumDimension](ShapeElement.html#maximumDimension(java.awt.Dimension)), [minimumOrMinimumShrinkableDimension](ShapeElement.html#minimumOrMinimumShrinkableDimension(java.awt.Dimension)), [moveLinksToSelf](ShapeElement.html#moveLinksToSelf()), [movePathElement](ShapeElement.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)), [movePathElements](ShapeElement.html#movePathElements()), [needAdjustToMaximumDimension](ShapeElement.html#needAdjustToMaximumDimension()), [onChildEdgeChange](ShapeElement.html#onChildEdgeChange(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)), [prepareForShadowDrawing](ShapeElement.html#prepareForShadowDrawing(java.awt.Graphics2D)), [providesHorizontalCenterline](ShapeElement.html#providesHorizontalCenterline()), [providesVerticalCenterline](ShapeElement.html#providesVerticalCenterline()), [resetCalculatePreferredRegardingChildren](ShapeElement.html#resetCalculatePreferredRegardingChildren()), [setAutosize](ShapeElement.html#setAutosize(boolean)), [setBorderElementMargin](ShapeElement.html#setBorderElementMargin(java.lang.String)), [setCalculatePreferredRegardingChildren](ShapeElement.html#setCalculatePreferredRegardingChildren(boolean)), [setLoadedDimension](ShapeElement.html#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)), [setMinimumDimension](ShapeElement.html#setMinimumDimension(int,int)), [setNeedAutosizeFlag](ShapeElement.html#setNeedAutosizeFlag(byte)), [setOldRect](ShapeElement.html#setOldRect(java.awt.Rectangle)), [setOnEdge](ShapeElement.html#setOnEdge(int)), [setPreferredDimension](ShapeElement.html#setPreferredDimension(int,int)), [setReshapeMode](ShapeElement.html#setReshapeMode(com.nomagic.magicdraw.uml.symbols.ReshapeMode)), [setSnapShapesOnBorderToGrid](ShapeElement.html#setSnapShapesOnBorderToGrid(boolean)), [setUseFixedConnectionPoints](ShapeElement.html#setUseFixedConnectionPoints(boolean)), [shouldDrawShadow](ShapeElement.html#shouldDrawShadow()), [simpleSetBounds](ShapeElement.html#simpleSetBounds(int,int,int,int,boolean)), [simpleSetBounds](ShapeElement.html#simpleSetBounds(java.awt.Rectangle)), [snapsToCenterlines](ShapeElement.html#snapsToCenterlines()), [sSetBorderElementMargin](ShapeElement.html#sSetBorderElementMargin(java.lang.String)), [sSetBounds](ShapeElement.html#sSetBounds(java.awt.Rectangle)), [sSetSuspendShapeAutoResizeMode](ShapeElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)), [sSetVisibility](ShapeElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [toString](ShapeElement.html#toString()), [updateLater](ShapeElement.html#updateLater())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[addConnectedPathElement](../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [dispose](../paths/PathConnector.html#dispose()), [disposeConnectedPaths](../paths/PathConnector.html#disposeConnectedPaths()), [findSymbolForEnd](../paths/PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)), [findSymbolForEnd](../paths/PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)), [getConnectedPathElement](../paths/PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [getConnectedPathElementCount](../paths/PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)), [getPreferredArrowLength](../paths/PathConnector.html#getPreferredArrowLength()), [isShowsProxy](../paths/PathConnector.html#isShowsProxy()), [movePathElement](../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)), [removeConnectedPathElement](../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sAddConnectedPathElement](../paths/PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [selectPathsForMoving](../paths/PathConnector.html#selectPathsForMoving(java.util.List)), [setParent](../paths/PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [setVisibility](../paths/PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [sRemoveConnectedPathElement](../paths/PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sSetConnectedPathElements](../paths/PathConnector.html#sSetConnectedPathElements(java.util.List)), [supportsVisibleConnectedPathElementsIfSelfInvisible](../paths/PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[addPresentationElement](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addProperty](../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [adjustChildBounds](../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [alwaysShowTooltip](../PresentationElement.html#alwaysShowTooltip()), [applyProperties](../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [askDeleteDataConfirmation](../PresentationElement.html#askDeleteDataConfirmation()), [atInsert](../PresentationElement.html#atInsert()), [atInsertChildren](../PresentationElement.html#atInsertChildren()), [autosizeAndResizeManipulatedParent](../PresentationElement.html#autosizeAndResizeManipulatedParent()), [beforeDelete](../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)), [boundsChanged](../PresentationElement.html#boundsChanged()), [boundsChanged](../PresentationElement.html#boundsChanged(java.awt.Rectangle)), [canAddChild](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)), [canAddInstance](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDisposedOnUpdate](../PresentationElement.html#canBeDisposedOnUpdate()), [canChangeElementOwner](../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canFill](../PresentationElement.html#canFill()), [changeProperties](../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [checkElementOwnerOnChange](../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [checkProxyVisibility](../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [childrenForMoving](../PresentationElement.html#childrenForMoving()), [collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)), [collectSubShowingPresentationElements](../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)), [coversPoint](../PresentationElement.html#coversPoint(int,int)), [createFillStrategy](../PresentationElement.html#createFillStrategy()), [createPresentationElementStyle](../PresentationElement.html#createPresentationElementStyle()), [createPropertyChangeListener](../PresentationElement.html#createPropertyChangeListener()), [disposeChildren](../PresentationElement.html#disposeChildren()), [disposePropertyChangeListener](../PresentationElement.html#disposePropertyChangeListener()), [draw](../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawBackground](../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbol](../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbolBackground](../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [dynamicFillColor](../PresentationElement.html#dynamicFillColor()), [dynamicLineColor](../PresentationElement.html#dynamicLineColor()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth(int)), [dynamicPaintShadow](../PresentationElement.html#dynamicPaintShadow()), [dynamicStroke](../PresentationElement.html#dynamicStroke()), [dynamicStroke](../PresentationElement.html#dynamicStroke(int)), [dynamicStroke](../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)), [dynamicStyleFillColor](../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)), [dynamicStyleLineColor](../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)), [dynamicStyleTextColor](../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency()), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)), [dynamicStyleValue](../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)), [dynamicTextAlignment](../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)), [dynamicTextColor](../PresentationElement.html#dynamicTextColor()), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [findOwnerForChildElement](../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [findPresentationElement](../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)), [firePropertyChange](../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateID](../PresentationElement.html#generateID()), [getAbstractDiagramPresentationElement](../PresentationElement.html#getAbstractDiagramPresentationElement()), [getActualElement](../PresentationElement.html#getActualElement()), [getAdditionalRenderersToNotifyOnPropertiesChange](../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()), [getAssignableModelElementsClasses](../PresentationElement.html#getAssignableModelElementsClasses()), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getBoundsWithChildrenOnEdge](../PresentationElement.html#getBoundsWithChildrenOnEdge()), [getCenterlinePoint](../PresentationElement.html#getCenterlinePoint()), [getCenterlinePointX](../PresentationElement.html#getCenterlinePointX()), [getCenterlinePointY](../PresentationElement.html#getCenterlinePointY()), [getChildPresentationElementForContextMenu](../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)), [getChildrenWithSymbolProperties](../PresentationElement.html#getChildrenWithSymbolProperties()), [getConfiguration](../PresentationElement.html#getConfiguration()), [getDiagramPresentationElement](../PresentationElement.html#getDiagramPresentationElement()), [getDiagramSurface](../PresentationElement.html#getDiagramSurface()), [getDrawComparator](../PresentationElement.html#getDrawComparator()), [getDynamicConfigurations](../PresentationElement.html#getDynamicConfigurations()), [getDynamicStyleOwner](../PresentationElement.html#getDynamicStyleOwner()), [getEffectiveStyleDelegate](../PresentationElement.html#getEffectiveStyleDelegate()), [getEffectiveStyleOwner](../PresentationElement.html#getEffectiveStyleOwner()), [getElementsForRelationshipConnecting](../PresentationElement.html#getElementsForRelationshipConnecting()), [getElementToConnectRelationship](../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFillColor](../PresentationElement.html#getFillColor()), [getFont](../PresentationElement.html#getFont()), [getFontHeight](../PresentationElement.html#getFontHeight()), [getFontRenderContext](../PresentationElement.html#getFontRenderContext()), [getHumanName](../PresentationElement.html#getHumanName()), [getHumanType](../PresentationElement.html#getHumanType()), [getLineColor](../PresentationElement.html#getLineColor()), [getLineWidth](../PresentationElement.html#getLineWidth()), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point)), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getManipulationBounds](../PresentationElement.html#getManipulationBounds(java.awt.Point)), [getModelElement](../PresentationElement.html#getModelElement()), [getModelElementsForRelationshipConnecting](../PresentationElement.html#getModelElementsForRelationshipConnecting()), [getModelElementToConnectRelationship](../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [getModelElementToMove](../PresentationElement.html#getModelElementToMove()), [getNotZoomedTolerance](../PresentationElement.html#getNotZoomedTolerance()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getOwnStyleDelegate](../PresentationElement.html#getOwnStyleDelegate()), [getParent](../PresentationElement.html#getParent()), [getParentSymbolStyleOwner](../PresentationElement.html#getParentSymbolStyleOwner()), [getPreferredSize](../PresentationElement.html#getPreferredSize()), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(int)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementCount](../PresentationElement.html#getPresentationElementCount()), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getProjectImpl](../PresentationElement.html#getProjectImpl()), [getProperty](../PresentationElement.html#getProperty(java.lang.String)), [getPropertyManager](../PresentationElement.html#getPropertyManager()), [getPropertyManagerName](../PresentationElement.html#getPropertyManagerName()), [getRenderer](../PresentationElement.html#getRenderer()), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [getStyle](../PresentationElement.html#getStyle()), [getSymbolRenderer](../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getTextColor](../PresentationElement.html#getTextColor()), [getTolerance](../PresentationElement.html#getTolerance()), [getVisibility](../PresentationElement.html#getVisibility()), [getVisiblePresentationElements](../PresentationElement.html#getVisiblePresentationElements()), [handleModelDelete](../PresentationElement.html#handleModelDelete()), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [initializeAndAutosize](../PresentationElement.html#initializeAndAutosize()), [internalBeforeUpdate](../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)), [internalCreatePropertyChangeListener](../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [internalGetModelElementToConnectRelationship](../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [internalGetPresentationElementStroke](../PresentationElement.html#internalGetPresentationElementStroke(int)), [internalGetSpecificFont](../PresentationElement.html#internalGetSpecificFont()), [internalGetSpecificTextColor](../PresentationElement.html#internalGetSpecificTextColor()), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(float)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)), [intersects](../PresentationElement.html#intersects(int,int,int,int)), [isChildVisible](../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isCreateElementListener](../PresentationElement.html#isCreateElementListener()), [isDetectable](../PresentationElement.html#isDetectable()), [isDisposed](../PresentationElement.html#isDisposed()), [isLayouting](../PresentationElement.html#isLayouting()), [isMovableByMoveManager](../PresentationElement.html#isMovableByMoveManager()), [isNotNull](../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isPreserveProportionsWhenGrowing](../PresentationElement.html#isPreserveProportionsWhenGrowing()), [isSelected](../PresentationElement.html#isSelected()), [isShowElementTypeAsLabel](../PresentationElement.html#isShowElementTypeAsLabel()), [isSortable](../PresentationElement.html#isSortable()), [isSuitableToConnectRelationship](../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [isTextEditable](../PresentationElement.html#isTextEditable()), [isUseFillColor](../PresentationElement.html#isUseFillColor()), [isUseFillColorByProperty](../PresentationElement.html#isUseFillColorByProperty()), [isUseGradientForFill](../PresentationElement.html#isUseGradientForFill()), [isVisible](../PresentationElement.html#isVisible()), [isVisibleInDiagram](../PresentationElement.html#isVisibleInDiagram()), [isVisibleOrShrunken](../PresentationElement.html#isVisibleOrShrunken()), [movePathElementsRecursively](../PresentationElement.html#movePathElementsRecursively()), [mustShowContextMenu](../PresentationElement.html#mustShowContextMenu()), [notifyCreated](../PresentationElement.html#notifyCreated()), [notifyDiagramFrameSizeChange](../PresentationElement.html#notifyDiagramFrameSizeChange()), [notifyRepaintManager](../PresentationElement.html#notifyRepaintManager(boolean)), [onChildAdd](../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onChildRemove](../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onDiagramSurfaceSet](../PresentationElement.html#onDiagramSurfaceSet()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [onFontChange](../PresentationElement.html#onFontChange()), [onParentChange](../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [paintAdornments](../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintAdornmentsBackground](../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenAndAdornments](../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelfBackground](../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [preDisposeOnUpdate](../PresentationElement.html#preDisposeOnUpdate()), [prepareForLineDrawing](../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)), [prepareForTextDrawing](../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)), [recreateListeners](../PresentationElement.html#recreateListeners()), [registerInSortManager](../PresentationElement.html#registerInSortManager()), [rememberBounds](../PresentationElement.html#rememberBounds()), [rememberBounds](../PresentationElement.html#rememberBounds(java.awt.Rectangle)), [removeFromSortManager](../PresentationElement.html#removeFromSortManager()), [removeItSelfOnUpdate](../PresentationElement.html#removeItSelfOnUpdate()), [sAddPresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [selectChildrenForMoving](../PresentationElement.html#selectChildrenForMoving()), [selectObjectsForMoving](../PresentationElement.html#selectObjectsForMoving()), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setBounds](../PresentationElement.html#setBounds(int,int,int,int)), [setCreateElementListener](../PresentationElement.html#setCreateElementListener(boolean)), [setElement](../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setFont](../PresentationElement.html#setFont(java.awt.Font)), [setLayouting](../PresentationElement.html#setLayouting(boolean)), [setLineColor](../PresentationElement.html#setLineColor(java.awt.Color)), [setLineWidth](../PresentationElement.html#setLineWidth(int)), [setLoadedVisibility](../PresentationElement.html#setLoadedVisibility(boolean)), [setLocation](../PresentationElement.html#setLocation(int,int)), [setLocation](../PresentationElement.html#setLocation(java.awt.Point)), [setModelElement](../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [setNeedRecreateListeners](../PresentationElement.html#setNeedRecreateListeners(boolean)), [setPropertyManagerName](../PresentationElement.html#setPropertyManagerName(java.lang.String)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [setSize](../PresentationElement.html#setSize(int,int)), [setSize](../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)), [setSize](../PresentationElement.html#setSize(java.awt.Dimension)), [setTextColor](../PresentationElement.html#setTextColor(java.awt.Color)), [setUseFillColor](../PresentationElement.html#setUseFillColor(boolean)), [setVisible](../PresentationElement.html#setVisible(boolean)), [silentApply](../PresentationElement.html#silentApply()), [silentApply](../PresentationElement.html#silentApply(boolean)), [simpleSetBounds](../PresentationElement.html#simpleSetBounds(int,int,int,int)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Point,float)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)), [snapViewToGrid](../PresentationElement.html#snapViewToGrid(float)), [sortObjectsByX](../PresentationElement.html#sortObjectsByX(java.util.List)), [sortObjectsByY](../PresentationElement.html#sortObjectsByY(java.util.List)), [sSetBounds](../PresentationElement.html#sSetBounds(int,int,int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(java.awt.Point)), [sSetModelElement](../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [sSetParent](../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetParentForAll](../PresentationElement.html#sSetParentForAll(java.util.Collection)), [sSetSize](../PresentationElement.html#sSetSize(int,int)), [sSetSize](../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)), [sSetSize](../PresentationElement.html#sSetSize(java.awt.Dimension)), [sSetVisible](../PresentationElement.html#sSetVisible(boolean)), [tryToDeleteModelElementUponRemoval](../PresentationElement.html#tryToDeleteModelElementUponRemoval()), [update](../PresentationElement.html#update()), [updateLabelsIgnoringSuspendableLater](../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)), [updateModelByView](../PresentationElement.html#updateModelByView()), [updateModelByViewInternal](../PresentationElement.html#updateModelByViewInternal()), [updateViewAfterPropertyChange](../PresentationElement.html#updateViewAfterPropertyChange()), [useParentProperties](../PresentationElement.html#useParentProperties()), [useParentStyle](../PresentationElement.html#useParentStyle())`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID`
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
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.paths.PathCustomDraw
`getLineWidth`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement
`addProperty, asPresentationElement, getProperty, getPropertyManager`

============ FIELD DETAIL =========== 
Field Details
TO_RIGHT
public static final int TO_RIGHT
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.MessageView.TO_RIGHT)
TO_LEFT
public static final int TO_LEFT
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.MessageView.TO_LEFT)
DISTANCE_FROM_LINK
public static final int DISTANCE_FROM_LINK
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.MessageView.DISTANCE_FROM_LINK)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MessageView
public MessageView()
MessageView
public MessageView(@CheckForNull
 [PresentationElement](../PresentationElement.html) parent)
 ============ METHOD DETAIL ========== 
Method Details
createNameLabelWrapper
protected com.nomagic.magicdraw.uml.symbols.shapes.NameLabelWrapper createNameLabelWrapper()
Overrides:
`createNameLabelWrapper` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
createLabels
protected void createLabels()
Overrides:
`createLabels` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
getNameLabelWrapper
public com.nomagic.magicdraw.uml.symbols.shapes.MessageNameLabelWrapper getNameLabelWrapper()
Overrides:
`getNameLabelWrapper` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels`
getMessageSignatureLabelBox
public com.nomagic.magicdraw.uml.symbols.shapes.MessageSignatureView getMessageSignatureLabelBox()
Returns the signature view from the
 container of this message. Data flows are
 contained in it too.
Returns:
the `MessageSignatureView`
updateNameBox
public void updateNameBox()
Overrides:
`updateNameBox` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
constructNameText
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) constructNameText()
Overrides:
`constructNameText` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
constructMessageText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) constructMessageText(@CheckForNull
 [Message](../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) message,
 boolean showAttributesAndParameters)
setMessageLabelNumberText
public static void setMessageLabelNumberText([PresentationElement](../PresentationElement.html) owner,
 com.nomagic.magicdraw.uml.symbols.shapes.MessageNameLabelWrapper nameLabelWrapper)
preferredSizeIgnoringOrientation
protected void preferredSizeIgnoringOrientation([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)
Overrides:
`preferredSizeIgnoringOrientation` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
minimumSizeIgnoringOrientation
protected void minimumSizeIgnoringOrientation([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) min)
Overrides:
`minimumSizeIgnoringOrientation` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
simpleSetBounds
public void simpleSetBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect,
 boolean moveChildren,
 boolean calculatePrefSize)
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Sets bounds for this container shape view and all its components
Overrides:
`simpleSetBounds` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels`
Parameters:
`rect` - container shape view bounding rectangle
`moveChildren` - if moveChildren equals true then this method calls
`calculatePrefSize` - calculate preferred size
getNearestLinkPart
public [Line](../../../../awt/Line.html) getNearestLinkPart(int x,
 int y)
Returns nearest link part to specified point.
addPresentationElement
public void addPresentationElement([PresentationElement](../PresentationElement.html) element,
 int index,
 boolean resize)
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
If a specified object not inserted in this container then adds a new object view to the container.
Overrides:
`addPresentationElement` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`element` - new PresentationElement object
`index` - index to add at
`resize` - resize parent
dynamicPathIcon
@CheckForNullpublic com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon dynamicPathIcon()
dynamicPathIcon
public com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon dynamicPathIcon(@CheckForNull
 com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon pathIcon)
getPathIcon
@CheckForNullpublic com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon getPathIcon()
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.paths.PathCustomDraw`
get definition of custom path ending (arrow, circle, icon, etc.) and stroke (dashed, solid, etc.)
Specified by:
`getPathIcon` in interface `com.nomagic.magicdraw.uml.symbols.paths.PathCustomDraw`
Returns:
custom path end draw, null if not specified
See Also:
`PathIcon`
paintSelf
public void paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
Specified by:
`[paintSelf](../PresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))` in class `[PresentationElement](../PresentationElement.html)`
clone
public [MessageView](MessageView.html) clone()
Specified by:
`[clone](../../BaseElement.html#clone())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`clone` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
canAddInstance
public boolean canAddInstance([PresentationElement](../PresentationElement.html) symbol)
Description copied from class: `[PresentationElement](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Object view has no children.
Overrides:
`canAddInstance` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels`
canHavePaths
public boolean canHavePaths()
Overrides:
`[canHavePaths](ShapeElement.html#canHavePaths())` in class `[ShapeElement](ShapeElement.html)`
Returns:
true if symbol can have connected paths. Return false here.
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
hasSharedModelElement
public boolean hasSharedModelElement()
Description copied from class: `[PresentationElement](../PresentationElement.html#hasSharedModelElement())`
Returns true if `ModelElement` of this symbol can represented with other symbol.
 If `ModelElement` is not shared, it can be deleted together with symbol deleting.
Overrides:
`[hasSharedModelElement](../PresentationElement.html#hasSharedModelElement())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
true if element of this symbol can be represented with other symbol.
resizeParent
public void resizeParent()
Description copied from class: `[PresentationElement](../PresentationElement.html#resizeParent())`
Method that initiates parent resize to accommodate children if some child's bounds are
 changed.
Overrides:
`[resizeParent](../PresentationElement.html#resizeParent())` in class `[PresentationElement](../PresentationElement.html)`
prefDimensionByManipulatedChildren
protected void prefDimensionByManipulatedChildren([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)
Overrides:
`prefDimensionByManipulatedChildren` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
autosizeByChildren
public void autosizeByChildren(boolean calculatePrefSize)
Overrides:
`autosizeByChildren` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
autosize
public void autosize(boolean calculatePrefSize)
Description copied from class: `[ShapeElement](ShapeElement.html#autosize(boolean))`
Calculate preferred size and make this shape size at least as preferred (if size is smaller)
Overrides:
`autosize` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView`
Parameters:
`calculatePrefSize` - calculate preferred size
initialize
public void initialize()
Description copied from class: `[PresentationElement](../PresentationElement.html#initialize())`
Initialize symbol and its children state. Symbol must be initialized before doing any
 resize, painting and etc. These operations can lead to unpredictable results otherwise.
Overrides:
`[initialize](ShapeElement.html#initialize())` in class `[ShapeElement](ShapeElement.html)`
recursiveAutosize
public void recursiveAutosize()
Description copied from class: `[PresentationElement](../PresentationElement.html#recursiveAutosize())`
Resize recursively all symbols. Method must be called if something is changed in symbol (for
 example minimum size) and you want to resize (autosize) all hierarchy
Overrides:
`recursiveAutosize` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
setDirection
public void setDirection(int direction)
getDirection
public int getDirection()
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
getBoundsToRepaint
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBoundsToRepaint()
 throws [NoRectangleDefinedException](../NoRectangleDefinedException.html)
Description copied from class: `[PresentationElement](../PresentationElement.html#getBoundsToRepaint())`
Return bounds of the symbol that must be repainted. throws NoRectangleDefinedException
Overrides:
`getBoundsToRepaint` in class `com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels`
Returns:
rectangle of bounds
Throws:
`[NoRectangleDefinedException](../NoRectangleDefinedException.html)`
internalApplyProperties
public void internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)
Description copied from class: `[PresentationElement](../PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))`
Applies properties from given property manager
Overrides:
`internalApplyProperties` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
Parameters:
`changer` - new properties
internalSilentApply
public void internalSilentApply()
Description copied from class: `[PresentationElement](../PresentationElement.html#internalSilentApply())`
Silently applies all properties after initialization
Overrides:
`internalSilentApply` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`
sSetShowPredecessors
public void sSetShowPredecessors(boolean show)
setShowPredecessors
public void setShowPredecessors(boolean show)
Sets show predecessors list.
Parameters:
`show` - show list
isShowPredecessors
public boolean isShowPredecessors()
Returns:
show predecessors property value.
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
resetMessagePositions
public static void resetMessagePositions([PathElement](../paths/PathElement.html) path)
getElement
public [Message](../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) getElement()
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
findOwnerForElement
public com.dassault_systemes.modeler.foundation.model.ModelElement findOwnerForElement([PresentationElement](../PresentationElement.html) newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)
Overrides:
`[findOwnerForElement](../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext))` in class `[PresentationElement](../PresentationElement.html)`
getMessage
public [Message](../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html) getMessage()
Description copied from interface: `[NumberedMessageView](../NumberedMessageView.html#getMessage())`
Message represented by the view.
Specified by:
`[getMessage](../NumberedMessageView.html#getMessage())` in interface `[NumberedMessageView](../NumberedMessageView.html)`
Returns:
message represented by the view
getNumber
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getNumber()
Description copied from interface: `[NumberedMessageView](../NumberedMessageView.html#getNumber())`
Returns number of the message
Specified by:
`[getNumber](../NumberedMessageView.html#getNumber())` in interface `[NumberedMessageView](../NumberedMessageView.html)`
Returns:
nested number of the message
getNumberManager
public com.nomagic.magicdraw.uml.symbols.MessageNumberManager getNumberManager()
setNumberManager
public void setNumberManager(com.nomagic.magicdraw.uml.symbols.MessageNumberManager numberManager)
getSender
public [PresentationElement](../PresentationElement.html) getSender()
getReceiver
public [PresentationElement](../PresentationElement.html) getReceiver()
setReceiver
public void setReceiver([PresentationElement](../PresentationElement.html) receiver)
setSender
public void setSender([PresentationElement](../PresentationElement.html) sender)
getConnector
public [ConnectorView](../paths/ConnectorView.html) getConnector()
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)
Description copied from class: `[PresentationElement](../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent))`
Listens for property change it can be: data was edited text box was edited
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
Overrides:
`[propertyChange](../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent))` in class `[PresentationElement](../PresentationElement.html)`
checkShowsProxy
protected boolean checkShowsProxy()
Overrides:
`checkShowsProxy` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
getChildrenInsets
public com.nomagic.ui.UnmodifiableInsets getChildrenInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)
Overrides:
`getChildrenInsets` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`insetsLevel` - describes the level of insets
Returns:
shape insets for children
getStroke
public [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke(boolean line,
 int lineStyle)
This method must be overridden, if you need to use DASHED_STROKE or another one.
Returns:
the stroke for line drawing ( by default SOLID_STROKE).
prepareForLineDrawing
protected boolean prepareForLineDrawing([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 boolean line)
Prepares graphics for line drawing.
 Calls super prepareForLineDrawing and sets stroke.
getStroke
public [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke(boolean line)
This method must be overridden, if you need to use DASHED_STROKE or another one.
Returns:
the stroke for line drawing ( by default SOLID_STROKE).
createSmartListenerConfig
protected void createSmartListenerConfig([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)
Overrides:
`createSmartListenerConfig` in class `com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.shapes</a></div>
<h1 class="title" title="Class MessageView">Class MessageView</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</a>
<div class="inheritance"><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.MessageView</div>
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
<dd><code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code>com.nomagic.magicdraw.uml.CompartmentSupport</code>, <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.LabelOwner</code>, <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code>, <code><a href="../NumberedMessageView.html" title="interface in com.nomagic.magicdraw.uml.symbols">NumberedMessageView</a></code>, <code>com.nomagic.magicdraw.uml.symbols.paths.PathCustomDraw</code>, <code>com.nomagic.magicdraw.uml.symbols.PropertyBasedPresentationElement</code>, <code><a href="StereotypesDisplayModeOwner.html" title="interface in com.nomagic.magicdraw.uml.symbols.shapes">StereotypesDisplayModeOwner</a></code>, <code>com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider</code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MessageView</span>
<span class="extends-implements">extends com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels
implements <a href="../NumberedMessageView.html" title="interface in com.nomagic.magicdraw.uml.symbols">NumberedMessageView</a>, com.nomagic.magicdraw.uml.symbols.paths.PathCustomDraw</span></div>
<div class="block">The <code>MessageView</code> class is used for displaying the message
 icon in Communication diagram of UML Drawing Tool.
 <p></p>
 This class has the reference to the data class - <code>MessageData</code>.</div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
</dl>
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
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DISTANCE_FROM_LINK">DISTANCE_FROM_LINK</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TO_LEFT">TO_LEFT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TO_RIGHT">TO_RIGHT</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MessageView</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement)">MessageView</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,boolean)">addPresentationElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index,
 boolean resize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If a specified object not inserted in this container then adds a new object view to the container.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#autosize(boolean)">autosize</a><wbr/>(boolean calculatePrefSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculate preferred size and make this shape size at least as preferred (if size is smaller)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#autosizeByChildren(boolean)">autosizeByChildren</a><wbr/>(boolean calculatePrefSize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddInstance</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Object view has no children.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">canChangeParent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether,
 <a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent,
 boolean changeElementParent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if element can change parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canHavePaths()">canHavePaths</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkShowsProxy()">checkShowsProxy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">MessageView</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#constructMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,boolean)">constructMessageText</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 boolean showAttributesAndParameters)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#constructNameText()">constructNameText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">coversPoint</a><wbr/>(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">checks if object covers provided point</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createLabels()">createLabels</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.uml.symbols.shapes.NameLabelWrapper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createNameLabelWrapper()">createNameLabelWrapper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicPathIcon()">dynamicPathIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicPathIcon(com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon)">dynamicPathIcon</a><wbr/>(com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon pathIcon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.model.ModelElement</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBoundsToRepaint()">getBoundsToRepaint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return bounds of the symbol that must be repainted.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ui.UnmodifiableInsets</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildrenInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel)">getChildrenInsets</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../paths/ConnectorView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ConnectorView</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnector()">getConnector</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirection()">getDirection</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model element of this presentation element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessage()">getMessage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Message represented by the view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.shapes.MessageSignatureView</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessageSignatureLabelBox()">getMessageSignatureLabelBox</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the signature view from the
 container of this message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.shapes.MessageNameLabelWrapper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNameLabelWrapper()">getNameLabelWrapper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../awt/Line.html" title="class in com.nomagic.awt">Line</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNearestLinkPart(int,int)">getNearestLinkPart</a><wbr/>(int x,
 int y)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns nearest link part to specified point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumber()">getNumber</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns number of the message</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.MessageNumberManager</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberManager()">getNumberManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathIcon()">getPathIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">get definition of custom path ending (arrow, circle, icon, etc.) and stroke (dashed, solid, etc.)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReceiver()">getReceiver</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSender()">getSender</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(boolean)">getStroke</a><wbr/>(boolean line)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method must be overridden, if you need to use DASHED_STROKE or another one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(boolean,int)">getStroke</a><wbr/>(boolean line,
 int lineStyle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method must be overridden, if you need to use DASHED_STROKE or another one.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasSharedModelElement()">hasSharedModelElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if <code>ModelElement</code> of this symbol can represented with other symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initialize()">initialize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize symbol and its children state.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies properties from given property manager</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSilentApply()">internalSilentApply</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Silently applies all properties after initialization</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a><wbr/>(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">checks whether object intersects with given rectangle</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowPredecessors()">isShowPredecessors</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#minimumSizeIgnoringOrientation(java.awt.Dimension)">minimumSizeIgnoringOrientation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> min)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelf</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prefDimensionByManipulatedChildren(java.awt.Dimension,int,int)">prefDimensionByManipulatedChildren</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#preferredSizeIgnoringOrientation(java.awt.Dimension,int,int)">preferredSizeIgnoringOrientation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prepareForLineDrawing(java.awt.Graphics2D,boolean)">prepareForLineDrawing</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 boolean line)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Prepares graphics for line drawing.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens for property change it can be: data was edited text box was edited</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#recursiveAutosize()">recursiveAutosize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Resize recursively all symbols.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#resetMessagePositions(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">resetMessagePositions</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resizeParent()">resizeParent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method that initiates parent resize to accommodate children if some child's bounds are
 changed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirection(int)">setDirection</a><wbr/>(int direction)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setMessageLabelNumberText(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.shapes.MessageNameLabelWrapper)">setMessageLabelNumberText</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> owner,
 com.nomagic.magicdraw.uml.symbols.shapes.MessageNameLabelWrapper nameLabelWrapper)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNumberManager(com.nomagic.magicdraw.uml.symbols.MessageNumberManager)">setNumberManager</a><wbr/>(com.nomagic.magicdraw.uml.symbols.MessageNumberManager numberManager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setReceiver(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setReceiver</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> receiver)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSender(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setSender</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> sender)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowPredecessors(boolean)">setShowPredecessors</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets show predecessors list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simpleSetBounds(java.awt.Rectangle,boolean,boolean)">simpleSetBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect,
 boolean moveChildren,
 boolean calculatePrefSize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets bounds for this container shape view and all its components</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetShowPredecessors(boolean)">sSetShowPredecessors</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNameBox()">updateNameBox</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</h3>
<code>createConstraintLabelWrapper, createElementPropertiesLabelWrapper, createStereotypeLabelWrapper, createTaggedValueLabelWrapper, getConstraintLabelBox, getConstraintLabelWrapper, getConstraintTextMode, getDSLStereotypesDisplayMode, getElementNumberDisplayMode, getElementPropertiesLabelBox, getElementPropertiesLabelWrapper, getStereotypeLabelBox, getStereotypeLabelWrapper, getStereotypesDisplayMode, getTaggedValueLabelBox, getTaggedValueLabelWrapper, isShowConstraints, isShowElementProperties, isShowNumberTagName, isShowTaggedValues, setConstraintTextMode, setDSLStereotypesDisplayMode, setShowConstraints, setShowElementProperties, setShowTaggedValues, setStereotypesDisplayMode, sSetConstraintTextMode, sSetDSLStereotypesDisplayMode, sSetElementNumberDisplayMode, sSetShowConstraints, sSetShowElementProperties, sSetShowNumberTagName, sSetShowTaggedValues, sSetStereotypesDisplayMode, updateAfterLoad</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels</h3>
<code>addLabel, asPresentationElement, canBeAutosized, createCompartmentElements, edgeChanged, editName, getCollections, getHeaderBoundsForPreferredBounds, getLabelHandler, getName, getNameLabelBox, internalAppendChildRect, internalPostUpdatePresentationElement, isLabelWrapText, isShowName, isShowText, isWordWrap, removeLabel, setCollections, setName, setNameResizeLabel, setShowName, setSuspendLabelAutoDisplayMode, setSuspendShapeAutoResizeMode, setTextEditable, setVisibleElements, setWordWrap, sSetElement, sSetName, sSetShowName, sSetSuspendLabelAutoDisplayMode, sSetWordWrap</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</h3>
<code>addExtraChildrenPrefSizePadding, adjustBoundsBeforeChange, autosizeAndResizeParent, calculateMinY, calculateOvalShapePreferredSize, correctChildrenVector, createBoundsShape, createStateForUpdateOperation, doInternalLayoutChildren, getAdditionalHeaderHeightForPreferredBounds, getChildrenBoundsForPreferredBounds, getHeaderDistanceFromTopForOvalShape, getHeaderInsets, getHeaderMaxYForShrinkableShape, getHeaderObject, getHeaderVerticalPosition, getHeaderVerticalPositionForLayout, getNameLabel, getOvalShapeAvailableWidth, getPreferredBounds, getPresentationElementAt, getProxyPresentationElementsStream, getStereotypesToDisplay, internalGetHeaderBoundsForPreferredBounds, internalGetHeaderInsets, internalLayoutChildren, internalPostSpecificUpdate, internalPreSpecificUpdate, internalSpecificUpdate, internalUpdatePresentationElement, invalidate, isBorderVisible, isChildLayoutable, isContentHidden, isHeaderOrientationVertical, isOvalShape, isParentShowsProxy, minimumDimension, minimumDimensionForShrinking, minimumSizeForShrinkingIgnoringOrientation, paintChildren, preferredDimension, setHeaderObject, setHeaderVerticalPosition, sSetAutosize, sSetHeaderVerticalPosition, switchWidthHeightIfVerticalOrientation</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</h3>
<code>addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, calculateAutosizeDimension, calculateAutosizeDimension, canAddChild, canMoveChildOutside, childrenBoundsForReshape, clearShowsProxy, constructLayoutHelper, getChildrenBounds, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getRemovableChildren, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildrenBackground, removePresentationElement, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></h3>
<code><a href="ShapeElement.html#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addBreakPoints</a>, <a href="ShapeElement.html#adjustBounds(java.awt.Rectangle)">adjustBounds</a>, <a href="ShapeElement.html#adjustOnEdge()">adjustOnEdge</a>, <a href="ShapeElement.html#adjustOnEdge(java.awt.Rectangle,int,int,int)">adjustOnEdge</a>, <a href="ShapeElement.html#adjustOnEdgeChildren()">adjustOnEdgeChildren</a>, <a href="ShapeElement.html#autosize()">autosize</a>, <a href="ShapeElement.html#calculateAdjustOnEdgeLocation(java.awt.Rectangle)">calculateAdjustOnEdgeLocation</a>, <a href="ShapeElement.html#calculateAndGetMinimumShrinkingDimension(int,int)">calculateAndGetMinimumShrinkingDimension</a>, <a href="ShapeElement.html#calculateAndGetPreferredDimension()">calculateAndGetPreferredDimension</a>, <a href="ShapeElement.html#calculateEdge()">calculateEdge</a>, <a href="ShapeElement.html#calculateMinimumDimension()">calculateMinimumDimension</a>, <a href="ShapeElement.html#calculateOnEdgeBounds()">calculateOnEdgeBounds</a>, <a href="ShapeElement.html#calculatePreferredDimension()">calculatePreferredDimension</a>, <a href="ShapeElement.html#calculatePreferredDimension(int,int)">calculatePreferredDimension</a>, <a href="ShapeElement.html#clearOldRect()">clearOldRect</a>, <a href="ShapeElement.html#ensureDimension(boolean)">ensureDimension</a>, <a href="ShapeElement.html#ensurePreferredDimensionIfShrinkable()">ensurePreferredDimensionIfShrinkable</a>, <a href="ShapeElement.html#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)">ensurePreferredDimensionIfShrinkable</a>, <a href="ShapeElement.html#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)">findFreePlaceForShapeOnBorder</a>, <a href="ShapeElement.html#getBorderElementMargin()">getBorderElementMargin</a>, <a href="ShapeElement.html#getBounds()">getBounds</a>, <a href="ShapeElement.html#getCenterlineableInnerParts(int)">getCenterlineableInnerParts</a>, <a href="ShapeElement.html#getDefaultDimension()">getDefaultDimension</a>, <a href="ShapeElement.html#getDimensionForShrinking(int,int)">getDimensionForShrinking</a>, <a href="ShapeElement.html#getEdgeLine(int)">getEdgeLine</a>, <a href="ShapeElement.html#getFixedConnectionPoints()">getFixedConnectionPoints</a>, <a href="ShapeElement.html#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)">getHeaderInsetReduce</a>, <a href="ShapeElement.html#getInsetsForOnEdgeShapes()">getInsetsForOnEdgeShapes</a>, <a href="ShapeElement.html#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="ShapeElement.html#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)">getIntersection</a>, <a href="ShapeElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="ShapeElement.html#getLoadedDimension()">getLoadedDimension</a>, <a href="ShapeElement.html#getMiddlePoint()">getMiddlePoint</a>, <a href="ShapeElement.html#getMiddlePoint(java.awt.Point)">getMiddlePoint</a>, <a href="ShapeElement.html#getMiddlePointX()">getMiddlePointX</a>, <a href="ShapeElement.html#getMiddlePointX(java.awt.Point)">getMiddlePointX</a>, <a href="ShapeElement.html#getMiddlePointY()">getMiddlePointY</a>, <a href="ShapeElement.html#getMiddlePointY(java.awt.Point)">getMiddlePointY</a>, <a href="ShapeElement.html#getMinimumDimension()">getMinimumDimension</a>, <a href="ShapeElement.html#getNearestEdge(int,int)">getNearestEdge</a>, <a href="ShapeElement.html#getNearestEdge(java.awt.Rectangle)">getNearestEdge</a>, <a href="ShapeElement.html#getNeedAutosizeFlag()">getNeedAutosizeFlag</a>, <a href="ShapeElement.html#getNotCopyBounds()">getNotCopyBounds</a>, <a href="ShapeElement.html#getOnEdge()">getOnEdge</a>, <a href="ShapeElement.html#getOnEdgeCornerDistance()">getOnEdgeCornerDistance</a>, <a href="ShapeElement.html#getOnEdgePosition()">getOnEdgePosition</a>, <a href="ShapeElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="ShapeElement.html#getPreferredDimensionForAutosize()">getPreferredDimensionForAutosize</a>, <a href="ShapeElement.html#getReshapeMode()">getReshapeMode</a>, <a href="ShapeElement.html#getSizeForDrawing()">getSizeForDrawing</a>, <a href="ShapeElement.html#getSuspendShapeAutoResizeMode()">getSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#hasManipulator()">hasManipulator</a>, <a href="ShapeElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a>, <a href="ShapeElement.html#isAutosized()">isAutosized</a>, <a href="ShapeElement.html#isCenterlineInner()">isCenterlineInner</a>, <a href="ShapeElement.html#isHorizontalCenterlineProvider()">isHorizontalCenterlineProvider</a>, <a href="ShapeElement.html#isOnEdge()">isOnEdge</a>, <a href="ShapeElement.html#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isShapeOnEdge</a>, <a href="ShapeElement.html#isShrinkable()">isShrinkable</a>, <a href="ShapeElement.html#isSnapShapesOnBorderToGrid()">isSnapShapesOnBorderToGrid</a>, <a href="ShapeElement.html#isSnapToGrid()">isSnapToGrid</a>, <a href="ShapeElement.html#isUseFixedConnectionPoints()">isUseFixedConnectionPoints</a>, <a href="ShapeElement.html#isVerticalCenterlineProvider()">isVerticalCenterlineProvider</a>, <a href="ShapeElement.html#layoutChildren()">layoutChildren</a>, <a href="ShapeElement.html#maximumDimension(java.awt.Dimension)">maximumDimension</a>, <a href="ShapeElement.html#minimumOrMinimumShrinkableDimension(java.awt.Dimension)">minimumOrMinimumShrinkableDimension</a>, <a href="ShapeElement.html#moveLinksToSelf()">moveLinksToSelf</a>, <a href="ShapeElement.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a>, <a href="ShapeElement.html#movePathElements()">movePathElements</a>, <a href="ShapeElement.html#needAdjustToMaximumDimension()">needAdjustToMaximumDimension</a>, <a href="ShapeElement.html#onChildEdgeChange(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">onChildEdgeChange</a>, <a href="ShapeElement.html#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a>, <a href="ShapeElement.html#providesHorizontalCenterline()">providesHorizontalCenterline</a>, <a href="ShapeElement.html#providesVerticalCenterline()">providesVerticalCenterline</a>, <a href="ShapeElement.html#resetCalculatePreferredRegardingChildren()">resetCalculatePreferredRegardingChildren</a>, <a href="ShapeElement.html#setAutosize(boolean)">setAutosize</a>, <a href="ShapeElement.html#setBorderElementMargin(java.lang.String)">setBorderElementMargin</a>, <a href="ShapeElement.html#setCalculatePreferredRegardingChildren(boolean)">setCalculatePreferredRegardingChildren</a>, <a href="ShapeElement.html#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)">setLoadedDimension</a>, <a href="ShapeElement.html#setMinimumDimension(int,int)">setMinimumDimension</a>, <a href="ShapeElement.html#setNeedAutosizeFlag(byte)">setNeedAutosizeFlag</a>, <a href="ShapeElement.html#setOldRect(java.awt.Rectangle)">setOldRect</a>, <a href="ShapeElement.html#setOnEdge(int)">setOnEdge</a>, <a href="ShapeElement.html#setPreferredDimension(int,int)">setPreferredDimension</a>, <a href="ShapeElement.html#setReshapeMode(com.nomagic.magicdraw.uml.symbols.ReshapeMode)">setReshapeMode</a>, <a href="ShapeElement.html#setSnapShapesOnBorderToGrid(boolean)">setSnapShapesOnBorderToGrid</a>, <a href="ShapeElement.html#setUseFixedConnectionPoints(boolean)">setUseFixedConnectionPoints</a>, <a href="ShapeElement.html#shouldDrawShadow()">shouldDrawShadow</a>, <a href="ShapeElement.html#simpleSetBounds(int,int,int,int,boolean)">simpleSetBounds</a>, <a href="ShapeElement.html#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a>, <a href="ShapeElement.html#snapsToCenterlines()">snapsToCenterlines</a>, <a href="ShapeElement.html#sSetBorderElementMargin(java.lang.String)">sSetBorderElementMargin</a>, <a href="ShapeElement.html#sSetBounds(java.awt.Rectangle)">sSetBounds</a>, <a href="ShapeElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)">sSetSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a>, <a href="ShapeElement.html#toString()">toString</a>, <a href="ShapeElement.html#updateLater()">updateLater</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addConnectedPathElement</a>, <a href="../paths/PathConnector.html#dispose()">dispose</a>, <a href="../paths/PathConnector.html#disposeConnectedPaths()">disposeConnectedPaths</a>, <a href="../paths/PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">findSymbolForEnd</a>, <a href="../paths/PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)">findSymbolForEnd</a>, <a href="../paths/PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">getConnectedPathElement</a>, <a href="../paths/PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="../paths/PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getPreferredArrowLength()">getPreferredArrowLength</a>, <a href="../paths/PathConnector.html#isShowsProxy()">isShowsProxy</a>, <a href="../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)">movePathElement</a>, <a href="../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">removeConnectedPathElement</a>, <a href="../paths/PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sAddConnectedPathElement</a>, <a href="../paths/PathConnector.html#selectPathsForMoving(java.util.List)">selectPathsForMoving</a>, <a href="../paths/PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a>, <a href="../paths/PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a>, <a href="../paths/PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sRemoveConnectedPathElement</a>, <a href="../paths/PathConnector.html#sSetConnectedPathElements(java.util.List)">sSetConnectedPathElements</a>, <a href="../paths/PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible()">supportsVisibleConnectedPathElementsIfSelfInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a>, <a href="../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBounds</a>, <a href="../PresentationElement.html#alwaysShowTooltip()">alwaysShowTooltip</a>, <a href="../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">applyProperties</a>, <a href="../PresentationElement.html#askDeleteDataConfirmation()">askDeleteDataConfirmation</a>, <a href="../PresentationElement.html#atInsert()">atInsert</a>, <a href="../PresentationElement.html#atInsertChildren()">atInsertChildren</a>, <a href="../PresentationElement.html#autosizeAndResizeManipulatedParent()">autosizeAndResizeManipulatedParent</a>, <a href="../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">beforeDelete</a>, <a href="../PresentationElement.html#boundsChanged()">boundsChanged</a>, <a href="../PresentationElement.html#boundsChanged(java.awt.Rectangle)">boundsChanged</a>, <a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../PresentationElement.html#canBeDisposedOnUpdate()">canBeDisposedOnUpdate</a>, <a href="../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeElementOwner</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../PresentationElement.html#canFill()">canFill</a>, <a href="../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">changeProperties</a>, <a href="../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a>, <a href="../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">checkProxyVisibility</a>, <a href="../PresentationElement.html#childrenForMoving()">childrenForMoving</a>, <a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)">collectSubShowingPresentationElements</a>, <a href="../PresentationElement.html#coversPoint(int,int)">coversPoint</a>, <a href="../PresentationElement.html#createFillStrategy()">createFillStrategy</a>, <a href="../PresentationElement.html#createPresentationElementStyle()">createPresentationElementStyle</a>, <a href="../PresentationElement.html#createPropertyChangeListener()">createPropertyChangeListener</a>, <a href="../PresentationElement.html#disposeChildren()">disposeChildren</a>, <a href="../PresentationElement.html#disposePropertyChangeListener()">disposePropertyChangeListener</a>, <a href="../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a>, <a href="../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawBackground</a>, <a href="../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbol</a>, <a href="../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbolBackground</a>, <a href="../PresentationElement.html#dynamicFillColor()">dynamicFillColor</a>, <a href="../PresentationElement.html#dynamicLineColor()">dynamicLineColor</a>, <a href="../PresentationElement.html#dynamicLineWidth()">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicLineWidth(int)">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicPaintShadow()">dynamicPaintShadow</a>, <a href="../PresentationElement.html#dynamicStroke()">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(int)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)">dynamicStyleFillColor</a>, <a href="../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)">dynamicStyleLineColor</a>, <a href="../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)">dynamicStyleTextColor</a>, <a href="../PresentationElement.html#dynamicStyleTransparency()">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)">dynamicStyleValue</a>, <a href="../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">dynamicTextAlignment</a>, <a href="../PresentationElement.html#dynamicTextColor()">dynamicTextColor</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOwnerForChildElement</a>, <a href="../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">findPresentationElement</a>, <a href="../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../PresentationElement.html#generateID()">generateID</a>, <a href="../PresentationElement.html#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>, <a href="../PresentationElement.html#getActualElement()">getActualElement</a>, <a href="../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()">getAdditionalRenderersToNotifyOnPropertiesChange</a>, <a href="../PresentationElement.html#getAssignableModelElementsClasses()">getAssignableModelElementsClasses</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getBoundsWithChildrenOnEdge()">getBoundsWithChildrenOnEdge</a>, <a href="../PresentationElement.html#getCenterlinePoint()">getCenterlinePoint</a>, <a href="../PresentationElement.html#getCenterlinePointX()">getCenterlinePointX</a>, <a href="../PresentationElement.html#getCenterlinePointY()">getCenterlinePointY</a>, <a href="../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)">getChildPresentationElementForContextMenu</a>, <a href="../PresentationElement.html#getChildrenWithSymbolProperties()">getChildrenWithSymbolProperties</a>, <a href="../PresentationElement.html#getConfiguration()">getConfiguration</a>, <a href="../PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="../PresentationElement.html#getDiagramSurface()">getDiagramSurface</a>, <a href="../PresentationElement.html#getDrawComparator()">getDrawComparator</a>, <a href="../PresentationElement.html#getDynamicConfigurations()">getDynamicConfigurations</a>, <a href="../PresentationElement.html#getDynamicStyleOwner()">getDynamicStyleOwner</a>, <a href="../PresentationElement.html#getEffectiveStyleDelegate()">getEffectiveStyleDelegate</a>, <a href="../PresentationElement.html#getEffectiveStyleOwner()">getEffectiveStyleOwner</a>, <a href="../PresentationElement.html#getElementsForRelationshipConnecting()">getElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementToConnectRelationship</a>, <a href="../PresentationElement.html#getFillColor()">getFillColor</a>, <a href="../PresentationElement.html#getFont()">getFont</a>, <a href="../PresentationElement.html#getFontHeight()">getFontHeight</a>, <a href="../PresentationElement.html#getFontRenderContext()">getFontRenderContext</a>, <a href="../PresentationElement.html#getHumanName()">getHumanName</a>, <a href="../PresentationElement.html#getHumanType()">getHumanType</a>, <a href="../PresentationElement.html#getLineColor()">getLineColor</a>, <a href="../PresentationElement.html#getLineWidth()">getLineWidth</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getManipulationBounds(java.awt.Point)">getManipulationBounds</a>, <a href="../PresentationElement.html#getModelElement()">getModelElement</a>, <a href="../PresentationElement.html#getModelElementsForRelationshipConnecting()">getModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">getModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#getModelElementToMove()">getModelElementToMove</a>, <a href="../PresentationElement.html#getNotZoomedTolerance()">getNotZoomedTolerance</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getOwnStyleDelegate()">getOwnStyleDelegate</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a>, <a href="../PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="../PresentationElement.html#getPresentationElementAt(int)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementCount()">getPresentationElementCount</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getProjectImpl()">getProjectImpl</a>, <a href="../PresentationElement.html#getProperty(java.lang.String)">getProperty</a>, <a href="../PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="../PresentationElement.html#getPropertyManagerName()">getPropertyManagerName</a>, <a href="../PresentationElement.html#getRenderer()">getRenderer</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#getStyle()">getStyle</a>, <a href="../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSymbolRenderer</a>, <a href="../PresentationElement.html#getTextColor()">getTextColor</a>, <a href="../PresentationElement.html#getTolerance()">getTolerance</a>, <a href="../PresentationElement.html#getVisibility()">getVisibility</a>, <a href="../PresentationElement.html#getVisiblePresentationElements()">getVisiblePresentationElements</a>, <a href="../PresentationElement.html#handleModelDelete()">handleModelDelete</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#initializeAndAutosize()">initializeAndAutosize</a>, <a href="../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)">internalBeforeUpdate</a>, <a href="../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">internalCreatePropertyChangeListener</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a>, <a href="../PresentationElement.html#internalGetSpecificFont()">internalGetSpecificFont</a>, <a href="../PresentationElement.html#internalGetSpecificTextColor()">internalGetSpecificTextColor</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalSnapToGrid(float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#intersects(int,int,int,int)">intersects</a>, <a href="../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildVisible</a>, <a href="../PresentationElement.html#isCreateElementListener()">isCreateElementListener</a>, <a href="../PresentationElement.html#isDetectable()">isDetectable</a>, <a href="../PresentationElement.html#isDisposed()">isDisposed</a>, <a href="../PresentationElement.html#isLayouting()">isLayouting</a>, <a href="../PresentationElement.html#isMovableByMoveManager()">isMovableByMoveManager</a>, <a href="../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNotNull</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isParentOf</a>, <a href="../PresentationElement.html#isPreserveProportionsWhenGrowing()">isPreserveProportionsWhenGrowing</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#isShowElementTypeAsLabel()">isShowElementTypeAsLabel</a>, <a href="../PresentationElement.html#isSortable()">isSortable</a>, <a href="../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">isSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#isTextEditable()">isTextEditable</a>, <a href="../PresentationElement.html#isUseFillColor()">isUseFillColor</a>, <a href="../PresentationElement.html#isUseFillColorByProperty()">isUseFillColorByProperty</a>, <a href="../PresentationElement.html#isUseGradientForFill()">isUseGradientForFill</a>, <a href="../PresentationElement.html#isVisible()">isVisible</a>, <a href="../PresentationElement.html#isVisibleInDiagram()">isVisibleInDiagram</a>, <a href="../PresentationElement.html#isVisibleOrShrunken()">isVisibleOrShrunken</a>, <a href="../PresentationElement.html#movePathElementsRecursively()">movePathElementsRecursively</a>, <a href="../PresentationElement.html#mustShowContextMenu()">mustShowContextMenu</a>, <a href="../PresentationElement.html#notifyCreated()">notifyCreated</a>, <a href="../PresentationElement.html#notifyDiagramFrameSizeChange()">notifyDiagramFrameSizeChange</a>, <a href="../PresentationElement.html#notifyRepaintManager(boolean)">notifyRepaintManager</a>, <a href="../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildAdd</a>, <a href="../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildRemove</a>, <a href="../PresentationElement.html#onDiagramSurfaceSet()">onDiagramSurfaceSet</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#onFontChange()">onFontChange</a>, <a href="../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">onParentChange</a>, <a href="../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornments</a>, <a href="../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornmentsBackground</a>, <a href="../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenAndAdornments</a>, <a href="../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelfBackground</a>, <a href="../PresentationElement.html#preDisposeOnUpdate()">preDisposeOnUpdate</a>, <a href="../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)">prepareForLineDrawing</a>, <a href="../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)">prepareForTextDrawing</a>, <a href="../PresentationElement.html#recreateListeners()">recreateListeners</a>, <a href="../PresentationElement.html#registerInSortManager()">registerInSortManager</a>, <a href="../PresentationElement.html#rememberBounds()">rememberBounds</a>, <a href="../PresentationElement.html#rememberBounds(java.awt.Rectangle)">rememberBounds</a>, <a href="../PresentationElement.html#removeFromSortManager()">removeFromSortManager</a>, <a href="../PresentationElement.html#removeItSelfOnUpdate()">removeItSelfOnUpdate</a>, <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sAddPresentationElement</a>, <a href="../PresentationElement.html#selectChildrenForMoving()">selectChildrenForMoving</a>, <a href="../PresentationElement.html#selectObjectsForMoving()">selectObjectsForMoving</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setBounds(int,int,int,int)">setBounds</a>, <a href="../PresentationElement.html#setCreateElementListener(boolean)">setCreateElementListener</a>, <a href="../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a>, <a href="../PresentationElement.html#setFont(java.awt.Font)">setFont</a>, <a href="../PresentationElement.html#setLayouting(boolean)">setLayouting</a>, <a href="../PresentationElement.html#setLineColor(java.awt.Color)">setLineColor</a>, <a href="../PresentationElement.html#setLineWidth(int)">setLineWidth</a>, <a href="../PresentationElement.html#setLoadedVisibility(boolean)">setLoadedVisibility</a>, <a href="../PresentationElement.html#setLocation(int,int)">setLocation</a>, <a href="../PresentationElement.html#setLocation(java.awt.Point)">setLocation</a>, <a href="../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">setModelElement</a>, <a href="../PresentationElement.html#setNeedRecreateListeners(boolean)">setNeedRecreateListeners</a>, <a href="../PresentationElement.html#setPropertyManagerName(java.lang.String)">setPropertyManagerName</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#setSize(int,int)">setSize</a>, <a href="../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)">setSize</a>, <a href="../PresentationElement.html#setSize(java.awt.Dimension)">setSize</a>, <a href="../PresentationElement.html#setTextColor(java.awt.Color)">setTextColor</a>, <a href="../PresentationElement.html#setUseFillColor(boolean)">setUseFillColor</a>, <a href="../PresentationElement.html#setVisible(boolean)">setVisible</a>, <a href="../PresentationElement.html#silentApply()">silentApply</a>, <a href="../PresentationElement.html#silentApply(boolean)">silentApply</a>, <a href="../PresentationElement.html#simpleSetBounds(int,int,int,int)">simpleSetBounds</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Point,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapViewToGrid(float)">snapViewToGrid</a>, <a href="../PresentationElement.html#sortObjectsByX(java.util.List)">sortObjectsByX</a>, <a href="../PresentationElement.html#sortObjectsByY(java.util.List)">sortObjectsByY</a>, <a href="../PresentationElement.html#sSetBounds(int,int,int,int)">sSetBounds</a>, <a href="../PresentationElement.html#sSetLocation(int,int)">sSetLocation</a>, <a href="../PresentationElement.html#sSetLocation(java.awt.Point)">sSetLocation</a>, <a href="../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">sSetModelElement</a>, <a href="../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a>, <a href="../PresentationElement.html#sSetParentForAll(java.util.Collection)">sSetParentForAll</a>, <a href="../PresentationElement.html#sSetSize(int,int)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(java.awt.Dimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetVisible(boolean)">sSetVisible</a>, <a href="../PresentationElement.html#tryToDeleteModelElementUponRemoval()">tryToDeleteModelElementUponRemoval</a>, <a href="../PresentationElement.html#update()">update</a>, <a href="../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)">updateLabelsIgnoringSuspendableLater</a>, <a href="../PresentationElement.html#updateModelByView()">updateModelByView</a>, <a href="../PresentationElement.html#updateModelByViewInternal()">updateModelByViewInternal</a>, <a href="../PresentationElement.html#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a>, <a href="../PresentationElement.html#useParentProperties()">useParentProperties</a>, <a href="../PresentationElement.html#useParentStyle()">useParentStyle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID</code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathCustomDraw">Methods inherited from interface com.nomagic.magicdraw.uml.symbols.paths.PathCustomDraw</h3>
<code>getLineWidth</code></div>
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
<section class="detail" id="TO_RIGHT">
<h3>TO_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TO_RIGHT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.MessageView.TO_RIGHT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TO_LEFT">
<h3>TO_LEFT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TO_LEFT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.MessageView.TO_LEFT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DISTANCE_FROM_LINK">
<h3>DISTANCE_FROM_LINK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DISTANCE_FROM_LINK</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.MessageView.DISTANCE_FROM_LINK">Constant Field Values</a></li>
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
<h3>MessageView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MessageView</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>MessageView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MessageView</span><wbr/><span class="parameters">(@CheckForNull
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
<section class="detail" id="getNameLabelWrapper()">
<h3>getNameLabelWrapper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.MessageNameLabelWrapper</span> <span class="element-name">getNameLabelWrapper</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getNameLabelWrapper</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMessageSignatureLabelBox()">
<h3>getMessageSignatureLabelBox</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.MessageSignatureView</span> <span class="element-name">getMessageSignatureLabelBox</span>()</div>
<div class="block">Returns the signature view from the
 container of this message. Data flows are
 contained in it too.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the <code>MessageSignatureView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNameBox()">
<h3>updateNameBox</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateNameBox</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>updateNameBox</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</code></dd>
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
<section class="detail" id="constructMessageText(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message,boolean)">
<h3>constructMessageText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructMessageText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> message,
 boolean showAttributesAndParameters)</span></div>
</section>
</li>
<li>
<section class="detail" id="setMessageLabelNumberText(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.shapes.MessageNameLabelWrapper)">
<h3>setMessageLabelNumberText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setMessageLabelNumberText</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> owner,
 com.nomagic.magicdraw.uml.symbols.shapes.MessageNameLabelWrapper nameLabelWrapper)</span></div>
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
<dd><code>preferredSizeIgnoringOrientation</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
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
<section class="detail" id="simpleSetBounds(java.awt.Rectangle,boolean,boolean)">
<h3>simpleSetBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">simpleSetBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect,
 boolean moveChildren,
 boolean calculatePrefSize)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></span></div>
<div class="block">Sets bounds for this container shape view and all its components</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>simpleSetBounds</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels</code></dd>
<dt>Parameters:</dt>
<dd><code>rect</code> - container shape view bounding rectangle</dd>
<dd><code>moveChildren</code> - if moveChildren equals true then this method calls</dd>
<dd><code>calculatePrefSize</code> - calculate preferred size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNearestLinkPart(int,int)">
<h3>getNearestLinkPart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../awt/Line.html" title="class in com.nomagic.awt">Line</a></span> <span class="element-name">getNearestLinkPart</span><wbr/><span class="parameters">(int x,
 int y)</span></div>
<div class="block">Returns nearest link part to specified point.</div>
</section>
</li>
<li>
<section class="detail" id="addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,boolean)">
<h3>addPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPresentationElement</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index,
 boolean resize)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></span></div>
<div class="block">If a specified object not inserted in this container then adds a new object view to the container.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>addPresentationElement</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - new PresentationElement object</dd>
<dd><code>index</code> - index to add at</dd>
<dd><code>resize</code> - resize parent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dynamicPathIcon()">
<h3>dynamicPathIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon</span> <span class="element-name">dynamicPathIcon</span>()</div>
</section>
</li>
<li>
<section class="detail" id="dynamicPathIcon(com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon)">
<h3>dynamicPathIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon</span> <span class="element-name">dynamicPathIcon</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon pathIcon)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPathIcon()">
<h3>getPathIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon</span> <span class="element-name">getPathIcon</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.uml.symbols.paths.PathCustomDraw</code></span></div>
<div class="block">get definition of custom path ending (arrow, circle, icon, etc.) and stroke (dashed, solid, etc.)</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getPathIcon</code> in interface <code>com.nomagic.magicdraw.uml.symbols.paths.PathCustomDraw</code></dd>
<dt>Returns:</dt>
<dd>custom path end draw, null if not specified</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><code>PathIcon</code></li>
</ul>
</dd>
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
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MessageView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">MessageView</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#clone()">clone</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>clone</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</code></dd>
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
<dd><code>canAddInstance</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels</code></dd>
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
<section class="detail" id="resizeParent()">
<h3>resizeParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resizeParent</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#resizeParent()">PresentationElement</a></code></span></div>
<div class="block">Method that initiates parent resize to accommodate children if some child's bounds are
 changed.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#resizeParent()">resizeParent</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prefDimensionByManipulatedChildren(java.awt.Dimension,int,int)">
<h3>prefDimensionByManipulatedChildren</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">prefDimensionByManipulatedChildren</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>prefDimensionByManipulatedChildren</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="autosizeByChildren(boolean)">
<h3>autosizeByChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">autosizeByChildren</span><wbr/><span class="parameters">(boolean calculatePrefSize)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>autosizeByChildren</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="autosize(boolean)">
<h3>autosize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">autosize</span><wbr/><span class="parameters">(boolean calculatePrefSize)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="ShapeElement.html#autosize(boolean)">ShapeElement</a></code></span></div>
<div class="block">Calculate preferred size and make this shape size at least as preferred (if size is smaller)</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>autosize</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractHeaderShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>calculatePrefSize</code> - calculate preferred size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initialize()">
<h3>initialize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">initialize</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#initialize()">PresentationElement</a></code></span></div>
<div class="block">Initialize symbol and its children state. Symbol must be initialized before doing any
 resize, painting and etc. These operations can lead to unpredictable results otherwise.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#initialize()">initialize</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="recursiveAutosize()">
<h3>recursiveAutosize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">recursiveAutosize</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#recursiveAutosize()">PresentationElement</a></code></span></div>
<div class="block">Resize recursively all symbols. Method must be called if something is changed in symbol (for
 example minimum size) and you want to resize (autosize) all hierarchy</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>recursiveAutosize</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirection(int)">
<h3>setDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirection</span><wbr/><span class="parameters">(int direction)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDirection()">
<h3>getDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDirection</span>()</div>
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
<section class="detail" id="getBoundsToRepaint()">
<h3>getBoundsToRepaint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBoundsToRepaint</span>()
                             throws <span class="exceptions"><a href="../NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getBoundsToRepaint()">PresentationElement</a></code></span></div>
<div class="block">Return bounds of the symbol that must be repainted. throws NoRectangleDefinedException</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getBoundsToRepaint</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.AbstractShapeWithLabels</code></dd>
<dt>Returns:</dt>
<dd>rectangle of bounds</dd>
<dt>Throws:</dt>
<dd><code><a href="../NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></code></dd>
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
<dd><code>internalApplyProperties</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</code></dd>
<dt>Parameters:</dt>
<dd><code>changer</code> - new properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalSilentApply()">
<h3>internalSilentApply</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalSilentApply</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#internalSilentApply()">PresentationElement</a></code></span></div>
<div class="block">Silently applies all properties after initialization</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalSilentApply</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ShapeWithLabels</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetShowPredecessors(boolean)">
<h3>sSetShowPredecessors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetShowPredecessors</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowPredecessors(boolean)">
<h3>setShowPredecessors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowPredecessors</span><wbr/><span class="parameters">(boolean show)</span></div>
<div class="block">Sets show predecessors list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>show</code> - show list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowPredecessors()">
<h3>isShowPredecessors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowPredecessors</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>show predecessors property value.</dd>
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
<li>
<section class="detail" id="resetMessagePositions(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>resetMessagePositions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetMessagePositions</span><wbr/><span class="parameters">(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</span></div>
</section>
</li>
<li>
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">getElement</span>()</div>
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
<section class="detail" id="getMessage()">
<h3>getMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">getMessage</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../NumberedMessageView.html#getMessage()">NumberedMessageView</a></code></span></div>
<div class="block">Message represented by the view.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../NumberedMessageView.html#getMessage()">getMessage</a></code> in interface <code><a href="../NumberedMessageView.html" title="interface in com.nomagic.magicdraw.uml.symbols">NumberedMessageView</a></code></dd>
<dt>Returns:</dt>
<dd>message represented by the view</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNumber()">
<h3>getNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getNumber</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../NumberedMessageView.html#getNumber()">NumberedMessageView</a></code></span></div>
<div class="block">Returns number of the message</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../NumberedMessageView.html#getNumber()">getNumber</a></code> in interface <code><a href="../NumberedMessageView.html" title="interface in com.nomagic.magicdraw.uml.symbols">NumberedMessageView</a></code></dd>
<dt>Returns:</dt>
<dd>nested number of the message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNumberManager()">
<h3>getNumberManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.MessageNumberManager</span> <span class="element-name">getNumberManager</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setNumberManager(com.nomagic.magicdraw.uml.symbols.MessageNumberManager)">
<h3>setNumberManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNumberManager</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.MessageNumberManager numberManager)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSender()">
<h3>getSender</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getSender</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getReceiver()">
<h3>getReceiver</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getReceiver</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setReceiver(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>setReceiver</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setReceiver</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> receiver)</span></div>
</section>
</li>
<li>
<section class="detail" id="setSender(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>setSender</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSender</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> sender)</span></div>
</section>
</li>
<li>
<section class="detail" id="getConnector()">
<h3>getConnector</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../paths/ConnectorView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ConnectorView</a></span> <span class="element-name">getConnector</span>()</div>
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
<section class="detail" id="checkShowsProxy()">
<h3>checkShowsProxy</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">checkShowsProxy</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>checkShowsProxy</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildrenInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel)">
<h3>getChildrenInsets</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.ui.UnmodifiableInsets</span> <span class="element-name">getChildrenInsets</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getChildrenInsets</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>insetsLevel</code> - describes the level of insets</dd>
<dt>Returns:</dt>
<dd>shape insets for children</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStroke(boolean,int)">
<h3>getStroke</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(boolean line,
 int lineStyle)</span></div>
<div class="block">This method must be overridden, if you need to use DASHED_STROKE or another one.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the stroke for line drawing ( by default SOLID_STROKE).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prepareForLineDrawing(java.awt.Graphics2D,boolean)">
<h3>prepareForLineDrawing</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">prepareForLineDrawing</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 boolean line)</span></div>
<div class="block">Prepares graphics for line drawing.
 Calls super prepareForLineDrawing and sets stroke.</div>
</section>
</li>
<li>
<section class="detail" id="getStroke(boolean)">
<h3>getStroke</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(boolean line)</span></div>
<div class="block">This method must be overridden, if you need to use DASHED_STROKE or another one.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the stroke for line drawing ( by default SOLID_STROKE).</dd>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
