# JAVA OPENAPI: LifeLineLineView (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/shapes/LifeLineLineView.html
- source_path: `com/nomagic/magicdraw/uml/symbols/shapes/LifeLineLineView.html`
- source_sha256: `11525b66811763d50cf27cda0e88bde444964eaeb7ce05630a61d0c0a494ab80`
- captured_utc: `2026-07-14T16:56:05.365568+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.shapes](package-summary.html)

## Class LifeLineLineView

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](../paths/PathConnector.html)
[com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement](ShapeElement.html)
com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView

All Implemented Interfaces:
`[BaseElement](../../BaseElement.html)`, `[MDElement](../../MDElement.html)`, `[ModelElementProvider](../../ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`, `com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApipublic classLifeLineLineView
extends com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView

Life line line in sequence diagram.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[CROSS_DELTA](#CROSS_DELTA)`

`static final int`
`[CROSS_WIDTH](#CROSS_WIDTH)`
cross width
`static final int`
`[DELTA_X](#DELTA_X)`

`static final int`
`[DELTA_Y](#DELTA_Y)`
constants for concurrent lifeline dimensions
`static final int`
`[MIN_EXTENSION](#MIN_EXTENSION)`
Minimal extension of lifeline line.
`static final int`
`[MIN_LENGTH](#MIN_LENGTH)`
Minimal length of lifeline line.
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
`[LifeLineLineView](#%3Cinit%3E())()`
Creates a new life line view.
`[LifeLineLineView](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) parent)`
Creates and initializes a new life line view from specified parameter.
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
`[addPresentationElement](#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,boolean))([PresentationElement](../PresentationElement.html) element,
 int index,
 boolean resize)`
If a specified object not inserted in this container then adds a new object view to the container.
`void`
`[adjustBounds](#adjustBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`
Adjust bounds
 1.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[adjustBoundsBeforeChange](#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rec,
 boolean autosizeOperation,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)> movedTogether)`
validate bounds for moving
`void`
`[atInsert](#atInsert())()`
Invalidates object at insert
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[calculateActivationsBounds](#calculateActivationsBounds())()`

`void`
`[calculateAutosizeDimension](#calculateAutosizeDimension(java.awt.Dimension,int,int,int,int))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size,
 int locationX,
 int locationY,
 int prefSizeWidth,
 int prefSizeHeight)`
Calculates size of shape to be at least as preferred and fit all children
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[calculateDestroyTimePoint](#calculateDestroyTimePoint())()`

`boolean`
`[canAddChild](#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) symbol)`
Check of given symbol can be added as child into this symbol.
`boolean`
`[canAddInstance](#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) symbol)`
Checks can this life line view add specified object or not.
`boolean`
`[checkElementOwnerOnChange](#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) child)`

`[LifeLineLineView](LifeLineLineView.html)`
`[clone](#clone())()`
Clones this object.
`void`
`[correctInnerStateInvariantBounds](#correctInnerStateInvariantBounds())()`
Adjust bounds of inner state invariants according bounds of this lifeline.
`boolean`
`[correctStateInvariantBounds](#correctStateInvariantBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`
Adjusts bounds of a given state invariant so that it lies correctly on
 this lifeline line.
`boolean`
`[coversPoint](#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
checks if object covers provided point
`[ContainerShape](../../../../awt/ContainerShape.html)`
`[createBoundsShape](#createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation))([PathElement](../paths/PathElement.html) path,
 [BoundsTransformation](../BoundsTransformation.html) transformation)`
Creates bounding shape for intersection calculation.
`void`
`[dispose](#dispose())()`
disposes ends of links when link is deleted
`protected void`
`[disposeChildren](#disposeChildren())()`
Removes all children from itself.
`[BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[dynamicStroke](#dynamicStroke(java.awt.BasicStroke))([BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) stroke)`

`void`
`[editName](#editName(java.awt.event.KeyEvent,java.util.Map))([KeyEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/KeyEvent.html) evt,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> textEditorOptions)`
Does nothing -- prevent from editing name box,
 which is an attribute of container.
`boolean`
`[ensureDestructionOccurrence](#ensureDestructionOccurrence(boolean))(boolean destruct)`
Ensures that a proper destruction occurrence is in the model on this lifeline.
`[ActivationView](ActivationView.html)`
`[getActivationAt](#getActivationAt(int))(int y)`
Returns Activation at specified point.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ActivationView](ActivationView.html)>`
`[getActivations](#getActivations())()`
Gets activations placed on this lifeline line.
`[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[ActivationView](ActivationView.html)>`
`[getActivationsIterator](#getActivationsIterator())()`

`[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getActualElement](#getActualElement())()`
Because some views returns theirs parent model element, we do not know have they this member
 set or not.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView>`
`[getAllMessages](#getAllMessages())()`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBoundsToRepaint](#getBoundsToRepaint())()`
Return bounds of the symbol that must be repainted.
`com.nomagic.ui.UnmodifiableInsets`
`[getChildrenInsets](#getChildrenInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel))(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)`

`[ActivationView](ActivationView.html)`
`[getClosestActivationAt](#getClosestActivationAt(int))(int ptY)`
Finds closest activation on this lifeline line at a given point.
`[PresentationElement](../PresentationElement.html)`
`[getDynamicStyleOwner](#getDynamicStyleOwner())()`

`[Lifeline](../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html)`
`[getElement](#getElement())()`
returns parent data
`com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView`
`[getIncomingMessageWithType](#getIncomingMessageWithType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort))([MessageSort](../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageSort.html) type)`

`[ActivationView](ActivationView.html)`
`[getLastActivation](#getLastActivation())()`
Returns last activation.
`[StateInvariantView](StateInvariantView.html)`
`[getLastStateInvariant](#getLastStateInvariant())()`
Returns last state invariant.
`int`
`[getLastStateInvariantPosition](#getLastStateInvariantPosition())()`
Calculates y coordinate of this lifeline line to cover the last state invariant
 lying on it.
`[Lifeline](../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html)`
`[getLifeline](#getLifeline())()`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getManipulationBounds](#getManipulationBounds(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint)`
Gets manipulation bounds of the symbol.
`int`
`[getMiddlePointX](#getMiddlePointX())()`

`int`
`[getMiddlePointY](#getMiddlePointY(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[LifeLineLineView](LifeLineLineView.html)>`
`[getNestedLines](#getNestedLines())()`
Returns nested lifeline lines.
`[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[LifeLineLineView](LifeLineLineView.html)>`
`[getNestedLinesIterator](#getNestedLinesIterator())()`

`protected int`
`[getNotZoomedTolerance](#getNotZoomedTolerance())()`

`[SequenceLifelineView](SequenceLifelineView.html)`
`[getObject](#getObject())()`

`[PresentationElement](../PresentationElement.html)`
`[getParentSymbolStyleOwner](#getParentSymbolStyleOwner())()`
Returns parent to which this symbol delegates style attributes related functionality.
`[PresentationElement](../PresentationElement.html)`
`[getPresentationElementAt](#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Searches and returns object that covers given point.
`com.nomagic.magicdraw.uml.symbols.SequenceObjectViewContainer`
`[getSeqContainer](#getSeqContainer())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ActivationView](ActivationView.html)>`
`[getSortedActivations](#getSortedActivations())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[StateInvariantView](StateInvariantView.html)>`
`[getStateInvariants](#getStateInvariants())()`
Gets state invariants lying on this lifeline line.
`int`
`[getUpperPointY](#getUpperPointY())()`

`boolean`
`[hasStateInvariants](#hasStateInvariants())()`
Indicates if this life line has any state invariants on it.
`protected [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[internalGetManipulatedChildrenRect](#internalGetManipulatedChildrenRect(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel))(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)`
Calculate union area of owned manipulated children added not on a shape border
`[BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[internalGetPresentationElementStroke](#internalGetPresentationElementStroke(int))(int width)`
Return a stroke used to paint symbol's main part
`void`
`[internalLayoutChildren](#internalLayoutChildren(boolean))(boolean calculatePrefSize)`

`protected void`
`[internalUpdatePresentationElement](#internalUpdatePresentationElement())()`
Internal symbol update method for subclassing.
`boolean`
`[isConcurrent](#isConcurrent())()`

`boolean`
`[isDestroyed](#isDestroyed())()`
Gets destroyed value.
`boolean`
`[isHidden](#isHidden())()`

`boolean`
`[isMovableByMoveManager](#isMovableByMoveManager())()`
Method indicates if object of this instance must be registered in move manager.
`boolean`
`[isNested](#isNested())()`
Indicates if this lifeline line is nested (not root).
`protected boolean`
`[isSnapToGrid](#isSnapToGrid())()`

`boolean`
`[isUseEntireActivation](#isUseEntireActivation())()`

`void`
`[moveChild](#moveChild(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,int))([PresentationElement](../PresentationElement.html) view,
 int dx,
 int dy)`

`protected void`
`[movePathElement](#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector))([PathElement](../paths/PathElement.html) lnk,
 [PathConnector](../paths/PathConnector.html) requestor)`
Calculates position of a path element.
`boolean`
`[mustShowContextMenu](#mustShowContextMenu())()`

`protected boolean`
`[needAdjustToPreferred](#needAdjustToPreferred())()`
Check if shape can be resized to a preferred size.
`void`
`[paintChildren](#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`void`
`[paintSelf](#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`protected void`
`[preferredDimension](#preferredDimension(java.awt.Dimension,int,int))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)`

`void`
`[rememberBounds](#rememberBounds())()`
Remember old bounds
`void`
`[rememberBounds](#rememberBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`

`void`
`[removePresentationElement](#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean))([PresentationElement](../PresentationElement.html) element,
 boolean resizeParent)`
Removes object view from container.
`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](../paths/PathElement.html)>`
`[selectPathsForMoving](#selectPathsForMoving(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../PresentationElement.html)> subPresentationElements)`
Select paths to move with current symbol from deep structure.
`void`
`[setConcurrent](#setConcurrent(boolean))(boolean concurrent)`

`void`
`[setElement](#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) el)`

`void`
`[setHidden](#setHidden(boolean))(boolean hidden)`

`void`
`[setPosition](#setPosition())()`
Sets life line view position depending on this object parent position.
`void`
`[simpleSetBounds](#simpleSetBounds(java.awt.Rectangle,boolean,boolean))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rct,
 boolean moveChildren,
 boolean calculatePrefSize)`
Sets bounds for this container shape view and all its components
`void`
`[sRemovePresentationElement](#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) element)`
Removes given child
`void`
`[sSetElement](#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) el)`

`boolean`
`[useParentStyle](#useParentStyle())()`
Use parent font always
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosize, autosizeByChildren, calculateAutosizeDimension, canMoveChildOutside, checkShowsProxy, childrenBoundsForReshape, clearShowsProxy, constructLayoutHelper, correctChildrenVector, getChildrenBounds, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getProxyPresentationElementsStream, getRemovableChildren, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalAppendChildRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChildren, paintChildrenBackground, prefDimensionByManipulatedChildren, recursiveAutosize, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, sSetPresentationElements`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.[ShapeElement](ShapeElement.html)
`[addBreakPoints](ShapeElement.html#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [adjustOnEdge](ShapeElement.html#adjustOnEdge()), [adjustOnEdge](ShapeElement.html#adjustOnEdge(java.awt.Rectangle,int,int,int)), [adjustOnEdgeChildren](ShapeElement.html#adjustOnEdgeChildren()), [autosize](ShapeElement.html#autosize()), [autosizeAndResizeParent](ShapeElement.html#autosizeAndResizeParent()), [calculateAdjustOnEdgeLocation](ShapeElement.html#calculateAdjustOnEdgeLocation(java.awt.Rectangle)), [calculateAndGetMinimumShrinkingDimension](ShapeElement.html#calculateAndGetMinimumShrinkingDimension(int,int)), [calculateAndGetPreferredDimension](ShapeElement.html#calculateAndGetPreferredDimension()), [calculateEdge](ShapeElement.html#calculateEdge()), [calculateMinimumDimension](ShapeElement.html#calculateMinimumDimension()), [calculateOnEdgeBounds](ShapeElement.html#calculateOnEdgeBounds()), [calculatePreferredDimension](ShapeElement.html#calculatePreferredDimension()), [calculatePreferredDimension](ShapeElement.html#calculatePreferredDimension(int,int)), [canBeAutosized](ShapeElement.html#canBeAutosized()), [canHavePaths](ShapeElement.html#canHavePaths()), [clearOldRect](ShapeElement.html#clearOldRect()), [edgeChanged](ShapeElement.html#edgeChanged()), [ensureDimension](ShapeElement.html#ensureDimension(boolean)), [ensurePreferredDimensionIfShrinkable](ShapeElement.html#ensurePreferredDimensionIfShrinkable()), [ensurePreferredDimensionIfShrinkable](ShapeElement.html#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)), [findFreePlaceForShapeOnBorder](ShapeElement.html#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)), [getBorderElementMargin](ShapeElement.html#getBorderElementMargin()), [getBounds](ShapeElement.html#getBounds()), [getCenterlineableInnerParts](ShapeElement.html#getCenterlineableInnerParts(int)), [getDefaultDimension](ShapeElement.html#getDefaultDimension()), [getDimensionForShrinking](ShapeElement.html#getDimensionForShrinking(int,int)), [getEdgeLine](ShapeElement.html#getEdgeLine(int)), [getFixedConnectionPoints](ShapeElement.html#getFixedConnectionPoints()), [getHeaderInsetReduce](ShapeElement.html#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)), [getInsetsForOnEdgeShapes](ShapeElement.html#getInsetsForOnEdgeShapes()), [getIntersection](ShapeElement.html#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getIntersection](ShapeElement.html#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)), [getIntersection](ShapeElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getLoadedDimension](ShapeElement.html#getLoadedDimension()), [getMiddlePoint](ShapeElement.html#getMiddlePoint()), [getMiddlePoint](ShapeElement.html#getMiddlePoint(java.awt.Point)), [getMiddlePointX](ShapeElement.html#getMiddlePointX(java.awt.Point)), [getMiddlePointY](ShapeElement.html#getMiddlePointY()), [getMinimumDimension](ShapeElement.html#getMinimumDimension()), [getNearestEdge](ShapeElement.html#getNearestEdge(int,int)), [getNearestEdge](ShapeElement.html#getNearestEdge(java.awt.Rectangle)), [getNeedAutosizeFlag](ShapeElement.html#getNeedAutosizeFlag()), [getNotCopyBounds](ShapeElement.html#getNotCopyBounds()), [getOnEdge](ShapeElement.html#getOnEdge()), [getOnEdgeCornerDistance](ShapeElement.html#getOnEdgeCornerDistance()), [getOnEdgePosition](ShapeElement.html#getOnEdgePosition()), [getPreferredDimension](ShapeElement.html#getPreferredDimension()), [getPreferredDimensionForAutosize](ShapeElement.html#getPreferredDimensionForAutosize()), [getReshapeMode](ShapeElement.html#getReshapeMode()), [getSizeForDrawing](ShapeElement.html#getSizeForDrawing()), [getSuspendShapeAutoResizeMode](ShapeElement.html#getSuspendShapeAutoResizeMode()), [hasManipulator](ShapeElement.html#hasManipulator()), [initialize](ShapeElement.html#initialize()), [internalApplyProperties](ShapeElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [internalGetBoundsShape](ShapeElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [internalSilentApply](ShapeElement.html#internalSilentApply()), [intersects](ShapeElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [isAutosized](ShapeElement.html#isAutosized()), [isCenterlineInner](ShapeElement.html#isCenterlineInner()), [isChildLayoutable](ShapeElement.html#isChildLayoutable(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isHorizontalCenterlineProvider](ShapeElement.html#isHorizontalCenterlineProvider()), [isOnEdge](ShapeElement.html#isOnEdge()), [isShapeOnEdge](ShapeElement.html#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isShrinkable](ShapeElement.html#isShrinkable()), [isSnapShapesOnBorderToGrid](ShapeElement.html#isSnapShapesOnBorderToGrid()), [isUseFixedConnectionPoints](ShapeElement.html#isUseFixedConnectionPoints()), [isVerticalCenterlineProvider](ShapeElement.html#isVerticalCenterlineProvider()), [layoutChildren](ShapeElement.html#layoutChildren()), [maximumDimension](ShapeElement.html#maximumDimension(java.awt.Dimension)), [minimumDimension](ShapeElement.html#minimumDimension(java.awt.Dimension)), [minimumDimensionForShrinking](ShapeElement.html#minimumDimensionForShrinking(java.awt.Dimension,int,int)), [minimumOrMinimumShrinkableDimension](ShapeElement.html#minimumOrMinimumShrinkableDimension(java.awt.Dimension)), [moveLinksToSelf](ShapeElement.html#moveLinksToSelf()), [movePathElements](ShapeElement.html#movePathElements()), [needAdjustToMaximumDimension](ShapeElement.html#needAdjustToMaximumDimension()), [onChildEdgeChange](ShapeElement.html#onChildEdgeChange(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)), [prepareForShadowDrawing](ShapeElement.html#prepareForShadowDrawing(java.awt.Graphics2D)), [providesHorizontalCenterline](ShapeElement.html#providesHorizontalCenterline()), [providesVerticalCenterline](ShapeElement.html#providesVerticalCenterline()), [resetCalculatePreferredRegardingChildren](ShapeElement.html#resetCalculatePreferredRegardingChildren()), [setAutosize](ShapeElement.html#setAutosize(boolean)), [setBorderElementMargin](ShapeElement.html#setBorderElementMargin(java.lang.String)), [setCalculatePreferredRegardingChildren](ShapeElement.html#setCalculatePreferredRegardingChildren(boolean)), [setLoadedDimension](ShapeElement.html#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)), [setMinimumDimension](ShapeElement.html#setMinimumDimension(int,int)), [setNeedAutosizeFlag](ShapeElement.html#setNeedAutosizeFlag(byte)), [setOldRect](ShapeElement.html#setOldRect(java.awt.Rectangle)), [setOnEdge](ShapeElement.html#setOnEdge(int)), [setPreferredDimension](ShapeElement.html#setPreferredDimension(int,int)), [setReshapeMode](ShapeElement.html#setReshapeMode(com.nomagic.magicdraw.uml.symbols.ReshapeMode)), [setSnapShapesOnBorderToGrid](ShapeElement.html#setSnapShapesOnBorderToGrid(boolean)), [setSuspendShapeAutoResizeMode](ShapeElement.html#setSuspendShapeAutoResizeMode(java.lang.String)), [setUseFixedConnectionPoints](ShapeElement.html#setUseFixedConnectionPoints(boolean)), [shouldDrawShadow](ShapeElement.html#shouldDrawShadow()), [simpleSetBounds](ShapeElement.html#simpleSetBounds(int,int,int,int,boolean)), [simpleSetBounds](ShapeElement.html#simpleSetBounds(java.awt.Rectangle)), [snapsToCenterlines](ShapeElement.html#snapsToCenterlines()), [sSetAutosize](ShapeElement.html#sSetAutosize(boolean)), [sSetBorderElementMargin](ShapeElement.html#sSetBorderElementMargin(java.lang.String)), [sSetBounds](ShapeElement.html#sSetBounds(java.awt.Rectangle)), [sSetSuspendShapeAutoResizeMode](ShapeElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)), [sSetVisibility](ShapeElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [toString](ShapeElement.html#toString()), [updateLater](ShapeElement.html#updateLater())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[addConnectedPathElement](../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [createSmartListenerConfig](../paths/PathConnector.html#createSmartListenerConfig(java.util.List)), [disposeConnectedPaths](../paths/PathConnector.html#disposeConnectedPaths()), [findSymbolForEnd](../paths/PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)), [findSymbolForEnd](../paths/PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)), [getConnectedPathElement](../paths/PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [getConnectedPathElementCount](../paths/PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)), [getPreferredArrowLength](../paths/PathConnector.html#getPreferredArrowLength()), [isShowsProxy](../paths/PathConnector.html#isShowsProxy()), [movePathElement](../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)), [removeConnectedPathElement](../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sAddConnectedPathElement](../paths/PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [setParent](../paths/PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [setVisibility](../paths/PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [sRemoveConnectedPathElement](../paths/PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sSetConnectedPathElements](../paths/PathConnector.html#sSetConnectedPathElements(java.util.List)), [supportsVisibleConnectedPathElementsIfSelfInvisible](../paths/PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[addPresentationElement](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addProperty](../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [adjustChildBounds](../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [alwaysShowTooltip](../PresentationElement.html#alwaysShowTooltip()), [applyProperties](../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [askDeleteDataConfirmation](../PresentationElement.html#askDeleteDataConfirmation()), [atInsertChildren](../PresentationElement.html#atInsertChildren()), [autosizeAndResizeManipulatedParent](../PresentationElement.html#autosizeAndResizeManipulatedParent()), [beforeDelete](../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)), [boundsChanged](../PresentationElement.html#boundsChanged()), [boundsChanged](../PresentationElement.html#boundsChanged(java.awt.Rectangle)), [canAddChild](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)), [canAddInstance](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDisposedOnUpdate](../PresentationElement.html#canBeDisposedOnUpdate()), [canChangeElementOwner](../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canFill](../PresentationElement.html#canFill()), [changeProperties](../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [checkProxyVisibility](../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [childrenForMoving](../PresentationElement.html#childrenForMoving()), [collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)), [collectSubShowingPresentationElements](../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)), [coversPoint](../PresentationElement.html#coversPoint(int,int)), [createFillStrategy](../PresentationElement.html#createFillStrategy()), [createPresentationElementStyle](../PresentationElement.html#createPresentationElementStyle()), [createPropertyChangeListener](../PresentationElement.html#createPropertyChangeListener()), [disposePropertyChangeListener](../PresentationElement.html#disposePropertyChangeListener()), [draw](../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawBackground](../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbol](../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbolBackground](../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [dynamicFillColor](../PresentationElement.html#dynamicFillColor()), [dynamicLineColor](../PresentationElement.html#dynamicLineColor()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth(int)), [dynamicPaintShadow](../PresentationElement.html#dynamicPaintShadow()), [dynamicStroke](../PresentationElement.html#dynamicStroke()), [dynamicStroke](../PresentationElement.html#dynamicStroke(int)), [dynamicStyleFillColor](../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)), [dynamicStyleLineColor](../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)), [dynamicStyleTextColor](../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency()), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)), [dynamicStyleValue](../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)), [dynamicTextAlignment](../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)), [dynamicTextColor](../PresentationElement.html#dynamicTextColor()), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [findOwnerForChildElement](../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [findOwnerForElement](../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)), [findPresentationElement](../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)), [firePropertyChange](../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateID](../PresentationElement.html#generateID()), [getAbstractDiagramPresentationElement](../PresentationElement.html#getAbstractDiagramPresentationElement()), [getAdditionalRenderersToNotifyOnPropertiesChange](../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()), [getAssignableModelElementsClasses](../PresentationElement.html#getAssignableModelElementsClasses()), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getBoundsWithChildrenOnEdge](../PresentationElement.html#getBoundsWithChildrenOnEdge()), [getCenterlinePoint](../PresentationElement.html#getCenterlinePoint()), [getCenterlinePointX](../PresentationElement.html#getCenterlinePointX()), [getCenterlinePointY](../PresentationElement.html#getCenterlinePointY()), [getChildPresentationElementForContextMenu](../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)), [getChildrenWithSymbolProperties](../PresentationElement.html#getChildrenWithSymbolProperties()), [getConfiguration](../PresentationElement.html#getConfiguration()), [getDiagramPresentationElement](../PresentationElement.html#getDiagramPresentationElement()), [getDiagramSurface](../PresentationElement.html#getDiagramSurface()), [getDrawComparator](../PresentationElement.html#getDrawComparator()), [getDynamicConfigurations](../PresentationElement.html#getDynamicConfigurations()), [getEffectiveStyleDelegate](../PresentationElement.html#getEffectiveStyleDelegate()), [getEffectiveStyleOwner](../PresentationElement.html#getEffectiveStyleOwner()), [getElementsForRelationshipConnecting](../PresentationElement.html#getElementsForRelationshipConnecting()), [getElementToConnectRelationship](../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFillColor](../PresentationElement.html#getFillColor()), [getFont](../PresentationElement.html#getFont()), [getFontHeight](../PresentationElement.html#getFontHeight()), [getFontRenderContext](../PresentationElement.html#getFontRenderContext()), [getHumanName](../PresentationElement.html#getHumanName()), [getHumanType](../PresentationElement.html#getHumanType()), [getLineColor](../PresentationElement.html#getLineColor()), [getLineWidth](../PresentationElement.html#getLineWidth()), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point)), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getModelElement](../PresentationElement.html#getModelElement()), [getModelElementsForRelationshipConnecting](../PresentationElement.html#getModelElementsForRelationshipConnecting()), [getModelElementToConnectRelationship](../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [getModelElementToMove](../PresentationElement.html#getModelElementToMove()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getOwnStyleDelegate](../PresentationElement.html#getOwnStyleDelegate()), [getParent](../PresentationElement.html#getParent()), [getPreferredBounds](../PresentationElement.html#getPreferredBounds()), [getPreferredSize](../PresentationElement.html#getPreferredSize()), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(int)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementCount](../PresentationElement.html#getPresentationElementCount()), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getProjectImpl](../PresentationElement.html#getProjectImpl()), [getProperty](../PresentationElement.html#getProperty(java.lang.String)), [getPropertyManager](../PresentationElement.html#getPropertyManager()), [getPropertyManagerName](../PresentationElement.html#getPropertyManagerName()), [getRenderer](../PresentationElement.html#getRenderer()), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [getStyle](../PresentationElement.html#getStyle()), [getSymbolRenderer](../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getTextColor](../PresentationElement.html#getTextColor()), [getTolerance](../PresentationElement.html#getTolerance()), [getVisibility](../PresentationElement.html#getVisibility()), [getVisiblePresentationElements](../PresentationElement.html#getVisiblePresentationElements()), [handleModelDelete](../PresentationElement.html#handleModelDelete()), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [hasSharedModelElement](../PresentationElement.html#hasSharedModelElement()), [initializeAndAutosize](../PresentationElement.html#initializeAndAutosize()), [internalBeforeUpdate](../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)), [internalCreatePropertyChangeListener](../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [internalGetModelElementToConnectRelationship](../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [internalGetSpecificFont](../PresentationElement.html#internalGetSpecificFont()), [internalGetSpecificTextColor](../PresentationElement.html#internalGetSpecificTextColor()), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(float)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)), [intersects](../PresentationElement.html#intersects(int,int,int,int)), [invalidate](../PresentationElement.html#invalidate()), [isChildVisible](../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isContentHidden](../PresentationElement.html#isContentHidden()), [isCreateElementListener](../PresentationElement.html#isCreateElementListener()), [isDetectable](../PresentationElement.html#isDetectable()), [isDisposed](../PresentationElement.html#isDisposed()), [isLayouting](../PresentationElement.html#isLayouting()), [isNotNull](../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isPreserveProportionsWhenGrowing](../PresentationElement.html#isPreserveProportionsWhenGrowing()), [isSelected](../PresentationElement.html#isSelected()), [isShowElementTypeAsLabel](../PresentationElement.html#isShowElementTypeAsLabel()), [isSortable](../PresentationElement.html#isSortable()), [isSuitableToConnectRelationship](../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [isTextEditable](../PresentationElement.html#isTextEditable()), [isUseFillColor](../PresentationElement.html#isUseFillColor()), [isUseFillColorByProperty](../PresentationElement.html#isUseFillColorByProperty()), [isUseGradientForFill](../PresentationElement.html#isUseGradientForFill()), [isVisible](../PresentationElement.html#isVisible()), [isVisibleInDiagram](../PresentationElement.html#isVisibleInDiagram()), [isVisibleOrShrunken](../PresentationElement.html#isVisibleOrShrunken()), [movePathElementsRecursively](../PresentationElement.html#movePathElementsRecursively()), [notifyCreated](../PresentationElement.html#notifyCreated()), [notifyDiagramFrameSizeChange](../PresentationElement.html#notifyDiagramFrameSizeChange()), [notifyRepaintManager](../PresentationElement.html#notifyRepaintManager(boolean)), [onChildAdd](../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onChildRemove](../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onDiagramSurfaceSet](../PresentationElement.html#onDiagramSurfaceSet()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [onFontChange](../PresentationElement.html#onFontChange()), [onParentChange](../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [paintAdornments](../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintAdornmentsBackground](../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenAndAdornments](../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelfBackground](../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [preDisposeOnUpdate](../PresentationElement.html#preDisposeOnUpdate()), [prepareForLineDrawing](../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)), [prepareForTextDrawing](../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)), [propertyChange](../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)), [recreateListeners](../PresentationElement.html#recreateListeners()), [registerInSortManager](../PresentationElement.html#registerInSortManager()), [removeFromSortManager](../PresentationElement.html#removeFromSortManager()), [removeItSelfOnUpdate](../PresentationElement.html#removeItSelfOnUpdate()), [resizeParent](../PresentationElement.html#resizeParent()), [sAddPresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [selectChildrenForMoving](../PresentationElement.html#selectChildrenForMoving()), [selectObjectsForMoving](../PresentationElement.html#selectObjectsForMoving()), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setBounds](../PresentationElement.html#setBounds(int,int,int,int)), [setCreateElementListener](../PresentationElement.html#setCreateElementListener(boolean)), [setFont](../PresentationElement.html#setFont(java.awt.Font)), [setLayouting](../PresentationElement.html#setLayouting(boolean)), [setLineColor](../PresentationElement.html#setLineColor(java.awt.Color)), [setLineWidth](../PresentationElement.html#setLineWidth(int)), [setLoadedVisibility](../PresentationElement.html#setLoadedVisibility(boolean)), [setLocation](../PresentationElement.html#setLocation(int,int)), [setLocation](../PresentationElement.html#setLocation(java.awt.Point)), [setModelElement](../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [setNeedRecreateListeners](../PresentationElement.html#setNeedRecreateListeners(boolean)), [setPropertyManagerName](../PresentationElement.html#setPropertyManagerName(java.lang.String)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [setSize](../PresentationElement.html#setSize(int,int)), [setSize](../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)), [setSize](../PresentationElement.html#setSize(java.awt.Dimension)), [setTextColor](../PresentationElement.html#setTextColor(java.awt.Color)), [setTextEditable](../PresentationElement.html#setTextEditable(boolean)), [setUseFillColor](../PresentationElement.html#setUseFillColor(boolean)), [setVisible](../PresentationElement.html#setVisible(boolean)), [silentApply](../PresentationElement.html#silentApply()), [silentApply](../PresentationElement.html#silentApply(boolean)), [simpleSetBounds](../PresentationElement.html#simpleSetBounds(int,int,int,int)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Point,float)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)), [snapViewToGrid](../PresentationElement.html#snapViewToGrid(float)), [sortObjectsByX](../PresentationElement.html#sortObjectsByX(java.util.List)), [sortObjectsByY](../PresentationElement.html#sortObjectsByY(java.util.List)), [sSetBounds](../PresentationElement.html#sSetBounds(int,int,int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(java.awt.Point)), [sSetModelElement](../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [sSetParent](../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetParentForAll](../PresentationElement.html#sSetParentForAll(java.util.Collection)), [sSetSize](../PresentationElement.html#sSetSize(int,int)), [sSetSize](../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)), [sSetSize](../PresentationElement.html#sSetSize(java.awt.Dimension)), [sSetVisible](../PresentationElement.html#sSetVisible(boolean)), [tryToDeleteModelElementUponRemoval](../PresentationElement.html#tryToDeleteModelElementUponRemoval()), [update](../PresentationElement.html#update()), [updateAfterLoad](../PresentationElement.html#updateAfterLoad()), [updateLabelsIgnoringSuspendableLater](../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)), [updateModelByView](../PresentationElement.html#updateModelByView()), [updateModelByViewInternal](../PresentationElement.html#updateModelByViewInternal()), [updateViewAfterPropertyChange](../PresentationElement.html#updateViewAfterPropertyChange()), [useParentProperties](../PresentationElement.html#useParentProperties())`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../BaseElement.html)
`[canAdd](../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape
`asPresentationElement, getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY`
Methods inherited from interface com.nomagic.magicdraw.uml.[MDElement](../../MDElement.html)
`[getProject](../../MDElement.html#getProject())`
Methods inherited from interface com.nomagic.magicdraw.utils.[NameOwner](../../../utils/NameOwner.html)
`[getName](../../../utils/NameOwner.html#getName())`

============ FIELD DETAIL =========== 
Field Details
MIN_EXTENSION
public static final int MIN_EXTENSION
Minimal extension of lifeline line.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView.MIN_EXTENSION)
MIN_LENGTH
public static final int MIN_LENGTH
Minimal length of lifeline line.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView.MIN_LENGTH)
CROSS_WIDTH
public static final int CROSS_WIDTH
cross width
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView.CROSS_WIDTH)
CROSS_DELTA
public static final int CROSS_DELTA
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView.CROSS_DELTA)
DELTA_Y
public static final int DELTA_Y
constants for concurrent lifeline dimensions
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView.DELTA_Y)
DELTA_X
public static final int DELTA_X
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView.DELTA_X)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
LifeLineLineView
public LifeLineLineView()
Creates a new life line view.
LifeLineLineView
public LifeLineLineView(@CheckForNull
 [PresentationElement](../PresentationElement.html) parent)
Creates and initializes a new life line view from specified parameter.
Parameters:
`parent` - this life line view parent object.
 ============ METHOD DETAIL ========== 
Method Details
getStateInvariants
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[StateInvariantView](StateInvariantView.html)> getStateInvariants()
Gets state invariants lying on this lifeline line.
Returns:
a list of state invariants.
hasStateInvariants
public boolean hasStateInvariants()
Indicates if this life line has any state invariants on it.
Returns:
true if this life line has any state invariants, false otherwise.
getLastStateInvariantPosition
public int getLastStateInvariantPosition()
Calculates y coordinate of this lifeline line to cover the last state invariant
 lying on it.
Returns:
last state invariant y position.
paintSelf
public void paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
Specified by:
`[paintSelf](../PresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))` in class `[PresentationElement](../PresentationElement.html)`
paintChildren
public void paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
Overrides:
`paintChildren` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
internalGetPresentationElementStroke
public [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) internalGetPresentationElementStroke(int width)
Description copied from class: `[PresentationElement](../PresentationElement.html#internalGetPresentationElementStroke(int))`
Return a stroke used to paint symbol's main part
Overrides:
`[internalGetPresentationElementStroke](../PresentationElement.html#internalGetPresentationElementStroke(int))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`width` - a custom stroke width. Other stroke parameters will be specific to symbol
Returns:
a stroke used to paint symbol's main part
dynamicStroke
public [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) dynamicStroke([BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) stroke)
Overrides:
`[dynamicStroke](../PresentationElement.html#dynamicStroke(java.awt.BasicStroke))` in class `[PresentationElement](../PresentationElement.html)`
calculateDestroyTimePoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) calculateDestroyTimePoint()
getMiddlePointX
public int getMiddlePointX()
Overrides:
`[getMiddlePointX](ShapeElement.html#getMiddlePointX())` in class `[ShapeElement](ShapeElement.html)`
canAddInstance
public boolean canAddInstance([PresentationElement](../PresentationElement.html) symbol)
Checks can this life line view add specified object or not.
 LifeLineView can add Activation and SequenceBaseMessageView objects.
Overrides:
`canAddInstance` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`symbol` - specified PresentationElement object.
Returns:
true if this object can add specified object
 otherwise false
canAddChild
public boolean canAddChild([PresentationElement](../PresentationElement.html) symbol)
Description copied from class: `[PresentationElement](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Check of given symbol can be added as child into this symbol.
Overrides:
`canAddChild` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`symbol` - symbol
Returns:
true if symbol can be added
selectPathsForMoving
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](../paths/PathElement.html)> selectPathsForMoving([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](../PresentationElement.html)> subPresentationElements)
Description copied from class: `[PresentationElement](../PresentationElement.html#selectPathsForMoving(java.util.List))`
Select paths to move with current symbol from deep structure.
 Some paths can be connected to current symbol, but owned in some deep child of this symbol.
Overrides:
`[selectPathsForMoving](../paths/PathConnector.html#selectPathsForMoving(java.util.List))` in class `[PathConnector](../paths/PathConnector.html)`
Parameters:
`subPresentationElements` - sub children of this symbol
Returns:
paths to move together with current symbol
setPosition
public void setPosition()
Sets life line view position depending on this object parent position.
 Moves all links and connection points.
moveChild
public void moveChild([PresentationElement](../PresentationElement.html) view,
 int dx,
 int dy)
Overrides:
`moveChild` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
simpleSetBounds
public void simpleSetBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rct,
 boolean moveChildren,
 boolean calculatePrefSize)
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Sets bounds for this container shape view and all its components
Overrides:
`simpleSetBounds` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`rct` - container shape view bounding rectangle
`moveChildren` - if moveChildren equals true then this method calls
`calculatePrefSize` - calculate preferred size
getNotZoomedTolerance
protected int getNotZoomedTolerance()
Overrides:
`[getNotZoomedTolerance](../PresentationElement.html#getNotZoomedTolerance())` in class `[PresentationElement](../PresentationElement.html)`
coversPoint
public boolean coversPoint(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
checks if object covers provided point
Overrides:
`[coversPoint](ShapeElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[ShapeElement](ShapeElement.html)`
Returns:
true if object covers this point
needAdjustToPreferred
protected boolean needAdjustToPreferred()
Description copied from class: `[ShapeElement](ShapeElement.html#needAdjustToPreferred())`
Check if shape can be resized to a preferred size. Usually it is true if shape is manipulated and isAutosize is true.
Overrides:
`needAdjustToPreferred` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Returns:
true if adjustments are necessary
getManipulationBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getManipulationBounds(@CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint)
Description copied from class: `[PresentationElement](../PresentationElement.html#getManipulationBounds(java.awt.Point))`
Gets manipulation bounds of the symbol. Manipulation bounds might
 differ from symbol bounds, they can be larger or smaller to help
 user manipulate the symbol.
Overrides:
`[getManipulationBounds](../PresentationElement.html#getManipulationBounds(java.awt.Point))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`relativePoint` - active user point to construct manipulation bounds.
Returns:
symbol manipulation bounds.
getBoundsToRepaint
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBoundsToRepaint()
Return bounds of the symbol that must be repainted.
 throws NoRectangleDefinedException
Overrides:
`[getBoundsToRepaint](../PresentationElement.html#getBoundsToRepaint())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
rectangle of bounds
movePathElement
protected void movePathElement([PathElement](../paths/PathElement.html) lnk,
 [PathConnector](../paths/PathConnector.html) requestor)
Description copied from class: `[PathConnector](../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector))`
Calculates position of a path element.
Overrides:
`[movePathElement](ShapeElement.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector))` in class `[ShapeElement](ShapeElement.html)`
Parameters:
`lnk` - element which position will be calculated.
`requestor` - the requestor of this path moving. Implementations may check to avoid endless loops.
getPresentationElementAt
public [PresentationElement](../PresentationElement.html) getPresentationElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Searches and returns object that covers given point.
Overrides:
`getPresentationElementAt` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`point` - given point
`kind` - intersection kind to check for
Returns:
PresentationElement that covers specified point
getSortedActivations
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ActivationView](ActivationView.html)> getSortedActivations()
Returns:
sorted activations by y ascending.
getMiddlePointY
public int getMiddlePointY([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint)
Overrides:
`[getMiddlePointY](ShapeElement.html#getMiddlePointY(java.awt.Point))` in class `[ShapeElement](ShapeElement.html)`
clone
public [LifeLineLineView](LifeLineLineView.html) clone()
Clones this object.
Specified by:
`[clone](../../BaseElement.html#clone())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`clone` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Returns:
copy of this object.
getActivationsIterator
public [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[ActivationView](ActivationView.html)> getActivationsIterator()
Returns:
all activations
getLastActivation
@CheckForNullpublic [ActivationView](ActivationView.html) getLastActivation()
Returns last activation.
Returns:
Activation object.
getLastStateInvariant
@CheckForNullpublic [StateInvariantView](StateInvariantView.html) getLastStateInvariant()
Returns last state invariant.
Returns:
state invariant symbol;
getActivationAt
@CheckForNullpublic [ActivationView](ActivationView.html) getActivationAt(int y)
Returns Activation at specified point.
Parameters:
`y` - point y
Returns:
activation what covers specified point
getClosestActivationAt
@CheckForNullpublic [ActivationView](ActivationView.html) getClosestActivationAt(int ptY)
Finds closest activation on this lifeline line at a given point.
Parameters:
`ptY` - Y of point closest to which an activation should be found
Returns:
closest activation at a given point
accept
public void accept([Visitor](../../Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
 See "Visitor" pattern for more details.
Specified by:
`[accept](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../../MDElement.html)`
Overrides:
`accept` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
atInsert
public void atInsert()
Description copied from class: `[PresentationElement](../PresentationElement.html#atInsert())`
Invalidates object at insert
Specified by:
`[atInsert](../../BaseElement.html#atInsert())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`[atInsert](../PresentationElement.html#atInsert())` in class `[PresentationElement](../PresentationElement.html)`
editName
public void editName(@CheckForNull
 [KeyEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/KeyEvent.html) evt,
 @CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> textEditorOptions)
Does nothing -- prevent from editing name box,
 which is an attribute of container.
Overrides:
`[editName](../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`evt` - first key event or null
`textEditorOptions` - boolean options for text editor. Passed when creating text editor with
 `TextEditorFactory`
internalGetManipulatedChildrenRect
@CheckForNullprotected [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) internalGetManipulatedChildrenRect(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Calculate union area of owned manipulated children added not on a shape border
Overrides:
`internalGetManipulatedChildrenRect` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`insetsLevel` - include insets if shape has manipulated children
Returns:
rectangle of children or null if there are no children
mustShowContextMenu
public boolean mustShowContextMenu()
Overrides:
`[mustShowContextMenu](../PresentationElement.html#mustShowContextMenu())` in class `[PresentationElement](../PresentationElement.html)`
dispose
public void dispose()
Description copied from class: `[PresentationElement](../PresentationElement.html#dispose())`
disposes ends of links when link is deleted
Specified by:
`[dispose](../../BaseElement.html#dispose())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`[dispose](../paths/PathConnector.html#dispose())` in class `[PathConnector](../paths/PathConnector.html)`
disposeChildren
protected void disposeChildren()
Removes all children from itself. Such removing causes
 calling dispose for every child.
Overrides:
`[disposeChildren](../PresentationElement.html#disposeChildren())` in class `[PresentationElement](../PresentationElement.html)`
adjustBounds
public void adjustBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
Adjust bounds
 1. if lifeline is not concurrent, y must be seq bottom
 2. (Disabled) if lifeline is concurrent y must be below parent life line upper point
 disabled because adjust bounds for moving does it
 3. if lifeline is concurrent. x must be same as parent x+parent.width
Overrides:
`[adjustBounds](ShapeElement.html#adjustBounds(java.awt.Rectangle))` in class `[ShapeElement](ShapeElement.html)`
Parameters:
`r` - bounds
setConcurrent
public void setConcurrent(boolean concurrent)
isConcurrent
public boolean isConcurrent()
correctInnerStateInvariantBounds
public void correctInnerStateInvariantBounds()
Adjust bounds of inner state invariants according bounds of this lifeline.
correctStateInvariantBounds
public boolean correctStateInvariantBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
Adjusts bounds of a given state invariant so that it lies correctly on
 this lifeline line.
Parameters:
`bounds` - bounds of state invariant to adjust.
Returns:
true if bounds were adjusted, false otherwise.
preferredDimension
protected void preferredDimension([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)
Overrides:
`preferredDimension` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
useParentStyle
public boolean useParentStyle()
Use parent font always
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
getDynamicStyleOwner
@CheckForNullpublic [PresentationElement](../PresentationElement.html) getDynamicStyleOwner()
Overrides:
`[getDynamicStyleOwner](../PresentationElement.html#getDynamicStyleOwner())` in class `[PresentationElement](../PresentationElement.html)`
getUpperPointY
public int getUpperPointY()
setHidden
public void setHidden(boolean hidden)
isHidden
public boolean isHidden()
calculateActivationsBounds
@CheckForNullpublic [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) calculateActivationsBounds()
adjustBoundsBeforeChange
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) adjustBoundsBeforeChange([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rec,
 boolean autosizeOperation,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)> movedTogether)
validate bounds for moving
Overrides:
`adjustBoundsBeforeChange` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
calculateAutosizeDimension
public void calculateAutosizeDimension([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size,
 int locationX,
 int locationY,
 int prefSizeWidth,
 int prefSizeHeight)
Description copied from class: `[ShapeElement](ShapeElement.html#calculateAutosizeDimension(java.awt.Dimension,int,int,int,int))`
Calculates size of shape to be at least as preferred and fit all children
Overrides:
`calculateAutosizeDimension` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`size` - size
`locationX` - x location
`locationY` - y location
`prefSizeWidth` - preferred size width
`prefSizeHeight` - preferred size height
getObject
public [SequenceLifelineView](SequenceLifelineView.html) getObject()
Returns:
owner - SequenceLifelineView
getAllMessages
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView> getAllMessages()
getIncomingMessageWithType
@CheckForNullpublic com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView getIncomingMessageWithType([MessageSort](../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageSort.html) type)
Parameters:
`type` - message type
Returns:
incoming message of give sort type
getElement
public [Lifeline](../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html) getElement()
returns parent data
Specified by:
`[getElement](../../ModelElementProvider.html#getElement())` in interface `[ModelElementProvider](../../ModelElementProvider.html)`
Overrides:
`[getElement](../PresentationElement.html#getElement())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
model element of this presentation element.
getLifeline
public [Lifeline](../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html) getLifeline()
isSnapToGrid
protected boolean isSnapToGrid()
Overrides:
`[isSnapToGrid](ShapeElement.html#isSnapToGrid())` in class `[ShapeElement](ShapeElement.html)`
sSetElement
public void sSetElement([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) el)
Overrides:
`[sSetElement](../PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))` in class `[PresentationElement](../PresentationElement.html)`
setElement
public void setElement([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) el)
Overrides:
`[setElement](../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))` in class `[PresentationElement](../PresentationElement.html)`
getActualElement
public [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getActualElement()
Description copied from class: `[PresentationElement](../PresentationElement.html#getActualElement())`
Because some views returns theirs parent model element, we do not know have they this member
 set or not.
Overrides:
`[getActualElement](../PresentationElement.html#getActualElement())` in class `[PresentationElement](../PresentationElement.html)`
isMovableByMoveManager
public boolean isMovableByMoveManager()
Description copied from class: `[PresentationElement](../PresentationElement.html#isMovableByMoveManager())`
Method indicates if object of this instance must be registered in move manager.
Overrides:
`[isMovableByMoveManager](../PresentationElement.html#isMovableByMoveManager())` in class `[PresentationElement](../PresentationElement.html)`
See Also:
[`PresentationElement.isMovableByMoveManager()`](../PresentationElement.html#isMovableByMoveManager())
isUseEntireActivation
public boolean isUseEntireActivation()
internalUpdatePresentationElement
protected void internalUpdatePresentationElement()
Description copied from class: `[PresentationElement](../PresentationElement.html#internalUpdatePresentationElement())`
Internal symbol update method for subclassing. It is called from update as part of full
 update action.
Overrides:
`internalUpdatePresentationElement` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
See Also:
[`PresentationElement.update()`](../PresentationElement.html#update())
getSeqContainer
public com.nomagic.magicdraw.uml.symbols.SequenceObjectViewContainer getSeqContainer()
rememberBounds
public void rememberBounds()
Description copied from class: `[PresentationElement](../PresentationElement.html#rememberBounds())`
Remember old bounds
Overrides:
`[rememberBounds](../PresentationElement.html#rememberBounds())` in class `[PresentationElement](../PresentationElement.html)`
rememberBounds
public void rememberBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
Overrides:
`[rememberBounds](../PresentationElement.html#rememberBounds(java.awt.Rectangle))` in class `[PresentationElement](../PresentationElement.html)`
removePresentationElement
public void removePresentationElement([PresentationElement](../PresentationElement.html) element,
 boolean resizeParent)
Description copied from class: `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Removes object view from container.
Overrides:
`removePresentationElement` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`element` - object to remove
`resizeParent` - resize parent
checkElementOwnerOnChange
public boolean checkElementOwnerOnChange([PresentationElement](../PresentationElement.html) child)
Overrides:
`[checkElementOwnerOnChange](../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[PresentationElement](../PresentationElement.html)`
getChildrenInsets
public com.nomagic.ui.UnmodifiableInsets getChildrenInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)
Overrides:
`getChildrenInsets` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`insetsLevel` - describes the level of insets
Returns:
shape insets for children
getNestedLines
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[LifeLineLineView](LifeLineLineView.html)> getNestedLines()
Returns nested lifeline lines.
Returns:
a list of nested lifeline list or empty list
getNestedLinesIterator
public [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[LifeLineLineView](LifeLineLineView.html)> getNestedLinesIterator()
Returns:
nested lifeline lines
getActivations
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ActivationView](ActivationView.html)> getActivations()
Gets activations placed on this lifeline line.
Returns:
a list of activations placed on this line.
isDestroyed
public boolean isDestroyed()
Gets destroyed value.
Returns:
destroyed value
ensureDestructionOccurrence
public boolean ensureDestructionOccurrence(boolean destruct)
Ensures that a proper destruction occurrence is in the model on this lifeline.
Parameters:
`destruct` - indicates whether lifeline is destructed or not.
Returns:
true if destruction event was changed
isNested
public boolean isNested()
Indicates if this lifeline line is nested (not root).
Returns:
true if this lifeline line is nested, false otherwise.
internalLayoutChildren
public void internalLayoutChildren(boolean calculatePrefSize)
Overrides:
`internalLayoutChildren` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
sRemovePresentationElement
public void sRemovePresentationElement([PresentationElement](../PresentationElement.html) element)
Description copied from class: `[PresentationElement](../PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Removes given child
Overrides:
`sRemovePresentationElement` in class `com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`
Parameters:
`element` - child
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
createBoundsShape
public [ContainerShape](../../../../awt/ContainerShape.html) createBoundsShape(@CheckForNull
 [PathElement](../paths/PathElement.html) path,
 [BoundsTransformation](../BoundsTransformation.html) transformation)
Description copied from class: `[ShapeElement](ShapeElement.html#createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation))`
Creates bounding shape for intersection calculation.
Overrides:
`[createBoundsShape](ShapeElement.html#createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation))` in class `[ShapeElement](ShapeElement.html)`
Parameters:
`path` - path
`transformation` - transformation
Returns:
shape

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.shapes</a></div>
<h1 class="title" title="Class LifeLineLineView">Class LifeLineLineView</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</a>
<div class="inheritance"><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView</div>
</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code>, <code>com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider</code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">LifeLineLineView</span>
<span class="extends-implements">extends com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</span></div>
<div class="block">Life line line in sequence diagram.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CROSS_DELTA">CROSS_DELTA</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CROSS_WIDTH">CROSS_WIDTH</a></code></div>
<div class="col-last odd-row-color">
<div class="block">cross width</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DELTA_X">DELTA_X</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DELTA_Y">DELTA_Y</a></code></div>
<div class="col-last odd-row-color">
<div class="block">constants for concurrent lifeline dimensions</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MIN_EXTENSION">MIN_EXTENSION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Minimal extension of lifeline line.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MIN_LENGTH">MIN_LENGTH</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Minimal length of lifeline line.</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">LifeLineLineView</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new life line view.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement)">LifeLineLineView</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates and initializes a new life line view from specified parameter.</div>
</div>
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,boolean)">addPresentationElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index,
 boolean resize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If a specified object not inserted in this container then adds a new object view to the container.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustBounds(java.awt.Rectangle)">adjustBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adjust bounds
 1.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">adjustBoundsBeforeChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rec,
 boolean autosizeOperation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">validate bounds for moving</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#atInsert()">atInsert</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invalidates object at insert</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateActivationsBounds()">calculateActivationsBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateAutosizeDimension(java.awt.Dimension,int,int,int,int)">calculateAutosizeDimension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size,
 int locationX,
 int locationY,
 int prefSizeWidth,
 int prefSizeHeight)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates size of shape to be at least as preferred and fit all children</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateDestroyTimePoint()">calculateDestroyTimePoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddChild</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check of given symbol can be added as child into this symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddInstance</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks can this life line view add specified object or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="LifeLineLineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LifeLineLineView</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones this object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#correctInnerStateInvariantBounds()">correctInnerStateInvariantBounds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adjust bounds of inner state invariants according bounds of this lifeline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#correctStateInvariantBounds(java.awt.Rectangle)">correctStateInvariantBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adjusts bounds of a given state invariant so that it lies correctly on
 this lifeline line.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">coversPoint</a><wbr/>(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">checks if object covers provided point</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">createBoundsShape</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 <a href="../BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols">BoundsTransformation</a> transformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates bounding shape for intersection calculation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">disposes ends of links when link is deleted</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#disposeChildren()">disposeChildren</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all children from itself.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a> stroke)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/KeyEvent.html" title="class or interface in java.awt.event">KeyEvent</a> evt,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; textEditorOptions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Does nothing -- prevent from editing name box,
 which is an attribute of container.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureDestructionOccurrence(boolean)">ensureDestructionOccurrence</a><wbr/>(boolean destruct)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Ensures that a proper destruction occurrence is in the model on this lifeline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActivationAt(int)">getActivationAt</a><wbr/>(int y)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Activation at specified point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActivations()">getActivations</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets activations placed on this lifeline line.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActivationsIterator()">getActivationsIterator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActualElement()">getActualElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Because some views returns theirs parent model element, we do not know have they this member
 set or not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllMessages()">getAllMessages</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBoundsToRepaint()">getBoundsToRepaint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return bounds of the symbol that must be repainted.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ui.UnmodifiableInsets</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildrenInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel)">getChildrenInsets</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClosestActivationAt(int)">getClosestActivationAt</a><wbr/>(int ptY)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds closest activation on this lifeline line at a given point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDynamicStyleOwner()">getDynamicStyleOwner</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">returns parent data</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIncomingMessageWithType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort)">getIncomingMessageWithType</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastActivation()">getLastActivation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns last activation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StateInvariantView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StateInvariantView</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastStateInvariant()">getLastStateInvariant</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns last state invariant.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastStateInvariantPosition()">getLastStateInvariantPosition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates y coordinate of this lifeline line to cover the last state invariant
 lying on it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLifeline()">getLifeline</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulationBounds(java.awt.Point)">getManipulationBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets manipulation bounds of the symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePointX()">getMiddlePointX</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePointY(java.awt.Point)">getMiddlePointY</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="LifeLineLineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LifeLineLineView</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNestedLines()">getNestedLines</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns nested lifeline lines.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="LifeLineLineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LifeLineLineView</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNestedLinesIterator()">getNestedLinesIterator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotZoomedTolerance()">getNotZoomedTolerance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SequenceLifelineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SequenceLifelineView</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getObject()">getObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns parent to which this symbol delegates style attributes related functionality.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Searches and returns object that covers given point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.SequenceObjectViewContainer</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeqContainer()">getSeqContainer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSortedActivations()">getSortedActivations</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="StateInvariantView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StateInvariantView</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStateInvariants()">getStateInvariants</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets state invariants lying on this lifeline line.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUpperPointY()">getUpperPointY</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasStateInvariants()">hasStateInvariants</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if this life line has any state invariants on it.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetManipulatedChildrenRect(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel)">internalGetManipulatedChildrenRect</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculate union area of owned manipulated children added not on a shape border</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a><wbr/>(int width)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a stroke used to paint symbol's main part</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalLayoutChildren(boolean)">internalLayoutChildren</a><wbr/>(boolean calculatePrefSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalUpdatePresentationElement()">internalUpdatePresentationElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Internal symbol update method for subclassing.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isConcurrent()">isConcurrent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDestroyed()">isDestroyed</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets destroyed value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHidden()">isHidden</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMovableByMoveManager()">isMovableByMoveManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method indicates if object of this instance must be registered in move manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNested()">isNested</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if this lifeline line is nested (not root).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSnapToGrid()">isSnapToGrid</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseEntireActivation()">isUseEntireActivation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#moveChild(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,int)">moveChild</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 int dx,
 int dy)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> lnk,
 <a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> requestor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates position of a path element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#mustShowContextMenu()">mustShowContextMenu</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#needAdjustToPreferred()">needAdjustToPreferred</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if shape can be resized to a preferred size.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildren</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelf</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#preferredDimension(java.awt.Dimension,int,int)">preferredDimension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#rememberBounds()">rememberBounds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remember old bounds</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#rememberBounds(java.awt.Rectangle)">rememberBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)">removePresentationElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 boolean resizeParent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes object view from container.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#selectPathsForMoving(java.util.List)">selectPathsForMoving</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; subPresentationElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Select paths to move with current symbol from deep structure.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setConcurrent(boolean)">setConcurrent</a><wbr/>(boolean concurrent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> el)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHidden(boolean)">setHidden</a><wbr/>(boolean hidden)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPosition()">setPosition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets life line view position depending on this object parent position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simpleSetBounds(java.awt.Rectangle,boolean,boolean)">simpleSetBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rct,
 boolean moveChildren,
 boolean calculatePrefSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets bounds for this container shape view and all its components</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sRemovePresentationElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given child</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">sSetElement</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> el)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#useParentStyle()">useParentStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Use parent font always</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</h3>
<code>addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosize, autosizeByChildren, calculateAutosizeDimension, canMoveChildOutside, checkShowsProxy, childrenBoundsForReshape, clearShowsProxy, constructLayoutHelper, correctChildrenVector, getChildrenBounds, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementIndex, getPresentationElements, getProxyPresentationElementsStream, getRemovableChildren, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalAppendChildRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalSetChildren, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChildren, paintChildrenBackground, prefDimensionByManipulatedChildren, recursiveAutosize, removePresentationElement, sAddPresentationElement, setBounds, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, sSetPresentationElements</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></h3>
<code><a href="ShapeElement.html#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addBreakPoints</a>, <a href="ShapeElement.html#adjustOnEdge()">adjustOnEdge</a>, <a href="ShapeElement.html#adjustOnEdge(java.awt.Rectangle,int,int,int)">adjustOnEdge</a>, <a href="ShapeElement.html#adjustOnEdgeChildren()">adjustOnEdgeChildren</a>, <a href="ShapeElement.html#autosize()">autosize</a>, <a href="ShapeElement.html#autosizeAndResizeParent()">autosizeAndResizeParent</a>, <a href="ShapeElement.html#calculateAdjustOnEdgeLocation(java.awt.Rectangle)">calculateAdjustOnEdgeLocation</a>, <a href="ShapeElement.html#calculateAndGetMinimumShrinkingDimension(int,int)">calculateAndGetMinimumShrinkingDimension</a>, <a href="ShapeElement.html#calculateAndGetPreferredDimension()">calculateAndGetPreferredDimension</a>, <a href="ShapeElement.html#calculateEdge()">calculateEdge</a>, <a href="ShapeElement.html#calculateMinimumDimension()">calculateMinimumDimension</a>, <a href="ShapeElement.html#calculateOnEdgeBounds()">calculateOnEdgeBounds</a>, <a href="ShapeElement.html#calculatePreferredDimension()">calculatePreferredDimension</a>, <a href="ShapeElement.html#calculatePreferredDimension(int,int)">calculatePreferredDimension</a>, <a href="ShapeElement.html#canBeAutosized()">canBeAutosized</a>, <a href="ShapeElement.html#canHavePaths()">canHavePaths</a>, <a href="ShapeElement.html#clearOldRect()">clearOldRect</a>, <a href="ShapeElement.html#edgeChanged()">edgeChanged</a>, <a href="ShapeElement.html#ensureDimension(boolean)">ensureDimension</a>, <a href="ShapeElement.html#ensurePreferredDimensionIfShrinkable()">ensurePreferredDimensionIfShrinkable</a>, <a href="ShapeElement.html#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)">ensurePreferredDimensionIfShrinkable</a>, <a href="ShapeElement.html#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)">findFreePlaceForShapeOnBorder</a>, <a href="ShapeElement.html#getBorderElementMargin()">getBorderElementMargin</a>, <a href="ShapeElement.html#getBounds()">getBounds</a>, <a href="ShapeElement.html#getCenterlineableInnerParts(int)">getCenterlineableInnerParts</a>, <a href="ShapeElement.html#getDefaultDimension()">getDefaultDimension</a>, <a href="ShapeElement.html#getDimensionForShrinking(int,int)">getDimensionForShrinking</a>, <a href="ShapeElement.html#getEdgeLine(int)">getEdgeLine</a>, <a href="ShapeElement.html#getFixedConnectionPoints()">getFixedConnectionPoints</a>, <a href="ShapeElement.html#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)">getHeaderInsetReduce</a>, <a href="ShapeElement.html#getInsetsForOnEdgeShapes()">getInsetsForOnEdgeShapes</a>, <a href="ShapeElement.html#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="ShapeElement.html#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)">getIntersection</a>, <a href="ShapeElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a>, <a href="ShapeElement.html#getLoadedDimension()">getLoadedDimension</a>, <a href="ShapeElement.html#getMiddlePoint()">getMiddlePoint</a>, <a href="ShapeElement.html#getMiddlePoint(java.awt.Point)">getMiddlePoint</a>, <a href="ShapeElement.html#getMiddlePointX(java.awt.Point)">getMiddlePointX</a>, <a href="ShapeElement.html#getMiddlePointY()">getMiddlePointY</a>, <a href="ShapeElement.html#getMinimumDimension()">getMinimumDimension</a>, <a href="ShapeElement.html#getNearestEdge(int,int)">getNearestEdge</a>, <a href="ShapeElement.html#getNearestEdge(java.awt.Rectangle)">getNearestEdge</a>, <a href="ShapeElement.html#getNeedAutosizeFlag()">getNeedAutosizeFlag</a>, <a href="ShapeElement.html#getNotCopyBounds()">getNotCopyBounds</a>, <a href="ShapeElement.html#getOnEdge()">getOnEdge</a>, <a href="ShapeElement.html#getOnEdgeCornerDistance()">getOnEdgeCornerDistance</a>, <a href="ShapeElement.html#getOnEdgePosition()">getOnEdgePosition</a>, <a href="ShapeElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="ShapeElement.html#getPreferredDimensionForAutosize()">getPreferredDimensionForAutosize</a>, <a href="ShapeElement.html#getReshapeMode()">getReshapeMode</a>, <a href="ShapeElement.html#getSizeForDrawing()">getSizeForDrawing</a>, <a href="ShapeElement.html#getSuspendShapeAutoResizeMode()">getSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#hasManipulator()">hasManipulator</a>, <a href="ShapeElement.html#initialize()">initialize</a>, <a href="ShapeElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a>, <a href="ShapeElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a>, <a href="ShapeElement.html#internalSilentApply()">internalSilentApply</a>, <a href="ShapeElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a>, <a href="ShapeElement.html#isAutosized()">isAutosized</a>, <a href="ShapeElement.html#isCenterlineInner()">isCenterlineInner</a>, <a href="ShapeElement.html#isChildLayoutable(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildLayoutable</a>, <a href="ShapeElement.html#isHorizontalCenterlineProvider()">isHorizontalCenterlineProvider</a>, <a href="ShapeElement.html#isOnEdge()">isOnEdge</a>, <a href="ShapeElement.html#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isShapeOnEdge</a>, <a href="ShapeElement.html#isShrinkable()">isShrinkable</a>, <a href="ShapeElement.html#isSnapShapesOnBorderToGrid()">isSnapShapesOnBorderToGrid</a>, <a href="ShapeElement.html#isUseFixedConnectionPoints()">isUseFixedConnectionPoints</a>, <a href="ShapeElement.html#isVerticalCenterlineProvider()">isVerticalCenterlineProvider</a>, <a href="ShapeElement.html#layoutChildren()">layoutChildren</a>, <a href="ShapeElement.html#maximumDimension(java.awt.Dimension)">maximumDimension</a>, <a href="ShapeElement.html#minimumDimension(java.awt.Dimension)">minimumDimension</a>, <a href="ShapeElement.html#minimumDimensionForShrinking(java.awt.Dimension,int,int)">minimumDimensionForShrinking</a>, <a href="ShapeElement.html#minimumOrMinimumShrinkableDimension(java.awt.Dimension)">minimumOrMinimumShrinkableDimension</a>, <a href="ShapeElement.html#moveLinksToSelf()">moveLinksToSelf</a>, <a href="ShapeElement.html#movePathElements()">movePathElements</a>, <a href="ShapeElement.html#needAdjustToMaximumDimension()">needAdjustToMaximumDimension</a>, <a href="ShapeElement.html#onChildEdgeChange(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">onChildEdgeChange</a>, <a href="ShapeElement.html#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a>, <a href="ShapeElement.html#providesHorizontalCenterline()">providesHorizontalCenterline</a>, <a href="ShapeElement.html#providesVerticalCenterline()">providesVerticalCenterline</a>, <a href="ShapeElement.html#resetCalculatePreferredRegardingChildren()">resetCalculatePreferredRegardingChildren</a>, <a href="ShapeElement.html#setAutosize(boolean)">setAutosize</a>, <a href="ShapeElement.html#setBorderElementMargin(java.lang.String)">setBorderElementMargin</a>, <a href="ShapeElement.html#setCalculatePreferredRegardingChildren(boolean)">setCalculatePreferredRegardingChildren</a>, <a href="ShapeElement.html#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)">setLoadedDimension</a>, <a href="ShapeElement.html#setMinimumDimension(int,int)">setMinimumDimension</a>, <a href="ShapeElement.html#setNeedAutosizeFlag(byte)">setNeedAutosizeFlag</a>, <a href="ShapeElement.html#setOldRect(java.awt.Rectangle)">setOldRect</a>, <a href="ShapeElement.html#setOnEdge(int)">setOnEdge</a>, <a href="ShapeElement.html#setPreferredDimension(int,int)">setPreferredDimension</a>, <a href="ShapeElement.html#setReshapeMode(com.nomagic.magicdraw.uml.symbols.ReshapeMode)">setReshapeMode</a>, <a href="ShapeElement.html#setSnapShapesOnBorderToGrid(boolean)">setSnapShapesOnBorderToGrid</a>, <a href="ShapeElement.html#setSuspendShapeAutoResizeMode(java.lang.String)">setSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#setUseFixedConnectionPoints(boolean)">setUseFixedConnectionPoints</a>, <a href="ShapeElement.html#shouldDrawShadow()">shouldDrawShadow</a>, <a href="ShapeElement.html#simpleSetBounds(int,int,int,int,boolean)">simpleSetBounds</a>, <a href="ShapeElement.html#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a>, <a href="ShapeElement.html#snapsToCenterlines()">snapsToCenterlines</a>, <a href="ShapeElement.html#sSetAutosize(boolean)">sSetAutosize</a>, <a href="ShapeElement.html#sSetBorderElementMargin(java.lang.String)">sSetBorderElementMargin</a>, <a href="ShapeElement.html#sSetBounds(java.awt.Rectangle)">sSetBounds</a>, <a href="ShapeElement.html#sSetSuspendShapeAutoResizeMode(java.lang.String)">sSetSuspendShapeAutoResizeMode</a>, <a href="ShapeElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a>, <a href="ShapeElement.html#toString()">toString</a>, <a href="ShapeElement.html#updateLater()">updateLater</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addConnectedPathElement</a>, <a href="../paths/PathConnector.html#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a>, <a href="../paths/PathConnector.html#disposeConnectedPaths()">disposeConnectedPaths</a>, <a href="../paths/PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">findSymbolForEnd</a>, <a href="../paths/PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)">findSymbolForEnd</a>, <a href="../paths/PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">getConnectedPathElement</a>, <a href="../paths/PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="../paths/PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getPreferredArrowLength()">getPreferredArrowLength</a>, <a href="../paths/PathConnector.html#isShowsProxy()">isShowsProxy</a>, <a href="../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)">movePathElement</a>, <a href="../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">removeConnectedPathElement</a>, <a href="../paths/PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sAddConnectedPathElement</a>, <a href="../paths/PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a>, <a href="../paths/PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a>, <a href="../paths/PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sRemoveConnectedPathElement</a>, <a href="../paths/PathConnector.html#sSetConnectedPathElements(java.util.List)">sSetConnectedPathElements</a>, <a href="../paths/PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible()">supportsVisibleConnectedPathElementsIfSelfInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a>, <a href="../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBounds</a>, <a href="../PresentationElement.html#alwaysShowTooltip()">alwaysShowTooltip</a>, <a href="../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">applyProperties</a>, <a href="../PresentationElement.html#askDeleteDataConfirmation()">askDeleteDataConfirmation</a>, <a href="../PresentationElement.html#atInsertChildren()">atInsertChildren</a>, <a href="../PresentationElement.html#autosizeAndResizeManipulatedParent()">autosizeAndResizeManipulatedParent</a>, <a href="../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">beforeDelete</a>, <a href="../PresentationElement.html#boundsChanged()">boundsChanged</a>, <a href="../PresentationElement.html#boundsChanged(java.awt.Rectangle)">boundsChanged</a>, <a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../PresentationElement.html#canBeDisposedOnUpdate()">canBeDisposedOnUpdate</a>, <a href="../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeElementOwner</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">canChangeParent</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../PresentationElement.html#canFill()">canFill</a>, <a href="../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">changeProperties</a>, <a href="../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">checkProxyVisibility</a>, <a href="../PresentationElement.html#childrenForMoving()">childrenForMoving</a>, <a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)">collectSubShowingPresentationElements</a>, <a href="../PresentationElement.html#coversPoint(int,int)">coversPoint</a>, <a href="../PresentationElement.html#createFillStrategy()">createFillStrategy</a>, <a href="../PresentationElement.html#createPresentationElementStyle()">createPresentationElementStyle</a>, <a href="../PresentationElement.html#createPropertyChangeListener()">createPropertyChangeListener</a>, <a href="../PresentationElement.html#disposePropertyChangeListener()">disposePropertyChangeListener</a>, <a href="../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a>, <a href="../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawBackground</a>, <a href="../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbol</a>, <a href="../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbolBackground</a>, <a href="../PresentationElement.html#dynamicFillColor()">dynamicFillColor</a>, <a href="../PresentationElement.html#dynamicLineColor()">dynamicLineColor</a>, <a href="../PresentationElement.html#dynamicLineWidth()">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicLineWidth(int)">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicPaintShadow()">dynamicPaintShadow</a>, <a href="../PresentationElement.html#dynamicStroke()">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(int)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)">dynamicStyleFillColor</a>, <a href="../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)">dynamicStyleLineColor</a>, <a href="../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)">dynamicStyleTextColor</a>, <a href="../PresentationElement.html#dynamicStyleTransparency()">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)">dynamicStyleValue</a>, <a href="../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">dynamicTextAlignment</a>, <a href="../PresentationElement.html#dynamicTextColor()">dynamicTextColor</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOwnerForChildElement</a>, <a href="../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a>, <a href="../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">findPresentationElement</a>, <a href="../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../PresentationElement.html#generateID()">generateID</a>, <a href="../PresentationElement.html#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>, <a href="../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()">getAdditionalRenderersToNotifyOnPropertiesChange</a>, <a href="../PresentationElement.html#getAssignableModelElementsClasses()">getAssignableModelElementsClasses</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getBoundsWithChildrenOnEdge()">getBoundsWithChildrenOnEdge</a>, <a href="../PresentationElement.html#getCenterlinePoint()">getCenterlinePoint</a>, <a href="../PresentationElement.html#getCenterlinePointX()">getCenterlinePointX</a>, <a href="../PresentationElement.html#getCenterlinePointY()">getCenterlinePointY</a>, <a href="../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)">getChildPresentationElementForContextMenu</a>, <a href="../PresentationElement.html#getChildrenWithSymbolProperties()">getChildrenWithSymbolProperties</a>, <a href="../PresentationElement.html#getConfiguration()">getConfiguration</a>, <a href="../PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="../PresentationElement.html#getDiagramSurface()">getDiagramSurface</a>, <a href="../PresentationElement.html#getDrawComparator()">getDrawComparator</a>, <a href="../PresentationElement.html#getDynamicConfigurations()">getDynamicConfigurations</a>, <a href="../PresentationElement.html#getEffectiveStyleDelegate()">getEffectiveStyleDelegate</a>, <a href="../PresentationElement.html#getEffectiveStyleOwner()">getEffectiveStyleOwner</a>, <a href="../PresentationElement.html#getElementsForRelationshipConnecting()">getElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementToConnectRelationship</a>, <a href="../PresentationElement.html#getFillColor()">getFillColor</a>, <a href="../PresentationElement.html#getFont()">getFont</a>, <a href="../PresentationElement.html#getFontHeight()">getFontHeight</a>, <a href="../PresentationElement.html#getFontRenderContext()">getFontRenderContext</a>, <a href="../PresentationElement.html#getHumanName()">getHumanName</a>, <a href="../PresentationElement.html#getHumanType()">getHumanType</a>, <a href="../PresentationElement.html#getLineColor()">getLineColor</a>, <a href="../PresentationElement.html#getLineWidth()">getLineWidth</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getModelElement()">getModelElement</a>, <a href="../PresentationElement.html#getModelElementsForRelationshipConnecting()">getModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">getModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#getModelElementToMove()">getModelElementToMove</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getOwnStyleDelegate()">getOwnStyleDelegate</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getPreferredBounds()">getPreferredBounds</a>, <a href="../PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="../PresentationElement.html#getPresentationElementAt(int)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementCount()">getPresentationElementCount</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getProjectImpl()">getProjectImpl</a>, <a href="../PresentationElement.html#getProperty(java.lang.String)">getProperty</a>, <a href="../PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="../PresentationElement.html#getPropertyManagerName()">getPropertyManagerName</a>, <a href="../PresentationElement.html#getRenderer()">getRenderer</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#getStyle()">getStyle</a>, <a href="../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSymbolRenderer</a>, <a href="../PresentationElement.html#getTextColor()">getTextColor</a>, <a href="../PresentationElement.html#getTolerance()">getTolerance</a>, <a href="../PresentationElement.html#getVisibility()">getVisibility</a>, <a href="../PresentationElement.html#getVisiblePresentationElements()">getVisiblePresentationElements</a>, <a href="../PresentationElement.html#handleModelDelete()">handleModelDelete</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#hasSharedModelElement()">hasSharedModelElement</a>, <a href="../PresentationElement.html#initializeAndAutosize()">initializeAndAutosize</a>, <a href="../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)">internalBeforeUpdate</a>, <a href="../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">internalCreatePropertyChangeListener</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#internalGetSpecificFont()">internalGetSpecificFont</a>, <a href="../PresentationElement.html#internalGetSpecificTextColor()">internalGetSpecificTextColor</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalSnapToGrid(float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#intersects(int,int,int,int)">intersects</a>, <a href="../PresentationElement.html#invalidate()">invalidate</a>, <a href="../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildVisible</a>, <a href="../PresentationElement.html#isContentHidden()">isContentHidden</a>, <a href="../PresentationElement.html#isCreateElementListener()">isCreateElementListener</a>, <a href="../PresentationElement.html#isDetectable()">isDetectable</a>, <a href="../PresentationElement.html#isDisposed()">isDisposed</a>, <a href="../PresentationElement.html#isLayouting()">isLayouting</a>, <a href="../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNotNull</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isParentOf</a>, <a href="../PresentationElement.html#isPreserveProportionsWhenGrowing()">isPreserveProportionsWhenGrowing</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#isShowElementTypeAsLabel()">isShowElementTypeAsLabel</a>, <a href="../PresentationElement.html#isSortable()">isSortable</a>, <a href="../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">isSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#isTextEditable()">isTextEditable</a>, <a href="../PresentationElement.html#isUseFillColor()">isUseFillColor</a>, <a href="../PresentationElement.html#isUseFillColorByProperty()">isUseFillColorByProperty</a>, <a href="../PresentationElement.html#isUseGradientForFill()">isUseGradientForFill</a>, <a href="../PresentationElement.html#isVisible()">isVisible</a>, <a href="../PresentationElement.html#isVisibleInDiagram()">isVisibleInDiagram</a>, <a href="../PresentationElement.html#isVisibleOrShrunken()">isVisibleOrShrunken</a>, <a href="../PresentationElement.html#movePathElementsRecursively()">movePathElementsRecursively</a>, <a href="../PresentationElement.html#notifyCreated()">notifyCreated</a>, <a href="../PresentationElement.html#notifyDiagramFrameSizeChange()">notifyDiagramFrameSizeChange</a>, <a href="../PresentationElement.html#notifyRepaintManager(boolean)">notifyRepaintManager</a>, <a href="../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildAdd</a>, <a href="../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildRemove</a>, <a href="../PresentationElement.html#onDiagramSurfaceSet()">onDiagramSurfaceSet</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#onFontChange()">onFontChange</a>, <a href="../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">onParentChange</a>, <a href="../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornments</a>, <a href="../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornmentsBackground</a>, <a href="../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenAndAdornments</a>, <a href="../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelfBackground</a>, <a href="../PresentationElement.html#preDisposeOnUpdate()">preDisposeOnUpdate</a>, <a href="../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)">prepareForLineDrawing</a>, <a href="../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)">prepareForTextDrawing</a>, <a href="../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a>, <a href="../PresentationElement.html#recreateListeners()">recreateListeners</a>, <a href="../PresentationElement.html#registerInSortManager()">registerInSortManager</a>, <a href="../PresentationElement.html#removeFromSortManager()">removeFromSortManager</a>, <a href="../PresentationElement.html#removeItSelfOnUpdate()">removeItSelfOnUpdate</a>, <a href="../PresentationElement.html#resizeParent()">resizeParent</a>, <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sAddPresentationElement</a>, <a href="../PresentationElement.html#selectChildrenForMoving()">selectChildrenForMoving</a>, <a href="../PresentationElement.html#selectObjectsForMoving()">selectObjectsForMoving</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setBounds(int,int,int,int)">setBounds</a>, <a href="../PresentationElement.html#setCreateElementListener(boolean)">setCreateElementListener</a>, <a href="../PresentationElement.html#setFont(java.awt.Font)">setFont</a>, <a href="../PresentationElement.html#setLayouting(boolean)">setLayouting</a>, <a href="../PresentationElement.html#setLineColor(java.awt.Color)">setLineColor</a>, <a href="../PresentationElement.html#setLineWidth(int)">setLineWidth</a>, <a href="../PresentationElement.html#setLoadedVisibility(boolean)">setLoadedVisibility</a>, <a href="../PresentationElement.html#setLocation(int,int)">setLocation</a>, <a href="../PresentationElement.html#setLocation(java.awt.Point)">setLocation</a>, <a href="../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">setModelElement</a>, <a href="../PresentationElement.html#setNeedRecreateListeners(boolean)">setNeedRecreateListeners</a>, <a href="../PresentationElement.html#setPropertyManagerName(java.lang.String)">setPropertyManagerName</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#setSize(int,int)">setSize</a>, <a href="../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)">setSize</a>, <a href="../PresentationElement.html#setSize(java.awt.Dimension)">setSize</a>, <a href="../PresentationElement.html#setTextColor(java.awt.Color)">setTextColor</a>, <a href="../PresentationElement.html#setTextEditable(boolean)">setTextEditable</a>, <a href="../PresentationElement.html#setUseFillColor(boolean)">setUseFillColor</a>, <a href="../PresentationElement.html#setVisible(boolean)">setVisible</a>, <a href="../PresentationElement.html#silentApply()">silentApply</a>, <a href="../PresentationElement.html#silentApply(boolean)">silentApply</a>, <a href="../PresentationElement.html#simpleSetBounds(int,int,int,int)">simpleSetBounds</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Point,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapViewToGrid(float)">snapViewToGrid</a>, <a href="../PresentationElement.html#sortObjectsByX(java.util.List)">sortObjectsByX</a>, <a href="../PresentationElement.html#sortObjectsByY(java.util.List)">sortObjectsByY</a>, <a href="../PresentationElement.html#sSetBounds(int,int,int,int)">sSetBounds</a>, <a href="../PresentationElement.html#sSetLocation(int,int)">sSetLocation</a>, <a href="../PresentationElement.html#sSetLocation(java.awt.Point)">sSetLocation</a>, <a href="../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">sSetModelElement</a>, <a href="../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a>, <a href="../PresentationElement.html#sSetParentForAll(java.util.Collection)">sSetParentForAll</a>, <a href="../PresentationElement.html#sSetSize(int,int)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(java.awt.Dimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetVisible(boolean)">sSetVisible</a>, <a href="../PresentationElement.html#tryToDeleteModelElementUponRemoval()">tryToDeleteModelElementUponRemoval</a>, <a href="../PresentationElement.html#update()">update</a>, <a href="../PresentationElement.html#updateAfterLoad()">updateAfterLoad</a>, <a href="../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)">updateLabelsIgnoringSuspendableLater</a>, <a href="../PresentationElement.html#updateModelByView()">updateModelByView</a>, <a href="../PresentationElement.html#updateModelByViewInternal()">updateModelByViewInternal</a>, <a href="../PresentationElement.html#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a>, <a href="../PresentationElement.html#useParentProperties()">useParentProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID</code></div>
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
<section class="detail" id="MIN_EXTENSION">
<h3>MIN_EXTENSION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">MIN_EXTENSION</span></div>
<div class="block">Minimal extension of lifeline line.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView.MIN_EXTENSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MIN_LENGTH">
<h3>MIN_LENGTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">MIN_LENGTH</span></div>
<div class="block">Minimal length of lifeline line.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView.MIN_LENGTH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CROSS_WIDTH">
<h3>CROSS_WIDTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CROSS_WIDTH</span></div>
<div class="block">cross width</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView.CROSS_WIDTH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CROSS_DELTA">
<h3>CROSS_DELTA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CROSS_DELTA</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView.CROSS_DELTA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DELTA_Y">
<h3>DELTA_Y</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DELTA_Y</span></div>
<div class="block">constants for concurrent lifeline dimensions</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView.DELTA_Y">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DELTA_X">
<h3>DELTA_X</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DELTA_X</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.LifeLineLineView.DELTA_X">Constant Field Values</a></li>
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
<h3>LifeLineLineView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LifeLineLineView</span>()</div>
<div class="block">Creates a new life line view.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>LifeLineLineView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LifeLineLineView</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span></div>
<div class="block">Creates and initializes a new life line view from specified parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - this life line view parent object.</dd>
</dl>
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
<section class="detail" id="getStateInvariants()">
<h3>getStateInvariants</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="StateInvariantView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StateInvariantView</a>&gt;</span> <span class="element-name">getStateInvariants</span>()</div>
<div class="block">Gets state invariants lying on this lifeline line.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of state invariants.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStateInvariants()">
<h3>hasStateInvariants</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasStateInvariants</span>()</div>
<div class="block">Indicates if this life line has any state invariants on it.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this life line has any state invariants, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastStateInvariantPosition()">
<h3>getLastStateInvariantPosition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLastStateInvariantPosition</span>()</div>
<div class="block">Calculates y coordinate of this lifeline line to cover the last state invariant
 lying on it.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>last state invariant y position.</dd>
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
<section class="detail" id="paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>paintChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintChildren</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>paintChildren</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalGetPresentationElementStroke(int)">
<h3>internalGetPresentationElementStroke</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">internalGetPresentationElementStroke</span><wbr/><span class="parameters">(int width)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#internalGetPresentationElementStroke(int)">PresentationElement</a></code></span></div>
<div class="block">Return a stroke used to paint symbol's main part</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>width</code> - a custom stroke width. Other stroke parameters will be specific to symbol</dd>
<dt>Returns:</dt>
<dd>a stroke used to paint symbol's main part</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dynamicStroke(java.awt.BasicStroke)">
<h3>dynamicStroke</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">dynamicStroke</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a> stroke)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateDestroyTimePoint()">
<h3>calculateDestroyTimePoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">calculateDestroyTimePoint</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getMiddlePointX()">
<h3>getMiddlePointX</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMiddlePointX</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#getMiddlePointX()">getMiddlePointX</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>canAddInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddInstance</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block">Checks can this life line view add specified object or not.
 LifeLineView can add Activation and SequenceBaseMessageView objects.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>canAddInstance</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>symbol</code> - specified PresentationElement object.</dd>
<dt>Returns:</dt>
<dd>true if this object can add specified object
 otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>canAddChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddChild</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PresentationElement</a></code></span></div>
<div class="block">Check of given symbol can be added as child into this symbol.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>canAddChild</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>symbol</code> - symbol</dd>
<dt>Returns:</dt>
<dd>true if symbol can be added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selectPathsForMoving(java.util.List)">
<h3>selectPathsForMoving</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</span> <span class="element-name">selectPathsForMoving</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; subPresentationElements)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#selectPathsForMoving(java.util.List)">PresentationElement</a></code></span></div>
<div class="block">Select paths to move with current symbol from deep structure.
 Some paths can be connected to current symbol, but owned in some deep child of this symbol.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../paths/PathConnector.html#selectPathsForMoving(java.util.List)">selectPathsForMoving</a></code> in class <code><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
<dt>Parameters:</dt>
<dd><code>subPresentationElements</code> - sub children of this symbol</dd>
<dt>Returns:</dt>
<dd>paths to move together with current symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPosition()">
<h3>setPosition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPosition</span>()</div>
<div class="block">Sets life line view position depending on this object parent position.
 Moves all links and connection points.</div>
</section>
</li>
<li>
<section class="detail" id="moveChild(com.nomagic.magicdraw.uml.symbols.PresentationElement,int,int)">
<h3>moveChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">moveChild</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 int dx,
 int dy)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>moveChild</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simpleSetBounds(java.awt.Rectangle,boolean,boolean)">
<h3>simpleSetBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">simpleSetBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rct,
 boolean moveChildren,
 boolean calculatePrefSize)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></span></div>
<div class="block">Sets bounds for this container shape view and all its components</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>simpleSetBounds</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>rct</code> - container shape view bounding rectangle</dd>
<dd><code>moveChildren</code> - if moveChildren equals true then this method calls</dd>
<dd><code>calculatePrefSize</code> - calculate preferred size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotZoomedTolerance()">
<h3>getNotZoomedTolerance</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">getNotZoomedTolerance</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getNotZoomedTolerance()">getNotZoomedTolerance</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>coversPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">coversPoint</span><wbr/><span class="parameters">(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">checks if object covers provided point</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">coversPoint</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if object covers this point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="needAdjustToPreferred()">
<h3>needAdjustToPreferred</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">needAdjustToPreferred</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="ShapeElement.html#needAdjustToPreferred()">ShapeElement</a></code></span></div>
<div class="block">Check if shape can be resized to a preferred size. Usually it is true if shape is manipulated and isAutosize is true.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>needAdjustToPreferred</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Returns:</dt>
<dd>true if adjustments are necessary</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManipulationBounds(java.awt.Point)">
<h3>getManipulationBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getManipulationBounds</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getManipulationBounds(java.awt.Point)">PresentationElement</a></code></span></div>
<div class="block">Gets manipulation bounds of the symbol. Manipulation bounds might
 differ from symbol bounds, they can be larger or smaller to help
 user manipulate the symbol.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getManipulationBounds(java.awt.Point)">getManipulationBounds</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>relativePoint</code> - active user point to construct manipulation bounds.</dd>
<dt>Returns:</dt>
<dd>symbol manipulation bounds.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBoundsToRepaint()">
<h3>getBoundsToRepaint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBoundsToRepaint</span>()</div>
<div class="block">Return bounds of the symbol that must be repainted.
 throws NoRectangleDefinedException</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getBoundsToRepaint()">getBoundsToRepaint</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>rectangle of bounds</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">
<h3>movePathElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">movePathElement</span><wbr/><span class="parameters">(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> lnk,
 <a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> requestor)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">PathConnector</a></code></span></div>
<div class="block">Calculates position of a path element.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>lnk</code> - element which position will be calculated.</dd>
<dd><code>requestor</code> - the requestor of this path moving. Implementations may check to avoid endless loops.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getPresentationElementAt</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getPresentationElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">Searches and returns object that covers given point.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getPresentationElementAt</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>point</code> - given point</dd>
<dd><code>kind</code> - intersection kind to check for</dd>
<dt>Returns:</dt>
<dd>PresentationElement that covers specified point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSortedActivations()">
<h3>getSortedActivations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a>&gt;</span> <span class="element-name">getSortedActivations</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>sorted activations by y ascending.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMiddlePointY(java.awt.Point)">
<h3>getMiddlePointY</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMiddlePointY</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#getMiddlePointY(java.awt.Point)">getMiddlePointY</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="LifeLineLineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LifeLineLineView</a></span> <span class="element-name">clone</span>()</div>
<div class="block">Clones this object.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#clone()">clone</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>clone</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Returns:</dt>
<dd>copy of this object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivationsIterator()">
<h3>getActivationsIterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a>&gt;</span> <span class="element-name">getActivationsIterator</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all activations</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastActivation()">
<h3>getLastActivation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a></span> <span class="element-name">getLastActivation</span>()</div>
<div class="block">Returns last activation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Activation object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastStateInvariant()">
<h3>getLastStateInvariant</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="StateInvariantView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">StateInvariantView</a></span> <span class="element-name">getLastStateInvariant</span>()</div>
<div class="block">Returns last state invariant.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>state invariant symbol;</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivationAt(int)">
<h3>getActivationAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a></span> <span class="element-name">getActivationAt</span><wbr/><span class="parameters">(int y)</span></div>
<div class="block">Returns Activation at specified point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>y</code> - point y</dd>
<dt>Returns:</dt>
<dd>activation what covers specified point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClosestActivationAt(int)">
<h3>getClosestActivationAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a></span> <span class="element-name">getClosestActivationAt</span><wbr/><span class="parameters">(int ptY)</span></div>
<div class="block">Finds closest activation on this lifeline line at a given point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ptY</code> - Y of point closest to which an activation should be found</dd>
<dt>Returns:</dt>
<dd>closest activation at a given point</dd>
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
<dd><code>accept</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
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
<section class="detail" id="editName(java.awt.event.KeyEvent,java.util.Map)">
<h3>editName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">editName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/KeyEvent.html" title="class or interface in java.awt.event">KeyEvent</a> evt,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; textEditorOptions)</span></div>
<div class="block">Does nothing -- prevent from editing name box,
 which is an attribute of container.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>evt</code> - first key event or null</dd>
<dd><code>textEditorOptions</code> - boolean options for text editor. Passed when creating text editor with
                          <code>TextEditorFactory</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalGetManipulatedChildrenRect(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel)">
<h3>internalGetManipulatedChildrenRect</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">internalGetManipulatedChildrenRect</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></span></div>
<div class="block">Calculate union area of owned manipulated children added not on a shape border</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalGetManipulatedChildrenRect</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>insetsLevel</code> - include insets if shape has manipulated children</dd>
<dt>Returns:</dt>
<dd>rectangle of children or null if there are no children</dd>
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
<section class="detail" id="disposeChildren()">
<h3>disposeChildren</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">disposeChildren</span>()</div>
<div class="block">Removes all children from itself. Such removing causes
 calling dispose for every child.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#disposeChildren()">disposeChildren</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="adjustBounds(java.awt.Rectangle)">
<h3>adjustBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">adjustBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span></div>
<div class="block">Adjust bounds
 1. if lifeline is not concurrent, y must be seq bottom
 2. (Disabled) if lifeline is concurrent y must be below parent life line upper point
 disabled because adjust bounds for moving does it
 3. if lifeline is concurrent. x must be same as parent x+parent.width</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#adjustBounds(java.awt.Rectangle)">adjustBounds</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>r</code> - bounds</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConcurrent(boolean)">
<h3>setConcurrent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setConcurrent</span><wbr/><span class="parameters">(boolean concurrent)</span></div>
</section>
</li>
<li>
<section class="detail" id="isConcurrent()">
<h3>isConcurrent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isConcurrent</span>()</div>
</section>
</li>
<li>
<section class="detail" id="correctInnerStateInvariantBounds()">
<h3>correctInnerStateInvariantBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">correctInnerStateInvariantBounds</span>()</div>
<div class="block">Adjust bounds of inner state invariants according bounds of this lifeline.</div>
</section>
</li>
<li>
<section class="detail" id="correctStateInvariantBounds(java.awt.Rectangle)">
<h3>correctStateInvariantBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">correctStateInvariantBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
<div class="block">Adjusts bounds of a given state invariant so that it lies correctly on
 this lifeline line.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bounds</code> - bounds of state invariant to adjust.</dd>
<dt>Returns:</dt>
<dd>true if bounds were adjusted, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="preferredDimension(java.awt.Dimension,int,int)">
<h3>preferredDimension</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">preferredDimension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>preferredDimension</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="useParentStyle()">
<h3>useParentStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">useParentStyle</span>()</div>
<div class="block">Use parent font always</div>
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
<section class="detail" id="getDynamicStyleOwner()">
<h3>getDynamicStyleOwner</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getDynamicStyleOwner</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getDynamicStyleOwner()">getDynamicStyleOwner</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUpperPointY()">
<h3>getUpperPointY</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getUpperPointY</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setHidden(boolean)">
<h3>setHidden</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHidden</span><wbr/><span class="parameters">(boolean hidden)</span></div>
</section>
</li>
<li>
<section class="detail" id="isHidden()">
<h3>isHidden</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isHidden</span>()</div>
</section>
</li>
<li>
<section class="detail" id="calculateActivationsBounds()">
<h3>calculateActivationsBounds</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">calculateActivationsBounds</span>()</div>
</section>
</li>
<li>
<section class="detail" id="adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">
<h3>adjustBoundsBeforeChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">adjustBoundsBeforeChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rec,
 boolean autosizeOperation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether)</span></div>
<div class="block">validate bounds for moving</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>adjustBoundsBeforeChange</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateAutosizeDimension(java.awt.Dimension,int,int,int,int)">
<h3>calculateAutosizeDimension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">calculateAutosizeDimension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size,
 int locationX,
 int locationY,
 int prefSizeWidth,
 int prefSizeHeight)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="ShapeElement.html#calculateAutosizeDimension(java.awt.Dimension,int,int,int,int)">ShapeElement</a></code></span></div>
<div class="block">Calculates size of shape to be at least as preferred and fit all children</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>calculateAutosizeDimension</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>size</code> - size</dd>
<dd><code>locationX</code> - x location</dd>
<dd><code>locationY</code> - y location</dd>
<dd><code>prefSizeWidth</code> - preferred size width</dd>
<dd><code>prefSizeHeight</code> - preferred size height</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObject()">
<h3>getObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SequenceLifelineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">SequenceLifelineView</a></span> <span class="element-name">getObject</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>owner - SequenceLifelineView</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllMessages()">
<h3>getAllMessages</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView&gt;</span> <span class="element-name">getAllMessages</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getIncomingMessageWithType(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort)">
<h3>getIncomingMessageWithType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.paths.SeqBaseMessageView</span> <span class="element-name">getIncomingMessageWithType</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a> type)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - message type</dd>
<dt>Returns:</dt>
<dd>incoming message of give sort type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">returns parent data</div>
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
<section class="detail" id="getLifeline()">
<h3>getLifeline</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></span> <span class="element-name">getLifeline</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isSnapToGrid()">
<h3>isSnapToGrid</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isSnapToGrid</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#isSnapToGrid()">isSnapToGrid</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>sSetElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetElement</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> el)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">sSetElement</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setElement</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> el)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActualElement()">
<h3>getActualElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getActualElement</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getActualElement()">PresentationElement</a></code></span></div>
<div class="block">Because some views returns theirs parent model element, we do not know have they this member
 set or not.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getActualElement()">getActualElement</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMovableByMoveManager()">
<h3>isMovableByMoveManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMovableByMoveManager</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#isMovableByMoveManager()">PresentationElement</a></code></span></div>
<div class="block">Method indicates if object of this instance must be registered in move manager.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#isMovableByMoveManager()">isMovableByMoveManager</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../PresentationElement.html#isMovableByMoveManager()"><code>PresentationElement.isMovableByMoveManager()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseEntireActivation()">
<h3>isUseEntireActivation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseEntireActivation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="internalUpdatePresentationElement()">
<h3>internalUpdatePresentationElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalUpdatePresentationElement</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#internalUpdatePresentationElement()">PresentationElement</a></code></span></div>
<div class="block">Internal symbol update method for subclassing. It is called from update as part of full
 update action.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalUpdatePresentationElement</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../PresentationElement.html#update()"><code>PresentationElement.update()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSeqContainer()">
<h3>getSeqContainer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.SequenceObjectViewContainer</span> <span class="element-name">getSeqContainer</span>()</div>
</section>
</li>
<li>
<section class="detail" id="rememberBounds()">
<h3>rememberBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">rememberBounds</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#rememberBounds()">PresentationElement</a></code></span></div>
<div class="block">Remember old bounds</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#rememberBounds()">rememberBounds</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="rememberBounds(java.awt.Rectangle)">
<h3>rememberBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">rememberBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#rememberBounds(java.awt.Rectangle)">rememberBounds</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)">
<h3>removePresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePresentationElement</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 boolean resizeParent)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></span></div>
<div class="block">Removes object view from container.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>removePresentationElement</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - object to remove</dd>
<dd><code>resizeParent</code> - resize parent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>checkElementOwnerOnChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">checkElementOwnerOnChange</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
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
<section class="detail" id="getNestedLines()">
<h3>getNestedLines</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="LifeLineLineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LifeLineLineView</a>&gt;</span> <span class="element-name">getNestedLines</span>()</div>
<div class="block">Returns nested lifeline lines.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of nested lifeline list or empty list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNestedLinesIterator()">
<h3>getNestedLinesIterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="LifeLineLineView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">LifeLineLineView</a>&gt;</span> <span class="element-name">getNestedLinesIterator</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>nested lifeline lines</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivations()">
<h3>getActivations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ActivationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ActivationView</a>&gt;</span> <span class="element-name">getActivations</span>()</div>
<div class="block">Gets activations placed on this lifeline line.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of activations placed on this line.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDestroyed()">
<h3>isDestroyed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDestroyed</span>()</div>
<div class="block">Gets destroyed value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>destroyed value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ensureDestructionOccurrence(boolean)">
<h3>ensureDestructionOccurrence</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">ensureDestructionOccurrence</span><wbr/><span class="parameters">(boolean destruct)</span></div>
<div class="block">Ensures that a proper destruction occurrence is in the model on this lifeline.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>destruct</code> - indicates whether lifeline is destructed or not.</dd>
<dt>Returns:</dt>
<dd>true if destruction event was changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNested()">
<h3>isNested</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNested</span>()</div>
<div class="block">Indicates if this lifeline line is nested (not root).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this lifeline line is nested, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalLayoutChildren(boolean)">
<h3>internalLayoutChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalLayoutChildren</span><wbr/><span class="parameters">(boolean calculatePrefSize)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>internalLayoutChildren</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>sRemovePresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sRemovePresentationElement</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PresentationElement</a></code></span></div>
<div class="block">Removes given child</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>sRemovePresentationElement</code> in class <code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - child</dd>
</dl>
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
<section class="detail" id="createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">
<h3>createBoundsShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></span> <span class="element-name">createBoundsShape</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 <a href="../BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols">BoundsTransformation</a> transformation)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="ShapeElement.html#createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">ShapeElement</a></code></span></div>
<div class="block">Creates bounding shape for intersection calculation.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="ShapeElement.html#createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">createBoundsShape</a></code> in class <code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>path</code> - path</dd>
<dd><code>transformation</code> - transformation</dd>
<dt>Returns:</dt>
<dd>shape</dd>
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
