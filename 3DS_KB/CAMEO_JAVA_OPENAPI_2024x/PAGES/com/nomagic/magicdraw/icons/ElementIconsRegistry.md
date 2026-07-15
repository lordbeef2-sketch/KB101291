# JAVA OPENAPI: ElementIconsRegistry (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/icons/ElementIconsRegistry.html
- source_path: `com/nomagic/magicdraw/icons/ElementIconsRegistry.html`
- source_sha256: `ba3bca58cff852e4526eeed48f7c2229a2d6d71bcd2a17153cb8c76aa246d61d`
- captured_utc: `2026-07-14T16:51:23.286230+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.icons](package-summary.html)

## Class ElementIconsRegistry

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.icons.ElementIconsRegistry

Direct Known Subclasses:
`[ElementIcon](../uml/ElementIcon.html)`

@OpenApiAllpublic classElementIconsRegistry
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Utility class for registering icons for Elements by class type and defining some constants.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[ABSTRACT_CLASS](#ABSTRACT_CLASS)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[ACCEPT_TIME_EVENT_ACTION](#ACCEPT_TIME_EVENT_ACTION)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[AGGREGATION](#AGGREGATION)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[ARTIFACT_DEPLOYMENT_INSTANCE](#ARTIFACT_DEPLOYMENT_INSTANCE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[ARTIFACT_INSTANCE](#ARTIFACT_INSTANCE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[ASSEMBLY_CONNECTOR](#ASSEMBLY_CONNECTOR)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[CALL_MESSAGE](#CALL_MESSAGE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[CHOICE_PSEUDO_STATE](#CHOICE_PSEUDO_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[COMPONENT_INSTANCE](#COMPONENT_INSTANCE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[COMPOSITE_STATE](#COMPOSITE_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[COMPOSITION](#COMPOSITION)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[CONCURRENT_STATE](#CONCURRENT_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[CREATE_MESSAGE](#CREATE_MESSAGE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[DEEP_HISTORY_PSEUDO_STATE](#DEEP_HISTORY_PSEUDO_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[DELEGATION_CONNECTOR](#DELEGATION_CONNECTOR)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[DESTROY_MESSAGE](#DESTROY_MESSAGE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[DEVICE_INSTANCE](#DEVICE_INSTANCE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[DIRECTED_AGGREGATION](#DIRECTED_AGGREGATION)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[DIRECTED_ASSOCIATION](#DIRECTED_ASSOCIATION)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[DIRECTED_COMPOSITION](#DIRECTED_COMPOSITION)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[DOCUMENTATION](#DOCUMENTATION)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[ENTRY_POINT_PSEUDO_STATE](#ENTRY_POINT_PSEUDO_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[EXECUTION_ENVIRONMENT_INSTANCE](#EXECUTION_ENVIRONMENT_INSTANCE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[EXIT_POINT_PSEUDO_STATE](#EXIT_POINT_PSEUDO_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[FORK_PSEUDO_STATE](#FORK_PSEUDO_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[INITIAL_PSEUDO_STATE](#INITIAL_PSEUDO_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[JOIN_PSEUDO_STATE](#JOIN_PSEUDO_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[JUNCTION_PSEUDO_STATE](#JUNCTION_PSEUDO_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[LINK](#LINK)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[METACLASS](#METACLASS)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[MODEL_MODEL_LIBRARY](#MODEL_MODEL_LIBRARY)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[NARY_ASSOCIATION](#NARY_ASSOCIATION)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[NODE_INSTANCE](#NODE_INSTANCE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[NON_NAVIGABLE_ASSOCIATION](#NON_NAVIGABLE_ASSOCIATION)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[NONE_ICON](#NONE_ICON)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[PACKAGE_MODEL_LIBRARY](#PACKAGE_MODEL_LIBRARY)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[PROFILE_MODEL_LIBRARY](#PROFILE_MODEL_LIBRARY)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[REPLY_MESSAGE](#REPLY_MESSAGE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[SEND_MESSAGE](#SEND_MESSAGE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[SHALLOW_HISTORY_PSEUDO_STATE](#SHALLOW_HISTORY_PSEUDO_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[SUBMACHINE_STATE](#SUBMACHINE_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[SUBSYSTEM](#SUBSYSTEM)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[SUBSYSTEM_INSTANCE](#SUBSYSTEM_INSTANCE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[TERMINATE_PSEUDO_STATE](#TERMINATE_PSEUDO_STATE)`

`static final [ResizableIcon](../../ui/ResizableIcon.html)`
`[USECASE_INSTANCE](#USECASE_INSTANCE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ElementIconsRegistry](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`protected static [ResizableIcon](../../ui/ResizableIcon.html)`
`[getIcon](#getIcon(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType)`

`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html),[ResizableIcon](../../ui/ResizableIcon.html)>`
`[internalGetIconByTypeMap](#internalGetIconByTypeMap())()`

`protected static [ResizableIcon](../../ui/ResizableIcon.html)`
`[loadDoubleSizeIcon](#loadDoubleSizeIcon(java.lang.Class,java.lang.String))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> resourceClass,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`

`protected static void`
`[putIcon](#putIcon(java.lang.Class,com.nomagic.ui.ResizableIcon))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType,
 [ResizableIcon](../../ui/ResizableIcon.html) icon)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
NONE_ICON
public static final [ResizableIcon](../../ui/ResizableIcon.html) NONE_ICON
ABSTRACT_CLASS
public static final [ResizableIcon](../../ui/ResizableIcon.html) ABSTRACT_CLASS
METACLASS
public static final [ResizableIcon](../../ui/ResizableIcon.html) METACLASS
LINK
public static final [ResizableIcon](../../ui/ResizableIcon.html) LINK
USECASE_INSTANCE
public static final [ResizableIcon](../../ui/ResizableIcon.html) USECASE_INSTANCE
SUBSYSTEM_INSTANCE
public static final [ResizableIcon](../../ui/ResizableIcon.html) SUBSYSTEM_INSTANCE
COMPONENT_INSTANCE
public static final [ResizableIcon](../../ui/ResizableIcon.html) COMPONENT_INSTANCE
NODE_INSTANCE
public static final [ResizableIcon](../../ui/ResizableIcon.html) NODE_INSTANCE
ARTIFACT_INSTANCE
public static final [ResizableIcon](../../ui/ResizableIcon.html) ARTIFACT_INSTANCE
DEVICE_INSTANCE
public static final [ResizableIcon](../../ui/ResizableIcon.html) DEVICE_INSTANCE
EXECUTION_ENVIRONMENT_INSTANCE
public static final [ResizableIcon](../../ui/ResizableIcon.html) EXECUTION_ENVIRONMENT_INSTANCE
ARTIFACT_DEPLOYMENT_INSTANCE
public static final [ResizableIcon](../../ui/ResizableIcon.html) ARTIFACT_DEPLOYMENT_INSTANCE
CALL_MESSAGE
public static final [ResizableIcon](../../ui/ResizableIcon.html) CALL_MESSAGE
CREATE_MESSAGE
public static final [ResizableIcon](../../ui/ResizableIcon.html) CREATE_MESSAGE
DESTROY_MESSAGE
public static final [ResizableIcon](../../ui/ResizableIcon.html) DESTROY_MESSAGE
SEND_MESSAGE
public static final [ResizableIcon](../../ui/ResizableIcon.html) SEND_MESSAGE
REPLY_MESSAGE
public static final [ResizableIcon](../../ui/ResizableIcon.html) REPLY_MESSAGE
ASSEMBLY_CONNECTOR
public static final [ResizableIcon](../../ui/ResizableIcon.html) ASSEMBLY_CONNECTOR
DELEGATION_CONNECTOR
public static final [ResizableIcon](../../ui/ResizableIcon.html) DELEGATION_CONNECTOR
PROFILE_MODEL_LIBRARY
public static final [ResizableIcon](../../ui/ResizableIcon.html) PROFILE_MODEL_LIBRARY
MODEL_MODEL_LIBRARY
public static final [ResizableIcon](../../ui/ResizableIcon.html) MODEL_MODEL_LIBRARY
PACKAGE_MODEL_LIBRARY
public static final [ResizableIcon](../../ui/ResizableIcon.html) PACKAGE_MODEL_LIBRARY
DIRECTED_ASSOCIATION
public static final [ResizableIcon](../../ui/ResizableIcon.html) DIRECTED_ASSOCIATION
DIRECTED_AGGREGATION
public static final [ResizableIcon](../../ui/ResizableIcon.html) DIRECTED_AGGREGATION
AGGREGATION
public static final [ResizableIcon](../../ui/ResizableIcon.html) AGGREGATION
COMPOSITION
public static final [ResizableIcon](../../ui/ResizableIcon.html) COMPOSITION
DIRECTED_COMPOSITION
public static final [ResizableIcon](../../ui/ResizableIcon.html) DIRECTED_COMPOSITION
NON_NAVIGABLE_ASSOCIATION
public static final [ResizableIcon](../../ui/ResizableIcon.html) NON_NAVIGABLE_ASSOCIATION
ACCEPT_TIME_EVENT_ACTION
public static final [ResizableIcon](../../ui/ResizableIcon.html) ACCEPT_TIME_EVENT_ACTION
SUBSYSTEM
public static final [ResizableIcon](../../ui/ResizableIcon.html) SUBSYSTEM
COMPOSITE_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) COMPOSITE_STATE
SUBMACHINE_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) SUBMACHINE_STATE
CONCURRENT_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) CONCURRENT_STATE
INITIAL_PSEUDO_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) INITIAL_PSEUDO_STATE
DEEP_HISTORY_PSEUDO_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) DEEP_HISTORY_PSEUDO_STATE
SHALLOW_HISTORY_PSEUDO_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) SHALLOW_HISTORY_PSEUDO_STATE
JOIN_PSEUDO_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) JOIN_PSEUDO_STATE
FORK_PSEUDO_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) FORK_PSEUDO_STATE
JUNCTION_PSEUDO_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) JUNCTION_PSEUDO_STATE
CHOICE_PSEUDO_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) CHOICE_PSEUDO_STATE
ENTRY_POINT_PSEUDO_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) ENTRY_POINT_PSEUDO_STATE
EXIT_POINT_PSEUDO_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) EXIT_POINT_PSEUDO_STATE
TERMINATE_PSEUDO_STATE
public static final [ResizableIcon](../../ui/ResizableIcon.html) TERMINATE_PSEUDO_STATE
DOCUMENTATION
public static final [ResizableIcon](../../ui/ResizableIcon.html) DOCUMENTATION
NARY_ASSOCIATION
public static final [ResizableIcon](../../ui/ResizableIcon.html) NARY_ASSOCIATION
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ElementIconsRegistry
public ElementIconsRegistry()
 ============ METHOD DETAIL ========== 
Method Details
internalGetIconByTypeMap
public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html),[ResizableIcon](../../ui/ResizableIcon.html)> internalGetIconByTypeMap()
loadDoubleSizeIcon
protected static [ResizableIcon](../../ui/ResizableIcon.html) loadDoubleSizeIcon([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> resourceClass,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
getIcon
protected static [ResizableIcon](../../ui/ResizableIcon.html) getIcon([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType)
putIcon
protected static void putIcon([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) classType,
 [ResizableIcon](../../ui/ResizableIcon.html) icon)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.icons</a></div>
<h1 class="title" title="Class ElementIconsRegistry">Class ElementIconsRegistry</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.icons.ElementIconsRegistry</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../uml/ElementIcon.html" title="class in com.nomagic.magicdraw.uml">ElementIcon</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementIconsRegistry</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class for registering icons for Elements by class type and defining some constants.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ABSTRACT_CLASS">ABSTRACT_CLASS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ACCEPT_TIME_EVENT_ACTION">ACCEPT_TIME_EVENT_ACTION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AGGREGATION">AGGREGATION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ARTIFACT_DEPLOYMENT_INSTANCE">ARTIFACT_DEPLOYMENT_INSTANCE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ARTIFACT_INSTANCE">ARTIFACT_INSTANCE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ASSEMBLY_CONNECTOR">ASSEMBLY_CONNECTOR</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CALL_MESSAGE">CALL_MESSAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CHOICE_PSEUDO_STATE">CHOICE_PSEUDO_STATE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COMPONENT_INSTANCE">COMPONENT_INSTANCE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COMPOSITE_STATE">COMPOSITE_STATE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COMPOSITION">COMPOSITION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONCURRENT_STATE">CONCURRENT_STATE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CREATE_MESSAGE">CREATE_MESSAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEEP_HISTORY_PSEUDO_STATE">DEEP_HISTORY_PSEUDO_STATE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DELEGATION_CONNECTOR">DELEGATION_CONNECTOR</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DESTROY_MESSAGE">DESTROY_MESSAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEVICE_INSTANCE">DEVICE_INSTANCE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIRECTED_AGGREGATION">DIRECTED_AGGREGATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIRECTED_ASSOCIATION">DIRECTED_ASSOCIATION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIRECTED_COMPOSITION">DIRECTED_COMPOSITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOCUMENTATION">DOCUMENTATION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENTRY_POINT_PSEUDO_STATE">ENTRY_POINT_PSEUDO_STATE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXECUTION_ENVIRONMENT_INSTANCE">EXECUTION_ENVIRONMENT_INSTANCE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EXIT_POINT_PSEUDO_STATE">EXIT_POINT_PSEUDO_STATE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FORK_PSEUDO_STATE">FORK_PSEUDO_STATE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INITIAL_PSEUDO_STATE">INITIAL_PSEUDO_STATE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#JOIN_PSEUDO_STATE">JOIN_PSEUDO_STATE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#JUNCTION_PSEUDO_STATE">JUNCTION_PSEUDO_STATE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LINK">LINK</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#METACLASS">METACLASS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MODEL_MODEL_LIBRARY">MODEL_MODEL_LIBRARY</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NARY_ASSOCIATION">NARY_ASSOCIATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NODE_INSTANCE">NODE_INSTANCE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NON_NAVIGABLE_ASSOCIATION">NON_NAVIGABLE_ASSOCIATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NONE_ICON">NONE_ICON</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PACKAGE_MODEL_LIBRARY">PACKAGE_MODEL_LIBRARY</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROFILE_MODEL_LIBRARY">PROFILE_MODEL_LIBRARY</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REPLY_MESSAGE">REPLY_MESSAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SEND_MESSAGE">SEND_MESSAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHALLOW_HISTORY_PSEUDO_STATE">SHALLOW_HISTORY_PSEUDO_STATE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SUBMACHINE_STATE">SUBMACHINE_STATE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SUBSYSTEM">SUBSYSTEM</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SUBSYSTEM_INSTANCE">SUBSYSTEM_INSTANCE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TERMINATE_PSEUDO_STATE">TERMINATE_PSEUDO_STATE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#USECASE_INSTANCE">USECASE_INSTANCE</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ElementIconsRegistry</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon(java.lang.Class)">getIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>,<wbr/><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#internalGetIconByTypeMap()">internalGetIconByTypeMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadDoubleSizeIcon(java.lang.Class,java.lang.String)">loadDoubleSizeIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; resourceClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#putIcon(java.lang.Class,com.nomagic.ui.ResizableIcon)">putIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType,
 <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="NONE_ICON">
<h3>NONE_ICON</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">NONE_ICON</span></div>
</section>
</li>
<li>
<section class="detail" id="ABSTRACT_CLASS">
<h3>ABSTRACT_CLASS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">ABSTRACT_CLASS</span></div>
</section>
</li>
<li>
<section class="detail" id="METACLASS">
<h3>METACLASS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">METACLASS</span></div>
</section>
</li>
<li>
<section class="detail" id="LINK">
<h3>LINK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">LINK</span></div>
</section>
</li>
<li>
<section class="detail" id="USECASE_INSTANCE">
<h3>USECASE_INSTANCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">USECASE_INSTANCE</span></div>
</section>
</li>
<li>
<section class="detail" id="SUBSYSTEM_INSTANCE">
<h3>SUBSYSTEM_INSTANCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">SUBSYSTEM_INSTANCE</span></div>
</section>
</li>
<li>
<section class="detail" id="COMPONENT_INSTANCE">
<h3>COMPONENT_INSTANCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">COMPONENT_INSTANCE</span></div>
</section>
</li>
<li>
<section class="detail" id="NODE_INSTANCE">
<h3>NODE_INSTANCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">NODE_INSTANCE</span></div>
</section>
</li>
<li>
<section class="detail" id="ARTIFACT_INSTANCE">
<h3>ARTIFACT_INSTANCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">ARTIFACT_INSTANCE</span></div>
</section>
</li>
<li>
<section class="detail" id="DEVICE_INSTANCE">
<h3>DEVICE_INSTANCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">DEVICE_INSTANCE</span></div>
</section>
</li>
<li>
<section class="detail" id="EXECUTION_ENVIRONMENT_INSTANCE">
<h3>EXECUTION_ENVIRONMENT_INSTANCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">EXECUTION_ENVIRONMENT_INSTANCE</span></div>
</section>
</li>
<li>
<section class="detail" id="ARTIFACT_DEPLOYMENT_INSTANCE">
<h3>ARTIFACT_DEPLOYMENT_INSTANCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">ARTIFACT_DEPLOYMENT_INSTANCE</span></div>
</section>
</li>
<li>
<section class="detail" id="CALL_MESSAGE">
<h3>CALL_MESSAGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">CALL_MESSAGE</span></div>
</section>
</li>
<li>
<section class="detail" id="CREATE_MESSAGE">
<h3>CREATE_MESSAGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">CREATE_MESSAGE</span></div>
</section>
</li>
<li>
<section class="detail" id="DESTROY_MESSAGE">
<h3>DESTROY_MESSAGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">DESTROY_MESSAGE</span></div>
</section>
</li>
<li>
<section class="detail" id="SEND_MESSAGE">
<h3>SEND_MESSAGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">SEND_MESSAGE</span></div>
</section>
</li>
<li>
<section class="detail" id="REPLY_MESSAGE">
<h3>REPLY_MESSAGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">REPLY_MESSAGE</span></div>
</section>
</li>
<li>
<section class="detail" id="ASSEMBLY_CONNECTOR">
<h3>ASSEMBLY_CONNECTOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">ASSEMBLY_CONNECTOR</span></div>
</section>
</li>
<li>
<section class="detail" id="DELEGATION_CONNECTOR">
<h3>DELEGATION_CONNECTOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">DELEGATION_CONNECTOR</span></div>
</section>
</li>
<li>
<section class="detail" id="PROFILE_MODEL_LIBRARY">
<h3>PROFILE_MODEL_LIBRARY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">PROFILE_MODEL_LIBRARY</span></div>
</section>
</li>
<li>
<section class="detail" id="MODEL_MODEL_LIBRARY">
<h3>MODEL_MODEL_LIBRARY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">MODEL_MODEL_LIBRARY</span></div>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_MODEL_LIBRARY">
<h3>PACKAGE_MODEL_LIBRARY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">PACKAGE_MODEL_LIBRARY</span></div>
</section>
</li>
<li>
<section class="detail" id="DIRECTED_ASSOCIATION">
<h3>DIRECTED_ASSOCIATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">DIRECTED_ASSOCIATION</span></div>
</section>
</li>
<li>
<section class="detail" id="DIRECTED_AGGREGATION">
<h3>DIRECTED_AGGREGATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">DIRECTED_AGGREGATION</span></div>
</section>
</li>
<li>
<section class="detail" id="AGGREGATION">
<h3>AGGREGATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">AGGREGATION</span></div>
</section>
</li>
<li>
<section class="detail" id="COMPOSITION">
<h3>COMPOSITION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">COMPOSITION</span></div>
</section>
</li>
<li>
<section class="detail" id="DIRECTED_COMPOSITION">
<h3>DIRECTED_COMPOSITION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">DIRECTED_COMPOSITION</span></div>
</section>
</li>
<li>
<section class="detail" id="NON_NAVIGABLE_ASSOCIATION">
<h3>NON_NAVIGABLE_ASSOCIATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">NON_NAVIGABLE_ASSOCIATION</span></div>
</section>
</li>
<li>
<section class="detail" id="ACCEPT_TIME_EVENT_ACTION">
<h3>ACCEPT_TIME_EVENT_ACTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">ACCEPT_TIME_EVENT_ACTION</span></div>
</section>
</li>
<li>
<section class="detail" id="SUBSYSTEM">
<h3>SUBSYSTEM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">SUBSYSTEM</span></div>
</section>
</li>
<li>
<section class="detail" id="COMPOSITE_STATE">
<h3>COMPOSITE_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">COMPOSITE_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="SUBMACHINE_STATE">
<h3>SUBMACHINE_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">SUBMACHINE_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="CONCURRENT_STATE">
<h3>CONCURRENT_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">CONCURRENT_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="INITIAL_PSEUDO_STATE">
<h3>INITIAL_PSEUDO_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">INITIAL_PSEUDO_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="DEEP_HISTORY_PSEUDO_STATE">
<h3>DEEP_HISTORY_PSEUDO_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">DEEP_HISTORY_PSEUDO_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="SHALLOW_HISTORY_PSEUDO_STATE">
<h3>SHALLOW_HISTORY_PSEUDO_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">SHALLOW_HISTORY_PSEUDO_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="JOIN_PSEUDO_STATE">
<h3>JOIN_PSEUDO_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">JOIN_PSEUDO_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="FORK_PSEUDO_STATE">
<h3>FORK_PSEUDO_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">FORK_PSEUDO_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="JUNCTION_PSEUDO_STATE">
<h3>JUNCTION_PSEUDO_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">JUNCTION_PSEUDO_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="CHOICE_PSEUDO_STATE">
<h3>CHOICE_PSEUDO_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">CHOICE_PSEUDO_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="ENTRY_POINT_PSEUDO_STATE">
<h3>ENTRY_POINT_PSEUDO_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">ENTRY_POINT_PSEUDO_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="EXIT_POINT_PSEUDO_STATE">
<h3>EXIT_POINT_PSEUDO_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">EXIT_POINT_PSEUDO_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="TERMINATE_PSEUDO_STATE">
<h3>TERMINATE_PSEUDO_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">TERMINATE_PSEUDO_STATE</span></div>
</section>
</li>
<li>
<section class="detail" id="DOCUMENTATION">
<h3>DOCUMENTATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">DOCUMENTATION</span></div>
</section>
</li>
<li>
<section class="detail" id="NARY_ASSOCIATION">
<h3>NARY_ASSOCIATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">NARY_ASSOCIATION</span></div>
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
<h3>ElementIconsRegistry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementIconsRegistry</span>()</div>
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
<section class="detail" id="internalGetIconByTypeMap()">
<h3>internalGetIconByTypeMap</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>,<wbr/><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>&gt;</span> <span class="element-name">internalGetIconByTypeMap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="loadDoubleSizeIcon(java.lang.Class,java.lang.String)">
<h3>loadDoubleSizeIcon</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">loadDoubleSizeIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; resourceClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
</section>
</li>
<li>
<section class="detail" id="getIcon(java.lang.Class)">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type"><a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType)</span></div>
</section>
</li>
<li>
<section class="detail" id="putIcon(java.lang.Class,com.nomagic.ui.ResizableIcon)">
<h3>putIcon</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type">void</span> <span class="element-name">putIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> classType,
 <a href="../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</span></div>
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
