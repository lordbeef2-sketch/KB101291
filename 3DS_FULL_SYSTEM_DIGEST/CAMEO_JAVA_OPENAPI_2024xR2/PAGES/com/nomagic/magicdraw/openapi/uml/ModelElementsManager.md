# JAVA OPENAPI: ModelElementsManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/openapi/uml/ModelElementsManager.html
- source_path: `com/nomagic/magicdraw/openapi/uml/ModelElementsManager.html`
- source_sha256: `dcd457d3924f1e04c08ce7b2bd4807953739718f5e3c21821a8b6285421ab7aa`
- captured_utc: `2026-07-14T16:55:24.776117+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.openapi.uml](package-summary.html)

## Class ModelElementsManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.openapi.uml.ModelElementsManager

@OpenApiAllpublic final classModelElementsManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

The utility class for ModelElements adding, removing and moving to other parents.
 Also it helps to create all 7 types of diagrams.
 Works together with `SessionManager`.
 This manager can be used only if some session was created with SessionManager. See code sample in SessionManager
 description for more details.

See Also:
[`SessionManager`](SessionManager.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addElement](#addElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent)`
Adds given element into the given parent.
`[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)`
`[createDiagram](#createDiagram(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [Namespace](../../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) parent)`
Creates new Diagram of given type.
`[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)`
`[createDiagram](#createDiagram(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [Namespace](../../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) parent,
 boolean openDiagram,
 boolean openInActiveTab)`
Creates new Diagram of given type.
`static [ModelElementsManager](ModelElementsManager.html)`
`[getInstance](#getInstance())()`
Returns an instance of this manager.
`void`
`[moveElement](#moveElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent)`
Moves given element from current parent into the given one.
`void`
`[removeElement](#removeElement(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`
Removes given element from the model.
`void`
`[removeElement](#removeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Removes given element from the model.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
public static [ModelElementsManager](ModelElementsManager.html) getInstance()
Returns an instance of this manager.
Returns:
instance of this manager.Pro
addElement
public void addElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Adds given element into the given parent.
Parameters:
`element` - the given model element to add into the given parent.
`parent` - the given model element parent.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if session is not created with SessionManager
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - given model element cannot be added into given parent. For example Operation
 cannot be added into Package or Operation cannot be added into not locked for editing Class(in teamwork project).
 Also it is thrown if element or parent is null.
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if given element is not editable(read only).
See Also:
[`SessionManager.createSession(java.lang.String)`](SessionManager.html#createSession(java.lang.String))
moveElement
public void moveElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) parent)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Moves given element from current parent into the given one.
Parameters:
`element` - the given ModelElement to move into the given parent.
`parent` - a new parent for given ModelElement.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if session is not created with SessionManager
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - given ModelElement cannot be added into given parent. For example Operation
 cannot be added into Package or Operation cannot be added into not locked for editing Class(in teamwork project).
 Also this exception is thrown if new parent already has the same type child with the same name as given element.
 It is thrown if element or parent is null, too.
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if given element is not editable(read only).
See Also:
[`SessionManager.createSession(java.lang.String)`](SessionManager.html#createSession(java.lang.String))
removeElement
public void removeElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Removes given element from the model.
Parameters:
`element` - the given ModelElement to remove.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if session is not created with SessionManager.
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given element is null.
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if given element is not editable(read only).
See Also:
[`SessionManager.createSession(java.lang.String)`](SessionManager.html#createSession(java.lang.String))
removeElement
public void removeElement(com.dassault_systemes.modeler.foundation.model.ModelElement element)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Removes given element from the model.
Parameters:
`element` - the given ModelElement to remove.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if session is not created with SessionManager.
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given element is null.
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if given element is not editable(read only).
See Also:
[`SessionManager.createSession(java.lang.String)`](SessionManager.html#createSession(java.lang.String))
createDiagram
public [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) createDiagram([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [Namespace](../../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) parent)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates new Diagram of given type. All available types are predefined in constants class DiagramTypeConstants.
 The created diagram instance is added into parent.
Parameters:
`type` - diagram type
`parent` - diagram owner
Returns:
The created diagram.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if session is not created with SessionManager
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given type is unknown. if given model element cannot be added into given parent. For example Operation
 cannot be added into Package or Operation cannot be added into not locked for editing Class(in teamwork project).
 Also it is thrown if element or parent is null.
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if parent element is not editable(read only).
See Also:
[`DiagramTypes.UML_CLASS_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_CLASS_DIAGRAM)
[`DiagramTypes.UML_USECASE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_USECASE_DIAGRAM)
[`DiagramTypes.UML_COMMUNICATION_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_COMMUNICATION_DIAGRAM)
[`DiagramTypes.UML_SEQUENCE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_SEQUENCE_DIAGRAM)
[`DiagramTypes.UML_STATECHART_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_STATECHART_DIAGRAM)
[`DiagramTypes.UML_PROTOCOL_STATE_MACHINE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_PROTOCOL_STATE_MACHINE_DIAGRAM)
[`DiagramTypes.UML_ACTIVITY_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_ACTIVITY_DIAGRAM)
[`DiagramTypes.UML_OBJECT_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_OBJECT_DIAGRAM)
[`DiagramTypes.UML_PACKAGE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_PACKAGE_DIAGRAM)
[`DiagramTypes.UML_COMPONENT_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_COMPONENT_DIAGRAM)
[`DiagramTypes.UML_DEPLOYMENT_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_DEPLOYMENT_DIAGRAM)
[`DiagramTypes.UML_PROFILE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_PROFILE_DIAGRAM)
[`DiagramTypes.UML_COMPOSITE_STRUCTURE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_COMPOSITE_STRUCTURE_DIAGRAM)
createDiagram
public [Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) createDiagram([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [Namespace](../../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html) parent,
 boolean openDiagram,
 boolean openInActiveTab)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Creates new Diagram of given type. All available types are predefined in constants class DiagramTypeConstants.
 The created diagram instance is added into parent.
Parameters:
`type` - diagram type
`parent` - diagram owner
`openDiagram` - if open created diagram
`openInActiveTab` - if open diagram in active tab if we open diagram
Returns:
The created diagram.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if session is not created with SessionManager
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if given type is unknown. if given model element cannot be added into given parent. For example Operation
 cannot be added into Package or Operation cannot be added into not locked for editing Class(in teamwork project).
 Also it is thrown if element or parent is null.
`[ReadOnlyElementException](ReadOnlyElementException.html)` - if parent element is not editable(read only).
See Also:
[`DiagramTypes.UML_CLASS_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_CLASS_DIAGRAM)
[`DiagramTypes.UML_USECASE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_USECASE_DIAGRAM)
[`DiagramTypes.UML_COMMUNICATION_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_COMMUNICATION_DIAGRAM)
[`DiagramTypes.UML_SEQUENCE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_SEQUENCE_DIAGRAM)
[`DiagramTypes.UML_STATECHART_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_STATECHART_DIAGRAM)
[`DiagramTypes.UML_PROTOCOL_STATE_MACHINE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_PROTOCOL_STATE_MACHINE_DIAGRAM)
[`DiagramTypes.UML_ACTIVITY_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_ACTIVITY_DIAGRAM)
[`DiagramTypes.UML_OBJECT_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_OBJECT_DIAGRAM)
[`DiagramTypes.UML_PACKAGE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_PACKAGE_DIAGRAM)
[`DiagramTypes.UML_COMPONENT_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_COMPONENT_DIAGRAM)
[`DiagramTypes.UML_DEPLOYMENT_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_DEPLOYMENT_DIAGRAM)
[`DiagramTypes.UML_PROFILE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_PROFILE_DIAGRAM)
[`DiagramTypes.UML_COMPOSITE_STRUCTURE_DIAGRAM`](../../../uml2/diagram/DiagramTypes.html#UML_COMPOSITE_STRUCTURE_DIAGRAM)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.openapi.uml</a></div>
<h1 class="title" title="Class ModelElementsManager">Class ModelElementsManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.openapi.uml.ModelElementsManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">ModelElementsManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The utility class for ModelElements adding, removing and moving to other parents.
 Also it helps to create all 7 types of diagrams.
 Works together with <code>SessionManager</code>.
 <p>
 This manager can be used only if some session was created with SessionManager. See code sample in SessionManager
 description for more details.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">addElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds given element into the given parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDiagram(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">createDiagram</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> parent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates new Diagram of given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDiagram(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace,boolean,boolean)">createDiagram</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> parent,
 boolean openDiagram,
 boolean openInActiveTab)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates new Diagram of given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ModelElementsManager.html" title="class in com.nomagic.magicdraw.openapi.uml">ModelElementsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an instance of this manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#moveElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">moveElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves given element from current parent into the given one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">removeElement</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given element from the model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given element from the model.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ModelElementsManager.html" title="class in com.nomagic.magicdraw.openapi.uml">ModelElementsManager</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Returns an instance of this manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance of this manager.Pro</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>addElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent)</span>
                throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Adds given element into the given parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given model element to add into the given parent.</dd>
<dd><code>parent</code> - the given model element parent.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session is not created with SessionManager</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - given model element cannot be added into given parent. For example Operation
                                  cannot be added into Package or Operation cannot be added into not locked for editing Class(in teamwork project).
                                  Also it is thrown if element or parent is null.</dd>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given element is not editable(read only).</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="SessionManager.html#createSession(java.lang.String)"><code>SessionManager.createSession(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="moveElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>moveElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">moveElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> parent)</span>
                 throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Moves given element from current parent into the given one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement to move into the given parent.</dd>
<dd><code>parent</code> - a new parent for given ModelElement.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session is not created with SessionManager</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - given ModelElement cannot be added into given parent. For example Operation
                                  cannot be added into Package or Operation cannot be added into not locked for editing Class(in teamwork project).
                                  Also this exception is thrown if new parent already has the same type child with the same name as given element.
                                  It is thrown if element or parent is null, too.</dd>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given element is not editable(read only).</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="SessionManager.html#createSession(java.lang.String)"><code>SessionManager.createSession(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span>
                   throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Removes given element from the model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement to remove.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session is not created with SessionManager.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given element is null.</dd>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given element is not editable(read only).</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="SessionManager.html#createSession(java.lang.String)"><code>SessionManager.createSession(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>removeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeElement</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element)</span>
                   throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Removes given element from the model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given ModelElement to remove.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session is not created with SessionManager.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given element is null.</dd>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if given element is not editable(read only).</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="SessionManager.html#createSession(java.lang.String)"><code>SessionManager.createSession(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDiagram(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>createDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></span> <span class="element-name">createDiagram</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> parent)</span>
                      throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates new Diagram of given type. All available types are predefined in constants class DiagramTypeConstants.
 The created diagram instance is added into parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type</dd>
<dd><code>parent</code> - diagram owner</dd>
<dt>Returns:</dt>
<dd>The created diagram.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session is not created with SessionManager</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given type is unknown. if given model element cannot be added into given parent. For example Operation
                                  cannot be added into Package or Operation cannot be added into not locked for editing Class(in teamwork project).
                                  Also it is thrown if element or parent is null.</dd>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if parent element is not editable(read only).</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_CLASS_DIAGRAM"><code>DiagramTypes.UML_CLASS_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_USECASE_DIAGRAM"><code>DiagramTypes.UML_USECASE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_COMMUNICATION_DIAGRAM"><code>DiagramTypes.UML_COMMUNICATION_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_SEQUENCE_DIAGRAM"><code>DiagramTypes.UML_SEQUENCE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_STATECHART_DIAGRAM"><code>DiagramTypes.UML_STATECHART_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_PROTOCOL_STATE_MACHINE_DIAGRAM"><code>DiagramTypes.UML_PROTOCOL_STATE_MACHINE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_ACTIVITY_DIAGRAM"><code>DiagramTypes.UML_ACTIVITY_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_OBJECT_DIAGRAM"><code>DiagramTypes.UML_OBJECT_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_PACKAGE_DIAGRAM"><code>DiagramTypes.UML_PACKAGE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_COMPONENT_DIAGRAM"><code>DiagramTypes.UML_COMPONENT_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_DEPLOYMENT_DIAGRAM"><code>DiagramTypes.UML_DEPLOYMENT_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_PROFILE_DIAGRAM"><code>DiagramTypes.UML_PROFILE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_COMPOSITE_STRUCTURE_DIAGRAM"><code>DiagramTypes.UML_COMPOSITE_STRUCTURE_DIAGRAM</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDiagram(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace,boolean,boolean)">
<h3>createDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></span> <span class="element-name">createDiagram</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> parent,
 boolean openDiagram,
 boolean openInActiveTab)</span>
                      throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Creates new Diagram of given type. All available types are predefined in constants class DiagramTypeConstants.
 The created diagram instance is added into parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type</dd>
<dd><code>parent</code> - diagram owner</dd>
<dd><code>openDiagram</code> - if open created diagram</dd>
<dd><code>openInActiveTab</code> - if open diagram in active tab if we open diagram</dd>
<dt>Returns:</dt>
<dd>The created diagram.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session is not created with SessionManager</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if given type is unknown. if given model element cannot be added into given parent. For example Operation
                                  cannot be added into Package or Operation cannot be added into not locked for editing Class(in teamwork project).
                                  Also it is thrown if element or parent is null.</dd>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if parent element is not editable(read only).</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_CLASS_DIAGRAM"><code>DiagramTypes.UML_CLASS_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_USECASE_DIAGRAM"><code>DiagramTypes.UML_USECASE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_COMMUNICATION_DIAGRAM"><code>DiagramTypes.UML_COMMUNICATION_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_SEQUENCE_DIAGRAM"><code>DiagramTypes.UML_SEQUENCE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_STATECHART_DIAGRAM"><code>DiagramTypes.UML_STATECHART_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_PROTOCOL_STATE_MACHINE_DIAGRAM"><code>DiagramTypes.UML_PROTOCOL_STATE_MACHINE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_ACTIVITY_DIAGRAM"><code>DiagramTypes.UML_ACTIVITY_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_OBJECT_DIAGRAM"><code>DiagramTypes.UML_OBJECT_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_PACKAGE_DIAGRAM"><code>DiagramTypes.UML_PACKAGE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_COMPONENT_DIAGRAM"><code>DiagramTypes.UML_COMPONENT_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_DEPLOYMENT_DIAGRAM"><code>DiagramTypes.UML_DEPLOYMENT_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_PROFILE_DIAGRAM"><code>DiagramTypes.UML_PROFILE_DIAGRAM</code></a></li>
<li><a href="../../../uml2/diagram/DiagramTypes.html#UML_COMPOSITE_STRUCTURE_DIAGRAM"><code>DiagramTypes.UML_COMPOSITE_STRUCTURE_DIAGRAM</code></a></li>
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
