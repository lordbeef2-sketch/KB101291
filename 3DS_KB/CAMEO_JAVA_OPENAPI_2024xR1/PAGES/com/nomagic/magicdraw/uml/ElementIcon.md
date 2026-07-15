# JAVA OPENAPI: ElementIcon (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml/ElementIcon.html
- source_path: `com/nomagic/magicdraw/uml/ElementIcon.html`
- source_sha256: `e037926fbb881dc50dec9b1d875dd38deb154cc06a0978990aecb032d289db04`
- captured_utc: `2026-07-14T16:52:07.431819+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class ElementIcon

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.icons.ElementIconsRegistry](../icons/ElementIconsRegistry.html)
com.nomagic.magicdraw.uml.ElementIcon

@OpenApiAllpublic classElementIcon
extends [ElementIconsRegistry](../icons/ElementIconsRegistry.html)
Utility class for providing icons for Elements.
 Icon can be provided for BaseElement object, class type of Element, diagram type.
 See [`ClassTypes`](ClassTypes.html) for useful utility methods to work with class types.
 Use [`BaseElement.getClassType()`](BaseElement.html#getClassType()) to retrieve class type of the Element.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[SYMBOL_ADORNMENT](#SYMBOL_ADORNMENT)`
Fields inherited from class com.nomagic.magicdraw.icons.[ElementIconsRegistry](../icons/ElementIconsRegistry.html)
`[ABSTRACT_CLASS](../icons/ElementIconsRegistry.html#ABSTRACT_CLASS), [ACCEPT_TIME_EVENT_ACTION](../icons/ElementIconsRegistry.html#ACCEPT_TIME_EVENT_ACTION), [AGGREGATION](../icons/ElementIconsRegistry.html#AGGREGATION), [ARTIFACT_DEPLOYMENT_INSTANCE](../icons/ElementIconsRegistry.html#ARTIFACT_DEPLOYMENT_INSTANCE), [ARTIFACT_INSTANCE](../icons/ElementIconsRegistry.html#ARTIFACT_INSTANCE), [ASSEMBLY_CONNECTOR](../icons/ElementIconsRegistry.html#ASSEMBLY_CONNECTOR), [CALL_MESSAGE](../icons/ElementIconsRegistry.html#CALL_MESSAGE), [CHOICE_PSEUDO_STATE](../icons/ElementIconsRegistry.html#CHOICE_PSEUDO_STATE), [COMPONENT_INSTANCE](../icons/ElementIconsRegistry.html#COMPONENT_INSTANCE), [COMPOSITE_STATE](../icons/ElementIconsRegistry.html#COMPOSITE_STATE), [COMPOSITION](../icons/ElementIconsRegistry.html#COMPOSITION), [CONCURRENT_STATE](../icons/ElementIconsRegistry.html#CONCURRENT_STATE), [CREATE_MESSAGE](../icons/ElementIconsRegistry.html#CREATE_MESSAGE), [DEEP_HISTORY_PSEUDO_STATE](../icons/ElementIconsRegistry.html#DEEP_HISTORY_PSEUDO_STATE), [DELEGATION_CONNECTOR](../icons/ElementIconsRegistry.html#DELEGATION_CONNECTOR), [DESTROY_MESSAGE](../icons/ElementIconsRegistry.html#DESTROY_MESSAGE), [DEVICE_INSTANCE](../icons/ElementIconsRegistry.html#DEVICE_INSTANCE), [DIRECTED_AGGREGATION](../icons/ElementIconsRegistry.html#DIRECTED_AGGREGATION), [DIRECTED_ASSOCIATION](../icons/ElementIconsRegistry.html#DIRECTED_ASSOCIATION), [DIRECTED_COMPOSITION](../icons/ElementIconsRegistry.html#DIRECTED_COMPOSITION), [DOCUMENTATION](../icons/ElementIconsRegistry.html#DOCUMENTATION), [ENTRY_POINT_PSEUDO_STATE](../icons/ElementIconsRegistry.html#ENTRY_POINT_PSEUDO_STATE), [EXECUTION_ENVIRONMENT_INSTANCE](../icons/ElementIconsRegistry.html#EXECUTION_ENVIRONMENT_INSTANCE), [EXIT_POINT_PSEUDO_STATE](../icons/ElementIconsRegistry.html#EXIT_POINT_PSEUDO_STATE), [FORK_PSEUDO_STATE](../icons/ElementIconsRegistry.html#FORK_PSEUDO_STATE), [INITIAL_PSEUDO_STATE](../icons/ElementIconsRegistry.html#INITIAL_PSEUDO_STATE), [JOIN_PSEUDO_STATE](../icons/ElementIconsRegistry.html#JOIN_PSEUDO_STATE), [JUNCTION_PSEUDO_STATE](../icons/ElementIconsRegistry.html#JUNCTION_PSEUDO_STATE), [LINK](../icons/ElementIconsRegistry.html#LINK), [METACLASS](../icons/ElementIconsRegistry.html#METACLASS), [MODEL_MODEL_LIBRARY](../icons/ElementIconsRegistry.html#MODEL_MODEL_LIBRARY), [NARY_ASSOCIATION](../icons/ElementIconsRegistry.html#NARY_ASSOCIATION), [NODE_INSTANCE](../icons/ElementIconsRegistry.html#NODE_INSTANCE), [NON_NAVIGABLE_ASSOCIATION](../icons/ElementIconsRegistry.html#NON_NAVIGABLE_ASSOCIATION), [NONE_ICON](../icons/ElementIconsRegistry.html#NONE_ICON), [PACKAGE_MODEL_LIBRARY](../icons/ElementIconsRegistry.html#PACKAGE_MODEL_LIBRARY), [PROFILE_MODEL_LIBRARY](../icons/ElementIconsRegistry.html#PROFILE_MODEL_LIBRARY), [REPLY_MESSAGE](../icons/ElementIconsRegistry.html#REPLY_MESSAGE), [SEND_MESSAGE](../icons/ElementIconsRegistry.html#SEND_MESSAGE), [SHALLOW_HISTORY_PSEUDO_STATE](../icons/ElementIconsRegistry.html#SHALLOW_HISTORY_PSEUDO_STATE), [SUBMACHINE_STATE](../icons/ElementIconsRegistry.html#SUBMACHINE_STATE), [SUBSYSTEM](../icons/ElementIconsRegistry.html#SUBSYSTEM), [SUBSYSTEM_INSTANCE](../icons/ElementIconsRegistry.html#SUBSYSTEM_INSTANCE), [TERMINATE_PSEUDO_STATE](../icons/ElementIconsRegistry.html#TERMINATE_PSEUDO_STATE), [USECASE_INSTANCE](../icons/ElementIconsRegistry.html#USECASE_INSTANCE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ElementIcon](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[get16x16Icon](#get16x16Icon(com.nomagic.ui.ResizableIcon))([ResizableIcon](../../ui/ResizableIcon.html) icon)`
Return scaled down to 16x16 icon for a given icon
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIcon](#getIcon(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](BaseElement.html) element)`
Returns icon for a given element
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIcon](#getIcon(com.nomagic.magicdraw.uml.BaseElement,boolean))([BaseElement](BaseElement.html) element,
 boolean hideCustomPathStyle)`
Returns icon for a given element
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIconByClassType](#getIconByClassType(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType)`
Returns icon by class type of the element.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIconByClassType](#getIconByClassType(java.lang.Class,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns icon by class type and stereotype.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIconByClassType](#getIconByClassType(java.lang.Class,java.util.Collection))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes)`
Returns icon, according class type and stereotypes.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIconByDiagramType](#getIconByDiagramType(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([DiagramPresentationElement](symbols/DiagramPresentationElement.html) diagram)`
Returns icon by diagram type.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIconByDiagramType](#getIconByDiagramType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)`
Returns icon by diagram type
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIconByStereotype](#getIconByStereotype(java.util.function.Supplier,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[ResizableIcon](../../ui/ResizableIcon.html)> iconSupplier,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns icon from stereotype or from iconSupplier if stereotype has no icon
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIconByType](#getIconByType(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](BaseElement.html) element)`
Returns image, according element meta type.
`static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getSVGIconByDiagramType](#getSVGIconByDiagramType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)`
Returns SVG icon by diagram type
Methods inherited from class com.nomagic.magicdraw.icons.[ElementIconsRegistry](../icons/ElementIconsRegistry.html)
`[getIcon](../icons/ElementIconsRegistry.html#getIcon(java.lang.Class)), [internalGetIconByTypeMap](../icons/ElementIconsRegistry.html#internalGetIconByTypeMap()), [loadDoubleSizeIcon](../icons/ElementIconsRegistry.html#loadDoubleSizeIcon(java.lang.Class,java.lang.String)), [putIcon](../icons/ElementIconsRegistry.html#putIcon(java.lang.Class,com.nomagic.ui.ResizableIcon))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
SYMBOL_ADORNMENT
public static final [ResizableIcon](../../ui/ResizableIcon.html) SYMBOL_ADORNMENT
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ElementIcon
public ElementIcon()
 ============ METHOD DETAIL ========== 
Method Details
get16x16Icon
@CheckForNullpublic static [ResizableIcon](../../ui/ResizableIcon.html) get16x16Icon(@CheckForNull
 [ResizableIcon](../../ui/ResizableIcon.html) icon)
Return scaled down to 16x16 icon for a given icon
Parameters:
`icon` - icon
Returns:
scaled icon
getIcon
@CheckForNullpublic static [ResizableIcon](../../ui/ResizableIcon.html) getIcon(@CheckForNull
 [BaseElement](BaseElement.html) element)
Returns icon for a given element
Parameters:
`element` - the Element
Returns:
icon
getIcon
@CheckForNullpublic static [ResizableIcon](../../ui/ResizableIcon.html) getIcon(@CheckForNull
 [BaseElement](BaseElement.html) element,
 boolean hideCustomPathStyle)
Returns icon for a given element
Parameters:
`element` - the Element
`hideCustomPathStyle` - if true custom path style icon is skipped and standard relationship icons is returned
Returns:
icon
getIconByClassType
@CheckForNullpublic static [ResizableIcon](../../ui/ResizableIcon.html) getIconByClassType([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType,
 @CheckForNull
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns icon by class type and stereotype.
Parameters:
`classType` - class type
`stereotype` - given stereotype
Returns:
icon
getIconByStereotype
@CheckForNullpublic static [ResizableIcon](../../ui/ResizableIcon.html) getIconByStereotype([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[ResizableIcon](../../ui/ResizableIcon.html)> iconSupplier,
 @CheckForNull
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns icon from stereotype or from iconSupplier if stereotype has no icon
Parameters:
`iconSupplier` - icon supplier
`stereotype` - given stereotype
Returns:
icon
getIconByClassType
@CheckForNullpublic static [ResizableIcon](../../ui/ResizableIcon.html) getIconByClassType([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes)
Returns icon, according class type and stereotypes.
Parameters:
`classType` - class type
`stereotypes` - stereotypes
Returns:
icon
getIconByClassType
@CheckForNullpublic static [ResizableIcon](../../ui/ResizableIcon.html) getIconByClassType([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType)
Returns icon by class type of the element.
Parameters:
`classType` - class type
Returns:
icon
getIconByType
@CheckForNullpublic static [ResizableIcon](../../ui/ResizableIcon.html) getIconByType(@CheckForNull
 [BaseElement](BaseElement.html) element)
Returns image, according element meta type.
Parameters:
`element` - element
Returns:
icon
getIconByDiagramType
@CheckForNullpublic static [ResizableIcon](../../ui/ResizableIcon.html) getIconByDiagramType([DiagramPresentationElement](symbols/DiagramPresentationElement.html) diagram)
Returns icon by diagram type.
Parameters:
`diagram` - the diagram
Returns:
icon
getIconByDiagramType
@CheckForNullpublic static [ResizableIcon](../../ui/ResizableIcon.html) getIconByDiagramType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)
Returns icon by diagram type
Parameters:
`diagramType` - the diagram.
Returns:
icon
getSVGIconByDiagramType
@CheckForNullpublic static [ResizableIcon](../../ui/ResizableIcon.html) getSVGIconByDiagramType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)
Returns SVG icon by diagram type
Parameters:
`diagramType` - the diagram.
Returns:
icon

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class ElementIcon">Class ElementIcon</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../icons/ElementIconsRegistry.html" title="class in com.nomagic.magicdraw.icons">com.nomagic.magicdraw.icons.ElementIconsRegistry</a>
<div class="inheritance">com.nomagic.magicdraw.uml.ElementIcon</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementIcon</span>
<span class="extends-implements">extends <a href="../icons/ElementIconsRegistry.html" title="class in com.nomagic.magicdraw.icons">ElementIconsRegistry</a></span></div>
<div class="block">Utility class for providing icons for Elements.
 Icon can be provided for BaseElement object, class type of Element, diagram type.
 See <a href="ClassTypes.html" title="class in com.nomagic.magicdraw.uml"><code>ClassTypes</code></a> for useful utility methods to work with class types.
 Use <a href="BaseElement.html#getClassType()"><code>BaseElement.getClassType()</code></a> to retrieve class type of the Element.</div>
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
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SYMBOL_ADORNMENT">SYMBOL_ADORNMENT</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.icons.ElementIconsRegistry">Fields inherited from class com.nomagic.magicdraw.icons.<a href="../icons/ElementIconsRegistry.html" title="class in com.nomagic.magicdraw.icons">ElementIconsRegistry</a></h3>
<code><a href="../icons/ElementIconsRegistry.html#ABSTRACT_CLASS">ABSTRACT_CLASS</a>, <a href="../icons/ElementIconsRegistry.html#ACCEPT_TIME_EVENT_ACTION">ACCEPT_TIME_EVENT_ACTION</a>, <a href="../icons/ElementIconsRegistry.html#AGGREGATION">AGGREGATION</a>, <a href="../icons/ElementIconsRegistry.html#ARTIFACT_DEPLOYMENT_INSTANCE">ARTIFACT_DEPLOYMENT_INSTANCE</a>, <a href="../icons/ElementIconsRegistry.html#ARTIFACT_INSTANCE">ARTIFACT_INSTANCE</a>, <a href="../icons/ElementIconsRegistry.html#ASSEMBLY_CONNECTOR">ASSEMBLY_CONNECTOR</a>, <a href="../icons/ElementIconsRegistry.html#CALL_MESSAGE">CALL_MESSAGE</a>, <a href="../icons/ElementIconsRegistry.html#CHOICE_PSEUDO_STATE">CHOICE_PSEUDO_STATE</a>, <a href="../icons/ElementIconsRegistry.html#COMPONENT_INSTANCE">COMPONENT_INSTANCE</a>, <a href="../icons/ElementIconsRegistry.html#COMPOSITE_STATE">COMPOSITE_STATE</a>, <a href="../icons/ElementIconsRegistry.html#COMPOSITION">COMPOSITION</a>, <a href="../icons/ElementIconsRegistry.html#CONCURRENT_STATE">CONCURRENT_STATE</a>, <a href="../icons/ElementIconsRegistry.html#CREATE_MESSAGE">CREATE_MESSAGE</a>, <a href="../icons/ElementIconsRegistry.html#DEEP_HISTORY_PSEUDO_STATE">DEEP_HISTORY_PSEUDO_STATE</a>, <a href="../icons/ElementIconsRegistry.html#DELEGATION_CONNECTOR">DELEGATION_CONNECTOR</a>, <a href="../icons/ElementIconsRegistry.html#DESTROY_MESSAGE">DESTROY_MESSAGE</a>, <a href="../icons/ElementIconsRegistry.html#DEVICE_INSTANCE">DEVICE_INSTANCE</a>, <a href="../icons/ElementIconsRegistry.html#DIRECTED_AGGREGATION">DIRECTED_AGGREGATION</a>, <a href="../icons/ElementIconsRegistry.html#DIRECTED_ASSOCIATION">DIRECTED_ASSOCIATION</a>, <a href="../icons/ElementIconsRegistry.html#DIRECTED_COMPOSITION">DIRECTED_COMPOSITION</a>, <a href="../icons/ElementIconsRegistry.html#DOCUMENTATION">DOCUMENTATION</a>, <a href="../icons/ElementIconsRegistry.html#ENTRY_POINT_PSEUDO_STATE">ENTRY_POINT_PSEUDO_STATE</a>, <a href="../icons/ElementIconsRegistry.html#EXECUTION_ENVIRONMENT_INSTANCE">EXECUTION_ENVIRONMENT_INSTANCE</a>, <a href="../icons/ElementIconsRegistry.html#EXIT_POINT_PSEUDO_STATE">EXIT_POINT_PSEUDO_STATE</a>, <a href="../icons/ElementIconsRegistry.html#FORK_PSEUDO_STATE">FORK_PSEUDO_STATE</a>, <a href="../icons/ElementIconsRegistry.html#INITIAL_PSEUDO_STATE">INITIAL_PSEUDO_STATE</a>, <a href="../icons/ElementIconsRegistry.html#JOIN_PSEUDO_STATE">JOIN_PSEUDO_STATE</a>, <a href="../icons/ElementIconsRegistry.html#JUNCTION_PSEUDO_STATE">JUNCTION_PSEUDO_STATE</a>, <a href="../icons/ElementIconsRegistry.html#LINK">LINK</a>, <a href="../icons/ElementIconsRegistry.html#METACLASS">METACLASS</a>, <a href="../icons/ElementIconsRegistry.html#MODEL_MODEL_LIBRARY">MODEL_MODEL_LIBRARY</a>, <a href="../icons/ElementIconsRegistry.html#NARY_ASSOCIATION">NARY_ASSOCIATION</a>, <a href="../icons/ElementIconsRegistry.html#NODE_INSTANCE">NODE_INSTANCE</a>, <a href="../icons/ElementIconsRegistry.html#NON_NAVIGABLE_ASSOCIATION">NON_NAVIGABLE_ASSOCIATION</a>, <a href="../icons/ElementIconsRegistry.html#NONE_ICON">NONE_ICON</a>, <a href="../icons/ElementIconsRegistry.html#PACKAGE_MODEL_LIBRARY">PACKAGE_MODEL_LIBRARY</a>, <a href="../icons/ElementIconsRegistry.html#PROFILE_MODEL_LIBRARY">PROFILE_MODEL_LIBRARY</a>, <a href="../icons/ElementIconsRegistry.html#REPLY_MESSAGE">REPLY_MESSAGE</a>, <a href="../icons/ElementIconsRegistry.html#SEND_MESSAGE">SEND_MESSAGE</a>, <a href="../icons/ElementIconsRegistry.html#SHALLOW_HISTORY_PSEUDO_STATE">SHALLOW_HISTORY_PSEUDO_STATE</a>, <a href="../icons/ElementIconsRegistry.html#SUBMACHINE_STATE">SUBMACHINE_STATE</a>, <a href="../icons/ElementIconsRegistry.html#SUBSYSTEM">SUBSYSTEM</a>, <a href="../icons/ElementIconsRegistry.html#SUBSYSTEM_INSTANCE">SUBSYSTEM_INSTANCE</a>, <a href="../icons/ElementIconsRegistry.html#TERMINATE_PSEUDO_STATE">TERMINATE_PSEUDO_STATE</a>, <a href="../icons/ElementIconsRegistry.html#USECASE_INSTANCE">USECASE_INSTANCE</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ElementIcon</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#get16x16Icon(com.nomagic.ui.ResizableIcon)">get16x16Icon</a><wbr/>(<a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return scaled down to 16x16 icon for a given icon</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(com.nomagic.magicdraw.uml.BaseElement)">getIcon</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns icon for a given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(com.nomagic.magicdraw.uml.BaseElement,boolean)">getIcon</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean hideCustomPathStyle)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns icon for a given element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconByClassType(java.lang.Class)">getIconByClassType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns icon by class type of the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconByClassType(java.lang.Class,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getIconByClassType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns icon by class type and stereotype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconByClassType(java.lang.Class,java.util.Collection)">getIconByClassType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns icon, according class type and stereotypes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconByDiagramType(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">getIconByDiagramType</a><wbr/>(<a href="symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns icon by diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconByDiagramType(java.lang.String)">getIconByDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns icon by diagram type</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconByStereotype(java.util.function.Supplier,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getIconByStereotype</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>&gt; iconSupplier,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns icon from stereotype or from iconSupplier if stereotype has no icon</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconByType(com.nomagic.magicdraw.uml.BaseElement)">getIconByType</a><wbr/>(<a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns image, according element meta type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSVGIconByDiagramType(java.lang.String)">getSVGIconByDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns SVG icon by diagram type</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.icons.ElementIconsRegistry">Methods inherited from class com.nomagic.magicdraw.icons.<a href="../icons/ElementIconsRegistry.html" title="class in com.nomagic.magicdraw.icons">ElementIconsRegistry</a></h3>
<code><a href="../icons/ElementIconsRegistry.html#getIcon(java.lang.Class)">getIcon</a>, <a href="../icons/ElementIconsRegistry.html#internalGetIconByTypeMap()">internalGetIconByTypeMap</a>, <a href="../icons/ElementIconsRegistry.html#loadDoubleSizeIcon(java.lang.Class,java.lang.String)">loadDoubleSizeIcon</a>, <a href="../icons/ElementIconsRegistry.html#putIcon(java.lang.Class,com.nomagic.ui.ResizableIcon)">putIcon</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="SYMBOL_ADORNMENT">
<h3>SYMBOL_ADORNMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">SYMBOL_ADORNMENT</span></div>
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
<h3>ElementIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementIcon</span>()</div>
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
<section class="detail" id="get16x16Icon(com.nomagic.ui.ResizableIcon)">
<h3>get16x16Icon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">get16x16Icon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</span></div>
<div class="block">Return scaled down to 16x16 icon for a given icon</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon</dd>
<dt>Returns:</dt>
<dd>scaled icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns icon for a given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the Element</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon(com.nomagic.magicdraw.uml.BaseElement,boolean)">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 boolean hideCustomPathStyle)</span></div>
<div class="block">Returns icon for a given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the Element</dd>
<dd><code>hideCustomPathStyle</code> - if true custom path style icon is skipped and standard relationship icons is returned</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconByClassType(java.lang.Class,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getIconByClassType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIconByClassType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns icon by class type and stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classType</code> - class type</dd>
<dd><code>stereotype</code> - given stereotype</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconByStereotype(java.util.function.Supplier,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getIconByStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIconByStereotype</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>&gt; iconSupplier,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns icon from stereotype or from iconSupplier if stereotype has no icon</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>iconSupplier</code> - icon supplier</dd>
<dd><code>stereotype</code> - given stereotype</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconByClassType(java.lang.Class,java.util.Collection)">
<h3>getIconByClassType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIconByClassType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes)</span></div>
<div class="block">Returns icon, according class type and stereotypes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classType</code> - class type</dd>
<dd><code>stereotypes</code> - stereotypes</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconByClassType(java.lang.Class)">
<h3>getIconByClassType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIconByClassType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType)</span></div>
<div class="block">Returns icon by class type of the element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classType</code> - class type</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconByType(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getIconByType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIconByType</span><wbr/><span class="parameters">(@CheckForNull
 <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns image, according element meta type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconByDiagramType(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>getIconByDiagramType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIconByDiagramType</span><wbr/><span class="parameters">(<a href="symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</span></div>
<div class="block">Returns icon by diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the diagram</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconByDiagramType(java.lang.String)">
<h3>getIconByDiagramType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIconByDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">Returns icon by diagram type</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - the diagram.</dd>
<dt>Returns:</dt>
<dd>icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSVGIconByDiagramType(java.lang.String)">
<h3>getSVGIconByDiagramType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getSVGIconByDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">Returns SVG icon by diagram type</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - the diagram.</dd>
<dt>Returns:</dt>
<dd>icon</dd>
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
