# JAVA OPENAPI: PresentationElement (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/PresentationElement.html
- source_path: `com/nomagic/magicdraw/uml/symbols/PresentationElement.html`
- source_sha256: `9710cd01a3a3db3fb348dcfd903ae60ef3eef11f2f0f0514253eb51241f64e46`
- captured_utc: `2026-07-14T16:55:58.745494+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class PresentationElement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
com.nomagic.magicdraw.uml.symbols.PresentationElement

All Implemented Interfaces:
`[BaseElement](../BaseElement.html)`, `[MDElement](../MDElement.html)`, `[ModelElementProvider](../ModelElementProvider.html)`, `[NameOwner](../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`, `[PathConnector](paths/PathConnector.html)`

@OpenApipublic abstract classPresentationElement
extends com.nomagic.magicdraw.uml.MDElementImpl
implements [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html), [ModelElementProvider](../ModelElementProvider.html), [NameOwner](../../utils/NameOwner.html)

Base class for all visual elements used in the UML diagrams.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[DASHED_STROKE](#DASHED_STROKE)`
Dashed path stroke.
`static final int`
`[DEFAULT_LINE_WIDTH](#DEFAULT_LINE_WIDTH)`

`static final int`
`[DOTTED_STROKE](#DOTTED_STROKE)`
Dotted path stroke.
`static final int`
`[HANDLE_SIZE](#HANDLE_SIZE)`

`static final double`
`[MAX_LINE_WIDTH](#MAX_LINE_WIDTH)`

`static final double`
`[MIN_LINE_WIDTH](#MIN_LINE_WIDTH)`

`protected com.dassault_systemes.modeler.foundation.diagram.style.PresentationElementStyle`
`[peStyle](#peStyle)`

`static final int`
`[SHADOW_WIDTH](#SHADOW_WIDTH)`
Symbol shadow width in pixels
`static final int`
`[SOLID_STROKE](#SOLID_STROKE)`
Solid path stroke.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PresentationElement](#%3Cinit%3E())()`

`[PresentationElement](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) parent)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`final void`
`[addPresentationElement](#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) element)`
Add given child to this symbol.
`void`
`[addPresentationElement](#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int))([PresentationElement](PresentationElement.html) element,
 int index)`
Add given child to this symbol at given index
`void`
`[addPresentationElementWithoutResize](#addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) element)`

`final void`
`[addProperty](#addProperty(com.nomagic.magicdraw.properties.Property))([Property](../../properties/Property.html) prop)`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`PresentationElementsManager.addProperty(PresentationElement, Property)`](../../openapi/uml/PresentationElementsManager.html#addProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.properties.Property)).
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[adjustBoundsBeforeChange](#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rec,
 boolean autosizeOperation,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> movedTogether)`
Validate bounds before bounds change operation
`void`
`[adjustChildBounds](#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds,
 [PresentationElement](PresentationElement.html) element)`
For adjusting child bounds when child type is not known but bounds should be corrected.
`void`
`[adjustChildBoundsForMoving](#adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds,
 [PresentationElement](PresentationElement.html) element)`
For adjusting child bounds when child type is not known but bounds should be corrected.
`boolean`
`[alwaysShowTooltip](#alwaysShowTooltip())()`

`final void`
`[applyProperties](#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)`
Applies properties from given property manager
`boolean`
`[askDeleteDataConfirmation](#askDeleteDataConfirmation())()`
Declared as interface with default implementation for subclasses.
`void`
`[atInsert](#atInsert())()`
Invalidates object at insert
`protected void`
`[atInsertChildren](#atInsertChildren())()`

`void`
`[autosizeAndResizeManipulatedParent](#autosizeAndResizeManipulatedParent())()`
Autosize and resize manipulated element - itself(if this element has manipulator) or
 manipulated parent.
`void`
`[autosizeAndResizeParent](#autosizeAndResizeParent())()`
Resize itself and initiate parent resize
`boolean`
`[beforeDelete](#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection))(com.dassault_systemes.modeler.foundation.editing.CompositeCommand deleteCommand,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) removeTogether)`
Method is called before deleting symbol with user "DELETE" action
`final void`
`[boundsChanged](#boundsChanged())()`

`final void`
`[boundsChanged](#boundsChanged(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`

`final boolean`
`[canAddChild](#canAddChild(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) element)`

`boolean`
`[canAddChild](#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) symbol)`
Check of given symbol can be added as child into this symbol.
`final boolean`
`[canAddInstance](#canAddInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) element)`
Checks if this object can add element of given type.
`boolean`
`[canAddInstance](#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) symbol)`
Object view has no children.
`protected boolean`
`[canBeDisposedOnUpdate](#canBeDisposedOnUpdate())()`
Some symbols removes themselves on update if they are not valid by model anymore.
`boolean`
`[canChangeElementOwner](#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> movedTogether,
 [BaseElement](../BaseElement.html) newParent)`
Returns true, if symbol does not restrict it's element ownership change
`boolean`
`[canChangeParent](#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [PresentationElement](PresentationElement.html)> movedTogether,
 [BaseElement](../BaseElement.html) newParent,
 boolean changeElementParent)`
Returns true, if element can change parent.
`final boolean`
`[canChangeParent](#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) children,
 [BaseElement](../BaseElement.html) newParent)`
Returns true, if element can change parent.
`protected boolean`
`[canFill](#canFill())()`

`boolean`
`[canHavePaths](#canHavePaths())()`

`void`
`[changeProperties](#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)`

`boolean`
`[checkElementOwnerOnChange](#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) child)`

`protected com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility`
`[checkProxyVisibility](#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility))(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)`

`protected boolean`
`[checkShowsProxy](#checkShowsProxy())()`

`protected final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[childrenForMoving](#childrenForMoving())()`
Calculates selected children for moving or takes result from cached.
`void`
`[clearShowsProxy](#clearShowsProxy())()`

`[PresentationElement](PresentationElement.html)`
`[clone](#clone())()`

`final void`
`[collectSubManipulatedElements](#collectSubManipulatedElements(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> col)`
Collects all visible and manipulated elements in this hierarchy.
`final void`
`[collectSubPresentationElements](#collectSubPresentationElements(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collection)`
Collects all sub-presentation elements into given collection.
`final void`
`[collectSubPresentationElements](#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collection,
 [Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[PresentationElement](PresentationElement.html)> predicate)`
Collects all sub-presentation elements that match given predicate into given collection.
`final void`
`[collectSubShowingPresentationElements](#collectSubShowingPresentationElements(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> col)`
Collect all visible children starting from current element.
`final boolean`
`[coversPoint](#coversPoint(int,int))(int x,
 int y)`
checks if object covers provided point
`abstract boolean`
`[coversPoint](#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
checks if object covers provided point
`com.nomagic.magicdraw.uml.symbols.FillStrategy`
`[createFillStrategy](#createFillStrategy())()`

`protected com.dassault_systemes.modeler.foundation.diagram.style.PresentationElementStyle`
`[createPresentationElementStyle](#createPresentationElementStyle())()`
Creates the presentation element style for this presentation element.
`final void`
`[createPropertyChangeListener](#createPropertyChangeListener())()`

`protected void`
`[createSmartListenerConfig](#createSmartListenerConfig(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)`

`void`
`[dispose](#dispose())()`
disposes ends of links when link is deleted
`protected void`
`[disposeChildren](#disposeChildren())()`
Removes all children from itself.
`protected void`
`[disposePropertyChangeListener](#disposePropertyChangeListener())()`

`void`
`[draw](#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`
Draw symbol using renderer or symbol specific draw if renderer is not available.
`void`
`[drawBackground](#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`final void`
`[drawSymbol](#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`
Draw symbol as defined by standard notation.
`void`
`[drawSymbolBackground](#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[dynamicFillColor](#dynamicFillColor())()`

`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[dynamicLineColor](#dynamicLineColor())()`

`int`
`[dynamicLineWidth](#dynamicLineWidth())()`

`int`
`[dynamicLineWidth](#dynamicLineWidth(int))(int width)`

`boolean`
`[dynamicPaintShadow](#dynamicPaintShadow())()`

`final [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[dynamicStroke](#dynamicStroke())()`

`[BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[dynamicStroke](#dynamicStroke(int))(int width)`

`[BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[dynamicStroke](#dynamicStroke(java.awt.BasicStroke))([BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) stroke)`

`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[dynamicStyleFillColor](#dynamicStyleFillColor(java.awt.Color,boolean))([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color,
 boolean useFill)`

`final [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[dynamicStyleLineColor](#dynamicStyleLineColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)`

`final [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[dynamicStyleTextColor](#dynamicStyleTextColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)`

`final int`
`[dynamicStyleTransparency](#dynamicStyleTransparency())()`

`final int`
`[dynamicStyleTransparency](#dynamicStyleTransparency(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) target)`

`protected <T> T`
`[dynamicStyleValue](#dynamicStyleValue(T,java.util.function.BiFunction))(T merged,
 [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html)<com.dassault_systemes.modeler.foundation.common.style.DynamicStyle,T,T> valueProvider)`

`com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition`
`[dynamicTextAlignment](#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition))(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition target)`

`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[dynamicTextColor](#dynamicTextColor())()`

`final void`
`[editName](#editName(java.awt.event.KeyEvent))([KeyEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/KeyEvent.html) evt)`
Starts online diagram editing for a symbol
`void`
`[editName](#editName(java.awt.event.KeyEvent,java.util.Map))([KeyEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/KeyEvent.html) evt,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> textEditorOptions)`
Starts online diagram editing for a symbol
`com.dassault_systemes.modeler.foundation.model.ModelElement`
`[findOwnerForChildElement](#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) child)`
Returns element owner for given child.
`com.dassault_systemes.modeler.foundation.model.ModelElement`
`[findOwnerForElement](#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext))([PresentationElement](PresentationElement.html) newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)`

`static [PresentationElement](PresentationElement.html)`
`[findPresentationElement](#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> elements,
 com.dassault_systemes.modeler.foundation.model.ModelElement modelElement)`
Finds presentation element with given Element among given elements
`void`
`[firePropertyChange](#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)`
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[generateID](#generateID())()`
Generate ID.
`[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`
`[getAbstractDiagramPresentationElement](#getAbstractDiagramPresentationElement())()`
Returns diagram of this presentation element.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getActualElement](#getActualElement())()`
Because some views returns theirs parent model element, we do not know have they this member
 set or not.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.uml.symbols.SymbolDecorator>`
`[getAdditionalRenderersToNotifyOnPropertiesChange](#getAdditionalRenderersToNotifyOnPropertiesChange())()`

`final [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[]`
`[getAssignableModelElementsClasses](#getAssignableModelElementsClasses())()`
Returns an array of ModelElements classes that can be assigned as ModelElement to this
 PresentationElement.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBounds](#getBounds())()`
Method returns bounds of this element.
`final [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html)`
`[getBoundsShape](#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape))([ConverterToShape](ConverterToShape.html) converterToShape)`
Provides a bounding shape of the symbol
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBoundsToRepaint](#getBoundsToRepaint())()`
Return bounds of the symbol that must be repainted.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBoundsWithChildrenOnEdge](#getBoundsWithChildrenOnEdge())()`

`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getCenterlinePoint](#getCenterlinePoint())()`
Gets a point for centerline drawing.
`int`
`[getCenterlinePointX](#getCenterlinePointX())()`
Gets x coordinate for centerline drawing.
`int`
`[getCenterlinePointY](#getCenterlinePointY())()`
Gets y coordinate for centerline drawing.
`[PresentationElement](PresentationElement.html)`
`[getChildPresentationElementForContextMenu](#getChildPresentationElementForContextMenu(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)`
Returns child element for showing context menu.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getChildrenWithSymbolProperties](#getChildrenWithSymbolProperties())()`

`protected final [SmartListenerConfig](../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)`
`[getConfiguration](#getConfiguration())()`

`final [DiagramPresentationElement](DiagramPresentationElement.html)`
`[getDiagramPresentationElement](#getDiagramPresentationElement())()`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`DiagramPresentationElement.get(PresentationElement)`](DiagramPresentationElement.html#get(com.nomagic.magicdraw.uml.symbols.PresentationElement)).Will be removed in 2026x.
`[DiagramSurface](DiagramSurface.html)`
`[getDiagramSurface](#getDiagramSurface())()`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`DiagramSurface.getDiagramSurface(PresentationElement)`](DiagramSurface.html#getDiagramSurface(com.nomagic.magicdraw.uml.symbols.PresentationElement)).
`[Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)<[PresentationElement](PresentationElement.html)>`
`[getDrawComparator](#getDrawComparator())()`

`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)>`
`[getDynamicConfigurations](#getDynamicConfigurations())()`
Gets non-cacheable smart listener configurations.
`[PresentationElement](PresentationElement.html)`
`[getDynamicStyleOwner](#getDynamicStyleOwner())()`

`com.dassault_systemes.modeler.foundation.diagram.style.StylePropertyDelegate`
`[getEffectiveStyleDelegate](#getEffectiveStyleDelegate())()`

`final [PresentationElement](PresentationElement.html)`
`[getEffectiveStyleOwner](#getEffectiveStyleOwner())()`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement())()`
Returns model element of this presentation element.
`final [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getElementsForRelationshipConnecting](#getElementsForRelationshipConnecting())()`
The same as getElementsForLinkConnecting(), just takes into account SymbolDecorators
`final [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElementToConnectRelationship](#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 boolean asClient)`
The same as `#internalGetElementToConnectRelationship(Element, boolean)`, just takes into account SymbolDecorators
`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[getFillColor](#getFillColor())()`
Returns fill color
`[Font](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html)`
`[getFont](#getFont())()`
Gets font of this object view.
`final int`
`[getFontHeight](#getFontHeight())()`
Gets font height.
`static [FontRenderContext](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/font/FontRenderContext.html)`
`[getFontRenderContext](#getFontRenderContext())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHumanName](#getHumanName())()`
Returns human representation of the data type
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHumanType](#getHumanType())()`
Returns human representation of the data type
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getIntersection](#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement))(int x,
 int y,
 [PathElement](paths/PathElement.html) path)`

`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[getLineColor](#getLineColor())()`
Returns line color
`int`
`[getLineWidth](#getLineWidth())()`

`final [PresentationElement](PresentationElement.html)`
`[getManipulatedElementAt](#getManipulatedElementAt(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)`
Gets manipulated symbol at specified point pt.
`[PresentationElement](PresentationElement.html)`
`[getManipulatedElementAt](#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind intersectionKind)`
Gets manipulated symbol at specified point pt.
`[PresentationElement](PresentationElement.html)`
`[getManipulatedElementAt](#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)`
Gets manipulate symbol at specified point pt.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getManipulatedIntersectionWith](#getManipulatedIntersectionWith(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)`
Returns vector of manipulated objects whose intersect with given rectangle
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getManipulatedIntersectionWith](#getManipulatedIntersectionWith(java.awt.Rectangle,boolean))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect,
 boolean completelyCovered)`
Returns vector of manipulated objects whose intersect with given rectangle
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getManipulatedIntersectionWith](#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect,
 boolean completelyCovered,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Returns vector of manipulated objects whose intersect with given rectangle
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getManipulatedIntersectionWith](#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Returns vector of manipulated objects whose intersect with given rectangle
`final [PresentationElement](PresentationElement.html)`
`[getManipulatedParent](#getManipulatedParent())()`

`final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getManipulatedPresentationElements](#getManipulatedPresentationElements())()`
Returns a list of children of this element those have manipulator.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getManipulationBounds](#getManipulationBounds(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint)`
Gets manipulation bounds of the symbol.
`[UnmodifiableDimension](../../../ui/UnmodifiableDimension.html)`
`[getManipulationPreferredDimension](#getManipulationPreferredDimension())()`

`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getMiddlePoint](#getMiddlePoint())()`
Returns middle point of this element.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getMiddlePoint](#getMiddlePoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint)`
Gets middle point of this view,
`int`
`[getMiddlePointX](#getMiddlePointX())()`

`protected int`
`[getMiddlePointX](#getMiddlePointX(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint)`

`int`
`[getMiddlePointY](#getMiddlePointY())()`

`protected int`
`[getMiddlePointY](#getMiddlePointY(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint)`

`[UnmodifiableDimension](../../../ui/UnmodifiableDimension.html)`
`[getMinimumDimension](#getMinimumDimension())()`
get minimum possible size for object
`com.dassault_systemes.modeler.foundation.model.ModelElement`
`[getModelElement](#getModelElement())()`

`final [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends com.dassault_systemes.modeler.foundation.model.ModelElement>`
`[getModelElementsForRelationshipConnecting](#getModelElementsForRelationshipConnecting())()`
Returns all possible element that can be used for relationships connecting.
`final com.dassault_systemes.modeler.foundation.model.ModelElement`
`[getModelElementToConnectRelationship](#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean))(com.dassault_systemes.modeler.foundation.model.ModelElement relationship,
 boolean asClient)`
The same as [`internalGetModelElementToConnectRelationship(ModelElement, boolean)`](#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), just takes into account SymbolDecorators
`com.dassault_systemes.modeler.foundation.model.ModelElement`
`[getModelElementToMove](#getModelElementToMove())()`
Returns element that should be used for during "move" operation.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getNotCopyBounds](#getNotCopyBounds())()`
get not copy bounds of object throws NoRectangleDefinedException
`protected int`
`[getNotZoomedTolerance](#getNotZoomedTolerance())()`

`[BaseElement](../BaseElement.html)`
`[getObjectParent](#getObjectParent())()`
Returns the presentation element parent.
`com.dassault_systemes.modeler.foundation.diagram.style.StylePropertyDelegate`
`[getOwnStyleDelegate](#getOwnStyleDelegate())()`

`final [PresentationElement](PresentationElement.html)`
`[getParent](#getParent())()`
Returns parent of this element.
`[PresentationElement](PresentationElement.html)`
`[getParentSymbolStyleOwner](#getParentSymbolStyleOwner())()`
Returns parent to which this symbol delegates style attributes related functionality.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getPreferredBounds](#getPreferredBounds())()`
Calculate the smallest rectangle which would fit all contained shapes
`[UnmodifiableDimension](../../../ui/UnmodifiableDimension.html)`
`[getPreferredDimension](#getPreferredDimension())()`
Returns preferable dimension of the element.
`[UnmodifiableDimension](../../../ui/UnmodifiableDimension.html)`
`[getPreferredDimensionForAutosize](#getPreferredDimensionForAutosize())()`
Returns preferable dimension of the element for autosize.This implementation simple returns
 preferred size.
`final [Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html)`
`[getPreferredSize](#getPreferredSize())()`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`getPreferredDimension()`](#getPreferredDimension()).
`final [PresentationElement](PresentationElement.html)`
`[getPresentationElementAt](#getPresentationElementAt(int))(int index)`
Gets object view at specified position from container
`final [PresentationElement](PresentationElement.html)`
`[getPresentationElementAt](#getPresentationElementAt(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p)`
Gets object view at point.
`[PresentationElement](PresentationElement.html)`
`[getPresentationElementAt](#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Gets object view at point.
`final [PresentationElement](PresentationElement.html)`
`[getPresentationElementAt](#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)`
Gets object view at point.
`[PresentationElement](PresentationElement.html)`
`[getPresentationElementAt](#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Gets object view at point.
`final int`
`[getPresentationElementCount](#getPresentationElementCount())()`
Returns children count in container.
`int`
`[getPresentationElementIndex](#getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) element)`
Get index of the given presentation element in the container.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getPresentationElements](#getPresentationElements())()`
Returns all children of this element
`final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getPresentationElementsAt](#getPresentationElementsAt(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p)`
Gets objects at point.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getPresentationElementsAt](#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Gets objects at point.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getPresentationElementsAt](#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)`
Gets object view at point.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getPresentationElementsAt](#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
Gets object view at point.
`final [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getPresentationElementStroke](#getPresentationElementStroke())()`
Return a stroke used to paint symbol's main part
`final [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getPresentationElementStroke](#getPresentationElementStroke(int))(int width)`
Return a stroke used to paint symbol's main part
`[Project](../../core/Project.html)`
`[getProjectImpl](#getProjectImpl())()`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`Project.getProject(BaseElement)`](../../core/Project.html#getProject(com.nomagic.magicdraw.uml.BaseElement)).
`final [Property](../../properties/Property.html)`
`[getProperty](#getProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyId)`
Deprecated, for removal: This API element is subject to removal in a future version.
use `PresentationElementsManager#getProperty(PresentationElement)`.
`final [PropertyManager](../../properties/PropertyManager.html)`
`[getPropertyManager](#getPropertyManager())()`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`PresentationElementsManager.addProperty(PresentationElement, Property)`](../../openapi/uml/PresentationElementsManager.html#addProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.properties.Property)).
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPropertyManagerName](#getPropertyManagerName())()`

`com.nomagic.magicdraw.uml.symbols.SymbolDecorator`
`[getRenderer](#getRenderer())()`
Gets rendered which could decorate this symbol.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getSelected](#getSelected())()`
Returns a list of selected elements in the diagram.
`static [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(float,int,int,float,float%5B%5D,float))(float width,
 int cap,
 int join,
 float miterLimit,
 float[] dash,
 float dash_phase)`
Get cached stroke.
`static [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(int))(int lineStyle)`
Get cached stroke of given style and default width.
`static [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(int,int))(int lineStyle,
 int width)`
Get cached stroke of given style and width.
`static [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(int,int,int))(int lineStyle,
 int width,
 int join)`
Get cached stroke of given style, width and join.
`static [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(int,int,int,int))(int lineStyle,
 int width,
 int join,
 int cap)`
Get cached stroke of given style, width and join.
`static [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(java.awt.BasicStroke,int))([BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) stroke,
 int width)`
Get cached stroke of given width.
`com.dassault_systemes.modeler.foundation.diagram.style.PresentationElementStyle`
`[getStyle](#getStyle())()`

`protected static com.nomagic.magicdraw.uml.symbols.SymbolDecorator`
`[getSymbolRenderer](#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) presentationElement)`

`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[getTextColor](#getTextColor())()`

`final int`
`[getTolerance](#getTolerance())()`
Returns tolerance
`com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility`
`[getVisibility](#getVisibility())()`

`final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getVisiblePresentationElements](#getVisiblePresentationElements())()`

`protected void`
`[handleModelDelete](#handleModelDelete())()`
Handles model element delete property Change event.
`final boolean`
`[hasManipulatedPresentationElements](#hasManipulatedPresentationElements())()`

`boolean`
`[hasManipulator](#hasManipulator())()`
Returns true, if view has manipulator (is selectable)
`boolean`
`[hasSharedModelElement](#hasSharedModelElement())()`
Returns true if `ModelElement` of this symbol can represented with other symbol.
`void`
`[initialize](#initialize())()`
Initialize symbol and its children state.
`final void`
`[initializeAndAutosize](#initializeAndAutosize())()`
Initialize symbol and call autosize recursively
`protected void`
`[internalApplyProperties](#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger))(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)`
Applies properties from given property manager
`protected void`
`[internalBeforeUpdate](#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator))(com.nomagic.magicdraw.uml.symbols.SymbolDecorator renderer)`

`protected void`
`[internalCreatePropertyChangeListener](#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData))(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData data)`

`[Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html)`
`[internalGetBoundsShape](#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape))([ConverterToShape](ConverterToShape.html) converterToShape)`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends com.dassault_systemes.modeler.foundation.model.ModelElement>`
`[internalGetModelElementsForRelationshipConnecting](#internalGetModelElementsForRelationshipConnecting())()`
Returns all possible element that can be used for some relationship connecting.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends com.dassault_systemes.modeler.foundation.model.ModelElement>`
`[internalGetModelElementsForRelationshipConnecting](#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) symbol)`

`com.dassault_systemes.modeler.foundation.model.ModelElement`
`[internalGetModelElementToConnectRelationship](#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean))(com.dassault_systemes.modeler.foundation.model.ModelElement relationship,
 boolean asClient)`
Returns element that should be used for given relationship connecting.
`[BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[internalGetPresentationElementStroke](#internalGetPresentationElementStroke(int))(int width)`
Return a stroke used to paint symbol's main part
`protected [Font](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html)`
`[internalGetSpecificFont](#internalGetSpecificFont())()`

`protected [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[internalGetSpecificTextColor](#internalGetSpecificTextColor())()`

`boolean`
`[internalIsSuitableToConnectRelationship](#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd))(com.dassault_systemes.modeler.foundation.model.RelationshipEnd<?> end)`

`static boolean`
`[internalIsSuitableToConnectRelationship](#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd))([PresentationElement](PresentationElement.html) symbol,
 com.dassault_systemes.modeler.foundation.model.RelationshipEnd<?> end)`

`void`
`[internalSilentApply](#internalSilentApply())()`
Silently applies all properties after initialization
`protected void`
`[internalSnapToGrid](#internalSnapToGrid(float))(float step)`

`protected void`
`[internalSnapToGrid](#internalSnapToGrid(java.awt.Point,float))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p,
 float step)`

`protected void`
`[internalUpdatePresentationElement](#internalUpdatePresentationElement())()`
Internal symbol update method for subclassing.
`final boolean`
`[intersects](#intersects(int,int,int,int))(int x,
 int y,
 int width,
 int height)`
checks whether object intersects with given rectangle
`abstract boolean`
`[intersects](#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind))(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)`
checks whether object intersects with given rectangle
`boolean`
`[invalidate](#invalidate())()`
Invalidates this element.
`boolean`
`[isCanChildrenChangeEdge](#isCanChildrenChangeEdge())()`

`boolean`
`[isChildVisible](#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) child)`
Returns true if given child of this object is visible.
`boolean`
`[isContentHidden](#isContentHidden())()`

`protected boolean`
`[isCreateElementListener](#isCreateElementListener())()`

`boolean`
`[isDetectable](#isDetectable())()`
Not detectable symbols are not drawn even they are visible.
`boolean`
`[isDisposed](#isDisposed())()`
Checks if element was explicitly disposed by calling [`dispose()`](#dispose()) method.
`boolean`
`[isLayouting](#isLayouting())()`

`boolean`
`[isMovableByMoveManager](#isMovableByMoveManager())()`
Method indicates if object of this instance must be registered in move manager.
`boolean`
`[isNotNull](#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`boolean`
`[isParentOf](#isParentOf(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) obj)`
Returns true, if current element is parent of given element.
`boolean`
`[isParentOf](#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) child)`
Checks if object is child of this object.
`boolean`
`[isPreserveProportionsWhenGrowing](#isPreserveProportionsWhenGrowing())()`
Controls if the symbol should preserve proportions when growing.
`boolean`
`[isSelected](#isSelected())()`
Returns true, if this element is selected in the diagram.
`boolean`
`[isShowElementTypeAsLabel](#isShowElementTypeAsLabel())()`

`boolean`
`[isShowsProxy](#isShowsProxy())()`

`protected boolean`
`[isSnapToGrid](#isSnapToGrid())()`

`boolean`
`[isSortable](#isSortable())()`
If OV is sortable (must be added to sort manager for sorting) method must return true;
`final boolean`
`[isSuitableToConnectRelationship](#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd))(com.dassault_systemes.modeler.foundation.model.RelationshipEnd end)`

`boolean`
`[isTextEditable](#isTextEditable())()`
Checks text editing flag.
`boolean`
`[isUseFillColor](#isUseFillColor())()`

`protected boolean`
`[isUseFillColorByProperty](#isUseFillColorByProperty())()`

`boolean`
`[isUseGradientForFill](#isUseGradientForFill())()`
Do we need to use gradient for fill color? Checks diagram property.
`final boolean`
`[isVisible](#isVisible())()`

`boolean`
`[isVisibleInDiagram](#isVisibleInDiagram())()`
Check if this symbol is visible in diagram (visible itself and its parent is visible)
`final boolean`
`[isVisibleOrShrunken](#isVisibleOrShrunken())()`

`void`
`[movePathElements](#movePathElements())()`

`final void`
`[movePathElementsRecursively](#movePathElementsRecursively())()`

`boolean`
`[mustShowContextMenu](#mustShowContextMenu())()`

`final void`
`[notifyCreated](#notifyCreated())()`
Notify move manager about created presentation element.
`protected void`
`[notifyDiagramFrameSizeChange](#notifyDiagramFrameSizeChange())()`
Notify diagram frame about change in this symbol.
`void`
`[notifyRepaintManager](#notifyRepaintManager(boolean))(boolean boundsChanged)`
Notifies the repaint manager about changes in bounds.
`void`
`[onChildAdd](#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) child)`

`void`
`[onChildRemove](#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) child)`

`void`
`[onDiagramSurfaceSet](#onDiagramSurfaceSet())()`

`final void`
`[onFind](#onFind())()`
Scrolls diagram canvas to this symbol and selects this symbol
`final void`
`[onFind](#onFind(boolean))(boolean center)`
Scrolls diagram canvas to this symbol and selects this symbol
`void`
`[onFontChange](#onFontChange())()`

`void`
`[onParentChange](#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) child,
 [PresentationElement](PresentationElement.html) oldChildParent)`

`void`
`[paintAdornments](#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`void`
`[paintAdornmentsBackground](#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`abstract void`
`[paintChildren](#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`final void`
`[paintChildrenAndAdornments](#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`
Paint symbol adornments and children
`void`
`[paintChildrenBackground](#paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`abstract void`
`[paintSelf](#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`void`
`[paintSelfBackground](#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext))(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)`

`protected boolean`
`[preDisposeOnUpdate](#preDisposeOnUpdate())()`
Validate symbol against model and try to fix it before actual symbol update.
`protected boolean`
`[prepareForLineDrawing](#prepareForLineDrawing(java.awt.Graphics2D))([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g)`
Prepares graphics for line drawing
`protected boolean`
`[prepareForShadowDrawing](#prepareForShadowDrawing(java.awt.Graphics2D))([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g)`
Prepares graphics for symbol shadow drawing.
`protected void`
`[prepareForTextDrawing](#prepareForTextDrawing(java.awt.Graphics2D))([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g)`
Prepares graphics for text drawing
`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)`
Listens for property change it can be: data was edited text box was edited
`void`
`[recreateListeners](#recreateListeners())()`
Recreates model listeners for this symbol.
`void`
`[recursiveAutosize](#recursiveAutosize())()`
Resize recursively all symbols.
`void`
`[registerInSortManager](#registerInSortManager())()`
Registers this view in the sort manager
`void`
`[rememberBounds](#rememberBounds())()`
Remember old bounds
`void`
`[rememberBounds](#rememberBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`

`void`
`[removeFromSortManager](#removeFromSortManager())()`
Removes this OV from sort manager.
`protected void`
`[removeItSelfOnUpdate](#removeItSelfOnUpdate())()`
Remove itself during update and register this changed in command history.
`void`
`[removePresentationElement](#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) element)`
Removes given child
`void`
`[resizeParent](#resizeParent())()`
Method that initiates parent resize to accommodate children if some child's bounds are
 changed.
`final void`
`[sAddPresentationElement](#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) element)`
Add given child to this symbol.
`void`
`[sAddPresentationElement](#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int))([PresentationElement](PresentationElement.html) element,
 int index)`
Add given child to this symbol at given index
`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[selectChildrenForMoving](#selectChildrenForMoving())()`
Calculates children for moving together with this symbol.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[selectObjectsForMoving](#selectObjectsForMoving())()`
if calling simple set bounds for container shapes container moves itself and inner/related
 views This method selects which views must be moved.
`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](paths/PathElement.html)>`
`[selectPathsForMoving](#selectPathsForMoving(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> subPresentationElements)`
Select paths to move with current symbol from deep structure.
`void`
`[setAllSelected](#setAllSelected(boolean))(boolean select)`
Selects(or deselects) all presentation elements in the diagram.
`final void`
`[setBounds](#setBounds(int,int,int,int))(int x,
 int y,
 int width,
 int height)`

`abstract void`
`[setBounds](#setBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)`
sets bounds of this object view
`void`
`[setCreateElementListener](#setCreateElementListener(boolean))(boolean createElementListener)`

`boolean`
`[setDummyResizeMode](#setDummyResizeMode(boolean))(boolean b)`
In dummy resize mode symbol may not resize according it children or move children on bounds
 changed and etc.
`void`
`[setElement](#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[setFillColor](#setFillColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) c)`
Sets fill color
`boolean`
`[setFont](#setFont(java.awt.Font))([Font](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html) font)`
Sets font for this object view.
`void`
`[setLayouting](#setLayouting(boolean))(boolean v)`

`void`
`[setLineColor](#setLineColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) c)`
Sets line color
`void`
`[setLineWidth](#setLineWidth(int))(int width)`

`final void`
`[setLoadedVisibility](#setLoadedVisibility(boolean))(boolean visible)`

`final void`
`[setLocation](#setLocation(int,int))(int x,
 int y)`
sets location of object
`final void`
`[setLocation](#setLocation(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
sets location of object
`void`
`[setModelElement](#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`

`void`
`[setNeedRecreateListeners](#setNeedRecreateListeners(boolean))(boolean needRecreateListeners)`
Set a need to recreated models listeners flag
`void`
`[setParent](#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) parent)`
Sets parent for this view.
`void`
`[setPresentationElements](#setPresentationElements(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> elements)`
Sets children of this element
`void`
`[setPropertyManagerName](#setPropertyManagerName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyManagerName)`

`void`
`[setSelected](#setSelected(boolean))(boolean select)`
Selects or deselects this presentation element in the diagram.
`void`
`[setSelected](#setSelected(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> elements)`
Selects given elements in the diagram.
`final void`
`[setSize](#setSize(int,int))(int width,
 int height)`
set dimension of draw object
`final void`
`[setSize](#setSize(com.nomagic.ui.UnmodifiableDimension))([UnmodifiableDimension](../../../ui/UnmodifiableDimension.html) size)`
set dimension of draw object
`final void`
`[setSize](#setSize(java.awt.Dimension))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size)`
set dimension of draw object
`void`
`[setTextColor](#setTextColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) c)`
Sets text color
`void`
`[setTextEditable](#setTextEditable(boolean))(boolean editable)`
Sets text editing flag.
`void`
`[setUseFillColor](#setUseFillColor(boolean))(boolean use)`
Sets use fill color
`void`
`[setVisibility](#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility))(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)`
Sets element visibility flag.
`final void`
`[setVisible](#setVisible(boolean))(boolean visible)`
Sets element visibility flag.
`final void`
`[silentApply](#silentApply())()`
Silently applies all properties after initialization
`final void`
`[silentApply](#silentApply(boolean))(boolean recreateListeners)`
Silently applies all properties after initialization
`final void`
`[simpleSetBounds](#simpleSetBounds(int,int,int,int))(int x,
 int y,
 int width,
 int height)`

`void`
`[simpleSetBounds](#simpleSetBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)`
Sets bounding rectangle.
`final void`
`[snapToGrid](#snapToGrid(java.awt.Point,float))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p,
 float step)`
Snap to grid this point
`final void`
`[snapToGrid](#snapToGrid(java.awt.Rectangle,float))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r,
 float step)`
Snap to grid this rectangle
`void`
`[snapViewToGrid](#snapViewToGrid(float))(float step)`
Snap to grid this point
`static void`
`[sortObjectsByX](#sortObjectsByX(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [PresentationElement](PresentationElement.html)> vector)`
Sorts objectViews by x ascending.
`static void`
`[sortObjectsByY](#sortObjectsByY(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [PresentationElement](PresentationElement.html)> vector)`
Sorts objectViews by y in ascending order.
`void`
`[sRemovePresentationElement](#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) element)`
Removes given child
`final void`
`[sSetBounds](#sSetBounds(int,int,int,int))(int x,
 int y,
 int width,
 int height)`

`abstract void`
`[sSetBounds](#sSetBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)`
Sets bounds of this object view only.
`void`
`[sSetElement](#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`final void`
`[sSetLocation](#sSetLocation(int,int))(int x,
 int y)`
Sets location of object.
`final void`
`[sSetLocation](#sSetLocation(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
sets location of object
`void`
`[sSetModelElement](#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`

`void`
`[sSetParent](#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) parent)`
Sets parent for this view.
`final void`
`[sSetParentForAll](#sSetParentForAll(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> elements)`
Sets itself as parent to the all PresentationElement from given vector.
`void`
`[sSetPresentationElements](#sSetPresentationElements(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> elements)`
Sets children of this element
`final void`
`[sSetSize](#sSetSize(int,int))(int width,
 int height)`
Sets dimension of draw object.
`final void`
`[sSetSize](#sSetSize(com.nomagic.ui.UnmodifiableDimension))([UnmodifiableDimension](../../../ui/UnmodifiableDimension.html) size)`
set dimension of draw object
`final void`
`[sSetSize](#sSetSize(java.awt.Dimension))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size)`
set dimension of draw object
`void`
`[sSetVisibility](#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility))(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)`
Sets element visibility flag.
`final void`
`[sSetVisible](#sSetVisible(boolean))(boolean visible)`
Sets element visibility flag.
`boolean`
`[tryToDeleteModelElementUponRemoval](#tryToDeleteModelElementUponRemoval())()`
Override this method if you do not want model element to be deleted upon symbol deletion.
`final void`
`[update](#update())()`
Major presentation element update by model element method.
`void`
`[updateAfterLoad](#updateAfterLoad())()`

`void`
`[updateLabelsIgnoringSuspendableLater](#updateLabelsIgnoringSuspendableLater(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.uml.symbols.shapes.LabelWrapper> wrappers)`

`void`
`[updateLater](#updateLater())()`
Registers this symbol to postponed "update" at the end of current command execution.
`final void`
`[updateModelByView](#updateModelByView())()`
Updates model according current view structure.
`protected void`
`[updateModelByViewInternal](#updateModelByViewInternal())()`
Updates model according current view structure.
`void`
`[updateViewAfterPropertyChange](#updateViewAfterPropertyChange())()`

`boolean`
`[useParentProperties](#useParentProperties())()`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`useParentStyle()`](#useParentStyle())
`boolean`
`[useParentStyle](#useParentStyle())()`
Does this element uses parent style or has it's own?
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../BaseElement.html)
`[canAdd](../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.uml.[MDElement](../MDElement.html)
`[getProject](../MDElement.html#getProject())`
Methods inherited from interface com.nomagic.magicdraw.utils.[NameOwner](../../utils/NameOwner.html)
`[getName](../../utils/NameOwner.html#getName())`

============ FIELD DETAIL =========== 
Field Details
MAX_LINE_WIDTH
public static final double MAX_LINE_WIDTH
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.MAX_LINE_WIDTH)
MIN_LINE_WIDTH
public static final double MIN_LINE_WIDTH
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.MIN_LINE_WIDTH)
HANDLE_SIZE
public static final int HANDLE_SIZE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.HANDLE_SIZE)
SOLID_STROKE
@OpenApipublic static final int SOLID_STROKE
Solid path stroke.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.SOLID_STROKE)
DASHED_STROKE
@OpenApipublic static final int DASHED_STROKE
Dashed path stroke.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.DASHED_STROKE)
DOTTED_STROKE
@OpenApipublic static final int DOTTED_STROKE
Dotted path stroke.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.DOTTED_STROKE)
SHADOW_WIDTH
public static final int SHADOW_WIDTH
Symbol shadow width in pixels
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.SHADOW_WIDTH)
DEFAULT_LINE_WIDTH
public static final int DEFAULT_LINE_WIDTH
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.DEFAULT_LINE_WIDTH)
peStyle
protected com.dassault_systemes.modeler.foundation.diagram.style.PresentationElementStyle peStyle
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PresentationElement
public PresentationElement()
PresentationElement
public PresentationElement(@CheckForNull
 [PresentationElement](PresentationElement.html) parent)
 ============ METHOD DETAIL ========== 
Method Details
sSetElement
public void sSetElement(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
generateID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) generateID()
Description copied from class: `com.nomagic.magicdraw.uml.MDElementImpl`
Generate ID.
Overrides:
`generateID` in class `com.nomagic.magicdraw.uml.MDElementImpl`
setElement
public void setElement(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getElement
@OpenApi
@CheckForNullpublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElement()
Returns model element of this presentation element. Some presentation elements (for example
 TextBoxes) do not have model elements.
Specified by:
`[getElement](../ModelElementProvider.html#getElement())` in interface `[ModelElementProvider](../ModelElementProvider.html)`
Returns:
model element of this presentation element.
getActualElement
@CheckForNullpublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getActualElement()
Because some views returns theirs parent model element, we do not know have they this member
 set or not.
sSetParent
public void sSetParent(@CheckForNull
 [PresentationElement](PresentationElement.html) parent)
Sets parent for this view.
 For adding symbols to other symbols use
 [`addPresentationElement(PresentationElement)`](#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)) or
 [`sAddPresentationElement(PresentationElement)`](#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))}
Parameters:
`parent` - parent view
setParent
public void setParent([PresentationElement](PresentationElement.html) parent)
Sets parent for this view.
 For adding symbols to other symbols use
 [`addPresentationElement(PresentationElement)`](#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)) or
 [`sAddPresentationElement(PresentationElement)`](#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))}
Parameters:
`parent` - parent view
onParentChange
public void onParentChange([PresentationElement](PresentationElement.html) child,
 [PresentationElement](PresentationElement.html) oldChildParent)
onChildAdd
public void onChildAdd([PresentationElement](PresentationElement.html) child)
onChildRemove
public void onChildRemove([PresentationElement](PresentationElement.html) child)
hasSharedModelElement
public boolean hasSharedModelElement()
Returns true if `ModelElement` of this symbol can represented with other symbol.
 If `ModelElement` is not shared, it can be deleted together with symbol deleting.
Returns:
true if element of this symbol can be represented with other symbol.
setTextEditable
public void setTextEditable(boolean editable)
Sets text editing flag.
Parameters:
`editable` - flag
isTextEditable
public boolean isTextEditable()
Checks text editing flag.
Returns:
`true` if the object view text is editable; `false` otherwise.
collectSubPresentationElements
public final void collectSubPresentationElements([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collection)
Collects all sub-presentation elements into given collection.
 Includes this symbol too.
Parameters:
`collection` - collection in which sub presentation elements should be collected.
collectSubPresentationElements
public final void collectSubPresentationElements([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collection,
 [Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[PresentationElement](PresentationElement.html)> predicate)
Collects all sub-presentation elements that match given predicate into given collection.
 Includes this symbol too.
Parameters:
`collection` - collection in which sub presentation elements should be collected.
`predicate` - predicate that will check if sub element should be included.
collectSubShowingPresentationElements
public final void collectSubShowingPresentationElements([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> col)
Collect all visible children starting from current element. In case some element in hierarchy
 is not visible, children of this element are not added also even if they are visible.
Parameters:
`col` - result
getPresentationElementAt
@CheckForNullpublic final [PresentationElement](PresentationElement.html) getPresentationElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p)
Gets object view at point.
Parameters:
`p` - object view at point location
Returns:
object view at this point
getPresentationElementAt
@CheckForNullpublic [PresentationElement](PresentationElement.html) getPresentationElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Gets object view at point.
Parameters:
`p` - object view at point location
`kind` - intersection kind to check for
Returns:
object view at this point
getPresentationElementAt
@CheckForNullpublic final [PresentationElement](PresentationElement.html) getPresentationElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)
Gets object view at point.
Parameters:
`relativePoint` - object view at point location.
`sortManagerProvider` - sort manager for searching elements.
Returns:
object view at this point.
getPresentationElementAt
@CheckForNullpublic [PresentationElement](PresentationElement.html) getPresentationElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Gets object view at point.
Parameters:
`relativePoint` - object view at point location.
`sortManagerProvider` - sort manager for searching elements.
`kind` - intersection kind to check for
Returns:
object view at this point.
getPresentationElementsAt
@CheckForNullpublic final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getPresentationElementsAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p)
Gets objects at point.
Parameters:
`p` - object view at point location.
Returns:
object view at this point.
getPresentationElementsAt
@CheckForNullpublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getPresentationElementsAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Gets objects at point.
Parameters:
`p` - object view at point location.
`kind` - intersection kind to check for
Returns:
object view at this point.
getPresentationElementsAt
@CheckForNullpublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getPresentationElementsAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)
Gets object view at point.
Parameters:
`relativePoint` - object view at point location.
`sortManagerProvider` - sort manager for searching elements.
Returns:
object view at this point.
getPresentationElementsAt
@CheckForNullpublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getPresentationElementsAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Gets object view at point.
Parameters:
`relativePoint` - object view at point location.
`sortManagerProvider` - sort manager for searching elements.
`kind` - intersection kind to check for
Returns:
object view at this point.
getPresentationElementAt
@CheckForNullpublic final [PresentationElement](PresentationElement.html) getPresentationElementAt(int index)
Gets object view at specified position from container
Parameters:
`index` - container element index
Returns:
symbol at given index
getPresentationElementCount
public final int getPresentationElementCount()
Returns children count in container.
Returns:
children count in container.
getPresentationElementIndex
public int getPresentationElementIndex([PresentationElement](PresentationElement.html) element)
Get index of the given presentation element in the container.
Parameters:
`element` - presentation element
Returns:
index in the presentation element container or -1 if such presentation element can not be found
isParentOf
public boolean isParentOf(@CheckForNull
 [PresentationElement](PresentationElement.html) child)
Checks if object is child of this object.
Parameters:
`child` - object to check.
Returns:
true if obj is child of this object.
isParentOf
public boolean isParentOf([BaseElement](../BaseElement.html) obj)
Description copied from interface: `[BaseElement](../BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement))`
Returns true, if current element is parent of given element.
 Return false in this implementation.
Specified by:
`[isParentOf](../BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement))` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`isParentOf` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Parameters:
`obj` - the given element(possible child).
Returns:
true if obj is the parent of this object.
onDiagramSurfaceSet
public void onDiagramSurfaceSet()
registerInSortManager
public void registerInSortManager()
Registers this view in the sort manager
getDiagramSurface
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)
@CheckForNull
@OpenApipublic [DiagramSurface](DiagramSurface.html) getDiagramSurface()
Deprecated, for removal: This API element is subject to removal in a future version.
use [`DiagramSurface.getDiagramSurface(PresentationElement)`](DiagramSurface.html#getDiagramSurface(com.nomagic.magicdraw.uml.symbols.PresentationElement)). Will be removed in 2026x version.
Returns diagram surface for this presentation element. DiagramSurface is null if diagram of
 this element is not opened in some window.
Returns:
diagram surface or null if diagram is not opened.
clone
public [PresentationElement](PresentationElement.html) clone()
Specified by:
`[clone](../BaseElement.html#clone())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`clone` in class `com.nomagic.magicdraw.uml.MDElementImpl`
getParent
@OpenApipublic final [PresentationElement](PresentationElement.html) getParent()
Returns parent of this element.
Returns:
parent of this element.
getPreferredSize
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2022x",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)
@OpenApipublic final [Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) getPreferredSize()
Deprecated, for removal: This API element is subject to removal in a future version.
use [`getPreferredDimension()`](#getPreferredDimension()). Will be removed in 2026x version.
Returns preferable dimension of the element.
Returns:
preferred dimension
getPreferredDimension
@OpenApipublic [UnmodifiableDimension](../../../ui/UnmodifiableDimension.html) getPreferredDimension()
Returns preferable dimension of the element.
Returns:
preferred dimension
getPreferredDimensionForAutosize
public [UnmodifiableDimension](../../../ui/UnmodifiableDimension.html) getPreferredDimensionForAutosize()
Returns preferable dimension of the element for autosize.This implementation simple returns
 preferred size.
Returns:
preferred dimension
getPreferredBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getPreferredBounds()
Calculate the smallest rectangle which would fit all contained shapes
Returns:
rectangle
getMinimumDimension
public [UnmodifiableDimension](../../../ui/UnmodifiableDimension.html) getMinimumDimension()
get minimum possible size for object
Returns:
minimum dimension
setSize
public final void setSize([UnmodifiableDimension](../../../ui/UnmodifiableDimension.html) size)
set dimension of draw object
setSize
public final void setSize([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size)
set dimension of draw object
sSetSize
public final void sSetSize([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) size)
set dimension of draw object
sSetSize
public final void sSetSize([UnmodifiableDimension](../../../ui/UnmodifiableDimension.html) size)
set dimension of draw object
setSize
public final void setSize(int width,
 int height)
set dimension of draw object
sSetSize
public final void sSetSize(int width,
 int height)
Sets dimension of draw object.
setLocation
public final void setLocation([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
sets location of object
sSetLocation
public final void sSetLocation([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
sets location of object
setLocation
public final void setLocation(int x,
 int y)
sets location of object
sSetLocation
public final void sSetLocation(int x,
 int y)
Sets location of object.
setBounds
public abstract void setBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)
 throws [NoRectangleDefinedException](NoRectangleDefinedException.html)
sets bounds of this object view
Parameters:
`rect` - rectangle of bounds
Throws:
`[NoRectangleDefinedException](NoRectangleDefinedException.html)`
sSetBounds
public abstract void sSetBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)
 throws [NoRectangleDefinedException](NoRectangleDefinedException.html)
Sets bounds of this object view only.
Parameters:
`rect` - rectangle of bounds.
Throws:
`[NoRectangleDefinedException](NoRectangleDefinedException.html)`
sSetBounds
public final void sSetBounds(int x,
 int y,
 int width,
 int height)
simpleSetBounds
public final void simpleSetBounds(int x,
 int y,
 int width,
 int height)
setBounds
public final void setBounds(int x,
 int y,
 int width,
 int height)
simpleSetBounds
public void simpleSetBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)
Sets bounding rectangle.
Parameters:
`rect` - new bounding rectangle.
movePathElements
public void movePathElements()
movePathElementsRecursively
public final void movePathElementsRecursively()
getMiddlePoint
@CheckForNull
@OpenApipublic [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getMiddlePoint()
Returns middle point of this element. Middle point for shapes usually will be center point of
 bounds, middle point for paths will be center of path curve.
Returns:
point that is considered as middle for this element.
getMiddlePointX
public int getMiddlePointX()
getMiddlePointY
public int getMiddlePointY()
getMiddlePoint
@CheckForNullpublic [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getMiddlePoint([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint)
Gets middle point of this view,
Parameters:
`relativePoint` - relative point
Returns:
middle point
getMiddlePointX
protected int getMiddlePointX([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint)
getMiddlePointY
protected int getMiddlePointY([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint)
getIntersection
@CheckForNullpublic [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getIntersection(int x,
 int y,
 @CheckForNull
 [PathElement](paths/PathElement.html) path)
getBounds
@OpenApipublic [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBounds()
 throws [NoRectangleDefinedException](NoRectangleDefinedException.html)
Method returns bounds of this element.
 Use PresentationElementsManager to change a bounds of the element.
Returns:
bounds of the element.
Throws:
`[NoRectangleDefinedException](NoRectangleDefinedException.html)` - when bounds can not be calculated (some presentation
 elements are abstract and can not have bounds).
See Also:
`PresentationElementsManager.reshapeShapeElement`
getManipulationBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getManipulationBounds(@CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) relativePoint)
Gets manipulation bounds of the symbol. Manipulation bounds might
 differ from symbol bounds, they can be larger or smaller to help
 user manipulate the symbol.
Parameters:
`relativePoint` - active user point to construct manipulation bounds.
Returns:
symbol manipulation bounds.
getBoundsToRepaint
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBoundsToRepaint()
 throws [NoRectangleDefinedException](NoRectangleDefinedException.html)
Return bounds of the symbol that must be repainted. throws NoRectangleDefinedException
Returns:
rectangle of bounds
Throws:
`[NoRectangleDefinedException](NoRectangleDefinedException.html)`
getNotCopyBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getNotCopyBounds()
 throws [NoRectangleDefinedException](NoRectangleDefinedException.html)
get not copy bounds of object throws NoRectangleDefinedException
Returns:
rectangle of bounds
Throws:
`[NoRectangleDefinedException](NoRectangleDefinedException.html)`
intersects
public final boolean intersects(int x,
 int y,
 int width,
 int height)
checks whether object intersects with given rectangle
Returns:
true if object and rectangle intersects
coversPoint
public final boolean coversPoint(int x,
 int y)
checks if object covers provided point
Returns:
true if object covers this point
intersects
public abstract boolean intersects(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
checks whether object intersects with given rectangle
Returns:
true if object and rectangle intersects
coversPoint
public abstract boolean coversPoint(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
checks if object covers provided point
Returns:
true if object covers this point
selectObjectsForMoving
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> selectObjectsForMoving()
if calling simple set bounds for container shapes container moves itself and inner/related
 views This method selects which views must be moved.
childrenForMoving
protected final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> childrenForMoving()
Calculates selected children for moving or takes result from cached.
Returns:
list of children for moving.
See Also:
[`selectChildrenForMoving()`](#selectChildrenForMoving())
`PresentationElement.StructureCache`
selectChildrenForMoving
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> selectChildrenForMoving()
Calculates children for moving together with this symbol. This method should not be called by
 user. This method is just for implementation and override purpose. childrenForMoving() must
 be used outside.
See Also:
[`childrenForMoving()`](#childrenForMoving())
selectPathsForMoving
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PathElement](paths/PathElement.html)> selectPathsForMoving(@CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> subPresentationElements)
Select paths to move with current symbol from deep structure.
 Some paths can be connected to current symbol, but owned in some deep child of this symbol.
Parameters:
`subPresentationElements` - sub children of this symbol
Returns:
paths to move together with current symbol
setPresentationElements
public void setPresentationElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> elements)
Sets children of this element
Parameters:
`elements` - children
sSetPresentationElements
public void sSetPresentationElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> elements)
Sets children of this element
Parameters:
`elements` - children
getPresentationElements
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getPresentationElements()
Returns all children of this element
Returns:
all children of this element. The collection is unmodifiable.
getVisiblePresentationElements
public final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getVisiblePresentationElements()
Returns:
not modifiable list of visible elements, including not detectable ones that should not be painted.
See Also:
[`isDetectable()`](#isDetectable())
removePresentationElement
public void removePresentationElement([PresentationElement](PresentationElement.html) element)
Removes given child
Parameters:
`element` - child
sRemovePresentationElement
public void sRemovePresentationElement([PresentationElement](PresentationElement.html) element)
Removes given child
Parameters:
`element` - child
addPresentationElement
public final void addPresentationElement([PresentationElement](PresentationElement.html) element)
Add given child to this symbol.
Parameters:
`element` - child to add
addPresentationElement
public void addPresentationElement([PresentationElement](PresentationElement.html) element,
 int index)
Add given child to this symbol at given index
Parameters:
`element` - child to add
`index` - index to add at. Can be -1
addPresentationElementWithoutResize
public void addPresentationElementWithoutResize([PresentationElement](PresentationElement.html) element)
sAddPresentationElement
public final void sAddPresentationElement([PresentationElement](PresentationElement.html) element)
Add given child to this symbol.
Parameters:
`element` - child to add
sAddPresentationElement
public void sAddPresentationElement([PresentationElement](PresentationElement.html) element,
 int index)
Add given child to this symbol at given index
Parameters:
`element` - child to add
`index` - index to add at. Can be -1
draw
public void draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
Draw symbol using renderer or symbol specific draw if renderer is not available. Also draw adornments.
Parameters:
`context` - paint context
drawBackground
public void drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
drawSymbolBackground
public void drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
paintSelfBackground
public void paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
paintChildrenBackground
public void paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
drawSymbol
public final void drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
Draw symbol as defined by standard notation. Does not use renderers and adornments.
Parameters:
`context` - paint context
paintChildrenAndAdornments
public final void paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
Paint symbol adornments and children
Parameters:
`context` - paint context
paintSelf
public abstract void paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
paintChildren
public abstract void paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
paintAdornmentsBackground
public void paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
paintAdornments
public void paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)
getRenderer
@CheckForNullpublic com.nomagic.magicdraw.uml.symbols.SymbolDecorator getRenderer()
Gets rendered which could decorate this symbol.
Returns:
symbol renderer.
getSymbolRenderer
@CheckForNullprotected static com.nomagic.magicdraw.uml.symbols.SymbolDecorator getSymbolRenderer([PresentationElement](PresentationElement.html) presentationElement)
getDrawComparator
public [Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)<[PresentationElement](PresentationElement.html)> getDrawComparator()
mustShowContextMenu
public boolean mustShowContextMenu()
canHavePaths
public boolean canHavePaths()
Returns:
true if symbol can have connected paths. Return false here.
canAddChild
public boolean canAddChild([PresentationElement](PresentationElement.html) symbol)
Check of given symbol can be added as child into this symbol.
Parameters:
`symbol` - symbol
Returns:
true if symbol can be added
canAddChild
public final boolean canAddChild([BaseElement](../BaseElement.html) element)
Specified by:
`[canAddChild](../MDElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement))` in interface `[MDElement](../MDElement.html)`
Overrides:
`canAddChild` in class `com.nomagic.magicdraw.uml.MDElementImpl`
canAddInstance
public boolean canAddInstance([PresentationElement](PresentationElement.html) symbol)
Object view has no children.
canAddInstance
public final boolean canAddInstance([BaseElement](../BaseElement.html) element)
Description copied from interface: `[BaseElement](../BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement))`
Checks if this object can add element of given type.
 Current implementation returns false.
Specified by:
`[canAddInstance](../BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement))` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`canAddInstance` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Returns:
true if this object can elements of a given type.
dispose
public void dispose()
disposes ends of links when link is deleted
Specified by:
`[dispose](../BaseElement.html#dispose())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`dispose` in class `com.nomagic.magicdraw.uml.MDElementImpl`
disposeChildren
protected void disposeChildren()
Removes all children from itself. Such removing causes calling dispose for every child.
setAllSelected
@OpenApipublic void setAllSelected(boolean select)
Selects(or deselects) all presentation elements in the diagram.
Parameters:
`select` - select or deselect all elements.
setSelected
@OpenApipublic void setSelected([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> elements)
Selects given elements in the diagram.
Parameters:
`elements` - elements to select.
setSelected
@OpenApipublic void setSelected(boolean select)
Selects or deselects this presentation element in the diagram.
Parameters:
`select` - select or deselect this presentation element.
getSelected
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getSelected()
Returns a list of selected elements in the diagram.
Returns:
a list of selected elements. List is unmodifiable.
isSelected
@OpenApipublic boolean isSelected()
Returns true, if this element is selected in the diagram.
Returns:
true, if this element is selected in the diagram.
isDetectable
public boolean isDetectable()
Not detectable symbols are not drawn even they are visible.
 Not detectable symbols cannot be selected even they have manipulator.
Returns:
true if selection and painting of this symbol is currently allowed
initializeAndAutosize
public final void initializeAndAutosize()
Initialize symbol and call autosize recursively
See Also:
[`recursiveAutosize()`](#recursiveAutosize())
[`initialize()`](#initialize())
recursiveAutosize
public void recursiveAutosize()
Resize recursively all symbols. Method must be called if something is changed in symbol (for
 example minimum size) and you want to resize (autosize) all hierarchy
initialize
public void initialize()
Initialize symbol and its children state. Symbol must be initialized before doing any
 resize, painting and etc. These operations can lead to unpredictable results otherwise.
getDiagramPresentationElement
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public final [DiagramPresentationElement](DiagramPresentationElement.html) getDiagramPresentationElement()
Deprecated, for removal: This API element is subject to removal in a future version.
use [`DiagramPresentationElement.get(PresentationElement)`](DiagramPresentationElement.html#get(com.nomagic.magicdraw.uml.symbols.PresentationElement)).Will be removed in 2026x.
Returns diagram of this presentation element.
Returns:
diagram of this presentation element.
getAbstractDiagramPresentationElement
public [AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html) getAbstractDiagramPresentationElement()
Returns diagram of this presentation element.
Returns:
diagram of this presentation element.
onFind
@OpenApipublic final void onFind()
Scrolls diagram canvas to this symbol and selects this symbol
onFind
@OpenApipublic final void onFind(boolean center)
Scrolls diagram canvas to this symbol and selects this symbol
Parameters:
`center` - if true, centers current view in the center of the window.
resizeParent
public void resizeParent()
Method that initiates parent resize to accommodate children if some child's bounds are
 changed.
autosizeAndResizeParent
public void autosizeAndResizeParent()
Resize itself and initiate parent resize
autosizeAndResizeManipulatedParent
public void autosizeAndResizeManipulatedParent()
Autosize and resize manipulated element - itself(if this element has manipulator) or
 manipulated parent.
update
public final void update()
Major presentation element update by model element method. Any outside code must call this
 method for updating the symbol by data. This method calls internal update
 (updatePresentationElement()) and also calls update for symbol decorator if such exits.
See Also:
[`internalUpdatePresentationElement()`](#internalUpdatePresentationElement())
`SymbolDecorator`
internalBeforeUpdate
protected void internalBeforeUpdate(@CheckForNull
 com.nomagic.magicdraw.uml.symbols.SymbolDecorator renderer)
removeItSelfOnUpdate
protected void removeItSelfOnUpdate()
Remove itself during update and register this changed in command history.
internalUpdatePresentationElement
protected void internalUpdatePresentationElement()
Internal symbol update method for subclassing. It is called from update as part of full
 update action.
See Also:
[`update()`](#update())
canBeDisposedOnUpdate
protected boolean canBeDisposedOnUpdate()
Some symbols removes themselves on update if they are not valid by model anymore. Check if such operation is
 possible at this moment. Do not remove symbol on undo or redo operations.
 We very often have situation when symbol is updated during these operations and structure in model is not yet fully restored.
Returns:
true if path can be removed if not valid
preDisposeOnUpdate
protected boolean preDisposeOnUpdate()
Validate symbol against model and try to fix it before actual symbol update. If symbol is not valid and can not be fixed,
 request symbol dispose by returning true.
 Check if symbol should be disposed, because model does not correspond to symbol.
 This may happen for example if path supplier or client in model is changed, but path still is connected to symbols of old ends.
 Method also can fix symbol if possible - for example reconnect path to other symbols in diagram and etc.
Returns:
true if symbol must be disposed
getFontHeight
public final int getFontHeight()
Gets font height.
Returns:
font height
isUseGradientForFill
public boolean isUseGradientForFill()
Do we need to use gradient for fill color? Checks diagram property.
Returns:
diagram gradient fill color value.
getFontRenderContext
public static [FontRenderContext](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/font/FontRenderContext.html) getFontRenderContext()
isVisible
public final boolean isVisible()
Returns:
true if element visibility is `PresentationElementVisibility.VISIBLE`
See Also:
`PresentationElementVisibility.isVisible()`
isVisibleOrShrunken
public final boolean isVisibleOrShrunken()
Returns:
true if element visibility is `PresentationElementVisibility.VISIBLE` or `PresentationElementVisibility.SHRUNKEN`
See Also:
`PresentationElementVisibility.isVisibleOrShrunken()`
sSetVisible
public final void sSetVisible(boolean visible)
Sets element visibility flag.
Parameters:
`visible` - flag value
See Also:
`PresentationElementVisibility.apply(boolean)`
setVisible
public final void setVisible(boolean visible)
Sets element visibility flag.
Parameters:
`visible` - flag value
See Also:
`PresentationElementVisibility.apply(boolean)`
getVisibility
public com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility getVisibility()
Returns:
element visibility
sSetVisibility
public void sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)
Sets element visibility flag.
Parameters:
`visibility` - flag value
setVisibility
public void setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)
Sets element visibility flag.
Parameters:
`visibility` - flag value
removeFromSortManager
public void removeFromSortManager()
Removes this OV from sort manager.
updateViewAfterPropertyChange
public void updateViewAfterPropertyChange()
updateLater
public void updateLater()
Registers this symbol to postponed "update" at the end of current command execution.
 Symbol will be updated when all other commands are executed.
 If this is not possible to register, updates symbol immediately.
updateLabelsIgnoringSuspendableLater
public void updateLabelsIgnoringSuspendableLater([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.uml.symbols.shapes.LabelWrapper> wrappers)
updateModelByViewInternal
protected void updateModelByViewInternal()
Updates model according current view structure. In some cases changes in model must
 be made keeping in mind current structure of symbols.
 Does nothing here, but subclasses may override
updateModelByView
public final void updateModelByView()
Updates model according current view structure. In some cases changes in model must
 be made keeping in mind current structure of symbols.
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)
Listens for property change it can be: data was edited text box was edited
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
handleModelDelete
protected void handleModelDelete()
Handles model element delete property Change event.
 Typical implementation is to delete this symbol from parent.
setFont
public boolean setFont([Font](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html) font)
Sets font for this object view.
Parameters:
`font` - new font.
getFont
public [Font](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html) getFont()
Gets font of this object view. It returns font from the project.
Returns:
font of the text object.
internalGetSpecificFont
@CheckForNullprotected [Font](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html) internalGetSpecificFont()
getHumanType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHumanType()
Returns human representation of the data type
Specified by:
`[getHumanType](../BaseElement.html#getHumanType())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`getHumanType` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Returns:
the name of the data
getHumanName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHumanName()
Returns human representation of the data type
Specified by:
`[getHumanName](../BaseElement.html#getHumanName())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`getHumanName` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Returns:
the name of the data
askDeleteDataConfirmation
public boolean askDeleteDataConfirmation()
Declared as interface with default implementation for subclasses. If some subclasses upon
 delete may ask about delete data object as well, they have to redefine this method and return
 true. By default all objects are removed without asking
Returns:
confirmation status -- true if asking is necessary, false otherwise
getManipulatedElementAt
@CheckForNullpublic final [PresentationElement](PresentationElement.html) getManipulatedElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)
Gets manipulated symbol at specified point pt.
Parameters:
`pt` - `Point`
Returns:
manipulate symbol
getManipulatedElementAt
@CheckForNullpublic [PresentationElement](PresentationElement.html) getManipulatedElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind intersectionKind)
Gets manipulated symbol at specified point pt.
Parameters:
`pt` - `Point`
`intersectionKind` - intersection kind to check for
Returns:
manipulate symbol
getManipulatedElementAt
@CheckForNullpublic [PresentationElement](PresentationElement.html) getManipulatedElementAt([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)
Gets manipulate symbol at specified point pt.
Parameters:
`pt` - `Point`
`sortManagerProvider` - provides sort manager in which to search.
Returns:
manipulate symbol
sSetParentForAll
public final void sSetParentForAll([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> elements)
Sets itself as parent to the all PresentationElement from given vector.
hasManipulator
public boolean hasManipulator()
Returns true, if view has manipulator (is selectable)
invalidate
public boolean invalidate()
Invalidates this element.
isSnapToGrid
protected boolean isSnapToGrid()
snapToGrid
public final void snapToGrid([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r,
 float step)
Snap to grid this rectangle
snapToGrid
public final void snapToGrid([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p,
 float step)
Snap to grid this point
internalSnapToGrid
protected void internalSnapToGrid([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p,
 float step)
snapViewToGrid
public void snapViewToGrid(float step)
Snap to grid this point
internalSnapToGrid
protected void internalSnapToGrid(float step)
collectSubManipulatedElements
@OpenApipublic final void collectSubManipulatedElements([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> col)
Collects all visible and manipulated elements in this hierarchy.
getManipulatedPresentationElements
@OpenApipublic final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getManipulatedPresentationElements()
Returns a list of children of this element those have manipulator.
Returns:
a list of manipulated elements. Collection is unmodifiable.
hasManipulatedPresentationElements
@OpenApipublic final boolean hasManipulatedPresentationElements()
Returns:
true if at least one child is manipulated and visible
getTolerance
public final int getTolerance()
Returns tolerance
getNotZoomedTolerance
protected int getNotZoomedTolerance()
atInsert
public void atInsert()
Invalidates object at insert
Specified by:
`[atInsert](../BaseElement.html#atInsert())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`atInsert` in class `com.nomagic.magicdraw.uml.MDElementImpl`
isDisposed
public boolean isDisposed()
Checks if element was explicitly disposed by calling [`dispose()`](#dispose()) method. Calling [`atInsert()`](#atInsert()) clears dispose flag.
 Newly created element is not disposed.
Returns:
true if element was disposed
atInsertChildren
protected void atInsertChildren()
sortObjectsByX
public static void sortObjectsByX([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [PresentationElement](PresentationElement.html)> vector)
Sorts objectViews by x ascending.
Parameters:
`vector` - - Vector which contains Object Views.
sortObjectsByY
public static void sortObjectsByY([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [PresentationElement](PresentationElement.html)> vector)
Sorts objectViews by y in ascending order.
Parameters:
`vector` - - Vector which contains Object Views.
isSortable
public boolean isSortable()
If OV is sortable (must be added to sort manager for sorting) method must return true;
isChildVisible
public boolean isChildVisible([PresentationElement](PresentationElement.html) child)
Returns true if given child of this object is visible. For methods and attributes Method or
 Attribute field view can hide objects without changing visibility flag method isVisible()
 returns true, but method can be not show. This method must avoid such situations and return
 true if parent shows this object and false if it hides.
isVisibleInDiagram
public boolean isVisibleInDiagram()
Check if this symbol is visible in diagram (visible itself and its parent is visible)
Returns:
true if symbol is visible in the diagram
getManipulatedIntersectionWith
@CheckForNullpublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getManipulatedIntersectionWith([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)
Returns vector of manipulated objects whose intersect with given rectangle
getManipulatedIntersectionWith
@CheckForNullpublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getManipulatedIntersectionWith([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Returns vector of manipulated objects whose intersect with given rectangle
getManipulatedIntersectionWith
@CheckForNullpublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getManipulatedIntersectionWith([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect,
 boolean completelyCovered)
Returns vector of manipulated objects whose intersect with given rectangle
Parameters:
`completelyCovered` - take only completely covered by rectangle symbols. Ignore symbols
 with just intersected bounds.
getManipulatedIntersectionWith
@CheckForNullpublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getManipulatedIntersectionWith([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect,
 boolean completelyCovered,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)
Returns vector of manipulated objects whose intersect with given rectangle
Parameters:
`completelyCovered` - take only completely covered by rectangle symbols. Ignore symbols
 with just intersected bounds.
`kind` - intersection kind to check for
findOwnerForElement
@CheckForNullpublic com.dassault_systemes.modeler.foundation.model.ModelElement findOwnerForElement([PresentationElement](PresentationElement.html) newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)
findOwnerForChildElement
@CheckForNullpublic com.dassault_systemes.modeler.foundation.model.ModelElement findOwnerForChildElement([PresentationElement](PresentationElement.html) child)
Returns element owner for given child.
Returns:
most suitable owner for given child's element
checkElementOwnerOnChange
public boolean checkElementOwnerOnChange([PresentationElement](PresentationElement.html) child)
getFillColor
public [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) getFillColor()
Returns fill color
getLineColor
public [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) getLineColor()
Returns line color
canFill
protected boolean canFill()
Returns:
true if symbol can be filled with some color
isUseFillColor
public boolean isUseFillColor()
Returns:
use fill color flag
isUseFillColorByProperty
protected boolean isUseFillColorByProperty()
getTextColor
public [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) getTextColor()
internalGetSpecificTextColor
@CheckForNullprotected [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) internalGetSpecificTextColor()
setTextColor
public void setTextColor([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) c)
Sets text color
setFillColor
public void setFillColor([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) c)
Sets fill color
createFillStrategy
public com.nomagic.magicdraw.uml.symbols.FillStrategy createFillStrategy()
dynamicTextColor
public [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) dynamicTextColor()
dynamicLineColor
public [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) dynamicLineColor()
dynamicFillColor
@CheckForNullpublic [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) dynamicFillColor()
dynamicStyleFillColor
@CheckForNullpublic [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) dynamicStyleFillColor(@CheckForNull
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color,
 boolean useFill)
dynamicStyleLineColor
public final [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) dynamicStyleLineColor([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)
dynamicStyleTextColor
public final [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) dynamicStyleTextColor([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color)
dynamicStyleTransparency
public final int dynamicStyleTransparency()
dynamicStyleTransparency
public final int dynamicStyleTransparency([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) target)
dynamicTextAlignment
@CheckForNullpublic com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition target)
dynamicStyleValue
@CheckForNullprotected <T> T dynamicStyleValue(@CheckForNull
 T merged,
 [BiFunction](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html)<com.dassault_systemes.modeler.foundation.common.style.DynamicStyle,T,T> valueProvider)
dynamicPaintShadow
public boolean dynamicPaintShadow()
getDynamicStyleOwner
@CheckForNullpublic [PresentationElement](PresentationElement.html) getDynamicStyleOwner()
prepareForShadowDrawing
protected boolean prepareForShadowDrawing([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g)
Prepares graphics for symbol shadow drawing. If diagram allows shadows, sets darker diagram background color to given graphics.
Parameters:
`g` - the given graphics
prepareForLineDrawing
protected boolean prepareForLineDrawing([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g)
Prepares graphics for line drawing
prepareForTextDrawing
protected void prepareForTextDrawing([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g)
Prepares graphics for text drawing
useParentStyle
@OpenApipublic boolean useParentStyle()
Does this element uses parent style or has it's own?
Returns:
true, if element does not have style and uses parent's style.
useParentProperties
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)
@OpenApipublic boolean useParentProperties()
Deprecated, for removal: This API element is subject to removal in a future version.
use [`useParentStyle()`](#useParentStyle())
getParentSymbolStyleOwner
@CheckForNullpublic [PresentationElement](PresentationElement.html) getParentSymbolStyleOwner()
Returns parent to which this symbol delegates style attributes related functionality.
Returns:
parent symbol to delegate or null if this symbol does not delegate.
getPropertyManager
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public final [PropertyManager](../../properties/PropertyManager.html) getPropertyManager()
Deprecated, for removal: This API element is subject to removal in a future version.
use [`PresentationElementsManager.addProperty(PresentationElement, Property)`](../../openapi/uml/PresentationElementsManager.html#addProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.properties.Property)). Will be removed in 2026x version.
Returns the propertyManager of this element. If element does not have properties, empty
 manager will be created. 

 Use method useParentProperties() to check if properties exist. 

 Use PresentationElementsManager to change the properties.
Returns:
propertyManager of this element.
See Also:
[`useParentStyle()`](#useParentStyle())
`PresentationElementsManager.setPresentationElementProperties`
createPresentationElementStyle
protected com.dassault_systemes.modeler.foundation.diagram.style.PresentationElementStyle createPresentationElementStyle()
Creates the presentation element style for this presentation element.
 Override only if a specific style for a specific presentation element should be created.
 The default implementation is to get style though style registry
getStyle
public com.dassault_systemes.modeler.foundation.diagram.style.PresentationElementStyle getStyle()
getProperty
@CheckForNull
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public final [Property](../../properties/Property.html) getProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyId)
Deprecated, for removal: This API element is subject to removal in a future version.
use `PresentationElementsManager#getProperty(PresentationElement)`. Will be removed in 2026x version.
Returns element's property with given id.
Parameters:
`propertyId` - ID of property.
Returns:
property with given id or null if element does not have such property.
addProperty
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)
@OpenApipublic final void addProperty([Property](../../properties/Property.html) prop)
Deprecated, for removal: This API element is subject to removal in a future version.
use [`PresentationElementsManager.addProperty(PresentationElement, Property)`](../../openapi/uml/PresentationElementsManager.html#addProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.properties.Property)). Will be removed in 2026x version.
Add property to a presentation element.
 This method should be called only on a new instance of a presentation element while it is not added into the diagram.
 In order to change some property use [`PresentationElementsManager`](../../openapi/uml/PresentationElementsManager.html)#setPresentationElementProperties
Parameters:
`prop` - property
changeProperties
public void changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)
applyProperties
public final void applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)
Applies properties from given property manager
Parameters:
`manager` - new properties
internalApplyProperties
protected void internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)
Applies properties from given property manager
Parameters:
`changer` - new properties
onFontChange
public void onFontChange()
getAdditionalRenderersToNotifyOnPropertiesChange
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.uml.symbols.SymbolDecorator> getAdditionalRenderersToNotifyOnPropertiesChange()
silentApply
public final void silentApply()
Silently applies all properties after initialization
silentApply
public final void silentApply(boolean recreateListeners)
Silently applies all properties after initialization
Parameters:
`recreateListeners` - recreate listeners if needed
internalSilentApply
public void internalSilentApply()
Silently applies all properties after initialization
adjustBoundsBeforeChange
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) adjustBoundsBeforeChange([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rec,
 boolean autosizeOperation,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> movedTogether)
Validate bounds before bounds change operation
adjustChildBoundsForMoving
public void adjustChildBoundsForMoving([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds,
 [PresentationElement](PresentationElement.html) element)
For adjusting child bounds when child type is not known but bounds should be corrected.
adjustChildBounds
public void adjustChildBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds,
 [PresentationElement](PresentationElement.html) element)
For adjusting child bounds when child type is not known but bounds should be corrected.
getEffectiveStyleOwner
public final [PresentationElement](PresentationElement.html) getEffectiveStyleOwner()
getEffectiveStyleDelegate
public com.dassault_systemes.modeler.foundation.diagram.style.StylePropertyDelegate getEffectiveStyleDelegate()
Returns:
the effective style property delegate, returned from the effective style owner
getOwnStyleDelegate
public com.dassault_systemes.modeler.foundation.diagram.style.StylePropertyDelegate getOwnStyleDelegate()
Returns:
the own style property delegate
isMovableByMoveManager
public boolean isMovableByMoveManager()
Method indicates if object of this instance must be registered in move manager.
boundsChanged
public final void boundsChanged()
boundsChanged
public final void boundsChanged([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
notifyCreated
public final void notifyCreated()
Notify move manager about created presentation element.
rememberBounds
public void rememberBounds()
Remember old bounds
rememberBounds
public void rememberBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
editName
@OpenApipublic final void editName(@CheckForNull
 [KeyEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/KeyEvent.html) evt)
Starts online diagram editing for a symbol
Parameters:
`evt` - first key event or null
editName
@OpenApipublic void editName(@CheckForNull
 [KeyEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/KeyEvent.html) evt,
 @CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> textEditorOptions)
Starts online diagram editing for a symbol
Parameters:
`evt` - first key event or null
`textEditorOptions` - boolean options for text editor. Passed when creating text editor with
 `TextEditorFactory`
isLayouting
public boolean isLayouting()
setLayouting
public void setLayouting(boolean v)
getManipulatedParent
@CheckForNull
@OpenApipublic final [PresentationElement](PresentationElement.html) getManipulatedParent()
Returns:
first parent with manipulator or null if such does not exist.
getManipulationPreferredDimension
public [UnmodifiableDimension](../../../ui/UnmodifiableDimension.html) getManipulationPreferredDimension()
Returns:
size for manipulator manipulations
getObjectParent
@OpenApipublic [BaseElement](../BaseElement.html) getObjectParent()
Returns the presentation element parent. Implementation of super method.
Specified by:
`[getObjectParent](../BaseElement.html#getObjectParent())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`getObjectParent` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Returns:
the parent of the element.
See Also:
[`getParent()`](#getParent())
notifyRepaintManager
public void notifyRepaintManager(boolean boundsChanged)
Notifies the repaint manager about changes in bounds.
notifyDiagramFrameSizeChange
protected void notifyDiagramFrameSizeChange()
Notify diagram frame about change in this symbol. Change may be a reason for diagram frame
 resize.
firePropertyChange
public void firePropertyChange([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue)
Description copied from interface: `[BaseElement](../BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))`
Delegates `firePropertyChange` to the
 `PropertyChangeSupport`, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new values are equal or null.
Specified by:
`[firePropertyChange](../BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object))` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`firePropertyChange` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Parameters:
`propertyName` - the programmatic name of the property that was changed.
`oldValue` - the old value of the property
`newValue` - the new value of the property
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
setLineColor
public void setLineColor([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) c)
Sets line color
setUseFillColor
public void setUseFillColor(boolean use)
Sets use fill color
findPresentationElement
@CheckForNullpublic static [PresentationElement](PresentationElement.html) findPresentationElement([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> elements,
 com.dassault_systemes.modeler.foundation.model.ModelElement modelElement)
Finds presentation element with given Element among given elements
canChangeElementOwner
public boolean canChangeElementOwner([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> movedTogether,
 @CheckForNull
 [BaseElement](../BaseElement.html) newParent)
Returns true, if symbol does not restrict it's element ownership change
Parameters:
`movedTogether` - collection of the elements, whose will change the parent together with this symbol
`newParent` - new symbol parent
Returns:
true if parent of element can be changed.
canChangeParent
public boolean canChangeParent([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [PresentationElement](PresentationElement.html)> movedTogether,
 @CheckForNull
 [BaseElement](../BaseElement.html) newParent,
 boolean changeElementParent)
Returns true, if element can change parent.
Parameters:
`movedTogether` - collection of the elements, whose will change the parent together with this.
`newParent` - new symbol parent
`changeElementParent` - change element parent
Returns:
true if parent of symbol can be changed
canChangeParent
public final boolean canChangeParent([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) children,
 @CheckForNull
 [BaseElement](../BaseElement.html) newParent)
Returns true, if element can change parent.
Specified by:
`[canChangeParent](../BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement))` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`canChangeParent` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Parameters:
`children` - collection of the elements, whose will change the parent together with this.
`newParent` - new parent object.
Returns:
true if an element can change parent.
getAssignableModelElementsClasses
public final [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] getAssignableModelElementsClasses()
Returns an array of ModelElements classes that can be assigned as ModelElement to this
 PresentationElement. The specific PresentationElement must override this method and return an
 array of specific ModelElements' classes.
Returns:
an array of assignable ModelElements' classes.
setPropertyManagerName
public void setPropertyManagerName(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyManagerName)
getPropertyManagerName
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPropertyManagerName()
getChildPresentationElementForContextMenu
public [PresentationElement](PresentationElement.html) getChildPresentationElementForContextMenu([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt)
Returns child element for showing context menu. Maybe it is better to show context menu for
 child, not for element itself. In such case returns child.
Parameters:
`pt` - the point
Returns:
child or itself.
isCanChildrenChangeEdge
public boolean isCanChildrenChangeEdge()
getBoundsWithChildrenOnEdge
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBoundsWithChildrenOnEdge()
getElementToConnectRelationship
@CheckForNullpublic final [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElementToConnectRelationship(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) relationship,
 boolean asClient)
The same as `#internalGetElementToConnectRelationship(Element, boolean)`, just takes into account SymbolDecorators
Returns:
all possible elements
See Also:
[`getElementsForRelationshipConnecting()`](#getElementsForRelationshipConnecting())
`#internalGetElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element, boolean)`
getModelElementToConnectRelationship
@CheckForNullpublic final com.dassault_systemes.modeler.foundation.model.ModelElement getModelElementToConnectRelationship(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement relationship,
 boolean asClient)
The same as [`internalGetModelElementToConnectRelationship(ModelElement, boolean)`](#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), just takes into account SymbolDecorators
Returns:
all possible elements
isSuitableToConnectRelationship
public final boolean isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd end)
Returns:
true if given possible elements (end of relationship) is suitable to connect given relationship to this symbol
internalGetModelElementToConnectRelationship
@CheckForNullpublic com.dassault_systemes.modeler.foundation.model.ModelElement internalGetModelElementToConnectRelationship(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement relationship,
 boolean asClient)
Returns element that should be used for given relationship connecting.
 All possible elements are returned by method [`getModelElementsForRelationshipConnecting()`](#getModelElementsForRelationshipConnecting()).
Returns:
all possible elements
See Also:
[`getModelElementsForRelationshipConnecting()`](#getModelElementsForRelationshipConnecting())
internalIsSuitableToConnectRelationship
public boolean internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd<?> end)
Returns:
true if given possible elements (end of relationship) is suitable to connect given relationship to this symbol
internalIsSuitableToConnectRelationship
public static boolean internalIsSuitableToConnectRelationship([PresentationElement](PresentationElement.html) symbol,
 com.dassault_systemes.modeler.foundation.model.RelationshipEnd<?> end)
getModelElementToMove
@CheckForNullpublic com.dassault_systemes.modeler.foundation.model.ModelElement getModelElementToMove()
Returns element that should be used for during "move" operation. In most cases this is the same as getElement(),
 but some symbols maybe override and return some other related element.
Returns:
element to move
See Also:
[`getElement()`](#getElement())
getElementsForRelationshipConnecting
public final [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getElementsForRelationshipConnecting()
The same as getElementsForLinkConnecting(), just takes into account SymbolDecorators
Returns:
all possible elements
See Also:
[`getElementsForRelationshipConnecting()`](#getElementsForRelationshipConnecting())
[`getElementToConnectRelationship(Element, boolean)`](#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))
getModelElementsForRelationshipConnecting
public final [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends com.dassault_systemes.modeler.foundation.model.ModelElement> getModelElementsForRelationshipConnecting()
Returns all possible element that can be used for relationships connecting.
Returns:
all possible elements
internalGetModelElementsForRelationshipConnecting
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends com.dassault_systemes.modeler.foundation.model.ModelElement> internalGetModelElementsForRelationshipConnecting()
Returns all possible element that can be used for some relationship connecting.
Returns:
all possible elements
internalGetModelElementsForRelationshipConnecting
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends com.dassault_systemes.modeler.foundation.model.ModelElement> internalGetModelElementsForRelationshipConnecting([PresentationElement](PresentationElement.html) symbol)
isCreateElementListener
protected boolean isCreateElementListener()
setCreateElementListener
public void setCreateElementListener(boolean createElementListener)
createPropertyChangeListener
public final void createPropertyChangeListener()
internalCreatePropertyChangeListener
protected void internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData data)
recreateListeners
public void recreateListeners()
Recreates model listeners for this symbol. This method should be called only in exceptional
 cases when new features to the symbol are added dynamically (e.g. decorators) and model
 listening scope should be expanded.
getConfiguration
protected final [SmartListenerConfig](../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html) getConfiguration()
Returns:
a merged configuration of both static and dynamic configs
getDynamicConfigurations
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> getDynamicConfigurations()
Gets non-cacheable smart listener configurations. Default symbol smart listeners are
 cacheable and reused in all instances of a symbol. Dynamic parts of symbols (e.g. added via
 renderers and decorators) should use dynamic configurations.
Returns:
a list of dynamic smart listener configurations.
disposePropertyChangeListener
protected void disposePropertyChangeListener()
updateAfterLoad
public void updateAfterLoad()
createSmartListenerConfig
protected void createSmartListenerConfig([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SmartListenerConfig](../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)> configurations)
isShowElementTypeAsLabel
public boolean isShowElementTypeAsLabel()
isShowsProxy
public boolean isShowsProxy()
clearShowsProxy
public void clearShowsProxy()
checkShowsProxy
protected boolean checkShowsProxy()
setLoadedVisibility
public final void setLoadedVisibility(boolean visible)
checkProxyVisibility
protected com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)
beforeDelete
public boolean beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand deleteCommand,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) removeTogether)
Method is called before deleting symbol with user "DELETE" action
Parameters:
`removeTogether` - other symbols participating in delete operation
Returns:
true, if symbol can be deleted
tryToDeleteModelElementUponRemoval
public boolean tryToDeleteModelElementUponRemoval()
Override this method if you do not want model element to be deleted upon symbol deletion.
Returns:
true, if model element has to be deleted.
alwaysShowTooltip
public boolean alwaysShowTooltip()
getBoundsShape
@OpenApi
@CheckForNullpublic final [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) getBoundsShape([ConverterToShape](ConverterToShape.html) converterToShape)
Provides a bounding shape of the symbol
Parameters:
`converterToShape` - transform bounding shape according this converter
Returns:
bounding shape of the symbol
internalGetBoundsShape
@CheckForNullpublic [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) internalGetBoundsShape([ConverterToShape](ConverterToShape.html) converterToShape)
getPresentationElementStroke
@OpenApipublic final [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) getPresentationElementStroke()
Return a stroke used to paint symbol's main part
Returns:
a stroke used to paint symbol's main part
isContentHidden
public boolean isContentHidden()
setLineWidth
public void setLineWidth(int width)
getLineWidth
public int getLineWidth()
dynamicLineWidth
public int dynamicLineWidth()
dynamicLineWidth
public int dynamicLineWidth(int width)
getPresentationElementStroke
@OpenApipublic final [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) getPresentationElementStroke(int width)
Return a stroke used to paint symbol's main part
Parameters:
`width` - a custom stroke width. Other stroke parameters will be specific to symbol
Returns:
a stroke used to paint symbol's main part
dynamicStroke
public final [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) dynamicStroke()
dynamicStroke
public [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) dynamicStroke(int width)
dynamicStroke
public [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) dynamicStroke([BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) stroke)
internalGetPresentationElementStroke
public [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) internalGetPresentationElementStroke(int width)
Return a stroke used to paint symbol's main part
Parameters:
`width` - a custom stroke width. Other stroke parameters will be specific to symbol
Returns:
a stroke used to paint symbol's main part
getStroke
@OpenApipublic static [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke([BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) stroke,
 int width)
Get cached stroke of given width.
Parameters:
`stroke` - base stroke.
`width` - of the stroke.
Returns:
stroke
getStroke
@OpenApipublic static [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke(int lineStyle)
Get cached stroke of given style and default width.
Parameters:
`lineStyle` - style of line.
Returns:
stroke
See Also:
[`SOLID_STROKE`](#SOLID_STROKE)
[`DASHED_STROKE`](#DASHED_STROKE)
[`DOTTED_STROKE`](#DOTTED_STROKE)
getStroke
@OpenApipublic static [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke(int lineStyle,
 int width)
Get cached stroke of given style and width.
Parameters:
`lineStyle` - style of line
`width` - width
Returns:
stroke
See Also:
[`SOLID_STROKE`](#SOLID_STROKE)
[`DASHED_STROKE`](#DASHED_STROKE)
[`DOTTED_STROKE`](#DOTTED_STROKE)
getStroke
@OpenApipublic static [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke(int lineStyle,
 int width,
 int join)
Get cached stroke of given style, width and join.
Parameters:
`lineStyle` - style of line
`width` - width
Returns:
stroke
See Also:
[`SOLID_STROKE`](#SOLID_STROKE)
[`DASHED_STROKE`](#DASHED_STROKE)
[`DOTTED_STROKE`](#DOTTED_STROKE)
[`BasicStroke.JOIN_BEVEL`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_BEVEL)
[`BasicStroke.JOIN_MITER`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_MITER)
[`BasicStroke.JOIN_ROUND`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_ROUND)
getStroke
@OpenApipublic static [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke(int lineStyle,
 int width,
 int join,
 int cap)
Get cached stroke of given style, width and join.
Parameters:
`lineStyle` - style of line
`width` - width
Returns:
stroke
See Also:
[`SOLID_STROKE`](#SOLID_STROKE)
[`DASHED_STROKE`](#DASHED_STROKE)
[`DOTTED_STROKE`](#DOTTED_STROKE)
[`BasicStroke.JOIN_BEVEL`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_BEVEL)
[`BasicStroke.JOIN_MITER`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_MITER)
[`BasicStroke.JOIN_ROUND`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_ROUND)
getStroke
@OpenApipublic static [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke(float width,
 int cap,
 int join,
 float miterLimit,
 @CheckForNull
 float[] dash,
 float dash_phase)
Get cached stroke.
See Also:
[`BasicStroke(float, int, int, float, float[], float)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#%3Cinit%3E(float,int,int,float,float%5B%5D,float))
getChildrenWithSymbolProperties
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getChildrenWithSymbolProperties()
isPreserveProportionsWhenGrowing
public boolean isPreserveProportionsWhenGrowing()
Controls if the symbol should preserve proportions when growing.
Returns:
true if proportions should be preserved, false otherwise.
setDummyResizeMode
public boolean setDummyResizeMode(boolean b)
In dummy resize mode symbol may not resize according it children or move children on bounds
 changed and etc. This is more as hack for resize problems during load or diagram layout
Parameters:
`b` - new value
getCenterlinePoint
@CheckForNullpublic [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getCenterlinePoint()
Gets a point for centerline drawing.
Returns:
centerline point.
getCenterlinePointX
public int getCenterlinePointX()
Gets x coordinate for centerline drawing.
Returns:
x coordinate for centerline.
getCenterlinePointY
public int getCenterlinePointY()
Gets y coordinate for centerline drawing.
Returns:
y coordinate for centerline.
getProjectImpl
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public [Project](../../core/Project.html) getProjectImpl()
Deprecated, for removal: This API element is subject to removal in a future version.
use [`Project.getProject(BaseElement)`](../../core/Project.html#getProject(com.nomagic.magicdraw.uml.BaseElement)). Will be removed in 2026x.
This method is deprecated and will be removed soon.
Specified by:
`[getProjectImpl](../MDElement.html#getProjectImpl())` in interface `[MDElement](../MDElement.html)`
Overrides:
`getProjectImpl` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Returns:
project
setNeedRecreateListeners
public void setNeedRecreateListeners(boolean needRecreateListeners)
Set a need to recreated models listeners flag
Parameters:
`needRecreateListeners` - a new value
isNotNull
public boolean isNotNull(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
getModelElement
@CheckForNullpublic com.dassault_systemes.modeler.foundation.model.ModelElement getModelElement()
sSetModelElement
public void sSetModelElement(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element)
setModelElement
public void setModelElement(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class PresentationElement">Class PresentationElement</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.PresentationElement</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code><a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code>, <code><a href="paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">PresentationElement</span>
<span class="extends-implements">extends com.nomagic.magicdraw.uml.MDElementImpl
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a>, <a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a>, <a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></span></div>
<div class="block">Base class for all visual elements used in the UML diagrams.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DASHED_STROKE">DASHED_STROKE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Dashed path stroke.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEFAULT_LINE_WIDTH">DEFAULT_LINE_WIDTH</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOTTED_STROKE">DOTTED_STROKE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Dotted path stroke.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#HANDLE_SIZE">HANDLE_SIZE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MAX_LINE_WIDTH">MAX_LINE_WIDTH</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MIN_LINE_WIDTH">MIN_LINE_WIDTH</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>protected com.dassault_systemes.modeler.foundation.diagram.style.PresentationElementStyle</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#peStyle">peStyle</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHADOW_WIDTH">SHADOW_WIDTH</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Symbol shadow width in pixels</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOLID_STROKE">SOLID_STROKE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Solid path stroke.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PresentationElement</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.PresentationElement)">PresentationElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add given child to this symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">addPresentationElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add given child to this symbol at given index</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPresentationElementWithoutResize</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> prop)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../../openapi/uml/PresentationElementsManager.html#addProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.properties.Property)"><code>PresentationElementsManager.addProperty(PresentationElement, Property)</code></a>.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">adjustBoundsBeforeChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rec,
 boolean autosizeOperation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Validate bounds before bounds change operation</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">For adjusting child bounds when child type is not known but bounds should be corrected.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustChildBoundsForMoving</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">For adjusting child bounds when child type is not known but bounds should be corrected.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#alwaysShowTooltip()">alwaysShowTooltip</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">applyProperties</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies properties from given property manager</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#askDeleteDataConfirmation()">askDeleteDataConfirmation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Declared as interface with default implementation for subclasses.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#atInsert()">atInsert</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invalidates object at insert</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#atInsertChildren()">atInsertChildren</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#autosizeAndResizeManipulatedParent()">autosizeAndResizeManipulatedParent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Autosize and resize manipulated element - itself(if this element has manipulator) or
 manipulated parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#autosizeAndResizeParent()">autosizeAndResizeParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Resize itself and initiate parent resize</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">beforeDelete</a><wbr/>(com.dassault_systemes.modeler.foundation.editing.CompositeCommand deleteCommand,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> removeTogether)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called before deleting symbol with user "DELETE" action</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#boundsChanged()">boundsChanged</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#boundsChanged(java.awt.Rectangle)">boundsChanged</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddChild</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check of given symbol can be added as child into this symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if this object can add element of given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">canAddInstance</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Object view has no children.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canBeDisposedOnUpdate()">canBeDisposedOnUpdate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Some symbols removes themselves on update if they are not valid by model anymore.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeElementOwner</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether,
 <a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if symbol does not restrict it's element ownership change</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">canChangeParent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether,
 <a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent,
 boolean changeElementParent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if element can change parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> children,
 <a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if element can change parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canFill()">canFill</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canHavePaths()">canHavePaths</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">changeProperties</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">checkElementOwnerOnChange</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">checkProxyVisibility</a><wbr/>(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkShowsProxy()">checkShowsProxy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#childrenForMoving()">childrenForMoving</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates selected children for moving or takes result from cached.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearShowsProxy()">clearShowsProxy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; col)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all visible and manipulated elements in this hierarchy.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectSubPresentationElements(java.util.Collection)">collectSubPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all sub-presentation elements into given collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">collectSubPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; predicate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all sub-presentation elements that match given predicate into given collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectSubShowingPresentationElements(java.util.Collection)">collectSubShowingPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; col)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collect all visible children starting from current element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#coversPoint(int,int)">coversPoint</a><wbr/>(int x,
 int y)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">checks if object covers provided point</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">coversPoint</a><wbr/>(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">checks if object covers provided point</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.FillStrategy</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createFillStrategy()">createFillStrategy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.dassault_systemes.modeler.foundation.diagram.style.PresentationElementStyle</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPresentationElementStyle()">createPresentationElementStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the presentation element style for this presentation element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPropertyChangeListener()">createPropertyChangeListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSmartListenerConfig(java.util.List)">createSmartListenerConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#disposePropertyChangeListener()">disposePropertyChangeListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">draw</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Draw symbol using renderer or symbol specific draw if renderer is not available.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawBackground</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbol</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Draw symbol as defined by standard notation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">drawSymbolBackground</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicFillColor()">dynamicFillColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicLineColor()">dynamicLineColor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicLineWidth()">dynamicLineWidth</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicLineWidth(int)">dynamicLineWidth</a><wbr/>(int width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicPaintShadow()">dynamicPaintShadow</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicStroke()">dynamicStroke</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicStroke(int)">dynamicStroke</a><wbr/>(int width)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicStroke(java.awt.BasicStroke)">dynamicStroke</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a> stroke)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicStyleFillColor(java.awt.Color,boolean)">dynamicStyleFillColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color,
 boolean useFill)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicStyleLineColor(java.awt.Color)">dynamicStyleLineColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicStyleTextColor(java.awt.Color)">dynamicStyleTextColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicStyleTransparency()">dynamicStyleTransparency</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicStyleTransparency(javax.swing.Icon)">dynamicStyleTransparency</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected &lt;T&gt; T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicStyleValue(T,java.util.function.BiFunction)">dynamicStyleValue</a><wbr/>(T merged,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html" title="class or interface in java.util.function">BiFunction</a>&lt;com.dassault_systemes.modeler.foundation.common.style.DynamicStyle,<wbr/>T,<wbr/>T&gt; valueProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">dynamicTextAlignment</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dynamicTextColor()">dynamicTextColor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editName(java.awt.event.KeyEvent)">editName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/KeyEvent.html" title="class or interface in java.awt.event">KeyEvent</a> evt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts online diagram editing for a symbol</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/KeyEvent.html" title="class or interface in java.awt.event">KeyEvent</a> evt,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; textEditorOptions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts online diagram editing for a symbol</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.model.ModelElement</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">findOwnerForChildElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns element owner for given child.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.model.ModelElement</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">findOwnerForElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">findPresentationElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements,
 com.dassault_systemes.modeler.foundation.model.ModelElement modelElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds presentation element with given Element among given elements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generateID()">generateID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generate ID.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns diagram of this presentation element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActualElement()">getActualElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Because some views returns theirs parent model element, we do not know have they this member
 set or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.uml.symbols.SymbolDecorator&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAdditionalRenderersToNotifyOnPropertiesChange()">getAdditionalRenderersToNotifyOnPropertiesChange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssignableModelElementsClasses()">getAssignableModelElementsClasses</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns an array of ModelElements classes that can be assigned as ModelElement to this
 PresentationElement.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBounds()">getBounds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method returns bounds of this element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a><wbr/>(<a href="ConverterToShape.html" title="class in com.nomagic.magicdraw.uml.symbols">ConverterToShape</a> converterToShape)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Provides a bounding shape of the symbol</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBoundsToRepaint()">getBoundsToRepaint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return bounds of the symbol that must be repainted.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBoundsWithChildrenOnEdge()">getBoundsWithChildrenOnEdge</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCenterlinePoint()">getCenterlinePoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a point for centerline drawing.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCenterlinePointX()">getCenterlinePointX</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets x coordinate for centerline drawing.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCenterlinePointY()">getCenterlinePointY</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets y coordinate for centerline drawing.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildPresentationElementForContextMenu(java.awt.Point)">getChildPresentationElementForContextMenu</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns child element for showing context menu.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildrenWithSymbolProperties()">getChildrenWithSymbolProperties</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a href="../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConfiguration()">getConfiguration</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>final <a href="DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDiagramPresentationElement()">getDiagramPresentationElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="DiagramPresentationElement.html#get(com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>DiagramPresentationElement.get(PresentationElement)</code></a>.Will be removed in 2026x.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="DiagramSurface.html" title="interface in com.nomagic.magicdraw.uml.symbols">DiagramSurface</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDiagramSurface()">getDiagramSurface</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="DiagramSurface.html#getDiagramSurface(com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>DiagramSurface.getDiagramSurface(PresentationElement)</code></a>.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDrawComparator()">getDrawComparator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDynamicConfigurations()">getDynamicConfigurations</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets non-cacheable smart listener configurations.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDynamicStyleOwner()">getDynamicStyleOwner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.diagram.style.StylePropertyDelegate</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEffectiveStyleDelegate()">getEffectiveStyleDelegate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEffectiveStyleOwner()">getEffectiveStyleOwner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model element of this presentation element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsForRelationshipConnecting()">getElementsForRelationshipConnecting</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The same as getElementsForLinkConnecting(), just takes into account SymbolDecorators</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementToConnectRelationship</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 boolean asClient)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The same as <code>#internalGetElementToConnectRelationship(Element, boolean)</code>, just takes into account SymbolDecorators</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFillColor()">getFillColor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns fill color</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFont()">getFont</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets font of this object view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFontHeight()">getFontHeight</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets font height.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/font/FontRenderContext.html" title="class or interface in java.awt.font">FontRenderContext</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFontRenderContext()">getFontRenderContext</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getIntersection</a><wbr/>(int x,
 int y,
 <a href="paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLineColor()">getLineColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns line color</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLineWidth()">getLineWidth</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedElementAt(java.awt.Point)">getManipulatedElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets manipulated symbol at specified point pt.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind intersectionKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets manipulated symbol at specified point pt.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getManipulatedElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets manipulate symbol at specified point pt.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedIntersectionWith(java.awt.Rectangle)">getManipulatedIntersectionWith</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns vector of manipulated objects whose intersect with given rectangle</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">getManipulatedIntersectionWith</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect,
 boolean completelyCovered)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns vector of manipulated objects whose intersect with given rectangle</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect,
 boolean completelyCovered,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns vector of manipulated objects whose intersect with given rectangle</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getManipulatedIntersectionWith</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns vector of manipulated objects whose intersect with given rectangle</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedParent()">getManipulatedParent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a list of children of this element those have manipulator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulationBounds(java.awt.Point)">getManipulationBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets manipulation bounds of the symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulationPreferredDimension()">getManipulationPreferredDimension</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePoint()">getMiddlePoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns middle point of this element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePoint(java.awt.Point)">getMiddlePoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets middle point of this view,</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePointX()">getMiddlePointX</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePointX(java.awt.Point)">getMiddlePointX</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePointY()">getMiddlePointY</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePointY(java.awt.Point)">getMiddlePointY</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMinimumDimension()">getMinimumDimension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">get minimum possible size for object</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.model.ModelElement</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelElement()">getModelElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends com.dassault_systemes.modeler.foundation.model.ModelElement&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelElementsForRelationshipConnecting()">getModelElementsForRelationshipConnecting</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all possible element that can be used for relationships connecting.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final com.dassault_systemes.modeler.foundation.model.ModelElement</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">getModelElementToConnectRelationship</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement relationship,
 boolean asClient)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The same as <a href="#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)"><code>internalGetModelElementToConnectRelationship(ModelElement, boolean)</code></a>, just takes into account SymbolDecorators</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.model.ModelElement</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelElementToMove()">getModelElementToMove</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns element that should be used for during "move" operation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotCopyBounds()">getNotCopyBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">get not copy bounds of object throws NoRectangleDefinedException</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotZoomedTolerance()">getNotZoomedTolerance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectParent()">getObjectParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the presentation element parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.diagram.style.StylePropertyDelegate</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnStyleDelegate()">getOwnStyleDelegate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParent()">getParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns parent of this element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentSymbolStyleOwner()">getParentSymbolStyleOwner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns parent to which this symbol delegates style attributes related functionality.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreferredBounds()">getPreferredBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculate the smallest rectangle which would fit all contained shapes</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreferredDimension()">getPreferredDimension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns preferable dimension of the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreferredDimensionForAutosize()">getPreferredDimensionForAutosize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns preferable dimension of the element for autosize.This implementation simple returns
 preferred size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPreferredSize()">getPreferredSize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="#getPreferredDimension()"><code>getPreferredDimension()</code></a>.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementAt(int)">getPresentationElementAt</a><wbr/>(int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets object view at specified position from container</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementAt(java.awt.Point)">getPresentationElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets object view at point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets object view at point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets object view at point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets object view at point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementCount()">getPresentationElementCount</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns children count in container.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getPresentationElementIndex</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get index of the given presentation element in  the container.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElements()">getPresentationElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all children of this element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementsAt(java.awt.Point)">getPresentationElementsAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets objects at point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets objects at point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">getPresentationElementsAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets object view at point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">getPresentationElementsAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets object view at point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementStroke()">getPresentationElementStroke</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a stroke used to paint symbol's main part</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementStroke(int)">getPresentationElementStroke</a><wbr/>(int width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a stroke used to paint symbol's main part</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getProjectImpl()">getProjectImpl</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../../core/Project.html#getProject(com.nomagic.magicdraw.uml.BaseElement)"><code>Project.getProject(BaseElement)</code></a>.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>final <a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getProperty(java.lang.String)">getProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <code>PresentationElementsManager#getProperty(PresentationElement)</code>.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>final <a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPropertyManager()">getPropertyManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../../openapi/uml/PresentationElementsManager.html#addProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.properties.Property)"><code>PresentationElementsManager.addProperty(PresentationElement, Property)</code></a>.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyManagerName()">getPropertyManagerName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.SymbolDecorator</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRenderer()">getRenderer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets rendered which could decorate this symbol.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelected()">getSelected</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a list of selected elements in the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a><wbr/>(float width,
 int cap,
 int join,
 float miterLimit,
 float[] dash,
 float dash_phase)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get cached stroke.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(int)">getStroke</a><wbr/>(int lineStyle)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get cached stroke of given style and default width.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(int,int)">getStroke</a><wbr/>(int lineStyle,
 int width)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get cached stroke of given style and width.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(int,int,int)">getStroke</a><wbr/>(int lineStyle,
 int width,
 int join)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get cached stroke of given style, width and join.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(int,int,int,int)">getStroke</a><wbr/>(int lineStyle,
 int width,
 int join,
 int cap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get cached stroke of given style, width and join.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(java.awt.BasicStroke,int)">getStroke</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a> stroke,
 int width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get cached stroke of given width.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.diagram.style.PresentationElementStyle</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyle()">getStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static com.nomagic.magicdraw.uml.symbols.SymbolDecorator</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSymbolRenderer</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTextColor()">getTextColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTolerance()">getTolerance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns tolerance</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibility()">getVisibility</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisiblePresentationElements()">getVisiblePresentationElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleModelDelete()">handleModelDelete</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handles model element delete property Change event.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initialize()">initialize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize symbol and its children state.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initializeAndAutosize()">initializeAndAutosize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize symbol and call autosize recursively</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">internalApplyProperties</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies properties from given property manager</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)">internalBeforeUpdate</a><wbr/>(com.nomagic.magicdraw.uml.symbols.SymbolDecorator renderer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">internalCreatePropertyChangeListener</a><wbr/>(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData data)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">internalGetBoundsShape</a><wbr/>(<a href="ConverterToShape.html" title="class in com.nomagic.magicdraw.uml.symbols">ConverterToShape</a> converterToShape)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends com.dassault_systemes.modeler.foundation.model.ModelElement&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetModelElementsForRelationshipConnecting()">internalGetModelElementsForRelationshipConnecting</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all possible element that can be used for some relationship connecting.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends com.dassault_systemes.modeler.foundation.model.ModelElement&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">internalGetModelElementsForRelationshipConnecting</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.model.ModelElement</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">internalGetModelElementToConnectRelationship</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement relationship,
 boolean asClient)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns element that should be used for given relationship connecting.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetPresentationElementStroke(int)">internalGetPresentationElementStroke</a><wbr/>(int width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a stroke used to paint symbol's main part</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetSpecificFont()">internalGetSpecificFont</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetSpecificTextColor()">internalGetSpecificTextColor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a><wbr/>(com.dassault_systemes.modeler.foundation.model.RelationshipEnd&lt;?&gt; end)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">internalIsSuitableToConnectRelationship</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol,
 com.dassault_systemes.modeler.foundation.model.RelationshipEnd&lt;?&gt; end)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSilentApply()">internalSilentApply</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Silently applies all properties after initialization</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSnapToGrid(float)">internalSnapToGrid</a><wbr/>(float step)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalSnapToGrid(java.awt.Point,float)">internalSnapToGrid</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p,
 float step)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalUpdatePresentationElement()">internalUpdatePresentationElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Internal symbol update method for subclassing.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intersects(int,int,int,int)">intersects</a><wbr/>(int x,
 int y,
 int width,
 int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">checks whether object intersects with given rectangle</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">intersects</a><wbr/>(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">checks whether object intersects with given rectangle</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#invalidate()">invalidate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invalidates this element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCanChildrenChangeEdge()">isCanChildrenChangeEdge</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isChildVisible</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if given child of this object is visible.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isContentHidden()">isContentHidden</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateElementListener()">isCreateElementListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDetectable()">isDetectable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Not detectable symbols are not drawn even they are visible.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisposed()">isDisposed</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if element was explicitly disposed by calling <a href="#dispose()"><code>dispose()</code></a> method.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLayouting()">isLayouting</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMovableByMoveManager()">isMovableByMoveManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method indicates if object of this instance must be registered in move manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNotNull</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if current element is parent of given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isParentOf</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if object is child of this object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isPreserveProportionsWhenGrowing()">isPreserveProportionsWhenGrowing</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Controls if the symbol should preserve proportions when growing.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSelected()">isSelected</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if this element is selected in the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowElementTypeAsLabel()">isShowElementTypeAsLabel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowsProxy()">isShowsProxy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSnapToGrid()">isSnapToGrid</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSortable()">isSortable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If OV is sortable (must be added to sort manager for sorting) method must return true;</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">isSuitableToConnectRelationship</a><wbr/>(com.dassault_systemes.modeler.foundation.model.RelationshipEnd end)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTextEditable()">isTextEditable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks text editing flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseFillColor()">isUseFillColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseFillColorByProperty()">isUseFillColorByProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseGradientForFill()">isUseGradientForFill</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Do we need to use gradient for fill color? Checks diagram property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isVisible()">isVisible</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isVisibleInDiagram()">isVisibleInDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if this symbol is visible in diagram (visible itself and its parent is visible)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isVisibleOrShrunken()">isVisibleOrShrunken</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePathElements()">movePathElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#movePathElementsRecursively()">movePathElementsRecursively</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#mustShowContextMenu()">mustShowContextMenu</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#notifyCreated()">notifyCreated</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notify move manager about created presentation element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#notifyDiagramFrameSizeChange()">notifyDiagramFrameSizeChange</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notify diagram frame about change in this symbol.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#notifyRepaintManager(boolean)">notifyRepaintManager</a><wbr/>(boolean boundsChanged)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notifies the repaint manager about changes in bounds.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildAdd</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">onChildRemove</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#onDiagramSurfaceSet()">onDiagramSurfaceSet</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#onFind()">onFind</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Scrolls diagram canvas to this symbol and selects this symbol</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#onFind(boolean)">onFind</a><wbr/>(boolean center)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Scrolls diagram canvas to this symbol and selects this symbol</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#onFontChange()">onFontChange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">onParentChange</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> oldChildParent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornments</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintAdornmentsBackground</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildren</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenAndAdornments</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Paint symbol adornments and children</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintChildrenBackground</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelf</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">paintSelfBackground</a><wbr/>(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#preDisposeOnUpdate()">preDisposeOnUpdate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Validate symbol against model and try to fix it before actual symbol update.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prepareForLineDrawing(java.awt.Graphics2D)">prepareForLineDrawing</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Prepares graphics for line drawing</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prepareForShadowDrawing(java.awt.Graphics2D)">prepareForShadowDrawing</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Prepares graphics for symbol shadow drawing.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prepareForTextDrawing(java.awt.Graphics2D)">prepareForTextDrawing</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Prepares graphics for text drawing</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens for property change it can be: data was edited text box was edited</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#recreateListeners()">recreateListeners</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Recreates model listeners for this symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#recursiveAutosize()">recursiveAutosize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Resize recursively all symbols.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerInSortManager()">registerInSortManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers this view in the sort manager</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#rememberBounds()">rememberBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remember old bounds</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#rememberBounds(java.awt.Rectangle)">rememberBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeFromSortManager()">removeFromSortManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes this OV from sort manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeItSelfOnUpdate()">removeItSelfOnUpdate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove itself during update and register this changed in command history.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">removePresentationElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given child</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resizeParent()">resizeParent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method that initiates parent resize to accommodate children if some child's bounds are
 changed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sAddPresentationElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add given child to this symbol.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">sAddPresentationElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add given child to this symbol at given index</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#selectChildrenForMoving()">selectChildrenForMoving</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculates children for moving together with this symbol.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#selectObjectsForMoving()">selectObjectsForMoving</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">if calling simple set bounds for container shapes container moves itself and inner/related
 views This method selects which views must be moved.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#selectPathsForMoving(java.util.List)">selectPathsForMoving</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; subPresentationElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Select paths to move with current symbol from deep structure.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAllSelected(boolean)">setAllSelected</a><wbr/>(boolean select)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Selects(or deselects) all presentation elements in the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBounds(int,int,int,int)">setBounds</a><wbr/>(int x,
 int y,
 int width,
 int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setBounds(java.awt.Rectangle)">setBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">sets bounds of this object view</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreateElementListener(boolean)">setCreateElementListener</a><wbr/>(boolean createElementListener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDummyResizeMode(boolean)">setDummyResizeMode</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">In dummy resize mode symbol may not resize according it children or move children on bounds
 changed and etc.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFillColor(java.awt.Color)">setFillColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> c)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets fill color</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFont(java.awt.Font)">setFont</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets font for this object view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayouting(boolean)">setLayouting</a><wbr/>(boolean v)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLineColor(java.awt.Color)">setLineColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> c)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets line color</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLineWidth(int)">setLineWidth</a><wbr/>(int width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoadedVisibility(boolean)">setLoadedVisibility</a><wbr/>(boolean visible)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLocation(int,int)">setLocation</a><wbr/>(int x,
 int y)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sets location of object</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLocation(java.awt.Point)">setLocation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sets location of object</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">setModelElement</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNeedRecreateListeners(boolean)">setNeedRecreateListeners</a><wbr/>(boolean needRecreateListeners)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a need to recreated models listeners flag</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setParent</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets parent for this view.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPresentationElements(java.util.List)">setPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets children of this element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPropertyManagerName(java.lang.String)">setPropertyManagerName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyManagerName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelected(boolean)">setSelected</a><wbr/>(boolean select)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Selects or deselects this presentation element in the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelected(java.util.List)">setSelected</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Selects given elements in the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSize(int,int)">setSize</a><wbr/>(int width,
 int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">set dimension of draw object</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSize(com.nomagic.ui.UnmodifiableDimension)">setSize</a><wbr/>(<a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a> size)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">set dimension of draw object</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSize(java.awt.Dimension)">setSize</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">set dimension of draw object</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTextColor(java.awt.Color)">setTextColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> c)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets text color</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTextEditable(boolean)">setTextEditable</a><wbr/>(boolean editable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets text editing flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseFillColor(boolean)">setUseFillColor</a><wbr/>(boolean use)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets use fill color</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">setVisibility</a><wbr/>(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets element visibility flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVisible(boolean)">setVisible</a><wbr/>(boolean visible)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets element visibility flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#silentApply()">silentApply</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Silently applies all properties after initialization</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#silentApply(boolean)">silentApply</a><wbr/>(boolean recreateListeners)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Silently applies all properties after initialization</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simpleSetBounds(int,int,int,int)">simpleSetBounds</a><wbr/>(int x,
 int y,
 int width,
 int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simpleSetBounds(java.awt.Rectangle)">simpleSetBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets bounding rectangle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#snapToGrid(java.awt.Point,float)">snapToGrid</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p,
 float step)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Snap to grid this point</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#snapToGrid(java.awt.Rectangle,float)">snapToGrid</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r,
 float step)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Snap to grid this rectangle</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#snapViewToGrid(float)">snapViewToGrid</a><wbr/>(float step)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Snap to grid this point</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#sortObjectsByX(java.util.List)">sortObjectsByX</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; vector)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sorts objectViews by x ascending.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#sortObjectsByY(java.util.List)">sortObjectsByY</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; vector)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sorts objectViews by y in ascending order.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sRemovePresentationElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given child</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetBounds(int,int,int,int)">sSetBounds</a><wbr/>(int x,
 int y,
 int width,
 int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#sSetBounds(java.awt.Rectangle)">sSetBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets bounds of this object view only.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">sSetElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetLocation(int,int)">sSetLocation</a><wbr/>(int x,
 int y)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets location of object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetLocation(java.awt.Point)">sSetLocation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sets location of object</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">sSetModelElement</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">sSetParent</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets parent for this view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetParentForAll(java.util.Collection)">sSetParentForAll</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets itself as parent to the all PresentationElement from given vector.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetPresentationElements(java.util.List)">sSetPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets children of this element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetSize(int,int)">sSetSize</a><wbr/>(int width,
 int height)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets dimension of draw object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetSize(com.nomagic.ui.UnmodifiableDimension)">sSetSize</a><wbr/>(<a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a> size)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">set dimension of draw object</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetSize(java.awt.Dimension)">sSetSize</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">set dimension of draw object</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">sSetVisibility</a><wbr/>(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets element visibility flag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetVisible(boolean)">sSetVisible</a><wbr/>(boolean visible)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets element visibility flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#tryToDeleteModelElementUponRemoval()">tryToDeleteModelElementUponRemoval</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Override this method if you do not want model element to be deleted upon symbol deletion.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#update()">update</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Major presentation element update by model element method.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateAfterLoad()">updateAfterLoad</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateLabelsIgnoringSuspendableLater(java.util.Collection)">updateLabelsIgnoringSuspendableLater</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.uml.symbols.shapes.LabelWrapper&gt; wrappers)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateLater()">updateLater</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers this symbol to postponed "update" at the end of current command execution.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateModelByView()">updateModelByView</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates model according current view structure.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateModelByViewInternal()">updateModelByViewInternal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates model according current view structure.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateViewAfterPropertyChange()">updateViewAfterPropertyChange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#useParentProperties()">useParentProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="#useParentStyle()"><code>useParentStyle()</code></a></div>
</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, setResourceIDProvider, sGetID, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../BaseElement.html#isSelfChangeable()">isSelfChangeable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></h3>
<code><a href="../MDElement.html#getProject()">getProject</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.utils.NameOwner">Methods inherited from interface com.nomagic.magicdraw.utils.<a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></h3>
<code><a href="../../utils/NameOwner.html#getName()">getName</a></code></div>
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
<section class="detail" id="MAX_LINE_WIDTH">
<h3>MAX_LINE_WIDTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">double</span> <span class="element-name">MAX_LINE_WIDTH</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.MAX_LINE_WIDTH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MIN_LINE_WIDTH">
<h3>MIN_LINE_WIDTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">double</span> <span class="element-name">MIN_LINE_WIDTH</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.MIN_LINE_WIDTH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HANDLE_SIZE">
<h3>HANDLE_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">HANDLE_SIZE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.HANDLE_SIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOLID_STROKE">
<h3>SOLID_STROKE</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SOLID_STROKE</span></div>
<div class="block">Solid path stroke.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.SOLID_STROKE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DASHED_STROKE">
<h3>DASHED_STROKE</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DASHED_STROKE</span></div>
<div class="block">Dashed path stroke.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.DASHED_STROKE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOTTED_STROKE">
<h3>DOTTED_STROKE</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DOTTED_STROKE</span></div>
<div class="block">Dotted path stroke.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.DOTTED_STROKE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHADOW_WIDTH">
<h3>SHADOW_WIDTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SHADOW_WIDTH</span></div>
<div class="block">Symbol shadow width in pixels</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.SHADOW_WIDTH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_LINE_WIDTH">
<h3>DEFAULT_LINE_WIDTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DEFAULT_LINE_WIDTH</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.DEFAULT_LINE_WIDTH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="peStyle">
<h3>peStyle</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.dassault_systemes.modeler.foundation.diagram.style.PresentationElementStyle</span> <span class="element-name">peStyle</span></div>
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
<h3>PresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PresentationElement</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>PresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PresentationElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span></div>
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
<section class="detail" id="sSetElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>sSetElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="generateID()">
<h3>generateID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">generateID</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.uml.MDElementImpl</code></span></div>
<div class="block">Generate ID.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>generateID</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">Returns model element of this presentation element. Some presentation elements (for example
 TextBoxes) do not have model elements.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../ModelElementProvider.html#getElement()">getElement</a></code> in interface <code><a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code></dd>
<dt>Returns:</dt>
<dd>model element of this presentation element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActualElement()">
<h3>getActualElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getActualElement</span>()</div>
<div class="block">Because some views returns theirs parent model element, we do not know have they this member
 set or not.</div>
</section>
</li>
<li>
<section class="detail" id="sSetParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>sSetParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetParent</span><wbr/><span class="parameters">(@CheckForNull
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span></div>
<div class="block">Sets parent for this view.
 For adding symbols to other symbols use
 <a href="#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>addPresentationElement(PresentationElement)</code></a> or
 <a href="#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>sAddPresentationElement(PresentationElement)</code></a>}</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent view</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParent(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>setParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParent</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> parent)</span></div>
<div class="block">Sets parent for this view.
 For adding symbols to other symbols use
 <a href="#addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>addPresentationElement(PresentationElement)</code></a> or
 <a href="#sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>sAddPresentationElement(PresentationElement)</code></a>}</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent view</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onParentChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>onParentChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onParentChange</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> oldChildParent)</span></div>
</section>
</li>
<li>
<section class="detail" id="onChildAdd(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>onChildAdd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onChildAdd</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</span></div>
</section>
</li>
<li>
<section class="detail" id="onChildRemove(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>onChildRemove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onChildRemove</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</span></div>
</section>
</li>
<li>
<section class="detail" id="hasSharedModelElement()">
<h3>hasSharedModelElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasSharedModelElement</span>()</div>
<div class="block">Returns true if <code>ModelElement</code> of this symbol can represented with other symbol.
 If <code>ModelElement</code> is not shared,  it can be deleted together with symbol deleting.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if element of this symbol can be represented with other symbol.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTextEditable(boolean)">
<h3>setTextEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTextEditable</span><wbr/><span class="parameters">(boolean editable)</span></div>
<div class="block">Sets text editing flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>editable</code> - flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTextEditable()">
<h3>isTextEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTextEditable</span>()</div>
<div class="block">Checks text editing flag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if the object view text is editable; <code>false</code> otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectSubPresentationElements(java.util.Collection)">
<h3>collectSubPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">collectSubPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; collection)</span></div>
<div class="block">Collects all sub-presentation elements into given collection.
 Includes this symbol too.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection in which sub presentation elements should be collected.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectSubPresentationElements(java.util.Collection,java.util.function.Predicate)">
<h3>collectSubPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">collectSubPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; predicate)</span></div>
<div class="block">Collects all sub-presentation elements that match given predicate into given collection.
 Includes this symbol too.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection in which sub presentation elements should be collected.</dd>
<dd><code>predicate</code> - predicate that will check if sub element should be included.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectSubShowingPresentationElements(java.util.Collection)">
<h3>collectSubShowingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">collectSubShowingPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; col)</span></div>
<div class="block">Collect all visible children starting from current element. In case some element in hierarchy
 is not visible, children of this element are not added also even if they are visible.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>col</code> - result</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementAt(java.awt.Point)">
<h3>getPresentationElementAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getPresentationElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p)</span></div>
<div class="block">Gets object view at point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p</code> - object view at point location</dd>
<dt>Returns:</dt>
<dd>object view at this point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getPresentationElementAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getPresentationElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">Gets object view at point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p</code> - object view at point location</dd>
<dd><code>kind</code> - intersection kind to check for</dd>
<dt>Returns:</dt>
<dd>object view at this point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">
<h3>getPresentationElementAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getPresentationElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)</span></div>
<div class="block">Gets object view at point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relativePoint</code> - object view at point location.</dd>
<dd><code>sortManagerProvider</code> - sort manager for searching elements.</dd>
<dt>Returns:</dt>
<dd>object view at this point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getPresentationElementAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getPresentationElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">Gets object view at point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relativePoint</code> - object view at point location.</dd>
<dd><code>sortManagerProvider</code> - sort manager for searching elements.</dd>
<dd><code>kind</code> - intersection kind to check for</dd>
<dt>Returns:</dt>
<dd>object view at this point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementsAt(java.awt.Point)">
<h3>getPresentationElementsAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElementsAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p)</span></div>
<div class="block">Gets objects at point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p</code> - object view at point location.</dd>
<dt>Returns:</dt>
<dd>object view at this point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getPresentationElementsAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElementsAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">Gets objects at point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p</code> - object view at point location.</dd>
<dd><code>kind</code> - intersection kind to check for</dd>
<dt>Returns:</dt>
<dd>object view at this point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">
<h3>getPresentationElementsAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElementsAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)</span></div>
<div class="block">Gets object view at point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relativePoint</code> - object view at point location.</dd>
<dd><code>sortManagerProvider</code> - sort manager for searching elements.</dd>
<dt>Returns:</dt>
<dd>object view at this point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementsAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getPresentationElementsAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElementsAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">Gets object view at point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relativePoint</code> - object view at point location.</dd>
<dd><code>sortManagerProvider</code> - sort manager for searching elements.</dd>
<dd><code>kind</code> - intersection kind to check for</dd>
<dt>Returns:</dt>
<dd>object view at this point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementAt(int)">
<h3>getPresentationElementAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getPresentationElementAt</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Gets object view at specified position from container</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - container element index</dd>
<dt>Returns:</dt>
<dd>symbol at given index</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementCount()">
<h3>getPresentationElementCount</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">int</span> <span class="element-name">getPresentationElementCount</span>()</div>
<div class="block">Returns children count in container.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>children count in container.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementIndex(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getPresentationElementIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPresentationElementIndex</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Get index of the given presentation element in  the container.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - presentation element</dd>
<dt>Returns:</dt>
<dd>index in the presentation element container or -1 if such presentation element can not be found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentOf(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isParentOf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isParentOf</span><wbr/><span class="parameters">(@CheckForNull
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</span></div>
<div class="block">Checks if object is child of this object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>child</code> - object to check.</dd>
<dt>Returns:</dt>
<dd>true if obj is child of this object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentOf(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isParentOf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isParentOf</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">BaseElement</a></code></span></div>
<div class="block">Returns true, if current element is parent of given element.
 Return false in this implementation.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>isParentOf</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>obj</code> - the given element(possible child).</dd>
<dt>Returns:</dt>
<dd>true if obj is the parent of this object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onDiagramSurfaceSet()">
<h3>onDiagramSurfaceSet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onDiagramSurfaceSet</span>()</div>
</section>
</li>
<li>
<section class="detail" id="registerInSortManager()">
<h3>registerInSortManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerInSortManager</span>()</div>
<div class="block">Registers this view in the sort manager</div>
</section>
</li>
<li>
<section class="detail" id="getDiagramSurface()">
<h3>getDiagramSurface</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="DiagramSurface.html" title="interface in com.nomagic.magicdraw.uml.symbols">DiagramSurface</a></span> <span class="element-name">getDiagramSurface</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="DiagramSurface.html#getDiagramSurface(com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>DiagramSurface.getDiagramSurface(PresentationElement)</code></a>. Will be removed in 2026x version.</div>
</div>
<div class="block">Returns diagram surface for this presentation element. DiagramSurface is null if diagram of
 this element is not opened in some window.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram surface or null if diagram is not opened.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#clone()">clone</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>clone</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParent()">
<h3>getParent</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getParent</span>()</div>
<div class="block">Returns parent of this element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent of this element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreferredSize()">
<h3>getPreferredSize</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2022x",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a></span> <span class="element-name">getPreferredSize</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="#getPreferredDimension()"><code>getPreferredDimension()</code></a>. Will be removed in 2026x version.</div>
</div>
<div class="block">Returns preferable dimension of the element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>preferred dimension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreferredDimension()">
<h3>getPreferredDimension</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getPreferredDimension</span>()</div>
<div class="block">Returns preferable dimension of the element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>preferred dimension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreferredDimensionForAutosize()">
<h3>getPreferredDimensionForAutosize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getPreferredDimensionForAutosize</span>()</div>
<div class="block">Returns preferable dimension of the element for autosize.This implementation simple returns
 preferred size.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>preferred dimension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreferredBounds()">
<h3>getPreferredBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getPreferredBounds</span>()</div>
<div class="block">Calculate the smallest rectangle which would fit all contained shapes</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>rectangle</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMinimumDimension()">
<h3>getMinimumDimension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getMinimumDimension</span>()</div>
<div class="block">get minimum possible size for object</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>minimum dimension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSize(com.nomagic.ui.UnmodifiableDimension)">
<h3>setSize</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setSize</span><wbr/><span class="parameters">(<a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a> size)</span></div>
<div class="block">set dimension of draw object</div>
</section>
</li>
<li>
<section class="detail" id="setSize(java.awt.Dimension)">
<h3>setSize</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setSize</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size)</span></div>
<div class="block">set dimension of draw object</div>
</section>
</li>
<li>
<section class="detail" id="sSetSize(java.awt.Dimension)">
<h3>sSetSize</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sSetSize</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> size)</span></div>
<div class="block">set dimension of draw object</div>
</section>
</li>
<li>
<section class="detail" id="sSetSize(com.nomagic.ui.UnmodifiableDimension)">
<h3>sSetSize</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sSetSize</span><wbr/><span class="parameters">(<a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a> size)</span></div>
<div class="block">set dimension of draw object</div>
</section>
</li>
<li>
<section class="detail" id="setSize(int,int)">
<h3>setSize</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setSize</span><wbr/><span class="parameters">(int width,
 int height)</span></div>
<div class="block">set dimension of draw object</div>
</section>
</li>
<li>
<section class="detail" id="sSetSize(int,int)">
<h3>sSetSize</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sSetSize</span><wbr/><span class="parameters">(int width,
 int height)</span></div>
<div class="block">Sets dimension of draw object.</div>
</section>
</li>
<li>
<section class="detail" id="setLocation(java.awt.Point)">
<h3>setLocation</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setLocation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span></div>
<div class="block">sets location of object</div>
</section>
</li>
<li>
<section class="detail" id="sSetLocation(java.awt.Point)">
<h3>sSetLocation</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sSetLocation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span></div>
<div class="block">sets location of object</div>
</section>
</li>
<li>
<section class="detail" id="setLocation(int,int)">
<h3>setLocation</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setLocation</span><wbr/><span class="parameters">(int x,
 int y)</span></div>
<div class="block">sets location of object</div>
</section>
</li>
<li>
<section class="detail" id="sSetLocation(int,int)">
<h3>sSetLocation</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sSetLocation</span><wbr/><span class="parameters">(int x,
 int y)</span></div>
<div class="block">Sets location of object.</div>
</section>
</li>
<li>
<section class="detail" id="setBounds(java.awt.Rectangle)">
<h3>setBounds</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">setBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</span>
                        throws <span class="exceptions"><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></span></div>
<div class="block">sets bounds of this object view</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rect</code> - rectangle of bounds</dd>
<dt>Throws:</dt>
<dd><code><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetBounds(java.awt.Rectangle)">
<h3>sSetBounds</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">sSetBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</span>
                         throws <span class="exceptions"><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></span></div>
<div class="block">Sets bounds of this object view only.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rect</code> - rectangle of bounds.</dd>
<dt>Throws:</dt>
<dd><code><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetBounds(int,int,int,int)">
<h3>sSetBounds</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sSetBounds</span><wbr/><span class="parameters">(int x,
 int y,
 int width,
 int height)</span></div>
</section>
</li>
<li>
<section class="detail" id="simpleSetBounds(int,int,int,int)">
<h3>simpleSetBounds</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">simpleSetBounds</span><wbr/><span class="parameters">(int x,
 int y,
 int width,
 int height)</span></div>
</section>
</li>
<li>
<section class="detail" id="setBounds(int,int,int,int)">
<h3>setBounds</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setBounds</span><wbr/><span class="parameters">(int x,
 int y,
 int width,
 int height)</span></div>
</section>
</li>
<li>
<section class="detail" id="simpleSetBounds(java.awt.Rectangle)">
<h3>simpleSetBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">simpleSetBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</span></div>
<div class="block">Sets bounding rectangle.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rect</code> - new bounding rectangle.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="movePathElements()">
<h3>movePathElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">movePathElements</span>()</div>
</section>
</li>
<li>
<section class="detail" id="movePathElementsRecursively()">
<h3>movePathElementsRecursively</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">movePathElementsRecursively</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getMiddlePoint()">
<h3>getMiddlePoint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getMiddlePoint</span>()</div>
<div class="block">Returns middle point of this element. Middle point for shapes usually will be center point of
 bounds, middle point for paths will be center of path curve.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>point that is considered as middle for this element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMiddlePointX()">
<h3>getMiddlePointX</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMiddlePointX</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getMiddlePointY()">
<h3>getMiddlePointY</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMiddlePointY</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getMiddlePoint(java.awt.Point)">
<h3>getMiddlePoint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getMiddlePoint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint)</span></div>
<div class="block">Gets middle point of this view,</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relativePoint</code> - relative point</dd>
<dt>Returns:</dt>
<dd>middle point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMiddlePointX(java.awt.Point)">
<h3>getMiddlePointX</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">getMiddlePointX</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint)</span></div>
</section>
</li>
<li>
<section class="detail" id="getMiddlePointY(java.awt.Point)">
<h3>getMiddlePointY</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">getMiddlePointY</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint)</span></div>
</section>
</li>
<li>
<section class="detail" id="getIntersection(int,int,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>getIntersection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getIntersection</span><wbr/><span class="parameters">(int x,
 int y,
 @CheckForNull
 <a href="paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</span></div>
</section>
</li>
<li>
<section class="detail" id="getBounds()">
<h3>getBounds</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBounds</span>()
                    throws <span class="exceptions"><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></span></div>
<div class="block">Method returns bounds of this element.
 Use PresentationElementsManager to change a bounds of the element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>bounds of the element.</dd>
<dt>Throws:</dt>
<dd><code><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></code> - when bounds can not be calculated (some presentation
                                     elements are abstract and can not have bounds).</dd>
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
<section class="detail" id="getManipulationBounds(java.awt.Point)">
<h3>getManipulationBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getManipulationBounds</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> relativePoint)</span></div>
<div class="block">Gets manipulation bounds of the symbol. Manipulation bounds might
 differ from symbol bounds, they can be larger or smaller to help
 user manipulate the symbol.</div>
<dl class="notes">
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBoundsToRepaint</span>()
                             throws <span class="exceptions"><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></span></div>
<div class="block">Return bounds of the symbol that must be repainted. throws NoRectangleDefinedException</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>rectangle of bounds</dd>
<dt>Throws:</dt>
<dd><code><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotCopyBounds()">
<h3>getNotCopyBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getNotCopyBounds</span>()
                           throws <span class="exceptions"><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></span></div>
<div class="block">get not copy bounds of object throws NoRectangleDefinedException</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>rectangle of bounds</dd>
<dt>Throws:</dt>
<dd><code><a href="NoRectangleDefinedException.html" title="class in com.nomagic.magicdraw.uml.symbols">NoRectangleDefinedException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="intersects(int,int,int,int)">
<h3>intersects</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">intersects</span><wbr/><span class="parameters">(int x,
 int y,
 int width,
 int height)</span></div>
<div class="block">checks whether object intersects with given rectangle</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if object and rectangle intersects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="coversPoint(int,int)">
<h3>coversPoint</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">coversPoint</span><wbr/><span class="parameters">(int x,
 int y)</span></div>
<div class="block">checks if object covers provided point</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if object covers this point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="intersects(int,int,int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>intersects</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">boolean</span> <span class="element-name">intersects</span><wbr/><span class="parameters">(int x,
 int y,
 int width,
 int height,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">checks whether object intersects with given rectangle</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if object and rectangle intersects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="coversPoint(int,int,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>coversPoint</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">boolean</span> <span class="element-name">coversPoint</span><wbr/><span class="parameters">(int x,
 int y,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">checks if object covers provided point</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if object covers this point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selectObjectsForMoving()">
<h3>selectObjectsForMoving</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">selectObjectsForMoving</span>()</div>
<div class="block">if calling simple set bounds for container shapes container moves itself and inner/related
 views This method selects which views must be moved.</div>
</section>
</li>
<li>
<section class="detail" id="childrenForMoving()">
<h3>childrenForMoving</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">childrenForMoving</span>()</div>
<div class="block">Calculates selected children for moving or takes result from cached.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of children for moving.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#selectChildrenForMoving()"><code>selectChildrenForMoving()</code></a></li>
<li><code>PresentationElement.StructureCache</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selectChildrenForMoving()">
<h3>selectChildrenForMoving</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">selectChildrenForMoving</span>()</div>
<div class="block">Calculates children for moving together with this symbol. This method should not be called by
 user. This method is just for implementation and override purpose. childrenForMoving() must
 be used outside.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#childrenForMoving()"><code>childrenForMoving()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selectPathsForMoving(java.util.List)">
<h3>selectPathsForMoving</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</span> <span class="element-name">selectPathsForMoving</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; subPresentationElements)</span></div>
<div class="block">Select paths to move with current symbol from deep structure.
 Some paths can be connected to current symbol, but owned in some deep child of this symbol.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subPresentationElements</code> - sub children of this symbol</dd>
<dt>Returns:</dt>
<dd>paths to move together with current symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPresentationElements(java.util.List)">
<h3>setPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</span></div>
<div class="block">Sets children of this element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - children</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetPresentationElements(java.util.List)">
<h3>sSetPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</span></div>
<div class="block">Sets children of this element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - children</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElements()">
<h3>getPresentationElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElements</span>()</div>
<div class="block">Returns all children of this element</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all children of this element. The collection is unmodifiable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisiblePresentationElements()">
<h3>getVisiblePresentationElements</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getVisiblePresentationElements</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>not modifiable list of visible elements, including not detectable ones that should not be painted.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isDetectable()"><code>isDetectable()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>removePresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePresentationElement</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Removes given child</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - child</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sRemovePresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>sRemovePresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sRemovePresentationElement</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Removes given child</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - child</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>addPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">addPresentationElement</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Add given child to this symbol.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - child to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">
<h3>addPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPresentationElement</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index)</span></div>
<div class="block">Add given child to this symbol at given index</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - child to add</dd>
<dd><code>index</code> - index to add at. Can be -1</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPresentationElementWithoutResize(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>addPresentationElementWithoutResize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPresentationElementWithoutResize</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>sAddPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sAddPresentationElement</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Add given child to this symbol.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - child to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sAddPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,int)">
<h3>sAddPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sAddPresentationElement</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element,
 int index)</span></div>
<div class="block">Add given child to this symbol at given index</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - child to add</dd>
<dd><code>index</code> - index to add at. Can be -1</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="draw(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>draw</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">draw</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
<div class="block">Draw symbol using renderer or symbol specific draw if renderer is not available. Also draw adornments.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - paint context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="drawBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>drawBackground</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">drawBackground</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
</section>
</li>
<li>
<section class="detail" id="drawSymbolBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>drawSymbolBackground</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">drawSymbolBackground</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
</section>
</li>
<li>
<section class="detail" id="paintSelfBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>paintSelfBackground</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintSelfBackground</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
</section>
</li>
<li>
<section class="detail" id="paintChildrenBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>paintChildrenBackground</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintChildrenBackground</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
</section>
</li>
<li>
<section class="detail" id="drawSymbol(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>drawSymbol</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">drawSymbol</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
<div class="block">Draw symbol as defined by standard notation. Does not use renderers and adornments.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - paint context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="paintChildrenAndAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>paintChildrenAndAdornments</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">paintChildrenAndAdornments</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
<div class="block">Paint symbol adornments and children</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - paint context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="paintSelf(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>paintSelf</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">paintSelf</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
</section>
</li>
<li>
<section class="detail" id="paintChildren(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>paintChildren</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">paintChildren</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
</section>
</li>
<li>
<section class="detail" id="paintAdornmentsBackground(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>paintAdornmentsBackground</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintAdornmentsBackground</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
</section>
</li>
<li>
<section class="detail" id="paintAdornments(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext)">
<h3>paintAdornments</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintAdornments</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.DiagramPaintContext context)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRenderer()">
<h3>getRenderer</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.SymbolDecorator</span> <span class="element-name">getRenderer</span>()</div>
<div class="block">Gets rendered which could decorate this symbol.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>symbol renderer.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSymbolRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getSymbolRenderer</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected static</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.SymbolDecorator</span> <span class="element-name">getSymbolRenderer</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDrawComparator()">
<h3>getDrawComparator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getDrawComparator</span>()</div>
</section>
</li>
<li>
<section class="detail" id="mustShowContextMenu()">
<h3>mustShowContextMenu</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">mustShowContextMenu</span>()</div>
</section>
</li>
<li>
<section class="detail" id="canHavePaths()">
<h3>canHavePaths</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canHavePaths</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if symbol can have connected paths. Return false here.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>canAddChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddChild</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block">Check of given symbol can be added as child into this symbol.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>symbol</code> - symbol</dd>
<dt>Returns:</dt>
<dd>true if symbol can be added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddChild(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canAddChild</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">canAddChild</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../MDElement.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a></code> in interface <code><a href="../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>canAddChild</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddInstance(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>canAddInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAddInstance</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block">Object view has no children.</div>
</section>
</li>
<li>
<section class="detail" id="canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canAddInstance</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">canAddInstance</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">BaseElement</a></code></span></div>
<div class="block">Checks if this object can add element of given type.
 Current implementation returns false.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>canAddInstance</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Returns:</dt>
<dd>true if this object can elements of a given type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">disposes ends of links when link is deleted</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#dispose()">dispose</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>dispose</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disposeChildren()">
<h3>disposeChildren</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">disposeChildren</span>()</div>
<div class="block">Removes all children from itself. Such removing causes calling dispose for every child.</div>
</section>
</li>
<li>
<section class="detail" id="setAllSelected(boolean)">
<h3>setAllSelected</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAllSelected</span><wbr/><span class="parameters">(boolean select)</span></div>
<div class="block">Selects(or deselects) all presentation elements in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>select</code> - select or deselect all elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelected(java.util.List)">
<h3>setSelected</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelected</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</span></div>
<div class="block">Selects given elements in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements to select.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelected(boolean)">
<h3>setSelected</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelected</span><wbr/><span class="parameters">(boolean select)</span></div>
<div class="block">Selects or deselects this presentation element in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>select</code> - select or deselect this presentation element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelected()">
<h3>getSelected</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getSelected</span>()</div>
<div class="block">Returns a list of selected elements in the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of selected elements. List is unmodifiable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSelected()">
<h3>isSelected</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSelected</span>()</div>
<div class="block">Returns true, if this element is selected in the diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if this element is selected in the diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDetectable()">
<h3>isDetectable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDetectable</span>()</div>
<div class="block">Not detectable symbols are not drawn even they are visible.
 Not detectable symbols cannot be selected even they have manipulator.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if selection and painting of this symbol is currently allowed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initializeAndAutosize()">
<h3>initializeAndAutosize</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">initializeAndAutosize</span>()</div>
<div class="block">Initialize symbol and call autosize recursively</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#recursiveAutosize()"><code>recursiveAutosize()</code></a></li>
<li><a href="#initialize()"><code>initialize()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="recursiveAutosize()">
<h3>recursiveAutosize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">recursiveAutosize</span>()</div>
<div class="block">Resize recursively all symbols. Method must be called if something is changed in symbol (for
 example minimum size) and you want to resize (autosize) all hierarchy</div>
</section>
</li>
<li>
<section class="detail" id="initialize()">
<h3>initialize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">initialize</span>()</div>
<div class="block">Initialize symbol and its children state. Symbol must be initialized before doing any
 resize, painting and etc. These operations can lead to unpredictable results otherwise.</div>
</section>
</li>
<li>
<section class="detail" id="getDiagramPresentationElement()">
<h3>getDiagramPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public final</span> <span class="return-type"><a href="DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></span> <span class="element-name">getDiagramPresentationElement</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="DiagramPresentationElement.html#get(com.nomagic.magicdraw.uml.symbols.PresentationElement)"><code>DiagramPresentationElement.get(PresentationElement)</code></a>.Will be removed in 2026x.</div>
</div>
<div class="block">Returns diagram of this presentation element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram of this presentation element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractDiagramPresentationElement()">
<h3>getAbstractDiagramPresentationElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></span> <span class="element-name">getAbstractDiagramPresentationElement</span>()</div>
<div class="block">Returns diagram of this presentation element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram of this presentation element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onFind()">
<h3>onFind</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">onFind</span>()</div>
<div class="block">Scrolls diagram canvas to this symbol and selects this symbol</div>
</section>
</li>
<li>
<section class="detail" id="onFind(boolean)">
<h3>onFind</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">onFind</span><wbr/><span class="parameters">(boolean center)</span></div>
<div class="block">Scrolls diagram canvas to this symbol and selects this symbol</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>center</code> - if true, centers current view in the center of the window.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resizeParent()">
<h3>resizeParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resizeParent</span>()</div>
<div class="block">Method that initiates parent resize to accommodate children if some child's bounds are
 changed.</div>
</section>
</li>
<li>
<section class="detail" id="autosizeAndResizeParent()">
<h3>autosizeAndResizeParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">autosizeAndResizeParent</span>()</div>
<div class="block">Resize itself and initiate parent resize</div>
</section>
</li>
<li>
<section class="detail" id="autosizeAndResizeManipulatedParent()">
<h3>autosizeAndResizeManipulatedParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">autosizeAndResizeManipulatedParent</span>()</div>
<div class="block">Autosize and resize manipulated element - itself(if this element has manipulator) or
 manipulated parent.</div>
</section>
</li>
<li>
<section class="detail" id="update()">
<h3>update</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">update</span>()</div>
<div class="block">Major presentation element update by model element method. Any outside code must call this
 method for updating the symbol by data. This method calls internal update
 (updatePresentationElement()) and also calls update for symbol decorator if such exits.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#internalUpdatePresentationElement()"><code>internalUpdatePresentationElement()</code></a></li>
<li><code>SymbolDecorator</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalBeforeUpdate(com.nomagic.magicdraw.uml.symbols.SymbolDecorator)">
<h3>internalBeforeUpdate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalBeforeUpdate</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.uml.symbols.SymbolDecorator renderer)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeItSelfOnUpdate()">
<h3>removeItSelfOnUpdate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">removeItSelfOnUpdate</span>()</div>
<div class="block">Remove itself during update and register this changed in command history.</div>
</section>
</li>
<li>
<section class="detail" id="internalUpdatePresentationElement()">
<h3>internalUpdatePresentationElement</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalUpdatePresentationElement</span>()</div>
<div class="block">Internal symbol update method for subclassing. It is called from update as part of full
 update action.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#update()"><code>update()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeDisposedOnUpdate()">
<h3>canBeDisposedOnUpdate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">canBeDisposedOnUpdate</span>()</div>
<div class="block">Some symbols removes themselves on update if they are not valid by model anymore. Check if such operation is
 possible at this moment. Do not remove symbol on undo or redo operations.
 We very often have situation when symbol is updated during these operations and structure in model is not yet fully restored.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if path can be removed if not valid</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="preDisposeOnUpdate()">
<h3>preDisposeOnUpdate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">preDisposeOnUpdate</span>()</div>
<div class="block">Validate symbol against model and try to fix it before actual symbol update. If symbol is not valid and can not be fixed,
 request symbol dispose by returning true.
 Check if symbol should be disposed, because model does not correspond to symbol.
 This may happen for example if path supplier or client in model is changed, but path still is connected to symbols of old ends.
 <p>
 Method also can fix symbol if possible - for example reconnect path to other symbols in diagram and etc.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if symbol must be disposed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFontHeight()">
<h3>getFontHeight</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">int</span> <span class="element-name">getFontHeight</span>()</div>
<div class="block">Gets font height.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>font height</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseGradientForFill()">
<h3>isUseGradientForFill</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseGradientForFill</span>()</div>
<div class="block">Do we need to use gradient for fill color? Checks diagram property.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram gradient fill color value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFontRenderContext()">
<h3>getFontRenderContext</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/font/FontRenderContext.html" title="class or interface in java.awt.font">FontRenderContext</a></span> <span class="element-name">getFontRenderContext</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isVisible()">
<h3>isVisible</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">isVisible</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if element visibility is <code>PresentationElementVisibility.VISIBLE</code></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>PresentationElementVisibility.isVisible()</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVisibleOrShrunken()">
<h3>isVisibleOrShrunken</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">isVisibleOrShrunken</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if element visibility is <code>PresentationElementVisibility.VISIBLE</code> or <code>PresentationElementVisibility.SHRUNKEN</code></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>PresentationElementVisibility.isVisibleOrShrunken()</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetVisible(boolean)">
<h3>sSetVisible</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sSetVisible</span><wbr/><span class="parameters">(boolean visible)</span></div>
<div class="block">Sets element visibility flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visible</code> - flag value</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>PresentationElementVisibility.apply(boolean)</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVisible(boolean)">
<h3>setVisible</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setVisible</span><wbr/><span class="parameters">(boolean visible)</span></div>
<div class="block">Sets element visibility flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visible</code> - flag value</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>PresentationElementVisibility.apply(boolean)</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibility()">
<h3>getVisibility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility</span> <span class="element-name">getVisibility</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element visibility</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">
<h3>sSetVisibility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetVisibility</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)</span></div>
<div class="block">Sets element visibility flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visibility</code> - flag value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">
<h3>setVisibility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisibility</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)</span></div>
<div class="block">Sets element visibility flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visibility</code> - flag value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeFromSortManager()">
<h3>removeFromSortManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeFromSortManager</span>()</div>
<div class="block">Removes this OV from sort manager.</div>
</section>
</li>
<li>
<section class="detail" id="updateViewAfterPropertyChange()">
<h3>updateViewAfterPropertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateViewAfterPropertyChange</span>()</div>
</section>
</li>
<li>
<section class="detail" id="updateLater()">
<h3>updateLater</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateLater</span>()</div>
<div class="block">Registers this symbol to postponed "update" at the end of current command execution.
 Symbol will be updated when all other commands are executed.
 If this is not possible to register, updates symbol immediately.</div>
</section>
</li>
<li>
<section class="detail" id="updateLabelsIgnoringSuspendableLater(java.util.Collection)">
<h3>updateLabelsIgnoringSuspendableLater</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateLabelsIgnoringSuspendableLater</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.uml.symbols.shapes.LabelWrapper&gt; wrappers)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateModelByViewInternal()">
<h3>updateModelByViewInternal</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">updateModelByViewInternal</span>()</div>
<div class="block">Updates model according current view structure. In some cases changes in model must
 be made keeping in mind current structure of symbols.
 <p>
 Does nothing here, but subclasses may override</p></div>
</section>
</li>
<li>
<section class="detail" id="updateModelByView()">
<h3>updateModelByView</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">updateModelByView</span>()</div>
<div class="block">Updates model according current view structure. In some cases changes in model must
 be made keeping in mind current structure of symbols.</div>
</section>
</li>
<li>
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</span></div>
<div class="block">Listens for property change it can be: data was edited text box was edited</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleModelDelete()">
<h3>handleModelDelete</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleModelDelete</span>()</div>
<div class="block">Handles model element delete property Change event.
 Typical implementation is to delete this symbol from parent.</div>
</section>
</li>
<li>
<section class="detail" id="setFont(java.awt.Font)">
<h3>setFont</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setFont</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font)</span></div>
<div class="block">Sets font for this object view.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>font</code> - new font.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFont()">
<h3>getFont</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a></span> <span class="element-name">getFont</span>()</div>
<div class="block">Gets font of this object view. It returns font from the project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>font of the text object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalGetSpecificFont()">
<h3>internalGetSpecificFont</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a></span> <span class="element-name">internalGetSpecificFont</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getHumanType()">
<h3>getHumanType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanType</span>()</div>
<div class="block">Returns human representation of the data type</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#getHumanType()">getHumanType</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>getHumanType</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Returns:</dt>
<dd>the name of the data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHumanName()">
<h3>getHumanName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanName</span>()</div>
<div class="block">Returns human representation of the data type</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#getHumanName()">getHumanName</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>getHumanName</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Returns:</dt>
<dd>the name of the data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="askDeleteDataConfirmation()">
<h3>askDeleteDataConfirmation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">askDeleteDataConfirmation</span>()</div>
<div class="block">Declared as interface with default implementation for subclasses. If some subclasses upon
 delete may ask about delete data object as well, they have to redefine this method and return
 true. By default all objects are removed without asking</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>confirmation status -- true if asking is necessary, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManipulatedElementAt(java.awt.Point)">
<h3>getManipulatedElementAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getManipulatedElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</span></div>
<div class="block">Gets manipulated symbol at specified point pt.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - <code> Point </code></dd>
<dt>Returns:</dt>
<dd>manipulate symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getManipulatedElementAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getManipulatedElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind intersectionKind)</span></div>
<div class="block">Gets manipulated symbol at specified point pt.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - <code> Point </code></dd>
<dd><code>intersectionKind</code> - intersection kind to check for</dd>
<dt>Returns:</dt>
<dd>manipulate symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManipulatedElementAt(java.awt.Point,com.nomagic.magicdraw.uml.symbols.SortManagerProvider)">
<h3>getManipulatedElementAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getManipulatedElementAt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 com.nomagic.magicdraw.uml.symbols.SortManagerProvider sortManagerProvider)</span></div>
<div class="block">Gets manipulate symbol at specified point pt.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - <code> Point </code></dd>
<dd><code>sortManagerProvider</code> - provides sort manager in which to search.</dd>
<dt>Returns:</dt>
<dd>manipulate symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sSetParentForAll(java.util.Collection)">
<h3>sSetParentForAll</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">sSetParentForAll</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</span></div>
<div class="block">Sets itself as parent to the all PresentationElement from given vector.</div>
</section>
</li>
<li>
<section class="detail" id="hasManipulator()">
<h3>hasManipulator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasManipulator</span>()</div>
<div class="block">Returns true, if view has manipulator (is selectable)</div>
</section>
</li>
<li>
<section class="detail" id="invalidate()">
<h3>invalidate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">invalidate</span>()</div>
<div class="block">Invalidates this element.</div>
</section>
</li>
<li>
<section class="detail" id="isSnapToGrid()">
<h3>isSnapToGrid</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isSnapToGrid</span>()</div>
</section>
</li>
<li>
<section class="detail" id="snapToGrid(java.awt.Rectangle,float)">
<h3>snapToGrid</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">snapToGrid</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r,
 float step)</span></div>
<div class="block">Snap to grid this rectangle</div>
</section>
</li>
<li>
<section class="detail" id="snapToGrid(java.awt.Point,float)">
<h3>snapToGrid</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">snapToGrid</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p,
 float step)</span></div>
<div class="block">Snap to grid this point</div>
</section>
</li>
<li>
<section class="detail" id="internalSnapToGrid(java.awt.Point,float)">
<h3>internalSnapToGrid</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalSnapToGrid</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p,
 float step)</span></div>
</section>
</li>
<li>
<section class="detail" id="snapViewToGrid(float)">
<h3>snapViewToGrid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">snapViewToGrid</span><wbr/><span class="parameters">(float step)</span></div>
<div class="block">Snap to grid this point</div>
</section>
</li>
<li>
<section class="detail" id="internalSnapToGrid(float)">
<h3>internalSnapToGrid</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalSnapToGrid</span><wbr/><span class="parameters">(float step)</span></div>
</section>
</li>
<li>
<section class="detail" id="collectSubManipulatedElements(java.util.List)">
<h3>collectSubManipulatedElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">collectSubManipulatedElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; col)</span></div>
<div class="block">Collects all visible and manipulated elements in this hierarchy.</div>
</section>
</li>
<li>
<section class="detail" id="getManipulatedPresentationElements()">
<h3>getManipulatedPresentationElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getManipulatedPresentationElements</span>()</div>
<div class="block">Returns a list of children of this element those have manipulator.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of manipulated elements. Collection is unmodifiable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasManipulatedPresentationElements()">
<h3>hasManipulatedPresentationElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">hasManipulatedPresentationElements</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if at least one child is manipulated and visible</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTolerance()">
<h3>getTolerance</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">int</span> <span class="element-name">getTolerance</span>()</div>
<div class="block">Returns tolerance</div>
</section>
</li>
<li>
<section class="detail" id="getNotZoomedTolerance()">
<h3>getNotZoomedTolerance</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">getNotZoomedTolerance</span>()</div>
</section>
</li>
<li>
<section class="detail" id="atInsert()">
<h3>atInsert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">atInsert</span>()</div>
<div class="block">Invalidates object at insert</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#atInsert()">atInsert</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>atInsert</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisposed()">
<h3>isDisposed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisposed</span>()</div>
<div class="block">Checks if element was explicitly disposed by calling <a href="#dispose()"><code>dispose()</code></a> method. Calling <a href="#atInsert()"><code>atInsert()</code></a> clears dispose flag.
 Newly created element is not disposed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if element was disposed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="atInsertChildren()">
<h3>atInsertChildren</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">atInsertChildren</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sortObjectsByX(java.util.List)">
<h3>sortObjectsByX</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">sortObjectsByX</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; vector)</span></div>
<div class="block">Sorts objectViews by x ascending.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector</code> - - Vector which contains Object Views.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sortObjectsByY(java.util.List)">
<h3>sortObjectsByY</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">sortObjectsByY</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; vector)</span></div>
<div class="block">Sorts objectViews by y in ascending order.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector</code> - - Vector which contains Object Views.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSortable()">
<h3>isSortable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSortable</span>()</div>
<div class="block">If OV is sortable (must be added to sort manager for sorting) method must return true;</div>
</section>
</li>
<li>
<section class="detail" id="isChildVisible(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isChildVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isChildVisible</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</span></div>
<div class="block">Returns true if given child of this object is visible. For methods and attributes Method or
 Attribute field view can hide objects without changing visibility flag method isVisible()
 returns true, but method can be not show. This method must avoid such situations and return
 true if parent shows this object and false if it hides.</div>
</section>
</li>
<li>
<section class="detail" id="isVisibleInDiagram()">
<h3>isVisibleInDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isVisibleInDiagram</span>()</div>
<div class="block">Check if this symbol is visible in diagram (visible itself and its parent is visible)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if symbol is visible in the diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManipulatedIntersectionWith(java.awt.Rectangle)">
<h3>getManipulatedIntersectionWith</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getManipulatedIntersectionWith</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</span></div>
<div class="block">Returns vector of manipulated objects whose intersect with given rectangle</div>
</section>
</li>
<li>
<section class="detail" id="getManipulatedIntersectionWith(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getManipulatedIntersectionWith</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getManipulatedIntersectionWith</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">Returns vector of manipulated objects whose intersect with given rectangle</div>
</section>
</li>
<li>
<section class="detail" id="getManipulatedIntersectionWith(java.awt.Rectangle,boolean)">
<h3>getManipulatedIntersectionWith</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getManipulatedIntersectionWith</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect,
 boolean completelyCovered)</span></div>
<div class="block">Returns vector of manipulated objects whose intersect with given rectangle</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>completelyCovered</code> - take only completely covered by rectangle symbols. Ignore symbols
                          with just intersected bounds.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManipulatedIntersectionWith(java.awt.Rectangle,boolean,com.nomagic.magicdraw.uml.symbols.IntersectionKind)">
<h3>getManipulatedIntersectionWith</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getManipulatedIntersectionWith</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect,
 boolean completelyCovered,
 com.nomagic.magicdraw.uml.symbols.IntersectionKind kind)</span></div>
<div class="block">Returns vector of manipulated objects whose intersect with given rectangle</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>completelyCovered</code> - take only completely covered by rectangle symbols. Ignore symbols
                          with just intersected bounds.</dd>
<dd><code>kind</code> - intersection kind to check for</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwnerForElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext)">
<h3>findOwnerForElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.model.ModelElement</span> <span class="element-name">findOwnerForElement</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> newParent,
 com.dassault_systemes.modeler.foundation.model.ModelElementOwnershipContext ownershipContext)</span></div>
</section>
</li>
<li>
<section class="detail" id="findOwnerForChildElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>findOwnerForChildElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.model.ModelElement</span> <span class="element-name">findOwnerForChildElement</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</span></div>
<div class="block">Returns element owner for given child.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>most suitable owner for given child's element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkElementOwnerOnChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>checkElementOwnerOnChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">checkElementOwnerOnChange</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> child)</span></div>
</section>
</li>
<li>
<section class="detail" id="getFillColor()">
<h3>getFillColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">getFillColor</span>()</div>
<div class="block">Returns fill color</div>
</section>
</li>
<li>
<section class="detail" id="getLineColor()">
<h3>getLineColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">getLineColor</span>()</div>
<div class="block">Returns line color</div>
</section>
</li>
<li>
<section class="detail" id="canFill()">
<h3>canFill</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">canFill</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if symbol can be filled with some color</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseFillColor()">
<h3>isUseFillColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseFillColor</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>use fill color flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseFillColorByProperty()">
<h3>isUseFillColorByProperty</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isUseFillColorByProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTextColor()">
<h3>getTextColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">getTextColor</span>()</div>
</section>
</li>
<li>
<section class="detail" id="internalGetSpecificTextColor()">
<h3>internalGetSpecificTextColor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">internalGetSpecificTextColor</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setTextColor(java.awt.Color)">
<h3>setTextColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTextColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> c)</span></div>
<div class="block">Sets text color</div>
</section>
</li>
<li>
<section class="detail" id="setFillColor(java.awt.Color)">
<h3>setFillColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFillColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> c)</span></div>
<div class="block">Sets fill color</div>
</section>
</li>
<li>
<section class="detail" id="createFillStrategy()">
<h3>createFillStrategy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.FillStrategy</span> <span class="element-name">createFillStrategy</span>()</div>
</section>
</li>
<li>
<section class="detail" id="dynamicTextColor()">
<h3>dynamicTextColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">dynamicTextColor</span>()</div>
</section>
</li>
<li>
<section class="detail" id="dynamicLineColor()">
<h3>dynamicLineColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">dynamicLineColor</span>()</div>
</section>
</li>
<li>
<section class="detail" id="dynamicFillColor()">
<h3>dynamicFillColor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">dynamicFillColor</span>()</div>
</section>
</li>
<li>
<section class="detail" id="dynamicStyleFillColor(java.awt.Color,boolean)">
<h3>dynamicStyleFillColor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">dynamicStyleFillColor</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color,
 boolean useFill)</span></div>
</section>
</li>
<li>
<section class="detail" id="dynamicStyleLineColor(java.awt.Color)">
<h3>dynamicStyleLineColor</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">dynamicStyleLineColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</span></div>
</section>
</li>
<li>
<section class="detail" id="dynamicStyleTextColor(java.awt.Color)">
<h3>dynamicStyleTextColor</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">dynamicStyleTextColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</span></div>
</section>
</li>
<li>
<section class="detail" id="dynamicStyleTransparency()">
<h3>dynamicStyleTransparency</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">int</span> <span class="element-name">dynamicStyleTransparency</span>()</div>
</section>
</li>
<li>
<section class="detail" id="dynamicStyleTransparency(javax.swing.Icon)">
<h3>dynamicStyleTransparency</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">int</span> <span class="element-name">dynamicStyleTransparency</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> target)</span></div>
</section>
</li>
<li>
<section class="detail" id="dynamicTextAlignment(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition)">
<h3>dynamicTextAlignment</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition</span> <span class="element-name">dynamicTextAlignment</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TextObject.HorizontalPosition target)</span></div>
</section>
</li>
<li>
<section class="detail" id="dynamicStyleValue(T,java.util.function.BiFunction)">
<h3 id="dynamicStyleValue(java.lang.Object,java.util.function.BiFunction)">dynamicStyleValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">T</span> <span class="element-name">dynamicStyleValue</span><wbr/><span class="parameters">(@CheckForNull
 T merged,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiFunction.html" title="class or interface in java.util.function">BiFunction</a>&lt;com.dassault_systemes.modeler.foundation.common.style.DynamicStyle,<wbr/>T,<wbr/>T&gt; valueProvider)</span></div>
</section>
</li>
<li>
<section class="detail" id="dynamicPaintShadow()">
<h3>dynamicPaintShadow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">dynamicPaintShadow</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDynamicStyleOwner()">
<h3>getDynamicStyleOwner</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getDynamicStyleOwner</span>()</div>
</section>
</li>
<li>
<section class="detail" id="prepareForShadowDrawing(java.awt.Graphics2D)">
<h3>prepareForShadowDrawing</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">prepareForShadowDrawing</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g)</span></div>
<div class="block">Prepares graphics for symbol shadow drawing. If diagram allows shadows, sets darker diagram background color to given graphics.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>g</code> - the given graphics</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prepareForLineDrawing(java.awt.Graphics2D)">
<h3>prepareForLineDrawing</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">prepareForLineDrawing</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g)</span></div>
<div class="block">Prepares graphics for line drawing</div>
</section>
</li>
<li>
<section class="detail" id="prepareForTextDrawing(java.awt.Graphics2D)">
<h3>prepareForTextDrawing</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">prepareForTextDrawing</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g)</span></div>
<div class="block">Prepares graphics for text drawing</div>
</section>
</li>
<li>
<section class="detail" id="useParentStyle()">
<h3>useParentStyle</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">useParentStyle</span>()</div>
<div class="block">Does this element uses parent style or has it's own?</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if element does not have style and uses parent's style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="useParentProperties()">
<h3>useParentProperties</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">useParentProperties</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="#useParentStyle()"><code>useParentStyle()</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getParentSymbolStyleOwner()">
<h3>getParentSymbolStyleOwner</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getParentSymbolStyleOwner</span>()</div>
<div class="block">Returns parent to which this symbol delegates style attributes related functionality.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent symbol to delegate or null if this symbol does not delegate.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyManager()">
<h3>getPropertyManager</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public final</span> <span class="return-type"><a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getPropertyManager</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../../openapi/uml/PresentationElementsManager.html#addProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.properties.Property)"><code>PresentationElementsManager.addProperty(PresentationElement, Property)</code></a>. Will be removed in 2026x version.</div>
</div>
<div class="block">Returns the propertyManager of this element. If element does not have properties, empty
 manager will be created.<br/>
 Use method useParentProperties() to check if properties exist.<br/>
 Use PresentationElementsManager to change the properties.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>propertyManager of this element.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#useParentStyle()"><code>useParentStyle()</code></a></li>
<li><code>PresentationElementsManager.setPresentationElementProperties</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPresentationElementStyle()">
<h3>createPresentationElementStyle</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.dassault_systemes.modeler.foundation.diagram.style.PresentationElementStyle</span> <span class="element-name">createPresentationElementStyle</span>()</div>
<div class="block">Creates the presentation element style for this presentation element.
 Override only if a specific style for a specific presentation element should be created.
 The default implementation is to get style though style registry</div>
</section>
</li>
<li>
<section class="detail" id="getStyle()">
<h3>getStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.diagram.style.PresentationElementStyle</span> <span class="element-name">getStyle</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getProperty(java.lang.String)">
<h3>getProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public final</span> <span class="return-type"><a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span> <span class="element-name">getProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyId)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <code>PresentationElementsManager#getProperty(PresentationElement)</code>. Will be removed in 2026x version.</div>
</div>
<div class="block">Returns element's property with given id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyId</code> - ID of property.</dd>
<dt>Returns:</dt>
<dd>property with given id or null if element does not have such property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProperty(com.nomagic.magicdraw.properties.Property)">
<h3>addProperty</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">addProperty</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> prop)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../../openapi/uml/PresentationElementsManager.html#addProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.properties.Property)"><code>PresentationElementsManager.addProperty(PresentationElement, Property)</code></a>. Will be removed in 2026x version.</div>
</div>
<div class="block">Add property to a presentation element.
 This method should be called only on a new instance of a presentation element while it is not added into the diagram.
 In order to change some property use <a href="../../openapi/uml/PresentationElementsManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>PresentationElementsManager</code></a>#setPresentationElementProperties</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prop</code> - property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="changeProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">
<h3>changeProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">changeProperties</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</span></div>
</section>
</li>
<li>
<section class="detail" id="applyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">
<h3>applyProperties</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">applyProperties</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</span></div>
<div class="block">Applies properties from given property manager</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - new properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalApplyProperties(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger)">
<h3>internalApplyProperties</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalApplyProperties</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.styledelegates.PresentationElementStyleChanger changer)</span></div>
<div class="block">Applies properties from given property manager</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>changer</code> - new properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onFontChange()">
<h3>onFontChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onFontChange</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAdditionalRenderersToNotifyOnPropertiesChange()">
<h3>getAdditionalRenderersToNotifyOnPropertiesChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.uml.symbols.SymbolDecorator&gt;</span> <span class="element-name">getAdditionalRenderersToNotifyOnPropertiesChange</span>()</div>
</section>
</li>
<li>
<section class="detail" id="silentApply()">
<h3>silentApply</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">silentApply</span>()</div>
<div class="block">Silently applies all properties after initialization</div>
</section>
</li>
<li>
<section class="detail" id="silentApply(boolean)">
<h3>silentApply</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">silentApply</span><wbr/><span class="parameters">(boolean recreateListeners)</span></div>
<div class="block">Silently applies all properties after initialization</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>recreateListeners</code> - recreate listeners if needed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalSilentApply()">
<h3>internalSilentApply</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">internalSilentApply</span>()</div>
<div class="block">Silently applies all properties after initialization</div>
</section>
</li>
<li>
<section class="detail" id="adjustBoundsBeforeChange(java.awt.Rectangle,boolean,java.util.Collection)">
<h3>adjustBoundsBeforeChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">adjustBoundsBeforeChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rec,
 boolean autosizeOperation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether)</span></div>
<div class="block">Validate bounds before bounds change operation</div>
</section>
</li>
<li>
<section class="detail" id="adjustChildBoundsForMoving(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>adjustChildBoundsForMoving</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">adjustChildBoundsForMoving</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">For adjusting child bounds when child type is not known but bounds should be corrected.</div>
</section>
</li>
<li>
<section class="detail" id="adjustChildBounds(java.awt.Rectangle,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>adjustChildBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">adjustChildBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">For adjusting child bounds when child type is not known but bounds should be corrected.</div>
</section>
</li>
<li>
<section class="detail" id="getEffectiveStyleOwner()">
<h3>getEffectiveStyleOwner</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getEffectiveStyleOwner</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getEffectiveStyleDelegate()">
<h3>getEffectiveStyleDelegate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.diagram.style.StylePropertyDelegate</span> <span class="element-name">getEffectiveStyleDelegate</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the effective style property delegate, returned from the effective style owner</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnStyleDelegate()">
<h3>getOwnStyleDelegate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.diagram.style.StylePropertyDelegate</span> <span class="element-name">getOwnStyleDelegate</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the own style property delegate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMovableByMoveManager()">
<h3>isMovableByMoveManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMovableByMoveManager</span>()</div>
<div class="block">Method indicates if object of this instance must be registered in move manager.</div>
</section>
</li>
<li>
<section class="detail" id="boundsChanged()">
<h3>boundsChanged</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">boundsChanged</span>()</div>
</section>
</li>
<li>
<section class="detail" id="boundsChanged(java.awt.Rectangle)">
<h3>boundsChanged</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">boundsChanged</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
</section>
</li>
<li>
<section class="detail" id="notifyCreated()">
<h3>notifyCreated</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">notifyCreated</span>()</div>
<div class="block">Notify move manager about created presentation element.</div>
</section>
</li>
<li>
<section class="detail" id="rememberBounds()">
<h3>rememberBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">rememberBounds</span>()</div>
<div class="block">Remember old bounds</div>
</section>
</li>
<li>
<section class="detail" id="rememberBounds(java.awt.Rectangle)">
<h3>rememberBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">rememberBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
</section>
</li>
<li>
<section class="detail" id="editName(java.awt.event.KeyEvent)">
<h3>editName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">editName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/KeyEvent.html" title="class or interface in java.awt.event">KeyEvent</a> evt)</span></div>
<div class="block">Starts online diagram editing for a symbol</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>evt</code> - first key event or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editName(java.awt.event.KeyEvent,java.util.Map)">
<h3>editName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">editName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/KeyEvent.html" title="class or interface in java.awt.event">KeyEvent</a> evt,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; textEditorOptions)</span></div>
<div class="block">Starts online diagram editing for a symbol</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>evt</code> - first key event or null</dd>
<dd><code>textEditorOptions</code> - boolean options for text editor. Passed when creating text editor with
                          <code>TextEditorFactory</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLayouting()">
<h3>isLayouting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLayouting</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLayouting(boolean)">
<h3>setLayouting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayouting</span><wbr/><span class="parameters">(boolean v)</span></div>
</section>
</li>
<li>
<section class="detail" id="getManipulatedParent()">
<h3>getManipulatedParent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getManipulatedParent</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>first parent with manipulator or null if such does not exist.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManipulationPreferredDimension()">
<h3>getManipulationPreferredDimension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">getManipulationPreferredDimension</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>size for manipulator manipulations</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectParent()">
<h3>getObjectParent</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getObjectParent</span>()</div>
<div class="block">Returns the presentation element parent. Implementation of super method.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#getObjectParent()">getObjectParent</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>getObjectParent</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Returns:</dt>
<dd>the parent of the element.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getParent()"><code>getParent()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="notifyRepaintManager(boolean)">
<h3>notifyRepaintManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">notifyRepaintManager</span><wbr/><span class="parameters">(boolean boundsChanged)</span></div>
<div class="block">Notifies the repaint manager about changes in bounds.</div>
</section>
</li>
<li>
<section class="detail" id="notifyDiagramFrameSizeChange()">
<h3>notifyDiagramFrameSizeChange</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">notifyDiagramFrameSizeChange</span>()</div>
<div class="block">Notify diagram frame about change in this symbol. Change may be a reason for diagram frame
 resize.</div>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">BaseElement</a></code></span></div>
<div class="block">Delegates <code>firePropertyChange</code> to the
 <code>PropertyChangeSupport</code>, the member of this class,
 which reports a bound property update to any registered listeners.
 No event is fired if old and new values are equal or null.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>firePropertyChange</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>propertyName</code> - the programmatic name of the property that was changed.</dd>
<dd><code>oldValue</code> - the old value of the property</dd>
<dd><code>newValue</code> - the new value of the property</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLineColor(java.awt.Color)">
<h3>setLineColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLineColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> c)</span></div>
<div class="block">Sets line color</div>
</section>
</li>
<li>
<section class="detail" id="setUseFillColor(boolean)">
<h3>setUseFillColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseFillColor</span><wbr/><span class="parameters">(boolean use)</span></div>
<div class="block">Sets use fill color</div>
</section>
</li>
<li>
<section class="detail" id="findPresentationElement(java.util.Collection,com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>findPresentationElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">findPresentationElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements,
 com.dassault_systemes.modeler.foundation.model.ModelElement modelElement)</span></div>
<div class="block">Finds presentation element with given Element among given elements</div>
</section>
</li>
<li>
<section class="detail" id="canChangeElementOwner(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">
<h3>canChangeElementOwner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canChangeElementOwner</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether,
 @CheckForNull
 <a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent)</span></div>
<div class="block">Returns true, if symbol does not restrict it's element ownership change</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>movedTogether</code> - collection of the elements, whose will change the parent together with this symbol</dd>
<dd><code>newParent</code> - new symbol parent</dd>
<dt>Returns:</dt>
<dd>true if parent of element can be changed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement,boolean)">
<h3>canChangeParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canChangeParent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; movedTogether,
 @CheckForNull
 <a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent,
 boolean changeElementParent)</span></div>
<div class="block">Returns true, if element can change parent.</div>
<dl class="notes">
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
<section class="detail" id="canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">
<h3>canChangeParent</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">canChangeParent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> children,
 @CheckForNull
 <a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> newParent)</span></div>
<div class="block">Returns true, if element can change parent.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>canChangeParent</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>children</code> - collection of the elements, whose will change the parent together with this.</dd>
<dd><code>newParent</code> - new parent object.</dd>
<dt>Returns:</dt>
<dd>true if an element can change parent.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssignableModelElementsClasses()">
<h3>getAssignableModelElementsClasses</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[]</span> <span class="element-name">getAssignableModelElementsClasses</span>()</div>
<div class="block">Returns an array of ModelElements classes that can be assigned as ModelElement to this
 PresentationElement. The specific PresentationElement must override this method and return an
 array of specific ModelElements' classes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array of assignable ModelElements' classes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPropertyManagerName(java.lang.String)">
<h3>setPropertyManagerName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPropertyManagerName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyManagerName)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPropertyManagerName()">
<h3>getPropertyManagerName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPropertyManagerName</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getChildPresentationElementForContextMenu(java.awt.Point)">
<h3>getChildPresentationElementForContextMenu</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getChildPresentationElementForContextMenu</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt)</span></div>
<div class="block">Returns child element for showing context menu. Maybe it is better to show context menu for
 child, not for element itself. In such case returns child.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pt</code> - the point</dd>
<dt>Returns:</dt>
<dd>child or itself.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCanChildrenChangeEdge()">
<h3>isCanChildrenChangeEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCanChildrenChangeEdge</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getBoundsWithChildrenOnEdge()">
<h3>getBoundsWithChildrenOnEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBoundsWithChildrenOnEdge</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>getElementToConnectRelationship</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElementToConnectRelationship</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> relationship,
 boolean asClient)</span></div>
<div class="block">The same as <code>#internalGetElementToConnectRelationship(Element, boolean)</code>, just takes into account SymbolDecorators</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all possible elements</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getElementsForRelationshipConnecting()"><code>getElementsForRelationshipConnecting()</code></a></li>
<li><code>#internalGetElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element, boolean)</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">
<h3>getModelElementToConnectRelationship</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type">com.dassault_systemes.modeler.foundation.model.ModelElement</span> <span class="element-name">getModelElementToConnectRelationship</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement relationship,
 boolean asClient)</span></div>
<div class="block">The same as <a href="#internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)"><code>internalGetModelElementToConnectRelationship(ModelElement, boolean)</code></a>, just takes into account SymbolDecorators</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all possible elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">
<h3>isSuitableToConnectRelationship</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">isSuitableToConnectRelationship</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.RelationshipEnd end)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if given possible elements (end of relationship) is suitable to connect given relationship to this symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalGetModelElementToConnectRelationship(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">
<h3>internalGetModelElementToConnectRelationship</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.model.ModelElement</span> <span class="element-name">internalGetModelElementToConnectRelationship</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement relationship,
 boolean asClient)</span></div>
<div class="block">Returns element that should be used for given relationship connecting.
 All possible elements are returned by method <a href="#getModelElementsForRelationshipConnecting()"><code>getModelElementsForRelationshipConnecting()</code></a>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all possible elements</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getModelElementsForRelationshipConnecting()"><code>getModelElementsForRelationshipConnecting()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalIsSuitableToConnectRelationship(com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">
<h3>internalIsSuitableToConnectRelationship</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">internalIsSuitableToConnectRelationship</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.RelationshipEnd&lt;?&gt; end)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if given possible elements (end of relationship) is suitable to connect given relationship to this symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalIsSuitableToConnectRelationship(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.dassault_systemes.modeler.foundation.model.RelationshipEnd)">
<h3>internalIsSuitableToConnectRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">internalIsSuitableToConnectRelationship</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol,
 com.dassault_systemes.modeler.foundation.model.RelationshipEnd&lt;?&gt; end)</span></div>
</section>
</li>
<li>
<section class="detail" id="getModelElementToMove()">
<h3>getModelElementToMove</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.model.ModelElement</span> <span class="element-name">getModelElementToMove</span>()</div>
<div class="block">Returns element that should be used for during "move" operation. In most cases this is the same as getElement(),
 but some symbols maybe override and return some other related element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element to move</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getElement()"><code>getElement()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementsForRelationshipConnecting()">
<h3>getElementsForRelationshipConnecting</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getElementsForRelationshipConnecting</span>()</div>
<div class="block">The same as getElementsForLinkConnecting(), just takes into account SymbolDecorators</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all possible elements</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getElementsForRelationshipConnecting()"><code>getElementsForRelationshipConnecting()</code></a></li>
<li><a href="#getElementToConnectRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)"><code>getElementToConnectRelationship(Element, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModelElementsForRelationshipConnecting()">
<h3>getModelElementsForRelationshipConnecting</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends com.dassault_systemes.modeler.foundation.model.ModelElement&gt;</span> <span class="element-name">getModelElementsForRelationshipConnecting</span>()</div>
<div class="block">Returns all possible element that can be used for relationships connecting.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all possible elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalGetModelElementsForRelationshipConnecting()">
<h3>internalGetModelElementsForRelationshipConnecting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends com.dassault_systemes.modeler.foundation.model.ModelElement&gt;</span> <span class="element-name">internalGetModelElementsForRelationshipConnecting</span>()</div>
<div class="block">Returns all possible element that can be used for some relationship connecting.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all possible elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalGetModelElementsForRelationshipConnecting(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>internalGetModelElementsForRelationshipConnecting</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends com.dassault_systemes.modeler.foundation.model.ModelElement&gt;</span> <span class="element-name">internalGetModelElementsForRelationshipConnecting</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
</section>
</li>
<li>
<section class="detail" id="isCreateElementListener()">
<h3>isCreateElementListener</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isCreateElementListener</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCreateElementListener(boolean)">
<h3>setCreateElementListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateElementListener</span><wbr/><span class="parameters">(boolean createElementListener)</span></div>
</section>
</li>
<li>
<section class="detail" id="createPropertyChangeListener()">
<h3>createPropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">createPropertyChangeListener</span>()</div>
</section>
</li>
<li>
<section class="detail" id="internalCreatePropertyChangeListener(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData)">
<h3>internalCreatePropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">internalCreatePropertyChangeListener</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.PresentationElement.SmartListenerConfigData data)</span></div>
</section>
</li>
<li>
<section class="detail" id="recreateListeners()">
<h3>recreateListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">recreateListeners</span>()</div>
<div class="block">Recreates model listeners for this symbol. This method should be called only in exceptional
 cases when new features to the symbol are added dynamically (e.g. decorators) and model
 listening scope should be expanded.</div>
</section>
</li>
<li>
<section class="detail" id="getConfiguration()">
<h3>getConfiguration</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a href="../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">getConfiguration</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a merged configuration of both static and dynamic configs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDynamicConfigurations()">
<h3>getDynamicConfigurations</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt;</span> <span class="element-name">getDynamicConfigurations</span>()</div>
<div class="block">Gets non-cacheable smart listener configurations. Default symbol smart listeners are
 cacheable and reused in all instances of a symbol. Dynamic parts of symbols (e.g. added via
 renderers and decorators) should use dynamic configurations.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of dynamic smart listener configurations.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disposePropertyChangeListener()">
<h3>disposePropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">disposePropertyChangeListener</span>()</div>
</section>
</li>
<li>
<section class="detail" id="updateAfterLoad()">
<h3>updateAfterLoad</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateAfterLoad</span>()</div>
</section>
</li>
<li>
<section class="detail" id="createSmartListenerConfig(java.util.List)">
<h3>createSmartListenerConfig</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createSmartListenerConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowElementTypeAsLabel()">
<h3>isShowElementTypeAsLabel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowElementTypeAsLabel</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowsProxy()">
<h3>isShowsProxy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowsProxy</span>()</div>
</section>
</li>
<li>
<section class="detail" id="clearShowsProxy()">
<h3>clearShowsProxy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearShowsProxy</span>()</div>
</section>
</li>
<li>
<section class="detail" id="checkShowsProxy()">
<h3>checkShowsProxy</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">checkShowsProxy</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLoadedVisibility(boolean)">
<h3>setLoadedVisibility</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setLoadedVisibility</span><wbr/><span class="parameters">(boolean visible)</span></div>
</section>
</li>
<li>
<section class="detail" id="checkProxyVisibility(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility)">
<h3>checkProxyVisibility</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility</span> <span class="element-name">checkProxyVisibility</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.PresentationElementVisibility visibility)</span></div>
</section>
</li>
<li>
<section class="detail" id="beforeDelete(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">
<h3>beforeDelete</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">beforeDelete</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.editing.CompositeCommand deleteCommand,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> removeTogether)</span></div>
<div class="block">Method is called before deleting symbol with user "DELETE" action</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>removeTogether</code> - other symbols participating in delete operation</dd>
<dt>Returns:</dt>
<dd>true, if symbol can be deleted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="tryToDeleteModelElementUponRemoval()">
<h3>tryToDeleteModelElementUponRemoval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">tryToDeleteModelElementUponRemoval</span>()</div>
<div class="block">Override this method if you do not want model element to be deleted upon symbol deletion.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if model element has to be deleted.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="alwaysShowTooltip()">
<h3>alwaysShowTooltip</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">alwaysShowTooltip</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">
<h3>getBoundsShape</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></span> <span class="element-name">getBoundsShape</span><wbr/><span class="parameters">(<a href="ConverterToShape.html" title="class in com.nomagic.magicdraw.uml.symbols">ConverterToShape</a> converterToShape)</span></div>
<div class="block">Provides a bounding shape of the symbol</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>converterToShape</code> - transform bounding shape according this converter</dd>
<dt>Returns:</dt>
<dd>bounding shape of the symbol</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalGetBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">
<h3>internalGetBoundsShape</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></span> <span class="element-name">internalGetBoundsShape</span><wbr/><span class="parameters">(<a href="ConverterToShape.html" title="class in com.nomagic.magicdraw.uml.symbols">ConverterToShape</a> converterToShape)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementStroke()">
<h3>getPresentationElementStroke</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getPresentationElementStroke</span>()</div>
<div class="block">Return a stroke used to paint symbol's main part</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a stroke used to paint symbol's main part</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isContentHidden()">
<h3>isContentHidden</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isContentHidden</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLineWidth(int)">
<h3>setLineWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLineWidth</span><wbr/><span class="parameters">(int width)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLineWidth()">
<h3>getLineWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLineWidth</span>()</div>
</section>
</li>
<li>
<section class="detail" id="dynamicLineWidth()">
<h3>dynamicLineWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">dynamicLineWidth</span>()</div>
</section>
</li>
<li>
<section class="detail" id="dynamicLineWidth(int)">
<h3>dynamicLineWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">dynamicLineWidth</span><wbr/><span class="parameters">(int width)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementStroke(int)">
<h3>getPresentationElementStroke</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getPresentationElementStroke</span><wbr/><span class="parameters">(int width)</span></div>
<div class="block">Return a stroke used to paint symbol's main part</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>width</code> - a custom stroke width. Other stroke parameters will be specific to symbol</dd>
<dt>Returns:</dt>
<dd>a stroke used to paint symbol's main part</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dynamicStroke()">
<h3>dynamicStroke</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">dynamicStroke</span>()</div>
</section>
</li>
<li>
<section class="detail" id="dynamicStroke(int)">
<h3>dynamicStroke</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">dynamicStroke</span><wbr/><span class="parameters">(int width)</span></div>
</section>
</li>
<li>
<section class="detail" id="dynamicStroke(java.awt.BasicStroke)">
<h3>dynamicStroke</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">dynamicStroke</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a> stroke)</span></div>
</section>
</li>
<li>
<section class="detail" id="internalGetPresentationElementStroke(int)">
<h3>internalGetPresentationElementStroke</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">internalGetPresentationElementStroke</span><wbr/><span class="parameters">(int width)</span></div>
<div class="block">Return a stroke used to paint symbol's main part</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>width</code> - a custom stroke width. Other stroke parameters will be specific to symbol</dd>
<dt>Returns:</dt>
<dd>a stroke used to paint symbol's main part</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStroke(java.awt.BasicStroke,int)">
<h3>getStroke</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a> stroke,
 int width)</span></div>
<div class="block">Get cached stroke of given width.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stroke</code> - base stroke.</dd>
<dd><code>width</code> - of the stroke.</dd>
<dt>Returns:</dt>
<dd>stroke</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStroke(int)">
<h3>getStroke</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(int lineStyle)</span></div>
<div class="block">Get cached stroke of given style and default width.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lineStyle</code> - style of line.</dd>
<dt>Returns:</dt>
<dd>stroke</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SOLID_STROKE"><code>SOLID_STROKE</code></a></li>
<li><a href="#DASHED_STROKE"><code>DASHED_STROKE</code></a></li>
<li><a href="#DOTTED_STROKE"><code>DOTTED_STROKE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStroke(int,int)">
<h3>getStroke</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(int lineStyle,
 int width)</span></div>
<div class="block">Get cached stroke of given style and width.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lineStyle</code> - style of line</dd>
<dd><code>width</code> - width</dd>
<dt>Returns:</dt>
<dd>stroke</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SOLID_STROKE"><code>SOLID_STROKE</code></a></li>
<li><a href="#DASHED_STROKE"><code>DASHED_STROKE</code></a></li>
<li><a href="#DOTTED_STROKE"><code>DOTTED_STROKE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStroke(int,int,int)">
<h3>getStroke</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(int lineStyle,
 int width,
 int join)</span></div>
<div class="block">Get cached stroke of given style, width and join.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lineStyle</code> - style of line</dd>
<dd><code>width</code> - width</dd>
<dt>Returns:</dt>
<dd>stroke</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SOLID_STROKE"><code>SOLID_STROKE</code></a></li>
<li><a href="#DASHED_STROKE"><code>DASHED_STROKE</code></a></li>
<li><a href="#DOTTED_STROKE"><code>DOTTED_STROKE</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_BEVEL" title="class or interface in java.awt"><code>BasicStroke.JOIN_BEVEL</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_MITER" title="class or interface in java.awt"><code>BasicStroke.JOIN_MITER</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_ROUND" title="class or interface in java.awt"><code>BasicStroke.JOIN_ROUND</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStroke(int,int,int,int)">
<h3>getStroke</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(int lineStyle,
 int width,
 int join,
 int cap)</span></div>
<div class="block">Get cached stroke of given style, width and join.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lineStyle</code> - style of line</dd>
<dd><code>width</code> - width</dd>
<dt>Returns:</dt>
<dd>stroke</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#SOLID_STROKE"><code>SOLID_STROKE</code></a></li>
<li><a href="#DASHED_STROKE"><code>DASHED_STROKE</code></a></li>
<li><a href="#DOTTED_STROKE"><code>DOTTED_STROKE</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_BEVEL" title="class or interface in java.awt"><code>BasicStroke.JOIN_BEVEL</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_MITER" title="class or interface in java.awt"><code>BasicStroke.JOIN_MITER</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_ROUND" title="class or interface in java.awt"><code>BasicStroke.JOIN_ROUND</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStroke(float,int,int,float,float[],float)">
<h3>getStroke</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(float width,
 int cap,
 int join,
 float miterLimit,
 @CheckForNull
 float[] dash,
 float dash_phase)</span></div>
<div class="block">Get cached stroke.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html#%3Cinit%3E(float,int,int,float,float%5B%5D,float)" title="class or interface in java.awt"><code>BasicStroke(float, int, int, float, float[], float)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildrenWithSymbolProperties()">
<h3>getChildrenWithSymbolProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getChildrenWithSymbolProperties</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isPreserveProportionsWhenGrowing()">
<h3>isPreserveProportionsWhenGrowing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPreserveProportionsWhenGrowing</span>()</div>
<div class="block">Controls if the symbol should preserve proportions when growing.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if proportions should be preserved, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDummyResizeMode(boolean)">
<h3>setDummyResizeMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setDummyResizeMode</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">In dummy resize mode symbol may not resize according it children or move children on bounds
 changed and etc. This is more as hack for resize problems during load or diagram layout</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - new value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCenterlinePoint()">
<h3>getCenterlinePoint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getCenterlinePoint</span>()</div>
<div class="block">Gets a point for centerline drawing.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>centerline point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCenterlinePointX()">
<h3>getCenterlinePointX</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getCenterlinePointX</span>()</div>
<div class="block">Gets x coordinate for centerline drawing.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>x coordinate for centerline.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCenterlinePointY()">
<h3>getCenterlinePointY</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getCenterlinePointY</span>()</div>
<div class="block">Gets y coordinate for centerline drawing.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>y coordinate for centerline.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectImpl()">
<h3>getProjectImpl</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProjectImpl</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../../core/Project.html#getProject(com.nomagic.magicdraw.uml.BaseElement)"><code>Project.getProject(BaseElement)</code></a>. Will be removed in 2026x.</div>
</div>
<div class="block">This method is deprecated and will be removed soon.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../MDElement.html#getProjectImpl()">getProjectImpl</a></code> in interface <code><a href="../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>getProjectImpl</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Returns:</dt>
<dd>project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNeedRecreateListeners(boolean)">
<h3>setNeedRecreateListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNeedRecreateListeners</span><wbr/><span class="parameters">(boolean needRecreateListeners)</span></div>
<div class="block">Set a need to recreated models listeners flag</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>needRecreateListeners</code> - a new value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNotNull(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isNotNull</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNotNull</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getModelElement()">
<h3>getModelElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.model.ModelElement</span> <span class="element-name">getModelElement</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sSetModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>sSetModelElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetModelElement</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>setModelElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setModelElement</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
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
