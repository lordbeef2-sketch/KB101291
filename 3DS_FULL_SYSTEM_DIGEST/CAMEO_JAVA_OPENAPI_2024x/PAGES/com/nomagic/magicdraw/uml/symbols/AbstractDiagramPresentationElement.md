# JAVA OPENAPI: AbstractDiagramPresentationElement (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html
- source_path: `com/nomagic/magicdraw/uml/symbols/AbstractDiagramPresentationElement.html`
- source_sha256: `86f96dec698ae155e5d96e158e3d093fc52df29c5518095d9cf4a4d635a7c1d2`
- captured_utc: `2026-07-14T16:52:10.930865+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class AbstractDiagramPresentationElement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.MDElementImpl
[com.nomagic.magicdraw.uml.symbols.PresentationElement](PresentationElement.html)
com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement

All Implemented Interfaces:
`com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer`, `[BaseElement](../BaseElement.html)`, `[MDElement](../MDElement.html)`, `[ModelElementProvider](../ModelElementProvider.html)`, `[NameOwner](../../utils/NameOwner.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`[DiagramPresentationElement](DiagramPresentationElement.html)`

@OpenApipublic abstract classAbstractDiagramPresentationElement
extends [PresentationElement](PresentationElement.html)
implements com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](PresentationElement.html)
`[DASHED_STROKE](PresentationElement.html#DASHED_STROKE), [DOTTED_STROKE](PresentationElement.html#DOTTED_STROKE), [SOLID_STROKE](PresentationElement.html#SOLID_STROKE)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.uml.Visitor))([Visitor](../Visitor.html) visitor)`
Method accepts visitor, and calls method visit<class name>(this) of visitor .
`boolean`
`[addContentPropertyChangeListener](#addContentPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Registers the listener for changes in all symbols contained in the diagram.
`final void`
`[close](#close())()`
Closes diagram window.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[collectPresentationElementsRecursively](#collectPresentationElementsRecursively())()`
Collects all elements in this diagram recursively.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[collectShowingManipulatedElementsRecursively](#collectShowingManipulatedElementsRecursively())()`
Collects all visible manipulated elements in this diagram recursively.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)>`
`[collectShowingPresentationElementsRecursively](#collectShowingPresentationElementsRecursively())()`
Collects all visible elements in this diagram recursively.
`void`
`[ensureLoaded](#ensureLoaded())()`
Ensures that diagram is loaded.
`final [PresentationElement](PresentationElement.html)`
`[findPresentationElement](#findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class))(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)`
Finds presentation element for given model element of given symbol type in this diagram.
`final [PresentationElement](PresentationElement.html)`
`[findPresentationElement](#findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)`
Finds presentation element for given model element of given symbol type in this diagram.
`final [PresentationElement](PresentationElement.html)`
`[findPresentationElementForPathConnecting](#findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class))([BaseElement](../BaseElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)`
Finds presentation element to connect some PathElement for given model element of given type in this diagram.
`final [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[PresentationElement](PresentationElement.html)>`
`[findPresentationElementsForPathConnecting](#findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)`
Finds presentations element to connect some PathElement for given model element of given type in this diagram.
`boolean`
`[isLoaded](#isLoaded())()`
Check if diagram is loaded.
`boolean`
`[isSymbolDiagram](#isSymbolDiagram())()`
Checks if diagram displays symbols as its contents.
`boolean`
`[layout](#layout(boolean))(boolean useCommands)`
Layout the diagram using default layouter.
`boolean`
`[layout](#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter))(boolean useCommands,
 [DiagramLayouter](layout/DiagramLayouter.html) layouter)`
Layouts the diagram with the specified layouter.
`boolean`
`[layout](#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup))(boolean useCommands,
 [DiagramLayouter](layout/DiagramLayouter.html) diagramLayouter,
 [AbstractDiagramLayouterOptionsGroup](../../core/options/AbstractDiagramLayouterOptionsGroup.html) options)`
Layout the diagram.
`void`
`[open](#open())()`
Open the diagram
`void`
`[open](#open(boolean))(boolean showProgress)`
Open the diagram in a new diagram tab, or activates diagram tab if this diagram is already open
`void`
`[openInActiveTab](#openInActiveTab(boolean))(boolean showProgress)`
Open diagram in currently active diagram tab
 If no other diagram is opened yet, creates a new tab
 If this diagram is already opened, simply activates that tab
`boolean`
`[removeContentPropertyChangeListener](#removeContentPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Unregister the given listener from the diagram.
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElement](PresentationElement.html)
`[addProperty](PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)), [collectSubManipulatedElements](PresentationElement.html#collectSubManipulatedElements(java.util.List)), [editName](PresentationElement.html#editName(java.awt.event.KeyEvent)), [editName](PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)), [getBoundsShape](PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)), [getDiagramPresentationElement](PresentationElement.html#getDiagramPresentationElement()), [getElement](PresentationElement.html#getElement()), [getManipulatedParent](PresentationElement.html#getManipulatedParent()), [getManipulatedPresentationElements](PresentationElement.html#getManipulatedPresentationElements()), [getMiddlePoint](PresentationElement.html#getMiddlePoint()), [getObjectParent](PresentationElement.html#getObjectParent()), [getParent](PresentationElement.html#getParent()), [getPreferredDimension](PresentationElement.html#getPreferredDimension()), [getPreferredSize](PresentationElement.html#getPreferredSize()), [getPresentationElementStroke](PresentationElement.html#getPresentationElementStroke()), [getPresentationElementStroke](PresentationElement.html#getPresentationElementStroke(int)), [getPropertyManager](PresentationElement.html#getPropertyManager()), [getSelected](PresentationElement.html#getSelected()), [getStroke](PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)), [getStroke](PresentationElement.html#getStroke(int)), [getStroke](PresentationElement.html#getStroke(int,int)), [getStroke](PresentationElement.html#getStroke(int,int,int)), [getStroke](PresentationElement.html#getStroke(int,int,int,int)), [getStroke](PresentationElement.html#getStroke(java.awt.BasicStroke,int)), [hasManipulatedPresentationElements](PresentationElement.html#hasManipulatedPresentationElements()), [isSelected](PresentationElement.html#isSelected()), [onFind](PresentationElement.html#onFind()), [onFind](PresentationElement.html#onFind(boolean)), [setAllSelected](PresentationElement.html#setAllSelected(boolean)), [setSelected](PresentationElement.html#setSelected(boolean)), [setSelected](PresentationElement.html#setSelected(java.util.List))`
Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl
`accept, canAdd, canAddChild, canBeDeleted, compareTo, createSortKeys, getClassType, getCommandForAppending, getName, getProject, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, setProjectProvider, sGetID, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../BaseElement.html)
`[canAdd](../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement))`
Methods inherited from interface com.nomagic.magicdraw.utils.[NameOwner](../../utils/NameOwner.html)
`[getName](../../utils/NameOwner.html#getName())`

============ METHOD DETAIL ========== 
Method Details
collectShowingManipulatedElementsRecursively
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collectShowingManipulatedElementsRecursively()
Collects all visible manipulated elements in this diagram recursively.
Returns:
manipulated elements in this diagram
collectShowingPresentationElementsRecursively
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collectShowingPresentationElementsRecursively()
Collects all visible elements in this diagram recursively.
Returns:
visible elements in this diagram
collectPresentationElementsRecursively
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> collectPresentationElementsRecursively()
Collects all elements in this diagram recursively.
Returns:
elements in this diagram
addContentPropertyChangeListener
@OpenApipublic boolean addContentPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Registers the listener for changes in all symbols contained in the diagram.
Parameters:
`listener` - the `PropertyChangeListener` to be added
Returns:
true if listener was added - it wasn't there yet, otherwise false
removeContentPropertyChangeListener
@OpenApipublic boolean removeContentPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Unregister the given listener from the diagram.
Parameters:
`listener` - the PropertyChangeListener to be removed
Returns:
true if listener was removed
isSymbolDiagram
@OpenApipublic boolean isSymbolDiagram()
Checks if diagram displays symbols as its contents. Other type of diagrams may be tables, matrices.
Returns:
true if diagram displays symbols
accept
@OpenApipublic void accept([Visitor](../Visitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[MDElement](../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))`
Method accepts visitor, and calls method visit<class name>(this) of visitor .
 See Visitor pattern for more details.
Specified by:
`[accept](../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor))` in interface `[MDElement](../MDElement.html)`
Overrides:
`accept` in class `com.nomagic.magicdraw.uml.MDElementImpl`
Parameters:
`visitor` - which visits this element.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
isLoaded
@OpenApipublic boolean isLoaded()
Check if diagram is loaded.
Returns:
true if diagram contents is loaded
ensureLoaded
@OpenApipublic void ensureLoaded()
Ensures that diagram is loaded. If diagram is not loaded, loads it.
 Make sure the project is active before invoking this method.
 Otherwise, diagram may not be loaded.
layout
@OpenApipublic boolean layout(boolean useCommands)
Layout the diagram using default layouter.
 **Make sure before doing layout:**diagram is opened - use [`open()`](#open()) to open diagram.
session is closed - use [`SessionManager.closeSession(Project)`](../../openapi/uml/SessionManager.html#closeSession(com.nomagic.magicdraw.core.Project)) to close session.
 Only selected symbols in diagram are layouted. All symbols are layouted if selection is empty.
 Use [`PresentationElement.setSelected(java.util.List)`](PresentationElement.html#setSelected(java.util.List)) ()} to selects symbols in the diagram.
Parameters:
`useCommands` - true to create commands. If true, this command will be available in project's command history.
Returns:
true if layout was performed.
layout
@OpenApipublic boolean layout(boolean useCommands,
 [DiagramLayouter](layout/DiagramLayouter.html) layouter)
Layouts the diagram with the specified layouter.
 **Make sure before doing layout:**diagram is opened - use [`open()`](#open()) to open diagram.
session is closed - use [`SessionManager.closeSession(Project)`](../../openapi/uml/SessionManager.html#closeSession(com.nomagic.magicdraw.core.Project)) to close session.
 Only selected symbols in diagram are layouted. All symbols are layouted if selection is empty.
 Use [`PresentationElement.setSelected(java.util.List)`](PresentationElement.html#setSelected(java.util.List)) ()} to selects symbols in the diagram.
Parameters:
`useCommands` - true to create commands. If true, this command will be available in project's command history
`layouter` - layouter to be used for layouting
Returns:
true if layout was performed.
layout
@OpenApipublic boolean layout(boolean useCommands,
 [DiagramLayouter](layout/DiagramLayouter.html) diagramLayouter,
 [AbstractDiagramLayouterOptionsGroup](../../core/options/AbstractDiagramLayouterOptionsGroup.html) options)
Layout the diagram.
 **Make sure before doing layout:**diagram is opened - use [`open()`](#open()) to open diagram.
session is closed - use [`SessionManager.closeSession(Project)`](../../openapi/uml/SessionManager.html#closeSession(com.nomagic.magicdraw.core.Project)) to close session.
 Only selected symbols in diagram are layouted. All symbols are layouted if selection is empty.
 Use [`PresentationElement.setSelected(java.util.List)`](PresentationElement.html#setSelected(java.util.List)) ()} to selects symbols in the diagram.
Parameters:
`useCommands` - true to create commands. If true, this command will be available in project's command history
`diagramLayouter` - layouter to use
`options` - layout options
Returns:
true if layout was performed
findPresentationElement
@OpenApi
@CheckForNullpublic final [PresentationElement](PresentationElement.html) findPresentationElement(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)
Finds presentation element for given model element of given symbol type in this diagram. Does recursive search in the diagram.
Parameters:
`element` - the given ModelElement.
`presentationElementClass` - the class of presentation element or null if any.
Returns:
found presentation element or null if given ModelElement does not have presentation element in this diagram.
findPresentationElement
@OpenApi
@CheckForNullpublic final [PresentationElement](PresentationElement.html) findPresentationElement(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)
Finds presentation element for given model element of given symbol type in this diagram. Does recursive search in the diagram.
Parameters:
`element` - the given ModelElement.
`presentationElementClass` - the class of presentation element or null if any.
Returns:
found presentation element or null if given ModelElement does not have presentation element in this diagram.
findPresentationElementForPathConnecting
@CheckForNull
@OpenApipublic final [PresentationElement](PresentationElement.html) findPresentationElementForPathConnecting([BaseElement](../BaseElement.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)
Finds presentation element to connect some PathElement for given model element of given type in this diagram. Does recursive search.
 For example if TemplateSignature will be passes as element, Class owning that signature will be found.
Parameters:
`element` - the given ModelElement
`presentationElementClass` - the class of presentation element or null if any.
Returns:
found presentation element or null if given ModelElement does not have presentation element in this diagram.
findPresentationElementsForPathConnecting
@OpenApipublic final [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<[PresentationElement](PresentationElement.html)> findPresentationElementsForPathConnecting([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) presentationElementClass)
Finds presentations element to connect some PathElement for given model element of given type in this diagram. Does recursive search.
 For example if TemplateSignature will be passes as element, Class owning that signature will be found.
Parameters:
`element` - the given ModelElement
`presentationElementClass` - the class of presentation element or null if any.
Returns:
a stream of presentation elements
open
@OpenApipublic void open()
Open the diagram
open
@OpenApipublic void open(boolean showProgress)
Open the diagram in a new diagram tab, or activates diagram tab if this diagram is already open
Parameters:
`showProgress` - show progress dialog
openInActiveTab
@OpenApipublic void openInActiveTab(boolean showProgress)
Open diagram in currently active diagram tab
 If no other diagram is opened yet, creates a new tab
 If this diagram is already opened, simply activates that tab
Parameters:
`showProgress` - show progress dialog
close
@OpenApipublic final void close()
Closes diagram window.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class AbstractDiagramPresentationElement">Class AbstractDiagramPresentationElement</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.MDElementImpl
<div class="inheritance"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElement</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer</code>, <code><a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code>, <code><a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code>, <code><a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractDiagramPresentationElement</span>
<span class="extends-implements">extends <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>
implements com.nomagic.magicdraw.core.diagram.DiagramPresentationImplementer</span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Fields inherited from class com.nomagic.magicdraw.uml.symbols.<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="PresentationElement.html#DASHED_STROKE">DASHED_STROKE</a>, <a href="PresentationElement.html#DOTTED_STROKE">DOTTED_STROKE</a>, <a href="PresentationElement.html#SOLID_STROKE">SOLID_STROKE</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a><wbr/>(<a href="../Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method accepts visitor, and calls method visit&lt;class name&gt;(this) of visitor .</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addContentPropertyChangeListener(java.beans.PropertyChangeListener)">addContentPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers the listener for changes in all symbols contained in the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#close()">close</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes diagram window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectPresentationElementsRecursively()">collectPresentationElementsRecursively</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements in this diagram recursively.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectShowingManipulatedElementsRecursively()">collectShowingManipulatedElementsRecursively</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all visible manipulated elements in this diagram recursively.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectShowingPresentationElementsRecursively()">collectShowingPresentationElementsRecursively</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all visible elements in this diagram recursively.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureLoaded()">ensureLoaded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Ensures that diagram is loaded.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class)">findPresentationElement</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds presentation element for given model element of given symbol type in this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findPresentationElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds presentation element for given model element of given symbol type in this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class)">findPresentationElementForPathConnecting</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds presentation element to connect some PathElement for given model element of given type in this diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findPresentationElementsForPathConnecting</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds presentations element to connect some PathElement for given model element of given type in this diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLoaded()">isLoaded</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if diagram is loaded.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSymbolDiagram()">isSymbolDiagram</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if diagram displays symbols as its contents.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#layout(boolean)">layout</a><wbr/>(boolean useCommands)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Layout the diagram using default layouter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">layout</a><wbr/>(boolean useCommands,
 <a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> layouter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Layouts the diagram with the specified layouter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">layout</a><wbr/>(boolean useCommands,
 <a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> diagramLayouter,
 <a href="../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Layout the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#open()">open</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Open the diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#open(boolean)">open</a><wbr/>(boolean showProgress)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Open the diagram in a new diagram tab, or activates diagram tab if this diagram is already open</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openInActiveTab(boolean)">openInActiveTab</a><wbr/>(boolean showProgress)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Open diagram in currently active diagram tab
 If no other diagram is opened yet, creates a new tab
 If this diagram is already opened, simply activates that tab</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeContentPropertyChangeListener(java.beans.PropertyChangeListener)">removeContentPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregister the given listener from the diagram.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElement">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></h3>
<code><a href="PresentationElement.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="PresentationElement.html#collectSubManipulatedElements(java.util.List)">collectSubManipulatedElements</a>, <a href="PresentationElement.html#editName(java.awt.event.KeyEvent)">editName</a>, <a href="PresentationElement.html#editName(java.awt.event.KeyEvent,java.util.Map)">editName</a>, <a href="PresentationElement.html#getBoundsShape(com.nomagic.magicdraw.uml.symbols.ConverterToShape)">getBoundsShape</a>, <a href="PresentationElement.html#getDiagramPresentationElement()">getDiagramPresentationElement</a>, <a href="PresentationElement.html#getElement()">getElement</a>, <a href="PresentationElement.html#getManipulatedParent()">getManipulatedParent</a>, <a href="PresentationElement.html#getManipulatedPresentationElements()">getManipulatedPresentationElements</a>, <a href="PresentationElement.html#getMiddlePoint()">getMiddlePoint</a>, <a href="PresentationElement.html#getObjectParent()">getObjectParent</a>, <a href="PresentationElement.html#getParent()">getParent</a>, <a href="PresentationElement.html#getPreferredDimension()">getPreferredDimension</a>, <a href="PresentationElement.html#getPreferredSize()">getPreferredSize</a>, <a href="PresentationElement.html#getPresentationElementStroke()">getPresentationElementStroke</a>, <a href="PresentationElement.html#getPresentationElementStroke(int)">getPresentationElementStroke</a>, <a href="PresentationElement.html#getPropertyManager()">getPropertyManager</a>, <a href="PresentationElement.html#getSelected()">getSelected</a>, <a href="PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)">getStroke</a>, <a href="PresentationElement.html#getStroke(int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(int,int,int,int)">getStroke</a>, <a href="PresentationElement.html#getStroke(java.awt.BasicStroke,int)">getStroke</a>, <a href="PresentationElement.html#hasManipulatedPresentationElements()">hasManipulatedPresentationElements</a>, <a href="PresentationElement.html#isSelected()">isSelected</a>, <a href="PresentationElement.html#onFind()">onFind</a>, <a href="PresentationElement.html#onFind(boolean)">onFind</a>, <a href="PresentationElement.html#setAllSelected(boolean)">setAllSelected</a>, <a href="PresentationElement.html#setSelected(boolean)">setSelected</a>, <a href="PresentationElement.html#setSelected(java.util.List)">setSelected</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.MDElementImpl">Methods inherited from class com.nomagic.magicdraw.uml.MDElementImpl</h3>
<code>accept, canAdd, canAddChild, canBeDeleted, compareTo, createSortKeys, getClassType, getCommandForAppending, getName, getProject, getProjectProvider, getResourceID, getSortKeys, hasListeners, isEditable, removeAllParents, removeAllPropertyChangeListeners, setProjectProvider, sGetID, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.utils.NameOwner">Methods inherited from interface com.nomagic.magicdraw.utils.<a href="../../utils/NameOwner.html" title="interface in com.nomagic.magicdraw.utils">NameOwner</a></h3>
<code><a href="../../utils/NameOwner.html#getName()">getName</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="collectShowingManipulatedElementsRecursively()">
<h3>collectShowingManipulatedElementsRecursively</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">collectShowingManipulatedElementsRecursively</span>()</div>
<div class="block">Collects all visible manipulated elements in this diagram recursively.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manipulated elements in this diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectShowingPresentationElementsRecursively()">
<h3>collectShowingPresentationElementsRecursively</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">collectShowingPresentationElementsRecursively</span>()</div>
<div class="block">Collects all visible elements in this diagram recursively.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>visible elements in this diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectPresentationElementsRecursively()">
<h3>collectPresentationElementsRecursively</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">collectPresentationElementsRecursively</span>()</div>
<div class="block">Collects all elements in this diagram recursively.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>elements in this diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addContentPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addContentPropertyChangeListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addContentPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Registers the listener for changes in all symbols contained in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the <code>PropertyChangeListener</code> to be added</dd>
<dt>Returns:</dt>
<dd>true if listener was added - it wasn't there yet, otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeContentPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removeContentPropertyChangeListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">removeContentPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Unregister the given listener from the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the PropertyChangeListener to be removed</dd>
<dt>Returns:</dt>
<dd>true if listener was removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSymbolDiagram()">
<h3>isSymbolDiagram</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSymbolDiagram</span>()</div>
<div class="block">Checks if diagram displays symbols as its contents. Other type of diagrams may be tables, matrices.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram displays symbols</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.Visitor)">
<h3>accept</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">MDElement</a></code></span></div>
<div class="block">Method accepts visitor, and calls method visit&lt;class name&gt;(this) of visitor .
 See Visitor pattern for more details.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../MDElement.html#accept(com.nomagic.magicdraw.uml.Visitor)">accept</a></code> in interface <code><a href="../MDElement.html" title="interface in com.nomagic.magicdraw.uml">MDElement</a></code></dd>
<dt>Overrides:</dt>
<dd><code>accept</code> in class <code>com.nomagic.magicdraw.uml.MDElementImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - which visits this element.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLoaded()">
<h3>isLoaded</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLoaded</span>()</div>
<div class="block">Check if diagram is loaded.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if diagram contents is loaded</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ensureLoaded()">
<h3>ensureLoaded</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">ensureLoaded</span>()</div>
<div class="block">Ensures that diagram is loaded. If diagram is not loaded, loads it.
 Make sure the project is active before invoking this method.
 Otherwise, diagram may not be loaded.</div>
</section>
</li>
<li>
<section class="detail" id="layout(boolean)">
<h3>layout</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(boolean useCommands)</span></div>
<div class="block">Layout the diagram using default layouter.
 <p><strong>Make sure before doing layout:</strong><ul>
<li>diagram is opened - use <a href="#open()"><code>open()</code></a> to open diagram.</li>
<li>session is closed - use <a href="../../openapi/uml/SessionManager.html#closeSession(com.nomagic.magicdraw.core.Project)"><code>SessionManager.closeSession(Project)</code></a> to close session.</li>
</ul></p>
 Only selected symbols in diagram are layouted. All symbols are layouted if selection is empty.
 Use <a href="PresentationElement.html#setSelected(java.util.List)"><code>PresentationElement.setSelected(java.util.List)</code></a> ()} to selects symbols in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCommands</code> - true to create commands. If true, this command will be available in project's command history.</dd>
<dt>Returns:</dt>
<dd>true if layout was performed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter)">
<h3>layout</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(boolean useCommands,
 <a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> layouter)</span></div>
<div class="block">Layouts the diagram with the specified layouter.
 <p><strong>Make sure before doing layout:</strong><ul>
<li>diagram is opened - use <a href="#open()"><code>open()</code></a> to open diagram.</li>
<li>session is closed - use <a href="../../openapi/uml/SessionManager.html#closeSession(com.nomagic.magicdraw.core.Project)"><code>SessionManager.closeSession(Project)</code></a> to close session.</li>
</ul></p>
 Only selected symbols in diagram are layouted. All symbols are layouted if selection is empty.
 Use <a href="PresentationElement.html#setSelected(java.util.List)"><code>PresentationElement.setSelected(java.util.List)</code></a> ()} to selects symbols in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCommands</code> - true to create commands. If true, this command will be available in project's command history</dd>
<dd><code>layouter</code> - layouter to be used for layouting</dd>
<dt>Returns:</dt>
<dd>true if layout was performed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="layout(boolean,com.nomagic.magicdraw.uml.symbols.layout.DiagramLayouter,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">
<h3>layout</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(boolean useCommands,
 <a href="layout/DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a> diagramLayouter,
 <a href="../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options)</span></div>
<div class="block">Layout the diagram.
 <p><strong>Make sure before doing layout:</strong><ul>
<li>diagram is opened - use <a href="#open()"><code>open()</code></a> to open diagram.</li>
<li>session is closed - use <a href="../../openapi/uml/SessionManager.html#closeSession(com.nomagic.magicdraw.core.Project)"><code>SessionManager.closeSession(Project)</code></a> to close session.</li>
</ul></p>
 Only selected symbols in diagram are layouted. All symbols are layouted if selection is empty.
 Use <a href="PresentationElement.html#setSelected(java.util.List)"><code>PresentationElement.setSelected(java.util.List)</code></a> ()} to selects symbols in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCommands</code> - true to create commands. If true, this command will be available in project's command history</dd>
<dd><code>diagramLayouter</code> - layouter to use</dd>
<dd><code>options</code> - layout options</dd>
<dt>Returns:</dt>
<dd>true if layout was performed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">findPresentationElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</span></div>
<div class="block">Finds presentation element for given model element of given symbol type in this diagram. Does recursive search in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement.</dd>
<dd><code>presentationElementClass</code> - the class of presentation element or null if any.</dd>
<dt>Returns:</dt>
<dd>found presentation element or null if given ModelElement does not have presentation element in this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElement(com.dassault_systemes.modeler.foundation.model.ModelElement,java.lang.Class)">
<h3>findPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">findPresentationElement</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.model.ModelElement element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</span></div>
<div class="block">Finds presentation element for given model element of given symbol type in this diagram. Does recursive search in the diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement.</dd>
<dd><code>presentationElementClass</code> - the class of presentation element or null if any.</dd>
<dt>Returns:</dt>
<dd>found presentation element or null if given ModelElement does not have presentation element in this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElementForPathConnecting(com.nomagic.magicdraw.uml.BaseElement,java.lang.Class)">
<h3>findPresentationElementForPathConnecting</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">findPresentationElementForPathConnecting</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</span></div>
<div class="block">Finds presentation element to connect some PathElement for given model element of given type in this diagram. Does recursive search.
 For example if TemplateSignature will be passes as element, Class owning that signature will be found.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement</dd>
<dd><code>presentationElementClass</code> - the class of presentation element or null if any.</dd>
<dt>Returns:</dt>
<dd>found presentation element or null if given ModelElement does not have presentation element in this diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPresentationElementsForPathConnecting(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>findPresentationElementsForPathConnecting</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">findPresentationElementsForPathConnecting</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> presentationElementClass)</span></div>
<div class="block">Finds presentations element to connect some PathElement for given model element of given type in this diagram. Does recursive search.
 For example if TemplateSignature will be passes as element, Class owning that signature will be found.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement</dd>
<dd><code>presentationElementClass</code> - the class of presentation element or null if any.</dd>
<dt>Returns:</dt>
<dd>a stream of presentation elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="open()">
<h3>open</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">open</span>()</div>
<div class="block">Open the diagram</div>
</section>
</li>
<li>
<section class="detail" id="open(boolean)">
<h3>open</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">open</span><wbr/><span class="parameters">(boolean showProgress)</span></div>
<div class="block">Open the diagram in a new diagram tab, or activates diagram tab if this diagram is already open</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showProgress</code> - show progress dialog</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openInActiveTab(boolean)">
<h3>openInActiveTab</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">openInActiveTab</span><wbr/><span class="parameters">(boolean showProgress)</span></div>
<div class="block">Open diagram in currently active diagram tab
 If no other diagram is opened yet, creates a new tab
 If this diagram is already opened, simply activates that tab</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showProgress</code> - show progress dialog</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="close()">
<h3>close</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">close</span>()</div>
<div class="block">Closes diagram window.</div>
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
