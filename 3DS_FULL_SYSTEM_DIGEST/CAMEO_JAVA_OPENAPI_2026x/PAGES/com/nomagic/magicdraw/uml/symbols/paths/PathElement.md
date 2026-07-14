# JAVA OPENAPI: PathElement (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml/symbols/paths/PathElement.html
- source_path: `com/nomagic/magicdraw/uml/symbols/paths/PathElement.html`
- source_sha256: `d09790c704b6f353699d4a8cb9b291cbba8a753b7391e257b304463dd885dd84`
- captured_utc: `2026-07-14T16:58:30.938213+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.paths](package-summary.html)

## Class PathElement

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.core.impl.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](PathConnector.html)
com.nomagic.magicdraw.uml.symbols.paths.PathElement

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.diagram.symbols.LineJumpDrawer`, `com.dassault_systemes.modeler.foundation.diagram.symbols.shapes.SuspendShapeAutoResizeModeProvider`, `com.dassault_systemes.modeler.foundation.project.ModelElementProjectProvider`, `[BaseElement](../../BaseElement.html)`, `[MDElement](../../core/MDElement.html)`, `[ModelElementProvider](../../core/ModelElementProvider.html)`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView`, `[ContainmentLinkView](ContainmentLinkView.html)`, `[LinkAttributeView](LinkAttributeView.html)`, `[NoteAnchorView](NoteAnchorView.html)`

@OpenApipublic abstract classPathElement
extends [PathConnector](PathConnector.html)
implements com.dassault_systemes.modeler.foundation.diagram.symbols.LineJumpDrawer, com.dassault_systemes.modeler.foundation.diagram.symbols.shapes.SuspendShapeAutoResizeModeProvider

Base class for all path kinds of symbols.
 Path is a symbol that connects two other symbols as a graphical path.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[BEZIER](#BEZIER)`
Bezier path line style.
`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[LINE_STYLE](#LINE_STYLE)`
All possible path line styles.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OBLIQUE](#OBLIQUE)`
Oblique path line style.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[RECTILINEAR](#RECTILINEAR)`
Path line style with rectilinear (90 degrees) breakpoint corners.
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.symbols.BasePresentationElementVisitor))([BasePresentationElementVisitor](../BasePresentationElementVisitor.html) visitor)`

`final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)>`
`[getAllBreakPoints](#getAllBreakPoints())()`
Returns a break points list with added supplier and client end point in the list as well.
`final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)>`
`[getBreakPoints](#getBreakPoints())()`
Returns break points of the path.
`[PresentationElement](../PresentationElement.html)`
`[getClient](#getClient())()`
Returns client of the path.
`final [Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)`
`[getClientPoint](#getClientPoint())()`
Returns point where path connects client end's element.
`[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)`
`[getPointOnPath](#getPointOnPath(java.awt.Point,java.awt.Point,java.util.List,double))([Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html) supplierPoint,
 [Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html) clientPoint,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)> breakpoints,
 double coefficient)`

`[PresentationElement](../PresentationElement.html)`
`[getSupplier](#getSupplier())()`
Returns supplier of the path.
`final [Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)`
`[getSupplierPoint](#getSupplierPoint())()`
Returns point where path connects supplier end's element.
`final boolean`
`[isConnectable](#isConnectable(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) supplier,
 [PresentationElement](../PresentationElement.html) client)`
Checks if this path can connect given two elements.
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](PathConnector.html)
`[getConnectedPathElementCount](PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](PathConnector.html#getConnectedPathElements(boolean,boolean))`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getElement](../PresentationElement.html#getElement()), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getParent](../PresentationElement.html#getParent()), [getPreferredDimension](../PresentationElement.html#getPreferredDimension()), [getPresentationElements](../PresentationElement.html#getPresentationElements()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [isSelected](../PresentationElement.html#isSelected()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List)), [useParentStyle](../PresentationElement.html#useParentStyle())`
Methods inherited from class com.nomagic.magicdraw.uml.core.impl.MDElementImpl
`addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, sGetID, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../BaseElement.html)
`[canAdd](../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../BaseElement.html#isSelfChangeable())`
Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.symbols.LineJumpDrawer
`getLineWidth`
Methods inherited from interface com.nomagic.magicdraw.utils.[NameOwner](../../../utils/NameOwner.html)
`[getName](../../../utils/NameOwner.html#getName())`

============ FIELD DETAIL =========== 
Field Details
RECTILINEAR
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) RECTILINEAR
Path line style with rectilinear (90 degrees) breakpoint corners.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.paths.PathElement.RECTILINEAR)
OBLIQUE
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OBLIQUE
Oblique path line style.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.paths.PathElement.OBLIQUE)
BEZIER
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) BEZIER
Bezier path line style.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.paths.PathElement.BEZIER)
LINE_STYLE
@OpenApipublic static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> LINE_STYLE
All possible path line styles.
 ============ METHOD DETAIL ========== 
Method Details
getBreakPoints
@OpenApipublic final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)> getBreakPoints()
Returns break points of the path.
 The order of break points is from supplier to the client path's end.
 Use PresentationElementsManager to change the break points for the path.
Returns:
break points list.Points in the list are not cloned, so do not modify them directly.
 The List is unmodifiable.
getAllBreakPoints
@OpenApipublic final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)> getAllBreakPoints()
Returns a break points list with added supplier and client end point in the list as well.
 Use PresentationElementsManager to change the break points for the path.
Returns:
supplier point + break points + client point. Points in the list are not cloned,
 so do not modify them directly. The List is modifiable.
getSupplierPoint
@OpenApipublic final [Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html) getSupplierPoint()
Returns point where path connects supplier end's element.
Returns:
supplier connection point. This method returns not cloned point, so do not modify it directly.
getClientPoint
@OpenApipublic final [Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html) getClientPoint()
Returns point where path connects client end's element.
Returns:
client point. This method returns not cloned point, so do not modify it directly.
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
getPointOnPath
@OpenApipublic [Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html) getPointOnPath([Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html) supplierPoint,
 [Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html) clientPoint,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)> breakpoints,
 double coefficient)
Parameters:
`supplierPoint` - supplier end point
`clientPoint` - client end point
`breakpoints` - list of breakpoints between supplier and client in that order
`coefficient` - ratio between 0 and 1 describing position relative to the path length.
 Provide 0.5 for middle point.
Returns:
point on path
accept
@OpenApipublic void accept([BasePresentationElementVisitor](../BasePresentationElementVisitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Overrides:
`[accept](PathConnector.html#accept(com.nomagic.magicdraw.uml.symbols.BasePresentationElementVisitor))` in class `[PathConnector](PathConnector.html)`
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.paths</a></div>
<h1 class="title" title="Class PathElement">Class PathElement</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.core.impl.MDElementImpl
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
<dd><code>com.dassault_systemes.modeler.foundation.diagram.symbols.LineJumpDrawer</code>, <code>com.dassault_systemes.modeler.foundation.diagram.symbols.shapes.SuspendShapeAutoResizeModeProvider</code>, <code>com.dassault_systemes.modeler.foundation.project.ModelElementProjectProvider</code>, <code><a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../../core/MDElement.html" title="interface in com.nomagic.magicdraw.uml.core">MDElement</a></code>, <code><a href="../../core/ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml.core">ModelElementProvider</a></code>, <code><a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code>com.nomagic.magicdraw.uml.symbols.paths.ContainerLinkView</code>, <code><a href="ContainmentLinkView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">ContainmentLinkView</a></code>, <code><a href="LinkAttributeView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">LinkAttributeView</a></code>, <code><a href="NoteAnchorView.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">NoteAnchorView</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">PathElement</span>
<span class="extends-implements">extends <a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a>
implements com.dassault_systemes.modeler.foundation.diagram.symbols.LineJumpDrawer, com.dassault_systemes.modeler.foundation.diagram.symbols.shapes.SuspendShapeAutoResizeModeProvider</span></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BEZIER">BEZIER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Bezier path line style.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LINE_STYLE">LINE_STYLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">All possible path line styles.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OBLIQUE">OBLIQUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Oblique path line style.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RECTILINEAR">RECTILINEAR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Path line style with rectilinear (90 degrees) breakpoint corners.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#DASHED_STROKE">DASHED_STROKE</a>, <a href="../PresentationElement.html#DOTTED_STROKE">DOTTED_STROKE</a>, <a href="../PresentationElement.html#SOLID_STROKE">SOLID_STROKE</a></code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.symbols.BasePresentationElementVisitor)">accept</a><wbr/>(<a href="../BasePresentationElementVisitor.html" title="interface in com.nomagic.magicdraw.uml.symbols">BasePresentationElementVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllBreakPoints()">getAllBreakPoints</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a break points list with added supplier and client end point in the list as well.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBreakPoints()">getBreakPoints</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns break points of the path.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClient()">getClient</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns client of the path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClientPoint()">getClientPoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns point where path connects client end's element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPointOnPath(java.awt.Point,java.awt.Point,java.util.List,double)">getPointOnPath</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplierPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> clientPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; breakpoints,
 double coefficient)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplier()">getSupplier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns supplier of the path.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierPoint()">getSupplierPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns point where path connects supplier end's element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isConnectable(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">isConnectable</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if this path can connect given two elements.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getElement()">getElement</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="../PresentationElement.html#getPresentationElements()">getPresentationElements</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a>, <a href="../PresentationElement.html#useParentStyle()">useParentStyle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.core.impl.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.core.impl.MDElementImpl</h3>
<code>addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getID, getName, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, sGetID, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../BaseElement.html#isSelfChangeable()">isSelfChangeable</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.diagram.symbols.LineJumpDrawer">Methods inherited from interface com.dassault_systemes.modeler.foundation.diagram.symbols.LineJumpDrawer</h3>
<code>getLineWidth</code></div>
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
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RECTILINEAR</span></div>
<div class="block">Path line style with rectilinear (90 degrees) breakpoint corners.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
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
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OBLIQUE</span></div>
<div class="block">Oblique path line style.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
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
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BEZIER</span></div>
<div class="block">Bezier path line style.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
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
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">LINE_STYLE</span></div>
<div class="block">All possible path line styles.</div>
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
<section class="detail" id="getBreakPoints()">
<h3>getBreakPoints</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</span> <span class="element-name">getBreakPoints</span>()</div>
<div class="block">Returns break points of the path.
 The order of break points is from supplier to the client path's end.
 Use PresentationElementsManager to change the break points for the path.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>break points list.Points in the list are not cloned, so do not modify them directly.
 The List is unmodifiable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllBreakPoints()">
<h3>getAllBreakPoints</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</span> <span class="element-name">getAllBreakPoints</span>()</div>
<div class="block">Returns a break points list with added supplier and client end point in the list as well.
 Use PresentationElementsManager to change the break points for the path.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>supplier point + break points + client point. Points in the list are not cloned,
 so do not modify them directly. The List is modifiable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplierPoint()">
<h3>getSupplierPoint</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getSupplierPoint</span>()</div>
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
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getClientPoint</span>()</div>
<div class="block">Returns point where path connects client end's element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>client point. This method returns not cloned point, so do not modify it directly.</dd>
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
<section class="detail" id="getPointOnPath(java.awt.Point,java.awt.Point,java.util.List,double)">
<h3>getPointOnPath</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getPointOnPath</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplierPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> clientPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; breakpoints,
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
<section class="detail" id="accept(com.nomagic.magicdraw.uml.symbols.BasePresentationElementVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../BasePresentationElementVisitor.html" title="interface in com.nomagic.magicdraw.uml.symbols">BasePresentationElementVisitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PathConnector.html#accept(com.nomagic.magicdraw.uml.symbols.BasePresentationElementVisitor)">accept</a></code> in class <code><a href="PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
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
