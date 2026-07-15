# JAVA OPENAPI: PresentationElement (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/symbols/PresentationElement.html
- source_path: `com/nomagic/magicdraw/uml/symbols/PresentationElement.html`
- source_sha256: `c672e2a4b622feb4a1ab1685ceb7f04530be66ecb4b4595df3ee4fd7714e09bc`
- captured_utc: `2026-07-14T16:46:06.197883+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class PresentationElement

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.core.impl.MDElementImpl
com.nomagic.magicdraw.uml.symbols.PresentationElement

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.ModelElementProjectProvider`, `[BaseElement](../BaseElement.html)`, `[MDElement](../core/MDElement.html)`, `[ModelElementProvider](../core/ModelElementProvider.html)`, `[NameOwner](../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`[AbstractDiagramPresentationElement](AbstractDiagramPresentationElement.html)`, `[PathConnector](paths/PathConnector.html)`

@OpenApipublic abstract classPresentationElement
extends com.nomagic.magicdraw.uml.core.impl.MDElementImpl
implements [PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html), [ModelElementProvider](../core/ModelElementProvider.html), [NameOwner](../../utils/NameOwner.html)

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
`[DOTTED_STROKE](#DOTTED_STROKE)`
Dotted path stroke.
`static final int`
`[SOLID_STROKE](#SOLID_STROKE)`
Solid path stroke.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`final void`
`[collectSubManipulatedElements](#collectSubManipulatedElements(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> col)`
Collects all visible and manipulated elements in this hierarchy.
`final void`
`[editName](#editName(java.awt.event.KeyEvent))([KeyEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/KeyEvent.html) evt)`
Starts online diagram editing for a symbol
`void`
`[editName](#editName(java.awt.event.KeyEvent,java.util.Map))([KeyEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/KeyEvent.html) evt,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)> textEditorOptions)`
Starts online diagram editing for a symbol
`[Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBounds](#getBounds())()`
Method returns bounds of this element.
`final [Shape](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Shape.html)`
`[getBoundsShape](#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape))([ConverterToShape](ConverterToShape.html) converterToShape)`
Provides a bounding shape of the symbol
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement())()`
Returns model element of this presentation element.
`final [PresentationElement](PresentationElement.html)`
`[getManipulatedParent](#getManipulatedParent())()`

`final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getManipulatedPresentationElements](#getManipulatedPresentationElements())()`
Returns a list of children of this element those have manipulator.
`[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)`
`[getMiddlePoint](#getMiddlePoint())()`
Returns middle point of this element.
`[BaseElement](../BaseElement.html)`
`[getObjectParent](#getObjectParent())()`
Returns the presentation element parent.
`final [PresentationElement](PresentationElement.html)`
`[getParent](#getParent())()`
Returns parent of this element.
`[UnmodifiableDimension](../../../ui/UnmodifiableDimension.html)`
`[getPreferredDimension](#getPreferredDimension())()`
Returns preferable dimension of the element.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getPresentationElements](#getPresentationElements())()`
Returns all children of this element
`final [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getPresentationElementStroke](#getPresentationElementStroke())()`
Return a stroke used to paint symbol's main part
`final [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getPresentationElementStroke](#getPresentationElementStroke(int))(int width)`
Return a stroke used to paint symbol's main part
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)>`
`[getSelected](#getSelected())()`
Returns a list of selected elements in the diagram.
`static [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(float,int,int,float,float%5B%5D,float))(float width,
 int cap,
 int join,
 float miterLimit,
 float[] dash,
 float dash_phase)`
Get cached stroke.
`static [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(int))(int lineStyle)`
Get cached stroke of given style and default width.
`static [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(int,int))(int lineStyle,
 int width)`
Get cached stroke of given style and width.
`static [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(int,int,int))(int lineStyle,
 int width,
 int join)`
Get cached stroke of given style, width and join.
`static [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(int,int,int,int))(int lineStyle,
 int width,
 int join,
 int cap)`
Get cached stroke of given style, width and join.
`static [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke(java.awt.BasicStroke,int))([BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html) stroke,
 int width)`
Get cached stroke of given width.
`final boolean`
`[hasManipulatedPresentationElements](#hasManipulatedPresentationElements())()`

`boolean`
`[isSelected](#isSelected())()`
Returns true, if this element is selected in the diagram.
`final void`
`[onFind](#onFind())()`
Scrolls diagram canvas to this symbol and selects this symbol
`final void`
`[onFind](#onFind(boolean))(boolean center)`
Scrolls diagram canvas to this symbol and selects this symbol
`void`
`[setAllSelected](#setAllSelected(boolean))(boolean select)`
Selects(or deselects) all presentation elements in the diagram.
`void`
`[setSelected](#setSelected(boolean))(boolean select)`
Selects or deselects this presentation element in the diagram.
`void`
`[setSelected](#setSelected(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> elements)`
Selects given elements in the diagram.
`boolean`
`[useParentStyle](#useParentStyle())()`
Does this element uses parent style or has it's own?
Methods inherited from class com.nomagic.magicdraw.uml.core.impl.MDElementImpl
`addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getResourceID, getSortKeys, hasListeners, isEditable, mdElementComputeIfAbsentProperty, mdElementGetProperty, mdElementRemoveProperty, mdElementSetOrRemoveProperty, mdElementSetProperty, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, sGetID, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../BaseElement.html)
`[canAdd](../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.nomagic.magicdraw.utils.[NameOwner](../../utils/NameOwner.html)
`[getName](../../utils/NameOwner.html#getName())`

============ FIELD DETAIL =========== 
Field Details
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
 ============ METHOD DETAIL ========== 
Method Details
getElement
@OpenApi
@CheckForNullpublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElement()
Returns model element of this presentation element. Some presentation elements (for example
 TextBoxes) do not have model elements.
Specified by:
`[getElement](../core/ModelElementProvider.html#getElement())` in interface `[ModelElementProvider](../core/ModelElementProvider.html)`
Returns:
model element of this presentation element.
getParent
@OpenApipublic final [PresentationElement](PresentationElement.html) getParent()
Returns parent of this element.
Returns:
parent of this element.
getPreferredDimension
@OpenApipublic [UnmodifiableDimension](../../../ui/UnmodifiableDimension.html) getPreferredDimension()
Returns preferable dimension of the element.
Returns:
preferred dimension
getMiddlePoint
@CheckForNull
@OpenApipublic [Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html) getMiddlePoint()
Returns middle point of this element. Middle point for shapes usually will be center point of
 bounds, middle point for paths will be center of path curve.
Returns:
point that is considered as middle for this element.
getBounds
@OpenApipublic [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) getBounds()
 throws [NoRectangleDefinedException](NoRectangleDefinedException.html)
Method returns bounds of this element.
 Use PresentationElementsManager to change a bounds of the element.
Returns:
bounds of the element.
Throws:
`[NoRectangleDefinedException](NoRectangleDefinedException.html)` - when bounds can not be calculated (some presentation
 elements are abstract and can not have bounds).
See Also:
invalid reference
`PresentationElementsManager.reshapeShapeElement`
getPresentationElements
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getPresentationElements()
Returns all children of this element
Returns:
all children of this element. The collection is unmodifiable.
setAllSelected
@OpenApipublic void setAllSelected(boolean select)
Selects(or deselects) all presentation elements in the diagram.
Parameters:
`select` - select or deselect all elements.
setSelected
@OpenApipublic void setSelected([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> elements)
Selects given elements in the diagram.
Parameters:
`elements` - elements to select.
setSelected
@OpenApipublic void setSelected(boolean select)
Selects or deselects this presentation element in the diagram.
Parameters:
`select` - select or deselect this presentation element.
getSelected
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getSelected()
Returns a list of selected elements in the diagram.
Returns:
a list of selected elements. List is unmodifiable.
isSelected
@OpenApipublic boolean isSelected()
Returns true, if this element is selected in the diagram.
Returns:
true, if this element is selected in the diagram.
onFind
@OpenApipublic final void onFind()
Scrolls diagram canvas to this symbol and selects this symbol
onFind
@OpenApipublic final void onFind(boolean center)
Scrolls diagram canvas to this symbol and selects this symbol
Parameters:
`center` - if true, centers current view in the center of the window.
collectSubManipulatedElements
@OpenApipublic final void collectSubManipulatedElements([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> col)
Collects all visible and manipulated elements in this hierarchy.
getManipulatedPresentationElements
@OpenApipublic final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PresentationElement](PresentationElement.html)> getManipulatedPresentationElements()
Returns a list of children of this element those have manipulator.
Returns:
a list of manipulated elements. Collection is unmodifiable.
hasManipulatedPresentationElements
@OpenApipublic final boolean hasManipulatedPresentationElements()
Returns:
true if at least one child is manipulated and visible
useParentStyle
@OpenApipublic boolean useParentStyle()
Does this element uses parent style or has it's own?
Returns:
true, if element does not have style and uses parent's style.
editName
@OpenApipublic final void editName(@CheckForNull
 [KeyEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/KeyEvent.html) evt)
Starts online diagram editing for a symbol
Parameters:
`evt` - first key event or null
editName
@OpenApipublic void editName(@CheckForNull
 [KeyEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/KeyEvent.html) evt,
 @CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)> textEditorOptions)
Starts online diagram editing for a symbol
Parameters:
`evt` - first key event or null
`textEditorOptions` - boolean options for text editor. Passed when creating text editor with
 `TextEditorFactory`
getManipulatedParent
@CheckForNull
@OpenApipublic final [PresentationElement](PresentationElement.html) getManipulatedParent()
Returns:
first parent with manipulator or null if such does not exist.
getObjectParent
@OpenApipublic [BaseElement](../BaseElement.html) getObjectParent()
Returns the presentation element parent. Implementation of super method.
Specified by:
`[getObjectParent](../BaseElement.html#getObjectParent())` in interface `[BaseElement](../BaseElement.html)`
Overrides:
`getObjectParent` in class `com.nomagic.magicdraw.uml.core.impl.MDElementImpl`
Returns:
the parent of the element.
See Also:
[`getParent()`](#getParent())
getBoundsShape
@OpenApi
@CheckForNullpublic final [Shape](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Shape.html) getBoundsShape([ConverterToShape](ConverterToShape.html) converterToShape)
Provides a bounding shape of the symbol
Parameters:
`converterToShape` - transform bounding shape according this converter
Returns:
bounding shape of the symbol
getPresentationElementStroke
@OpenApipublic final [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html) getPresentationElementStroke()
Return a stroke used to paint symbol's main part
Returns:
a stroke used to paint symbol's main part
getPresentationElementStroke
@OpenApipublic final [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html) getPresentationElementStroke(int width)
Return a stroke used to paint symbol's main part
Parameters:
`width` - a custom stroke width. Other stroke parameters will be specific to symbol
Returns:
a stroke used to paint symbol's main part
getStroke
@OpenApipublic static [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke([BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html) stroke,
 int width)
Get cached stroke of given width.
Parameters:
`stroke` - base stroke.
`width` - of the stroke.
Returns:
stroke
getStroke
@OpenApipublic static [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke(int lineStyle)
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
@OpenApipublic static [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke(int lineStyle,
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
@OpenApipublic static [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke(int lineStyle,
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
[`BasicStroke.JOIN_BEVEL`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_BEVEL)
[`BasicStroke.JOIN_MITER`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_MITER)
[`BasicStroke.JOIN_ROUND`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_ROUND)
getStroke
@OpenApipublic static [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke(int lineStyle,
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
[`BasicStroke.JOIN_BEVEL`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_BEVEL)
[`BasicStroke.JOIN_MITER`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_MITER)
[`BasicStroke.JOIN_ROUND`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_ROUND)
getStroke
@OpenApipublic static [BasicStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke(float width,
 int cap,
 int join,
 float miterLimit,
 @CheckForNull
 float[] dash,
 float dash_phase)
Get cached stroke.
See Also:
[`BasicStroke(float, int, int, float, float[], float)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#%3Cinit%3E(float,int,int,float,float%5B%5D,float))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class PresentationElement">Class PresentationElement</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.core.impl.MDElementImpl
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.PresentationElement</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.ModelElementProjectProvider</code>, <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../core/MDElement.html" title="interface in com.nomagic.magicdraw.uml.core">MDElement</a></code>, <code><a href="../core/ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml.core">ModelElementProvider</a></code>, <code><a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code>, <code><a href="paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">PresentationElement</span>
<span class="extends-implements">extends com.nomagic.magicdraw.uml.core.impl.MDElementImpl
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a>, <a href="../core/ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml.core">ModelElementProvider</a>, <a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></span></div>
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
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DOTTED_STROKE">DOTTED_STROKE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Dotted path stroke.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOLID_STROKE">SOLID_STROKE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Solid path stroke.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; col)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all visible and manipulated elements in this hierarchy.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editName(java.awt.event.KeyEvent)">editName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/KeyEvent.html" title="class or interface in java.awt.event">KeyEvent</a> evt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts online diagram editing for a symbol</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/KeyEvent.html" title="class or interface in java.awt.event">KeyEvent</a> evt,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; textEditorOptions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts online diagram editing for a symbol</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBounds()">getBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method returns bounds of this element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a><wbr/>(<a href="ConverterToShape.html" title="class in com.nomagic.magicdraw.uml.symbols">ConverterToShape</a> converterToShape)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Provides a bounding shape of the symbol</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model element of this presentation element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedParent()">getManipulatedParent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a list of children of this element those have manipulator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMiddlePoint()">getMiddlePoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns middle point of this element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectParent()">getObjectParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the presentation element parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParent()">getParent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns parent of this element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../ui/UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreferredDimension()">getPreferredDimension</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns preferable dimension of the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElements()">getPresentationElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all children of this element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementStroke()">getPresentationElementStroke</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a stroke used to paint symbol's main part</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPresentationElementStroke(int)">getPresentationElementStroke</a><wbr/>(int width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a stroke used to paint symbol's main part</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelected()">getSelected</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a list of selected elements in the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a><wbr/>(float width,
 int cap,
 int join,
 float miterLimit,
 float[] dash,
 float dash_phase)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get cached stroke.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(int)">getStroke</a><wbr/>(int lineStyle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get cached stroke of given style and default width.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(int,int)">getStroke</a><wbr/>(int lineStyle,
 int width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get cached stroke of given style and width.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(int,int,int)">getStroke</a><wbr/>(int lineStyle,
 int width,
 int join)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get cached stroke of given style, width and join.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(int,int,int,int)">getStroke</a><wbr/>(int lineStyle,
 int width,
 int join,
 int cap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get cached stroke of given style, width and join.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke(java.awt.BasicStroke,int)">getStroke</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a> stroke,
 int width)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get cached stroke of given width.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSelected()">isSelected</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if this element is selected in the diagram.</div>
</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAllSelected(boolean)">setAllSelected</a><wbr/>(boolean select)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Selects(or deselects) all presentation elements in the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelected(boolean)">setSelected</a><wbr/>(boolean select)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Selects or deselects this presentation element in the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelected(java.util.List)">setSelected</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Selects given elements in the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#useParentStyle()">useParentStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Does this element uses parent style or has it's own?</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.core.impl.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.core.impl.MDElementImpl</h3>
<code>addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getResourceID, getSortKeys, hasListeners, isEditable, mdElementComputeIfAbsentProperty, mdElementGetProperty, mdElementRemoveProperty, mdElementSetOrRemoveProperty, mdElementSetProperty, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, sGetID, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../BaseElement.html#isSelfChangeable()">isSelfChangeable</a></code></div>
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
<section class="detail" id="SOLID_STROKE">
<h3>SOLID_STROKE</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SOLID_STROKE</span></div>
<div class="block">Solid path stroke.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
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
<ul class="tag-list">
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
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.PresentationElement.DOTTED_STROKE">Constant Field Values</a></li>
</ul>
</dd>
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
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">Returns model element of this presentation element. Some presentation elements (for example
 TextBoxes) do not have model elements.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../core/ModelElementProvider.html#getElement()">getElement</a></code> in interface <code><a href="../core/ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml.core">ModelElementProvider</a></code></dd>
<dt>Returns:</dt>
<dd>model element of this presentation element.</dd>
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
<section class="detail" id="getMiddlePoint()">
<h3>getMiddlePoint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getMiddlePoint</span>()</div>
<div class="block">Returns middle point of this element. Middle point for shapes usually will be center point of
 bounds, middle point for paths will be center of path curve.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>point that is considered as middle for this element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBounds()">
<h3>getBounds</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBounds</span>()
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
<ul class="tag-list-long">
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>PresentationElementsManager.reshapeShapeElement</code></pre>
</details>
</li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElements()">
<h3>getPresentationElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getPresentationElements</span>()</div>
<div class="block">Returns all children of this element</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all children of this element. The collection is unmodifiable.</dd>
</dl>
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
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelected</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; elements)</span></div>
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
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getSelected</span>()</div>
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
<section class="detail" id="collectSubManipulatedElements(java.util.List)">
<h3>collectSubManipulatedElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">collectSubManipulatedElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; col)</span></div>
<div class="block">Collects all visible and manipulated elements in this hierarchy.</div>
</section>
</li>
<li>
<section class="detail" id="getManipulatedPresentationElements()">
<h3>getManipulatedPresentationElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getManipulatedPresentationElements</span>()</div>
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
<section class="detail" id="editName(java.awt.event.KeyEvent)">
<h3>editName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">editName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/KeyEvent.html" title="class or interface in java.awt.event">KeyEvent</a> evt)</span></div>
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
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/event/KeyEvent.html" title="class or interface in java.awt.event">KeyEvent</a> evt,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; textEditorOptions)</span></div>
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
<section class="detail" id="getObjectParent()">
<h3>getObjectParent</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getObjectParent</span>()</div>
<div class="block">Returns the presentation element parent. Implementation of super method.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseElement.html#getObjectParent()">getObjectParent</a></code> in interface <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>getObjectParent</code> in class <code>com.nomagic.magicdraw.uml.core.impl.MDElementImpl</code></dd>
<dt>Returns:</dt>
<dd>the parent of the element.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getParent()"><code>getParent()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">
<h3>getBoundsShape</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></span> <span class="element-name">getBoundsShape</span><wbr/><span class="parameters">(<a href="ConverterToShape.html" title="class in com.nomagic.magicdraw.uml.symbols">ConverterToShape</a> converterToShape)</span></div>
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
<section class="detail" id="getPresentationElementStroke()">
<h3>getPresentationElementStroke</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getPresentationElementStroke</span>()</div>
<div class="block">Return a stroke used to paint symbol's main part</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a stroke used to paint symbol's main part</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPresentationElementStroke(int)">
<h3>getPresentationElementStroke</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getPresentationElementStroke</span><wbr/><span class="parameters">(int width)</span></div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a> stroke,
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
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(int lineStyle)</span></div>
<div class="block">Get cached stroke of given style and default width.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lineStyle</code> - style of line.</dd>
<dt>Returns:</dt>
<dd>stroke</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
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
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(int lineStyle,
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
<ul class="tag-list">
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
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(int lineStyle,
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
<ul class="tag-list">
<li><a href="#SOLID_STROKE"><code>SOLID_STROKE</code></a></li>
<li><a href="#DASHED_STROKE"><code>DASHED_STROKE</code></a></li>
<li><a href="#DOTTED_STROKE"><code>DOTTED_STROKE</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_BEVEL" title="class or interface in java.awt"><code>BasicStroke.JOIN_BEVEL</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_MITER" title="class or interface in java.awt"><code>BasicStroke.JOIN_MITER</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_ROUND" title="class or interface in java.awt"><code>BasicStroke.JOIN_ROUND</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStroke(int,int,int,int)">
<h3>getStroke</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(int lineStyle,
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
<ul class="tag-list">
<li><a href="#SOLID_STROKE"><code>SOLID_STROKE</code></a></li>
<li><a href="#DASHED_STROKE"><code>DASHED_STROKE</code></a></li>
<li><a href="#DOTTED_STROKE"><code>DOTTED_STROKE</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_BEVEL" title="class or interface in java.awt"><code>BasicStroke.JOIN_BEVEL</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_MITER" title="class or interface in java.awt"><code>BasicStroke.JOIN_MITER</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#JOIN_ROUND" title="class or interface in java.awt"><code>BasicStroke.JOIN_ROUND</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStroke(float,int,int,float,float[],float)">
<h3>getStroke</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span><wbr/><span class="parameters">(float width,
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
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/BasicStroke.html#%3Cinit%3E(float,int,int,float,float%5B%5D,float)" title="class or interface in java.awt"><code>BasicStroke(float, int, int, float, float[], float)</code></a></li>
</ul>
</dd>
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
