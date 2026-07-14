# JAVA OPENAPI: PathElement (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/paths/PathElement.html
- source_path: `com/nomagic/magicdraw/uml/symbols/paths/PathElement.html`
- source_sha256: `83796c5c3bd2aff00132b3e978aedcf8fcbe17fe48d22fc8f499d032c7d0203d`
- captured_utc: `2026-07-14T16:56:01.805531+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.paths](package-summary.html)

## Class PathElement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](PathConnector.html)
com.nomagic.magicdraw.uml.symbols.paths.PathElement

All Implemented Interfaces:
`[BaseElement](../../BaseElement.html)`, `[MDElement](../../MDElement.html)`, `[ModelElementProvider](../../ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.LineJumpDrawer`, `com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView`, `[ContainmentLinkView](ContainmentLinkView.html)`, `[LinkAttributeView](LinkAttributeView.html)`, `[NoteAnchorView](NoteAnchorView.html)`

@OpenApipublic abstract classPathElement
extends [PathConnector](PathConnector.html)
implements com.nomagic.magicdraw.uml.symbols.LineJumpDrawer, com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider

Base class for all path kinds of symbols.
 Path is a symbol that connects two other symbols as a graphical path.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BEZIER](#BEZIER)`
Bezier path line style.
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[LINE_STYLE](#LINE_STYLE)`
All possible path line styles.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OBLIQUE](#OBLIQUE)`
Polyline path line style.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RECTILINEAR](#RECTILINEAR)`
Path line style with rectilinear (90 degrees) breakpoint corners.
Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](PathConnector.html)
`[showsProxy](PathConnector.html#showsProxy)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DEFAULT_LINE_WIDTH](../PresentationElement.html#DEFAULT_LINE_WIDTH), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [HANDLE_SIZE](../PresentationElement.html#HANDLE_SIZE), [MAX_LINE_WIDTH](../PresentationElement.html#MAX_LINE_WIDTH), [MIN_LINE_WIDTH](../PresentationElement.html#MIN_LINE_WIDTH), [peStyle](../PresentationElement.html#peStyle), [SHADOW_WIDTH](../PresentationElement.html#SHADOW_WIDTH), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PathElement](#%3Cinit%3E())()`

`[PathElement](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) parent)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../../Visitor.html) visitor)`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
`boolean`
`[addConnectedPathElement](#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](PathElement.html) link)`
Method to add sub link to this link.
`void`
`[addLineJumps](#addLineJumps(java.awt.geom.GeneralPath,java.awt.Point,java.awt.Point,java.awt.Point))([GeneralPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html) path,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) segmentStartPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) startPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) endPoint)`
Adds line jumps to the specified path.
`static void`
`[applyStrokeForLineDrawing](#applyStrokeForLineDrawing(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Graphics2D,boolean,java.awt.BasicStroke))([PresentationElement](../PresentationElement.html) pathElement,
 [Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 boolean line,
 [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) stroke)`

`boolean`
`[askDeleteDataConfirmation](#askDeleteDataConfirmation())()`
Return true, because while deleting link view user must be prompt about deleting data
`void`
`[atInsert](#atInsert())()`
Inserts ends of link into shapes.
`final void`
`[breakPointsChanged](#breakPointsChanged(java.util.List,java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> oldPoints,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> newPoints)`
Moves all connection point for the links that are attached to this
 link middle point.
`protected void`
`[cacheActualDrawPoints](#cacheActualDrawPoints(java.awt.Point,java.awt.Point,java.util.List))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplierDrawPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) clientDrawPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> breakPoints)`

`protected void`
`[cacheValues](#cacheValues(java.awt.Point,java.awt.Point,java.awt.Point,java.awt.Point,java.util.List))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) cachedActualSupplierDrawPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) cachedActualClientDrawPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) cacheSupplierDrawPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) cacheClientDrawPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> cacheBreakPoints)`

`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[calculatePathBounds](#calculatePathBounds(java.awt.Point,java.awt.Point,java.util.List))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplier,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) client,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> breaks)`

`boolean`
`[canChangeClient](#canChangeClient())()`

`boolean`
`[canChangeLineStyle](#canChangeLineStyle())()`

`boolean`
`[canChangeSupplier](#canChangeSupplier())()`

`boolean`
`[canClearBreakPoints](#canClearBreakPoints())()`

`void`
`[clearClientTranslation](#clearClientTranslation())()`
Clears a client translated flag.
`void`
`[clearRegisteredLineJumpInfos](#clearRegisteredLineJumpInfos())()`
Clears all registered LineJumpInfos.
`void`
`[clearSupplierTranslation](#clearSupplierTranslation())()`
Clears a supplier translated flag.
`[PathElement](PathElement.html)`
`[clone](#clone())()`

`void`
`[connectModelElement](#connectModelElement(com.nomagic.magicdraw.uml.symbols.paths.ConnectModelElementParticipant))(com.nomagic.magicdraw.uml.symbols.paths.ConnectModelElementParticipant participant)`
Connects `ModelElement` of this path to related elements of a given client and supplier
`boolean`
`[coversPoint](#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Checks if object covers provided point
`com.nomagic.magicdraw.uml.symbols.FillStrategy`
`[createFillStrategy](#createFillStrategy())()`

`protected void`
`[createSmartListenerConfig](#createSmartListenerConfig(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)`

`void`
`[dispose](#dispose())()`
Disconnect this link from shapes.
`void`
`[draw](#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`
abstract method for drawing ViewObject object
 used to draw object on graphics
`void`
`[draw](#draw(java.awt.Graphics2D,java.awt.Point,java.awt.Point,java.util.List))([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplierPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) clientPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> breakPoints)`
Draws link from given point pt1 through break points
 to given point pt2.
`com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon`
`[dynamicPathIcon](#dynamicPathIcon())()`

`com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon`
`[dynamicPathIcon](#dynamicPathIcon(com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon))(com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon pathIcon)`

`final com.dassault_systemes.modeler.foundation.model.ModelElement`
`[findOwnerForElement](#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext))([PresentationElement](../PresentationElement.html) newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)`

`com.dassault_systemes.modeler.foundation.model.ModelElement`
`[findOwnerForElement](#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext))([PresentationElement](../PresentationElement.html) newParent,
 [PresentationElement](../PresentationElement.html) client,
 [PresentationElement](../PresentationElement.html) supplier,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)`

`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getActualClientDrawPoint](#getActualClientDrawPoint())()`
Returns actual client side draw point.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getActualSupplierDrawPoint](#getActualSupplierDrawPoint())()`
Returns actual supplier side draw point.
`final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)>`
`[getAllBreakPoints](#getAllBreakPoints())()`
Returns a break points list with added supplier and client end point in the list as well.
`[GeneralPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html)`
`[getBezierPath](#getBezierPath())()`
Calculates path for bezier curve drawing.
`[GeneralPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html)`
`[getBezierPath](#getBezierPath(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> points)`
Calculates path from breakpoints for bezier curve drawing.
`final [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBounds](#getBounds())()`
Calculates bounds of this link.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBoundsToRepaint](#getBoundsToRepaint())()`
Return bounds of the symbol that must be repainted.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getBreakPoint](#getBreakPoint(int))(int pos)`
Returns break point with given index.
`int`
`[getBreakPointCount](#getBreakPointCount())()`
returns size of break point vector
`final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)>`
`[getBreakPoints](#getBreakPoints())()`
Returns break points of the path.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getCachedActualClientDrawPoint](#getCachedActualClientDrawPoint())()`

`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getCachedActualSupplierDrawPoint](#getCachedActualSupplierDrawPoint())()`

`[PresentationElement](../PresentationElement.html)`
`[getClient](#getClient())()`
Returns client of the path.
`int`
`[getClientConnectionType](#getClientConnectionType())()`

`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getClientDrawPoint](#getClientDrawPoint())()`
Returns point where path drawing should start
`final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getClientPoint](#getClientPoint())()`
Returns point where path connects client end's element.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getCustomClientPoint](#getCustomClientPoint())()`

`static com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon`
`[getCustomStereotypeIcon](#getCustomStereotypeIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getCustomSupplierPoint](#getCustomSupplierPoint())()`

`[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getDefaultParentForData](#getDefaultParentForData())()`
Presentation element could suggest parent, which would be more acceptable, than adding to the client
 If returning null, general mechanism will work
`final int`
`[getIndexOfCoveredPath](#getIndexOfCoveredPath(int,int))(int x,
 int y)`
This method is used to get segment of path with witch given point has intersection.
`int`
`[getIndexOfCoveredPathInternal](#getIndexOfCoveredPathInternal(int,int,int,int))(int x,
 int y,
 int width,
 int height)`
This method is used to get segment of path with witch given rectangle has intersection.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getIntersection](#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement))(int x,
 int y,
 [PathElement](PathElement.html) path)`

`double`
`[getLineJumpStartAngle](#getLineJumpStartAngle(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLinkLineStyle](#getLinkLineStyle())()`

`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getMiddlePoint](#getMiddlePoint())()`
Calculates and returns middle point of link.
`final [Line](../../../../awt/Line.html)`
`[getNearestLinkPart](#getNearestLinkPart(int,int))(int x,
 int y)`
Returns the nearest link part to specified point.
`final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getNearestPoint](#getNearestPoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)`
Returns first break point or client point if arg is supplier point.
`int`
`[getNewBreakPointIndex](#getNewBreakPointIndex(java.awt.Point,java.util.List))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> brk)`
Find the nearest breakpoints for new one and
 calculate the position of the new breakpoint in breakpoint vector.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getNewPointByTheLink](#getNewPointByTheLink(java.util.List,java.util.List,java.awt.Point))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> oldBreaks,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> newBreaks,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) oldLocation)`

`[PresentationElement](../PresentationElement.html)`
`[getNextEnd](#getNextEnd(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) obj)`
Returns other than given end.
`final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getNextPoint](#getNextPoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)`
Returns next point to a given one.
`final [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getNotCopyBounds](#getNotCopyBounds())()`
get not copy bounds of object throws NoRectangleDefinedException
`com.dassault_systemes.modeler.foundation.diagram.style.PathStylePropertyDelegate`
`[getOwnStyleDelegate](#getOwnStyleDelegate())()`

`com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon`
`[getPathIcon](#getPathIcon())()`

`com.nomagic.magicdraw.uml.symbols.paths.painters.PathPainter<[PathElement](PathElement.html)>`
`[getPathPainter](#getPathPainter())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)>>`
`[getPaths](#getPaths())()`
Returns only one path which consist of actual supplier draw point, break points of the path element
 and actual client draw point.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getPointOnPath](#getPointOnPath(java.awt.Point,java.awt.Point,java.util.List,double))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplierPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) clientPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> breakpoints,
 double coefficient)`

`final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getPreviousPoint](#getPreviousPoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)`
Returns previous point to given one.
`[PresentationElement](../PresentationElement.html)`
`[getSupplier](#getSupplier())()`
Returns supplier of the path.
`int`
`[getSupplierConnectionType](#getSupplierConnectionType())()`

`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getSupplierDrawPoint](#getSupplierDrawPoint())()`
Returns point where path drawing should start
`final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getSupplierPoint](#getSupplierPoint())()`
Returns point where path connects supplier end's element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSuspendShapeAutoResizeMode](#getSuspendShapeAutoResizeMode())()`

`com.dassault_systemes.modeler.foundation.editing.Command`
`[handleRemoveBreaksAction](#handleRemoveBreaksAction())()`

`protected boolean`
`[hasClientPoint](#hasClientPoint())()`
Check if client point is already not null
`boolean`
`[hasManipulator](#hasManipulator())()`
Returns true, if view has manipulator (is selectable)
`boolean`
`[hasSharedModelElement](#hasSharedModelElement())()`
Returns true if `ModelElement` of this symbol can represented with other symbol.
`protected boolean`
`[hasSupplierPoint](#hasSupplierPoint())()`
Check if supplier point is already not null
`void`
`[internalApplyProperties](#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)`
Applies properties
`[Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html)`
`[internalGetBoundsShape](#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape))([ConverterToShape](../ConverterToShape.html) converterToShape)`

`[BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[internalGetPresentationElementStroke](#internalGetPresentationElementStroke(boolean,int))(boolean line,
 int width)`
This method must be overridden, if you need to use DASHED_STROKE or another one.
`protected [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[internalGetPresentationElementStroke](#internalGetPresentationElementStroke(boolean,int,int))(boolean line,
 int lineStyle,
 int width)`

`[BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[internalGetPresentationElementStroke](#internalGetPresentationElementStroke(int))(int width)`
Return a stroke used to paint symbol's main part
`void`
`[internalMovedAsToSelf](#internalMovedAsToSelf(int,int))(int dx,
 int dy)`
This is an internal method to notify a path that it was moved by connecting shape as the path "to self"
`void`
`[internalSilentApply](#internalSilentApply())()`
Silently applies all properties after initialization
`protected void`
`[internalSnapToGrid](#internalSnapToGrid(float))(float step)`

`final boolean`
`[intersects](#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Check if any line between breakpoints intersect with given points of rectangle
`boolean`
`[intersectsInternal](#intersectsInternal(int,int,int,int))(int x,
 int y,
 int width,
 int height)`
Check intersection with given rectangle.
`boolean`
`[isAlwaysToSelf](#isAlwaysToSelf())()`

`boolean`
`[isBezier](#isBezier())()`

`boolean`
`[isBezierIntersects](#isBezierIntersects(int,int,int,int))(int x,
 int y,
 int width,
 int height)`
Check if it is bezier path intersection with rectangle.
`boolean`
`[isBreakable](#isBreakable())()`
Shows whether a path is breakable.
`final boolean`
`[isConnectable](#isConnectable(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) supplier,
 [PresentationElement](../PresentationElement.html) client)`
Checks if this path can connect given two elements.
`final boolean`
`[isConnectable](#isConnectable(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.Map))([PresentationElement](../PresentationElement.html) supplier,
 [PresentationElement](../PresentationElement.html) client,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> options)`
Checks if this path can connect given two elements.
`boolean`
`[isDrawLineJumps](#isDrawLineJumps())()`
Returns true if the path element wants to draw line jumps.
`boolean`
`[isFixed](#isFixed())()`
If a path tied to its supplier and client (cannot be reconnected)
`boolean`
`[isLinkLineStyleDefined](#isLinkLineStyleDefined())()`

`boolean`
`[isOblique](#isOblique())()`

`boolean`
`[isRectilinear](#isRectilinear())()`

`boolean`
`[isRounded](#isRounded())()`
Returns value of the "Is Rounded" path symbol property.
`boolean`
`[isSmartLayoutNeeded](#isSmartLayoutNeeded())()`
Returns smart layout needed flag.
`protected boolean`
`[isSnapToGrid](#isSnapToGrid())()`

`boolean`
`[isToSelf](#isToSelf())()`

`boolean`
`[isUseFlowLayoutLogic](#isUseFlowLayoutLogic())()`
Indicates if smart path/shape edit should be used in this diagram.
`boolean`
`[isVertical](#isVertical())()`
Indicates if path element is drawn in the diagram which has vertical orientation.
`void`
`[makeRectilinear](#makeRectilinear())()`
Makes link rectilinear.
`void`
`[makeRectilinear](#makeRectilinear(boolean))(boolean notify)`
Makes link rectilinear.
`void`
`[moveLinkToClientParent](#moveLinkToClientParent(boolean))(boolean simpleAdd)`

`protected void`
`[movePathElement](#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector))([PathElement](PathElement.html) link,
 [PathConnector](PathConnector.html) requestor)`
Moves link.
`boolean`
`[needsToMoveOtherEnd](#needsToMoveOtherEnd())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[nextStyle](#nextStyle())()`

`void`
`[notifyBreakPointsChanged](#notifyBreakPointsChanged(java.util.List,java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> oldPoints,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> newPoints)`
Notifies about break point vector changes
`void`
`[notifyRepaintManager](#notifyRepaintManager(boolean))(boolean boundsChanged)`
Notifies the repaint manager about changes in bounds.
`protected final void`
`[notifyRepaintManager](#notifyRepaintManager(java.util.List,java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> oldBreakpoints,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> newBreakpoints)`

`void`
`[optimizeLoops](#optimizeLoops())()`
Removes loops from paths for example:
 path
 |
 ----------+
 | |
 ------
`void`
`[paintSelf](#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`protected boolean`
`[preDisposeOnUpdate](#preDisposeOnUpdate())()`
Validate symbol against model and try to fix it before actual symbol update.
`boolean`
`[prepareForLineDrawing](#prepareForLineDrawing(java.awt.Graphics2D,boolean))([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 boolean line)`
Prepares graphics for line drawing.
`void`
`[registerLineJumpInfos](#registerLineJumpInfos(int,java.awt.Point,java.util.List))(int pathIndex,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) segmentStartPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.uml.symbols.LineJumpInfo> lineJumps)`
Registers line jump info for specified path and specified segmentStartPoint in the path.
`void`
`[registerLineJumpStartAngle](#registerLineJumpStartAngle(int,java.awt.Point,double))(int pathIndex,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point,
 double lineJumpStartAngle)`
Registers start angle for the specified path and specified start point of the path segment.
`boolean`
`[removeBreakPoints](#removeBreakPoints())()`
Removes break points if they do not really break the path (a path looks like without break points but really has them).
`void`
`[removeBreaks](#removeBreaks(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> points)`
Removes all break points if they are covered by client or client bounds.
`void`
`[removeRedundantBreakPoints](#removeRedundantBreakPoints(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> vct)`
Removes redundant breakpoints from link.
`void`
`[removeUnnecessaryBreakPoints](#removeUnnecessaryBreakPoints())()`
Removes unnecessary points from break point vector.
`protected void`
`[resetCache](#resetCache())()`

`void`
`[resizeParent](#resizeParent())()`
Do nothing, because path does not affect parent size
`final void`
`[sAddBreakPoint](#sAddBreakPoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)`
Adds new break point.
`final void`
`[sClearBreakPoints](#sClearBreakPoints())()`
Clear break points list.
`void`
`[setBounds](#setBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`
Moves link to new location.
`void`
`[setBreakable](#setBreakable(boolean))(boolean value)`
Sets a breakable flag on/off.
`final void`
`[setBreakPoints](#setBreakPoints(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> vct)`
Sets break point vector.
`protected void`
`[setCachedPathBounds](#setCachedPathBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`

`void`
`[setClient](#setClient(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) shape)`
Sets client for this link.
`void`
`[setClientPoint](#setClientPoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)`
Sets client point.
`void`
`[setCustomClientPoint](#setCustomClientPoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point)`

`void`
`[setCustomSupplierPoint](#setCustomSupplierPoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point)`

`void`
`[setLineJumpPlace](#setLineJumpPlace(com.nomagic.magicdraw.uml.symbols.LineJumpPlace))(com.nomagic.magicdraw.uml.symbols.LineJumpPlace lineJumpPlace)`
Sets line jump place of the path element.
`void`
`[setLinkLineStyle](#setLinkLineStyle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) style)`
sets LINK_LINE_STYLE property value.
`protected final void`
`[setPathPainter](#setPathPainter(com.nomagic.magicdraw.uml.symbols.paths.painters.PathPainter))(com.nomagic.magicdraw.uml.symbols.paths.painters.PathPainter pathPainter)`

`void`
`[setRectilinear](#setRectilinear())()`
Sets link rectilinear property value.
`void`
`[setRounded](#setRounded(boolean))(boolean rounded)`
Sets value of the "Is Rounded" path symbol property.
`void`
`[setSmartLayoutNeeded](#setSmartLayoutNeeded(boolean))(boolean smartLayoutNeeded)`
Sets smart layout needed flag.
`void`
`[setSupplier](#setSupplier(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) shape)`
Sets supplier end for link.
`void`
`[setSupplierPoint](#setSupplierPoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)`
Sets first point.
`void`
`[setSuspendShapeAutoResizeMode](#setSuspendShapeAutoResizeMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`

`void`
`[simpleSetBounds](#simpleSetBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`
calls break point vector changed method.
`void`
`[sSetBounds](#sSetBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`
Moves path to new location.
`void`
`[sSetBreakable](#sSetBreakable(boolean))(boolean value)`
Sets a breakable flag on/off.
`final void`
`[sSetBreakPoint](#sSetBreakPoint(java.awt.Point,int))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 int pos)`
Sets break point at the given position.
`final void`
`[sSetBreakPoints](#sSetBreakPoints(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> vct)`
Only sets break point vector.
`void`
`[sSetClient](#sSetClient(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) symbol)`
Sets client for this link.
`void`
`[sSetClientPoint](#sSetClientPoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)`
Sets client connection Point.
`void`
`[sSetLinkLineStyle](#sSetLinkLineStyle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) style)`
Change value of LINK_LINE_STYLE property.
`void`
`[sSetParent](#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) parent)`
Sets parent for this view.
`void`
`[sSetRounded](#sSetRounded(boolean))(boolean rounded)`
Sets value of the "Is Rounded" path symbol property.
`void`
`[sSetSupplier](#sSetSupplier(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) symbol)`
Sets supplier for this link.
`void`
`[sSetSupplierPoint](#sSetSupplierPoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)`
Sets supplier connection point.
`void`
`[sSetSuspendShapeAutoResizeMode](#sSetSuspendShapeAutoResizeMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)`

`void`
`[swapEnds](#swapEnds())()`
Swaps ends of the link
`final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[translateClientPoint](#translateClientPoint(java.awt.Rectangle,java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) old,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) newR)`

`final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[translateSupplierPoint](#translateSupplierPoint(java.awt.Rectangle,java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) old,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) newR)`

`com.nomagic.utils.Pair<com.dassault_systemes.modeler.foundation.model.ModelElement,[Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<com.dassault_systemes.modeler.foundation.model.ModelElement>>`
`[useOtherExistingElement](#useOtherExistingElement())()`
Finds and returns other model element which is semantically equivalent to this path model element.
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](PathConnector.html)
`[checkShowsProxy](PathConnector.html#checkShowsProxy()), [clearShowsProxy](PathConnector.html#clearShowsProxy()), [disposeConnectedPaths](PathConnector.html#disposeConnectedPaths()), [findSymbolForEnd](PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)), [findSymbolForEnd](PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)), [getConnectedPathElement](PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [getConnectedPathElementCount](PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](PathConnector.html#getConnectedPathElements(boolean,boolean)), [getPreferredArrowLength](PathConnector.html#getPreferredArrowLength()), [isShowsProxy](PathConnector.html#isShowsProxy()), [movePathElement](PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)), [movePathElements](PathConnector.html#movePathElements()), [removeConnectedPathElement](PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sAddConnectedPathElement](PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [selectPathsForMoving](PathConnector.html#selectPathsForMoving(java.util.List)), [setParent](PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [setVisibility](PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [sRemoveConnectedPathElement](PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [sSetConnectedPathElements](PathConnector.html#sSetConnectedPathElements(java.util.List)), [sSetVisibility](PathConnector.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [supportsVisibleConnectedPathElementsIfSelfInvisible](PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible())`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[addPresentationElement](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addPresentationElement](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)), [addPresentationElementWithoutResize](../PresentationElement.html#addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addProperty](../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [adjustBoundsBeforeChange](../PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)), [adjustChildBounds](../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [adjustChildBoundsForMoving](../PresentationElement.html#adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [alwaysShowTooltip](../PresentationElement.html#alwaysShowTooltip()), [applyProperties](../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [atInsertChildren](../PresentationElement.html#atInsertChildren()), [autosizeAndResizeManipulatedParent](../PresentationElement.html#autosizeAndResizeManipulatedParent()), [autosizeAndResizeParent](../PresentationElement.html#autosizeAndResizeParent()), [beforeDelete](../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)), [boundsChanged](../PresentationElement.html#boundsChanged()), [boundsChanged](../PresentationElement.html#boundsChanged(java.awt.Rectangle)), [canAddChild](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)), [canAddChild](../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [canAddInstance](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canAddInstance](../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [canBeDisposedOnUpdate](../PresentationElement.html#canBeDisposedOnUpdate()), [canChangeElementOwner](../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)), [canChangeParent](../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canFill](../PresentationElement.html#canFill()), [canHavePaths](../PresentationElement.html#canHavePaths()), [changeProperties](../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)), [checkElementOwnerOnChange](../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [checkProxyVisibility](../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)), [childrenForMoving](../PresentationElement.html#childrenForMoving()), [collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection)), [collectSubPresentationElements](../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)), [collectSubShowingPresentationElements](../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)), [coversPoint](../PresentationElement.html#coversPoint(int,int)), [createPresentationElementStyle](../PresentationElement.html#createPresentationElementStyle()), [createPropertyChangeListener](../PresentationElement.html#createPropertyChangeListener()), [disposeChildren](../PresentationElement.html#disposeChildren()), [disposePropertyChangeListener](../PresentationElement.html#disposePropertyChangeListener()), [drawBackground](../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbol](../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [drawSymbolBackground](../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [dynamicFillColor](../PresentationElement.html#dynamicFillColor()), [dynamicLineColor](../PresentationElement.html#dynamicLineColor()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth()), [dynamicLineWidth](../PresentationElement.html#dynamicLineWidth(int)), [dynamicPaintShadow](../PresentationElement.html#dynamicPaintShadow()), [dynamicStroke](../PresentationElement.html#dynamicStroke()), [dynamicStroke](../PresentationElement.html#dynamicStroke(int)), [dynamicStroke](../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)), [dynamicStyleFillColor](../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)), [dynamicStyleLineColor](../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)), [dynamicStyleTextColor](../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency()), [dynamicStyleTransparency](../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)), [dynamicStyleValue](../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)), [dynamicTextAlignment](../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)), [dynamicTextColor](../PresentationElement.html#dynamicTextColor()), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)), [findOwnerForChildElement](../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [findPresentationElement](../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)), [firePropertyChange](../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [generateID](../PresentationElement.html#generateID()), [getAbstractDiagramPresentationElement](../PresentationElement.html#getAbstractDiagramPresentationElement()), [getActualElement](../PresentationElement.html#getActualElement()), [getAdditionalRenderersToNotifyOnPropertiesChange](../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()), [getAssignableModelElementsClasses](../PresentationElement.html#getAssignableModelElementsClasses()), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getBoundsWithChildrenOnEdge](../PresentationElement.html#getBoundsWithChildrenOnEdge()), [getCenterlinePoint](../PresentationElement.html#getCenterlinePoint()), [getCenterlinePointX](../PresentationElement.html#getCenterlinePointX()), [getCenterlinePointY](../PresentationElement.html#getCenterlinePointY()), [getChildPresentationElementForContextMenu](../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)), [getChildrenWithSymbolProperties](../PresentationElement.html#getChildrenWithSymbolProperties()), [getConfiguration](../PresentationElement.html#getConfiguration()), [getDiagramPresentationElement](../PresentationElement.html#getDiagramPresentationElement()), [getDiagramSurface](../PresentationElement.html#getDiagramSurface()), [getDrawComparator](../PresentationElement.html#getDrawComparator()), [getDynamicConfigurations](../PresentationElement.html#getDynamicConfigurations()), [getDynamicStyleOwner](../PresentationElement.html#getDynamicStyleOwner()), [getEffectiveStyleDelegate](../PresentationElement.html#getEffectiveStyleDelegate()), [getEffectiveStyleOwner](../PresentationElement.html#getEffectiveStyleOwner()), [getElement](../PresentationElement.html#getElement()), [getElementsForRelationshipConnecting](../PresentationElement.html#getElementsForRelationshipConnecting()), [getElementToConnectRelationship](../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFillColor](../PresentationElement.html#getFillColor()), [getFont](../PresentationElement.html#getFont()), [getFontHeight](../PresentationElement.html#getFontHeight()), [getFontRenderContext](../PresentationElement.html#getFontRenderContext()), [getHumanName](../PresentationElement.html#getHumanName()), [getHumanType](../PresentationElement.html#getHumanType()), [getLineColor](../PresentationElement.html#getLineColor()), [getLineWidth](../PresentationElement.html#getLineWidth()), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point)), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedElementAt](../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedIntersectionWith](../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getManipulationBounds](../PresentationElement.html#getManipulationBounds(java.awt.Point)), [getManipulationPreferredDimension](../PresentationElement.html#getManipulationPreferredDimension()), [getMiddlePoint](../PresentationElement.html#getMiddlePoint(java.awt.Point)), [getMiddlePointX](../PresentationElement.html#getMiddlePointX()), [getMiddlePointX](../PresentationElement.html#getMiddlePointX(java.awt.Point)), [getMiddlePointY](../PresentationElement.html#getMiddlePointY()), [getMiddlePointY](../PresentationElement.html#getMiddlePointY(java.awt.Point)), [getMinimumDimension](../PresentationElement.html#getMinimumDimension()), [getModelElement](../PresentationElement.html#getModelElement()), [getModelElementsForRelationshipConnecting](../PresentationElement.html#getModelElementsForRelationshipConnecting()), [getModelElementToConnectRelationship](../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [getModelElementToMove](../PresentationElement.html#getModelElementToMove()), [getNotZoomedTolerance](../PresentationElement.html#getNotZoomedTolerance()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getParent](../PresentationElement.html#getParent()), [getParentSymbolStyleOwner](../PresentationElement.html#getParentSymbolStyleOwner()), [getPreferredBounds](../PresentationElement.html#getPreferredBounds()), [getPreferredDimension](../PresentationElement.html#getPreferredDimension()), [getPreferredDimensionForAutosize](../PresentationElement.html#getPreferredDimensionForAutosize()), [getPreferredSize](../PresentationElement.html#getPreferredSize()), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(int)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementAt](../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementCount](../PresentationElement.html#getPresentationElementCount()), [getPresentationElementIndex](../PresentationElement.html#getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getPresentationElements](../PresentationElement.html#getPresentationElements()), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)), [getPresentationElementsAt](../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getProjectImpl](../PresentationElement.html#getProjectImpl()), [getProperty](../PresentationElement.html#getProperty(java.lang.String)), [getPropertyManager](../PresentationElement.html#getPropertyManager()), [getPropertyManagerName](../PresentationElement.html#getPropertyManagerName()), [getRenderer](../PresentationElement.html#getRenderer()), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [getStyle](../PresentationElement.html#getStyle()), [getSymbolRenderer](../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getTextColor](../PresentationElement.html#getTextColor()), [getTolerance](../PresentationElement.html#getTolerance()), [getVisibility](../PresentationElement.html#getVisibility()), [getVisiblePresentationElements](../PresentationElement.html#getVisiblePresentationElements()), [handleModelDelete](../PresentationElement.html#handleModelDelete()), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [initialize](../PresentationElement.html#initialize()), [initializeAndAutosize](../PresentationElement.html#initializeAndAutosize()), [internalBeforeUpdate](../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)), [internalCreatePropertyChangeListener](../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()), [internalGetModelElementsForRelationshipConnecting](../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [internalGetModelElementToConnectRelationship](../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [internalGetSpecificFont](../PresentationElement.html#internalGetSpecificFont()), [internalGetSpecificTextColor](../PresentationElement.html#internalGetSpecificTextColor()), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalIsSuitableToConnectRelationship](../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)), [internalUpdatePresentationElement](../PresentationElement.html#internalUpdatePresentationElement()), [intersects](../PresentationElement.html#intersects(int,int,int,int)), [invalidate](../PresentationElement.html#invalidate()), [isCanChildrenChangeEdge](../PresentationElement.html#isCanChildrenChangeEdge()), [isChildVisible](../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isContentHidden](../PresentationElement.html#isContentHidden()), [isCreateElementListener](../PresentationElement.html#isCreateElementListener()), [isDetectable](../PresentationElement.html#isDetectable()), [isDisposed](../PresentationElement.html#isDisposed()), [isLayouting](../PresentationElement.html#isLayouting()), [isMovableByMoveManager](../PresentationElement.html#isMovableByMoveManager()), [isNotNull](../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isPreserveProportionsWhenGrowing](../PresentationElement.html#isPreserveProportionsWhenGrowing()), [isSelected](../PresentationElement.html#isSelected()), [isShowElementTypeAsLabel](../PresentationElement.html#isShowElementTypeAsLabel()), [isSortable](../PresentationElement.html#isSortable()), [isSuitableToConnectRelationship](../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)), [isTextEditable](../PresentationElement.html#isTextEditable()), [isUseFillColor](../PresentationElement.html#isUseFillColor()), [isUseFillColorByProperty](../PresentationElement.html#isUseFillColorByProperty()), [isUseGradientForFill](../PresentationElement.html#isUseGradientForFill()), [isVisible](../PresentationElement.html#isVisible()), [isVisibleInDiagram](../PresentationElement.html#isVisibleInDiagram()), [isVisibleOrShrunken](../PresentationElement.html#isVisibleOrShrunken()), [movePathElementsRecursively](../PresentationElement.html#movePathElementsRecursively()), [mustShowContextMenu](../PresentationElement.html#mustShowContextMenu()), [notifyCreated](../PresentationElement.html#notifyCreated()), [notifyDiagramFrameSizeChange](../PresentationElement.html#notifyDiagramFrameSizeChange()), [onChildAdd](../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onChildRemove](../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [onDiagramSurfaceSet](../PresentationElement.html#onDiagramSurfaceSet()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [onFontChange](../PresentationElement.html#onFontChange()), [onParentChange](../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [paintAdornments](../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintAdornmentsBackground](../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildren](../PresentationElement.html#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenAndAdornments](../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintChildrenBackground](../PresentationElement.html#paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [paintSelfBackground](../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)), [prepareForLineDrawing](../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)), [prepareForShadowDrawing](../PresentationElement.html#prepareForShadowDrawing(java.awt.Graphics2D)), [prepareForTextDrawing](../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)), [propertyChange](../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)), [recreateListeners](../PresentationElement.html#recreateListeners()), [recursiveAutosize](../PresentationElement.html#recursiveAutosize()), [registerInSortManager](../PresentationElement.html#registerInSortManager()), [rememberBounds](../PresentationElement.html#rememberBounds()), [rememberBounds](../PresentationElement.html#rememberBounds(java.awt.Rectangle)), [removeFromSortManager](../PresentationElement.html#removeFromSortManager()), [removeItSelfOnUpdate](../PresentationElement.html#removeItSelfOnUpdate()), [removePresentationElement](../PresentationElement.html#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sAddPresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sAddPresentationElement](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)), [selectChildrenForMoving](../PresentationElement.html#selectChildrenForMoving()), [selectObjectsForMoving](../PresentationElement.html#selectObjectsForMoving()), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setBounds](../PresentationElement.html#setBounds(int,int,int,int)), [setCreateElementListener](../PresentationElement.html#setCreateElementListener(boolean)), [setDummyResizeMode](../PresentationElement.html#setDummyResizeMode(boolean)), [setElement](../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setFillColor](../PresentationElement.html#setFillColor(java.awt.Color)), [setFont](../PresentationElement.html#setFont(java.awt.Font)), [setLayouting](../PresentationElement.html#setLayouting(boolean)), [setLineColor](../PresentationElement.html#setLineColor(java.awt.Color)), [setLineWidth](../PresentationElement.html#setLineWidth(int)), [setLoadedVisibility](../PresentationElement.html#setLoadedVisibility(boolean)), [setLocation](../PresentationElement.html#setLocation(int,int)), [setLocation](../PresentationElement.html#setLocation(java.awt.Point)), [setModelElement](../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [setNeedRecreateListeners](../PresentationElement.html#setNeedRecreateListeners(boolean)), [setPresentationElements](../PresentationElement.html#setPresentationElements(java.util.List)), [setPropertyManagerName](../PresentationElement.html#setPropertyManagerName(java.lang.String)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [setSize](../PresentationElement.html#setSize(int,int)), [setSize](../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)), [setSize](../PresentationElement.html#setSize(java.awt.Dimension)), [setTextColor](../PresentationElement.html#setTextColor(java.awt.Color)), [setTextEditable](../PresentationElement.html#setTextEditable(boolean)), [setUseFillColor](../PresentationElement.html#setUseFillColor(boolean)), [setVisible](../PresentationElement.html#setVisible(boolean)), [silentApply](../PresentationElement.html#silentApply()), [silentApply](../PresentationElement.html#silentApply(boolean)), [simpleSetBounds](../PresentationElement.html#simpleSetBounds(int,int,int,int)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Point,float)), [snapToGrid](../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)), [snapViewToGrid](../PresentationElement.html#snapViewToGrid(float)), [sortObjectsByX](../PresentationElement.html#sortObjectsByX(java.util.List)), [sortObjectsByY](../PresentationElement.html#sortObjectsByY(java.util.List)), [sRemovePresentationElement](../PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [sSetBounds](../PresentationElement.html#sSetBounds(int,int,int,int)), [sSetElement](../PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [sSetLocation](../PresentationElement.html#sSetLocation(int,int)), [sSetLocation](../PresentationElement.html#sSetLocation(java.awt.Point)), [sSetModelElement](../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)), [sSetParentForAll](../PresentationElement.html#sSetParentForAll(java.util.Collection)), [sSetPresentationElements](../PresentationElement.html#sSetPresentationElements(java.util.List)), [sSetSize](../PresentationElement.html#sSetSize(int,int)), [sSetSize](../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)), [sSetSize](../PresentationElement.html#sSetSize(java.awt.Dimension)), [sSetVisible](../PresentationElement.html#sSetVisible(boolean)), [tryToDeleteModelElementUponRemoval](../PresentationElement.html#tryToDeleteModelElementUponRemoval()), [update](../PresentationElement.html#update()), [updateAfterLoad](../PresentationElement.html#updateAfterLoad()), [updateLabelsIgnoringSuspendableLater](../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)), [updateLater](../PresentationElement.html#updateLater()), [updateModelByView](../PresentationElement.html#updateModelByView()), [updateModelByViewInternal](../PresentationElement.html#updateModelByViewInternal()), [updateViewAfterPropertyChange](../PresentationElement.html#updateViewAfterPropertyChange()), [useParentProperties](../PresentationElement.html#useParentProperties()), [useParentStyle](../PresentationElement.html#useParentStyle())`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../BaseElement.html)
`[canAdd](../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.LineJumpDrawer
`getLineWidth`
Methods inherited from interface com.nomagic.magicdraw.uml.[MDElement](../../MDElement.html)
`[getProject](../../MDElement.html#getProject())`
Methods inherited from interface com.nomagic.magicdraw.utils.[NameOwner](../../../utils/NameOwner.html)
`[getName](../../../utils/NameOwner.html#getName())`

============ FIELD DETAIL =========== 
Field Details
RECTILINEAR
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RECTILINEAR
Path line style with rectilinear (90 degrees) breakpoint corners.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.paths.PathElement.RECTILINEAR)
OBLIQUE
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OBLIQUE
Polyline path line style.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.paths.PathElement.OBLIQUE)
BEZIER
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BEZIER
Bezier path line style.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.paths.PathElement.BEZIER)
LINE_STYLE
@OpenApipublic static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> LINE_STYLE
All possible path line styles.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PathElement
public PathElement()
PathElement
public PathElement(@CheckForNull
 [PresentationElement](../PresentationElement.html) parent)
 ============ METHOD DETAIL ========== 
Method Details
getOwnStyleDelegate
public com.dassault_systemes.modeler.foundation.diagram.style.PathStylePropertyDelegate getOwnStyleDelegate()
Overrides:
`[getOwnStyleDelegate](../PresentationElement.html#getOwnStyleDelegate())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
the own style property delegate
clearSupplierTranslation
public void clearSupplierTranslation()
Clears a supplier translated flag.
clearClientTranslation
public void clearClientTranslation()
Clears a client translated flag.
translateSupplierPoint
public final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) translateSupplierPoint([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) old,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) newR)
translateClientPoint
public final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) translateClientPoint([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) old,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) newR)
getNewPointByTheLink
@CheckForNullpublic [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getNewPointByTheLink([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> oldBreaks,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> newBreaks,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) oldLocation)
hasSharedModelElement
public boolean hasSharedModelElement()
Description copied from class: `[PresentationElement](../PresentationElement.html#hasSharedModelElement())`
Returns true if `ModelElement` of this symbol can represented with other symbol.
 If `ModelElement` is not shared, it can be deleted together with symbol deleting.
Overrides:
`[hasSharedModelElement](../PresentationElement.html#hasSharedModelElement())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
true if element of this symbol can be represented with other symbol.
askDeleteDataConfirmation
public boolean askDeleteDataConfirmation()
Return true, because while deleting link view user must be prompt about deleting data
Overrides:
`[askDeleteDataConfirmation](../PresentationElement.html#askDeleteDataConfirmation())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
confirmation status -- true if asking is necessary, false otherwise
setBreakable
public void setBreakable(boolean value)
Sets a breakable flag on/off. If a flag is not set, a path cannot be broken.
 However, a path can have break points and be non-breakable.
 This means that path has fixed points that cannot be moved.
Parameters:
`value` - flag value
sSetBreakable
public void sSetBreakable(boolean value)
Sets a breakable flag on/off. If a flag is not set, a path cannot be broken.
 However, a path can have break points and be non-breakable.
 This means that path has fixed points that cannot be moved.
Parameters:
`value` - flag value
isBreakable
public boolean isBreakable()
Shows whether a path is breakable.
Returns:
true if a path can be broken
isFixed
public boolean isFixed()
If a path tied to its supplier and client (cannot be reconnected)
Returns:
true, if it can be reconnected, else false
getBreakPoints
@OpenApipublic final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> getBreakPoints()
Returns break points of the path.
 The order of break points is from supplier to the client path's end.
 Use PresentationElementsManager to change the break points for the path.
Returns:
break points list.Points in the list are not cloned, so do not modify them directly.
 The List is unmodifiable.
See Also:
[`PresentationElementsManager.changePathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement, java.util.List)`](../../../openapi/uml/PresentationElementsManager.html#changePathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.util.List))
getAllBreakPoints
@OpenApipublic final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> getAllBreakPoints()
Returns a break points list with added supplier and client end point in the list as well.
 Use PresentationElementsManager to change the break points for the path.
Returns:
supplier point + break points + client point. Points in the list are not cloned,
 so do not modify them directly. The List is modifiable.
See Also:
[`PresentationElementsManager.changePathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement, java.util.List)`](../../../openapi/uml/PresentationElementsManager.html#changePathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.util.List))
setBreakPoints
public final void setBreakPoints([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> vct)
Sets break point vector.
Parameters:
`vct` - new break point vector.
sClearBreakPoints
public final void sClearBreakPoints()
Clear break points list.
sSetBreakPoints
public final void sSetBreakPoints([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> vct)
Only sets break point vector.
Parameters:
`vct` - new break point vector.
sAddBreakPoint
public final void sAddBreakPoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)
Adds new break point.
Parameters:
`pt` - point to be added.
sSetBreakPoint
public final void sSetBreakPoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 int pos)
Sets break point at the given position.
Parameters:
`pt` - point to be set
`pos` - position where it must be set
needsToMoveOtherEnd
public boolean needsToMoveOtherEnd()
Returns:
true, if one end of links changed bounds and move link must be called for both ends.
getBreakPoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getBreakPoint(int pos)
Returns break point with given index.
Parameters:
`pos` - position where point resides.
Returns:
point at position pos.
getBreakPointCount
public int getBreakPointCount()
returns size of break point vector
Returns:
break point count
setBounds
public void setBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
Moves link to new location.
Specified by:
`[setBounds](../PresentationElement.html#setBounds(java.awt.Rectangle))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`r` - new location of a path
simpleSetBounds
public void simpleSetBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
calls break point vector changed method.
Overrides:
`[simpleSetBounds](../PresentationElement.html#simpleSetBounds(java.awt.Rectangle))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`r` - new bounding rectangle.
isToSelf
public boolean isToSelf()
Returns:
true if this path is to self (client and supplier are the same).
isAlwaysToSelf
public boolean isAlwaysToSelf()
sSetBounds
public void sSetBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
Moves path to new location.
Specified by:
`[sSetBounds](../PresentationElement.html#sSetBounds(java.awt.Rectangle))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`r` - new location of a path
removeUnnecessaryBreakPoints
public void removeUnnecessaryBreakPoints()
Removes unnecessary points from break point vector.
 Checks if break point vector has useless points (covered by shape or invisible).
 Does not do anything if a path cannot be breakable.
 If it has, remove them.
getPathIcon
@CheckForNullpublic com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon getPathIcon()
dynamicPathIcon
@CheckForNullpublic com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon dynamicPathIcon()
dynamicPathIcon
public com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon dynamicPathIcon(@CheckForNull
 com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon pathIcon)
getCustomStereotypeIcon
@CheckForNullpublic static com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon getCustomStereotypeIcon(@CheckForNull
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
draw
public void draw([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplierPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) clientPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> breakPoints)
Draws link from given point pt1 through break points
 to given point pt2.
Parameters:
`g` - graphics
`supplierPoint` - first point
`clientPoint` - second point
`breakPoints` - points between supplier and client points, in that order
internalGetBoundsShape
@CheckForNullpublic [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) internalGetBoundsShape([ConverterToShape](../ConverterToShape.html) converterToShape)
Overrides:
`[internalGetBoundsShape](../PresentationElement.html#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape))` in class `[PresentationElement](../PresentationElement.html)`
setLineJumpPlace
public void setLineJumpPlace(@CheckForNull
 com.nomagic.magicdraw.uml.symbols.LineJumpPlace lineJumpPlace)
Sets line jump place of the path element.
 
**NOTE: Only `LineJumpManager` can set jump place of the link. Since `LineJumpManager`
 will reset line jump place on every repaint of a diagram then other invocations of the method will not have
 an effect.**
Specified by:
`setLineJumpPlace` in interface `com.nomagic.magicdraw.uml.symbols.LineJumpDrawer`
Parameters:
`lineJumpPlace` - new line jump place.
registerLineJumpInfos
public void registerLineJumpInfos(int pathIndex,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) segmentStartPoint,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.uml.symbols.LineJumpInfo> lineJumps)
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.LineJumpDrawer`
Registers line jump info for specified path and specified segmentStartPoint in the path.
 Index of the path coincident with the index of the path which was returned by `LineJumpDrawer.getPaths()`
 method.
Specified by:
`registerLineJumpInfos` in interface `com.nomagic.magicdraw.uml.symbols.LineJumpDrawer`
Parameters:
`pathIndex` - index of the path.
`segmentStartPoint` - start point of the segment.
`lineJumps` - list of information about line jumps.
clearRegisteredLineJumpInfos
public void clearRegisteredLineJumpInfos()
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.LineJumpDrawer`
Clears all registered LineJumpInfos.
Specified by:
`clearRegisteredLineJumpInfos` in interface `com.nomagic.magicdraw.uml.symbols.LineJumpDrawer`
registerLineJumpStartAngle
public void registerLineJumpStartAngle(int pathIndex,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point,
 double lineJumpStartAngle)
Description copied from interface: `com.nomagic.magicdraw.uml.symbols.LineJumpDrawer`
Registers start angle for the specified path and specified start point of the path segment.
Specified by:
`registerLineJumpStartAngle` in interface `com.nomagic.magicdraw.uml.symbols.LineJumpDrawer`
Parameters:
`pathIndex` - index of the path.
`point` - start point of the segment.
`lineJumpStartAngle` - start angle of the line jump.
getLineJumpStartAngle
public double getLineJumpStartAngle([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point)
addLineJumps
public void addLineJumps([GeneralPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html) path,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) segmentStartPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) startPoint,
 @CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) endPoint)
Adds line jumps to the specified path.
Specified by:
`addLineJumps` in interface `com.nomagic.magicdraw.uml.symbols.LineJumpDrawer`
Parameters:
`path` - a path object.
`segmentStartPoint` - segment start point.
`startPoint` - start point from which to start adding the line jumps.
`endPoint` - point until which line jumps should be added.
isDrawLineJumps
public boolean isDrawLineJumps()
Returns true if the path element wants to draw line jumps.
Specified by:
`isDrawLineJumps` in interface `com.nomagic.magicdraw.uml.symbols.LineJumpDrawer`
Returns:
true if line jumps should be drawn for the path element.
getPaths
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)>> getPaths()
Returns only one path which consist of actual supplier draw point, break points of the path element
 and actual client draw point.
Specified by:
`getPaths` in interface `com.nomagic.magicdraw.uml.symbols.LineJumpDrawer`
Returns:
paths.
setSupplierPoint
public void setSupplierPoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)
Sets first point.
 Sets new location for text boxes if a point is changed, text boxes must be moved too.
Parameters:
`pt` - new 1st point
sSetSupplierPoint
public void sSetSupplierPoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)
Sets supplier connection point.
Parameters:
`pt` - new supplier point.
sSetClientPoint
public void sSetClientPoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)
Sets client connection Point.
Parameters:
`pt` - new client point.
setClientPoint
public void setClientPoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)
Sets client point.
Parameters:
`pt` - new client point.
breakPointsChanged
public final void breakPointsChanged([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> oldPoints,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> newPoints)
Moves all connection point for the links that are attached to this
 link middle point.
Parameters:
`oldPoints` - old breakpoint vector.
`newPoints` - new breakpoint vector.
notifyRepaintManager
public void notifyRepaintManager(boolean boundsChanged)
Description copied from class: `[PresentationElement](../PresentationElement.html#notifyRepaintManager(boolean))`
Notifies the repaint manager about changes in bounds.
Overrides:
`[notifyRepaintManager](../PresentationElement.html#notifyRepaintManager(boolean))` in class `[PresentationElement](../PresentationElement.html)`
notifyRepaintManager
protected final void notifyRepaintManager([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> oldBreakpoints,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> newBreakpoints)
notifyBreakPointsChanged
public void notifyBreakPointsChanged([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> oldPoints,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> newPoints)
Notifies about break point vector changes
Parameters:
`oldPoints` - old points
`newPoints` - new points
getNearestLinkPart
public final [Line](../../../../awt/Line.html) getNearestLinkPart(int x,
 int y)
Returns the nearest link part to specified point.
Parameters:
`x` - x of point
`y` - y of point
Returns:
line
removeBreakPoints
public boolean removeBreakPoints()
Removes break points if they do not really break the path (a path looks like without break points but really has them).
 Does nothing if a path is not breakable.
getSupplierPoint
@OpenApipublic final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getSupplierPoint()
Returns point where path connects supplier end's element.
Returns:
supplier connection point. This method returns not cloned point, so do not modify it directly.
getClientPoint
@OpenApipublic final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getClientPoint()
Returns point where path connects client end's element.
Returns:
client point. This method returns not cloned point, so do not modify it directly.
getClientDrawPoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getClientDrawPoint()
Returns point where path drawing should start
Returns:
point
getActualClientDrawPoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getActualClientDrawPoint()
Returns actual client side draw point.
Returns:
actual client draw point.
getActualSupplierDrawPoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getActualSupplierDrawPoint()
Returns actual supplier side draw point.
Returns:
actual supplier draw point.
getSupplierDrawPoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getSupplierDrawPoint()
Returns point where path drawing should start
Returns:
point
getNextPoint
public final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getNextPoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)
Returns next point to a given one. If given point does not belong to the link, returns parameter point.
Parameters:
`pt` - point for which next point is necessary
Returns:
next point(not cloned)
getPreviousPoint
public final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getPreviousPoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)
Returns previous point to given one. If given point does not belong to the link, returns
 parameter point.
Parameters:
`pt` - point for which previous point is necessary
Returns:
previous point(not cloned)
getNearestPoint
public final [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getNearestPoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)
Returns first break point or client point if arg is supplier point.
 Or returns last break point or client point if arg is client point.
Parameters:
`pt` - given point
Returns:
nearest point(not cloned)
sSetClient
public void sSetClient(@CheckForNull
 [PresentationElement](../PresentationElement.html) symbol)
Sets client for this link.
Parameters:
`symbol` - new client.
sSetSupplier
public void sSetSupplier(@CheckForNull
 [PresentationElement](../PresentationElement.html) symbol)
Sets supplier for this link.
Parameters:
`symbol` - new supplier.
setSupplier
public void setSupplier([PresentationElement](../PresentationElement.html) shape)
Sets supplier end for link.
 Removes this link from old shape.
 Inserts this link to new shape.
 Method also sets supplier point to the middle point of shape.
Parameters:
`shape` - new supplier.
getClient
@OpenApipublic [PresentationElement](../PresentationElement.html) getClient()
Returns client of the path.
Returns:
client element.
getSupplier
@OpenApipublic [PresentationElement](../PresentationElement.html) getSupplier()
Returns supplier of the path.
Returns:
supplier end element.
getNextEnd
public [PresentationElement](../PresentationElement.html) getNextEnd([PresentationElement](../PresentationElement.html) obj)
Returns other than given end.
 If given end is supplier method returns client of this path.
 If given end is not supplier method returns supplier of this path.
Parameters:
`obj` - given end
Returns:
other opposite end
movePathElement
protected void movePathElement([PathElement](PathElement.html) link,
 @CheckForNull
 [PathConnector](PathConnector.html) requestor)
Moves link.
 Link can connect more links ( such as note anchors in UML class diagrams ).
 After link was moved positions of connected links must be updated.
 Method checks if moving link supplier is this link recalculates supplier point moving link,
 otherwise it calculates client point of moving link.
 Point is calculated to middle point of this link.
Specified by:
`[movePathElement](PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector))` in class `[PathConnector](PathConnector.html)`
Parameters:
`link` - link to move.
`requestor` - requestor
optimizeLoops
public void optimizeLoops()
Removes loops from paths for example:
 path
 |
 ----------+
 | |
 ------
 
 will be changed to
 |
 -----
clone
public [PathElement](PathElement.html) clone()
Specified by:
`[clone](../../BaseElement.html#clone())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`[clone](PathConnector.html#clone())` in class `[PathConnector](PathConnector.html)`
coversPoint
public boolean coversPoint(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Checks if object covers provided point
Specified by:
`[coversPoint](../PresentationElement.html#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[PresentationElement](../PresentationElement.html)`
Returns:
true if object covers this point
intersects
public final boolean intersects(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Check if any line between breakpoints intersect with given points of rectangle
Specified by:
`[intersects](../PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))` in class `[PresentationElement](../PresentationElement.html)`
Returns:
true if object and rectangle intersects
intersectsInternal
public boolean intersectsInternal(int x,
 int y,
 int width,
 int height)
Check intersection with given rectangle. Intersection is counted by getting index of segment in path.
Parameters:
`x` - top left x point.
`y` - top left y point.
`width` - width of rectangle.
`height` - height of rectangle.
Returns:
true if rectangle intersect with any line of path.
isBezierIntersects
public boolean isBezierIntersects(int x,
 int y,
 int width,
 int height)
Check if it is bezier path intersection with rectangle.
Parameters:
`x` - top left x point of rectangle.
`y` - top left y point of rectangle.
`width` - width of rectangle.
`height` - height of rectangle.
Returns:
true if bezier path intersects with rectangle.
getIndexOfCoveredPathInternal
public int getIndexOfCoveredPathInternal(int x,
 int y,
 int width,
 int height)
This method is used to get segment of path with witch given rectangle has intersection. It will
 be returned index starting from 1 of segment. This segment is counted using all breakpoints
 (including client and supplier point). If anybody needs end points of segments, you must take
 all breakpoints and take point of return index minus 1 and point of segment's index. If there
 is no intersection, this method return -1.
 For example:
 this method returns value 2.
 segmentIndex = 2;
 Point start and end point of this segment will be:
 Point startPoint = getAllBreakPoints().get(segmentIndex-1);
 Point endPoint = getAllBreakPoints().get(segmentIndex);
Parameters:
`x` - top left x point of rectangle.
`y` - top left y point of rectangle.
`width` - width of rectangle.
`height` - height of rectangle.
Returns:
index of segment in path with witch intersect given rectangle.
getIndexOfCoveredPath
public final int getIndexOfCoveredPath(int x,
 int y)
This method is used to get segment of path with witch given point has intersection. It will
 be returned index starting from 1 of segment. This segment is counted using all breakpoints
 (including client and supplier point). If anybody needs end points of segments, you must take
 all breakpoints and take point of return index minus 1 and point of segment's index. If there
 is no intersection, this method return -1. If renderer is set for path element, intersection
 will be counted depending on this renderer.
 For example:
 this method returns value 2.
 segmentIndex = 2;
 Point start and end point of this segment will be:
 Point startPoint = getAllBreakPoints().get(segmentIndex-1);
 Point endPoint = getAllBreakPoints().get(segmentIndex);
Parameters:
`x` - point x value.
`y` - point y value.
Returns:
index of segment of path which intersects with the given point.
getNewBreakPointIndex
public int getNewBreakPointIndex([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> brk)
Find the nearest breakpoints for new one and
 calculate the position of the new breakpoint in breakpoint vector.
 Used for new breakpoint calculation for Bézier curve.
Parameters:
`point` - the new point.
`brk` - the breakpoint Vector.
Returns:
position in that the new point must be inserted in a breakpoint vector.
isConnectable
@OpenApipublic final boolean isConnectable(@CheckForNull
 [PresentationElement](../PresentationElement.html) supplier,
 @CheckForNull
 [PresentationElement](../PresentationElement.html) client)
Checks if this path can connect given two elements.
Parameters:
`supplier` - candidate for path's supplier.
`client` - candidate for path's client.
Returns:
true, if path can connect given elements.
isConnectable
public final boolean isConnectable(@CheckForNull
 [PresentationElement](../PresentationElement.html) supplier,
 @CheckForNull
 [PresentationElement](../PresentationElement.html) client,
 @CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> options)
Checks if this path can connect given two elements.
Parameters:
`supplier` - candidate for path's supplier.
`client` - candidate for path's client.
`options` - options
Returns:
true, if path can connect given elements.
getMiddlePoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getMiddlePoint()
Calculates and returns middle point of link.
 For this link it is average between supplier's and client's points.
Overrides:
`[getMiddlePoint](../PresentationElement.html#getMiddlePoint())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
middle point.
getPointOnPath
@OpenApipublic [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getPointOnPath([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplierPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) clientPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> breakpoints,
 double coefficient)
Parameters:
`supplierPoint` - supplier end point
`clientPoint` - client end point
`breakpoints` - list of breakpoints between supplier and client in that order
`coefficient` - ratio between 0 and 1 describing position relative to the path length.
 Provide 0.5 for middle point.
Returns:
point on path
dispose
public void dispose()
Disconnect this link from shapes.
Specified by:
`[dispose](../../BaseElement.html#dispose())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`[dispose](PathConnector.html#dispose())` in class `[PathConnector](PathConnector.html)`
atInsert
public void atInsert()
Inserts ends of link into shapes.
Specified by:
`[atInsert](../../BaseElement.html#atInsert())` in interface `[BaseElement](../../BaseElement.html)`
Overrides:
`[atInsert](../PresentationElement.html#atInsert())` in class `[PresentationElement](../PresentationElement.html)`
addConnectedPathElement
public boolean addConnectedPathElement([PathElement](PathElement.html) link)
Method to add sub link to this link.
 If link is note anchor it will be added to this link.
 If link is not note anchor, it will be added to generalization tree.
Overrides:
`[addConnectedPathElement](PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))` in class `[PathConnector](PathConnector.html)`
Parameters:
`link` - link to be added.
Returns:
true if an element was added
getBounds
public final [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBounds()
Calculates bounds of this link.
 Returns minimal rectangle in which link can fit.
Overrides:
`[getBounds](../PresentationElement.html#getBounds())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
bounds of this link.
See Also:
`PresentationElementsManager.reshapeShapeElement`
getNotCopyBounds
public final [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getNotCopyBounds()
Description copied from class: `[PresentationElement](../PresentationElement.html#getNotCopyBounds())`
get not copy bounds of object throws NoRectangleDefinedException
Overrides:
`[getNotCopyBounds](../PresentationElement.html#getNotCopyBounds())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
rectangle of bounds
setCachedPathBounds
protected void setCachedPathBounds(@CheckForNull
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
calculatePathBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) calculatePathBounds([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplier,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) client,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> breaks)
accept
@OpenApipublic void accept([Visitor](../../Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts a visitor, and calls method "visit<class name>(this)" of a visitor.
 See "Visitor" pattern for more details.
Specified by:
`[accept](../../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../../MDElement.html)`
Overrides:
`[accept](PathConnector.html#accept(com.nomagic.magicdraw.uml.Visitor))` in class `[PathConnector](PathConnector.html)`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
setRectilinear
public void setRectilinear()
Sets link rectilinear property value.
isRectilinear
public boolean isRectilinear()
Returns:
true if link path style is rectilinear.
isOblique
public boolean isOblique()
Returns:
true if link path style is oblique.
makeRectilinear
public void makeRectilinear()
Makes link rectilinear.
makeRectilinear
public void makeRectilinear(boolean notify)
Makes link rectilinear.
Parameters:
`notify` - notify about this change
removeRedundantBreakPoints
public void removeRedundantBreakPoints([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> vct)
Removes redundant breakpoints from link.
 Remove breakpoints only from rectilinear link.
Parameters:
`vct` - points
isVertical
public boolean isVertical()
Indicates if path element is drawn in the diagram which has vertical orientation.
Returns:
true if diagram is vertical, false otherwise.
removeBreaks
public void removeBreaks([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> points)
Removes all break points if they are covered by client or client bounds.
Parameters:
`points` - points
swapEnds
public void swapEnds()
Swaps ends of the link
setClient
public void setClient([PresentationElement](../PresentationElement.html) shape)
Sets client for this link.
 Changes parent object to the parent of client.
 Client's parent will always contain incoming links.
Parameters:
`shape` - shape to check
moveLinkToClientParent
public void moveLinkToClientParent(boolean simpleAdd)
internalSnapToGrid
protected void internalSnapToGrid(float step)
Overrides:
`[internalSnapToGrid](../PresentationElement.html#internalSnapToGrid(float))` in class `[PresentationElement](../PresentationElement.html)`
isSnapToGrid
protected boolean isSnapToGrid()
Overrides:
`[isSnapToGrid](../PresentationElement.html#isSnapToGrid())` in class `[PresentationElement](../PresentationElement.html)`
canChangeSupplier
public boolean canChangeSupplier()
Returns:
true, if view can change supplier.
canChangeClient
public boolean canChangeClient()
Returns:
true, if view can change client
canClearBreakPoints
public boolean canClearBreakPoints()
Returns:
true if link can be modified (all break points can be removed):
canChangeLineStyle
public boolean canChangeLineStyle()
Returns:
true if this link can change line style.
internalApplyProperties
public void internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)
Applies properties
Overrides:
`[internalApplyProperties](../PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`changer` - new properties
draw
public void draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
abstract method for drawing ViewObject object
 used to draw object on graphics
Overrides:
`[draw](../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`context` - Graphics on which object should be drawn
getIntersection
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getIntersection(int x,
 int y,
 @CheckForNull
 [PathElement](PathElement.html) path)
Overrides:
`[getIntersection](../PresentationElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement))` in class `[PresentationElement](../PresentationElement.html)`
useOtherExistingElement
@CheckForNullpublic com.nomagic.utils.Pair<com.dassault_systemes.modeler.foundation.model.ModelElement,[Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<com.dassault_systemes.modeler.foundation.model.ModelElement>> useOtherExistingElement()
Finds and returns other model element which is semantically equivalent to this path model element.
 Found element can be modified.
 This method is invoked during new PathElement creation and purpose of it is to reuse existing model elements instead of creating new ones.
Returns:
element
getBezierPath
public [GeneralPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html) getBezierPath()
Calculates path for bezier curve drawing.
Returns:
bezier path
isBezier
public boolean isBezier()
Returns:
true if LINK_LINE_STYLE property value equals to BEZIER.
isLinkLineStyleDefined
public boolean isLinkLineStyleDefined()
getLinkLineStyle
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLinkLineStyle()
Returns:
LINK_LINE_STYLE property value
sSetLinkLineStyle
public void sSetLinkLineStyle([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) style)
Change value of LINK_LINE_STYLE property.
Parameters:
`style` - the line style.
setLinkLineStyle
public void setLinkLineStyle([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) style)
sets LINK_LINE_STYLE property value.
Parameters:
`style` - the line style.
internalSilentApply
public void internalSilentApply()
Description copied from class: `[PresentationElement](../PresentationElement.html#internalSilentApply())`
Silently applies all properties after initialization
Overrides:
`[internalSilentApply](../PresentationElement.html#internalSilentApply())` in class `[PresentationElement](../PresentationElement.html)`
handleRemoveBreaksAction
public com.dassault_systemes.modeler.foundation.editing.Command handleRemoveBreaksAction()
nextStyle
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) nextStyle()
Returns:
link style for TOGGLE LINK STYLE command.
getBezierPath
public [GeneralPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html) getBezierPath([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> points)
Calculates path from breakpoints for bezier curve drawing.
Parameters:
`points` - points
Returns:
path
prepareForLineDrawing
public boolean prepareForLineDrawing([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 boolean line)
Prepares graphics for line drawing.
 Calls super prepareForLineDrawing and sets stroke.
Parameters:
`g` - graphics
`line` - true if for line, false if for adornments also
Returns:
stroke
applyStrokeForLineDrawing
public static void applyStrokeForLineDrawing([PresentationElement](../PresentationElement.html) pathElement,
 [Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 boolean line,
 [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) stroke)
internalGetPresentationElementStroke
public [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) internalGetPresentationElementStroke(boolean line,
 int width)
This method must be overridden, if you need to use DASHED_STROKE or another one.
Parameters:
`line` - true if for line, false if for adornments also
`width` - width
Returns:
the stroke for line drawing ( by default SOLID_STROKE).
internalGetPresentationElementStroke
protected [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) internalGetPresentationElementStroke(boolean line,
 int lineStyle,
 int width)
getBoundsToRepaint
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBoundsToRepaint()
 throws [NoRectangleDefinedException](../NoRectangleDefinedException.html)
Description copied from class: `[PresentationElement](../PresentationElement.html#getBoundsToRepaint())`
Return bounds of the symbol that must be repainted. throws NoRectangleDefinedException
Overrides:
`[getBoundsToRepaint](../PresentationElement.html#getBoundsToRepaint())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
rectangle of bounds
Throws:
`[NoRectangleDefinedException](../NoRectangleDefinedException.html)`
createFillStrategy
public com.nomagic.magicdraw.uml.symbols.FillStrategy createFillStrategy()
Overrides:
`[createFillStrategy](../PresentationElement.html#createFillStrategy())` in class `[PresentationElement](../PresentationElement.html)`
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
paintSelf
public void paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
Specified by:
`[paintSelf](../PresentationElement.html#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))` in class `[PresentationElement](../PresentationElement.html)`
getPathPainter
public com.nomagic.magicdraw.uml.symbols.paths.painters.PathPainter<[PathElement](PathElement.html)> getPathPainter()
setPathPainter
protected final void setPathPainter(com.nomagic.magicdraw.uml.symbols.paths.painters.PathPainter pathPainter)
getSupplierConnectionType
public int getSupplierConnectionType()
getClientConnectionType
public int getClientConnectionType()
getDefaultParentForData
@CheckForNullpublic [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getDefaultParentForData()
Presentation element could suggest parent, which would be more acceptable, than adding to the client
 If returning null, general mechanism will work
Returns:
parent for data
hasClientPoint
protected boolean hasClientPoint()
Check if client point is already not null
Returns:
true if client point is set
hasSupplierPoint
protected boolean hasSupplierPoint()
Check if supplier point is already not null
Returns:
true if supplier point is set
isRounded
public boolean isRounded()
Returns value of the "Is Rounded" path symbol property.
Returns:
value of the "Is Rounded" property.
setRounded
public void setRounded(boolean rounded)
Sets value of the "Is Rounded" path symbol property.
Parameters:
`rounded` - - value of the "Is Rounded" property.
sSetRounded
public void sSetRounded(boolean rounded)
Sets value of the "Is Rounded" path symbol property.
Parameters:
`rounded` - - value of the "Is Rounded" property.
isUseFlowLayoutLogic
public boolean isUseFlowLayoutLogic()
Indicates if smart path/shape edit should be used in this diagram.
Returns:
true if smart symbol editing should be used, false otherwise.
isSmartLayoutNeeded
public boolean isSmartLayoutNeeded()
Returns smart layout needed flag.
Returns:
value of smart layout needed flag.
setSmartLayoutNeeded
public void setSmartLayoutNeeded(boolean smartLayoutNeeded)
Sets smart layout needed flag.
Parameters:
`smartLayoutNeeded` - - smart layout needed flag value.
resetCache
protected void resetCache()
cacheValues
protected void cacheValues([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) cachedActualSupplierDrawPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) cachedActualClientDrawPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) cacheSupplierDrawPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) cacheClientDrawPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> cacheBreakPoints)
cacheActualDrawPoints
protected void cacheActualDrawPoints([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplierDrawPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) clientDrawPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> breakPoints)
getCachedActualClientDrawPoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getCachedActualClientDrawPoint()
getCachedActualSupplierDrawPoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getCachedActualSupplierDrawPoint()
resizeParent
public void resizeParent()
Do nothing, because path does not affect parent size
Overrides:
`[resizeParent](../PresentationElement.html#resizeParent())` in class `[PresentationElement](../PresentationElement.html)`
getCustomSupplierPoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getCustomSupplierPoint()
setCustomSupplierPoint
public void setCustomSupplierPoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point)
getCustomClientPoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getCustomClientPoint()
setCustomClientPoint
public void setCustomClientPoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point)
preDisposeOnUpdate
protected boolean preDisposeOnUpdate()
Description copied from class: `[PresentationElement](../PresentationElement.html#preDisposeOnUpdate())`
Validate symbol against model and try to fix it before actual symbol update. If symbol is not valid and can not be fixed,
 request symbol dispose by returning true.
 Check if symbol should be disposed, because model does not correspond to symbol.
 This may happen for example if path supplier or client in model is changed, but path still is connected to symbols of old ends.
 Method also can fix symbol if possible - for example reconnect path to other symbols in diagram and etc.
Overrides:
`[preDisposeOnUpdate](../PresentationElement.html#preDisposeOnUpdate())` in class `[PresentationElement](../PresentationElement.html)`
Returns:
true if symbol must be disposed
createSmartListenerConfig
protected void createSmartListenerConfig([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)
Overrides:
`[createSmartListenerConfig](PathConnector.html#createSmartListenerConfig(java.util.List))` in class `[PathConnector](PathConnector.html)`
internalMovedAsToSelf
public void internalMovedAsToSelf(int dx,
 int dy)
This is an internal method to notify a path that it was moved by connecting shape as the path "to self"
Parameters:
`dx` - delta x
`dy` - delta y
sSetParent
public void sSetParent(@CheckForNull
 [PresentationElement](../PresentationElement.html) parent)
Description copied from class: `[PresentationElement](../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Sets parent for this view.
 For adding symbols to other symbols use
 [`PresentationElement.addPresentationElement(PresentationElement)`](../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)) or
 [`PresentationElement.sAddPresentationElement(PresentationElement)`](../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))}
Overrides:
`[sSetParent](../PresentationElement.html#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[PresentationElement](../PresentationElement.html)`
Parameters:
`parent` - parent view
hasManipulator
public boolean hasManipulator()
Description copied from class: `[PresentationElement](../PresentationElement.html#hasManipulator())`
Returns true, if view has manipulator (is selectable)
Overrides:
`[hasManipulator](../PresentationElement.html#hasManipulator())` in class `[PresentationElement](../PresentationElement.html)`
getSuspendShapeAutoResizeMode
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSuspendShapeAutoResizeMode()
Specified by:
`getSuspendShapeAutoResizeMode` in interface `com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider`
sSetSuspendShapeAutoResizeMode
public void sSetSuspendShapeAutoResizeMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
setSuspendShapeAutoResizeMode
public void setSuspendShapeAutoResizeMode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mode)
findOwnerForElement
@CheckForNullpublic final com.dassault_systemes.modeler.foundation.model.ModelElement findOwnerForElement([PresentationElement](../PresentationElement.html) newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)
Overrides:
`[findOwnerForElement](../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext))` in class `[PresentationElement](../PresentationElement.html)`
findOwnerForElement
@CheckForNullpublic com.dassault_systemes.modeler.foundation.model.ModelElement findOwnerForElement([PresentationElement](../PresentationElement.html) newParent,
 [PresentationElement](../PresentationElement.html) client,
 [PresentationElement](../PresentationElement.html) supplier,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)
connectModelElement
public void connectModelElement(com.nomagic.magicdraw.uml.symbols.paths.ConnectModelElementParticipant participant)
Connects `ModelElement` of this path to related elements of a given client and supplier
Parameters:
`participant` - participant of this operation

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.paths</a></div>
<h1 class="title" title="Class PathElement">Class PathElement</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.paths.PathElement</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code>com.nomagic.magicdraw.uml.symbols.LineJumpDrawer</code>, <code>com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider</code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code>com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView</code>, <code><a href="ContainmentLinkView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ContainmentLinkView</a></code>, <code><a href="LinkAttributeView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">LinkAttributeView</a></code>, <code><a href="NoteAnchorView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">NoteAnchorView</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">PathElement</span>
<span class="extends-implements">extends <a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a>
implements com.nomagic.magicdraw.uml.symbols.LineJumpDrawer, com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider</span></div>
<div class="block">Base class for all path kinds of symbols.
 Path is a symbol that connects two other symbols as a graphical path.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BEZIER">BEZIER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Bezier path line style.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LINE_STYLE">LINE_STYLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">All possible path line styles.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OBLIQUE">OBLIQUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Polyline path line style.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RECTILINEAR">RECTILINEAR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Path line style with rectilinear (90 degrees) breakpoint corners.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Fields inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="PathConnector.html#showsProxy">showsProxy</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PathElement</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PathElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addConnectedPathElement</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> link)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method to add sub link to this link.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addLineJumps(java.awt.geom.GeneralPath,java.awt.Point,java.awt.Point,java.awt.Point)">addLineJumps</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html" title="class or interface in java.awt.geom">GeneralPath</a> path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> segmentStartPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> startPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> endPoint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds line jumps to the specified path.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#applyStrokeForLineDrawing(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Graphics2D,boolean,java.awt.BasicStroke)">applyStrokeForLineDrawing</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pathElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 boolean line,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a> stroke)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#askDeleteDataConfirmation()">askDeleteDataConfirmation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return true, because while deleting link view user must be prompt about deleting data</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#atInsert()">atInsert</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Inserts ends of link into shapes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#breakPointsChanged(java.util.List,java.util.List)">breakPointsChanged</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; oldPoints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; newPoints)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves all connection point for the links that are attached to this
 link middle point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#cacheActualDrawPoints(java.awt.Point,java.awt.Point,java.util.List)">cacheActualDrawPoints</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplierDrawPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> clientDrawPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; breakPoints)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#cacheValues(java.awt.Point,java.awt.Point,java.awt.Point,java.awt.Point,java.util.List)">cacheValues</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> cachedActualSupplierDrawPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> cachedActualClientDrawPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> cacheSupplierDrawPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> cacheClientDrawPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; cacheBreakPoints)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculatePathBounds(java.awt.Point,java.awt.Point,java.util.List)">calculatePathBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> client,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; breaks)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeClient()">canChangeClient</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeLineStyle()">canChangeLineStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeSupplier()">canChangeSupplier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canClearBreakPoints()">canClearBreakPoints</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearClientTranslation()">clearClientTranslation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clears a client translated flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearRegisteredLineJumpInfos()">clearRegisteredLineJumpInfos</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clears all registered LineJumpInfos.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearSupplierTranslation()">clearSupplierTranslation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clears a supplier translated flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#connectModelElement(com.nomagic.magicdraw.uml.symbols.paths.ConnectModelElementParticipant)">connectModelElement</a><wbr/>(com.nomagic.magicdraw.uml.symbols.paths.ConnectModelElementParticipant participant)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Connects <code>ModelElement</code> of this path to related elements of a given client and supplier</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">coversPoint</a><wbr/>(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if object covers provided point</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.FillStrategy</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createFillStrategy()">createFillStrategy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Disconnect this link from shapes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">abstract method for drawing ViewObject object
 used to draw object on graphics</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#draw(java.awt.Graphics2D,java.awt.Point,java.awt.Point,java.util.List)">draw</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplierPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> clientPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; breakPoints)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Draws link from given point pt1 through break points
 to given point pt2.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicPathIcon()">dynamicPathIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicPathIcon(com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon)">dynamicPathIcon</a><wbr/>(com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon pathIcon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final com.dassault_systemes.modeler.foundation.model.ModelElement</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.model.ModelElement</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> newParent,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActualClientDrawPoint()">getActualClientDrawPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns actual client side draw point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActualSupplierDrawPoint()">getActualSupplierDrawPoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns actual supplier side draw point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllBreakPoints()">getAllBreakPoints</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a break points list with added supplier and client end point in the list as well.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html" title="class or interface in java.awt.geom">GeneralPath</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBezierPath()">getBezierPath</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates path for bezier curve drawing.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html" title="class or interface in java.awt.geom">GeneralPath</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBezierPath(java.util.List)">getBezierPath</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; points)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates path from breakpoints for bezier curve drawing.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBounds()">getBounds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates bounds of this link.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBoundsToRepaint()">getBoundsToRepaint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return bounds of the symbol that must be repainted.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBreakPoint(int)">getBreakPoint</a><wbr/>(int pos)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns break point with given index.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBreakPointCount()">getBreakPointCount</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">returns size of break point vector</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBreakPoints()">getBreakPoints</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns break points of the path.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCachedActualClientDrawPoint()">getCachedActualClientDrawPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCachedActualSupplierDrawPoint()">getCachedActualSupplierDrawPoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClient()">getClient</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns client of the path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClientConnectionType()">getClientConnectionType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClientDrawPoint()">getClientDrawPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns point where path drawing should start</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClientPoint()">getClientPoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns point where path connects client end's element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomClientPoint()">getCustomClientPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomStereotypeIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCustomStereotypeIcon</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomSupplierPoint()">getCustomSupplierPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultParentForData()">getDefaultParentForData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Presentation element could suggest parent, which would be more acceptable, than adding to the client
 If returning null, general mechanism will work</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIndexOfCoveredPath(int,int)">getIndexOfCoveredPath</a><wbr/>(int x,
 int y)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method is used to get segment of path with witch given point has intersection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIndexOfCoveredPathInternal(int,int,int,int)">getIndexOfCoveredPathInternal</a><wbr/>(int x,
 int y,
 int width,
 int height)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method is used to get segment of path with witch given rectangle has intersection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a><wbr/>(int x,
 int y,
 <a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLineJumpStartAngle(java.awt.Point)">getLineJumpStartAngle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLinkLineStyle()">getLinkLineStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePoint()">getMiddlePoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates and returns middle point of link.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../../../../awt/Line.html" title="class in com.nomagic.awt">Line</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNearestLinkPart(int,int)">getNearestLinkPart</a><wbr/>(int x,
 int y)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the nearest link part to specified point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNearestPoint(java.awt.Point)">getNearestPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns first break point or client point if arg is supplier point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNewBreakPointIndex(java.awt.Point,java.util.List)">getNewBreakPointIndex</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; brk)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Find the nearest breakpoints for new one and
 calculate the position of the new breakpoint in breakpoint vector.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNewPointByTheLink(java.util.List,java.util.List,java.awt.Point)">getNewPointByTheLink</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; oldBreaks,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; newBreaks,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> oldLocation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNextEnd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getNextEnd</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns other than given end.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNextPoint(java.awt.Point)">getNextPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns next point to a given one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotCopyBounds()">getNotCopyBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">get not copy bounds of object throws NoRectangleDefinedException</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.diagram.style.PathStylePropertyDelegate</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnStyleDelegate()">getOwnStyleDelegate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathIcon()">getPathIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.paths.painters.PathPainter&lt;<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathPainter()">getPathPainter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPaths()">getPaths</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns only one path which consist of actual supplier draw point, break points of the path element
 and actual client draw point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPointOnPath(java.awt.Point,java.awt.Point,java.util.List,double)">getPointOnPath</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplierPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> clientPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; breakpoints,
 double coefficient)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreviousPoint(java.awt.Point)">getPreviousPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns previous point to given one.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplier()">getSupplier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns supplier of the path.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierConnectionType()">getSupplierConnectionType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierDrawPoint()">getSupplierDrawPoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns point where path drawing should start</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierPoint()">getSupplierPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns point where path connects supplier end's element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSuspendShapeAutoResizeMode()">getSuspendShapeAutoResizeMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.editing.Command</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleRemoveBreaksAction()">handleRemoveBreaksAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasClientPoint()">hasClientPoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if client point is already not null</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasManipulator()">hasManipulator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if view has manipulator (is selectable)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasSharedModelElement()">hasSharedModelElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if <code>ModelElement</code> of this symbol can represented with other symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasSupplierPoint()">hasSupplierPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if supplier point is already not null</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies properties</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a><wbr/>(<a href="../ConverterToShape.html" title="class in com.nomagic.magicdraw.uml.symbols">ConverterToShape</a> converterToShape)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetPresentationElementStroke(boolean,int)">internalGetPresentationElementStroke</a><wbr/>(boolean line,
 int width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method must be overridden, if you need to use DASHED_STROKE or another one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetPresentationElementStroke(boolean,int,int)">internalGetPresentationElementStroke</a><wbr/>(boolean line,
 int lineStyle,
 int width)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a><wbr/>(int width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a stroke used to paint symbol's main part</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalMovedAsToSelf(int,int)">internalMovedAsToSelf</a><wbr/>(int dx,
 int dy)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This is an internal method to notify a path that it was moved by connecting shape as the path "to self"</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSilentApply()">internalSilentApply</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Silently applies all properties after initialization</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSnapToGrid(float)">internalSnapToGrid</a><wbr/>(float step)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a><wbr/>(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if any line between breakpoints intersect with given points of rectangle</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intersectsInternal(int,int,int,int)">intersectsInternal</a><wbr/>(int x,
 int y,
 int width,
 int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check intersection with given rectangle.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAlwaysToSelf()">isAlwaysToSelf</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isBezier()">isBezier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isBezierIntersects(int,int,int,int)">isBezierIntersects</a><wbr/>(int x,
 int y,
 int width,
 int height)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if it is bezier path intersection with rectangle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isBreakable()">isBreakable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows whether a path is breakable.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isConnectable(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">isConnectable</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if this path can connect given two elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isConnectable(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.Map)">isConnectable</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if this path can connect given two elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDrawLineJumps()">isDrawLineJumps</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if the path element wants to draw line jumps.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFixed()">isFixed</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If a path tied to its supplier and client (cannot be reconnected)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLinkLineStyleDefined()">isLinkLineStyleDefined</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOblique()">isOblique</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRectilinear()">isRectilinear</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRounded()">isRounded</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns value of the "Is Rounded" path symbol property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSmartLayoutNeeded()">isSmartLayoutNeeded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns smart layout needed flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSnapToGrid()">isSnapToGrid</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isToSelf()">isToSelf</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseFlowLayoutLogic()">isUseFlowLayoutLogic</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if smart path/shape edit should be used in this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isVertical()">isVertical</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if path element is drawn in the diagram which has vertical orientation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#makeRectilinear()">makeRectilinear</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Makes link rectilinear.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#makeRectilinear(boolean)">makeRectilinear</a><wbr/>(boolean notify)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Makes link rectilinear.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#moveLinkToClientParent(boolean)">moveLinkToClientParent</a><wbr/>(boolean simpleAdd)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> link,
 <a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> requestor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves link.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#needsToMoveOtherEnd()">needsToMoveOtherEnd</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#nextStyle()">nextStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#notifyBreakPointsChanged(java.util.List,java.util.List)">notifyBreakPointsChanged</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; oldPoints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; newPoints)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notifies about break point vector changes</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#notifyRepaintManager(boolean)">notifyRepaintManager</a><wbr/>(boolean boundsChanged)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notifies the repaint manager about changes in bounds.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#notifyRepaintManager(java.util.List,java.util.List)">notifyRepaintManager</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; oldBreakpoints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; newBreakpoints)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#optimizeLoops()">optimizeLoops</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes loops from paths for example:
 path
 |
 ----------+
 |     |
 ------</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelf</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#preDisposeOnUpdate()">preDisposeOnUpdate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Validate symbol against model and try to fix it before actual symbol update.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prepareForLineDrawing(java.awt.Graphics2D,boolean)">prepareForLineDrawing</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 boolean line)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Prepares graphics for line drawing.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerLineJumpInfos(int,java.awt.Point,java.util.List)">registerLineJumpInfos</a><wbr/>(int pathIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> segmentStartPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.uml.symbols.LineJumpInfo&gt; lineJumps)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers line jump info for specified path and specified segmentStartPoint in the path.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerLineJumpStartAngle(int,java.awt.Point,double)">registerLineJumpStartAngle</a><wbr/>(int pathIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point,
 double lineJumpStartAngle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers start angle for the specified path and specified start point of the path segment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeBreakPoints()">removeBreakPoints</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes break points if they do not really break the path (a path looks like without break points but really has them).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeBreaks(java.util.List)">removeBreaks</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; points)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all break points if they are covered by client or client bounds.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeRedundantBreakPoints(java.util.List)">removeRedundantBreakPoints</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; vct)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes redundant breakpoints from link.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeUnnecessaryBreakPoints()">removeUnnecessaryBreakPoints</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes unnecessary points from break point vector.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resetCache()">resetCache</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resizeParent()">resizeParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Do nothing, because path does not affect parent size</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sAddBreakPoint(java.awt.Point)">sAddBreakPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds new break point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sClearBreakPoints()">sClearBreakPoints</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clear break points list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBounds(java.awt.Rectangle)">setBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves link to new location.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBreakable(boolean)">setBreakable</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a breakable flag on/off.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBreakPoints(java.util.List)">setBreakPoints</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; vct)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets break point vector.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCachedPathBounds(java.awt.Rectangle)">setCachedPathBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setClient(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setClient</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> shape)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets client for this link.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setClientPoint(java.awt.Point)">setClientPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets client point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCustomClientPoint(java.awt.Point)">setCustomClientPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCustomSupplierPoint(java.awt.Point)">setCustomSupplierPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLineJumpPlace(com.nomagic.magicdraw.uml.symbols.LineJumpPlace)">setLineJumpPlace</a><wbr/>(com.nomagic.magicdraw.uml.symbols.LineJumpPlace lineJumpPlace)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets line jump place of the path element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLinkLineStyle(java.lang.String)">setLinkLineStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> style)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sets LINK_LINE_STYLE property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPathPainter(com.nomagic.magicdraw.uml.symbols.paths.painters.PathPainter)">setPathPainter</a><wbr/>(com.nomagic.magicdraw.uml.symbols.paths.painters.PathPainter pathPainter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRectilinear()">setRectilinear</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets link rectilinear property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRounded(boolean)">setRounded</a><wbr/>(boolean rounded)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets value of the "Is Rounded" path symbol property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSmartLayoutNeeded(boolean)">setSmartLayoutNeeded</a><wbr/>(boolean smartLayoutNeeded)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets smart layout needed flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSupplier(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setSupplier</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> shape)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets supplier end for link.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSupplierPoint(java.awt.Point)">setSupplierPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets first point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSuspendShapeAutoResizeMode(java.lang.String)">setSuspendShapeAutoResizeMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">calls break point vector changed method.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetBounds(java.awt.Rectangle)">sSetBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves path to new location.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetBreakable(boolean)">sSetBreakable</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a breakable flag on/off.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetBreakPoint(java.awt.Point,int)">sSetBreakPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 int pos)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets break point at the given position.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetBreakPoints(java.util.List)">sSetBreakPoints</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; vct)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Only sets break point vector.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetClient(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetClient</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets client for this link.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetClientPoint(java.awt.Point)">sSetClientPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets client connection Point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetLinkLineStyle(java.lang.String)">sSetLinkLineStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Change value of LINK_LINE_STYLE property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets parent for this view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetRounded(boolean)">sSetRounded</a><wbr/>(boolean rounded)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets value of the "Is Rounded" path symbol property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetSupplier(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetSupplier</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets supplier for this link.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetSupplierPoint(java.awt.Point)">sSetSupplierPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets supplier connection point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetSuspendShapeAutoResizeMode(java.lang.String)">sSetSuspendShapeAutoResizeMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#swapEnds()">swapEnds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Swaps ends of the link</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#translateClientPoint(java.awt.Rectangle,java.awt.Rectangle)">translateClientPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> old,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> newR)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#translateSupplierPoint(java.awt.Rectangle,java.awt.Rectangle)">translateSupplierPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> old,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> newR)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.utils.Pair&lt;com.dassault_systemes.modeler.foundation.model.ModelElement,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;com.dassault_systemes.modeler.foundation.model.ModelElement&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#useOtherExistingElement()">useOtherExistingElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds and returns other model element which  is semantically equivalent to this path model element.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="PathConnector.html#checkShowsProxy()">checkShowsProxy</a>, <a href="PathConnector.html#clearShowsProxy()">clearShowsProxy</a>, <a href="PathConnector.html#disposeConnectedPaths()">disposeConnectedPaths</a>, <a href="PathConnector.html#findSymbolForEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">findSymbolForEnd</a>, <a href="PathConnector.html#findSymbolForEnd(java.util.stream.Stream,boolean)">findSymbolForEnd</a>, <a href="PathConnector.html#getConnectedPathElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">getConnectedPathElement</a>, <a href="PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a>, <a href="PathConnector.html#getPreferredArrowLength()">getPreferredArrowLength</a>, <a href="PathConnector.html#isShowsProxy()">isShowsProxy</a>, <a href="PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,boolean)">movePathElement</a>, <a href="PathConnector.html#movePathElements()">movePathElements</a>, <a href="PathConnector.html#removeConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">removeConnectedPathElement</a>, <a href="PathConnector.html#sAddConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sAddConnectedPathElement</a>, <a href="PathConnector.html#selectPathsForMoving(java.util.List)">selectPathsForMoving</a>, <a href="PathConnector.html#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a>, <a href="PathConnector.html#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a>, <a href="PathConnector.html#sRemoveConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">sRemoveConnectedPathElement</a>, <a href="PathConnector.html#sSetConnectedPathElements(java.util.List)">sSetConnectedPathElements</a>, <a href="PathConnector.html#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a>, <a href="PathConnector.html#supportsVisibleConnectedPathElementsIfSelfInvisible()">supportsVisibleConnectedPathElementsIfSelfInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a>, <a href="../PresentationElement.html#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">addPresentationElement</a>, <a href="../PresentationElement.html#addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElementWithoutResize</a>, <a href="../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="../PresentationElement.html#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">adjustBoundsBeforeChange</a>, <a href="../PresentationElement.html#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBounds</a>, <a href="../PresentationElement.html#adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBoundsForMoving</a>, <a href="../PresentationElement.html#alwaysShowTooltip()">alwaysShowTooltip</a>, <a href="../PresentationElement.html#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">applyProperties</a>, <a href="../PresentationElement.html#atInsertChildren()">atInsertChildren</a>, <a href="../PresentationElement.html#autosizeAndResizeManipulatedParent()">autosizeAndResizeManipulatedParent</a>, <a href="../PresentationElement.html#autosizeAndResizeParent()">autosizeAndResizeParent</a>, <a href="../PresentationElement.html#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">beforeDelete</a>, <a href="../PresentationElement.html#boundsChanged()">boundsChanged</a>, <a href="../PresentationElement.html#boundsChanged(java.awt.Rectangle)">boundsChanged</a>, <a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="../PresentationElement.html#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddChild</a>, <a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../PresentationElement.html#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddInstance</a>, <a href="../PresentationElement.html#canBeDisposedOnUpdate()">canBeDisposedOnUpdate</a>, <a href="../PresentationElement.html#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeElementOwner</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">canChangeParent</a>, <a href="../PresentationElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../PresentationElement.html#canFill()">canFill</a>, <a href="../PresentationElement.html#canHavePaths()">canHavePaths</a>, <a href="../PresentationElement.html#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">changeProperties</a>, <a href="../PresentationElement.html#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a>, <a href="../PresentationElement.html#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">checkProxyVisibility</a>, <a href="../PresentationElement.html#childrenForMoving()">childrenForMoving</a>, <a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">collectSubPresentationElements</a>, <a href="../PresentationElement.html#collectSubShowingPresentationElements(java.util.Collection)">collectSubShowingPresentationElements</a>, <a href="../PresentationElement.html#coversPoint(int,int)">coversPoint</a>, <a href="../PresentationElement.html#createPresentationElementStyle()">createPresentationElementStyle</a>, <a href="../PresentationElement.html#createPropertyChangeListener()">createPropertyChangeListener</a>, <a href="../PresentationElement.html#disposeChildren()">disposeChildren</a>, <a href="../PresentationElement.html#disposePropertyChangeListener()">disposePropertyChangeListener</a>, <a href="../PresentationElement.html#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawBackground</a>, <a href="../PresentationElement.html#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbol</a>, <a href="../PresentationElement.html#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbolBackground</a>, <a href="../PresentationElement.html#dynamicFillColor()">dynamicFillColor</a>, <a href="../PresentationElement.html#dynamicLineColor()">dynamicLineColor</a>, <a href="../PresentationElement.html#dynamicLineWidth()">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicLineWidth(int)">dynamicLineWidth</a>, <a href="../PresentationElement.html#dynamicPaintShadow()">dynamicPaintShadow</a>, <a href="../PresentationElement.html#dynamicStroke()">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(int)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a>, <a href="../PresentationElement.html#dynamicStyleFillColor(java.awt.Color,boolean)">dynamicStyleFillColor</a>, <a href="../PresentationElement.html#dynamicStyleLineColor(java.awt.Color)">dynamicStyleLineColor</a>, <a href="../PresentationElement.html#dynamicStyleTextColor(java.awt.Color)">dynamicStyleTextColor</a>, <a href="../PresentationElement.html#dynamicStyleTransparency()">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleTransparency(javax.swing.Icon)">dynamicStyleTransparency</a>, <a href="../PresentationElement.html#dynamicStyleValue(T,java.util.function.BiFunction)">dynamicStyleValue</a>, <a href="../PresentationElement.html#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">dynamicTextAlignment</a>, <a href="../PresentationElement.html#dynamicTextColor()">dynamicTextColor</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a>, <a href="../PresentationElement.html#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOwnerForChildElement</a>, <a href="../PresentationElement.html#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">findPresentationElement</a>, <a href="../PresentationElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../PresentationElement.html#generateID()">generateID</a>, <a href="../PresentationElement.html#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>, <a href="../PresentationElement.html#getActualElement()">getActualElement</a>, <a href="../PresentationElement.html#getAdditionalRenderersToNotifyOnPropertiesChange()">getAdditionalRenderersToNotifyOnPropertiesChange</a>, <a href="../PresentationElement.html#getAssignableModelElementsClasses()">getAssignableModelElementsClasses</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getBoundsWithChildrenOnEdge()">getBoundsWithChildrenOnEdge</a>, <a href="../PresentationElement.html#getCenterlinePoint()">getCenterlinePoint</a>, <a href="../PresentationElement.html#getCenterlinePointX()">getCenterlinePointX</a>, <a href="../PresentationElement.html#getCenterlinePointY()">getCenterlinePointY</a>, <a href="../PresentationElement.html#getChildPresentationElementForContextMenu(java.awt.Point)">getChildPresentationElementForContextMenu</a>, <a href="../PresentationElement.html#getChildrenWithSymbolProperties()">getChildrenWithSymbolProperties</a>, <a href="../PresentationElement.html#getConfiguration()">getConfiguration</a>, <a href="../PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="../PresentationElement.html#getDiagramSurface()">getDiagramSurface</a>, <a href="../PresentationElement.html#getDrawComparator()">getDrawComparator</a>, <a href="../PresentationElement.html#getDynamicConfigurations()">getDynamicConfigurations</a>, <a href="../PresentationElement.html#getDynamicStyleOwner()">getDynamicStyleOwner</a>, <a href="../PresentationElement.html#getEffectiveStyleDelegate()">getEffectiveStyleDelegate</a>, <a href="../PresentationElement.html#getEffectiveStyleOwner()">getEffectiveStyleOwner</a>, <a href="../PresentationElement.html#getElement()">getElement</a>, <a href="../PresentationElement.html#getElementsForRelationshipConnecting()">getElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementToConnectRelationship</a>, <a href="../PresentationElement.html#getFillColor()">getFillColor</a>, <a href="../PresentationElement.html#getFont()">getFont</a>, <a href="../PresentationElement.html#getFontHeight()">getFontHeight</a>, <a href="../PresentationElement.html#getFontRenderContext()">getFontRenderContext</a>, <a href="../PresentationElement.html#getHumanName()">getHumanName</a>, <a href="../PresentationElement.html#getHumanType()">getHumanType</a>, <a href="../PresentationElement.html#getLineColor()">getLineColor</a>, <a href="../PresentationElement.html#getLineWidth()">getLineWidth</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getManipulationBounds(java.awt.Point)">getManipulationBounds</a>, <a href="../PresentationElement.html#getManipulationPreferredDimension()">getManipulationPreferredDimension</a>, <a href="../PresentationElement.html#getMiddlePoint(java.awt.Point)">getMiddlePoint</a>, <a href="../PresentationElement.html#getMiddlePointX()">getMiddlePointX</a>, <a href="../PresentationElement.html#getMiddlePointX(java.awt.Point)">getMiddlePointX</a>, <a href="../PresentationElement.html#getMiddlePointY()">getMiddlePointY</a>, <a href="../PresentationElement.html#getMiddlePointY(java.awt.Point)">getMiddlePointY</a>, <a href="../PresentationElement.html#getMinimumDimension()">getMinimumDimension</a>, <a href="../PresentationElement.html#getModelElement()">getModelElement</a>, <a href="../PresentationElement.html#getModelElementsForRelationshipConnecting()">getModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">getModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#getModelElementToMove()">getModelElementToMove</a>, <a href="../PresentationElement.html#getNotZoomedTolerance()">getNotZoomedTolerance</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a>, <a href="../PresentationElement.html#getPreferredBounds()">getPreferredBounds</a>, <a href="../PresentationElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="../PresentationElement.html#getPreferredDimensionForAutosize()">getPreferredDimensionForAutosize</a>, <a href="../PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="../PresentationElement.html#getPresentationElementAt(int)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a>, <a href="../PresentationElement.html#getPresentationElementCount()">getPresentationElementCount</a>, <a href="../PresentationElement.html#getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getPresentationElementIndex</a>, <a href="../PresentationElement.html#getPresentationElements()">getPresentationElements</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getProjectImpl()">getProjectImpl</a>, <a href="../PresentationElement.html#getProperty(java.lang.String)">getProperty</a>, <a href="../PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="../PresentationElement.html#getPropertyManagerName()">getPropertyManagerName</a>, <a href="../PresentationElement.html#getRenderer()">getRenderer</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#getStyle()">getStyle</a>, <a href="../PresentationElement.html#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSymbolRenderer</a>, <a href="../PresentationElement.html#getTextColor()">getTextColor</a>, <a href="../PresentationElement.html#getTolerance()">getTolerance</a>, <a href="../PresentationElement.html#getVisibility()">getVisibility</a>, <a href="../PresentationElement.html#getVisiblePresentationElements()">getVisiblePresentationElements</a>, <a href="../PresentationElement.html#handleModelDelete()">handleModelDelete</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#initialize()">initialize</a>, <a href="../PresentationElement.html#initializeAndAutosize()">initializeAndAutosize</a>, <a href="../PresentationElement.html#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)">internalBeforeUpdate</a>, <a href="../PresentationElement.html#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">internalCreatePropertyChangeListener</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">internalGetModelElementsForRelationshipConnecting</a>, <a href="../PresentationElement.html#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a>, <a href="../PresentationElement.html#internalGetSpecificFont()">internalGetSpecificFont</a>, <a href="../PresentationElement.html#internalGetSpecificTextColor()">internalGetSpecificTextColor</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#internalSnapToGrid(java.awt.Point,float)">internalSnapToGrid</a>, <a href="../PresentationElement.html#internalUpdatePresentationElement()">internalUpdatePresentationElement</a>, <a href="../PresentationElement.html#intersects(int,int,int,int)">intersects</a>, <a href="../PresentationElement.html#invalidate()">invalidate</a>, <a href="../PresentationElement.html#isCanChildrenChangeEdge()">isCanChildrenChangeEdge</a>, <a href="../PresentationElement.html#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildVisible</a>, <a href="../PresentationElement.html#isContentHidden()">isContentHidden</a>, <a href="../PresentationElement.html#isCreateElementListener()">isCreateElementListener</a>, <a href="../PresentationElement.html#isDetectable()">isDetectable</a>, <a href="../PresentationElement.html#isDisposed()">isDisposed</a>, <a href="../PresentationElement.html#isLayouting()">isLayouting</a>, <a href="../PresentationElement.html#isMovableByMoveManager()">isMovableByMoveManager</a>, <a href="../PresentationElement.html#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNotNull</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../PresentationElement.html#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isParentOf</a>, <a href="../PresentationElement.html#isPreserveProportionsWhenGrowing()">isPreserveProportionsWhenGrowing</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#isShowElementTypeAsLabel()">isShowElementTypeAsLabel</a>, <a href="../PresentationElement.html#isSortable()">isSortable</a>, <a href="../PresentationElement.html#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">isSuitableToConnectRelationship</a>, <a href="../PresentationElement.html#isTextEditable()">isTextEditable</a>, <a href="../PresentationElement.html#isUseFillColor()">isUseFillColor</a>, <a href="../PresentationElement.html#isUseFillColorByProperty()">isUseFillColorByProperty</a>, <a href="../PresentationElement.html#isUseGradientForFill()">isUseGradientForFill</a>, <a href="../PresentationElement.html#isVisible()">isVisible</a>, <a href="../PresentationElement.html#isVisibleInDiagram()">isVisibleInDiagram</a>, <a href="../PresentationElement.html#isVisibleOrShrunken()">isVisibleOrShrunken</a>, <a href="../PresentationElement.html#movePathElementsRecursively()">movePathElementsRecursively</a>, <a href="../PresentationElement.html#mustShowContextMenu()">mustShowContextMenu</a>, <a href="../PresentationElement.html#notifyCreated()">notifyCreated</a>, <a href="../PresentationElement.html#notifyDiagramFrameSizeChange()">notifyDiagramFrameSizeChange</a>, <a href="../PresentationElement.html#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildAdd</a>, <a href="../PresentationElement.html#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildRemove</a>, <a href="../PresentationElement.html#onDiagramSurfaceSet()">onDiagramSurfaceSet</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#onFontChange()">onFontChange</a>, <a href="../PresentationElement.html#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">onParentChange</a>, <a href="../PresentationElement.html#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornments</a>, <a href="../PresentationElement.html#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornmentsBackground</a>, <a href="../PresentationElement.html#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildren</a>, <a href="../PresentationElement.html#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenAndAdornments</a>, <a href="../PresentationElement.html#paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenBackground</a>, <a href="../PresentationElement.html#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelfBackground</a>, <a href="../PresentationElement.html#prepareForLineDrawing(java.awt.Graphics2D)">prepareForLineDrawing</a>, <a href="../PresentationElement.html#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a>, <a href="../PresentationElement.html#prepareForTextDrawing(java.awt.Graphics2D)">prepareForTextDrawing</a>, <a href="../PresentationElement.html#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a>, <a href="../PresentationElement.html#recreateListeners()">recreateListeners</a>, <a href="../PresentationElement.html#recursiveAutosize()">recursiveAutosize</a>, <a href="../PresentationElement.html#registerInSortManager()">registerInSortManager</a>, <a href="../PresentationElement.html#rememberBounds()">rememberBounds</a>, <a href="../PresentationElement.html#rememberBounds(java.awt.Rectangle)">rememberBounds</a>, <a href="../PresentationElement.html#removeFromSortManager()">removeFromSortManager</a>, <a href="../PresentationElement.html#removeItSelfOnUpdate()">removeItSelfOnUpdate</a>, <a href="../PresentationElement.html#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">removePresentationElement</a>, <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sAddPresentationElement</a>, <a href="../PresentationElement.html#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">sAddPresentationElement</a>, <a href="../PresentationElement.html#selectChildrenForMoving()">selectChildrenForMoving</a>, <a href="../PresentationElement.html#selectObjectsForMoving()">selectObjectsForMoving</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setBounds(int,int,int,int)">setBounds</a>, <a href="../PresentationElement.html#setCreateElementListener(boolean)">setCreateElementListener</a>, <a href="../PresentationElement.html#setDummyResizeMode(boolean)">setDummyResizeMode</a>, <a href="../PresentationElement.html#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a>, <a href="../PresentationElement.html#setFillColor(java.awt.Color)">setFillColor</a>, <a href="../PresentationElement.html#setFont(java.awt.Font)">setFont</a>, <a href="../PresentationElement.html#setLayouting(boolean)">setLayouting</a>, <a href="../PresentationElement.html#setLineColor(java.awt.Color)">setLineColor</a>, <a href="../PresentationElement.html#setLineWidth(int)">setLineWidth</a>, <a href="../PresentationElement.html#setLoadedVisibility(boolean)">setLoadedVisibility</a>, <a href="../PresentationElement.html#setLocation(int,int)">setLocation</a>, <a href="../PresentationElement.html#setLocation(java.awt.Point)">setLocation</a>, <a href="../PresentationElement.html#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">setModelElement</a>, <a href="../PresentationElement.html#setNeedRecreateListeners(boolean)">setNeedRecreateListeners</a>, <a href="../PresentationElement.html#setPresentationElements(java.util.List)">setPresentationElements</a>, <a href="../PresentationElement.html#setPropertyManagerName(java.lang.String)">setPropertyManagerName</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#setSize(int,int)">setSize</a>, <a href="../PresentationElement.html#setSize(com.nomagic.ui.UnmodifiableDimension)">setSize</a>, <a href="../PresentationElement.html#setSize(java.awt.Dimension)">setSize</a>, <a href="../PresentationElement.html#setTextColor(java.awt.Color)">setTextColor</a>, <a href="../PresentationElement.html#setTextEditable(boolean)">setTextEditable</a>, <a href="../PresentationElement.html#setUseFillColor(boolean)">setUseFillColor</a>, <a href="../PresentationElement.html#setVisible(boolean)">setVisible</a>, <a href="../PresentationElement.html#silentApply()">silentApply</a>, <a href="../PresentationElement.html#silentApply(boolean)">silentApply</a>, <a href="../PresentationElement.html#simpleSetBounds(int,int,int,int)">simpleSetBounds</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Point,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapToGrid(java.awt.Rectangle,float)">snapToGrid</a>, <a href="../PresentationElement.html#snapViewToGrid(float)">snapViewToGrid</a>, <a href="../PresentationElement.html#sortObjectsByX(java.util.List)">sortObjectsByX</a>, <a href="../PresentationElement.html#sortObjectsByY(java.util.List)">sortObjectsByY</a>, <a href="../PresentationElement.html#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sRemovePresentationElement</a>, <a href="../PresentationElement.html#sSetBounds(int,int,int,int)">sSetBounds</a>, <a href="../PresentationElement.html#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">sSetElement</a>, <a href="../PresentationElement.html#sSetLocation(int,int)">sSetLocation</a>, <a href="../PresentationElement.html#sSetLocation(java.awt.Point)">sSetLocation</a>, <a href="../PresentationElement.html#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">sSetModelElement</a>, <a href="../PresentationElement.html#sSetParentForAll(java.util.Collection)">sSetParentForAll</a>, <a href="../PresentationElement.html#sSetPresentationElements(java.util.List)">sSetPresentationElements</a>, <a href="../PresentationElement.html#sSetSize(int,int)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(com.nomagic.ui.UnmodifiableDimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetSize(java.awt.Dimension)">sSetSize</a>, <a href="../PresentationElement.html#sSetVisible(boolean)">sSetVisible</a>, <a href="../PresentationElement.html#tryToDeleteModelElementUponRemoval()">tryToDeleteModelElementUponRemoval</a>, <a href="../PresentationElement.html#update()">update</a>, <a href="../PresentationElement.html#updateAfterLoad()">updateAfterLoad</a>, <a href="../PresentationElement.html#updateLabelsIgnoringSuspendableLater(java.util.Collection)">updateLabelsIgnoringSuspendableLater</a>, <a href="../PresentationElement.html#updateLater()">updateLater</a>, <a href="../PresentationElement.html#updateModelByView()">updateModelByView</a>, <a href="../PresentationElement.html#updateModelByViewInternal()">updateModelByViewInternal</a>, <a href="../PresentationElement.html#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a>, <a href="../PresentationElement.html#useParentProperties()">useParentProperties</a>, <a href="../PresentationElement.html#useParentStyle()">useParentStyle</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.LineJumpDrawer">Methods inherited from interface com.nomagic.magicdraw.uml.symbols.LineJumpDrawer</h3>
<code>getLineWidth</code></div>
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
<section class="detail" id="RECTILINEAR">
<h3>RECTILINEAR</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RECTILINEAR</span></div>
<div class="block">Path line style with rectilinear (90 degrees) breakpoint corners.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.paths.PathElement.RECTILINEAR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OBLIQUE">
<h3>OBLIQUE</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OBLIQUE</span></div>
<div class="block">Polyline path line style.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.paths.PathElement.OBLIQUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BEZIER">
<h3>BEZIER</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BEZIER</span></div>
<div class="block">Bezier path line style.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.paths.PathElement.BEZIER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LINE_STYLE">
<h3>LINE_STYLE</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">LINE_STYLE</span></div>
<div class="block">All possible path line styles.</div>
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
<h3>PathElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PathElement</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>PathElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PathElement</span><wbr/><span class="parameters">(@CheckForNull
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
<section class="detail" id="getOwnStyleDelegate()">
<h3>getOwnStyleDelegate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.diagram.style.PathStylePropertyDelegate</span> <span class="element-name">getOwnStyleDelegate</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getOwnStyleDelegate()">getOwnStyleDelegate</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>the own style property delegate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearSupplierTranslation()">
<h3>clearSupplierTranslation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearSupplierTranslation</span>()</div>
<div class="block">Clears a supplier translated flag.</div>
</section>
</li>
<li>
<section class="detail" id="clearClientTranslation()">
<h3>clearClientTranslation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearClientTranslation</span>()</div>
<div class="block">Clears a client translated flag.</div>
</section>
</li>
<li>
<section class="detail" id="translateSupplierPoint(java.awt.Rectangle,java.awt.Rectangle)">
<h3>translateSupplierPoint</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">translateSupplierPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> old,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> newR)</span></div>
</section>
</li>
<li>
<section class="detail" id="translateClientPoint(java.awt.Rectangle,java.awt.Rectangle)">
<h3>translateClientPoint</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">translateClientPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> old,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> newR)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNewPointByTheLink(java.util.List,java.util.List,java.awt.Point)">
<h3>getNewPointByTheLink</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getNewPointByTheLink</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; oldBreaks,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; newBreaks,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> oldLocation)</span></div>
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
<section class="detail" id="askDeleteDataConfirmation()">
<h3>askDeleteDataConfirmation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">askDeleteDataConfirmation</span>()</div>
<div class="block">Return true, because while deleting link view user must be prompt about deleting data</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#askDeleteDataConfirmation()">askDeleteDataConfirmation</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>confirmation status -- true if asking is necessary, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBreakable(boolean)">
<h3>setBreakable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBreakable</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets a breakable flag on/off. If a flag is not set, a path cannot be broken.
 However, a path can have break points and be non-breakable.
 This means that path has fixed points that cannot be moved.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - flag value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetBreakable(boolean)">
<h3>sSetBreakable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetBreakable</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets a breakable flag on/off. If a flag is not set, a path cannot be broken.
 However, a path can have break points and be non-breakable.
 This means that path has fixed points that cannot be moved.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - flag value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isBreakable()">
<h3>isBreakable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBreakable</span>()</div>
<div class="block">Shows whether a path is breakable.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if a path can be broken</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFixed()">
<h3>isFixed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFixed</span>()</div>
<div class="block">If a path tied to its supplier and client (cannot be reconnected)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if it can be reconnected, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBreakPoints()">
<h3>getBreakPoints</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</span> <span class="element-name">getBreakPoints</span>()</div>
<div class="block">Returns break points of the path.
 The order of break points is from supplier to the client path's end.
 Use PresentationElementsManager to change the break points for the path.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>break points list.Points in the list are not cloned, so do not modify them directly.
 The List is unmodifiable.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../openapi/uml/PresentationElementsManager.html#changePathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.util.List)"><code>PresentationElementsManager.changePathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement, java.util.List)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllBreakPoints()">
<h3>getAllBreakPoints</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</span> <span class="element-name">getAllBreakPoints</span>()</div>
<div class="block">Returns a break points list with added supplier and client end point in the list as well.
 Use PresentationElementsManager to change the break points for the path.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>supplier point + break points + client point. Points in the list are not cloned,
 so do not modify them directly. The List is modifiable.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../openapi/uml/PresentationElementsManager.html#changePathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.util.List)"><code>PresentationElementsManager.changePathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement, java.util.List)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBreakPoints(java.util.List)">
<h3>setBreakPoints</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setBreakPoints</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; vct)</span></div>
<div class="block">Sets break point vector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vct</code> - new break point vector.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sClearBreakPoints()">
<h3>sClearBreakPoints</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sClearBreakPoints</span>()</div>
<div class="block">Clear break points list.</div>
</section>
</li>
<li>
<section class="detail" id="sSetBreakPoints(java.util.List)">
<h3>sSetBreakPoints</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sSetBreakPoints</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; vct)</span></div>
<div class="block">Only sets break point vector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vct</code> - new break point vector.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sAddBreakPoint(java.awt.Point)">
<h3>sAddBreakPoint</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sAddBreakPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</span></div>
<div class="block">Adds new break point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - point to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetBreakPoint(java.awt.Point,int)">
<h3>sSetBreakPoint</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sSetBreakPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 int pos)</span></div>
<div class="block">Sets break point at the given position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - point to be set</dd>
<dd><code>pos</code> - position where it must be set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="needsToMoveOtherEnd()">
<h3>needsToMoveOtherEnd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">needsToMoveOtherEnd</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if one end of links changed bounds and move link must be called for both ends.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBreakPoint(int)">
<h3>getBreakPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getBreakPoint</span><wbr/><span class="parameters">(int pos)</span></div>
<div class="block">Returns break point with given index.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pos</code> - position where point resides.</dd>
<dt>Returns:</dt>
<dd>point at position pos.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBreakPointCount()">
<h3>getBreakPointCount</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getBreakPointCount</span>()</div>
<div class="block">returns size of break point vector</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>break point count</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBounds(java.awt.Rectangle)">
<h3>setBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span></div>
<div class="block">Moves link to new location.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../PresentationElement.html#setBounds(java.awt.Rectangle)">setBounds</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>r</code> - new location of a path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="simpleSetBounds(java.awt.Rectangle)">
<h3>simpleSetBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">simpleSetBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span></div>
<div class="block">calls break point vector changed method.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>r</code> - new bounding rectangle.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isToSelf()">
<h3>isToSelf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isToSelf</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this path is to self (client and supplier are the same).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAlwaysToSelf()">
<h3>isAlwaysToSelf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAlwaysToSelf</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetBounds(java.awt.Rectangle)">
<h3>sSetBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span></div>
<div class="block">Moves path to new location.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../PresentationElement.html#sSetBounds(java.awt.Rectangle)">sSetBounds</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>r</code> - new location of a path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeUnnecessaryBreakPoints()">
<h3>removeUnnecessaryBreakPoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeUnnecessaryBreakPoints</span>()</div>
<div class="block">Removes unnecessary points from break point vector.
 Checks if break point vector has useless points (covered by shape or invisible).
 Does not do anything if a path cannot be breakable.
 If it has, remove them.</div>
</section>
</li>
<li>
<section class="detail" id="getPathIcon()">
<h3>getPathIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon</span> <span class="element-name">getPathIcon</span>()</div>
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
<section class="detail" id="getCustomStereotypeIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getCustomStereotypeIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.dassault_systemes.modeler.foundation.image.pathicon.PathIcon</span> <span class="element-name">getCustomStereotypeIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="draw(java.awt.Graphics2D,java.awt.Point,java.awt.Point,java.util.List)">
<h3>draw</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">draw</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplierPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> clientPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; breakPoints)</span></div>
<div class="block">Draws link from given point pt1 through break points
 to given point pt2.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>g</code> - graphics</dd>
<dd><code>supplierPoint</code> - first point</dd>
<dd><code>clientPoint</code> - second point</dd>
<dd><code>breakPoints</code> - points between supplier and client points, in that order</dd>
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
<section class="detail" id="setLineJumpPlace(com.nomagic.magicdraw.uml.symbols.LineJumpPlace)">
<h3>setLineJumpPlace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLineJumpPlace</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.uml.symbols.LineJumpPlace lineJumpPlace)</span></div>
<div class="block">Sets line jump place of the path element.
 <br/><b>NOTE: Only <code>LineJumpManager</code> can set jump place of the link. Since <code>LineJumpManager</code>
 will reset line jump place on every repaint of a diagram then other invocations of the method will not have
 an effect.</b></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setLineJumpPlace</code> in interface <code>com.nomagic.magicdraw.uml.symbols.LineJumpDrawer</code></dd>
<dt>Parameters:</dt>
<dd><code>lineJumpPlace</code> - new line jump place.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerLineJumpInfos(int,java.awt.Point,java.util.List)">
<h3>registerLineJumpInfos</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerLineJumpInfos</span><wbr/><span class="parameters">(int pathIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> segmentStartPoint,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.uml.symbols.LineJumpInfo&gt; lineJumps)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.uml.symbols.LineJumpDrawer</code></span></div>
<div class="block">Registers line jump info for specified path and specified segmentStartPoint in the path.
 Index of the path coincident with the index of the path which was returned by <code>LineJumpDrawer.getPaths()</code>
 method.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>registerLineJumpInfos</code> in interface <code>com.nomagic.magicdraw.uml.symbols.LineJumpDrawer</code></dd>
<dt>Parameters:</dt>
<dd><code>pathIndex</code> - index of the path.</dd>
<dd><code>segmentStartPoint</code> - start point of the segment.</dd>
<dd><code>lineJumps</code> - list of information about line jumps.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearRegisteredLineJumpInfos()">
<h3>clearRegisteredLineJumpInfos</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearRegisteredLineJumpInfos</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.uml.symbols.LineJumpDrawer</code></span></div>
<div class="block">Clears all registered LineJumpInfos.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>clearRegisteredLineJumpInfos</code> in interface <code>com.nomagic.magicdraw.uml.symbols.LineJumpDrawer</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerLineJumpStartAngle(int,java.awt.Point,double)">
<h3>registerLineJumpStartAngle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerLineJumpStartAngle</span><wbr/><span class="parameters">(int pathIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point,
 double lineJumpStartAngle)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.uml.symbols.LineJumpDrawer</code></span></div>
<div class="block">Registers start angle for the specified path and specified start point of the path segment.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>registerLineJumpStartAngle</code> in interface <code>com.nomagic.magicdraw.uml.symbols.LineJumpDrawer</code></dd>
<dt>Parameters:</dt>
<dd><code>pathIndex</code> - index of the path.</dd>
<dd><code>point</code> - start point of the segment.</dd>
<dd><code>lineJumpStartAngle</code> - start angle of the line jump.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLineJumpStartAngle(java.awt.Point)">
<h3>getLineJumpStartAngle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getLineJumpStartAngle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point)</span></div>
</section>
</li>
<li>
<section class="detail" id="addLineJumps(java.awt.geom.GeneralPath,java.awt.Point,java.awt.Point,java.awt.Point)">
<h3>addLineJumps</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addLineJumps</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html" title="class or interface in java.awt.geom">GeneralPath</a> path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> segmentStartPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> startPoint,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> endPoint)</span></div>
<div class="block">Adds line jumps to the specified path.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>addLineJumps</code> in interface <code>com.nomagic.magicdraw.uml.symbols.LineJumpDrawer</code></dd>
<dt>Parameters:</dt>
<dd><code>path</code> - a path object.</dd>
<dd><code>segmentStartPoint</code> - segment start point.</dd>
<dd><code>startPoint</code> - start point from which to start adding the line jumps.</dd>
<dd><code>endPoint</code> - point until which line jumps should be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDrawLineJumps()">
<h3>isDrawLineJumps</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDrawLineJumps</span>()</div>
<div class="block">Returns true if the path element wants to draw line jumps.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isDrawLineJumps</code> in interface <code>com.nomagic.magicdraw.uml.symbols.LineJumpDrawer</code></dd>
<dt>Returns:</dt>
<dd>true if line jumps should be drawn for the path element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPaths()">
<h3>getPaths</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;&gt;</span> <span class="element-name">getPaths</span>()</div>
<div class="block">Returns only one path which consist of actual supplier draw point, break points of the path element
 and actual client draw point.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getPaths</code> in interface <code>com.nomagic.magicdraw.uml.symbols.LineJumpDrawer</code></dd>
<dt>Returns:</dt>
<dd>paths.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSupplierPoint(java.awt.Point)">
<h3>setSupplierPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSupplierPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</span></div>
<div class="block">Sets first point.
 Sets new location for text boxes if a point is changed, text boxes must be moved too.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - new 1st point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetSupplierPoint(java.awt.Point)">
<h3>sSetSupplierPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetSupplierPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</span></div>
<div class="block">Sets supplier connection point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - new supplier point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetClientPoint(java.awt.Point)">
<h3>sSetClientPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetClientPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</span></div>
<div class="block">Sets client connection Point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - new client point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClientPoint(java.awt.Point)">
<h3>setClientPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setClientPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</span></div>
<div class="block">Sets client point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - new client point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="breakPointsChanged(java.util.List,java.util.List)">
<h3>breakPointsChanged</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">breakPointsChanged</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; oldPoints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; newPoints)</span></div>
<div class="block">Moves all connection point for the links that are attached to this
 link middle point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>oldPoints</code> - old breakpoint vector.</dd>
<dd><code>newPoints</code> - new breakpoint vector.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="notifyRepaintManager(boolean)">
<h3>notifyRepaintManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">notifyRepaintManager</span><wbr/><span class="parameters">(boolean boundsChanged)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#notifyRepaintManager(boolean)">PresentationElement</a></code></span></div>
<div class="block">Notifies the repaint manager about changes in bounds.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#notifyRepaintManager(boolean)">notifyRepaintManager</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="notifyRepaintManager(java.util.List,java.util.List)">
<h3>notifyRepaintManager</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">notifyRepaintManager</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; oldBreakpoints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; newBreakpoints)</span></div>
</section>
</li>
<li>
<section class="detail" id="notifyBreakPointsChanged(java.util.List,java.util.List)">
<h3>notifyBreakPointsChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">notifyBreakPointsChanged</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; oldPoints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; newPoints)</span></div>
<div class="block">Notifies about break point vector changes</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>oldPoints</code> - old points</dd>
<dd><code>newPoints</code> - new points</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNearestLinkPart(int,int)">
<h3>getNearestLinkPart</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a href="../../../../awt/Line.html" title="class in com.nomagic.awt">Line</a></span> <span class="element-name">getNearestLinkPart</span><wbr/><span class="parameters">(int x,
 int y)</span></div>
<div class="block">Returns the nearest link part to specified point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - x of point</dd>
<dd><code>y</code> - y of point</dd>
<dt>Returns:</dt>
<dd>line</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeBreakPoints()">
<h3>removeBreakPoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">removeBreakPoints</span>()</div>
<div class="block">Removes break points if they do not really break the path (a path looks like without break points but really has them).
 Does nothing if a path is not breakable.</div>
</section>
</li>
<li>
<section class="detail" id="getSupplierPoint()">
<h3>getSupplierPoint</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getSupplierPoint</span>()</div>
<div class="block">Returns point where path connects supplier end's element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>supplier connection point. This method returns not cloned point, so do not modify it directly.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClientPoint()">
<h3>getClientPoint</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getClientPoint</span>()</div>
<div class="block">Returns point where path connects client end's element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>client point. This method returns not cloned point, so do not modify it directly.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClientDrawPoint()">
<h3>getClientDrawPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getClientDrawPoint</span>()</div>
<div class="block">Returns point where path drawing should start</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActualClientDrawPoint()">
<h3>getActualClientDrawPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getActualClientDrawPoint</span>()</div>
<div class="block">Returns actual client side draw point.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>actual client draw point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActualSupplierDrawPoint()">
<h3>getActualSupplierDrawPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getActualSupplierDrawPoint</span>()</div>
<div class="block">Returns actual supplier side draw point.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>actual supplier draw point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplierDrawPoint()">
<h3>getSupplierDrawPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getSupplierDrawPoint</span>()</div>
<div class="block">Returns point where path drawing should start</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNextPoint(java.awt.Point)">
<h3>getNextPoint</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getNextPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</span></div>
<div class="block">Returns next point to a given one. If given point does not belong to the link, returns parameter point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - point for which next point is necessary</dd>
<dt>Returns:</dt>
<dd>next point(not cloned)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreviousPoint(java.awt.Point)">
<h3>getPreviousPoint</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getPreviousPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</span></div>
<div class="block">Returns previous point to given one. If given point does not belong to the link, returns
 parameter point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - point for which previous point is necessary</dd>
<dt>Returns:</dt>
<dd>previous point(not cloned)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNearestPoint(java.awt.Point)">
<h3>getNearestPoint</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getNearestPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</span></div>
<div class="block">Returns first break point or client point if arg is supplier point.
 Or returns last break point or client point if arg is client point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - given point</dd>
<dt>Returns:</dt>
<dd>nearest point(not cloned)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetClient(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>sSetClient</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetClient</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block">Sets client for this link.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>symbol</code> - new client.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetSupplier(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>sSetSupplier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetSupplier</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block">Sets supplier for this link.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>symbol</code> - new supplier.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSupplier(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>setSupplier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSupplier</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> shape)</span></div>
<div class="block">Sets supplier end for link.
 Removes this link from old shape.
 Inserts this link to new shape.
 Method also sets supplier point to the middle point of shape.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shape</code> - new supplier.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClient()">
<h3>getClient</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getClient</span>()</div>
<div class="block">Returns client of the path.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>client element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplier()">
<h3>getSupplier</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getSupplier</span>()</div>
<div class="block">Returns supplier of the path.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>supplier end element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNextEnd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getNextEnd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getNextEnd</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> obj)</span></div>
<div class="block">Returns other than given end.
 If given end is supplier method returns client of this path.
 If given end is not supplier method returns supplier of this path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - given end</dd>
<dt>Returns:</dt>
<dd>other opposite end</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">
<h3>movePathElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">movePathElement</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> link,
 @CheckForNull
 <a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> requestor)</span></div>
<div class="block">Moves link.
 Link can connect more links ( such as note anchors in UML class diagrams ).
 After link was moved positions of connected links must be updated.
 Method checks if moving link supplier is this link recalculates supplier point moving link,
 otherwise it calculates client point of moving link.
 Point is calculated to  middle point of this link.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PathConnector.html#movePathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">movePathElement</a></code> in class <code><a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
<dt>Parameters:</dt>
<dd><code>link</code> - link to move.</dd>
<dd><code>requestor</code> - requestor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="optimizeLoops()">
<h3>optimizeLoops</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">optimizeLoops</span>()</div>
<div class="block">Removes loops from paths for example:
 path
 |
 ----------+
 |     |
 ------
 <p></p>
 will be changed to
 |
 -----</div>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#clone()">clone</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="PathConnector.html#clone()">clone</a></code> in class <code><a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>coversPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">coversPoint</span><wbr/><span class="parameters">(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">Checks if object covers provided point</div>
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
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">intersects</span><wbr/><span class="parameters">(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">Check if any line between breakpoints intersect with given points of rectangle</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../PresentationElement.html#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if object and rectangle intersects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="intersectsInternal(int,int,int,int)">
<h3>intersectsInternal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">intersectsInternal</span><wbr/><span class="parameters">(int x,
 int y,
 int width,
 int height)</span></div>
<div class="block">Check intersection with given rectangle. Intersection is counted by getting index of segment in path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - top left x point.</dd>
<dd><code>y</code> - top left y point.</dd>
<dd><code>width</code> - width of rectangle.</dd>
<dd><code>height</code> - height of rectangle.</dd>
<dt>Returns:</dt>
<dd>true if rectangle intersect with any line of path.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isBezierIntersects(int,int,int,int)">
<h3>isBezierIntersects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBezierIntersects</span><wbr/><span class="parameters">(int x,
 int y,
 int width,
 int height)</span></div>
<div class="block">Check if it is bezier path intersection with rectangle.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - top left x point of rectangle.</dd>
<dd><code>y</code> - top left y point of rectangle.</dd>
<dd><code>width</code> - width of rectangle.</dd>
<dd><code>height</code> - height of rectangle.</dd>
<dt>Returns:</dt>
<dd>true if bezier path intersects with rectangle.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIndexOfCoveredPathInternal(int,int,int,int)">
<h3>getIndexOfCoveredPathInternal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIndexOfCoveredPathInternal</span><wbr/><span class="parameters">(int x,
 int y,
 int width,
 int height)</span></div>
<div class="block">This method is used to get segment of path with witch given rectangle has intersection. It will
 be returned index starting from 1 of segment.  This segment is counted using all breakpoints
 (including client and supplier point). If anybody needs end points of segments, you must take
 all breakpoints and take point of return index minus 1 and point of segment's index. If there
 is no intersection, this method return -1.
 For example:
 this method returns value 2.
 segmentIndex = 2;
 Point start and end point of this segment will be:
 Point startPoint = getAllBreakPoints().get(segmentIndex-1);
 Point endPoint = getAllBreakPoints().get(segmentIndex);</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - top left x point of rectangle.</dd>
<dd><code>y</code> - top left y point of rectangle.</dd>
<dd><code>width</code> - width of rectangle.</dd>
<dd><code>height</code> - height of rectangle.</dd>
<dt>Returns:</dt>
<dd>index of segment in path with witch intersect given rectangle.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIndexOfCoveredPath(int,int)">
<h3>getIndexOfCoveredPath</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">int</span> <span class="element-name">getIndexOfCoveredPath</span><wbr/><span class="parameters">(int x,
 int y)</span></div>
<div class="block">This method is used to get segment of path with witch given point has intersection. It will
 be returned index starting from 1 of segment. This segment is counted using all breakpoints
 (including client and supplier point). If anybody needs end points of segments, you must take
 all breakpoints and take point of return index minus 1 and point of segment's index. If there
 is no intersection, this method return -1. If renderer is set for path element, intersection
 will be counted depending on this renderer.
 For example:
 this method returns value 2.
 segmentIndex = 2;
 Point start and end point of this segment will be:
 Point startPoint = getAllBreakPoints().get(segmentIndex-1);
 Point endPoint = getAllBreakPoints().get(segmentIndex);</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - point x value.</dd>
<dd><code>y</code> - point y value.</dd>
<dt>Returns:</dt>
<dd>index of segment of path which intersects with the given point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNewBreakPointIndex(java.awt.Point,java.util.List)">
<h3>getNewBreakPointIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getNewBreakPointIndex</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; brk)</span></div>
<div class="block">Find the nearest breakpoints for new one and
 calculate the position of the new breakpoint in breakpoint vector.
 Used for new breakpoint calculation for Bézier curve.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>point</code> - the new point.</dd>
<dd><code>brk</code> - the breakpoint Vector.</dd>
<dt>Returns:</dt>
<dd>position in that the new point must be inserted in a breakpoint vector.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConnectable(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isConnectable</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">isConnectable</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier,
 @CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client)</span></div>
<div class="block">Checks if this path can connect given two elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>supplier</code> - candidate for path's supplier.</dd>
<dd><code>client</code> - candidate for path's client.</dd>
<dt>Returns:</dt>
<dd>true, if path can connect given elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConnectable(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.Map)">
<h3>isConnectable</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">isConnectable</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier,
 @CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; options)</span></div>
<div class="block">Checks if this path can connect given two elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>supplier</code> - candidate for path's supplier.</dd>
<dd><code>client</code> - candidate for path's client.</dd>
<dd><code>options</code> - options</dd>
<dt>Returns:</dt>
<dd>true, if path can connect given elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMiddlePoint()">
<h3>getMiddlePoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getMiddlePoint</span>()</div>
<div class="block">Calculates and returns middle point of link.
 For this link it is average between supplier's and client's points.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getMiddlePoint()">getMiddlePoint</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>middle point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPointOnPath(java.awt.Point,java.awt.Point,java.util.List,double)">
<h3>getPointOnPath</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getPointOnPath</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplierPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> clientPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; breakpoints,
 double coefficient)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>supplierPoint</code> - supplier end point</dd>
<dd><code>clientPoint</code> - client end point</dd>
<dd><code>breakpoints</code> - list of breakpoints between supplier and client in that order</dd>
<dd><code>coefficient</code> - ratio between 0 and 1 describing position relative to the path length.
                      Provide 0.5 for middle point.</dd>
<dt>Returns:</dt>
<dd>point on path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">Disconnect this link from shapes.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#dispose()">dispose</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="PathConnector.html#dispose()">dispose</a></code> in class <code><a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="atInsert()">
<h3>atInsert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">atInsert</span>()</div>
<div class="block">Inserts ends of link into shapes.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../BaseElement.html#atInsert()">atInsert</a></code> in interface <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#atInsert()">atInsert</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>addConnectedPathElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addConnectedPathElement</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> link)</span></div>
<div class="block">Method to add sub link to this link.
 If link is note anchor it will be added to this link.
 If link is not note anchor, it will be added to generalization tree.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PathConnector.html#addConnectedPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addConnectedPathElement</a></code> in class <code><a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
<dt>Parameters:</dt>
<dd><code>link</code> - link to be added.</dd>
<dt>Returns:</dt>
<dd>true if an element was added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBounds()">
<h3>getBounds</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBounds</span>()</div>
<div class="block">Calculates bounds of this link.
 Returns minimal rectangle in which link can fit.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getBounds()">getBounds</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>bounds of this link.</dd>
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
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getNotCopyBounds</span>()</div>
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
<section class="detail" id="setCachedPathBounds(java.awt.Rectangle)">
<h3>setCachedPathBounds</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setCachedPathBounds</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span></div>
</section>
</li>
<li>
<section class="detail" id="calculatePathBounds(java.awt.Point,java.awt.Point,java.util.List)">
<h3>calculatePathBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">calculatePathBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> client,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; breaks)</span></div>
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
<dd><code><a href="PathConnector.html#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a></code> in class <code><a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRectilinear()">
<h3>setRectilinear</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRectilinear</span>()</div>
<div class="block">Sets link rectilinear property value.</div>
</section>
</li>
<li>
<section class="detail" id="isRectilinear()">
<h3>isRectilinear</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRectilinear</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if link path style is rectilinear.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOblique()">
<h3>isOblique</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOblique</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if link path style is oblique.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeRectilinear()">
<h3>makeRectilinear</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">makeRectilinear</span>()</div>
<div class="block">Makes link rectilinear.</div>
</section>
</li>
<li>
<section class="detail" id="makeRectilinear(boolean)">
<h3>makeRectilinear</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">makeRectilinear</span><wbr/><span class="parameters">(boolean notify)</span></div>
<div class="block">Makes link rectilinear.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notify</code> - notify about this change</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeRedundantBreakPoints(java.util.List)">
<h3>removeRedundantBreakPoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeRedundantBreakPoints</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; vct)</span></div>
<div class="block">Removes redundant breakpoints from link.
 Remove breakpoints only from rectilinear link.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vct</code> - points</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVertical()">
<h3>isVertical</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isVertical</span>()</div>
<div class="block">Indicates if path element is drawn in the diagram which has vertical orientation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram is vertical, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeBreaks(java.util.List)">
<h3>removeBreaks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeBreaks</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; points)</span></div>
<div class="block">Removes all break points if they are covered by client or client bounds.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>points</code> - points</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="swapEnds()">
<h3>swapEnds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">swapEnds</span>()</div>
<div class="block">Swaps ends of the link</div>
</section>
</li>
<li>
<section class="detail" id="setClient(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>setClient</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setClient</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> shape)</span></div>
<div class="block">Sets client for this link.
 Changes parent object to the parent of client.
 Client's parent will always contain incoming links.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shape</code> - shape to check</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="moveLinkToClientParent(boolean)">
<h3>moveLinkToClientParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">moveLinkToClientParent</span><wbr/><span class="parameters">(boolean simpleAdd)</span></div>
</section>
</li>
<li>
<section class="detail" id="internalSnapToGrid(float)">
<h3>internalSnapToGrid</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalSnapToGrid</span><wbr/><span class="parameters">(float step)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#internalSnapToGrid(float)">internalSnapToGrid</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
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
<section class="detail" id="canChangeSupplier()">
<h3>canChangeSupplier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canChangeSupplier</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if view can change supplier.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canChangeClient()">
<h3>canChangeClient</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canChangeClient</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if view can change client</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canClearBreakPoints()">
<h3>canClearBreakPoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canClearBreakPoints</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if link can be modified (all break points can be removed):</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canChangeLineStyle()">
<h3>canChangeLineStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canChangeLineStyle</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this link can change line style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">
<h3>internalApplyProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalApplyProperties</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</span></div>
<div class="block">Applies properties</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>changer</code> - new properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>draw</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">draw</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
<div class="block">abstract method for drawing ViewObject object
 used to draw object on graphics</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Parameters:</dt>
<dd><code>context</code> - Graphics on which object should be drawn</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>getIntersection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getIntersection</span><wbr/><span class="parameters">(int x,
 int y,
 @CheckForNull
 <a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="useOtherExistingElement()">
<h3>useOtherExistingElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.utils.Pair&lt;com.dassault_systemes.modeler.foundation.model.ModelElement,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;com.dassault_systemes.modeler.foundation.model.ModelElement&gt;&gt;</span> <span class="element-name">useOtherExistingElement</span>()</div>
<div class="block">Finds and returns other model element which  is semantically equivalent to this path model element.
 Found element can be modified.
 This method is invoked during new PathElement creation and purpose of it is to reuse existing model elements instead of creating new ones.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBezierPath()">
<h3>getBezierPath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html" title="class or interface in java.awt.geom">GeneralPath</a></span> <span class="element-name">getBezierPath</span>()</div>
<div class="block">Calculates path for bezier curve drawing.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>bezier path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isBezier()">
<h3>isBezier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBezier</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if LINK_LINE_STYLE property value equals to BEZIER.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLinkLineStyleDefined()">
<h3>isLinkLineStyleDefined</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLinkLineStyleDefined</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLinkLineStyle()">
<h3>getLinkLineStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLinkLineStyle</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>LINK_LINE_STYLE property value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetLinkLineStyle(java.lang.String)">
<h3>sSetLinkLineStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetLinkLineStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> style)</span></div>
<div class="block">Change value of LINK_LINE_STYLE property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - the line style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLinkLineStyle(java.lang.String)">
<h3>setLinkLineStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLinkLineStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> style)</span></div>
<div class="block">sets LINK_LINE_STYLE property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - the line style.</dd>
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
<dd><code><a href="../PresentationElement.html#internalSilentApply()">internalSilentApply</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleRemoveBreaksAction()">
<h3>handleRemoveBreaksAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.editing.Command</span> <span class="element-name">handleRemoveBreaksAction</span>()</div>
</section>
</li>
<li>
<section class="detail" id="nextStyle()">
<h3>nextStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">nextStyle</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>link style for TOGGLE LINK STYLE command.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBezierPath(java.util.List)">
<h3>getBezierPath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html" title="class or interface in java.awt.geom">GeneralPath</a></span> <span class="element-name">getBezierPath</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; points)</span></div>
<div class="block">Calculates path from breakpoints for bezier curve drawing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>points</code> - points</dd>
<dt>Returns:</dt>
<dd>path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prepareForLineDrawing(java.awt.Graphics2D,boolean)">
<h3>prepareForLineDrawing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">prepareForLineDrawing</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 boolean line)</span></div>
<div class="block">Prepares graphics for line drawing.
 Calls super prepareForLineDrawing and sets stroke.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>g</code> - graphics</dd>
<dd><code>line</code> - true if for line, false if for adornments also</dd>
<dt>Returns:</dt>
<dd>stroke</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyStrokeForLineDrawing(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Graphics2D,boolean,java.awt.BasicStroke)">
<h3>applyStrokeForLineDrawing</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">applyStrokeForLineDrawing</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pathElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 boolean line,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a> stroke)</span></div>
</section>
</li>
<li>
<section class="detail" id="internalGetPresentationElementStroke(boolean,int)">
<h3>internalGetPresentationElementStroke</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">internalGetPresentationElementStroke</span><wbr/><span class="parameters">(boolean line,
 int width)</span></div>
<div class="block">This method must be overridden, if you need to use DASHED_STROKE or another one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>line</code> - true if for line, false if for adornments also</dd>
<dd><code>width</code> - width</dd>
<dt>Returns:</dt>
<dd>the stroke for line drawing ( by default SOLID_STROKE).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalGetPresentationElementStroke(boolean,int,int)">
<h3>internalGetPresentationElementStroke</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">internalGetPresentationElementStroke</span><wbr/><span class="parameters">(boolean line,
 int lineStyle,
 int width)</span></div>
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
<dd><code><a href="../PresentationElement.html#getBoundsToRepaint()">getBoundsToRepaint</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>rectangle of bounds</dd>
<dt>Throws:</dt>
<dd><code><a href="../NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFillStrategy()">
<h3>createFillStrategy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.FillStrategy</span> <span class="element-name">createFillStrategy</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#createFillStrategy()">createFillStrategy</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
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
<section class="detail" id="getPathPainter()">
<h3>getPathPainter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.paths.painters.PathPainter&lt;<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</span> <span class="element-name">getPathPainter</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setPathPainter(com.nomagic.magicdraw.uml.symbols.paths.painters.PathPainter)">
<h3>setPathPainter</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">setPathPainter</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.paths.painters.PathPainter pathPainter)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSupplierConnectionType()">
<h3>getSupplierConnectionType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSupplierConnectionType</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getClientConnectionType()">
<h3>getClientConnectionType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getClientConnectionType</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDefaultParentForData()">
<h3>getDefaultParentForData</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getDefaultParentForData</span>()</div>
<div class="block">Presentation element could suggest parent, which would be more acceptable, than adding to the client
 If returning null, general mechanism will work</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent for data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasClientPoint()">
<h3>hasClientPoint</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">hasClientPoint</span>()</div>
<div class="block">Check if client point is already not null</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if client point is set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasSupplierPoint()">
<h3>hasSupplierPoint</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">hasSupplierPoint</span>()</div>
<div class="block">Check if supplier point is already not null</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if supplier point is set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRounded()">
<h3>isRounded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRounded</span>()</div>
<div class="block">Returns value of the "Is Rounded" path symbol property.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value of the "Is Rounded" property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRounded(boolean)">
<h3>setRounded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRounded</span><wbr/><span class="parameters">(boolean rounded)</span></div>
<div class="block">Sets value of the "Is Rounded" path symbol property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rounded</code> - - value of the "Is Rounded" property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetRounded(boolean)">
<h3>sSetRounded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetRounded</span><wbr/><span class="parameters">(boolean rounded)</span></div>
<div class="block">Sets value of the "Is Rounded" path symbol property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rounded</code> - - value of the "Is Rounded" property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseFlowLayoutLogic()">
<h3>isUseFlowLayoutLogic</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseFlowLayoutLogic</span>()</div>
<div class="block">Indicates if smart path/shape edit should be used in this diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if smart symbol editing should be used, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSmartLayoutNeeded()">
<h3>isSmartLayoutNeeded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSmartLayoutNeeded</span>()</div>
<div class="block">Returns smart layout needed flag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value of smart layout needed flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSmartLayoutNeeded(boolean)">
<h3>setSmartLayoutNeeded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSmartLayoutNeeded</span><wbr/><span class="parameters">(boolean smartLayoutNeeded)</span></div>
<div class="block">Sets smart layout needed flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>smartLayoutNeeded</code> - - smart layout needed flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetCache()">
<h3>resetCache</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">resetCache</span>()</div>
</section>
</li>
<li>
<section class="detail" id="cacheValues(java.awt.Point,java.awt.Point,java.awt.Point,java.awt.Point,java.util.List)">
<h3>cacheValues</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">cacheValues</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> cachedActualSupplierDrawPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> cachedActualClientDrawPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> cacheSupplierDrawPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> cacheClientDrawPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; cacheBreakPoints)</span></div>
</section>
</li>
<li>
<section class="detail" id="cacheActualDrawPoints(java.awt.Point,java.awt.Point,java.util.List)">
<h3>cacheActualDrawPoints</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">cacheActualDrawPoints</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplierDrawPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> clientDrawPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; breakPoints)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCachedActualClientDrawPoint()">
<h3>getCachedActualClientDrawPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getCachedActualClientDrawPoint</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCachedActualSupplierDrawPoint()">
<h3>getCachedActualSupplierDrawPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getCachedActualSupplierDrawPoint</span>()</div>
</section>
</li>
<li>
<section class="detail" id="resizeParent()">
<h3>resizeParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resizeParent</span>()</div>
<div class="block">Do nothing, because path does not affect parent size</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#resizeParent()">resizeParent</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCustomSupplierPoint()">
<h3>getCustomSupplierPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getCustomSupplierPoint</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCustomSupplierPoint(java.awt.Point)">
<h3>setCustomSupplierPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomSupplierPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCustomClientPoint()">
<h3>getCustomClientPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getCustomClientPoint</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCustomClientPoint(java.awt.Point)">
<h3>setCustomClientPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomClientPoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point)</span></div>
</section>
</li>
<li>
<section class="detail" id="preDisposeOnUpdate()">
<h3>preDisposeOnUpdate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">preDisposeOnUpdate</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../PresentationElement.html#preDisposeOnUpdate()">PresentationElement</a></code></span></div>
<div class="block">Validate symbol against model and try to fix it before actual symbol update. If symbol is not valid and can not be fixed,
 request symbol dispose by returning true.
 Check if symbol should be disposed, because model does not correspond to symbol.
 This may happen for example if path supplier or client in model is changed, but path still is connected to symbols of old ends.
 <p>
 Method also can fix symbol if possible - for example reconnect path to other symbols in diagram and etc.</p></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#preDisposeOnUpdate()">preDisposeOnUpdate</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
<dt>Returns:</dt>
<dd>true if symbol must be disposed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSmartListenerConfig(java.util.List)">
<h3>createSmartListenerConfig</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createSmartListenerConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PathConnector.html#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a></code> in class <code><a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalMovedAsToSelf(int,int)">
<h3>internalMovedAsToSelf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalMovedAsToSelf</span><wbr/><span class="parameters">(int dx,
 int dy)</span></div>
<div class="block">This is an internal method to notify a path that it was moved by connecting shape as the path "to self"</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dx</code> - delta x</dd>
<dd><code>dy</code> - delta y</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>sSetParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetParent</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span></div>
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
<section class="detail" id="findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">
<h3>findOwnerForElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type">com.dassault_systemes.modeler.foundation.model.ModelElement</span> <span class="element-name">findOwnerForElement</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../PresentationElement.html#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a></code> in class <code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">
<h3>findOwnerForElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.model.ModelElement</span> <span class="element-name">findOwnerForElement</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> newParent,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)</span></div>
</section>
</li>
<li>
<section class="detail" id="connectModelElement(com.nomagic.magicdraw.uml.symbols.paths.ConnectModelElementParticipant)">
<h3>connectModelElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">connectModelElement</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.paths.ConnectModelElementParticipant participant)</span></div>
<div class="block">Connects <code>ModelElement</code> of this path to related elements of a given client and supplier</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>participant</code> - participant of this operation</dd>
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
