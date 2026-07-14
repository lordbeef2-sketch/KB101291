# JAVA OPENAPI: DisplayRelatedSymbolsInfo (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml/symbols/DisplayRelatedSymbolsInfo.html
- source_path: `com/nomagic/magicdraw/uml/symbols/DisplayRelatedSymbolsInfo.html`
- source_sha256: `e784aa7ca68751062dd3de74df1532d387cbb9b04c7170716085c909a54c8c9f`
- captured_utc: `2026-07-14T16:58:30.414209+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class DisplayRelatedSymbolsInfo

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo

@OpenApiAllpublic classDisplayRelatedSymbolsInfo
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Controls behavior of display related symbols functionality.

See Also:
[`DisplayRelatedSymbols`](DisplayRelatedSymbols.html)
[`LinkType`](LinkType.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[DEFAULT_DEPTH_LIMIT](#DEFAULT_DEPTH_LIMIT)`
Default related element search depth limit.
`static final boolean`
`[DEFAULT_IS_DEPTH_LIMITED](#DEFAULT_IS_DEPTH_LIMITED)`
Default is depth limited value.
`static final boolean`
`[DEFAULT_IS_PACKAGE_SCOPE](#DEFAULT_IS_PACKAGE_SCOPE)`
Default is package scope flag value.
`static final int`
`[DEFAULT_RELATION_TYPE](#DEFAULT_RELATION_TYPE)`
Default display relation type.
`static final int`
`[RELATION_TYPE_BOTH](#RELATION_TYPE_BOTH)`
Displays both clients and suppliers.
`static final int`
`[RELATION_TYPE_CLIENT](#RELATION_TYPE_CLIENT)`
Displays only clients.
`static final int`
`[RELATION_TYPE_SUPPLIER](#RELATION_TYPE_SUPPLIER)`
Displays only suppliers.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DisplayRelatedSymbolsInfo](#%3Cinit%3E(java.util.Set))([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[LinkType](LinkType.html)> linkTypes)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`int`
`[getDepthLimit](#getDepthLimit())()`
Gets depth limit value.
`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[LinkType](LinkType.html)>`
`[getLinkTypes](#getLinkTypes())()`
Gets link types for display related elements functionality.
`int`
`[getRelationType](#getRelationType())()`
Gets relation type flag value.
`boolean`
`[isCreateAnnotatedElements](#isCreateAnnotatedElements())()`
Gets is create annotated elements flag value.
`boolean`
`[isCreateClients](#isCreateClients())()`
Indicates if relationship clients should be created.
`static boolean`
`[isCreateClients](#isCreateClients(int))(int relationType)`
Indicates if relationship clients should be created.
`boolean`
`[isCreateComments](#isCreateComments())()`
Gets is create comments flag value.
`boolean`
`[isCreateContainment](#isCreateContainment())()`
Gets is create containment flag value.
`boolean`
`[isCreateNewSymbols](#isCreateNewSymbols())()`
Gets is create new symbols flag value.
`boolean`
`[isCreateSuppliers](#isCreateSuppliers())()`
Indicates if relationship suppliers should be created.
`static boolean`
`[isCreateSuppliers](#isCreateSuppliers(int))(int relationType)`
Indicates if relationship suppliers should be created.
`boolean`
`[isDepthLimited](#isDepthLimited())()`
Gets is depth limited flag value.
`boolean`
`[isPackageScope](#isPackageScope())()`
Gets is in package scope flag value.
`void`
`[setCreateAnnotatedElements](#setCreateAnnotatedElements(boolean))(boolean isCreateAnnotatedElements)`
Sets is create annotated elements flag value.
`void`
`[setCreateComments](#setCreateComments(boolean))(boolean isCreateComments)`
Sets is create comments flag value.
`void`
`[setCreateContainment](#setCreateContainment(boolean))(boolean isCreateContainment)`
Sets is create containment flag value.
`void`
`[setCreateNewSymbols](#setCreateNewSymbols(boolean))(boolean createNewSymbols)`
Sets create new symbols flag value.
`void`
`[setDepthLimit](#setDepthLimit(int))(int depthLimit)`
Sets depth limit value.
`void`
`[setDepthLimited](#setDepthLimited(boolean))(boolean isDepthLimited)`
Sets is depth limited flag value.
`void`
`[setLinkTypes](#setLinkTypes(java.util.Set))([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[LinkType](LinkType.html)> linkTypes)`
Sets link types for display related elements functionality.
`void`
`[setPackageScope](#setPackageScope(boolean))(boolean isPackageScope)`
Sets is in package scope flag value.
`void`
`[setRelationType](#setRelationType(int))(int relationType)`
Sets relation type flag value.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
RELATION_TYPE_BOTH
public static final int RELATION_TYPE_BOTH
Displays both clients and suppliers.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.RELATION_TYPE_BOTH)
RELATION_TYPE_CLIENT
public static final int RELATION_TYPE_CLIENT
Displays only clients.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.RELATION_TYPE_CLIENT)
RELATION_TYPE_SUPPLIER
public static final int RELATION_TYPE_SUPPLIER
Displays only suppliers.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.RELATION_TYPE_SUPPLIER)
DEFAULT_RELATION_TYPE
public static final int DEFAULT_RELATION_TYPE
Default display relation type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.DEFAULT_RELATION_TYPE)
DEFAULT_IS_PACKAGE_SCOPE
public static final boolean DEFAULT_IS_PACKAGE_SCOPE
Default is package scope flag value.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.DEFAULT_IS_PACKAGE_SCOPE)
DEFAULT_IS_DEPTH_LIMITED
public static final boolean DEFAULT_IS_DEPTH_LIMITED
Default is depth limited value.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.DEFAULT_IS_DEPTH_LIMITED)
DEFAULT_DEPTH_LIMIT
public static final int DEFAULT_DEPTH_LIMIT
Default related element search depth limit.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.DEFAULT_DEPTH_LIMIT)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DisplayRelatedSymbolsInfo
public DisplayRelatedSymbolsInfo([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[LinkType](LinkType.html)> linkTypes)
 ============ METHOD DETAIL ========== 
Method Details
isCreateClients
public static boolean isCreateClients(int relationType)
Indicates if relationship clients should be created.
Parameters:
`relationType` - value of relation type flag.
Returns:
true if relationship clients should be created, false otherwise.
isCreateClients
public boolean isCreateClients()
Indicates if relationship clients should be created.
Returns:
true if relationship clients should be created, false otherwise.
isCreateSuppliers
public static boolean isCreateSuppliers(int relationType)
Indicates if relationship suppliers should be created.
Parameters:
`relationType` - value of relation type flag.
Returns:
true if relationship suppliers should be created, false otherwise.
isCreateSuppliers
public boolean isCreateSuppliers()
Indicates if relationship suppliers should be created.
Returns:
true if relationship suppliers should be created, false otherwise.
getRelationType
public int getRelationType()
Gets relation type flag value.
Returns:
relation type flag value.
setRelationType
public void setRelationType(int relationType)
Sets relation type flag value.
Parameters:
`relationType` - relation type flag value.
getLinkTypes
public [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[LinkType](LinkType.html)> getLinkTypes()
Gets link types for display related elements functionality.
Returns:
link types.
setLinkTypes
public void setLinkTypes([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[LinkType](LinkType.html)> linkTypes)
Sets link types for display related elements functionality.
Parameters:
`linkTypes` - link types to set.
isPackageScope
public boolean isPackageScope()
Gets is in package scope flag value.
Returns:
is in package scope flag value.
setPackageScope
public void setPackageScope(boolean isPackageScope)
Sets is in package scope flag value.
Parameters:
`isPackageScope` - is in package scope flag value.
isDepthLimited
public boolean isDepthLimited()
Gets is depth limited flag value.
Returns:
is depth limited flag value.
setDepthLimited
public void setDepthLimited(boolean isDepthLimited)
Sets is depth limited flag value.
Parameters:
`isDepthLimited` - is depth limited flag value.
getDepthLimit
public int getDepthLimit()
Gets depth limit value.
Returns:
depth limit value.
setDepthLimit
public void setDepthLimit(int depthLimit)
Sets depth limit value.
Parameters:
`depthLimit` - depth limit value.
isCreateContainment
public boolean isCreateContainment()
Gets is create containment flag value.
Returns:
create containment flag value.
setCreateContainment
public void setCreateContainment(boolean isCreateContainment)
Sets is create containment flag value.
Parameters:
`isCreateContainment` - is create containment flag value.
isCreateComments
public boolean isCreateComments()
Gets is create comments flag value.
Returns:
is create comments flag value.
setCreateComments
public void setCreateComments(boolean isCreateComments)
Sets is create comments flag value.
Parameters:
`isCreateComments` - is create comments flag value.
isCreateAnnotatedElements
public boolean isCreateAnnotatedElements()
Gets is create annotated elements flag value.
Returns:
is create annotated elements flag value.
setCreateAnnotatedElements
public void setCreateAnnotatedElements(boolean isCreateAnnotatedElements)
Sets is create annotated elements flag value.
Parameters:
`isCreateAnnotatedElements` - is create annotated elements flag value.
isCreateNewSymbols
public boolean isCreateNewSymbols()
Gets is create new symbols flag value.
Returns:
is create new symbols flag value.
setCreateNewSymbols
public void setCreateNewSymbols(boolean createNewSymbols)
Sets create new symbols flag value.
Parameters:
`createNewSymbols` - create new symbols flag value.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class DisplayRelatedSymbolsInfo">Class DisplayRelatedSymbolsInfo</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DisplayRelatedSymbolsInfo</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Controls behavior of display related symbols functionality.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="DisplayRelatedSymbols.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>DisplayRelatedSymbols</code></a></li>
<li><a href="LinkType.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>LinkType</code></a></li>
</ul>
</dd>
</dl>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_DEPTH_LIMIT">DEFAULT_DEPTH_LIMIT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default related element search depth limit.</div>
</div>
<div class="col-first odd-row-color"><code>static final boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEFAULT_IS_DEPTH_LIMITED">DEFAULT_IS_DEPTH_LIMITED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Default is depth limited value.</div>
</div>
<div class="col-first even-row-color"><code>static final boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_IS_PACKAGE_SCOPE">DEFAULT_IS_PACKAGE_SCOPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default is package scope flag value.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEFAULT_RELATION_TYPE">DEFAULT_RELATION_TYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Default display relation type.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RELATION_TYPE_BOTH">RELATION_TYPE_BOTH</a></code></div>
<div class="col-last even-row-color">
<div class="block">Displays both clients and suppliers.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RELATION_TYPE_CLIENT">RELATION_TYPE_CLIENT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Displays only clients.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RELATION_TYPE_SUPPLIER">RELATION_TYPE_SUPPLIER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Displays only suppliers.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Set)">DisplayRelatedSymbolsInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="LinkType.html" title="class in com.nomagic.magicdraw.uml.symbols">LinkType</a>&gt; linkTypes)</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDepthLimit()">getDepthLimit</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets depth limit value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a href="LinkType.html" title="class in com.nomagic.magicdraw.uml.symbols">LinkType</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLinkTypes()">getLinkTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets link types for display related elements functionality.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationType()">getRelationType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets relation type flag value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateAnnotatedElements()">isCreateAnnotatedElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets is create annotated elements flag value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateClients()">isCreateClients</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if relationship clients should be created.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateClients(int)">isCreateClients</a><wbr/>(int relationType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if relationship clients should be created.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateComments()">isCreateComments</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets is create comments flag value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateContainment()">isCreateContainment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets is create containment flag value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateNewSymbols()">isCreateNewSymbols</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets is create new symbols flag value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateSuppliers()">isCreateSuppliers</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if relationship suppliers should be created.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreateSuppliers(int)">isCreateSuppliers</a><wbr/>(int relationType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if relationship suppliers should be created.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDepthLimited()">isDepthLimited</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets is depth limited flag value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isPackageScope()">isPackageScope</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets is in package scope flag value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreateAnnotatedElements(boolean)">setCreateAnnotatedElements</a><wbr/>(boolean isCreateAnnotatedElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets is create annotated elements flag value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreateComments(boolean)">setCreateComments</a><wbr/>(boolean isCreateComments)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets is create comments flag value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreateContainment(boolean)">setCreateContainment</a><wbr/>(boolean isCreateContainment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets is create containment flag value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreateNewSymbols(boolean)">setCreateNewSymbols</a><wbr/>(boolean createNewSymbols)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets create new symbols flag value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDepthLimit(int)">setDepthLimit</a><wbr/>(int depthLimit)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets depth limit value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDepthLimited(boolean)">setDepthLimited</a><wbr/>(boolean isDepthLimited)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets is depth limited flag value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLinkTypes(java.util.Set)">setLinkTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="LinkType.html" title="class in com.nomagic.magicdraw.uml.symbols">LinkType</a>&gt; linkTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets link types for display related elements functionality.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPackageScope(boolean)">setPackageScope</a><wbr/>(boolean isPackageScope)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets is in package scope flag value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRelationType(int)">setRelationType</a><wbr/>(int relationType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets relation type flag value.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="RELATION_TYPE_BOTH">
<h3>RELATION_TYPE_BOTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">RELATION_TYPE_BOTH</span></div>
<div class="block">Displays both clients and suppliers.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.RELATION_TYPE_BOTH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RELATION_TYPE_CLIENT">
<h3>RELATION_TYPE_CLIENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">RELATION_TYPE_CLIENT</span></div>
<div class="block">Displays only clients.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.RELATION_TYPE_CLIENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RELATION_TYPE_SUPPLIER">
<h3>RELATION_TYPE_SUPPLIER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">RELATION_TYPE_SUPPLIER</span></div>
<div class="block">Displays only suppliers.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.RELATION_TYPE_SUPPLIER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_RELATION_TYPE">
<h3>DEFAULT_RELATION_TYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DEFAULT_RELATION_TYPE</span></div>
<div class="block">Default display relation type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.DEFAULT_RELATION_TYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_IS_PACKAGE_SCOPE">
<h3>DEFAULT_IS_PACKAGE_SCOPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">boolean</span> <span class="element-name">DEFAULT_IS_PACKAGE_SCOPE</span></div>
<div class="block">Default is package scope flag value.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.DEFAULT_IS_PACKAGE_SCOPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_IS_DEPTH_LIMITED">
<h3>DEFAULT_IS_DEPTH_LIMITED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">boolean</span> <span class="element-name">DEFAULT_IS_DEPTH_LIMITED</span></div>
<div class="block">Default is depth limited value.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.DEFAULT_IS_DEPTH_LIMITED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_DEPTH_LIMIT">
<h3>DEFAULT_DEPTH_LIMIT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DEFAULT_DEPTH_LIMIT</span></div>
<div class="block">Default related element search depth limit.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.DisplayRelatedSymbolsInfo.DEFAULT_DEPTH_LIMIT">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(java.util.Set)">
<h3>DisplayRelatedSymbolsInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DisplayRelatedSymbolsInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="LinkType.html" title="class in com.nomagic.magicdraw.uml.symbols">LinkType</a>&gt; linkTypes)</span></div>
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
<section class="detail" id="isCreateClients(int)">
<h3>isCreateClients</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCreateClients</span><wbr/><span class="parameters">(int relationType)</span></div>
<div class="block">Indicates if relationship clients should be created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationType</code> - value of relation type flag.</dd>
<dt>Returns:</dt>
<dd>true if relationship clients should be created, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreateClients()">
<h3>isCreateClients</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCreateClients</span>()</div>
<div class="block">Indicates if relationship clients should be created.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if relationship clients should be created, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreateSuppliers(int)">
<h3>isCreateSuppliers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCreateSuppliers</span><wbr/><span class="parameters">(int relationType)</span></div>
<div class="block">Indicates if relationship suppliers should be created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationType</code> - value of relation type flag.</dd>
<dt>Returns:</dt>
<dd>true if relationship suppliers should be created, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreateSuppliers()">
<h3>isCreateSuppliers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCreateSuppliers</span>()</div>
<div class="block">Indicates if relationship suppliers should be created.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if relationship suppliers should be created, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelationType()">
<h3>getRelationType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getRelationType</span>()</div>
<div class="block">Gets relation type flag value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>relation type flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRelationType(int)">
<h3>setRelationType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRelationType</span><wbr/><span class="parameters">(int relationType)</span></div>
<div class="block">Sets relation type flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationType</code> - relation type flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLinkTypes()">
<h3>getLinkTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="LinkType.html" title="class in com.nomagic.magicdraw.uml.symbols">LinkType</a>&gt;</span> <span class="element-name">getLinkTypes</span>()</div>
<div class="block">Gets link types for display related elements functionality.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>link types.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLinkTypes(java.util.Set)">
<h3>setLinkTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLinkTypes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="LinkType.html" title="class in com.nomagic.magicdraw.uml.symbols">LinkType</a>&gt; linkTypes)</span></div>
<div class="block">Sets link types for display related elements functionality.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>linkTypes</code> - link types to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPackageScope()">
<h3>isPackageScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPackageScope</span>()</div>
<div class="block">Gets is in package scope flag value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>is in package scope flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPackageScope(boolean)">
<h3>setPackageScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPackageScope</span><wbr/><span class="parameters">(boolean isPackageScope)</span></div>
<div class="block">Sets is in package scope flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>isPackageScope</code> - is in package scope flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDepthLimited()">
<h3>isDepthLimited</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDepthLimited</span>()</div>
<div class="block">Gets is depth limited flag value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>is depth limited flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDepthLimited(boolean)">
<h3>setDepthLimited</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDepthLimited</span><wbr/><span class="parameters">(boolean isDepthLimited)</span></div>
<div class="block">Sets is depth limited flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>isDepthLimited</code> - is depth limited flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDepthLimit()">
<h3>getDepthLimit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDepthLimit</span>()</div>
<div class="block">Gets depth limit value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>depth limit value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDepthLimit(int)">
<h3>setDepthLimit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDepthLimit</span><wbr/><span class="parameters">(int depthLimit)</span></div>
<div class="block">Sets depth limit value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>depthLimit</code> - depth limit value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreateContainment()">
<h3>isCreateContainment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCreateContainment</span>()</div>
<div class="block">Gets is create containment flag value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>create containment flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCreateContainment(boolean)">
<h3>setCreateContainment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateContainment</span><wbr/><span class="parameters">(boolean isCreateContainment)</span></div>
<div class="block">Sets is create containment flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>isCreateContainment</code> - is create containment flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreateComments()">
<h3>isCreateComments</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCreateComments</span>()</div>
<div class="block">Gets is create comments flag value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>is create comments flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCreateComments(boolean)">
<h3>setCreateComments</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateComments</span><wbr/><span class="parameters">(boolean isCreateComments)</span></div>
<div class="block">Sets is create comments flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>isCreateComments</code> - is create comments flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreateAnnotatedElements()">
<h3>isCreateAnnotatedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCreateAnnotatedElements</span>()</div>
<div class="block">Gets is create annotated elements flag value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>is create annotated elements flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCreateAnnotatedElements(boolean)">
<h3>setCreateAnnotatedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateAnnotatedElements</span><wbr/><span class="parameters">(boolean isCreateAnnotatedElements)</span></div>
<div class="block">Sets is create annotated elements flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>isCreateAnnotatedElements</code> - is create annotated elements flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreateNewSymbols()">
<h3>isCreateNewSymbols</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCreateNewSymbols</span>()</div>
<div class="block">Gets is create new symbols flag value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>is create new symbols flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCreateNewSymbols(boolean)">
<h3>setCreateNewSymbols</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateNewSymbols</span><wbr/><span class="parameters">(boolean createNewSymbols)</span></div>
<div class="block">Sets create new symbols flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>createNewSymbols</code> - create new symbols flag value.</dd>
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
