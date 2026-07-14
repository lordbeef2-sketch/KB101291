# JAVA OPENAPI: ActivationView (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml/symbols/shapes/ActivationView.html
- source_path: `com/nomagic/magicdraw/uml/symbols/shapes/ActivationView.html`
- source_sha256: `d04f35acc1b84dee03c88c3fbfaea6cc030b74b2633c5aace0f9c18a11682969`
- captured_utc: `2026-07-14T16:52:13.402896+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.shapes](package-summary.html)

## Class ActivationView

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](../PresentationElement.html)
[com.nomagic.magicdraw.uml.symbols.paths.PathConnector](../paths/PathConnector.html)
[com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement](ShapeElement.html)
com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
com.nomagic.magicdraw.uml.symbols.shapes.ActivationView

All Implemented Interfaces:
`[BaseElement](../../BaseElement.html)`, `[MDElement](../../MDElement.html)`, `[ModelElementProvider](../../ModelElementProvider.html)`, `com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape`, `com.nomagic.magicdraw.uml.symbols.SuspendShapeAutoResizeModeProvider`, `[NameOwner](../../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApipublic classActivationView
extends com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView

Creates activation object in sequence diagram.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`CONTAINER_SHAPE_INSETS, SHAPE_DISTANCE_FROM_EDGE`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[DASHED_STROKE](../PresentationElement.html#DASHED_STROKE), [DOTTED_STROKE](../PresentationElement.html#DOTTED_STROKE), [SOLID_STROKE](../PresentationElement.html#SOLID_STROKE)`
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
`addPresentationElement, addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosize, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, canAddChild, canMoveChildOutside, checkShowsProxy, childrenBoundsForReshape, clearShowsProxy, clone, constructLayoutHelper, correctChildrenVector, getChildrenBounds, getChildrenInsets, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementAt, getPresentationElementIndex, getPresentationElements, getProxyPresentationElementsStream, getRemovableChildren, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalAppendChildRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalSetChildren, internalUpdatePresentationElement, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildren, paintChildrenBackground, prefDimensionByManipulatedChildren, preferredDimension, recursiveAutosize, removePresentationElement, removePresentationElement, sAddPresentationElement, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.[PathConnector](../paths/PathConnector.html)
`[getConnectedPathElementCount](../paths/PathConnector.html#getConnectedPathElementCount()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements()), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean)), [getConnectedPathElements](../paths/PathConnector.html#getConnectedPathElements(boolean,boolean))`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](../PresentationElement.html)
`[addProperty](../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [collectSubManipulatedElements](../PresentationElement.html#collectSubManipulatedElements(java.util.List)), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent)), [editName](../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)), [getBoundsShape](../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getDiagramPresentationElement](../PresentationElement.html#getDiagramPresentationElement()), [getDiagramSurface](../PresentationElement.html#getDiagramSurface()), [getManipulatedParent](../PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](../PresentationElement.html#getManipulatedPresentationElements()), [getObjectParent](../PresentationElement.html#getObjectParent()), [getParent](../PresentationElement.html#getParent()), [getPreferredSize](../PresentationElement.html#getPreferredSize()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](../PresentationElement.html#getPresentationElementStroke(int)), [getProperty](../PresentationElement.html#getProperty(java.lang.String)), [getPropertyManager](../PresentationElement.html#getPropertyManager()), [getSelected](../PresentationElement.html#getSelected()), [getStroke](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](../PresentationElement.html#getStroke(int)), [getStroke](../PresentationElement.html#getStroke(int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int)), [getStroke](../PresentationElement.html#getStroke(int,int,int,int)), [getStroke](../PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [hasManipulatedPresentationElements](../PresentationElement.html#hasManipulatedPresentationElements()), [isSelected](../PresentationElement.html#isSelected()), [onFind](../PresentationElement.html#onFind()), [onFind](../PresentationElement.html#onFind(boolean)), [setAllSelected](../PresentationElement.html#setAllSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(boolean)), [setSelected](../PresentationElement.html#setSelected(java.util.List))`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getCommandForAppending, getID, getName, getProject, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, sGetID`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../BaseElement.html)
`[canAdd](../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement))`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape
`getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY`
Methods inherited from interface com.nomagic.magicdraw.utils.[NameOwner](../../../utils/NameOwner.html)
`[getName](../../../utils/NameOwner.html#getName())`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.shapes</a></div>
<h1 class="title" title="Class ActivationView">Class ActivationView</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance"><a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">com.nomagic.magicdraw.uml.symbols.paths.PathConnector</a>
<div class="inheritance"><a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ActivationView</div>
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
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ActivationView</span>
<span class="extends-implements">extends com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</span></div>
<div class="block">Creates activation object in sequence diagram.</div>
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
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#DASHED_STROKE">DASHED_STROKE</a>, <a href="../PresentationElement.html#DOTTED_STROKE">DOTTED_STROKE</a>, <a href="../PresentationElement.html#SOLID_STROKE">SOLID_STROKE</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView">Methods inherited from class com.nomagic.magicdraw.uml.symbols.shapes.ContainerShapeView</h3>
<code>addPresentationElement, addPresentationElement, addPresentationElementWithoutResize, adjustChildBoundsForMoving, autosize, autosizeByChildren, calculateAutosizeDimension, calculateAutosizeDimension, canAddChild, canMoveChildOutside, checkShowsProxy, childrenBoundsForReshape, clearShowsProxy, clone, constructLayoutHelper, correctChildrenVector, getChildrenBounds, getChildrenInsets, getChildrenOnBorderBounds, getContainerBounds, getDefaultChildrenInsets, getLayoutHelper, getLayoutHelperClone, getManipulatedElementAt, getManipulationPreferredDimension, getPresentationElementAt, getPresentationElementIndex, getPresentationElements, getProxyPresentationElementsStream, getRemovableChildren, hasManipulatedChildrenIncludingIndirect, hasManipulatedShapesNotOnEdge, hasManipulatedShapesOnEdge, hasManipulatedShapesOnEdge, internalAddIndirectManipulatedChildrenRect, internalAppendChildRect, internalGetChildAt, internalGetIndirectManipulatedChildrenRect, internalGetManipulatedChildrenRect, internalGetSelfManipulationPreferredSize, internalSetChildren, internalUpdatePresentationElement, isCanChildrenChangeEdge, isCanMoveChildren, isChildMovable, layoutChildren, moveChild, moveChildren, needAdjustToPreferred, paintChildren, paintChildrenBackground, prefDimensionByManipulatedChildren, preferredDimension, recursiveAutosize, removePresentationElement, removePresentationElement, sAddPresentationElement, setBounds, setCanMoveChildren, setDummyResizeMode, setFillColor, setFillColorForChildren, setLayoutHelper, setPresentationElements, showPathElements, simpleSetBounds, simpleSetBounds, sRemovePresentationElement, sSetPresentationElements</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.paths.PathConnector">Methods inherited from class com.nomagic.magicdraw.uml.symbols.paths.<a href="../paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a></h3>
<code><a href="../paths/PathConnector.html#getConnectedPathElementCount()">getConnectedPathElementCount</a>, <a href="../paths/PathConnector.html#getConnectedPathElements()">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean)">getConnectedPathElements</a>, <a href="../paths/PathConnector.html#getConnectedPathElements(boolean,boolean)">getConnectedPathElements</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="../PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="../PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="../PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a>, <a href="../PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="../PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="../PresentationElement.html#getDiagramSurface()">getDiagramSurface</a>, <a href="../PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="../PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="../PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="../PresentationElement.html#getParent()">getParent</a>, <a href="../PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="../PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="../PresentationElement.html#getProperty(java.lang.String)">getProperty</a>, <a href="../PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="../PresentationElement.html#getSelected()">getSelected</a>, <a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="../PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="../PresentationElement.html#isSelected()">isSelected</a>, <a href="../PresentationElement.html#onFind()">onFind</a>, <a href="../PresentationElement.html#onFind(boolean)">onFind</a>, <a href="../PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="../PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="../PresentationElement.html#setSelected(java.util.List)">setSelected</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, addPropertyChangeListener, canAdd, canAddChild, canBeDeleted, canDeleteChild, compareTo, createSortKeys, getClassType, getCommandForAppending, getID, getName, getProject, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, removePropertyChangeListener, setID, setProjectProvider, sGetID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape">Methods inherited from interface com.nomagic.magicdraw.uml.symbols.manipulators.centerlines.CenterlineableShape</h3>
<code>getAbstractDiagramPresentationElement, getCenterlinePoint, getCenterlinePointX, getCenterlinePointY</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.utils.NameOwner">Methods inherited from interface com.nomagic.magicdraw.utils.<a href="../../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></h3>
<code><a href="../../../utils/NameOwner.html#getName()">getName</a></code></div>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
