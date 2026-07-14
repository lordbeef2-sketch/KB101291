# JAVA OPENAPI: ShapeElement (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/shapes/ShapeElement.html
- source_path: `com/nomagic/magicdraw/uml/symbols/shapes/ShapeElement.html`
- source_sha256: `638386dd52a4cf9f6d5dcebd64098b450b4953a21544a9e2475d668e3c729580`
- captured_utc: `2026-07-14T16:56:04.948565+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.shapes](package-summary.html)

## Class ShapeElement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](../paths/PathConnector.html)
com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement

All Implemented Interfaces:
`[BaseElement](../../BaseElement.html)`, `[MDElement](../../MDElement.html)`, `[ModelElementProvider](../../ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`, `com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView`, `[NNaryAssociationView](NNaryAssociationView.html)`

@OpenApipublic abstract classShapeElement
extends [PathConnector](../paths/PathConnector.html)
implements com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape, com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider

Base class for all kinds of "shape" like symbols.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BORDER_ELEMENT_MARGIN_ALL](#BORDER_ELEMENT_MARGIN_ALL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BORDER_ELEMENT_MARGIN_BOTTOM](#BORDER_ELEMENT_MARGIN_BOTTOM)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BORDER_ELEMENT_MARGIN_LEFT](#BORDER_ELEMENT_MARGIN_LEFT)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BORDER_ELEMENT_MARGIN_LEFT_RIGHT](#BORDER_ELEMENT_MARGIN_LEFT_RIGHT)`

`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[BORDER_ELEMENT_MARGIN_MODES](#BORDER_ELEMENT_MARGIN_MODES)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BORDER_ELEMENT_MARGIN_NONE](#BORDER_ELEMENT_MARGIN_NONE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BORDER_ELEMENT_MARGIN_RIGHT](#BORDER_ELEMENT_MARGIN_RIGHT)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BORDER_ELEMENT_MARGIN_TOP](#BORDER_ELEMENT_MARGIN_TOP)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BORDER_ELEMENT_MARGIN_TOP_BOTTOM](#BORDER_ELEMENT_MARGIN_TOP_BOTTOM)`

`static final int`
`[BOTTOM_EDGE](#BOTTOM_EDGE)`

`static final int`
`[INSIDE_EDGE_POSITION](#INSIDE_EDGE_POSITION)`

`static final int`
`[LEFT_EDGE](#LEFT_EDGE)`

`static final byte`
`[NEED_AUTOSIZE_FULL](#NEED_AUTOSIZE_FULL)`
Flag for doing full autosize - calculation of preferred size and children layout
`static final byte`
`[NEED_AUTOSIZE_LAYOUT](#NEED_AUTOSIZE_LAYOUT)`
Flag for doing only children layout during autosize
`static final byte`
`[NEED_AUTOSIZE_NONE](#NEED_AUTOSIZE_NONE)`
Flag for ignoring autosize
`static final int`
`[NO_EDGE](#NO_EDGE)`

`static final com.nomagic.ui.UnmodifiableInsets`
`[NULL_INSETS](#NULL_INSETS)`
Insets with all locations equal to 0
`static final int`
`[ON_EDGE_POSITION](#ON_EDGE_POSITION)`

`static final int`
`[OUTSIDE_EDGE_POSITION](#OUTSIDE_EDGE_POSITION)`

`static final int`
`[RIGHT_EDGE](#RIGHT_EDGE)`

`static final int`
`[SPACE](#SPACE)`
Space between bounds and some inner object.
`static final com.nomagic.ui.UnmodifiableInsets`
`[SPACE_INSETS](#SPACE_INSETS)`
Insets with all locations equal to SPACE
`static final com.nomagic.ui.UnmodifiableInsets`
`[SPACE_INSETS_EMPTY_TOP_BOTTOM](#SPACE_INSETS_EMPTY_TOP_BOTTOM)`
Insets with top/bottom equals to zero and right/left equals to SPACE
`static final int`
`[TOP_EDGE](#TOP_EDGE)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[showsProxy](../paths/PathConnector.html#showsProxy)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DEFAULT_LINE_WIDTH](../PresentationElement.html#DEFAULT_LINE_WIDTH), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [HANDLE_SIZE](../PresentationElement.html#HANDLE_SIZE), [MAX_LINE_WIDTH](../PresentationElement.html#MAX_LINE_WIDTH), [MIN_LINE_WIDTH](../PresentationElement.html#MIN_LINE_WIDTH), [peStyle](../PresentationElement.html#peStyle), [SHADOW_WIDTH](../PresentationElement.html#SHADOW_WIDTH), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ShapeElement](#%3Cinit%3E())()`

`[ShapeElement](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) parent)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../../Visitor.html) visitor)`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
`protected void`
`[addBreakPoints](#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](../paths/PathElement.html) link)`
Adds break points to link to self.
`void`
`[adjustBounds](#adjustBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`
Validates bounds
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[adjustBoundsBeforeChange](#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rec,
 boolean autosizeOperation,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)> movedTogether)`
Validate bounds before bounds change operation
`void`
`[adjustOnEdge](#adjustOnEdge())()`
Adjust shape on the edge of its parent.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[adjustOnEdge](#adjustOnEdge(java.awt.Rectangle,int,int,int))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds,
 int edge,
 int position,
 int cornerDistance)`
Calculates location of given rectangle according given parent edge and position on edge.
`void`
`[adjustOnEdgeChildren](#adjustOnEdgeChildren())()`
Adjust on edge all children
`final void`
`[autosize](#autosize())()`

`void`
`[autosize](#autosize(boolean))(boolean calculatePrefSize)`
Calculate preferred size and make this shape size at least as preferred (if size is smaller)
`void`
`[autosizeAndResizeParent](#autosizeAndResizeParent())()`
Resize itself and initiate parent resize
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[calculateAdjustOnEdgeLocation](#calculateAdjustOnEdgeLocation(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`
Calculates on edge location for a shape.
`[UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[calculateAndGetMinimumShrinkingDimension](#calculateAndGetMinimumShrinkingDimension(int,int))(int locationX,
 int locationY)`

`[UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[calculateAndGetPreferredDimension](#calculateAndGetPreferredDimension())()`

`protected void`
`[calculateAutosizeDimension](#calculateAutosizeDimension(java.awt.Dimension,int,int,int,int))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size,
 int locationX,
 int locationY,
 int prefSizeWidth,
 int prefSizeHeight)`
Calculates size of shape to be at least as preferred and fit all children
`void`
`[calculateEdge](#calculateEdge())()`

`final void`
`[calculateMinimumDimension](#calculateMinimumDimension())()`
calculates minimum size
`protected com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds`
`[calculateOnEdgeBounds](#calculateOnEdgeBounds())()`

`final void`
`[calculatePreferredDimension](#calculatePreferredDimension())()`

`final void`
`[calculatePreferredDimension](#calculatePreferredDimension(int,int))(int locationX,
 int locationY)`

`protected boolean`
`[canBeAutosized](#canBeAutosized())()`

`boolean`
`[canHavePaths](#canHavePaths())()`

`final void`
`[clearOldRect](#clearOldRect())()`

`[ShapeElement](ShapeElement.html)`
`[clone](#clone())()`

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
`[edgeChanged](#edgeChanged())()`

`final void`
`[ensureDimension](#ensureDimension(boolean))(boolean rememberBounds)`
If size is smaller than the preferred size, makes shape larger.
`void`
`[ensurePreferredDimensionIfShrinkable](#ensurePreferredDimensionIfShrinkable())()`

`void`
`[ensurePreferredDimensionIfShrinkable](#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`

`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[findFreePlaceForShapeOnBorder](#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle))([ShapeElement](ShapeElement.html) shape,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) shapeB)`
Looks for available position slot for given shape on a border
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getBorderElementMargin](#getBorderElementMargin())()`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBounds](#getBounds())()`
Method returns bounds of this element.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape>`
`[getCenterlineableInnerParts](#getCenterlineableInnerParts(int))(int orientation)`
Gets shape inner parts which have centerlines.
`com.nomagic.ui.UnmodifiableInsets`
`[getChildrenInsets](#getChildrenInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel))(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)`

`protected [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[getDefaultDimension](#getDefaultDimension())()`

`[UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[getDimensionForShrinking](#getDimensionForShrinking(int,int))(int width,
 int height)`

`[Line](../../../../awt/Line.html)`
`[getEdgeLine](#getEdgeLine(int))(int edge)`
Returns a line representing a specified edge.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)[]`
`[getFixedConnectionPoints](#getFixedConnectionPoints())()`
-----1------
 | |
 | |
 4 2
 | |
 | |
 ----3-------
`protected int`
`[getHeaderInsetReduce](#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds))(int edge,
 com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds bounds)`

`protected [Insets](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Insets.html)`
`[getInsetsForOnEdgeShapes](#getInsetsForOnEdgeShapes())()`

`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getIntersection](#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement))(int x1,
 int y1,
 int x2,
 int y2,
 [PathElement](../paths/PathElement.html) path)`
Gets intersection point between shape view bounding rectangle
 and line.
`static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getIntersection](#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape))(int x1,
 int y1,
 int x2,
 int y2,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds,
 [ContainerShape](../../../../awt/ContainerShape.html) boundingShape)`
Gets intersection point between bounding shape (or rectangle) and line.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getIntersection](#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement))(int x,
 int y,
 [PathElement](../paths/PathElement.html) path)`

`[UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[getLoadedDimension](#getLoadedDimension())()`

`[PresentationElement](../PresentationElement.html)`
`[getManipulatedElementAt](#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind intersectionKind)`
Gets manipulated symbol at specified point pt.
`[UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[getManipulationPreferredDimension](#getManipulationPreferredDimension())()`

`final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getMiddlePoint](#getMiddlePoint())()`
Returns middle point of this element.
`final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getMiddlePoint](#getMiddlePoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) rel)`
Gets middle point of this view,
`int`
`[getMiddlePointX](#getMiddlePointX())()`

`int`
`[getMiddlePointX](#getMiddlePointX(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) rel)`

`int`
`[getMiddlePointY](#getMiddlePointY())()`

`int`
`[getMiddlePointY](#getMiddlePointY(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) rel)`

`final [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[getMinimumDimension](#getMinimumDimension())()`
get minimum possible size for object
`int`
`[getNearestEdge](#getNearestEdge(int,int))(int x,
 int y)`
Return the nearest edge to given point.
`int`
`[getNearestEdge](#getNearestEdge(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`
Return the nearest edge to given rectangle.
`byte`
`[getNeedAutosizeFlag](#getNeedAutosizeFlag())()`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getNotCopyBounds](#getNotCopyBounds())()`
get not copy bounds of object throws NoRectangleDefinedException
`int`
`[getOnEdge](#getOnEdge())()`
Returns some edge constant if this shape must be on its parent edge.
`int`
`[getOnEdgeCornerDistance](#getOnEdgeCornerDistance())()`

`int`
`[getOnEdgePosition](#getOnEdgePosition())()`
Returns position on edge.
`final [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[getPreferredDimension](#getPreferredDimension())()`
Returns preferable dimension of the element.
`[UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[getPreferredDimensionForAutosize](#getPreferredDimensionForAutosize())()`
Returns preferable dimension of the element for autosize.This implementation simple returns
 preferred size.
`com.nomagic.magicdraw.uml.symbols.ReshapeMode`
`[getReshapeMode](#getReshapeMode())()`

`[UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html)`
`[getSizeForDrawing](#getSizeForDrawing())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSuspendShapeAutoResizeMode](#getSuspendShapeAutoResizeMode())()`

`boolean`
`[hasManipulator](#hasManipulator())()`
Returns true, if view has manipulator (is selectable)
`void`
`[initialize](#initialize())()`
Initialize symbol and its children state.
`void`
`[internalApplyProperties](#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)`
Applies properties from given property manager
`[Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html)`
`[internalGetBoundsShape](#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape))([ConverterToShape](../ConverterToShape.html) converterToShape)`

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
`[isAutosized](#isAutosized())()`
Returns autosize flag.
`boolean`
`[isCenterlineInner](#isCenterlineInner())()`
Indicates if the centerline provided by this shape is provided by its inner parts, not the shape itself.
`boolean`
`[isChildLayoutable](#isChildLayoutable(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) child)`
Check if given child is "layoutable" - it means this shape controls the bounds of child inside layoutChildren() method.
`boolean`
`[isHorizontalCenterlineProvider](#isHorizontalCenterlineProvider())()`
Indicates whether this shape provides horizontal center-lines to other shapes.
`boolean`
`[isOnEdge](#isOnEdge())()`
Returns true if symbol is on edge
`static boolean`
`[isShapeOnEdge](#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) symbol)`

`boolean`
`[isShrinkable](#isShrinkable())()`

`static boolean`
`[isSnapShapesOnBorderToGrid](#isSnapShapesOnBorderToGrid())()`

`protected boolean`
`[isSnapToGrid](#isSnapToGrid())()`

`boolean`
`[isUseFixedConnectionPoints](#isUseFixedConnectionPoints())()`

`boolean`
`[isVerticalCenterlineProvider](#isVerticalCenterlineProvider())()`
Indicates whether this shape provides vertical center-lines to other shapes.
`void`
`[layoutChildren](#layoutChildren())()`
Layout children of this shape.
`void`
`[layoutChildren](#layoutChildren(boolean))(boolean calculatePrefSize)`
Layout children of this shape.
`protected void`
`[maximumDimension](#maximumDimension(java.awt.Dimension))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size)`

`protected void`
`[minimumDimension](#minimumDimension(java.awt.Dimension))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) min)`
calculates minimum size
`void`
`[minimumDimensionForShrinking](#minimumDimensionForShrinking(java.awt.Dimension,int,int))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size,
 int locationX,
 int locationY)`

`protected void`
`[minimumOrMinimumShrinkableDimension](#minimumOrMinimumShrinkableDimension(java.awt.Dimension))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size)`

`protected void`
`[moveLinksToSelf](#moveLinksToSelf())()`
Move links to self.
`protected void`
`[movePathElement](#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector))([PathElement](../paths/PathElement.html) path,
 [PathConnector](../paths/PathConnector.html) requestor)`
Calculates position of a path element.
`void`
`[movePathElements](#movePathElements())()`

`protected boolean`
`[needAdjustToMaximumDimension](#needAdjustToMaximumDimension())()`
Check if shape should be resized to a maximum size.
`protected boolean`
`[needAdjustToPreferred](#needAdjustToPreferred())()`
Check if shape can be resized to a preferred size.
`protected void`
`[onChildEdgeChange](#onChildEdgeChange(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](ShapeElement.html) child)`

`protected void`
`[prefDimensionByManipulatedChildren](#prefDimensionByManipulatedChildren(java.awt.Dimension,int,int))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)`

`protected void`
`[preferredDimension](#preferredDimension(java.awt.Dimension,int,int))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)`

`protected boolean`
`[prepareForShadowDrawing](#prepareForShadowDrawing(java.awt.Graphics2D))([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g)`
Prepares graphics for symbol shadow drawing.
`boolean`
`[providesHorizontalCenterline](#providesHorizontalCenterline())()`
Indicates if this shape can provide a horizontal centerline for other shapes to snap.
`boolean`
`[providesVerticalCenterline](#providesVerticalCenterline())()`
Indicates if this shape can provide a vertical centerline for other shapes to snap.
`void`
`[recursiveAutosize](#recursiveAutosize())()`
Resize recursively all symbols.
`void`
`[resetCalculatePreferredRegardingChildren](#resetCalculatePreferredRegardingChildren())()`
Resets the CALCULATE_PREFERRED_REGARDING_CHILDREN value to the default.
`void`
`[setAutosize](#setAutosize(boolean))(boolean val)`
Sets autosize flag.
`void`
`[setBorderElementMargin](#setBorderElementMargin(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setBounds](#setBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`
sets bounds of this object view
`void`
`[setCalculatePreferredRegardingChildren](#setCalculatePreferredRegardingChildren(boolean))(boolean flag)`
Sets the CALCULATE_PREFERRED_REGARDING_CHILDREN value.
`void`
`[setLoadedDimension](#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension))([UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) loadedDimension)`

`final void`
`[setMinimumDimension](#setMinimumDimension(int,int))(int width,
 int height)`
Sets min size
`void`
`[setNeedAutosizeFlag](#setNeedAutosizeFlag(byte))(byte needAutosize)`

`final void`
`[setOldRect](#setOldRect(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) old)`

`void`
`[setOnEdge](#setOnEdge(int))(int onEdge)`
Sets on edge property.
`final void`
`[setPreferredDimension](#setPreferredDimension(int,int))(int width,
 int height)`

`void`
`[setReshapeMode](#setReshapeMode(com.nomagic.magicdraw.uml.symbols.ReshapeMode))(com.nomagic.magicdraw.uml.symbols.ReshapeMode mode)`
Set symbol reshape mode
`static void`
`[setSnapShapesOnBorderToGrid](#setSnapShapesOnBorderToGrid(boolean))(boolean snapShapesOnBorderToGrid)`

`void`
`[setSuspendShapeAutoResizeMode](#setSuspendShapeAutoResizeMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`

`void`
`[setUseFixedConnectionPoints](#setUseFixedConnectionPoints(boolean))(boolean useFixed)`

`protected boolean`
`[shouldDrawShadow](#shouldDrawShadow())()`

`final void`
`[simpleSetBounds](#simpleSetBounds(int,int,int,int,boolean))(int x,
 int y,
 int width,
 int height,
 boolean calculatePrefSize)`

`final void`
`[simpleSetBounds](#simpleSetBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)`
Sets bounding rectangle.
`void`
`[simpleSetBounds](#simpleSetBounds(java.awt.Rectangle,boolean))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect,
 boolean calculatePrefSize)`
Sets the bounding rectangle of this shape view to the specified
 value for `bounds`.
`boolean`
`[snapsToCenterlines](#snapsToCenterlines())()`
Indicates if this shape can be snapped to centerlines.
`void`
`[sSetAutosize](#sSetAutosize(boolean))(boolean val)`
Simple setter for autosize flag.
`void`
`[sSetBorderElementMargin](#sSetBorderElementMargin(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[sSetBounds](#sSetBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`
Sets bounds of this object view only.
`void`
`[sSetSuspendShapeAutoResizeMode](#sSetSuspendShapeAutoResizeMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`

`void`
`[sSetVisibility](#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility))(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)`
Sets element visibility flag.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Returns string representation of this element.
`void`
`[updateLater](#updateLater())()`
Registers this symbol to postponed "update" at the end of current command execution.
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[addConnectedPathElement](../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [checkShowsProxy](../paths/PathConnector.html#checkShowsProxy()), [clearShowsProxy](../paths/PathConnector.html#clearShowsProxy()), [createSmartListenerConfig](../paths/PathConnector.html#createSmartListenerConfig(java.util.List)), [dispose](../paths/PathConnector.html#dispose()), [disposeConnectedPaths](../paths/PathConnector.html#disposeConnectedPaths()), [findSymbolForEnd](../paths/PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)), [findSymbolForEnd](../paths/PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)), [getConnectedPathElement](../paths/PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [getConnectedPathElementCount](../paths/PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)), [getPreferredArrowLength](../paths/PathConnector.html#getPreferredArrowLength()), [isShowsProxy](../paths/PathConnector.html#isShowsProxy()), [movePathElement](../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)), [removeConnectedPathElement](../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sAddConnectedPathElement](../paths/PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [selectPathsForMoving](../paths/PathConnector.html#selectPathsForMoving(java.util.List)), [setParent](../paths/PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [setVisibility](../paths/PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [sRemoveConnectedPathElement](../paths/PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sSetConnectedPathElements](../paths/PathConnector.html#sSetConnectedPathElements(java.util.List)), [supportsVisibleConnectedPathElementsIfSelfInvisible](../paths/PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[addPresentationElement](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addPresentationElement](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)), [addPresentationElementWithoutResize](../PresentationElement.html#addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addProperty](../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [adjustChildBounds](../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [adjustChildBoundsForMoving](../PresentationElement.html#adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [alwaysShowTooltip](../PresentationElement.html#alwaysShowTooltip()), [applyProperties](../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [askDeleteDataConfirmation](../PresentationElement.html#askDeleteDataConfirmation()), [atInsert](../PresentationElement.html#atInsert()), [atInsertChildren](../PresentationElement.html#atInsertChildren()), [autosizeAndResizeManipulatedParent](../PresentationElement.html#autosizeAndResizeManipulatedParent()), [beforeDelete](../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)), [boundsChanged](../PresentationElement.html#boundsChanged()), [boundsChanged](../PresentationElement.html#boundsChanged(java.awt.Rectangle)), [canAddChild](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)), [canAddChild](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [canAddInstance](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canAddInstance](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [canBeDisposedOnUpdate](../PresentationElement.html#canBeDisposedOnUpdate()), [canChangeElementOwner](../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canFill](../PresentationElement.html#canFill()), [changeProperties](../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [checkElementOwnerOnChange](../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [checkProxyVisibility](../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [childrenForMoving](../PresentationElement.html#childrenForMoving()), [collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)), [collectSubShowingPresentationElements](../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)), [coversPoint](../PresentationElement.html#coversPoint(int,int)), [createFillStrategy](../PresentationElement.html#createFillStrategy()), [createPresentationElementStyle](../PresentationElement.html#createPresentationElementStyle()), [createPropertyChangeListener](../PresentationElement.html#createPropertyChangeListener()), [disposeChildren](../PresentationElement.html#disposeChildren()), [disposePropertyChangeListener](../PresentationElement.html#disposePropertyChangeListener()), [draw](../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawBackground](../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbol](../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbolBackground](../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [dynamicFillColor](../PresentationElement.html#dynamicFillColor()), [dynamicLineColor](../PresentationElement.html#dynamicLineColor()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth(int)), [dynamicPaintShadow](../PresentationElement.html#dynamicPaintShadow()), [dynamicStroke](../PresentationElement.html#dynamicStroke()), [dynamicStroke](../PresentationElement.html#dynamicStroke(int)), [dynamicStroke](../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)), [dynamicStyleFillColor](../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)), [dynamicStyleLineColor](../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)), [dynamicStyleTextColor](../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency()), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)), [dynamicStyleValue](../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)), [dynamicTextAlignment](../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)), [dynamicTextColor](../PresentationElement.html#dynamicTextColor()), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)), [findOwnerForChildElement](../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [findOwnerForElement](../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)), [findPresentationElement](../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)), [firePropertyChange](../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateID](../PresentationElement.html#generateID()), [getAbstractDiagramPresentationElement](../PresentationElement.html#getAbstractDiagramPresentationElement()), [getActualElement](../PresentationElement.html#getActualElement()), [getAdditionalRenderersToNotifyOnPropertiesChange](../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()), [getAssignableModelElementsClasses](../PresentationElement.html#getAssignableModelElementsClasses()), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getBoundsToRepaint](../PresentationElement.html#getBoundsToRepaint()), [getBoundsWithChildrenOnEdge](../PresentationElement.html#getBoundsWithChildrenOnEdge()), [getCenterlinePoint](../PresentationElement.html#getCenterlinePoint()), [getCenterlinePointX](../PresentationElement.html#getCenterlinePointX()), [getCenterlinePointY](../PresentationElement.html#getCenterlinePointY()), [getChildPresentationElementForContextMenu](../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)), [getChildrenWithSymbolProperties](../PresentationElement.html#getChildrenWithSymbolProperties()), [getConfiguration](../PresentationElement.html#getConfiguration()), [getDiagramPresentationElement](../PresentationElement.html#getDiagramPresentationElement()), [getDiagramSurface](../PresentationElement.html#getDiagramSurface()), [getDrawComparator](../PresentationElement.html#getDrawComparator()), [getDynamicConfigurations](../PresentationElement.html#getDynamicConfigurations()), [getDynamicStyleOwner](../PresentationElement.html#getDynamicStyleOwner()), [getEffectiveStyleDelegate](../PresentationElement.html#getEffectiveStyleDelegate()), [getEffectiveStyleOwner](../PresentationElement.html#getEffectiveStyleOwner()), [getElement](../PresentationElement.html#getElement()), [getElementsForRelationshipConnecting](../PresentationElement.html#getElementsForRelationshipConnecting()), [getElementToConnectRelationship](../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFillColor](../PresentationElement.html#getFillColor()), [getFont](../PresentationElement.html#getFont()), [getFontHeight](../PresentationElement.html#getFontHeight()), [getFontRenderContext](../PresentationElement.html#getFontRenderContext()), [getHumanName](../PresentationElement.html#getHumanName()), [getHumanType](../PresentationElement.html#getHumanType()), [getLineColor](../PresentationElement.html#getLineColor()), [getLineWidth](../PresentationElement.html#getLineWidth()), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point)), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getManipulationBounds](../PresentationElement.html#getManipulationBounds(java.awt.Point)), [getModelElement](../PresentationElement.html#getModelElement()), [getModelElementsForRelationshipConnecting](../PresentationElement.html#getModelElementsForRelationshipConnecting()), [getModelElementToConnectRelationship](../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [getModelElementToMove](../PresentationElement.html#getModelElementToMove()), [getNotZoomedTolerance](../PresentationElement.html#getNotZoomedTolerance()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getOwnStyleDelegate](../PresentationElement.html#getOwnStyleDelegate()), [getParent](../PresentationElement.html#getParent()), [getParentSymbolStyleOwner](../PresentationElement.html#getParentSymbolStyleOwner()), [getPreferredBounds](../PresentationElement.html#getPreferredBounds()), [getPreferredSize](../PresentationElement.html#getPreferredSize()), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(int)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementCount](../PresentationElement.html#getPresentationElementCount()), [getPresentationElementIndex](../PresentationElement.html#getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getPresentationElements](../PresentationElement.html#getPresentationElements()), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getProjectImpl](../PresentationElement.html#getProjectImpl()), [getProperty](../PresentationElement.html#getProperty(java.lang.String)), [getPropertyManager](../PresentationElement.html#getPropertyManager()), [getPropertyManagerName](../PresentationElement.html#getPropertyManagerName()), [getRenderer](../PresentationElement.html#getRenderer()), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [getStyle](../PresentationElement.html#getStyle()), [getSymbolRenderer](../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getTextColor](../PresentationElement.html#getTextColor()), [getTolerance](../PresentationElement.html#getTolerance()), [getVisibility](../PresentationElement.html#getVisibility()), [getVisiblePresentationElements](../PresentationElement.html#getVisiblePresentationElements()), [handleModelDelete](../PresentationElement.html#handleModelDelete()), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [hasSharedModelElement](../PresentationElement.html#hasSharedModelElement()), [initializeAndAutosize](../PresentationElement.html#initializeAndAutosize()), [internalBeforeUpdate](../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)), [internalCreatePropertyChangeListener](../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [internalGetModelElementToConnectRelationship](../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [internalGetPresentationElementStroke](../PresentationElement.html#internalGetPresentationElementStroke(int)), [internalGetSpecificFont](../PresentationElement.html#internalGetSpecificFont()), [internalGetSpecificTextColor](../PresentationElement.html#internalGetSpecificTextColor()), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(float)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)), [internalUpdatePresentationElement](../PresentationElement.html#internalUpdatePresentationElement()), [intersects](../PresentationElement.html#intersects(int,int,int,int)), [invalidate](../PresentationElement.html#invalidate()), [isCanChildrenChangeEdge](../PresentationElement.html#isCanChildrenChangeEdge()), [isChildVisible](../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isContentHidden](../PresentationElement.html#isContentHidden()), [isCreateElementListener](../PresentationElement.html#isCreateElementListener()), [isDetectable](../PresentationElement.html#isDetectable()), [isDisposed](../PresentationElement.html#isDisposed()), [isLayouting](../PresentationElement.html#isLayouting()), [isMovableByMoveManager](../PresentationElement.html#isMovableByMoveManager()), [isNotNull](../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isPreserveProportionsWhenGrowing](../PresentationElement.html#isPreserveProportionsWhenGrowing()), [isSelected](../PresentationElement.html#isSelected()), [isShowElementTypeAsLabel](../PresentationElement.html#isShowElementTypeAsLabel()), [isSortable](../PresentationElement.html#isSortable()), [isSuitableToConnectRelationship](../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [isTextEditable](../PresentationElement.html#isTextEditable()), [isUseFillColor](../PresentationElement.html#isUseFillColor()), [isUseFillColorByProperty](../PresentationElement.html#isUseFillColorByProperty()), [isUseGradientForFill](../PresentationElement.html#isUseGradientForFill()), [isVisible](../PresentationElement.html#isVisible()), [isVisibleInDiagram](../PresentationElement.html#isVisibleInDiagram()), [isVisibleOrShrunken](../PresentationElement.html#isVisibleOrShrunken()), [movePathElementsRecursively](../PresentationElement.html#movePathElementsRecursively()), [mustShowContextMenu](../PresentationElement.html#mustShowContextMenu()), [notifyCreated](../PresentationElement.html#notifyCreated()), [notifyDiagramFrameSizeChange](../PresentationElement.html#notifyDiagramFrameSizeChange()), [notifyRepaintManager](../PresentationElement.html#notifyRepaintManager(boolean)), [onChildAdd](../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onChildRemove](../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onDiagramSurfaceSet](../PresentationElement.html#onDiagramSurfaceSet()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [onFontChange](../PresentationElement.html#onFontChange()), [onParentChange](../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [paintAdornments](../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintAdornmentsBackground](../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildren](../PresentationElement.html#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenAndAdornments](../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenBackground](../PresentationElement.html#paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelf](../PresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelfBackground](../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [preDisposeOnUpdate](../PresentationElement.html#preDisposeOnUpdate()), [prepareForLineDrawing](../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)), [prepareForTextDrawing](../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)), [propertyChange](../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)), [recreateListeners](../PresentationElement.html#recreateListeners()), [registerInSortManager](../PresentationElement.html#registerInSortManager()), [rememberBounds](../PresentationElement.html#rememberBounds()), [rememberBounds](../PresentationElement.html#rememberBounds(java.awt.Rectangle)), [removeFromSortManager](../PresentationElement.html#removeFromSortManager()), [removeItSelfOnUpdate](../PresentationElement.html#removeItSelfOnUpdate()), [removePresentationElement](../PresentationElement.html#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [resizeParent](../PresentationElement.html#resizeParent()), [sAddPresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sAddPresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)), [selectChildrenForMoving](../PresentationElement.html#selectChildrenForMoving()), [selectObjectsForMoving](../PresentationElement.html#selectObjectsForMoving()), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setBounds](../PresentationElement.html#setBounds(int,int,int,int)), [setCreateElementListener](../PresentationElement.html#setCreateElementListener(boolean)), [setDummyResizeMode](../PresentationElement.html#setDummyResizeMode(boolean)), [setElement](../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setFillColor](../PresentationElement.html#setFillColor(java.awt.Color)), [setFont](../PresentationElement.html#setFont(java.awt.Font)), [setLayouting](../PresentationElement.html#setLayouting(boolean)), [setLineColor](../PresentationElement.html#setLineColor(java.awt.Color)), [setLineWidth](../PresentationElement.html#setLineWidth(int)), [setLoadedVisibility](../PresentationElement.html#setLoadedVisibility(boolean)), [setLocation](../PresentationElement.html#setLocation(int,int)), [setLocation](../PresentationElement.html#setLocation(java.awt.Point)), [setModelElement](../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [setNeedRecreateListeners](../PresentationElement.html#setNeedRecreateListeners(boolean)), [setPresentationElements](../PresentationElement.html#setPresentationElements(java.util.List)), [setPropertyManagerName](../PresentationElement.html#setPropertyManagerName(java.lang.String)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [setSize](../PresentationElement.html#setSize(int,int)), [setSize](../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)), [setSize](../PresentationElement.html#setSize(java.awt.Dimension)), [setTextColor](../PresentationElement.html#setTextColor(java.awt.Color)), [setTextEditable](../PresentationElement.html#setTextEditable(boolean)), [setUseFillColor](../PresentationElement.html#setUseFillColor(boolean)), [setVisible](../PresentationElement.html#setVisible(boolean)), [silentApply](../PresentationElement.html#silentApply()), [silentApply](../PresentationElement.html#silentApply(boolean)), [simpleSetBounds](../PresentationElement.html#simpleSetBounds(int,int,int,int)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Point,float)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)), [snapViewToGrid](../PresentationElement.html#snapViewToGrid(float)), [sortObjectsByX](../PresentationElement.html#sortObjectsByX(java.util.List)), [sortObjectsByY](../PresentationElement.html#sortObjectsByY(java.util.List)), [sRemovePresentationElement](../PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetBounds](../PresentationElement.html#sSetBounds(int,int,int,int)), [sSetElement](../PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [sSetLocation](../PresentationElement.html#sSetLocation(int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(java.awt.Point)), [sSetModelElement](../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [sSetParent](../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetParentForAll](../PresentationElement.html#sSetParentForAll(java.util.Collection)), [sSetPresentationElements](../PresentationElement.html#sSetPresentationElements(java.util.List)), [sSetSize](../PresentationElement.html#sSetSize(int,int)), [sSetSize](../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)), [sSetSize](../PresentationElement.html#sSetSize(java.awt.Dimension)), [sSetVisible](../PresentationElement.html#sSetVisible(boolean)), [tryToDeleteModelElementUponRemoval](../PresentationElement.html#tryToDeleteModelElementUponRemoval()), [update](../PresentationElement.html#update()), [updateAfterLoad](../PresentationElement.html#updateAfterLoad()), [updateLabelsIgnoringSuspendableLater](../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)), [updateModelByView](../PresentationElement.html#updateModelByView()), [updateModelByViewInternal](../PresentationElement.html#updateModelByViewInternal()), [updateViewAfterPropertyChange](../PresentationElement.html#updateViewAfterPropertyChange()), [useParentProperties](../PresentationElement.html#useParentProperties()), [useParentStyle](../PresentationElement.html#useParentStyle())`
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
SPACE
public static final int SPACE
Space between bounds and some inner object.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.SPACE)
SPACE_INSETS
public static final com.nomagic.ui.UnmodifiableInsets SPACE_INSETS
Insets with all locations equal to SPACE
See Also:
[`SPACE`](#SPACE)
SPACE_INSETS_EMPTY_TOP_BOTTOM
public static final com.nomagic.ui.UnmodifiableInsets SPACE_INSETS_EMPTY_TOP_BOTTOM
Insets with top/bottom equals to zero and right/left equals to SPACE
See Also:
[`SPACE`](#SPACE)
NULL_INSETS
public static final com.nomagic.ui.UnmodifiableInsets NULL_INSETS
Insets with all locations equal to 0
NEED_AUTOSIZE_FULL
public static final byte NEED_AUTOSIZE_FULL
Flag for doing full autosize - calculation of preferred size and children layout
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.NEED_AUTOSIZE_FULL)
NEED_AUTOSIZE_LAYOUT
public static final byte NEED_AUTOSIZE_LAYOUT
Flag for doing only children layout during autosize
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.NEED_AUTOSIZE_LAYOUT)
NEED_AUTOSIZE_NONE
public static final byte NEED_AUTOSIZE_NONE
Flag for ignoring autosize
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.NEED_AUTOSIZE_NONE)
BORDER_ELEMENT_MARGIN_ALL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BORDER_ELEMENT_MARGIN_ALL
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_ALL)
BORDER_ELEMENT_MARGIN_LEFT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BORDER_ELEMENT_MARGIN_LEFT
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_LEFT)
BORDER_ELEMENT_MARGIN_RIGHT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BORDER_ELEMENT_MARGIN_RIGHT
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_RIGHT)
BORDER_ELEMENT_MARGIN_TOP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BORDER_ELEMENT_MARGIN_TOP
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_TOP)
BORDER_ELEMENT_MARGIN_BOTTOM
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BORDER_ELEMENT_MARGIN_BOTTOM
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_BOTTOM)
BORDER_ELEMENT_MARGIN_LEFT_RIGHT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BORDER_ELEMENT_MARGIN_LEFT_RIGHT
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_LEFT_RIGHT)
BORDER_ELEMENT_MARGIN_TOP_BOTTOM
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BORDER_ELEMENT_MARGIN_TOP_BOTTOM
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_TOP_BOTTOM)
BORDER_ELEMENT_MARGIN_NONE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BORDER_ELEMENT_MARGIN_NONE
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_NONE)
BORDER_ELEMENT_MARGIN_MODES
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> BORDER_ELEMENT_MARGIN_MODES
NO_EDGE
public static final int NO_EDGE
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.NO_EDGE)
TOP_EDGE
public static final int TOP_EDGE
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.TOP_EDGE)
RIGHT_EDGE
public static final int RIGHT_EDGE
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.RIGHT_EDGE)
BOTTOM_EDGE
public static final int BOTTOM_EDGE
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BOTTOM_EDGE)
LEFT_EDGE
public static final int LEFT_EDGE
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.LEFT_EDGE)
ON_EDGE_POSITION
public static final int ON_EDGE_POSITION
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.ON_EDGE_POSITION)
OUTSIDE_EDGE_POSITION
public static final int OUTSIDE_EDGE_POSITION
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OUTSIDE_EDGE_POSITION)
INSIDE_EDGE_POSITION
public static final int INSIDE_EDGE_POSITION
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.INSIDE_EDGE_POSITION)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ShapeElement
public ShapeElement()
ShapeElement
public ShapeElement(@CheckForNull
 [PresentationElement](../PresentationElement.html) parent)
 ============ METHOD DETAIL ========== 
Method Details
setAutosize
public void setAutosize(boolean val)
Sets autosize flag.
Parameters:
`val` - new value of a flag
isAutosized
public boolean isAutosized()
Returns autosize flag.
Returns:
value of autosize flag.
sSetAutosize
public void sSetAutosize(boolean val)
Simple setter for autosize flag.
Parameters:
`val` - value
getSuspendShapeAutoResizeMode
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSuspendShapeAutoResizeMode()
Specified by:
`getSuspendShapeAutoResizeMode` in interface `com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider`
sSetSuspendShapeAutoResizeMode
public void sSetSuspendShapeAutoResizeMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
setSuspendShapeAutoResizeMode
public void setSuspendShapeAutoResizeMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
getBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBounds()
Description copied from class: `[PresentationElement](../PresentationElement.html#getBounds())`
Method returns bounds of this element.
 Use PresentationElementsManager to change a bounds of the element.
Overrides:
`[getBounds](../PresentationElement.html#getBounds())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
bounds of the element.
See Also:
`PresentationElementsManager.reshapeShapeElement`
getNotCopyBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getNotCopyBounds()
Description copied from class: `[PresentationElement](../PresentationElement.html#getNotCopyBounds())`
get not copy bounds of object throws NoRectangleDefinedException
Overrides:
`[getNotCopyBounds](../PresentationElement.html#getNotCopyBounds())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
rectangle of bounds
getMiddlePoint
public final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getMiddlePoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) rel)
Description copied from class: `[PresentationElement](../PresentationElement.html#getMiddlePoint(java.awt.Point))`
Gets middle point of this view,
Overrides:
`[getMiddlePoint](../PresentationElement.html#getMiddlePoint(java.awt.Point))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`rel` - relative point
Returns:
middle point
getMiddlePointX
public int getMiddlePointX([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) rel)
Overrides:
`[getMiddlePointX](../PresentationElement.html#getMiddlePointX(java.awt.Point))` in class `[PresentationElement](../PresentationElement.html)`
getMiddlePointY
public int getMiddlePointY([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) rel)
Overrides:
`[getMiddlePointY](../PresentationElement.html#getMiddlePointY(java.awt.Point))` in class `[PresentationElement](../PresentationElement.html)`
getMiddlePoint
public final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getMiddlePoint()
Description copied from class: `[PresentationElement](../PresentationElement.html#getMiddlePoint())`
Returns middle point of this element. Middle point for shapes usually will be center point of
 bounds, middle point for paths will be center of path curve.
Overrides:
`[getMiddlePoint](../PresentationElement.html#getMiddlePoint())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
point that is considered as middle for this element.
getMiddlePointX
public int getMiddlePointX()
Overrides:
`[getMiddlePointX](../PresentationElement.html#getMiddlePointX())` in class `[PresentationElement](../PresentationElement.html)`
getMiddlePointY
public int getMiddlePointY()
Overrides:
`[getMiddlePointY](../PresentationElement.html#getMiddlePointY())` in class `[PresentationElement](../PresentationElement.html)`
sSetBounds
public void sSetBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
Description copied from class: `[PresentationElement](../PresentationElement.html#sSetBounds(java.awt.Rectangle))`
Sets bounds of this object view only.
Specified by:
`[sSetBounds](../PresentationElement.html#sSetBounds(java.awt.Rectangle))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`bounds` - rectangle of bounds.
adjustBounds
public void adjustBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
Validates bounds
Parameters:
`bounds` - bounds
setBounds
public void setBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
Description copied from class: `[PresentationElement](../PresentationElement.html#setBounds(java.awt.Rectangle))`
sets bounds of this object view
Specified by:
`[setBounds](../PresentationElement.html#setBounds(java.awt.Rectangle))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`bounds` - rectangle of bounds
coversPoint
public boolean coversPoint(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Description copied from class: `[PresentationElement](../PresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))`
checks if object covers provided point
Specified by:
`[coversPoint](../PresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[PresentationElement](../PresentationElement.html)`
Returns:
true if object covers this point
intersects
public boolean intersects(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Description copied from class: `[PresentationElement](../PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))`
checks whether object intersects with given rectangle
Specified by:
`[intersects](../PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[PresentationElement](../PresentationElement.html)`
Returns:
true if object and rectangle intersects
clone
public [ShapeElement](ShapeElement.html) clone()
Specified by:
`[clone](../../BaseElement.html#clone())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`[clone](../paths/PathConnector.html#clone())` in class `[PathConnector](../paths/PathConnector.html)`
movePathElements
public void movePathElements()
Overrides:
`[movePathElements](../paths/PathConnector.html#movePathElements())` in class `[PathConnector](../paths/PathConnector.html)`
clearOldRect
public final void clearOldRect()
setOldRect
public final void setOldRect([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) old)
movePathElement
protected void movePathElement([PathElement](../paths/PathElement.html) path,
 @CheckForNull
 [PathConnector](../paths/PathConnector.html) requestor)
Description copied from class: `[PathConnector](../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector))`
Calculates position of a path element.
Specified by:
`[movePathElement](../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector))` in class `[PathConnector](../paths/PathConnector.html)`
Parameters:
`path` - element which position will be calculated.
`requestor` - the requestor of this path moving. Implementations may check to avoid endless loops.
getIntersection
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getIntersection(int x,
 int y,
 @CheckForNull
 [PathElement](../paths/PathElement.html) path)
Overrides:
`[getIntersection](../PresentationElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement))` in class `[PresentationElement](../PresentationElement.html)`
getIntersection
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getIntersection(int x1,
 int y1,
 int x2,
 int y2,
 @CheckForNull
 [PathElement](../paths/PathElement.html) path)
Gets intersection point between shape view bounding rectangle
 and line.
Parameters:
`x1` - first point of the line
`y1` - first point of the line
`x2` - second point of the line
`y2` - second point of the line
`path` - path
Returns:
intersection point
getIntersection
public static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getIntersection(int x1,
 int y1,
 int x2,
 int y2,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds,
 [ContainerShape](../../../../awt/ContainerShape.html) boundingShape)
Gets intersection point between bounding shape (or rectangle) and line.
Parameters:
`x1` - first point of the line
`y1` - first point of the line
`x2` - second point of the line
`y2` - second point of the line
`bounds` - shape bounds
`boundingShape` - bounding shape
Returns:
intersection point
accept
@OpenApipublic void accept([Visitor](../../Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
 See "Visitor" pattern for more details.
Specified by:
`[accept](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../../MDElement.html)`
Overrides:
`[accept](../paths/PathConnector.html#accept(com.nomagic.magicdraw.uml.Visitor))` in class `[PathConnector](../paths/PathConnector.html)`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
setPreferredDimension
public final void setPreferredDimension(int width,
 int height)
getPreferredDimension
public final [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) getPreferredDimension()
Description copied from class: `[PresentationElement](../PresentationElement.html#getPreferredDimension())`
Returns preferable dimension of the element.
Overrides:
`[getPreferredDimension](../PresentationElement.html#getPreferredDimension())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
preferred dimension
simpleSetBounds
public final void simpleSetBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)
Description copied from class: `[PresentationElement](../PresentationElement.html#simpleSetBounds(java.awt.Rectangle))`
Sets bounding rectangle.
Overrides:
`[simpleSetBounds](../PresentationElement.html#simpleSetBounds(java.awt.Rectangle))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`rect` - new bounding rectangle.
simpleSetBounds
public final void simpleSetBounds(int x,
 int y,
 int width,
 int height,
 boolean calculatePrefSize)
simpleSetBounds
public void simpleSetBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect,
 boolean calculatePrefSize)
Sets the bounding rectangle of this shape view to the specified
 value for `bounds`. Moves all links connected to this
 shape connection points.
Parameters:
`rect` - the new *bounds* for the shape view.
`calculatePrefSize` - need to calculate preferred size
calculateEdge
public void calculateEdge()
edgeChanged
public void edgeChanged()
autosize
public final void autosize()
autosize
public void autosize(boolean calculatePrefSize)
Calculate preferred size and make this shape size at least as preferred (if size is smaller)
Parameters:
`calculatePrefSize` - calculate preferred size
autosizeAndResizeParent
public void autosizeAndResizeParent()
Description copied from class: `[PresentationElement](../PresentationElement.html#autosizeAndResizeParent())`
Resize itself and initiate parent resize
Overrides:
`[autosizeAndResizeParent](../PresentationElement.html#autosizeAndResizeParent())` in class `[PresentationElement](../PresentationElement.html)`
moveLinksToSelf
protected void moveLinksToSelf()
Move links to self.
addBreakPoints
protected void addBreakPoints([PathElement](../paths/PathElement.html) link)
Adds break points to link to self.
Parameters:
`link` - path
calculateAutosizeDimension
protected void calculateAutosizeDimension([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size,
 int locationX,
 int locationY,
 int prefSizeWidth,
 int prefSizeHeight)
Calculates size of shape to be at least as preferred and fit all children
Parameters:
`size` - size
`locationX` - x location
`locationY` - y location
`prefSizeWidth` - preferred size width
`prefSizeHeight` - preferred size height
maximumDimension
protected void maximumDimension([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size)
ensureDimension
public final void ensureDimension(boolean rememberBounds)
If size is smaller than the preferred size, makes shape larger.
Parameters:
`rememberBounds` - flag
needAdjustToPreferred
protected boolean needAdjustToPreferred()
Check if shape can be resized to a preferred size. Usually it is true if shape is manipulated and isAutosize is true.
Returns:
true if adjustments are necessary
needAdjustToMaximumDimension
protected boolean needAdjustToMaximumDimension()
Check if shape should be resized to a maximum size.
Returns:
true if adjustments are necessary
getDefaultDimension
@CheckForNullprotected [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) getDefaultDimension()
getSizeForDrawing
@CheckForNullpublic [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) getSizeForDrawing()
recursiveAutosize
public void recursiveAutosize()
Description copied from class: `[PresentationElement](../PresentationElement.html#recursiveAutosize())`
Resize recursively all symbols. Method must be called if something is changed in symbol (for
 example minimum size) and you want to resize (autosize) all hierarchy
Overrides:
`[recursiveAutosize](../PresentationElement.html#recursiveAutosize())` in class `[PresentationElement](../PresentationElement.html)`
initialize
public void initialize()
Description copied from class: `[PresentationElement](../PresentationElement.html#initialize())`
Initialize symbol and its children state. Symbol must be initialized before doing any
 resize, painting and etc. These operations can lead to unpredictable results otherwise.
Overrides:
`[initialize](../PresentationElement.html#initialize())` in class `[PresentationElement](../PresentationElement.html)`
calculateMinimumDimension
public final void calculateMinimumDimension()
calculates minimum size
minimumDimension
protected void minimumDimension([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) min)
calculates minimum size
Parameters:
`min` - minimum size
setMinimumDimension
public final void setMinimumDimension(int width,
 int height)
Sets min size
Parameters:
`width` - width
`height` - height
getMinimumDimension
public final [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) getMinimumDimension()
Description copied from class: `[PresentationElement](../PresentationElement.html#getMinimumDimension())`
get minimum possible size for object
Overrides:
`[getMinimumDimension](../PresentationElement.html#getMinimumDimension())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
minimum dimension
getManipulatedElementAt
public [PresentationElement](../PresentationElement.html) getManipulatedElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind intersectionKind)
Description copied from class: `[PresentationElement](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))`
Gets manipulated symbol at specified point pt.
Overrides:
`[getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`pt` - `Point`
`intersectionKind` - intersection kind to check for
Returns:
manipulate symbol
calculatePreferredDimension
public final void calculatePreferredDimension()
calculatePreferredDimension
public final void calculatePreferredDimension(int locationX,
 int locationY)
preferredDimension
protected void preferredDimension([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)
prefDimensionByManipulatedChildren
protected void prefDimensionByManipulatedChildren([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) pref,
 int locationX,
 int locationY)
canHavePaths
public boolean canHavePaths()
Overrides:
`[canHavePaths](../PresentationElement.html#canHavePaths())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
true if symbol can have connected paths. Return false here.
createBoundsShape
public [ContainerShape](../../../../awt/ContainerShape.html) createBoundsShape(@CheckForNull
 [PathElement](../paths/PathElement.html) path,
 [BoundsTransformation](../BoundsTransformation.html) transformation)
Creates bounding shape for intersection calculation.
Parameters:
`path` - path
`transformation` - transformation
Returns:
shape
internalGetBoundsShape
@CheckForNullpublic [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) internalGetBoundsShape([ConverterToShape](../ConverterToShape.html) converterToShape)
Overrides:
`[internalGetBoundsShape](../PresentationElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape))` in class `[PresentationElement](../PresentationElement.html)`
internalApplyProperties
public void internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)
Description copied from class: `[PresentationElement](../PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))`
Applies properties from given property manager
Overrides:
`[internalApplyProperties](../PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`changer` - new properties
canBeAutosized
protected boolean canBeAutosized()
isSnapToGrid
protected boolean isSnapToGrid()
Overrides:
`[isSnapToGrid](../PresentationElement.html#isSnapToGrid())` in class `[PresentationElement](../PresentationElement.html)`
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Description copied from class: `com.nomagic.magicdraw.uml.MDElementImpl`
Returns string representation of this element.
 Useful for debugging purposes.
Overrides:
`toString` in class `com.nomagic.magicdraw.uml.MDElementImpl`
getFixedConnectionPoints
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)[] getFixedConnectionPoints()
-----1------
 | |
 | |
 4 2
 | |
 | |
 ----3-------
Returns:
array of 4 points used to connect paths to fixed points.
isUseFixedConnectionPoints
public boolean isUseFixedConnectionPoints()
setUseFixedConnectionPoints
public void setUseFixedConnectionPoints(boolean useFixed)
internalSilentApply
public void internalSilentApply()
Description copied from class: `[PresentationElement](../PresentationElement.html#internalSilentApply())`
Silently applies all properties after initialization
Overrides:
`[internalSilentApply](../PresentationElement.html#internalSilentApply())` in class `[PresentationElement](../PresentationElement.html)`
getChildrenInsets
@CheckForNullpublic com.nomagic.ui.UnmodifiableInsets getChildrenInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)
Parameters:
`insetsLevel` - describes the level of insets
Returns:
shape insets for children
setOnEdge
public void setOnEdge(int onEdge)
Sets on edge property.
Parameters:
`onEdge` - the edge constant
See Also:
[`getOnEdge()`](#getOnEdge())
onChildEdgeChange
protected void onChildEdgeChange([ShapeElement](ShapeElement.html) child)
getOnEdge
public int getOnEdge()
Returns some edge constant if this shape must be on its parent edge.
Returns:
edge constant
See Also:
[`NO_EDGE`](#NO_EDGE)
[`LEFT_EDGE`](#LEFT_EDGE)
[`RIGHT_EDGE`](#RIGHT_EDGE)
[`TOP_EDGE`](#TOP_EDGE)
[`BOTTOM_EDGE`](#BOTTOM_EDGE)
getOnEdgePosition
public int getOnEdgePosition()
Returns position on edge.
Returns:
position on edge.
See Also:
[`ON_EDGE_POSITION`](#ON_EDGE_POSITION)
[`INSIDE_EDGE_POSITION`](#INSIDE_EDGE_POSITION)
[`OUTSIDE_EDGE_POSITION`](#OUTSIDE_EDGE_POSITION)
getOnEdgeCornerDistance
public int getOnEdgeCornerDistance()
Returns:
inset from a corner
adjustOnEdge
public void adjustOnEdge()
Adjust shape on the edge of its parent.
calculateAdjustOnEdgeLocation
@CheckForNullpublic [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) calculateAdjustOnEdgeLocation([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
Calculates on edge location for a shape.
Parameters:
`bounds` - bounds
Returns:
location on edge or null if shape is not on edge
isOnEdge
public boolean isOnEdge()
Returns true if symbol is on edge
Returns:
true if on edge
isShapeOnEdge
public static boolean isShapeOnEdge([PresentationElement](../PresentationElement.html) symbol)
adjustOnEdgeChildren
public void adjustOnEdgeChildren()
Adjust on edge all children
adjustOnEdge
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) adjustOnEdge([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds,
 int edge,
 int position,
 int cornerDistance)
Calculates location of given rectangle according given parent edge and position on edge.
Parameters:
`bounds` - the given rectangle
`edge` - the parent bounds
`position` - the position on edge
`cornerDistance` - distance from a corner
Returns:
adjusted point
adjustBoundsBeforeChange
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) adjustBoundsBeforeChange([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rec,
 boolean autosizeOperation,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)> movedTogether)
Description copied from class: `[PresentationElement](../PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection))`
Validate bounds before bounds change operation
Overrides:
`[adjustBoundsBeforeChange](../PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection))` in class `[PresentationElement](../PresentationElement.html)`
getNearestEdge
public int getNearestEdge([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
Return the nearest edge to given rectangle.
Parameters:
`r` - the given rectangle.
Returns:
nearest edge
See Also:
[`TOP_EDGE`](#TOP_EDGE)
[`BOTTOM_EDGE`](#BOTTOM_EDGE)
[`LEFT_EDGE`](#LEFT_EDGE)
[`RIGHT_EDGE`](#RIGHT_EDGE)
getNearestEdge
public int getNearestEdge(int x,
 int y)
Return the nearest edge to given point.
Parameters:
`x` - the given point x
`y` - the given point y
Returns:
nearest edge
See Also:
[`TOP_EDGE`](#TOP_EDGE)
[`BOTTOM_EDGE`](#BOTTOM_EDGE)
[`LEFT_EDGE`](#LEFT_EDGE)
[`RIGHT_EDGE`](#RIGHT_EDGE)
setLoadedDimension
public void setLoadedDimension(@CheckForNull
 [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) loadedDimension)
getLoadedDimension
@CheckForNullpublic [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) getLoadedDimension()
updateLater
public void updateLater()
Description copied from class: `[PresentationElement](../PresentationElement.html#updateLater())`
Registers this symbol to postponed "update" at the end of current command execution.
 Symbol will be updated when all other commands are executed.
 If this is not possible to register, updates symbol immediately.
Overrides:
`[updateLater](../PresentationElement.html#updateLater())` in class `[PresentationElement](../PresentationElement.html)`
getInsetsForOnEdgeShapes
protected [Insets](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Insets.html) getInsetsForOnEdgeShapes()
calculateOnEdgeBounds
protected com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds calculateOnEdgeBounds()
getHeaderInsetReduce
protected int getHeaderInsetReduce(int edge,
 com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds bounds)
isVerticalCenterlineProvider
public boolean isVerticalCenterlineProvider()
Indicates whether this shape provides vertical center-lines to other shapes.
Returns:
true if this shape provides vertical center lines, false otherwise.
isHorizontalCenterlineProvider
public boolean isHorizontalCenterlineProvider()
Indicates whether this shape provides horizontal center-lines to other shapes.
Returns:
true if this shape provides horizontal center-lines, false otherwise.
prepareForShadowDrawing
protected boolean prepareForShadowDrawing([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g)
Description copied from class: `[PresentationElement](../PresentationElement.html#prepareForShadowDrawing(java.awt.Graphics2D))`
Prepares graphics for symbol shadow drawing. If diagram allows shadows, sets darker diagram background color to given graphics.
Overrides:
`[prepareForShadowDrawing](../PresentationElement.html#prepareForShadowDrawing(java.awt.Graphics2D))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`g` - the given graphics
shouldDrawShadow
protected boolean shouldDrawShadow()
getEdgeLine
@CheckForNullpublic [Line](../../../../awt/Line.html) getEdgeLine(int edge)
Returns a line representing a specified edge.
Parameters:
`edge` - - edge of the shape element.
Returns:
a line that represents an edge.
getCenterlineableInnerParts
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape> getCenterlineableInnerParts(int orientation)
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Gets shape inner parts which have centerlines.
Specified by:
`getCenterlineableInnerParts` in interface `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Parameters:
`orientation` - orientation of inner parts centerlines.
Returns:
a list of inner parts which can have centerlines.
findFreePlaceForShapeOnBorder
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) findFreePlaceForShapeOnBorder([ShapeElement](ShapeElement.html) shape,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) shapeB)
Looks for available position slot for given shape on a border
Parameters:
`shape` - shape added on some border
`shapeB` - bounds of shape. This method can be used while drawing a new shape, so we cannot take bounds from shape
Returns:
new location for shape
providesVerticalCenterline
public boolean providesVerticalCenterline()
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Indicates if this shape can provide a vertical centerline for other shapes to snap.
Specified by:
`providesVerticalCenterline` in interface `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Returns:
true if this shape provides vertical centerline, false otherwise.
providesHorizontalCenterline
public boolean providesHorizontalCenterline()
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Indicates if this shape can provide a horizontal centerline for other shapes to snap.
Specified by:
`providesHorizontalCenterline` in interface `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Returns:
true if this shape provides horizontal centerline, false otherwise.
snapsToCenterlines
public boolean snapsToCenterlines()
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Indicates if this shape can be snapped to centerlines.
Specified by:
`snapsToCenterlines` in interface `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Returns:
true if this shape can be snapped to centerlines, false otherwise.
isCenterlineInner
public boolean isCenterlineInner()
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Indicates if the centerline provided by this shape is provided by its inner parts, not the shape itself.
Specified by:
`isCenterlineInner` in interface `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`
Returns:
true if centerline is inner, false otherwise.
getNeedAutosizeFlag
public byte getNeedAutosizeFlag()
setNeedAutosizeFlag
public void setNeedAutosizeFlag(byte needAutosize)
sSetVisibility
public void sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)
Description copied from class: `[PresentationElement](../PresentationElement.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility))`
Sets element visibility flag.
Overrides:
`[sSetVisibility](../paths/PathConnector.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility))` in class `[PathConnector](../paths/PathConnector.html)`
Parameters:
`visibility` - flag value
layoutChildren
public void layoutChildren()
Layout children of this shape.
 This method is declared final to control a layout flag.
 Subclasses must override internalLayoutChildren.
layoutChildren
public void layoutChildren(boolean calculatePrefSize)
Layout children of this shape.
 This method is declared final to a control layout flag.
 Subclasses must override internalLayoutChildren
Parameters:
`calculatePrefSize` - calculate preferred size
isChildLayoutable
public boolean isChildLayoutable([PresentationElement](../PresentationElement.html) child)
Check if given child is "layoutable" - it means this shape controls the bounds of child inside layoutChildren() method.
 Not "layoutable" children are just moved together with parents, but layoutChildren() do not control their location.
Parameters:
`child` - child
Returns:
true, if given child is layed-out inside autosize method of this shape. False here
setCalculatePreferredRegardingChildren
public void setCalculatePreferredRegardingChildren(boolean flag)
Sets the CALCULATE_PREFERRED_REGARDING_CHILDREN value.
 By default, this value is true.
 If it was changed, it must be reverted, so put the resetting to default in finally block.
 For resetting to default value use: [`resetCalculatePreferredRegardingChildren()`](#resetCalculatePreferredRegardingChildren())
Parameters:
`flag` - the value to set
resetCalculatePreferredRegardingChildren
public void resetCalculatePreferredRegardingChildren()
Resets the CALCULATE_PREFERRED_REGARDING_CHILDREN value to the default.
getBorderElementMargin
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getBorderElementMargin()
sSetBorderElementMargin
public void sSetBorderElementMargin([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
setBorderElementMargin
public void setBorderElementMargin([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
hasManipulator
public boolean hasManipulator()
Description copied from class: `[PresentationElement](../PresentationElement.html#hasManipulator())`
Returns true, if view has manipulator (is selectable)
Overrides:
`[hasManipulator](../PresentationElement.html#hasManipulator())` in class `[PresentationElement](../PresentationElement.html)`
getReshapeMode
public com.nomagic.magicdraw.uml.symbols.ReshapeMode getReshapeMode()
Returns:
current symbol reshape mode
setReshapeMode
public void setReshapeMode(com.nomagic.magicdraw.uml.symbols.ReshapeMode mode)
Set symbol reshape mode
Parameters:
`mode` - reshape mode
getManipulationPreferredDimension
public [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) getManipulationPreferredDimension()
Overrides:
`[getManipulationPreferredDimension](../PresentationElement.html#getManipulationPreferredDimension())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
size for manipulator manipulations
minimumOrMinimumShrinkableDimension
protected void minimumOrMinimumShrinkableDimension([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size)
minimumDimensionForShrinking
public void minimumDimensionForShrinking([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size,
 int locationX,
 int locationY)
Parameters:
`size` - size
`locationX` - location X
`locationY` - location Y
getDimensionForShrinking
public [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) getDimensionForShrinking(int width,
 int height)
isShrinkable
public boolean isShrinkable()
ensurePreferredDimensionIfShrinkable
public void ensurePreferredDimensionIfShrinkable()
ensurePreferredDimensionIfShrinkable
public void ensurePreferredDimensionIfShrinkable([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
calculateAndGetPreferredDimension
public [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) calculateAndGetPreferredDimension()
calculateAndGetMinimumShrinkingDimension
public [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) calculateAndGetMinimumShrinkingDimension(int locationX,
 int locationY)
getPreferredDimensionForAutosize
public [UnmodifiableDimension](../../../../ui/UnmodifiableDimension.html) getPreferredDimensionForAutosize()
Description copied from class: `[PresentationElement](../PresentationElement.html#getPreferredDimensionForAutosize())`
Returns preferable dimension of the element for autosize.This implementation simple returns
 preferred size.
Overrides:
`[getPreferredDimensionForAutosize](../PresentationElement.html#getPreferredDimensionForAutosize())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
preferred dimension
isSnapShapesOnBorderToGrid
public static boolean isSnapShapesOnBorderToGrid()
setSnapShapesOnBorderToGrid
public static void setSnapShapesOnBorderToGrid(boolean snapShapesOnBorderToGrid)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.shapes</a></div>
<h1 class="title" title="Class ShapeElement">Class ShapeElement</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code>, <code>com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider</code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code>com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</code>, <code><a href="NNaryAssociationView.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">NNaryAssociationView</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">ShapeElement</span>
<span class="extends-implements">extends <a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a>
implements com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape, com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider</span></div>
<div class="block">Base class for all kinds of "shape" like symbols.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BORDER_ELEMENT_MARGIN_ALL">BORDER_ELEMENT_MARGIN_ALL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BORDER_ELEMENT_MARGIN_BOTTOM">BORDER_ELEMENT_MARGIN_BOTTOM</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BORDER_ELEMENT_MARGIN_LEFT">BORDER_ELEMENT_MARGIN_LEFT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BORDER_ELEMENT_MARGIN_LEFT_RIGHT">BORDER_ELEMENT_MARGIN_LEFT_RIGHT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BORDER_ELEMENT_MARGIN_MODES">BORDER_ELEMENT_MARGIN_MODES</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BORDER_ELEMENT_MARGIN_NONE">BORDER_ELEMENT_MARGIN_NONE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BORDER_ELEMENT_MARGIN_RIGHT">BORDER_ELEMENT_MARGIN_RIGHT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BORDER_ELEMENT_MARGIN_TOP">BORDER_ELEMENT_MARGIN_TOP</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BORDER_ELEMENT_MARGIN_TOP_BOTTOM">BORDER_ELEMENT_MARGIN_TOP_BOTTOM</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BOTTOM_EDGE">BOTTOM_EDGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INSIDE_EDGE_POSITION">INSIDE_EDGE_POSITION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LEFT_EDGE">LEFT_EDGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final byte</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NEED_AUTOSIZE_FULL">NEED_AUTOSIZE_FULL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Flag for doing full autosize - calculation of preferred size and children layout</div>
</div>
<div class="col-first odd-row-color"><code>static final byte</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NEED_AUTOSIZE_LAYOUT">NEED_AUTOSIZE_LAYOUT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Flag for doing only children layout during autosize</div>
</div>
<div class="col-first even-row-color"><code>static final byte</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NEED_AUTOSIZE_NONE">NEED_AUTOSIZE_NONE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Flag for ignoring autosize</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NO_EDGE">NO_EDGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final com.nomagic.ui.UnmodifiableInsets</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NULL_INSETS">NULL_INSETS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Insets with all locations equal to 0</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ON_EDGE_POSITION">ON_EDGE_POSITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OUTSIDE_EDGE_POSITION">OUTSIDE_EDGE_POSITION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RIGHT_EDGE">RIGHT_EDGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SPACE">SPACE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Space between bounds and some inner object.</div>
</div>
<div class="col-first odd-row-color"><code>static final com.nomagic.ui.UnmodifiableInsets</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SPACE_INSETS">SPACE_INSETS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Insets with all locations equal to SPACE</div>
</div>
<div class="col-first even-row-color"><code>static final com.nomagic.ui.UnmodifiableInsets</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SPACE_INSETS_EMPTY_TOP_BOTTOM">SPACE_INSETS_EMPTY_TOP_BOTTOM</a></code></div>
<div class="col-last even-row-color">
<div class="block">Insets with top/bottom equals to zero and right/left equals to SPACE</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TOP_EDGE">TOP_EDGE</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ShapeElement</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement)">ShapeElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addBreakPoints</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> link)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds break points to link to self.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustBounds(java.awt.Rectangle)">adjustBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Validates bounds</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">adjustBoundsBeforeChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rec,
 boolean autosizeOperation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Validate bounds before bounds change operation</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustOnEdge()">adjustOnEdge</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adjust shape on the edge of its parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustOnEdge(java.awt.Rectangle,int,int,int)">adjustOnEdge</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds,
 int edge,
 int position,
 int cornerDistance)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates location of given rectangle according given parent edge and position on edge.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustOnEdgeChildren()">adjustOnEdgeChildren</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adjust on edge all children</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#autosize()">autosize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#autosize(boolean)">autosize</a><wbr/>(boolean calculatePrefSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculate preferred size and make this shape size at least as preferred (if size is smaller)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#autosizeAndResizeParent()">autosizeAndResizeParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Resize itself and initiate parent resize</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateAdjustOnEdgeLocation(java.awt.Rectangle)">calculateAdjustOnEdgeLocation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates on edge location for a shape.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateAndGetMinimumShrinkingDimension(int,int)">calculateAndGetMinimumShrinkingDimension</a><wbr/>(int locationX,
 int locationY)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateAndGetPreferredDimension()">calculateAndGetPreferredDimension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateAutosizeDimension(java.awt.Dimension,int,int,int,int)">calculateAutosizeDimension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size,
 int locationX,
 int locationY,
 int prefSizeWidth,
 int prefSizeHeight)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates size of shape to be at least as preferred and fit all children</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateEdge()">calculateEdge</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateMinimumDimension()">calculateMinimumDimension</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">calculates minimum size</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateOnEdgeBounds()">calculateOnEdgeBounds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculatePreferredDimension()">calculatePreferredDimension</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculatePreferredDimension(int,int)">calculatePreferredDimension</a><wbr/>(int locationX,
 int locationY)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canBeAutosized()">canBeAutosized</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canHavePaths()">canHavePaths</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearOldRect()">clearOldRect</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">coversPoint</a><wbr/>(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">checks if object covers provided point</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">createBoundsShape</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 <a href="../BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols">BoundsTransformation</a> transformation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates bounding shape for intersection calculation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#edgeChanged()">edgeChanged</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureDimension(boolean)">ensureDimension</a><wbr/>(boolean rememberBounds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If size is smaller than the preferred size, makes shape larger.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ensurePreferredDimensionIfShrinkable()">ensurePreferredDimensionIfShrinkable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)">ensurePreferredDimensionIfShrinkable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)">findFreePlaceForShapeOnBorder</a><wbr/>(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> shapeB)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Looks for available position slot for given shape on a border</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBorderElementMargin()">getBorderElementMargin</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBounds()">getBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method returns bounds of this element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCenterlineableInnerParts(int)">getCenterlineableInnerParts</a><wbr/>(int orientation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets shape inner parts which have centerlines.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ui.UnmodifiableInsets</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildrenInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel)">getChildrenInsets</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultDimension()">getDefaultDimension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDimensionForShrinking(int,int)">getDimensionForShrinking</a><wbr/>(int width,
 int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../awt/Line.html" title="class in com.nomagic.awt">Line</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEdgeLine(int)">getEdgeLine</a><wbr/>(int edge)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a line representing a specified edge.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFixedConnectionPoints()">getFixedConnectionPoints</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">-----1------
 |             |
 |             |
 4             2
 |             |
 |             |
 ----3-------</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)">getHeaderInsetReduce</a><wbr/>(int edge,
 com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds bounds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Insets.html" title="class or interface in java.awt">Insets</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInsetsForOnEdgeShapes()">getInsetsForOnEdgeShapes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a><wbr/>(int x1,
 int y1,
 int x2,
 int y2,
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets intersection point between shape view bounding rectangle
 and line.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)">getIntersection</a><wbr/>(int x1,
 int y1,
 int x2,
 int y2,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds,
 <a href="../../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a> boundingShape)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets intersection point between bounding shape (or rectangle) and line.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a><wbr/>(int x,
 int y,
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoadedDimension()">getLoadedDimension</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind intersectionKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets manipulated symbol at specified point pt.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulationPreferredDimension()">getManipulationPreferredDimension</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePoint()">getMiddlePoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns middle point of this element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePoint(java.awt.Point)">getMiddlePoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> rel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets middle point of this view,</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePointX()">getMiddlePointX</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePointX(java.awt.Point)">getMiddlePointX</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> rel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePointY()">getMiddlePointY</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePointY(java.awt.Point)">getMiddlePointY</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> rel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimumDimension()">getMinimumDimension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">get minimum possible size for object</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNearestEdge(int,int)">getNearestEdge</a><wbr/>(int x,
 int y)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the nearest edge to given point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNearestEdge(java.awt.Rectangle)">getNearestEdge</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the nearest edge to given rectangle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>byte</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNeedAutosizeFlag()">getNeedAutosizeFlag</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotCopyBounds()">getNotCopyBounds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">get not copy bounds of object throws NoRectangleDefinedException</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOnEdge()">getOnEdge</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns some edge constant if this shape must be on its parent edge.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOnEdgeCornerDistance()">getOnEdgeCornerDistance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOnEdgePosition()">getOnEdgePosition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns position on edge.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreferredDimension()">getPreferredDimension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns preferable dimension of the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreferredDimensionForAutosize()">getPreferredDimensionForAutosize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns preferable dimension of the element for autosize.This implementation simple returns
 preferred size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.ReshapeMode</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReshapeMode()">getReshapeMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSizeForDrawing()">getSizeForDrawing</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSuspendShapeAutoResizeMode()">getSuspendShapeAutoResizeMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasManipulator()">hasManipulator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if view has manipulator (is selectable)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initialize()">initialize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize symbol and its children state.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies properties from given property manager</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a><wbr/>(<a href="../ConverterToShape.html" title="class in com.nomagic.magicdraw.uml.symbols">ConverterToShape</a> converterToShape)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutosized()">isAutosized</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns autosize flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCenterlineInner()">isCenterlineInner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if the centerline provided by this shape is provided by its inner parts, not the shape itself.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isChildLayoutable(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildLayoutable</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if given child is "layoutable" - it means this shape controls the bounds of child inside layoutChildren() method.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHorizontalCenterlineProvider()">isHorizontalCenterlineProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates whether this shape provides horizontal center-lines to other shapes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOnEdge()">isOnEdge</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if symbol is on edge</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isShapeOnEdge</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShrinkable()">isShrinkable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSnapShapesOnBorderToGrid()">isSnapShapesOnBorderToGrid</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSnapToGrid()">isSnapToGrid</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseFixedConnectionPoints()">isUseFixedConnectionPoints</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isVerticalCenterlineProvider()">isVerticalCenterlineProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates whether this shape provides vertical center-lines to other shapes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#layoutChildren()">layoutChildren</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Layout children of this shape.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#layoutChildren(boolean)">layoutChildren</a><wbr/>(boolean calculatePrefSize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Layout children of this shape.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#maximumDimension(java.awt.Dimension)">maximumDimension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#minimumDimension(java.awt.Dimension)">minimumDimension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> min)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">calculates minimum size</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#minimumDimensionForShrinking(java.awt.Dimension,int,int)">minimumDimensionForShrinking</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size,
 int locationX,
 int locationY)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#minimumOrMinimumShrinkableDimension(java.awt.Dimension)">minimumOrMinimumShrinkableDimension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#moveLinksToSelf()">moveLinksToSelf</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Move links to self.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 <a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> requestor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates position of a path element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePathElements()">movePathElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#needAdjustToMaximumDimension()">needAdjustToMaximumDimension</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if shape should be resized to a maximum size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#needAdjustToPreferred()">needAdjustToPreferred</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if shape can be resized to a preferred size.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#onChildEdgeChange(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">onChildEdgeChange</a><wbr/>(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prefDimensionByManipulatedChildren(java.awt.Dimension,int,int)">prefDimensionByManipulatedChildren</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#preferredDimension(java.awt.Dimension,int,int)">preferredDimension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Prepares graphics for symbol shadow drawing.</div>
</div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#recursiveAutosize()">recursiveAutosize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Resize recursively all symbols.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resetCalculatePreferredRegardingChildren()">resetCalculatePreferredRegardingChildren</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Resets the CALCULATE_PREFERRED_REGARDING_CHILDREN value to the default.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutosize(boolean)">setAutosize</a><wbr/>(boolean val)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets autosize flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBorderElementMargin(java.lang.String)">setBorderElementMargin</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBounds(java.awt.Rectangle)">setBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sets bounds of this object view</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCalculatePreferredRegardingChildren(boolean)">setCalculatePreferredRegardingChildren</a><wbr/>(boolean flag)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the CALCULATE_PREFERRED_REGARDING_CHILDREN value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)">setLoadedDimension</a><wbr/>(<a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a> loadedDimension)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMinimumDimension(int,int)">setMinimumDimension</a><wbr/>(int width,
 int height)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets min size</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNeedAutosizeFlag(byte)">setNeedAutosizeFlag</a><wbr/>(byte needAutosize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOldRect(java.awt.Rectangle)">setOldRect</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> old)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOnEdge(int)">setOnEdge</a><wbr/>(int onEdge)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets on edge property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPreferredDimension(int,int)">setPreferredDimension</a><wbr/>(int width,
 int height)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setReshapeMode(com.nomagic.magicdraw.uml.symbols.ReshapeMode)">setReshapeMode</a><wbr/>(com.nomagic.magicdraw.uml.symbols.ReshapeMode mode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set symbol reshape mode</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSnapShapesOnBorderToGrid(boolean)">setSnapShapesOnBorderToGrid</a><wbr/>(boolean snapShapesOnBorderToGrid)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSuspendShapeAutoResizeMode(java.lang.String)">setSuspendShapeAutoResizeMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseFixedConnectionPoints(boolean)">setUseFixedConnectionPoints</a><wbr/>(boolean useFixed)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#shouldDrawShadow()">shouldDrawShadow</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simpleSetBounds(int,int,int,int,boolean)">simpleSetBounds</a><wbr/>(int x,
 int y,
 int width,
 int height,
 boolean calculatePrefSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets bounding rectangle.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simpleSetBounds(java.awt.Rectangle,boolean)">simpleSetBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect,
 boolean calculatePrefSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the bounding rectangle of this shape view to the specified
 value for <code>bounds</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#snapsToCenterlines()">snapsToCenterlines</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if this shape can be snapped to centerlines.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetAutosize(boolean)">sSetAutosize</a><wbr/>(boolean val)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Simple setter for autosize flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetBorderElementMargin(java.lang.String)">sSetBorderElementMargin</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetBounds(java.awt.Rectangle)">sSetBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets bounds of this object view only.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetSuspendShapeAutoResizeMode(java.lang.String)">sSetSuspendShapeAutoResizeMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a><wbr/>(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets element visibility flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns string representation of this element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateLater()">updateLater</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers this symbol to postponed "update" at the end of current command execution.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="../paths/PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addConnectedPathElement</a>, <a href="../paths/PathConnector.html#checkShowsProxy()">checkShowsProxy</a>, <a href="../paths/PathConnector.html#clearShowsProxy()">clearShowsProxy</a>, <a href="../paths/PathConnector.html#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a>, <a href="../paths/PathConnector.html#dispose()">dispose</a>, <a href="../paths/PathConnector.html#disposeConnectedPaths()">disposeConnectedPaths</a>, <a href="../paths/PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">findSymbolForEnd</a>, <a href="../paths/PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)">findSymbolForEnd</a>, <a href="../paths/PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">getConnectedPathElement</a>, <a href="../paths/PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="../paths/PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getPreferredArrowLength()">getPreferredArrowLength</a>, <a href="../paths/PathConnector.html#isShowsProxy()">isShowsProxy</a>, <a href="../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)">movePathElement</a>, <a href="../paths/PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">removeConnectedPathElement</a>, <a href="../paths/PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sAddConnectedPathElement</a>, <a href="../paths/PathConnector.html#selectPathsForMoving(java.util.List)">selectPathsForMoving</a>, <a href="../paths/PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a>, <a href="../paths/PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a>, <a href="../paths/PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sRemoveConnectedPathElement</a>, <a href="../paths/PathConnector.html#sSetConnectedPathElements(java.util.List)">sSetConnectedPathElements</a>, <a href="../paths/PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible()">supportsVisibleConnectedPathElementsIfSelfInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a>, <a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">addPresentationElement</a>, <a href="../PresentationElement.html#addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElementWithoutResize</a>, <a href="../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBounds</a>, <a href="../PresentationElement.html#adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBoundsForMoving</a>, <a href="../PresentationElement.html#alwaysShowTooltip()">alwaysShowTooltip</a>, <a href="../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">applyProperties</a>, <a href="../PresentationElement.html#askDeleteDataConfirmation()">askDeleteDataConfirmation</a>, <a href="../PresentationElement.html#atInsert()">atInsert</a>, <a href="../PresentationElement.html#atInsertChildren()">atInsertChildren</a>, <a href="../PresentationElement.html#autosizeAndResizeManipulatedParent()">autosizeAndResizeManipulatedParent</a>, <a href="../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">beforeDelete</a>, <a href="../PresentationElement.html#boundsChanged()">boundsChanged</a>, <a href="../PresentationElement.html#boundsChanged(java.awt.Rectangle)">boundsChanged</a>, <a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddChild</a>, <a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddInstance</a>, <a href="../PresentationElement.html#canBeDisposedOnUpdate()">canBeDisposedOnUpdate</a>, <a href="../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeElementOwner</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">canChangeParent</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../PresentationElement.html#canFill()">canFill</a>, <a href="../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">changeProperties</a>, <a href="../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a>, <a href="../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">checkProxyVisibility</a>, <a href="../PresentationElement.html#childrenForMoving()">childrenForMoving</a>, <a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)">collectSubShowingPresentationElements</a>, <a href="../PresentationElement.html#coversPoint(int,int)">coversPoint</a>, <a href="../PresentationElement.html#createFillStrategy()">createFillStrategy</a>, <a href="../PresentationElement.html#createPresentationElementStyle()">createPresentationElementStyle</a>, <a href="../PresentationElement.html#createPropertyChangeListener()">createPropertyChangeListener</a>, <a href="../PresentationElement.html#disposeChildren()">disposeChildren</a>, <a href="../PresentationElement.html#disposePropertyChangeListener()">disposePropertyChangeListener</a>, <a href="../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a>, <a href="../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawBackground</a>, <a href="../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbol</a>, <a href="../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbolBackground</a>, <a href="../PresentationElement.html#dynamicFillColor()">dynamicFillColor</a>, <a href="../PresentationElement.html#dynamicLineColor()">dynamicLineColor</a>, <a href="../PresentationElement.html#dynamicLineWidth()">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicLineWidth(int)">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicPaintShadow()">dynamicPaintShadow</a>, <a href="../PresentationElement.html#dynamicStroke()">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(int)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)">dynamicStyleFillColor</a>, <a href="../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)">dynamicStyleLineColor</a>, <a href="../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)">dynamicStyleTextColor</a>, <a href="../PresentationElement.html#dynamicStyleTransparency()">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)">dynamicStyleValue</a>, <a href="../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">dynamicTextAlignment</a>, <a href="../PresentationElement.html#dynamicTextColor()">dynamicTextColor</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a>, <a href="../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOwnerForChildElement</a>, <a href="../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a>, <a href="../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">findPresentationElement</a>, <a href="../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../PresentationElement.html#generateID()">generateID</a>, <a href="../PresentationElement.html#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>, <a href="../PresentationElement.html#getActualElement()">getActualElement</a>, <a href="../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()">getAdditionalRenderersToNotifyOnPropertiesChange</a>, <a href="../PresentationElement.html#getAssignableModelElementsClasses()">getAssignableModelElementsClasses</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getBoundsToRepaint()">getBoundsToRepaint</a>, <a href="../PresentationElement.html#getBoundsWithChildrenOnEdge()">getBoundsWithChildrenOnEdge</a>, <a href="../PresentationElement.html#getCenterlinePoint()">getCenterlinePoint</a>, <a href="../PresentationElement.html#getCenterlinePointX()">getCenterlinePointX</a>, <a href="../PresentationElement.html#getCenterlinePointY()">getCenterlinePointY</a>, <a href="../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)">getChildPresentationElementForContextMenu</a>, <a href="../PresentationElement.html#getChildrenWithSymbolProperties()">getChildrenWithSymbolProperties</a>, <a href="../PresentationElement.html#getConfiguration()">getConfiguration</a>, <a href="../PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="../PresentationElement.html#getDiagramSurface()">getDiagramSurface</a>, <a href="../PresentationElement.html#getDrawComparator()">getDrawComparator</a>, <a href="../PresentationElement.html#getDynamicConfigurations()">getDynamicConfigurations</a>, <a href="../PresentationElement.html#getDynamicStyleOwner()">getDynamicStyleOwner</a>, <a href="../PresentationElement.html#getEffectiveStyleDelegate()">getEffectiveStyleDelegate</a>, <a href="../PresentationElement.html#getEffectiveStyleOwner()">getEffectiveStyleOwner</a>, <a href="../PresentationElement.html#getElement()">getElement</a>, <a href="../PresentationElement.html#getElementsForRelationshipConnecting()">getElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementToConnectRelationship</a>, <a href="../PresentationElement.html#getFillColor()">getFillColor</a>, <a href="../PresentationElement.html#getFont()">getFont</a>, <a href="../PresentationElement.html#getFontHeight()">getFontHeight</a>, <a href="../PresentationElement.html#getFontRenderContext()">getFontRenderContext</a>, <a href="../PresentationElement.html#getHumanName()">getHumanName</a>, <a href="../PresentationElement.html#getHumanType()">getHumanType</a>, <a href="../PresentationElement.html#getLineColor()">getLineColor</a>, <a href="../PresentationElement.html#getLineWidth()">getLineWidth</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getManipulationBounds(java.awt.Point)">getManipulationBounds</a>, <a href="../PresentationElement.html#getModelElement()">getModelElement</a>, <a href="../PresentationElement.html#getModelElementsForRelationshipConnecting()">getModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">getModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#getModelElementToMove()">getModelElementToMove</a>, <a href="../PresentationElement.html#getNotZoomedTolerance()">getNotZoomedTolerance</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getOwnStyleDelegate()">getOwnStyleDelegate</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a>, <a href="../PresentationElement.html#getPreferredBounds()">getPreferredBounds</a>, <a href="../PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="../PresentationElement.html#getPresentationElementAt(int)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementCount()">getPresentationElementCount</a>, <a href="../PresentationElement.html#getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getPresentationElementIndex</a>, <a href="../PresentationElement.html#getPresentationElements()">getPresentationElements</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getProjectImpl()">getProjectImpl</a>, <a href="../PresentationElement.html#getProperty(java.lang.String)">getProperty</a>, <a href="../PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="../PresentationElement.html#getPropertyManagerName()">getPropertyManagerName</a>, <a href="../PresentationElement.html#getRenderer()">getRenderer</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#getStyle()">getStyle</a>, <a href="../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSymbolRenderer</a>, <a href="../PresentationElement.html#getTextColor()">getTextColor</a>, <a href="../PresentationElement.html#getTolerance()">getTolerance</a>, <a href="../PresentationElement.html#getVisibility()">getVisibility</a>, <a href="../PresentationElement.html#getVisiblePresentationElements()">getVisiblePresentationElements</a>, <a href="../PresentationElement.html#handleModelDelete()">handleModelDelete</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#hasSharedModelElement()">hasSharedModelElement</a>, <a href="../PresentationElement.html#initializeAndAutosize()">initializeAndAutosize</a>, <a href="../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)">internalBeforeUpdate</a>, <a href="../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">internalCreatePropertyChangeListener</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a>, <a href="../PresentationElement.html#internalGetSpecificFont()">internalGetSpecificFont</a>, <a href="../PresentationElement.html#internalGetSpecificTextColor()">internalGetSpecificTextColor</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalSnapToGrid(float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#internalUpdatePresentationElement()">internalUpdatePresentationElement</a>, <a href="../PresentationElement.html#intersects(int,int,int,int)">intersects</a>, <a href="../PresentationElement.html#invalidate()">invalidate</a>, <a href="../PresentationElement.html#isCanChildrenChangeEdge()">isCanChildrenChangeEdge</a>, <a href="../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildVisible</a>, <a href="../PresentationElement.html#isContentHidden()">isContentHidden</a>, <a href="../PresentationElement.html#isCreateElementListener()">isCreateElementListener</a>, <a href="../PresentationElement.html#isDetectable()">isDetectable</a>, <a href="../PresentationElement.html#isDisposed()">isDisposed</a>, <a href="../PresentationElement.html#isLayouting()">isLayouting</a>, <a href="../PresentationElement.html#isMovableByMoveManager()">isMovableByMoveManager</a>, <a href="../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNotNull</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isParentOf</a>, <a href="../PresentationElement.html#isPreserveProportionsWhenGrowing()">isPreserveProportionsWhenGrowing</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#isShowElementTypeAsLabel()">isShowElementTypeAsLabel</a>, <a href="../PresentationElement.html#isSortable()">isSortable</a>, <a href="../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">isSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#isTextEditable()">isTextEditable</a>, <a href="../PresentationElement.html#isUseFillColor()">isUseFillColor</a>, <a href="../PresentationElement.html#isUseFillColorByProperty()">isUseFillColorByProperty</a>, <a href="../PresentationElement.html#isUseGradientForFill()">isUseGradientForFill</a>, <a href="../PresentationElement.html#isVisible()">isVisible</a>, <a href="../PresentationElement.html#isVisibleInDiagram()">isVisibleInDiagram</a>, <a href="../PresentationElement.html#isVisibleOrShrunken()">isVisibleOrShrunken</a>, <a href="../PresentationElement.html#movePathElementsRecursively()">movePathElementsRecursively</a>, <a href="../PresentationElement.html#mustShowContextMenu()">mustShowContextMenu</a>, <a href="../PresentationElement.html#notifyCreated()">notifyCreated</a>, <a href="../PresentationElement.html#notifyDiagramFrameSizeChange()">notifyDiagramFrameSizeChange</a>, <a href="../PresentationElement.html#notifyRepaintManager(boolean)">notifyRepaintManager</a>, <a href="../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildAdd</a>, <a href="../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildRemove</a>, <a href="../PresentationElement.html#onDiagramSurfaceSet()">onDiagramSurfaceSet</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#onFontChange()">onFontChange</a>, <a href="../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">onParentChange</a>, <a href="../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornments</a>, <a href="../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornmentsBackground</a>, <a href="../PresentationElement.html#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildren</a>, <a href="../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenAndAdornments</a>, <a href="../PresentationElement.html#paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenBackground</a>, <a href="../PresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelf</a>, <a href="../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelfBackground</a>, <a href="../PresentationElement.html#preDisposeOnUpdate()">preDisposeOnUpdate</a>, <a href="../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)">prepareForLineDrawing</a>, <a href="../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)">prepareForTextDrawing</a>, <a href="../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a>, <a href="../PresentationElement.html#recreateListeners()">recreateListeners</a>, <a href="../PresentationElement.html#registerInSortManager()">registerInSortManager</a>, <a href="../PresentationElement.html#rememberBounds()">rememberBounds</a>, <a href="../PresentationElement.html#rememberBounds(java.awt.Rectangle)">rememberBounds</a>, <a href="../PresentationElement.html#removeFromSortManager()">removeFromSortManager</a>, <a href="../PresentationElement.html#removeItSelfOnUpdate()">removeItSelfOnUpdate</a>, <a href="../PresentationElement.html#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">removePresentationElement</a>, <a href="../PresentationElement.html#resizeParent()">resizeParent</a>, <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sAddPresentationElement</a>, <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">sAddPresentationElement</a>, <a href="../PresentationElement.html#selectChildrenForMoving()">selectChildrenForMoving</a>, <a href="../PresentationElement.html#selectObjectsForMoving()">selectObjectsForMoving</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setBounds(int,int,int,int)">setBounds</a>, <a href="../PresentationElement.html#setCreateElementListener(boolean)">setCreateElementListener</a>, <a href="../PresentationElement.html#setDummyResizeMode(boolean)">setDummyResizeMode</a>, <a href="../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a>, <a href="../PresentationElement.html#setFillColor(java.awt.Color)">setFillColor</a>, <a href="../PresentationElement.html#setFont(java.awt.Font)">setFont</a>, <a href="../PresentationElement.html#setLayouting(boolean)">setLayouting</a>, <a href="../PresentationElement.html#setLineColor(java.awt.Color)">setLineColor</a>, <a href="../PresentationElement.html#setLineWidth(int)">setLineWidth</a>, <a href="../PresentationElement.html#setLoadedVisibility(boolean)">setLoadedVisibility</a>, <a href="../PresentationElement.html#setLocation(int,int)">setLocation</a>, <a href="../PresentationElement.html#setLocation(java.awt.Point)">setLocation</a>, <a href="../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">setModelElement</a>, <a href="../PresentationElement.html#setNeedRecreateListeners(boolean)">setNeedRecreateListeners</a>, <a href="../PresentationElement.html#setPresentationElements(java.util.List)">setPresentationElements</a>, <a href="../PresentationElement.html#setPropertyManagerName(java.lang.String)">setPropertyManagerName</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#setSize(int,int)">setSize</a>, <a href="../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)">setSize</a>, <a href="../PresentationElement.html#setSize(java.awt.Dimension)">setSize</a>, <a href="../PresentationElement.html#setTextColor(java.awt.Color)">setTextColor</a>, <a href="../PresentationElement.html#setTextEditable(boolean)">setTextEditable</a>, <a href="../PresentationElement.html#setUseFillColor(boolean)">setUseFillColor</a>, <a href="../PresentationElement.html#setVisible(boolean)">setVisible</a>, <a href="../PresentationElement.html#silentApply()">silentApply</a>, <a href="../PresentationElement.html#silentApply(boolean)">silentApply</a>, <a href="../PresentationElement.html#simpleSetBounds(int,int,int,int)">simpleSetBounds</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Point,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapViewToGrid(float)">snapViewToGrid</a>, <a href="../PresentationElement.html#sortObjectsByX(java.util.List)">sortObjectsByX</a>, <a href="../PresentationElement.html#sortObjectsByY(java.util.List)">sortObjectsByY</a>, <a href="../PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sRemovePresentationElement</a>, <a href="../PresentationElement.html#sSetBounds(int,int,int,int)">sSetBounds</a>, <a href="../PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">sSetElement</a>, <a href="../PresentationElement.html#sSetLocation(int,int)">sSetLocation</a>, <a href="../PresentationElement.html#sSetLocation(java.awt.Point)">sSetLocation</a>, <a href="../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">sSetModelElement</a>, <a href="../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a>, <a href="../PresentationElement.html#sSetParentForAll(java.util.Collection)">sSetParentForAll</a>, <a href="../PresentationElement.html#sSetPresentationElements(java.util.List)">sSetPresentationElements</a>, <a href="../PresentationElement.html#sSetSize(int,int)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(java.awt.Dimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetVisible(boolean)">sSetVisible</a>, <a href="../PresentationElement.html#tryToDeleteModelElementUponRemoval()">tryToDeleteModelElementUponRemoval</a>, <a href="../PresentationElement.html#update()">update</a>, <a href="../PresentationElement.html#updateAfterLoad()">updateAfterLoad</a>, <a href="../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)">updateLabelsIgnoringSuspendableLater</a>, <a href="../PresentationElement.html#updateModelByView()">updateModelByView</a>, <a href="../PresentationElement.html#updateModelByViewInternal()">updateModelByViewInternal</a>, <a href="../PresentationElement.html#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a>, <a href="../PresentationElement.html#useParentProperties()">useParentProperties</a>, <a href="../PresentationElement.html#useParentStyle()">useParentStyle</a></code></div>
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
<section class="detail" id="SPACE">
<h3>SPACE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SPACE</span></div>
<div class="block">Space between bounds and some inner object.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.SPACE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SPACE_INSETS">
<h3>SPACE_INSETS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">com.nomagic.ui.UnmodifiableInsets</span> <span class="element-name">SPACE_INSETS</span></div>
<div class="block">Insets with all locations equal to SPACE</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SPACE"><code>SPACE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SPACE_INSETS_EMPTY_TOP_BOTTOM">
<h3>SPACE_INSETS_EMPTY_TOP_BOTTOM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">com.nomagic.ui.UnmodifiableInsets</span> <span class="element-name">SPACE_INSETS_EMPTY_TOP_BOTTOM</span></div>
<div class="block">Insets with top/bottom equals to zero and right/left equals to SPACE</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SPACE"><code>SPACE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NULL_INSETS">
<h3>NULL_INSETS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">com.nomagic.ui.UnmodifiableInsets</span> <span class="element-name">NULL_INSETS</span></div>
<div class="block">Insets with all locations equal to 0</div>
</section>
</li>
<li>
<section class="detail" id="NEED_AUTOSIZE_FULL">
<h3>NEED_AUTOSIZE_FULL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">byte</span> <span class="element-name">NEED_AUTOSIZE_FULL</span></div>
<div class="block">Flag for doing full autosize - calculation of preferred size and children layout</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.NEED_AUTOSIZE_FULL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NEED_AUTOSIZE_LAYOUT">
<h3>NEED_AUTOSIZE_LAYOUT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">byte</span> <span class="element-name">NEED_AUTOSIZE_LAYOUT</span></div>
<div class="block">Flag for doing only children layout during autosize</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.NEED_AUTOSIZE_LAYOUT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NEED_AUTOSIZE_NONE">
<h3>NEED_AUTOSIZE_NONE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">byte</span> <span class="element-name">NEED_AUTOSIZE_NONE</span></div>
<div class="block">Flag for ignoring autosize</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.NEED_AUTOSIZE_NONE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BORDER_ELEMENT_MARGIN_ALL">
<h3>BORDER_ELEMENT_MARGIN_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BORDER_ELEMENT_MARGIN_ALL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BORDER_ELEMENT_MARGIN_LEFT">
<h3>BORDER_ELEMENT_MARGIN_LEFT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BORDER_ELEMENT_MARGIN_LEFT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_LEFT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BORDER_ELEMENT_MARGIN_RIGHT">
<h3>BORDER_ELEMENT_MARGIN_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BORDER_ELEMENT_MARGIN_RIGHT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_RIGHT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BORDER_ELEMENT_MARGIN_TOP">
<h3>BORDER_ELEMENT_MARGIN_TOP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BORDER_ELEMENT_MARGIN_TOP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_TOP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BORDER_ELEMENT_MARGIN_BOTTOM">
<h3>BORDER_ELEMENT_MARGIN_BOTTOM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BORDER_ELEMENT_MARGIN_BOTTOM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_BOTTOM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BORDER_ELEMENT_MARGIN_LEFT_RIGHT">
<h3>BORDER_ELEMENT_MARGIN_LEFT_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BORDER_ELEMENT_MARGIN_LEFT_RIGHT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_LEFT_RIGHT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BORDER_ELEMENT_MARGIN_TOP_BOTTOM">
<h3>BORDER_ELEMENT_MARGIN_TOP_BOTTOM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BORDER_ELEMENT_MARGIN_TOP_BOTTOM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_TOP_BOTTOM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BORDER_ELEMENT_MARGIN_NONE">
<h3>BORDER_ELEMENT_MARGIN_NONE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BORDER_ELEMENT_MARGIN_NONE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BORDER_ELEMENT_MARGIN_NONE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BORDER_ELEMENT_MARGIN_MODES">
<h3>BORDER_ELEMENT_MARGIN_MODES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">BORDER_ELEMENT_MARGIN_MODES</span></div>
</section>
</li>
<li>
<section class="detail" id="NO_EDGE">
<h3>NO_EDGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">NO_EDGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.NO_EDGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TOP_EDGE">
<h3>TOP_EDGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TOP_EDGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.TOP_EDGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RIGHT_EDGE">
<h3>RIGHT_EDGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">RIGHT_EDGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.RIGHT_EDGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BOTTOM_EDGE">
<h3>BOTTOM_EDGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">BOTTOM_EDGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.BOTTOM_EDGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LEFT_EDGE">
<h3>LEFT_EDGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">LEFT_EDGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.LEFT_EDGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ON_EDGE_POSITION">
<h3>ON_EDGE_POSITION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ON_EDGE_POSITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.ON_EDGE_POSITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OUTSIDE_EDGE_POSITION">
<h3>OUTSIDE_EDGE_POSITION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">OUTSIDE_EDGE_POSITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OUTSIDE_EDGE_POSITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INSIDE_EDGE_POSITION">
<h3>INSIDE_EDGE_POSITION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">INSIDE_EDGE_POSITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.INSIDE_EDGE_POSITION">Constant Field Values</a></li>
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
<h3>ShapeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ShapeElement</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>ShapeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ShapeElement</span><wbr/><span class="parameters">(@CheckForNull
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
<section class="detail" id="setAutosize(boolean)">
<h3>setAutosize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutosize</span><wbr/><span class="parameters">(boolean val)</span></div>
<div class="block">Sets autosize flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>val</code> - new value of a flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAutosized()">
<h3>isAutosized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAutosized</span>()</div>
<div class="block">Returns autosize flag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value of autosize flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetAutosize(boolean)">
<h3>sSetAutosize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetAutosize</span><wbr/><span class="parameters">(boolean val)</span></div>
<div class="block">Simple setter for autosize flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>val</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSuspendShapeAutoResizeMode()">
<h3>getSuspendShapeAutoResizeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSuspendShapeAutoResizeMode</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getSuspendShapeAutoResizeMode</code> in interface <code>com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetSuspendShapeAutoResizeMode(java.lang.String)">
<h3>sSetSuspendShapeAutoResizeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetSuspendShapeAutoResizeMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
</section>
</li>
<li>
<section class="detail" id="setSuspendShapeAutoResizeMode(java.lang.String)">
<h3>setSuspendShapeAutoResizeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSuspendShapeAutoResizeMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</span></div>
</section>
</li>
<li>
<section class="detail" id="getBounds()">
<h3>getBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBounds</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getBounds()">PresentationElement</a></code></span></div>
<div class="block">Method returns bounds of this element.
 Use PresentationElementsManager to change a bounds of the element.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getBounds()">getBounds</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>bounds of the element.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>PresentationElementsManager.reshapeShapeElement</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotCopyBounds()">
<h3>getNotCopyBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getNotCopyBounds</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getNotCopyBounds()">PresentationElement</a></code></span></div>
<div class="block">get not copy bounds of object throws NoRectangleDefinedException</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getNotCopyBounds()">getNotCopyBounds</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>rectangle of bounds</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMiddlePoint(java.awt.Point)">
<h3>getMiddlePoint</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getMiddlePoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> rel)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getMiddlePoint(java.awt.Point)">PresentationElement</a></code></span></div>
<div class="block">Gets middle point of this view,</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getMiddlePoint(java.awt.Point)">getMiddlePoint</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>rel</code> - relative point</dd>
<dt>Returns:</dt>
<dd>middle point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMiddlePointX(java.awt.Point)">
<h3>getMiddlePointX</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMiddlePointX</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> rel)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getMiddlePointX(java.awt.Point)">getMiddlePointX</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMiddlePointY(java.awt.Point)">
<h3>getMiddlePointY</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMiddlePointY</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> rel)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getMiddlePointY(java.awt.Point)">getMiddlePointY</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMiddlePoint()">
<h3>getMiddlePoint</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getMiddlePoint</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getMiddlePoint()">PresentationElement</a></code></span></div>
<div class="block">Returns middle point of this element. Middle point for shapes usually will be center point of
 bounds, middle point for paths will be center of path curve.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getMiddlePoint()">getMiddlePoint</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>point that is considered as middle for this element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMiddlePointX()">
<h3>getMiddlePointX</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMiddlePointX</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getMiddlePointX()">getMiddlePointX</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMiddlePointY()">
<h3>getMiddlePointY</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMiddlePointY</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getMiddlePointY()">getMiddlePointY</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetBounds(java.awt.Rectangle)">
<h3>sSetBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#sSetBounds(java.awt.Rectangle)">PresentationElement</a></code></span></div>
<div class="block">Sets bounds of this object view only.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../PresentationElement.html#sSetBounds(java.awt.Rectangle)">sSetBounds</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>bounds</code> - rectangle of bounds.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="adjustBounds(java.awt.Rectangle)">
<h3>adjustBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">adjustBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
<div class="block">Validates bounds</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bounds</code> - bounds</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBounds(java.awt.Rectangle)">
<h3>setBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#setBounds(java.awt.Rectangle)">PresentationElement</a></code></span></div>
<div class="block">sets bounds of this object view</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../PresentationElement.html#setBounds(java.awt.Rectangle)">setBounds</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>bounds</code> - rectangle of bounds</dd>
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
<dt>Specified by:</dt>
<dd><code><a href="../PresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">coversPoint</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if object covers this point</dd>
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
<dt>Specified by:</dt>
<dd><code><a href="../PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if object and rectangle intersects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#clone()">clone</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../paths/PathConnector.html#clone()">clone</a></code> in class <code><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePathElements()">
<h3>movePathElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">movePathElements</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../paths/PathConnector.html#movePathElements()">movePathElements</a></code> in class <code><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearOldRect()">
<h3>clearOldRect</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">clearOldRect</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setOldRect(java.awt.Rectangle)">
<h3>setOldRect</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setOldRect</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> old)</span></div>
</section>
</li>
<li>
<section class="detail" id="movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">
<h3>movePathElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">movePathElement</span><wbr/><span class="parameters">(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 @CheckForNull
 <a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> requestor)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">PathConnector</a></code></span></div>
<div class="block">Calculates position of a path element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../paths/PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a></code> in class <code><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
<dt>Parameters:</dt>
<dd><code>path</code> - element which position will be calculated.</dd>
<dd><code>requestor</code> - the requestor of this path moving. Implementations may check to avoid endless loops.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>getIntersection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getIntersection</span><wbr/><span class="parameters">(int x,
 int y,
 @CheckForNull
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntersection(int,int,int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>getIntersection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getIntersection</span><wbr/><span class="parameters">(int x1,
 int y1,
 int x2,
 int y2,
 @CheckForNull
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</span></div>
<div class="block">Gets intersection point between shape view bounding rectangle
 and line.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x1</code> - first point of the line</dd>
<dd><code>y1</code> - first point of the line</dd>
<dd><code>x2</code> - second point of the line</dd>
<dd><code>y2</code> - second point of the line</dd>
<dd><code>path</code> - path</dd>
<dt>Returns:</dt>
<dd>intersection point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntersection(int,int,int,int,java.awt.Rectangle,com.nomagic.awt.ContainerShape)">
<h3>getIntersection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getIntersection</span><wbr/><span class="parameters">(int x1,
 int y1,
 int x2,
 int y2,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds,
 <a href="../../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a> boundingShape)</span></div>
<div class="block">Gets intersection point between bounding shape (or rectangle) and line.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x1</code> - first point of the line</dd>
<dd><code>y1</code> - first point of the line</dd>
<dd><code>x2</code> - second point of the line</dd>
<dd><code>y2</code> - second point of the line</dd>
<dd><code>bounds</code> - shape bounds</dd>
<dd><code>boundingShape</code> - bounding shape</dd>
<dt>Returns:</dt>
<dd>intersection point</dd>
</dl>
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
<dd><code><a href="../paths/PathConnector.html#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a></code> in class <code><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPreferredDimension(int,int)">
<h3>setPreferredDimension</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setPreferredDimension</span><wbr/><span class="parameters">(int width,
 int height)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPreferredDimension()">
<h3>getPreferredDimension</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getPreferredDimension</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getPreferredDimension()">PresentationElement</a></code></span></div>
<div class="block">Returns preferable dimension of the element.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getPreferredDimension()">getPreferredDimension</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>preferred dimension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simpleSetBounds(java.awt.Rectangle)">
<h3>simpleSetBounds</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">simpleSetBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#simpleSetBounds(java.awt.Rectangle)">PresentationElement</a></code></span></div>
<div class="block">Sets bounding rectangle.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>rect</code> - new bounding rectangle.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simpleSetBounds(int,int,int,int,boolean)">
<h3>simpleSetBounds</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">simpleSetBounds</span><wbr/><span class="parameters">(int x,
 int y,
 int width,
 int height,
 boolean calculatePrefSize)</span></div>
</section>
</li>
<li>
<section class="detail" id="simpleSetBounds(java.awt.Rectangle,boolean)">
<h3>simpleSetBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">simpleSetBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect,
 boolean calculatePrefSize)</span></div>
<div class="block">Sets the bounding rectangle of this shape view to the specified
 value for <code>bounds</code>. Moves all links connected to this
 shape connection points.
 <p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rect</code> - the new <i>bounds</i> for the shape view.</dd>
<dd><code>calculatePrefSize</code> - need to calculate preferred size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateEdge()">
<h3>calculateEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">calculateEdge</span>()</div>
</section>
</li>
<li>
<section class="detail" id="edgeChanged()">
<h3>edgeChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">edgeChanged</span>()</div>
</section>
</li>
<li>
<section class="detail" id="autosize()">
<h3>autosize</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">autosize</span>()</div>
</section>
</li>
<li>
<section class="detail" id="autosize(boolean)">
<h3>autosize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">autosize</span><wbr/><span class="parameters">(boolean calculatePrefSize)</span></div>
<div class="block">Calculate preferred size and make this shape size at least as preferred (if size is smaller)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>calculatePrefSize</code> - calculate preferred size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="autosizeAndResizeParent()">
<h3>autosizeAndResizeParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">autosizeAndResizeParent</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#autosizeAndResizeParent()">PresentationElement</a></code></span></div>
<div class="block">Resize itself and initiate parent resize</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#autosizeAndResizeParent()">autosizeAndResizeParent</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="moveLinksToSelf()">
<h3>moveLinksToSelf</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">moveLinksToSelf</span>()</div>
<div class="block">Move links to self.</div>
</section>
</li>
<li>
<section class="detail" id="addBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>addBreakPoints</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addBreakPoints</span><wbr/><span class="parameters">(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> link)</span></div>
<div class="block">Adds break points to link to self.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>link</code> - path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateAutosizeDimension(java.awt.Dimension,int,int,int,int)">
<h3>calculateAutosizeDimension</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">calculateAutosizeDimension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size,
 int locationX,
 int locationY,
 int prefSizeWidth,
 int prefSizeHeight)</span></div>
<div class="block">Calculates size of shape to be at least as preferred and fit all children</div>
<dl class="notes">
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
<section class="detail" id="maximumDimension(java.awt.Dimension)">
<h3>maximumDimension</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">maximumDimension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size)</span></div>
</section>
</li>
<li>
<section class="detail" id="ensureDimension(boolean)">
<h3>ensureDimension</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">ensureDimension</span><wbr/><span class="parameters">(boolean rememberBounds)</span></div>
<div class="block">If size is smaller than the preferred size, makes shape larger.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rememberBounds</code> - flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="needAdjustToPreferred()">
<h3>needAdjustToPreferred</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">needAdjustToPreferred</span>()</div>
<div class="block">Check if shape can be resized to a preferred size. Usually it is true if shape is manipulated and isAutosize is true.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if adjustments are necessary</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="needAdjustToMaximumDimension()">
<h3>needAdjustToMaximumDimension</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">needAdjustToMaximumDimension</span>()</div>
<div class="block">Check if shape should be resized to a maximum size.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if adjustments are necessary</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultDimension()">
<h3>getDefaultDimension</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getDefaultDimension</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSizeForDrawing()">
<h3>getSizeForDrawing</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getSizeForDrawing</span>()</div>
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
<dd><code><a href="../PresentationElement.html#recursiveAutosize()">recursiveAutosize</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
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
<dd><code><a href="../PresentationElement.html#initialize()">initialize</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateMinimumDimension()">
<h3>calculateMinimumDimension</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">calculateMinimumDimension</span>()</div>
<div class="block">calculates minimum size</div>
</section>
</li>
<li>
<section class="detail" id="minimumDimension(java.awt.Dimension)">
<h3>minimumDimension</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">minimumDimension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> min)</span></div>
<div class="block">calculates minimum size</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>min</code> - minimum size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMinimumDimension(int,int)">
<h3>setMinimumDimension</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setMinimumDimension</span><wbr/><span class="parameters">(int width,
 int height)</span></div>
<div class="block">Sets min size</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>width</code> - width</dd>
<dd><code>height</code> - height</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMinimumDimension()">
<h3>getMinimumDimension</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getMinimumDimension</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getMinimumDimension()">PresentationElement</a></code></span></div>
<div class="block">get minimum possible size for object</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getMinimumDimension()">getMinimumDimension</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>minimum dimension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getManipulatedElementAt</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getManipulatedElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind intersectionKind)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">PresentationElement</a></code></span></div>
<div class="block">Gets manipulated symbol at specified point pt.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedElementAt</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>pt</code> - <code> Point </code></dd>
<dd><code>intersectionKind</code> - intersection kind to check for</dd>
<dt>Returns:</dt>
<dd>manipulate symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculatePreferredDimension()">
<h3>calculatePreferredDimension</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">calculatePreferredDimension</span>()</div>
</section>
</li>
<li>
<section class="detail" id="calculatePreferredDimension(int,int)">
<h3>calculatePreferredDimension</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">calculatePreferredDimension</span><wbr/><span class="parameters">(int locationX,
 int locationY)</span></div>
</section>
</li>
<li>
<section class="detail" id="preferredDimension(java.awt.Dimension,int,int)">
<h3>preferredDimension</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">preferredDimension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</span></div>
</section>
</li>
<li>
<section class="detail" id="prefDimensionByManipulatedChildren(java.awt.Dimension,int,int)">
<h3>prefDimensionByManipulatedChildren</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">prefDimensionByManipulatedChildren</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> pref,
 int locationX,
 int locationY)</span></div>
</section>
</li>
<li>
<section class="detail" id="canHavePaths()">
<h3>canHavePaths</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canHavePaths</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#canHavePaths()">canHavePaths</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if symbol can have connected paths. Return false here.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBoundsShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">
<h3>createBoundsShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></span> <span class="element-name">createBoundsShape</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 <a href="../BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols">BoundsTransformation</a> transformation)</span></div>
<div class="block">Creates bounding shape for intersection calculation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - path</dd>
<dd><code>transformation</code> - transformation</dd>
<dt>Returns:</dt>
<dd>shape</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">
<h3>internalGetBoundsShape</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></span> <span class="element-name">internalGetBoundsShape</span><wbr/><span class="parameters">(<a href="../ConverterToShape.html" title="class in com.nomagic.magicdraw.uml.symbols">ConverterToShape</a> converterToShape)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
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
<dd><code><a href="../PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>changer</code> - new properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeAutosized()">
<h3>canBeAutosized</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">canBeAutosized</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isSnapToGrid()">
<h3>isSnapToGrid</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isSnapToGrid</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#isSnapToGrid()">isSnapToGrid</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.MDElementImpl</code></span></div>
<div class="block">Returns string representation of this element.
 Useful for debugging purposes.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>toString</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFixedConnectionPoints()">
<h3>getFixedConnectionPoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>[]</span> <span class="element-name">getFixedConnectionPoints</span>()</div>
<div class="block">-----1------
 |             |
 |             |
 4             2
 |             |
 |             |
 ----3-------</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>array of 4 points used to connect paths to fixed points.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseFixedConnectionPoints()">
<h3>isUseFixedConnectionPoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseFixedConnectionPoints</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setUseFixedConnectionPoints(boolean)">
<h3>setUseFixedConnectionPoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseFixedConnectionPoints</span><wbr/><span class="parameters">(boolean useFixed)</span></div>
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
<dd><code><a href="../PresentationElement.html#internalSilentApply()">internalSilentApply</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildrenInsets(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel)">
<h3>getChildrenInsets</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.ui.UnmodifiableInsets</span> <span class="element-name">getChildrenInsets</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.InsetsLevel insetsLevel)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>insetsLevel</code> - describes the level of insets</dd>
<dt>Returns:</dt>
<dd>shape insets for children</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOnEdge(int)">
<h3>setOnEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOnEdge</span><wbr/><span class="parameters">(int onEdge)</span></div>
<div class="block">Sets on edge property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>onEdge</code> - the edge constant</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOnEdge()"><code>getOnEdge()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onChildEdgeChange(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>onChildEdgeChange</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">onChildEdgeChange</span><wbr/><span class="parameters">(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> child)</span></div>
</section>
</li>
<li>
<section class="detail" id="getOnEdge()">
<h3>getOnEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getOnEdge</span>()</div>
<div class="block">Returns some edge constant if this shape must be on its parent edge.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>edge constant</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#NO_EDGE"><code>NO_EDGE</code></a></li>
<li><a href="#LEFT_EDGE"><code>LEFT_EDGE</code></a></li>
<li><a href="#RIGHT_EDGE"><code>RIGHT_EDGE</code></a></li>
<li><a href="#TOP_EDGE"><code>TOP_EDGE</code></a></li>
<li><a href="#BOTTOM_EDGE"><code>BOTTOM_EDGE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOnEdgePosition()">
<h3>getOnEdgePosition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getOnEdgePosition</span>()</div>
<div class="block">Returns position on edge.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>position on edge.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#ON_EDGE_POSITION"><code>ON_EDGE_POSITION</code></a></li>
<li><a href="#INSIDE_EDGE_POSITION"><code>INSIDE_EDGE_POSITION</code></a></li>
<li><a href="#OUTSIDE_EDGE_POSITION"><code>OUTSIDE_EDGE_POSITION</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOnEdgeCornerDistance()">
<h3>getOnEdgeCornerDistance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getOnEdgeCornerDistance</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>inset from a corner</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="adjustOnEdge()">
<h3>adjustOnEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">adjustOnEdge</span>()</div>
<div class="block">Adjust shape on the edge of its parent.</div>
</section>
</li>
<li>
<section class="detail" id="calculateAdjustOnEdgeLocation(java.awt.Rectangle)">
<h3>calculateAdjustOnEdgeLocation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">calculateAdjustOnEdgeLocation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
<div class="block">Calculates on edge location for a shape.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bounds</code> - bounds</dd>
<dt>Returns:</dt>
<dd>location on edge or null if shape is not on edge</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOnEdge()">
<h3>isOnEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOnEdge</span>()</div>
<div class="block">Returns true if symbol is on edge</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if on edge</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShapeOnEdge(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isShapeOnEdge</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isShapeOnEdge</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
</section>
</li>
<li>
<section class="detail" id="adjustOnEdgeChildren()">
<h3>adjustOnEdgeChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">adjustOnEdgeChildren</span>()</div>
<div class="block">Adjust on edge all children</div>
</section>
</li>
<li>
<section class="detail" id="adjustOnEdge(java.awt.Rectangle,int,int,int)">
<h3>adjustOnEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">adjustOnEdge</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds,
 int edge,
 int position,
 int cornerDistance)</span></div>
<div class="block">Calculates location of given rectangle according given parent edge and position on edge.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bounds</code> - the given rectangle</dd>
<dd><code>edge</code> - the parent bounds</dd>
<dd><code>position</code> - the position on edge</dd>
<dd><code>cornerDistance</code> - distance from a corner</dd>
<dt>Returns:</dt>
<dd>adjusted point</dd>
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
<dd><code><a href="../PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">adjustBoundsBeforeChange</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNearestEdge(java.awt.Rectangle)">
<h3>getNearestEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getNearestEdge</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span></div>
<div class="block">Return the nearest edge to given rectangle.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - the given rectangle.</dd>
<dt>Returns:</dt>
<dd>nearest edge</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#TOP_EDGE"><code>TOP_EDGE</code></a></li>
<li><a href="#BOTTOM_EDGE"><code>BOTTOM_EDGE</code></a></li>
<li><a href="#LEFT_EDGE"><code>LEFT_EDGE</code></a></li>
<li><a href="#RIGHT_EDGE"><code>RIGHT_EDGE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNearestEdge(int,int)">
<h3>getNearestEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getNearestEdge</span><wbr/><span class="parameters">(int x,
 int y)</span></div>
<div class="block">Return the nearest edge to given point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - the given point x</dd>
<dd><code>y</code> - the given point y</dd>
<dt>Returns:</dt>
<dd>nearest edge</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#TOP_EDGE"><code>TOP_EDGE</code></a></li>
<li><a href="#BOTTOM_EDGE"><code>BOTTOM_EDGE</code></a></li>
<li><a href="#LEFT_EDGE"><code>LEFT_EDGE</code></a></li>
<li><a href="#RIGHT_EDGE"><code>RIGHT_EDGE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLoadedDimension(com.nomagic.ui.UnmodifiableDimension)">
<h3>setLoadedDimension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLoadedDimension</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a> loadedDimension)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLoadedDimension()">
<h3>getLoadedDimension</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getLoadedDimension</span>()</div>
</section>
</li>
<li>
<section class="detail" id="updateLater()">
<h3>updateLater</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateLater</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#updateLater()">PresentationElement</a></code></span></div>
<div class="block">Registers this symbol to postponed "update" at the end of current command execution.
 Symbol will be updated when all other commands are executed.
 If this is not possible to register, updates symbol immediately.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#updateLater()">updateLater</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInsetsForOnEdgeShapes()">
<h3>getInsetsForOnEdgeShapes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Insets.html" title="class or interface in java.awt">Insets</a></span> <span class="element-name">getInsetsForOnEdgeShapes</span>()</div>
</section>
</li>
<li>
<section class="detail" id="calculateOnEdgeBounds()">
<h3>calculateOnEdgeBounds</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds</span> <span class="element-name">calculateOnEdgeBounds</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getHeaderInsetReduce(int,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds)">
<h3>getHeaderInsetReduce</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">getHeaderInsetReduce</span><wbr/><span class="parameters">(int edge,
 com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement.OnEdgeBounds bounds)</span></div>
</section>
</li>
<li>
<section class="detail" id="isVerticalCenterlineProvider()">
<h3>isVerticalCenterlineProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isVerticalCenterlineProvider</span>()</div>
<div class="block">Indicates whether this shape provides vertical center-lines to other shapes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this shape provides vertical center lines, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isHorizontalCenterlineProvider()">
<h3>isHorizontalCenterlineProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isHorizontalCenterlineProvider</span>()</div>
<div class="block">Indicates whether this shape provides horizontal center-lines to other shapes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this shape provides horizontal center-lines, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prepareForShadowDrawing(java.awt.Graphics2D)">
<h3>prepareForShadowDrawing</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">prepareForShadowDrawing</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#prepareForShadowDrawing(java.awt.Graphics2D)">PresentationElement</a></code></span></div>
<div class="block">Prepares graphics for symbol shadow drawing. If diagram allows shadows, sets darker diagram background color to given graphics.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>g</code> - the given graphics</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="shouldDrawShadow()">
<h3>shouldDrawShadow</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">shouldDrawShadow</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getEdgeLine(int)">
<h3>getEdgeLine</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../../awt/Line.html" title="class in com.nomagic.awt">Line</a></span> <span class="element-name">getEdgeLine</span><wbr/><span class="parameters">(int edge)</span></div>
<div class="block">Returns a line representing a specified edge.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>edge</code> - - edge of the shape element.</dd>
<dt>Returns:</dt>
<dd>a line that represents an edge.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCenterlineableInnerParts(int)">
<h3>getCenterlineableInnerParts</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape&gt;</span> <span class="element-name">getCenterlineableInnerParts</span><wbr/><span class="parameters">(int orientation)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code></span></div>
<div class="block">Gets shape inner parts which have centerlines.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getCenterlineableInnerParts</code> in interface <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code></dd>
<dt>Parameters:</dt>
<dd><code>orientation</code> - orientation of inner parts centerlines.</dd>
<dt>Returns:</dt>
<dd>a list of inner parts which can have centerlines.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findFreePlaceForShapeOnBorder(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Rectangle)">
<h3>findFreePlaceForShapeOnBorder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">findFreePlaceForShapeOnBorder</span><wbr/><span class="parameters">(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> shapeB)</span></div>
<div class="block">Looks for available position slot for given shape on a border</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shape</code> - shape added on some border</dd>
<dd><code>shapeB</code> - bounds of shape. This method can be used while drawing a new shape, so we cannot take bounds from shape</dd>
<dt>Returns:</dt>
<dd>new location for shape</dd>
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
<dt>Returns:</dt>
<dd>true if this shape provides horizontal centerline, false otherwise.</dd>
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
<dt>Returns:</dt>
<dd>true if this shape can be snapped to centerlines, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCenterlineInner()">
<h3>isCenterlineInner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCenterlineInner</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code></span></div>
<div class="block">Indicates if the centerline provided by this shape is provided by its inner parts, not the shape itself.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isCenterlineInner</code> in interface <code>com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</code></dd>
<dt>Returns:</dt>
<dd>true if centerline is inner, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNeedAutosizeFlag()">
<h3>getNeedAutosizeFlag</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">byte</span> <span class="element-name">getNeedAutosizeFlag</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setNeedAutosizeFlag(byte)">
<h3>setNeedAutosizeFlag</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNeedAutosizeFlag</span><wbr/><span class="parameters">(byte needAutosize)</span></div>
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
<dd><code><a href="../paths/PathConnector.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a></code> in class <code><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visibility</code> - flag value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="layoutChildren()">
<h3>layoutChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">layoutChildren</span>()</div>
<div class="block">Layout children of this shape.
 This method is declared final to control a layout flag.
 Subclasses must override internalLayoutChildren.</div>
</section>
</li>
<li>
<section class="detail" id="layoutChildren(boolean)">
<h3>layoutChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">layoutChildren</span><wbr/><span class="parameters">(boolean calculatePrefSize)</span></div>
<div class="block">Layout children of this shape.
 This method is declared final to a control layout flag.
 Subclasses must override internalLayoutChildren</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>calculatePrefSize</code> - calculate preferred size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isChildLayoutable(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isChildLayoutable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isChildLayoutable</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</span></div>
<div class="block">Check if given child is "layoutable" - it means this shape controls the bounds of child inside layoutChildren() method.
 Not "layoutable" children are just moved together with parents, but layoutChildren() do not control their location.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>child</code> - child</dd>
<dt>Returns:</dt>
<dd>true, if given child is layed-out inside autosize method of this shape. False here</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCalculatePreferredRegardingChildren(boolean)">
<h3>setCalculatePreferredRegardingChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCalculatePreferredRegardingChildren</span><wbr/><span class="parameters">(boolean flag)</span></div>
<div class="block">Sets the CALCULATE_PREFERRED_REGARDING_CHILDREN value.
 By default, this value is true.
 If it was changed, it must be reverted, so put the resetting to default in finally block.
 For resetting to default value use: <a href="#resetCalculatePreferredRegardingChildren()"><code>resetCalculatePreferredRegardingChildren()</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flag</code> - the value to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetCalculatePreferredRegardingChildren()">
<h3>resetCalculatePreferredRegardingChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resetCalculatePreferredRegardingChildren</span>()</div>
<div class="block">Resets the CALCULATE_PREFERRED_REGARDING_CHILDREN value to the default.</div>
</section>
</li>
<li>
<section class="detail" id="getBorderElementMargin()">
<h3>getBorderElementMargin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getBorderElementMargin</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetBorderElementMargin(java.lang.String)">
<h3>sSetBorderElementMargin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetBorderElementMargin</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="setBorderElementMargin(java.lang.String)">
<h3>setBorderElementMargin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBorderElementMargin</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="hasManipulator()">
<h3>hasManipulator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasManipulator</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#hasManipulator()">PresentationElement</a></code></span></div>
<div class="block">Returns true, if view has manipulator (is selectable)</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#hasManipulator()">hasManipulator</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReshapeMode()">
<h3>getReshapeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.ReshapeMode</span> <span class="element-name">getReshapeMode</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>current symbol reshape mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReshapeMode(com.nomagic.magicdraw.uml.symbols.ReshapeMode)">
<h3>setReshapeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setReshapeMode</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.ReshapeMode mode)</span></div>
<div class="block">Set symbol reshape mode</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mode</code> - reshape mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManipulationPreferredDimension()">
<h3>getManipulationPreferredDimension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getManipulationPreferredDimension</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getManipulationPreferredDimension()">getManipulationPreferredDimension</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>size for manipulator manipulations</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="minimumOrMinimumShrinkableDimension(java.awt.Dimension)">
<h3>minimumOrMinimumShrinkableDimension</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">minimumOrMinimumShrinkableDimension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size)</span></div>
</section>
</li>
<li>
<section class="detail" id="minimumDimensionForShrinking(java.awt.Dimension,int,int)">
<h3>minimumDimensionForShrinking</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">minimumDimensionForShrinking</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size,
 int locationX,
 int locationY)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>size</code> - size</dd>
<dd><code>locationX</code> - location X</dd>
<dd><code>locationY</code> - location Y</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDimensionForShrinking(int,int)">
<h3>getDimensionForShrinking</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getDimensionForShrinking</span><wbr/><span class="parameters">(int width,
 int height)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShrinkable()">
<h3>isShrinkable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShrinkable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="ensurePreferredDimensionIfShrinkable()">
<h3>ensurePreferredDimensionIfShrinkable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">ensurePreferredDimensionIfShrinkable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="ensurePreferredDimensionIfShrinkable(java.awt.Rectangle)">
<h3>ensurePreferredDimensionIfShrinkable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">ensurePreferredDimensionIfShrinkable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
</section>
</li>
<li>
<section class="detail" id="calculateAndGetPreferredDimension()">
<h3>calculateAndGetPreferredDimension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">calculateAndGetPreferredDimension</span>()</div>
</section>
</li>
<li>
<section class="detail" id="calculateAndGetMinimumShrinkingDimension(int,int)">
<h3>calculateAndGetMinimumShrinkingDimension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">calculateAndGetMinimumShrinkingDimension</span><wbr/><span class="parameters">(int locationX,
 int locationY)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPreferredDimensionForAutosize()">
<h3>getPreferredDimensionForAutosize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getPreferredDimensionForAutosize</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#getPreferredDimensionForAutosize()">PresentationElement</a></code></span></div>
<div class="block">Returns preferable dimension of the element for autosize.This implementation simple returns
 preferred size.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getPreferredDimensionForAutosize()">getPreferredDimensionForAutosize</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>preferred dimension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSnapShapesOnBorderToGrid()">
<h3>isSnapShapesOnBorderToGrid</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSnapShapesOnBorderToGrid</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setSnapShapesOnBorderToGrid(boolean)">
<h3>setSnapShapesOnBorderToGrid</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSnapShapesOnBorderToGrid</span><wbr/><span class="parameters">(boolean snapShapesOnBorderToGrid)</span></div>
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
